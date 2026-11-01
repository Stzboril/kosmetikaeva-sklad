# -*- coding: utf-8 -*-
"""Nové výrobky LR 1. 11. 2026 – data pro založení v Shoptetu.

Zástupné značky v popisech (doplní skript v prohlížeči):
  {{INCI:<kód LR>}}            složení doslova z lr-czech.com
  {{B|<id>|<TYP>|<nadpis>}}   rozbalovací blok z popisu existujícího výrobku e-shopu
                               (ve stejném jazyce), nadpis bloku se přepíše
TYP: INCI, USE, NUTR, WARN, PRED, HT, ZAM, UCIN
Ceny: prodejní = aktuální cena LR (u Měsíční akce akční) − 8 %, nahoru na Kč končící 9;
nákupní = aktuální partnerská cena LR (≈ cena LR × 0,741). Bez přeškrtnuté ceny a bez štítku Akce
(nový výrobek nemá cenovou historii).
"""
import json, math

def our(x):
    n = math.ceil(x * 0.92)
    while n % 10 != 9:
        n += 1
    return min(n, x)

VYR_CZ = '<p><strong>Výrobce:</strong> LR Health &amp; Beauty Systems GmbH, Kruppstraße 55, 59227 Ahlen, Německo</p>'
VYR_SK = '<p><strong>Výrobca:</strong> LR Health &amp; Beauty Systems GmbH, Kruppstraße 55, 59227 Ahlen, Nemecko</p>'
VYR_TP = 'LR Health & Beauty Systems GmbH, Kruppstraße 55, 59227 Ahlen, Německo'

def ul(items):
    return '<ul>\n' + '\n'.join(f'<li>{i}</li>' for i in items) + '\n</ul>'

def det(summary, body):
    return f'<details> <summary>{summary}</summary>\n{body}\n</details>'

def page(h2, intro, blocks, obsah, sk=False):
    return (f'<h2><em>{h2}</em></h2>\n<p>{intro}</p>\n<div>' + ' '.join(blocks) + '</div>\n'
            f'<p><strong>Obsah:</strong> {obsah}</p>\n' + (VYR_SK if sk else VYR_CZ))

def inci_cz(code, label=''):
    return det('Složení (Ingredients)' + (f' – {label}' if label else ''), f'<p>{{{{INCI:{code}}}}}</p>')

def inci_sk(code, label=''):
    return det('Zloženie (Ingredients)' + (f' – {label}' if label else ''), f'<p>{{{{INCI:{code}}}}}</p>')

def B(pid, typ, summary):
    return f'{{{{B|{pid}|{typ}|{summary}}}}}'

P = []  # seznam výrobků

def add(**k):
    P.append(k)

TP_DE = [('Země původu', 'Německo'), ('Výrobce', VYR_TP)]

# ---------------------------------------------------------------- 1
add(code='20336-1', lr=239, src=10024, cats=[1693, 1801, 1774], defcat=1774,
    name_cz='LR Aloe Vera Kids Kouzelné třpytivé pěnové mýdlo 200 ml',
    name_sk='LR Aloe Vera Kids Čarovné trblietavé penové mydlo 200 ml',
    tp=[('Objem', '200 ml'), ('Pro koho', 'Děti')] + TP_DE, ip={1255: 157, 1138: 166},
    pkg=(200, 'ml'), weight='0,25',
    meta_cz='Limitované pěnové mýdlo pro děti LR Aloe Vera Kids s 30 % aloe vera a bio broskví. Jemně umyje ruce a třpytivá pěna promění mytí v zábavu.',
    meta_sk='Limitované penové mydlo pre deti LR Aloe Vera Kids s 30 % aloe vera a bio broskyňou. Jemne umyje ruky a trblietavá pena zmení umývanie na zábavu.',
    d_cz=page('Mytí rukou, které děti baví',
        '<strong>Kouzelné třpytivé pěnové mýdlo</strong> z dětské řady LR Aloe Vera Kids je limitovaná zimní edice s ledním medvídkem na lahvičce. Z pumpičky rovnou vychází hebká třpytivá pěna, která ruce jemně umyje a díky 30 % aloe vera a extraktu z bio broskve je nevysušuje. Ovocná vůně a jiskřičky v pěně udělají z každého mytí rukou malý rituál.',
        [det('Hlavní přednosti', ul(['30 % aloe vera a extrakt z bio broskve', 'Hotová pěna přímo z pumpičky – snadné pro malé ruce', 'Jemně čistí a pečuje o hydrataci dětské pokožky', 'Svěží ovocná vůně a třpytivá pěna', 'Limitovaná zimní edice, vyrobeno v Německu'])),
         det('Pro koho je vhodné', '<p>Pro děti, které si rády myjí ruce samy – i pro ty, které je přemlouvat potřeba. Hodí se také jako drobný vánoční dárek.</p>'),
         det('Aplikace', '<p>Jedno až dvě stisknutí pumpičky vezměte do vlhkých dlaní, pěnu rozetřete po rukou a pak důkladně opláchněte vodou.</p>')],
        '200 ml'),
    d_sk=page('Umývanie rúk, ktoré deti baví',
        '<strong>Čarovné trblietavé penové mydlo</strong> z detského radu LR Aloe Vera Kids je limitovaná zimná edícia s ľadovým medvedíkom na fľaštičke. Z pumpičky rovno vychádza jemná trblietavá pena, ktorá ruky šetrne umyje a vďaka 30 % aloe vera a extraktu z bio broskyne ich nevysušuje. Ovocná vôňa a iskričky v pene urobia z každého umývania rúk malý rituál.',
        [det('Hlavné prednosti', ul(['30 % aloe vera a extrakt z bio broskyne', 'Hotová pena priamo z pumpičky – jednoduché pre malé ruky', 'Jemne čistí a stará sa o hydratáciu detskej pokožky', 'Svieža ovocná vôňa a trblietavá pena', 'Limitovaná zimná edícia, vyrobené v Nemecku'])),
         det('Pre koho je vhodné', '<p>Pre deti, ktoré si rady umývajú ruky samy – aj pre tie, ktoré treba prehovárať. Hodí sa aj ako drobný vianočný darček.</p>'),
         det('Aplikácia', '<p>Jedno až dve stlačenia pumpičky naberte do vlhkých dlaní, penu rozotrite po rukách a potom dôkladne opláchnite vodou.</p>')],
        '200 ml', sk=True))

# ---------------------------------------------------------------- 2 (skrytý výrobek 3459 – zveřejnit s novým kódem)
add(code='20613-301', lr=319, reuse=3459, src=2682, cats=[1693, 1927], defcat=1927,
    name_cz='LR Aloe Vera Extra hustý krém na ruce 75 ml',
    name_sk='LR Aloe Vera Extra hustý krém na ruky 75 ml',
    tp=[('Objem', '75 ml'), ('Pro koho', 'Unisex')] + TP_DE, ip={1132: 157, 1153: 166},
    pkg=(75, 'ml'), weight='0,1',
    meta_cz='LR Aloe Vera Extra hustý krém na ruce se 40 % aloe vera a bio měsíčkem. Intenzivní péče pro velmi suché a namáhané ruce, rychle se vstřebá.',
    meta_sk='LR Aloe Vera Extra hustý krém na ruky so 40 % aloe vera a bio nechtíkom. Intenzívna starostlivosť o veľmi suché a namáhané ruky, rýchlo sa vstrebe.',
    d_cz=page('Bohatá péče pro hodně namáhané ruce',
        '<strong>LR Aloe Vera Extra hustý krém na ruce</strong> je určený rukám, kterým běžný krém nestačí – po práci venku, v mrazu nebo po častém mytí. Obsahuje <strong>40 % aloe vera</strong> a extrakt z <strong>bio měsíčku lékařského</strong>, které doplňují panthenol, alantoin, skvalan, rostlinné oleje a vitamín E. Ruce hydratuje a vyživuje, drsná místa zjemní a i přes bohatou texturu se krém rychle vstřebá.',
        [det('Hlavní přednosti', ul(['40 % aloe vera a extrakt z bio měsíčku lékařského', 'Intenzivně pečuje o velmi suchou a drsnou pokožku rukou', 'Panthenol a alantoin pro jemné a hladké ruce', 'Rychle se vstřebává', 'Patentovaná receptura (DE 10 2010 030 654.1)'])),
         det('Pro koho je vhodný', '<p>Pro velmi suché, drsné a namáhané ruce – ženy i muže.</p>'),
         det('Aplikace', '<p>Podle potřeby jemně vmasírujte do pokožky rukou, klidně několikrát denně – nejlépe po každém mytí.</p>'),
         det('Tip', '<p>Krém můžete použít i jako masku na ruce: naneste silnější vrstvu a nechte působit alespoň 30 minut nebo přes noc.</p>'),
         inci_cz('20613-301')],
        '75 ml'),
    d_sk=page('Bohatá starostlivosť pre veľmi namáhané ruky',
        '<strong>LR Aloe Vera Extra hustý krém na ruky</strong> je určený rukám, ktorým bežný krém nestačí – po práci vonku, v mraze alebo po častom umývaní. Obsahuje <strong>40 % aloe vera</strong> a extrakt z <strong>bio nechtíka lekárskeho</strong>, ktoré dopĺňajú panthenol, alantoín, skvalán, rastlinné oleje a vitamín E. Ruky hydratuje a vyživuje, drsné miesta zjemní a napriek bohatej textúre sa krém rýchlo vstrebe.',
        [det('Hlavné prednosti', ul(['40 % aloe vera a extrakt z bio nechtíka lekárskeho', 'Intenzívne sa stará o veľmi suchú a drsnú pokožku rúk', 'Panthenol a alantoín pre jemné a hladké ruky', 'Rýchlo sa vstrebáva', 'Patentovaná receptúra (DE 10 2010 030 654.1)'])),
         det('Pre koho je vhodný', '<p>Pre veľmi suché, drsné a namáhané ruky – ženy aj mužov.</p>'),
         det('Aplikácia', '<p>Podľa potreby jemne vmasírujte do pokožky rúk, pokojne aj niekoľkokrát denne – najlepšie po každom umytí.</p>'),
         det('Tip', '<p>Krém môžete použiť aj ako masku na ruky: naneste hrubšiu vrstvu a nechajte pôsobiť aspoň 30 minút alebo cez noc.</p>'),
         inci_sk('20613-301')],
        '75 ml', sk=True))

