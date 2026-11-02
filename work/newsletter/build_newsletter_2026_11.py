# Newsletter KosmetikaEva.eu – listopad 2026 (odeslání čt 5. 11. 2026 9:00, CZ a SK zvlášť)
# Majitel 26. 10. 2026: „kampaně i newsletter odsouhlasuji“ – obsah: Eucasol, Olej z 31 bylin, tymián, vánoční sady
# JUST/Essens, dárkové poukazy, doprava; SK vlastní obsah + jednorázový kupón „doprava zdarma“ (text, kupón až po schválení).
# Výběr podle marže (2. 11. 2026): Eucasol 50 ml, Olej z 31 bylin 20/50 ml, Tymiánový krém 100 ml, Essens sady a krémy,
# Eurona svíčka O´Jingle. Bez zdravotních tvrzení (žádné nachlazení, dýchání, hrudník, spánek) a bez cizích parfémových značek.
# Všechny odkazy s UTM: utm_source=newsletter&utm_medium=email&utm_campaign=2026-11-cz|sk&utm_content=<odkaz>.
# Spuštění: python3 build_newsletter_2026_11.py
import os

from build_newsletter import (ACC, INK, LINE, MUTED, SOFT, WEB, a, box, btn, h2, p, product, row, small, wrap)

CAMPAIGN = '2026-11'
CDN = 'https://cdn.myshoptet.com/usr/www.kosmetikaeva.eu/user/shop/detail/'
IMG = {
    'eucasol': CDN + '7390_eucasol-50-ml.png',
    'olej': CDN + '8836_olej-z-31-kompozice-50-ml-web.png',
    'krem': CDN + '8833-2_tymianovy-krem-kompozice-web.png',
    'solar': CDN + '10819_essens-parfemovany-set-solar-noire.jpg',
    'western': CDN + '10825_essens-parfemovany-set-western-spirit.jpg',
    'ruce': CDN + '6629-4_essens-set-kremu-na-ruce-3-x-30-ml.png',
    'svicka': CDN + '11158-1_eurona-designova-vonna-svicka-o--jingle-200-g.jpg',
}
PATH = {
    'eucasol': '/esencialni-oleje/just-eucasol-sprej-50-ml/?variantId=54214',
    'olej': '/esencialni-oleje/just-olej-z-31-lecivych-bylin-75-ml/',
    'krem': '/telo-2/just-tymianovy-krem-100-ml/?variantId=53944',
    'solar': '/damske-parfemy/essens-parfemovany-set-solar-noire/',
    'western': '/panske-parfemy/essens-parfemovany-set-western-spirit/',
    'ruce': '/ruce-a-nohy-2/essens-set-kremu-na-ruce-3-x-30-ml/',
    'svicka': '/osvezovace-vzduchu-a-textilii/eurona-designova-vonna-svicka-o--jingle-200-g/',
}
CONTENT = {'eucasol': 'eucasol', 'olej': 'olej-31-bylin', 'krem': 'tymianovy-krem', 'solar': 'solar-noire',
           'western': 'western-spirit', 'ruce': 'kremy-na-ruce', 'svicka': 'svicka-ojingle'}

COUPON = 'DOPRAVA-SK'


def utm(url, lang, content):
    sep = '&' if '?' in url else '?'
    country = 'cz' if lang == 'cs' else lang
    return f'{url}{sep}utm_source=newsletter&utm_medium=email&utm_campaign={CAMPAIGN}-{country}&utm_content={content}'


