/* KosmetikaEva.eu – pruh „Podobné výrobky“ v okně „Přidáno do košíku“ (v1, 31. 10. 2026)
   Majitel 31. 10.: „přidat ještě pruh pod to, s výrobky, které jsou podobné (tedy ne související)“.
   - Po otevření okna (událost ShoptetDOMAdvancedOrderLoaded) ukáže až 8 Podobných výrobků přidaného zboží.
   - Zdroj = záložka „Podobné“ na detailu výrobku (#productsAlternative): na detailu se čte přímo ze stránky,
     jinde (výpis kategorie, úvod) se detail přidaného výrobku jednou načte a uloží do paměti stránky.
   - Vynechá přidaný výrobek a výrobky, které okno už ukazuje (Související = příslušenství).
   - Tlačítko „Do košíku“ používá standardní formulář Shoptetu (pr-action), u variant jen odkaz na detail.
   - Návrat / vypnutí = v zápatí HTML kódů odebrat zavaděč ke-podobne. */
(function () {
  if (window.__kePodobne) return; window.__kePodobne = 1;
  var SK = /^sk/i.test(document.documentElement.lang || '') || /^\/sk\//.test(location.pathname);
  var T = SK
    ? { h: 'Podobné produkty', cart: 'Do košíka', detail: 'Vybrať', prev: 'Predchádzajúce', next: 'Ďalšie' }
    : { h: 'Podobné výrobky', cart: 'Do košíku', detail: 'Vybrat', prev: 'Předchozí', next: 'Další' };
  var MAX = 8, last = null, cache = {};

  function path(u) { try { return new URL(u, location.href).pathname; } catch (e) { return String(u || ''); } }
  function isDetail() { return document.body && /\btype-detail\b/.test(document.body.className); }
  function esc(s) { return String(s == null ? '' : s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }

  /* který výrobek se právě přidal */
  function remember(el) {
    if (!el || !el.closest) return;
    if (el.closest('.ke-pod')) { var c0 = el.closest('.ke-pod__c'); if (c0) last = { url: c0.getAttribute('data-url'), pid: c0.getAttribute('data-id'), t: Date.now() }; return; }
    var card = el.closest('.p[data-micro-product-id], .product');
    var main = el.closest('#product-detail-form, .p-detail');
    if (card && !main) {
      var a = card.querySelector('a.name, a.image, a[href]');
      var pi = card.querySelector('[name=productId]') || card;
      last = { url: a && a.getAttribute('href'), pid: pi.value || pi.getAttribute('data-micro-product-id'), t: Date.now() };
    } else if (isDetail()) {
      var pd = document.querySelector('#product-detail-form [name=productId]');
      last = { url: location.pathname, pid: pd && pd.value, t: Date.now() };
    }
  }
  document.addEventListener('click', function (e) { var b = e.target.closest && e.target.closest('.add-to-cart-button, button[type=submit], .btn-cart'); if (b) remember(b); }, true);
  document.addEventListener('submit', function (e) { remember(e.target); }, true);

  /* karty z bloku Podobné */
  function cardsFrom(root) {
    var out = [], seen = {};
    var nodes = root.querySelectorAll('#productsAlternative .product:not(.slick-cloned) .p[data-micro-product-id], .products-alternative .product:not(.slick-cloned) .p[data-micro-product-id]');
    for (var i = 0; i < nodes.length; i++) {
      var p = nodes[i], id = p.getAttribute('data-micro-product-id');
      if (!id || seen[id]) continue; seen[id] = 1;
      var a = p.querySelector('a.name') || p.querySelector('a.image'), img = p.querySelector('a.image img');
      var pr = p.querySelector('.price-final'), f = p.querySelector('form.pr-action');
      var nm = p.querySelector('[data-micro=name]') || a;
      out.push({
        id: id, url: a ? a.getAttribute('href') : '',
        name: nm ? nm.textContent.replace(/\s+/g, ' ').trim() : '',
        img: img ? (img.getAttribute('data-src') || img.getAttribute('src') || '').trim() : '',
        price: pr ? pr.textContent.replace(/\s+/g, ' ').trim() : '',
        priceId: f && f.querySelector('[name=priceId]') ? f.querySelector('[name=priceId]').value : '',
        lang: f && f.querySelector('[name=language]') ? f.querySelector('[name=language]').value : (SK ? 'sk' : 'cs')
      });
    }
    return out;
  }
  function load(url) {
    var k = path(url);
    if (cache[k]) return cache[k];
    cache[k] = fetch(url, { credentials: 'same-origin' }).then(function (r) { return r.ok ? r.text() : ''; })
      .then(function (h) { return h ? cardsFrom(new DOMParser().parseFromString(h, 'text/html')) : []; })
      .catch(function () { delete cache[k]; return []; });
    return cache[k];
  }

  function css() {
    if (document.getElementById('ke-pod-css')) return;
    var s = document.createElement('style'); s.id = 'ke-pod-css';
    s.textContent =
      '.ke-pod{padding:18px 40px 26px;background:#fff;font-family:inherit}' +
      '.ke-pod__h{font-size:18px;font-weight:700;color:#1f1f2b;margin:0 0 12px}' +
      '.ke-pod__wrap{position:relative}' +
      '.ke-pod__row{display:flex;gap:12px;overflow-x:auto;scroll-snap-type:x mandatory;scroll-behavior:smooth;padding:2px 2px 8px;scrollbar-width:thin}' +
      '.ke-pod__c{flex:0 0 calc((100% - 36px)/4);max-width:calc((100% - 36px)/4);min-width:0;scroll-snap-align:start;display:flex;flex-direction:column;background:#fff;border:1px solid #eee;border-radius:14px;padding:10px;box-sizing:border-box;transition:box-shadow .15s,border-color .15s}' +
      '.ke-pod__c:hover{border-color:#e6cfca;box-shadow:0 6px 18px rgba(80,30,20,.10)}' +
      '.ke-pod__img{display:flex;align-items:center;justify-content:center;height:110px;margin-bottom:8px}' +
      '.ke-pod__img img{max-width:100%;max-height:110px;object-fit:contain}' +
      '.ke-pod__n{font-size:13px;line-height:1.35;color:#1f1f2b;text-decoration:none;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden;min-height:35px}' +
      '.ke-pod__n:hover{color:#a3392a}' +
      '.ke-pod__f{display:flex;align-items:center;justify-content:space-between;gap:6px;margin-top:auto;padding-top:8px}' +
      '.ke-pod__p{font-weight:700;font-style:italic;color:#a3392a;font-size:14px;white-space:nowrap}' +
      '.ke-pod__f form{margin:0;flex:0 0 auto}' +
      '.ke-pod .ke-pod__b{border:1px solid #a3392a!important;background:#fff!important;color:#a3392a!important;border-radius:999px!important;padding:5px 11px!important;font-size:12px!important;font-weight:600;line-height:1.2!important;cursor:pointer;white-space:nowrap;text-decoration:none;display:inline-block!important;width:auto!important;min-width:0!important;height:auto!important;min-height:0!important;text-transform:none!important;letter-spacing:0!important;box-shadow:none!important}' +
      '.ke-pod .ke-pod__b:hover{background:#a3392a!important;color:#fff!important}' +
      '.ke-pod__arr{position:absolute;top:50%;transform:translateY(-60%);width:34px;height:34px;border-radius:50%;border:1px solid #e3e3e3;background:#fff;box-shadow:0 2px 8px rgba(0,0,0,.12);color:#a3392a;font-size:20px;line-height:30px;cursor:pointer;z-index:2;padding:0}' +
      '.ke-pod__arr--l{left:-17px}.ke-pod__arr--r{right:-17px}.ke-pod__arr[hidden]{display:none}' +
      '@media (max-width:767px){.ke-pod{padding:14px 16px 18px}.ke-pod__c{flex-basis:44%;max-width:44%}.ke-pod__arr{display:none}.ke-pod__img{height:90px}.ke-pod__img img{max-height:90px}}';
    (document.head || document.documentElement).appendChild(s);
  }

  function render(ao, list) {
    css();
    var h = '<div class="ke-pod" role="region" aria-label="' + T.h + '"><div class="ke-pod__h">' + T.h + '</div><div class="ke-pod__wrap">' +
      '<button type="button" class="ke-pod__arr ke-pod__arr--l" aria-label="' + T.prev + '" hidden>&#8249;</button><div class="ke-pod__row">';
    list.forEach(function (x, i) {
      var btn = x.priceId
        ? '<form action="/action/Cart/addCartItem/" method="post" class="pr-action csrf-enabled"><input type="hidden" name="language" value="' + esc(x.lang) + '"><input type="hidden" name="priceId" value="' + esc(x.priceId) + '"><input type="hidden" name="productId" value="' + esc(x.id) + '"><input type="hidden" name="amount" value="1"><button type="submit" class="ke-pod__b">' + T.cart + '</button></form>'
        : '<a class="ke-pod__b" href="' + esc(x.url) + '">' + T.detail + '</a>';
      h += '<div class="ke-pod__c" data-id="' + esc(x.id) + '" data-url="' + esc(x.url) + '">' +
        '<a class="ke-pod__img" href="' + esc(x.url) + '" tabindex="-1">' + (x.img ? '<img src="' + esc(x.img) + '" alt=""' + (i > 3 ? ' loading="lazy"' : '') + '>' : '') + '</a>' +
        '<a class="ke-pod__n" href="' + esc(x.url) + '">' + esc(x.name) + '</a>' +
        '<div class="ke-pod__f"><span class="ke-pod__p">' + esc(x.price) + '</span>' + btn + '</div></div>';
    });
    h += '</div><button type="button" class="ke-pod__arr ke-pod__arr--r" aria-label="' + T.next + '" hidden>&#8250;</button></div></div>';
    var box = document.createElement('div'); box.innerHTML = h; var el = box.firstChild;
    var anchor = ao.querySelector('.extras-wrap');
    if (anchor && anchor.parentNode) anchor.parentNode.insertBefore(el, anchor.nextSibling); else ao.appendChild(el);
    try { if (window.shoptet && shoptet.csrf && shoptet.csrf.enabled) el.querySelectorAll('form').forEach(function (f) { if (shoptet.csrf.injectToken) shoptet.csrf.injectToken(f); else { var i = document.createElement('input'); i.type = 'hidden'; i.name = '__csrf__'; i.value = shoptet.csrf.token; f.appendChild(i); } }); } catch (e) {}
    var row = el.querySelector('.ke-pod__row'), L = el.querySelector('.ke-pod__arr--l'), R = el.querySelector('.ke-pod__arr--r');
    function upd() { L.hidden = row.scrollLeft < 5; R.hidden = row.scrollLeft + row.clientWidth >= row.scrollWidth - 5; }
    L.addEventListener('click', function () { row.scrollLeft -= row.clientWidth; });
    R.addEventListener('click', function () { row.scrollLeft += row.clientWidth; });
    row.addEventListener('scroll', upd, { passive: true });
    setTimeout(upd, 60);
    try { if (window.shoptet && shoptet.modal && shoptet.modal.shoptetResize) setTimeout(function () { shoptet.modal.shoptetResize(); }, 80); } catch (e) {}
  }

  function onPopup() {
    var ao = document.querySelector('#cboxLoadedContent .advanced-order') || document.querySelector('.advanced-order');
    if (!ao || ao.querySelector('.ke-pod')) return;
    var src = (last && Date.now() - last.t < 60000) ? last : (isDetail() ? { url: location.pathname } : null);
    if (!src || !src.url) return;
    var here = isDetail() && path(src.url) === location.pathname;
    var shown = {};
    ao.querySelectorAll('[data-micro-product-id]').forEach(function (n) { shown[n.getAttribute('data-micro-product-id')] = 1; });
    Promise.resolve(here ? cardsFrom(document) : load(src.url)).then(function (list) {
      list = list.filter(function (x) { return x.id !== String(src.pid || '') && !shown[x.id] && path(x.url) !== path(src.url); }).slice(0, MAX);
      if (list.length && document.body.contains(ao) && !ao.querySelector('.ke-pod')) render(ao, list);
    });
  }
  document.addEventListener('ShoptetDOMAdvancedOrderLoaded', function () { setTimeout(onPopup, 30); });
  window.kePodobneTest = onPopup; /* jen pro náhled */
})();