# ---------------------------------------------------------------- 3
add(code='20740-201', lr=869, src=3567, cats=[1693, 1921], defcat=1921,
    name_cz='LR Aloe Vera Extra výživný denní krém 50 ml',
    name_sk='LR Aloe Vera Extra výživný denný krém 50 ml',
    tp=[('Objem', '50 ml'), ('Pro koho', 'Unisex')] + TP_DE, ip={1132: 157, 1129: 166},
    pkg=(50, 'ml'), weight='0,15',
    meta_cz='Limitovaný LR Aloe Vera Extra výživný denní krém 50 ml s 50 % aloe vera, arganovým olejem a bio olivou. Bohatá denní péče pro pleť v chladném období.',
    meta_sk='Limitovaný LR Aloe Vera Extra výživný denný krém 50 ml s 50 % aloe vera, argánovým olejom a bio olivou. Bohatá denná starostlivosť o pleť v chladnom období.',
    d_cz=page('Bohatá denní péče na zimní dny',
        'Limitovaný <strong>LR Aloe Vera Extra výživný denní krém</strong> je hutnější varianta denní péče pro chladné měsíce, kdy pleť trápí mráz, vítr a suchý vzduch z topení. Spojuje <strong>50 % gelu aloe vera</strong> s <strong>arganovým olejem</strong>, bambuckým máslem a extraktem z <strong>bio oliv</strong>. Pleť vydatně vyživí a pomáhá ji chránit před chladem a nepříznivými vnějšími vlivy.',
        [det('Hlavní přednosti', ul(['Extra bohatá textura pro chladné období', '50 % gelu aloe vera', 'Arganový olej, bambucké máslo a extrakt z bio oliv', 'Pomáhá chránit pleť před chladem a vnějšími vlivy', 'Limitovaná edice, vyrobeno v Německu'])),
         det('Pro koho je vhodný', '<p>Pro suchou a normální pleť, která v zimě potřebuje víc výživy – pro ženy i muže.</p>'),
         det('Aplikace', '<p>Každé ráno naneste na vyčištěnou pleť obličeje a krku a jemně vmasírujte.</p>'),
         inci_cz('20740-201')],
        '50 ml'),
    d_sk=page('Bohatá denná starostlivosť na zimné dni',
        'Limitovaný <strong>LR Aloe Vera Extra výživný denný krém</strong> je hutnejšia varianta dennej starostlivosti na chladné mesiace, keď pleť trápi mráz, vietor a suchý vzduch z kúrenia. Spája <strong>50 % gélu aloe vera</strong> s <strong>argánovým olejom</strong>, bambuckým maslom a extraktom z <strong>bio olív</strong>. Pleť výdatne vyživí a pomáha ju chrániť pred chladom a nepriaznivými vonkajšími vplyvmi.',
        [det('Hlavné prednosti', ul(['Extra bohatá textúra na chladné obdobie', '50 % gélu aloe vera', 'Argánový olej, bambucké maslo a extrakt z bio olív', 'Pomáha chrániť pleť pred chladom a vonkajšími vplyvmi', 'Limitovaná edícia, vyrobené v Nemecku'])),
         det('Pre koho je vhodný', '<p>Pre suchú a normálnu pleť, ktorá v zime potrebuje viac výživy – pre ženy aj mužov.</p>'),
         det('Aplikácia', '<p>Každé ráno naneste na vyčistenú pleť tváre a krku a jemne vmasírujte.</p>'),
         inci_sk('20740-201')],
        '50 ml', sk=True))

# ---------------------------------------------------------------- 4
add(code='20925-1', lr=685, src=10003, cats=[1693, 1921], defcat=1921,
    name_cz='LR Aloe Vera Pleťové sérum pro posílení kožní bariéry 30 ml',
    name_sk='LR Aloe Vera Pleťové sérum na posilnenie kožnej bariéry 30 ml',
    tp=[('Objem', '30 ml'), ('Pro koho', 'Unisex')] + TP_DE, ip={1132: 157, 1162: 166},
    pkg=(30, 'ml'), weight='0,1',
    meta_cz='Limitované LR Aloe Vera sérum 30 ml s ceramidy, 50 % aloe vera a fermentovaným aloe gelem. Posiluje kožní bariéru a dodává pleti hloubkovou hydrataci.',
    meta_sk='Limitované LR Aloe Vera sérum 30 ml s ceramidmi, 50 % aloe vera a fermentovaným aloe gélom. Posilňuje kožnú bariéru a dodáva pleti hĺbkovú hydratáciu.',
    d_cz=page('Silnější kožní bariéra, víc hydratace',
        'Limitované <strong>LR Aloe Vera Pleťové sérum pro posílení kožní bariéry</strong> (Skin Barrier Serum) je lehké sérum s <strong>ceramidy</strong>, <strong>50 % aloe vera</strong> a <strong>fermentovaným aloe gelem</strong>. Pomáhá posílit ochrannou bariéru pokožky a dodává jí hloubkovou hydrataci – hodí se hlavně v období, kdy pleť zatěžuje chlad, vítr a vytápění.',
        [det('Hlavní přednosti', ul(['Ceramidy pro posílení kožní bariéry', '50 % aloe vera a fermentovaný aloe gel', 'Hloubková hydratace pleti', 'Lehká textura pod krém', 'Limitovaná edice, vyrobeno v Německu'])),
         det('Pro koho je vhodné', '<p>Pro suchou, citlivou a namáhanou pleť, která potřebuje posílit a hydratovat – pro ženy i muže.</p>'),
         det('Aplikace', '<p>Ráno a večer naneste pár kapek na vyčištěnou pleť obličeje a krku, jemně vklepejte a poté použijte krém.</p>'),
         det('Složení (Ingredients)', '<p>LR úplné složení na svém webu zatím neuvádí – doplníme podle obalu.</p>')],
        '30 ml'),
    d_sk=page('Silnejšia kožná bariéra, viac hydratácie',
        'Limitované <strong>LR Aloe Vera Pleťové sérum na posilnenie kožnej bariéry</strong> (Skin Barrier Serum) je ľahké sérum s <strong>ceramidmi</strong>, <strong>50 % aloe vera</strong> a <strong>fermentovaným aloe gélom</strong>. Pomáha posilniť ochrannú bariéru pokožky a dodáva jej hĺbkovú hydratáciu – hodí sa hlavne v období, keď pleť zaťažuje chlad, vietor a kúrenie.',
        [det('Hlavné prednosti', ul(['Ceramidy na posilnenie kožnej bariéry', '50 % aloe vera a fermentovaný aloe gél', 'Hĺbková hydratácia pleti', 'Ľahká textúra pod krém', 'Limitovaná edícia, vyrobené v Nemecku'])),
         det('Pre koho je vhodné', '<p>Pre suchú, citlivú a namáhanú pleť, ktorú treba posilniť a hydratovať – pre ženy aj mužov.</p>'),
         det('Aplikácia', '<p>Ráno a večer naneste pár kvapiek na vyčistenú pleť tváre a krku, jemne vklepte a potom použite krém.</p>'),
         det('Zloženie (Ingredients)', '<p>Úplné zloženie LR na svojom webe zatiaľ neuvádza – doplníme podľa obalu.</p>')],
        '30 ml', sk=True))

# ---------------------------------------------------------------- 5–8 Milk & Honey
MH_CZ = 'Limitovaná zimní řada <strong>LR Milk &amp; Honey</strong> spojuje výživné mléko a cenný med s hřejivou, smyslnou vůní.'
MH_SK = 'Limitovaný zimný rad <strong>LR Milk &amp; Honey</strong> spája výživné mlieko a vzácny med s hrejivou, zmyselnou vôňou.'
add(code='27073-201', lr=469, src=11558, cats=[1693, 1924], defcat=1924,
    name_cz='LR Milk & Honey Tělový krém 200 ml', name_sk='LR Milk & Honey Telový krém 200 ml',
    tp=[('Objem', '200 ml'), ('Pro koho', 'Ženy')] + TP_DE, ip={1117: 157, 1138: 166},
    pkg=(200, 'ml'), weight='0,3',
    meta_cz='Limitovaný LR Milk & Honey Tělový krém 200 ml s mlékem, medem a bambuckým máslem. Bohatá péče pro hebkou pokožku a zimní chvíle pohody.',
    meta_sk='Limitovaný LR Milk & Honey Telový krém 200 ml s mliekom, medom a bambuckým maslom. Bohatá starostlivosť o hebkú pokožku a zimné chvíle pohody.',
    d_cz=page('Hedvábně jemná pokožka s vůní mléka a medu',
        MH_CZ + ' <strong>Tělový krém</strong> má bohatou texturu s mléčným proteinem, extraktem z medu, bambuckým máslem, včelím voskem a mandlovým olejem. Pokožku hýčká, vyživuje a zanechává ji hedvábně jemnou – ideální závěr zimní koupele.',
        [det('Hlavní přednosti', ul(['Bohatý tělový krém s mlékem a medem', 'Bambucké máslo, včelí vosk a mandlový olej', 'Pokožka je hebká a hedvábně jemná', 'Smyslná vůně pro chvíle odpočinku', 'Limitovaná edice – tip na vánoční dárek'])),
         det('Pro koho je vhodný', '<p>Pro všechny, kdo mají rádi bohatou tělovou péči a sladké, hřejivé vůně – zvlášť pro suchou pokožku v zimě.</p>'),
         det('Aplikace', '<p>Po koupeli nebo sprchování naneste na pokožku těla a jemně vmasírujte, dokud se krém nevstřebá.</p>'),
         inci_cz('27073-201')],
        '200 ml'),
    d_sk=page('Hodvábne jemná pokožka s vôňou mlieka a medu',
        MH_SK + ' <strong>Telový krém</strong> má bohatú textúru s mliečnym proteínom, extraktom z medu, bambuckým maslom, včelím voskom a mandľovým olejom. Pokožku hýčka, vyživuje a zanecháva ju hodvábne jemnú – ideálne zakončenie zimného kúpeľa.',
        [det('Hlavné prednosti', ul(['Bohatý telový krém s mliekom a medom', 'Bambucké maslo, včelí vosk a mandľový olej', 'Pokožka je hebká a hodvábne jemná', 'Zmyselná vôňa pre chvíle oddychu', 'Limitovaná edícia – tip na vianočný darček'])),
         det('Pre koho je vhodný', '<p>Pre všetkých, ktorí majú radi bohatú telovú starostlivosť a sladké, hrejivé vône – najmä pre suchú pokožku v zime.</p>'),
         det('Aplikácia', '<p>Po kúpeli alebo sprchovaní naneste na pokožku tela a jemne vmasírujte, kým sa krém nevstrebe.</p>'),
         inci_sk('27073-201')],
        '200 ml', sk=True))

add(code='27074-501', lr=319, src=11555, cats=[1693, 1804], defcat=1804,
    name_cz='LR Milk & Honey Pěna do koupele 250 ml', name_sk='LR Milk & Honey Pena do kúpeľa 250 ml',
    tp=[('Objem', '250 ml'), ('Pro koho', 'Ženy')] + TP_DE, ip={1117: 157, 1156: 166},
    pkg=(250, 'ml'), weight='0,3',
    meta_cz='Limitovaná LR Milk & Honey Pěna do koupele 250 ml s mlékem a medem. Bohatá pěna a smyslná vůně pro relaxační zimní koupel.',
    meta_sk='Limitovaná LR Milk & Honey Pena do kúpeľa 250 ml s mliekom a medom. Bohatá pena a zmyselná vôňa pre relaxačný zimný kúpeľ.',
    d_cz=page('Relaxační koupel s mlékem a medem',
        MH_CZ + ' <strong>Pěna do koupele</strong> vytvoří ve vaně bohatou, jemnou pěnu, pokožku při koupeli hýčká mléčným proteinem a extraktem z medu a celou koupelnu provoní hřejivou vůní. Přesně to pravé na dlouhé zimní večery.',
        [det('Hlavní přednosti', ul(['Jemná pěna do koupele s mlékem a medem', 'Pokožka po koupeli působí hebce a jemně', 'Bohatá pěna a smyslná vůně', 'Pro relaxační zimní rituály', 'Limitovaná edice – tip na vánoční dárek'])),
         det('Pro koho je vhodná', '<p>Pro všechny, kdo si rádi dopřejí dlouhou koupel a hřejivé, sladké vůně.</p>'),
         det('Aplikace', '<p>Do napouštějící se vany nalijte přibližně jedno až dvě víčka pěny a nechte vytvořit pěnu. Po koupeli pokožku opláchněte.</p>'),
         inci_cz('27074-501')],
        '250 ml'),
    d_sk=page('Relaxačný kúpeľ s mliekom a medom',
        MH_SK + ' <strong>Pena do kúpeľa</strong> vytvorí vo vani bohatú, jemnú penu, pokožku pri kúpeli hýčka mliečnym proteínom a extraktom z medu a celú kúpeľňu prevonia hrejivou vôňou. Presne to pravé na dlhé zimné večery.',
        [det('Hlavné prednosti', ul(['Jemná pena do kúpeľa s mliekom a medom', 'Pokožka po kúpeli pôsobí hebko a jemne', 'Bohatá pena a zmyselná vôňa', 'Pre relaxačné zimné rituály', 'Limitovaná edícia – tip na vianočný darček'])),
         det('Pre koho je vhodná', '<p>Pre všetkých, ktorí si radi doprajú dlhý kúpeľ a hrejivé, sladké vône.</p>'),
         det('Aplikácia', '<p>Do napúšťajúcej sa vane nalejte približne jedno až dve viečka peny a nechajte vytvoriť penu. Po kúpeli pokožku opláchnite.</p>'),
         inci_sk('27074-501')],
        '250 ml', sk=True))

