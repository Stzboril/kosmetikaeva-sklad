/* Úprava ke-ikony-v1.js → ke-ikony-v2.js (19. 10. 2026, majitel: „obrys Německa nebo mapa Evropy“,
   „klidně dodělej i další ikony“). Zdroj ikon je živý soubor na webu (data jsou uvnitř), tento skript ho jen upraví:
   - „Vyrobeno v Německu“: místo špendlíku (pin) obrys Německa (majitel: vlajka „strašná“, chtěl obrys Německa; mapa Evropy je v reálné velikosti nečitelná)
   - nová ikona „Ledovcová voda“ (glyf glacier = hory se sněhem)
   - ikony pro nové výrobky 11434 Alpský vánek, 11437 Lesní vánek, 11440 LR Serox série, 11443 Aroma Care Vitality peeling
   Použití v prohlížeči: keIkonyPatch(textV1) → textV2. */
function keIkonyPatch(src) {
  function block(name) {
    var i = src.indexOf('var ' + name + ' = '); if (i < 0) throw new Error('chybí ' + name);
    var s = src.indexOf('{', i), d = 0, e = s;
    for (; e < src.length; e++) { if (src[e] === '{') d++; else if (src[e] === '}') { d--; if (d === 0) { e++; break; } } }
    return { s: s, e: e, v: JSON.parse(src.slice(s, e)) };
  }
  function put(b, v) { src = src.slice(0, b.s) + JSON.stringify(v) + src.slice(b.e); }

  var gl = block('GL');
  /* obrys Německa (zjednodušená hranice, 54 bodů, výška 21,5 z 24) */
  gl.v.demap = {
    f: 'M10.2 1.5 11.4 2.5 13.0 2.5 12.7 3.9 13.6 3.8 15.6 2.5 17.2 2.0 18.0 3.5 18.6 3.9 18.9 5.5 18.5 7.0 19.3 8.4 19.3 10.1 20.0 11.8 19.6 12.6 18.9 12.5 17.4 12.9 16.5 13.8 15.2 14.1 14.9 14.5 15.5 15.2 15.9 16.6 17.3 18.0 17.8 19.1 16.5 20.0 16.4 21.4 16.5 22.1 15.5 21.5 15.0 21.8 13.6 22.2 12.8 22.4 11.5 22.8 10.6 22.0 9.7 21.6 8.7 21.6 6.9 21.9 6.9 20.4 8.0 18.0 5.4 17.3 4.7 16.6 5.0 15.6 4.3 14.7 4.1 12.9 4.2 11.7 4.0 9.8 6.0 8.9 5.9 7.7 6.2 5.8 6.4 4.6 7.6 4.6 8.9 4.2 9.1 3.6 8.8 2.5 8.8 1.2z'
  };
  gl.v.glacier = {
    f: 'M1.5 20.5L9 6l4 6.6L16 8l6.5 12.5z',
    s: 'M16 8l6.5 12.5h-4z M9 6l4 6.6-1.8 2.8z',
    h: 'M9 6L4.8 14l1.1-.3z',
    c: 'M9 6l2.4 4.6-1.3-.6-1.1 1.3-1.1-1.3-1.3.6z M16 8l2.1 4-1.1-.5-1 1.1-1-1.1-1.1.5z'
  };
  put(gl, gl.v);

  var ic = block('IC');
  if (!ic.v.de) throw new Error('chybí ikona de');
  ic.v.de[0] = 'demap';
  ic.v.ledovec = ['glacier', 'Ledovcová voda', 'Ľadovcová voda',
    'Se švýcarskou ledovcovou vodou z Engelbergu – podle údajů výrobce.',
    'So švajčiarskou ľadovcovou vodou z Engelbergu – podľa údajov výrobcu.'];
  put(ic, ic.v);

  var p = block('P');
  p.v['11434'] = 'vegan,ch,d_vune';
  p.v['11437'] = 'ch,d_vune';
  p.v['11440'] = 'de,d_plet';
  p.v['11443'] = 'ledovec,ch,u_energ,vs_citr,d_sprcha,d_telo';
  put(p, p.v);

  src = src.replace('/* ke-ikony-v1.js – ', '/* ke-ikony-v2.js – ')
    .replace('Ikony výrobků: vygenerováno 2026-10-15 z exportu produktů a údajů výrobců. */',
      'Ikony výrobků: vygenerováno 2026-10-15 z exportu produktů a údajů výrobců.\n' +
      '   v2 (19. 10. 2026): Německo = obrys Německa (demap), nová ikona Ledovcová voda, ikony výrobků 11434, 11437, 11440, 11443. */');
  return src;
}
