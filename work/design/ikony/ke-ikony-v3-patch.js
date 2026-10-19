/* Úprava ke-ikony-v2.js → ke-ikony-v3.js (19. 10. 2026, majitel: „tady ti taky chybí ikony, projdi celý eshop a doplň ikony všude“).
   Zdroj je živý soubor na webu (data jsou uvnitř), tento skript ho jen upraví:
   - ikony se zobrazí i u vyprodaného zboží: v2 je vkládala jen k tlačítku „Vložit do košíku“, které u vyprodaného
     zboží chybí (místo něj je hlídací pes) → teď stačí spodní část nákupního boxu (.bottom); ikony jdou pod tlačítko
     hlídacího psa, je-li tam
   - ikony pro 21 viditelných výrobků, které žádné neměly (20 Essens, 1 Eurona); dárkové poukazy záměrně bez ikon
   - nové ikony „Péče o vousy“ (glyf beard = knír a bradka) a „Domácí jogurt“ (glyf yogurt = sklenička s víčkem)
   Použití v prohlížeči: keIkonyPatch3(textV2) → textV3. */
function keIkonyPatch3(src) {
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
  /* knír (souměrný podle x = 12); bradka pod ním vypadala jako úsměv → jen knír */
  gl.v.beard = {
    f: 'M12 10.6c1.2-1.5 3.4-2 5.2-1 1.4.8 2.2 2.4 3.6 2.6.6.1 1.1-.1 1.5-.6.1 1.9-1.2 3.6-3.2 3.9-2.4.4-4.6-1-5.9-2.4-.4-.4-.8-.6-1.2-.6s-.8.2-1.2.6c-1.3 1.4-3.5 2.8-5.9 2.4-2-.3-3.3-2-3.2-3.9.4.5.9.7 1.5.6 1.4-.2 2.2-1.8 3.6-2.6 1.8-1 4-.5 5.2 1z',
    h: 'M3.6 11.6c1.3-.3 2.2-1.6 3.4-2.2l.3.5c-1.2.7-2.1 2-3.5 2.3z'
  };
  /* sklenička jogurtu s víčkem, světlý vlnitý pruh = jogurt */
  gl.v.yogurt = {
    f: 'M6 9h12v9.5a2.5 2.5 0 0 1-2.5 2.5h-7A2.5 2.5 0 0 1 6 18.5z',
    s: 'M5.2 5.5h13.6a.8.8 0 0 1 .8.8V9H4.4V6.3a.8.8 0 0 1 .8-.8z',
    h: 'M7.3 10.4h1v7.8h-1z',
    c: 'M8.2 13.4c1.3-1.2 2.6-1.2 3.8 0s2.5 1.2 3.8 0v1.7c-1.3 1.2-2.5 1.2-3.8 0s-2.5-1.2-3.8 0z'
  };
  put(gl, gl.v);

  var ic = block('IC');
  ic.v.vousy = ['beard', 'Péče o vousy', 'Starostlivosť o bradu',
    'Výrobek na péči o vousy a knír.', 'Výrobok na starostlivosť o bradu a fúzy.'];
  ic.v.jogurt = ['yogurt', 'Domácí jogurt', 'Domáci jogurt',
    'K přípravě domácího jogurtu.', 'Na prípravu domáceho jogurtu.'];
  put(ic, ic.v);

  var p = block('P');
  var add = {
    '6281': 'jogurt,f_sacky',                         // Colostrum probiotika 6 ks (sáčky na domácí jogurt)
    '6335': 'f_gel', '6338': 'f_gel',                 // Collagen / Collagen FISH měsíční kúra (ovocný gel)
    '6347': 'f_gel', '6350': 'f_gel',                 // Collagen / Collagen FISH týdenní kúra
    '6518': 'jogurt',                                 // Jogurtovač
    '7183': 'aloe,u_ukl,u_hydr,p_muzi,d_plet',        // Aloe Vera Balzám po holení (zklidňuje a hydratuje)
    '7186': 'aloe,u_ukl,u_osv,u_vyz,p_muzi,d_plet',   // Aloe Vera Pěna na holení (zklidňuje, vyživuje, mentol osvěží)
    '7276': 'vegan,bezpar,aloe,u_hydr,u_ukl,d_telo',  // Aloe Vera Soft Spray („Vegan složení – bez parabenů“)
    '8232': 'vegan,bezpar,aloe,u_hydr,u_ukl,d_telo',  // Aloe Vera Soft Spray Plus („Veganský produkt bez parabenů“)
    '10642': 'aloe,u_hydr,p_deti,d_telo',             // Set Soft Spray 3 × 100 ml (i sprej pro děti)
    '9487': 'd_parfprani',                            // Eurona Vianelle Parfém na praní
    '10312': 'vousy,u_hydr,u_ukl,p_muzi',             // Šampon na vousy
    '10315': 'vousy,u_hydr,p_muzi',                   // Sada pro péči o vousy
    '10318': 'vousy,u_vyz,u_hydr,p_muzi',             // Vosk na vousy a knír
    '10405': 'd_esolej,d_telo',                       // Set Eucassens + Tymiánový krém
    '10408': 'f_kaps',                                // Vitassens Balance Duo (kapsle)
    '10414': 'f_kaps',                                // Elastir 30 tobolek
    '10516': 'f_gel,f_kaps', '10519': 'f_gel,f_kaps', // Skin Renewal Duo (Fish): kolagen v gelu + Elastir tobolky
    '10750': 'jogurt,f_sacky'                         // Set Colostrum Probiotics s jogurtovačem
  };
  Object.keys(add).forEach(function (id) {
    if (p.v[id]) throw new Error('výrobek už ikony má: ' + id);
    add[id].split(',').forEach(function (k) { if (!ic.v[k]) throw new Error('neznámá ikona ' + k + ' u ' + id); });
    p.v[id] = add[id];
  });
  put(p, p.v);

  /* vložení i bez tlačítka „Vložit do košíku“ (vyprodané zboží) */
  once("    if (!box || !btn) return false;",
    "    var bot = null;\n" +
    "    if (box) for (var b = 0; b < box.children.length; b++) if (box.children[b].classList.contains('bottom')) bot = box.children[b];\n" +
    "    if (!box || (!btn && !(bot && (force || document.querySelector('tr.sold-out') || document.querySelector('.p-info-wrapper .watchdog'))))) return false;");
  once("  function place() {", "  function place(force) {");
  once("    var anchor = bottom || btn.closest('.add-to-cart') || null;",
    "    var wd = null;\n" +
    "    for (i = 0; i < box.children.length; i++) if (box.children[i].classList.contains('ke-wd')) wd = box.children[i];\n" +
    "    var anchor = wd || bottom || (btn && btn.closest('.add-to-cart')) || null;");
  once("(function tryPlace() { if (!place() && ++tries < 60) setTimeout(tryPlace, 250); })();",
    "(function tryPlace() { if (!place(tries >= 20) && ++tries < 60) setTimeout(tryPlace, 250); })();");

  once('/* ke-ikony-v2.js – ', '/* ke-ikony-v3.js – ');
  once('text na obvodu dál od vnitřního kruhu. */',
    'text na obvodu dál od vnitřního kruhu.\n' +
    '   v3 (19. 10. 2026): ikony i u vyprodaného zboží (pod tlačítkem hlídacího psa), ikony 21 výrobků Essens/Eurona, nové ikony Péče o vousy a Domácí jogurt. */');
  return src;
}
