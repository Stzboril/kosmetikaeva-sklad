import json, re, sys
BR = re.compile(r"inspir|\bDior\b|Chanel|Lanc[oô]me|Guerlain|Givenchy|Yves Saint|\bYSL\b|Armani|Versace|Gucci|\bPrada\b|Rabanne|Hugo Boss|Calvin Klein|Dolce|Gabbana|Herrera|Mugler|Gaultier|Tom Ford|\bCreed\b|Kurkdjian|Byredo|Le Labo|Jo Malone|Viktor|Narciso|Bvlgari|\bBulgari\b|Cartier|Herm[eè]s|Kenzo|Marc Jacobs|Burberry|Valentino|Nina Ricci|Azzaro|Montale|Mancera|Kilian|Initio|Parfums de Marly|Xerjoff|Ariana Grande|Victoria'?s Secret|Escentric|Dsquared|Moschino|Jimmy Choo|Montblanc|Davidoff|Lacoste|Diesel|Chlo[ée]|Cacharel|Est[ée]e Lauder|Elizabeth Arden|Lalique|Rochas|Balenciaga|Ralph Lauren|Bottega|Fendi|Loewe|Amouage|Nishane|Louis Vuitton|Ferragamo|\bDKNY\b|Donna Karan|Escada|Michael Kors|Lanvin|Diptyque|Maison Margiela|Comme des|Sauvage|Kayali|Juliette Has a Gun|Molecule", re.I)
vstup = {x['code']: x for x in json.load(open(sys.argv[1]))}
out = json.load(open(sys.argv[2]))
chyby = []
def txt(h): return re.sub(r'<[^>]+>', ' ', h or '')
def slozeni(h):
    m = re.search(r'<summary>[^<]*(Složení|INCI|Ingredients)[^<]*</summary>(.*?)</details>', h or '', re.S | re.I)
    return re.sub(r'\s+', ' ', m.group(2)).strip() if m else None
for c, x in vstup.items():
    o = out.get(c)
    if not o: chyby.append(f'{c}: chybí ve výstupu'); continue
    for f in ('name', 'description', 'metaDescription', 'seoTitle'):
        if f not in o: chyby.append(f'{c}: chybí pole {f}'); continue
        m = BR.search(txt(o[f]))
        if m: chyby.append(f'{c}: {f} pořád obsahuje „{m.group(0)}“')
    if slozeni(x['description']) != slozeni(o.get('description', '')):
        chyby.append(f'{c}: změnilo se Složení/INCI')
    a, b = len(txt(x['description'])), len(txt(o.get('description', '')))
    if b < a * 0.6: chyby.append(f'{c}: popis je výrazně kratší ({b} vs {a} znaků)')
    if o.get('description', '').count('<details') != x['description'].count('<details'):
        chyby.append(f'{c}: změnil se počet rozbalovacích sekcí <details>')
print('\n'.join(chyby) if chyby else 'OK')
