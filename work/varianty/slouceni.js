/* Sloučení stejných výrobků v různých objemech do jednoho výrobku s variantami (Shoptet admin, KosmetikaEva.eu).
   Majitel 19. 10. 2026: „proč neuděláš tyto a další parfémy jako sdruženou položku … aby si zákazník mohl vybrat z roletkového seznamu“,
   po zkoušce na The Garden of Dreams „ano sluč vše“.
   Spouští se v záložce administrace (potřebuje shoptet.csrf.token). keSloucit(skupina) → protokol; nic nemaže, druhé výrobky jen skryje.
   skupina = {main: id hlavního výrobku, others: [id…], tpl: id šablony variant, param: id parametru, vals: {popisek: id hodnoty}} */
(function () {
  const BASE = location.origin;
  async function getForm(url) {
    const h = await (await fetch(url, { cache: 'no-store' })).text();
    const d = new DOMParser().parseFromString(h, 'text/html');
    const f = d.querySelector('#main-form') || [...d.querySelectorAll('form')].find(x => /pridat-variantu/.test(x.getAttribute('action') || ''));
    const o = {}; for (const [k, v] of new FormData(f)) if (k !== '__csrf__') o[k] = (o[k] !== undefined ? o[k] + '|' : '') + (typeof v === 'string' ? v : '[file]');
    return { f, o, d };
  }
  const prod = (id, lang) => getForm('/admin/produkty-detail/?id=' + id + '&language=' + lang);
  async function post(f, set) {
    const fd = new FormData(f);
    for (const k in set) { if (set[k] === null) fd.delete(k); else fd.set(k, set[k]); }
    fd.set('buttonAction', 'saveAndStay'); fd.set('__csrf__', shoptet.csrf.token);
    const r = await fetch(f.getAttribute('action'), { method: 'POST', body: fd });
    if (!r.ok) throw new Error('POST ' + r.status + ' ' + f.getAttribute('action'));
  }
  // objem / hmotnost z názvu: „… 200 ml“, „…, 2750 g“, „… Refill 500 ml“, „…2750g“
  function vol(name) {
    const m = name.match(/(\d[\d\s]*)\s*(ml|g)\b(?!.*\d\s*(ml|g)\b)/i);
    if (!m) throw new Error('objem nenalezen: ' + name);
    const n = +m[1].replace(/\s/g, ''), u = m[2].toLowerCase();
    const refill = /refill|náplň/i.test(name);
    const label = (n >= 1000 && u === 'g' ? String(n).replace(/(\d)(\d{3})$/, '$1 $2') : String(n)) + ' ' + u + (refill ? ' (náplň)' : '');
    return { n, u, refill, label };
  }
  function base(name) {
    return name.replace(/[\s,–-]*(Refill\s*)?\d[\d\s]*\s*(ml|g)\s*$/i, '').replace(/^(Essens)\s+Refill\s+/i, '$1 ').replace(/\s+Refill\s*$/i, '').trim();
  }
  function joinVals(list, lang) {
    const a = list.map(v => v.label);
    const and = lang === 'sk' ? ' a ' : ' a ';
    return a.length === 2 ? a[0] + and + a[1] : a.slice(0, -1).join(', ') + and + a[a.length - 1];
  }
  async function skUrl(path) {
    const h = await (await fetch(path, { credentials: 'omit', cache: 'no-store' })).text();
    const d = new DOMParser().parseFromString(h, 'text/html');
    const a = d.querySelector('link[rel=alternate][hreflang=sk]');
    return a ? a.getAttribute('href').replace(BASE, '') : null;
  }
  async function pubPath(id) { // cesta výrobku na webu z odkazu „Zobrazit“ v administraci
    const { d } = await prod(id, 'cs');
    const a = [...d.querySelectorAll('a')].find(x => /Zobrazit/.test(x.textContent) && /^https?:\/\/www\.kosmetikaeva\.eu\//.test(x.getAttribute('href') || ''));
    return a ? a.getAttribute('href').replace(BASE, '') : null;
  }
  async function redirect(from, to) {
    const fd = new FormData(); fd.append('fromUrl', from); fd.append('toUrl', to); fd.append('id', '0'); fd.append('action', 'add'); fd.append('__csrf__', shoptet.csrf.token);
    const r = await fetch('/admin/presmerovani-url-detail/', { method: 'POST', body: fd, headers: { 'X-Inertia': 'true', 'Persist-Messages': '0' } });
    return r.status;
  }
  // řádek „<strong>Objem</strong>: 200 ml (40 dávek)“ v popisu
  const LINE = /(<strong>\s*(Objem|Obsah|Hmotnost|Hmotnosť|Balení|Balenie)\s*<\/strong>\s*:?\s*)([^<]+)/i;

  window.keSloucit = async function (g) {
    const log = [];
    const ids = [g.main, ...g.others];
    const P = {};
    for (const id of ids) { P[id] = { cs: (await prod(id, 'cs')).o, sk: (await prod(id, 'sk')).o }; P[id].v = vol(P[id].cs.name); P[id].path = await pubPath(id); P[id].skPath = P[id].path ? await skUrl(P[id].path) : null; }
    const M = P[g.main];
    if (M.cs.hasVariants === '1') throw new Error('hlavní výrobek už má varianty');
    for (const id of ids) if (!(P[id].v.label in g.vals)) throw new Error('hodnota ' + P[id].v.label + ' není v šabloně');
    try { localStorage.setItem('keSlouceniZaloha_' + g.main, JSON.stringify(P)); } catch (e) {}
    // 1) uvolnit kódy druhých výrobků
    for (const id of g.others) { const { f } = await prod(id, 'cs'); await post(f, { code: P[id].cs.code + '-SLOUCENO' }); log.push('kód ' + P[id].cs.code + ' → ' + P[id].cs.code + '-SLOUCENO (' + id + ')'); }
    // 2) fotka druhého výrobku k hlavnímu
    for (const id of g.others) {
      const img = (P[id].cs['shop_images[]'] || '').split('|')[0];
      const { d: pd } = await prod(id, 'cs');
      const src = [...pd.querySelectorAll('img')].map(i => i.getAttribute('src') || '').find(x => /\/user\/shop\/admin_detail\//.test(x));
      let blob = null;
      if (src) { const r = await fetch(src.replace('/admin_detail/', '/orig/').split('?')[0], { cache: 'no-store' }); if (r.ok && /image/.test(r.headers.get('content-type') || '')) blob = await r.blob(); }
      if (!blob) { log.push('fotka ' + id + ' nenalezena'); P[id].newImg = (M.cs['shop_images[]'] || '').split('|')[0]; continue; }
      const fn = P[g.main].path.split('/').filter(Boolean).pop() + '-' + P[id].v.n + '.' + (blob.type === 'image/png' ? 'png' : 'jpg');
      const fd = new FormData(); fd.append('name', fn); fd.append('__csrf__', shoptet.csrf.token); fd.append('Filedata', new File([blob], fn, { type: blob.type }));
      const j = await (await fetch('/admin/action/ProductDetail/UploadImage/?productId=' + g.main, { method: 'POST', body: fd })).json();
      P[id].newImg = String(j.imageId); log.push('fotka ' + id + ' (' + img + ') → ' + j.imageId);
    }
    // 3) varianty
    const fd = new FormData();
    const dv = { action: 'addVariants', parameterGroupId: String(g.tpl), price: M.cs['pricelistPrice[1]'], standardPrice: M.cs.standardPrice || '', purchasePrice: (M.cs.purchasePrice || '').replace(',', '.'), weight: '', stock: M.cs['stocksAmount[1]'] || '0', availabilityInStockId: M.cs.availabilityInStockId, availabilityId: M.cs.availabilityId, variantImage: (M.cs['shop_images[]'] || '').split('|')[0] };
    for (const k in dv) fd.append(k, dv[k]);
    for (const id of ids) fd.append('parameterValues[' + g.param + '][]', g.vals[P[id].v.label]);
    fd.append('__csrf__', shoptet.csrf.token);
    await fetch('/admin/pridat-varianty-produktu/?productId=' + g.main + '&parentControllerReferer=', { method: 'POST', body: fd });
    const after = await prod(g.main, 'cs');
    if (after.o.hasVariants !== '1') throw new Error('varianty se nevytvořily');
    const links = [...after.d.querySelectorAll('a')].map(a => [a.textContent.trim(), (a.getAttribute('href') || '').match(/pridat-variantu\/\?id=(\d+)/)]).filter(x => x[1]);
    const vid = {}; links.forEach(([t, m]) => { vid[t] = m[1]; });
    log.push('varianty: ' + JSON.stringify(vid));
    // 4) údaje variant
    for (const id of ids) {
      const p = P[id], c = p.cs, v = vid[p.v.label]; if (!v) throw new Error('varianta ' + p.v.label + ' chybí');
      const { f } = await getForm('/admin/pridat-variantu/?id=' + v + '&language=cs');
      await post(f, {
        code: c.code, 'pricelistPrice[1]': c['pricelistPrice[1]'], standardPrice: c.standardPrice || '', purchasePrice: c.purchasePrice || '',
        'stocksAmount[1]': c['stocksAmount[1]'] || '0', ean: c.ean || '', packageAmount: String(p.v.n), packageUnitId: c.packageUnitId || '',
        measureAmount: c.measureAmount || '', measureUnitId: c.measureUnitId || '', 'packageDimensions[weight]': c['packageDimensions[weight]'] || '0',
        availabilityId: c.availabilityId, availabilityInStockId: c.availabilityInStockId,
        variantImage: id === g.main ? (M.cs['shop_images[]'] || '').split('|')[0] : p.newImg
      });
      const chk = (await getForm('/admin/pridat-variantu/?id=' + v + '&language=cs')).o;
      if (chk.code !== c.code.toUpperCase() && chk.code !== c.code) throw new Error('kód varianty ' + v + ' = ' + chk.code);
      log.push('varianta ' + p.v.label + ': kód ' + chk.code + ', ' + chk['pricelistPrice[1]'] + ' Kč, sklad ' + chk['stocksAmount[1]']);
    }
    // 5) hlavní výrobek CZ a SK
    const sorted = ids.map(id => P[id].v).sort((a, b) => a.n - b.n || (a.refill ? 1 : -1));
    for (const lang of ['cs', 'sk']) {
      const cur = await prod(g.main, lang); const o = cur.o, set = {};
      const nm = base(o.name); set.name = nm;
      set.seoTitle = nm + ' ' + joinVals(sorted, lang) + ' | KosmetikaEva.eu';
      const mv = M.v.n + ' ' + M.v.u, alt = sorted.map(v => v.label).join(lang === 'sk' ? ' alebo ' : ' nebo ');
      if (o.metaDescription && o.metaDescription.indexOf(mv) >= 0) set.metaDescription = o.metaDescription.replace(mv, alt).slice(0, 300);
      // popis: řádek Objem/Hmotnost
      const desc = cur.f.querySelector('[name=description]') ? new FormData(cur.f).get('description') : '';
      const mm = desc.match(LINE);
      if (mm && desc.split(mm[0]).length === 2) {
        const parts = [mm[3].trim()];
        for (const id of g.others) { const od = P[id][lang].description || ''; const om = od.match(LINE); if (om) parts.push(om[3].trim()); }
        if (parts.length === ids.length) set.description = desc.replace(mm[0], mm[1] + parts.join(lang === 'sk' ? ' alebo ' : ' nebo '));
      }
      if (lang === 'cs') {
        // doplňkové parametry: rozdílné hodnoty spojit „ / “
        const fdx = new FormData(cur.f); const names = fdx.getAll('textPropertyName[]'), vals = fdx.getAll('textPropertyValue[]');
        const others = g.others.map(id => { const n = (P[id].cs['textPropertyName[]'] || '').split('|'), v = (P[id].cs['textPropertyValue[]'] || '').split('|'); const m = {}; n.forEach((x, i) => m[x] = v[i]); return m; });
        const nv = vals.map((v, i) => { const all = [v, ...others.map(m => m[names[i]])].filter(x => x !== undefined && x !== ''); const u = [...new Set(all)]; return u.length > 1 ? u.join(' / ') : v; });
        set['__props'] = JSON.stringify({ names, nv });
        for (const id of g.others) for (const k in P[id].cs) if (/^informationParameterId\[/.test(k) && !(k in o)) set[k] = P[id].cs[k];
        for (const id of g.others) if (P[id].newImg) set['alts[' + P[id].newImg + ']'] = P[id].cs.name;
      }
      const props = set['__props'] ? JSON.parse(set['__props']) : null; delete set['__props'];
      const fd2 = new FormData(cur.f); for (const k in set) fd2.set(k, set[k]);
      if (props) { fd2.delete('textPropertyName[]'); fd2.delete('textPropertyValue[]'); props.names.forEach((n, i) => { fd2.append('textPropertyName[]', n); fd2.append('textPropertyValue[]', props.nv[i]); }); }
      fd2.set('buttonAction', 'saveAndStay'); fd2.set('__csrf__', shoptet.csrf.token);
      await fetch(cur.f.getAttribute('action'), { method: 'POST', body: fd2 });
      log.push(lang + ': ' + set.name + ' | ' + set.seoTitle + (set.description ? ' | popis upraven' : ' | popis beze změny') + (set.metaDescription ? ' | meta upraven' : ''));
    }
    // CZ SEO titulek po uložení SK zkontrolovat
    const csNow = (await prod(g.main, 'cs')).o; if (!/KosmetikaEva/.test(csNow.seoTitle || '')) log.push('POZOR: CZ seoTitle prázdný');
    // 6) skrýt druhé výrobky + přesměrování
    const mainPath = M.path, mainSk = M.skPath;
    for (const id of g.others) {
      const { f } = await prod(id, 'cs'); await post(f, { visibility: '0' });
      const s1 = await redirect(P[id].path, mainPath); const s2 = P[id].skPath && mainSk ? await redirect(P[id].skPath, mainSk) : 'bez SK';
      log.push('skryto ' + id + ', přesměrování ' + P[id].path + ' → ' + mainPath + ' (' + s1 + '), SK ' + P[id].skPath + ' (' + s2 + ')');
    }
    return log;
  };
})();
