# Vyrenderuje PNG 800×800 (průhledné rohy) pro všech 42 kategorií do složky png/
import os, sys, re, json, unicodedata
sys.path.insert(0,'.')
from buildall import ORDER, inner
from seal2 import seal2
def slug(n):
    s=unicodedata.normalize('NFKD',n).encode('ascii','ignore').decode().lower()
    return re.sub(r'[^a-z0-9]+','-',s).strip('-')
os.makedirs('png',exist_ok=True)
names=[n for v in ORDER.values() for n in v]
from playwright.sync_api import sync_playwright
with sync_playwright() as pw:
    b=pw.chromium.launch(); pg=b.new_page(viewport={'width':800,'height':800})
    for i,n in enumerate(names):
        svg=seal2(inner(n),'p'+str(i)).replace('<svg ','<svg width="800" height="800" ',1)
        pg.set_content(f'<html><body style="margin:0;background:transparent">{svg}</body></html>')
        pg.screenshot(path=f'png/kat-{slug(n)}.png',omit_background=True,clip={'x':0,'y':0,'width':800,'height':800})
    b.close()
print(len(names)); json.dump({n:f'kat-{slug(n)}.png' for n in names},open('png/mapa.json','w'),ensure_ascii=False,indent=0)
