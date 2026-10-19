import sys, os
sys.path.insert(0,'.')
from lux2 import DEFS, FRAME, spark
from taper import brush
def mx(d):
    import re
    nums=re.findall(r'-?\d*\.?\d+',d); cmds=re.findall(r'[A-Za-z]',d)
    # jen absolutní M a C: zrcadlení x -> 100-x
    out='';i=0
    vals=[float(n) for n in nums]
    toks=re.findall(r'[MC]|-?\d*\.?\d+',d); res=[];xturn=True
    for t in toks:
        if t in 'MC': res.append(t); xturn=True; continue
        v=float(t)
        if xturn: v=100-v
        res.append(f'{v:.2f}'); xturn=not xturn
    o=''
    for t in res: o+= t if t in 'MC' else ' '+t
    return o.replace('M ','M').replace('C ','C')
def face(uid='a'):
    B=lambda d,w=1.6,**k: brush(d,w,**k)
    s=''
    # vlasy
    s+=B('M46 21.4C35 20 26.6 28 27.4 40C28 49 25.6 56 23 63C21.4 68 22.6 73 26 77',2.0)
    s+=B('M46 21.4C59 17.4 71.6 24.4 72.2 38C72.6 47 74.4 53 76.6 59.6C78.4 65.4 77 71 73.2 75.4',2.0)
    s+=B('M45.6 22.4C52 24 57.6 28 61 33.4C63.6 37.6 64.6 42.4 64.8 47C65 52 66.6 56.6 67.2 61.6',1.4)
    s+=B('M45 22.6C39.4 25.8 36.4 31.4 36 38C35.8 42 35.6 44.6 35.4 46',1.2)
    s+=B('M49.4 20.4C61 20.6 67.4 28.4 68.2 38C68.8 45 69.6 51 72 57C73.6 61.4 73.4 66.4 70.8 70.4',.9)
    s+=B('M55 21.6C62.6 25 66 31 66.6 38.4',.7)
    s+=B('M41 21.4C33.8 24.6 31 31.4 31.4 39C31.8 46 29.8 52.6 27.4 58.6',.85)
    s+=B('M37.2 23.8C33 28 31.6 33 32.2 38',.6)
    # obličej, krk, ramena
    s+=B('M35.4 45C35.2 53 37.6 59.4 42 64.6C44.6 67.8 47.4 69.6 50 69.8',1.45,start=.05)
    s+=B('M50 69.8C52.6 69.6 55.4 67.8 58 64.6C61.6 60.2 63.6 54.6 64 48.6',1.1,end=.35)
    s+=B('M44.4 67C44.8 71.4 44.2 75.4 42.8 79.4',1.0)+B('M55.6 67C55.2 71.4 55.8 75.4 57.2 79.4',1.0)
    s+=B('M42.8 79.4C39 81 35.2 82 31.4 83',.85)+B('M57.2 79.4C61 81 64.8 82 68.6 83',.85)
    # obočí
    L_brow='M37.2 41.8C39.6 39.2 43.8 38.2 47.4 39.4'
    s+=B(L_brow,1.15,start=.1,end=.45)+B(mx(L_brow),1.15,start=.1,end=.45)
    # oči: mandlový tvar, duhovka schovaná pod víčkem, linka s křidélkem
    up='M38 47.4C40 44.6 44.6 43.8 48 46.2'; lo='M48 46.2C46.6 48.6 44.2 49.6 41.8 49.4C40.2 49.2 38.8 48.4 38 47.4'
    def eye(u,l,iris,k):
        cid=f'ey{k}{uid}'
        return (f'<clipPath id="{cid}"><path d="{u}{l[l.index("C"):]}Z"/></clipPath>'
                f'<g clip-path="url(#{cid})"><circle cx="{iris[0]}" cy="{iris[1]}" r="2.35" fill="url(#gold)"/><circle cx="{iris[0]+.7}" cy="{iris[1]-.7}" r=".55" fill="#fbf6ec"/></g>'
                +B(u,1.7,start=.18,end=.1)+B(l,.45,start=.2,end=.2))
    s+=eye(up,lo,(43.4,47.6),'l')
    upr=mx(up); lor=mx(lo)
    s+=eye(upr,lor,(56.6,47.6),'r')
    s+=B('M38.4 47.1C37.2 46.7 36.2 46 35.4 45.1',.95,start=0)+B(mx('M38.4 47.1C37.2 46.7 36.2 46 35.4 45.1'),.95,start=0)
    # nos
    s+=B('M51.2 50.6C51.6 53 52.4 54.6 52.8 55.4',.7)+B('M48.6 56C49.4 56.6 50.6 56.6 51.6 56',.7,start=.2,end=.2)
    # rty
    s+='<path d="M44.8 61C46.6 59.2 48.6 58.8 50 59.9C51.4 58.8 53.4 59.2 55.2 61C53 61.8 47 61.8 44.8 61Z" fill="url(#gold)"/>'
    s+='<path d="M45.4 61.5C47.4 64.6 52.6 64.6 54.6 61.5C52.4 62.4 47.6 62.4 45.4 61.5Z" fill="url(#gold)" opacity=".8"/>'
    s+='<path d="M48.4 62.9C49.4 63.3 50.8 63.3 51.8 62.9" stroke="#fbf6ec" stroke-width=".5" fill="none" stroke-linecap="round" opacity=".8"/>'
    # řetízek
    s+=B('M45.4 74.4C48.2 77.2 52 77.2 54.8 74.2',.5,start=0,end=0)+'<path d="M50.2 76.8c.8 1.1 1.4 1.8 1.4 2.6a1.4 1.4 0 0 1-2.8 0c0-.8.6-1.5 1.4-2.6z" fill="url(#gold)"/>'
    return s
if __name__=='__main__':
    html=f'''<html><body style="margin:0;background:#fff;display:flex;gap:30px;align-items:center;padding:24px">
<svg viewBox="0 0 100 100" width="360" height="360">{DEFS}{FRAME}{face('a')}</svg>
<svg viewBox="0 0 100 100" width="86" height="86">{DEFS.replace('id="bgg"','id="b3"').replace('id="gold"','id="g3"')}{(FRAME+face('b')).replace('url(#bgg)','url(#b3)').replace('url(#gold)','url(#g3)')}</svg></body></html>'''
    open('face4.html','w').write(html)
    from playwright.sync_api import sync_playwright
    with sync_playwright() as pw:
        b=pw.chromium.launch(); pg=b.new_page(viewport={'width':560,'height':420}); pg.goto('file://'+os.path.abspath('face4.html')); pg.wait_for_timeout(300); pg.screenshot(path=sys.argv[1]); b.close()
    print('ok')
