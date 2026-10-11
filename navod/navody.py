# Návody k použití – podle textů výrobce (u sad podle návodů jednotlivých produktů výrobce)
# kód -> (titulek CZ, html CZ, titulek SK, html SK)

PARFEM = (
    'Použití',
    '<p>Naneste malé množství parfému na pulzní body – zápěstí, krk, loketní jamku či dekolt. Pro delší výdrž můžete lehce provonět i vlasy nebo oblečení ze vzdálenosti cca 20 cm (nejprve vyzkoušejte na nenápadném místě). Vyhněte se kontaktu s očima a podrážděnou pokožkou.</p>',
    'Použitie',
    '<p>Naneste malé množstvo parfumu na pulzné body – zápästie, krk, lakťovú jamku či dekolt. Pre dlhšiu výdrž môžete jemne navoňať aj vlasy alebo oblečenie zo vzdialenosti cca 20 cm (najskôr vyskúšajte na nenápadnom mieste). Vyhnite sa kontaktu s očami a podráždenou pokožkou.</p>',
)

PARFEM_KODY = '''LUX10 LUX09 LUX08 LUX07 LUX06 LUX05 LUX04 LUX03 LUX02 LUX01
W19450 W19350 W18850 W18450 W17450 W17250 W17150 W16850 W16650 W15750 W15650 W150150
W14850 W14551 W14450 W14250 W13050 W12750 W11850 W11750 W10650 W10450 W10250
M04250 M03450 M02850 M01650 M01450 M00850 M00750 M00350 M00150'''.split()

SET_PARFEM = (
    'Použití',
    '<p>Sprchový gel naneste na vlhkou pokožku, vmasírujte a důkladně opláchněte vodou. Po osušení nastříkejte parfém na pulzní body – zápěstí, krk nebo za uši. Vyhněte se kontaktu s očima a podrážděnou pokožkou.</p>',
    'Použitie',
    '<p>Sprchový gél naneste na vlhkú pokožku, vmasírujte a dôkladne opláchnite vodou. Po osušení nastriekajte parfum na pulzné body – zápästie, krk alebo za uši. Vyhnite sa kontaktu s očami a podráždenou pokožkou.</p>',
)

KREM_RUCE = (
    'Použití',
    '<p>Naneste na čisté, umyté ruce a rozetřete. Krém je vhodný pro každodenní použití.</p>',
    'Použitie',
    '<p>Naneste na čisté, umyté ruky a rozotrite. Krém je vhodný na každodenné použitie.</p>',
)

DOPLNEK_CZ = 'Nepřekračujte doporučenou denní dávku. Doplňky stravy nejsou náhradou pestré a vyvážené stravy. Uchovávejte mimo dosah dětí.'
DOPLNEK_SK = 'Neprekračujte odporúčanú dennú dávku. Doplnky stravy nie sú náhradou pestrej a vyváženej stravy. Uchovávajte mimo dosahu detí.'

ZG_PRO_POZN_CZ = 'Čisticí krém, pleťová voda a pečující krémy LR ZEITGARD nejsou součástí setu.'
ZG_PRO_POZN_SK = 'Čistiaci krém, pleťová voda a ošetrujúce krémy LR ZEITGARD nie sú súčasťou setu.'

N = {}
for k in PARFEM_KODY:
    N[k] = PARFEM
for k in ('SETLUX10', 'SETLUX08', 'SETLUX05', 'SETLUX01'):
    N[k] = SET_PARFEM
N['HC03'] = KREM_RUCE
N['HC05'] = KREM_RUCE

N['SETCH21'] = (
    'Použití',
    '<p><strong>Krém na ruce:</strong> naneste na čisté, umyté ruce a rozetřete. Je vhodný pro každodenní použití.<br /><strong>Krém na nohy:</strong> naneste na umytou pokožku chodidel a rozetřete.</p>',
    'Použitie',
    '<p><strong>Krém na ruky:</strong> naneste na čisté, umyté ruky a rozotrite. Je vhodný na každodenné použitie.<br /><strong>Krém na nohy:</strong> naneste na umytú pokožku chodidiel a rozotrite.</p>',
)

N['HOME85'] = (
    'Použití',
    '<p>Koncentrát z litrové láhve nalévejte přes odměrku – podle vyznačených rysek snadno odměříte přesné množství. Odměrka je určená k opakovanému použití.</p>',
    'Použitie',
    '<p>Koncentrát z litrovej fľaše nalievajte cez odmerku – podľa vyznačených rysiek ľahko odmeriate presné množstvo. Odmerka je určená na opakované použitie.</p>',
)

