"""Diagnostika: zda jde lr-czech.com stáhnout ze serverů GitHubu."""
import re
import sys

URLS = ["https://www.lr-czech.com/zdravi", "https://www.lr-czech.com/parfemy"]
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"


def popis(nazev, status, text):
    titul = re.search(r"<title>(.*?)</title>", text, re.S | re.I)
    print(f"[{nazev}] status={status} delka={len(text)} title={titul.group(1).strip()[:80] if titul else '-'}"
          f" pocet_Kod={text.count('Kód')} cloudflare={'challenge' in text.lower() or 'cf-chl' in text}")
    i = text.find("Kód")
    if i >= 0:
        print("  ukazka:", re.sub(r"\s+", " ", text[max(0, i - 1500):i + 600]))


for url in URLS:
    print("=====", url)
    try:
        import requests
        r = requests.get(url, headers={"User-Agent": UA, "Accept-Language": "cs-CZ,cs;q=0.9"}, timeout=30)
        popis("requests", r.status_code, r.text)
    except Exception as e:
        print("[requests] chyba:", e)
    for imp in ("chrome", "safari", "firefox"):
        try:
            from curl_cffi import requests as cr
            r = cr.get(url, impersonate=imp, timeout=30, headers={"Accept-Language": "cs-CZ,cs;q=0.9"})
            popis(f"curl_cffi-{imp}", r.status_code, r.text)
        except Exception as e:
            print(f"[curl_cffi-{imp}] chyba:", e)
