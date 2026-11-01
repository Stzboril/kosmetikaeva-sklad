// ke-ikony-v24.js = živý ke-ikony-v23.js + ikony 31 nových výrobků LR (1. 11. 2026, majitel: „ano dopln vše“)
// Výsledek: 201 232 B, SHA-256 61c224bb723dd39ae8d37f413f97162dc2396d21772dd56282c8b4ae7e1d1212
// Zavaděč v zápatí HTML kódů: ke-ikony-v24.js?v=1 (záloha localStorage keHtmlKodyBackup_20261101_ikony24).
// Návrat = zpět na ke-ikony-v23.js?v=1. Další verze = ke-ikony-v25.js.
// Pravidla: jen podle popisu/složení výrobce (u výrobků bez INCI podle obalu), původ „de“ vždy první, max. 6, žádný glyf 2×.
const KE_IKONY_V24_NOVE = {"11567":"de,d_plet,s_levan,s_jojoba,s_shea,s_hyal","11570":"de,aloe,p_deti,d_mydlo,u_hydr","3459":"de,aloe,s_mesic,s_panth,v_e,d_ruce","11573":"de,aloe,s_argan,s_oliva,s_shea,d_plet","11576":"de,aloe,u_hydr,d_plet","11579":"de,s_med,s_shea,s_mandle,u_vyz,d_telo","11582":"de,s_med,u_relax,d_telo","11585":"de,s_med,d_mydlo,u_zjem","11588":"de,s_med,s_jojoba,v_e,u_vyz,d_ruce","11591":"de,aloe,s_sipek,u_vyz,d_telo","11594":"de,aloe,s_sipek,u_vyz,d_ruce,d_nohy","11597":"de,v_pan,d_vlasy,d_sprcha","11600":"de,v_dam,d_telo","11603":"de,aloe,s_panth,p_deti,d_sprcha,d_mydlo","11606":"de,aloe,s_argan,s_oliva,u_hydr,d_plet","11609":"de,s_med,s_shea,s_mandle,u_relax,d_telo","11612":"de,aloe,s_sipek,u_vyz,d_telo,d_nohy","11615":"de,s_hyal,s_peptid,d_plet","11618":"de,d_plet,v_c,v_b,s_argan,s_rasy","11621":"de,d_plet,c_zrala,s_peptid,s_jojoba,s_rakyt","11624":"de,d_plet,s_jojoba,s_shea,s_hyal,u_hydr","11627":"de,bezbarv,s_reva,s_sipek,s_rakyt,d_dopl","11630":"de,m_zn,m_mg,f_kaps,d_dopl","11633":"de,aloe,s_med,f_gel,d_dopl,d_ruce","11636":"de,aloe,f_gel,d_dopl,d_ruce","11639":"de,aloe,s_med,f_gel,d_dopl,d_ruce","11642":"de,aloe,s_kolag,v_c,f_gel,d_ruce","11645":"de,aloe,s_zazvor,s_med,f_gel,d_ruce","11648":"de,v_pan,t_edp,t_sada,d_sprcha","11651":"de,v_dam,t_edp,t_sada,d_telo","11654":"de,f_kaps,f_gel,aloe,m_zn,d_dopl"};
function keIkonyPatch24(textV23) {
  const i = textV23.indexOf('var P'); let j = textV23.indexOf('=', i) + 1; while (/\s/.test(textV23[j])) j++;
  let d = 0, k = j, s = false, e = false;
  for (; k < textV23.length; k++) { const c = textV23[k]; if (s) { if (e) e = false; else if (c === '\\') e = true; else if (c === '"') s = false; continue; }
    if (c === '"') s = true; else if (c === '{' || c === '[') d++; else if (c === '}' || c === ']') { d--; if (d === 0) { k++; break; } } }
  const P = Object.assign({}, JSON.parse(textV23.slice(j, k)), KE_IKONY_V24_NOVE);
  return (textV23.slice(0, j) + JSON.stringify(P) + textV23.slice(k)).replace('/* ke-ikony-v23.js',
    '/* ke-ikony-v24.js – v24 (1. 11. 2026): = v23 + ikony 31 nových výrobků LR (id 3459, 11567–11654) podle popisů a složení výrobce, původ „de“ vždy první; návrat = v23\n   ke-ikony-v23.js');
}