N['HOME83'] = (
    'Použití',
    '<p>Etiketu nalepte na ředicí láhev podle prostředku ESSENS Home Clean, který do ní naředíte. Naředěné prostředky si tak nespletete.</p>',
    'Použitie',
    '<p>Etiketu nalepte na riediacu fľašu podľa prostriedku ESSENS Home Clean, ktorý do nej nariedite. Nariedené prostriedky si tak nepomýlite.</p>',
)

N['SCOL01N'] = (
    'Příprava jogurtu',
    '<p>Do nerezové nádoby jogurtovače nalijte 1 litr mléka pokojové teploty, přidejte 1 sáček Colostrum Probiotics a důkladně promíchejte. Nádobu vložte do jogurtovače, zakryjte průhledným víkem a zapojte do zásuvky – topné těleso se zahřeje nejvýše na 43 °C. Jogurt je hotový přibližně za 8 hodin; hustší a kyselejší jogurt získáte delší přípravou, ne však déle než 12 hodin. Hotový jogurt doporučujeme stabilizovat v chladničce a uchovávat tam nejvýše 3–5 dnů. Jogurt konzumujte dlouhodobě a pravidelně.</p><p>Podrobný návod k jogurtovači v českém jazyce je součástí balení.</p>',
    'Príprava jogurtu',
    '<p>Do nerezovej nádoby jogurtovača nalejte 1 liter mlieka izbovej teploty, pridajte 1 vrecúško Colostrum Probiotics a dôkladne premiešajte. Nádobu vložte do jogurtovača, zakryte priehľadným vekom a zapojte do zásuvky – výhrevné teleso sa zahreje najviac na 43 °C. Jogurt je hotový približne za 8 hodín; hustejší a kyslejší jogurt získate dlhšou prípravou, nie však dlhšie ako 12 hodín. Hotový jogurt odporúčame stabilizovať v chladničke a uchovávať tam najviac 3–5 dní. Jogurt konzumujte dlhodobo a pravidelne.</p><p>Podrobný návod k jogurtovaču je súčasťou balenia.</p>',
)

N['SCOL13N'] = (
    'Použití',
    '<p><strong>Sprchový gel s colostrem:</strong> naneste na vlhkou pokožku, napěňte a důkladně opláchněte.<br /><strong>Krém proti celulitidě s colostrem:</strong> naneste na čistou, umytou pokožku a rozetřete. Je určený pro každodenní péči o tělo.<br /><strong>Výživný tělový krém s colostrem:</strong> naneste na umytou pokožku a rozetřete.</p>',
    'Použitie',
    '<p><strong>Sprchový gél s colostrom:</strong> naneste na vlhkú pokožku, napeňte a dôkladne opláchnite.<br /><strong>Krém proti celulitíde s colostrom:</strong> naneste na čistú, umytú pokožku a rozotrite. Je určený na každodennú starostlivosť o telo.<br /><strong>Výživný telový krém s colostrom:</strong> naneste na umytú pokožku a rozotrite.</p>',
)

N['SAVE07'] = (
    'Použití',
    '<p><strong>Aloe Vera Soft Spray:</strong> před použitím důkladně protřepejte, malé množství nastříkejte podle potřeby na pokožku a nechte volně uschnout. Pouze k zevnímu použití.<br /><strong>Pěna na holení s Aloe vera:</strong> na navlhčenou pokožku naneste malé množství pěny, oholte se obvyklým způsobem a pokožku pečlivě opláchněte vodou.<br /><strong>Hydratační pleťový krém:</strong> naneste ráno a večer na vyčištěnou pleť a jemně rozetřete.<br /><strong>Tělový peeling s Aloe vera:</strong> naneste na navlhčenou pokožku, jemně masírujte krouživými pohyby a poté důkladně opláchněte vodou. Doporučujeme používat 2–3× týdně.</p>',
    'Použitie',
    '<p><strong>Aloe Vera Soft Spray:</strong> pred použitím dôkladne pretrepte, malé množstvo nastriekajte podľa potreby na pokožku a nechajte voľne uschnúť. Iba na vonkajšie použitie.<br /><strong>Pena na holenie s Aloe vera:</strong> na navlhčenú pokožku naneste malé množstvo peny, oholte sa obvyklým spôsobom a pokožku starostlivo opláchnite vodou.<br /><strong>Hydratačný pleťový krém:</strong> naneste ráno a večer na vyčistenú pleť a jemne rozotrite.<br /><strong>Telový peeling s Aloe vera:</strong> naneste na navlhčenú pokožku, jemne masírujte krúživými pohybmi a potom dôkladne opláchnite vodou. Odporúčame používať 2–3× týždenne.</p>',
)