add(code='27087-101', lr=275, src=2964, cats=[1693, 1801], defcat=1801,
    name_cz='LR Milk & Honey Krémové mýdlo na ruce 250 ml', name_sk='LR Milk & Honey Krémové mydlo na ruky 250 ml',
    tp=[('Objem', '250 ml'), ('Pro koho', 'Unisex')] + TP_DE, ip={1132: 157, 1156: 166},
    pkg=(250, 'ml'), weight='0,3',
    meta_cz='Limitované LR Milk & Honey Krémové mýdlo na ruce 250 ml s mlékem a medem. Jemně čistí, ruce zanechává hebké a provoněné.',
    meta_sk='Limitované LR Milk & Honey Krémové mydlo na ruky 250 ml s mliekom a medom. Jemne čistí, ruky zanecháva hebké a prevoňané.',
    d_cz=page('Každodenní mytí rukou jako malý luxus',
        MH_CZ + ' <strong>Krémové mýdlo na ruce</strong> s mléčným proteinem a extraktem z medu ruce jemně umyje a zanechá je hebké a příjemně provoněné. Pumpička je praktická u umyvadla v koupelně i v kuchyni.',
        [det('Hlavní přednosti', ul(['Jemné krémové mýdlo s mlékem a medem', 'Šetrně čistí, ruce zůstávají hebké', 'Hřejivá vůně pro každodenní péči', 'Praktické balení s pumpičkou', 'Limitovaná edice – i jako drobný dárek'])),
         det('Pro koho je vhodné', '<p>Pro celou rodinu na každodenní mytí rukou.</p>'),
         det('Aplikace', '<p>Malé množství mýdla napěňte ve vlhkých dlaních, umyjte ruce a důkladně opláchněte vodou.</p>'),
         inci_cz('27087-101')],
        '250 ml'),
    d_sk=page('Každodenné umývanie rúk ako malý luxus',
        MH_SK + ' <strong>Krémové mydlo na ruky</strong> s mliečnym proteínom a extraktom z medu ruky jemne umyje a zanechá ich hebké a príjemne prevoňané. Pumpička je praktická pri umývadle v kúpeľni aj v kuchyni.',
        [det('Hlavné prednosti', ul(['Jemné krémové mydlo s mliekom a medom', 'Šetrne čistí, ruky zostávajú hebké', 'Hrejivá vôňa pre každodennú starostlivosť', 'Praktické balenie s pumpičkou', 'Limitovaná edícia – aj ako drobný darček'])),
         det('Pre koho je vhodné', '<p>Pre celú rodinu na každodenné umývanie rúk.</p>'),
         det('Aplikácia', '<p>Malé množstvo mydla speňte vo vlhkých dlaniach, umyte ruky a dôkladne opláchnite vodou.</p>'),
         inci_sk('27087-101')],
        '250 ml', sk=True))

add(code='27089-1', lr=275, src=2682, cats=[1693, 1927], defcat=1927,
    name_cz='LR Milk & Honey Krém na ruce 75 ml', name_sk='LR Milk & Honey Krém na ruky 75 ml',
    tp=[('Objem', '75 ml'), ('Pro koho', 'Unisex')] + TP_DE, ip={1132: 157, 1153: 166},
    pkg=(75, 'ml'), weight='0,1',
    meta_cz='Limitovaný LR Milk & Honey Krém na ruce 75 ml s propolisem, medem a vitamínem E. Vyživuje suché ruce, rychle se vstřebá a voní mlékem a medem.',
    meta_sk='Limitovaný LR Milk & Honey Krém na ruky 75 ml s propolisom, medom a vitamínom E. Vyživuje suché ruky, rýchlo sa vstrebe a vonia mliekom a medom.',
    d_cz=page('Výživa pro suché ruce v zimě',
        'V zimě dostávají ruce nejvíc zabrat – mráz, topení a časté mytí je vysušují. <strong>LR Milk &amp; Honey Krém na ruce</strong> s extraktem z <strong>propolisu</strong> a medu, mléčným proteinem a vosky ze slunečnice, jojoby a mimózy posiluje kožní bariéru a chrání ruce před vysycháním. <strong>Vitamín E</strong> pomáhá udržet jejich přirozenou hydrataci. Krém se rychle vstřebá a ruce zanechá sametově hebké.',
        [det('Hlavní přednosti', ul(['Intenzivně vyživuje a chrání ruce před popraskáním', 'Pomáhá obnovit přirozenou bariéru pokožky', 'Propolis, med, mléčný protein a vitamín E', 'Rychle se vstřebává, vhodný pro všechny typy pokožky', 'Vůně mléka a medu pro pocit pohody'])),
         det('Pro koho je vhodný', '<p>Pro suché a namáhané ruce, šetrné složení se hodí i pro citlivou pokožku.</p>'),
         det('Aplikace', '<p>Malé množství krému rozetřete v dlaních a vmasírujte do pokožky až ke konečkům prstů, dokud se nevstřebá. Používejte několikrát denně, hlavně po mytí rukou.</p>'),
         inci_cz('27089-1')],
        '75 ml'),
    d_sk=page('Výživa pre suché ruky v zime',
        'V zime dostávajú ruky najviac zabrať – mráz, kúrenie a časté umývanie ich vysušujú. <strong>LR Milk &amp; Honey Krém na ruky</strong> s extraktom z <strong>propolisu</strong> a medu, mliečnym proteínom a voskami zo slnečnice, jojoby a mimózy posilňuje kožnú bariéru a chráni ruky pred vysychaním. <strong>Vitamín E</strong> pomáha udržať ich prirodzenú hydratáciu. Krém sa rýchlo vstrebe a ruky zanechá zamatovo hebké.',
        [det('Hlavné prednosti', ul(['Intenzívne vyživuje a chráni ruky pred popraskaním', 'Pomáha obnoviť prirodzenú bariéru pokožky', 'Propolis, med, mliečny proteín a vitamín E', 'Rýchlo sa vstrebáva, vhodný pre všetky typy pokožky', 'Vôňa mlieka a medu pre pocit pohody'])),
         det('Pre koho je vhodný', '<p>Pre suché a namáhané ruky, šetrné zloženie sa hodí aj pre citlivú pokožku.</p>'),
         det('Aplikácia', '<p>Malé množstvo krému rozotrite v dlaniach a vmasírujte do pokožky až ku končekom prstov, kým sa nevstrebe. Používajte niekoľkokrát denne, hlavne po umytí rúk.</p>'),
         inci_sk('27089-1')],
        '75 ml', sk=True))

# ---------------------------------------------------------------- 9–10 Frosted Rosehip
FR_CZ = 'Limitovaná zimní řada <strong>LR Aloe Vera Frosted Rosehip</strong> spojuje aloe vera, fermentovaný aloe gel a extrakt z bio šípku.'
FR_SK = 'Limitovaný zimný rad <strong>LR Aloe Vera Frosted Rosehip</strong> spája aloe vera, fermentovaný aloe gél a extrakt z bio šípky.'
NOINCI_CZ = det('Složení (Ingredients)', '<p>LR úplné složení na svém webu zatím neuvádí – doplníme podle obalu.</p>')
NOINCI_SK = det('Zloženie (Ingredients)', '<p>Úplné zloženie LR na svojom webe zatiaľ neuvádza – doplníme podľa obalu.</p>')
add(code='27180-1', lr=629, src=11558, cats=[1693, 1924], defcat=1924,
    name_cz='LR Aloe Vera Frosted Rosehip Tělový balzám 250 ml', name_sk='LR Aloe Vera Frosted Rosehip Telový balzam 250 ml',
    tp=[('Objem', '250 ml'), ('Pro koho', 'Unisex')] + TP_DE, ip={1132: 157, 1156: 166},
    pkg=(250, 'ml'), weight='0,3',
    meta_cz='Limitovaný LR Aloe Vera Frosted Rosehip Tělový balzám 250 ml se 75 % aloe vera a bio šípkem. Intenzivně vyživuje a podporuje lipidovou bariéru pokožky.',
    meta_sk='Limitovaný LR Aloe Vera Frosted Rosehip Telový balzam 250 ml so 75 % aloe vera a bio šípkou. Intenzívne vyživuje a podporuje lipidovú bariéru pokožky.',
    d_cz=page('Intenzivní výživa pro suchou pokožku těla',
        FR_CZ + ' <strong>Tělový balzám</strong> (Intense Body Balm) obsahuje <strong>75 % aloe vera</strong>, pokožku intenzivně vyživuje a podporuje její přirozenou lipidovou bariéru – přesně to, co suchá pokožka v zimě potřebuje.',
        [det('Hlavní přednosti', ul(['75 % aloe vera a fermentovaný aloe gel', 'Extrakt z bio šípku', 'Intenzivně vyživuje suchou pokožku', 'Podporuje lipidovou bariéru pokožky', 'Limitovaná zimní edice, vyrobeno v Německu'])),
         det('Pro koho je vhodný', '<p>Pro suchou a namáhanou pokožku těla – pro ženy i muže.</p>'),
         det('Aplikace', '<p>Po sprchování nebo koupeli naneste na pokožku těla a jemně vmasírujte.</p>'),
         NOINCI_CZ],
        '250 ml'),
    d_sk=page('Intenzívna výživa pre suchú pokožku tela',
        FR_SK + ' <strong>Telový balzam</strong> (Intense Body Balm) obsahuje <strong>75 % aloe vera</strong>, pokožku intenzívne vyživuje a podporuje jej prirodzenú lipidovú bariéru – presne to, čo suchá pokožka v zime potrebuje.',
        [det('Hlavné prednosti', ul(['75 % aloe vera a fermentovaný aloe gél', 'Extrakt z bio šípky', 'Intenzívne vyživuje suchú pokožku', 'Podporuje lipidovú bariéru pokožky', 'Limitovaná zimná edícia, vyrobené v Nemecku'])),
         det('Pre koho je vhodný', '<p>Pre suchú a namáhanú pokožku tela – pre ženy aj mužov.</p>'),
         det('Aplikácia', '<p>Po sprchovaní alebo kúpeli naneste na pokožku tela a jemne vmasírujte.</p>'),
         NOINCI_SK],
        '250 ml', sk=True))

