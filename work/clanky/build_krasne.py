"""Zkrášlené verze článků – jednotné komponenty ke-* (styl v ke-clanky.css v HTML kódech)."""
import json, re, html, os

U = 'https://cdn.myshoptet.com/usr/www.kosmetikaeva.eu/user/documents/upload/'
O = '/home/claude/work/clanky/krasne/'
os.makedirs(O, exist_ok=True)
E = html.escape


def obal(obsah):
    # nadpis H1 vypisuje Shoptet sám (název článku) – v obsahu by byl podruhé
    obsah = re.sub(r'^\s*<h1[^>]*>.*?</h1>\s*', '', obsah.strip(), count=1, flags=re.S)
    return f'<div class="ke-clanek">\n{obsah.strip()}\n</div>'


def tlacitko(url, text):
    return f'<p class="ke-tlacitko-obal"><a class="ke-tlacitko" href="{url}">{text}</a></p>'


def seznam(polozky, cls='ke-seznam'):
    return f'<ul class="{cls}">\n' + '\n'.join(f'<li>{p}</li>' for p in polozky) + '\n</ul>'


def karty(items):
    """items: (stitek, nadpis, text)"""
    out = ['<div class="ke-mrizka">']
    for st, nad, txt in items:
        s = f'<span class="ke-karta-stitek">{st}</span>' if st else ''
        n = f'<h3>{nad}</h3>' if nad else ''
        out.append(f'<div class="ke-karta">{s}{n}<p>{txt}</p></div>')
    out.append('</div>')
    return '\n'.join(out)


def produkt(url, img, nadpis, odstavce, tl=None):
    t = '\n'.join(f'<p>{p}</p>' for p in odstavce)
    b = f'\n<p><a class="ke-tlacitko" href="{url}">{tl}</a></p>' if tl else ''
    return f"""<div class="ke-produkt">
<div class="ke-produkt-foto"><a href="{url}"><img src="{img}" alt="{E(nadpis)}" /></a></div>
<div class="ke-produkt-text">
<h3><a href="{url}">{nadpis}</a></h3>
{t}{b}
</div>
</div>"""


def tabulka(hlavicka, radky):
    th = ''.join(f'<th>{h}</th>' for h in hlavicka)
    tr = '\n'.join('<tr>' + ''.join(f'<td>{c}</td>' for c in r) + '</tr>' for r in radky)
    return f'<div class="ke-tab-obal"><table class="ke-tab">\n<thead><tr>{th}</tr></thead>\n<tbody>\n{tr}\n</tbody>\n</table></div>'


CL = {}

# ======================================================================== 155 / 198 parfémy Essens
DATA = json.load(open('/home/claude/work/clanky/parfemy_typy.json'))
ZAM = json.load(open('/home/claude/work/clanky/parfemy_zamena.json'))
from build_parfemy import norm_typ, nazev, skupina, klic, RUCNE


def parf_tab(rows, sk):
    hl = ['Parfum', 'Typ vône', 'Zákazníci si ho najčastejšie zamieňajú s'] if sk else ['Parfém', 'Typ vůně', 'Zákazníci ho nejčastěji zaměňují za']
    radky = []
    for r in sorted(rows, key=klic):
        n, lux = nazev(r)
        url = r[3] if sk else r[2]
        typ = norm_typ(r[5] if sk else r[4], sk)
        if r[0] in RUCNE and RUCNE[r[0]][0]:
            typ = 'tóny: ' + RUCNE[r[0]][1 if sk else 0]
        label = f'Essens {n}' + ((' (luxusný)' if sk else ' (luxusní)') if lux else '')
        z = ZAM.get(r[0], ['', ''])[1 if sk else 0]
        radky.append([f'<a href="{url}">{E(label)}</a>', E(typ or '–'), E(z) if z else '–'])
    return tabulka(hl, radky)


