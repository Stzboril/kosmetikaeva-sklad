import os, sys
sys.path.insert(0,'.')
from lux import PAL, defs, frame, icons
order=['Obličej','Tělo','Parfémy','Vlasy','Esenciální oleje','Pro děti','Praní prádla','Medové speciality']
font='/home/claude/kosmetikaeva-sklad/work/design/fonts/'
css=f'''@font-face{{font-family:M;font-weight:700;src:url(file://{font}montserrat-700.woff)}}@font-face{{font-family:M;font-weight:400;src:url(file://{font}montserrat-400.woff)}}
body{{margin:0;background:#fff;font-family:M;color:#1c1b29}} .sec{{padding:24px 36px 10px}} h2{{font:700 21px M;margin:0 0 14px;color:#1c1b29}} h2 span{{color:#a3392a}}
.row{{display:grid;grid-template-columns:repeat(8,1fr);gap:14px}} .row div{{text-align:center;font:700 12.5px M}} .row svg{{width:132px;height:132px;display:block;margin:0 auto 6px}}
.grid{{display:grid;grid-template-columns:repeat(4,1fr);gap:20px 28px;margin-top:6px}} .t{{display:flex;align-items:center;gap:16px}} .t svg{{width:86px;height:86px;flex:0 0 86px}} .t b{{font:700 18px M}}'''
html=f'<html><head><style>{css}</style></head><body>'
for i,(k,p) in enumerate(PAL.items()):
    I=icons(p)
    def svg(n, k=k): return (f'<svg viewBox="0 0 100 100">{defs(p)}{frame(p)}{I[n]}</svg>').replace('id="bgg"',f'id="bgg_{k}"').replace('url(#bgg)',f'url(#bgg_{k})').replace('id="gold"',f'id="gold_{k}"').replace('url(#gold)',f'url(#gold_{k})')
    html+=f'<div class="sec"><h2><span>{chr(69+i)}</span> – {p["name"]}</h2><div class="row">'+''.join(f'<div>{svg(n)}{n}</div>' for n in order)+'</div>'
    html+='<div class="grid">'+''.join(f'<div class="t">{svg(n)}<b>{n}</b></div>' for n in order[:4])+'</div></div>'
html+='</body></html>'
open('lux.html','w').write(html)
from playwright.sync_api import sync_playwright
with sync_playwright() as pw:
    b=pw.chromium.launch(); pg=b.new_page(viewport={'width':1280,'height':800}); pg.goto('file://'+os.path.abspath('lux.html')); pg.wait_for_timeout(400); pg.screenshot(path=sys.argv[1],full_page=True); b.close()
print('ok')