T = {
 'cs': dict(
   base=WEB,
   subject='Eucasol, olej z 31 bylin a první vánoční dárky',
   preheader='Oblíbené bylinky od JUST na listopad a dárkové sady Essens – doprava zdarma od 2 500 Kč.',
   eyebrow='Novinky z KosmetikaEva.eu · listopad 2026',
   h1='Listopad voní bylinkami',
   intro=['Dobrý den,',
          'listopad je tu a s ním první mrazivá rána. Posíláme pár tipů z našeho e-shopu – oblíbené bylinky od švýcarské značky JUST a první dárky pod stromeček.'],
   coupon=None,
   s1=('Bylinky od JUST', 'Vůně, které k listopadu patří'),
   prods=[
     ('eucasol', 'Eucasol sprej 50 ml',
      'Bylinný sprej s éterickými oleji z eukalyptu, máty a rozmarýnu. Stačí jedno stříknutí do vzduchu a místnost se naplní svěží bylinkovou vůní – doma, v kanceláři i v autě.',
      '529 Kč', 'Nejoblíbenější'),
     ('olej', 'Olej z 31 bylin',
      'Koncentrovaná směs éterických olejů a bylinných výtažků z 31 pečlivě vybraných bylin. Pár kapek do aromalampy či difuzéru, do teplé koupele nebo zředěný v nosném oleji k masáži.',
      '20 ml 539 Kč · 50 ml 1 199 Kč', None),
     ('krem', 'Tymiánový krém 100 ml',
      'Bylinný krém s éterickými oleji z tymiánu, eukalyptu, borovice a rozmarýnu. Při jemné masáži příjemně hřeje a jeho bylinná vůně patří k pohodovému večeru.',
      '769 Kč', None),
   ],
   buy='Koupit',
   s2=('Vánoce 2026', 'Dárky, které potěší'),
   s2text='Na dárky je nejlepší myslet včas. Tady je pár tipů – další najdete v kategorii Vánoční dárky.',
   gifts=[
     ('solar', 'Essens sada Solar Noire', 'Parfém Solar Noire a sprchový gel v jedné dárkové sadě. Sladký ovocný úvod s jahodou a broskví, kořenité srdce a sametový vanilkový základ.', '1 279 Kč', 'Pro ni'),
     ('western', 'Essens sada Western Spirit', 'Pánský parfém Western Spirit a sprchový gel stejného jména. Svěží bergamot se zelenými tóny, kosatec s ambrou a santalové dřevo v základu.', '1 279 Kč', 'Pro něj'),
     ('ruce', 'Essens sada krémů na ruce 3 × 30 ml', 'Tři hydratační krémy na ruce – med s jasmínem, černý čaj s granátovým jablkem a růžové dřevo. Rychle se vstřebávají a nemastí.', '399 Kč', None),
     ('svicka', 'Eurona vonná svíčka O´Jingle', 'Vánoční vůně červených jablek, skořice a vanilky. Sójový a kokosový vosk a dřevěný knot, který při hoření jemně praská. Hoří až 40 hodin.', '459 Kč', None),
   ],
   s2btn=('/vanocni-darky/', 'Vánoční dárky'),
   s2link=('/darkove-poukazy/', 'Dárkové poukazy – pošleme je e-mailem'),
   ship='<strong>Doprava</strong> na výdejní místa a do Z-BOXů Zásilkovny za 80&nbsp;Kč, při nákupu od 2&nbsp;500&nbsp;Kč <strong>zdarma</strong>.',
   regards='S pozdravem a přáním klidného listopadu',
   fb='Sledujte nás na Facebooku',
   why='Tento e-mail dostáváte, protože jste u nás nakoupili. Pokud už o naše novinky nestojíte, odhlásit se můžete zde: #unsubscribe#',
   op='Provozovatel: Stanislav Zbořil, IČO 86963139, Přílucká 4118, 760 01 Zlín · '),
 'sk': dict(
   base=WEB + '/sk',
   subject='Doprava zadarmo, Eucasol a olej z 31 bylín',
   preheader='Obľúbené bylinky od JUST, vianočné sady Essens a doprava zadarmo s kódom do 11. 11.',
   eyebrow='Novinky z KosmetikaEva.eu · november 2026',
   h1='November vonia bylinkami',
   intro=['Dobrý deň,',
          'november je tu a s ním prvé mrazivé rána. Posielame pár tipov z nášho e-shopu – obľúbené bylinky od švajčiarskej značky JUST, prvé darčeky pod stromček a pre Vás aj dopravu zadarmo.'],
   coupon=('Len pre Vás', f'Doprava zadarmo s kódom {COUPON}',
           f'Pri nákupe od 40&nbsp;€ zadajte v košíku kód <strong>{COUPON}</strong> a dopravu máte zadarmo – na výdajné miesto, do Z-BOXu aj kuriérom. Kód platí do stredy 11.&nbsp;11.&nbsp;2026.',
           'Nakupovať'),
   s1=('Bylinky od JUST', 'Vône, ktoré k novembru patria'),
   prods=[
     ('eucasol', 'Eucasol sprej 50 ml',
      'Bylinný sprej s éterickými olejmi z eukalyptu, mäty a rozmarínu. Stačí jedno streknutie do vzduchu a miestnosť sa naplní sviežou bylinkovou vôňou – doma, v kancelárii aj v aute.',
      '21,72 €', 'Najobľúbenejší'),
     ('olej', 'Olej z 31 bylín',
      'Koncentrovaná zmes éterických olejov a bylinných výťažkov z 31 starostlivo vybraných bylín. Pár kvapiek do aromalampy či difuzéra, do teplého kúpeľa alebo zriedený v nosnom oleji na masáž.',
      '20 ml 22,13 € · 50 ml 49,22 €', None),
     ('krem', 'Tymianový krém 100 ml',
      'Bylinný krém s éterickými olejmi z tymianu, eukalyptu, borovice a rozmarínu. Pri jemnej masáži príjemne hreje a jeho bylinná vôňa patrí k pohodovému večeru.',
      '31,57 €', None),
   ],
   buy='Kúpiť',
   s2=('Vianoce 2026', 'Darčeky, ktoré potešia'),
   s2text='Na darčeky je najlepšie myslieť včas. Tu je pár tipov – ďalšie nájdete v kategórii Vianočné darčeky.',
   gifts=[
     ('solar', 'Essens sada Solar Noire', 'Parfum Solar Noire a sprchový gél v jednej darčekovej sade. Sladký ovocný úvod s jahodou a broskyňou, korenisté srdce a zamatový vanilkový základ.', '52,50 €', 'Pre ňu'),
     ('western', 'Essens sada Western Spirit', 'Pánsky parfum Western Spirit a sprchový gél rovnakého mena. Svieži bergamot so zelenými tónmi, kosatec s ambrou a santalové drevo v základe.', '52,50 €', 'Pre neho'),
     ('ruce', 'Essens sada krémov na ruky 3 × 30 ml', 'Tri hydratačné krémy na ruky – med s jazmínom, čierny čaj s granátovým jablkom a ružové drevo. Rýchlo sa vstrebávajú a nemastia.', '16,38 €', None),
     ('svicka', 'Eurona vonná sviečka O´Jingle', 'Vianočná vôňa červených jabĺk, škorice a vanilky. Sójový a kokosový vosk a drevený knôt, ktorý pri horení jemne praská. Horí až 40 hodín.', '18,84 €', None),
   ],
   s2btn=('/vanocni-darky/', 'Vianočné darčeky'),
   s2link=('/darkove-poukazy/', 'Darčekové poukážky – pošleme ich e-mailom'),
   ship='<strong>Doprava</strong> na výdajné miesta a do Z-BOXov Packety za 6&nbsp;€, pri nákupe od 120&nbsp;€ <strong>zadarmo</strong>.',
   regards='S pozdravom a prianím pokojného novembra',
   fb='Sledujte nás na Facebooku',
   why='Tento e-mail dostávate, pretože ste u nás nakúpili. Ak už o naše novinky nestojíte, odhlásiť sa môžete tu: #unsubscribe#',
   op='Prevádzkovateľ: Stanislav Zbořil, IČO 86963139, Přílucká 4118, 760 01 Zlín, Česká republika · '),
}


