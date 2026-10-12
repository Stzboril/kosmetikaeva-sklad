"""Část 2: články 45, 149 (přepis), 131, 177, 195 (úpravy)."""
import json, re, os
from build_ostatni import nahrad, nahrad_text_p, smaz_blok, P, O, CDN

META = {}
E = CDN + 'Eurona/'

# ---------------------------------------------------------------- 45 Opalování
SUN = {
    'lr30': ('/opalovani/lr-aloe-vera-sun-spf-30-opalovaci-mleko-100-ml/', 'LR Aloe Vera Sun SPF 30 Opalovací mléko', 'lehké mléko na celé tělo pro běžné opalování'),
    'lr50': ('/opalovani/lr-aloe-vera-sun-spf-50-opalovaci-krem-75-ml/', 'LR Aloe Vera Sun SPF 50 Opalovací krém', 'vysoká ochrana pro světlou a citlivou pokožku, na obličej i tělo'),
    'kids': ('/opalovani/lr-aloe-vera-kids-sun-spf-50-opalovaci-mleko-ve-spreji-150-ml/', 'LR Aloe Vera Kids Sun SPF 50 Opalovací mléko ve spreji', 'pro děti, ve spreji se snadno a rychle nanáší'),
    'after': ('/opalovani/lr-aloe-vera-after-sun-kremovy-gel-po-opalovani-200-ml/', 'LR Aloe Vera After Sun Krémový gel po opalování', 'osvěžující péče po opalování, neobsahuje UV filtry'),
    'just50': ('/opalovani/just-opalovaci-mleko-spf-50-125-ml/', 'Just Opalovací mléko SPF 50', 'vysoká ochrana od švýcarské značky JUST'),
    'just30': ('/opalovani/just-opalovaci-krem-spf-30-2-x-30-ml/', 'Just Opalovací krém SPF 30 (2 × 30 ml)', 'praktické menší balení na cesty'),
    'balzam': ('/opalovani/just-balzam-po-opalovani-250-ml/', 'Just Balzám po opalování', 'hydratační péče po slunění'),
}
li = '\n'.join(f'<li><a class="odkaz" href="{u}">{n}</a> – {t}</li>' for u, n, t in SUN.values())
c45 = f"""<p>Sluníčko k létu patří, ale pokožku je potřeba před ním chránit. Dermatologové se shodují, že nadměrné vystavování slunci a spálení patří mezi hlavní faktory, které urychlují stárnutí pokožky a zvyšují riziko kožních onemocnění. Správně zvolený a správně nanesený opalovací přípravek proto patří do každé letní tašky.</p>
<p>Sluneční záření obsahuje kromě viditelného světla také infračervené záření, které cítíme jako teplo, a ultrafialové (UV) záření. Právě UV záření je pro pokožku nejdůležitější – dělí se na UVA, UVB a UVC (to zachytí atmosféra).</p>
<h2>UVA a UVB – v čem je rozdíl</h2>
<p><strong>UVA</strong> – proniká hlouběji do kůže, je přítomné po celý den a v každém ročním období a podílí se na předčasném stárnutí pokožky (vrásky, pigmentové skvrny).</p>
<p><strong>UVB</strong> – působí na povrchové vrstvy kůže a je hlavní příčinou zarudnutí a spálení.</p>
<p>Kvalitní opalovací přípravek proto musí chránit proti oběma typům záření. Hodnota <strong>SPF</strong> udává ochranu před UVB, ochranu před UVA označuje symbol „UVA“ v kroužku.</p>
<h2>Jaký jste fototyp?</h2>
<p>Fototyp popisuje, jak vaše pokožka reaguje na slunce. Čím je pokožka světlejší a citlivější, tím vyšší ochranu potřebuje.</p>
<p><a href="/opalovani/"><img src='{CDN}blobid0-2.jpg?1606131576' alt="opalování a ochrana pokožky" style="float: right; margin: 0 0 10px 15px; max-width: 45%;" /></a><strong>Fototyp I</strong> – velmi světlá, bledá nebo pihovatá pokožka, která se prakticky neopálí a na slunci se snadno spálí. Vlasy bývají světlé nebo zrzavé.</p>
<p><strong>Fototyp II</strong> – světlá pokožka se sklonem k pihám, opaluje se obtížně a často se spálí. Vlasy bývají světlé.</p>
<p><strong>Fototyp III</strong> – u nás nejběžnější typ. Pokožka se zpočátku může spálit, ale postupně se opálí rovnoměrně. Vlasy od tmavě blond po hnědé.</p>
<p><strong>Fototyp IV</strong> – snědší pokožka, která se rychle opaluje a spálí se jen výjimečně. Vlasy hnědé až černé.</p>
<h2>Jaký ochranný faktor zvolit</h2>
<ul>
<li><strong>SPF 50</strong> – děti, fototyp I a II, citlivá pokožka, pobyt u moře, na horách a v jižních zemích, první dny na slunci.</li>
<li><strong>SPF 30</strong> – fototyp III a IV při běžném letním pobytu venku.</li>
<li>Miminka a malé děti by neměly být vystavovány přímému slunci vůbec – chraňte je stínem, oblečením a pokrývkou hlavy.</li>
</ul>
<p>Pozor na výpočty typu „vlastní ochranná doba × SPF“. V praxi naneseme obvykle méně přípravku, než se používá při testování, a krém se postupně stírá potem, vodou i ručníkem. Skutečná ochrana je proto nižší a dobu na slunci tímto způsobem neprodlužujte.</p>
<h2>Zásady bezpečného opalování</h2>
<ul>
<li>Přípravek naneste <strong>dostatečně</strong> a rovnoměrně zhruba 15–30 minut před pobytem na slunci.</li>
<li>Nanášení opakujte <strong>přibližně každé 2 hodiny</strong> a vždy po koupání, pocení nebo osušení ručníkem.</li>
<li>Opakované nanesení <strong>neprodlužuje</strong> dobu, kterou můžete na slunci bezpečně strávit – jen udržuje ochranu.</li>
<li>Mezi 11. a 15. hodinou vyhledávejte stín a noste klobouk, tričko a sluneční brýle.</li>
<li>Po opalování dopřejte pokožce hydratační péči.</li>
</ul>
<h2>Opalovací přípravky v naší nabídce</h2>
<ul>
{li}
</ul>
<p>Všechny přípravky najdete v kategorii <a class="odkaz" href="/opalovani/">Opalování</a>.</p>"""
META['45'] = dict(title='Jak se chránit při opalování',
                  metaTitle='Jak se chránit při opalování – SPF a fototyp',
                  metaDescription='Jak vybrat opalovací krém podle fototypu, rozdíl mezi UVA a UVB, jaké SPF zvolit a zásady bezpečného opalování. Přehled opalovací kosmetiky LR a Just.')
