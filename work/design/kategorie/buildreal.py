import os, sys
sys.path.insert(0,'.')
from lux2 import I
from face5 import face
from seal import seal
from seal2 import seal2
I['Obličej']=face('x')
order=['Obličej','Tělo','Parfémy','Vlasy','Esenciální oleje','Pro děti','Praní prádla','Medové speciality']
font='/home/claude/kosmetikaeva-sklad/work/design/fonts/'
css=f'''@font-face{{font-family:Montserrat;font-weight:700;src:url(file://{font}montserrat-700.woff)}}@font-face{{font-family:M;font-weight:700;src:url(file://{font}montserrat-700.woff)}}
body{{margin:0;background:#f6f4f4;font-family:M;color:#1c1b29}} .sec{{padding:18px 24px 6px}} h2{{font:700 16px M;margin:0 0 10px;color:#7c1f17}}
.grid{{display:grid;grid-template-columns:repeat(4,1fr);gap:10px 10px}} .t{{display:flex;align-items:center;gap:14px;background:#fff;border-radius:14px;padding:6px 12px;height:58px}} .t svg{{width:56px;height:56px;flex:0 0 56px}} .t b{{font:700 14px/1.3 M}}
.zoom{{display:flex;gap:30px;align-items:center}} .zoom svg{{width:200px;height:200px}} .zoom span{{font:700 13px M;color:#6e6c7a}}'''
def grid(fn,p): return '<div class="grid">'+''.join(f'<div class="t">{fn(n,p+str(i))}<b>{n}</b></div>' for i,n in enumerate(order))+'</div>'
html=f'<html><head><style>{css}</style></head><body>'
html+='<div class="sec"><h2>Schválený návrh – skutečná velikost na webu (56 px)</h2>'+grid(lambda n,u: seal(n,I[n],u),'a')+'</div>'
html+='<div class="sec"><h2>Návrh: bez textu v kruhu, větší kresba, silnější linka (56 px)</h2>'+grid(lambda n,u: seal2(I[n],u),'b')+'</div>'
html+='<div class="sec"><h2>Zvětšeno pro porovnání</h2><div class="zoom">'+seal('Obličej',I['Obličej'],'z1')+'<span>teď</span>'+seal2(I['Obličej'],'z2')+'<span>návrh</span>'+seal('Medové speciality',I['Medové speciality'],'z3')+seal2(I['Medové speciality'],'z4')+'</div></div></body></html>'
open('real.html','w').write(html)
from playwright.sync_api import sync_playwright
with sync_playwright() as pw:
    b=pw.chromium.launch(); pg=b.new_page(viewport={'width':1100,'height':600},device_scale_factor=2); pg.goto('file://'+os.path.abspath('real.html')); pg.wait_for_timeout(500); pg.screenshot(path=sys.argv[1],full_page=True); b.close()
print('ok')
