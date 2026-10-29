# Newsletter KosmetikaEva.eu – JUST: Sérum na kuperózu 30 ml, Oční sprej 18 ml, Alpský bylinný balzám 13 ml
# Majitel 29. 10. 2026: „newsletter a článek na facebooku. krem na kuperosu 30 ml, alpský balzám 13 ml, oční sprej 18 ml“
# Styl a pomocné funkce z build_newsletter.py (vínový akcent, karty, tlačítka 14 px).
# Všechny odkazy na web mají UTM (utm_source=newsletter&utm_medium=email&utm_campaign=<RRRR-MM>-cz|sk).
# Spuštění: python3 build_newsletter_just_trio.py [RRRR-MM]   (výchozí 2026-11)
import os
import sys

from build_newsletter import (ACC, INK, LINE, MUTED, SOFT, WEB, a, box, btn, h2, p, product, row, small, wrap)

CAMPAIGN = sys.argv[1] if len(sys.argv) > 1 else '2026-11'
CDN = 'https://cdn.myshoptet.com/usr/www.kosmetikaeva.eu/user/shop/detail/'
IMG = {
    'serum': CDN + '9808_serum-na-kuperosu-kompozice-web.png?ff=1&x=423&y=318&q=85&ts=6aad156c&sg=2175fb9d',
    'sprej': CDN + '7726_ocni-sprej-kompozice-web.png?ff=1&x=423&y=318&q=85&ts=6aaecd2d&sg=2175fb9d',
    'balzam': CDN + '8715_alpsky-balzam-kompozice.png?ff=1&x=423&y=318&q=85&ts=674ee46e&sg=2175fb9d',
}
PATH = {
    'serum': '/ruce-a-nohy-2/just-serum-na-kuperozu-30-ml/',
    'sprej': '/oblicej-3/just-ocni-sprej-18-ml/',
    'balzam': '/specialni-pece/just-alpsky-bylinny-balzam-13-ml/',
}


def utm(url, lang):
    sep = '&' if '?' in url else '?'
    country = 'cz' if lang == 'cs' else lang
    return f'{url}{sep}utm_source=newsletter&utm_medium=email&utm_campaign={CAMPAIGN}-{country}'


def steps(items):
    out = ''
    for i, text in enumerate(items, 1):
        out += (f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse;margin:0 0 10px 0;"><tr>'
                f'<td width="30" valign="top" style="width:30px;padding:0;">'
                f'<span style="display:inline-block;width:24px;height:24px;line-height:24px;border-radius:12px;background:{ACC};color:#ffffff;'
                f'font-size:12px;font-weight:bold;text-align:center;">{i}</span></td>'
                f'<td valign="top" style="padding:2px 0 0 6px;font-size:14px;line-height:1.55;color:{SOFT};">{text}</td></tr></table>')
    return out


