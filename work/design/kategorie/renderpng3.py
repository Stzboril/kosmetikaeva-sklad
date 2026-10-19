# PNG 800×800 pro 20 hlubších podkategorií → png/ (název podle id kategorie)
import os, sys, json
sys.path.insert(0,'.')
from cat3 import I as I3
from seal2 import seal2
IDS={'1864':('Parfémy dámské','kat-parfemy-damske.png'),'1867':('Parfémy pánské','kat-parfemy-panske.png'),'1870':('Parfémy unisex','kat-parfemy-unisex.png'),
 '1852':('Make-up obličej','kat-makeup-oblicej.png'),'1855':('Make-up oči','kat-makeup-oci.png'),'1858':('Make-up rty','kat-makeup-rty.png'),'1861':('Make-up nehty','kat-makeup-nehty.png'),
 '1822':('Bílé prádlo','kat-bile-pradlo.png'),'1825':('Černé prádlo','kat-cerne-pradlo.png'),'1828':('Barevné prádlo','kat-barevne-pradlo.png'),
 '1831':('Univerzální prací prostředky','kat-univerzalni-praci-prostredky.png'),'1834':('Aviváže s kondicionérem','kat-avivaze-s-kondicionerem.png'),
 '1939':('Parfémy na praní','kat-parfemy-na-prani.png'),'1837':('Na skvrny','kat-na-skvrny.png'),'1840':('Jemné prádlo','kat-jemne-pradlo.png'),
 '1843':('Speciální prací prostředky','kat-specialni-praci-prostredky.png'),'1876':('Na záclony','kat-na-zaclony.png'),'1879':('Pro miminka','kat-pro-miminka.png'),
 '1846':('Ruční mytí','kat-rucni-myti.png'),'1849':('Mytí v myčce','kat-myti-v-mycce.png')}
from playwright.sync_api import sync_playwright
with sync_playwright() as pw:
    b=pw.chromium.launch(); pg=b.new_page(viewport={'width':800,'height':800})
    for i,(cid,(key,fn)) in enumerate(IDS.items()):
        svg=seal2(I3[key],'q'+str(i)).replace('<svg ','<svg width="800" height="800" ',1)
        pg.set_content(f'<html><body style="margin:0;background:transparent">{svg}</body></html>')
        pg.screenshot(path='png/'+fn,omit_background=True,clip={'x':0,'y':0,'width':800,'height':800})
    b.close()
json.dump({k:v[1] for k,v in IDS.items()},open('png/mapa-podkategorie.json','w'),ensure_ascii=False,indent=0)
print(len(IDS))
