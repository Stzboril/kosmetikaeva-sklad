/* KosmetikaEva.eu – oživení webu (v5, 19. 10. 2026)
   Úvodní stránka: 4. výhoda v pásu výhod, vánoční pruh, fotky v dlaždicích kategorií.
   Detail produktu: kolik zbývá do dopravy zdarma, výhody pod tlačítkem, na mobilu plovoucí lišta s tlačítkem,
   popis výrobku do strukturovaných dat (Google hlásil chybějící „description“).
   v5 – hlídací pes (formulář je Shoptetu, skript ho jen zviditelní):
     • detail výrobku, který nejde objednat (Brzy skladem, Na dotaz, Na cestě…; ne Prodej skončil): místo „Vložit do košíku“
       tlačítko „Upozornit, až bude skladem“ – otevře formulář hlídacího psa s předvyplněným „bude na skladě“ a zvolenou variantou;
       u výrobků s variantami podle zvolené varianty (nebo když jsou vyprodané všechny); na mobilu totéž v plovoucí liště;
     • karty výrobků (kategorie, značky, vyhledávání, související…): u výrobků, které nejdou objednat, odkaz „Hlídat naskladnění“
       → detail s #hlidat, který formulář rovnou otevře;
     • oprava v4: plovoucí lišta na mobilu brala „Do košíku“ i ze souvisejících výrobků (u vyprodaného výrobku by přidala jiný).
   Styly: ke-styl-v17.css + styly hlídacího psa vkládá tento skript (funkce wdCss). Vypnutí = v zápatí HTML kódů vrátit ke-ozivi-v4.js. */
