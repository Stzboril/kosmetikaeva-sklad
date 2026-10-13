# Generátor e-mailových šablon KosmetikaEva.eu – styl C (schválený vzor: doručena dobírka CZ, 13. 10. 2026)
# Bankovní údaje se NEDÁVAJÍ do repozitáře: tokeny {{CZK_UCET}}, {{CZK_IBAN}}, {{EUR_UCET}}, {{EUR_IBAN}}, {{UCET36}}
# se doplní v prohlížeči z původních šablon při ukládání.
import json, os, urllib.parse

INK, SOFT, MUTED, LINE, BLUSH, ACC, STAR = '#1c1b29', '#3f3d4f', '#6e6c7a', '#eeedf2', '#fbf3f1', '#a3392a', '#e0a100'
FONT = 'Montserrat,Arial,Helvetica,sans-serif'
WEB = 'https://www.kosmetikaeva.eu'

def p(text, size=15, color=INK, mb=12, extra=''):
    return f'<p style="margin:0 0 {mb}px 0;font-size:{size}px;line-height:1.6;color:{color};{extra}">{text}</p>'

def small(text, mt=12):
    return f'<p style="margin:{mt}px 0 0 0;font-size:13px;line-height:1.6;color:{MUTED};">{text}</p>'

def a(href, text, color=ACC):
    return f'<a href="{href}" style="color:{color};">{text}</a>'

def btn(href, text, kind='fill'):
    if kind == 'fill':
        td = f'<td bgcolor="{ACC}" style="background:{ACC};border-radius:999px;">'
        st = f'display:inline-block;padding:12px 26px;font-size:14px;font-weight:bold;color:#ffffff;text-decoration:none;border-radius:999px;'
    elif kind == 'outline':
        td = f'<td style="border:2px solid {ACC};border-radius:999px;">'
        st = f'display:inline-block;padding:10px 24px;font-size:14px;font-weight:bold;color:{ACC};text-decoration:none;border-radius:999px;'
    else:  # dark
        td = f'<td bgcolor="{INK}" style="background:{INK};border-radius:999px;">'
        st = f'display:inline-block;padding:9px 20px;font-size:13px;font-weight:bold;color:#ffffff;text-decoration:none;border-radius:999px;'
    return (f'<table role="presentation" cellpadding="0" cellspacing="0" border="0" style="border-collapse:separate;"><tr>'
            f'{td}<a href="{href}" style="{st}">{text}</a></td></tr></table>')

def box(inner, kind='border', mb=16):
    bg = f'background:{BLUSH};' if kind == 'blush' else f'border:1px solid {LINE};'
    pad = '20px 22px' if kind == 'blush' else '18px 22px'
    return (f'<tr><td style="padding:0 0 {mb}px 0;">'
            f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="border-collapse:separate;{bg}border-radius:14px;">'
            f'<tr><td style="padding:{pad};">{inner}</td></tr></table></td></tr>')

def box_title(text, size=16):
    return f'<p style="margin:0 0 6px 0;font-size:{size}px;font-weight:bold;color:{INK};">{text}</p>'

def row(inner, pad='0 0 16px 0'):
    return f'<tr><td style="padding:{pad};">{inner}</td></tr>'

def intro(eyebrow, h1, paras, note=None):
    out = f'<p style="margin:0 0 6px 0;font-size:12px;letter-spacing:2px;text-transform:uppercase;color:{ACC};font-weight:bold;">{eyebrow}</p>'
    out += f'<h1 style="margin:0 0 16px 0;font-size:24px;line-height:1.3;font-weight:bold;color:{INK};">{h1}</h1>'
    if note:
        out += p(note, size=13, color=MUTED, mb=12)
    for i, t in enumerate(paras):
        out += p(t, mb=20 if i == len(paras) - 1 else 12)
    return f'<tr><td style="padding:8px 0 4px 0;">{out}</td></tr>'

def wrap(rows):
    return (f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse;font-family:{FONT};color:{INK};">\n'
            f'<tr><td align="center" style="padding:0;">\n'
            f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="max-width:600px;border-collapse:collapse;">\n'
            + '\n'.join(rows) +
            '\n</table>\n</td></tr>\n</table>\n')

