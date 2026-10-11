import json, glob, re, sys, csv, io
sys.path.insert(0, '/home/claude/work/box'); sys.path.insert(0, '/home/claude/work/insp')
from zamena_box import insert
cur = json.load(open('/home/claude/work/cs_current.json'))
cleaned = set(json.load(open('/home/claude/work/insp/cleaned_codes.json')))
zmap = json.load(open('/home/claude/work/box/zam_map.json'))
sk = {}
for f in glob.glob('/home/claude/work/sk/out/sk_*.json'):
    sk.update(json.load(open(f)))
units = {}
for f in glob.glob('/home/claude/work/sk/batches/sk_*.json'):
    for it in json.load(open(f)):
        units[it['key']] = (it['codes'], 'description' in it)

def write(name, header, rows):
    buf = io.StringIO()
    w = csv.writer(buf, delimiter=';', quoting=csv.QUOTE_ALL, lineterminator='\r\n')
    w.writerow(header); w.writerows(rows)
    open(f'/home/claude/work/import/{name}', 'w', encoding='utf-8-sig', newline='').write(buf.getvalue())
    print(name, len(rows), 'řádků', len(buf.getvalue()) // 1024, 'kB')

# A) CZ – Essens: vyčištěné texty a box „zaměňují za“
rowsA = []
for c, r in sorted(cur.items()):
    if r['man'] != 'Essens': continue
    z = zmap.get(c)
    if c not in cleaned and not z: continue
    desc = insert(r['description'], z, 'cs') if z else r['description']
    rowsA.append([c, r['pairCode'], r['name'], desc, r['metaDescription'], r['seoTitle']])
write('A_cz_essens.csv', ['code', 'pairCode', 'name', 'description', 'metaDescription', 'seoTitle'], rowsA)

# B) SK – plný překlad (+ box u parfémů Essens)
rowsB, hotove = [], set()
for key, (codes, full) in units.items():
    if not full: continue
    o = sk[key]
    for c in codes:
        z = zmap.get(c)
        desc = insert(o['description'], z, 'sk') if z else o['description']
        rowsB.append([c, cur[c]['pairCode'], o['name'], desc, o['metaDescription'], o['seoTitle']])
        hotove.add(c)
# parfémy Essens s boxem, jejichž SK text byl v pořádku (nepřekládal se) – jen doplnit box
for c, z in zmap.items():
    if z and c not in hotove:
        s = cur[c]['sk']
        rowsB.append([c, cur[c]['pairCode'], s['name'], insert(s['description'], z, 'sk'), s['metaDescription'], s['seoTitle']])
        hotove.add(c)
rowsB.sort()
write('B_sk_texty.csv', ['code', 'pairCode', 'name:sk', 'description:sk', 'metaDescription:sk', 'seoTitle:sk'], rowsB)

# C) SK – jen název, meta a SEO titulek
rowsC = []
for key, (codes, full) in units.items():
    if full: continue
    o = sk[key]
    for c in codes:
        if c in hotove: continue
        rowsC.append([c, cur[c]['pairCode'], o['name'], o['metaDescription'], o['seoTitle']])
rowsC.sort()
write('C_sk_nazvy_meta.csv', ['code', 'pairCode', 'name:sk', 'metaDescription:sk', 'seoTitle:sk'], rowsC)

# kontroly
CZ = re.compile('[řůěŘŮĚ]')
def txt(h): return re.sub(r'<[^>]+>', ' ', (h or '').replace('Hrabůvka', 'X'))
bad = [r[0] for r in rowsB + rowsC if any(CZ.search(txt(x)) for x in r[2:])]
print('SK s českými písmeny:', bad[:10])
print('boxy CZ:', sum(1 for r in rowsA if 'zamena-vune' in r[3]), ' boxy SK:', sum(1 for r in rowsB if 'zamena-vune' in r[3]))
print('dvojité boxy:', [r[0] for r in rowsA + rowsB if r[3].count('zamena-vune') > 1])
from znacky import BR
print('CZ se značkou:', [r[0] for r in rowsA if BR.search(txt(r[3]) + txt(r[4]) + txt(r[5]) + txt(r[2]))][:10])
print('SK se značkou:', [r[0] for r in rowsB + rowsC if BR.search(' '.join(txt(x) for x in r[2:])) and cur[r[0]]['man'] == 'Essens'][:10])
