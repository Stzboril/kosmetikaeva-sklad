# Pravidla pro produkty LR, Eurona, Essens – KosmetikaEva.eu

Stav k 12. 10. 2026.

## Ceny
- Prodejní cena = doporučená cena výrobce − 8 %, zaokrouhleno NAHORU na Kč končící 9, nikdy nad doporučenou cenu.
- Výjimka: parfémy Essens 50 ml starší řady (doporučená cena 600 Kč, nákup 405/410 Kč) mají pevnou cenu 499 Kč – 62 parfémů (rozhodnutí majitele 11. 10. 2026).
- Novější řada parfémů Essens 50 ml (w183–w211, w904–w913, m041–m053, m809, m902–m905; doporučená 635 Kč, nákup 425 Kč) má 589 Kč = běžné pravidlo – 49 parfémů (rozhodnutí majitele 11. 10. 2026: „u těch novějších řad dej cenu vyšší“ → 589 Kč).
- Výjimka se netýká luxusních / niche parfémů (959 Kč), 4 ELEMENTS / BLANC (939 Kč), Boudoir, Passenger Princess, parfémových sad a dětských toaletních vod – ty jdou podle pravidla.
- Nákupní cena = partnerská cena. LR parfémy se nakupují jako série 3 ks → nákupní cena = cena série / 3 (982,33 Kč).
- Ceny Just a Nahrin se NEMĚNÍ.
- Produkt v akci (akční cena) → měnit jen nákupní cenu.
- Když by nová cena byla ≤ nákupní cena × 1,03 → cenu neměnit, jen nákupní cenu.
- LR: ceny se štítkem „Akce …“ nebo „Měsíční akce“ na lr-czech.com jsou akční, pro výpočet se nepoužijí.
- Essens: prohlížeč v aplikaci je přihlášený do Essens → ukazuje partnerské ceny. Doporučená cena = cena bez přihlášení (detail produktu / výpis kategorie).
- Změny cen jdou vždy ke schválení majiteli.

## Sklad
- U dodavatele skladem → sklad 20; není skladem → 0.
- Mění se jen produkty, kde nesedí „skladem / není skladem“ (e-shop má i jiná čísla než 20).
- Produkty, které dodavatel přestal prodávat → skrýt (po odsouhlasení). PŘED skrytím vždy ověřit u dodavatele: 11. 10. 2026 se 7 „ukončených“ produktů ukázalo jako prodávané pod jiným kódem nebo jen dočasně nedostupné → nic se neskrylo, 6 naskladněno (6512, HOP51, CE0008, CC6734, SAVE06, SAVE24), W190GX zůstává 0 (Essens „Nedostupné“).
- Essens „Nedostupné“ = dočasně nedostupné → produkt nechat viditelný se skladem 0.
- Nekontrolují se: vzorky parfémů LR (97541-x, 97543-x, 9597/1 M), LR 29034-101 (jen pro partnery).

## Automatická kontrola (GitHub: Stzboril/kosmetikaeva-sklad, veřejný repozitář)
- 5:22 naplánovaná úloha Claude „LR sklad KosmetikaEva“ (cloud, PC nemusí běžet): přes WebFetch projde 15 kategorií lr-czech.com, štítky „Není skladem“ ověří druhým dotazem, uloží data/lr.json + data/lr_protokol.txt a spustí kontrolu. LR blokuje servery GitHubu (Cloudflare), proto přes Claude. Zkušební běh 11. 10. 2026 úspěšný (218 produktů), první pravidelný běh 12. 10. 2026.
- 6:15 GitHub Actions: Eurona (veřejné JSON API /webapi/eshop/products/all), Essens (výpisy kategorií eshop.php?cat_id=…&load-more=…; produkty mimo kategorie přes detail z data/essens_url.csv – vyhledávání essens.cz bez přihlášení nic nevrací), e-shop z veřejných feedů (Google feed + Heureka availability).
- Google feed e-shopu vynechává vyprodané produkty a CBD → kontrola si pamatuje všechny produkty v data/eshop_produkty.json a ty, které ve feedu chybí, ověří přímo na jejich stránce (404 = skrytý; schema.org/InStock = skladem). Bez toho by se vyprodaný produkt nikdy znovu nenaskladnil (opraveno 11. 10. 2026).
- Kontrola cen u Essens parfémů 50 ml: 499 Kč jen u starší řady (doporučená ≤ 600 Kč), novější řada podle pravidla (589 Kč). Parfém se pozná podle názvu i kódu (Google feed má srovnávačové názvy „Essens m001 parfém pánský 50 ml“).
- Výstup: ke_importu/sklad.csv a ke_importu/ceny.csv + GitHub issue (štítek k-importu) s přehledem → e-mail majiteli.
- Doplněk Shoptet „Automatické importy“ (400 Kč/měs bez DPH) majitel NEchce → import souborů ručně, nebo Claude na požádání.
- Párování kódů: Essens mění kódy příponou (AVE01 → AVE01B, W18350 → W18350X); Eurona předpona E nebo písmeno navíc; LR shoda čísla před pomlčkou. Výjimky v data/aliasy.csv (mj. 6512→HOP71 ES'Pure, HOP51→VIT51 Clea'NS, CE0008→CE0003 káva Brazílie, CC6734→CA0168 difuzér Lavender), data/nesledovat.csv, data/nemenit_cenu.csv.
- V repozitáři nikdy nákupní ceny ani hesla. Pracovní soubory (texty, importy) ve větvi „prace“.

