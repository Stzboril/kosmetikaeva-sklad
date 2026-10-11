import json, re, sys
vstup = json.load(open(sys.argv[1]))
out = json.load(open(sys.argv[2]))
CZ = re.compile('[řůěŘŮĚ]')
def tagy(h):
    t = re.findall(r'<[^>]+>', h or '')
    return [re.sub(r'\s(alt|title)="[^"]*"', '', x) for x in t]
def txt(h): return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', h or '')).strip()
def slozeni(h):
    m = re.search(r'<summary>[^<]*(Složení|Zloženie|INCI|Ingredients)[^<]*</summary>(.*?)</details>', h or '', re.S | re.I)
    return txt(m.group(2)) if m else None
chyby = []
for it in vstup:
    k = it['key']; o = out.get(k)
    if not o: chyby.append(f'{k}: chybí'); continue
    for f in ('name', 'metaDescription', 'seoTitle') + (('description',) if 'description' in it else ()):
        if f not in o: chyby.append(f'{k}: chybí {f}'); continue
        if CZ.search(txt(o[f])): chyby.append(f'{k}: {f} obsahuje české ř/ů/ě: „{CZ.search(txt(o[f])).group(0)}“ v „{txt(o[f])[max(0,CZ.search(txt(o[f])).start()-30):CZ.search(txt(o[f])).start()+30]}“')
    if not o.get('seoTitle', '').endswith('| KosmetikaEva.eu'): chyby.append(f'{k}: seoTitle nekončí „| KosmetikaEva.eu“')
    if 'description' in it and 'description' in o:
        a, b = tagy(it['description']), tagy(o['description'])
        if a != b:
            i = next((j for j in range(min(len(a), len(b))) if a[j] != b[j]), min(len(a), len(b)))
            chyby.append(f'{k}: HTML se liší (značka č. {i}: {a[i] if i < len(a) else "-"} vs {b[i] if i < len(b) else "-"})')
        s1 = slozeni(it['description'])
        if s1 and not re.search('[ěščřžýáíéůúňťď]', s1, re.I):  # INCI v latině -> musí být doslova
            if slozeni(o['description']) != s1: chyby.append(f'{k}: INCI se změnilo (má zůstat doslova)')
        la, lb = len(txt(it['description'])), len(txt(o['description']))
        if la > 200 and not (0.8 * la <= lb <= 1.3 * la): chyby.append(f'{k}: délka popisu nesedí ({lb} vs {la})')
print('\n'.join(chyby) if chyby else 'OK')
