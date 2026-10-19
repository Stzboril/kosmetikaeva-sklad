# Pečeť bez textu (název je na webu vedle obrázku): větší kresba, silnější linka – čitelné i v 56 px
import math, re
from lux2 import DEFS
def thick(inner, k=1.5, edge=.55):
    inner = re.sub(r'stroke-width="([\d.]+)"', lambda m: f'stroke-width="{float(m.group(1))*k:.2f}"', inner)
    return inner.replace('" fill="url(#gold)"/>', f'" fill="url(#gold)" stroke="url(#gold)" stroke-width="{edge}" stroke-linejoin="round"/>')
def seal2(inner, uid, scale=.9, k=1.5):
    g=f'url(#gold{uid})'
    def star(x,y,s): return f'<path d="M{x} {y-s}Q{x} {y} {x+s} {y}Q{x} {y} {x} {y+s}Q{x} {y} {x-s} {y}Q{x} {y} {x} {y-s}Z" fill="{g}"/>'
    defs=DEFS.replace('id="bgg"',f'id="bgg{uid}"').replace('id="gold"',f'id="gold{uid}"')
    body=(f'<circle cx="50" cy="50" r="48" fill="url(#bgg{uid})"/>'
          f'<circle cx="50" cy="50" r="46" fill="none" stroke="{g}" stroke-width="1.6"/>'
          f'<circle cx="50" cy="50" r="43.4" fill="none" stroke="{g}" stroke-width=".6"/>'
          f'<g transform="translate(50 50) scale({scale}) translate(-50 -50)">{thick(inner,k).replace("url(#gold)",g).replace("url(#bgg)",f"url(#bgg{uid})")}</g>')
    return f'<svg viewBox="0 0 100 100">{defs}{body}</svg>'