N['SAVE05'] = (
    'Použití',
    '<p>Před použitím protřepejte. Malé množství spreje naneste podle potřeby na pokožku a nechte volně uschnout. Platí pro všechny tři spreje v sadě. Pouze k zevnímu použití. Případný sediment není na závadu účinnosti.</p>',
    'Použitie',
    '<p>Pred použitím pretrepte. Malé množstvo spreja naneste podľa potreby na pokožku a nechajte voľne uschnúť. Platí pre všetky tri spreje v sade. Iba na vonkajšie použitie. Prípadný sediment nie je na závadu účinnosti.</p>',
)

N['SETCH41'] = (
    'Doporučené dávkování',
    f'<p>15–90 ml denně v několika dávkách (1 polévková lžíce = cca 15 ml). Před použitím protřepejte. Platí pro každý ze tří gel drinků v sadě.</p><p>{DOPLNEK_CZ}</p>',
    'Odporúčané dávkovanie',
    f'<p>15–90 ml denne v niekoľkých dávkach (1 polievková lyžica = cca 15 ml). Pred použitím pretrepte. Platí pre každý z troch gél drinkov v sade.</p><p>{DOPLNEK_SK}</p>',
)

N['SETCH79'] = (
    'Použití',
    '<p><strong>Pěna na holení s Aloe vera:</strong> na navlhčenou pokožku naneste malé množství pěny, oholte se obvyklým způsobem a pokožku pečlivě opláchněte vodou.<br /><strong>Aloe vera Deo Stick:</strong> aplikujte na suchou pokožku v podpaží. Počkejte, až přípravek zcela zaschne, a teprve potom se oblékněte.</p>',
    'Použitie',
    '<p><strong>Pena na holenie s Aloe vera:</strong> na navlhčenú pokožku naneste malé množstvo peny, oholte sa obvyklým spôsobom a pokožku starostlivo opláchnite vodou.<br /><strong>Aloe vera Deo Stick:</strong> aplikujte na suchú pokožku podpazušia. Počkajte, kým prípravok úplne zaschne, a až potom sa oblečte.</p>',
)

N['SAVE08'] = (
    'Doporučené dávkování',
    f'<p><strong>Aloe Vera + Q10:</strong> 2 kapsle denně, nejlépe večer před jídlem, zapijte dostatečným množstvím tekutiny. Doporučuje se užívat pravidelně 3 měsíce.<br /><strong>Aloe Vera + Boswellia:</strong> 2 kapsle denně, nejlépe večer před jídlem, zapijte dostatečným množstvím tekutiny. Doporučená doba užívání jsou 3 měsíce souvisle.<br />U obou produktů nepřekračujte ani krátkodobě denní dávku 6 kapslí.</p><p>{DOPLNEK_CZ}</p>',
    'Odporúčané dávkovanie',
    f'<p><strong>Aloe Vera + Q10:</strong> 2 kapsuly denne, najlepšie večer pred jedlom, zapite dostatočným množstvom tekutiny. Odporúča sa užívať pravidelne 3 mesiace.<br /><strong>Aloe Vera + Boswellia:</strong> 2 kapsuly denne, najlepšie večer pred jedlom, zapite dostatočným množstvom tekutiny. Odporúčaná doba užívania sú 3 mesiace súvisle.<br />Pri oboch produktoch neprekračujte ani krátkodobo dennú dávku 6 kapsúl.</p><p>{DOPLNEK_SK}</p>',
)

N['SETCH54'] = (
    'Použití',
    '<p><strong>Hydratační pleťový krém:</strong> naneste ráno a večer na vyčištěnou pleť a jemně rozetřete.<br /><strong>Aloe Vera Soft Spray Plus:</strong> před použitím protřepejte, malé množství naneste podle potřeby na pokožku a nechte zaschnout.</p>',
    'Použitie',
    '<p><strong>Hydratačný pleťový krém:</strong> naneste ráno a večer na vyčistenú pleť a jemne rozotrite.<br /><strong>Aloe Vera Soft Spray Plus:</strong> pred použitím pretrepte, malé množstvo naneste podľa potreby na pokožku a nechajte zaschnúť.</p>',
)

N['SETCH80'] = (
    'Použití',
    '<p><strong>Plátýnkové masky:</strong> masku rozložte rovnoměrně na vyčištěnou pleť tak, aby nezakrývala oči a ústa. Nechte působit 10–15 minut, pak ji sejměte a zbylou esenci jemně vmasírujte do pleti.<br /><strong>Hydratační pleťová maska:</strong> naneste na pleť, nechte 15 minut působit a poté opláchněte studenou vodou.<br />Masky doporučujeme používat 1–2× týdně.</p>',
    'Použitie',
    '<p><strong>Plátenné masky:</strong> masku rozložte rovnomerne na vyčistenú pleť tak, aby nezakrývala oči a ústa. Nechajte pôsobiť 10–15 minút, potom ju zložte a zvyšnú esenciu jemne vmasírujte do pleti.<br /><strong>Hydratačná pleťová maska:</strong> naneste na pleť, nechajte 15 minút pôsobiť a potom opláchnite studenou vodou.<br />Masky odporúčame používať 1–2× týždenne.</p>',
)

