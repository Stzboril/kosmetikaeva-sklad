# Sloučení stejných výrobků v různých objemech do variant (19. 10. 2026)

Majitel: „proč neuděláš tyto a další parfémy jako sdruženou položku, např. jako je Eucasol, aby si zákazník
mohl vybrat z roletkového seznamu?“ → „ano sluč vše“. Pak: „upravit i pořadí v roletce u všech výrobků,
sjednotit do jednoho seznamu a nepotřebné smazat“.

## Co se udělalo
- 26 výrobků má teď varianty (roletka „Objem“ nebo „Hmotnost“), 27 dřívějších samostatných výrobků je
  **skrytých** (nesmazaných), jejich kód má příponu `-SLOUCENO` a jejich adresa CZ i SK je přesměrovaná
  na hlavní výrobek (seznam v `sloucene.tsv`, 54 přesměrování).
- Hlavní výrobek si nechal svou adresu, hodnocení, ikony (ke-ikony mapa P podle ID hlavního výrobku).
- Varianta dostala kód, cenu, běžnou cenu, nákupní cenu, sklad, EAN, jednotky, hmotnost, dostupnost
  a obrázek ze sloučeného výrobku. Ceny se neměnily (SK cena se dál přepočítává z CZK).
- Název bez objemu, SEO titulek „<název> 200 ml a 500 ml | KosmetikaEva.eu“, v popisu řádek
  Objem/Hmotnost „200 ml nebo 500 ml“ (SK „alebo“), meta popis upraven.
- Zálohy formulářů před změnou: localStorage prohlížeče v aplikaci, klíče `keSlouceniZaloha_<id>`
  (Garden of Dreams `keMergeBackup_garden_20261019`).

## Skupiny (hlavní ← skryté)
| Výrobek | Hlavní | Skryté | Šablona |
|---|---|---|---|
| Parfémy na praní (10 vůní) 200/500 ml | 10900, 10852, 10858, 10864, 10876, 10888, 10894, 10906, 10912, 10918 | 10903, 10855, 10861, 10867, 10879, 10891, 10897, 10909, 10915, 10921 | 172 |
| Prací prostředky 935 g / 2 750 g | 4466, 4481, 8013, 5324 | 4460, 4478, 8019, 5321 | 193 (Hmotnost) |
| Mytí nádobí 400/1000 ml (Lesní plody, Auri Skye) | 4577, 7888 | 4574, 7891 | 175 |
| Pohotovostní žehlička 100/500 ml (Green, Black Grape) | 5360, 5372 | 5375, 5378 | 178 |
| Essens colostrum krémy 150 ml / 500 ml (náplň) | 6524, 10723 | 10702, 10708 | 181 |
| Essens Aloe vera šampony a kondicionéry 200 ml / 500 ml (náplň) | 10648, 10654, 10666, 10669 | 10651, 10657, 10678, 10675 | 184 |
| Just Bodyfresh 30/60/100 ml | 8919 | 7990, 7621 | 187 |
| Just Univerzální čistič NR 500/1000 ml | 8911 | 7813 | 190 |

Kontrola 19. 10.: všech 26 stránek CZ i SK vrací 200, roletka má správné objemy a ceny, staré adresy přesměrují.

## Roletka – jeden seznam „Objem“
- Všechny výrobky s objemy používají parametr **Objem (id 145)**. Hodnoty seřazeny vzestupně
  (1 ml, 1,5 ml, 2 ml, 3 ml … 500 ml, 500 ml (náplň), 700 ml, 750 ml, 1000 ml, 2000 ml) → stejné pořadí
  v roletce u všech výrobků. Původní pořadí v localStorage `ke145poradiZaloha_20261019`.
- Šablony variant „Reapir Gel“, „Appenzellský balzám“, „olej z 31“, „Biopeptide Serum Spray“ přepnuty
  ze starých seznamů na Objem (145); záloha `keSablonyZaloha_20261019`.
- Hmotnost (178) zůstává zvlášť (gramy, prací prášky), barva (124) zvlášť (odstíny).
- Nepoužívané (0 výrobků, 0 šablon) – ke smazání majitelem (mazání dělá majitel sám):
  parametry 131 „100 ml“, 134 „200 ml“, 127 „Biopeptide Serum Spray“, 137 „Objem_2“, 139 „Objem_1“;
  nepoužité hodnoty v Objem (145: „1ml“) a barva (124: „04 Velevet Mink“, „Cobalt Blue“).

## Postup (skript `slouceni.js`, spouští se v adminu v prohlížeči)
1. Šablona variant: POST `/admin/generator-variant/` (`action=save`, `templateTitle`,
   `newParameterName[<id parametru>]=Objem`, `newParameterValues[<id>]="200 ml\n500 ml"`).
   Úprava šablony: totéž na `?id=<šablona>`.
2. `keSloucit({main, others, tpl, param, vals})` – viz komentáře ve skriptu.
3. Pořadí hodnot: formulář `/admin/parametry-variant-detail/?id=145&language=cs`, pole `priority[]`.
4. Po sloučení zkontrolovat CZ i SK stránku a přesměrování.

## Just Slézový krém 30 ml + 60 ml (30. 10. 2026, majitel)
- Majitel: „vytvoř Just Slézový krém 60 ml variantu 30 ml, obrázek bude stejný, množství 1 ks, cena bude 1 ml + 1 % z ceny 60 ml krému. CZ i SK verzi“.
- Produkt id 7654 (/telo-2/just-slezovy-krem-60-ml/ – adresa zůstala), dřív bez variant. Šablona 187 (Objem 30/60/100 ml), vybrány hodnoty 30 ml (1030) a 60 ml (1033) parametru Objem (145).
- Varianta 60 ml (56666): kód 5145 (beze změny), 549 Kč, přeškrtnutá 580 (= JUST CZ), sklad 10, obrázek 12319.
- Varianta 30 ml (56663): kód 5145_30, 277 Kč (549 / 60 × 1,01 × 30 = 277,25), bez přeškrtnuté ceny (JUST CZ má jen 60 ml za 580 Kč), sklad 1, dostupnost bez skladu Brzy skladem, obrázek 12319, měrná cena / 100 ml.
- Hlavní výrobek CZ/SK: název „Just Slézový krém“ / „Just Slezový krém“, SEO titulek „… 30 ml a 60 ml | KosmetikaEva.eu“, řádek Objem v popisu „30 ml | 60 ml“ CZ i SK (majitel 30. 10.: jen popis), meta „30 ml nebo 60 ml“ (SK „alebo“), doplňkový parametr Objem „30 ml / 60 ml“, filtr Objem + 30 ml ([1162]=166).
- Zálohy formulářů: localStorage keBackup_7654_cs_20261030, keBackup_7654_sk_20261030.