def parfemy(sk):
    pre = '/sk' if sk else ''
    g = {k: [r for r in DATA if skupina(r) == k] for k in ('zeny', 'muzi', 'unisex')}
    if sk:
        h = f"""<h1>Parfumy Essens – prehľad vôní podľa typu</h1>
<p class="ke-perex"><a href="{pre}/znacka/essens/"><img src="{U}Essens/essens parfémy.jpg" alt="parfumy Essens" width="203" height="203" style="float: right; margin: 0 0 12px 18px;" /></a>Kvalitný a dobre zvolený parfum sa stane vašou druhou kožou. Parfumy <strong>Essens</strong> obsahujú až 20 % vonných esencií a vyrábajú sa v Českej republike. V tomto sprievodcovi zistíte, ako parfum správne nanášať, čím sa líši parfum od toaletnej vody a ktorá vôňa Essens je tá vaša.</p>
<h2>Kam nanášať parfum, aby vydržal celý deň</h2>
<p>Vôňu aplikujte na tzv. <strong>pulzné body</strong> – miesta, kde je pokožka najteplejšia a vôňa sa najlepšie rozvinie:</p>
{seznam(['spánky a oblasť za ušami', 'krk a dekolt', 'vnútorná strana zápästí a lakťové jamky', 'podkolenné jamky – v lete sa vôňa krásne uvoľňuje pri chôdzi'])}
<div class="ke-box"><span class="ke-box-titulek">Tip</span><p>Parfum nestriekajte priamo na jemné tkaniny – vonné oleje by ich mohli poškodiť. S intenzitou to nepreháňajte, menej je často viac.</p></div>
<h2>Hlava, srdce a základ vône</h2>
<p>Každý parfum sa uvoľňuje postupne v troch fázach:</p>
{karty([('1. fáza', 'Hlava', 'Prvý dojem po nanesení. Je intenzívna, ale prchavá – cítite ju niekoľko minút až štvrť hodiny.'), ('2. fáza', 'Srdce', 'Charakter vône, ktorý sa rozvinie po odznení hlavy a vydrží zhruba 2–3 hodiny.'), ('3. fáza', 'Základ', 'To, čo cítite najdlhšie. Pomaly prchavé látky vydržia voňať niekoľko hodín, často celý deň.')])}
<h2>Parfum, toaletná, alebo kolínska voda?</h2>
{tabulka(['Druh', 'Podiel vonných esencií', 'Výdrž'], [['Parfum', '15–30 %', 'najdlhšia'], ['Eau de Parfum (EdP)', '8–15 %', 'dlhá'], ['Eau de Toilette (EdT)', '4–8 %', 'stredná'], ['Eau de Cologne (EdC)', '3–5 %', 'krátka, na osvieženie']])}
<div class="ke-box"><span class="ke-box-titulek">Vedeli ste?</span><p>Vône Essens obsahujú až <strong>20 % vonných esencií</strong>. Nie sú to toaletné vody, ale skutočné parfumy s dlhou výdržou.</p></div>
<h2>Ako si vybrať vôňu podľa typu</h2>
{karty([('', 'Kvetinová', 'ruža, jazmín, pivonka či konvalinka – ženská a nežná'), ('', 'Ovocná', 'broskyňa, malina alebo jablko – svieža a hravá'), ('', 'Citrusová', 'bergamot, citrón, grep – ľahká a osviežujúca'), ('', 'Drevitá', 'céder, santal, vetiver – elegantná a pokojná'), ('', 'Orientálna', 'ambra, vanilka, korenie – plná a zmyselná'), ('', 'Chyprová', 'citrusy a zemitý mach – sofistikovaná klasika'), ('', 'Fougérová', 'levanduľa, kumarín, bylinky – čistá pánska vôňa'), ('', 'Gurmánska', 'karamel, vanilka, sladké tóny – lákavá a hrejivá'), ('', 'Vodná a zelená', 'morské tóny, tráva a lístie – prirodzená sviežosť')])}
<h2>Zoznam parfumov Essens</h2>
<p>V tabuľkách nájdete všetky parfumy Essens, ktoré máme v ponuke, aj s typom vône a s tým, s akou vôňou si ich naši zákazníci najčastejšie zamieňajú. Kliknutím na názov sa dostanete na detail parfumu, kde nájdete celé zloženie vône.</p>
<h3>Dámske parfumy</h3>
{parf_tab(g['zeny'], True)}
<h3>Pánske parfumy</h3>
{parf_tab(g['muzi'], True)}
<h3>Unisex parfumy</h3>
{parf_tab(g['unisex'], True)}
{tlacitko(pre + '/znacka/essens/', 'Všetky produkty Essens')}"""
    else:
        h = f"""<h1>Parfémy Essens – přehled vůní podle typu</h1>
<p class="ke-perex"><a href="{pre}/znacka/essens/"><img src="{U}Essens/essens parfémy.jpg" alt="parfémy Essens" width="203" height="203" style="float: right; margin: 0 0 12px 18px;" /></a>Kvalitní a dobře zvolený parfém se stane vaší druhou kůží. Parfémy <strong>Essens</strong> obsahují až 20 % vonných esencí a vyrábějí se v České republice. V tomto průvodci zjistíte, jak parfém správně nanášet, čím se liší parfém od toaletní vody a která vůně Essens je ta vaše.</p>
<h2>Kam nanášet parfém, aby vydržel celý den</h2>
<p>Vůni aplikujte na tzv. <strong>pulzní body</strong> – místa, kde je pokožka nejteplejší a vůně se nejlépe rozvine:</p>
{seznam(['spánky a oblast za ušima', 'krk a dekolt', 'vnitřní strana zápěstí a loketní jamky', 'podkolenní jamky – v létě se vůně krásně uvolňuje při chůzi'])}
<div class="ke-box"><span class="ke-box-titulek">Tip</span><p>Parfém nestříkejte přímo na jemné tkaniny – vonné oleje by je mohly poškodit. S intenzitou to nepřehánějte, méně je často více.</p></div>
<h2>Hlava, srdce a základ vůně</h2>
<p>Každý parfém se uvolňuje postupně ve třech fázích:</p>
{karty([('1. fáze', 'Hlava', 'První dojem po nanesení. Je intenzivní, ale prchavá – cítíte ji několik minut až čtvrt hodiny.'), ('2. fáze', 'Srdce', 'Charakter vůně, který se rozvine po odeznění hlavy a vydrží zhruba 2–3 hodiny.'), ('3. fáze', 'Základ', 'To, co cítíte nejdéle. Pomalu prchavé látky vydrží vonět několik hodin, často celý den.')])}
<h2>Parfém, toaletní, nebo kolínská voda?</h2>
{tabulka(['Druh', 'Podíl vonných esencí', 'Výdrž'], [['Parfum (parfém)', '15–30 %', 'nejdelší'], ['Eau de Parfum (EdP)', '8–15 %', 'dlouhá'], ['Eau de Toilette (EdT)', '4–8 %', 'střední'], ['Eau de Cologne (EdC)', '3–5 %', 'krátká, na osvěžení']])}
<div class="ke-box"><span class="ke-box-titulek">Věděli jste?</span><p>Vůně Essens obsahují až <strong>20 % vonných esencí</strong>. Nejsou to toaletní vody, ale skutečné parfémy s dlouhou výdrží.</p></div>
<h2>Jak si vybrat vůni podle typu</h2>
{karty([('', 'Květinová', 'růže, jasmín, pivoňka či konvalinka – ženská a něžná'), ('', 'Ovocná', 'broskev, malina nebo jablko – svěží a hravá'), ('', 'Citrusová', 'bergamot, citron, grep – lehká a osvěžující'), ('', 'Dřevitá', 'cedr, santal, vetiver – elegantní a klidná'), ('', 'Orientální', 'ambra, vanilka, koření – plná a smyslná'), ('', 'Chyprová', 'citrusy a zemitý mech – sofistikovaná klasika'), ('', 'Fougérová', 'levandule, kumarin, bylinky – čistá pánská vůně'), ('', 'Gurmánská', 'karamel, vanilka, sladké tóny – lákavá a hřejivá'), ('', 'Vodní a zelená', 'mořské tóny, tráva a listí – přirozená svěžest')])}
<h2>Seznam parfémů Essens</h2>
<p>V tabulkách najdete všechny parfémy Essens, které máme v nabídce, i s typem vůně a s tím, za jakou vůni je naši zákazníci nejčastěji zaměňují. Kliknutím na název se dostanete na detail parfému, kde najdete celé složení vůně.</p>
<h3>Dámské parfémy</h3>
{parf_tab(g['zeny'], False)}
<h3>Pánské parfémy</h3>
{parf_tab(g['muzi'], False)}
<h3>Unisex parfémy</h3>
{parf_tab(g['unisex'], False)}
{tlacitko(pre + '/znacka/essens/', 'Všechny produkty Essens')}"""
    return obal(h)


