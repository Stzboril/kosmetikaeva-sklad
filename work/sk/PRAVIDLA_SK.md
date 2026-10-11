# Překlad produktů KosmetikaEva.eu do slovenštiny

Překládáš texty produktů českého e-shopu (LR, Eurona, Essens) do přirozené, spisovné slovenštiny, jakou píší slovenské e-shopy s kosmetikou. Žádný strojový doslovný překlad – věty musí znít slovensky.

## Co přeložit
Pro každou položku vstupu: `name`, `description` (pokud je ve vstupu), `metaDescription`, `seoTitle`.

## Pravidla
1. HTML zachovej PŘESNĚ: stejné značky ve stejném pořadí, stejné atributy (class, src, href, data-…, style). Překládáš jen viditelný text mezi značkami a atributy `alt` a `title`.
2. Složení / INCI (latinské a anglické názvy surovin, např. „Aqua, Glycerin, Parfum…“) ponech DOSLOVA beze změny. Nadpis sekce přelož („Složení“ → „Zloženie“). Pokud je složení napsané česky (doplňky stravy, potraviny), přelož ho věrně, čísla, procenta a jednotky beze změny.
3. Nutriční hodnoty: čísla a jednotky beze změny, popisky přelož (Energetická hodnota → Energetická hodnota, Tuky → Tuky, z toho nasycené mastné kyseliny → z toho nasýtené mastné kyseliny, Sacharidy → Sacharidy, z toho cukry → z toho cukry, Bílkoviny → Bielkoviny, Sůl → Soľ, Vláknina → Vláknina, DDD/RHP → RHP).
4. Bezpečnostní upozornění a H/P věty přelož věrně standardním slovenským zněním (např. „Uchovávejte mimo dosah dětí.“ → „Uchovávajte mimo dosahu detí.“). Nic nevynechávej ani nepřidávej.
5. Značky, řady a názvy produktů (Essens, LR, Eurona, Aloe Vera, Zeitgard, Lifetakt, Microsilver, Cerny Cosmetix, Vitassens, kódy jako w107, m022…) nepřekládej.
6. Názvy firem a adresy výrobce ponech, jen „Výrobce:“ → „Výrobca:“, „Distributor“ → „Distribútor“.
7. `name`: přelož (např. „Essens Dámský parfém w107 50 ml“ → „Essens Dámsky parfum w107 50 ml“, „Pánský“ → „Pánsky“, „Sprchový gel“ → „Sprchový gél“), objem a kódy beze změny.
8. `seoTitle`: vždy „{slovenský name} | KosmetikaEva.eu“.
9. `metaDescription`: přelož, délka cca 140–160 znaků.
10. Ve výsledku nesmí být česká písmena ř, ů, ě. Používej slovenské ä, ô, ľ, ĺ, ŕ, ď, ť, ň podle pravopisu.
11. Nevkládej nic nového (žádné boxy, poznámky, odkazy). Text nezkracuj.

## Výstup
Do zadaného výstupního souboru zapiš JSON objekt: klíč = `key` položky, hodnota = `{"name": ..., "description": ..., "metaDescription": ..., "seoTitle": ...}` (u položek bez `description` ve vstupu pole `description` vynech).
Pak spusť `python3 /home/claude/work/sk/kontrola_sk.py <vstup> <výstup>` a oprav vše, co nahlásí, dokud nevypíše OK.
Výstup zapisuj průběžně (např. po několika položkách), aby se práce neztratila.
