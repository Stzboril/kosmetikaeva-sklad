// ke-ikony-v17.js = živý ke-ikony-v16.js + ikony výrobku 7684 (Just VJ Krém na okolí očí 30 ml)
// 29. 10. 2026, majitel: „u výrobku chybí výhody, ty doplň“
// Výsledek: 195 176 B, SHA-256 6c5e11e847ed3c99b944550b187ad54364d5cc0678e276c4f8e8169033a857c9
// Návrat = zavaděč v zápatí HTML kódů zpět na ke-ikony-v16.js?v=1. Další verze = ke-ikony-v18.js.
function keIkonyPatch17(textV16) {
  if (textV16.includes('"7684":')) throw new Error('7684 už v souboru je');
  let t = textV16.replace('"7687":"', '"7684":"ch,s_protez,s_alpruze,bezparf,derm,u_hydr","7687":"');
  t = t.replace('/* ke-ikony-v16.js', '/* ke-ikony-v17.js – v17 (29. 10. 2026): + 7684 Just VJ Krém na okolí očí (ch,s_protez,s_alpruze,bezparf,derm,u_hydr); návrat = v16\n   ke-ikony-v16.js');
  return t;
}