CL['155'] = parfemy(False)
CL['198'] = parfemy(True)

# ======================================================================== 15 Aloe Vera Gel dávkování
AV = '/aloe-vera-gel/'
CL['15'] = obal(f"""<h1>Dávkování Aloe Vera Gelu</h1>
<p class="ke-perex">Nápojové gely LR LIFETAKT Aloe Vera Drinking Gel jsou doplňky stravy s vysokým podílem gelu z listů aloe vera. Jak je užívat, kolik denně a jakou příchuť si vybrat?</p>
<div class="ke-box"><span class="ke-box-titulek">Doporučené dávkování výrobce</span><span class="ke-box-velky">3× denně 30 ml</span><p>Nejlépe před jídlem, denní dávka je tedy 90 ml. Doporučenou denní dávku nepřekračujte.</p></div>
<h2>Jak gel pít</h2>
{seznam(['čistý, nebo zředěný vodou', 'lehce vychlazený i při pokojové teplotě', 'přesné pokyny k uchovávání najdete na obalu každého výrobku'])}
<h2>Časté otázky</h2>
<h3>Mohou Aloe Vera Gel pít děti, těhotné a kojící ženy?</h3>
<p>Doplňky stravy jsou určeny dospělým a je potřeba je uchovávat mimo dosah malých dětí. Pokud zvažujete podávání dítěti, nebo jste těhotná či kojíte, poraďte se nejprve s lékařem.</p>
<h3>Jak dlouho Aloe Vera Gel užívat?</h3>
<p>Gel je určený k pravidelnému každodennímu užívání. Pro delší užívání se vyplatí výhodnější série 6 × 1000 ml. Pokud užíváte léky nebo máte zdravotní potíže, poraďte se před užíváním s lékařem.</p>
<h2>Přehled příchutí</h2>
{tabulka(['Gel', 'Složení v kostce'], [
 ['<a href="/aloe-vera-gel/lr-aloe-vera-drinking-gel-honey-1000-ml/">Traditional s medem</a>', '90 % gelu z listů aloe vera, 9 % medu'],
 ['<a href="/aloe-vera-gel/lr-aloe-vera-drinking-gel-s-prichuti-broskvi-1000-ml-2/">Broskev</a>', '98 % gelu z aloe vera, broskvová příchuť, bez přidaného cukru (se sladidly)'],
 ['<a href="/aloe-vera-gel/lr-aloe-vera-drinking-gel-freedom-1000-ml-2/">Active Freedom</a>', '88 % gelu z listů aloe vera, glukosamin sulfát, chondroitin sulfát, kolagen, vitamíny C a E'],
 ['<a href="/aloe-vera-gel/lr-aloe-vera-drinking-gel-sivera-1000-ml-2/">Intense Sivera</a>', '90 % gelu z aloe vera, 7 % květového medu, extrakt z kopřivy'],
 ['<a href="/aloe-vera-gel/lr-aloe-vera-drinking-gel-immune-plus-1000-ml/">Immune Plus</a>', '85 % gelu z aloe vera, 8 % květového medu, 6 % zázvorové šťávy, vitamín C, zinek a selen']])}
<p class="ke-pozn">Doplněk stravy není náhradou pestré a vyvážené stravy a zdravého životního stylu.</p>
{tlacitko(AV, 'Všechny Aloe Vera gely')}""")

# ======================================================================== 183 Eucasol
EUC = '/esencialni-oleje/just-eucasol-sprej-50-ml/'
CL['183'] = obal(f"""<h1>Eucasol</h1>
<p class="ke-perex"><a href="{EUC}"><img src="{U}Herbar/JUST_eucasol_1.png" alt="JUST Eucasol" width="200" style="float: right; margin: 0 0 12px 18px;" /></a>Bylinný sprej od švýcarské značky JUST se svěží vůní éterických olejů – pro příjemný vzduch doma, v autě i na cestách. Patří k našim nejoblíbenějším produktům díky jednoduchému použití a výrazné vůni.</p>
<div class="ke-box"><span class="ke-box-titulek">Hlavní složky</span><p>éterické oleje z eukalyptu, rozmarýnu, máty, jalovce, smrku, borovice lesní a kleče, hřebíčku, mentol, kafr</p></div>
<h2>Charakter vůně</h2>
{karty([('', 'Eukalyptus', 'čistá, svěží a lehce kafrová vůně'), ('', 'Máta a mentol', 'chladivý, osvěžující tón'), ('', 'Rozmarýn', 'bylinná, povzbudivá vůně'), ('', 'Jehličnany', 'jalovec, smrk, borovice a kleč – vůně lesa'), ('', 'Hřebíček a kafr', 'teplý, kořenitý podtón')])}
<h2>Proč si Eucasol oblíbit</h2>
{seznam(['rychle provoní místnost a pomůže potlačit nepříjemné pachy', 'navodí svěží atmosféru doma, v kanceláři i v autě', 'příjemná vůně k večernímu odpočinku – na polštář nebo do koupele', 'nezanechává skvrny na textiliích'])}
<h2>Jak se Eucasol používá</h2>
<p>Kvůli vysoké koncentraci éterických olejů stačí 1–2 stříknutí, například:</p>
{seznam(['na kapesník, který máte během dne u sebe', 'do koupele – vodu dobře promíchejte, v teplé vodě se vůně krásně rozvine', 'do místnosti nebo do aromalampy', 'na polštář', 'na šálu nebo bundu – nejprve vyzkoušejte na nenápadném místě'])}
<div class="ke-box"><span class="ke-box-titulek">Upozornění</span><p>Eucasol není určen k nanášení přímo na kůži ani k vnitřnímu použití. Chraňte před očima a uchovávejte mimo dosah dětí.</p></div>
{tlacitko(EUC, 'Koupit Eucasol')}""")