## Texty
- Podklad = text výrobce, napsat vlastními slovy.
- Složení / INCI / nutriční hodnoty a bezpečnostní upozornění: doslova podle výrobce.
- Nepřidávat zdravotní ani léčebná tvrzení, která výrobce neuvádí.
- Vzory: LR https://www.kosmetikaeva.eu/damske-parfemy/lr-be-magical-edp-pro-zeny/ · Eurona https://www.kosmetikaeva.eu/bile-pradlo/eurona-tekuty-praci-prostredek-na-prani-bileho-a-jemneho-svetleho-pradla--1000-ml/ · Essens https://www.kosmetikaeva.eu/damske-parfemy/essens-damsky-parfem-w107-50-ml/
- Název: značka + název + objem. SEO titulek „Název | KosmetikaEva.eu“. Meta popis vlastní, cca 150 znaků.
- Fotky od výrobce.
- Každý produkt má mít sekci s návodem (Použití / Aplikace / Návod k použití / Doporučené dávkování / Jak podávat / Příprava) – podle výrobce, u sad podle návodů jednotlivých produktů výrobce. Když výrobce na webu návod nemá, použije se jeho návod pro stejný typ produktu (např. parfémy Essens, séra LR). Sekce se vkládá před „Složení (INCI)“ / „Upozornění“ / „Skladování“.
- 11. 10. 2026 doplněn návod u 86 produktů (CZ i SK): 42 parfémů Essens, sady Essens a LR, ZEITGARD PRO, séra LR, parfémy a příslušenství Eurona, PB2026, CE0005.
- 11. 10. 2026 doplněny obecné tipy „Jak podávat“ / „Příprava“ u 24 potravin Eurona, kde výrobce návod nemá (schválil majitel): 10 tyčinek JETBAR, 7 medů MEDBAR, nápoje AURA/ZEN/VERVE, zrnkové kávy CE0004/6/7/8.
- Bez návodu zůstávají: zubní kartáčky Essens, ořezávátko EBA06, taštička LR 29034-101.
- Hodnocení produktů Claude nevytváří (majitel 12. 10. 2026: „nechystej“).

## Essens parfémy – „zaměňují za“
- V textech NESMÍ být „inspirováno …“ ani názvy cizích značek / parfémových domů (vyčištěno 11. 10. 2026 u 63 produktů, 12. 10. 2026 ještě W90350 / w903).
- Pod první nadpis popisu je box s ikonou: „Naši zákazníci tuto vůni nejčastěji zaměňují za: <název vůně>“ (SK: „Naši zákazníci si túto vôňu najčastejšie zamieňajú s:“). Hodnota podle Essens, jen název vůně bez značky. Box mají 140 parfémů a sad (CZ i SK).
- Bez boxu: obecné názvy bez značky nedávají smysl (Eau de Parfum, Pour Femme, Woman, Body, For Her) a „Bleu de Chanel“ (obsahuje značku).

## Slovenská verze
- Všechny texty LR/Eurona/Essens přeloženy do SK (11. 10. 2026: 898 produktů celý text, 126 název + meta + SEO), INCI beze změny.

## Srovnávače
- Kategorie Heureka a Zboží přiřazeny u všech viditelných produktů (kontrola 11. 10. 2026: 1 329 viditelných, chybí jen u 6 dárkových poukazů a služby „Káva pro Pampelišku“ – záměrně). Přiřazení podle kategorie e-shopu + klíčových slov v názvu.
- Nově přidané produkty dostanou kategorie Heureka/Zboží automaticky NE → nastavit vždy při přidání produktu.
- Feedy: Heureka https://www.kosmetikaeva.eu/heureka/export/products.xml (1 249 položek), Zboží/Seznam https://www.kosmetikaeva.eu/seznam/export/products.xml (1 250 položek), 11. 10. 2026 obsahují i nové produkty Eurona.
- Import: XML (HEUREKA_CATEGORY_ID = skutečné ID Heureky, ne hodnota z roletky Shoptetu; ZBOZI_CATEGORY_ID = hodnota z roletky). Varianty jen celým produktem (export → úprava → import).
- Názvy parfémů ve feedu (xmlFeedName) u 214 parfémů: výrobce + model + typ + pohlaví + objem (u produktů s variantami bez objemu – Shoptet přidá „Objem: …“ sám). Shoptet je používá i v Google feedu.
- Pozor: produkt jen ve skryté kategorii „Výchozí kategorie“ (id 1684) není na webu (404), ve feedech ani v sitemap. LR 20670-101 Aloe Vera Harmonizující čisticí mléko 200 ml tam byl – 11. 10. 2026 přesunut do Kosmetika › Obličej (id 1921) a doplněny kategorie srovnávačů.

