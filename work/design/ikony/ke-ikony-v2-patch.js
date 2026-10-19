/* Úprava ke-ikony-v1.js → ke-ikony-v2.js (19. 10. 2026, majitel: „Německo – vlajka jako u Švýcarska“,
   „klidně dodělej i další ikony“). Zdroj ikon je živý soubor na webu (data jsou uvnitř), tento skript ho jen upraví:
   - „Vyrobeno v Německu“: místo špendlíku (pin) vlajka ve stejném rámečku jako švýcarská (tmavý / vínový / světlý pruh)
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
  gl.v.deflag = {
    f: 'M6 3h12a3 3 0 0 1 3 3v12a3 3 0 0 1-3 3H6a3 3 0 0 1-3-3V6a3 3 0 0 1 3-3z',
    s: 'M6 3h12a3 3 0 0 1 3 3v3H3V6a3 3 0 0 1 3-3z',
    h: 'M6 4.2h12A1.8 1.8 0 0 1 19.8 6v1.4C15 6.6 9 6.6 4.2 7.6V6A1.8 1.8 0 0 1 6 4.2z',
    c: 'M4.2 15h15.6v2.8a1.9 1.9 0 0 1-1.9 1.9H6.1a1.9 1.9 0 0 1-1.9-1.9z'
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
  ic.v.de[0] = 'deflag';
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
      '   v2 (19. 10. 2026): Německo = vlajka (deflag), nová ikona Ledovcová voda, ikony výrobků 11434, 11437, 11440, 11443. */');
  return src;
}
