# Newsletter KosmetikaEva.eu – styl C (vínový akcent, karty, tlačítka se zaoblenými rohy 14 px)
# Vkládá se do Shoptetu: Marketing → Newslettery → Přidat (TinyMCE, zdrojový kód).
# Odhlášení: značka #unsubscribe# (Shoptet ji nahradí odkazem pro konkrétního příjemce).
import os

INK, SOFT, MUTED, LINE, BLUSH, ACC = '#1c1b29', '#3f3d4f', '#6e6c7a', '#eeedf2', '#fbf3f1', '#a3392a'
FONT = 'Montserrat,Arial,Helvetica,sans-serif'
WEB = 'https://www.kosmetikaeva.eu'
CDN = 'https://cdn.myshoptet.com/usr/www.kosmetikaeva.eu/user/shop/detail/'
IMG = {
    'krem': CDN + '8833-2_tymianovy-krem-kompozice-web.png?ff=1&x=423&y=318&q=85&ts=6acb411a&sg=2175fb9d',
    'olej': CDN + '11431_tymianovy-olej-kompozice-web.png?ff=1&x=423&y=318&q=85&ts=6ad30c3a&sg=2175fb9d',
    'esence': CDN + '7408_tymianovy-olej-kompozice.png?ff=1&x=423&y=318&q=85&ts=67503a85&sg=2175fb9d',
    'eucasol': CDN + '7390_eucasol-50-ml.png?ff=1&x=423&y=318&q=85&ts=6acb4118&sg=2175fb9d',
}
RADIUS = '14px'


def p(text, size=15, color=INK, mb=12, extra=''):
    return f'<p style="margin:0 0 {mb}px 0;font-size:{size}px;line-height:1.6;color:{color};{extra}">{text}</p>'


def small(text, mt=12, align='left'):
    return f'<p style="margin:{mt}px 0 0 0;font-size:12px;line-height:1.6;color:{MUTED};text-align:{align};">{text}</p>'


def a(href, text, color=ACC):
    return f'<a href="{href}" style="color:{color};">{text}</a>'


def btn(href, text, kind='fill'):
    if kind == 'fill':
        td = f'<td bgcolor="{ACC}" style="background:{ACC};border-radius:{RADIUS};">'
        st = f'display:inline-block;padding:12px 24px;font-size:14px;font-weight:bold;color:#ffffff;text-decoration:none;border-radius:{RADIUS};'
    elif kind == 'outline':
        td = f'<td style="border:2px solid {ACC};border-radius:{RADIUS};">'
        st = f'display:inline-block;padding:9px 20px;font-size:13px;font-weight:bold;color:{ACC};text-decoration:none;border-radius:{RADIUS};'
    else:  # dark
        td = f'<td bgcolor="{INK}" style="background:{INK};border-radius:{RADIUS};">'
        st = f'display:inline-block;padding:9px 20px;font-size:13px;font-weight:bold;color:#ffffff;text-decoration:none;border-radius:{RADIUS};'
    return (f'<table role="presentation" cellpadding="0" cellspacing="0" border="0" style="border-collapse:separate;"><tr>'
            f'{td}<a href="{href}" style="{st}">{text}</a></td></tr></table>')


def row(inner, pad='0 0 16px 0'):
    return f'<tr><td style="padding:{pad};">{inner}</td></tr>'


def box(inner, kind='border', mb=18):
    bg = f'background:{BLUSH};' if kind == 'blush' else f'border:1px solid {LINE};'
    return (f'<tr><td style="padding:0 0 {mb}px 0;">'
            f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="border-collapse:separate;{bg}border-radius:16px;">'
            f'<tr><td style="padding:20px 22px;">{inner}</td></tr></table></td></tr>')


def h2(eyebrow, title):
    return (f'<p style="margin:0 0 4px 0;font-size:11px;letter-spacing:2px;text-transform:uppercase;color:{ACC};font-weight:bold;">{eyebrow}</p>'
            f'<h2 style="margin:0 0 10px 0;font-size:20px;line-height:1.3;font-weight:bold;color:{INK};">{title}</h2>')


