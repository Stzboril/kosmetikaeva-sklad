"""Náhled ikon ve stylu ke-ikony (stejný badge() jako na webu). python3 nahled.py glyfy.json ikony.json out.png [sirka_px]"""
import json, sys, html
from playwright.sync_api import sync_playwright

FONTS = '/home/claude/ke/work/design/fonts/'
GL = json.load(open(sys.argv[1]))
IC = json.load(open(sys.argv[2]))   # seznam [klic, glyf, CZ název, SK název, CZ popisek, SK popisek]
OUT = sys.argv[3]
BIG = int(sys.argv[4]) if len(sys.argv) > 4 else 150
COLS = int(sys.argv[5]) if len(sys.argv) > 5 else 4
COMPACT = len(sys.argv) > 6

DEFS = ('<svg width="0" height="0" style="position:absolute"><defs>'
        '<path id="keik-arc" d="M 18.48 68.2 A 36.4 36.4 0 1 1 81.52 68.2" fill="none"/>'
        '<radialGradient id="keik-base" cx=".35" cy=".28" r=".9"><stop offset="0" stop-color="#fdf2ee"/><stop offset=".55" stop-color="#f3d9d1"/><stop offset="1" stop-color="#e1b6a9"/></radialGradient>'
        '<linearGradient id="keik-raise" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fff"/><stop offset=".5" stop-color="#efd2c9"/><stop offset="1" stop-color="#b47a6a"/></linearGradient>'
        '<linearGradient id="keik-sink" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#b47a6a"/><stop offset=".5" stop-color="#efd2c9"/><stop offset="1" stop-color="#fff"/></linearGradient>'
        '<radialGradient id="keik-disc" cx=".4" cy=".32" r=".75"><stop offset="0" stop-color="#fffaf8"/><stop offset=".6" stop-color="#f8e8e3"/><stop offset="1" stop-color="#ecd0c7"/></radialGradient>'
        '<linearGradient id="keik-gly" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#bb4835"/><stop offset="1" stop-color="#7c1f17"/></linearGradient>'
        '<filter id="keik-bev" x="-20%" y="-20%" width="140%" height="140%" color-interpolation-filters="sRGB">'
        '<feGaussianBlur in="SourceAlpha" stdDeviation=".7" result="b"/>'
        '<feSpecularLighting in="b" surfaceScale="3" specularConstant=".9" specularExponent="18" lighting-color="#fff" result="sp"><feDistantLight azimuth="225" elevation="42"/></feSpecularLighting>'
        '<feComposite in="sp" in2="SourceAlpha" operator="in" result="spi"/>'
        '<feOffset in="SourceAlpha" dx=".35" dy=".6" result="o"/><feGaussianBlur in="o" stdDeviation=".45" result="ob"/>'
        '<feFlood flood-color="#3a0a06" flood-opacity=".4" result="fc"/><feComposite in="fc" in2="ob" operator="in" result="sh"/>'
        '<feMerge><feMergeNode in="sh"/><feMergeNode in="SourceGraphic"/><feMergeNode in="spi"/></feMerge>'
        '</filter></defs></svg>')

def fsz(n):
    return 5.9 if n > 22 else 6.5 if n > 19 else 7.2 if n > 15 else 7.9 if n > 10 else 8.6