open(O + '45.html', 'w').write(c45)

# ---------------------------------------------------------------- 149 Eco Mimi / Pure Mimi (přepis se zachováním obrázků)
def blok(nadpis, url, img, texty):
    t = '\n'.join(texty)
    return f"""<table style="width: 100%;">
<tbody>
<tr><td colspan="2"><h3><a href="{url}">{nadpis}</a></h3></td></tr>
<tr>
<td style="width: 30%; vertical-align: top;"><a href="{url}"><img class="h" src='{img}' alt="{nadpis}" style="max-width: 100%;" /></a></td>
<td style="vertical-align: top;">
{t}
</td>
</tr>
</tbody>
</table>"""

F = f"<img src='{CDN}fajfka.png' alt=\"\" width=\"16\" />"
c149 = f"""<p style="text-align: justify;">Když žena přivede na svět nový život, je to jeden z největších a nejkrásnějších zázraků přírody. Pokožka novorozenců a kojenců je tenčí a citlivější než pokožka dospělých a rychleji ztrácí vlhkost. Proto si zaslouží jemnou péči a šetrné prostředky – na tělo i na prádlo, které se jí dotýká.</p>
<h2>Jak o dětskou pokožku pečovat?</h2>
<p style="text-align: justify;">Česká společnost Eurona by Cerny vyvinula pro nejmenší dvě speciální řady: <a title="Eurona Eco Mimi" href="/praci-prostredky-pro-nejmensi/">Eco Mimi</a> pro praní dětského prádla a <a title="Eurona Pure Mimi" href="/pro-deti/">Pure Mimi</a> pro péči o pokožku. Obě řady jsou určeny pro miminka od narození, děti i dospělé s citlivou pokožkou. Výrobky neobsahují fosfáty, formaldehyd ani chlór a nejsou testovány na zvířatech.</p>
<p><img class="h" style="display: block; margin-left: auto; margin-right: auto;" src='{E}eurona bez-chemie.png' alt="Eurona bez zbytečné chemie" /></p>
<p><img class="h" style="display: block; margin-left: auto; margin-right: auto;" src='{E}Eurona Natural product.png' alt="Eurona Natural Product" /></p>
<p>Výrobky označené značkou „NATURAL PRODUCT“ jsou:</p>
<p>{F} bez parabenů</p>
<p>{F} bez ropných derivátů</p>
<p>{F} bez SLS/SLES (laurylsulfát sodný / laurethsulfát sodný)</p>
<p>{F} bez barviv</p>
<h2>Eco Mimi – šetrné praní pro miminka</h2>
<p><a href="/praci-prostredky-pro-nejmensi/"><img class="h" src='{E}ecomimi.png' alt="Eurona Eco Mimi" /></a></p>
{blok('Eurona Eco Mimi 0+ Jemný prací prostředek pro miminka', '/praci-prostredky-pro-nejmensi/eurona-eco-mimi-0--jemny-praci-prostredek-pro-miminka--935-g/', E + 'eco mimi sensitive 935 g.png', [
 '<p>Ekologický prací prostředek na prádlo miminek, dětí i dospělých s citlivou pokožkou. Vyrobený z obnovitelných zdrojů na rostlinné bázi, bez fosfátů, fosfonátů a optických zjasňovačů. Obsahuje draselné mýdlo a složky, které omezují žmolkování a prodlužují životnost prádla. Jemná vůně čerstvých hrušek a krémové ovesné kaše. Účinný na dětské nečistoty a přitom šetrný.</p>',
 '<p>Dermatologicky testováno Státním zdravotním ústavem.</p>',
 '<p><strong>Speciální složky:</strong> draselné mýdlo, celulóza (brání zpětnému usazování nečistot), inulin z čekanky (chrání vlákna před nečistotami), perkarbonát sodný (bělicí složka), enzymy.</p>',
 '<p>Balení: 935 g a 2 750 g (2 750 g vystačí přibližně na 100–120 pracích dávek).</p>'])}
{blok('Eurona Eco Mimi 0+ Jemný prací gel pro miminka, 1000 ml', '/praci-prostredky-pro-nejmensi/eurona-eco-mimi-0--jemny-praci-gel-pro-miminka--1000-ml/', E + '5318_eurona-eco-mimi-0--jemny-praci-gel-pro-miminka--1000-ml.png', [
 '<p>Ekologický prací gel na prádlo miminek, dětí i dospělých s citlivou pokožkou. Vyrobený z obnovitelných zdrojů na rostlinné bázi, bez fosfátů, fosfonátů a optických zjasňovačů. Jemná vůně čerstvých hrušek a krémové ovesné kaše.</p>',
 '<p>Dermatologicky testováno Státním zdravotním ústavem.</p>',
 '<p><strong>Speciální složky:</strong> kokosový olej, draselné mýdlo, slunečnicový olej, inulin, enzymy.</p>',
 '<p>Balení: 1000 ml – 50 pracích dávek.</p>'])}
{blok('Eurona Eco Mimi 0+ Jemný avivážní kondicionér pro miminka, 1000 ml', '/avivaze-s-kondicionerem/eurona-eco-mimi-0--jemny-avivazni-kondicioner-pro-miminka--1000-ml/', E + 'Avivážní kondicionér.png', [
 '<p>Ekologická aviváž s kondicionérem 2 v 1 pro hebké a měkké prádlo. Má antistatický účinek a usnadňuje žehlení. Vyrobená z obnovitelných zdrojů na rostlinné bázi. Jemná vůně čerstvých hrušek a krémové ovesné kaše.</p>',
 '<p><strong>Speciální složky:</strong> složka z palmových semen s certifikací RSPO (zjemňuje prádlo), hemisqualan z cukrové třtiny, propanediol z kukuřičného cukru, kyselina mléčná.</p>',
 '<p>Balení: 1000 ml – 55 pracích dávek.</p>'])}
{blok('Eurona Eco Mimi 0+ Jemný neutralizační roztok pro miminka, 1000 ml', '/praci-prostredky-pro-nejmensi/eurona-eco-mimi-0--jemny-neutralizacni-roztok-pro-miminka--1000-ml/', E + 'Neutralizační roztok.png', [
 '<p>Ekologický prostředek pro velmi citlivou pokožku. Upravuje pH máchací lázně na hodnotu bližší pH lidské pokožky, odstraňuje zbytky pracích prostředků z prádla a mírně ho změkčuje i bez aviváže. Neobsahuje parfemaci.</p>',
 '<p>Přidává se do posledního máchání místo aviváže. Vhodný na všechny druhy prádla.</p>',
 '<p>Balení: 1000 ml – 33 pracích dávek.</p>'])}
<h2>Pure Mimi – jemná péče o pokožku</h2>
<p><a href="/pro-deti/"><img class="h" src='{E}puremimi.png' alt="Eurona Pure Mimi" /></a></p>
<p>Řada <a href="/pro-deti/">Pure Mimi</a> je ekologicky šetrná kosmetika pro miminka od narození, děti i dospělé s citlivou pokožkou. Výrobky jsou vyrobené z obnovitelných zdrojů na rostlinné bázi a nesou označení Natural Product.</p>
<h3>Hlavní složky řady Pure Mimi</h3>
<p><strong>Ovesný olej a ovesný výtažek</strong> – jemně čistí, hydratuje a vyživuje pokožku. Olej má certifikát ECOCERT.</p>
<p><strong>Meruňkový olej a meruňkové mléko</strong> – zjemňují a vyživují citlivou pokožku a zanechávají ji vláčnou.</p>
{blok('Eurona Pure Mimi Jemný mycí olej na zadeček pro miminka, 150 ml', '/pro-deti/eurona-puremimi-jemny-myci-olej-na-zadecek-pro-miminka--150-ml/', E + 'jemný olej pro miminka.png', [
 '<p>Jemné složení s lehkou konzistencí a rostlinnými oleji pro miminka od prvních dnů. Šetrná alternativa vlhčených ubrousků při každodenní péči o zadeček – jemně odstraní nečistoty a pokožku nezatíží.</p>',
 '<p>Dermatologicky testováno Státním zdravotním ústavem.</p>',
 '<p><strong>Speciální složky:</strong> ovesný olej, meruňkový olej, antioxidanty včetně vitamínu E, jemné aroma sladkých meruněk.</p>',
 '<p>Balení: 150 ml.</p>'])}
{blok('Eurona Pure Mimi 0+ Jemné vlhčené ubrousky pro miminka, 72 ks', '/pro-deti/eurona-pure-mimi-0--jemne-vlhcene-ubrousky-pro-miminka--72-ks/', E + 'vlhčené ubrousky.jpg', [
 '<p>Hypoalergenní vlhčené ubrousky z přírodní viskózy s hebkou texturou. Obsahují olej z ovesných lipidů, meruňkové mléko, aloe vera, panthenol, squalane a antioxidanty. Jemně čistí, hydratují a zanechávají pokožku vláčnou bez pocitu mastnoty. Vhodné i na obličej, pH neutrální.</p>',
 '<p>Biologicky odbouratelné a kompostovatelné. Dermatologicky testováno Státním zdravotním ústavem.</p>',
 '<p><strong>Speciální složky:</strong> viskóza ze dřeva s certifikací PEFC, ovesný olej s certifikací ECOCERT, meruňkové mléko, aloe vera, squalane, panthenol, antioxidanty.</p>',
 '<p>Balení: 72 ks.</p>'])}
<p>Celou nabídku najdete v kategoriích <a class="odkaz" href="/praci-prostredky-pro-nejmensi/">Prací prostředky pro nejmenší</a> a <a class="odkaz" href="/pro-deti/">Pro děti</a>.</p>"""
META['149'] = dict(title='Péče o citlivou dětskou pokožku s Eurona Eco Mimi a Pure Mimi',
                   metaTitle='Eurona Eco Mimi a Pure Mimi – péče o miminka',
                   metaDescription='Šetrné praní dětského prádla s Eurona Eco Mimi a jemná péče o pokožku miminek s Pure Mimi. Přehled výrobků, složení a balení na KosmetikaEva.eu.')
