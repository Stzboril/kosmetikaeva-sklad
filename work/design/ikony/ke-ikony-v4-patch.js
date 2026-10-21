/* Úprava ke-ikony-v3.js → ke-ikony-v4.js (21. 10. 2026, majitel: „Klidně vymysli i další ikonky k doplnění.
   Například nejvíc zastoupené bylinky apod.“ a „klidně projdi všechny výrobky, jestli najdeš nějaké informace,
   ke kterým by se dala vytvořit ikona, udělej ji“).
   Zdroj je živý soubor na webu (data jsou uvnitř), tento skript ho jen upraví:
   - 40 nových glyfů (v4-glyfy.json; generátory v4-glyfy.py a v4-glyfy2.py, náhled v4-nahled.py)
   - 44 nových ikon složek (v4-ikony.json): byliny, oleje, vitaminy, minerály, aktivní látky – popisek „Obsahuje …“
   - ikony výrobků: set = { '<id produktu>': 'klíč,klíč,…' } – nahradí celé pole výrobku (max. 6 ikon)
   Přiřazení složek (ke-ikony-v4-slozky.js): složka v názvu nebo v sekcích Hlavní benefity / Hlavní účinné složky /
   Aktivní složky / Přednosti… ; u kosmetiky navíc musí být latinsky v INCI (ne jen vůně); u doplňků a potravin
   v názvu nebo v českém složení (u potravin jen hlavní složka – mezi prvními 3 nebo s %); bez parfémů, vůní
   do domácnosti, drogerie a úklidu; max. 2 složky na výrobek, řazení za ikony „složení a vlastnosti“ (vegan, bez…),
   celkem max. 6 (při přebytku odpadnou poslední = nejméně důležité).
   Použití v prohlížeči: keIkonyPatch4(textV3, glyfy, ikony, set) → textV4 */
function keIkonyPatch4(src, glyfy, ikony, set) {
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
  Object.keys(set).forEach(function (id) {
    var ks = set[id].split(',');
    if (ks.length > 6) throw new Error('víc než 6 ikon u ' + id);
    ks.forEach(function (k) { if (!ic.v[k]) throw new Error('neznámá ikona ' + k + ' u ' + id); });
    p.v[id] = set[id];
  });
  put(p, p.v);

  once('/* ke-ikony-v3.js – ', '/* ke-ikony-v4.js – ');
  once('nové ikony Péče o vousy a Domácí jogurt. */',
    'nové ikony Péče o vousy a Domácí jogurt.\n' +
    '   v4 (21. 10. 2026): 44 ikon složek (byliny, oleje, vitaminy, minerály, aktivní látky) u výrobků, které je opravdu obsahují; ikony výrobků JUST 5574, 5580, 5381. */');
  return src;
}
