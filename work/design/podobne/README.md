# Pruh „Podobné výrobky“ v okně Přidáno do košíku (ke-podobne-v1.js)

31. 10. 2026, majitel: „co sem přidat ještě pruh pod to, s výrobky, které jsou podobné (tedy ne související)“; náhled schválen „ano“ (10:54).

## Co dělá
- Po otevření okna „Přidáno do košíku“ (událost Shoptetu `ShoptetDOMAdvancedOrderLoaded`) přidá pod řádek s dopravou a tlačítkem košíku pruh „Podobné výrobky“ (SK „Podobné produkty“).
- Až 8 výrobků, na počítači 4 vedle sebe + šipky, na mobilu 2 a tažení prstem. Karta: obrázek, název, cena, tlačítko „Do košíku“ (standardní formulář Shoptetu `form.pr-action`, přidá přes AJAX a otevře okno znovu), u výrobků s variantami „Vybrat“ → detail.
- Zdroj = záložka Podobné (#productsAlternative) přidaného výrobku: na detailu přímo ze stránky (bez slick klonů), z výpisu kategorie / úvodu se detail přidaného výrobku jednou načte (fetch) a uloží do paměti stránky.
- Který výrobek se přidal: zachytí klik/odeslání tlačítka do košíku (karta ve výpisu → její odkaz; hlavní formulář detailu → aktuální stránka).
- Vynechá přidaný výrobek a výrobky, které okno už ukazuje (Související = příslušenství).
- Nenačítá se v pokladně (/objednavka/).

## Nasazení
- Soubor `/user/documents/upload/CSS/ke-podobne-v1.js`, 11 205 B, SHA-256 `5db8c5d6ea5024797e6edd34da834e7c0c88a4550c7b0bddcd86da580e5f79b9` (commit 4146913).
- Zavaděč na konci HTML kódů → Zápatí (31. 10. 2026; záloha zápatí v prohlížeči `keBackup_footer_20261031_podobne`):
  ```html
  <script>(function(){if(!/\/objednavka\//.test(location.pathname)){var s=document.createElement('script');s.src='/user/documents/upload/CSS/ke-podobne-v1.js?v=1';s.defer=true;document.body.appendChild(s);}})();</script>
  ```
- Vypnutí = smazat blok zavaděče. Další verze = ke-podobne-v2.js.

## Test 31. 10. 2026
- Okno „Přidáno do košíku“ se v prohlížeči přihlášeném do administrace neotevírá (GetExtendedOrder vrací content:false), test proto přes napodobené okno se stejnými třídami (shoptet.modal.open + ShoptetDOMAdvancedOrderLoaded).
- Detail Just Jalovcový krém → 8 karet (Eucasol, Jalovcová esence, Tymiánový krém, Slézový krém…), šablona Venus vzhled okna zachová.
- Výpis Tělo → LR Aloe Vera Ochranný deo roll-on → načten detail, 8 karet LR Aloe Vera. Košík beze změny.