def build(lang):
    t = T[lang]
    link = lambda path, content: utm(t['base'] + path, lang, content)  # noqa: E731
    rows = []
    head = (f'<p style="margin:0 0 6px 0;font-size:12px;letter-spacing:2px;text-transform:uppercase;color:{ACC};font-weight:bold;">{t["eyebrow"]}</p>'
            f'<h1 style="margin:0 0 16px 0;font-size:24px;line-height:1.3;font-weight:bold;color:{INK};">{t["h1"]}</h1>'
            + p(t['intro'][0]) + p(t['intro'][1], mb=8))
    rows.append(row(head, '8px 0 18px 0'))
    if t['coupon']:
        eb, title, text, cta = t['coupon']
        rows.append(box(h2(eb, title) + p(text, 14, SOFT, 14) + btn(link('/', 'kupon'), cta), 'blush'))
    rows.append(row(h2(*t['s1']), '6px 0 4px 0'))
    for key, name, desc, price, tag in t['prods']:
        rows.append(product(IMG[key], name, link(PATH[key], CONTENT[key]), desc, price, t['buy'], tag))
    rows.append(row('', '0 0 14px 0'))
    rows.append(row(h2(*t['s2']) + p(t['s2text'], 14, SOFT, 4), '6px 0 8px 0'))
    for key, name, desc, price, tag in t['gifts']:
        rows.append(product(IMG[key], name, link(PATH[key], CONTENT[key]), desc, price, t['buy'], tag))
    rows.append(row(btn(link(t['s2btn'][0], 'vanocni-darky'), t['s2btn'][1])
                    + small(a(link(t['s2link'][0], 'darkove-poukazy'), t['s2link'][1] + ' ›'), 12), '4px 0 22px 0'))
    rows.append(row(p(t['ship'], 14, SOFT, 0), '0 0 18px 0'))
    sig = (f'<p style="margin:18px 0 4px 0;font-size:14px;line-height:1.6;color:{SOFT};">{t["regards"]}</p>'
           f'<p style="margin:0 0 2px 0;font-size:15px;font-weight:bold;color:{INK};">Stanislav Zbořil</p>'
           f'<p style="margin:0 0 14px 0;font-size:13px;line-height:1.7;color:{MUTED};">'
           f'<a href="{link("/", "podpis")}" style="color:{MUTED};text-decoration:none;">KosmetikaEva.eu</a><br />'
           f'<a href="tel:+420773905902" style="color:{MUTED};text-decoration:none;">+420 773 905 902</a> · '
           f'<a href="mailto:info@kosmetikaeva.eu" style="color:{ACC};">info@kosmetikaeva.eu</a></p>'
           + btn('https://www.facebook.com/kosmetikaevaeshop/', t['fb'], 'dark'))
    rows.append(f'<tr><td style="padding:0 0 8px 0;border-top:1px solid {LINE};">{sig}</td></tr>')
    rows.append(row(small(t['why'], 14) + small(t['op'] + a('mailto:info@kosmetikaeva.eu', 'info@kosmetikaeva.eu', MUTED), 6), '6px 0 0 0'))
    return t['subject'], wrap(rows, t['preheader'])


if __name__ == '__main__':
    here = os.path.dirname(os.path.abspath(__file__))
    out = os.path.join(here, 'out')
    os.makedirs(out, exist_ok=True)
    for lang in ('cs', 'sk'):
        subj, html = build(lang)
        name = f'{CAMPAIGN}_{lang}'
        with open(os.path.join(out, name + '.html'), 'w', encoding='utf-8') as f:
            f.write(html)
        with open(os.path.join(out, name + '_predmet.txt'), 'w', encoding='utf-8') as f:
            f.write(subj + '\n')
        print(lang, subj, len(html))
