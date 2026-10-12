"""Tři stylové návrhy vzhledu KosmetikaEva.eu – statické náhledy (ilustrační)."""
import subprocess, sys

PRODUKTY = [
    ('just_eucasol_crop.png', 'Just', 'Just Eucasol sprej', 'od 45 Kč', 'Detail'),
    ('essens_m024_crop.png', 'Essens', 'Essens Pánský parfém m024 50 ml', '499 Kč', 'Do košíku'),
    ('lr_colostrum_crop.png', 'LR', 'LR LIFETAKT Colostrum Kapsle 60 kapslí', '999 Kč', 'Do košíku'),
    ('eurona_praci_crop.png', 'Eurona', 'Eurona Prací prostředek na bílé a jemné světlé prádlo, 935 g', '319 Kč', 'Do košíku'),
]
FONTS = """
@font-face{font-family:Jost;src:url('fonts/Jost[wght].ttf');font-weight:100 900}
@font-face{font-family:Montserrat;src:url('fonts/Montserrat[wght].ttf');font-weight:100 900}
@font-face{font-family:'Tenor Sans';src:url('fonts/TenorSans-Regular.ttf')}
"""
BASE = """
*{box-sizing:border-box;margin:0;padding:0}
body{width:1280px;background:var(--bg);color:var(--ink);font-family:var(--body);-webkit-font-smoothing:antialiased}
.top{height:36px;display:flex;align-items:center;justify-content:space-between;padding:0 48px;font-size:12px;letter-spacing:.06em;background:var(--topbg);color:var(--topink)}
header{height:84px;display:flex;align-items:center;padding:0 48px;gap:48px;border-bottom:1px solid var(--line);background:var(--hbg)}
header img{height:44px}
nav{display:flex;gap:34px;flex:1}
nav a{font-size:var(--navfs);letter-spacing:var(--navls);text-transform:var(--navtt);color:var(--navink);text-decoration:none;font-weight:var(--navfw)}
.icons{display:flex;gap:22px;align-items:center;font-size:13px;color:var(--navink)}
.ico{width:20px;height:20px;border:1.6px solid currentColor;border-radius:50%}
.cart{font-weight:600}
.hero{display:flex;align-items:center;gap:40px;padding:var(--herop);background:var(--herobg);color:var(--heroink)}
.hero .t{flex:0 0 540px}
.eyebrow{font-size:12px;letter-spacing:.28em;text-transform:uppercase;color:var(--accent2);margin-bottom:18px}
.hero h1{font-family:var(--head);font-weight:var(--h1fw);font-size:var(--h1fs);line-height:1.12;letter-spacing:var(--h1ls);text-transform:var(--h1tt)}
.hero p{margin:18px 0 28px;font-size:15px;line-height:1.7;opacity:.85}
.hero .imgs{flex:1;display:flex;gap:18px;justify-content:flex-end}
.hero .imgs div{width:138px;height:190px;background:var(--heroimgbg);border-radius:var(--r);display:flex;align-items:center;justify-content:center;border:var(--heroimgborder)}
.hero .imgs img{max-width:80%;max-height:80%}
.btn{display:inline-block;background:var(--btn);color:var(--btnink);padding:15px 30px;font-size:12px;letter-spacing:.18em;text-transform:uppercase;border-radius:var(--btnr);font-weight:500;border:1px solid var(--btnborder)}
.btn.o{background:transparent;color:var(--ink);border:1px solid var(--ink)}
.usp{display:flex;justify-content:center;gap:90px;padding:30px 48px;border-bottom:1px solid var(--line);font-size:13px;letter-spacing:.04em;color:var(--muted)}
.usp b{color:var(--ink);font-weight:500;display:block;font-size:14px;margin-bottom:3px;letter-spacing:var(--uspls);text-transform:var(--usptt)}
.sec{padding:64px 48px 40px}
.sec h2{font-family:var(--head);text-align:center;font-weight:var(--h2fw);font-size:var(--h2fs);letter-spacing:var(--h2ls);text-transform:var(--h2tt)}
.sec .rule{width:44px;height:1px;background:var(--accent2);margin:18px auto 40px}
.grid{display:grid;grid-template-columns:repeat(4,1fr);gap:var(--gap)}
.card{background:var(--cardbg);border-radius:var(--r);padding:var(--cardp);border:var(--cardborder);box-shadow:var(--cardshadow);text-align:var(--cardalign)}
.card .im{height:230px;display:flex;align-items:center;justify-content:center;background:var(--imgbg);border-radius:var(--r)}
.card .im img{max-height:190px;max-width:80%}
.brand{margin-top:18px;font-size:11px;letter-spacing:.22em;text-transform:uppercase;color:var(--accent2)}
.name{margin-top:8px;font-size:14px;line-height:1.5;min-height:42px;color:var(--ink);font-weight:var(--namefw);letter-spacing:var(--namels)}
.price{margin:12px 0 16px;font-size:16px;font-weight:600;color:var(--ink)}
.stars{color:var(--star);font-size:12px;letter-spacing:2px;margin-top:10px}
.card .btn{padding:12px 22px;font-size:11px}
footer{background:var(--fbg);color:var(--fink);padding:48px 48px 30px;display:grid;grid-template-columns:1.3fr 1fr 1fr;gap:48px}
footer h4{font-family:var(--head);font-weight:var(--h2fw);font-size:17px;letter-spacing:var(--h2ls);text-transform:var(--h2tt);color:var(--fhead);margin-bottom:16px}
footer li{list-style:none;font-size:13px;line-height:2;opacity:.85}
footer li::before{content:'— ';color:var(--accent2)}
.label{position:absolute;top:12px;right:16px;background:#fff;color:#111;font:600 13px Montserrat;padding:6px 12px;border-radius:6px;box-shadow:0 2px 10px rgba(0,0,0,.15)}
"""