N['SETMHE16'] = (
    'Doporučené dávkování',
    f'<p><strong>Collagen Fish:</strong> 1 balení gelu (50 g) denně. Dodržujte dostatečný pitný režim.<br /><strong>Elastir:</strong> 1 tobolka denně po jídle, dobře zapijte vodou nebo jinou vhodnou tekutinou.</p><p>{DOPLNEK_CZ}</p>',
    'Odporúčané dávkovanie',
    f'<p><strong>Collagen Fish:</strong> 1 balenie gélu (50 g) denne. Dodržiavajte dostatočný pitný režim.<br /><strong>Elastir:</strong> 1 kapsula denne po jedle, dobre zapite vodou alebo inou vhodnou tekutinou.</p><p>{DOPLNEK_SK}</p>',
)

N['SETMHE15'] = (
    'Doporučené dávkování',
    f'<p><strong>Collagen Premium:</strong> 1 balení gelu (50 g) denně. Dodržujte dostatečný pitný režim.<br /><strong>Elastir:</strong> 1 tobolka denně po jídle, dobře zapijte vodou nebo jinou vhodnou tekutinou.</p><p>{DOPLNEK_CZ}</p>',
    'Odporúčané dávkovanie',
    f'<p><strong>Collagen Premium:</strong> 1 balenie gélu (50 g) denne. Dodržiavajte dostatočný pitný režim.<br /><strong>Elastir:</strong> 1 kapsula denne po jedle, dobre zapite vodou alebo inou vhodnou tekutinou.</p><p>{DOPLNEK_SK}</p>',
)

N['SETCH88'] = (
    'Použití',
    '<p><strong>Krémový korektor:</strong> aplikátorem naneste korektor na místa, která chcete sjednotit nebo rozjasnit, a jemně ho vklepejte bříšky prstů nebo štětcem.<br /><strong>Paleta pudrových tvářenek 3v1:</strong> naneste kosmetickým štětcem na lícní kosti, střední část obličeje, oblast pod obočím a nos – podle nákresu na obalu.<br /><strong>Řasenka:</strong> jedním tahem naneste na horní i spodní řasy.</p>',
    'Použitie',
    '<p><strong>Krémový korektor:</strong> aplikátorom naneste korektor na miesta, ktoré chcete zjednotiť alebo rozjasniť, a jemne ho vklepte bruškami prstov alebo štetcom.<br /><strong>Paleta púdrových líceniek 3v1:</strong> naneste kozmetickým štetcom na lícne kosti, strednú časť tváre, oblasť pod obočím a nos – podľa nákresu na obale.<br /><strong>Riasenka:</strong> jedným ťahom naneste na horné aj spodné riasy.</p>',
)

N['SCOL15'] = (
    'Doporučené dávkování',
    f'<p>Dávkování je u všech tří doplňků stravy stejné: 2 tobolky denně, nejlépe večer před jídlem, zapijte dostatečným množstvím tekutiny. Není určeno dětem do 3 let věku, těhotným a kojícím ženám.</p><p>{DOPLNEK_CZ}</p>',
    'Odporúčané dávkovanie',
    f'<p>Dávkovanie je pri všetkých troch doplnkoch stravy rovnaké: 2 kapsuly denne, najlepšie večer pred jedlom, zapite dostatočným množstvom tekutiny. Nie je určené deťom do 3 rokov, tehotným a dojčiacim ženám.</p><p>{DOPLNEK_SK}</p>',
)

# ---------------- EURONA
for k in ('CC6784', 'CC6787'):
    N[k] = (
        'Návod k použití',
        '<p>Aplikujte na suchou a čistou pokožku nebo na vlasy. Nepoužívejte na podrážděnou nebo poraněnou pokožku.</p>',
        'Návod na použitie',
        '<p>Aplikujte na suchú a čistú pokožku alebo na vlasy. Nepoužívajte na podráždenú alebo poranenú pokožku.</p>',
    )

N['CL0085'] = (
    'Návod k použití',
    '<p>Sítko naplňte sypaným čajem, ponořte ho do šálku s horkou vodou a nechte louhovat podle doporučení na balení čaje. Poté sítko vyjměte a vysypte.</p>',
    'Návod na použitie',
    '<p>Sitko naplňte sypaným čajom, ponorte ho do šálky s horúcou vodou a nechajte lúhovať podľa odporúčania na balení čaju. Potom sitko vyberte a vysypte.</p>',
)

