/* Úprava ke-ikony-v10.js → ke-ikony-v11.js (23. 10. 2026, majitel: „horský jalovec není kosmetika“).
   Nahrin Horský jalovec 500 g (id 7537, kód 4526) = doplněk stravy; jeho CZ popis měl omylem složení z gelu na holení JUST
   (proto ve v10 ikona Řasy). Popis opraven podle JUST CZ (work/opravy/4526) → ikony podle výrobce:
   Švýcarsko, Vegan, Bez lepku, Bez laktózy (justnahrin.cz „slozeniAAlergeny“), Jalovec, Doplněk stravy.
   Použití v prohlížeči: keIkonyPatch11(textV10) → textV11 */
function keIkonyPatch11(src) {
  var set = { '7537': ['ch,vegan,bezlep,bezlakt,s_jalov,d_dopl', 'ch,s_jalov,s_rasy'] };
  function block(name) {
    var i = src.indexOf('var ' + name + ' = '); if (i < 0) throw new Error('chybí ' + name);
    var s = src.indexOf('{', i), d = 0, e = s;
    for (; e < src.length; e++) { if (src[e] === '{') d++; else if (src[e] === '}') { d--; if (d === 0) { e++; break; } } }
    return { s: s, e: e, v: JSON.parse(src.slice(s, e)) };
  }
  function once(a, b) {
    if (src.split(a).length !== 2) throw new Error('nečekaný výskyt: ' + a);
    src = src.replace(a, b);
  }
  var ic = block('IC').v, p = block('P');
  Object.keys(set).forEach(function (id) {
    if (p.v[id] !== set[id][1]) throw new Error('výrobek ' + id + ' má jiné ikony: ' + p.v[id]);
    set[id][0].split(',').forEach(function (k) { if (!ic[k]) throw new Error('neznámá ikona ' + k); });
    p.v[id] = set[id][0];
  });
  src = src.slice(0, p.s) + JSON.stringify(p.v) + src.slice(p.e);
  once('/* ke-ikony-v10.js – ', '/* ke-ikony-v11.js – ');
  once('Omega-3, Med, Doplněk stravy. */',
    'Omega-3, Med, Doplněk stravy.\n' +
    '   v11 (23. 10. 2026): Nahrin Horský jalovec (7537) – doplněk stravy: Vegan, Bez lepku, Bez laktózy, Jalovec, Doplněk stravy (místo Řasy). */');
  return src;
}