# ======================================================================== 186 Tymiánový krém
TYM = '/telo-2/just-tymianovy-krem-100-ml/'
CL['186'] = obal(f"""<h1>Tymiánový krém</h1>
<p class="ke-perex"><a href="{TYM}"><img src="{U}Herbar/tymianovy_krem.jpg" alt="Just Tymiánový krém" width="220" style="float: right; margin: 0 0 12px 18px;" /></a>Hřejivý bylinný krém od švýcarské značky JUST s vysokým obsahem éterických olejů. Po nanesení se rozvine výrazná vůně tymiánu, eukalyptu a borovice. Oblíbený je hlavně v chladných měsících k masáži hrudníku, zad nebo chodidel.</p>
<div class="ke-box"><span class="ke-box-titulek">Hlavní složky</span><p>tymián, éterické oleje z eukalyptu, borovice, rozmarýnu a heřmánku, extrakt z citronu, kafr</p></div>
<h2>Co v krému najdete</h2>
{karty([('', 'Tymián', 'výrazná, teplá bylinná vůně typická pro tento krém'), ('', 'Rozmarýn', 'povzbudivá vůně a příjemný hřejivý pocit při masáži'), ('', 'Eukalyptus', 'svěží, čistá vůně připomínající kafr'), ('', 'Borovice', 'vůně jehličnatého lesa'), ('', 'Heřmánek', 'jemná bylinná vůně, pečuje o pokožku')])}
<h2>Proč si krém oblíbit</h2>
{seznam(['hřejivý pocit a výrazná bylinná vůně při masáži', 'ideální na chladné podzimní a zimní dny', 'příjemný večerní rituál před spaním', 'vhodný k masáži hrudníku, zad i chodidel'])}
<h2>Jak se krém používá</h2>
<ol class="ke-cisla">
<li>Malé množství krému naneste na požadované místo.</li>
<li>Jemně vmasírujte do úplného vstřebání.</li>
<li>Místo můžete zakrýt, aby se hřejivý pocit udržel déle.</li>
</ol>
<p class="ke-pozn">Nenanášejte na podrážděnou pokožku a do okolí očí.</p>
{tlacitko(TYM, 'Koupit Tymiánový krém')}""")

# ======================================================================== 57 Doplněk stravy vs. lék
CL['57'] = obal(f"""<h1>Doplněk stravy, nebo lék? V čem je rozdíl</h1>
<p class="ke-perex">Na první pohled mohou doplňky stravy a volně prodejné léky vypadat podobně – tablety, kapsle nebo tekutiny. Z pohledu zákona jde ale o úplně odlišné výrobky. Co od kterého můžete čekat?</p>
<div class="ke-mrizka">
<div class="ke-karta"><span class="ke-karta-stitek">Léčivý přípravek</span><h3>Lék</h3><p>Registruje ho Státní ústav pro kontrolu léčiv (SÚKL). Před uvedením na trh se hodnotí jeho jakost, bezpečnost a účinnost, kterou musí doložit klinické studie. Jen lék může být určen k léčbě nebo prevenci onemocnění.</p></div>
<div class="ke-karta"><span class="ke-karta-stitek">Potravina</span><h3>Doplněk stravy</h3><p>Doplňuje běžnou stravu o vitamíny, minerální látky nebo jiné látky s nutričním či fyziologickým účinkem. Není určen k léčbě a nesmí mu být připisovány vlastnosti týkající se prevence či léčby nemocí.</p></div>
</div>
<h2>Kdo doplňky stravy kontroluje</h2>
<p>Doplňky stravy dozoruje Ministerstvo zemědělství a Státní zemědělská a potravinářská inspekce. Předpisy stanovují například, které látky a v jakém množství smějí obsahovat.</p>
<div class="ke-box"><span class="ke-box-titulek">Schválená zdravotní tvrzení</span><p>Výrobce smí u doplňku stravy uvádět jen tvrzení z registru Evropské unie – například „Vitamín C přispívá k normální funkci imunitního systému“ – a to jen tehdy, když výrobek obsahuje dostatečné množství dané látky.</p></div>
<h2>Jak číst etiketu doplňku stravy</h2>
{seznam(['<strong>Doporučená denní dávka</strong> – kolik a jak často výrobek užívat; dávku nepřekračujte.', '<strong>Složení</strong> – všechny složky výrobku, seřazené podle množství.', '<strong>Obsah účinných látek v denní dávce</strong> – často i v % referenční hodnoty příjmu (RHP).', '<strong>Upozornění</strong> – např. že výrobek není náhradou pestré stravy a má se uchovávat mimo dosah dětí.'])}
<p>Pokud užíváte léky, máte zdravotní potíže, jste těhotná nebo kojíte, poraďte se před užíváním doplňku stravy s lékařem nebo lékárníkem.</p>
<h2>Příklad: Aloe Vera Drinking Gel od LR</h2>
<p>Nápojové gely LR LIFETAKT Aloe Vera Drinking Gel jsou doplňky stravy. Obsahují 85–98 % gelu z listů aloe vera a podle příchuti další složky, například med, zázvor nebo extrakt z kopřivy. Doporučená denní dávka je 3× 30 ml před jídlem – více v článku <a href="/clanky-2-2/aloe-vera-gel/">Aloe Vera Gel dávkování</a>.</p>
{tlacitko('/aloe-vera-gel/', 'Aloe Vera gely')}""")

