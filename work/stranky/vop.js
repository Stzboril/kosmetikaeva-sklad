/* Převod obchodních podmínek do vzhledu ke-vop. Text zůstává beze změny, mění se jen struktura (a velikost písmen v nadpisech). */
window.keVopTransform = function (raw, lang) {
  var loc = lang === 'sk' ? 'sk' : 'cs';
  var d = new DOMParser().parseFromString('<div id="r">' + raw + '</div>', 'text/html');
  var root = d.getElementById('r');
  var sentence = function (s) { s = s.replace(/\s+/g, ' ').trim().toLocaleLowerCase(loc); return s.charAt(0).toLocaleUpperCase(loc) + s.slice(1); };
  /* stavy zboží jako štítky */
  [].slice.call(root.querySelectorAll('span[style]')).forEach(function (sp) {
    if (!/color/i.test(sp.getAttribute('style'))) return;
    var t = sp.textContent.trim().toUpperCase(), cls = 'ke-vop-stav';
    if (/^SKLADEM$/.test(t)) cls += ' ke-vop-stav--ok';
    else if (/(PRODEJ|PREDAJ) SKON/.test(t)) cls += ' ke-vop-stav--konec';
    sp.removeAttribute('style'); sp.className = cls;
  });
  var nodes = [].slice.call(root.childNodes).filter(function (n) { return !(n.nodeType === 3 && !n.textContent.trim()) && n.nodeType !== 8 && !(n.nodeType === 1 && n.tagName === 'STYLE'); });
  var out = [], toc = [], intro = 0, mode = 'intro', appendix = null;
  var split = function (html) {
    var res = [], last = 'b';
    html.split(/<br\s*\/?>/i).forEach(function (seg) {
      seg.split(/(?:\s|&nbsp;){2,}(?=[a-h]\)(?:\s|&nbsp;))/).forEach(function (t) {
        t = t.replace(/^(?:\s|&nbsp;)+|(?:\s|&nbsp;)+$/g, '');
        if (!t) return;
        var m = t.match(/^(\d+\.\d+\.?)(?:\s|&nbsp;)+([\s\S]*)$/);
        if (m) { res.push('<p class="ke-vop-b"><b class="ke-vop-c">' + m[1] + '</b> ' + m[2] + '</p>'); last = 'b'; return; }
        m = t.match(/^([a-h]\))(?:\s|&nbsp;)+([\s\S]*)$/);
        if (m) { res.push('<p class="ke-vop-p"><b class="ke-vop-c">' + m[1] + '</b> ' + m[2] + '</p>'); last = 'p'; return; }
        res.push('<p class="ke-vop-' + last + ' ke-vop-dal">' + t + '</p>');
      });
    });
    return res.join('\n');
  };
  var closeAppendix = function () { if (appendix) { out.push('</section>'); appendix = null; } };
  nodes.forEach(function (n) {
    if (n.nodeType !== 1) { out.push(n.textContent); return; }
    var tag = n.tagName, txt = n.textContent.replace(/\s+/g, ' ').trim();
    if (tag === 'H2' && mode === 'intro') return; /* duplicitní nadpis – stránka má vlastní H1 */
    var m;
    if (tag === 'H3' && (m = txt.match(/^(\d+)\.\s*(.+)$/))) {
      closeAppendix(); mode = 'clanek';
      var h = sentence(m[2]);
      toc.push('<li><a href="#cl-' + m[1] + '"><span>' + m[1] + '</span>' + h + '</a></li>');
      out.push('<h2 class="ke-vop-h" id="cl-' + m[1] + '"><span class="ke-vop-n">' + m[1] + '</span>' + h + '</h2>');
      return;
    }
    if (tag === 'H3' && (m = txt.match(/^(PŘÍLOHA|PRÍLOHA)\s+Č\.\s*(\d+)\s*[-–]\s*(.+)$/i))) {
      closeAppendix(); mode = 'priloha';
      var nm = sentence(m[1] + ' č. ' + m[2]).replace(/ č\. /, ' č. ') + ' – ' + sentence(m[3]);
      toc.push('<li><a href="#priloha-' + m[2] + '"><span>P' + m[2] + '</span>' + nm + '</a></li>');
      out.push('<section class="ke-vop-priloha" id="priloha-' + m[2] + '">\n<h2>' + nm + '</h2>');
      appendix = m[2];
      return;
    }
    if (tag === 'H4') { out.push('<h3>' + n.innerHTML + '</h3>'); return; }
    if (mode === 'intro' && tag === 'P') {
      out.push(intro === 0 ? '<div class="ke-box ke-vop-uvod"><p>' + n.innerHTML + '</p></div>' : n.outerHTML);
      intro++;
      return;
    }
    if (mode === 'clanek' && tag === 'P') { out.push(split(n.innerHTML)); return; }
    out.push(n.outerHTML);
  });
  closeAppendix();
  var obsahT = 'Obsah';
  var html = '<div class="ke-clanek ke-info ke-vop">\n' + out.slice(0, 0).join('') +
    out.join('\n').replace(/^/, '') + '\n</div>\n';
  /* obsah vložit za úvod (za poslední úvodní odstavec, před první článek) */
  var first = html.indexOf('<h2 class="ke-vop-h"');
  html = html.slice(0, first) + '<nav class="ke-vop-obsah" id="obsah"><span class="ke-box-titulek">' + obsahT + '</span><ol>' + toc.join('') + '</ol></nav>\n' + html.slice(first);
  return html;
};
/* kontrola: text bez nadpisů musí být stejný (bez mezer), nadpisy stejné bez ohledu na velikost písmen */
window.keVopCheck = function (raw, html, lang) {
  var loc = lang === 'sk' ? 'sk' : 'cs';
  var P = function (h) { return new DOMParser().parseFromString('<div id="r">' + h + '</div>', 'text/html').getElementById('r'); };
  var a = P(raw), b = P(html);
  [].slice.call(a.querySelectorAll('style')).forEach(function (e) { e.remove(); });
  var ah = [].slice.call(a.querySelectorAll('h2,h3')).map(function (e) { var t = e.textContent; e.remove(); return t; });
  var nav = b.querySelector('.ke-vop-obsah'); if (nav) nav.remove();
  var bh = [].slice.call(b.querySelectorAll('h2')).map(function (e) { var t = e.textContent; e.remove(); return t; });
  var norm = function (s) { return s.replace(/[\s ]+/g, ''); };
  var hn = function (s) { return norm(s).toLocaleLowerCase(loc).replace(/^\d+\./, '').replace(/^\d+/, ''); };
  var ta = norm(a.textContent), tb = norm(b.textContent);
  var diff = -1; for (var i = 0; i < Math.max(ta.length, tb.length); i++) if (ta[i] !== tb[i]) { diff = i; break; }
  return { textSame: ta === tb, diffAt: diff, around: diff < 0 ? '' : [ta.slice(diff - 40, diff + 40), tb.slice(diff - 40, diff + 40)],
    heads: ah.length + '/' + bh.length,
    headsSame: JSON.stringify(ah.slice(1).map(function (x) { return hn(x).replace(/-/g, '–'); })) === JSON.stringify(bh.map(hn)),
    hA: ah.slice(1).map(function (x) { return hn(x).replace(/-/g, '–'); }), hB: bh.map(hn) };
};
'ok';
