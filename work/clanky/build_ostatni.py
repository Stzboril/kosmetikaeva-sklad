"""Úpravy článků 15, 45, 57, 131, 149, 177, 183, 186, 195 – bez zdravotních tvrzení, s funkčními odkazy."""
import json, re, os

P = '/home/claude/work/clanky/puvodni/'
O = '/home/claude/work/clanky/upravene/'
os.makedirs(O, exist_ok=True)
CDN = 'https://cdn.myshoptet.com/usr/www.kosmetikaeva.eu/user/documents/upload/'
META = {}


def nahrad(h, stare, nove, pocet=1):
    n = h.count(stare)
    assert n == pocet, f'{stare[:60]!r}: nalezeno {n}x, čekáno {pocet}x'
    return h.replace(stare, nove)


def nahrad_text_p(h, zacatek, novy_text):
    """Nahradí text odstavce od úryvku `zacatek` po nejbližší </p>."""
    assert h.count(zacatek) == 1, f'úryvek {zacatek[:50]!r} nalezen {h.count(zacatek)}x'
    i = h.find(zacatek)
    j = h.find('</p>', i)
    return h[:i] + novy_text + h[j:]


def smaz_blok(h, od, do_vcetne):
    i = h.find(od)
    assert i >= 0, od[:50]
    j = h.find(do_vcetne, i)
    assert j >= 0, do_vcetne[:50]
    return h[:i] + h[j + len(do_vcetne):]


# ---------------------------------------------------------------- 15 Aloe Vera Gel dávkování
AV = '/aloe-vera-gel/'
c15 = f"""<h1>Dávkování Aloe Vera Gelu</h1>
<p>Výrobce LR u nápojových gelů řady <a class="odkaz" href="{AV}">LR LIFETAKT Aloe Vera Drinking Gel</a> doporučuje užívat <strong>3× denně 30 ml</strong>, nejlépe před jídlem. Denní dávka je tedy 90 ml. Doporučenou denní dávku nepřekračujte.</p>
<p>Gel můžete pít čistý nebo zředěný vodou, lehce vychlazený i při pokojové teplotě. Přesné pokyny k uchovávání najdete na obalu každého výrobku.</p>
<h3>Mohou Aloe Vera Gel pít děti, těhotné a kojící ženy?</h3>
<p>Doplňky stravy jsou určeny dospělým a je potřeba je uchovávat mimo dosah malých dětí. Pokud zvažujete podávání dítěti, nebo jste těhotná či kojíte, poraďte se nejprve s lékařem.</p>
<h3>Jak dlouho Aloe Vera Gel užívat?</h3>
<p>Gel je určený k pravidelnému každodennímu užívání. Pro delší užívání se vyplatí výhodnější série 6 × 1000 ml. Pokud užíváte léky nebo máte zdravotní potíže, poraďte se před užíváním s lékařem.</p>
<p><em>Doplněk stravy není náhradou pestré a vyvážené stravy a zdravého životního stylu.</em></p>
<h2>Přehled příchutí LR Aloe Vera Drinking Gel</h2>
<table class="tab" style="width: 100%;">
<tbody class="tab">
<tr class="tab"><th class="tab"><span style="color: #ffffff;">Gel</span></th><th class="tab"><span style="color: #ffffff;">Složení v kostce</span></th></tr>
<tr class="tab"><td class="tab"><a class="odkaz" href="/aloe-vera-gel/lr-aloe-vera-drinking-gel-honey-1000-ml/">Traditional s medem</a></td><td class="tab">90 % gelu z listů aloe vera, 9 % medu</td></tr>
<tr class="tab"><td class="tab"><a class="odkaz" href="/aloe-vera-gel/lr-aloe-vera-drinking-gel-s-prichuti-broskvi-1000-ml-2/">Broskev</a></td><td class="tab">98 % gelu z aloe vera, broskvová příchuť, bez přidaného cukru (se sladidly)</td></tr>
<tr class="tab"><td class="tab"><a class="odkaz" href="/aloe-vera-gel/lr-aloe-vera-drinking-gel-freedom-1000-ml-2/">Active Freedom</a></td><td class="tab">88 % gelu z listů aloe vera, glukosamin sulfát, chondroitin sulfát, kolagen, vitamíny C a E</td></tr>
<tr class="tab"><td class="tab"><a class="odkaz" href="/aloe-vera-gel/lr-aloe-vera-drinking-gel-sivera-1000-ml-2/">Intense Sivera</a></td><td class="tab">90 % gelu z aloe vera, 7 % květového medu, extrakt z kopřivy</td></tr>
<tr class="tab"><td class="tab"><a class="odkaz" href="/aloe-vera-gel/lr-aloe-vera-drinking-gel-immune-plus-1000-ml/">Immune Plus</a></td><td class="tab">85 % gelu z aloe vera, 8 % květového medu, 6 % zázvorové šťávy, vitamín C, zinek a selen</td></tr>
</tbody>
</table>
<p>Všechny gely najdete v kategorii <a class="odkaz" href="{AV}">Aloe Vera gel</a>.</p>"""
META['15'] = dict(title='Aloe Vera Gel dávkování',
                  metaTitle='Aloe Vera Gel LR: dávkování a přehled příchutí',
                  metaDescription='Jak dávkovat LR Aloe Vera Drinking Gel: doporučená dávka 3× denně 30 ml před jídlem, jak gel pít a přehled příchutí včetně složení.')
