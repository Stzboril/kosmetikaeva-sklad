# Kontrola skladu a cen – KosmetikaEva.eu

Každé ráno se automaticky porovná sklad a ceny produktů **LR, Eurona a Essens** na e-shopu s dodavateli. Nic se v Shoptetu nemění samo – připraví se soubory k importu a přehled změn.

## Jak to běží

| Čas (cca) | Co se děje |
|---|---|
| 5:22 | Naplánovaná úloha Claude „LR sklad KosmetikaEva“ projde 15 stránek lr-czech.com a uloží `data/lr.json` (web LR blokuje servery GitHubu, proto přes Claude). |
| po ní a v 6:15 | GitHub Actions („Kontrola skladu a cen“) stáhne Euronu (veřejné API e-shopu) a Essens (výpisy kategorií), porovná je s e-shopem (veřejný Google feed a Heureka dostupnost) a připraví soubory. |

Když je co importovat, vznikne **upozornění (Issue)** s přehledem a GitHub pošle e-mail. Starší upozornění se samo zavře.

## Pravidla

- Dodavatel má skladem a e-shop ne → **sklad 20**. Dodavatel nemá (nebo produkt nenašel) a e-shop ano → **sklad 0**.
- Nová cena = **doporučená cena − 8 %, zaokrouhleno nahoru na Kč končící 9**, nikdy nad doporučenou. Výjimka: **parfémy Essens 50 ml starší řady (doporučená cena 600 Kč) mají pevnou cenu 499 Kč**; novější řada (doporučená 635 Kč) jde podle pravidla na 589 Kč. Luxusní parfémy a sady se řídí pravidlem.
- Ceny se jen **navrhují ke schválení**. Produkty v akci, Just a Nahrin se nemění. U LR se nepoužijí ceny se štítkem „Akce“ / „Měsíční akce“.
- **Akce LR → akce i na e-shopu:** když má LR produkt v akci („Akce 17.–23. 10.“, „Měsíční akce“), připraví se `ke_importu/akce.csv` s akční cenou = akční cena LR − 8 %, zaokrouhleno nahoru na Kč končící 9, s platností podle štítku LR („Měsíční akce“ = do konce měsíce) a se štítkem Akce. Navrhuje se jen tehdy, když je akční cena nižší než běžná cena na e-shopu a e-shop ji ještě nemá. Po skončení platnosti se akce v Shoptetu sama vypne. Import stejně jako u cen – po schválení.

## Co udělat, když přijde e-mail

1. Otevřete upozornění – je v něm seznam změn skladu a tabulka navržených cen.
2. **Sklad:** soubor `ke_importu/sklad.csv` naimportujte v Shoptetu (Produkty → Import).
3. **Ceny:** pokud s návrhem souhlasíte, naimportujte `ke_importu/ceny.csv`. Když s některou cenou nesouhlasíte, napište Claudovi, které vynechat (nebo zapište kód do `data/nemenit_cenu.csv`).
4. Při importu vždy nechte **„Neměnit produkty a varianty, které nejsou obsaženy v importu“** a **nezaškrtávejte** „Změňte adresu URL produktu podle názvu“.

Soubor stáhnete tak, že v upozornění kliknete pravým tlačítkem na odkaz a zvolíte „Uložit odkaz jako…“. Import může udělat i Claude – stačí napsat „naimportuj sklad“.

## Soubory

- `zprava.md` – poslední zpráva (stejná jako v upozornění)
- `ke_importu/sklad.csv`, `ke_importu/ceny.csv`, `ke_importu/akce.csv` – soubory pro import do Shoptetu
- `data/lr.json`, `data/lr_protokol.txt` – data LR a protokol posledního stažení
- `data/aliasy.csv` – ruční párování kódů e-shop → dodavatel (např. když dodavatel změní kód)
- `data/eshop_produkty.json` – seznam všech sledovaných produktů e-shopu; vyprodané produkty, které Google feed vynechává, se podle něj kontrolují přímo na jejich stránce, aby se mohly znovu naskladnit
- `data/nesledovat.csv` – produkty, které se nekontrolují (vzorky, partnerské zboží)
- `data/essens_url.csv` – odkazy na detail Essens u produktů, které nejsou v žádné kategorii na essens.cz
- `data/nemenit_cenu.csv` – produkty, u kterých se cena nenavrhuje
- `data/eshop_kody.csv` – párové kódy variant pro import
- `data/google_doplnek.tsv` – doplňkový zdroj pro Google Merchant Center (stahuje se denně): produkty vyřazené z reklam (nízká marže, podle filtru „Marže do 15 %“ v Shoptetu). Ve výsledcích zdarma na Googlu zůstávají. Kód smažete z řádku = produkt se do reklam vrátí.
- `skript/` – program kontroly

V repozitáři nejsou žádná hesla ani nákupní ceny – je veřejný, protože Shoptet i GitHub potřebují soubory číst bez přihlášení.