N['4050'] = (
    'Návod k použití',
    '<p>Původní rozprašovač odšroubujte a na lahev o objemu 250 ml nebo 500 ml našroubujte náhradní rozprašovač. Rozprašovač můžete používat opakovaně.</p>',
    'Návod na použitie',
    '<p>Pôvodný rozprašovač odskrutkujte a na fľašu s objemom 250 ml alebo 500 ml naskrutkujte náhradný rozprašovač. Rozprašovač môžete používať opakovane.</p>',
)

N['4001'] = (
    'Návod k použití',
    '<p>Podle rysek nalijte do lahvičky přípravek Eurona a vodu v poměru, který je uvedený na obalu přípravku. Nasaďte rozprašovač a roztok nanášejte podle návodu k přípravku. Obsah lahvičky si můžete označit samolepicí etiketou Eurona.</p>',
    'Návod na použitie',
    '<p>Podľa rysiek nalejte do fľaštičky prípravok Eurona a vodu v pomere, ktorý je uvedený na obale prípravku. Nasaďte rozprašovač a roztok nanášajte podľa návodu k prípravku. Obsah fľaštičky si môžete označiť samolepiacou etiketou Eurona.</p>',
)

N['4008'] = (
    'Návod k použití',
    '<p>Odměrkou odměřte prací nebo čisticí prostředek podle dávkování uvedeného na obalu prostředku.</p>',
    'Návod na použitie',
    '<p>Odmerkou odmerajte prací alebo čistiaci prostriedok podľa dávkovania uvedeného na obale prostriedku.</p>',
)

N['PB2026'] = (
    'Jak podávat',
    '<p>Pastovaný med neteče, a proto se skvěle roztírá – třeba na pečivo. Vyzkoušejte také lžičku medu v teplém mléce před spaním.</p>',
    'Ako podávať',
    '<p>Pastovaný med netečie, a preto sa skvele roztiera – napríklad na pečivo. Vyskúšajte aj lyžičku medu v teplom mlieku pred spaním.</p>',
)

N['CE0005'] = (
    'Příprava',
    '<p>Směs je ideální pro přípravu espressa, kávy v moka konvičce i silné filtrované kávy.</p>',
    'Príprava',
    '<p>Zmes je ideálna na prípravu espressa, kávy v moka kanvičke aj silnej filtrovanej kávy.</p>',
)

# ---------------- LR
SERUM = (
    'Aplikace',
    '<p>Ráno a večer naneste malé množství séra na vyčištěnou pleť obličeje a jemně vmasírujte. Poté pokračujte obvyklým pleťovým krémem.</p>',
    'Aplikácia',
    '<p>Ráno a večer naneste malé množstvo séra na vyčistenú pleť tváre a jemne vmasírujte. Potom pokračujte obvyklým pleťovým krémom.</p>',
)
N['20856-1'] = SERUM
N['27166-1'] = SERUM

N['28283-1'] = (
    'Aplikace',
    '<p>Sedmidenní kúra: každý den použijte jednu dávku (2,5 ml). Naneste ji na vyčištěnou pleť a jemně vmasírujte, poté pokračujte obvyklou denní nebo noční péčí.</p>',
    'Aplikácia',
    '<p>Sedemdňová kúra: každý deň použite jednu dávku (2,5 ml). Naneste ju na vyčistenú pleť a jemne vmasírujte, potom pokračujte obvyklou dennou alebo nočnou starostlivosťou.</p>',
)

