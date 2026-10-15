# Vyplnitelné formuláře (reklamace, odstoupení) – text podle příloh obchodních podmínek, CZ a SK
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor, white
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
pdfmetrics.registerFont(TTFont('M', 'Montserrat-400-nh.ttf'))
ACC = HexColor('#a3392a'); INK = HexColor('#1c1b29'); TXT = HexColor('#3f3d4f'); MUT = HexColor('#6e6c7a'); BL = HexColor('#fbf3f1'); LINE = HexColor('#e7c9c2')
W, H = A4; L = 50; R = W - 50

T = {
 'cz': dict(kontakt='KosmetikaEva.eu  ·  info@kosmetikaeva.eu  ·  +420 773 905 902', prilohy='Příloha č. {n} obchodních podmínek',
            pozn='Vyplněný formulář můžete poslat e-mailem na info@kosmetikaeva.eu. Pole lze vyplnit přímo v počítači, nebo formulář vytiskněte.',
            datum='Datum:', podpis='Podpis:', poucenih='Poučení'),
 'sk': dict(kontakt='KosmetikaEva.eu  ·  info@kosmetikaeva.eu  ·  +420 773 905 902', prilohy='Príloha č. {n} obchodných podmienok',
            pozn='Vyplnený formulár môžete poslať e-mailom na info@kosmetikaeva.eu. Polia môžete vyplniť priamo v počítači alebo formulár vytlačte.',
            datum='Dátum:', podpis='Podpis:', poucenih='Poučenie'),
}
F = {
 ('cz', 1): dict(file='formular-reklamace.pdf', title='Formulář pro reklamaci', adresat='Adresát: Stanislav Zbořil, Přílucká 4118, 760 01 Zlín', sub='Uplatnění reklamace', intro=None,
   fields=[('Datum uzavření Smlouvy:',1),('Číslo objednávky:',1),('Jméno a příjmení:',1),('Adresa:',1),('E-mailová adresa:',1),('Zboží, které je reklamováno:',2),('Popis vad Zboží:',3),('Navrhovaný způsob pro vyřízení reklamace:',2)],
   after=['Zároveň žádám o vystavení potvrzení o uplatnění reklamace s uvedením, kdy jsem toto právo uplatnil, co je obsahem reklamace, jaký způsob vyřízení reklamace požaduji, spolu s uvedením mých kontaktních údajů pro účely poskytnutí informace o vyřízení reklamace.'], poučení=[]),
 ('cz', 2): dict(file='formular-odstoupeni-od-smlouvy.pdf', title='Formulář pro odstoupení od smlouvy', adresat='Adresát: Stanislav Zbořil, Přílucká 4118, 760 01 Zlín', sub=None, intro='Tímto prohlašuji, že odstupuji od Smlouvy:',
   fields=[('Datum uzavření Smlouvy:',1),('Číslo objednávky:',1),('Jméno a příjmení:',1),('Adresa:',1),('E-mailová adresa:',1),('Specifikace Zboží, kterého se Smlouva týká:',3),('Způsob pro navrácení obdržených finančních prostředků, případně uvedení čísla bankovního účtu:',2)],
   after=[], poučení=[
   'Je-li kupující spotřebitelem, má právo v případě, že objednal zboží prostřednictvím e-shopu www.kosmetikaeva.eu Podnikatele Stanislava Zbořila („Prodávající“) nebo jiného prostředku komunikace na dálku, mimo případy uvedené v § 1837 zák. č. 89/2012 Sb., občanský zákoník, ve znění pozdějších předpisů odstoupit od již uzavřené kupní smlouvy do 14 dnů ode dne uzavření smlouvy, resp. pokud se jedná o koupi zboží, pak do čtrnácti dnů od jeho převzetí. V případě smlouvy, jejímž předmětem je několik kusů zboží nebo dodání několika částí zboží, začíná tato lhůta běžet až dnem dodání posledního kusu nebo části zboží, a v případě smlouvy, na základě které má být zboží dodáváno pravidelně a opakovaně, ode dne dodání první dodávky.',
   'Toto odstoupení oznámí kupující Prodávajícímu písemně na adresu Nová, 467, 691 67 Šakvice nebo elektronicky na e-mail uvedený na vzorovém formuláři.',
   'Odstoupí-li kupující, který je spotřebitelem, od kupní smlouvy, zašle nebo předá Prodávajícímu bez zbytečného odkladu, nejpozději do 14 dnů od odstoupení od kupní smlouvy, zboží, které od něj obdržel.',
   'Odstoupí-li kupující, který je spotřebitelem, od kupní smlouvy, vrátí mu Prodávající bez zbytečného odkladu, nejpozději do 14 dnů od odstoupení od kupní smlouvy, všechny peněžní prostředky (kupní cenu dodaného zboží) včetně nákladů na dodání, které od něho na základě kupní smlouvy přijal, stejným způsobem. Jestliže kupující zvolil jiný, než nejlevnější způsob dodání zboží, který Prodávající nabízí, vrátí Prodávající kupujícímu náklady na dodání zboží pouze ve výši odpovídající nejlevnějšímu nabízenému způsobu dodání zboží. Prodávající není povinen vrátit přijaté peněžní prostředky kupujícímu dříve, než zboží obdrží zpět nebo než kupující prokáže, že zboží Prodávajícímu odeslal.']),
 ('sk', 1): dict(file='formular-reklamacia.pdf', title='Formulár na reklamáciu', adresat='Adresát: Stanislav Zbořil, Přílucká 4118, 760 01 Zlín', sub='Uplatnenie reklamácie', intro=None,
   fields=[('Dátum uzavretia Zmluvy:',1),('Číslo objednávky:',1),('Meno a priezvisko:',1),('Adresa:',1),('E-mailová adresa:',1),('Tovar, ktorý je reklamovaný:',2),('Opis vád Tovaru:',3),('Navrhovaný spôsob vybavenia reklamácie:',2)],
   after=['Zároveň žiadam o vystavenie potvrdenia o uplatnení reklamácie s uvedením, kedy som toto právo uplatnil, čo je obsahom reklamácie, aký spôsob vybavenia reklamácie požadujem, spolu s uvedením mojich kontaktných údajov na účely poskytnutia informácie o vybavení reklamácie.'], poučení=[]),
 ('sk', 2): dict(file='formular-odstupenie-od-zmluvy.pdf', title='Formulár na odstúpenie od zmluvy', adresat='Adresát: Stanislav Zbořil, Přílucká 4118, 760 01 Zlín', sub=None, intro='Týmto vyhlasujem, že odstupujem od Zmluvy:',
   fields=[('Dátum uzavretia Zmluvy:',1),('Číslo objednávky:',1),('Meno a priezvisko:',1),('Adresa:',1),('E-mailová adresa:',1),('Špecifikácia Tovaru, ktorého sa Zmluva týka:',3),('Spôsob na vrátenie prijatých finančných prostriedkov, prípadne uvedenie čísla bankového účtu:',2)],
   after=[], poučení=[
   'Ak je kupujúci spotrebiteľom, má právo v prípade, že objednal Tovar prostredníctvom e-shopu www.kosmetikaeva.eu Podnikateľa Stanislava Zbořila („Predávajúci“) alebo iného prostriedku komunikácie na diaľku, okrem prípadov uvedených v § 1837 zákona č. 89/2012 Zb., Občiansky zákonník, v znení neskorších predpisov, odstúpiť od už uzavretej kúpnej zmluvy do 14 dní odo dňa uzavretia zmluvy, resp. ak ide o kúpu tovaru, potom do štrnástich dní od jeho prevzatia. V prípade zmluvy, ktorej predmetom je niekoľko kusov Tovaru alebo dodanie niekoľkých častí Tovaru, začína táto lehota plynúť až dňom dodania posledného kusu alebo časti Tovaru, a v prípade zmluvy, na základe ktorej má byť Tovar dodávaný pravidelne a opakovane, odo dňa dodania prvej dodávky.',
   'Toto odstúpenie oznámi kupujúci Predávajúcemu písomne na adresu Nová, 467, 691 67 Šakvice alebo elektronicky na e-mail uvedený vo vzorovom formulári.',
   'Ak odstúpi kupujúci, ktorý je spotrebiteľom, od kúpnej zmluvy, zašle alebo odovzdá Predávajúcemu bez zbytočného odkladu, najneskôr do 14 dní od odstúpenia od kúpnej zmluvy, Tovar, ktorý od neho obdržal.',
   'Ak odstúpi kupujúci, ktorý je spotrebiteľom, od kúpnej zmluvy, vráti mu Predávajúci bez zbytočného odkladu, najneskôr do 14 dní od odstúpenia od kúpnej zmluvy, všetky peňažné prostriedky (kúpnu cenu dodaného Tovaru) vrátane nákladov na dodanie, ktoré od neho na základe kúpnej zmluvy prijal, rovnakým spôsobom. Ak kupujúci zvolil iný než najlacnejší spôsob dodania Tovaru, ktorý Predávajúci ponúka, vráti Predávajúci kupujúcemu náklady na dodanie Tovaru iba vo výške zodpovedajúcej najlacnejšiemu ponúkanému spôsobu dodania Tovaru. Predávajúci nie je povinný vrátiť prijaté peňažné prostriedky kupujúcemu skôr, než Tovar obdrží späť alebo než kupujúci preukáže, že Tovar Predávajúcemu odoslal.']),
}
PS = ParagraphStyle('p', fontName='M', fontSize=9.6, leading=14, textColor=TXT)
PSS = ParagraphStyle('s', fontName='M', fontSize=8.4, leading=12, textColor=TXT)