THEMES = {
'A': ('A – Černobílá elegance', """
--bg:#fff;--ink:#111;--muted:#6b6b6b;--line:#ececec;--topbg:#111;--topink:#f2f2f2;--hbg:#fff;
--body:Jost,sans-serif;--head:Jost,sans-serif;--navfs:12.5px;--navls:.2em;--navtt:uppercase;--navink:#111;--navfw:500;
--herop:72px 48px;--herobg:#fff;--heroink:#111;--heroimgbg:#fff;--heroimgborder:1px solid #ececec;--r:0px;
--accent2:#111;--h1fw:400;--h1fs:46px;--h1ls:.04em;--h1tt:uppercase;
--btn:#111;--btnink:#fff;--btnr:0;--btnborder:#111;--uspls:.12em;--usptt:uppercase;
--h2fw:400;--h2fs:26px;--h2ls:.24em;--h2tt:uppercase;--gap:28px;
--cardbg:#fff;--cardp:0 0 8px;--cardborder:0;--cardshadow:none;--cardalign:center;--imgbg:#fff;
--namefw:400;--namels:.02em;--star:#111;
--fbg:#111;--fink:#e8e8e8;--fhead:#fff;
"""),
'B': ('B – Zlatá noblesa', """
--bg:#fff;--ink:#141414;--muted:#6f6a63;--line:#ebe6dd;--topbg:#0f0f10;--topink:#cbb37f;--hbg:#fff;
--body:Montserrat,sans-serif;--head:'Tenor Sans',sans-serif;--navfs:12px;--navls:.18em;--navtt:uppercase;--navink:#141414;--navfw:500;
--herop:64px 48px;--herobg:#0f0f10;--heroink:#f5f1ea;--heroimgbg:#fff;--heroimgborder:1px solid #b39253;--r:2px;
--accent2:#b39253;--h1fw:400;--h1fs:38px;--h1ls:.06em;--h1tt:uppercase;
--btn:#b39253;--btnink:#0f0f10;--btnr:0;--btnborder:#b39253;--uspls:.12em;--usptt:uppercase;
--h2fw:400;--h2fs:28px;--h2ls:.2em;--h2tt:uppercase;--gap:28px;
--cardbg:#fff;--cardp:0 0 10px;--cardborder:1px solid #efeae1;--cardshadow:none;--cardalign:center;--imgbg:#fff;
--namefw:400;--namels:.01em;--star:#b39253;
--fbg:#0f0f10;--fink:#d9d4cb;--fhead:#cbb37f;
"""),
'C': ('C – Moderní boutique', """
--bg:#fff;--ink:#1c1b29;--muted:#6e6c7a;--line:#eeedf2;--topbg:#f6f5f8;--topink:#4a4858;--hbg:#fff;
--body:Montserrat,sans-serif;--head:Montserrat,sans-serif;--navfs:14px;--navls:.01em;--navtt:none;--navink:#1c1b29;--navfw:600;
--herop:56px 48px;--herobg:linear-gradient(120deg,#fff 0%,#fbf3f1 100%);--heroink:#1c1b29;--heroimgbg:#fff;--heroimgborder:0;--r:18px;
--accent2:#a3392a;--h1fw:700;--h1fs:44px;--h1ls:-.01em;--h1tt:none;
--btn:#a3392a;--btnink:#fff;--btnr:999px;--btnborder:#a3392a;--uspls:0;--usptt:none;
--h2fw:700;--h2fs:30px;--h2ls:-.01em;--h2tt:none;--gap:24px;
--cardbg:#fff;--cardp:14px 14px 18px;--cardborder:1px solid #f0eff3;--cardshadow:0 10px 30px rgba(28,27,41,.06);--cardalign:left;--imgbg:#fff;
--namefw:500;--namels:0;--star:#e0a100;
--fbg:#1c1b29;--fink:#d9d8e2;--fhead:#fff;
"""),
}