N['29069-99'] = (
    'Aplikace',
    '<ul>'
    '<li><strong>Rozjasňující make-up:</strong> naneste na hřbet ruky nebo přímo na obličej a rozetřete štětcem či houbičkou. Pro vyšší krytí naneste další vrstvu.</li>'
    '<li><strong>Rozjasňující korektor:</strong> po ošetření pleti naneste na místa, která chcete zakrýt, a jemně rozetřete štětcem nebo navlhčenou houbičkou.</li>'
    '<li><strong>Tekutá tvářenka:</strong> houbičkou, štětcem nebo prsty rozprostřete po tvářích a lícních kostech.</li>'
    '<li><strong>Tekutý rozjasňovač:</strong> použijte až po make-upu a tvářence – rozetřete ho na lícní kosti, hřbet a špičku nosu, střed horního rtu a bradu.</li>'
    '<li><strong>Fixační pudr:</strong> jako poslední krok líčení naneste štětcem na T-zónu – čelo, nos a bradu.</li>'
    '<li><strong>Paletka očních stínů:</strong> stíny nanášejte štětcem nebo prstem na víčka po napudrování.</li>'
    '<li><strong>Řasenka:</strong> kartáčkem naneste řasenku na řasy.</li>'
    '<li><strong>Gel na obočí:</strong> kartáčkem učešte obočí do požadovaného tvaru a gel nechte chvilku zaschnout.</li>'
    '<li><strong>Konturovací tužka a rtěnka:</strong> tužkou obtáhněte obrys rtů, poté naneste rtěnku v odpovídajícím odstínu.</li>'
    '<li><strong>Aktivační sérum na řasy:</strong> ráno a večer po odlíčení naneste jedním tahem na horní i spodní linii řas.</li>'
    '</ul>',
    'Aplikácia',
    '<ul>'
    '<li><strong>Rozjasňujúci make-up:</strong> naneste na chrbát ruky alebo priamo na tvár a rozotrite štetcom či hubkou. Pre vyššie krytie naneste ďalšiu vrstvu.</li>'
    '<li><strong>Rozjasňujúci korektor:</strong> po ošetrení pleti naneste na miesta, ktoré chcete zakryť, a jemne rozotrite štetcom alebo navlhčenou hubkou.</li>'
    '<li><strong>Tekutá lícenka:</strong> hubkou, štetcom alebo prstami rozotrite po lícach a lícnych kostiach.</li>'
    '<li><strong>Tekutý rozjasňovač:</strong> použite až po make-upe a lícenke – rozotrite ho na lícne kosti, chrbát a špičku nosa, stred hornej pery a bradu.</li>'
    '<li><strong>Fixačný púder:</strong> ako posledný krok líčenia naneste štetcom na T-zónu – čelo, nos a bradu.</li>'
    '<li><strong>Paletka očných tieňov:</strong> tiene nanášajte štetcom alebo prstom na viečka po napúdrovaní.</li>'
    '<li><strong>Riasenka:</strong> kefkou naneste riasenku na riasy.</li>'
    '<li><strong>Gél na obočie:</strong> kefkou učešte obočie do požadovaného tvaru a gél nechajte chvíľu zaschnúť.</li>'
    '<li><strong>Kontúrovacia ceruzka a rúž:</strong> ceruzkou obtiahnite obrys pier, potom naneste rúž v zodpovedajúcom odtieni.</li>'
    '<li><strong>Aktivačné sérum na riasy:</strong> ráno a večer po odlíčení naneste jedným ťahom na hornú aj spodnú líniu rias.</li>'
    '</ul>',
)

N['96999-19'] = (
    'Aplikace',
    '<ul>'
    '<li><strong>Čisticí krém:</strong> používejte 1–2× denně jako součást každodenního čištění obličeje.</li>'
    '<li><strong>Pleťová voda:</strong> po vyčištění pleti naneste 1–2× denně malé množství na kosmetický tampon a jemně rozetřete na obličej, krk a dekolt. Vyhněte se očnímu okolí.</li>'
    '<li><strong>Beauty Diamonds Denní krém:</strong> nanášejte na obličej každé ráno po očištění pleti.</li>'
    '<li><strong>Beauty Diamonds Noční krém:</strong> nanášejte každý večer na vyčištěnou pleť obličeje, krku a dekoltu.</li>'
    '<li><strong>Beauty Diamonds 2v1 Oční krém a maska:</strong> jako oční krém nanášejte denně jemně na oční okolí. Jako masku 2–3× týdně naneste větší množství krému na oční okolí, nechte 15 minut vstřebávat a přebytek vmasírujte nebo setřete kosmetickým ubrouskem.</li>'
    '</ul>',
    'Aplikácia',
    '<ul>'
    '<li><strong>Čistiaci krém:</strong> používajte 1–2× denne ako súčasť každodenného čistenia tváre.</li>'
    '<li><strong>Pleťová voda:</strong> po vyčistení pleti naneste 1–2× denne malé množstvo na kozmetický tampón a jemne rozotrite na tvár, krk a dekolt. Vyhnite sa očnému okoliu.</li>'
    '<li><strong>Beauty Diamonds Denný krém:</strong> nanášajte na tvár každé ráno po očistení pleti.</li>'
    '<li><strong>Beauty Diamonds Nočný krém:</strong> nanášajte každý večer na vyčistenú pleť tváre, krku a dekoltu.</li>'
    '<li><strong>Beauty Diamonds 2v1 Očný krém a maska:</strong> ako očný krém nanášajte denne jemne na očné okolie. Ako masku 2–3× týždenne naneste väčšie množstvo krému na očné okolie, nechajte 15 minút vstrebávať a prebytok vmasírujte alebo zotrite kozmetickou servítkou.</li>'
    '</ul>',
)

