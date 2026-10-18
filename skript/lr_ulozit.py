"""Uloží data LR stažená mimo GitHub (LR blokuje servery GitHubu).

Vstup: textový soubor, na každém řádku  KOD|CENA|STAV|AKCE|STITEK|NAZEV|URL_KATEGORIE
       (starší tvar KOD|CENA|STAV|AKCE|URL se přijímá také)
       STAV   = ANO (skladem) / NE (karta má štítek „Není skladem“)
       AKCE   = ANO, když má karta štítek akce („Akce 17.-23.10.2026“, „Měsíční akce“) – cena je pak akční
       STITEK = přesný text štítku akce (z něj se čte platnost), jinak prázdné
       NAZEV  = název produktu na kartě
Výstup: data/lr.json  {"cas": ..., "produkty": {KOD: {"skladem", "cena", "nazev", "url", "akce"?}}}
       cena = běžná (neakční) cena, pokud ji některá kategorie ukazuje bez akce, jinak None
       akce = {"cena", "od", "do", "stitek"} – když je produkt u LR v akci
"""
import calendar
import json
import os
import re
import sys
from datetime import date, datetime, timezone, timedelta

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ted = datetime.now(timezone(timedelta(hours=2)))


def platnost(stitek, dnes):
    """Z textu štítku akce vrátí (od, do) jako date; neznámé -> do konce měsíce."""
    t = re.sub(r"\s", "", stitek or "")
    # „Akce 17.-23.10.2026“, „Akce 28.10.-03.11.2026“, „Akce 30.12.2026-05.01.2027“
    m = re.search(r"(\d{1,2})\.(?:(\d{1,2})\.)?(\d{4})?[-–](\d{1,2})\.(\d{1,2})\.(\d{4})", t)
    if m:
        d1, m1, y1, d2, m2, y2 = m.groups()
        try:
            do = date(int(y2), int(m2), int(d2))
            od = date(int(y1 or y2), int(m1 or m2), int(d1))
            if od > do:  # přelom roku bez uvedeného roku u začátku
                od = od.replace(year=od.year - 1)
            return od, do
        except ValueError:
            pass
    m = re.search(r"(?:do)?(\d{1,2})\.(\d{1,2})\.(\d{4})", t)
    if m and "do" in t.lower():
        try:
            return dnes, date(int(m.group(3)), int(m.group(2)), int(m.group(1)))
        except ValueError:
            pass
    # „Měsíční akce“ nebo nečitelný štítek: celý aktuální měsíc
    return dnes.replace(day=1), dnes.replace(day=calendar.monthrange(dnes.year, dnes.month)[1])


vstup = sys.argv[1]
produkty = {}
for radek in open(vstup, encoding="utf-8"):
    casti = [c.strip() for c in radek.strip().split("|")]
    if len(casti) < 3 or not re.match(r"^[\w/ -]+$", casti[0]):
        continue
    kod = re.sub(r"\s", "", casti[0]).upper()
    cena = re.sub(r"[^\d]", "", casti[1])
    stav = casti[2].upper()
    if not cena or stav not in ("ANO", "NE"):
        continue
    akce = len(casti) > 3 and casti[3].upper() == "ANO"
    if len(casti) >= 7:
        stitek, nazev, url = casti[4], casti[5], casti[6]
    else:
        stitek, nazev, url = "", "", (casti[4] if len(casti) > 4 else "")
    p = produkty.setdefault(kod, {"nazev": "", "url": url, "_ano": 0, "_ne": 0, "_bezne": [], "_akce": []})
    p["_ne" if stav == "NE" else "_ano"] += 1
    if nazev and not p["nazev"]:
        p["nazev"] = nazev
    if akce:
        p["_akce"].append((float(cena), stitek))
    else:
        p["_bezne"].append(float(cena))

for p in produkty.values():
    # produkt bývá ve více kategoriích; při rozporu (chyba čtení) rozhoduje většina, při shodě „není skladem“
    p["skladem"] = p.pop("_ano") > p.pop("_ne")
    bezne, akce = p.pop("_bezne"), p.pop("_akce")
    # běžná cena jen z karet bez akce (akční cena se pro návrh běžné ceny nepoužije)
    p["cena"] = max(bezne) if bezne else None
    # akce: jen platné (stránka kategorie může být ze staršího stavu se skončenou akcí); nejnižší cena
    platne = []
    for cena_akce, stitek in akce:
        od, do = platnost(stitek, ted.date())
        if do >= ted.date():
            platne.append((cena_akce, not re.search(r"\d", stitek or ""), od, do, stitek))
    if platne:
        cena_akce, _, od, do, stitek = min(platne)  # při stejné ceně má přednost štítek s datem
        if p["cena"] is None or cena_akce < p["cena"]:
            p["akce"] = {"cena": cena_akce, "od": od.isoformat(), "do": do.isoformat(), "stitek": stitek}

if len(produkty) < 150:
    sys.exit(f"Podezřele málo produktů LR ({len(produkty)}), neukládám.")
with open(os.path.join(ROOT, "data", "lr.json"), "w", encoding="utf-8") as f:
    json.dump({"cas": ted.isoformat(timespec="minutes"), "produkty": produkty}, f, ensure_ascii=False, indent=0, sort_keys=True)
print(f"Uloženo {len(produkty)} produktů LR, z toho není skladem: "
      f"{sum(1 for p in produkty.values() if not p['skladem'])}, v akci: "
      f"{sum(1 for p in produkty.values() if p.get('akce'))}")