L = {
 'cs': dict(eyebrow='Objednávka č. #ORDER_CODE#', hello='Dobrý den,',
   recap='Rekapitulace objednávky', dt='Datum a čas objednávky', num='Číslo objednávky (variabilní symbol)',
   you='Vaše údaje', note='Poznámka', name='Jméno', email='E-mail', phone='Telefon', company='Firma', addr='Doručovací adresa',
   regards='S pozdravem a přáním krásného dne', fb='Sledujte nás na Facebooku', vop=WEB + '/obchodni-podminky/',
   contact='+420 773 905 902', reply='Máte dotaz, podnět nebo připomínku? Stačí odpovědět na tento e-mail – jsme tu pro Vás.'),
 'sk': dict(eyebrow='Objednávka č. #ORDER_CODE#', hello='Dobrý deň,',
   recap='Rekapitulácia objednávky', dt='Dátum a čas objednávky', num='Číslo objednávky (variabilný symbol)',
   you='Vaše údaje', note='Poznámka', name='Meno', email='E-mail', phone='Telefón', company='Firma', addr='Doručovacia adresa',
   regards='S pozdravom a prianím krásneho dňa', fb='Sledujte nás na Facebooku', vop=WEB + '/sk/obchodni-podminky/',
   contact='+420 773 905 902', reply='Máte otázku, podnet alebo pripomienku? Stačí odpovedať na tento e-mail – sme tu pre Vás.'),
}

def kv(label, value):
    return (f'<tr><td style="padding:3px 12px 3px 0;font-size:13px;line-height:1.5;color:{MUTED};vertical-align:top;white-space:nowrap;">{label}</td>'
            f'<td style="padding:3px 0;font-size:14px;line-height:1.5;color:{INK};vertical-align:top;">{value}</td></tr>')

def kvtable(rows):
    return '<table role="presentation" cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse;">' + ''.join(rows) + '</table>'

def recap(lang):
    t = L[lang]
    head = box_title(t['recap'], 17) + kvtable([kv(t['dt'], '#ORDER_DATETIME#'), kv(t['num'], '<strong>#ORDER_CODE#</strong>')])
    rows = [row(head, '6px 0 12px 0'), row('#TEMPLATE.orderContent#', '0 0 16px 0')]
    you = box_title(t['you']) + kvtable([
        kv(t['note'], '#REMARK#'), kv(t['name'], '#DELIVERY_FULL_NAME#'), kv(t['email'], '#EMAIL#'), kv(t['phone'], '#PHONE#'),
        kv(t['company'], '#DELIVERY_COMPANY#'),
        kv(t['addr'], '#DELIVERY_STREET# #DELIVERY_HOUSE_NUMBER#<br />#DELIVERY_ADDITIONAL#<br />#DELIVERY_ZIP# #DELIVERY_CITY#')])
    rows.append(box(you, mb=22))
    return rows

def signature(lang):
    t = L[lang]
    inner = (f'<p style="margin:18px 0 4px 0;font-size:14px;line-height:1.6;color:{SOFT};">{t["regards"]}</p>'
             f'<p style="margin:0 0 2px 0;font-size:15px;font-weight:bold;color:{INK};">Stanislav Zbořil</p>'
             f'<p style="margin:0 0 14px 0;font-size:13px;line-height:1.7;color:{MUTED};">KosmetikaEva.eu<br />'
             f'<a href="tel:+420773905902" style="color:{MUTED};text-decoration:none;">+420 773 905 902</a> · '
             f'<a href="mailto:info@kosmetikaeva.eu" style="color:{ACC};">info@kosmetikaeva.eu</a> · '
             f'<a href="{WEB}/" style="color:{ACC};">www.kosmetikaeva.eu</a></p>'
             + btn('https://www.facebook.com/kosmetikaevaeshop/', t['fb'], 'dark'))
    return f'<tr><td style="padding:0 0 8px 0;border-top:1px solid {LINE};">{inner}</td></tr>'

def mailto_return(lang):
    subj = ('Odstoupení od smlouvy – objednávka ' if lang == 'cs' else 'Odstúpenie od zmluvy – objednávka ') + '#ORDER_CODE#'
    return 'mailto:info@kosmetikaeva.eu?subject=' + urllib.parse.quote(subj, safe='')

def box_return(lang):
    if lang == 'cs':
        inner = (box_title('Potřebujete zboží vrátit?')
                 + p('Jako spotřebitel můžete od smlouvy odstoupit bez udání důvodu do 14&nbsp;dnů od převzetí zboží. Dejte nám vědět tlačítkem níže a&nbsp;<strong>my Vám pošleme štítek na vrácení zboží</strong>.', 14, SOFT)
                 + btn(mailto_return('cs'), 'Chci vrátit zboží', 'outline')
                 + small('Podrobnosti najdete v&nbsp;' + a(L['cs']['vop'], 'obchodních podmínkách') + '.'))
    else:
        inner = (box_title('Potrebujete tovar vrátiť?')
                 + p('Ako spotrebiteľ môžete od zmluvy odstúpiť bez udania dôvodu do 14&nbsp;dní od prevzatia tovaru. Dajte nám vedieť tlačidlom nižšie a&nbsp;<strong>my Vám pošleme štítok na vrátenie tovaru</strong>.', 14, SOFT)
                 + btn(mailto_return('sk'), 'Chcem vrátiť tovar', 'outline')
                 + small('Podrobnosti nájdete v&nbsp;' + a(L['sk']['vop'], 'obchodných podmienkach') + '.'))
    return box(inner, mb=22)

