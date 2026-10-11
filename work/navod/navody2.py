# Tipy k podávání (výrobce návod neuvádí – majitel schválil doplnění 11. 10. 2026)
# kód -> (titulek CZ, html CZ, titulek SK, html SK)
N = {}

TYCINKA = (
    'Jak podávat',
    '<p>Tyčinka je připravená k jídlu hned po rozbalení. Hodí se jako rychlá svačina do školy, do práce, na výlet nebo ke sportu.</p>',
    'Ako podávať',
    '<p>Tyčinka je pripravená na jedenie hneď po rozbalení. Hodí sa ako rýchla desiata do školy, do práce, na výlet alebo k športu.</p>',
)
for k in 'PB1032 PB1034 PB1001 PB1014 PB1003 PB1002 PB1004 PB1019 PB1030 PB1029'.split():
    N[k] = TYCINKA

MED_BYLINY = (
    'Jak podávat',
    '<p>Vychutnejte si ho samotný na lžičce, na pečivu nebo jím oslaďte čaj. Do čaje ho přidávejte, až trochu přechladne – med patří do teplého, ne horkého nápoje.</p>',
    'Ako podávať',
    '<p>Vychutnajte si ho samotný na lyžičke, na pečive alebo ním osláďte čaj. Do čaju ho pridávajte, až trochu vychladne – med patrí do teplého, nie horúceho nápoja.</p>',
)
for k in 'PB2011 PB2008 PB2007 PB2006 PB2005'.split():
    N[k] = MED_BYLINY

N['PB2013'] = (
    'Jak podávat',
    '<p>Hodí se do snídaňové kaše, do jogurtu, k palačinkám nebo na pečivo. Vychutnat si ji můžete i jen tak na lžičce.</p>',
    'Ako podávať',
    '<p>Hodí sa do raňajkovej kaše, do jogurtu, k palacinkám alebo na pečivo. Vychutnať si ju môžete aj len tak na lyžičke.</p>',
)

N['PB2025'] = (
    'Jak podávat',
    '<p>Vychutnejte si ho samotný na lžičce, na pečivu, v jogurtu nebo jím oslaďte čaj či mléko. Do nápoje ho přidávejte, až trochu přechladne – med patří do teplého, ne horkého nápoje.</p>',
    'Ako podávať',
    '<p>Vychutnajte si ho samotný na lyžičke, na pečive, v jogurte alebo ním osláďte čaj či mlieko. Do nápoja ho pridávajte, až trochu vychladne – med patrí do teplého, nie horúceho nápoja.</p>',
)

NAPOJ = (
    'Jak podávat',
    '<p>Nejlépe chutná dobře vychlazený, klidně s ledem. Po otevření uchovávejte v chladu a spotřebujte do 24 hodin.</p>',
    'Ako podávať',
    '<p>Najlepšie chutí dobre vychladený, pokojne s ľadom. Po otvorení uchovávajte v chlade a spotrebujte do 24 hodín.</p>',
)
for k in 'PB7001 PB7002 PB7003'.split():
    N[k] = NAPOJ

KAVA = (
    'Příprava',
    '<p>Zrna umelte až těsně před přípravou – káva si tak zachová co nejvíc aroma. Po otevření sáček vždy pečlivě uzavřete.</p>',
    'Príprava',
    '<p>Zrná zomeľte až tesne pred prípravou – káva si tak zachová čo najviac arómy. Po otvorení vrecko vždy starostlivo uzavrite.</p>',
)
for k in 'CE0004 CE0006 CE0007 CE0008'.split():
    N[k] = KAVA