open(O + '149.html', 'w').write(c149)

# ---------------------------------------------------------------- 131 Proč používat Euronu (úpravy)
h = open(P + '131.html').read()
h = nahrad(h, 'V roce 2017 společnost Eurona by Cerny získala prestižní ocenění Národních cen kvality, které udílí Rada kvality ve spolupráci s Ministerstvem životního prostředí, obchodu a průmyslu.',
           'V roce 2017 získala společnost Eurona by Cerny ocenění v rámci Národních cen kvality ČR.')
h = nahrad(h, 'Díky tomu stačí oproti komerčním prostředkům jen minimální množství se stejnými, mnohdy lepšími výsledky čištění a praní.',
           'Díky tomu stačí na čištění i praní jen malé množství přípravku.')
h = nahrad(h, 'tak během životní cyklus výrobku (např. spotřeba energie a surovin při výrobu nebo zda a jak se dá recyklovat)',
           'tak během celého životního cyklu výrobku (např. spotřeba energie a surovin při výrobě nebo zda a jak se dá recyklovat)')
h = nahrad(h, 'Udělení značky je podmíněno certifikaci produktu', 'Udělení značky je podmíněno certifikací produktu')
h = nahrad(h, '<h2>Zdravotní nezávadnost</h2>', '<h2>Šetrnost k pokožce</h2>')
h = nahrad_text_p(h, 'Výrobky jsou vhodné pro alergiky,',
                  'Řada výrobků je vhodná i pro citlivou pokožku. Tekutá mýdla obsahují aloe vera gel a další hydratační složky, díky kterým pokožka po umytí nepůsobí vysušeně. Prostředky na mytí nádobí jsou hypoalergenní a obsahují aloe vera gel. Některé aviváže mají hypoalergenní parfemaci.')
