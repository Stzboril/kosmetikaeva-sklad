import json, re, csv, io, sys
sys.path.insert(0, '/home/claude/work/navod')
from navody2 import N
BEZ = {}

kand = {x['code']: x for x in json.load(open('/home/claude/work/navod/kandidati.json'))}
cs_utf8 = json.load(open('/home/claude/work/navod/cs_utf8.json'))

# znaky, které CSV export (windows-1250) poškodil – vrátit podle UTF-8 (XML) verze
SK_OPRAVY = [('>Acqua di Gio<', '>Acqua di Giò<'), ('>Si</strong>', '>Sì</strong>'),
             ("d'Arpege<", "d'Arpège<"), ('549\xa041', '549 41')]

TAIL = {
    'cs': re.compile(r'^(Složení(?! vůně)|Upozornění|Skladování|Péče|Nutriční|Výživové)', re.I),
    'sk': re.compile(r'^(Zloženie(?! vône)|Zložky|Upozornenie|Skladovanie|Starostlivosť|Nutričné|Výživové)', re.I),
}
USE = re.compile(r'Použit|Aplikac|Aplikác|dávkov|Návod|Příprava|Príprava|podávat|podávať', re.I)


def vloz(html, title, body, lang):
    summaries = re.findall(r'<summary>(.*?)</summary>', html, re.S)
    if any(USE.search(re.sub('<[^>]+>', '', s)) for s in summaries):
        raise ValueError('už obsahuje návod')
    sp = ' ' if '<details> <summary>' in html else ''
    blok = f'<details>{sp}<summary>{title}</summary>\n{body}\n</details>{sp}'
    # 1) před první „koncovou“ sekci (složení, upozornění…)
    for m in re.finditer(r'<details>\s*<summary>(.*?)</summary>', html, re.S):
        if TAIL[lang].search(re.sub('<[^>]+>', '', m.group(1)).strip()):
            return html[:m.start()] + blok + html[m.start():]
    # 2) na konec kontejneru sekcí
    i = html.rfind('</details></div>')
    if i >= 0:
        i += len('</details>')
        return html[:i] + (' ' if sp else '') + blok.rstrip() + html[i:]
    # 3) bez kontejneru – nový blok před množství / objem / výrobce
    for pat in (r'<p><strong>Množství', r'<p><strong>Objem', r'<p><strong>Obsah', r'<h4>Výrobce', r'<p><strong>Výrobce',
                r'<p><strong>Množstvo', r'<p><strong>Výrobca', r'<h4>Výrobca'):
        m = re.search(pat, html)
        if m:
            return html[:m.start()] + f'<div><details><summary>{title}</summary>\n{body}\n</details></div>\n' + html[m.start():]
    raise ValueError('nenašel jsem místo pro vložení')


rows, chyby = [], []
for code, (tcs, hcs, tsk, hsk) in sorted(N.items()):
    k = kand[code]
    cs = cs_utf8[code]
    sk = k['sk']
    for a, b in SK_OPRAVY:
        if a in sk and b in cs:
            sk = sk.replace(a, b)
    try:
        ncs = vloz(cs, tcs, hcs, 'cs')
        nsk = vloz(sk, tsk, hsk, 'sk')
    except ValueError as e:
        chyby.append((code, str(e)))
        continue
    # kontroly: jediná změna je vložený blok, párové tagy sedí
    for old, new, h in ((cs, ncs, hcs), (sk, nsk, hsk)):
        assert len(new) > len(old)
        assert new.count('<details>') == old.count('<details>') + 1 and new.count('</details>') == old.count('</details>') + 1
        assert new.count('<div') - new.count('</div>') == old.count('<div') - old.count('</div>')
        assert h in new
    rows.append([code, k['pairCode'] or '', ncs, nsk])

print('připraveno', len(rows), 'chyby', chyby)
pokryto = set(N)
for kody, duvod in BEZ.items():
    pokryto |= set(kody.split())


buf = io.StringIO()
w = csv.writer(buf, delimiter=';', quoting=csv.QUOTE_ALL, lineterminator='\r\n')
w.writerow(['code', 'pairCode', 'description', 'description:sk'])
w.writerows(rows)
open('/home/claude/work/navod/G2_navody.csv', 'w', encoding='utf-8-sig', newline='').write(buf.getvalue())
json.dump({r[0]: {'cs': r[2], 'sk': r[3]} for r in rows}, open('/home/claude/work/navod/vystup2.json', 'w'), ensure_ascii=False)
print('G2_navody.csv', len(buf.getvalue()) // 1024, 'kB')
