/* Úprava ke-ikony-v5.js → ke-ikony-v6.js (21. 10. 2026, majitel: „kde to bylo vyrobeno bude vždy na prvním místě“).
   U všech výrobků se ikona původu (ch = Vyrobeno ve Švýcarsku, de = Vyrobeno v Německu, ceskymed = Český med)
   přesune na první místo; pořadí ostatních ikon zůstává.
   Použití v prohlížeči: keIkonyPatch6(textV5) → { src: textV6, moved: počet výrobků } */
function keIkonyPatch6(src) {
  var ORIGIN = ['ch', 'de', 'ceskymed'];
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
  var p = block('P'), moved = 0;
  Object.keys(p.v).forEach(function (id) {
    var ks = p.v[id].split(',');
    var o = ks.filter(function (k) { return ORIGIN.indexOf(k) >= 0; });
    if (!o.length) return;
    var n = o.concat(ks.filter(function (k) { return ORIGIN.indexOf(k) < 0; })).join(',');
    if (n !== p.v[id]) { p.v[id] = n; moved++; }
  });
  src = src.slice(0, p.s) + JSON.stringify(p.v) + src.slice(p.e);
  once('/* ke-ikony-v5.js – ', '/* ke-ikony-v6.js – ');
  once('v5 (21. 10. 2026): ikony Just for Men sprchový gel 250 ml (11444). */',
    'v5 (21. 10. 2026): ikony Just for Men sprchový gel 250 ml (11444).\n' +
    '   v6 (21. 10. 2026): ikona původu (Švýcarsko, Německo, Český med) vždy na prvním místě. */');
  return { src: src, moved: moved };
}
