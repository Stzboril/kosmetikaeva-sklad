# Denní ruční indexace nových výrobků (Search Console)

Zavedeno 17. 10. 2026 po kontrole indexace (projektový dokument claude/indexace-google.md).

## Proč
546 nejnovějších výrobků (ID produktu od 9802) Google neznal – mapa webu /sitemap.xml byla od 7/2025 ve stavu „Nelze načíst“.
17. 10. 2026 odeslána /sitemap.xml?v=2 → Google ji hned načetl (1 428 stránek). Ruční žádosti indexaci jen urychlují.

## Soubory
- fronta.txt – adresy (cesta od kořene webu, CZ verze) v pořadí priority: nejdřív výrobky s prodeji 1/2025–10/2026 (podle kódu), pak podle prodejů kategorie (esenciální oleje, dámské parfémy, tělo, pánské parfémy, obličej…).
- stav.tsv – co už je hotové: datum<TAB>cesta<TAB>výsledek (pozadano | na-googlu | chyba: …). Hlavička se nemaže.

## Postup jednoho běhu (max. 10 žádostí denně – limit Search Console)
1. Prohlížeč v aplikaci Claude (přihlášený Google účet majitele). Hesla nikdy nezadávat; když je potřeba přihlášení, napsat majiteli.
2. Search Console, vlastnost https://www.kosmetikaeva.eu/ → Soubory Sitemap: zapsat stav /sitemap.xml?v=2 (poslední čtení, objevené stránky). Když je chyba, napsat majiteli.
3. Vzít další adresy z fronta.txt, které nejsou ve stav.tsv. Pro každou: lupa nahoře → vložit https://www.kosmetikaeva.eu + cesta → Enter → počkat na výsledek.
   - „Adresa URL je na Googlu“ → zapsat na-googlu (nežádat).
   - jinak → „Požádat o indexování“ → počkat (~20 s) na „Požádáno o indexování“ → zapsat pozadano.
   - hláška o překročení kvóty → skončit, zbytek zítra.
4. Po 10 žádostech skončit. Zapsat stav.tsv, commit + push do větve „prace“.
5. Když je fronta hotová: napsat majiteli shrnutí a navrhnout smazání naplánované úlohy.