N['20905-1'] = (
    'Použití',
    '<ul>'
    '<li><strong>Aloe Vera Sprej první pomoci:</strong> rozstříkejte rovnoměrně na postižené místo a jemně vmasírujte. Podle potřeby opakujte několikrát denně, zejména po slunění nebo po podráždění pokožky.</li>'
    '<li><strong>Aloe Vera Hydratační gelový koncentrát:</strong> nanášejte v tenké vrstvě přímo na pokožku – pravidelně nebo podle potřeby, např. po opalování, holení či při dehydrataci pokožky.</li>'
    '<li><strong>Aloe Vera Ochranný krém s propolisem:</strong> nanášejte podle potřeby na suchá nebo namáhaná místa (např. obličej, ruce, lokty) a jemně vmasírujte.</li>'
    '<li><strong>Aloe Vera Krémový gel první pomoci:</strong> naneste přímo na postižené místo. Na větší plochy použijte raději sprej první pomoci.</li>'
    '</ul>',
    'Použitie',
    '<ul>'
    '<li><strong>Aloe Vera Sprej prvej pomoci:</strong> rozstriekajte rovnomerne na postihnuté miesto a jemne vmasírujte. Podľa potreby opakujte niekoľkokrát denne, najmä po opaľovaní alebo po podráždení pokožky.</li>'
    '<li><strong>Aloe Vera Hydratačný gélový koncentrát:</strong> nanášajte v tenkej vrstve priamo na pokožku – pravidelne alebo podľa potreby, napr. po opaľovaní, holení či pri dehydratácii pokožky.</li>'
    '<li><strong>Aloe Vera Ochranný krém s propolisom:</strong> nanášajte podľa potreby na suché alebo namáhané miesta (napr. tvár, ruky, lakte) a jemne vmasírujte.</li>'
    '<li><strong>Aloe Vera Krémový gél prvej pomoci:</strong> naneste priamo na postihnuté miesto. Na väčšie plochy použite radšej sprej prvej pomoci.</li>'
    '</ul>',
)

N['20729-1'] = (
    'Použití',
    '<p>Krém nanášejte podle potřeby na suchá nebo namáhaná místa (např. obličej, ruce, lokty) a jemně vmasírujte do pokožky. Je vhodný pro každodenní použití.</p>',
    'Použitie',
    '<p>Krém nanášajte podľa potreby na suché alebo namáhané miesta (napr. tvár, ruky, lakte) a jemne vmasírujte do pokožky. Je vhodný na každodenné použitie.</p>',
)

N['20757-1'] = (
    'Použití',
    '<p>Aplikujte denně ráno a večer na čistou pokožku podpaží. Hodí se i k osvěžení během dne.</p>',
    'Použitie',
    '<p>Aplikujte denne ráno a večer na čistú pokožku podpazušia. Hodí sa aj na osvieženie počas dňa.</p>',
)

CISTENI_CZ = 'Navlhčete si obličej vodou a naneste na pleť Čisticí krém LR ZEITGARD. Zapněte přístroj s Čisticí hlavicí a jemně čistěte levou a pravou stranu obličeje a čelo (T-zónu), vždy asi 20 sekund. Po vyčištění pleť projasněte pleťovou vodou LR ZEITGARD.'
CISTENI_SK = 'Navlhčite si tvár vodou a naneste na pleť Čistiaci krém LR ZEITGARD. Zapnite prístroj s Čistiacou hlavicou a jemne čistite ľavú a pravú stranu tváre a čelo (T-zónu), vždy asi 20 sekúnd. Po vyčistení pleť rozjasnite pleťovou vodou LR ZEITGARD.'
PEELING_CZ = 'Na navlhčenou pleť naneste Čisticí krém LR ZEITGARD, vmasírujte ho, opláchněte vodou a obličej neosušujte. Zapněte přístroj s Peelingovou hlavicí a kovovou špachtlí jemně přejíždějte po dobře navlhčeném obličeji pod úhlem 45°, nejdéle 3 minuty. Postupujte vždy zevnitř ven a zdola nahoru. Nakonec čisticím tamponem naneste pleťovou vodu LR ZEITGARD, která pleť po peelingu zklidní.'
PEELING_SK = 'Na navlhčenú pleť naneste Čistiaci krém LR ZEITGARD, vmasírujte ho, opláchnite vodou a tvár neosušujte. Zapnite prístroj s Peelingovou hlavicou a kovovou špachtľou jemne prechádzajte po dobre navlhčenej tvári pod uhlom 45°, najdlhšie 3 minúty. Postupujte vždy zvnútra von a zdola nahor. Nakoniec čistiacim tampónom naneste pleťovú vodu LR ZEITGARD, ktorá pleť po peelingu upokojí.'
ANTIAGING_CZ = 'Pleť nejprve vyčistěte Čisticí nebo Peelingovou hlavicí. Na obličej naneste v malých tečkách pečující krém LR ZEITGARD (Nanogold, Beauty Diamonds nebo Platinum) a vmasírujte ho Anti-aging hlavicí. Levou stranu obličeje, pravou stranu i čelo ošetřujte vždy 30 sekund krouživými pohyby zevnitř ven a zdola nahoru.'
ANTIAGING_SK = 'Pleť najprv vyčistite Čistiacou alebo Peelingovou hlavicou. Na tvár naneste v malých bodkách ošetrujúci krém LR ZEITGARD (Nanogold, Beauty Diamonds alebo Platinum) a vmasírujte ho Anti-aging hlavicou. Ľavú stranu tváre, pravú stranu aj čelo ošetrujte vždy 30 sekúnd krúživými pohybmi zvnútra von a zdola nahor.'
TELO_CZ = 'Hlavici pro péči o tělo používejte spolu s Tělovým krémem LR ZEITGARD 1–2× denně: krém naneste na pokožku a zapracujte ho hlavicí – každé partii těla věnujte 1–2 minuty.'
TELO_SK = 'Hlavicu na starostlivosť o telo používajte spolu s Telovým krémom LR ZEITGARD 1–2× denne: krém naneste na pokožku a zapracujte ho hlavicou – každej partii tela venujte 1–2 minúty.'

