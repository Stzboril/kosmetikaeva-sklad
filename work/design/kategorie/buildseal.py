import os, sys
sys.path.insert(0,'.')
from lux2 import I
from face5 import face
from seal import seal
I['Obličej']=face('x')
order=['Obličej','Tělo','Parfémy','Vlasy','Esenciální oleje','Pro děti','Praní prádla','Medové speciality']
font='/home/claude/kosmetikaeva-sklad/work/design/fonts/'
css=f'''@font-face{{font-family:Montserrat;font-weight:700;src:url(file://{font}montserrat-700.woff)}}@font-face{{font-family:M;font-weight:700;src:url(file://{font}montserrat-700.woff)}}
body{{margin:0;background:#fff;font-family:M;color:#1c1b29}} .sec{{padding:24px 36px 10px}} h2{{font:700 21px M;margin:0 0 14px}}
.big{{display:grid;grid-template-columns:repeat(4,1fr);gap:24px 26px}} .big svg{{width:250px;height:250px;display:block;margin:0 auto}}
.grid{{display:grid;grid-template-columns:repeat(4,1fr);gap:20px 28px;margin-top:6px}} .t{{display:flex;align-items:center;gap:16px}} .t svg{{width:86px;height:86px;flex:0 0 86px}} .t b{{font:700 18px M}}'''
html=f'<html><head><style>{css}</style></head><body><div class="sec"><h2>Slonovina a zlato – název v mezikruží</h2><div class="big">'+''.join(seal(n,I[n],f'b{i}') for i,n in enumerate(order))+'</div></div>'
html+='<div class="sec"><h2>Ve skutečné velikosti na stránce kategorie</h2><div class="grid">'+''.join(f'<div class="t">{seal(n,I[n],f"s{i}")}<b>{n}</b></div>' for i,n in enumerate(order))+'</div></div></body></html>'
open('seal.html','w').write(html)
from playwright.sync_api import sync_playwright
with sync_playwright() as pw:
    b=pw.chromium.launch(); pg=b.new_page(viewport={'width':1200,'height':800}); pg.goto('file://'+os.path.abspath('seal.html')); pg.wait_for_timeout(500); pg.screenshot(path=sys.argv[1],full_page=True); b.close()
print('ok')
