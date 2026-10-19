import sys, os
sys.path.insert(0,'.')
from lux2 import DEFS, FRAME, spark
from taper import brush
from face4 import mx
def face(uid='a'):
    B=lambda d,w=1.6,**k: brush(d,w,**k)
    s=''
    # vlasy – vlny po obou stranách
    s+=B('M47 20.6C60 17 72 25 71.6 39C71.2 50 75.8 56 77 63C78.2 70 74.8 75.8 69 78.4',2.1)
    s+=B('M47 20.6C36 19.6 28.6 27.6 29.4 39.6C30 48.6 27.4 55.6 25.4 62C23.8 67.4 25 72 28.6 75.6',2.0)
    s+=B('M48.8 21.6C58.6 22 64.6 29.4 64.6 38.4C64.6 46 67.6 52.6 69 59.4C70.2 65 68.6 69.8 65.4 72.8',1.15)
    s+=B('M53.6 21C62.4 22.4 68 29.6 68 38.6C68 46.6 71.4 52.6 72.6 58.8',.75)
    s+=B('M45.4 21.8C38.4 23.4 35 30.4 35.4 37.6C35.8 44 33.8 50.6 31.2 56.6',1.0)
    s+=B('M41.8 21.6C35 24 31.8 30.6 32.4 38.6',.6)
    # obličej – jen levá líce a brada, krk
    s+=B('M36.4 43C36.6 50.6 39.4 57.4 44.4 62.6C46.4 64.6 48.4 65.8 50.6 66',1.3,start=.12,end=.25)
    s+=B('M44.6 63.8C45 68.6 44.4 73 42.6 77.4',1.0)+B('M57 62.8C56.8 66.8 57.2 70.6 58.4 74.6',.7)
    s+=B('M42.6 77.4C38.8 79 35 80 31.4 81',.8)
    # obočí
    br='M39 41.4C41.2 39.4 44.4 38.8 46.8 39.8'
    s+=B(br,1.0,start=.12,end=.5)+B(mx(br),1.0,start=.12,end=.5)
    # zavřené oči s dlouhými řasami
    ey='M39.6 46.4C41.6 48.4 44.6 48.6 46.8 46.6'
    s+=B(ey,1.35,start=.2,end=.2)+B(mx(ey),1.35,start=.2,end=.2)
    lashes=['M40.8 47.4C40.2 48.2 39.6 48.8 38.8 49.3','M42.5 48.1C42.2 49 41.9 49.7 41.4 50.4','M44.3 48.2C44.3 49.1 44.3 49.8 44.1 50.6','M45.9 47.6C46.2 48.4 46.5 49 47 49.6']
    for l in lashes: s+=B(l,.55,start=0,end=.6)+B(mx(l),.55,start=0,end=.6)
    # nos
    s+=B('M51.2 48.6C51.6 51.4 52.6 53.4 53 54.4C52 55.2 50.8 55.4 49.6 55',.75)
    # rty
    s+='<path d="M45.6 58.8C47.2 57.4 48.8 57 50.1 58C51.4 57 53 57.4 54.6 58.8C52.6 59.6 47.6 59.6 45.6 58.8Z" fill="url(#gold)"/>'
    s+='<path d="M46 59.3C47.8 62.2 52.4 62.2 54.2 59.3C52.2 60.1 48 60.1 46 59.3Z" fill="url(#gold)" opacity=".8"/>'
    # řetízek
    s+=B('M45.2 71.4C48 74 52.2 73.8 55.6 71',.5,start=0,end=0)+'<path d="M50.3 73.4c.8 1.1 1.4 1.8 1.4 2.6a1.4 1.4 0 0 1-2.8 0c0-.8.6-1.5 1.4-2.6z" fill="url(#gold)"/>'
    return s
if __name__=='__main__':
    html=f'''<html><body style="margin:0;background:#fff;display:flex;gap:30px;align-items:center;padding:24px">
<svg viewBox="0 0 100 100" width="360" height="360">{DEFS}{FRAME}{face('a')}</svg>
<svg viewBox="0 0 100 100" width="86" height="86">{DEFS.replace('id="bgg"','id="b3"').replace('id="gold"','id="g3"')}{(FRAME+face('b')).replace('url(#bgg)','url(#b3)').replace('url(#gold)','url(#g3)')}</svg></body></html>'''
    open('face5.html','w').write(html)
    from playwright.sync_api import sync_playwright
    with sync_playwright() as pw:
        b=pw.chromium.launch(); pg=b.new_page(viewport={'width':560,'height':420}); pg.goto('file://'+os.path.abspath('face5.html')); pg.wait_for_timeout(300); pg.screenshot(path=sys.argv[1]); b.close()
    print('ok')
