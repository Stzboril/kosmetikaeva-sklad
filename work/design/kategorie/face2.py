import sys, os
sys.path.insert(0,'.')
from lux2 import DEFS, FRAME, spark
from taper import brush
def face():
    s=''
    B=lambda d,w=1.7,**k: brush(d,w,**k)
    # vlasy – plné, vlnité, sčesané dozadu
    s+=B('M57.4 23.4C54 18.6 45 16.4 37.6 19.6C30 23 27.4 32 29.8 41.6C31.8 49.4 36 55 34.8 63C34 68.4 30.6 72.6 27 76.6',2.1)
    s+=B('M57.4 23.4C52.2 25.6 49.4 30.6 50.4 36.4C51.2 41.2 50.6 45 48.6 48.2',1.5)
    s+=B('M55.2 21C47.6 20.4 40 24.4 37.4 31.8C35 38.8 38.4 45 39.4 51.6C40.4 58.4 38.4 64.4 34.6 70',1.15)
    s+=B('M52 24.6C45.6 26.4 42.2 31.4 42.4 37.8C42.6 44 45.4 48.6 44.8 55C44.2 60.6 41.6 64.8 38.6 68.4',1.0)
    s+=B('M48.6 29.4C46.2 33.6 46.4 38.4 47.8 43',.8)
    s+=B('M41.4 20.6C35.4 23.4 32.4 29.6 33.2 36.8C34 43.6 37.6 48.6 37.4 55.4C37.2 60.4 35.4 64.6 32.6 68.4',.9)
    # profil
    s+=B('M56.8 23.2C61.2 25.6 63.8 30 63.6 35.6C63.5 37.4 63 38.6 63.2 39.8C64.6 42.4 67.6 45.4 69.2 47.4C69.6 48.2 68.6 49.2 66.6 49.4C65.6 49.6 65.4 50.6 65.8 51.4C66.6 52.2 67.8 52.8 67.6 53.6C67.4 54.4 66 54.6 65.8 55C66.6 55.6 67.4 56.4 67 57.4C66.6 58.4 65 58.6 64.6 59.6C64.4 60.8 65.8 61.6 65.8 63C65.8 64.8 64 66.6 61.6 67C60 67.4 59 68.4 58.8 70.6C58.6 74 59.2 78 60.4 82.4',1.7,start=.04,end=.12)
    s+=B('M61.8 66.8C57.8 66.6 54 64.8 51.6 61.6',1.1)
    s+=B('M47.2 64.6C47 70 46.4 76 44.8 82.4',1.3)
    s+=B('M58.8 80.6C61.8 81.4 64.8 82.6 67.6 84.6',1.0)
    s+=B('M44.8 82.4C41 83.8 37.4 85 34 86.6',1.0)
    # oko, řasy, obočí
    s+=B('M56.4 41.6C57.8 43 60 43.4 61.6 42.6',1.3)
    s+=B('M57.4 42.6C57.1 43.4 56.8 44 56.2 44.6',.7,start=.0)+B('M58.8 43.1C58.8 43.9 58.7 44.6 58.4 45.2',.7,start=.0)+B('M60.2 43.1C60.4 43.8 60.6 44.4 60.9 45',.7,start=.0)
    s+=B('M54.8 37.6C56.8 36.2 59.6 35.8 62 36.6',1.2)
    # rty
    s+='<path d="M65.8 51.6C66.8 52.2 67.8 52.8 67.6 53.6C67.4 54.4 66.2 54.8 64.4 54.8C64.6 53.6 65.2 52.4 65.8 51.6Z" fill="url(#gold)"/>'
    s+='<path d="M64.4 55.2C66 55 67.2 55.8 67 57C66.8 58 65.6 58.6 64.6 58.6C64.8 57.6 64.6 56.2 64.4 55.2Z" fill="url(#gold)" opacity=".8"/>'
    # náušnice
    s+=B('M49.8 49.8C49.9 50.8 49.9 51.6 49.8 52.4',.6,start=0,end=0)+'<circle cx="49.8" cy="53.8" r="1.5" fill="url(#gold)"/>'
    s+=spark(74,30,2.6)+spark(79,42,1.4)+spark(24,52,1.6)
    return s
if __name__=='__main__':
    html=f'''<html><body style="margin:0;background:#fff;display:flex;gap:30px;align-items:center;padding:24px">
<svg viewBox="0 0 100 100" width="360" height="360">{DEFS}{FRAME}{face()}</svg>
<svg viewBox="0 0 100 100" width="86" height="86">{DEFS.replace('id="bgg"','id="b3"').replace('id="gold"','id="g3"')}{(FRAME+face()).replace('url(#bgg)','url(#b3)').replace('url(#gold)','url(#g3)')}</svg></body></html>'''
    open('face2.html','w').write(html)
    from playwright.sync_api import sync_playwright
    with sync_playwright() as pw:
        b=pw.chromium.launch(); pg=b.new_page(viewport={'width':560,'height':420}); pg.goto('file://'+os.path.abspath('face2.html')); pg.wait_for_timeout(300); pg.screenshot(path=sys.argv[1]); b.close()
    print('ok')