add(code='27181-1', lr=319, src=2682, cats=[1693, 1927, 1936], defcat=1927,
    name_cz='LR Aloe Vera Frosted Rosehip Maska na ruce a chodidla 100 ml', name_sk='LR Aloe Vera Frosted Rosehip Maska na ruky a chodidlá 100 ml',
    tp=[('Objem', '100 ml'), ('Pro koho', 'Unisex')] + TP_DE, ip={1132: 157, 1147: 166},
    pkg=(100, 'ml'), weight='0,15',
    meta_cz='Limitovaná LR Aloe Vera Frosted Rosehip Maska na ruce a chodidla 100 ml s aloe vera a bio šípkem. Vyživuje a zjemňuje suchou pokožku rukou i nohou.',
    meta_sk='Limitovaná LR Aloe Vera Frosted Rosehip Maska na ruky a chodidlá 100 ml s aloe vera a bio šípkou. Vyživuje a zjemňuje suchú pokožku rúk aj nôh.',
    d_cz=page('Zimní kúra pro ruce i chodidla',
        FR_CZ + ' <strong>Maska na ruce a chodidla</strong> (Hand &amp; Foot Mask) s <strong>30 % aloe vera</strong> intenzivně vyživuje suchou pokožku, podporuje její regeneraci a zklidňuje ji. Ruce i chodidla jsou po ní zase hebké.',
        [det('Hlavní přednosti', ul(['30 % aloe vera a fermentovaný aloe gel', 'Extrakt z bio šípku', 'Intenzivně vyživuje a zjemňuje suchou pokožku', 'Jedna maska pro ruce i chodidla', 'Limitovaná zimní edice, vyrobeno v Německu'])),
         det('Pro koho je vhodná', '<p>Pro suchou a drsnou pokožku rukou a chodidel.</p>'),
         det('Aplikace', '<p>Naneste silnější vrstvu na čisté ruce a chodidla a nechte působit alespoň 30 minut, případně přes noc (třeba pod bavlněnými rukavicemi a ponožkami). Zbytek vmasírujte do pokožky.</p>'),
         NOINCI_CZ],
        '100 ml'),
    d_sk=page('Zimná kúra pre ruky aj chodidlá',
        FR_SK + ' <strong>Maska na ruky a chodidlá</strong> (Hand &amp; Foot Mask) s <strong>30 % aloe vera</strong> intenzívne vyživuje suchú pokožku, podporuje jej regeneráciu a upokojuje ju. Ruky aj chodidlá sú po nej opäť hebké.',
        [det('Hlavné prednosti', ul(['30 % aloe vera a fermentovaný aloe gél', 'Extrakt z bio šípky', 'Intenzívne vyživuje a zjemňuje suchú pokožku', 'Jedna maska pre ruky aj chodidlá', 'Limitovaná zimná edícia, vyrobené v Nemecku'])),
         det('Pre koho je vhodná', '<p>Pre suchú a drsnú pokožku rúk a chodidiel.</p>'),
         det('Aplikácia', '<p>Naneste hrubšiu vrstvu na čisté ruky a chodidlá a nechajte pôsobiť aspoň 30 minút, prípadne cez noc (napríklad pod bavlnenými rukavicami a ponožkami). Zvyšok vmasírujte do pokožky.</p>'),
         NOINCI_SK],
        '100 ml', sk=True))

# ---------------------------------------------------------------- 11 Into Jungle šampon
add(code='30730-1', lr=339, src=11555, cats=[1693, 1804, 1786, 1777], defcat=1804,
    name_cz='LR Into Jungle Vlasový a tělový šampon 200 ml', name_sk='LR Into Jungle Vlasový a telový šampón 200 ml',
    tp=[('Objem', '200 ml'), ('Pro koho', 'Muži')] + TP_DE, ip={1135: 157, 1138: 166},
    pkg=(200, 'ml'), weight='0,25',
    meta_cz='LR Into Jungle Vlasový a tělový šampon 200 ml s vůní pánského parfému Into Jungle z řady Mood Infusion. Umyje vlasy i tělo v jednom kroku.',
    meta_sk='LR Into Jungle Vlasový a telový šampón 200 ml s vôňou pánskeho parfumu Into Jungle z radu Mood Infusion. Umyje vlasy aj telo v jednom kroku.',
    d_cz=page('Vůně Into Jungle už ze sprchy',
        '<strong>LR Into Jungle Vlasový a tělový šampon</strong> patří k pánské vůni <strong>Into Jungle</strong> z řady LR Mood Infusion. Jeden přípravek do sprchy umyje vlasy i tělo a zanechá na nich jemný závoj vůně, na který pak můžete navázat parfémem.',
        [det('Hlavní přednosti', ul(['Šampon na vlasy i tělo v jednom', 'Parfémovaný vůní Into Jungle', 'Praktický do sprchy, posilovny i na cesty', 'Hodí se jako doplněk k parfému Into Jungle', 'Vyrobeno v Německu'])),
         B(9636, 'HT', 'Hlavní tóny vůně Into Jungle'),
         det('Aplikace', '<p>Malé množství naneste na mokré vlasy a tělo, napěňte a důkladně opláchněte vodou.</p>'),
         NOINCI_CZ],
        '200 ml'),
    d_sk=page('Vôňa Into Jungle už zo sprchy',
        '<strong>LR Into Jungle Vlasový a telový šampón</strong> patrí k pánskej vôni <strong>Into Jungle</strong> z radu LR Mood Infusion. Jeden prípravok do sprchy umyje vlasy aj telo a zanechá na nich jemný závoj vône, na ktorý potom môžete nadviazať parfumom.',
        [det('Hlavné prednosti', ul(['Šampón na vlasy aj telo v jednom', 'Parfumovaný vôňou Into Jungle', 'Praktický do sprchy, posilňovne aj na cesty', 'Hodí sa ako doplnok k parfumu Into Jungle', 'Vyrobené v Nemecku'])),
         B(9636, 'HT', 'Hlavné tóny vône Into Jungle'),
         det('Aplikácia', '<p>Malé množstvo naneste na mokré vlasy a telo, speňte a dôkladne opláchnite vodou.</p>'),
         NOINCI_SK],
        '200 ml', sk=True))

# ---------------------------------------------------------------- 12 Be Flirty tělový krém
add(code='30731-1', lr=629, src=11558, cats=[1693, 1924], defcat=1924,
    name_cz='LR Be Flirty Tělový krém 200 ml', name_sk='LR Be Flirty Telový krém 200 ml',
    tp=[('Objem', '200 ml'), ('Pro koho', 'Ženy')] + TP_DE, ip={1117: 157, 1138: 166},
    pkg=(200, 'ml'), weight='0,35',
    meta_cz='Limitovaný LR Be Flirty Tělový krém 200 ml s vůní dámského parfému Be Flirty z řady Mood Infusion. Pečuje o pokožku a jemně ji provoní.',
    meta_sk='Limitovaný LR Be Flirty Telový krém 200 ml s vôňou dámskeho parfumu Be Flirty z radu Mood Infusion. Stará sa o pokožku a jemne ju prevonia.',
    d_cz=page('Pokožka provoněná vůní Be Flirty',
        'Limitovaný <strong>LR Be Flirty Tělový krém</strong> nese vůni dámského parfému <strong>Be Flirty</strong> z řady LR Mood Infusion. Pokožku po koupeli zjemní a provoní, takže vůně parfému vydrží déle a působí plněji.',
        [det('Hlavní přednosti', ul(['Tělový krém s vůní Be Flirty', 'Zjemňuje a pečuje o pokožku těla', 'Prodlužuje a podtrhuje vůni parfému', 'Elegantní kelímek – i jako dárek', 'Limitovaná edice, vyrobeno v Německu'])),
         B(9594, 'HT', 'Hlavní tóny vůně Be Flirty'),
         det('Aplikace', '<p>Po sprchování nebo koupeli naneste na pokožku těla a jemně vmasírujte. Pro výraznější vůni pak použijte parfém Be Flirty.</p>'),
         NOINCI_CZ],
        '200 ml'),
    d_sk=page('Pokožka prevoňaná vôňou Be Flirty',
        'Limitovaný <strong>LR Be Flirty Telový krém</strong> nesie vôňu dámskeho parfumu <strong>Be Flirty</strong> z radu LR Mood Infusion. Pokožku po kúpeli zjemní a prevonia, takže vôňa parfumu vydrží dlhšie a pôsobí plnšie.',
        [det('Hlavné prednosti', ul(['Telový krém s vôňou Be Flirty', 'Zjemňuje a stará sa o pokožku tela', 'Predlžuje a zvýrazňuje vôňu parfumu', 'Elegantný téglik – aj ako darček', 'Limitovaná edícia, vyrobené v Nemecku'])),
         B(9594, 'HT', 'Hlavné tóny vône Be Flirty'),
         det('Aplikácia', '<p>Po sprchovaní alebo kúpeli naneste na pokožku tela a jemne vmasírujte. Pre výraznejšiu vôňu potom použite parfum Be Flirty.</p>'),
         NOINCI_SK],
        '200 ml', sk=True))

# ---------------------------------------------------------------- 13 Noční maska levandule
add(code='71014-1', lr=739, src=3396, cats=[1693, 1921], defcat=1921,
    name_cz='LR ZEITGARD Noční maska s vůní levandule 50 ml', name_sk='LR ZEITGARD Nočná maska s vôňou levandule 50 ml',
    tp=[('Objem', '50 ml'), ('Pro koho', 'Unisex')] + TP_DE, ip={1132: 157, 1129: 166},
    pkg=(50, 'ml'), weight='0,1',
    meta_cz='LR ZEITGARD Noční maska s vůní levandule 50 ml s jojobovým olejem, schizandrou a Ultra Filling Spheres. Noční anti-age péče, která se nesmývá.',
    meta_sk='LR ZEITGARD Nočná maska s vôňou levandule 50 ml s jojobovým olejom, schizandrou a Ultra Filling Spheres. Nočná anti-age starostlivosť, ktorá sa nezmýva.',
    d_cz=page('Noční péče s uklidňující vůní levandule',
        'Nová <strong>LR ZEITGARD Noční maska s vůní levandule</strong> pečuje o pleť během spánku. Koncentrovaný komplex s <strong>Ultra Filling Spheres™</strong>, <strong>jojobovým olejem</strong> a plody <strong>schizandry</strong> dodává pleti péči proti stárnutí a podporuje její přirozenou noční regeneraci. Vůně levandule navodí pocit klidu před spaním – ráno se probudíte s hebčí, vyživenou a svěže vypadající pletí.',
        [det('Hlavní přednosti', ul(['Vyživuje pleť a podporuje její regeneraci přes noc', 'Jojobový olej pro hydrataci', 'Ultra Filling Spheres™ pro péči proti stárnutí', 'Plody schizandry', 'Uklidňující vůně levandule', 'Nesmývá se – stačí 2× týdně'])),
         det('Pro koho je vhodná', '<p>Pro každého, kdo chce pleti dopřát extra noční péči proti stárnutí a má rád vůni levandule – pro ženy i muže.</p>'),
         det('Aplikace', '<p>Večer naneste na vyčištěnou pleť jako poslední krok péče a nechte působit přes noc, masku neoplachujte. Pro nejlepší výsledek používejte 2× týdně.</p>'),
         inci_cz('71014-1')],
        '50 ml'),
    d_sk=page('Nočná starostlivosť s upokojujúcou vôňou levandule',
        'Nová <strong>LR ZEITGARD Nočná maska s vôňou levandule</strong> sa stará o pleť počas spánku. Koncentrovaný komplex s <strong>Ultra Filling Spheres™</strong>, <strong>jojobovým olejom</strong> a plodmi <strong>schizandry</strong> dodáva pleti starostlivosť proti starnutiu a podporuje jej prirodzenú nočnú regeneráciu. Vôňa levandule navodí pocit pokoja pred spaním – ráno sa zobudíte s hebkejšou, vyživenou a sviežo vyzerajúcou pleťou.',
        [det('Hlavné prednosti', ul(['Vyživuje pleť a podporuje jej regeneráciu cez noc', 'Jojobový olej na hydratáciu', 'Ultra Filling Spheres™ pre starostlivosť proti starnutiu', 'Plody schizandry', 'Upokojujúca vôňa levandule', 'Nezmýva sa – stačí 2× týždenne'])),
         det('Pre koho je vhodná', '<p>Pre každého, kto chce pleti dopriať extra nočnú starostlivosť proti starnutiu a má rád vôňu levandule – pre ženy aj mužov.</p>'),
         det('Aplikácia', '<p>Večer naneste na vyčistenú pleť ako posledný krok starostlivosti a nechajte pôsobiť cez noc, masku neoplachujte. Pre najlepší výsledok používajte 2× týždenne.</p>'),
         inci_sk('71014-1')],
        '50 ml', sk=True))

