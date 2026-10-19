import os, sys
sys.path.insert(0,'.')
from icons import I, DEFS
order=['Obličej','Tělo','Parfémy','Vlasy','Esenciální oleje','Pro děti','Praní prádla','Medové speciality']
font='/home/claude/kosmetikaeva-sklad/work/design/fonts/'
css=f'''@font-face{{font-family:M;font-weight:700;src:url(file://{font}montserrat-700.woff)}}@font-face{{font-family:M;font-weight:400;src:url(file://{font}montserrat-400.woff)}}
body{{margin:0;background:#fff;font-family:M;color:#1c1b29}} .sec{{padding:26px 36px 14px}} h2{{font:700 22px M;margin:0 0 4px;color:#a3392a}} p.d{{font:400 15px M;color:#6e6c7a;margin:0 0 18px}}
.big{{display:grid;grid-template-columns:repeat(4,1fr);gap:26px 30px}} .big div{{text-align:center;font:700 16px M}} .big svg{{width:170px;height:170px;display:block;margin:0 auto 8px}}
.grid{{display:grid;grid-template-columns:repeat(4,1fr);gap:22px 30px}} .t{{display:flex;align-items:center;gap:18px}} .t svg{{width:86px;height:86px;flex:0 0 86px}} .t b{{font:700 19px M}}'''
def svg(k): return f'<svg viewBox="0 0 100 100">{DEFS}{I[k]}</svg>'
html=f'<html><head><style>{css}</style></head><body><div class="sec"><h2>D – Ilustrace (zvětšené)</h2><p class="d">Plochá ilustrace ve vínové, růžové a medové, bez ražení – jiný styl než ikony u výrobků.</p><div class="big">'
html+=''.join(f'<div>{svg(k)}{k}</div>' for k in order)+'</div></div>'
html+='<div class="sec"><h2>Ve skutečné velikosti na stránce kategorie</h2><p class="d">Stejné rozložení jako dnes: obrázek a název vedle sebe.</p><div class="grid">'+''.join(f'<div class="t">{svg(k)}<b>{k}</b></div>' for k in order)+'</div></div></body></html>'
open('d.html','w').write(html)
from playwright.sync_api import sync_playwright
with sync_playwright() as pw:
    b=pw.chromium.launch(); pg=b.new_page(viewport={'width':1280,'height':800}); pg.goto('file://'+os.path.abspath('d.html')); pg.wait_for_timeout(400); pg.screenshot(path=sys.argv[1] if len(sys.argv)>1 else 'd.png',full_page=True); b.close()
print('ok')