h = nahrad(h, '<h2>&nbsp;</h2>\n', '')
h = nahrad_text_p(h, 'jsou velmi koncentrované, proto k&nbsp;dokonalému',
                  'jsou koncentrované, proto stačí jen malé množství, které se ještě dále ředí. Přesné dávkování najdete na obalu podle tvrdosti vody a míry znečištění. Díky tomu nemusíte z obchodu nosit těžké prací prášky a velké lahve – stačí udělat objednávku přes internet a balíček vám dovezeme až domů nebo na výdejní místo.')
h = smaz_blok(h, '<h2 style="text-align: left;">Srovnání', '</table>')
h = nahrad(h, '<p>* S heselm pro hosta&nbsp;', '<p>S heslem pro hosta&nbsp;')
h = nahrad(h, 'nebu problému', 'nebo problému')
h = nahrad(h, 'Kontaktujte mne na telefonním čísle', 'Kontaktujte mě na telefonním čísle')
h = nahrad(h, 'obraťte se přímo na mne buď na tel.', 'obraťte se přímo na mě, buď na tel.')
assert 'Ariel' not in h and 'Persil' not in h and 'alergik' not in h
open(O + '131.html', 'w').write(h)
META['131'] = dict(title='Proč používat Euronu',
                   metaTitle='Proč používat Euronu – český výrobce drogerie',
                   metaDescription='Eurona by Cerny je český výrobce ekologicky šetrné drogerie s certifikací EU Ecolabel. Koncentrované přípravky, šetrnost k pokožce i přírodě.')

