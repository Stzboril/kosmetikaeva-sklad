// Obrázek na Facebook 1080×1350 – JUST: Sérum na kuperózu, Oční sprej, Alpský bylinný balzám (29. 10. 2026)
// Spouští se na stránce www.kosmetikaeva.eu (Montserrat je tam načtený, fotky z cdn.myshoptet.com mají CORS).
// Výsledek: window.keFbImg (data URL JPEG) + localStorage keFbDraft20261029.
(async () => {
  const W = 1080, H = 1350;
  const INK = '#1c1b29', SOFT = '#3f3d4f', MUTED = '#6e6c7a', LINE = '#eeedf2', BLUSH = '#fbf3f1', ACC = '#a3392a';
  const ORIG = 'https://cdn.myshoptet.com/usr/www.kosmetikaeva.eu/user/shop/orig/';
  const P = [
    { img: ORIG + '9808_serum-na-kuperosu-kompozice-web.png?6aad156c', name: 'Sérum na kuperózu 30\u00a0ml', line: 'pro citlivou pleť se sklonem k začervenání', price: '589\u00a0Kč', tag: 'NOVINKA' },
    { img: ORIG + '7726_ocni-sprej-kompozice-web.png?6aaecd2d', name: 'Oční sprej 18\u00a0ml', line: 'osvěží oční okolí', price: '718\u00a0Kč' },
    { img: ORIG + '8715_alpsky-balzam-kompozice.png?674ee46e', name: 'Alpský bylinný balzám 13\u00a0ml', line: 'svěží vůně alpských bylin a mentolu', price: '675\u00a0Kč' },
  ];
  await document.fonts.load('700 40px Montserrat');
  await document.fonts.load('500 30px Montserrat');
  await document.fonts.load('600 30px Montserrat');
  const load = (src) => new Promise((res, rej) => { const i = new Image(); i.crossOrigin = 'anonymous'; i.onload = () => res(i); i.onerror = rej; i.src = src; });
  const imgs = await Promise.all(P.map((p) => load(p.img)));

  const c = document.createElement('canvas'); c.width = W; c.height = H;
  const g = c.getContext('2d');
  const rr = (x, y, w, h, r) => { g.beginPath(); g.moveTo(x + r, y); g.arcTo(x + w, y, x + w, y + h, r); g.arcTo(x + w, y + h, x, y + h, r); g.arcTo(x, y + h, x, y, r); g.arcTo(x, y, x + w, y, r); g.closePath(); };
  const wrap = (text, maxW) => { const words = text.split(' '); /* \u00a0 drží číslo s jednotkou */ const lines = []; let cur = ''; for (const w of words) { const t = cur ? cur + ' ' + w : w; if (g.measureText(t).width > maxW && cur) { lines.push(cur); cur = w; } else cur = t; } if (cur) lines.push(cur); return lines; };
  const spaced = (text, x, y, sp) => { let cx = x; for (const ch of text) { g.fillText(ch, cx, y); cx += g.measureText(ch).width + sp; } };

  // pozadí
  g.fillStyle = '#ffffff'; g.fillRect(0, 0, W, H);
  g.fillStyle = BLUSH; g.fillRect(0, 0, W, 330);

  // hlavička
  g.textBaseline = 'alphabetic'; g.textAlign = 'left';
  g.fillStyle = ACC; g.font = '700 26px Montserrat'; spaced('ŠVÝCARSKÁ PÉČE JUST', 72, 118, 4);
  g.fillStyle = INK; g.font = '700 76px Montserrat'; g.fillText('Péče na chladné dny', 68, 206);
  g.fillStyle = SOFT; g.font = '500 36px Montserrat'; g.fillText('pleť  ·  oční okolí  ·  tělo', 72, 268);

  // karty
  const X = 56, CW = W - 2 * X, CH = 268, GAP = 26; let y = 300;
  P.forEach((p, i) => {
    g.save(); g.shadowColor = 'rgba(28,27,41,0.08)'; g.shadowBlur = 30; g.shadowOffsetY = 8;
    rr(X, y, CW, CH, 28); g.fillStyle = '#ffffff'; g.fill(); g.restore();
    rr(X, y, CW, CH, 28); g.strokeStyle = LINE; g.lineWidth = 2; g.stroke();
    // fotka (poměr 4:3)
    const im = imgs[i]; const bw = 330, bh = 248; const s = Math.min(bw / im.naturalWidth, bh / im.naturalHeight);
    const iw = im.naturalWidth * s, ih = im.naturalHeight * s; const ix = X + 20 + (bw - iw) / 2, iy = y + (CH - ih) / 2;
    g.save(); rr(X + 20, y + 10, bw, CH - 20, 20); g.clip(); g.drawImage(im, ix, iy, iw, ih); g.restore();
    // text
    const tx = X + 20 + bw + 34, tw = X + CW - 34 - tx; let ty = y + 70;
    if (p.tag) { g.font = '700 20px Montserrat'; const w = g.measureText(p.tag).width + 30; rr(tx, ty - 40, w, 34, 10); g.fillStyle = ACC; g.fill(); g.fillStyle = '#ffffff'; spaced(p.tag, tx + 14, ty - 16, 1.5); ty += 22; }
    g.fillStyle = INK; g.font = '700 38px Montserrat';
    const nl = wrap(p.name, tw); nl.forEach((l) => { g.fillText(l, tx, ty); ty += 46; });
    g.fillStyle = MUTED; g.font = '500 26px Montserrat';
    const ll = wrap(p.line, tw); ll.forEach((l) => { g.fillText(l, tx, ty + 2); ty += 34; });
    g.fillStyle = ACC; g.font = '700 44px Montserrat'; g.fillText(p.price, tx, Math.min(ty + 44, y + CH - 30));
    y += CH + GAP;
  });

  // pruh dole
  const by = y + 4, bh2 = H - by - 48;
  rr(X, by, CW, bh2, 24); g.fillStyle = ACC; g.fill();
  g.fillStyle = '#ffffff'; g.font = '700 34px Montserrat'; g.textAlign = 'left';
  g.fillText('Doprava zdarma od 2 500 Kč', X + 40, by + bh2 / 2 + 12);
  g.font = '600 30px Montserrat'; g.textAlign = 'right';
  g.fillText('kosmetikaeva.eu', X + CW - 40, by + bh2 / 2 + 11);
  g.textAlign = 'left';

  const url = c.toDataURL('image/jpeg', 0.9);
  window.keFbImg = url;
  try { localStorage.setItem('keFbDraft20261029', url); } catch (e) { /* plná paměť */ }
  return { bytes: Math.round(url.length * 0.75), bottomBand: [by, bh2] };
})();
