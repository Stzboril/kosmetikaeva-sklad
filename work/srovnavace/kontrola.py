#!/usr/bin/env python3
"""Kontrola vystup.json:
  1) každá value existuje v moznosti.json (H pro heureka, Z pro zbozi) a není „Odpárováno“,
  2) výstup obsahuje všechny kódy z eshop_kategorie.tsv,
  3) seznam produktů bez kategorie,
  4) tabulka defaultCategory -> nejčastější cesta Heureka / Zboží,
  5) 15 příkladů xmlFeedName.
Navíc zapíše kontrola_detail.tsv (produkt po produktu) pro ruční kontrolu v tabulce.
"""
import json
import os
import random
from collections import Counter, defaultdict

BASE = os.path.dirname(os.path.abspath(__file__))
opt = json.load(open(os.path.join(BASE, 'moznosti.json'), encoding='utf-8'))
out = json.load(open(os.path.join(BASE, 'vystup.json'), encoding='utf-8'))
rows = [l.rstrip('\n').split('\t') for l in open(os.path.join(BASE, 'eshop_kategorie.tsv'), encoding='utf-8') if l.strip()]

cesta = {k: {v: (p.replace(' | ', ' > ') + ' > ' + n).lstrip(' >') for v, n, p in opt[k]} for k in 'HZ'}

# 1) + 2)
chyby = []
for code, *_ in rows:
    if code not in out:
        chyby.append(f'{code}: chybí ve výstupu')
for code, d in out.items():
    for key, k in (('heureka', 'H'), ('zbozi', 'Z')):
        v = d[key]
        if v and (v not in cesta[k] or v == '0'):
            chyby.append(f'{code}: {key}={v} není platná hodnota')
print('== 1) Platnost hodnot:', 'OK – všechny value existují v moznosti.json' if not chyby else f'{len(chyby)} chyb')
for c in chyby:
    print('   ', c)
print(f'== 2) Kódů v TSV: {len(rows)}, ve výstupu: {len(out)}')

# 3)
bez = [(c, cat, name) for c, _, _, cat, name in rows if not out[c]['heureka'] or not out[c]['zbozi']]
print(f'\n== 3) Bez kategorie: {len(bez)} z {len(rows)}  (namapováno {len(rows) - len(bez)})')
for c, cat, name in bez:
    print(f'    {c:<10} {cat:<38} {name}')

# 4)
print('\n== 4) defaultCategory -> nejčastější Heureka / Zboží (počet produktů, počet různých kategorií H/Z)')
byc = defaultdict(list)
for code, _, _, cat, name in rows:
    byc[cat].append(out[code])
for cat in sorted(byc):
    ds = byc[cat]
    hc = Counter(d['heureka'] for d in ds)
    zc = Counter(d['zbozi'] for d in ds)
    hv, zv = hc.most_common(1)[0][0], zc.most_common(1)[0][0]
    print(f'  {cat}  [{len(ds)} ks, H {len(hc)}× / Z {len(zc)}×]')
    print(f'      H: {cesta["H"].get(hv, "—")}')
    print(f'      Z: {cesta["Z"].get(zv, "—")}')

# 5)
xml = [(c, n, out[c]['xmlFeedName']) for c, _, _, _, n in rows if out[c]['xmlFeedName']]
print(f'\n== 5) xmlFeedName vyplněno u {len(xml)} produktů, 15 příkladů:')
random.seed(1)
for c, n, x in random.sample(xml, 15):
    print(f'    {n:<62} -> {x}')

with open(os.path.join(BASE, 'kontrola_detail.tsv'), 'w', encoding='utf-8') as f:
    f.write('code\tpairCode\tmanufacturer\tdefaultCategory\tname\theureka\theureka_cesta\tzbozi\tzbozi_cesta\txmlFeedName\n')
    for code, pair, manu, cat, name in rows:
        d = out[code]
        f.write('\t'.join([code, pair, manu, cat, name, d['heureka'], cesta['H'].get(d['heureka'], ''),
                           d['zbozi'], cesta['Z'].get(d['zbozi'], ''), d['xmlFeedName']]) + '\n')
print('\nDetail produkt po produktu: kontrola_detail.tsv')