def box_heureka(lang):
    stars = f'<span style="color:{STAR};letter-spacing:1px;">★★★★★</span>'
    if lang == 'cs':
        inner = (box_title('Byli jste spokojeni? Ohodnoťte nás ' + stars, 17)
                 + p('Pokud jste před odesláním objednávky souhlasili se zasláním dotazníku, pošle Vám ho portál Heureka během několika dní. Podívejte se případně i&nbsp;do složky Spam nebo Hromadné. Ohodnotit nás můžete také hned:', 14, SOFT, 14)
                 + btn('https://obchody.heureka.cz/kosmetikaeva-eu/recenze/', 'Ohodnotit na Heureka.cz')
                 + small('Zákazníci ze Slovenska: ' + a('https://obchody.heureka.sk/kosmetikaeva-eu/recenze/', 'ohodnotit na Heureka.sk')))
    else:
        inner = (box_title('Boli ste spokojní? Ohodnoťte nás ' + stars, 17)
                 + p('Ak ste pred odoslaním objednávky súhlasili so zaslaním dotazníka, portál Heureka Vám ho pošle v&nbsp;priebehu niekoľkých dní. Pozrite sa prípadne aj do priečinka Spam alebo Hromadné. Ohodnotiť nás môžete aj hneď:', 14, SOFT, 14)
                 + btn('https://obchody.heureka.sk/kosmetikaeva-eu/recenze/', 'Ohodnotiť na Heureka.sk')
                 + small('Zákazníci z&nbsp;Česka: ' + a('https://obchody.heureka.cz/kosmetikaeva-eu/recenze/', 'ohodnotiť na Heureka.cz')))
    return box(inner, 'blush')

def box_sleva(lang):
    if lang == 'cs':
        inner = (box_title('5&nbsp;% sleva na další nákup')
                 + p(f'Při nákupu nad 1&nbsp;500&nbsp;Kč (65&nbsp;€) zadejte v&nbsp;košíku do pole <strong>Slevový kupón</strong> kód <strong style="color:{ACC};">sleva5</strong> (na Slovensku <strong style="color:{ACC};">zľava5</strong>).', 14, SOFT, 0)
                 + small('Nakupujete pravidelně? Podívejte se na ' + a(WEB + '/sleva-10/proc-se-mam-zaregistrovat/', 'výhody registrace') + '.', 10))
    else:
        inner = (box_title('5&nbsp;% zľava na ďalší nákup')
                 + p(f'Pri nákupe nad 65&nbsp;€ zadajte v&nbsp;košíku do poľa <strong>Zľavový kupón</strong> kód <strong style="color:{ACC};">zľava5</strong>.', 14, SOFT, 0))
    return box(inner)

def phone_mail(lang):
    tel = f'<a href="tel:+420773905902" style="color:{ACC};">+420 773 905 902</a>'
    mail = f'<a href="mailto:info@kosmetikaeva.eu" style="color:{ACC};">info@kosmetikaeva.eu</a>'
    return (tel + ' nebo e-mailu ' + mail) if lang == 'cs' else (tel + ' alebo e-mailom ' + mail)

def bank_box(lang, qr_eur):
    qr = lambda f: f'<img src="{WEB}/user/documents/upload/QR%20kody%20pro%20platby/{f}" alt="QR platba" width="110" height="110" style="display:block;border:0;margin-top:8px;" />'
    if lang == 'cs':
        czk = box_title('Platba v&nbsp;Kč', 15) + kvtable([kv('Číslo účtu', '<strong>{{CZK_UCET}}</strong>'), kv('IBAN', '{{CZK_IBAN}}'), kv('SWIFT', 'AIRACZPP'), kv('Variabilní symbol', '<strong>#ORDER_CODE#</strong>')]) + qr('CZK.jpg')
        eur = box_title('Platba v&nbsp;EUR', 15) + kvtable([kv('Číslo účtu', '<strong>{{EUR_UCET}}</strong>'), kv('IBAN', '{{EUR_IBAN}}'), kv('SWIFT', 'AIRACZPP'), kv('Variabilní symbol', '<strong>#ORDER_CODE#</strong>')]) + qr(qr_eur)
        inner = box_title('Pro jistotu posíláme naše bankovní údaje', 17) + p('Banka: Air Bank', 13, MUTED, 12) + czk + '<div style="height:16px;line-height:16px;">&nbsp;</div>' + eur + small('Příjemce: Stanislav Zboril, Prilucka 4118, Zlin')
    else:
        eur = box_title('Platba v&nbsp;EUR', 15) + kvtable([kv('Číslo účtu', '<strong>{{EUR_UCET}}</strong>'), kv('IBAN', '{{EUR_IBAN}}'), kv('SWIFT', 'AIRACZPP'), kv('Variabilný symbol', '<strong>#ORDER_CODE#</strong>')]) + qr(qr_eur)
        czk = box_title('Platba v&nbsp;CZK', 15) + kvtable([kv('Číslo účtu', '<strong>{{CZK_UCET}}</strong>'), kv('IBAN', '{{CZK_IBAN}}'), kv('SWIFT', 'AIRACZPP'), kv('Variabilný symbol', '<strong>#ORDER_CODE#</strong>')]) + qr('CZK.jpg')
        inner = box_title('Pre istotu posielame naše bankové údaje', 17) + p('Banka: Air Bank', 13, MUTED, 12) + eur + '<div style="height:16px;line-height:16px;">&nbsp;</div>' + czk + small('Príjemca: Stanislav Zboril, Prilucka 4118, Zlin')
    return box(inner, 'blush', 22)

