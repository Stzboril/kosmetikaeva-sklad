import sys
sys.path.insert(0,'.')
from lux2 import DEFS, FRAME, M, D, O, spark, leaf
L='fill="none" stroke="url(#gold)" stroke-width="1.05" stroke-linecap="round" stroke-linejoin="round"'
def face(v=1):
    s='<g transform="rotate(-7 50 52)">' if v else '<g>'
    # vlasy – pěšinka vlevo, objem a vlny vpravo
    s+=f'<path d="M44 22C36 23 30.6 31 31.2 41C31.8 49 28.4 54 28.6 61C28.8 67 25 71 25.8 76.4" {M}/>'
    s+=f'<path d="M44 22C56 18.4 69 24 69.4 37C69.8 46 66.8 51 69.2 58C71.4 64.6 76 68 74.6 75C73.6 80 69 82.2 63.8 81.6" {M}/>'
    s+=f'<path d="M44 22.4C39.4 26 37 31.6 37.2 38" {L}/>'
    s+=f'<path d="M44.4 22.6C52 23 58.6 26.8 61.4 33.4C63.4 38.4 62.6 44 62.8 49C63 55 65.4 60 64.2 66.4C63.6 70 61.6 72.6 59.4 74" {L}/>'
    s+=f'<path d="M50 21.4C60 21.6 66 28 65.8 37C65.6 45 63.8 51 66.6 58.4C68.6 64 71.8 68.6 70.2 74.6C69.4 77.6 67.6 79.4 65.4 80.4" {D}/>'
    s+=f'<path d="M56 22.4C64 25 67.6 31 67.4 39.4C67.2 45 66.4 49.4 67.8 54" {D}/>'
    s+=f'<path d="M41 23.6C35.6 28 33.6 34.8 34.2 42.4C34.8 49.6 31.6 54.4 31.8 60.4C32 64.6 30.4 67.6 29 70" {D}/>'
    # obličej, krk, ramena, náhrdelník
    s+=f'<path d="M37.2 38C36 46.6 36.8 55 40.8 62C43.6 67 47 69.6 50.4 69.8C53.6 69.6 56.6 67.6 59 64C60.4 62 61.4 59.8 62.2 57.4" {L}/>'
    s+=f'<path d="M44.2 68.2C44.6 72.8 44 77.2 42.4 81.2 M56.4 67.4C56.2 72 56.8 76.2 58.6 80" {D}/>'
    s+=f'<path d="M42.4 81.2C38.8 82.8 35.4 83.8 32.2 84.6 M58.6 80C61 81.2 63.2 82 65 82.4" {D}/>'
    s+=f'<path d="M44.6 76.4C47.4 79.6 53.4 79.6 56.4 76" {D}/><path d="M50.4 79.2c.9 1.2 1.5 2 1.5 2.8a1.5 1.5 0 0 1-3 0c0-.8.6-1.6 1.5-2.8z" fill="url(#gold)"/>'
    # obočí, zavřené oči s řasami
    s+=f'<path d="M40.4 43C42.6 41 45.6 40.6 47.8 41.6 M52.4 41.6C54.6 40.6 57.6 41 59.6 43" {L}/>'
    s+=f'<path d="M41.2 48C43 49.8 45.8 50 47.4 48.4 M52.6 48.4C54.2 50 57 49.8 58.8 48" {L}/>'
    s+=f'<path d="M42.2 48.9l-.9 1.6 M44 49.5l-.4 1.8 M45.9 49.5l.2 1.7 M57.8 48.9l.9 1.6 M56 49.5l.4 1.8 M54.1 49.5l-.2 1.7" {D}/>'
    # nos
    s+=f'<path d="M50.4 46C50.2 50.2 49.4 53 48.4 55C49.2 56.2 50.8 56.4 52.2 55.6" {D}/>'
    # rty
    s+='<path d="M45.4 60.2C46.8 58.6 48.6 58.2 50 59.2C51.4 58.2 53.2 58.6 54.6 60.2C52.6 60.8 47.4 60.8 45.4 60.2Z" fill="url(#gold)"/>'
    s+='<path d="M45.8 60.6C47.6 63.4 52.4 63.4 54.2 60.6C52.4 61.4 47.6 61.4 45.8 60.6Z" fill="url(#gold)" opacity=".75"/>'
    s+='</g>'+spark(25,32,2.4)+spark(78,40,1.5)
    return s
if __name__=='__main__':
    html=f'''<html><body style="margin:0;background:#fff;display:flex;gap:30px;align-items:center;padding:24px">
    <svg viewBox="0 0 100 100" width="340" height="340">{DEFS}{FRAME}{face(1)}</svg>
    <svg viewBox="0 0 100 100" width="340" height="340">{DEFS.replace('id="bgg"','id="b2"').replace('id="gold"','id="g2"')}{(FRAME+face(0)).replace('url(#bgg)','url(#b2)').replace('url(#gold)','url(#g2)')}</svg>
    <svg viewBox="0 0 100 100" width="86" height="86">{DEFS.replace('id="bgg"','id="b3"').replace('id="gold"','id="g3"')}{(FRAME+face(1)).replace('url(#bgg)','url(#b3)').replace('url(#gold)','url(#g3)')}</svg>
    </body></html>'''
    open('face.html','w').write(html)
    import os
    from playwright.sync_api import sync_playwright
    with sync_playwright() as pw:
        b=pw.chromium.launch(); pg=b.new_page(viewport={'width':900,'height':400}); pg.goto('file://'+os.path.abspath('face.html')); pg.wait_for_timeout(300); pg.screenshot(path=sys.argv[1]); b.close()
    print('ok')
