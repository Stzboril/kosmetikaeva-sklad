/* Úprava ke-ikony-v6.js → ke-ikony-v7.js (21. 10. 2026, majitel: „tento výrobek předělej, aby byl v pořádku, CZ i SK“).
   Nahrin Vitamin D3 Complex 60 kapslí (id 9364, kód 6250): přidány ikony Bez lepku a Bez laktózy
   (výrobce na nahrin.ch uvádí „laktosefrei, glutenfrei“). Pořadí: původ, složení a vlastnosti (bez…), složky, forma.
   Použití v prohlížeči: keIkonyPatch7(textV6) → textV7 */
function keIkonyPatch7(src) {
  var set = { '9364': 'ch,bezlep,bezlakt,v_d,v_b,f_kaps' };
  var expectOld = { '9364': 'ch,v_d,v_b,f_kaps' };
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
  var ic = block('IC').v;
  var p = block('P');
  Object.keys(set).forEach(function (id) {
    if (p.v[id] !== expectOld[id]) throw new Error('výrobek ' + id + ' má jiné ikony: ' + p.v[id]);
    var ks = set[id].split(',');
    if (ks.length > 6) throw new Error('víc než 6 ikon u ' + id);
    ks.forEach(function (k) { if (!ic[k]) throw new Error('neznámá ikona ' + k); });
    p.v[id] = set[id];
  });
  src = src.slice(0, p.s) + JSON.stringify(p.v) + src.slice(p.e);
  once('/* ke-ikony-v6.js – ', '/* ke-ikony-v7.js – ');
  once('v6 (21. 10. 2026): ikona původu (Švýcarsko, Německo, Český med) vždy na prvním místě. */',
    'v6 (21. 10. 2026): ikona původu (Švýcarsko, Německo, Český med) vždy na prvním místě.\n' +
    '   v7 (21. 10. 2026): Nahrin Vitamin D3 Complex (9364) + Bez lepku, Bez laktózy. */');
  return src;
}
