"""Článek Vánoční dárky 2026 (CZ + SK). Živá data výrobků (adresa, obrázek, ceny) v live.json
– načíst z webu těsně před vložením (ceny jsou v textu napevno)."""
import json, html, os, sys
D = os.path.dirname(os.path.abspath(__file__))
L = json.load(open(os.path.join(D, 'live.json'), encoding='utf-8'))
E = html.escape

def cena(p, sk):
    if sk:
        return f"{p['sk']:.2f}".replace('.', ',') + ' €'
    return f"{p['cz']:,}".replace(',', ' ') + ' Kč'

# texty karet: id -> (štítek cs, štítek sk, nadpis cs, nadpis sk, text cs, text sk, balení cs, balení sk)
P = json.load(open(os.path.join(D, 'texty.json'), encoding='utf-8'))

def url(i, sk):
    u = L[i]['url']
    return '/sk' + u if sk else u

def produkt(i, sk):
    t = P[i]; p = L[i]; k = 1 if sk else 0
    u = url(i, sk)
    bal = t['bal'][k]
    return f"""<div class="ke-produkt">
<div class="ke-produkt-foto"><a href="{u}"><img src="{E(p['img'])}" alt="{E(t['nadpis'][k])}" /></a></div>
<div class="ke-produkt-text">
<span class="ke-karta-stitek">{t['stitek'][k]}</span>
<h3><a href="{u}">{t['nadpis'][k]}</a></h3>
<p>{t['text'][k]}</p>
<p><strong>{'Balenie a cena' if sk else 'Balení a cena'}:</strong> {bal} {'za' if not sk else 'za'} {cena(p, sk)}</p>
<p><a class="ke-tlacitko" href="{u}">{'Kúpiť' if sk else 'Koupit'}</a></p>
</div>
</div>"""

def karta(i, sk):
    t = P[i]; p = L[i]; k = 1 if sk else 0
    u = url(i, sk)
    return f'<div class="ke-karta"><span class="ke-karta-stitek">{cena(p, sk)}</span><h3><a href="{u}">{t["nadpis"][k]}</a></h3><p>{t["text"][k]}</p></div>'

def clanek(sk):
    k = 1 if sk else 0
    S = json.load(open(os.path.join(D, 'kostra.json'), encoding='utf-8'))
    out = ['<div class="ke-clanek">', f'<p class="ke-perex">{S["perex"][k]}</p>']
    for sek in S['sekce']:
        out.append(f'<h2>{sek["h2"][k]}</h2>')
        if sek.get('uvod'):
            out.append(f'<p>{sek["uvod"][k]}</p>')
        if sek.get('produkty'):
            out += [produkt(i, sk) for i in sek['produkty'] if i in L and L[i].get('ok')]
        if sek.get('karty'):
            ks = [karta(i, sk) for i in sek['karty'] if i in L and L[i].get('ok')]
            out.append('<div class="ke-mrizka">\n' + '\n'.join(ks) + '\n</div>')
        if sek.get('pozn'):
            out.append(f'<p class="ke-pozn">{sek["pozn"][k]}</p>')
        if sek.get('tlacitko'):
            u, tx = sek['tlacitko'][k]
            out.append(f'<p class="ke-tlacitko-obal"><a class="ke-tlacitko" href="{u}">{tx}</a></p>')
    for b in S['boxy']:
        out.append(f'<div class="ke-box"><span class="ke-box-titulek">{b["t"][k]}</span><p>{b["p"][k]}</p></div>')
    out.append('</div>')
    return '\n'.join(out)

for sk, name in ((False, 'vanoce_cs.html'), (True, 'vanoce_sk.html')):
    open(os.path.join(D, name), 'w', encoding='utf-8').write(clanek(sk))
print('ok')
