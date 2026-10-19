# Náhled všech 42 obrázků kategorií (pečeť bez textu): velké + skutečná velikost 56 px
import os, sys
sys.path.insert(0,'.')
from lux2 import I as I1
from face5 import face
from cat2 import I as I2
from seal2 import seal2
I1['Obličej']=face('x')
ORDER={'Kosmetika':['Obličej','Tělo','Ruce a nehty','Nohy a chodidla','Parfémy','Dekorativní kosmetika','Vlasy','Péče o ústa a zuby','Sprchové gely a pěny','Tekutá mýdla','Speciální péče','Pro děti','Pro muže','Opalování','Esenciální oleje','CBD'],
 'Doplňky stravy':['Imunitní systém','Koření','Aloe Vera gel','Vitamíny a minerály','Oleje','Sypané čaje','Káva','Medové speciality','Swissycandy'],
 'Domácnost':['Praní prádla','Mytí nádobí','Kuchyně','Koupelny','Okna a zrcadla','WC, toalety, odpady','Podlahy','Univerzální čisticí prostředky','Speciální čisticí prostředky','Koberce a vysavače','Osvěžovače vzduchu a textilií','Odpuzovače hmyzu','Péče o rostliny','Péče o vozidlo','Dezinfekce','Pro zvířata'],
 'Doplňkové služby':['Dárkové poukazy']}
ALL={**I1,**I2}
def inner(n): return ALL[n]
if __name__=='__main__':
    only=sys.argv[2].split('|') if len(sys.argv)>2 else None
    font='/home/claude/kosmetikaeva-sklad/work/design/fonts/'
    css=f'''@font-face{{font-family:M;font-weight:700;src:url(file://{font}montserrat-700.woff)}}
body{{margin:0;background:#f6f4f4;font-family:M;color:#1c1b29}} .sec{{padding:14px 22px 4px}} h2{{font:700 16px M;margin:0 0 10px;color:#7c1f17}}
.big{{display:grid;grid-template-columns:repeat(6,1fr);gap:12px}} .big div{{background:#fff;border-radius:14px;padding:10px 6px 8px;text-align:center;font:700 12px/1.25 M}} .big svg{{width:150px;height:150px;display:block;margin:0 auto 6px}}
.grid{{display:grid;grid-template-columns:repeat(4,1fr);gap:8px}} .t{{display:flex;align-items:center;gap:12px;background:#fff;border-radius:14px;padding:6px 12px;height:58px}} .t svg{{width:56px;height:56px;flex:0 0 56px}} .t b{{font:700 13px/1.25 M}}'''
    html=f'<html><head><style>{css}</style></head><body>'
    k=0
    for sec,names in ORDER.items():
        names=[n for n in names if (not only or n in only)]
        if not names: continue
        html+=f'<div class="sec"><h2>{sec}</h2><div class="big">'
        for n in names: k+=1; html+=f'<div>{seal2(inner(n),"b"+str(k))}{n}</div>'
        html+='</div></div>'
    html+='<div class="sec"><h2>Skutečná velikost 56 px</h2><div class="grid">'
    for sec,names in ORDER.items():
        for n in names:
            if only and n not in only: continue
            k+=1; html+=f'<div class="t">{seal2(inner(n),"s"+str(k))}<b>{n}</b></div>'
    html+='</div></div></body></html>'
    open('all.html','w').write(html)
    from playwright.sync_api import sync_playwright
    with sync_playwright() as pw:
        b=pw.chromium.launch(); pg=b.new_page(viewport={'width':1100,'height':600},device_scale_factor=1.5); pg.goto('file://'+os.path.abspath('all.html')); pg.wait_for_timeout(600); pg.screenshot(path=sys.argv[1],full_page=True); b.close()
    print('ok',k)