# ================================================================ SADY
XMAS = 1915
# ---------------------------------------------------------------- 14 Kids set
add(code='20345-1', lr=529, src=11564, cats=[1693, 1774, XMAS], defcat=1774, sada=True,
    name_cz='LR Aloe Vera Kids Set péče pro děti', name_sk='LR Aloe Vera Kids Set starostlivosti pre deti',
    tp=[('Obsah', '250 ml + 200 ml'), ('Pro koho', 'Děti')] + TP_DE, ip={1255: 157},
    pkg=None, weight='0,55',
    meta_cz='Dětský set LR Aloe Vera Kids: přípravek 3v1 šampon, kondicionér a sprchový gel 250 ml + kouzelné třpytivé pěnové mýdlo 200 ml. Tip na dárek.',
    meta_sk='Detský set LR Aloe Vera Kids: prípravok 3v1 šampón, kondicionér a sprchový gél 250 ml + čarovné trblietavé penové mydlo 200 ml. Tip na darček.',
    d_cz=page('Koupání a mytí rukou jako hra',
        '<strong>LR Aloe Vera Kids Set péče pro děti</strong> spojuje dva oblíbené dětské pomocníky: přípravek <strong>3v1 na vlasy i tělo</strong> s opičkou Andym a limitované <strong>Kouzelné třpytivé pěnové mýdlo</strong> s ledním medvídkem. Oba obsahují aloe vera, jsou šetrné k dětské pokožce a díky veselému designu se hodí i pod stromeček.',
        [det('Obsah sady', ul(['LR Aloe Vera Kids Care 3v1 Šampon, kondicionér a sprchový gel 250 ml', 'LR Aloe Vera Kids Kouzelné třpytivé pěnové mýdlo 200 ml (limitovaná edice)'])),
         det('Pro koho je vhodný', '<p>Pro děti, které se rády koupou a myjí samy – a pro rodiče, kteří hledají praktický a hezký dárek.</p>'),
         det('Aplikace', '<p><strong>3v1:</strong> malé množství napěňte na mokrých vlasech a těle a opláchněte vodou.</p>\n<p><strong>Pěnové mýdlo:</strong> jedno až dvě stisknutí pumpičky rozetřete ve vlhkých dlaních, ruce umyjte a opláchněte.</p>'),
         B(10024, 'INCI', 'Složení (Ingredients) – Kids Care 3v1')],
        '250 ml + 200 ml'),
    d_sk=page('Kúpanie a umývanie rúk ako hra',
        '<strong>LR Aloe Vera Kids Set starostlivosti pre deti</strong> spája dvoch obľúbených detských pomocníkov: prípravok <strong>3v1 na vlasy aj telo</strong> s opičkou Andym a limitované <strong>Čarovné trblietavé penové mydlo</strong> s ľadovým medvedíkom. Oba obsahujú aloe vera, sú šetrné k detskej pokožke a vďaka veselému dizajnu sa hodia aj pod stromček.',
        [det('Obsah setu', ul(['LR Aloe Vera Kids Care 3v1 Šampón, kondicionér a sprchový gél 250 ml', 'LR Aloe Vera Kids Čarovné trblietavé penové mydlo 200 ml (limitovaná edícia)'])),
         det('Pre koho je vhodný', '<p>Pre deti, ktoré sa rady kúpu a umývajú samy – a pre rodičov, ktorí hľadajú praktický a pekný darček.</p>'),
         det('Aplikácia', '<p><strong>3v1:</strong> malé množstvo speňte na mokrých vlasoch a tele a opláchnite vodou.</p>\n<p><strong>Penové mydlo:</strong> jedno až dve stlačenia pumpičky rozotrite vo vlhkých dlaniach, ruky umyte a opláchnite.</p>'),
         B(10024, 'INCI', 'Zloženie (Ingredients) – Kids Care 3v1')],
        '250 ml + 200 ml', sk=True))

# ---------------------------------------------------------------- 15 Face set
add(code='20886-1', lr=1159, src=11564, cats=[1693, 1921, XMAS], defcat=1921, sada=True,
    name_cz='LR Aloe Vera Set pro péči o obličej – dárkové balení', name_sk='LR Aloe Vera Set starostlivosti o tvár – darčekové balenie',
    tp=[('Obsah', '50 ml + 30 ml'), ('Pro koho', 'Unisex')] + TP_DE, ip={1132: 157},
    pkg=None, weight='0,3',
    meta_cz='Limitovaný dárkový set LR Aloe Vera: Extra výživný denní krém 50 ml + Pleťové sérum pro posílení kožní bariéry 30 ml. Zimní péče o pleť.',
    meta_sk='Limitovaný darčekový set LR Aloe Vera: Extra výživný denný krém 50 ml + Pleťové sérum na posilnenie kožnej bariéry 30 ml. Zimná starostlivosť o pleť.',
    d_cz=page('Zimní duo pro výživu a silnou kožní bariéru',
        'Limitovaný <strong>LR Aloe Vera Set pro péči o obličej</strong> v dárkovém balení spojuje dvě novinky pro chladné období: <strong>Extra výživný denní krém</strong> s 50 % aloe vera, arganovým olejem a bio olivou a <strong>Pleťové sérum pro posílení kožní bariéry</strong> s ceramidy a fermentovaným aloe gelem. Sérum pleť hloubkově hydratuje, krém ji vyživí a pomáhá chránit před chladem.',
        [det('Obsah sady', ul(['LR Aloe Vera Extra výživný denní krém 50 ml', 'LR Aloe Vera Pleťové sérum pro posílení kožní bariéry 30 ml'])),
         det('Pro koho je vhodný', '<p>Pro suchou a namáhanou pleť v zimě – pro ženy i muže. Hezky zabalený se hodí jako vánoční dárek.</p>'),
         det('Aplikace', '<p><strong>Sérum:</strong> ráno a večer naneste pár kapek na vyčištěnou pleť a jemně vklepejte.</p>\n<p><strong>Denní krém:</strong> každé ráno naneste po séru na obličej a krk a vmasírujte.</p>'),
         inci_cz('20740-201', 'Extra výživný denní krém')],
        '50 ml + 30 ml'),
    d_sk=page('Zimné duo pre výživu a silnú kožnú bariéru',
        'Limitovaný <strong>LR Aloe Vera Set starostlivosti o tvár</strong> v darčekovom balení spája dve novinky na chladné obdobie: <strong>Extra výživný denný krém</strong> s 50 % aloe vera, argánovým olejom a bio olivou a <strong>Pleťové sérum na posilnenie kožnej bariéry</strong> s ceramidmi a fermentovaným aloe gélom. Sérum pleť hĺbkovo hydratuje, krém ju vyživí a pomáha chrániť pred chladom.',
        [det('Obsah setu', ul(['LR Aloe Vera Extra výživný denný krém 50 ml', 'LR Aloe Vera Pleťové sérum na posilnenie kožnej bariéry 30 ml'])),
         det('Pre koho je vhodný', '<p>Pre suchú a namáhanú pleť v zime – pre ženy aj mužov. Pekne zabalený sa hodí ako vianočný darček.</p>'),
         det('Aplikácia', '<p><strong>Sérum:</strong> ráno a večer naneste pár kvapiek na vyčistenú pleť a jemne vklepte.</p>\n<p><strong>Denný krém:</strong> každé ráno naneste po sére na tvár a krk a vmasírujte.</p>'),
         inci_sk('20740-201', 'Extra výživný denný krém')],
        '50 ml + 30 ml', sk=True))

# ---------------------------------------------------------------- 16 Milk & Honey série (skrytý výrobek 4211)
add(code='27091-101', lr=999, reuse=4211, src=11564, cats=[1693, 1924, XMAS], defcat=1924, sada=True,
    name_cz='LR Milk & Honey Série pro péči o tělo – dárkové balení', name_sk='LR Milk & Honey Séria starostlivosti o telo – darčekové balenie',
    tp=[('Obsah', '200 ml + 250 ml + 250 ml + 75 ml'), ('Pro koho', 'Ženy')] + TP_DE, ip={1117: 157},
    pkg=None, weight='1,1',
    meta_cz='Limitovaná dárková série LR Milk & Honey: tělový krém, pěna do koupele, krémové mýdlo a krém na ruce s mlékem a medem. Vánoční dárek.',
    meta_sk='Limitovaná darčeková séria LR Milk & Honey: telový krém, pena do kúpeľa, krémové mydlo a krém na ruky s mliekom a medom. Vianočný darček.',
    d_cz=page('Kompletní zimní rituál s mlékem a medem',
        MH_CZ + ' <strong>Dárková série pro péči o tělo</strong> obsahuje všechny čtyři produkty řady – od relaxační koupele přes mytí rukou až po bohatý tělový krém. Hezky zabalená je hotovým vánočním dárkem.',
        [det('Obsah sady', ul(['LR Milk &amp; Honey Tělový krém 200 ml', 'LR Milk &amp; Honey Pěna do koupele 250 ml', 'LR Milk &amp; Honey Krémové mýdlo na ruce 250 ml', 'LR Milk &amp; Honey Krém na ruce 75 ml'])),
         det('Pro koho je vhodná', '<p>Pro všechny, kdo mají rádi hřejivé, sladké vůně a chvíle pohody – jako dárek pro maminku, kamarádku i pro sebe.</p>'),
         det('Aplikace', '<p><strong>Pěna do koupele:</strong> jedno až dvě víčka do napouštějící se vany.</p>\n<p><strong>Krémové mýdlo:</strong> napěňte ve vlhkých dlaních a opláchněte.</p>\n<p><strong>Tělový krém:</strong> po koupeli vmasírujte do pokožky těla.</p>\n<p><strong>Krém na ruce:</strong> několikrát denně, hlavně po mytí rukou.</p>'),
         inci_cz('27073-201', 'Tělový krém'), inci_cz('27074-501', 'Pěna do koupele'),
         inci_cz('27087-101', 'Krémové mýdlo na ruce'), inci_cz('27089-1', 'Krém na ruce')],
        '200 ml + 250 ml + 250 ml + 75 ml'),
    d_sk=page('Kompletný zimný rituál s mliekom a medom',
        MH_SK + ' <strong>Darčeková séria starostlivosti o telo</strong> obsahuje všetky štyri produkty radu – od relaxačného kúpeľa cez umývanie rúk až po bohatý telový krém. Pekne zabalená je hotovým vianočným darčekom.',
        [det('Obsah setu', ul(['LR Milk &amp; Honey Telový krém 200 ml', 'LR Milk &amp; Honey Pena do kúpeľa 250 ml', 'LR Milk &amp; Honey Krémové mydlo na ruky 250 ml', 'LR Milk &amp; Honey Krém na ruky 75 ml'])),
         det('Pre koho je vhodná', '<p>Pre všetkých, ktorí majú radi hrejivé, sladké vône a chvíle pohody – ako darček pre mamu, kamarátku aj pre seba.</p>'),
         det('Aplikácia', '<p><strong>Pena do kúpeľa:</strong> jedno až dve viečka do napúšťajúcej sa vane.</p>\n<p><strong>Krémové mydlo:</strong> speňte vo vlhkých dlaniach a opláchnite.</p>\n<p><strong>Telový krém:</strong> po kúpeli vmasírujte do pokožky tela.</p>\n<p><strong>Krém na ruky:</strong> niekoľkokrát denne, hlavne po umytí rúk.</p>'),
         inci_sk('27073-201', 'Telový krém'), inci_sk('27074-501', 'Pena do kúpeľa'),
         inci_sk('27087-101', 'Krémové mydlo na ruky'), inci_sk('27089-1', 'Krém na ruky')],
        '200 ml + 250 ml + 250 ml + 75 ml', sk=True))

