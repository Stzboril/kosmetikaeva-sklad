#!/usr/bin/env python3
"""Přiřazení kategorií Heureka.cz / Zboží.cz a názvů parfémů do XML feedu (xmlFeedName)
pro produkty KosmetikaEva.eu (Shoptet).

Vstupy (ve stejné složce):
  eshop_kategorie.tsv  code, pairCode, manufacturer, defaultCategory, name (bez hlavičky)
  moznosti.json        {"H": [[value, nazev, cesta_skupiny], ...], "Z": [...]} = hodnoty z roletek Shoptetu
Výstup:
  vystup.json          {code: {"heureka": value|"", "zbozi": value|"", "xmlFeedName": str|""}}

Kategorie se v pravidlech zadávají NÁZVEM (příp. s částí cesty pro jednoznačnost);
funkce h()/z() je převedou na value z moznosti.json a skončí chybou, pokud název
neexistuje nebo není jednoznačný – do výstupu se tak nedostane nic mimo nabídku Shoptetu.
"""
import json
import os
import re
import sys
from collections import defaultdict

BASE = os.path.dirname(os.path.abspath(__file__))
OPT = json.load(open(os.path.join(BASE, 'moznosti.json'), encoding='utf-8'))


def _lookup(kind, name, within=''):
    hits = {v for v, n, p in OPT[kind] if n == name and within in p}
    if len(hits) != 1:
        sys.exit(f'Kategorie {kind} "{name}" ({within}) – nalezeno {len(hits)}: {hits}')
    return hits.pop()


def h(name, within=''):
    return _lookup('H', name, within)


def z(name, within=''):
    return _lookup('Z', name, within)


def R(pattern, hname, zname, hwithin='', zwithin=''):
    """Pravidlo: regulární výraz nad názvem produktu -> (heureka value, zbozi value)."""
    return (re.compile(pattern, re.I), h(hname, hwithin), z(zname, zwithin))


# ---------------------------------------------------------------- sdílené kategorie
SADA = (h('Kosmetické sady'), z('Kosmetické sady'))
DOPLNEK_H = h('Vitamíny a doplňky stravy')


def je_smisena_sada(name):
    """Dárková / smíšená sada → Kosmetické sady.
    Nepočítá se: „X + refill“ (stejný produkt ve dvou baleních) a multipacky
    stejného produktu („Série 6 x 1000 ml“, „série 2 ks“, „3 × 100 ml“)."""
    if re.search(r'refill', name, re.I) and '+' in name:
        return False
    if re.search(r'\d+\s*[x×]\s*\d', name) or re.search(r'série\s*\d+\s*ks', name, re.I):
        return False
    if re.search(r'\d+\s*ks\b', name) and not re.search(r'\b(set|sada|série)\b', name, re.I):
        return False
    return bool(re.search(r'\b(set|sada|série|duo|combo)\b', name, re.I))


# ---------------------------------------------------------------- pravidla podle kategorie e-shopu
# Každá položka: defaultCategory -> (seznam pravidel [první shoda vyhrává; 'SADA' = test smíšené sady], výchozí (H, Z))
PRANI = [
    R(r'čistič pračky', 'Čisticí prostředky na spotřebiče', 'Čističe pračky'),
    R(r'skvrn', 'Odstraňovače skvrn', 'Odstraňovače skvrn'),
    R(r'agent s obsahem kyslíku', 'Bělidla, změkčovadla, škroby', 'Odstraňovače skvrn'),
    R(r'žehličk|tužidlo', 'Bělidla, změkčovadla, škroby', 'Škroby'),
    R(r'sušičk', 'Vůně do sušičky', 'Parfémy na praní'),
    R(r'kondicionér|neutralizační', 'Aviváže', 'Aviváže'),
    R(r'\d\s*g\b', 'Prací prášky', 'Prací prášky'),          # sypký prací prostředek (g)
    R(r'\d\s*ml\b|tekut|gel', 'Prací gely', 'Prací gely'),   # tekutý prací prostředek (ml)
]
PRANI_DEF = (h('Prací gely'), z('Prací gely'))

ODLICOVANI = [
    R(r'micelár', 'Přípravky na čištění pleti', 'Micelární vody'),
    R(r'odličovač|dvoufázov|pleťové mléko', 'Přípravky na čištění pleti', 'Odličovače'),
    R(r'ubrousk', 'Přípravky na čištění pleti', 'Odličovací ubrousky'),
    R(r'tonik|pleťová voda|toner|růžová voda', 'Přípravky na čištění pleti', 'Pleťové vody a tonika'),
    R(r'mýdl', 'Přípravky na čištění pleti', 'Čisticí mýdla'),
    R(r'čistic|čistíc|mycí krém', 'Přípravky na čištění pleti', 'Čisticí gely'),
]