# ======================================================================== 45 Opalování
SUN = [
    ('/opalovani/lr-aloe-vera-sun-spf-30-opalovaci-mleko-100-ml/', 'LR Aloe Vera Sun SPF 30 Opalovací mléko', 'lehké mléko na celé tělo pro běžné opalování'),
    ('/opalovani/lr-aloe-vera-sun-spf-50-opalovaci-krem-75-ml/', 'LR Aloe Vera Sun SPF 50 Opalovací krém', 'vysoká ochrana pro světlou a citlivou pokožku'),
    ('/opalovani/lr-aloe-vera-kids-sun-spf-50-opalovaci-mleko-ve-spreji-150-ml/', 'LR Aloe Vera Kids Sun SPF 50 ve spreji', 'pro děti, ve spreji se snadno nanáší'),
    ('/opalovani/just-opalovaci-mleko-spf-50-125-ml/', 'Just Opalovací mléko SPF 50', 'vysoká ochrana od švýcarské značky JUST'),
    ('/opalovani/just-opalovaci-krem-spf-30-2-x-30-ml/', 'Just Opalovací krém SPF 30 (2 × 30 ml)', 'praktické menší balení na cesty'),
    ('/opalovani/lr-aloe-vera-after-sun-kremovy-gel-po-opalovani-200-ml/', 'LR Aloe Vera After Sun Krémový gel', 'osvěžující péče po opalování, bez UV filtrů'),
    ('/opalovani/just-balzam-po-opalovani-250-ml/', 'Just Balzám po opalování', 'hydratační péče po slunění'),
]
CL['45'] = obal(f"""<h1>Jak se chránit při opalování</h1>
<p class="ke-perex"><a href="/opalovani/"><img src="{U}blobid0-2.jpg?1606131576" alt="opalování" style="float: right; margin: 0 0 12px 18px; max-width: 42%;" /></a>Sluníčko k létu patří, ale pokožku je potřeba před ním chránit. Nadměrné slunění a spálení patří k hlavním faktorům, které urychlují stárnutí pokožky a zvyšují riziko kožních onemocnění. Jak vybrat správnou ochranu?</p>
<h2>UVA a UVB – v čem je rozdíl</h2>
{karty([('Hlubší vrstvy kůže', 'UVA záření', 'Je přítomné celý den a po celý rok a podílí se na předčasném stárnutí pokožky – vráskách a pigmentových skvrnách.'), ('Povrch kůže', 'UVB záření', 'Působí na povrchové vrstvy kůže a je hlavní příčinou zarudnutí a spálení.')])}
<p>Kvalitní opalovací přípravek chrání proti oběma. Hodnota <strong>SPF</strong> udává ochranu před UVB, ochranu před UVA označuje symbol „UVA“ v kroužku.</p>
<h2>Jaký jste fototyp?</h2>
{karty([('Fototyp I', 'Velmi světlá pokožka', 'Bledá nebo pihovatá, prakticky se neopálí a snadno se spálí. Vlasy světlé nebo zrzavé.'), ('Fototyp II', 'Světlá pokožka', 'Sklon k pihám, opaluje se obtížně a často se spálí. Vlasy světlé.'), ('Fototyp III', 'Běžná pokožka', 'U nás nejčastější. Zpočátku se může spálit, pak se opálí rovnoměrně.'), ('Fototyp IV', 'Snědší pokožka', 'Rychle se opaluje a spálí se jen výjimečně. Vlasy hnědé až černé.')])}
<h2>Jaký ochranný faktor zvolit</h2>
{tabulka(['Situace', 'Doporučený faktor'], [['děti, fototyp I a II, citlivá pokožka', 'SPF 50'], ['moře, hory, jižní země, první dny na slunci', 'SPF 50'], ['fototyp III a IV při běžném letním pobytu venku', 'SPF 30'], ['miminka a malé děti', 'žádné přímé slunce – stín, oblečení, pokrývka hlavy']])}
<div class="ke-box"><span class="ke-box-titulek">Pozor na výpočty „vlastní ochranná doba × SPF“</span><p>V praxi naneseme obvykle méně přípravku, než se používá při testování, a krém se postupně stírá potem, vodou i ručníkem. Skutečná ochrana je proto nižší – dobu na slunci tímto způsobem neprodlužujte.</p></div>
<h2>Zásady bezpečného opalování</h2>
<ol class="ke-cisla">
<li>Přípravek naneste <strong>dostatečně</strong> a rovnoměrně zhruba 15–30 minut před pobytem na slunci.</li>
<li>Nanášení opakujte <strong>přibližně každé 2 hodiny</strong> a vždy po koupání, pocení nebo osušení ručníkem.</li>
<li>Opakované nanesení <strong>neprodlužuje</strong> dobu, kterou můžete na slunci bezpečně strávit – jen udržuje ochranu.</li>
<li>Mezi 11. a 15. hodinou vyhledávejte stín a noste klobouk, tričko a sluneční brýle.</li>
<li>Po opalování dopřejte pokožce hydratační péči.</li>
</ol>
<h2>Opalovací přípravky v naší nabídce</h2>
{tabulka(['Přípravek', 'Kdy se hodí'], [[f'<a href="{u}">{n}</a>', t] for u, n, t in SUN])}
{tlacitko('/opalovani/', 'Všechny opalovací přípravky')}""")

