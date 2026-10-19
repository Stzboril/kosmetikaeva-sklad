# Náhled 20 hlubších podkategorií
import os, sys
sys.path.insert(0,'.')
from cat3 import I as I3
from seal2 import seal2
SUB={'Parfémy':[('Dámské','Parfémy dámské'),('Pánské','Parfémy pánské'),('Unisex','Parfémy unisex')],
 'Dekorativní kosmetika':[('Obličej','Make-up obličej'),('Oči','Make-up oči'),('Rty','Make-up rty'),('Nehty','Make-up nehty')],
 'Praní prádla':[(n,n) for n in ['Bílé prádlo','Černé prádlo','Barevné prádlo','Univerzální prací prostředky','Aviváže s kondicionérem','Parfémy na praní','Na skvrny','Jemné prádlo','Speciální prací prostředky','Na záclony','Pro miminka']],
 'Mytí nádobí':[('Ruční mytí','Ruční mytí'),('Mytí v myčce','Mytí v myčce')]}
if __name__=='__main__':
    font='/home/claude/kosmetikaeva-sklad/work/design/fonts/'
    css=f'''@font-face{{font-family:M;font-weight:700;src:url(file://{font}montserrat-700.woff)}}
body{{margin:0;background:#f6f4f4;font-family:M;color:#1c1b29}} .sec{{padding:14px 22px 4px}} h2{{font:700 16px M;margin:0 0 10px;color:#7c1f17}}
.big{{display:grid;grid-template-columns:repeat(6,1fr);gap:12px}} .big div{{background:#fff;border-radius:14px;padding:10px 6px 8px;text-align:center;font:700 12px/1.25 M}} .big svg{{width:150px;height:150px;display:block;margin:0 auto 6px}}
.grid{{display:grid;grid-template-columns:repeat(4,1fr);gap:8px}} .t{{display:flex;align-items:center;gap:12px;background:#fff;border-radius:14px;padding:6px 12px;height:58px}} .t svg{{width:56px;height:56px;flex:0 0 56px}} .t b{{font:700 13px/1.25 M}}'''
    html=f'<html><head><style>{css}</style></head><body>'; k=0
    for sec,items in SUB.items():
        html+=f'<div class="sec"><h2>{sec}</h2><div class="big">'
        for lab,key in items: k+=1; html+=f'<div>{seal2(I3[key],"b"+str(k))}{lab}</div>'
        html+='</div></div>'
    html+='<div class="sec"><h2>Skutečná velikost 56 px</h2><div class="grid">'
    for sec,items in SUB.items():
        for lab,key in items: k+=1; html+=f'<div class="t">{seal2(I3[key],"s"+str(k))}<b>{lab}</b></div>'
    html+='</div></div></body></html>'
    open('sub.html','w').write(html)
    from playwright.sync_api import sync_playwright
    with sync_playwright() as pw:
        b=pw.chromium.launch(); pg=b.new_page(viewport={'width':1100,'height':600},device_scale_factor=1.5); pg.goto('file://'+os.path.abspath('sub.html')); pg.wait_for_timeout(600); pg.screenshot(path=sys.argv[1],full_page=True); b.close()
    print('ok',k)
