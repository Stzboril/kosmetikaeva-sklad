/* Úprava ke-ikony-v8.js → ke-ikony-v9.js (23. 10. 2026, majitel: „projdi celý web a ikony podoplňuj“, „i u ostatních výrobků“).
   - 10 nových glyfů a 11 ikon (v9-glyfy.json, v9-ikony.json; generátor v9-glyfy.py):
     s_kolos Kolostrum, s_slez Sléz/Slez, s_oves Oves/Ovos, s_reva Vinná réva/Vinič, s_rasy Řasy/Riasy, s_peptid Peptidy,
     s_kurkuma Kurkuma, s_avokado Avokádo, s_omega Omega-3, s_med Med (glyf honey), d_dopl Doplněk stravy/Výživový doplnok
   - doplnění ikon u výrobků z celého webu (mapa webu, 1 304 viditelných výrobků, analýza v prohlížeči):
     složky (pravidla v4: název, nebo hlavní složky + INCI u kosmetiky; u doplňků název / hlavní složky / první 3 složky
     nebo s množstvím; bez parfémů a domácnosti; nejvýš 3 ikony složek), vlastnosti doslova uvedené v textu výrobce
     (vegan, bez parabenů, bez lepku, bez laktózy, bez barviv, bez alkoholu, bez přidaného cukru, bez parfemace,
     bez silikonů, bez konzervantů), účinek z názvu výrobku, Pro muže/Pro děti podle kategorie, Doplněk stravy.
     Nové ikony se vkládají podle skupin (původ, vlastnosti, složky, přednosti, účinek, pro koho, typ, vůně, prádlo,
     forma, vhodné na, druh), dosavadní ikony zůstávají; původ vždy první, celkem nejvýš 6.
   Použití v prohlížeči: keIkonyPatch9(textV8, glyfy, ikony, set) → textV9, kde set = { id: [nové, dosavadní] }.
   Seznam změn (set) je uložen v živém souboru (blok P) – rozdíl proti v8 jde kdykoli spočítat porovnáním P. */
function keIkonyPatch9(src, glyfy, ikony, set) {
  function block(name) {
    var i = src.indexOf('var ' + name + ' = '); if (i < 0) throw new Error('chybí ' + name);
    var s = src.indexOf('{', i), d = 0, e = s;
    for (; e < src.length; e++) { if (src[e] === '{') d++; else if (src[e] === '}') { d--; if (d === 0) { e++; break; } } }
    return { s: s, e: e, v: JSON.parse(src.slice(s, e)) };
  }
  function put(b, v) { src = src.slice(0, b.s) + JSON.stringify(v) + src.slice(b.e); }
  function once(a, b) {
    if (src.split(a).length !== 2) throw new Error('nečekaný výskyt: ' + a);
    src = src.replace(a, b);
  }
  var gl = block('GL');
  Object.keys(glyfy).forEach(function (k) {
    if (gl.v[k]) throw new Error('glyf už existuje: ' + k);
    gl.v[k] = glyfy[k];
  });
  put(gl, gl.v);
  var ic = block('IC');
  ikony.forEach(function (r) {
    if (ic.v[r[0]]) throw new Error('ikona už existuje: ' + r[0]);
    if (!gl.v[r[1]]) throw new Error('chybí glyf ' + r[1]);
    ic.v[r[0]] = r.slice(1);
  });
  put(ic, ic.v);
  var p = block('P'), puvod = ['ch', 'de', 'ceskymed'];
  Object.keys(set).forEach(function (id) {
    var nove = set[id][0], stare = set[id][1];
    if (p.v[id] !== stare) throw new Error('výrobek ' + id + ' má jiné ikony: ' + p.v[id]);
    var ks = nove.split(',');
    if (ks.length > 6) throw new Error('víc než 6 ikon u ' + id);
    ks.forEach(function (k, i) {
      if (!ic.v[k]) throw new Error('neznámá ikona ' + k + ' u ' + id);
      if (i > 0 && puvod.indexOf(k) >= 0) throw new Error('původ není první u ' + id);
      if (ks.indexOf(k) !== i) throw new Error('duplicitní ikona ' + k + ' u ' + id);
    });
    stare.split(',').forEach(function (k) { if (ks.indexOf(k) < 0) throw new Error('ztratila by se ikona ' + k + ' u ' + id); });
    p.v[id] = nove;
  });
  put(p, p.v);
  once('/* ke-ikony-v8.js – ', '/* ke-ikony-v9.js – ');
  once('Just Infiore sérum (11456) a 18 výrobků JUST/Essens s těmito složkami. */',
    'Just Infiore sérum (11456) a 18 výrobků JUST/Essens s těmito složkami.\n' +
    '   v9 (23. 10. 2026): ikony doplněny u výrobků z celého webu (složky, vlastnosti podle výrobce, účinek z názvu, Pro muže/děti, Doplněk stravy);\n' +
    '      nové ikony Kolostrum, Sléz, Oves, Vinná réva, Řasy, Peptidy, Kurkuma, Avokádo, Omega-3, Med, Doplněk stravy. */');
  return src;
}