# ======================================================================== 149 Eco Mimi / Pure Mimi
EU = U + 'Eurona/'
CL['149'] = obal(f"""<h1>Péče o citlivou dětskou pokožku s Eurona Eco Mimi a Pure Mimi</h1>
<p class="ke-perex">Pokožka novorozenců a kojenců je tenčí a citlivější než pokožka dospělých a rychleji ztrácí vlhkost. Zaslouží si proto jemnou péči a šetrné prostředky – na tělo i na prádlo, které se jí dotýká.</p>
<p>Česká společnost Eurona by Cerny vyvinula pro nejmenší dvě řady: <a href="/praci-prostredky-pro-nejmensi/">Eco Mimi</a> pro praní dětského prádla a <a href="/pro-deti/">Pure Mimi</a> pro péči o pokožku. Jsou určené pro miminka od narození, děti i dospělé s citlivou pokožkou, neobsahují fosfáty, formaldehyd ani chlór a nejsou testované na zvířatech.</p>
<div class="ke-box"><span class="ke-box-titulek">Výrobky s označením Natural Product jsou</span>
{seznam(['bez parabenů', 'bez ropných derivátů', 'bez SLS/SLES (laurylsulfát sodný / laurethsulfát sodný)', 'bez barviv'])}</div>
<h2>Eco Mimi – šetrné praní pro miminka</h2>
{produkt('/praci-prostredky-pro-nejmensi/eurona-eco-mimi-0--jemny-praci-prostredek-pro-miminka--935-g/', EU + 'eco mimi sensitive 935 g.png', 'Eco Mimi 0+ Jemný prací prostředek pro miminka', ['Ekologický prací prostředek na rostlinné bázi, bez fosfátů, fosfonátů a optických zjasňovačů. Draselné mýdlo a speciální složky omezují žmolkování a prodlužují životnost prádla. Jemná vůně čerstvých hrušek a krémové ovesné kaše. Dermatologicky testováno Státním zdravotním ústavem.', '<strong>Balení:</strong> 935 g a 2 750 g (cca 100–120 pracích dávek).'], 'Zobrazit')}
{produkt('/praci-prostredky-pro-nejmensi/eurona-eco-mimi-0--jemny-praci-gel-pro-miminka--1000-ml/', EU + '5318_eurona-eco-mimi-0--jemny-praci-gel-pro-miminka--1000-ml.png', 'Eco Mimi 0+ Jemný prací gel pro miminka', ['Tekutá varianta s kokosovým a slunečnicovým olejem, inulinem a enzymy. Bez fosfátů, fosfonátů a optických zjasňovačů, s jemnou vůní hrušek a ovesné kaše. Dermatologicky testováno Státním zdravotním ústavem.', '<strong>Balení:</strong> 1000 ml – 50 pracích dávek.'], 'Zobrazit')}
{produkt('/avivaze-s-kondicionerem/eurona-eco-mimi-0--jemny-avivazni-kondicioner-pro-miminka--1000-ml/', EU + 'Avivážní kondicionér.png', 'Eco Mimi 0+ Jemný avivážní kondicionér', ['Aviváž s kondicionérem 2 v 1 pro hebké a měkké prádlo, s antistatickým účinkem a snazším žehlením. Vyrobená z obnovitelných zdrojů na rostlinné bázi.', '<strong>Balení:</strong> 1000 ml – 55 pracích dávek.'], 'Zobrazit')}
{produkt('/praci-prostredky-pro-nejmensi/eurona-eco-mimi-0--jemny-neutralizacni-roztok-pro-miminka--1000-ml/', EU + 'Neutralizační roztok.png', 'Eco Mimi 0+ Jemný neutralizační roztok', ['Přidává se do posledního máchání místo aviváže. Upravuje pH máchací lázně na hodnotu bližší pH pokožky, odstraňuje zbytky pracích prostředků a prádlo mírně změkčuje. Bez parfemace.', '<strong>Balení:</strong> 1000 ml – 33 pracích dávek.'], 'Zobrazit')}
<h2>Pure Mimi – jemná péče o pokožku</h2>
<p>Ekologicky šetrná kosmetika z obnovitelných zdrojů na rostlinné bázi s označením Natural Product.</p>
{karty([('Hlavní složka', 'Ovesný olej a výtažek', 'jemně čistí, hydratuje a vyživuje pokožku; olej má certifikát ECOCERT'), ('Hlavní složka', 'Meruňkový olej a mléko', 'zjemňují a vyživují citlivou pokožku a zanechávají ji vláčnou')])}
{produkt('/pro-deti/eurona-puremimi-jemny-myci-olej-na-zadecek-pro-miminka--150-ml/', EU + 'jemný olej pro miminka.png', 'Pure Mimi Jemný mycí olej na zadeček', ['Lehká konzistence s rostlinnými oleji pro miminka od prvních dnů. Šetrná alternativa vlhčených ubrousků při každodenní péči o zadeček. Obsahuje ovesný a meruňkový olej a vitamín E. Dermatologicky testováno Státním zdravotním ústavem.', '<strong>Balení:</strong> 150 ml.'], 'Zobrazit')}
{produkt('/pro-deti/eurona-pure-mimi-0--jemne-vlhcene-ubrousky-pro-miminka--72-ks/', EU + 'vlhčené ubrousky.jpg', 'Pure Mimi 0+ Jemné vlhčené ubrousky', ['Hypoalergenní ubrousky z přírodní viskózy s olejem z ovesných lipidů, meruňkovým mlékem, aloe vera, panthenolem a squalanem. Vhodné i na obličej, pH neutrální, biologicky odbouratelné a kompostovatelné.', '<strong>Balení:</strong> 72 ks.'], 'Zobrazit')}
<p class="ke-tlacitko-obal"><a class="ke-tlacitko" href="/praci-prostredky-pro-nejmensi/">Prací prostředky pro nejmenší</a> &nbsp; <a class="ke-tlacitko" href="/pro-deti/">Péče pro děti</a></p>""")

