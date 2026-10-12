"""Nová verze článků 155 (CZ) a 198 (SK): parfémy Essens podle typu vůně – bez cizích značek."""
import json, re, html

DATA = json.load(open('/home/claude/work/clanky/parfemy_typy.json'))
P = '/home/claude/work/clanky/puvodni/'

RUCNE = {  # u produktů bez uvedeného typu vůně – hlavní tóny z jejich stránky
    'LUX01': ('bergamot, cedrové dřevo, ambra', 'bergamot, cédrové drevo, ambra'),
    'LUX02': ('broskev, konvalinka, vanilka', 'broskyňa, konvalinka, vanilka'),
    'W16050': ('', ''),
}


def norm_typ(t, sk):
    t = t.strip().rstrip('.,;: ')
    t = re.sub(r'\s*Voňavá pyramída:?.*$', '', t)
    t = re.sub(r'\bChypre\b', 'Chyprová' if not sk else 'Chyprová', t, flags=re.I)
    t = t.replace('Cyprusová', 'Chyprová').replace('Fougerová', 'Fougérová').replace('fougerová', 'fougérová')
    parts = [p.strip().lower() for p in t.split(',') if p.strip()]
    s = ', '.join(parts)
    return s[:1].upper() + s[1:] if s else ''


def nazev(row):
    pid, title = row[0], row[1]
    m = re.search(r'\b([wm]\d{3})\b', title, re.I)
    if m and not pid.startswith(('LUX', '4EL', 'WBOUD')):
        return m.group(1).lower(), ''
    t = re.sub(r'^Essens\s+', '', title)
    t = re.sub(r'\s+(luxusní\s+)?parfém\s+(dámský|pánský|unisex)\s+50 ml$', '', t)
    return t, ('luxusní' if 'luxusní' in title else '')


def skupina(row):
    t = row[1]
    if 'unisex' in t:
        return 'unisex'
    if 'pánský' in t:
        return 'muzi'
    return 'zeny'


def klic(row):
    n, _ = nazev(row)
    m = re.match(r'[wm](\d{3})$', n)
    return (0, int(m.group(1)), '') if m else (1, 0, n.lower())


def tabulka(rows, sk):
    hl = ('Parfum', 'Typ vône') if sk else ('Parfém', 'Typ vůně')
    out = ['<table class="tab ke-vune">', '<tbody class="tab">',
           f'<tr class="tab"><th class="tab"><span style="color: #ffffff;">{hl[0]}</span></th>'
           f'<th class="tab"><span style="color: #ffffff;">{hl[1]}</span></th></tr>']
    for r in sorted(rows, key=klic):
        n, lux = nazev(r)
        url = r[3] if sk else r[2]
        typ = norm_typ(r[5] if sk else r[4], sk)
        if r[0] in RUCNE:
            typ = RUCNE[r[0]][1 if sk else 0] or '–'
            if RUCNE[r[0]][0]:
                typ = ('tóny: ' if sk else 'tóny: ') + typ
        label = f'Essens {n}'
        if lux:
            label += ' (luxusný)' if sk else ' (luxusní)'
        out.append(f'<tr class="tab"><td class="tab"><div class="item"><a class="odkaz" href="{url}">{html.escape(label)}</a></div></td>'
                   f'<td class="tab">{html.escape(typ or "–")}</td></tr>')
    out += ['</tbody>', '</table>']
    return '\n'.join(out)