# ---------------------------------------------------------------- 177 Esence JUST (úpravy textů)
h = open(P + '177.html').read()
TEXTY = [
    ('Máte pocit, že jste dlouhodobě ve stresu', 'Hledáte chvíli klidu uprostřed rušného dne? Antistress Activator je směs éterických olejů s jemnou, harmonizující vůní. Pomůže vám vytvořit doma příjemnou a uvolněnou atmosféru – třeba večer po náročném dni nebo před důležitou schůzkou, kdy si chcete na chvíli vydechnout.'),
    ('Milujete levanduli?', 'Milujete levanduli? Levandulový olej má jemnou, květinovou vůni, která se hodí k večernímu odpočinku, do relaxační koupele nebo k masáži. Klasika, kterou ocení hlavně milovnice květinových vůní.'),
    ('Máte rádi pohodu a radost?', 'Máte rádi pohodu a radost? Sladká a svěží vůně pomeranče navodí doma veselou, přátelskou atmosféru – ať už čekáte návštěvu, nebo si chcete zpříjemnit sychravé odpoledne. Hodí se i do masážního oleje nebo koupele.'),
    ('Chodíte spát s obavou', 'Chcete si připravit klidný večerní rituál? Gardenia Roll-on s jemnou květinovou vůní je praktická v kabelce i na cestách. Naneste ji před spaním na zápěstí nebo za uši a dopřejte si chvíli zklidnění – doma i v hotelu.'),
    ('Potřebujete uvolnit dých', 'Máte rádi svěží, čisté vůně? Eukalyptový olej má výraznou, osvěžující vůni, která provoní místnost a pomůže potlačit nepříjemné pachy. Oblíbený je hlavně v zimních měsících do aromalampy, koupele nebo sauny.'),
    ('Preferujete univerzální řešení', 'Preferujete univerzální řešení typu „vše v jednom“? Olej z 31 léčivých bylin patří k nejprodávanějším produktům JUST. Bohatá bylinná vůně se hodí k masáži po sportu či fyzické práci, do koupele i do aromalampy.'),
    ('Jste celý den rozptylováni', 'Potřebujete se osvěžit? 3 Mint Mix spojuje vůni tří druhů máty – je svěží, chladivý a povzbudivý. Hodí se do aromalampy při práci nebo studiu, k osvěžující masáži i na cesty.'),
    ('Jste často bez nápadů', 'Představuje pro vás vůně citronu svěžest a čistotu? Citronový olej provoní domov jiskřivou citrusovou vůní, která osvěží atmosféru v pracovně i v kuchyni. Hodí se do aromalampy, koupele i k masáži.'),
    ('Cítíte se smutní', 'Potřebujete se rychle osvěžit a nabrat elán? Guduchi Roll-on s povzbudivou vůní máte vždy po ruce – před dlouhou cestou autem, na školení nebo poradě. Stačí nanést na zápěstí nebo za uši.'),
    ('Chodíte rádi do lesa?', 'Chodíte rádi do lesa? Olej z jedle sibiřské přinese domů vůni jehličnatého lesa – svěží, pryskyřičnou a čistou. Oblíbený je hlavně v zimě do aromalampy, sauny nebo koupele a také k masáži po sportu.'),
]
for zac, novy in TEXTY:
    h = nahrad_text_p(h, zac, novy)
