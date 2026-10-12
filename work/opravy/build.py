"""Opravy: Nahrin 4207 (překlep), Essens W90350 (bez „inspirováno“, box, SK texty, značka), dárkové poukazy.
Záloha původních hodnot: exp5.json + exp_dp.json (export z administrace 12. 10. 2026)."""
import csv, io, json, re, sys
sys.path.insert(0, '/home/claude/work/box')
from zamena_box import box

D = {}
for f in ('exp5.json', 'exp_dp.json'):
    for k, t in json.load(open(f'/home/claude/work/opravy/{f}')).items():
        r = list(csv.reader(io.StringIO(t), delimiter=';'))
        D[k] = dict(zip(r[0], r[1]))


GTX = re.compile(r'\s*<div id="gtx-trans"[^>]*>.*?</div>', re.S)  # zbytek po rozšíření Google Překladač


def sub1(pat, rep, s, n=1):
    new, c = re.subn(pat, rep, s)
    assert c == n, (pat, c)
    return new


SUFFIX = ' | KosmetikaEva.eu'
cz_names, cz_desc, sk_names, sk_desc = {}, {}, {}, {}

# ---------- Nahrin Echinacina 4207
cz_names['4207'] = 'Nahrin Echinacina doplněk stravy 250 ml'
sk_names['4207'] = 'Nahrin Echinacina výživový doplnok 250 ml'

# ---------- dárkové poukazy
HODNOTA = {'DP15': '15 €', 'DP40': '40 €', 'DP50': '50 €', 'DP60': '60 €', 'DP75': '75 €',
           'DP200': '200 Kč', 'DP400': '400 Kč', 'DP500': '500 Kč', 'DP1000': '1000 Kč',
           'DP1500': '1500 Kč', 'DP2000': '2000 Kč'}
for kod, h in HODNOTA.items():
    x = D[kod]
    # CZ název ve slovenštině
    if x['name:cs'].startswith('Darčekový'):
        cz_names[kod] = f'Dárkový poukaz {h}'
    # SK název v češtině
    if x['name:sk'].startswith('Dárkový'):
        sk_names[kod] = f'Darčekový poukaz {h}'
    if x['seoTitle:sk'] == 'Darčekový poukaz' + SUFFIX:
        sk_names.setdefault(kod, x['name:sk'])
    # CZ popis: špatný nadpis a „dle zvolené varianty“
    d = x['description:cs']
    nd = re.sub(r'<h2><em>Dárkový poukaz [^<]*? KosmetikaEva\.eu</em></h2>',
                f'<h2><em>Dárkový poukaz {h} KosmetikaEva.eu</em></h2>', d, count=1)
    nd = re.sub(r'(<strong>Hodnota poukazu:</strong>)\s*(?:&nbsp;)?dle zvolené varianty', r'\1 ' + h, nd)
    nd = GTX.sub('', nd)
    if nd != d:
        cz_desc[kod] = nd
    # SK popis: chybějící hodnota v nadpisu, „podľa zvolenej varianty“, překlep „najmeněj“
    d = x['description:sk']
    nd = re.sub(r'<h2><em>Darčekový poukaz (?:[^<]*? )?KosmetikaEva\.eu</em></h2>',
                f'<h2><em>Darčekový poukaz {h.replace("1500 Kč", "1 500 Kč")} KosmetikaEva.eu</em></h2>', d, count=1)
    nd = re.sub(r'(<strong>Hodnota poukazu:</strong>)\s*(?:&nbsp;)?podľa zvolenej varianty', r'\1 ' + h, nd)
    nd = nd.replace('najmeněj', 'najmenej')
    nd = GTX.sub('', nd)
    if nd != d:
        sk_desc[kod] = nd

# ---------- Essens W90350 (w903)
x = D['W90350']
inci = re.search(r'<summary>Složení \(INCI\)</summary>\s*<p>(.*?)</p>', x['description:cs'], re.S).group(1)
assert 'inspirováno' in x['description:cs']
POUZITI_CS = ('Naneste malé množství parfému na pulzní body – zápěstí, krk, místa za ušima nebo dekolt. Vůni můžete lehce '
              'rozprášit i do vlasů či na oblečení (u jemných látek nejprve vyzkoušejte na nenápadném místě). Vyhněte se '
              'kontaktu s očima a podrážděnou pokožkou.')
POUZITI_SK = ('Naneste malé množstvo parfumu na pulzné body – zápästie, krk, miesta za ušami alebo dekolt. Vôňu môžete jemne '
              'rozprášiť aj do vlasov či na oblečenie (pri jemných látkach najprv vyskúšajte na nenápadnom mieste). Vyhnite sa '
              'kontaktu s očami a podráždenou pokožkou.')