def product(img, name, href, desc, price, buy, tag=None):
    tag_html = (f'<span style="display:inline-block;margin:0 0 6px 0;padding:3px 8px;border-radius:6px;background:{ACC};color:#ffffff;'
                f'font-size:10px;font-weight:bold;letter-spacing:1px;text-transform:uppercase;">{tag}</span><br />') if tag else ''
    return (f'<tr><td style="padding:0 0 12px 0;">'
            f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="border-collapse:separate;border:1px solid {LINE};border-radius:16px;">'
            f'<tr><td width="120" valign="middle" align="center" style="padding:14px 6px 14px 14px;width:120px;">'
            f'<a href="{href}"><img src="{img}" width="110" alt="{name}" style="display:block;width:110px;max-width:110px;height:auto;border:0;" /></a></td>'
            f'<td valign="middle" style="padding:14px 16px 14px 10px;">'
            f'{tag_html}<p style="margin:0 0 4px 0;font-size:16px;font-weight:bold;line-height:1.35;"><a href="{href}" style="color:{INK};text-decoration:none;">{name}</a></p>'
            f'<p style="margin:0 0 8px 0;font-size:13px;line-height:1.55;color:{SOFT};">{desc}</p>'
            f'<p style="margin:0 0 10px 0;font-size:15px;font-weight:bold;color:{ACC};">{price}</p>'
            f'{btn(href, buy, "outline")}</td></tr></table></td></tr>')


def wrap(rows, preheader):
    pre = (f'<div style="display:none;max-height:0;overflow:hidden;opacity:0;color:transparent;font-size:1px;line-height:1px;">{preheader}</div>')
    return (pre + f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse;font-family:{FONT};color:{INK};">\n'
            f'<tr><td align="center" style="padding:0;">\n'
            f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="max-width:600px;border-collapse:collapse;">\n'
            + '\n'.join(rows) +
            '\n</table>\n</td></tr>\n</table>\n')