KAT = {
    # ------------------------------------------------ PARFÉMY (zbozi doplněno podle pohlaví níže)
    'Kosmetika > Parfémy': ([], None),
    'Kosmetika > Parfémy > Dámské parfémy': ([], None),
    'Kosmetika > Parfémy > Pánské parfémy': ([], None),
    'Kosmetika > Parfémy > Unisex parfémy': ([], None),

    # ------------------------------------------------ KOSMETIKA
    'Kosmetika > Obličej': ([
        R(r'ZEITGARD PRO .*hlavice', 'Přístroje na čištění pleti', 'Příslušenství k elektrickým čističům pleti'),
        R(r'ZEITGARD PRO .*(set|série)', 'Přístroje na čištění pleti', 'Elektrické čističe pleti'),
        R(r'gua sha', 'Ostatní kosmetické pomůcky', 'Ostatní kosmetické pomůcky'),
        'SADA',
        R(r'nosní sprej', 'Nosní kapky, spreje a oleje', 'Nosní spreje'),
        R(r'(?<!\w)oční|eye patch', 'Oční krémy a gely', 'Péče o oční okolí'),
        R(r'balzám na rty', 'Balzámy na rty', 'Péče o rty'),
        R(r'dekolt', 'Přípravky pro péči o krk a dekolt', 'Péče o krk a dekolt'),
        *ODLICOVANI,
        R(r'peeling', 'Přípravky na čištění pleti', 'Pleťové peelingy'),
        R(r'mask', 'Pleťové masky', 'Pleťové masky'),
        R(r'perfector', 'Tónovací krémy', 'BB a CC krémy'),
        R(r'sérum|serum|essence|koncentrát', 'Pleťová séra, emulze a koncentráty', 'Pleťová séra'),
        R(r'\bolej\b|\boil\b', 'Pleťové oleje', 'Pleťové oleje'),
    ], (h('Pleťové krémy'), z('Pleťové krémy'))),

    'Kosmetika > Tělo': ([
        R(r'ZEITGARD PRO .*hlavice', 'Přístroje na čištění pleti', 'Příslušenství k elektrickým čističům pleti'),
        R(r'ZEITGARD PRO .*set', 'Přístroje na čištění pleti', 'Elektrické čističe pleti'),
        'SADA',
        R(r'pleťov.*mask', 'Pleťové masky', 'Pleťové masky'),
        R(r'pleťov.*peeling', 'Přípravky na čištění pleti', 'Pleťové peelingy'),
        R(r'\bdeo', 'Deodoranty a antiperspiranty', 'Deodoranty a antiperspiranty'),
        R(r'intim', 'Intimní mycí prostředky', 'Intimní hygienické prostředky'),
        R(r'gel na holení', 'Pěny a gely na holení', 'Gely na holení'),
        R(r'celulit|strie', 'Přípravky na celulitidu a strie', 'Celulitida a strie'),
        R(r'tvarující|zeštíhl', 'Zeštíhlující přípravky', 'Zeštíhlující přípravky'),
        R(r'roll-on', 'Masážní přípravky', 'Masážní roll-ony'),
        R(r'(hřejiv|chladiv).*krém', 'Masážní přípravky', 'Masážní krémy'),
        R(r'MSM', 'Masážní přípravky', 'Masážní gely'),
        R(r'peeling', 'Tělové peelingy', 'Tělové peelingy'),
        R(r'\bolej\b|\boil\b', 'Tělové oleje', 'Tělové oleje'),
        R(r'máslo', 'Tělová másla', 'Tělová másla'),
        R(r'mléko', 'Tělová mléka', 'Tělová mléka'),
        R(r'balzám', 'Tělové balzámy', 'Tělové balzámy'),
    ], (h('Tělové krémy'), z('Tělové krémy'))),

    'Kosmetika > Speciální péče': ([
        'SADA',
        R(r'(GO SPUNKY|Pinky Frou).*pěna do koupele', 'Dětské pěny do koupele', 'Dětské přípravky do koupele'),
        R(r'pěna do koupele', 'Přípravky do koupele', 'Pěny do koupele'),
        R(r'sůl', 'Přípravky do koupele', 'Soli do koupele'),
        R(r'koupel', 'Přípravky do koupele', 'Ostatní přípravky do koupele'),
        R(r'esence', 'Přípravky do koupele', 'Oleje do koupele'),
        R(r'bodyfresh', 'Přípravky pro péči o nohy', 'Krémy na nohy'),
        R(r'sprej|spray', 'Speciální péče o pokožku', 'Tělové spreje'),
        R(r'hřejivé mléko', 'Masážní přípravky', 'Masážní emulze'),
        R(r'krém', 'Tělové krémy', 'Tělové krémy'),
    ], (h('Speciální péče o pokožku'), z('Tělové balzámy'))),

    'Kosmetika > CBD kosmetika': ([
        'SADA',
        R(r'kapky', 'Speciální péče o pokožku', 'Tělové oleje'),
        R(r'roll-on', 'Masážní přípravky', 'Masážní roll-ony'),
        R(r'mast', 'Masážní přípravky', 'Masážní masti'),
    ], (h('Masážní přípravky'), z('Masážní gely'))),

    'Kosmetika > Dekorativní kosmetika > Dekorativní kosmetika - Oči': ([
        R(r'ořezávátko', 'Ostatní kosmetické pomůcky', 'Ostatní kosmetické pomůcky'),
        R(r'báze', 'Oční stíny', 'Podkladové báze na oční stíny'),
        R(r'stín', 'Oční stíny', 'Oční stíny'),
        R(r'sérum na řasy', 'Séra na řasy a obočí', 'Séra na obočí a řasy'),
        R(r'řasenk', 'Řasenky', 'Řasenky'),
        R(r'gel na obočí', 'Řasenky a gely na obočí', 'Gely a řasenky na obočí'),
        R(r'vosk na obočí', 'Vosky na obočí', 'Gely a řasenky na obočí'),
        R(r'tužka na obočí', 'Tužky na obočí', 'Tužky na obočí'),
        R(r'link', 'Oční linky', 'Linky na oči'),
    ], (h('Oční stíny'), z('Oční stíny'))),

    'Kosmetika > Dekorativní kosmetika > Dekorativní kosmetika - Rty': ([
        R(r'máslo|olej na rty|balzám', 'Balzámy na rty', 'Péče o rty'),
        R(r'rtěnk', 'Rtěnky', 'Rtěnky'),
        R(r'lesk', 'Lesky na rty', 'Lesky na rty'),
        R(r'tužka', 'Tužky na rty', 'Tužky na rty'),
    ], (h('Rtěnky'), z('Rtěnky'))),

    'Kosmetika > Dekorativní kosmetika > Dekorativní kosmetika na obličej': ([
        'SADA',
        R(r'pouch', 'Kosmetické tašky', 'Kosmetické tašky'),
        R(r'podkladová báze', 'Podkladové báze', 'Podkladové báze na tvář'),
        R(r'\bBB\b', 'Tónovací krémy', 'BB a CC krémy'),
        R(r'make-up', 'Make-upy', 'Make-up'),
        R(r'tvářen', 'Tvářenky', 'Tvářenky'),
        R(r'rozjasňov', 'Rozjasňovače', 'Rozjasňovače'),
        R(r'korektor', 'Korektory na tvář', 'Korektory'),
        R(r'pudr', 'Pudry na tvář', 'Pudry'),
        R(r'konturovací', 'Přípravky na konturování tváře', 'Ostatní přípravky na tvář'),
    ], (h('Make-upy'), z('Make-up'))),

    'Kosmetika > Kosmetika pro děti': ([
        R(r'toaletní voda', 'Parfémy', 'Dětské parfémy'),
        R(r'koupelový olej|mycí olej', 'Dětské oleje', 'Dětské přípravky do koupele'),
        R(r'masážní olej', 'Dětské oleje', 'Masážní oleje'),
        R(r'mycí balzám', 'Dětské sprchové gely', 'Dětské sprchové gely'),
        R(r'šampon', 'Dětské šampony', 'Dětské šampony'),
        R(r'balzám', 'Ostatní dětská kosmetika', 'Kondicionéry a balzámy'),
        R(r'ubrousk', 'Vlhčené ubrousky', 'Dětské vlhčené ubrousky'),
        R(r'sůl', 'Ostatní dětská kosmetika', 'Dětské přípravky do koupele'),
        R(r'krém', 'Dětské krémy', 'Krémy a emulze pro děti'),
    ], (h('Ostatní dětská kosmetika'), z('Krémy a emulze pro děti'))),

    'Kosmetika > Kosmetika pro muže': ([
        'SADA',
        R(r'chlapská údržba', 'Sprchové gely', 'Sprchové gely'),
        R(r'deodorant', 'Deodoranty a antiperspiranty', 'Deodoranty a antiperspiranty'),
        R(r'pěna na holení', 'Pěny a gely na holení', 'Pěny na holení'),
        R(r'gel na holení|oholení', 'Pěny a gely na holení', 'Gely na holení'),
        R(r'balzám po holení', 'Balzámy po holení', 'Balzámy po holení'),
        R(r'po holení', 'Krémy a gely po holení', 'Balzámy po holení'),
        R(r'vypadávání', 'Přípravky proti vypadávání vlasů', 'Přípravky proti padání vlasů'),
        R(r'šampon na vousy', 'Šampony na vousy', 'Péče o vousy'),
        R(r'vosk na vousy', 'Vosky na vousy', 'Péče o vousy'),
        R(r'šampon', 'Šampony', 'Šampony'),
    ], (h('Sprchové gely'), z('Sprchové gely'))),

    'Kosmetika > Krémy na nohy': ([], (h('Přípravky pro péči o nohy'), z('Krémy na nohy'))),

    'Kosmetika > Opalování': ([
        R(r'gel po opalování', 'Přípravky po opalování', 'Gely po opalování'),
        R(r'po opalování|after sun', 'Přípravky po opalování', 'Ostatní přípravky po opalování'),
        R(r'sprej', 'Opalovací přípravky', 'Spreje na opalování'),
        R(r'mléko', 'Opalovací přípravky', 'Mléka na opalování'),
        R(r'krém|cream', 'Opalovací přípravky', 'Krémy na opalování'),
    ], (h('Opalovací přípravky'), z('Ostatní přípravky na opalování'))),

    'Kosmetika > Ruce': ([
        'SADA',
        R(r'kuperóz', 'Pleťová séra, emulze a koncentráty', 'Pleťová séra'),
        R(r'hedvábný balzám', 'Tělové balzámy', 'Tělové balzámy'),
        R(r'čisticí gel', 'Tekutá mýdla', 'Mycí pasty'),
    ], (h('Přípravky pro péči o ruce a nehty'), z('Péče o ruce'))),

    'Kosmetika > Sprchové gely a pěny': ([
        'SADA',
        R(r'GO SPUNKY|Pinky Frou', 'Dětské sprchové gely', 'Dětské sprchové gely'),
        R(r'mycí krém', 'Přípravky na čištění pleti', 'Čisticí gely'),
        R(r'intim', 'Intimní mycí prostředky', 'Intimní hygienické prostředky'),
        R(r'koupel', 'Přípravky do koupele', 'Ostatní přípravky do koupele'),
    ], (h('Sprchové gely'), z('Sprchové gely'))),

    'Kosmetika > Tekutá mýdla': ([
        R(r'tuhé', 'Tuhá mýdla', 'Tuhá mýdla'),
        R(r'GO SPUNKY|Pinky Frou|Mimi', 'Tekutá mýdla', 'Dětská mýdla'),
    ], (h('Tekutá mýdla'), z('Tekutá mýdla'))),

    'Kosmetika > Vlasová kosmetika': ([
        'SADA',
        R(r'tonikum|lotion|elixír|vypadávání', 'Přípravky proti vypadávání vlasů', 'Přípravky proti padání vlasů'),
        R(r'kondicionér|balzám', 'Kondicionéry a balzámy na vlasy', 'Kondicionéry a balzámy'),
        R(r'mask', 'Masky na vlasy', 'Vlasová regenerace'),
        R(r'šampon.*lup', 'Přípravky proti lupům', 'Šampony'),
        R(r'šampon', 'Šampony', 'Šampony'),
    ], (h('Vlasová regenerace'), z('Vlasová regenerace'))),

    'Kosmetika > Ústa a zuby': ([
        R(r'mezizubní', 'Mezizubní kartáčky', 'Mezizubní kartáčky'),
        'SADA',
        R(r'balzám na rty', 'Balzámy na rty', 'Péče o rty'),
        R(r'ústní voda', 'Ústní vody', 'Ústní vody'),
        R(r'sprej', 'Ústní spreje', 'Ústní spreje'),
        R(r'mezizubní', 'Mezizubní kartáčky', 'Mezizubní kartáčky'),
        R(r'kartáček', 'Manuální zubní kartáčky', 'Zubní kartáčky'),
    ], (h('Zubní pasty'), z('Zubní pasty'))),

    'Kosmetika > Esenciální oleje': ([
        R(r'aroma lampa|aromalampa', 'Aroma lampy', 'Aroma lampy'),
        R(r'Iconic Stars', 'Vonné oleje', 'Vonné oleje'),
        R(r'esence', 'Přípravky do koupele', 'Oleje do koupele'),
        R(r'Eucassens', 'Aromaterapie', 'Osvěžovače vzduchu'),
    ], (h('Aromaterapie'), z('Vonné oleje'))),

    # ------------------------------------------------ DOPLŇKY STRAVY A POTRAVINY
    'Doplňky stravy > Aloe Vera gel': ([
        R(r'detox', 'Vitamíny a doplňky stravy', 'Přípravky na detoxikaci organismu'),
    ], (DOPLNEK_H, z('Přírodní produkty'))),

    'Doplňky stravy > Imunitní systém': ([
        R(r'probio|synbio|essynbio', 'Vitamíny a doplňky stravy', 'Probiotika a prebiotika'),
    ], (DOPLNEK_H, z('Přírodní produkty'))),

    'Doplňky stravy > Vitamíny a minerály': ([
        R(r'jogurtovač', 'Jogurtovače', 'Jogurtovače'),
        R(r'protein power', 'Proteiny', 'Proteiny', 'Sportovní výživa', 'Sportovní výživa'),
        R(r'tyčinka', 'Müsli tyčinky', 'Proteinové a energetické tyčinky'),
        R(r'figu ?active|slim', 'Vitamíny a doplňky stravy', 'Přípravky na hubnutí'),
        R(r'detox|clea.?ns', 'Vitamíny a doplňky stravy', 'Přípravky na detoxikaci organismu'),
        R(r'probio|synbio', 'Vitamíny a doplňky stravy', 'Probiotika a prebiotika'),
        R(r'es.?leep|relax|mind master', 'Vitamíny a doplňky stravy', 'Přípravky na podporu paměti a spánku'),
    ], (DOPLNEK_H, z('Vitamíny a minerály'))),

    'Doplňky stravy > Med': ([
        R(r'tyčinka', 'Müsli tyčinky', 'Proteinové a energetické tyčinky'),
        R(r'granola', 'Cereálie a müsli', 'Cereálie a müsli'),
        R(r'nektar', 'Šťávy', 'Sirupy'),
        R(r'nápoj', 'Limonády', 'Limonády'),
    ], (h('Medy'), z('Med a pyl'))),

    'Doplňky stravy > Káva': ([
        R(r'ledová', 'Ledová káva', 'Ledové kávy'),
    ], (h('Zrnková káva'), z('Káva'))),

    'Doplňky stravy > Sypané čaje': ([
        R(r'sítko', 'Sítka na čaj', 'Sítka na čaj'),
        R(r'ledov', 'Ledové čaje', 'Ledové čaje'),
    ], (h('Čaje'), z('Čaje'))),

    'Doplňky stravy > Koření': ([
        R(r'bujón', 'Bujóny', 'Koření'),
    ], (h('Kořenící směsi'), z('Koření'))),

    'Doplňky stravy > Oleje': ([], (h('Kuchyňské oleje'), z('Rostlinné oleje'))),
    'Doplňky stravy > Swissycandy': ([], (h('Bonbóny'), z('Bonbony'))),

    # ------------------------------------------------ DOMÁCNOST
    'Domácnost': ([], (h('Speciální čisticí prostředky'), z('Ostatní úklidové pomůcky a příslušenství'))),

    'Domácnost > Dezinfekce': ([
        R(r'gel', 'Dezinfekce', 'Antibakteriální gely a pěny', 'Zdravotnické potřeby'),
    ], (h('Úklidové dezinfekce'), z('Dezinfekce'))),

    'Domácnost > Koberce a vysavače': ([
        R(r'vysavač', 'Vůně do vysavačů', 'Vůně do vysavačů'),
    ], (h('Čisticí prostředky na koberce a čalounění'), z('Čisticí prostředky na koberce a čalounění'))),

    'Domácnost > Koupelny': ([], (h('Čisticí prostředky do koupelny a kuchyně'), z('Čisticí prostředky do koupelny'))),

    'Domácnost > Kuchyně': ([
        R(r'vodního kamene', 'Odstraňovače vodního kamene', 'Čisticí prostředky do kuchyně'),
        R(r'mikrovln|sporák|sklokeramick|odmrazovač|lednic|digesto', 'Čisticí prostředky na spotřebiče', 'Čisticí prostředky do kuchyně'),
        R(r'pohlcovač', 'Osvěžovače vzduchu', 'Pohlcovače pachů'),
        R(r'prkénka', 'Speciální čisticí prostředky', 'Čisticí prostředky do kuchyně'),
    ], (h('Čisticí prostředky do koupelny a kuchyně'), z('Čisticí prostředky do kuchyně'))),

    'Domácnost > Mytí nádobí > Mytí v myčce': ([
        R(r'čisticí prostředek do myč', 'Čističe myčky', 'Čističe myček'),
        R(r'oplachovací|lešticí', 'Leštidla do myčky', 'Leštidla do myčky'),
        R(r'gel', 'Gely do myčky', 'Gely do myčky'),
        R(r'prášek', 'Prášky do myčky', 'Prášky do myčky'),
        R(r'sůl', 'Soli do myčky', 'Soli do myčky'),
        R(r'tablet', 'Tablety a kapsle do myčky', 'Tablety do myčky'),
        R(r'vůně', 'Osvěžovače do myčky', 'Vůně do myčky'),
    ], (h('Gely do myčky'), z('Gely do myčky'))),

    'Domácnost > Mytí nádobí > Ruční mytí': ([], (h('Prostředky na ruční mytí nádobí'), z('Mycí prostředky'))),
    'Domácnost > Odpuzovače hmyzu': ([], (h('Repelenty'), z('Repelenty'))),

    'Domácnost > Okna a zrcadla': ([
        R(r'brýl', 'Čistící prostředky na okna a skla', 'Čisticí roztoky na brýle'),
    ], (h('Čistící prostředky na okna a skla'), z('Čisticí prostředky na okna'))),

    'Domácnost > Osvěžovače vzduchu a textilií': ([
        R(r'aroma parfém|iconic stars', 'Vonné oleje', 'Vonné oleje'),
        R(r'svíčk', 'Svíčky', 'Svíčky', 'Vůně do bytu', 'Bytové dekorace'),
        R(r'aromalamp|aroma lamp', 'Aroma lampy', 'Aroma lampy'),
        R(r'ultrasonick', 'Aroma difuzéry', 'Elektrické aroma difuzéry'),
        R(r'náplň', 'Příslušenství pro aroma difuzéry', 'Náplně do osvěžovačů vzduchu'),
        R(r'difuzér|home perfume', 'Aroma difuzéry', 'Tyčinkové aroma difuzéry'),
        R(r'sašetk|sáček', 'Vonné sáčky', 'Osvěžovače vzduchu'),
        R(r'do bot', 'Osvěžovače vzduchu', 'Spreje do bot'),
        R(r'pohlcovač|asanace', 'Osvěžovače vzduchu', 'Pohlcovače pachů'),
    ], (h('Osvěžovače vzduchu'), z('Osvěžovače vzduchu'))),

    'Domácnost > Podlahy': ([], (h('Čistící prostředky na podlahy'), z('Čističe podlah'))),
    'Domácnost > Praní prádla > Aviváže s kondicionérem': ([], (h('Aviváže'), z('Aviváže'))),
    'Domácnost > Praní prádla > Barevné prádlo': (PRANI, PRANI_DEF),
    'Domácnost > Praní prádla > Bílé prádlo': (PRANI, PRANI_DEF),
    'Domácnost > Praní prádla > Jemné prádlo': (PRANI, PRANI_DEF),
    'Domácnost > Praní prádla > Na skvrny': (PRANI, PRANI_DEF),
    'Domácnost > Praní prádla > Parfémy na praní': ([], (h('Aviváže'), z('Parfémy na praní'))),
    'Domácnost > Praní prádla > Prací prostředky na záclony': (PRANI, PRANI_DEF),
    'Domácnost > Praní prádla > Prací prostředky pro nejmenší': (PRANI, PRANI_DEF),
    'Domácnost > Praní prádla > Speciální prací prostředky': (PRANI, PRANI_DEF),
    'Domácnost > Praní prádla > Univerzální prací prostředky': (PRANI, PRANI_DEF),
    'Domácnost > Praní prádla > Černé prádlo': (PRANI, PRANI_DEF),

    'Domácnost > Pro zvířata': ([
        R(r'šampon', 'Šampony pro psy', 'Kosmetika pro psy'),
        R(r'tlapk', 'Kosmetika a úprava psa', 'Kosmetika pro psy'),
        R(r'pohlcovač', 'Osvěžovače vzduchu', 'Pohlcovače pachů'),
    ], (h('Speciální čisticí prostředky'), z('Ostatní čisticí prostředky'))),

    'Domácnost > Péče o rostliny': ([], (h('Hnojiva'), z('Hnojiva'))),

    'Domácnost > Péče o vozidlo': ([
        R(r'autošampon', 'Přípravky na mytí aut', 'Autošampóny'),
        R(r'interiér|sedačk', 'Péče o interiér auta', 'Ostatní autokosmetika'),
        R(r'hmyz', 'Čištění a dekontaminace laku', 'Ostatní autokosmetika'),
        R(r'leštěnka', 'Leštění laku', 'Autovosky'),
        R(r'ostřikovač', 'Vody do ostřikovačů', 'Směsi do ostřikovačů'),
    ], (h('Univerzální čističe aut'), z('Ostatní autokosmetika'))),

    'Domácnost > Speciální čisticí prostředky': ([
        R(r'písek na nádobí|dětského nádobí', 'Prostředky na ruční mytí nádobí', 'Mycí prostředky'),
        R(r'odměr|lahvička|láhev|rozprašovač|pumpa|etikety', 'Speciální čisticí prostředky', 'Ostatní úklidové pomůcky a příslušenství'),
        R(r'trouby a grily', 'Čisticí prostředky na spotřebiče', 'Čištění grilů'),
        R(r'pohlcovač|filtry do obuvi', 'Osvěžovače vzduchu', 'Pohlcovače pachů'),
        R(r'obuvi', 'Speciální čisticí prostředky', 'Spreje do bot'),
        R(r'krbov', 'Čistící přípravky na kamna a krby', 'Ostatní čisticí prostředky'),
        R(r'vodní kámen', 'Odstraňovače vodního kamene', 'Ostatní čisticí prostředky'),
        R(r'leštěnka na nábytek|na dřevo', 'Leštidla na nábytek a přípravky proti prachu', 'Ostatní čisticí prostředky'),
        R(r'molům', 'Repelenty', 'Hubicí a odpuzovací přípravky na hmyz'),
        R(r'ubrousky', 'Čisticí ubrousky', 'Ostatní čisticí prostředky'),
        R(r'skvrn', 'Odstraňovače skvrn', 'Odstraňovače skvrn'),
        R(r'elektronik', 'Čisticí prostředky na spotřebiče', 'Ostatní čisticí prostředky'),
    ], (h('Speciální čisticí prostředky'), z('Ostatní čisticí prostředky'))),

    'Domácnost > Univerzální čisticí prostředky': ([], (h('Univerzální čisticí prostředky', 'Drogerie'), z('Univerzální čisticí prostředky'))),

    'Domácnost > WC, toalety, odpady': ([
        R(r'septik', 'Přípravky pro žumpy, septiky a čističky', 'Čističe septiků a jímek'),
        R(r'odpad', 'Čističe odpadu', 'Čističe odpadu'),
    ], (h('Dezinfekční prostředky na WC'), z('WC čističe'))),

    # ------------------------------------------------ NEMAPOVAT (záměrně prázdné)
    'Doplňkové služby': None,
    'Doplňkové služby > Dárkové poukazy': None,
    'Výchozí kategorie': None,
}