def page(key):
    title, vars_ = THEMES[key]
    cards = ''.join(f"""<div class="card"><div class="im"><img src="{img}"></div>
      <div class="brand">{b}</div><div class="stars">★★★★★</div><div class="name">{n}</div><div class="price">{p}</div>
      <span class="btn{' o' if bt=='Detail' else ''}">{bt}</span></div>""" for img,b,n,p,bt in PRODUKTY)
    hero_imgs = ''.join(f'<div><img src="{x[0]}"></div>' for x in PRODUKTY)
    return f"""<!doctype html><html lang="cs"><head><meta charset="utf-8"><style>{FONTS}:root{{{vars_}}}{BASE}</style></head><body style="position:relative">
<div class="label">{title}</div>
<div class="top"><span>Všeobecné obchodní podmínky · Doprava a platba</span><span>CZK · Čeština</span></div>
<header><img src="logo.webp"><nav><a>Doplňky stravy</a><a>Domácnost</a><a>Kosmetika</a><a>Parfémy</a><a>Dárkové poukazy</a></nav>
<div class="icons"><span class="ico"></span><span class="ico"></span><span class="cart">169 Kč</span></div></header>
<section class="hero"><div class="t"><div class="eyebrow">Just · LR · Eurona · Essens · Nahrin</div>
<h1>Kosmetika, parfémy a drogerie od značek, které znáte</h1>
<p>Stovky produktů skladem. Na Zásilkovnu zdarma od 2 500 Kč.</p><span class="btn">Vybrat z nabídky</span></div>
<div class="imgs">{hero_imgs}</div></section>
<div class="usp"><div><b>Poštovné od 80 Kč</b>Zásilkovna zdarma nad 2 500 Kč</div><div><b>Stovky produktů skladem</b>Připraveno k expedici</div><div><b>Hodnocení 4,9 z 5</b>545 hodnocení obchodu</div></div>
<section class="sec"><h2>Skladem a oblíbené</h2><div class="rule"></div><div class="grid">{cards}</div></section>
<footer><div><h4>Proč nakoupit u nás</h4><ul><li>Už 10 let prodáváme značky Just, LR, Eurona, Essens a Nahrin</li><li>Hodnocení obchodu 4,9 z 5</li><li>14 dní na vrácení zboží</li></ul></div>
<div><h4>Zákaznický servis</h4><ul><li>Obchodní podmínky</li><li>Doprava a platba</li><li>Kontaktní informace</li></ul></div>
<div><h4>Kontakt</h4><ul><li>+420 773 905 902</li><li>info@kosmetikaeva.eu</li></ul></div></footer>
</body></html>"""

for k in THEMES:
    open(f'navrh_{k}.html','w',encoding='utf-8').write(page(k))
print('ok')