T = {
 'cs': dict(
   subject='Tymián a Eucasol od JUST, nový vzhled e-shopu a vánoční tipy',
   preheader='Hřejivá tymiánová péče, oblíbený Eucasol, e-shop v novém kabátě a dárky, které potěší.',
   eyebrow='Novinky z KosmetikaEva.eu · říjen 2026',
   h1='Dlouho jsme se neozvali – to napravujeme',
   intro=['Dobrý den,',
          'od teď Vám jednou za měsíc pošleme to nejzajímavější z našeho e-shopu: novinky, tipy, jak výrobky používat, a výhodné nabídky. Píšeme Vám, protože jste u nás v posledních dvou letech nakoupili – moc děkujeme!'],
   s1=('Podzimní tip', 'Bylinky od JUST na sychravé dny'),
   s1text='Když venku fouká a prší, nic nepotěší víc než vůně bylinek. Švýcarská značka JUST z tymiánu vyrábí hřejivý krém, čistý éterický olej i esenci do koupele – a k nim patří oblíbený bylinný sprej Eucasol.',
   prods=[
     ('krem', 'Tymiánový krém', WEB + '/telo-2/just-tymianovy-krem-100-ml/',
      'Hřejivý bylinný krém s tymiánem, eukalyptem, borovicí a rozmarýnem – ideální k večerní masáži hrudníku a zad.',
      '60 ml 479 Kč · 100 ml 769 Kč', None),
     ('olej', 'Tymiánový olej 10 ml', WEB + '/esencialni-oleje/just-tymianovy-olej-10-ml/',
      '100% éterický olej z divokého tymiánu (mateřídoušky) s jemnou, lehce nasládlou vůní. Do aromalampy, koupele i k masáži.',
      '799 Kč', 'Novinka'),
     ('esence', 'Tymiánová esence do koupele 75 ml', WEB + '/specialni-pece/just-tymianova-esence-75-ml/',
      'Tymián, eukalyptus, šalvěj a mandlový olej. Stačí 1–2 uzávěry do vany a celá koupelna provoní bylinkami.',
      '879 Kč', None),
     ('eucasol', 'Eucasol sprej 50 ml a 75 ml', WEB + '/esencialni-oleje/just-eucasol-sprej-50-ml/',
      'Oblíbený bylinný sprej s éterickými oleji z eukalyptu, máty, rozmarýnu a jehličnanů. Stačí jedno stříknutí na kapesník, do místnosti nebo do koupele.',
      '50 ml 529 Kč · 75 ml 695 Kč', 'Oblíbený'),
   ],
   buy='Koupit',
   article=(WEB + '/clanky-2-2/tymian-od-just-krem-olej-a-esence-do-koupele/', 'V čem se liší a jak je používat? Přečtěte si náš článek'),
   s2=('Novinka na webu', 'E-shop v novém kabátě'),
   s2text='Nabídka je přehlednější a nakupování na mobilu pohodlnější. U výrobků nově najdete ikony s hlavními vlastnostmi a hned vidíte, kolik Vám chybí do dopravy zdarma.',
   s2btn=(WEB + '/', 'Prohlédnout e-shop'),
   s3=('Vánoce 2026', 'Dárky, které potěší'),
   s3text='Na dárky je nejlepší myslet včas. Vybírat můžete z vánočních kolekcí Eurony, limitovaných edic Essens nebo oleje Zimní večer od JUST. A když si nevíte rady, potěší dárkový poukaz – pošleme ho e-mailem.',
   s3btn=(WEB + '/vyhledavani/?string=v%C3%A1no%C4%8Dn%C3%AD', 'Vánoční nabídka'),
   s3link=(WEB + '/darkove-poukazy/', 'Dárkové poukazy'),
   ship='<strong>Doprava zdarma</strong> na výdejní místa a do Z-BOXů Zásilkovny při nákupu od 2&nbsp;500&nbsp;Kč.',
   regards='S pozdravem a přáním krásného podzimu',
   fb='Sledujte nás na Facebooku',
   why='Tento e-mail dostáváte, protože jste u nás nakoupili. Pokud už o naše novinky nestojíte, odhlásit se můžete zde: #unsubscribe#',
   op='Provozovatel: Stanislav Zbořil, IČO 86963139, Přílucká 4118, 760 01 Zlín · ' ),
 'sk': dict(
   subject='Tymian a Eucasol od JUST, nový vzhľad e-shopu a vianočné tipy',
   preheader='Hrejivá tymianová starostlivosť, obľúbený Eucasol, e-shop v novom šate a darčeky, ktoré potešia.',
   eyebrow='Novinky z KosmetikaEva.eu · október 2026',
   h1='Dlho sme sa neozvali – napravujeme to',
   intro=['Dobrý deň,',
          'odteraz Vám raz za mesiac pošleme to najzaujímavejšie z nášho e-shopu: novinky, tipy, ako produkty používať, a výhodné ponuky. Píšeme Vám, pretože ste u nás v posledných dvoch rokoch nakúpili – veľmi ďakujeme!'],
   s1=('Jesenný tip', 'Bylinky od JUST na sychravé dni'),
   s1text='Keď vonku fúka a prší, nič nepoteší viac ako vôňa byliniek. Švajčiarska značka JUST z tymianu vyrába hrejivý krém, čistý éterický olej aj esenciu do kúpeľa – a k nim patrí obľúbený bylinný sprej Eucasol.',
   prods=[
     ('krem', 'Tymianový krém', WEB + '/sk/telo-2/just-tymianovy-krem-100-ml/',
      'Hrejivý bylinkový krém s tymianom, eukalyptom, borovicou a rozmarínom – ideálny na večernú masáž hrudníka a chrbta.',
      '60 ml 19,69 € · 100 ml 31,61 €', None),
     ('olej', 'Tymianový olej 10 ml', WEB + '/sk/esencialni-oleje/just-tymianovy-olej-10-ml/',
      '100 % éterický olej z divokého tymianu (materinej dúšky) s jemnou, mierne nasladlou vôňou. Do aromalampy, kúpeľa aj na masáž.',
      '32,85 €', 'Novinka'),
     ('esence', 'Tymianová esencia do kúpeľa 75 ml', WEB + '/sk/specialni-pece/just-tymianova-esence-75-ml/',
      'Tymian, eukalyptus, šalvia a mandľový olej. Stačia 1–2 uzávery do vane a celá kúpeľňa zavonia bylinkami.',
      '36,14 €', None),
     ('eucasol', 'Eucasol sprej 50 ml a 75 ml', WEB + '/sk/esencialni-oleje/just-eucasol-sprej-50-ml/',
      'Obľúbený bylinný sprej s éterickými olejmi z eukalyptu, mäty, rozmarínu a ihličnanov. Stačí jedno streknutie na vreckovku, do miestnosti alebo do kúpeľa.',
      '50 ml 21,75 € · 75 ml 28,57 €', 'Obľúbený'),
   ],
   buy='Kúpiť',
   article=(WEB + '/sk/clanky-2-2/tymian-od-just-krem-olej-a-esencia-do-kupela/', 'V čom sa líšia a ako ich používať? Prečítajte si náš článok'),
   s2=('Novinka na webe', 'E-shop v novom šate'),
   s2text='Ponuka je prehľadnejšia a nakupovanie na mobile pohodlnejšie. Pri produktoch nájdete nové ikony s hlavnými vlastnosťami a hneď vidíte, koľko Vám chýba do dopravy zadarmo.',
   s2btn=(WEB + '/sk/', 'Prezrieť e-shop'),
   s3=('Vianoce 2026', 'Darčeky, ktoré potešia'),
   s3text='Na darčeky je najlepšie myslieť včas. Vyberať môžete z vianočných kolekcií Eurony, limitovaných edícií Essens alebo oleja Zimný večer od JUST. A keď si neviete rady, poteší darčeková poukážka – pošleme ju e-mailom.',
   s3btn=(WEB + '/sk/vyhladavanie/?string=viano%C4%8Dn%C3%A1', 'Vianočná ponuka'),
   s3link=(WEB + '/sk/darkove-poukazy/', 'Darčekové poukážky'),
   ship='<strong>Doprava zadarmo</strong> na výdajné miesta a do Z-BOXov Packety pri nákupe od 120&nbsp;€.',
   regards='S pozdravom a prianím krásnej jesene',
   fb='Sledujte nás na Facebooku',
   why='Tento e-mail dostávate, pretože ste u nás nakúpili. Ak už o naše novinky nestojíte, odhlásiť sa môžete tu: #unsubscribe#',
   op='Prevádzkovateľ: Stanislav Zbořil, IČO 86963139, Přílucká 4118, 760 01 Zlín, Česká republika · '),
}