# Parfémy
PARFEM_H = h('Parfémy', 'Kosmetika a parfémy')
PARFEM_Z = {'F': z('Dámské parfémy', 'Kosmetika a drogerie'), 'M': z('Pánské parfémy'),
            'U': z('Unisex parfémy'), 'K': z('Dětské parfémy')}
TELOVY_SPREJ = (h('Tělové spreje'), z('Tělové spreje'))


# ---------------------------------------------------------------- pomocné
def znacka(manufacturer, name):
    """Značka z pole výrobce, při prázdném výrobci z názvu."""
    for b in ('LR', 'Essens', 'Eurona'):
        if manufacturer.strip().lower() == b.lower():
            return b
    m = re.match(r'(LR|Essens|Eurona)\b', name, re.I)
    return {'lr': 'LR', 'essens': 'Essens', 'eurona': 'Eurona'}[m.group(1).lower()] if m else None


def pohlavi(name, cat):
    if re.search(r'pro dívky|pro chlapce', name, re.I):
        return 'K'
    if re.search(r'dámsk|pro ženy|for her|for women', name, re.I):
        return 'F'
    if re.search(r'pánsk|pro muže|for him|for men', name, re.I):
        return 'M'
    if re.search(r'unisex', name, re.I):
        return 'U'
    return {'Dámské parfémy': 'F', 'Pánské parfémy': 'M', 'Unisex parfémy': 'U'}.get(cat.split(' > ')[-1])