# ---------------------------------------------------------------- 17 Frosted Rosehip set
add(code='27183-1', lr=755, src=11564, cats=[1693, 1924, XMAS], defcat=1924, sada=True,
    name_cz='LR Aloe Vera Frosted Rosehip Set pro péči o tělo', name_sk='LR Aloe Vera Frosted Rosehip Set starostlivosti o telo',
    tp=[('Obsah', '250 ml + 100 ml'), ('Pro koho', 'Unisex')] + TP_DE, ip={1132: 157},
    pkg=None, weight='0,45',
    meta_cz='Limitovaný set LR Aloe Vera Frosted Rosehip: Tělový balzám 250 ml + Maska na ruce a chodidla 100 ml s aloe vera a bio šípkem. Zimní péče i dárek.',
    meta_sk='Limitovaný set LR Aloe Vera Frosted Rosehip: Telový balzam 250 ml + Maska na ruky a chodidlá 100 ml s aloe vera a bio šípkou. Zimná starostlivosť aj darček.',
    d_cz=page('Zimní péče od hlavy až k patě',
        FR_CZ + ' Set obsahuje <strong>Tělový balzám</strong> se 75 % aloe vera pro intenzivní výživu suché pokožky a <strong>Masku na ruce a chodidla</strong>, která zjemní i nejvíc namáhaná místa.',
        [det('Obsah sady', ul(['LR Aloe Vera Frosted Rosehip Tělový balzám 250 ml', 'LR Aloe Vera Frosted Rosehip Maska na ruce a chodidla 100 ml'])),
         det('Pro koho je vhodný', '<p>Pro suchou pokožku v zimě – pro ženy i muže. Praktický vánoční dárek.</p>'),
         det('Aplikace', '<p><strong>Tělový balzám:</strong> po sprchování vmasírujte do pokožky těla.</p>\n<p><strong>Maska:</strong> silnější vrstvu nechte na rukou a chodidlech působit alespoň 30 minut nebo přes noc, zbytek vmasírujte.</p>'),
         NOINCI_CZ],
        '250 ml + 100 ml'),
    d_sk=page('Zimná starostlivosť od hlavy až po päty',
        FR_SK + ' Set obsahuje <strong>Telový balzam</strong> so 75 % aloe vera na intenzívnu výživu suchej pokožky a <strong>Masku na ruky a chodidlá</strong>, ktorá zjemní aj najviac namáhané miesta.',
        [det('Obsah setu', ul(['LR Aloe Vera Frosted Rosehip Telový balzam 250 ml', 'LR Aloe Vera Frosted Rosehip Maska na ruky a chodidlá 100 ml'])),
         det('Pre koho je vhodný', '<p>Pre suchú pokožku v zime – pre ženy aj mužov. Praktický vianočný darček.</p>'),
         det('Aplikácia', '<p><strong>Telový balzam:</strong> po sprchovaní vmasírujte do pokožky tela.</p>\n<p><strong>Maska:</strong> hrubšiu vrstvu nechajte na rukách a chodidlách pôsobiť aspoň 30 minút alebo cez noc, zvyšok vmasírujte.</p>'),
         NOINCI_SK],
        '250 ml + 100 ml', sk=True))

# ---------------------------------------------------------------- 18 PowerLIFT série
add(code='28101-1', lr=1085, src=11564, cats=[1693, 1921, XMAS], defcat=1921, sada=True,
    name_cz='LR ZEITGARD PowerLIFT Série 2 × 30 ml', name_sk='LR ZEITGARD PowerLIFT Séria 2 × 30 ml',
    tp=[('Obsah', '2 × 30 ml'), ('Pro koho', 'Unisex')] + TP_DE, ip={1132: 157},
    pkg=(60, 'ml'), weight='0,25',
    meta_cz='Výhodná série 2 kusů LR ZEITGARD PowerLIFT Pleťový krém 30 ml – lehká krémová emulze proti stárnutí pleti pro svěží a vypnutý vzhled.',
    meta_sk='Výhodná séria 2 kusov LR ZEITGARD PowerLIFT Pleťový krém 30 ml – ľahká krémová emulzia proti starnutiu pleti pre svieži a vypnutý vzhľad.',
    d_cz=page('Dvojité balení oblíbeného PowerLIFT',
        '<strong>LR ZEITGARD PowerLIFT Série</strong> obsahuje dva kusy pleťového krému <strong>PowerLIFT 30 ml</strong> – lehké krémové emulze proti stárnutí, která unavené pleti rychle dodá svěží a vypnutý vzhled. Výhodné balení vystačí na delší dobu, nebo se o něj můžete rozdělit.',
        [det('Obsah sady', ul(['2 × LR ZEITGARD PowerLIFT Pleťový krém 30 ml'])),
         B(10087, 'PRED', 'Hlavní přednosti'),
         B(10087, 'USE', 'Aplikace'),
         B(10087, 'INCI', 'Složení (Ingredients)')],
        '2 × 30 ml'),
    d_sk=page('Dvojité balenie obľúbeného PowerLIFT',
        '<strong>LR ZEITGARD PowerLIFT Séria</strong> obsahuje dva kusy pleťového krému <strong>PowerLIFT 30 ml</strong> – ľahkej krémovej emulzie proti starnutiu, ktorá unavenej pleti rýchlo dodá svieži a vypnutý vzhľad. Výhodné balenie vystačí na dlhší čas, alebo sa oň môžete podeliť.',
        [det('Obsah setu', ul(['2 × LR ZEITGARD PowerLIFT Pleťový krém 30 ml'])),
         B(10087, 'PRED', 'Hlavné prednosti'),
         B(10087, 'USE', 'Aplikácia'),
         B(10087, 'INCI', 'Zloženie (Ingredients)')],
        '2 × 30 ml', sk=True))

# ---------------------------------------------------------------- 19 Séra série (volný výběr – varianty doplní zvlášť)
SERA = [(9544, 'LR ZEITGARD Vitamín C sérum 30 ml'), (10093, 'LR ZEITGARD Niacinamid sérum 30 ml'), (3897, 'LR ZEITGARD Radiant Youth Pleťový olej 30 ml'), (10078, 'LR ZEITGARD Blue Light Defender Sérum 30 ml')]
add(code='28172', lr=1925, src=11564, cats=[1693, 1921, XMAS], defcat=1921, sada=True, varianty='sera',
    name_cz='LR ZEITGARD Séra pro péči o pleť Série 2 × 30 ml (volný výběr)', name_sk='LR ZEITGARD Séra na starostlivosť o pleť Séria 2 × 30 ml (voľný výber)',
    tp=[('Obsah', '2 × 30 ml'), ('Pro koho', 'Unisex')] + TP_DE, ip={1132: 157},
    pkg=(60, 'ml'), weight='0,25',
    meta_cz='Série 2 sér LR ZEITGARD 30 ml podle vašeho výběru: Vitamín C, Niacinamid, Radiant Youth pleťový olej nebo Blue Light Defender.',
    meta_sk='Séria 2 sér LR ZEITGARD 30 ml podľa vášho výberu: Vitamín C, Niacinamid, Radiant Youth pleťový olej alebo Blue Light Defender.',
    d_cz=page('Dvě séra ZEITGARD podle vaší pleti',
        'V <strong>sérii LR ZEITGARD Séra pro péči o pleť</strong> si vyberete libovolnou kombinaci dvou sér po 30 ml – klidně dvakrát stejné. Kombinaci zvolíte v nabídce u ceny.',
        [det('Z čeho vybírat', ul(['<strong>Vitamín C sérum</strong> – pro rozjasnění a sjednocení tónu pleti', '<strong>Niacinamid sérum</strong> – s 10 % niacinamidu pro hladší pleť a méně viditelné póry', '<strong>Radiant Youth Pleťový olej</strong> – šest olejů přírodního původu pro mladistvý jas', '<strong>Blue Light Defender Sérum</strong> – ochrana pleti před modrým světlem z obrazovek'])),
         det('Aplikace', '<p>Séra nanášejte na vyčištěnou pleť před krémem, několik kapek jemně vklepejte do obličeje a krku. Podrobnosti k jednotlivým sérům najdete u samostatných výrobků.</p>')]
        + [B(pid, 'INCI', f'Složení (Ingredients) – {n.replace("LR ZEITGARD ", "")}') for pid, n in SERA],
        '2 × 30 ml'),
    d_sk=page('Dve séra ZEITGARD podľa vašej pleti',
        'V <strong>sérii LR ZEITGARD Séra na starostlivosť o pleť</strong> si vyberiete ľubovoľnú kombináciu dvoch sér po 30 ml – pokojne dvakrát rovnaké. Kombináciu zvolíte v ponuke pri cene.',
        [det('Z čoho vyberať', ul(['<strong>Vitamín C sérum</strong> – na rozjasnenie a zjednotenie tónu pleti', '<strong>Niacinamid sérum</strong> – s 10 % niacínamidu pre hladšiu pleť a menej viditeľné póry', '<strong>Radiant Youth Pleťový olej</strong> – šesť olejov prírodného pôvodu pre mladistvý jas', '<strong>Blue Light Defender Sérum</strong> – ochrana pleti pred modrým svetlom z obrazoviek'])),
         det('Aplikácia', '<p>Séra nanášajte na vyčistenú pleť pred krémom, niekoľko kvapiek jemne vklepte do tváre a krku. Podrobnosti k jednotlivým sérám nájdete pri samostatných výrobkoch.</p>')]
        + [B(pid, 'INCI', f'Zloženie (Ingredients) – {n.replace("LR ZEITGARD ", "")}') for pid, n in SERA],
        '2 × 30 ml', sk=True))

# ---------------------------------------------------------------- 20 Beauty Diamonds série
add(code='28325-1', lr=3125, src=10054, cats=[1693, 1921, XMAS], defcat=1921, sada=True,
    name_cz='LR ZEITGARD Beauty Diamonds série + kosmetická taštička', name_sk='LR ZEITGARD Beauty Diamonds séria + kozmetická taštička',
    tp=[('Obsah', '50 ml + 50 ml + 30 ml + taštička'), ('Pro koho', 'Ženy')] + TP_DE, ip={1117: 157},
    pkg=None, weight='0,9',
    meta_cz='Série LR ZEITGARD Beauty Diamonds: Denní krém 50 ml, Noční krém 50 ml a 2v1 Oční krém & maska 30 ml + taštička Smart Make-up Pouch.',
    meta_sk='Séria LR ZEITGARD Beauty Diamonds: Denný krém 50 ml, Nočný krém 50 ml a 2v1 Očný krém & maska 30 ml + taštička Smart Make-up Pouch.',
    d_cz=page('Luxusní péče Beauty Diamonds na den, noc i okolí očí',
        '<strong>Série LR ZEITGARD Beauty Diamonds</strong> spojuje tři krémy luxusní řady Beauty Diamonds pro zralou pleť – <strong>denní</strong>, <strong>noční</strong> a <strong>2v1 oční krém &amp; masku</strong>. K sérii dostanete kosmetickou taštičku <strong>LR Zeitgard Signature Smart Make-up Pouch</strong>. Kompletní rituál péče, který se hodí i jako výjimečný dárek.',
        [det('Obsah sady', ul(['LR ZEITGARD Beauty Diamonds Denní krém 50 ml', 'LR ZEITGARD Beauty Diamonds Noční krém 50 ml', 'LR ZEITGARD Beauty Diamonds 2v1 Oční krém &amp; maska 30 ml', 'Kosmetická taštička LR Zeitgard Signature Smart Make-up Pouch'])),
         det('Pro koho je vhodná', '<p>Pro zralou pleť, která si zaslouží luxusní péči – a jako dárek pro ženu, které chcete udělat radost.</p>'),
         B(2121, 'USE', 'Použití – Denní krém'), B(2130, 'USE', 'Použití – Noční krém'), B(10084, 'USE', 'Aplikace – 2v1 Oční krém &amp; maska'),
         B(2121, 'INCI', 'Složení (Ingredients) – Denní krém'), B(2130, 'INCI', 'Složení (Ingredients) – Noční krém'), B(10084, 'INCI', 'Složení (Ingredients) – 2v1 Oční krém &amp; maska')],
        '50 ml + 50 ml + 30 ml + kosmetická taštička'),
    d_sk=page('Luxusná starostlivosť Beauty Diamonds na deň, noc aj okolie očí',
        '<strong>Séria LR ZEITGARD Beauty Diamonds</strong> spája tri krémy luxusného radu Beauty Diamonds pre zrelú pleť – <strong>denný</strong>, <strong>nočný</strong> a <strong>2v1 očný krém &amp; masku</strong>. K sérii dostanete kozmetickú taštičku <strong>LR Zeitgard Signature Smart Make-up Pouch</strong>. Kompletný rituál starostlivosti, ktorý sa hodí aj ako výnimočný darček.',
        [det('Obsah setu', ul(['LR ZEITGARD Beauty Diamonds Denný krém 50 ml', 'LR ZEITGARD Beauty Diamonds Nočný krém 50 ml', 'LR ZEITGARD Beauty Diamonds 2v1 Očný krém &amp; maska 30 ml', 'Kozmetická taštička LR Zeitgard Signature Smart Make-up Pouch'])),
         det('Pre koho je vhodná', '<p>Pre zrelú pleť, ktorá si zaslúži luxusnú starostlivosť – a ako darček pre ženu, ktorej chcete urobiť radosť.</p>'),
         B(2121, 'USE', 'Použitie – Denný krém'), B(2130, 'USE', 'Použitie – Nočný krém'), B(10084, 'USE', 'Aplikácia – 2v1 Očný krém &amp; maska'),
         B(2121, 'INCI', 'Zloženie (Ingredients) – Denný krém'), B(2130, 'INCI', 'Zloženie (Ingredients) – Nočný krém'), B(10084, 'INCI', 'Zloženie (Ingredients) – 2v1 Očný krém &amp; maska')],
        '50 ml + 50 ml + 30 ml + kozmetická taštička', sk=True))