open(O + '15.html', 'w').write(c15)

# ---------------------------------------------------------------- 183 Eucasol
EUC = '/esencialni-oleje/just-eucasol-sprej-50-ml/'
c183 = f"""<h1 class="nadpish1">Eucasol</h1>
<h3>Bylinný sprej se svěží vůní éterických olejů – pro příjemný vzduch doma i na cestách</h3>
<div id="nadech"><strong>Hlavní složky:</strong> éterické oleje z eukalyptu, rozmarýnu, máty, jalovce, smrku, borovice lesní a kleče, hřebíčku, mentol, kafr</div>
<p><a href="{EUC}" title="Eucasol"><img class="h" src="{CDN}Herbar/JUST_eucasol_1.png" alt="JUST Eucasol" width="225" height="256" style="float: right;" /></a>Eucasol od švýcarské značky JUST patří k velmi oblíbeným produktům díky jednoduchému použití a výrazné, svěží vůni. Je to směs éterických olejů s typickou eukalyptovou a mentolovou vůní, která osvěží vzduch v místnosti a pomůže potlačit nepříjemné pachy.</p>
<p>Kvůli vysoké koncentraci éterických olejů stačí jen 1–2 stříknutí. Nejjemnější je nastříkat Eucasol na kapesník, polštář nebo do prostoru, kde se vůně postupně rozptýlí. Eucasol není určen k nanášení přímo na kůži ani k vnitřnímu použití. Chraňte před očima a uchovávejte mimo dosah dětí.</p>
<h4>Charakteristika vůně</h4>
<p><strong>Eukalyptus</strong> – čistá, svěží a lehce kafrová vůně.</p>
<p><strong>Máta a mentol</strong> – chladivý, osvěžující tón.</p>
<p><strong>Rozmarýn</strong> – bylinná, povzbudivá vůně.</p>
<p><strong>Jalovec, smrk, borovice a kleč</strong> – vůně jehličnatého lesa.</p>
<p><strong>Hřebíček a kafr</strong> – teplý, kořenitý podtón.</p>
<div id="ucinky">
<h4>Proč si Eucasol oblíbit</h4>
<ul>
<li>rychle provoní místnost a pomůže potlačit nepříjemné pachy</li>
<li>navodí svěží atmosféru doma, v kanceláři i v autě</li>
<li>příjemná vůně k večernímu odpočinku – na polštář nebo do koupele</li>
<li>nezanechává skvrny na textiliích</li>
</ul>
</div>
<h4>Jak se Eucasol používá</h4>
<p>Sprej krátce nastříkejte například:</p>
<ul>
<li>na kapesník (1–2 stříknutí) a mějte ho během dne u sebe,</li>
<li>do koupele a vodu dobře promíchejte – v teplé vodě se vůně krásně rozvine,</li>
<li>do místnosti – svěží vůně se rozptýlí v prostoru,</li>
<li>na polštář,</li>
<li>na oblečení (např. šálu nebo bundu) – nejprve vyzkoušejte na nenápadném místě,</li>
<li>do aromalampy.</li>
</ul>
<h3><a class="odkaz" href="{EUC}" title="JUST Eucasol">Koupit Eucasol</a></h3>"""
META['183'] = dict(title='Eucasol',
                   metaTitle='JUST Eucasol – bylinný sprej se svěží vůní',
                   metaDescription='JUST Eucasol je sprej s éterickými oleji z eukalyptu, máty, rozmarýnu a jehličnanů. Osvěží vzduch v místnosti, provoní kapesník i polštář. Jak ho používat.')
