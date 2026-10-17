# Texty pro nové produkty JUST – aroma spreje (17. 10. 2026)
# Alpský vánek: podle justnahrin.cz/produkty/aroma-sprej-alpsky-vanek (kat. č. 6061), vlastními slovy; složení doslova (CZ), SK překlad seznamu.
# Lesní vánek (Pure Waldbrise): podle just.ch/de/aromaspray-pure-waldbrise.html (Artikel-Nr. 369), vlastními slovy; složení přeloženo z němčiny.
# Výrobce u žádného nemá na webu bezpečnostní upozornění ani výstražné symboly → sekce Upozornění se nevkládá (zkontrolovat etiketu).
import json, os

VYROBCE_CS = '<h4>Výrobce:</h4>\n<p>JUST International AG<br />CH 9428, Walzenhausen, Švýcarsko</p>'
VYROBCE_SK = '<h4>Výrobca:</h4>\n<p>JUST International AG<br />CH 9428, Walzenhausen, Švajčiarsko</p>'
SLOZENI_POZN_CS = ('<p>Vyjmenovaný seznam použitých ingrediencí představuje složení aktuálně vyráběných výrobků. Protože výrobky jsou neustále '
                   'inovovány tak, aby odrážely nejnovější vědecké poznatky i přání spotřebitelů, složení výrobku se může mírně změnit. '
                   'Pro přesné složení sledujte vždy zadní etiketu výrobku.</p>')
SLOZENI_POZN_SK = ('<p>Vymenovaný zoznam použitých ingrediencií predstavuje zloženie aktuálne vyrábaných výrobkov. Pretože výrobky sú neustále '
                   'inovované tak, aby odrážali najnovšie vedecké poznatky aj priania spotrebiteľov, zloženie výrobku sa môže mierne zmeniť. '
                   'Pre presné zloženie sledujte vždy zadnú etiketu výrobku.</p>')


def det(summary, inner):
    return f'<details><summary>{summary}</summary>\n{inner}\n</details>'


def ul(items):
    return '<ul>\n' + '\n'.join(f'<li>{i}</li>' for i in items) + '\n</ul>'


def page(h2, paras, benefits_t, benefits, use_t, use, active_t, active, comp_t, comp, comp_note, objem_t, vyrobce):
    out = f'<h2><em>{h2}</em></h2>\n' + '\n'.join(f'<p>{p}</p>' for p in paras) + '\n<div>'
    out += det(benefits_t, ul(benefits)) + ' ' + det(use_t, f'<p>{use}</p>') + ' '
    out += det(active_t, f'<p>{active}</p>') + ' ' + det(comp_t, f'<p>{comp}</p>\n{comp_note}')
    out += f'</div>\n<p><strong>{objem_t}</strong>: 100 ml</p>\n{vyrobce}'
    return out


P = {}

# ---------- Alpský vánek (6061) ----------
P['alp_cs'] = dict(
    name='Just Aroma sprej Alpský vánek 100 ml',
    seo='Just Aroma sprej Alpský vánek 100 ml | KosmetikaEva.eu',
    meta='Just Aroma sprej Alpský vánek 100 ml: svěží vůně horského vzduchu, lučních květů a bylin. Přírodní éterické oleje, do domova, kanceláře i auta.',
    desc=page('Just Aroma sprej Alpský vánek 100 ml',
        ['<strong>Aroma sprej Alpský vánek</strong> od švýcarské značky Just provoní domov čistou, svěží vůní, která připomíná horský vzduch v&nbsp;Alpách na začátku léta – rozkvetlé louky a&nbsp;křišťálově čistou vodu.',
         'Vonná kompozice je svěží a živá: bylinné tóny se v&nbsp;ní snoubí s&nbsp;hřejivým dřevem, zemitou trávou a&nbsp;citrusovými akcenty. Navodí příjemnou atmosféru pohody a&nbsp;odpočinku a vydrží dlouho. Sprej s&nbsp;přírodním složením přichází v&nbsp;atraktivním flakonu, který je ozdobou každého interiéru.'],
        'Hlavní benefity',
        ['Svěží vůně horského vzduchu, lučních květů a&nbsp;bylin', 'Přírodní složení – bio alkohol, éterické oleje a&nbsp;extrakt z&nbsp;horského sena',
         'Intenzivní a dlouhotrvající vůně', 'Veganský výrobek', 'Do domova, kanceláře, auta i&nbsp;na cesty'],
        'Použití',
        'Sprej nastříkejte do prostoru, množství přizpůsobte velikosti místnosti. Hodí se k&nbsp;osvěžení vzduchu doma, v&nbsp;kanceláři, v&nbsp;autě i&nbsp;v&nbsp;ubytování na cestách.',
        'Hlavní účinné složky',
        'éterické oleje z jalovce, máty, citronu, levandule a rozmarýnu, extrakt z horského sena, bio alkohol',
        'Složení a alergeny',
        'bio-alcohol, extrakt z horského sena obsahující luční květy a byliny, éterické oleje z jalovce (Juniperus virginiana, dřevo), máty (Mentha piperita), citronu (Citrus limon, kůra), levandule (Lavandula angustifolia, květy), rozmarýnu (Rosmarinus officinalis, konce kvetoucích větviček), pryskyřice z elemi (Canarium luzonicum), beta-pinene*, linalyl acetate*, linalool*, methyl cyclopentenolone*<br />* přirozená složka přírodních éterických olejů',
        SLOZENI_POZN_CS, 'Objem', VYROBCE_CS))
