/* Úprava ke-ikony-v4.js → ke-ikony-v5.js (21. 10. 2026, majitel „ano přidej ho“):
   ikony pro Just for Men sprchový gel 250 ml (id 11444, kód 848/250) – byl při tvorbě v4 skrytý.
   Panthenol podle INCI a popisu, Švýcarsko, Osvěžující (osvěžující mytí), Pro muže, Do sprchy.
   Použití v prohlížeči: keIkonyPatch5(textV4) → textV5 */
function keIkonyPatch5(src) {
  var set = { '11444': 's_panth,ch,u_osv,p_muzi,d_sprcha' };
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
    if (p.v[id]) throw new Error('výrobek už ikony má: ' + id);
    set[id].split(',').forEach(function (k) { if (!ic[k]) throw new Error('neznámá ikona ' + k); });
    p.v[id] = set[id];
  });
  src = src.slice(0, p.s) + JSON.stringify(p.v) + src.slice(p.e);
  once('/* ke-ikony-v4.js – ', '/* ke-ikony-v5.js – ');
  once('ikony výrobků JUST 5574, 5580, 5381. */',
    'ikony výrobků JUST 5574, 5580, 5381.\n   v5 (21. 10. 2026): ikony Just for Men sprchový gel 250 ml (11444). */');
  return src;
}
