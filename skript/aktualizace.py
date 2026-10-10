"""Denní kontrola skladu a cen KosmetikaEva.eu podle dodavatelů.

Výstupy:
  feed/sklad.csv   – import skladu pro Shoptet (stahuje se automaticky)
  navrh/ceny.csv   – navržené změny prodejních cen (jdou ke schválení přes Pull request)
  navrh/popis.md   – text Pull requestu s tabulkou změn cen
  zprava.md        – čitelná zpráva o posledním běhu
  data/stav.json   – stav posledního běhu (pro porovnání)

Pravidla (dohodnutá s majitelem e-shopu):
  * skladem u dodavatele -> sklad 20, není skladem / nenalezeno -> sklad 0
  * prodejní cena = doporučená cena výrobce − 8 %, zaokrouhleno nahoru na Kč končící 9,
    nikdy ne nad doporučenou cenu
  * ceny Just a Nahrin se nemění (skript je vůbec nezpracovává)
  * produkt v akci (má akční cenu) -> cena se nenavrhuje
"""
import csv
import io
import json
import math
import os
import re
import sys
import time
import xml.etree.ElementTree as ET
from datetime import datetime, timezone, timedelta

import requests

sys.path.insert(0, os.path.dirname(__file__))
import dodavatele  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ESHOP_FEED = "https://www.kosmetikaeva.eu/google/export/products.xml"
G = "{http://base.google.com/ns/1.0}"
SLEDOVANE = {"Eurona", "Essens", "LR"}
NE_SKLAD, ANO_SKLAD = "0", "20"
PRAHA = timezone(timedelta(hours=2))


def cesta(*p):
    return os.path.join(ROOT, *p)


def ceil9(x):
    """Nejbližší vyšší (nebo stejná) cena v Kč končící devítkou."""
    n = math.ceil(round(x, 2))
    return n + (9 - n % 10) % 10


def nova_cena(doporucena):
    return min(ceil9(doporucena * 0.92), math.floor(doporucena))


def cislo(s):
    m = re.search(r"[\d.,]+", s or "")
    return float(m.group(0).replace(",", ".")) if m else None


# ------------------------------------------------------------ e-shop
def eshop_produkty():
    """Viditelné produkty e-shopu z veřejného Google feedu Shoptetu."""
    r = requests.get(ESHOP_FEED, timeout=120, headers={"User-Agent": dodavatele.UA})
    r.raise_for_status()
    root = ET.fromstring(r.content)
    out = {}
    for it in root.iter("item"):
        kod = (it.findtext(G + "id") or "").strip()
        znacka = (it.findtext(G + "brand") or "").strip()
        if not kod or znacka not in SLEDOVANE:
            continue
        out[kod.upper()] = {
            "kod": kod,
            "nazev": (it.findtext("title") or "").strip(),
            "znacka": znacka,
            "cena": cislo(it.findtext(G + "price")),
            "akce": cislo(it.findtext(G + "sale_price")),
            "skladem": (it.findtext(G + "availability") or "") == "in stock",
            "skupina": (it.findtext(G + "item_group_id") or "").strip(),
            "url": (it.findtext("link") or "").strip(),
        }
    if len(out) < 300:
        raise RuntimeError(f"E-shop feed: podezřele málo produktů ({len(out)})")
    return out


def nacti_csv(nazev):
    p = cesta(*nazev.split("/"))
    if not os.path.exists(p):
        return []
    with open(p, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f, delimiter=";"))


def zapis_csv(nazev, hlavicka, radky):
    """CSV ve formátu importu Shoptetu: UTF-8 s BOM, středník, vše v uvozovkách."""
    buf = io.StringIO()
    w = csv.writer(buf, delimiter=";", quoting=csv.QUOTE_ALL, lineterminator="\r\n")
    w.writerow(hlavicka)
    w.writerows(radky)
    with open(cesta(*nazev.split("/")), "w", encoding="utf-8-sig", newline="") as f:
        f.write(buf.getvalue())


# ------------------------------------------------------------ párování kódů
def najdi(kod, katalog):
    """Najde produkt dodavatele podle kódu e-shopu (velikost písmen nehraje roli)."""
    k = kod.upper()
    if k in katalog:
        return katalog[k]
    alias = ALIASY.get(k)
    if alias and alias in katalog:
        return katalog[alias]
    if k.startswith("E") and k[1:] in katalog:  # Eurona kódy s předponou E (kolize s jiným výrobcem)
        return katalog[k[1:]]
    return None