P['alp_sk'] = dict(
    name='Just Aroma sprej Alpský vánok 100 ml',
    seo='Just Aroma sprej Alpský vánok 100 ml | KosmetikaEva.eu',
    meta='Just Aroma sprej Alpský vánok 100 ml: svieža vôňa horského vzduchu, lúčnych kvetov a byliniek. Prírodné éterické oleje, do domova, kancelárie aj auta.',
    desc=page('Just Aroma sprej Alpský vánok 100 ml',
        ['<strong>Aroma sprej Alpský vánok</strong> od švajčiarskej značky Just prevonia domov čistou, sviežou vôňou, ktorá pripomína horský vzduch v&nbsp;Alpách na začiatku leta – rozkvitnuté lúky a&nbsp;krištáľovo čistú vodu.',
         'Vonná kompozícia je svieža a živá: bylinkové tóny sa v&nbsp;nej snúbia s&nbsp;hrejivým drevom, zemitou trávou a&nbsp;citrusovými akcentmi. Navodí príjemnú atmosféru pohody a&nbsp;oddychu a vydrží dlho. Sprej s&nbsp;prírodným zložením prichádza v&nbsp;atraktívnom flakóne, ktorý je ozdobou každého interiéru.'],
        'Hlavné benefity',
        ['Svieža vôňa horského vzduchu, lúčnych kvetov a&nbsp;byliniek', 'Prírodné zloženie – bio alkohol, éterické oleje a&nbsp;extrakt z&nbsp;horského sena',
         'Intenzívna a dlhotrvajúca vôňa', 'Vegánsky výrobok', 'Do domova, kancelárie, auta aj&nbsp;na cesty'],
        'Použitie',
        'Sprej nastriekajte do priestoru, množstvo prispôsobte veľkosti miestnosti. Hodí sa na osvieženie vzduchu doma, v&nbsp;kancelárii, v&nbsp;aute aj&nbsp;v&nbsp;ubytovaní na cestách.',
        'Hlavné účinné zložky',
        'éterické oleje z borievky, mäty, citróna, levandule a rozmarínu, extrakt z horského sena, bio alkohol',
        'Zloženie a alergény',
        'bio-alcohol, extrakt z horského sena obsahujúci lúčne kvety a byliny, éterické oleje z borievky (Juniperus virginiana, drevo), mäty (Mentha piperita), citróna (Citrus limon, kôra), levandule (Lavandula angustifolia, kvety), rozmarínu (Rosmarinus officinalis, konce kvitnúcich vetvičiek), živice z elemi (Canarium luzonicum), beta-pinene*, linalyl acetate*, linalool*, methyl cyclopentenolone*<br />* prirodzená zložka prírodných éterických olejov',
        SLOZENI_POZN_SK, 'Objem', VYROBCE_SK))