(function () {
  if (window.keOzivi) return; window.keOzivi = 1;
  var SK = (document.documentElement.lang || '').slice(0, 2) === 'sk';
  var T = SK ? {
    fsLeft: 'Pridajte tovar za {x} a máte dopravu zadarmo', fsDone: 'Máte dopravu zadarmo', fsShort: 'Do dopravy zadarmo chýba {x}', fsShortDone: 'Dopravu máte zadarmo',
    perkShip: 'Doprava zadarmo nad {x}', perkStock: 'Stovky produktov skladom', perkReturn: 'Vrátenie do 14 dní', perkPay: 'Kartou, Apple Pay aj prevodom',
    ben4t: '10 rokov s vami', ben4d: 'Radi vám poradíme s výberom', btn: 'Do košíka',
    xk: 'Vianoce 2026', xh: 'Darčeky, ktoré potešia', xp: 'Vianočné edície a darčekové sady JUST, Essens a Eurona', xb: 'Vybrať darček →', xu: '/sk/vanocni-darky/',
    wdBtn: 'Upozorniť, keď bude skladom', wdNote: 'Pošleme vám e-mail, keď tovar naskladníme.', wdShort: 'Upozorniť ma', wdCard: 'Strážiť naskladnenie'
  } : {
    fsLeft: 'Přidejte zboží za {x} a máte dopravu zdarma', fsDone: 'Máte dopravu zdarma', fsShort: 'Do dopravy zdarma zbývá {x}', fsShortDone: 'Dopravu máte zdarma',
    perkShip: 'Na Zásilkovnu zdarma nad {x}', perkStock: 'Stovky produktů skladem', perkReturn: 'Vrácení do 14 dnů', perkPay: 'Kartou, Apple Pay i převodem',
    ben4t: '10 let s vámi', ben4d: 'Rádi vám poradíme s výběrem', btn: 'Do košíku',
    xk: 'Vánoce 2026', xh: 'Dárky, které potěší', xp: 'Vánoční edice a dárkové sady JUST, Essens a Eurona', xb: 'Vybrat dárek →', xu: '/vanocni-darky/',
    wdBtn: 'Upozornit, až bude skladem', wdNote: 'Pošleme vám e-mail, jakmile zboží naskladníme.', wdShort: 'Upozornit mě', wdCard: 'Hlídat naskladnění'
  };
  /* Výrobky (id produktu v Shoptetu), u kterých se hlídání nenabízí – zboží se už nenaskladní. */
  var NOWATCH = [];
  var ENDED = /^\s*(prodej|predaj) skon/i; /* „Prodej skončil“ / „Predaj skončil“ – hlídání nedává smysl */
  var I = {
    truck: '<path d="M3 7h11v8H3zM14 10h4l3 3v2h-7z"/><circle cx="7" cy="17" r="1.6"/><circle cx="17" cy="17" r="1.6"/>',
    box: '<path d="M3 8l9-4 9 4-9 4-9-4z"/><path d="M3 8v8l9 4 9-4V8"/><path d="M12 12v8"/>',
    ret: '<path d="M4 9h11a5 5 0 0 1 0 10H8"/><path d="M8 5L4 9l4 4"/>',
    card: '<rect x="3" y="6" width="18" height="12" rx="2"/><path d="M3 10h18"/>',
    heart: '<path d="M12 20s-7-4.4-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 10c0 5.6-7 10-7 10z"/>',
    gift: '<rect x="4" y="9" width="16" height="11" rx="1.5"/><path d="M4 13h16M12 9v11"/><path d="M12 9c-2-4-6-4-6-1.5S10 9 12 9zM12 9c2-4 6-4 6-1.5S14 9 12 9z"/>',
    bell: '<path d="M18 8a6 6 0 0 0-12 0c0 7-3 9-3 9h18s-3-2-3-9"/><path d="M13.7 21a2 2 0 0 1-3.4 0"/>'
  };
  function svg(n) { return '<svg class="ke-ico" viewBox="0 0 24 24" aria-hidden="true">' + I[n] + '</svg>'; }
  function bell() { return '<svg class="ke-wd-ico" viewBox="0 0 24 24" aria-hidden="true">' + I.bell + '</svg>'; }
  function fire(el) { try { el.dispatchEvent(new Event('change', { bubbles: true })); } catch (e) {} }
  function wdCss() {
    if (document.getElementById('ke-wd-css')) return;
    var s = document.createElement('style'); s.id = 'ke-wd-css';
    s.textContent =
      '.ke-wd{display:none;margin:16px 0 4px}' +
      '.buy-box.ke-wd-on .ke-wd{display:block}' +
      '.buy-box.ke-wd-on .add-to-cart,.buy-box.ke-wd-on .ke-free{display:none!important}' +
      '.ke-wd__btn{display:flex;align-items:center;justify-content:center;gap:10px;width:100%;min-height:52px;margin:0;padding:12px 24px;' +
        'border:1px solid var(--ke-accent,#a3392a);border-radius:14px;background:var(--ke-accent,#a3392a);color:#fff;' +
        'font:600 12px/1.3 var(--ke-font,Montserrat,system-ui,sans-serif);letter-spacing:.12em;text-transform:uppercase;cursor:pointer;' +
        'box-shadow:0 6px 16px -10px rgba(163,57,42,.6);transition:background-color .3s,border-color .3s,translate .3s}' +
      '.ke-wd__btn:hover,.ke-wd__btn:focus-visible{background:var(--ke-accent-hover,#87301f);border-color:var(--ke-accent-hover,#87301f);translate:0 -2px}' +
      '.ke-wd__btn:active{translate:0 0}' +
      '.ke-wd-ico{width:18px;height:18px;flex:0 0 auto;fill:none;stroke:currentColor;stroke-width:1.9;stroke-linecap:round;stroke-linejoin:round}' +
      '.ke-wd__t{margin:9px 0 0!important;font-size:13px;line-height:1.45;color:var(--ke-muted,#6e6c7a);text-align:center}' +
      '.ke-wd-card{position:relative;z-index:2;display:flex;align-items:center;justify-content:center;gap:6px;width:-moz-fit-content;width:fit-content;' +
        'margin:6px auto 0;padding:2px 4px;font:600 13px/1.35 var(--ke-font,Montserrat,system-ui,sans-serif);color:var(--ke-accent,#a3392a)!important;text-decoration:none!important}' +
      '.ke-wd-card .ke-wd-ico{width:15px;height:15px}' +
      '.ke-wd-card:hover span{text-decoration:underline}' +
      '.ke-wd-has .availability::before{display:none!important}' +
      '.ke-sticky.is-wd .ke-sticky__free{display:none}';
    (document.head || document.documentElement).appendChild(s);
  }
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

  /* ---------- hlídací pes ---------- */
  function wdLink() { return document.querySelector('.p-info-wrapper a.link-icon.watchdog') || document.querySelector('.p-detail a.link-icon.watchdog'); }
  function variantData() { return window.shoptet && shoptet.variantsSplit && shoptet.variantsSplit.necessaryVariantData; }
  /* zvolená varianta podle selectů parameterValueId[…] (klíč dat = „param-hodnota[-param-hodnota…]“) */
  function selectedVariant(data) {
    var sels = document.querySelectorAll('.p-info-wrapper select[name^="parameterValueId"]');
    if (!sels.length) return null;
    var want = {}, n = 0;
    for (var i = 0; i < sels.length; i++) {
      if (!sels[i].value) return null;
      var pid = sels[i].getAttribute('data-parameter-id') || (sels[i].name.match(/\d+/) || [])[0];
      want[pid] = sels[i].value; n++;
    }
    for (var k in data) {
      var p = k.split('-'); if (p.length !== n * 2) continue;
      var ok = true;
      for (var j = 0; j < p.length; j += 2) if (want[p[j]] !== p[j + 1]) { ok = false; break; }
      if (ok) return data[k];
    }
    return null;
  }
  /* on = výrobek (zvolená varianta) nejde objednat a hlídání má smysl; vid = id varianty pro formulář */
  function wdState() {
    var p = dl('product') || {};
    if (!wdLink() || NOWATCH.indexOf(Number(p.id)) > -1) return { on: false };
    if (p.hasVariants) {
      var data = variantData(); if (!data) return { on: false };
      var v = selectedVariant(data);
      if (v) return { on: !v.isNotSoldOut && !ENDED.test(v.availabilityName || ''), vid: v.id };
      var buyable = false, watch = false;
      for (var k in data) { if (data[k].isNotSoldOut) buyable = true; else if (!ENDED.test(data[k].availabilityName || '')) watch = true; }
      return { on: !buyable && watch };
    }
    if (document.querySelector('.p-info-wrapper .add-to-cart-button')) return { on: false };
    var av = document.querySelector('.p-info-wrapper .availability-value');
    if (av && ENDED.test(av.textContent)) return { on: false };
    return { on: !!document.querySelector('.p-info-wrapper tr.sold-out') };
  }
  /* otevře formulář hlídacího psa Shoptetu (okno colorbox) a předvyplní „bude na skladě“ + variantu */
  function openWatchdog(vid) {
    var a = wdLink(); if (!a) return;
    var old = document.getElementById('watchdog-form'), n = 0;
    a.click();
    (function fill() {
      var f = document.getElementById('watchdog-form');
      if (!f || f === old) { if (++n < 50) setTimeout(fill, 120); return; }
      var s = f.querySelector('#watchdog-simple-variants-select');
      if (s && vid && s.querySelector('option[value="' + vid + '"]') && s.value !== String(vid)) { s.value = String(vid); fire(s); }
      var c = f.querySelector('#onStock');
      if (c && !c.checked) { c.checked = true; fire(c); }
    })();
  }
  /* karty výrobků: u výrobků, které nejdou objednat, odkaz „Hlídat naskladnění“ → detail#hlidat */
  function wdCards() {
    var ps = document.querySelectorAll('.product > .p[data-micro="product"]:not([data-ke-wd])');
    for (var i = 0; i < ps.length; i++) {
      var p = ps[i]; p.setAttribute('data-ke-wd', '1');
      var off = p.querySelector('[data-micro="offer"]'), av = p.querySelector('.availability');
      if (!off || !av || /InStock/i.test(off.getAttribute('data-micro-availability') || '')) continue;
      if (ENDED.test(av.textContent) || NOWATCH.indexOf(Number(p.getAttribute('data-micro-product-id'))) > -1) continue;
      var a0 = p.querySelector('a.name') || p.querySelector('a.image'); if (!a0 || !a0.getAttribute('href')) continue;
      wdCss();
      var l = document.createElement('a'); l.className = 'ke-wd-card';
      l.href = a0.getAttribute('href').split('#')[0] + '#hlidat';
      l.innerHTML = bell() + '<span>' + T.wdCard + '</span>';
      av.parentNode.insertBefore(l, av.nextSibling);
      p.classList.add('ke-wd-has');
    }
  }
  try { wdCards(); } catch (e) {}
  ['ShoptetDOMPageContentLoaded', 'ShoptetDOMPageMoreProductsLoaded', 'ShoptetDOMContentLoaded'].forEach(function (ev) {
    document.addEventListener(ev, function () { setTimeout(function () { try { wdCards(); } catch (e) {} }, 60); });
  });

  /* ---------- detail produktu ---------- */
  /* .buy-box skládá až skript šablony po načtení stránky, proto se na něj čeká.
     Tlačítko „Do košíku“ se hledá jen v hlavní části (.p-info-wrapper), ne u souvisejících výrobků. */
  function detail() {
    var box = document.querySelector('.p-info-wrapper .buy-box');
    var mainBtn = document.querySelector('.p-info-wrapper .add-to-cart-button');
    if (!box || (!mainBtn && !document.querySelector('.p-info-wrapper tr.sold-out'))) return false;
    if (document.querySelector('.ke-buy-extra')) return true;
    {
      wdCss();
      var wd = document.createElement('div'); wd.className = 'ke-wd';
      wd.innerHTML = '<button type="button" class="ke-wd__btn">' + bell() + '<span>' + T.wdBtn + '</span></button><p class="ke-wd__t">' + T.wdNote + '</p>';
      var bottom = box.querySelector('.bottom');
      if (bottom && bottom.parentNode === box) box.insertBefore(wd, bottom.nextSibling); else box.appendChild(wd);
      var state = { on: false };
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
      var setWd = function () {
        try { state = wdState(); } catch (e) { state = { on: false }; }
        box.classList.toggle('ke-wd-on', !!state.on);
        st.classList.toggle('is-wd', !!state.on);
        var b = st.querySelector('.ke-sticky__btn'), t = state.on ? T.wdShort : T.btn;
        if (b.textContent !== t) b.textContent = t;
      };
      var update = function () {
        setWd();
        var f = ex.querySelector('.ke-free'), info = fsInfo();
        f.innerHTML = fsHTML(false); f.classList.toggle('is-free', !!(info && info.done)); f.style.display = info ? '' : 'none';
        st.querySelector('.ke-sticky__free').innerHTML = fsHTML(true);
        st.querySelector('.ke-sticky__p').textContent = price();
        toggle();
      };
      /* lišta se ukáže, když hlavní tlačítko (Do košíku, nebo Upozornit) zmizí nahoře z obrazovky */
      var toggle = function () {
        var el = state.on ? wd.querySelector('.ke-wd__btn') : mainBtn;
        var on = !!el && window.innerWidth < 768 && el.getBoundingClientRect().bottom < 0;
        if (on !== st.classList.contains('is-on')) { st.classList.toggle('is-on', on); document.body.classList.toggle('ke-sticky-on', on); }
      };
      window.addEventListener('scroll', toggle, { passive: true }); window.addEventListener('resize', toggle);
      wd.querySelector('.ke-wd__btn').addEventListener('click', function () { openWatchdog(state.vid); });
      st.querySelector('.ke-sticky__btn').addEventListener('click', function () {
        if (state.on) {
          wd.scrollIntoView({ behavior: 'smooth', block: 'center' });
          setTimeout(function () { openWatchdog(state.vid); }, 450);
          return;
        }
        if (!mainBtn) return;
        var sel = document.querySelector('.p-info-wrapper select[name^="parameterValueId"]');
        if (sel && !sel.value) {
          sel.scrollIntoView({ behavior: 'smooth', block: 'center' });
          setTimeout(function () { try { sel.focus(); } catch (e) {} }, 450);
          return;
        }
        mainBtn.scrollIntoView({ behavior: 'smooth', block: 'center' });
        setTimeout(function () { mainBtn.click(); }, 450);
      });
      ['ShoptetDataLayerUpdated', 'ShoptetCartUpdated', 'ShoptetDOMCartCountUpdated', 'ShoptetVariantAvailable', 'ShoptetVariantUnavailable', 'ShoptetSimpleVariantChange', 'ShoptetSplitVariantParameterChange'].forEach(function (ev) {
        document.addEventListener(ev, function () { setTimeout(update, 60); });
      });
      document.addEventListener('change', function (e) { if (e.target && e.target.closest && e.target.closest('.p-info-wrapper')) setTimeout(update, 60); });
      update();
      /* příchod z odkazu „Hlídat naskladnění“ na kartě (#hlidat) → rovnou otevřít formulář */
      if (/^#hlidat$/i.test(location.hash)) {
        try { history.replaceState(null, '', location.pathname + location.search); } catch (e) {}
        if (state.on) setTimeout(function () { wd.scrollIntoView({ block: 'center' }); openWatchdog(state.vid); }, 400);
      }
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