def highlight(inner, mb=16):
    return box(inner, 'blush', mb)

T = {}
S = {}
oc = '<strong>#ORDER_CODE#</strong>'

# ---------- ČESKY ----------
cs = L['cs']
T['cs3'] = [intro(cs['eyebrow'], 'Děkujeme za Vaši objednávku', [cs['hello'],
    f'Potvrzujeme přijetí Vaší objednávky č.&nbsp;{oc}. Tímto potvrzením s&nbsp;Vámi zároveň uzavíráme kupní smlouvu. Obchodní podmínky, zásady ochrany osobních údajů, formulář pro odstoupení od smlouvy a&nbsp;reklamační formulář jsme Vám již zaslali v&nbsp;rekapitulaci objednávky.',
    'Teď je to na nás – objednávku připravíme a&nbsp;pečlivě zabalíme. Někdy nám to chvilku trvá, proto děkujeme za trpělivost. Jakmile bude objednávka připravená k&nbsp;expedici, pošleme Vám e-mail a&nbsp;potom také číslo pro sledování zásilky.',
    'Máte dotaz? Jsme tu pro Vás na telefonu ' + phone_mail('cs') + '.']),
    row('#EMAIL[BILLING_METHOD=transfer].billingInfo#')] + recap('cs') + [signature('cs')]
S['cs3'] = 'Potvrzení přijetí objednávky č. #ORDER_CODE# na KosmetikaEva.eu'

T['cs42'] = [intro(cs['eyebrow'], 'Děkujeme za platbu', [cs['hello'],
    f'Děkujeme Vám za úhradu objednávky č.&nbsp;{oc}. Tímto e-mailem potvrzujeme přijetí platby a&nbsp;v&nbsp;příloze Vám zasíláme daňový doklad.'])] + recap('cs') + [signature('cs')]
S['cs42'] = 'Objednávka č. #ORDER_CODE# na KosmetikaEva.eu je zaplacena – daňový doklad'

T['cs6'] = [intro(cs['eyebrow'], 'Objednávka je připravená k&nbsp;expedici', [cs['hello'],
    f'Vaši objednávku č.&nbsp;{oc} máme připravenou k&nbsp;expedici a&nbsp;brzy ji předáme dopravci. Jakmile ji dopravce převezme, pošleme Vám také číslo, podle kterého můžete zásilku sledovat.'])] + recap('cs') + [signature('cs')]
S['cs6'] = 'Objednávka č. #ORDER_CODE# na KosmetikaEva.eu je připravena k expedici'

T['cs18'] = [intro(cs['eyebrow'], 'A už to frčí k&nbsp;Vám!', [cs['hello'],
    f'Vaši objednávku č.&nbsp;{oc} jsme předali dopravci. Ten Vás bude informovat o&nbsp;doručení, případně o&nbsp;možnosti vyzvednutí na výdejním místě.'])] + recap('cs') + [box_return('cs'), signature('cs')]
S['cs18'] = 'Objednávka č. #ORDER_CODE# na KosmetikaEva.eu byla expedována'

T['cs24'] = [intro(cs['eyebrow'], 'Těšíte se na balík? Ukážeme Vám, kde je!', [cs['hello'],
    f'Vaše zásilka s&nbsp;objednávkou č.&nbsp;{oc} je už na cestě k&nbsp;Vám. Kde se právě nachází, uvidíte po kliknutí na tlačítko.']),
    row(btn('#PACKAGE_URL#', 'Sledovat zásilku') + small('Odkaz pro sledování zásilky: #PACKAGE_URL#'), '0 0 22px 0'), signature('cs')]