# ---------- Lesní vánek / Pure Waldbrise (369) ----------
P['les_cs'] = dict(
    name='Just Aroma sprej Lesní vánek 100 ml',
    seo='Just Aroma sprej Lesní vánek 100 ml | KosmetikaEva.eu',
    meta='Just Aroma sprej Lesní vánek 100 ml: teplá vůně jehličnanů a lesa ze 100% přírodních éterických olejů. Bez hnacího plynu, do domova, kanceláře i auta.',
    desc=page('Just Aroma sprej Lesní vánek 100 ml',
        ['<strong>Aroma sprej Lesní vánek</strong> (v originále Aromaspray Pure Waldbrise) od švýcarské značky Just přenese do vašeho domova atmosféru dlouhé procházky lesem. Jemně kořenitá vůně jehličnanů a lesní půdy vytvoří klidné a útulné prostředí – doma, v&nbsp;kanceláři i&nbsp;v&nbsp;autě.',
         'Kompozici tvoří výhradně 100% přírodní éterické oleje z&nbsp;borovice limby, borovice lesní, cedru, jedle bělokoré a&nbsp;kleče. Teplá dřevitá vůně s&nbsp;kořenitým nádechem navozuje pocit klidu a pohody a vydrží dlouho. Sprej je bez hnacího plynu – stačí pár stisků pumpičky.'],
        'Hlavní benefity',
        ['100% přírodní éterické oleje z&nbsp;jehličnatých stromů', 'Teplá, dřevitá a jemně kořenitá vůně lesa', 'Dlouhotrvající vůně',
         'Bez hnacího plynu', 'Do domova, kanceláře i&nbsp;auta'],
        'Použití',
        'Podle velikosti místnosti nastříkejte do vzduchu několik dávek a vychutnejte si příjemnou lesní atmosféru.',
        'Hlavní účinné složky',
        'éterické oleje z borovice limby, borovice lesní, cedru, jedle bělokoré a kleče, bio alkohol',
        'Složení a alergeny',
        'bio alkohol, přírodní éterické oleje z borovice limby, borovice lesní, cedru atlaského, jedle bělokoré, kleče a jalovce viržinského',
        '<p>Složení podle údajů výrobce (překlad z němčiny). Pro přesné složení sledujte vždy zadní etiketu výrobku.</p>', 'Objem', VYROBCE_CS))
P['les_sk'] = dict(
    name='Just Aroma sprej Lesný vánok 100 ml',
    seo='Just Aroma sprej Lesný vánok 100 ml | KosmetikaEva.eu',
    meta='Just Aroma sprej Lesný vánok 100 ml: teplá vôňa ihličnanov a lesa zo 100 % prírodných éterických olejov. Bez hnacieho plynu, do domova, kancelárie aj auta.',
    desc=page('Just Aroma sprej Lesný vánok 100 ml',
        ['<strong>Aroma sprej Lesný vánok</strong> (v originále Aromaspray Pure Waldbrise) od švajčiarskej značky Just prenesie do vášho domova atmosféru dlhej prechádzky lesom. Jemne korenistá vôňa ihličnanov a lesnej pôdy vytvorí pokojné a útulné prostredie – doma, v&nbsp;kancelárii aj&nbsp;v&nbsp;aute.',
         'Kompozíciu tvoria výhradne 100 % prírodné éterické oleje z&nbsp;borovice limbovej, borovice lesnej, cédra, jedle bielej a&nbsp;kosodreviny. Teplá drevitá vôňa s&nbsp;korenistým nádychom navodzuje pocit pokoja a pohody a vydrží dlho. Sprej je bez hnacieho plynu – stačí pár stlačení pumpičky.'],
        'Hlavné benefity',
        ['100 % prírodné éterické oleje z&nbsp;ihličnatých stromov', 'Teplá, drevitá a jemne korenistá vôňa lesa', 'Dlhotrvajúca vôňa',
         'Bez hnacieho plynu', 'Do domova, kancelárie aj&nbsp;auta'],
        'Použitie',
        'Podľa veľkosti miestnosti nastriekajte do vzduchu niekoľko dávok a vychutnajte si príjemnú lesnú atmosféru.',
        'Hlavné účinné zložky',
        'éterické oleje z borovice limbovej, borovice lesnej, cédra, jedle bielej a kosodreviny, bio alkohol',
        'Zloženie a alergény',
        'bio alkohol, prírodné éterické oleje z borovice limbovej, borovice lesnej, cédra atlaského, jedle bielej, kosodreviny a borievky virgínskej',
        '<p>Zloženie podľa údajov výrobcu (preklad z nemčiny). Pre presné zloženie sledujte vždy zadnú etiketu výrobku.</p>', 'Objem', VYROBCE_SK))

if __name__ == '__main__':
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, 'aroma-spreje.json'), 'w', encoding='utf-8') as f:
        json.dump(P, f, ensure_ascii=False, indent=1)
    for k, v in P.items():
        print(k, len(v['meta']), len(v['desc']))