T = {
 'cs': dict(
   base=WEB,
   subject='Péče na chladné dny: sérum na kuperózu, oční sprej a alpský balzám',
   preheader='Švýcarská péče JUST pro citlivou pleť, unavené oční okolí a masáž po zimní procházce.',
   eyebrow='Tipy z KosmetikaEva.eu · švýcarská péče JUST',
   h1='Venku zima, doma topení – dopřejte si víc péče',
   intro=['Dobrý den,',
          'studený vítr venku, suchý vzduch z topení doma a k tomu dlouhé večery u obrazovky. Na pleti, očích i těle je to v tomhle období znát. Vybrali jsme proto tři výrobky švýcarské značky JUST, které se do chladných dnů hodí nejvíc.'],
   s1=('Švýcarská péče JUST', 'Pro pleť, oči i tělo'),
   prods=[
     ('serum', 'Sérum na kuperózu 30 ml',
      'Lehké sérum pro citlivou pleť se sklonem ke kuperóze a začervenání. Bambucké máslo, mandlový olej, panthenol a vitamin E pleť hydratují a dodají jí pocit zklidnění, výtažky z bezu černého a úročníku pomáhají vizuálně sjednotit její tón. Ráno i večer pod krém.',
      '589 Kč', 'Novinka'),
     ('sprej', 'Oční sprej 18 ml',
      'Rychlé osvěžení pro unavené oční okolí – u počítače, v přetopené kanceláři i na cestách. Stačí 1–2 vstřiky na zavřená víčka: sprej příjemně chladí a lipozomy se světlíkem lékařským dodají pokožce vláhu. Nerozmaže make-up a hodí se i pro nositele kontaktních čoček.',
      '718 Kč', None),
     ('balzam', 'Alpský bylinný balzám 13 ml',
      'Malé balení do kapsy i kabelky s vůní alpských bylin a mentolu. Bambucké máslo, včelí vosk a deset éterických olejů – jedle, eukalyptus, levandule, tymián, máta a další. Ideální k masáži ramen a šíje po sportu nebo po dlouhé zimní procházce.',
      '675 Kč', 'Do kapsy'),
   ],
   buy='Koupit',
   s2=('Náš tip', 'Jak je zapojit do dne'),
   s2steps=['<strong>Ráno a večer:</strong> malé množství séra na vyčištěnou pleť, nechte vstřebat a pak naneste svůj běžný krém.',
            '<strong>Přes den:</strong> 1–2 vstřiky očního spreje na zavřená víčka a oči nechte asi 5 sekund zavřené.',
            '<strong>Večer:</strong> trocha balzámu k masáži ramen a šíje. Kvůli mentolu ho nanášejte mimo oblast očí.'],
   s3=('Vánoce 2026', 'Dárky vybírejte s předstihem'),
   s3text='V kategorii Vánoční dárky jsme pro Vás připravili dárkové sady a tipy na dárky. A když si nevíte rady, potěší dárkový poukaz – pošleme ho e-mailem.',
   s3btn=('/vanocni-darky/', 'Vánoční dárky'),
   s3link=('/darkove-poukazy/', 'Dárkové poukazy'),
   ship='<strong>Doprava zdarma</strong> na výdejní místa a do Z-BOXů Zásilkovny při nákupu od 2&nbsp;500&nbsp;Kč.',
   regards='S pozdravem a přáním příjemných podzimních dnů',
   fb='Sledujte nás na Facebooku',
   why='Tento e-mail dostáváte, protože jste u nás nakoupili. Pokud už o naše novinky nestojíte, odhlásit se můžete zde: #unsubscribe#',
   op='Provozovatel: Stanislav Zbořil, IČO 86963139, Přílucká 4118, 760 01 Zlín · '),
 'sk': dict(
   base=WEB + '/sk',
   subject='Starostlivosť na chladné dni: sérum na kuperózu, očný sprej a alpský balzam',
   preheader='Švajčiarska starostlivosť JUST pre citlivú pleť, unavené očné okolie a masáž po zimnej prechádzke.',
   eyebrow='Tipy z KosmetikaEva.eu · švajčiarska starostlivosť JUST',
   h1='Vonku zima, doma kúrenie – doprajte si viac starostlivosti',
   intro=['Dobrý deň,',
          'studený vietor vonku, suchý vzduch z kúrenia doma a k tomu dlhé večery pri obrazovke. Na pleti, očiach aj tele je to v tomto období poznať. Vybrali sme preto tri produkty švajčiarskej značky JUST, ktoré sa do chladných dní hodia najviac.'],
   s1=('Švajčiarska starostlivosť JUST', 'Pre pleť, oči aj telo'),
   prods=[
     ('serum', 'Sérum na kuperózu 30 ml',
      'Ľahké sérum pre citlivú pleť so sklonom ku kuperóze a začervenaniu. Bambucké maslo, mandľový olej, panthenol a vitamín E pleť hydratujú a dodajú jej pocit upokojenia, výťažky z bazy čiernej a úročníka pomáhajú vizuálne zjednotiť jej tón. Ráno aj večer pod krém.',
      '24,20 €', 'Novinka'),
     ('sprej', 'Očný sprej 18 ml',
      'Rýchle osvieženie pre unavené očné okolie – pri počítači, v prekúrenej kancelárii aj na cestách. Stačia 1–2 vstreky na zatvorené viečka: sprej príjemne chladí a lipozómy so svetlíkom lekárskym dodajú pokožke vlahu. Nerozmaže make-up a hodí sa aj pre nositeľov kontaktných šošoviek.',
      '29,50 €', None),
     ('balzam', 'Alpský bylinný balzam 13 ml',
      'Malé balenie do vrecka aj kabelky s vôňou alpských bylín a mentolu. Bambucké maslo, včelí vosk a desať éterických olejov – jedľa, eukalyptus, levanduľa, tymian, mäta a ďalšie. Ideálny na masáž ramien a šije po športe alebo po dlhej zimnej prechádzke.',
      '27,73 €', 'Do vrecka'),
   ],
   buy='Kúpiť',
   s2=('Náš tip', 'Ako ich zapojiť do dňa'),
   s2steps=['<strong>Ráno a večer:</strong> malé množstvo séra na vyčistenú pleť, nechajte vstrebať a potom naneste svoj bežný krém.',
            '<strong>Cez deň:</strong> 1–2 vstreky očného spreja na zatvorené viečka a oči nechajte asi 5 sekúnd zatvorené.',
            '<strong>Večer:</strong> trocha balzamu na masáž ramien a šije. Kvôli mentolu ho nanášajte mimo oblasti očí.'],
   s3=('Vianoce 2026', 'Darčeky vyberajte s predstihom'),
   s3text='V kategórii Vianočné darčeky sme pre Vás pripravili darčekové sady a tipy na darčeky. A keď si neviete rady, poteší darčeková poukážka – pošleme ju e-mailom.',
   s3btn=('/vanocni-darky/', 'Vianočné darčeky'),
   s3link=('/darkove-poukazy/', 'Darčekové poukážky'),
   ship='<strong>Doprava zadarmo</strong> na výdajné miesta a do Z-BOXov Packety pri nákupe od 120&nbsp;€.',
   regards='S pozdravom a prianím príjemných jesenných dní',
   fb='Sledujte nás na Facebooku',
   why='Tento e-mail dostávate, pretože ste u nás nakúpili. Ak už o naše novinky nestojíte, odhlásiť sa môžete tu: #unsubscribe#',
   op='Prevádzkovateľ: Stanislav Zbořil, IČO 86963139, Přílucká 4118, 760 01 Zlín, Česká republika · '),
}


