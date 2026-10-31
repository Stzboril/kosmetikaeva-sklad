/* KosmetikaEva.eu – našeptávač a kontrola adresy z Mapy.com (v1, 31. 10. 2026)
   Běží jen v pokladně, krok 2 (/objednavka/krok-2/, /sk/objednavka/krok-2/), a jen když je zvolené doručení kurýrem.
   - Ulice / číslo domu: od 3. znaku a po pauze 300 ms nabídne skutečné adresy (Mapy.com Suggest, 4 kredity/dotaz),
     po výběru doplní ulici, číslo, město a PSČ. Fakturační i dodací adresa.
   - Když zákazník návrh nevybere, po vyplnění adresy ji ověří (Geocode) a když ji nenajde, ukáže upozornění.
     Objednávku nikdy neblokuje.
   - API klíč: window.KE_MAPY_KEY (vkládá majitel v HTML kódech). Bez klíče skript nic nedělá.
   - Logo Mapy.com pod návrhy (podmínka Mapy.com). Návrat = v zápatí HTML kódů odebrat zavaděč ke-adresy. */
(function () {
  if (window.__keAdresy) return; window.__keAdresy = 1;
  if (!/\/objednavka\/krok-2\//.test(location.pathname)) return;
  var SK = /^sk/i.test(document.documentElement.lang || '') || /^\/sk\//.test(location.pathname);
  var T = SK ? {
    warn: 'Túto adresu sme na mape nenašli. Skontrolujte prosím ulicu, číslo domu, mesto a PSČ – kuriér podľa nej doručuje.',
    ok: 'Adresa overená', none: 'Žiadna zhoda – pokračujte v písaní', by: 'Adresy z'
  } : {
    warn: 'Tuto adresu jsme na mapě nenašli. Zkontrolujte prosím ulici, číslo domu, město a PSČ – kurýr podle ní doručuje.',
    ok: 'Adresa ověřena', none: 'Nic jsme nenašli – pište dál', by: 'Adresy z'
  };
  var API = 'https://api.mapy.com/v1/';
  var LOGO = 'https://api.mapy.com/img/api/logo.svg';
  var cache = {}, ctrl = null, timer = null, vtimer = null, box = null, activeGroup = null, items = [], sel = -1;
  var verified = { bill: '', delivery: '' };

  function key() { return window.KE_MAPY_KEY || ''; }
  function $(id) { return document.getElementById(id); }
  function courier() {
    try {
      var dl = window.dataLayer || [];
      for (var i = dl.length - 1; i >= 0; i--) {
        var e = dl[i], o = e && (e[2] || e);
        if (o && typeof o.shipping_tier === 'string') return /kur[ýy]r|kuri[ée]r/i.test(o.shipping_tier);
      }
    } catch (e) {}
    var r = document.querySelector('.order-recapitulation, .order-summary, #summary-box') || document.body;
    return /Doručení kurýrem|Doručenie kuriérom|kurýrem na adresu|kuriérom na adresu/i.test(r.textContent || '');
  }
  function F(g) {
    var p = g === 'bill' ? 'bill' : 'delivery';
    return { street: $(p + 'Street'), num: $(p + 'HouseNumber'), city: $(p + 'City'), zip: $(p + 'Zip') };
  }
  function country() {
    var s = $('billCountryId'), v = s ? String(s.value) : '';
    if (v === '151') return 'sk';
    if (v === '43') return 'cz';
    return SK ? 'sk' : 'cz';
  }
  function usedGroup() { var a = $('another-shipping'); return a && a.checked ? 'delivery' : 'bill'; }
  function fmtZip(z) { var d = String(z || '').replace(/\D/g, ''); return d.length === 5 ? d.slice(0, 3) + ' ' + d.slice(3) : String(z || ''); }
  function setVal(el, v) {
    if (!el) return;
    var proto = Object.getOwnPropertyDescriptor(HTMLInputElement.prototype, 'value');
    proto.set.call(el, v);
    el.dispatchEvent(new Event('input', { bubbles: true }));
    el.dispatchEvent(new Event('change', { bubbles: true }));
    el.dispatchEvent(new Event('blur', { bubbles: true }));
  }
  function parts(it) {
    var rs = it.regionalStructure || [], o = {};
    for (var i = 0; i < rs.length; i++) { var t = rs[i].type; if (!o[t]) o[t] = rs[i].name; }
    var num = o['regional.address'] || '';
    var street = o['regional.street'] || o['regional.municipality_part'] || o['regional.municipality'] || '';
    return { street: street, num: num, city: o['regional.municipality'] || '', zip: fmtZip(it.zip), part: o['regional.municipality_part'] || '' };
  }
  function api(path, q, signal) {
    var u = API + path + '?' + new URLSearchParams({ query: q, lang: SK ? 'sk' : 'cs', limit: '6', type: 'regional.address', locality: country() });
    return fetch(u, { headers: { 'X-Mapy-Api-Key': key() }, signal: signal }).then(function (r) { return r.ok ? r.json() : { items: [] }; });
  }
  function css() {
    if ($('ke-adr-css')) return;
    var s = document.createElement('style'); s.id = 'ke-adr-css';
    s.textContent =
      '.ke-adr{position:absolute;z-index:9999;background:#fff;border:1px solid #e3d9dc;border-radius:14px;box-shadow:0 10px 30px rgba(28,27,41,.12);overflow:hidden;font:14px/1.35 Montserrat,system-ui,sans-serif}' +
      '.ke-adr__i{padding:10px 14px;cursor:pointer;border-bottom:1px solid #f3eef0}.ke-adr__i:last-of-type{border-bottom:0}' +
      '.ke-adr__i b{display:block;font-weight:600;color:#1c1b29}.ke-adr__i span{color:#6e6c7a;font-size:12.5px}' +
      '.ke-adr__i.on,.ke-adr__i:hover{background:#faf2f0}' +
      '.ke-adr__n{padding:10px 14px;color:#6e6c7a;font-size:13px}' +
      '.ke-adr__f{display:flex;align-items:center;justify-content:flex-end;gap:6px;padding:6px 12px;background:#faf7f6;color:#8a8796;font-size:11px}' +
      '.ke-adr__f img{height:14px;width:auto;display:block}' +
      '.ke-adr-w{margin:8px 0 4px;padding:10px 14px;border-radius:14px;background:#fff4e5;border:1px solid #f1d29c;color:#6b4a0f;font-size:13.5px;line-height:1.4}' +
      '.ke-adr-ok{margin:6px 0 2px;color:#1d7a3a;font-size:12.5px}';
    (document.head || document.documentElement).appendChild(s);
  }
  function close() { if (box) box.remove(); box = null; items = []; sel = -1; }
  function render(group, anchor, list) {
    css(); close(); activeGroup = group; items = list;
    box = document.createElement('div'); box.className = 'ke-adr'; box.setAttribute('role', 'listbox');
    var h = '';
    if (!list.length) h += '<div class="ke-adr__n">' + T.none + '</div>';
    for (var i = 0; i < list.length; i++) {
      var p = parts(list[i]);
      h += '<div class="ke-adr__i" role="option" data-i="' + i + '"><b>' + esc(list[i].name) + '</b><span>' + esc([p.zip, p.city + (p.part && p.part !== p.city ? ' – ' + p.part : '')].filter(Boolean).join(' ')) + '</span></div>';
    }
    h += '<div class="ke-adr__f">' + T.by + ' <a href="https://mapy.com/" target="_blank" rel="noopener"><img src="' + LOGO + '" alt="Mapy.com"></a></div>';
    box.innerHTML = h;
    var r = anchor.getBoundingClientRect();
    box.style.left = (r.left + window.scrollX) + 'px';
    box.style.top = (r.bottom + window.scrollY + 4) + 'px';
    box.style.width = Math.max(r.width, Math.min(360, window.innerWidth - 24)) + 'px';
    if (r.left + parseFloat(box.style.width) > window.innerWidth - 8) box.style.left = Math.max(8, window.innerWidth - 8 - parseFloat(box.style.width)) + window.scrollX + 'px';
    document.body.appendChild(box);
    box.addEventListener('mousedown', function (e) {
      var el = e.target.closest('.ke-adr__i'); if (!el) return;
      e.preventDefault(); pick(+el.getAttribute('data-i'));
    });
  }
  function esc(s) { return String(s == null ? '' : s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  function pick(i) {
    var it = items[i]; if (!it) return;
    var f = F(activeGroup), p = parts(it);
    setVal(f.street, p.street); setVal(f.num, p.num); setVal(f.city, p.city); setVal(f.zip, p.zip);
    verified[activeGroup] = sig(activeGroup);
    close(); showWarn(activeGroup, false, true);
  }
  function sig(g) { var f = F(g); return [f.street, f.num, f.city, f.zip].map(function (e) { return e ? e.value.trim().toLowerCase() : ''; }).join('|'); }
  function query(g) {
    var f = F(g);
    return [f.street && f.street.value, f.num && f.num.value, f.city && f.city.value].map(function (s) { return (s || '').trim(); }).filter(Boolean).join(' ');
  }
  function suggest(g, anchor) {
    clearTimeout(timer);
    var q = query(g);
    var f = F(g);
    if (!key() || !courier() || !f.street || f.street.value.trim().length < 3) { close(); return; }
    timer = setTimeout(function () {
      var ck = country() + '|' + q.toLowerCase();
      if (cache[ck]) { render(g, anchor, cache[ck]); return; }
      if (ctrl) ctrl.abort();
      ctrl = window.AbortController ? new AbortController() : null;
      api('suggest', q, ctrl && ctrl.signal).then(function (j) {
        var list = (j.items || []).filter(function (x) { return x.type === 'regional.address'; });
        cache[ck] = list;
        if (document.activeElement === anchor) render(g, anchor, list);
      }).catch(function () {});
    }, 300);
  }
  function warnEl(g) {
    var f = F(g), host = f.zip && (f.zip.closest('fieldset') || f.zip.parentNode);
    if (!host) return null;
    var id = 'ke-adr-w-' + g, el = $(id);
    if (!el) { el = document.createElement('div'); el.id = id; host.appendChild(el); }
    return el;
  }
  function showWarn(g, bad, ok) {
    var el = warnEl(g); if (!el) return;
    el.className = bad ? 'ke-adr-w' : (ok ? 'ke-adr-ok' : '');
    el.textContent = bad ? T.warn : (ok ? '✓ ' + T.ok : '');
  }
  function validate(g) {
    clearTimeout(vtimer);
    vtimer = setTimeout(function () {
      if (!key() || !courier() || g !== usedGroup()) { showWarn(g, false, false); return; }
      var f = F(g);
      var v = { street: f.street && f.street.value.trim(), num: f.num && f.num.value.trim(), city: f.city && f.city.value.trim(), zip: f.zip && f.zip.value.replace(/\D/g, '') };
      if (!v.street || !v.num || !v.city || v.zip.length !== 5) { showWarn(g, false, false); return; }
      var s = sig(g);
      if (verified[g] === s) { showWarn(g, false, true); return; }
      var q = v.street + ' ' + v.num + ', ' + fmtZip(v.zip) + ' ' + v.city;
      api('geocode', q).then(function (j) {
        if (sig(g) !== s) return;
        var nNum = v.num.toLowerCase().replace(/\s/g, '');
        var hit = (j.items || []).some(function (it) {
          if (it.type !== 'regional.address') return false;
          var p = parts(it), pn = String(p.num).toLowerCase().replace(/\s/g, '');
          var numOk = pn === nNum || pn.split('/').indexOf(nNum) >= 0 || nNum.split('/').indexOf(pn) >= 0;
          var zipOk = String(it.zip || '').replace(/\D/g, '') === v.zip;
          var cityOk = p.city.toLowerCase() === v.city.toLowerCase() || (p.part && p.part.toLowerCase() === v.city.toLowerCase());
          return numOk && (zipOk || cityOk);
        });
        if (hit) verified[g] = s;
        showWarn(g, !hit, hit);
      }).catch(function () { showWarn(g, false, false); });
    }, 900);
  }
  function groupOf(el) {
    if (!el || !el.id) return null;
    if (/^bill(Street|HouseNumber|City|Zip)$/.test(el.id)) return 'bill';
    if (/^delivery(Street|HouseNumber|City|Zip)$/.test(el.id)) return 'delivery';
    return null;
  }
  document.addEventListener('input', function (e) {
    var g = groupOf(e.target); if (!g) return;
    if (e.isTrusted && !e.inputType) return; /* automatické vyplnění prohlížeče – nenašeptávat */
    if (/Street$|HouseNumber$/.test(e.target.id) && e.isTrusted) suggest(g, e.target);
    if (verified[g] && verified[g] !== sig(g)) verified[g] = '';
    validate(g);
  }, true);
  document.addEventListener('change', function (e) {
    var g = groupOf(e.target); if (g) validate(g);
    if (e.target && (e.target.id === 'another-shipping' || e.target.id === 'billCountryId')) { close(); validate('bill'); validate('delivery'); }
  }, true);
  document.addEventListener('keydown', function (e) {
    if (!box || groupOf(e.target) === null) return;
    var n = box.querySelectorAll('.ke-adr__i');
    if (e.key === 'ArrowDown' || e.key === 'ArrowUp') {
      e.preventDefault(); if (!n.length) return;
      sel = (sel + (e.key === 'ArrowDown' ? 1 : -1) + n.length) % n.length;
      for (var i = 0; i < n.length; i++) n[i].classList.toggle('on', i === sel);
    } else if (e.key === 'Enter' && sel >= 0) { e.preventDefault(); pick(sel); }
    else if (e.key === 'Escape') close();
  }, true);
  document.addEventListener('focusout', function (e) { if (groupOf(e.target)) setTimeout(function () { if (box && !box.contains(document.activeElement)) close(); }, 150); }, true);
  window.addEventListener('resize', close);
  /* po načtení zkontrolovat už vyplněnou adresu (přihlášený zákazník) */
  setTimeout(function () { validate(usedGroup()); }, 1500);
})();