# ======================================================================== 131 Proč používat Euronu
CL['131'] = obal(f"""<h1>Proč používat Euronu</h1>
<p class="ke-perex"><a href="/znacka/eurona/"><img src="{EU}34600_1462443c3b.jpg" alt="Eurona" width="124" style="float: right; margin: 0 0 12px 18px;" /></a><strong>Eurona by Cerny</strong> je český výrobce ekologicky šetrné drogerie. Firmu založil Lukáš Černý v roce 2003 a vývoj, výroba i distribuce sídlí ve Lhotě u Červeného Kostelce.</p>
{karty([('Kvalita', 'Národní cena kvality', 'V roce 2017 získala společnost Eurona by Cerny ocenění v rámci Národních cen kvality ČR.'), ('Ekologie', 'EU Ecolabel', 'Výrobky jako <a href="/bile-pradlo/">White &amp; Bright</a> nebo <a href="/praci-prostredky-pro-nejmensi/">Eco Mimi</a> nesou EU Ecolabel a ekoznačku Ekologicky šetrný výrobek.'), ('Úspora', 'Koncentrované', 'Stačí jen malé množství, které se ještě dále ředí.')])}
<h2>Účinnost a šetrnost</h2>
<p>Výrobky Eurona jsou účinné a zároveň šetrné k čištěným plochám, na kterých nezanechávají stopy. Speciální čisticí prostředky vytvářejí ochrannou vrstvu, díky které je další čištění snazší. Neobsahují zbytečné přísady, jako jsou plnidla nebo drcené soli, a prací prostředky obsahují složky, které jsou šetrné k textiliím a podporují stálobarevnost.</p>
<h2>Ekologie</h2>
<p><img src="{EU}CrLC5qWXgAAXYM1.jpg" alt="EU Ecolabel" width="110" style="float: right; margin: 0 0 12px 18px;" />Výrobky Eurona jsou biologicky odbouratelné, proto se hodí i do domácností s domovní čističkou odpadních vod. Neobsahují chlór, fosfáty, formaldehyd ani perboráty.</p>
<p>Značku Ekologicky šetrný výrobek propůjčuje Ministerstvo životního prostředí ČR. Hodnotí se vliv výrobku při používání (emise, spotřeba energie, uvolňování chemických látek) i během celého životního cyklu – od spotřeby surovin při výrobě až po recyklaci obalu. Udělení značky je podmíněno certifikací nezávislou třetí stranou.</p>
<h2>Šetrnost k pokožce</h2>
<p>Řada výrobků je vhodná i pro citlivou pokožku. Tekutá mýdla obsahují aloe vera gel a hydratační složky, díky kterým pokožka po umytí nepůsobí vysušeně. Prostředky na mytí nádobí jsou hypoalergenní a obsahují aloe vera gel, některé aviváže mají hypoalergenní parfemaci.</p>
<h2>Úspora času i peněz</h2>
<p>Koncentrované přípravky znamenají menší dávky – přesné dávkování najdete na obalu podle tvrdosti vody a míry znečištění. Nemusíte z obchodu nosit těžké prací prášky a velké lahve: stačí objednat přes internet a balíček vám dovezeme až domů nebo na výdejní místo.</p>
<h2>Nákup se slevou s heslem pro hosta</h2>
<div class="ke-box"><span class="ke-box-titulek">Heslo pro hosta</span><span class="ke-box-velky">420-1568768186</span><p>S tímto heslem můžete nakupovat na stránkách <a href="https://www.euronabycerny.com/?sucl=c388138aae875bfa246d5cbb28e45927" target="_blank" rel="noopener noreferrer">Eurona</a> za zvýhodněné ceny.</p></div>
<ol class="ke-cisla">
<li>Vytvořte si objednávku na <a href="https://www.euronabycerny.com/?sucl=c388138aae875bfa246d5cbb28e45927" target="_blank" rel="noopener noreferrer">euronabycerny.com</a>.</li>
<li>Zadejte heslo pro hosta <strong>420-1568768186</strong> (pokud není vyplněné automaticky).</li>
<li>Aktuální výhody a bonusy pro nové zákazníky najdete přímo u objednávky.</li>
</ol>
<h2>Časté dotazy</h2>
<h3>Vznikají mi nějaké povinnosti?</h3>
<p>Ne. Prémiovým zákazníkům nevznikají žádné povinnosti, není potřeba mít měsíční obrat ani platit poplatky.</p>
<h3>Mohu výrobky Eurona dále prodávat?</h3>
<p>Ano, výrobky můžete libovolně prodávat nebo používat pro vlastní potřebu.</p>
<h3>Na koho se mohu obrátit s dotazem?</h3>
<p>Přímo na mě – na telefonu <a href="tel:+420773905902">773 905 902</a> (můžete poslat i SMS, zavolám zpět) nebo e-mailem na <a href="mailto:info@kosmetikaeva.eu">info@kosmetikaeva.eu</a>.</p>
{tlacitko('/znacka/eurona/', 'Všechny produkty Eurona')}""")

# ======================================================================== 177 Esence JUST
OLEJE = [
    ('Antistres', 'Antistress Activator', '/esencialni-oleje/just-antistress-activator-10-ml/', 'antistress.png', 'Hledáte chvíli klidu uprostřed rušného dne? Směs éterických olejů s jemnou, harmonizující vůní pomůže vytvořit doma příjemnou a uvolněnou atmosféru – třeba večer po náročném dni.', 'aroma'),
    ('Relax', 'Levandulový olej', '/esencialni-oleje/just-levandulovy-olej-10-ml/', 's-l1600.png', 'Jemná květinová vůně levandule se hodí k večernímu odpočinku, do relaxační koupele nebo k masáži. Klasika pro milovnice květinových vůní.', 'aroma'),
    ('Pohoda', 'Pomerančový olej', '/esencialni-oleje/just-pomerancovy-olej-10-ml/', '1013.jpg', 'Sladká a svěží vůně pomeranče navodí doma veselou, přátelskou atmosféru – když čekáte návštěvu nebo si chcete zpříjemnit sychravé odpoledne.', 'aroma'),
    ('Zklidnění', 'Gardenia Roll-on', '/esencialni-oleje/just-gardenia-roll-on-10-ml/', 'gardenia.png', 'Jemná květinová vůně pro klidný večerní rituál. Praktická v kabelce i na cestách – naneste ji před spaním na zápěstí nebo za uši.', 'rollon'),
    ('Svěžest', 'Eukalyptový olej', '/esencialni-oleje/just-eukalyptovy-olej-10-ml/', 'eucalyptus.jpg', 'Výrazná, osvěžující vůně, která provoní místnost a pomůže potlačit nepříjemné pachy. Oblíbený hlavně v zimě do aromalampy, koupele nebo sauny.', 'aroma'),
    ('Perla JUSTu', 'Olej z 31 léčivých bylin', '/esencialni-oleje/just-olej-z-31-lecivych-bylin-75-ml/', 'olejz31bylin-1.png', 'Univerzální „vše v jednom“ a jeden z nejprodávanějších produktů JUST. Bohatá bylinná vůně k masáži po sportu či fyzické práci, do koupele i do aromalampy.', 'aroma'),
    ('Povzbuzení', '3 Mint Mix', '/esencialni-oleje/just-3-mint-mix-10-ml/', '3-Mint-Mix-Essential-Oil-10-ml.png', 'Vůně tří druhů máty – svěží, chladivá a povzbudivá. Do aromalampy při práci nebo studiu, k osvěžující masáži i na cesty.', 'aroma'),
    ('Osvěžení', 'Citronový olej', '/esencialni-oleje/just-citronovy-olej-10-ml/', 'zitronen-oel.png', 'Jiskřivá citrusová vůně, která osvěží atmosféru v pracovně i v kuchyni. Hodí se do aromalampy, koupele i k masáži.', 'aroma'),
    ('Životabudič', 'Guduchi Roll-on', '/esencialni-oleje/just-guduchi-roll-on-10-ml/', 'guduchi-roll-on.jpg', 'Povzbudivá vůně, kterou máte vždy po ruce – před dlouhou cestou autem, na školení nebo poradě. Stačí nanést na zápěstí nebo za uši.', 'rollon'),
    ('Vůně lesa', 'Olej z jedle sibiřské', '/esencialni-oleje/just-olej-z-jedle-sibirske-10-ml/', 'olej z jedle sibiřské_1.png', 'Svěží, pryskyřičná vůně jehličnatého lesa. Oblíbený hlavně v zimě do aromalampy, sauny nebo koupele a k masáži po sportu.', 'aroma'),
]
pouziti_aroma = '<strong>Aromalampa / difuzér:</strong> 2 kapky do teplé vody. <strong>Koupel:</strong> 5–10 kapek s trochou mléka, smetany či medu jako emulgátorem. <strong>Masáž:</strong> 10–15 kapek do masážního oleje.'
pouziti_rollon = '<strong>Použití:</strong> kuličkou naneste na šíji, zápěstí a za uši. Jen k zevnímu použití.'
bloky = '\n'.join(produkt(url, U + 'essence JUST/' + img, f'{st}: {nm}', [txt, pouziti_aroma if typ == 'aroma' else pouziti_rollon], 'Koupit') for st, nm, url, img, txt, typ in OLEJE)
CL['177'] = obal(f"""<h1>Esence JUST: klíč k výběru</h1>
<p class="ke-perex">Éterické oleje a roll-ony švýcarské značky JUST provoní domov, zpříjemní koupel i masáž. Každá vůně má svůj charakter – podívejte se, která se hodí k vaší náladě a chvíli.</p>
{bloky}
<h2>Doporučené používání éterických olejů</h2>
{tabulka(['Použití', 'Množství', 'Poznámka'], [['Koupel', '5–10 kapek', 'podle objemu koupele'], ['Zvlhčení vzduchu, sauna', '3–4 kapky', 'podle velikosti místnosti'], ['Aromalampa', '2–5 kapek', 'podle velikosti místnosti'], ['Obklad', '2–5 kapek', 'na 2 dl vody'], ['Lokální masáž s krémem', '3–5 kapek', ''], ['Masážní olej', '10–15 kapek', 'na 50 ml olejového nosiče'], ['Pleťové tonikum', '2–5 kapek', 'na 2 dl převařené vody']])}
<p class="ke-pozn">Éterické oleje jsou určené k zevnímu použití, vždy po kapkách. Chraňte před očima a uchovávejte mimo dosah dětí.</p>
{tlacitko('/esencialni-oleje/', 'Všechny éterické oleje')}""")