def parfem(lang):
    t = {
        'cs': dict(h2='Dámský parfém w903 – smyslná pižmová vůně s květinovými tóny',
                   p='Smyslná kořeněná vůně vás zahalí do oblaku, který probudí vaše druhé já. Je odlehčenou verzí tradiční '
                     'vůně pižma, obohacenou o květinové tóny. Užijte si netradiční orientální vůni, aniž byste se cítili převonění.',
                   sekce=[('Hlava', 'Květinové tóny'), ('Srdce', 'Konvalinka, dřevité tóny'), ('Základ', 'Pižmo, větvičník, ambra'),
                          ('Typ vůně', 'Květinová'), ('Použití', POUZITI_CS), ('Složení (INCI)', inci)],
                   pata='<p><strong>Objem:</strong> 50 ml<br /> <strong>Výrobce:</strong> ESSENS EUROPE SE, Zaoralova 3045/1e, 628 00 Brno</p>'),
        'sk': dict(h2='Dámsky parfum w903 – zmyselná pižmová vôňa s kvetinovými tónmi',
                   p='Zmyselná korenistá vôňa vás zahalí do oblaku, ktorý prebudí vaše druhé ja. Je odľahčenou verziou tradičnej '
                     'vône pižma, obohatenou o kvetinové tóny. Užite si netradičnú orientálnu vôňu bez pocitu, že ste sa navoňali priveľa.',
                   sekce=[('Hlava', 'Kvetinové tóny'), ('Srdce', 'Konvalinka, drevité tóny'), ('Základ', 'Pižmo, dubový mach, ambra'),
                          ('Typ vône', 'Kvetinová'), ('Použitie', POUZITI_SK), ('Zloženie (INCI)', inci)],
                   pata='<p><strong>Objem:</strong> 50 ml<br /> <strong>Výrobca:</strong> ESSENS EUROPE SE, Zaoralova 3045/1e, 628 00 Brno</p>'),
    }[lang]
    det = ' '.join(f'<details> <summary>{a}</summary>\n<p>{b}</p>\n</details>' for a, b in t['sekce'])
    return (f'<h2><em>{t["h2"]}</em></h2>\n{box("Musk Kashmir", lang)}\n<p>{t["p"]}</p>\n'
            f'<div>{det}</div>\n{t["pata"]}')


cz_desc['W90350'] = parfem('cs')
sk_desc['W90350'] = parfem('sk')
sk_names['W90350'] = 'Essens Dámsky parfum w903 50 ml'

# ---------- kontroly
for k, v in list(cz_desc.items()) + list(sk_desc.items()):
    assert 'inspirov' not in v.lower() and '?' not in re.sub(r'<[^>]+>', '', v), k
    assert v.count('<details>') == v.count('</details>') and v.count('<div') == v.count('</div>'), k
for k, v in cz_desc.items():
    if k.startswith('DP'):
        assert '40 €' not in v or k == 'DP40', k
        assert 'dle zvolené' not in v, k
for k, v in sk_desc.items():
    assert 'najmeněj' not in v and 'podľa zvolenej' not in v, k


def zapis(nazev, hlavicka, radky):
    buf = io.StringIO()
    w = csv.writer(buf, delimiter=';', quoting=csv.QUOTE_ALL, lineterminator='\r\n')
    w.writerow(hlavicka)
    w.writerows(radky)
    open(f'/home/claude/work/import/{nazev}', 'w', encoding='utf-8-sig', newline='').write(buf.getvalue())
    print(nazev, len(radky), 'řádků:', ', '.join(r[0] for r in radky))


zapis('M1_cz_nazvy.csv', ['code', 'pairCode', 'name', 'seoTitle'],
      [[k, '', n, n + SUFFIX] for k, n in sorted(cz_names.items())])
zapis('M2_cz_popisy.csv', ['code', 'pairCode', 'description'],
      [[k, '', v] for k, v in sorted(cz_desc.items())])
zapis('M3_sk_nazvy.csv', ['code', 'pairCode', 'name:sk', 'seoTitle:sk'],
      [[k, '', n, n + SUFFIX] for k, n in sorted(sk_names.items())])
zapis('M4_sk_popisy.csv', ['code', 'pairCode', 'description:sk'],
      [[k, '', v] for k, v in sorted(sk_desc.items())])
zapis('M5_vyrobce.csv', ['code', 'pairCode', 'manufacturer'], [['W90350', '', 'Essens']])
json.dump({'cz_names': cz_names, 'sk_names': sk_names, 'cz_desc': cz_desc, 'sk_desc': sk_desc},
          open('/home/claude/work/opravy/vystup.json', 'w'), ensure_ascii=False, indent=1)