def sestav(sk):
    src = open(P + ('198.html' if sk else '155.html')).read()
    head = src[:src.find('<h2>Seznam parfémů' if not sk else '<h2>Zoznam parfumov')]
    assert len(head) > 1000
    pre = '/sk' if sk else ''
    # odkazy na vyhledávání -> kategorie
    head = head.replace('/vyhledavani/?string=essens+parf%C3%A9m', pre + '/znacka/essens/')
    head = head.replace('/vyhledavani/?string=niche', pre + '/unisex-parfemy/')
    if sk:
        head = head.replace('<h1>Parfumy Essens – Zoznam vôní a sprievodca svetom alternatív</h1>',
                            '<h1>Parfumy Essens – prehľad vôní podľa typu</h1>')
        head = head.replace('Nejde o lacné napodobeniny, ale o prvotriedne parfumy s vysokým obsahom vonných esencií, inšpirované svetovými bestsellermi.',
                            'Ide o prvotriedne parfumy s vysokým, 20 % obsahom vonných esencií, ktoré sa vyrábajú v Českej republike.')
    else:
        head = head.replace('<h1>Parfémy Essens – Seznam vůní a průvodce světem alternativ</h1>',
                            '<h1>Parfémy Essens – přehled vůní podle typu</h1>')
        head = head.replace('Nejde o napodobeniny v nízké kvalitě, ale o prvotřídní parfémy s vysokým obsahem vonných esencí, inspirované světovými bestsellery.',
                            'Jde o prvotřídní parfémy s vysokým, 20% obsahem vonných esencí, které se vyrábějí v České republice.')
    assert 'inspir' not in head.lower() and 'inšpir' not in head.lower(), 'zbylo inspirováno'

    rows = DATA
    g = {k: [r for r in rows if skupina(r) == k] for k in ('zeny', 'muzi', 'unisex')}
    if sk:
        typy = """<h2>Ako si vybrať vôňu podľa typu</h2>
<p>Každý parfum Essens má uvedený typ vône. Podľa neho rýchlo zistíte, aký charakter vôňa má, a vyberiete si podobnú tej, ktorá vám vonia:</p>
<ul>
<li><strong>Kvetinová</strong> – ruža, jazmín, pivonka či konvalinka; ženská a nežná.</li>
<li><strong>Ovocná</strong> – šťavnaté ovocie ako broskyňa, malina alebo jablko; svieža a hravá.</li>
<li><strong>Citrusová</strong> – bergamot, citrón, grep; ľahká a osviežujúca, ideálna na leto.</li>
<li><strong>Drevitá</strong> – céder, santal, vetiver; elegantná a pokojná.</li>
<li><strong>Orientálna</strong> – ambra, vanilka, korenie; plná, hrejivá a zmyselná.</li>
<li><strong>Chyprová</strong> – kontrast sviežich citrusov a zemitého machu; sofistikovaná klasika.</li>
<li><strong>Fougérová</strong> – levanduľa, kumarín a bylinky; typicky pánska, čistá vôňa.</li>
<li><strong>Gurmánska</strong> – karamel, vanilka, sladké tóny; lákavá a hrejivá.</li>
<li><strong>Vodná a zelená</strong> – morské tóny, čerstvo pokosená tráva a lístie; prirodzená sviežosť.</li>
</ul>
<p>Podrobné zloženie vône – hlavu, srdce a základ – nájdete pri každom parfume na jeho stránke.</p>"""
        h_z, h_m, h_u = 'Dámske parfumy Essens', 'Pánske parfumy Essens', 'Unisex parfumy Essens'
        uvod = '<h2>Zoznam parfumov Essens podľa typu vône</h2>\n<p>V tabuľkách nájdete všetky parfumy Essens, ktoré máme v ponuke. Kliknutím na názov sa dostanete na detail parfumu.</p>'
        zaver = f'<p><a class="odkaz" href="{pre}/znacka/essens/">Zobraziť všetky produkty Essens</a></p>'
    else:
        typy = """<h2>Jak si vybrat vůni podle typu</h2>
<p>Každý parfém Essens má uvedený typ vůně. Podle něj rychle poznáte, jaký má vůně charakter, a vyberete si podobnou té, která vám voní:</p>
<ul>
<li><strong>Květinová</strong> – růže, jasmín, pivoňka či konvalinka; ženská a něžná.</li>
<li><strong>Ovocná</strong> – šťavnaté ovoce jako broskev, malina nebo jablko; svěží a hravá.</li>
<li><strong>Citrusová</strong> – bergamot, citron, grep; lehká a osvěžující, ideální na léto.</li>
<li><strong>Dřevitá</strong> – cedr, santal, vetiver; elegantní a klidná.</li>
<li><strong>Orientální</strong> – ambra, vanilka, koření; plná, hřejivá a smyslná.</li>
<li><strong>Chyprová</strong> – kontrast svěžích citrusů a zemitého mechu; sofistikovaná klasika.</li>
<li><strong>Fougérová</strong> – levandule, kumarin a bylinky; typicky pánská, čistá vůně.</li>
<li><strong>Gurmánská</strong> – karamel, vanilka, sladké tóny; lákavá a hřejivá.</li>
<li><strong>Vodní a zelená</strong> – mořské tóny, čerstvě posečená tráva a listí; přirozená svěžest.</li>
</ul>
<p>Podrobné složení vůně – hlavu, srdce a základ – najdete u každého parfému na jeho stránce.</p>"""
        h_z, h_m, h_u = 'Dámské parfémy Essens', 'Pánské parfémy Essens', 'Unisex parfémy Essens'
        uvod = '<h2>Seznam parfémů Essens podle typu vůně</h2>\n<p>V tabulkách najdete všechny parfémy Essens, které máme v nabídce. Kliknutím na název se dostanete na detail parfému.</p>'
        zaver = f'<p><a class="odkaz" href="{pre}/znacka/essens/">Zobrazit všechny produkty Essens</a></p>'
    body = (head + typy + '\n' + uvod + '\n'
            + f'<h3>{h_z}</h3>\n' + tabulka(g['zeny'], sk) + '\n'
            + f'<h3>{h_m}</h3>\n' + tabulka(g['muzi'], sk) + '\n'
            + f'<h3>{h_u}</h3>\n' + tabulka(g['unisex'], sk) + '\n' + zaver)
    return body, {k: len(v) for k, v in g.items()}


if __name__ == '__main__':
    import os
    os.makedirs('/home/claude/work/clanky/upravene', exist_ok=True)
    for sk, cid in ((False, '155'), (True, '198')):
        b, n = sestav(sk)
        open(f'/home/claude/work/clanky/upravene/{cid}.html', 'w').write(b)
        print(cid, len(b), n)