# ======================================================================== 195 SK LR parfémy
LRD = [('/sk/damske-parfemy/lr-feel-comfy-edp/', 'LR Feel Comfy', 'PURE by Guido Maria Kretschmer'), ('/sk/damske-parfemy/stay-calm-edp-pro-zeny/', 'LR Stay Calm', 'Pseudonym'), ('/sk/damske-parfemy/lr-think-big-edp-pro-zeny/', 'LR Think Big', 'Marbella'), ('/sk/damske-parfemy/lr-impress-me-edp-pro-zeny/', 'LR Impress Me', 'Femme Nobless'), ('/sk/damske-parfemy/lr-be-magical-edp-pro-zeny/', 'LR Be Magical', 'Harem'), ('/sk/damske-parfemy/lr-feel-gorgeous-edp-pro-zeny/', 'LR Feel Gorgeous', 'Heart &amp; Soul'), ('/sk/parfemy/lr-feel-savage-edp-pro-zeny/', 'LR Feel Savage', 'Rockin Romance'), ('/sk/damske-parfemy/lr-feel-shiny-edp-pro-zeny/', 'LR Feel Shiny', 'Los Angeles'), ('/sk/damske-parfemy/lr-be-cheerful-edp-pro-zeny/', 'LR Be Cheerful', 'Hawaii'), ('/sk/damske-parfemy/lr-be-flirty-edp-pro-zeny-50-ml/', 'LR Be Flirty', 'Guido Maria Kretschmer for Women')]
LRP = [('/sk/panske-parfemy/lr-think-wild-edp-pro-muze/', 'LR Think Wild', 'Boston'), ('/sk/panske-parfemy/lr-get-addicted-edp-pro-muze/', 'LR Get Addicted', 'Bruce Willis Personal Edition'), ('/sk/panske-parfemy/lr-in-focus-edp-pro-muze/', 'LR In Focus', 'Niagara'), ('/sk/panske-parfemy/lr-into-jungle-edp-pro-muze/', 'LR Into Jungle', 'Jungle Man'), ('/sk/panske-parfemy/lr-no-bounds-edp-pro-muze/', 'LR No Bounds', 'Bruce Willis'), ('/sk/panske-parfemy/lr-feel-sexy-edp-pro-muze/', 'LR Feel Sexy', 'Guido Maria Kretschmer for Man'), ('/sk/panske-parfemy/lr-be-back-edp-pro-muze/', 'LR Be Back', 'Terminator')]
CL['195'] = obal(f"""<h1>Nové LR parfumy – nájdite náhradu za svoju obľúbenú vôňu</h1>
<p class="ke-perex">Značka LR Health &amp; Beauty prichádza s kolekciou nových parfumov s modernou identitou a názvami, ktoré lepšie vystihujú charakter vôní. Ak ste milovali niektorý zo starších parfumov LR, nemusíte sa ho vzdať – v tabuľke nájdete jeho nového nástupcu.</p>
<h2>Dámske parfumy</h2>
{tabulka(['Nový parfum', 'Vonia podobne ako starší parfum LR'], [[f'<a href="{u}">{n}</a>', o] for u, n, o in LRD])}
<h2>Pánske parfumy</h2>
{tabulka(['Nový parfum', 'Vonia podobne ako starší parfum LR'], [[f'<a href="{u}">{n}</a>', o] for u, n, o in LRP])}
<div class="ke-box"><span class="ke-box-titulek">Nájdite si svoju vôňu v mobile</span><p><img src="{U}qr_fragrance_finder.png" alt="QR kód" width="150" style="float: right; margin: 0 0 8px 16px;" />Naskenujte QR kód a vyberte si vôňu presne pre vás. Novinky sú skladom a pripravené potešiť vás aj vaše okolie.</p></div>
{tlacitko('/sk/parfemy/', 'Všetky parfumy')}""")

for k, v in CL.items():
    open(O + k + '.html', 'w').write(v)
    print(k, len(v))
