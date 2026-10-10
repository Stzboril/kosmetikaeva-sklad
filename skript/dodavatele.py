"""Stažení dostupnosti a doporučených cen z veřejných stránek dodavatelů.

Každá funkce vrací slovník  KÓD (velkými písmeny) -> {
    "skladem": True/False,
    "cena": doporučená prodejní cena s DPH (float) nebo None,
    "nazev": název u dodavatele,
    "url": odkaz na produkt u dodavatele,
}
Používají se jen veřejné stránky bez přihlášení.
"""
import json
import re
import time

import requests
from bs4 import BeautifulSoup

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36")
S = requests.Session()
S.headers.update({"User-Agent": UA, "Accept-Language": "cs-CZ,cs;q=0.9"})


def get(url, **kw):
    """GET s opakováním (3 pokusy)."""
    last = None
    for pokus in range(3):
        try:
            r = S.get(url, timeout=40, **kw)
            if r.status_code == 200:
                return r
            last = f"HTTP {r.status_code}"
        except requests.RequestException as e:  # síťová chyba
            last = repr(e)
        time.sleep(3 * (pokus + 1))
    raise RuntimeError(f"Nepodařilo se stáhnout {url}: {last}")


# ---------------------------------------------------------------- EURONA
EURONA = "https://www.euronabycerny.com"


def eurona():
    """Celý katalog Eurona přes veřejné JSON API e-shopu (20 produktů na stránku)."""
    out = {}
    stranka, posledni = 1, 1
    while stranka <= posledni:
        j = get(f"{EURONA}/webapi/eshop/products/all?page={stranka}").json()["products"]
        posledni = j["last_page"]
        for p in j["data"]:
            kod = str(p["sku"]).strip().upper()
            out[kod] = {
                "skladem": bool(p.get("orderable")),
                "cena": float(p["cataloguePrice"]) if p.get("cataloguePrice") else None,
                "nazev": p.get("name", ""),
                "url": f"{EURONA}/p/{p['sku']}/{p.get('slug', '')}",
            }
        stranka += 1
        time.sleep(0.5)
    if len(out) < 300:
        raise RuntimeError(f"Eurona: podezřele málo produktů ({len(out)}), končím bez změn")
    return out


# ---------------------------------------------------------------- ESSENS
ESSENS = "https://www.essens.cz"
DOSTUPNOST = re.compile(r"(Skladem|Méně než \d+ ks|Nedostupné|Vyprodáno|Dočasně nedostupné|Brzy skladem)")


def _essens_dlazdice(html, out):
    """Z HTML výpisu kategorie / vyhledávání vytáhne produkty."""
    soup = BeautifulSoup(html, "lxml")
    n = 0
    for a in soup.select("a.p-item-fc"):
        m = re.search(r"addObjectToCart\((\{.*?\})\s*,", a.get("onclick", ""))
        if not m:
            continue
        try:
            j = json.loads(m.group(1))
        except ValueError:
            continue
        box = a.find_parent(class_="thumbnail-new") or a.parent.parent
        text = " ".join(box.get_text(" ").split())
        d = DOSTUPNOST.search(text)
        stav = d.group(1) if d else ""
        det = box.select_one("a.p-item-fd")
        kod = j["goo_code"].strip().upper()
        out[kod] = {
            "skladem": stav.startswith("Skladem") or stav.startswith("Méně než"),
            "stav": stav,
            "cena": float(j["price"]) if j.get("price") else None,
            "nazev": j.get("name", ""),
            "url": det["href"] if det and det.has_attr("href") else "",
        }
        n += 1
    return n


def essens():
    """Projde všechny kategorie z menu essens.cz včetně „Načíst další“."""
    home = get(ESSENS + "/").text
    kategorie = sorted(set(re.findall(r"https://www\.essens\.cz/[^\"'?#\s]*-c(\d+)/?[\"']", home)), key=int)
    out = {}
    for c in kategorie:
        html = get(f"{ESSENS}/eshop.php", params={"cat_id": c}).text
        _essens_dlazdice(html, out)
        strana = 1
        while "has-more" in html and strana < 60:
            html = get(f"{ESSENS}/eshop.php", params={"cat_id": c, "load-more": strana}).text
            _essens_dlazdice(html, out)
            strana += 1
            time.sleep(0.3)
    if len(out) < 300:
        raise RuntimeError(f"Essens: podezřele málo produktů ({len(out)}), končím bez změn")
    return out


def essens_hledej(kod):
    """Dohledá jeden kód přes vyhledávání (pro produkty, které nejsou v žádné kategorii)."""
    out = {}
    for dotaz in {kod.lower(), re.sub(r"\d{2}X?$", "", kod.lower())}:
        _essens_dlazdice(get(f"{ESSENS}/eshop.php", params={"search": dotaz}).text, out)
        if kod in out:
            return out[kod]
    return None


def essens_detail(url):
    """Dostupnost z detailu produktu (záloha, když produkt není ve výpisu)."""
    r = S.get(url, timeout=40)
    if r.status_code != 200:
        return None
    soup = BeautifulSoup(r.text, "lxml")
    el = soup.select_one(".detail-availability")
    stav = " ".join(el.get_text(" ").split()) if el else ""
    d = DOSTUPNOST.search(stav)
    stav = d.group(1) if d else stav
    cena = None
    el = soup.select_one(".price-wrap .price")
    if el:
        num = re.sub(r"[^\d,]", "", el.get_text()).replace(",", ".")
        cena = float(num) if num else None
    return {"skladem": stav.startswith("Skladem") or stav.startswith("Méně než"),
            "stav": stav, "cena": cena, "nazev": "", "url": url}
