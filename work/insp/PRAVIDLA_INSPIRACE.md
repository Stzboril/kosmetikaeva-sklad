# Úprava popisů parfémů Essens – odstranění zmínek o cizích značkách

E-shop KosmetikaEva.eu prodává parfémy Essens. V popisech nesmí být uvedeno, jakým parfémem jiné značky je vůně „inspirována“. Text je česky.

## Co udělat u každého produktu
1. Odstraň VŠECHNY zmínky o cizích značkách, parfémových domech a názvech originálních parfémů (např. Dior, Chanel, Dolce & Gabbana Light Blue, DKNY Be Delicious, Lanvin Éclat d'Arpege, Good Girl, Baccarat Rouge…) a všechny tvary slov „inspirováno / inspirovaný / inspirovaná / inspirace / inspiruje“ ve vztahu k jinému parfému.
2. Nadpis typu `<h2>Dámský parfém W104 – inspirováno Dolce &amp; Gabbana Light Blue</h2>` nahraď krátkým výstižným heslem o charakteru vůně ve tvaru `<h2><em>…</em></h2>` (např. `<h2><em>Svěží citrusová vůně plná energie</em></h2>`). Heslo odvoď z tónů a popisu vůně v textu.
3. Věty, které jen odkazují na inspiraci / originál, vypusť. Věty, kde je zmínka jen část, přepiš bez ní, aby zněly přirozeně.
4. Všechno ostatní nech BEZE ZMĚNY: HTML strukturu a značky, odstavce, odrážky, tóny vůně, Složení / INCI (doslova), upozornění, objem, výrobce, odkazy a obrázky.
5. Nepřidávej žádný nový obsah ani box „zaměňují za“ (ten se doplní později automaticky). Nepiš název originální vůně nikam.
6. `metaDescription`: pokud obsahuje značku nebo „inspirovaný“, napiš nový (cca 140–155 znaků, česky, bez cizích značek, popis vůně + „Essens“ + objem). Jinak ponech beze změny.
7. `seoTitle`: pokud obsahuje cizí značku nebo „inspirováno“, nastav na „{name} | KosmetikaEva.eu“. Jinak beze změny.
8. `name`: pokud obsahuje cizí značku, odstraň ji (jinak beze změny).
9. Slova „smyslný, smyslnost“ apod. nejsou značka (YSL) – neměň je.

## Výstup
Do zadaného výstupního souboru zapiš JSON objekt: klíč = `code`, hodnota = objekt
`{"name": ..., "description": ..., "metaDescription": ..., "seoTitle": ..., "zmeneno": "krátce co se změnilo"}`
pro KAŽDÝ produkt ze vstupu (i když by se nic neměnilo – pak vrať původní texty a "zmeneno": "nic").
Ověř, že soubor jde načíst `python3 -c "import json;json.load(open('…'))"` a že obsahuje všechny kódy.
Po zápisu spusť `python3 /home/claude/work/insp/kontrola.py <vstup> <výstup>` a oprav vše, co nahlásí, dokud nevypíše OK.