def build(lang):
    t = T[lang]
    rows = []
    head = (f'<p style="margin:0 0 6px 0;font-size:12px;letter-spacing:2px;text-transform:uppercase;color:{ACC};font-weight:bold;">{t["eyebrow"]}</p>'
            f'<h1 style="margin:0 0 16px 0;font-size:24px;line-height:1.3;font-weight:bold;color:{INK};">{t["h1"]}</h1>'
            + p(t['intro'][0]) + p(t['intro'][1], mb=8))
    rows.append(row(head, '8px 0 18px 0'))
    rows.append(row(h2(*t['s1']) + p(t['s1text'], 14, SOFT, 4), '6px 0 12px 0'))
    for key, name, href, desc, price, tag in t['prods']:
        rows.append(product(IMG[key], name, href, desc, price, t['buy'], tag))
    rows.append(row(p(a(t['article'][0], t['article'][1] + ' ›'), 14, ACC, 0, 'font-weight:bold;'), '2px 0 26px 0'))
    rows.append(box(h2(*t['s2']) + p(t['s2text'], 14, SOFT, 14) + btn(*t['s2btn']), 'blush'))
    rows.append(box(h2(*t['s3']) + p(t['s3text'], 14, SOFT, 14) + btn(*t['s3btn'])
                    + small(a(t['s3link'][0], t['s3link'][1] + ' ›'), 12)))
    rows.append(row(p(t['ship'], 14, SOFT, 0), '0 0 18px 0'))
    sig = (f'<p style="margin:18px 0 4px 0;font-size:14px;line-height:1.6;color:{SOFT};">{t["regards"]}</p>'
           f'<p style="margin:0 0 2px 0;font-size:15px;font-weight:bold;color:{INK};">Stanislav Zbořil</p>'
           f'<p style="margin:0 0 14px 0;font-size:13px;line-height:1.7;color:{MUTED};">KosmetikaEva.eu<br />'
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
        with open(os.path.join(out, f'2026-10_{lang}.html'), 'w', encoding='utf-8') as f:
            f.write(html)
        with open(os.path.join(out, f'2026-10_{lang}_predmet.txt'), 'w', encoding='utf-8') as f:
            f.write(subj + '\n')
        print(lang, subj, len(html))