def je_parfem(cat, name):
    """Osobní parfém (ne tělová mlha / body mist / bytové a prací vůně)."""
    if re.search(r'body mist|tělová mlha', name, re.I):
        return False
    return cat.startswith('Kosmetika > Parfémy') or bool(re.search(r'toaletní voda|parfémovaná voda|\bed[pt]\b', name, re.I))


def je_parfemova_sada(name):
    return bool(re.search(r'parfémovaný set|parfémová sada', name, re.I))


# ---------------------------------------------------------------- kategorie
def kategorie(cat, name):
    if cat not in KAT:
        return '', '', 'NEZNÁMÁ KATEGORIE'
    spec = KAT[cat]
    if spec is None:
        return '', '', 'záměrně nemapováno'
    if cat.startswith('Kosmetika > Parfémy'):
        if je_parfemova_sada(name):
            return SADA[0], SADA[1], 'sada parfémů'
        if re.search(r'body mist|tělová mlha', name, re.I):
            return TELOVY_SPREJ[0], TELOVY_SPREJ[1], 'tělový sprej'
        g = pohlavi(name, cat)
        return PARFEM_H, PARFEM_Z[g], 'parfém'
    rules, default = spec
    for rule in rules:
        if rule == 'SADA':
            if je_smisena_sada(name):
                return SADA[0], SADA[1], 'sada'
            continue
        rx, hv, zv = rule
        if rx.search(name):
            return hv, zv, rx.pattern
    return default[0], default[1], 'výchozí'