## Google Ads a Merchant Center (stav 12. 10. 2026)
- Merchant Center 110663991: primární zdroje jsou feedy z Mergada (CZ „KosmetikaEva.eu - Mergado“, SK „KosmetikaEva.eu - Mergado - SK“), ID produktu = kód produktu v Shoptetu.
- Výkonnostní kampaně rozdělené podle značek (rozhodnutí majitele):
  - „VP: PMax - Eurona a LR - ROAS 600 %“ (CZ, 400 Kč/den) a „VP: PMax SK - Eurona a LR - ROAS 600 %“ (SK, 200 Kč/den, zapnuta 12. 10. 2026).
  - „VP: PMax - Just a Essens - ROAS 450 %“ (CZ, 350 Kč/den) a „VP: PMax SK - Just a Essens - ROAS 450 %“ (SK, 400 Kč/den).
  - Značky se oddělují ve skupinách záznamů (listing groups) podle značky; skupiny podkladů Essens a wellU v kampaních Eurona + LR jsou pozastavené.
- Nahrin a wellU jsou z reklam vyřazené (rozhodnutí majitele).
- Produkty s marží do 15 % (filtr „Marže do“ v exportu Shoptetu) jsou vyřazené z reklam přes doplňkové zdroje Merchant Center „Vyřazení z reklam (nízká marže) CZ“ a „… SK“ = soubor data/google_doplnek.tsv v repozitáři (id + excluded_destination Shopping_ads,Display_ads; stahuje se denně). 12. 10. 2026: 32 produktů. Ve výsledcích zdarma na Googlu zůstávají. Kód smazaný ze souboru = produkt se do reklam vrátí. Vyřazení levných produktů pod 150 Kč majitel nechtěl.
- Vyhodnocení rozdělení kampaní zhruba po 14 dnech (učení algoritmu).

## Úvodní stránka a patička (12. 10. 2026)
- Hero banner (carousel): banner30 desktop 1920×400, banner31 mobil 750×600, CZ i SK obrázek zvlášť. Zdroj grafiky: větev „prace“, work/banner (hero*.html → shot.py). Boxy produktů v jedné lince, produkty zarovnané ke spodní hraně.
- Text úvodní stránky: H1 + dlaždice značek (.ke-tile) a kategorií (.ke-cat); hover efekt v HTML kódech (záhlaví, blok „KE uvodni stranka“). Tamtéž skrytý starý box „Poslední komentáře“ (2017).
- Patička: prvky Heureka (hodnocení), „Proč nakoupit u nás“ (banner32, CZ i SK), Zákaznický servis, Kontakt, Facebook. Prvky se mění v Šablony → Prvky (/admin/prvky-stranky/).
- V seznamu s odrážkami v patičce je položka flex → odkaz a text za ním se slepí; celý řádek proto dávat do odkazu.
- SK adresa hodnocení obchodu: /sk/hodnotenie-obchodu/.

## Indexace Google
- Search Console (vlastnost https://www.kosmetikaeva.eu/): sitemap https://www.kosmetikaeva.eu/sitemap.xml byla od 7/2025 ve stavu „Nelze načíst“, 11. 10. 2026 znovu odeslána. Živý test URL sitemap 11. 10. 2026: Google ji načte bez problému; sitemap má 1 425 adres, platné XML, načtení 0,5 s.
- Stav k 4. 10. 2026: indexováno 2,29 tis., neindexováno 1,19 tis. (robots.txt 705, noindex 261 – filtry, „Hlídat cenu“, „Dotaz“, správně; 89 procházeno – neindexováno; 49× 404; 50 alternativní kanonické; 33 přesměrování).

## Import do Shoptetu
- Vždy „Neměnit produkty a varianty, které nejsou obsaženy v importu“ a NIKDY „Změnit adresu URL produktu podle názvu“.
- Sloupec pairCode musí být v souboru vždy.
- Prázdná buňka v CSV může pole smazat → každý soubor jen se sloupci, které se mění.
- CZ a SK popis NIKDY v jednom CSV (sloupce description + description:sk v jednom souboru → import se zasekne a nedoběhne). Vždy dva samostatné soubory.
- CSV export Shoptetu je ve windows-1250 – znaky è, ò, ì (např. Éclat d'Arpège, Acqua di Giò, Sì) se v něm ztratí. CZ texty pro zpětný import brát z XML exportu (UTF-8), u SK tyto znaky opravit.
- Záloha (export) před každou hromadnou změnou.
- Přihlášení do administrace dělá vždy majitel sám (hesla Claude neukládá ani nevyplňuje).