ALIASY = {}  # doplní se z data/aliasy.csv (kod_eshop;kod_dodavatel)
NEMENIT_CENU = set()  # data/nemenit_cenu.csv – sady, série a jiné výjimky


def main():
    ted = datetime.now(PRAHA)
    for r in nacti_csv("data/aliasy.csv"):
        ALIASY[r["kod_eshop"].strip().upper()] = r["kod_dodavatel"].strip().upper()
    for r in nacti_csv("data/nemenit_cenu.csv"):
        NEMENIT_CENU.add(r["kod"].strip().upper())
    parove = {r["code"].strip().upper(): r["pairCode"].strip() for r in nacti_csv("data/eshop_kody.csv")}
    # ceny schválené v posledních 48 h, které si Shoptet možná ještě nestáhl
    schvalene = {r["code"].strip().upper(): cislo(r["price"]) for r in nacti_csv("feed/ceny.csv")}

    eshop = eshop_produkty()
    predchozi = {}
    if os.path.exists(cesta("data", "stav.json")):
        predchozi = json.load(open(cesta("data", "stav.json"), encoding="utf-8"))

    katalogy, chyby = {}, {}
    for znacka, fce in (("Eurona", dodavatele.eurona), ("Essens", dodavatele.essens)):
        try:
            katalogy[znacka] = fce()
        except Exception as e:  # dodavatel nedostupný -> jeho sklad tentokrát neměníme
            chyby[znacka] = str(e)
    chyby.setdefault("LR", "web lr-czech.com blokuje servery (Cloudflare) – LR se kontroluje zvlášť")

    sklad_radky, ceny_radky, zmeny_skladu, nenalezeno, tabulka = [], [], [], [], []
    stav = {"cas": ted.isoformat(timespec="minutes"), "produkty": {}}

    # Essens: kódy, které nejsou v žádné kategorii, ještě dohledáme
    if "Essens" in katalogy:
        chybi = [k for k, p in eshop.items() if p["znacka"] == "Essens" and not najdi(k, katalogy["Essens"])]
        for kod in chybi[:120]:
            if True:
                nalez = None
                url = (predchozi.get("produkty", {}).get(kod) or {}).get("url_dodavatel")
                try:
                    nalez = dodavatele.essens_hledej(kod) or (dodavatele.essens_detail(url) if url else None)
                except Exception:
                    nalez = None
                if nalez:
                    katalogy["Essens"][kod] = nalez
                time.sleep(0.3)

    for kod, p in sorted(eshop.items()):
        znacka = p["znacka"]
        if znacka not in katalogy:
            continue
        sup = najdi(kod, katalogy[znacka])
        stary = (predchozi.get("produkty", {}).get(kod) or {})
        if sup is None:
            nenalezeno.append(p)
            sklad = NE_SKLAD
        else:
            sklad = ANO_SKLAD if sup["skladem"] else NE_SKLAD
        sklad_radky.append([p["kod"], parove.get(kod, ""), sklad])
        if (ANO_SKLAD if p["skladem"] else NE_SKLAD) != sklad:
            zmeny_skladu.append((p, sklad))
        stav["produkty"][kod] = {
            "sklad": sklad,
            "dop": sup["cena"] if sup else None,
            "url_dodavatel": (sup or {}).get("url") or stary.get("url_dodavatel", ""),
        }

        # ---- cena
        if not sup or not sup.get("cena") or kod in NEMENIT_CENU or p["cena"] is None:
            continue
        if p["akce"]:
            continue
        nova = nova_cena(sup["cena"])
        if abs(nova - p["cena"]) < 0.5 or schvalene.get(kod) == nova:
            continue
        zmena = (nova - p["cena"]) / p["cena"] * 100
        ceny_radky.append([p["kod"], parove.get(kod, ""), f"{nova:.0f}"])
        tabulka.append((znacka, p["nazev"], p["kod"], p["cena"], nova, sup["cena"], zmena, p["url"]))

    # Dodavatel, který tentokrát nešel stáhnout: ponecháme jeho řádky z minula
    stary_feed = {r["code"].upper(): r for r in nacti_csv("feed/sklad.csv")}
    for kod, p in eshop.items():
        if p["znacka"] not in katalogy and kod in stary_feed:
            r = stary_feed[kod]
            sklad_radky.append([r["code"], r.get("pairCode", ""), r["stock"]])

    zapis_csv("feed/sklad.csv", ["code", "pairCode", "stock"], sklad_radky)
    zapis_csv("navrh/ceny.csv", ["code", "pairCode", "price"], ceny_radky)

    # ---- text Pull requestu s návrhem cen
    tabulka.sort(key=lambda x: (x[0], -abs(x[6])))
    md = [f"Návrh nových prodejních cen podle doporučených cen výrobců ({ted:%d.%m.%Y %H:%M}).",
          "",
          "Pravidlo: doporučená cena − 8 %, zaokrouhleno nahoru na Kč končící 9, nikdy nad doporučenou cenu. "
          "Produkty v akci, Just a Nahrin se nemění.",
          "",
          "**Schválení:** dole klikněte na *Merge pull request* → *Confirm merge*. Shoptet si nové ceny "
          "stáhne při nejbližším automatickém importu. Když nesouhlasíte, Pull request jen zavřete.",
          "",
          f"Počet změn: **{len(tabulka)}**"
          + (f" (z toho **{sum(1 for t in tabulka if abs(t[6]) >= 20)}** o 20 % a víc – zkontrolujte, "
             "jestli nejde o sadu nebo jiné balení)" if any(abs(t[6]) >= 20 for t in tabulka) else ""),
          "",
          "| Výrobce | Produkt | Kód | Nyní | Nově | Doporučená | Změna |",
          "|---|---|---|--:|--:|--:|--:|"]
    for z, n, k, c, nc, d, pct in tabulka:
        varovani = " ⚠️" if abs(pct) >= 20 else ""
        md.append(f"| {z} | [{n}]({_url(eshop, k)}) | {k} | {c:.0f} Kč | **{nc:.0f} Kč** | {d:.0f} Kč | {pct:+.1f} %{varovani} |")
    with open(cesta("navrh", "popis.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(md) + "\n")

    # ---- zpráva
    z = [f"# Kontrola skladu a cen – {ted:%d.%m.%Y %H:%M}", ""]
    for znacka in ("Eurona", "Essens", "LR"):
        if znacka in katalogy:
            pocet = sum(1 for p in eshop.values() if p["znacka"] == znacka)
            z.append(f"- **{znacka}:** zkontrolováno {pocet} produktů e-shopu (u dodavatele {len(katalogy[znacka])} produktů)")
        else:
            z.append(f"- **{znacka}:** sklad se tentokrát neměnil – {chyby.get(znacka, '')}")
    z += ["", f"## Změny skladu ({len(zmeny_skladu)})", ""]
    for p, s in zmeny_skladu:
        z.append(f"- {'✅ naskladněno' if s == ANO_SKLAD else '❌ vyprodáno'}: {p['nazev']} ({p['kod']})")
    z += ["", f"## Nenalezeno u dodavatele ({len(nenalezeno)}) – sklad 0, zvažte skrytí", ""]
    for p in nenalezeno:
        z.append(f"- {p['nazev']} ({p['kod']})")
    z += ["", f"## Navržené změny cen: {len(tabulka)} – viz otevřený Pull request", ""]
    with open(cesta("zprava.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(z) + "\n")

    with open(cesta("data", "stav.json"), "w", encoding="utf-8") as f:
        json.dump(stav, f, ensure_ascii=False, indent=0, sort_keys=True)

    print(f"Sklad: {len(sklad_radky)} řádků, změn {len(zmeny_skladu)}; návrhy cen: {len(tabulka)}; "
          f"nenalezeno: {len(nenalezeno)}; chyby: {chyby}")
    # GitHub Actions: předáme počet návrhů dalšímu kroku
    if os.environ.get("GITHUB_OUTPUT"):
        with open(os.environ["GITHUB_OUTPUT"], "a") as f:
            f.write(f"navrhu={len(tabulka)}\n")


def _url(eshop, kod):
    return eshop.get(kod.upper(), {}).get("url", "")


if __name__ == "__main__":
    main()