h = nahrad(h, 'má uvolňují účinek', 'má uvolňující účinek', pocet=h.count('má uvolňují účinek'))
h = nahrad(h, 'a Eukalyptový olej rozvine své blahodárné vlastnosti', 'a olej rozvine svou vůni', pocet=h.count('a Eukalyptový olej rozvine své blahodárné vlastnosti'))
h = nahrad(h, 'do teplé vody nebo do difuzéru pro podporu koncentrace, osvěžení mysli, navození dobré nálady', 'do teplé vody nebo do difuzéru pro svěží vůni v místnosti')
h = nahrad(h, 'Citronového oleje k masážnímu oleji pro osvěžení těla i mysli', 'Citronového oleje k masážnímu oleji pro svěží vůni')
h = nahrad(h, 'taková masáž má chladivý a relaxační účinek', 'taková masáž příjemně chladí')
h = nahrad(h, 'VOLNÝ DECH - EUKALYPTOVÝ OLEJ', 'SVĚŽEST - EUKALYPTOVÝ OLEJ')
h = nahrad(h, 'LESNÍ LÉKAŘ - OLEJ Z JEDLE SIBIŘSKÉ', 'VŮNĚ LESA - OLEJ Z JEDLE SIBIŘSKÉ')
h = nahrad(h, '/esencialni-oleje/just-olej-z-31-lecivych-bylin-50-ml/', '/esencialni-oleje/just-olej-z-31-lecivych-bylin-75-ml/', pocet=h.count('/esencialni-oleje/just-olej-z-31-lecivych-bylin-50-ml/'))
# z tabulky odstranit řádky s vnitřním / inhalačním použitím
for radek in ('Výplach úst, kloktání', 'Inhalace'):
    i = h.find(radek)
    assert i > 0, radek
    a = h.rfind('<tr', 0, i)
    b = h.find('</tr>', i) + len('</tr>')
    h = h[:a] + h[b:].lstrip('\n')
