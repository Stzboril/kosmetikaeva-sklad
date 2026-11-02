// ke-ikony-v25.js = živý ke-ikony-v24.js (SHA-256 61c224bb723dd39ae8d37f413f97162dc2396d21772dd56282c8b4ae7e1d1212) + ikony výrobku 11657 (Just Mýdlo na ruce 250 ml, kód 9091)
// 2. 11. 2026, majitel: „ikony doplň, to už bude platit pro vždycky“ (= každý nový výrobek hned s ikonami)
// Klíče: ch (Vyrobeno ve Švýcarsku, vždy první), s_reva (olej z hroznových jadérek), s_mata (máta peprná), vs_citr (citron, mandarinka),
//        jemcis (jemné mycí látky z kokosového oleje), d_mydlo (tekuté mýdlo); glyfy swiss, grape, mint, citrus, feather, soap – žádný dvakrát.
// Výsledek: 201 416 B, SHA-256 213dc4e61d7141817e9b86bd8752f275a9807231259818f5bf97af4cba219a9a
// Návrat = zavaděč v zápatí HTML kódů zpět na ke-ikony-v24.js?v=1 (záloha zápatí localStorage keHtmlKodyBackup_20261102_ikony25). Další verze = ke-ikony-v26.js.
function keIkonyPatch25(textV24) {
  if (textV24.includes('"11657":')) throw new Error('11657 už v souboru je');
  const keys = 'ch,s_reva,s_mata,vs_citr,jemcis,d_mydlo';
  const m = textV24.match(/"11654":"[^"]*"/);
  if (!m) throw new Error('kotva 11654 chybí');
  let t = textV24.replace(m[0], m[0] + ',"11657":"' + keys + '"');
  t = t.replace('/* ke-ikony-v24.js – v24', '/* ke-ikony-v25.js – v25 (2. 11. 2026): + 11657 Just Mýdlo na ruce 250 ml (' + keys + '); návrat = v24\n   ke-ikony-v24.js – v24');
  return t;
}