def build(lang):
    t = T[lang]
    link = lambda path: utm(t['base'] + path, lang)  # noqa: E731
    rows = []
    head = (f'<p style="margin:0 0 6px 0;font-size:12px;letter-spacing:2px;text-transform:uppercase;color:{ACC};font-weight:bold;">{t["eyebrow"]}</p>'
            f'<h1 style="margin:0 0 16px 0;font-size:24px;line-height:1.3;font-weight:bold;color:{INK};">{t["h1"]}</h1>'
            + p(t['intro'][0]) + p(t['intro'][1], mb=8))
    rows.append(row(head, '8px 0 18px 0'))
    rows.append(row(h2(*t['s1']), '6px 0 4px 0'))
    for key, name, desc, price, tag in t['prods']:
        rows.append(product(IMG[key], name, link(PATH[key]), desc, price, t['buy'], tag))
    rows.append(row('', '0 0 14px 0'))
    rows.append(box(h2(*t['s2']) + steps(t['s2steps']), 'blush'))
    rows.append(box(h2(*t['s3']) + p(t['s3text'], 14, SOFT, 14) + btn(link(t['s3btn'][0]), t['s3btn'][1])
                    + small(a(link(t['s3link'][0]), t['s3link'][1] + ' ›'), 12)))
    rows.append(row(p(t['ship'], 14, SOFT, 0), '0 0 18px 0'))
    sig = (f'<p style="margin:18px 0 4px 0;font-size:14px;line-height:1.6;color:{SOFT};">{t["regards"]}</p>'
           f'<p style="margin:0 0 2px 0;font-size:15px;font-weight:bold;color:{INK};">Stanislav Zbořil</p>'
           f'<p style="margin:0 0 14px 0;font-size:13px;line-height:1.7;color:{MUTED};">'
           f'<a href="{link("/")}" style="color:{MUTED};text-decoration:none;">KosmetikaEva.eu</a><br />'
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
        name = f'{CAMPAIGN}_just-trio_{lang}'
        with open(os.path.join(out, name + '.html'), 'w', encoding='utf-8') as f:
            f.write(html)
        with open(os.path.join(out, name + '_predmet.txt'), 'w', encoding='utf-8') as f:
            f.write(subj + '\n')
        print(lang, subj, len(html))