def header(c, lang, n):
    c.drawImage('logo.jpg', L, H-74, width=150, height=38, mask='auto')
    c.setFont('M', 8.5); c.setFillColor(MUT); c.drawRightString(R, H-52, T[lang]['kontakt'])
    c.setStrokeColor(ACC); c.setLineWidth(1.2); c.line(L, H-86, R, H-86)

def para(c, text, y, style=PS, width=None):
    p = Paragraph(text, style); w, h = p.wrap((width or (R-L)), 1000); p.drawOn(c, L, y-h); return y-h

def build(lang, n):
    d = F[(lang, n)]; t = T[lang]
    c = canvas.Canvas(d['file'], pagesize=A4, pageCompression=1)
    c.setTitle(d['title'] + ' – KosmetikaEva.eu'); c.setAuthor('Stanislav Zbořil – KosmetikaEva.eu'); c.setSubject(t['prilohy'].format(n=n))
    header(c, lang, n)
    y = H-122
    c.setFont('M', 9); c.setFillColor(ACC); c.drawString(L, y, t['prilohy'].format(n=n).upper())
    y -= 26; c.setFont('M', 22); c.setFillColor(ACC); c.drawString(L, y, d['title'])
    y -= 30
    # adresát v rámečku
    c.setFillColor(BL); c.roundRect(L, y-30, R-L, 34, 8, stroke=0, fill=1)
    c.setFont('M', 10); c.setFillColor(INK); c.drawString(L+14, y-17, d['adresat'])
    y -= 54
    if d['sub']:
        c.setFont('M', 12.5); c.setFillColor(INK); c.drawString(L, y, d['sub']); y -= 20
    if d['intro']:
        c.setFont('M', 10.5); c.setFillColor(INK); c.drawString(L, y, d['intro']); y -= 20
    form = c.acroForm
    for i, (lab, rows) in enumerate(d['fields']):
        y = para(c, '<font name="M" color="#1c1b29">%s</font>' % lab, y, PS) - 4
        hgt = 20 if rows == 1 else 14*rows+8
        form.textfield(name='pole%d' % (i+1), tooltip=lab, x=L, y=y-hgt, width=R-L, height=hgt, fontName='Helvetica', fontSize=10,
                       borderStyle='solid', borderColor=LINE, fillColor=HexColor('#fffdfc'), textColor=INK, borderWidth=0.8,
                       fieldFlags='multiline' if rows > 1 else '', forceBorder=True)
        y -= hgt + 10
    for a in d['after']:
        y = para(c, a, y-2, PS) - 12
    # datum a podpis
    y -= 8
    c.setFont('M', 10); c.setFillColor(INK); c.drawString(L, y, t['datum'])
    form.textfield(name='datum', tooltip=t['datum'], x=L+48, y=y-6, width=150, height=20, fontName='Helvetica', fontSize=10, borderStyle='solid', borderColor=LINE, fillColor=HexColor('#fffdfc'), textColor=INK, borderWidth=0.8, forceBorder=True)
    c.drawString(L+250, y, t['podpis']); c.setStrokeColor(MUT); c.setLineWidth(0.6); c.line(L+300, y-4, R, y-4)
    y -= 34
    if d['poučení']:
        if y < 300:
            c.setFont('M', 8); c.setFillColor(MUT); c.drawString(L, 36, t['pozn']); c.showPage(); header(c, lang, n); y = H-122
        c.setFont('M', 11.5); c.setFillColor(INK); c.drawString(L, y, t['poucenih']); y -= 10
        for p in d['poučení']:
            y = para(c, p, y, PSS) - 7
    c.setFont('M', 8); c.setFillColor(MUT); c.drawString(L, 36, t['pozn'])
    c.save(); return d['file']

for k in F: print(build(*k))
