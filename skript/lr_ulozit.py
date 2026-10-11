"""Uloží data LR stažená mimo GitHub (LR blokuje servery GitHubu).

Vstup: textový soubor, na každém řádku  KOD|CENA|STAV|URL_KATEGORIE
       STAV = ANO (skladem) / NE (karta má štítek „Není skladem“)
Výstup: data/lr.json  {"cas": ..., "produkty": {KOD: {"skladem", "cena", "nazev", "url"}}}
"""
import json
import os
import re
import sys
from datetime import datetime, timezone, timedelta

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
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
    p = produkty.setdefault(kod, {"skladem": True, "cena": float(cena), "nazev": "", "url": casti[3] if len(casti) > 3 else ""})
    if stav == "NE":  # stačí jedna kategorie se štítkem „Není skladem“
        p["skladem"] = False
if len(produkty) < 150:
    sys.exit(f"Podezřele málo produktů LR ({len(produkty)}), neukládám.")
ted = datetime.now(timezone(timedelta(hours=2)))
with open(os.path.join(ROOT, "data", "lr.json"), "w", encoding="utf-8") as f:
    json.dump({"cas": ted.isoformat(timespec="minutes"), "produkty": produkty}, f, ensure_ascii=False, indent=0, sort_keys=True)
print(f"Uloženo {len(produkty)} produktů LR, z toho není skladem: {sum(1 for p in produkty.values() if not p['skladem'])}")
