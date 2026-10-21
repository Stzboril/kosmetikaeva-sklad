/* Úprava ke-ikony-v3.js → ke-ikony-v4.js (21. 10. 2026, majitel: „Klidně vymysli i další ikonky k doplnění.
   Například nejvíc zastoupené bylinky apod.“).
   Zdroj je živý soubor na webu (data jsou uvnitř), tento skript ho jen upraví:
   - 7 nových glyfů složek (v4-glyfy.json, generátor v4-glyfy.py): mint, verbena, lime, jasmine, cone, buckthorn, sacha
   - 7 nových ikon (v4-ikony.json): s_mata, s_sporys, s_limet, s_jasmin, s_cedr, s_rakyt, s_sacha
   - ikony nových výrobků JUST 5574, 5580, 5381 (id produktů doplnit po založení)
   Použití v prohlížeči: keIkonyPatch4(textV3, glyfy, ikony, add) → textV4
     glyfy = obsah v4-glyfy.json, ikony = obsah v4-ikony.json ([klíč, glyf, CZ, SK, CZ popisek, SK popisek]),
     add = { '<id produktu>': 'klíč,klíč,…' } */
function keIkonyPatch4(src, glyfy, ikony, add) {
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

  var p = block('P');
  Object.keys(add).forEach(function (id) {
    if (p.v[id]) throw new Error('výrobek už ikony má: ' + id);
    var ks = add[id].split(',');
    if (ks.length > 6) throw new Error('víc než 6 ikon u ' + id);
    ks.forEach(function (k) { if (!ic.v[k]) throw new Error('neznámá ikona ' + k + ' u ' + id); });
    p.v[id] = add[id];
  });
  put(p, p.v);

  once('/* ke-ikony-v3.js – ', '/* ke-ikony-v4.js – ');
  once('nové ikony Péče o vousy a Domácí jogurt. */',
    'nové ikony Péče o vousy a Domácí jogurt.\n' +
    '   v4 (21. 10. 2026): ikony složek Máta, Sporýš, Limetka, Jasmín, Cedr, Rakytník, Sacha inchi; ikony výrobků JUST 5574, 5580, 5381. */');
  return src;
}
