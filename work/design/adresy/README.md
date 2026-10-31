# Našeptávač a kontrola adres z Mapy.com (ke-adresy-v2.js)

31. 10. 2026, majitel: „líbí se mi i našeptávač i alternativa a bude jen při doručení kurýrem, jinak to nemá smysl“.

## Co dělá
- Běží jen v košíku v kroku 2 (`/objednavka/krok-2/`, i `/sk/objednavka/krok-2/`) a jen když je zvolen kurýr.
- Našeptávač: od 3. znaku v poli Ulice / Číslo domu, po 300 ms pauze, cache a rušení starých dotazů. Po výběru doplní ulici, číslo, město a PSČ.
- Kontrola: když je adresa vyplněná, za 900 ms ji ověří přes geocode. Nenalezená adresa = oranžové upozornění (objednávku neblokuje), vybraná nebo ověřená = „✓ Adresa ověřena“.
- Automatické vyplnění prohlížečem nenašeptává (šetří kredity), ale adresu zkontroluje.
- Logo Mapy.com v patičce našeptávače (podmínka API).
- Bez `window.KE_MAPY_KEY` nedělá nic.

## Nasazení
- **v2 (31. 10. 10:00, živá):** chyba API (neplatný klíč, vyčerpané kredity, výpadek) nikdy neukáže upozornění; po 401/403/429 už na stránce nic nevolá; klíč kratší než 12 znaků = jako bez klíče. Soubor `/user/documents/upload/CSS/ke-adresy-v2.js`, 12 725 B, SHA-256 `baf1d4cd768db4306d0f708c7abb2926c6e64e1cf731e25d711a6403052fb84f` (commit 7736e52). Zavaděč v Zápatí přepnut na ke-adresy-v2.js?v=1 (záloha zápatí `keBackup_footer_20261031_adresy_v2`). Návrat = v1. Důvod: majitel vložil řádek se zástupným klíčem „KLIC“ a v1 by pak ukazovala upozornění u každé kurýrní adresy.
- v1:
- Soubor: `/user/documents/upload/CSS/ke-adresy-v1.js`, 12 299 B, SHA-256 `66a29815a1cfe629e267ef426e960caa6cb400cd6c3b05d81380f90f8f987a0d` (= commit 72d3d9b).
- Zavaděč na konci HTML kódů → Zápatí (vložen 31. 10. 2026, záloha zápatí v prohlížeči `keBackup_footer_20261031_adresy`):
  ```html
  <script>(function(){if(/\/objednavka\/krok-2\//.test(location.pathname)){var s=document.createElement('script');s.src='/user/documents/upload/CSS/ke-adresy-v1.js?v=1';s.defer=true;document.body.appendChild(s);}})();</script>
  ```
- Klíč vkládá majitel sám jedním řádkem do Zápatí: `<script>window.KE_MAPY_KEY='…';</script>`. Klíč nepatří do repozitáře, dokumentů ani paměti.
- Vypnutí = smazat blok zavaděče (nebo řádek s klíčem). Další verze = ke-adresy-v2.js (správce souborů nepřepisuje).

## Kredity
- Basic tarif 250 000 kreditů měsíčně zdarma, 1 dotaz = 4 kredity, placené čerpání je ve výchozím stavu vypnuté.
- Typicky ~5 dotazů našeptávače + 1 kontrola na jednu adresu ≈ 24 kreditů → zhruba 10 000 kurýrních adres měsíčně zdarma.

## Test 31. 10. 2026 (krok 2, kurýr)
- „Masarykova 12“ → návrhy s logem, šipky + Enter vybraly „Masarykova 318/12, 602 00 Brno“ bez odeslání formuláře.
- Přílucká 4118, Zlín 76001 ověřeno; Vymyšlená 999, Horní Dolní 12345 → upozornění; Těšetice 213, 67161 ověřeno; Masarykova 12, Brno 60200 ověřeno.

## Další
- Zásady ochrany osobních údajů (stránka id 1908, CZ i SK): doplněna položka Seznam.cz, a.s. – služba Mapy.com (31. 10.).
- Naplánovaná úloha „Kontrola adres kurýrních objednávek“ trig_017sweA2RY2iai4kiVGucSTQ, po–pá 7:53, upozornění e-mailem (text: kontrola-objednavek-uloha.md).