# ---------------------------------------------------------------- xmlFeedName (Heureka: výrobce + model + typ + pohlaví + objem)
LR_OBJEM = {'Elixir': '100 ml'}   # LR EdP 50 ml, řada Elixir 100 ml (dle popisu „Obsah: 50 ml | 2 ml“ / „100 ml | 2 ml“)
ROD_M = {'F': 'dámský', 'M': 'pánský', 'U': 'unisex', 'K': None}
ROD_Z = {'F': 'dámská', 'M': 'pánská', 'U': 'unisex', 'K': None}

ODSTRANIT = [
    r'\d+(?:[.,]\d+)?\s*ml',
    r'\bEd[PT]\b', r'Eau de (Parfum|Toilette)', r'parfémovaná voda', r'toaletní voda',
    r'Aroma roll-on', r'olejový parfém',
    r'(Dámský|Pánský)?\s*parfémovaný set', r'Luxusní (dámský|pánský|unisex) parfém',
    r'(Dámský|Pánský) parfém', r'Parfém pro (muže|ženy)', r'Parfém Niche', r'\bParfém\b',
    r'pro (ženy|muže|dívky|chlapce)', r'\bunisex\b', r'by ESSENS', r'^\s*CC\s+',
]


def velka_pismena(tok):
    """Slova psaná VERZÁLKAMI -> Velké první písmeno (Heureka nechce názvy kapitálkami)."""
    if re.fullmatch(r'[WwMm]\d{3}', tok):
        return tok.lower()                       # kódy vůní Essens: w904, m041
    pism = re.sub(r'[^A-Za-zÀ-ž]', '', tok)
    if len(pism) >= 2 and pism.isupper() and tok not in ('LR',):
        return tok[0] + tok[1:].lower()
    return tok


