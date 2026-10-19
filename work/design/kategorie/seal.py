# Rámeček „pečeť“: název kategorie dole v mezikruží, kresba uvnitř
import math
from lux2 import DEFS
def arc_bottom(r, a1=168, a2=12, cx=50, cy=50):
    p=lambda a:(cx+r*math.cos(math.radians(a)), cy+r*math.sin(math.radians(a)))
    x1,y1=p(a1); x2,y2=p(a2)
    return f'M{x1:.2f} {y1:.2f}A{r} {r} 0 0 0 {x2:.2f} {y2:.2f}'
def fsz(n): return 6.4 if n<=12 else 5.8 if n<=16 else 5.2 if n<=20 else 4.6 if n<=25 else 4.1
def seal(label, inner, uid):
    t=label.upper(); fs=fsz(len(t))
    span = 168 if len(t)<=20 else 186
    a1=90+span/2; a2=90-span/2
    base=40.4+fs*.36
    arc=arc_bottom(base,a1,a2)
    g=f'url(#gold{uid})'
    def star(x,y,s): return f'<path d="M{x} {y-s}Q{x} {y} {x+s} {y}Q{x} {y} {x} {y+s}Q{x} {y} {x-s} {y}Q{x} {y} {x} {y-s}Z" fill="{g}"/>'
    top=star(50,9.6,2.2)+''.join(f'<circle cx="{50+40.3*math.cos(math.radians(a)):.2f}" cy="{50+40.3*math.sin(math.radians(a)):.2f}" r=".75" fill="{g}"/>' for a in (-120,-60))
    defs=DEFS.replace('id="bgg"',f'id="bgg{uid}"').replace('id="gold"',f'id="gold{uid}"')
    body=(f'<circle cx="50" cy="50" r="48" fill="url(#bgg{uid})"/>'
          f'<circle cx="50" cy="50" r="46.2" fill="none" stroke="{g}" stroke-width=".9"/><circle cx="50" cy="50" r="45.1" fill="none" stroke="{g}" stroke-width=".3"/>'
          f'<circle cx="50" cy="50" r="35.6" fill="none" stroke="{g}" stroke-width=".9"/><circle cx="50" cy="50" r="34.5" fill="none" stroke="{g}" stroke-width=".3"/>'
          f'<path id="arc{uid}" d="{arc}" fill="none"/>'
          f'<text style="font-family:Montserrat,sans-serif;font-weight:700;font-size:{fs}px;letter-spacing:.14em" fill="{g}" text-anchor="middle"><textPath href="#arc{uid}" startOffset="50%">{t}</textPath></text>'
          + top +
          f'<g transform="translate(50 50) scale(.72) translate(-50 -50)">{inner.replace("url(#gold)",g).replace("url(#bgg)",f"url(#bgg{uid})")}</g>')
    return f'<svg viewBox="0 0 100 100">{defs}{body}</svg>'