# ---------------------------------------------------------------- 21 Noční maska série (volný výběr)
add(code='71024', lr=1105, src=11564, cats=[1693, 1921, XMAS], defcat=1921, sada=True, varianty='masky',
    name_cz='LR ZEITGARD Noční maska Série 2 × 50 ml (volný výběr)', name_sk='LR ZEITGARD Nočná maska Séria 2 × 50 ml (voľný výber)',
    tp=[('Obsah', '2 × 50 ml'), ('Pro koho', 'Unisex')] + TP_DE, ip={1132: 157, 1141: 166},
    pkg=(100, 'ml'), weight='0,25',
    meta_cz='Série 2 nočních masek LR ZEITGARD 50 ml podle výběru: klasická Noční maska nebo nová Noční maska s vůní levandule, i v kombinaci.',
    meta_sk='Séria 2 nočných masiek LR ZEITGARD 50 ml podľa výberu: klasická Nočná maska alebo nová Nočná maska s vôňou levandule, aj v kombinácii.',
    d_cz=page('Dvě noční masky ZEITGARD podle chuti',
        'V <strong>sérii LR ZEITGARD Noční maska</strong> dostanete dvě noční masky po 50 ml – klasickou <strong>Noční masku</strong>, novou <strong>Noční masku s vůní levandule</strong>, nebo od každé jednu. Kombinaci zvolíte v nabídce u ceny. Obě masky pečují o pleť přes noc a nesmývají se.',
        [det('Z čeho vybírat', ul(['<strong>LR ZEITGARD Noční maska 50 ml</strong> – hydratace, podpora regenerace a péče proti stárnutí s jojobovým olejem a schizandrou', '<strong>LR ZEITGARD Noční maska s vůní levandule 50 ml</strong> – stejná péče s uklidňující vůní levandule'])),
         det('Aplikace', '<p>Dvakrát týdně večer naneste na vyčištěnou pleť jako poslední krok péče a nechte působit přes noc, neoplachujte.</p>'),
         B(3396, 'INCI', 'Složení (Ingredients) – Noční maska'), inci_cz('71014-1', 'Noční maska s vůní levandule')],
        '2 × 50 ml'),
    d_sk=page('Dve nočné masky ZEITGARD podľa chuti',
        'V <strong>sérii LR ZEITGARD Nočná maska</strong> dostanete dve nočné masky po 50 ml – klasickú <strong>Nočnú masku</strong>, novú <strong>Nočnú masku s vôňou levandule</strong>, alebo od každej jednu. Kombináciu zvolíte v ponuke pri cene. Obe masky sa starajú o pleť cez noc a nezmývajú sa.',
        [det('Z čoho vyberať', ul(['<strong>LR ZEITGARD Nočná maska 50 ml</strong> – hydratácia, podpora regenerácie a starostlivosť proti starnutiu s jojobovým olejom a schizandrou', '<strong>LR ZEITGARD Nočná maska s vôňou levandule 50 ml</strong> – rovnaká starostlivosť s upokojujúcou vôňou levandule'])),
         det('Aplikácia', '<p>Dvakrát týždenne večer naneste na vyčistenú pleť ako posledný krok starostlivosti a nechajte pôsobiť cez noc, neoplachujte.</p>'),
         B(3396, 'INCI', 'Zloženie (Ingredients) – Nočná maska'), inci_sk('71014-1', 'Nočná maska s vôňou levandule')],
        '2 × 50 ml', sk=True))

# ---------------------------------------------------------------- 22 Vita Active Red série
add(code='80527-19', lr=1205, src=814, cats=[1687, 1708, XMAS], defcat=1708, sada=True,
    name_cz='LR LIFETAKT Vita Active Red Série 2 × 150 ml', name_sk='LR LIFETAKT Vita Active Red Séria 2 × 150 ml',
    tp=[('Objem', '2 × 150 ml')] + TP_DE, ip={},
    pkg=(300, 'ml'), weight='0,4',
    meta_cz='Doplněk stravy LR LIFETAKT Vita Active Red ve výhodné sérii 2 × 150 ml – koncentrát z ovoce a zeleniny s 10 vitamíny, cca na 60 dní.',
    meta_sk='Doplnok stravy LR LIFETAKT Vita Active Red vo výhodnej sérii 2 × 150 ml – koncentrát z ovocia a zeleniny s 10 vitamínmi, cca na 60 dní.',
    d_cz=page('Vitamínový koncentrát Vita Active Red na dva měsíce',
        '<strong>LR LIFETAKT Vita Active Red Série</strong> obsahuje dvě lahvičky doplňku stravy <strong>Vita Active Red 150 ml</strong> – koncentrátu z červeného ovoce a zeleniny s 10 vitamíny. Jedna lahvička vystačí přibližně na 30 dní, série tedy zhruba na dva měsíce.',
        [det('Obsah sady', ul(['2 × LR LIFETAKT Vita Active Red 150 ml'])),
         B(811, 'USE', 'Použití'), B(811, 'UCIN', 'Hlavní účinné složky'), B(811, 'INCI', 'Složení'), B(811, 'WARN', 'Upozornění')],
        '2 × 150 ml (cca 60 dní)'),
    d_sk=page('Vitamínový koncentrát Vita Active Red na dva mesiace',
        '<strong>LR LIFETAKT Vita Active Red Séria</strong> obsahuje dve fľaštičky doplnku stravy <strong>Vita Active Red 150 ml</strong> – koncentrátu z červeného ovocia a zeleniny s 10 vitamínmi. Jedna fľaštička vystačí približne na 30 dní, séria teda zhruba na dva mesiace.',
        [det('Obsah setu', ul(['2 × LR LIFETAKT Vita Active Red 150 ml'])),
         B(811, 'USE', 'Použitie'), B(811, 'UCIN', 'Hlavné účinné zložky'), B(811, 'INCI', 'Zloženie'), B(811, 'WARN', 'Upozornenie')],
        '2 × 150 ml (cca 60 dní)', sk=True))

# ---------------------------------------------------------------- 23 Cistus série
add(code='80528-199', lr=2199, src=826, cats=[1687, 1918, XMAS], defcat=1918, sada=True,
    name_cz='LR LIFETAKT Cistus Incanus Kapsle Série 2 × 60 kapslí', name_sk='LR LIFETAKT Cistus Incanus Kapsuly Séria 2 × 60 kapsúl',
    tp=[('Forma', 'Kapsle'), ('Počet kusů v balení', '120'), ('Množství', '2 × 60 kapslí')] + TP_DE, ip={1171: 169},
    pkg=(120, 'ks'), weight='0,2',
    meta_cz='Doplněk stravy LR LIFETAKT Cistus Incanus Kapsle ve výhodné sérii 2 × 60 kapslí s extraktem z cistu šedého a vitamínem C.',
    meta_sk='Doplnok stravy LR LIFETAKT Cistus Incanus Kapsuly vo výhodnej sérii 2 × 60 kapsúl s extraktom z cistusu šedého a vitamínom C.',
    d_cz=page('Cistus Incanus Kapsle ve dvojitém balení',
        '<strong>LR LIFETAKT Cistus Incanus Kapsle Série</strong> obsahuje dvě balení doplňku stravy <strong>Cistus Incanus Kapsle po 60 kapslích</strong>. Výhodná série vystačí na delší dobu, zvlášť v zimních měsících.',
        [det('Obsah sady', ul(['2 × LR LIFETAKT Cistus Incanus Kapsle 60 kapslí'])),
         B(826, 'USE', 'Doporučené dávkování'), B(826, 'INCI', 'Složení'), B(826, 'NUTR', 'Výživové údaje'), B(826, 'WARN', 'Upozornění')],
        '2 × 60 kapslí'),
    d_sk=page('Cistus Incanus Kapsuly v dvojitom balení',
        '<strong>LR LIFETAKT Cistus Incanus Kapsuly Séria</strong> obsahuje dve balenia doplnku stravy <strong>Cistus Incanus Kapsuly po 60 kapsulách</strong>. Výhodná séria vystačí na dlhší čas, najmä v zimných mesiacoch.',
        [det('Obsah setu', ul(['2 × LR LIFETAKT Cistus Incanus Kapsuly 60 kapsúl'])),
         B(826, 'USE', 'Odporúčané dávkovanie'), B(826, 'INCI', 'Zloženie'), B(826, 'NUTR', 'Výživové údaje'), B(826, 'WARN', 'Upozornenie')],
        '2 × 60 kapsúl', sk=True))