for zakaz in ('deprese', 'nespavost', 'dýchací', 'trávicí', 'bolest', 'lékárn', 'kloktat', 'Inhalace'):
    assert zakaz.lower() not in h.lower(), zakaz
open(O + '177.html', 'w').write(h)
META['177'] = dict(title='Esence JUST: Klíč k výběru',
                   metaTitle='Éterické oleje JUST – jak vybrat tu pravou vůni',
                   metaDescription='Průvodce éterickými oleji a roll-ony JUST: levandule, pomeranč, eukalyptus, máta, citron i olej z 31 bylin. Jaká vůně se hodí kdy a jak oleje používat.')

# ---------------------------------------------------------------- 195 SK LR parfémy (vyčištění, SK odkazy)
h = open(P + '195.html').read()
h = re.sub(r'^<p><meta[^>]*/><meta[^>]*/></p>\s*', '', h)
h = re.sub(r'<style><!--\s*(?:<style><!--\s*)?(.*?)--></style>', lambda m: '<style><!--\n' + m.group(1).strip() + '\n--></style>', h, count=1, flags=re.S)
assert '<meta' not in h and h.count('<style') == 1, h[:300]
h = re.sub(r'href="/(?!sk/)', 'href="/sk/', h)
h = nahrad(h, '<p><a href="/sk/parfemy/">Zobraziť celú kategóriu parfémov</a></p>', '<p><a class="odkaz" href="/sk/parfemy/">Zobraziť celú kategóriu parfumov</a></p>') if '<p><a href="/sk/parfemy/">Zobraziť celú kategóriu parfémov</a></p>' in h else h
open(O + '195.html', 'w').write(h)
META['195'] = dict(title='Nové LR parfémy – nájdite náhradu za svoju obľúbenú vôňu',
                   metaTitle='Nové LR parfumy – nájdite náhradu za obľúbenú vôňu',
                   metaDescription='Nová edícia parfumov LR: jednoducho nájdete náhradu za svoj obľúbený starší parfum LR. Prehľad dámskych aj pánskych noviniek na KosmetikaEva.eu.')

json.dump(META, open(O + 'meta_cast2.json', 'w'), ensure_ascii=False, indent=1)
print('ok', list(META))