open(O + '183.html', 'w').write(c183)

# ---------------------------------------------------------------- 186 Tymiánový krém
TYM = '/telo-2/just-tymianovy-krem-100-ml/'
c186 = f"""<h1 class="nadpish1">Tymiánový krém</h1>
<h3>Hřejivý bylinný krém s éterickými oleji pro příjemnou masáž</h3>
<div id="nadech"><strong>Hlavní složky:</strong> tymián, éterické oleje z eukalyptu, borovice, rozmarýnu a heřmánku, extrakt z citronu, kafr</div>
<p style="text-align: justify;"><a href="{TYM}" title="Just Tymiánový krém"><img class="h" src="{CDN}Herbar/tymianovy_krem.jpg" alt="Just Tymiánový krém" width="286" height="286" style="float: right;" /></a>Bylinný krém od švýcarské značky JUST s vysokým obsahem éterických olejů. Po nanesení se rozvine výrazná bylinná vůně tymiánu, eukalyptu a borovice, která působí svěže a povzbudivě. Krém je oblíbený hlavně v chladných měsících – k masáži hrudníku, zad nebo chodidel, například večer před spaním.</p>
<h4>Charakteristika klíčových složek</h4>
<p style="text-align: justify;"><strong>Tymián</strong> – výrazná, teplá bylinná vůně, typická pro tento krém.</p>
<p style="text-align: justify;"><strong>Rozmarýn</strong> – povzbudivá bylinná vůně a příjemný hřejivý pocit při masáži.</p>
<p style="text-align: justify;"><strong>Eukalyptus</strong> – svěží, čistá vůně připomínající kafr.</p>
<p style="text-align: justify;"><strong>Borovice</strong> – vůně jehličnatého lesa.</p>
<p style="text-align: justify;"><strong>Heřmánek</strong> – jemná bylinná vůně, pečuje o pokožku.</p>
<div id="ucinky">
<h4>Proč si krém oblíbit</h4>
<ul>
<li>hřejivý pocit a výrazná bylinná vůně při masáži</li>
<li>ideální na chladné podzimní a zimní dny</li>
<li>příjemný večerní rituál – vůně se rozvine po nanesení</li>
<li>vhodný k masáži hrudníku, zad i chodidel</li>
</ul>
</div>
<h4>Jak se krém používá</h4>
<ul>
<li>malé množství krému naneste na požadované místo a jemně vmasírujte do úplného vstřebání,</li>
<li>po masáži můžete místo zakrýt, aby se hřejivý pocit udržel déle,</li>
<li>nenanášejte na podrážděnou pokožku a do okolí očí.</li>
</ul>
<h3><a class="odkaz" href="{TYM}" title="JUST Tymiánový krém">Koupit Tymiánový krém</a></h3>"""
META['186'] = dict(title='Tymiánový krém',
                   metaTitle='JUST Tymiánový krém – hřejivý bylinný krém',
                   metaDescription='JUST Tymiánový krém s tymiánem, eukalyptem, borovicí a rozmarýnem. Hřejivý bylinný krém k masáži hrudníku, zad i chodidel. Složení a použití.')