# ---------------------------------------------------------------- 24–28 Drinking Gel série + krém na ruce
def gelset(code, lr, gid, gname_cz, gname_sk, slug_cz, slug_sk):
    name_cz = f'LR LIFETAKT Aloe Vera Drinking Gel {gname_cz} Série 2 × 1000 ml + Extra hustý krém na ruce'
    name_sk = f'LR LIFETAKT Aloe Vera Drinking Gel {gname_sk} Séria 2 × 1000 ml + Extra hustý krém na ruky'
    add(code=code, lr=lr, src=3441, cats=[1687, 1699, XMAS], defcat=1699, sada=True,
        name_cz=name_cz, name_sk=name_sk,
        tp=[('Obsah', '2 × 1000 ml + 75 ml'), ('Forma', 'Gel')] + TP_DE, ip={1213: 169},
        pkg=None, weight='2,3',
        meta_cz=f'Série 2 × LR Aloe Vera Drinking Gel {gname_cz} 1000 ml (doplněk stravy) a k tomu LR Aloe Vera Extra hustý krém na ruce 75 ml.',
        meta_sk=f'Séria 2 × LR Aloe Vera Drinking Gel {gname_sk} 1000 ml (doplnok stravy) a k tomu LR Aloe Vera Extra hustý krém na ruky 75 ml.',
        d_cz=page(f'Drinking Gel {gname_cz} na tři týdny a krém pro zimní ruce',
            f'Série obsahuje dvě lahve doplňku stravy <strong>LR LIFETAKT Aloe Vera Drinking Gel {gname_cz} 1000 ml</strong> – jedna vystačí přibližně na 11 dní při doporučeném dávkování. K nim dostanete <strong>LR Aloe Vera Extra hustý krém na ruce 75 ml</strong> se 40 % aloe vera a bio měsíčkem pro suché a namáhané ruce.',
            [det('Obsah sady', ul([f'2 × LR LIFETAKT Aloe Vera Drinking Gel {gname_cz} 1000 ml', 'LR Aloe Vera Extra hustý krém na ruce 75 ml'])),
             B(gid, 'USE', f'Doporučené dávkování – Drinking Gel {gname_cz}'),
             B(gid, 'INCI', f'Složení – Drinking Gel {gname_cz}'),
             B(gid, 'NUTR', f'Výživové údaje – Drinking Gel {gname_cz}'),
             B(gid, 'WARN', f'Upozornění – Drinking Gel {gname_cz}'),
             det('Aplikace – Extra hustý krém na ruce', '<p>Podle potřeby jemně vmasírujte do pokožky rukou, klidně několikrát denně.</p>'),
             inci_cz('20613-301', 'Extra hustý krém na ruce')],
            '2 × 1000 ml + 75 ml'),
        d_sk=page(f'Drinking Gel {gname_sk} na tri týždne a krém pre zimné ruky',
            f'Séria obsahuje dve fľaše doplnku stravy <strong>LR LIFETAKT Aloe Vera Drinking Gel {gname_sk} 1000 ml</strong> – jedna vystačí približne na 11 dní pri odporúčanom dávkovaní. K nim dostanete <strong>LR Aloe Vera Extra hustý krém na ruky 75 ml</strong> so 40 % aloe vera a bio nechtíkom pre suché a namáhané ruky.',
            [det('Obsah setu', ul([f'2 × LR LIFETAKT Aloe Vera Drinking Gel {gname_sk} 1000 ml', 'LR Aloe Vera Extra hustý krém na ruky 75 ml'])),
             B(gid, 'USE', f'Odporúčané dávkovanie – Drinking Gel {gname_sk}'),
             B(gid, 'INCI', f'Zloženie – Drinking Gel {gname_sk}'),
             B(gid, 'NUTR', f'Výživové údaje – Drinking Gel {gname_sk}'),
             B(gid, 'WARN', f'Upozornenie – Drinking Gel {gname_sk}'),
             det('Aplikácia – Extra hustý krém na ruky', '<p>Podľa potreby jemne vmasírujte do pokožky rúk, pokojne aj niekoľkokrát denne.</p>'),
             inci_sk('20613-301', 'Extra hustý krém na ruky')],
            '2 × 1000 ml + 75 ml', sk=True))

gelset('80702-680', 1839, 3438, 'Traditional s medem', 'Traditional s medom', '', '')
gelset('80779-681', 1839, 3447, 'Broskev', 'Broskyňa', '', '')
gelset('80802-780', 2059, 3450, 'Intense Sivera', 'Intense Sivera', '', '')
gelset('80868-683', 2059, 3432, 'Active Freedom', 'Active Freedom', '', '')
gelset('81002-19', 2059, 5405, 'Immune Plus', 'Immune Plus', '', '')

# ---------------------------------------------------------------- 29–30 Parfémové sety
def perfset(code, lr, pid, vune, pro, extra_cz, extra_sk, extra_obsah_cz, extra_obsah_sk, cats, ipk):
    vk = 'Pro koho'
    add(code=code, lr=lr, src=11564, cats=cats, defcat=cats[2], sada=True,
        name_cz=f'LR {vune} Pečující set – EdP 50 ml + {extra_cz} + roll-on parfém',
        name_sk=f'LR {vune} Set starostlivosti – EdP 50 ml + {extra_sk} + roll-on parfum',
        tp=[('Obsah', '50 ml + 200 ml + roll-on'), (vk, pro)] + TP_DE, ip={ipk: 157},
        pkg=None, weight='0,75',
        meta_cz=f'Limitovaný set LR {vune}: parfémovaná voda 50 ml, {extra_obsah_cz} 200 ml a roll-on parfém se stejnou vůní. Vánoční dárek z řady Mood Infusion.',
        meta_sk=f'Limitovaný set LR {vune}: parfumovaná voda 50 ml, {extra_obsah_sk} 200 ml a roll-on parfum s rovnakou vôňou. Vianočný darček z radu Mood Infusion.',
        d_cz=page(f'Vůně {vune} ve třech podobách',
            f'Limitovaný <strong>Pečující set {vune}</strong> z řady LR Mood Infusion obsahuje <strong>parfémovanou vodu {vune} 50 ml</strong>, <strong>{extra_obsah_cz} 200 ml</strong> se stejnou vůní a navíc <strong>roll-on parfém</strong> do kabelky či na cesty. Vůni tak můžete vrstvit od sprchy až po večerní vyjití – a máte hotový vánoční dárek.',
            [det('Obsah sady', ul([f'LR {vune} EdP 50 ml', f'LR {vune} {extra_obsah_cz[0].upper() + extra_obsah_cz[1:]} 200 ml', f'LR {vune} roll-on parfém'])),
             B(pid, 'ZAM', 'Zaměření vůně'), B(pid, 'HT', 'Hlavní tóny'),
             B(pid, 'USE', 'Aplikace – parfém'),
             B(pid, 'INCI', 'Složení (Ingredients) – EdP'), B(pid, 'WARN', 'Upozornění k používání')],
            '50 ml + 200 ml + roll-on parfém'),
        d_sk=page(f'Vôňa {vune} v troch podobách',
            f'Limitovaný <strong>Set starostlivosti {vune}</strong> z radu LR Mood Infusion obsahuje <strong>parfumovanú vodu {vune} 50 ml</strong>, <strong>{extra_obsah_sk} 200 ml</strong> s rovnakou vôňou a navyše <strong>roll-on parfum</strong> do kabelky či na cesty. Vôňu tak môžete vrstviť od sprchy až po večerný výstup – a máte hotový vianočný darček.',
            [det('Obsah setu', ul([f'LR {vune} EdP 50 ml', f'LR {vune} {extra_obsah_sk[0].upper() + extra_obsah_sk[1:]} 200 ml', f'LR {vune} roll-on parfum'])),
             B(pid, 'ZAM', 'Zameranie vône'), B(pid, 'HT', 'Hlavné tóny'),
             B(pid, 'USE', 'Aplikácia – parfum'),
             B(pid, 'INCI', 'Zloženie (Ingredients) – EdP'), B(pid, 'WARN', 'Upozornenie k používaniu')],
            '50 ml + 200 ml + roll-on parfum', sk=True))

perfset('30734-1', 1579, 9636, 'Into Jungle', 'Muži', 'šampon', 'šampón', 'vlasový a tělový šampon', 'vlasový a telový šampón', [1693, 1795, 1867, XMAS], 1135)
perfset('30735-1', 1799, 9594, 'Be Flirty', 'Ženy', 'tělový krém', 'telový krém', 'tělový krém', 'telový krém', [1693, 1795, 1864, XMAS], 1117)

# ---------------------------------------------------------------- 31 Cistus Winter Cure Set
add(code='97386-99', lr=5169, src=826, cats=[1687, 1918, XMAS], defcat=1918, sada=True,
    name_cz='LR LIFETAKT Cistus Incanus Winter Cure Set (5 × kapsle + Drinking Gel Immune Plus)',
    name_sk='LR LIFETAKT Cistus Incanus Winter Cure Set (5 × kapsuly + Drinking Gel Immune Plus)',
    tp=[('Obsah', '5 × 60 kapslí + 1000 ml')] + TP_DE, ip={},
    pkg=None, weight='1,6',
    meta_cz='Zimní set LR LIFETAKT: 5 × Cistus Incanus Kapsle a LR Aloe Vera Drinking Gel Immune Plus 1000 ml. Doplňky stravy ve výhodném balení na zimu.',
    meta_sk='Zimný set LR LIFETAKT: 5 × Cistus Incanus Kapsuly a LR Aloe Vera Drinking Gel Immune Plus 1000 ml. Doplnky stravy vo výhodnom balení na zimu.',
    d_cz=page('Zimní set Cistus Incanus a Drinking Gel Immune Plus',
        '<strong>LR LIFETAKT Cistus Incanus Winter Cure Set</strong> spojuje pět balení doplňku stravy <strong>Cistus Incanus Kapsle</strong> a jednu lahev <strong>LR Aloe Vera Drinking Gel Immune Plus 1000 ml</strong>. Výhodné balení na celou zimu.',
        [det('Obsah sady', ul(['5 × LR LIFETAKT Cistus Incanus Kapsle 60 kapslí', '1 × LR LIFETAKT Aloe Vera Drinking Gel Immune Plus 1000 ml'])),
         B(826, 'USE', 'Doporučené dávkování – Cistus Incanus Kapsle'), B(826, 'INCI', 'Složení – Cistus Incanus Kapsle'),
         B(826, 'NUTR', 'Výživové údaje – Cistus Incanus Kapsle'), B(826, 'WARN', 'Upozornění – Cistus Incanus Kapsle'),
         B(5405, 'USE', 'Příprava – Drinking Gel Immune Plus'), B(5405, 'INCI', 'Složení – Drinking Gel Immune Plus'),
         B(5405, 'NUTR', 'Výživové údaje – Drinking Gel Immune Plus'), B(5405, 'WARN', 'Upozornění – Drinking Gel Immune Plus')],
        '5 × 60 kapslí + 1000 ml'),
    d_sk=page('Zimný set Cistus Incanus a Drinking Gel Immune Plus',
        '<strong>LR LIFETAKT Cistus Incanus Winter Cure Set</strong> spája päť balení doplnku stravy <strong>Cistus Incanus Kapsuly</strong> a jednu fľašu <strong>LR Aloe Vera Drinking Gel Immune Plus 1000 ml</strong>. Výhodné balenie na celú zimu.',
        [det('Obsah setu', ul(['5 × LR LIFETAKT Cistus Incanus Kapsuly 60 kapsúl', '1 × LR LIFETAKT Aloe Vera Drinking Gel Immune Plus 1000 ml'])),
         B(826, 'USE', 'Odporúčané dávkovanie – Cistus Incanus Kapsuly'), B(826, 'INCI', 'Zloženie – Cistus Incanus Kapsuly'),
         B(826, 'NUTR', 'Výživové údaje – Cistus Incanus Kapsuly'), B(826, 'WARN', 'Upozornenie – Cistus Incanus Kapsuly'),
         B(5405, 'USE', 'Príprava – Drinking Gel Immune Plus'), B(5405, 'INCI', 'Zloženie – Drinking Gel Immune Plus'),
         B(5405, 'NUTR', 'Výživové údaje – Drinking Gel Immune Plus'), B(5405, 'WARN', 'Upozornenie – Drinking Gel Immune Plus')],
        '5 × 60 kapsúl + 1000 ml', sk=True))

# ---------------------------------------------------------------- výstup
for p in P:
    p['price'] = our(p['lr'])
    p['buy'] = round(p['lr'] * 0.741)
    p['seo_cz'] = f"{p['name_cz']} | KosmetikaEva.eu"
    p['seo_sk'] = f"{p['name_sk']} | KosmetikaEva.eu"
    for k in ('meta_cz', 'meta_sk'):
        assert len(p[k]) <= 165, (p['code'], k, len(p[k]))
json.dump(P, open('products.json', 'w'), ensure_ascii=False, indent=1)
print(len(P), 'výrobků')
for p in P:
    print(f"{p['code']:10} {p['price']:5} nák {p['buy']:5} src {p.get('reuse') or p['src']:6} {p['name_cz']}")