N['70110-1'] = ('Aplikace', f'<p>{CISTENI_CZ}</p><p>{ZG_PRO_POZN_CZ}</p>', 'Aplikácia', f'<p>{CISTENI_SK}</p><p>{ZG_PRO_POZN_SK}</p>')
N['70110-2'] = ('Aplikace', f'<p>{PEELING_CZ}</p><p>{ZG_PRO_POZN_CZ}</p>', 'Aplikácia', f'<p>{PEELING_SK}</p><p>{ZG_PRO_POZN_SK}</p>')
N['70110-3'] = ('Aplikace', f'<p>{ANTIAGING_CZ}</p><p>{ZG_PRO_POZN_CZ}</p>', 'Aplikácia', f'<p>{ANTIAGING_SK}</p><p>{ZG_PRO_POZN_SK}</p>')
N['70110-4'] = ('Aplikace', f'<p>{TELO_CZ}</p><p>Tělový krém LR ZEITGARD není součástí setu.</p>', 'Aplikácia', f'<p>{TELO_SK}</p><p>Telový krém LR ZEITGARD nie je súčasťou setu.</p>')
N['70106-1'] = (
    'Aplikace',
    f'<p>{CISTENI_CZ}</p><p>Čisticí krém používejte 1–2× denně, ideálně ráno a večer. Pleťová voda LR ZEITGARD není součástí série.</p>',
    'Aplikácia',
    f'<p>{CISTENI_SK}</p><p>Čistiaci krém používajte 1–2× denne, ideálne ráno a večer. Pleťová voda LR ZEITGARD nie je súčasťou série.</p>',
)
N['70111-1'] = (
    'Aplikace',
    f'<ul><li><strong>Čištění:</strong> {CISTENI_CZ}</li><li><strong>Peeling:</strong> {PEELING_CZ}</li><li><strong>Anti-aging:</strong> {ANTIAGING_CZ} Pečující krém není součástí setu.</li><li><strong>Péče o tělo:</strong> {TELO_CZ}</li></ul>',
    'Aplikácia',
    f'<ul><li><strong>Čistenie:</strong> {CISTENI_SK}</li><li><strong>Peeling:</strong> {PEELING_SK}</li><li><strong>Anti-aging:</strong> {ANTIAGING_SK} Ošetrujúci krém nie je súčasťou setu.</li><li><strong>Starostlivosť o telo:</strong> {TELO_SK}</li></ul>',
)

# Bez návodu (výrobce návod neuvádí / nedává smysl):
BEZ = {
    'PB1032 PB1034 PB1001 PB1014 PB1003 PB1002 PB1004 PB1019 PB1030 PB1029': 'tyčinky JETBAR – výrobce návod neuvádí',
    'PB2013 PB2011 PB2008 PB2007 PB2006 PB2005 PB2025': 'medy MEDBAR – výrobce návod neuvádí',
    'PB7001 PB7002 PB7003': 'nápoje AURA/ZEN/VERVE – výrobce uvádí jen skladování (už v popisu)',
    'CE0004 CE0006 CE0007': 'zrnková káva – výrobce způsob přípravy neuvádí',
    'CE0008': 'dodavatel už neprodává',
    'AVE56 AVE57 AVE59 AVE62': 'zubní kartáčky – výrobce návod neuvádí',
    'EBA06': 'ořezávátko',
    '29034-101': 'taštička na make-up',
}