S['cs24'] = 'Sledování zásilky č. #ORDER_CODE# z KosmetikaEva.eu'

def delivered(lang, invoice):
    t = L[lang]
    if lang == 'cs':
        txt = f'Vaše objednávka č.&nbsp;{oc} byla doručena. Věříme, že vše proběhlo podle Vašich představ a&nbsp;k&nbsp;Vaší spokojenosti.' + (' V&nbsp;příloze Vám zasíláme daňový doklad.' if invoice else '')
        h1 = 'Vaše objednávka je doručena'
    else:
        txt = f'Vaša objednávka č.&nbsp;{oc} bola doručená. Veríme, že všetko prebehlo podľa Vašich predstáv a&nbsp;k&nbsp;Vašej spokojnosti.' + (' V&nbsp;prílohe Vám zasielame daňový doklad.' if invoice else '')
        h1 = 'Vaša objednávka je doručená'
    return [intro(t['eyebrow'], h1, [t['hello'], txt, t['reply']]), box_heureka(lang), box_sleva(lang), box_return(lang), signature(lang)]

T['cs15'] = delivered('cs', True)
S['cs15'] = 'Objednávka č. #ORDER_CODE# na KosmetikaEva.eu byla doručena'
T['cs45'] = delivered('cs', False)
S['cs45'] = 'Objednávka č. #ORDER_CODE# na KosmetikaEva.eu byla doručena'

T['cs30'] = [intro(cs['eyebrow'], 'Nepodařilo se nám spárovat Vaši platbu', [cs['hello'],
    f'Ve Vaší objednávce č.&nbsp;{oc} jste zvolili platbu předem na účet. Rádi bychom Vám zboží poslali, ale platbu se nám zatím nepodařilo spárovat. Zkontrolujte prosím Vaši platbu, hlavně variabilní symbol a&nbsp;číslo účtu.',
    'Ozvěte se nám prosím, ať můžeme zboží co nejdříve odeslat. Pokud chcete raději zaplatit na dobírku při převzetí zboží, dejte nám také vědět.'],
    note='Tento e-mail je zasílán automaticky.'), bank_box('cs', 'EUR.jpg'), signature('cs')]
S['cs30'] = 'Prosba o pomoc se spárováním platby za objednávku č. #ORDER_CODE# na KosmetikaEva.eu'

T['cs9'] = [intro(cs['eyebrow'], 'Objednávka byla stornována', [cs['hello'],
    f'Vaši objednávku č.&nbsp;{oc} jsme stornovali, kupní smlouva tedy nebyla uzavřena.',
    'Pokud máte o zboží stále zájem, ozvěte se nám na telefonu ' + phone_mail('cs') + ' a&nbsp;vše rádi napravíme k&nbsp;Vaší spokojenosti.']), signature('cs')]
S['cs9'] = 'Storno objednávky č. #ORDER_CODE# na KosmetikaEva.eu'

T['cs36'] = [intro(cs['eyebrow'], 'Objednávku jste si nevyzvedli', [cs['hello'],
    'Obrátil jste se k&nbsp;nám zády? To nás mrzí.',
    'Na našem e-shopu jste si objednal zboží na dobírku, ale nevyzvedl jste ho. Chápeme, že o&nbsp;zboží už nemusíte mít zájem nebo Vám okolnosti vyzvednutí nedovolily. Objednáním zboží jste však uzavřel platnou kupní smlouvu, kterou jste nevyzvednutím zásilky porušil. Z&nbsp;Vaší strany také došlo k&nbsp;porušení §&nbsp;2118 odst.&nbsp;1 zákona č.&nbsp;89/2012&nbsp;Sb. (občanský zákoník). Vznikly nám tak náklady na dopravu zboží k&nbsp;Vám i&nbsp;zpět, na expedici, balné, opětovnou kontrolu zboží a&nbsp;administrativu spojenou s&nbsp;jeho naskladněním.',
    'K&nbsp;zákazníkům přistupujeme férově a&nbsp;totéž očekáváme i&nbsp;od Vás. Pokud jde o&nbsp;nedorozumění a&nbsp;objednávku si přejete doručit, kontaktujte nás na telefonu ' + phone_mail('cs') + ' – vše v&nbsp;klidu vyřešíme k&nbsp;Vaší spokojenosti.']),
    highlight(box_title('Pokud už o&nbsp;objednávku nemáte zájem') + p(f'Podle obchodních podmínek (čl.&nbsp;6.5) máme nárok na úhradu <strong>200&nbsp;Kč</strong>. Prosíme Vás o&nbsp;její zaplacení bankovním převodem na účet č.&nbsp;<strong>{{{{UCET36}}}}</strong> s&nbsp;variabilním symbolem {oc}.', 14, SOFT, 0)),
    row('#EMAIL[BILLING_METHOD=transfer].billingInfo#')] + recap('cs') + [signature('cs')]
