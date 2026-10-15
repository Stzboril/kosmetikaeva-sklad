# Generátor stránek Doprava a platba + Kontaktní informace (CZ a SK). Čísla účtů jen jako tokeny {{...}}.
import json
CDN='https://cdn.myshoptet.com/usr/www.kosmetikaeva.eu/user/documents/upload/'
Z_LOGO=CDN+'Logo_doprava_platba/Zasilkovna_logo_WEB.png'
KARTY=CDN+'pngegg.png'; APPLE=CDN+'ApplePayLogo.jpg'
QR_CZK=CDN+'QR kody pro platby/CZK.jpg'; QR_EUR=CDN+'QR kody pro platby/EUR.jpg'
Z='<span class="ke-info-zdarma">{}</span>'

def doprava(L):
    cz = L=='cz'
    zd = 'zdarma' if cz else 'zadarmo'
    h=[]
    if cz:
        h.append('<p class="ke-perex">Zboží pečlivě zabalíme a pošleme Zásilkovnou – na výdejní místo, do Z-BOXu nebo kurýrem až k vám domů. Platit můžete kartou, přes Apple Pay nebo převodem, vždy bez poplatku.</p>')
        hl=[('Výdejní místo','80 Kč','zdarma nad 2 500 Kč'),('Kurýr až domů','99 Kč','zdarma nad 3 500 Kč'),('Platba','zdarma','kartou, Apple Pay i převodem'),('Balné','v ceně','je už v ceně dopravy')]
    else:
        h.append('<p class="ke-perex">Tovar starostlivo zabalíme a pošleme cez Packetu – na výdajné miesto, do Z-BOXu alebo kuriérom až k vám domov. Platiť môžete kartou, cez Apple Pay alebo prevodom v eurách, vždy bez poplatku.</p>')
        hl=[('Výdajné miesto','6 €','zadarmo nad 120 €'),('Kuriér až domov','6,70 €','zadarmo nad 120 €'),('Platba','zadarmo','kartou, Apple Pay aj prevodom'),('Balné','v cene','je už v cene dopravy')]
    h.append('<div class="ke-info-hl">'+''.join('<div><span class="ke-info-hl__k">%s</span><b>%s</b><span>%s</span></div>'%x for x in hl)+'</div>')
    if cz:
        h.append('<h2>Způsoby dopravy</h2>\n<div class="ke-mrizka">'
          '<div class="ke-karta" id="Zasilkovna"><img class="ke-info-logo" src="%s" alt="Zásilkovna"><span class="ke-karta-stitek">Nejoblíbenější</span><h3>Výdejní místo nebo Z-BOX</h3><p>Zásilku si vyzvednete na vybrané pobočce Zásilkovny, na partnerském výdejním místě nebo v Z-BOXu. Jakmile bude připravená, přijde vám SMS s kódem pro vyzvednutí. <a href="https://www.zasilkovna.cz/pobocky" target="_blank" rel="noopener">Najít výdejní místo ›</a></p><div class="ke-info-cena"><b>80 Kč</b>, nad 2 500 Kč %s</div></div>'
          '<div class="ke-karta" id="doruceni_kuryrem"><img class="ke-info-logo" src="%s" alt="Zásilkovna"><span class="ke-karta-stitek">Až ke dveřím</span><h3>Kurýr na adresu</h3><p>Zásilku vám přiveze kurýr Zásilkovny až domů na adresu uvedenou v objednávce. Před doručením vám dá vědět, kdy dorazí.</p><div class="ke-info-cena"><b>99 Kč</b>, od 2 500 Kč <b>95 Kč</b>, nad 3 500 Kč %s</div></div>'
          '</div>' % (Z_LOGO, Z.format(zd), Z_LOGO, Z.format(zd)))
        h.append('<h2 id="CZ">Ceník dopravy</h2>\n<div class="ke-tab-obal"><table class="ke-tab ke-info-cenik"><thead><tr><th>Objednávka</th><th>Výdejní místo</th><th>Kurýr na adresu</th></tr></thead><tbody>'
          '<tr><td><span class="ke-nw">do 2&nbsp;500&nbsp;Kč</span></td><td>80&nbsp;Kč</td><td>99&nbsp;Kč</td></tr>'
          '<tr><td><span class="ke-nw">2&nbsp;500–3&nbsp;500&nbsp;Kč</span></td><td>%s</td><td>95&nbsp;Kč</td></tr>'
          '<tr><td><span class="ke-nw">nad 3&nbsp;500&nbsp;Kč</span></td><td>%s</td><td>%s</td></tr></tbody></table></div>' % ((Z.format(zd),)*3))
        h.append('<p class="ke-pozn">Balné je už v ceně dopravy. Nejnižší možná hodnota objednávky je 130 Kč. Elektronické dárkové poukazy posíláme e-mailem zdarma.</p>')
        h.append('<h2>Jak to u nás funguje</h2>\n<ol class="ke-cisla">'
          '<li><strong>Pečlivě zabalíme.</strong> Zboží balíme do papírových krabic, parfémy a křehké věci navíc do bublinkové fólie.</li>'
          '<li><strong>Pošleme odkaz na sledování.</strong> Po předání zásilky dopravci vám přijde e-mail s odkazem, kde uvidíte, kde zásilka právě je.</li>'
          '<li><strong>Dopravce se ozve.</strong> Kurýr vám předem dá vědět, kdy přijede. Na výdejním místě nebo v Z-BOXu na vás zásilka počká a přijde vám SMS s kódem pro vyzvednutí.</li>'
          '<li><strong>Hlídáme každou zásilku.</strong> Průběh doručení denně kontrolujeme. Když se něco zadrhne, sami se vám ozveme a domluvíme řešení.</li></ol>')
        h.append('<h2>Způsoby platby</h2>\n<p>Všechny způsoby platby jsou zdarma. Zboží odesíláme hned po připsání platby.</p>\n<div class="ke-mrizka">'
          '<div class="ke-karta" id="pk"><img class="ke-info-logo" src="%s" alt="Platební karty"><span class="ke-karta-stitek">Zdarma</span><h3>Kartou online</h3><p>Po odeslání objednávky vás přesměrujeme na zabezpečenou platební bránu Comgate, kde zaplatíte kartou.</p></div>'
          '<div class="ke-karta" id="Apple"><img class="ke-info-logo" src="%s" alt="Apple Pay"><span class="ke-karta-stitek">Zdarma</span><h3>Apple Pay</h3><p>Na iPhonu, iPadu nebo Macu zaplatíte přes Apple Pay bez vyplňování údajů o kartě. Platba proběhne přes bránu Comgate.</p></div>'
          '</div>\n<div class="ke-mrizka ke-info-1"><div class="ke-karta" id="air"><span class="ke-karta-stitek">Zdarma</span><h3>Převodem na účet</h3><p>Zaplaťte převodem z internetového bankovnictví, nejrychleji načtením QR kódu. Účet vedeme u Air Bank.</p>'
          '<div class="ke-info-ucet"><img src="%s" alt="QR kód pro platbu"><div class="ke-info-ucet__t"><span>Číslo účtu</span><b>{{CZK_UCET}}</b><span>IBAN</span><b>{{CZK_IBAN}}</b><span>Variabilní symbol</span><b>číslo objednávky</b></div></div></div></div>' % (KARTY, APPLE, QR_CZK))
        h.append('<div class="ke-box" id="dobirka"><span class="ke-box-titulek">Dobírka jen po dohodě</span><p>Protože si zákazníci zásilky na dobírku opakovaně nevyzvedávali, dobírku běžně nenabízíme. Pokud ji opravdu potřebujete, napište nám a domluvíme se.</p></div>')
        h.append('<h2>Dorazila zásilka poškozená?</h2>\n<p>Stává se to výjimečně, ale může se to stát. Pokud je zásilka zjevně poškozená, nepřebírejte ji, sepište s doručovatelem protokol o poškození a co nejdříve se nám ozvěte – vyřešíme to ve váš prospěch. Kdyby dopravce zásilku ztratil, hned vás budeme informovat a domluvíme odeslání nového zboží.</p>')
        h.append('<div class="ke-box ke-info-jinde"><span class="ke-box-titulek">Nakupujete ze Slovenska?</span><p>Ceny dopravy v eurech a platební údaje pro Slovensko najdete ve slovenské verzi této stránky.</p><div class="ke-info-odkazy"><a href="/sk/vse-o-doprave/">Doprava na Slovensko →</a></div></div>')
        h.append('<div class="ke-box"><span class="ke-box-titulek">Máte dotaz k dopravě nebo platbě?</span><p>Zavolejte nám nebo napište, rádi poradíme.</p><div class="ke-info-odkazy"><a href="tel:+420773905902">+420 773 905 902</a><a href="mailto:info@kosmetikaeva.eu">info@kosmetikaeva.eu</a><a href="/kontaktni-informace/">Kontakty</a></div></div>')
    else:
        h.append('<h2>Spôsoby dopravy</h2>\n<div class="ke-mrizka">'
          '<div class="ke-karta" id="Zasilkovna"><span class="ke-karta-stitek">Najobľúbenejšie</span><h3>Výdajné miesto alebo Z-BOX</h3><p>Zásielku si vyzdvihnete na vybranej pobočke Packety, na partnerskom výdajnom mieste alebo v Z-BOXe. Keď bude pripravená, príde vám SMS s kódom na vyzdvihnutie. <a href="https://www.zasilkovna.cz/pobocky" target="_blank" rel="noopener">Nájsť výdajné miesto ›</a></p><div class="ke-info-cena"><b>6 €</b>, nad 120 € %s</div></div>'
          '<div class="ke-karta" id="doruceni_kuryrem"><span class="ke-karta-stitek">Až k dverám</span><h3>Kuriér na adresu</h3><p>Zásielku vám prinesie kuriér Packety až domov na adresu uvedenú v objednávke. Pred doručením vám dá vedieť, kedy príde.</p><div class="ke-info-cena"><b>6,70 €</b>, nad 120 € %s</div></div>'
          '</div>' % (Z.format(zd), Z.format(zd)))
        h.append('<h2 id="SK">Cenník dopravy</h2>\n<div class="ke-tab-obal"><table class="ke-tab ke-info-cenik"><thead><tr><th>Objednávka</th><th>Výdajné miesto</th><th>Kuriér na adresu</th></tr></thead><tbody>'
          '<tr><td><span class="ke-nw">do 120&nbsp;€</span></td><td>6&nbsp;€</td><td>6,70&nbsp;€</td></tr>'
          '<tr><td><span class="ke-nw">nad 120&nbsp;€</span></td><td>%s</td><td>%s</td></tr></tbody></table></div>' % ((Z.format(zd),)*2))
        h.append('<p class="ke-pozn">Balné je už v cene dopravy. Najnižšia možná hodnota objednávky je 12 €. Elektronické darčekové poukážky posielame e-mailom zadarmo.</p>')
        h.append('<h2>Ako to u nás funguje</h2>\n<ol class="ke-cisla">'
          '<li><strong>Starostlivo zabalíme.</strong> Tovar balíme do papierových krabíc, parfumy a krehké veci navyše do bublinkovej fólie.</li>'
          '<li><strong>Pošleme odkaz na sledovanie.</strong> Po odovzdaní zásielky prepravcovi vám príde e-mail s odkazom, kde uvidíte, kde sa zásielka práve nachádza.</li>'
          '<li><strong>Prepravca sa ozve.</strong> Kuriér vám vopred dá vedieť, kedy príde. Na výdajnom mieste alebo v Z-BOXe na vás zásielka počká a príde vám SMS s kódom na vyzdvihnutie.</li>'
          '<li><strong>Strážime každú zásielku.</strong> Priebeh doručenia denne kontrolujeme. Ak sa niečo zasekne, sami sa vám ozveme a dohodneme riešenie.</li></ol>')
        h.append('<h2>Spôsoby platby</h2>\n<p>Všetky spôsoby platby sú zadarmo. Tovar odosielame hneď po pripísaní platby.</p>\n<div class="ke-mrizka">'
          '<div class="ke-karta" id="pk"><img class="ke-info-logo" src="%s" alt="Platobné karty"><span class="ke-karta-stitek">Zadarmo</span><h3>Kartou online</h3><p>Po odoslaní objednávky vás presmerujeme na zabezpečenú platobnú bránu Comgate, kde zaplatíte kartou.</p></div>'
          '<div class="ke-karta" id="Apple"><img class="ke-info-logo" src="%s" alt="Apple Pay"><span class="ke-karta-stitek">Zadarmo</span><h3>Apple Pay</h3><p>Na iPhone, iPade alebo Macu zaplatíte cez Apple Pay bez vypĺňania údajov o karte. Platba prebehne cez bránu Comgate.</p></div>'
          '</div>\n<div class="ke-mrizka ke-info-1"><div class="ke-karta" id="eur"><span class="ke-karta-stitek">Zadarmo</span><h3>Prevodom v eurách (SEPA)</h3><p>Zaplaťte SEPA prevodom zo svojho internet bankingu, najrýchlejšie načítaním QR kódu. Účet vedieme v Air Bank.</p>'
          '<div class="ke-info-ucet"><img src="%s" alt="QR kód pre platbu v eurách"><div class="ke-info-ucet__t"><span>Číslo účtu</span><b>{{EUR_UCET}}</b><span>IBAN</span><b>{{EUR_IBAN}}</b><span>SWIFT/BIC</span><b>AIRACZPP</b><span>Variabilný symbol</span><b>číslo objednávky</b><span>Príjemca</span><b>Stanislav Zboril, Prilucka 4118, Zlin</b></div></div></div></div>' % (KARTY, APPLE, QR_EUR))
        h.append('<div class="ke-box" id="dobirka"><span class="ke-box-titulek">Dobierka len po dohode</span><p>Keďže si zákazníci zásielky na dobierku opakovane nevyzdvihávali, dobierku bežne neponúkame. Ak ju naozaj potrebujete, napíšte nám a dohodneme sa.</p></div>')
        h.append('<h2>Prišla zásielka poškodená?</h2>\n<p>Stáva sa to výnimočne, ale môže sa to stať. Ak je zásielka viditeľne poškodená, nepreberajte ju, spíšte s doručovateľom protokol o poškodení a čo najskôr sa nám ozvite – vyriešime to vo váš prospech. Ak by prepravca zásielku stratil, hneď vás budeme informovať a dohodneme odoslanie nového tovaru.</p>')
        h.append('<div class="ke-box ke-info-jinde"><span class="ke-box-titulek">Nakupujete z Česka?</span><p>Ceny dopravy v korunách a platobné údaje pre Českú republiku nájdete v českej verzii tejto stránky.</p><div class="ke-info-odkazy"><a href="/action/Language/changeLanguage/?language=cs">Doprava do Česka →</a></div></div>')
        h.append('<div class="ke-box"><span class="ke-box-titulek">Máte otázku k doprave alebo platbe?</span><p>Zavolajte nám alebo napíšte, radi poradíme.</p><div class="ke-info-odkazy"><a href="tel:+420773905902">+420 773 905 902</a><a href="mailto:info@kosmetikaeva.eu">info@kosmetikaeva.eu</a><a href="/sk/kontaktni-informace/">Kontakty</a></div></div>')
    return ('<div class="ke-clanek ke-info">\n'+'\n'.join(h)+'\n</div>\n').replace('Z-BOX','<span class="ke-nw">Z-BOX</span>')

