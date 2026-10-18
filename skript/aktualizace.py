"""Denní kontrola skladu a cen KosmetikaEva.eu podle dodavatelů.

Výstupy (ukládají se do repozitáře):
  ke_importu/sklad.csv – jen produkty, u kterých je potřeba změnit sklad (import do Shoptetu)
  ke_importu/ceny.csv  – navržené nové prodejní ceny (import po schválení)
  ke_importu/akce.csv  – akční ceny podle akcí LR (import po schválení)
  zprava.md            – čitelná zpráva: co se změnilo a proč
  data/stav.json       – stav posledního běhu

Pravidla (dohodnutá s majitelem e-shopu):
  * dodavatel má skladem a e-shop ne  -> sklad 20
  * dodavatel nemá skladem (nebo produkt nenašel) a e-shop ano -> sklad 0
  * prodejní cena = doporučená cena výrobce − 8 %, zaokrouhleno nahoru na Kč končící 9,
    nikdy ne nad doporučenou cenu
  * Just a Nahrin se nezpracovávají vůbec
  * produkt v akci (má akční cenu) -> cena se nenavrhuje
  * LR má produkt v akci -> navrhne se akční cena na e-shopu = akční cena LR − 8 % (stejné zaokrouhlení),
    s platností podle štítku LR („Měsíční akce“ do konce měsíce) – ke_importu/akce.csv
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
ESHOP = "https://www.kosmetikaeva.eu"
GOOGLE_FEED = ESHOP + "/google/export/products.xml"
SKLAD_FEED = ESHOP + "/heureka/export/availability.xml"
G = "{http://base.google.com/ns/1.0}"
SNIMEK = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "eshop_produkty.json")
SLEDOVANE = {"Eurona", "Essens", "LR"}
NOVY_SKLAD = 20
# Parfémy Essens 50 ml (w…, m…, u…) starší řady (doporučená cena do 600 Kč) mají pevnou cenu 499 Kč
# podle rozhodnutí majitele (11. 10. 2026). Novější řada (doporučená 635 Kč) jde podle pravidla −8 % (589 Kč).
# Netýká se luxusních / niche parfémů, sad a vzorků.
ESSENS_PARFEM = re.compile(r"^Essens (Dámský|Pánský|Unisex) parfém [WMU]\d+ 50 ml$", re.I)
# Google feed může mít jiný (srovnávačový) název, např. „Essens m001 parfém pánský 50 ml“ -> poznáme i podle kódu
ESSENS_PARFEM_FEED = re.compile(r"^Essens [WMU]\d+ parfém (dámský|pánský|unisex) 50 ml$", re.I)
ESSENS_PARFEM_KOD = re.compile(r"^[WMU]\d{3}5[01][A-Z]?$")
ESSENS_PARFEM_CENA = 499
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
    m = re.search(r"-?[\d.,]+", s or "")
    return float(m.group(0).replace(",", ".")) if m else None


# ------------------------------------------------------------ e-shop
def eshop_produkty():
    """Viditelné produkty e-shopu z veřejných feedů Shoptetu (Google + Heureka dostupnost)."""
    ua = {"User-Agent": dodavatele.UA}
    r = requests.get(GOOGLE_FEED, timeout=120, headers=ua)
    r.raise_for_status()
    out = {}
    for it in ET.fromstring(r.content).iter("item"):
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
            "sklad": 1 if (it.findtext(G + "availability") or "") == "in stock" else 0,
            "url": (it.findtext("link") or "").strip(),
        }
    if len(out) < 300:
        raise RuntimeError(f"E-shop feed: podezřele málo produktů ({len(out)})")
    # přesné počty kusů z Heureka feedu dostupnosti
    r = requests.get(SKLAD_FEED, timeout=120, headers=ua)
    if r.ok:
        for it in ET.fromstring(r.content).iter("item"):
            kod = (it.get("id") or "").strip().upper()
            q = cislo(it.findtext("stock_quantity"))
            if kod in out and q is not None:
                out[kod]["sklad"] = int(q)

    # Google feed vynechává vyprodané produkty (a např. CBD). Bez nich by se vyprodaný produkt
    # už nikdy nenaskladnil -> pamatujeme si všechny produkty (data/eshop_produkty.json)
    # a ty, které ve feedu chybí, zkontrolujeme přímo na jejich stránce.
    znam = {}
    if os.path.exists(SNIMEK):
        znam = json.load(open(SNIMEK, encoding="utf-8"))
    for k, p in out.items():
        znam[k] = {"kod": p["kod"], "nazev": p["nazev"], "znacka": p["znacka"], "url": p["url"]}
    for k, z in sorted(znam.items()):
        if k in out or not z.get("url"):
            continue
        try:
            r = requests.get(z["url"], timeout=40, headers=ua)
        except requests.RequestException:
            continue
        if r.status_code != 200 or z["kod"].replace(" ", "").lower() not in r.text.replace(" ", "").lower():
            continue  # skrytý nebo smazaný produkt
        out[k] = {**z, "cena": None, "akce": None, "mimo_feed": True,
                  "sklad": 1 if "schema.org/InStock" in r.text else 0}
        time.sleep(0.2)
    with open(SNIMEK, "w", encoding="utf-8") as f:
        json.dump(znam, f, ensure_ascii=False, indent=0, sort_keys=True)
    return out


def nacti_csv(nazev):
    p = cesta(*nazev.split("/"))
    if not os.path.exists(p):
        return []
    with open(p, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f, delimiter=";"))


def zapis_csv(nazev, hlavicka, radky):
    """CSV ve formátu importu Shoptetu: UTF-8 s BOM, středník, vše v uvozovkách."""
    os.makedirs(os.path.dirname(cesta(*nazev.split("/"))), exist_ok=True)
    buf = io.StringIO()
    w = csv.writer(buf, delimiter=";", quoting=csv.QUOTE_ALL, lineterminator="\r\n")
    w.writerow(hlavicka)
    w.writerows(radky)
    with open(cesta(*nazev.split("/")), "w", encoding="utf-8-sig", newline="") as f:
        f.write(buf.getvalue())


# ------------------------------------------------------------ párování kódů
ALIASY = {}        # data/aliasy.csv (kod_eshop;kod_dodavatel)
NEMENIT_CENU = set()  # data/nemenit_cenu.csv – sady, série a jiné výjimky
NESLEDOVAT = set()    # data/nesledovat.csv – produkty, které se vůbec nekontrolují
ESSENS_URL = {}       # data/essens_url.csv – detail produktu Essens, který není v žádné kategorii
                      # (vyhledávání essens.cz bez přihlášení nefunguje)


def najdi(kod, katalog):
    """Najde produkt dodavatele podle kódu e-shopu (velikost písmen nehraje roli)."""
    k = re.sub(r"\s", "", kod.upper())
    if k in ALIASY:
        return katalog.get(ALIASY[k])
    if k in katalog:
        return katalog[k]
    if k.startswith("E") and k[1:] in katalog:  # Eurona kódy s předponou E (kolize s jiným výrobcem)
        return katalog[k[1:]]
    # Essens mění kódy přidáním písmene na konec (AVE01 -> AVE01B, W18350 -> W18350X, AVE61B -> AVE61N)
    zaklad = re.sub(r"(?<=\d)[A-Z]{1,2}$", "", k)
    for z in dict.fromkeys((k, zaklad)):
        for pripona in ("X", "N", "B", ""):
            if z + pripona != k and z + pripona in katalog:
                return katalog[z + pripona]
    # LR mění koncovku za pomlčkou (20679-101 -> 20679-301): stačí shoda čísla před pomlčkou, je-li jediná
    cislo_lr = k.split("-")[0]
    if cislo_lr.isdigit():
        shody = [x for x in katalog if x.split("-")[0] == cislo_lr]
        if len(shody) == 1:
            return katalog[shody[0]]
    return None


NOVE_JSON = "data/nove_u_dodavatele.json"    # kdy se který produkt u dodavatele objevil poprvé
NOVE_CSV = "nove_u_dodavatele.csv"            # úplný seznam produktů dodavatelů, které e-shop nemá
NOVE_IGNOROVAT = set()  # data/nove_ignorovat.csv – produkty dodavatele, které na e-shop nechceme
NOVE_DNI = 14           # jak dlouho se nový produkt ukazuje ve zprávě
# propagační a pomocné materiály dodavatelů (katalogy, tašky, nálepky, vzorky, startovací sady…)
NOVE_NE = re.compile(r"katalog|catalogue|start[ée]r|ta[šs]k|n[áa]lepk|samolepk|odznak|vzorek|vzork|tester|"
                     r"testovac[íi] pap|kick ?off|let[áa]k|bro[žz]ur|po[uú]kaz|voucher|registra[cč]|"
                     r"propisk|deštník|destnik|kel[ií]mek|hrnek|tri[čc]ko|kartičk|mikin|tepl[áa]k|selfie|shaker|krabi[čc]k|"
                     r"\bblok\b|sample|bestseller pack|v[íi]no\b|medovin|frizzante|[šs][áa]la\b|pono[žz]k|ru[čc]n[íi]k|osu[šs]k|"
                     r"ut[ěe]rk|[žz][íi]nk|p[řr]edlo[žz]k|pareo|[šs][áa]tek|hadř[íi]k|kybl[íi]k|pumpi[čc]k|bez n[áa]pln|"
                     r"galave[čc]er|bylo nebylo|caf[ée]\b|vzore[čc]|propisovac", re.I)


def nove_u_dodavatele(katalogy, eshop, ted):
    """Produkty dodavatelů, které na e-shopu nejsou (ani mezi skrytými známými produkty).
    Vrací (seznam položek, výchozí běh True/False)."""
    znam = dict(eshop)
    if os.path.exists(SNIMEK):  # i skryté produkty e-shopu, ať se nehlásí jako nové
        for k, z in json.load(open(SNIMEK, encoding="utf-8")).items():
            znam.setdefault(k, z)
    def zaklad(znacka, kod):  # Essens: AVE91 = AVE91N, LR: 20679-101 = 20679-301
        k = re.sub(r"\s", "", kod.upper())
        if znacka == "Essens":
            return re.sub(r"(?<=\d)[A-Z]{1,2}$", "", k)
        if znacka == "LR":
            return k.split("-")[0]
        return k
    zaklady = {(p.get("znacka"), zaklad(p.get("znacka"), kod)) for kod, p in znam.items()}
    pouzite = {}
    for kod, p in znam.items():
        if p.get("znacka") in katalogy:
            sup = najdi(kod, katalogy[p["znacka"]])
            if sup is not None:
                pouzite.setdefault(p["znacka"], set()).add(id(sup))

    p_json = cesta(*NOVE_JSON.split("/"))
    vychozi = not os.path.exists(p_json)
    historie = {} if vychozi else json.load(open(p_json, encoding="utf-8"))
    dnes = ted.date().isoformat()
    polozky = []
    for znacka, katalog in katalogy.items():
        for kod, sup in katalog.items():
            klic = f"{znacka}:{kod}"
            if id(sup) in pouzite.get(znacka, set()) or kod in NOVE_IGNOROVAT or klic.upper() in NOVE_IGNOROVAT:
                continue
            if NOVE_NE.search(sup.get("nazev") or "") or (znacka, zaklad(znacka, kod)) in zaklady:
                continue  # propagační materiál, nebo jen nový kód produktu, který e-shop už má
            if sup.get("cena") is not None and sup["cena"] < 20:
                continue  # vzorky a drobnosti
            h = historie.setdefault(klic, {"od": "výchozí" if vychozi else dnes})
            h["naposledy"] = dnes
            polozky.append({"znacka": znacka, "kod": kod, "od": h["od"], **sup})
    # produkty, které dodavatel přestal nabízet, zapomeneme po 30 dnech
    hranice = (ted.date() - timedelta(days=30)).isoformat()
    historie = {k: v for k, v in historie.items() if v.get("naposledy", dnes) >= hranice}
    with open(p_json, "w", encoding="utf-8") as f:
        json.dump(historie, f, ensure_ascii=False, indent=0, sort_keys=True)
    polozky.sort(key=lambda x: (x["znacka"], not x["skladem"], x["kod"]))
    zapis_csv("prehled/" + NOVE_CSV,
              ["vyrobce", "kod", "nazev", "skladem", "doporucena_cena", "navrzena_cena", "od", "url"],
              [[x["znacka"], x["kod"], " ".join((x.get("nazev") or "").split()), "ano" if x["skladem"] else "ne",
                f"{x['cena']:.0f}" if x.get("cena") else "",
                f"{nova_cena(x['cena']):.0f}" if x.get("cena") else "", x["od"], x.get("url", "")]
               for x in polozky])
    return polozky, vychozi


def odkaz(nazev, url):
    nazev = nazev.replace("|", "/")
    return f"[{nazev}]({url})" if url else nazev


def main():
    ted = datetime.now(PRAHA)
    for r in nacti_csv("data/aliasy.csv"):
        ALIASY[r["kod_eshop"].strip().upper()] = r["kod_dodavatel"].strip().upper()
    for r in nacti_csv("data/nemenit_cenu.csv"):
        NEMENIT_CENU.add(r["kod"].strip().upper())
    for r in nacti_csv("data/nesledovat.csv"):
        NESLEDOVAT.add(r["kod"].strip().upper())
    for r in nacti_csv("data/nove_ignorovat.csv"):
        NOVE_IGNOROVAT.add(r["kod"].strip().upper())
    for r in nacti_csv("data/essens_url.csv"):
        ESSENS_URL[r["kod"].strip().upper()] = r["url"].strip()
    parove = {r["code"].strip().upper(): r["pairCode"].strip() for r in nacti_csv("data/eshop_kody.csv")}

    eshop = eshop_produkty()
    predchozi = {}
    if os.path.exists(cesta("data", "stav.json")):
        predchozi = json.load(open(cesta("data", "stav.json"), encoding="utf-8"))

    katalogy, chyby = {}, {}
    for znacka, fce in (("Eurona", dodavatele.eurona), ("Essens", dodavatele.essens)):
        try:
            katalogy[znacka] = fce()
        except Exception as e:  # dodavatel nedostupný -> jeho produkty tentokrát neměníme
            chyby[znacka] = str(e)
    lr, lr_kdy = nacti_lr()
    lr_dnes = bool(lr_kdy) and lr_kdy.astimezone(PRAHA).date() == ted.date()
    lr_datum = f"{lr_kdy.astimezone(PRAHA):%d.%m.%Y}" if lr_kdy else "neznámo"
    if lr:
        katalogy["LR"] = lr
    else:
        chyby["LR"] = (f"data LR jsou starší než 3 dny (poslední z {lr_datum}); "
                       "stahují se úlohou Claude „LR sklad KosmetikaEva“, protože LR blokuje servery GitHubu")

    # Essens: kódy, které nejsou v žádné kategorii, dohledáme přes vyhledávání / detail
    if "Essens" in katalogy:
        chybi = [k for k, p in eshop.items() if p["znacka"] == "Essens" and k not in NESLEDOVAT
                 and not najdi(k, katalogy["Essens"])]
        # nejdřív vyprodané produkty mimo Google feed (ty jinak nikdo nezkontroluje)
        chybi.sort(key=lambda k: not eshop[k].get("mimo_feed"))
        for kod in chybi[:250]:
            hledat = ALIASY.get(kod, kod)
            url = ESSENS_URL.get(kod) or (predchozi.get("produkty", {}).get(kod) or {}).get("url_dodavatel")
            try:
                nalez = dodavatele.essens_hledej(hledat) or (dodavatele.essens_detail(url) if url else None)
            except Exception as e:
                nalez = None
                if eshop[kod].get("mimo_feed"):
                    print(f"::warning title=Essens hledání {kod}::{str(e)[:300]}")
            if nalez:
                katalogy["Essens"][hledat] = nalez
            elif eshop[kod].get("mimo_feed"):
                print(f"::notice title=Essens nenašel {kod}::hledáno jako {hledat}")
            time.sleep(0.3)
        print(f"::notice title=Essens dohledávání::chybělo {len(chybi)}, zkoušeno {min(len(chybi), 250)}")

    sklad_radky, ceny_radky, akce_radky = [], [], []
    naskladnit, vyprodat, nenalezeno, ceny, lr_overit, akce = [], [], [], [], [], []
    stav = {"cas": ted.isoformat(timespec="minutes"), "produkty": {}}

    for kod, p in sorted(eshop.items()):
        znacka = p["znacka"]
        if znacka not in katalogy or kod in NESLEDOVAT:
            continue
        sup = najdi(kod, katalogy[znacka])
        stary = predchozi.get("produkty", {}).get(kod) or {}
        stav["produkty"][kod] = {
            "skladem": bool(sup and sup["skladem"]),
            "dop": sup["cena"] if sup else None,
            "url_dodavatel": (sup or {}).get("url") or stary.get("url_dodavatel", ""),
        }

        # ---- sklad: měníme jen tam, kde nesedí „skladem / není skladem“
        if sup is None:
            nenalezeno.append(p)
            if p.get("mimo_feed"):
                continue  # produkt mimo Google feed, který dodavatel nezná: raději neměnit
        dodavatel_ma = bool(sup and sup["skladem"])
        if dodavatel_ma and p["sklad"] <= 0:
            sklad_radky.append([p["kod"], parove.get(kod, ""), str(NOVY_SKLAD)])
            naskladnit.append(p)
        elif not dodavatel_ma and p["sklad"] > 0:
            sklad_radky.append([p["kod"], parove.get(kod, ""), "0"])
            vyprodat.append((p, "dodavatel ho nenašel" if sup is None else (sup.get("stav") or "není skladem")))

        # ---- akce LR -> akční cena i na e-shopu
        a = (sup or {}).get("akce")
        if znacka == "LR" and a and a.get("cena") and kod not in NEMENIT_CENU and p["cena"] is not None \
                and a.get("do", "") >= ted.date().isoformat():
            akcni = nova_cena(a["cena"])
            # jen když je akční cena nižší než běžná na e-shopu a e-shop ji ještě nemá
            if akcni < p["cena"] - 0.5 and not (p["akce"] and abs(p["akce"] - akcni) < 0.5):
                od = a["od"]
                akce_radky.append([p["kod"], parove.get(kod, ""), f"{akcni:.0f}", od, a["do"], "1", od, a["do"]])
                akce.append((p, akcni, a))

        # ---- cena
        if not sup or not sup.get("cena") or kod in NEMENIT_CENU or p["cena"] is None or p["akce"]:
            continue
        nova = nova_cena(sup["cena"])
        nazev = " ".join(p["nazev"].split())
        if (znacka == "Essens" and sup["cena"] <= 600
                and (ESSENS_PARFEM.match(nazev) or ESSENS_PARFEM_FEED.match(nazev) or ESSENS_PARFEM_KOD.match(kod))):
            nova = ESSENS_PARFEM_CENA
        if abs(nova - p["cena"]) < 0.5:
            continue
        zmena = (nova - p["cena"]) / p["cena"] * 100
        if znacka == "LR" and abs(zmena) >= 20:
            # ceny LR se čtou z výpisu kategorií (WebFetch) a umí se splést s vedlejší kartou
            # -> velkou změnu do importu nedáváme, jen ji ukážeme k ruční kontrole
            lr_overit.append((p, nova, sup["cena"], zmena, sup.get("url", "")))
            continue
        ceny_radky.append([p["kod"], parove.get(kod, ""), f"{nova:.0f}"])
        ceny.append((znacka, p, nova, sup["cena"], zmena))

    zapis_csv("ke_importu/sklad.csv", ["code", "pairCode", "stock"], sklad_radky)
    zapis_csv("ke_importu/ceny.csv", ["code", "pairCode", "price"], ceny_radky)
    zapis_csv("ke_importu/akce.csv", ["code", "pairCode", "actionPrice", "actionFrom", "actionUntil",
                                      "actionFlagActive", "actionFlagValidFrom", "actionFlagValidUntil"], akce_radky)

    # ---- zpráva (zároveň text upozornění na GitHubu)
    raw = "https://github.com/Stzboril/kosmetikaeva-sklad/raw/main/ke_importu"
    z = [f"Kontrola u dodavatelů proběhla {ted:%d.%m.%Y v %H:%M}.", ""]
    for znacka in ("Eurona", "Essens", "LR"):
        if znacka in katalogy:
            pocet = sum(1 for p in eshop.values() if p["znacka"] == znacka)
            pozn = ""
            if znacka == "LR" and not lr_dnes:
                pozn = (f" – ⚠️ data LR jsou z {lr_datum}, dnešní stažení zatím neproběhlo "
                        "(stačí napsat Claude „stáhni LR“)")
            z.append(f"- **{znacka}:** zkontrolováno {pocet} viditelných produktů{pozn}")
        else:
            z.append(f"- **{znacka}:** nekontrolováno – {chyby.get(znacka, '')}")
    z += ["", "## Sklad", ""]
    if sklad_radky:
        z.append(f"Soubor k importu: [sklad.csv]({raw}/sklad.csv) ({len(sklad_radky)} produktů)")
        z.append("")
        for p in naskladnit:
            z.append(f"- ✅ zase skladem → 20 ks: {odkaz(p['nazev'], p['url'])} ({p['kod']})")
        for p, proc in vyprodat:
            z.append(f"- ❌ {proc} → 0 ks: {odkaz(p['nazev'], p['url'])} ({p['kod']})")
    else:
        z.append("Beze změn – sklad na e-shopu odpovídá dodavatelům.")
    z += ["", "## Ceny ke schválení", ""]
    if ceny:
        velke = sum(1 for c in ceny if abs(c[4]) >= 20)
        z.append(f"Soubor k importu: [ceny.csv]({raw}/ceny.csv) ({len(ceny)} produktů). "
                 "Pravidlo: doporučená cena − 8 %, zaokrouhleno nahoru na Kč končící 9. "
                 "Produkty v akci, Just a Nahrin se nemění.")
        if velke:
            z.append("")
            z.append(f"⚠️ {velke}× změna o 20 % a víc – zkontrolujte, jestli nejde o sadu nebo jiné balení.")
        z += ["", "| Výrobce | Produkt | Kód | Nyní | Nově | Doporučená | Změna |", "|---|---|---|--:|--:|--:|--:|"]
        for znacka, p, nova, dop, pct in sorted(ceny, key=lambda c: (c[0], -abs(c[4]))):
            z.append(f"| {znacka} | {odkaz(p['nazev'], p['url'])} | {p['kod']} | {p['cena']:.0f} Kč | "
                     f"**{nova:.0f} Kč** | {dop:.0f} Kč | {pct:+.1f} %{' ⚠️' if abs(pct) >= 20 else ''} |")
    else:
        z.append("Beze změn – ceny odpovídají pravidlu.")
    z += ["", "## Akce podle LR", ""]
    if akce:
        z.append(f"Soubor k importu: [akce.csv]({raw}/akce.csv) ({len(akce)} produktů). "
                 "LR má produkt v akci → akční cena na e-shopu = akční cena LR − 8 %, zaokrouhleno nahoru "
                 "na Kč končící 9, platnost a štítek Akce podle LR („Měsíční akce“ do konce měsíce). "
                 "Po skončení se akční cena v Shoptetu sama vypne.")
        z += ["", "| Produkt | Kód | Běžná | Akční | Akce LR | Platnost |", "|---|---|--:|--:|--:|---|"]
        for p, akcni, a in sorted(akce, key=lambda x: x[0]["nazev"]):
            od, do = (datetime.fromisoformat(x).strftime("%d.%m.") for x in (a["od"], a["do"]))
            z.append(f"| {odkaz(p['nazev'], p['url'])} | {p['kod']} | {p['cena']:.0f} Kč | **{akcni:.0f} Kč** | "
                     f"{a['cena']:.0f} Kč ({a.get('stitek') or 'akce'}) | {od}–{do} |")
    else:
        z.append("Žádná nová akce – produkty LR v akci buď na e-shopu nejsou, nebo už akční cenu mají.")
    if lr_overit:
        z += ["", f"### LR – ověřit ručně ({len(lr_overit)})", "",
              "Změna o 20 % a víc u LR není v ceny.csv: cena z webu LR může patřit vedlejší kartě. "
              "Ověřte na stránce produktu u LR; je-li správně, upravte cenu ručně.", ""]
        for p, nova, dop, pct, url in lr_overit:
            z.append(f"- {odkaz(p['nazev'], p['url'])} ({p['kod']}): nyní {p['cena']:.0f} Kč, "
                     f"LR uvádí {dop:.0f} Kč ([stránka]({url})) → vycházelo by {nova:.0f} Kč ({pct:+.1f} %)")
    if nenalezeno:
        z += ["", f"## Dodavatel produkt nenašel ({len(nenalezeno)})", "",
              "Nejspíš ho přestal prodávat, nebo má jiný kód. Pokud prodej skončil, produkt je vhodné skrýt.", ""]
        for p in nenalezeno:
            z.append(f"- {odkaz(p['nazev'], p['url'])} ({p['kod']})")

    # ---- nové produkty u dodavatelů, které e-shop nemá
    nove, vychozi = nove_u_dodavatele(katalogy, eshop, ted)
    hranice = (ted.date() - timedelta(days=NOVE_DNI - 1)).isoformat()
    cerstve = [x for x in nove if x["od"] != "výchozí" and x["od"] >= hranice]
    po_znackach = ", ".join(f"{zn} {sum(1 for x in nove if x['znacka'] == zn)}"
                            for zn in ("Eurona", "Essens", "LR") if any(x["znacka"] == zn for x in nove))
    z += ["", f"## Nové u dodavatele ({len(cerstve)})", ""]
    if vychozi:
        z.append("První přehled: zatím se jen zaznamenalo, co dodavatelé nabízejí navíc. "
                 "Od příští kontroly se tu ukážou produkty, které dodavatel nově přidá.")
    elif cerstve:
        z.append(f"Produkty, které se u dodavatele objevily za posledních {NOVE_DNI} dní a na e-shopu nejsou. "
                 "Navržená cena = doporučená − 8 % podle pravidla.")
        z += ["", "| Výrobce | Produkt | Kód | Skladem | Doporučená | Navržená | Od |", "|---|---|---|:-:|--:|--:|--:|"]
        for x in sorted(cerstve, key=lambda x: (x["od"], x["znacka"], x["kod"]), reverse=True):
            nazev = " ".join((x.get("nazev") or "").split()) or "(název neuveden)"
            dop = f"{x['cena']:.0f} Kč" if x.get("cena") else "–"
            nav = f"{nova_cena(x['cena']):.0f} Kč" if x.get("cena") else "–"
            od = datetime.fromisoformat(x["od"]).strftime("%d.%m.")
            z.append(f"| {x['znacka']} | {odkaz(nazev, x.get('url'))} | {x['kod']} | "
                     f"{'✅' if x['skladem'] else '❌'} | {dop} | {nav} | {od} |")
    else:
        z.append(f"Za posledních {NOVE_DNI} dní dodavatelé nepřidali nic, co by e-shop neměl.")
    if nove:
        z += ["", f"Celkem dodavatelé nabízejí {len(nove)} produktů, které na e-shopu nejsou ({po_znackach}) – "
                  f"úplný seznam: [{NOVE_CSV}]({raw.replace('ke_importu', 'prehled')}/{NOVE_CSV}). Produkt, který na e-shop nechcete, "
                  "stačí zapsat do data/nove_ignorovat.csv a přestane se ukazovat."]
    with open(cesta("zprava.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(z) + "\n")

    with open(cesta("data", "stav.json"), "w", encoding="utf-8") as f:
        json.dump(stav, f, ensure_ascii=False, indent=0, sort_keys=True)

    souhrn = f"sklad {len(sklad_radky)}, ceny {len(ceny)}, akce {len(akce)}"
    print(f"Hotovo: {souhrn}; nenalezeno {len(nenalezeno)}; chyby: {chyby}")
    if os.environ.get("GITHUB_OUTPUT"):
        with open(os.environ["GITHUB_OUTPUT"], "a") as f:
            f.write(f"sklad={len(sklad_radky)}\nceny={len(ceny)}\nakce={len(akce)}\n"
                    f"lr_dnes={1 if lr_dnes else 0}\nlr_datum={lr_datum}\n")


def nacti_lr():
    """Data LR se stahují zvlášť (data/lr.json); použijí se, jen když nejsou starší než 3 dny.
    Vrací (katalog nebo None, čas stažení nebo None)."""
    p = cesta("data", "lr.json")
    if not os.path.exists(p):
        return None, None
    d = json.load(open(p, encoding="utf-8"))
    try:
        kdy = datetime.fromisoformat(d["cas"])
    except (KeyError, ValueError):
        return None, None
    if datetime.now(PRAHA) - kdy > timedelta(days=3):
        return None, kdy
    return {k.upper(): v for k, v in d["produkty"].items()}, kdy


if __name__ == "__main__":
    try:
        main()
    except Exception:
        import traceback
        tb = traceback.format_exc()
        # chyba se zobrazí přímo v přehledu běhu na GitHubu
        print("::error title=Chyba kontroly::" + tb.replace("%", "%25").replace("\r", "").replace("\n", "%0A"))
        raise
