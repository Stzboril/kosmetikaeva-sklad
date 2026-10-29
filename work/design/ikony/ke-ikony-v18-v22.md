# ke-ikony v18–v22 (29. 10. 2026)

Majitel: „zmen tuti ikonku, vypadá to jako černoch“ (Dermatologicky testováno – glyf face, vínově vyplněný obličej),
„také na mobilu to není na střed stránky“, „ta ikona drmatologicky není hezká“, „mohou tam být třeba bunky kuze pod lupou“,
„muže tam být te kuže víc“, „i mimo lupu a co kdyby ta lupy byla na ženském obličeji?“, „varianta B“, „to mikado je strašné“.

- v18 (derm = skintest, vrstvy pokožky + fajfka) – nahráno, NEPOUŽITO
- v19 (v18 + střed) – nahráno, NEPOUŽITO
- v20 = v17 + .ke-ik-row justify-content:center, .ke-ik-note text-align:center – NA WEBU 10:31–10:36
- v21 (v20 + skinlupa = lupa s buňkami) – nahráno, NEPOUŽITO
- v22 = v20 + glyf skinzena (varianta B z derm/varianty.json @ ab9889a: ženský obličej obkreslený, vlasy vínové, lupa s kožními buňkami na tváři), IC derm[0] = "skinzena"
  - 198 232 B, SHA-256 a4dcca1392380e4e24b5f13bdd6fe6326c13648e0519c7ddaeedc8e7d0784798 – NA WEBU od ~10:37
  - Návrat = v20 (stará ikona obličeje + střed), resp. v17.
- Glyf face dál používá d_plet „Péče o pleť“ (129 výrobků).
- Varianta A (kůže všude) a upravená B (mikádo – majitel zamítl) jsou v derm/varianty.json @ 376f0f0.

## v23 (29. 10. 2026 ~11:35) – NA WEBU
- Ikona „Péče o pleť“ (d_plet, 129 výrobků): glyf face → pletzena = obkreslený ženský obličej (celá hlava, vpravo vlasy za uchem), kapátko a kapka séra na tváři, jiskry; data derm/plet-kapatko.json @ 14afac1 (klíč K). Majitel: „ano nasaď“.
- 199 721 B, SHA-256 207f34562a34e9c8358bd99d943072ad32e93b974d859a999af1348543142a70. Zápatí v22 → v23, záloha localStorage keHtmlKodyBackup_20261029_ikony23. Návrat = v22.
- Glyf face už nepoužívá žádná ikona. Další verze = ke-ikony-v24.js.
- Náhledy pro majitele se renderují i mimo prohlížeč aplikace: scratchpad nahled/render.py (Playwright, PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers) → PNG do chatu.