S['cs36'] = 'Objednávka č. #ORDER_CODE# na KosmetikaEva.eu nebyla vyzvednuta'

T['cs38'] = [intro(cs['eyebrow'], 'Upomínka – nevyzvednutá objednávka', [cs['hello'],
    'Odesláním objednávky a&nbsp;jejím přijetím a&nbsp;potvrzením naším e-shopem vznikla platná kupní smlouva, která se řídí našimi ' + a(cs['vop'], 'všeobecnými obchodními podmínkami') + ' (odsouhlasil/a jste je v&nbsp;posledním kroku před odesláním objednávky) a&nbsp;platnými zákony České republiky.',
    'Náš e-shop od Vás nezaznamenal žádnou žádost o&nbsp;změnu ani storno objednávky – ani do její expedice, ani do posledního dne, kdy bylo možné zásilku vyzvednout na Vámi zvoleném výdejním místě.',
    f'Na nevyzvednutou objednávku č.&nbsp;{oc} jsme Vás již upozornili, ale v&nbsp;této věci jste s&nbsp;námi nekomunikoval/a. V&nbsp;souladu s&nbsp;obchodními podmínkami jsme proto nuceni Vám přeúčtovat náklady spojené s&nbsp;vrácením zboží ve výši <strong>200&nbsp;Kč</strong>. Přesto Vám chceme dát na výběr – zvolte prosím jednu z&nbsp;možností:']),
    box(box_title('1. Objednávku si převezmete') + p(f'Odpovězte na tento e-mail větou: „O&nbsp;objednávku č.&nbsp;#ORDER_CODE# mám zájem a&nbsp;převezmu si ji. Zvýšené náklady na dopravu uhradím předem na účet.“ Zásilku Vám pak pošleme znovu – požadujeme platbu předem na účet a&nbsp;uhradíte jen náklady na marnou přepravu. Objednávku upravíme a&nbsp;pošleme Vám potvrzení s&nbsp;platebními údaji a&nbsp;QR kódem.', 14, SOFT, 0)),
    box(box_title('2. Objednávku si nepřevezmete') + p('Nemusíte dělat nic. Během několika dní Vám pošleme fakturu na <strong>200&nbsp;Kč</strong> jako náhradu nákladů spojených s&nbsp;vrácením zboží. Pokud ji neuhradíte do data splatnosti, předáme pohledávku vymáhací agentuře a&nbsp;částka se navýší o&nbsp;poplatky za vymáhání, které činí řádově 1&nbsp;500–5&nbsp;000&nbsp;Kč. Věříme ale, že tak daleko nebudeme muset zajít.', 14, SOFT, 0), mb=12),
    row(small('V&nbsp;příloze najdete Vaši objednávku.', 0), '0 0 22px 0'), signature('cs')]
S['cs38'] = 'Upomínka – nevyzvednutá objednávka č. #ORDER_CODE# na KosmetikaEva.eu'

# ---------- SLOVENSKY ----------
sk = L['sk']
T['sk3'] = [intro(sk['eyebrow'], 'Ďakujeme za Vašu objednávku', [sk['hello'],
    f'Potvrdzujeme prijatie Vašej objednávky č.&nbsp;{oc}. Týmto potvrdením s&nbsp;Vami zároveň uzatvárame kúpnu zmluvu. Obchodné podmienky, podmienky ochrany osobných údajov, formulár na odstúpenie od zmluvy a&nbsp;reklamačný formulár sme Vám už zaslali v&nbsp;rekapitulácii objednávky.',
    'Teraz je to na nás – objednávku pripravíme a&nbsp;starostlivo zabalíme. Niekedy nám to chvíľu trvá, preto ďakujeme za trpezlivosť. Hneď ako bude objednávka pripravená na expedíciu, pošleme Vám e-mail a&nbsp;potom aj číslo na sledovanie zásielky.',
    'Máte otázku? Sme tu pre Vás na telefóne ' + phone_mail('sk') + '.']),
    row('#EMAIL[BILLING_METHOD=transfer].billingInfo#')] + recap('sk') + [signature('sk')]
S['sk3'] = 'Potvrdenie prijatia objednávky č. #ORDER_CODE# na KosmetikaEva.eu'