def xml_nazev(brand, name, cat):
    n = re.sub(r'^(LR|Essens|Eurona)\s+', '', name, flags=re.I)
    if je_parfemova_sada(n):
        typ, rod = 'parfémová sada', ROD_Z
    elif re.search(r'\bEdP\b|Eau de Parfum|parfémovaná voda', n, re.I):
        typ, rod = 'parfémovaná voda', ROD_Z
    elif re.search(r'\bEdT\b|Eau de Toilette|toaletní voda', n, re.I):
        typ, rod = 'toaletní voda', ROD_Z
    elif re.search(r'olejový parfém', n, re.I):
        typ, rod = 'olejový parfém', ROD_M
    elif re.search(r'luxusní|niche', n, re.I):
        typ, rod = 'luxusní parfém', ROD_M
    else:
        typ, rod = 'parfém', ROD_M
    g = pohlavi(n, cat)
    if g == 'K':
        poh = re.search(r'pro (dívky|chlapce)', n, re.I).group(0).lower()
    else:
        poh = rod[g]

    objem = ''
    if typ != 'parfémová sada':
        m = re.search(r'(\d+(?:[.,]\d+)?)\s*ml', n)
        if m:
            objem = m.group(1) + ' ml'
        elif brand == 'LR':
            objem = next((v for k, v in LR_OBJEM.items() if k in n), '50 ml')

    model = n
    for rx in ODSTRANIT:
        model = re.sub(rx, ' ', model, flags=re.I)
    model = re.sub(r'\s[-–]\s|\s[-–]$|^[-–]\s', ' ', ' ' + model + ' ')
    model = ' '.join(velka_pismena(t) for t in model.split())
    return ' '.join(x for x in (brand, model, typ, poh, objem) if x)


# ---------------------------------------------------------------- běh
def main():
    rows = [l.rstrip('\n').split('\t') for l in open(os.path.join(BASE, 'eshop_kategorie.tsv'), encoding='utf-8') if l.strip()]
    out = {}
    for code, pair, manu, cat, name in rows:
        hv, zv, _ = kategorie(cat, name)
        xml = ''
        b = znacka(manu, name)
        if b and je_parfem(cat, name):
            xml = xml_nazev(b, name, cat)
        out[code] = {'heureka': hv, 'zbozi': zv, 'xmlFeedName': xml}

    # kontrola konzistence v rámci produktu (pairCode = varianty jednoho produktu)
    skup = defaultdict(set)
    for code, pair, *_ in rows:
        if pair:
            skup[pair].add(json.dumps(out[code], ensure_ascii=False, sort_keys=True))
    bad = {p: s for p, s in skup.items() if len(s) > 1}
    if bad:
        sys.exit(f'Nekonzistentní hodnoty v rámci pairCode: {bad}')

    json.dump(out, open(os.path.join(BASE, 'vystup.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(f'Zapsáno {len(out)} produktů do vystup.json')


if __name__ == '__main__':
    main()