def badge(gk, name):
    g = GL[gk]; ring = name.upper()
    ts = 'font-family:Montserrat,system-ui,sans-serif;font-weight:700;font-size:%spx;letter-spacing:.08em;text-anchor:middle;' % fsz(len(ring))
    t = '<textPath href="#keik-arc" startOffset="50%%">%s</textPath>' % html.escape(ring)
    p = lambda d, a: '<path d="%s" %s/>' % (d, a) if d else ''
    return ('<svg viewBox="0 0 100 100">'
            '<circle cx="50" cy="50" r="48" fill="url(#keik-base)"/>'
            '<circle cx="50" cy="50" r="46.6" fill="none" stroke="url(#keik-raise)" stroke-width="2.6"/>'
            '<circle cx="50" cy="50" r="44.9" fill="none" stroke="url(#keik-sink)" stroke-width="1"/>'
            '<g transform="translate(-.35 -.35)"><text style="' + ts + 'fill:#fff;opacity:.95">' + t + '</text></g>'
            '<g transform="translate(.4 .45)"><text style="' + ts + 'fill:#a86a5a;opacity:.55">' + t + '</text></g>'
            '<text style="' + ts + 'fill:#9b3426">' + t + '</text>'
            '<circle cx="42.2" cy="88" r="1.15" fill="url(#keik-raise)"/><circle cx="50" cy="89.6" r="1.4" fill="url(#keik-raise)"/><circle cx="57.8" cy="88" r="1.15" fill="url(#keik-raise)"/>'
            '<circle cx="50" cy="50" r="32.4" fill="none" stroke="url(#keik-sink)" stroke-width="1.2"/>'
            '<circle cx="50" cy="50" r="30.8" fill="url(#keik-disc)"/>'
            '<circle cx="50" cy="50" r="30.8" fill="none" stroke="url(#keik-raise)" stroke-width="1.8"/>'
            '<g transform="translate(30.8 30.8) scale(1.6)" filter="url(#keik-bev)">' +
            p(g.get('f'), 'fill="url(#keik-gly)"') + p(g.get('s'), 'fill="#6a1912"') + p(g.get('h'), 'fill="rgba(255,255,255,.5)"') +
            p(g.get('c'), 'fill="#f8e8e3"') +
            p(g.get('l'), 'fill="none" stroke="#5a140e" stroke-width="1.1" stroke-linecap="round" stroke-linejoin="round"') +
            p(g.get('l2'), 'fill="none" stroke="#f8e8e3" stroke-width=".8" stroke-linecap="round" stroke-linejoin="round"') +
            '</g></svg>')

items = ''.join(
    '<div class="it"><div class="big">%s</div><div class="sm">%s</div><b>%s</b><span>%s</span></div>'
    % (badge(g, cz), badge(g, cz), html.escape(cz), html.escape(tp)) for k, g, cz, sk, tp, tps in IC)
doc = ('<!doctype html><meta charset="utf-8"><style>'
       + ''.join('@font-face{font-family:Montserrat;font-weight:%s;src:url(file://%smontserrat-%s.woff)}' % (w, FONTS, w) for w in (400, 600, 700)) +
       'body{margin:0;background:#fff;font-family:Montserrat;padding:24px}'
       '.g{display:flex;flex-wrap:wrap;gap:22px 26px;width:%dpx}' % (COLS * (BIG + 40) + (COLS - 1) * 26) +
       '.it{width:%dpx;display:flex;flex-direction:column;align-items:center;text-align:center;gap:8px}' % (BIG + 40) +
       '.big{width:%dpx;height:%dpx}.sm{width:80px;height:80px}svg{width:100%%;height:100%%;overflow:visible;filter:drop-shadow(0 3px 5px rgba(94,20,14,.2))}' % (BIG, BIG) +
       'b{font-size:13px;color:#7c1f17}span{font-size:11.5px;color:#6e6c7a;line-height:1.35}' + ('.sm,span{display:none}' if COMPACT else '') +
       '</style>' + DEFS + '<div class="g">' + items + '</div>')
open(OUT + '.html', 'w').write(doc)
with sync_playwright() as pw:
    b = pw.chromium.launch()
    pg = b.new_page(viewport={'width': COLS * (BIG + 40) + (COLS - 1) * 26 + 48, 'height': 400}, device_scale_factor=2)
    pg.goto('file://' + OUT + '.html'); pg.wait_for_timeout(400)
    pg.screenshot(path=OUT, full_page=True)
    b.close()
print('ok', OUT)