T['sk42'] = [intro(sk['eyebrow'], 'Ďakujeme za platbu', [sk['hello'],
    f'Ďakujeme Vám za úhradu objednávky č.&nbsp;{oc}. Týmto e-mailom potvrdzujeme prijatie platby a&nbsp;v&nbsp;prílohe Vám zasielame daňový doklad.'])] + recap('sk') + [signature('sk')]
S['sk42'] = 'Objednávka č. #ORDER_CODE# na KosmetikaEva.eu je zaplatená – daňový doklad'

T['sk6'] = [intro(sk['eyebrow'], 'Objednávka je pripravená na expedíciu', [sk['hello'],
    f'Vašu objednávku č.&nbsp;{oc} máme pripravenú na expedíciu a&nbsp;čoskoro ju odovzdáme dopravcovi. Hneď ako ju dopravca prevezme, pošleme Vám aj číslo, podľa ktorého môžete zásielku sledovať.'])] + recap('sk') + [signature('sk')]
S['sk6'] = 'Objednávka č. #ORDER_CODE# na KosmetikaEva.eu je pripravená na expedíciu'

T['sk18'] = [intro(sk['eyebrow'], 'A už to letí k&nbsp;Vám!', [sk['hello'],
    f'Vašu objednávku č.&nbsp;{oc} sme odovzdali dopravcovi. Ten Vás bude informovať o&nbsp;doručení, prípadne o&nbsp;možnosti vyzdvihnutia na výdajnom mieste.'])] + recap('sk') + [box_return('sk'), signature('sk')]
S['sk18'] = 'Objednávka č. #ORDER_CODE# na KosmetikaEva.eu bola expedovaná'

T['sk24'] = [intro(sk['eyebrow'], 'Tešíte sa na balík? Ukážeme Vám, kde je!', [sk['hello'],
    f'Vaša zásielka s&nbsp;objednávkou č.&nbsp;{oc} je už na ceste k&nbsp;Vám. Kde sa práve nachádza, uvidíte po kliknutí na tlačidlo.']),
    row(btn('#PACKAGE_URL#', 'Sledovať zásielku') + small('Odkaz na sledovanie zásielky: #PACKAGE_URL#'), '0 0 22px 0'), signature('sk')]
S['sk24'] = 'Sledovanie zásielky č. #ORDER_CODE# z KosmetikaEva.eu'

T['sk15'] = delivered('sk', True)
S['sk15'] = 'Objednávka č. #ORDER_CODE# na KosmetikaEva.eu bola doručená'
T['sk45'] = delivered('sk', False)
S['sk45'] = 'Objednávka č. #ORDER_CODE# na KosmetikaEva.eu bola doručená'

T['sk30'] = [intro(sk['eyebrow'], 'Nepodarilo sa nám spárovať Vašu platbu', [sk['hello'],
    f'Vo Vašej objednávke č.&nbsp;{oc} ste zvolili platbu vopred na účet. Radi by sme Vám tovar poslali, ale platbu sa nám zatiaľ nepodarilo spárovať. Skontrolujte prosím Vašu platbu, najmä variabilný symbol a&nbsp;číslo účtu.',
    'Ozvite sa nám prosím, aby sme mohli tovar čo najskôr odoslať. Ak chcete radšej zaplatiť na dobierku pri prevzatí tovaru, dajte nám tiež vedieť.'],
    note='Tento e-mail je zasielaný automaticky.'), bank_box('sk', 'QR_EUR.jpg'), signature('sk')]
S['sk30'] = 'Prosba o pomoc so spárovaním platby za objednávku č. #ORDER_CODE# na KosmetikaEva.eu'

T['sk9'] = [intro(sk['eyebrow'], 'Objednávka bola stornovaná', [sk['hello'],
    f'Vašu objednávku č.&nbsp;{oc} sme stornovali, kúpna zmluva teda nebola uzavretá.',
    'Ak máte o&nbsp;tovar stále záujem, ozvite sa nám na telefóne ' + phone_mail('sk') + ' a&nbsp;všetko radi napravíme k&nbsp;Vašej spokojnosti.']), signature('sk')]
S['sk9'] = 'Storno objednávky č. #ORDER_CODE# na KosmetikaEva.eu'

