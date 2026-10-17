/* KosmetikaEva.eu – oživení webu (v3, 17. 10. 2026)
   Úvodní stránka: 4. výhoda v pásu výhod, vánoční pruh, fotky v dlaždicích kategorií.
   Detail produktu: kolik zbývá do dopravy zdarma, výhody pod tlačítkem, na mobilu plovoucí lišta s tlačítkem,
   popis výrobku do strukturovaných dat (Google hlásil chybějící „description“).
   Styly jsou v ke-styl-v9.css. Vypnutí = odebrat <script> z HTML kódů (zápatí). */
(function () {
  if (window.keOzivi) return; window.keOzivi = 1;
  var SK = (document.documentElement.lang || '').slice(0, 2) === 'sk';
  var T = SK ? {
    fsLeft: 'Pridajte tovar za {x} a máte dopravu zadarmo', fsDone: 'Máte dopravu zadarmo', fsShort: 'Do dopravy zadarmo chýba {x}', fsShortDone: 'Dopravu máte zadarmo',
    perkShip: 'Doprava zadarmo nad {x}', perkStock: 'Stovky produktov skladom', perkReturn: 'Vrátenie do 14 dní', perkPay: 'Kartou, Apple Pay aj prevodom',
    ben4t: '10 rokov s vami', ben4d: 'Radi vám poradíme s výberom', btn: 'Do košíka',
    xk: 'Vianoce 2026', xh: 'Darčeky, ktoré potešia', xp: 'Vianočné edície a darčekové sady JUST, Essens a Eurona', xb: 'Vybrať darček →', xu: '/sk/vyhladavanie/?string=viano%C4%8Dn%C3%A1'
  } : {
    fsLeft: 'Přidejte zboží za {x} a máte dopravu zdarma', fsDone: 'Máte dopravu zdarma', fsShort: 'Do dopravy zdarma zbývá {x}', fsShortDone: 'Dopravu máte zdarma',
    perkShip: 'Na Zásilkovnu zdarma nad {x}', perkStock: 'Stovky produktů skladem', perkReturn: 'Vrácení do 14 dnů', perkPay: 'Kartou, Apple Pay i převodem',
    ben4t: '10 let s vámi', ben4d: 'Rádi vám poradíme s výběrem', btn: 'Do košíku',
    xk: 'Vánoce 2026', xh: 'Dárky, které potěší', xp: 'Vánoční edice a dárkové sady JUST, Essens a Eurona', xb: 'Vybrat dárek →', xu: '/vyhledavani/?string=v%C3%A1no%C4%8Dn%C3%AD'
  };
  var I = {
    truck: '<path d="M3 7h11v8H3zM14 10h4l3 3v2h-7z"/><circle cx="7" cy="17" r="1.6"/><circle cx="17" cy="17" r="1.6"/>',
    box: '<path d="M3 8l9-4 9 4-9 4-9-4z"/><path d="M3 8v8l9 4 9-4V8"/><path d="M12 12v8"/>',
    ret: '<path d="M4 9h11a5 5 0 0 1 0 10H8"/><path d="M8 5L4 9l4 4"/>',
    card: '<rect x="3" y="6" width="18" height="12" rx="2"/><path d="M3 10h18"/>',
    heart: '<path d="M12 20s-7-4.4-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 10c0 5.6-7 10-7 10z"/>',
    gift: '<rect x="4" y="9" width="16" height="11" rx="1.5"/><path d="M4 13h16M12 9v11"/><path d="M12 9c-2-4-6-4-6-1.5S10 9 12 9zM12 9c2-4 6-4 6-1.5S14 9 12 9z"/>'
  };
  function svg(n) { return '<svg class="ke-ico" viewBox="0 0 24 24" aria-hidden="true">' + I[n] + '</svg>'; }
  function dl(k) { try { return window.getShoptetDataLayer ? window.getShoptetDataLayer(k) : null; } catch (e) { return null; } }
  function money(v) {
    var c = dl('currencyInfo') || { symbol: 'Kč', symbolLeft: 0, thousandSeparator: ' ', priceDecimalPlaces: 0 };
    var s = Number(v).toFixed(Number(v) % 1 ? (c.priceDecimalPlaces || 0) : 0).replace('.', c.decimalSeparator || ',').replace(/\B(?=(\d{3})+(?!\d))/g, c.thousandSeparator || ' ');
    return c.symbolLeft == 1 ? c.symbol + s : s + ' ' + c.symbol;
  }
  function fsInfo() {
    var ci = dl('cartInfo'); if (!ci) return null;
    var from = Number(ci.freeShippingFrom) || 0, left, leftF = '';
    if (from) {
      left = ci.leftToFreeShipping ? Number(ci.leftToFreeShipping.priceLeft) || 0 : 0;
      leftF = ci.leftToFreeShipping && ci.leftToFreeShipping.formattedPrice;
    } else {
      /* Shoptet u eur hranici neposílá – Slovensko má dopravu zdarma nad 120 € */
      var cur = dl('currencyInfo'); if (!cur || cur.code !== 'EUR') return null;
      from = 120;
      var tot = ci.getNoBillingShippingPrice ? Number(ci.getNoBillingShippingPrice.withVat) || 0 : 0;
      left = Math.max(0, Math.round((from - tot) * 100) / 100);
    }
    var done = !!ci.freeShipping || left <= 0;
    return { done: done, left: left, leftF: leftF || money(left), from: from,
      pct: done ? 100 : Math.max(4, Math.min(100, Math.round((from - left) / from * 100))) };
  }
  function fsHTML(short) {
    var f = fsInfo(); if (!f) return '';
    var t = f.done ? (short ? T.fsShortDone : T.fsDone) : (short ? T.fsShort : T.fsLeft).replace('{x}', '<b>' + f.leftF + '</b>');
    return short ? '<span>' + t + '</span><div class="ke-free__bar"><i style="width:' + f.pct + '%"></i></div>'
      : '<div class="ke-free__t">' + svg('truck') + '<span>' + t + '</span></div><div class="ke-free__bar"><i style="width:' + f.pct + '%"></i></div>';
  }
  var page = dl('pageType');

  /* ---------- úvodní stránka ---------- */
  if (page === 'homepage') {
    var bb = document.querySelector('.benefitBanner.position--benefitHomepage');
    if (bb && bb.querySelectorAll('.benefitBanner__item').length === 3) {
      var it = document.createElement('div'); it.className = 'benefitBanner__item ke-ben4';
      it.innerHTML = '<div class="benefitBanner__picture">' + svg('heart') + '</div><div class="benefitBanner__content"><strong class="benefitBanner__title">' + T.ben4t + '</strong><div class="benefitBanner__data">' + T.ben4d + '</div></div>';
      bb.appendChild(it);
    }
    var head = document.querySelector('.homepage-group-title.homepage-products-heading-6');
    if (head && !document.querySelector('.ke-xmas')) {
      var x = document.createElement('a'); x.className = 'ke-xmas'; x.href = T.xu;
      x.innerHTML = '<svg viewBox="0 0 24 24" aria-hidden="true">' + I.gift + '</svg><div><div class="ke-xmas__k">' + T.xk + '</div><div class="ke-xmas__h">' + T.xh + '</div><div class="ke-xmas__p">' + T.xp + '</div></div><span class="ke-xmas__b">' + T.xb + '</span>';
      head.parentNode.insertBefore(x, head);
    }
    var CDN = 'https://cdn.myshoptet.com/usr/www.kosmetikaeva.eu/user/shop/detail/', Q = '?ff=1&x=423&y=318&q=85&sg=2175fb9d&ts=';
    var IMG = {
      '/damske-parfemy/': '5915_essens-damsky-parfem-w124-50-ml.jpg' + Q + '6ac9e918',
      '/panske-parfemy/': '10393_essens-pansky-parfem-m901-50-ml.png' + Q + '6aca009b',
      '/kosmetika/': '7390_eucasol-50-ml.png' + Q + '6acb4118',
      '/doplnky-stravy/': '3843-1_3843-1-lr-lifetakt-colostrum-kapsle-60-kapsli.jpg' + Q + '5a4b52f7',
      '/domacnost/': '4466_eurona-praci-prostredek-na-bile-a-jemne-svetle-pradlo--935-g.jpg' + Q + '6acca004'
    };
    var cats = document.querySelectorAll('a.ke-cat');
    for (var i = 0; i < cats.length; i++) {
      var a = cats[i], href = (a.getAttribute('href') || '').replace(/^https?:\/\/[^/]+/, '').replace(/^\/sk\//, '/');
      var name = a.textContent.replace(/\s*→\s*$/, '').trim();
      var pic = IMG[href] ? '<img src="' + CDN + IMG[href] + '" alt="" loading="lazy" onerror="this.parentNode.innerHTML=\'' + svg('gift').replace(/"/g, '&quot;') + '\'">' : svg('gift');
      a.classList.add('ke-cat--img');
      a.innerHTML = '<span class="ke-cat__img">' + pic + '</span><span class="ke-cat__t">' + name + ' <span>→</span></span>';
    }
  }

  /* ---------- detail produktu ---------- */
  /* .buy-box skládá až skript šablony po načtení stránky, proto se na něj čeká */
  function detail() {
    var box = document.querySelector('.p-info-wrapper .buy-box') || document.querySelector('.buy-box');
    var mainBtn = document.querySelector('.p-info-wrapper .add-to-cart-button') || document.querySelector('.add-to-cart-button');
    if (!box || !mainBtn) return false;
    if (document.querySelector('.ke-buy-extra')) return true;
    {
      var from = (fsInfo() || {}).from;
      var ex = document.createElement('div'); ex.className = 'ke-buy-extra';
      ex.innerHTML = '<div class="ke-free"></div><div class="ke-perks">' +
        (from ? '<div class="ke-perk"><span class="ke-perk__c">' + svg('truck') + '</span>' + T.perkShip.replace('{x}', money(from)) + '</div>' : '') +
        '<div class="ke-perk"><span class="ke-perk__c">' + svg('box') + '</span>' + T.perkStock + '</div>' +
        '<div class="ke-perk"><span class="ke-perk__c">' + svg('ret') + '</span>' + T.perkReturn + '</div>' +
        '<div class="ke-perk"><span class="ke-perk__c">' + svg('card') + '</span>' + T.perkPay + '</div></div>';
      box.appendChild(ex);
      var st = document.createElement('div'); st.className = 'ke-sticky';
      var img = document.querySelector('.p-image img, .p-main-image img, .p-image-wrapper img');
      var h1 = document.querySelector('.p-detail-inner h1, h1');
      st.innerHTML = '<div class="ke-sticky__row">' + (img ? '<img class="ke-sticky__img" alt="" src="' + (img.currentSrc || img.src) + '">' : '') +
        '<div class="ke-sticky__n"><span>' + (h1 ? h1.textContent.trim().replace(/</g, '&lt;') : '') + '</span><b class="ke-sticky__p"></b></div>' +
        '<button type="button" class="ke-sticky__btn">' + T.btn + '</button></div><div class="ke-sticky__free"></div>';
      document.body.appendChild(st);
      var price = function () {
        var hs = document.querySelectorAll('.p-info-wrapper .price-final-holder, .buy-box .price-final-holder');
        for (var j = 0; j < hs.length; j++) if (hs[j].offsetParent !== null) return hs[j].textContent.replace(/\s+/g, ' ').trim();
        return '';
      };
      var update = function () {
        var f = ex.querySelector('.ke-free'), info = fsInfo();
        f.innerHTML = fsHTML(false); f.classList.toggle('is-free', !!(info && info.done)); f.style.display = info ? '' : 'none';
        st.querySelector('.ke-sticky__free').innerHTML = fsHTML(true);
        st.querySelector('.ke-sticky__p').textContent = price();
      };
      var toggle = function () {
        var on = window.innerWidth < 768 && mainBtn.getBoundingClientRect().bottom < 0;
        if (on !== st.classList.contains('is-on')) { st.classList.toggle('is-on', on); document.body.classList.toggle('ke-sticky-on', on); }
      };
      window.addEventListener('scroll', toggle, { passive: true }); window.addEventListener('resize', toggle);
      st.querySelector('.ke-sticky__btn').addEventListener('click', function () {
        var sel = document.querySelector('.p-info-wrapper select[name^="parameterValueId"]');
        if (sel && !sel.value) {
          sel.scrollIntoView({ behavior: 'smooth', block: 'center' });
          setTimeout(function () { try { sel.focus(); } catch (e) {} }, 450);
          return;
        }
        mainBtn.scrollIntoView({ behavior: 'smooth', block: 'center' });
        setTimeout(function () { mainBtn.click(); }, 450);
      });
      ['ShoptetDataLayerUpdated', 'ShoptetCartUpdated', 'ShoptetDOMCartCountUpdated', 'ShoptetVariantAvailable', 'ShoptetSimpleVariantChange', 'ShoptetSplitVariantParameterChange'].forEach(function (ev) {
        document.addEventListener(ev, function () { setTimeout(update, 60); });
      });
      document.addEventListener('change', function (e) { if (e.target && e.target.closest && e.target.closest('.p-info-wrapper')) setTimeout(update, 60); });
      update(); toggle();
    }
    return true;
  }
  /* strukturovaná data: Shoptet u Product nevypisuje description → doplnit z popisu výrobku
     (.basic-description bez nadpisu „Detailní popis produktu“; odstavce a odrážky oddělené mezerou) */
  function sdDescription() {
    var prod = document.querySelector('[itemscope][itemtype$="schema.org/Product"]');
    if (!prod || prod.querySelector('[itemprop="description"]')) return;
    var src = document.querySelector('#description .basic-description') || document.querySelector('.basic-description');
    if (!src) return;
    var parts = [], els = src.querySelectorAll('h2, h4, p, li');
    for (var i = 0; i < els.length && parts.join(' ').length < 1200; i++) {
      var t = (els[i].textContent || '').replace(/\s+/g, ' ').trim();
      if (t && !(els[i].tagName === 'P' && els[i].querySelector('li'))) parts.push(/[.!?:]$/.test(t) ? t : t + '.');
    }
    var txt = parts.join(' ').replace(/\s+/g, ' ').trim();
    if (txt.length < 20) txt = (src.textContent || '').replace(/^\s*(Detailní popis produktu|Podrobný popis)\s*/i, '').replace(/\s+/g, ' ').trim();
    if (txt.length < 20) return;
    if (txt.length > 1000) txt = txt.slice(0, 1000).replace(/\s+\S*$/, '') + '…';
    var m = document.createElement('meta');
    m.setAttribute('itemprop', 'description'); m.setAttribute('content', txt);
    prod.appendChild(m);
  }
  if (page === 'productDetail') {
    try { sdDescription(); } catch (e) {}
    var tries = 0;
    var tryDetail = function () { if (!detail() && ++tries < 60) setTimeout(tryDetail, 250); };
    if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', tryDetail); else tryDetail();
  }
})();
