/* Úprava ke-ikony-v7.js → ke-ikony-v8.js (23. 10. 2026, majitel: „taky udělej ikony, klidně i další vymysli“
   k novému výrobku Just Infiore Ultra-regenerační pleťové sérum 30 ml, id 11456).
   - 4 nové glyfy a ikony složek (v8-glyfy.json, v8-ikony.json; generátor v8-glyfy.py):
     s_protez Protěž alpská / Plesnivec alpínsky, s_alpruze Alpská růže / Alpská ruža,
     s_bakuch Bakuchiol, s_acmella Acmella – popisek „Obsahuje …“
   - přiřazení jako ve v4: složka v názvu, nebo v sekcích hlavních složek/benefitů A latinsky v INCI
     (jen INCI nestačí – 9215 protěž, 7696 alpská růže, 10072 acmella vynechány; sada 10525 bez INCI vynechána);
     původ (ch) vždy první, nejvýš 6 ikon.
   Použití v prohlížeči: keIkonyPatch8(textV7, glyfy, ikony) → textV8 */
function keIkonyPatch8(src, glyfy, ikony) {
  // id produktu: [nové ikony, očekávané dosavadní ikony]
  var set = {
    '11456': ['ch,s_protez,s_alpruze,s_bakuch,s_acmella,v_c', undefined], // Just Infiore sérum (nový)
    '7702': ['ch,s_protez,s_alpruze,s_bakuch,s_acmella,v_c', 'ch,d_plet'],   // Just VJ Sérum
    '7609': ['ch,s_protez', 'ch'],                                          // Gel po holení s protěží
    '7753': ['ch,s_protez,d_telo', 'ch,d_telo'],                            // Deo roll-on s protěží
    '7669': ['ch,s_protez,s_alpruze,s_hyal,v_c,d_plet', 'ch,s_hyal,v_c,d_plet'],          // VJ 24h krém
    '7672': ['ch,s_protez,s_alpruze,s_mandle,s_shea,d_plet', 'ch,s_mandle,s_shea,d_plet'], // VJ Čisticí krém
    '7687': ['ch,s_protez,s_alpruze,s_hyal,s_panth,d_plet', 'ch,s_hyal,s_panth,d_plet'],  // VJ Maska
    '7693': ['ch,s_protez,s_alpruze,s_levan,v_c,d_plet', 'ch,s_levan,v_c,d_plet'],        // VJ Noční krém
    '9657': ['ch,s_protez,s_alpruze,v_c,s_panth,d_plet', 'ch,v_c,s_panth,d_plet'],        // VJ Denní krém
    '7696': ['ch,s_protez,s_ruze,s_sipek,p_zeny,d_plet', 'ch,s_ruze,s_sipek,p_zeny,d_plet'], // VJ Odličovač
    '8715': ['ch,s_mentol,s_shea,s_protez,s_alpruze', 'ch,s_mentol,s_shea'],             // Alpský bylinný balzám
    '7618': ['ch,s_arnika,s_shea,s_protez', 'ch,s_arnika,s_shea'],                       // Appenzellský bylinný krém
    '8399': ['ch,s_arnika,s_panth,s_protez', 'ch,s_arnika,s_panth'],                     // Alpská koupel
    '9088': ['ch,s_sipek,s_jojoba,s_protez,d_opal', 'ch,s_sipek,s_jojoba,d_opal'],       // Balzám po opalování
    '9454': ['ch,s_panth,v_c,s_protez,d_opal', 'ch,s_panth,v_c,d_opal'],                 // Opalovací mléko SPF 50
    '9460': ['ch,s_panth,s_shea,s_protez,d_opal', 'ch,s_panth,s_shea,d_opal'],           // Opalovací krém SPF 30
    '9774': ['ch,s_panth,s_protez', 'ch,s_panth'],                                       // Dárková sada Pro něj
    '10411': ['s_bakuch,v_e,s_argan,d_plet', 'v_e,s_argan,d_plet'],                      // Essens sérum s bakuchiolem LE
    '10549': ['s_bakuch,s_argan,s_jojoba,d_plet', 's_argan,s_jojoba,d_plet']             // Essens sérum s bakuchiolem
  };
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
    var nove = set[id][0], stare = set[id][1];
    if (p.v[id] !== stare) throw new Error('výrobek ' + id + ' má jiné ikony: ' + p.v[id]);
    var ks = nove.split(',');
    if (ks.length > 6) throw new Error('víc než 6 ikon u ' + id);
    ks.forEach(function (k) { if (!ic.v[k]) throw new Error('neznámá ikona ' + k + ' u ' + id); });
    p.v[id] = nove;
  });
  put(p, p.v);

  once('/* ke-ikony-v7.js – ', '/* ke-ikony-v8.js – ');
  once('   v7 (21. 10. 2026): Nahrin Vitamin D3 Complex (9364) + Bez lepku, Bez laktózy. */',
    '   v7 (21. 10. 2026): Nahrin Vitamin D3 Complex (9364) + Bez lepku, Bez laktózy.\n' +
    '   v8 (23. 10. 2026): nové ikony Protěž alpská, Alpská růže, Bakuchiol, Acmella; Just Infiore sérum (11456) a 18 výrobků JUST/Essens s těmito složkami. */');
  return src;
}