T['sk36'] = [intro(sk['eyebrow'], 'Objednávku ste si nevyzdvihli', [sk['hello'],
    'Otočili ste sa k&nbsp;nám chrbtom? To nás mrzí.',
    'V&nbsp;našom e-shope ste si objednali tovar na dobierku, ale nevyzdvihli ste ho. Chápeme, že o&nbsp;tovar už nemusíte mať záujem alebo Vám okolnosti vyzdvihnutie nedovolili. Objednaním tovaru ste však uzavreli platnú kúpnu zmluvu, ktorú ste nevyzdvihnutím zásielky porušili. Z&nbsp;Vašej strany tiež došlo k&nbsp;porušeniu §&nbsp;2118 ods.&nbsp;1 zákona č.&nbsp;89/2012&nbsp;Sb. (český občiansky zákonník). Vznikli nám tak náklady na dopravu tovaru k&nbsp;Vám aj späť, na expedíciu, balné, opätovnú kontrolu tovaru a&nbsp;administratívu spojenú s&nbsp;jeho naskladnením.',
    'K&nbsp;zákazníkom pristupujeme férovo a&nbsp;to isté očakávame aj od Vás. Ak ide o&nbsp;nedorozumenie a&nbsp;objednávku si želáte doručiť, kontaktujte nás na telefóne ' + phone_mail('sk') + ' – všetko v&nbsp;pokoji vyriešime k&nbsp;Vašej spokojnosti.']),
    highlight(box_title('Ak už o&nbsp;objednávku nemáte záujem') + p(f'Podľa obchodných podmienok (čl.&nbsp;6.5) máme nárok na úhradu <strong>7,60&nbsp;€</strong> (200&nbsp;Kč). Prosíme Vás o&nbsp;jej zaplatenie bankovým prevodom na účet IBAN&nbsp;<strong>{{{{EUR_IBAN}}}}</strong> s&nbsp;variabilným symbolom {oc}.', 14, SOFT, 0)),
    row('#EMAIL[BILLING_METHOD=transfer].billingInfo#')] + recap('sk') + [signature('sk')]
S['sk36'] = 'Objednávka č. #ORDER_CODE# na KosmetikaEva.eu nebola vyzdvihnutá'

T['sk38'] = [intro(sk['eyebrow'], 'Upomienka – nevyzdvihnutá objednávka', [sk['hello'],
    'Odoslaním objednávky a&nbsp;jej prijatím a&nbsp;potvrdením naším e-shopom vznikla platná kúpna zmluva, ktorá sa riadi našimi ' + a(sk['vop'], 'všeobecnými obchodnými podmienkami') + ' (odsúhlasili ste ich v&nbsp;poslednom kroku pred odoslaním objednávky) a&nbsp;platnými zákonmi Českej republiky.',
    'Náš e-shop od Vás nezaznamenal žiadnu žiadosť o&nbsp;zmenu ani storno objednávky – ani do jej expedície, ani do posledného dňa, keď bolo možné zásielku vyzdvihnúť na Vami zvolenom výdajnom mieste.',
    f'Na nevyzdvihnutú objednávku č.&nbsp;{oc} sme Vás už upozornili, ale v&nbsp;tejto veci ste s&nbsp;nami nekomunikovali. V&nbsp;súlade s&nbsp;obchodnými podmienkami sme preto nútení Vám preúčtovať náklady spojené s&nbsp;vrátením tovaru vo výške <strong>7,60&nbsp;€</strong> (200&nbsp;Kč). Napriek tomu Vám chceme dať na výber – zvoľte prosím jednu z&nbsp;možností:']),
    box(box_title('1. Objednávku si prevezmete') + p('Odpovedzte na tento e-mail vetou: „O&nbsp;objednávku č.&nbsp;#ORDER_CODE# mám záujem a&nbsp;prevezmem si ju. Zvýšené náklady na dopravu uhradím vopred na účet.“ Zásielku Vám potom pošleme znova – požadujeme platbu vopred na účet a&nbsp;uhradíte len náklady na márnu prepravu. Objednávku upravíme a&nbsp;pošleme Vám potvrdenie s&nbsp;platobnými údajmi a&nbsp;QR kódom.', 14, SOFT, 0)),
    box(box_title('2. Objednávku si neprevezmete') + p('Nemusíte robiť nič. V&nbsp;priebehu niekoľkých dní Vám pošleme faktúru na <strong>7,60&nbsp;€</strong> ako náhradu nákladov spojených s&nbsp;vrátením tovaru. Ak ju neuhradíte do dátumu splatnosti, odovzdáme pohľadávku vymáhacej agentúre a&nbsp;suma sa zvýši o&nbsp;poplatky za vymáhanie, ktoré predstavujú rádovo 60–200&nbsp;€. Veríme však, že tak ďaleko nebudeme musieť zájsť.', 14, SOFT, 0), mb=12),
    row(small('V&nbsp;prílohe nájdete Vašu objednávku.', 0), '0 0 22px 0'), signature('sk')]
S['sk38'] = 'Upomienka – nevyzdvihnutá objednávka č. #ORDER_CODE# na KosmetikaEva.eu'

os.makedirs('out', exist_ok=True)
for k, rows in T.items():
    open(f'out/{k}.html', 'w', encoding='utf-8').write(wrap(rows))
json.dump(S, open('out/predmety.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(T), 'šablon')