open(O + '186.html', 'w').write(c186)

# ---------------------------------------------------------------- 57 Doplněk stravy vs. lék
c57 = f"""<h1>Doplněk stravy, nebo lék? V čem je rozdíl</h1>
<p>Na první pohled mohou doplňky stravy a volně prodejné léky vypadat podobně – tablety, kapsle nebo tekutiny. Z pohledu zákona jde ale o úplně odlišné výrobky a je dobré vědět, co od kterého můžete čekat.</p>
<h2>Léčivé přípravky</h2>
<p>Léky, včetně těch volně prodejných, registruje Státní ústav pro kontrolu léčiv (SÚKL). Před uvedením na trh procházejí registračním řízením, ve kterém se hodnotí jejich jakost, bezpečnost a účinnost v přesně vymezených indikacích. Účinnost musí být doložena klinickými studiemi a bezpečnost léku se sleduje i po uvedení na trh. Jen léky mohou být určeny k léčbě nebo prevenci onemocnění.</p>
<h2>Doplňky stravy</h2>
<p>Doplňky stravy jsou z pohledu zákona <strong>potraviny</strong>. Jejich účelem je doplnit běžnou stravu o vitamíny, minerální látky nebo jiné látky s nutričním či fyziologickým účinkem. Nejsou určeny k léčbě onemocnění a nesmí jim být připisovány vlastnosti týkající se prevence, léčby či vyléčení nemocí.</p>
<p>Doplňky stravy dozoruje Ministerstvo zemědělství a Státní zemědělská a potravinářská inspekce, předpisy stanovují například, které látky a v jakém množství mohou obsahovat. Výrobce smí u doplňku stravy uvádět jen tzv. schválená zdravotní tvrzení z registru Evropské unie – například „Vitamín C přispívá k normální funkci imunitního systému“, a to jen tehdy, když výrobek obsahuje dostatečné množství dané látky.</p>
<h2>Jak číst etiketu doplňku stravy</h2>
<ul>
<li><strong>Doporučená denní dávka</strong> – kolik a jak často výrobek užívat; dávku nepřekračujte.</li>
<li><strong>Složení</strong> – všechny složky výrobku, seřazené podle množství.</li>
<li><strong>Obsah účinných látek v denní dávce</strong> – často i v % referenční hodnoty příjmu (RHP).</li>
<li><strong>Upozornění</strong> – např. že výrobek není náhradou pestré stravy a má se uchovávat mimo dosah dětí.</li>
</ul>
<p>Pokud užíváte léky, máte zdravotní potíže, jste těhotná nebo kojíte, poraďte se před užíváním doplňku stravy s lékařem nebo lékárníkem.</p>
<h2>Příklad: Aloe Vera Drinking Gel od LR</h2>
<p>Nápojové gely <a class="odkaz" href="/aloe-vera-gel/">LR LIFETAKT Aloe Vera Drinking Gel</a> jsou doplňky stravy. Obsahují 85–98 % gelu z listů aloe vera a podle příchuti další složky, například med, zázvor nebo extrakt z kopřivy. Doporučená denní dávka je 3× 30 ml před jídlem. Přehled příchutí a jejich složení najdete v článku <a class="odkaz" href="/vse-o-produktech/aloe-vera-gel/">Aloe Vera Gel dávkování</a>.</p>"""
META['57'] = dict(title='Doplněk stravy, nebo lék? V čem je rozdíl',
                  metaTitle='Doplněk stravy, nebo lék? V čem je rozdíl',
                  metaDescription='Jaký je rozdíl mezi doplňkem stravy a lékem, kdo je kontroluje, co smí výrobce tvrdit a jak číst etiketu doplňku stravy. Srozumitelný přehled.')
open(O + '57.html', 'w').write(c57)

json.dump(META, open(O + 'meta_cast1.json', 'w'), ensure_ascii=False, indent=1)
print('ok', list(META))