def kontakty(L):
    cz = L=='cz'
    if cz:
        perex='Rádi vám poradíme s výběrem kosmetiky, parfémů, doplňků stravy i drogerie a pomůžeme s objednávkou. Ozvěte se nám telefonem, e-mailem nebo přes chat tady na webu.'
        k=[('tel','tel:+420773905902','Telefon','+420 773 905 902','Zavolejte nám'),('mail','mailto:info@kosmetikaeva.eu','E-mail','info@kosmetikaeva.eu','Napište nám'),('fb','https://www.facebook.com/kosmetikaevaeshop','Facebook','KosmetikaEva.eu','Novinky a tipy')]
        prov=('Provozovatel e-shopu','Provozovatel','Firemní údaje','IČO: 86963139<br>DIČ: CZ8008264176<br>Jsme plátci DPH.','Podnikatel zapsaný v živnostenském rejstříku vedeném Magistrátem města Brna.')
        odk=('Mohlo by se hodit',[('/vse-o-doprave/','Doprava a platba'),('/obchodni-podminky/','Obchodní podmínky'),('/hodnoceni-obchodu/','Hodnocení obchodu')])
    else:
        perex='Radi vám poradíme s výberom kozmetiky, parfumov, výživových doplnkov aj drogérie a pomôžeme s objednávkou. Ozvite sa nám telefonicky, e-mailom alebo cez chat priamo na webe.'
        k=[('tel','tel:+420773905902','Telefón','+420 773 905 902','Zavolajte nám'),('mail','mailto:info@kosmetikaeva.eu','E-mail','info@kosmetikaeva.eu','Napíšte nám'),('fb','https://www.facebook.com/kosmetikaevaeshop','Facebook','KosmetikaEva.eu','Novinky a tipy')]
        prov=('Prevádzkovateľ e-shopu','Prevádzkovateľ','Firemné údaje','IČO: 86963139<br>DIČ: CZ8008264176<br>Sme platiteľmi DPH.','Podnikateľ zapísaný v živnostenskom registri vedenom Magistrátom mesta Brna.')
        odk=('Mohlo by sa hodiť',[('/sk/vse-o-doprave/','Doprava a platba'),('/sk/obchodni-podminky/','Obchodné podmienky'),('/sk/hodnotenie-obchodu/','Hodnotenie obchodu')])
    h=['<p class="ke-perex">%s</p>'%perex,'<div class="ke-info-kontakt">'+''.join('<a class="ke-info-k ke-info-k--%s" href="%s"%s><span class="ke-info-k__l">%s</span><b>%s</b><span class="ke-info-k__p">%s</span></a>'%(c,u,' target="_blank" rel="noopener"' if u.startswith('http') else '',l,v,p) for c,u,l,v,p in k)+'</div>',
       '<h2>%s</h2>\n<div class="ke-mrizka"><div class="ke-karta"><span class="ke-karta-stitek">%s</span><h3>Stanislav Zbořil</h3><p>Přílucká 4118<br>760 01 Zlín</p></div><div class="ke-karta"><span class="ke-karta-stitek">%s</span><p>%s</p><p class="ke-pozn">%s</p></div></div>'%prov,
       '<h2>%s</h2>\n<div class="ke-info-odkazy">%s</div>'%(odk[0],''.join('<a href="%s">%s</a>'%x for x in odk[1]))]
    return '<div class="ke-clanek ke-info">\n'+'\n'.join(h)+'\n</div>\n'

out={'keDopravaCz':doprava('cz'),'keDopravaSk':doprava('sk'),'keKontaktyCz':kontakty('cz'),'keKontaktySk':kontakty('sk')}
for k,v in out.items(): open(k+'.html','w',encoding='utf-8').write(v); print(k,len(v))
css=open('ke-info.css',encoding='utf-8').read()
js=''.join("sessionStorage.setItem(%s,%s);"%(json.dumps(k),json.dumps(v)) for k,v in list(out.items())+[('keInfoCss',css)])+"'ok'"
open('payload2.js','w',encoding='utf-8').write(js); print('payload',len(js))
