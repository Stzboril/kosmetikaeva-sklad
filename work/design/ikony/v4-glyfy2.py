"""Další glyfy pro ke-ikony-v4.js – složky napříč e-shopem (24×24, vrstvy f/s/h/c/l/l2)."""
import json, math, sys
from glyfy import f, pt, petal, circle, leaf, serr_leaf, rot, G as G1

G = {}

def ring(cx, cy, R, r):
    """mezikruží (výplň evenodd) – vnější kruh + vnitřní opačně"""
    return (circle(cx, cy, R) + ' ' +
            'M%s %sa%s %s 0 1 0 0 %sa%s %s 0 1 0 0 -%sz' % (f(cx), f(cy - r), f(r), f(r), f(2 * r), f(r), f(r), f(2 * r)))

def arcband(cx, cy, R, r, a0, a1):
    """výseč mezikruží od úhlu a0 do a1 (stupně, 0 = vpravo, po směru hodin)"""
    def P(rr, a): a = math.radians(a); return (cx + rr * math.cos(a), cy + rr * math.sin(a))
    large = 1 if (a1 - a0) % 360 > 180 else 0
    return ('M' + pt(P(R, a0)) + 'A%s %s 0 %d 1 %s' % (f(R), f(R), large, pt(P(R, a1))) +
            'L' + pt(P(r, a1)) + 'A%s %s 0 %d 0 %s' % (f(r), f(r), large, pt(P(r, a0))) + 'z')

def rect(x, y, w, h):
    return 'M%s %sh%sv%sh-%sz' % (f(x), f(y), f(w), f(h), f(w))

def poly(*ps):
    return 'M' + 'L'.join(pt(p) for p in ps) + 'z'

# ---------- písmena (plné tvary, tloušťka t) v rámečku x..x+w, y..y+h ----------
def L_C(x, y, w, h, t):
    cx, cy = x + w / 2, y + h / 2; R = h / 2; r = R - t
    return arcband(cx, cy, R, r, 40, 320)
def L_E(x, y, w, h, t):
    return ' '.join([rect(x, y, t, h), rect(x, y, w, t), rect(x, y + h / 2 - t / 2, w * .85, t), rect(x, y + h - t, w, t)])
def L_D(x, y, w, h, t):
    R = h / 2; r = R - t; cx = x + w - R
    return ' '.join([rect(x, y, t, h), rect(x, y, cx - x + .01, t), rect(x, y + h - t, cx - x + .01, t), arcband(cx, y + R, R, r, -90, 90)])
def L_B(x, y, w, h, t):
    R1 = h / 4; r1 = R1 - t * .95; cx = x + w - R1
    return ' '.join([rect(x, y, t, h), rect(x, y, cx - x + .01, t), rect(x, y + h / 2 - t / 2, cx - x + .01, t), rect(x, y + h - t, cx - x + .01, t),
                     arcband(cx, y + R1, R1, r1, -90, 90), arcband(cx, y + 3 * R1, R1, r1, -90, 90)])
def L_A(x, y, w, h, t):
    top = (x + w / 2, y); bl = (x, y + h); br = (x + w, y + h)
    k = t / math.cos(math.atan((w / 2) / h))
    left = poly(bl, (top[0] - k / 2, y), (top[0] + k / 2, y), (bl[0] + k, y + h))
    right = poly((br[0] - k, y + h), (top[0] - k / 2, y), (top[0] + k / 2, y), br)
    cy = y + h * .62
    return ' '.join([left, right, rect(x + w * .24, cy, w * .52, t * .9)])
def L_1(x, y, w, h, t):
    cx = x + w / 2
    return ' '.join([rect(cx - t / 2, y, t, h), poly((cx - t / 2, y), (cx - t / 2 - w * .35, y + h * .28), (cx - t / 2 - w * .35, y + h * .28 + t * .9), (cx - t / 2, y + t * 1.2))])
def L_0(x, y, w, h, t):
    cx, cy = x + w / 2, y + h / 2
    rx, ry = w / 2, h / 2
    return ('M%s %sa%s %s 0 1 1 0 %sa%s %s 0 1 1 0 -%sz' % (f(cx), f(y), f(rx), f(ry), f(h), f(rx), f(ry), f(h)) + ' ' +
            'M%s %sa%s %s 0 1 0 0 %sa%s %s 0 1 0 0 -%sz' % (f(cx), f(y + t), f(rx - t), f(ry - t), f(h - 2 * t), f(rx - t), f(ry - t), f(h - 2 * t)))
def L_Q(x, y, w, h, t):
    return L_0(x, y, w, h, t) + ' ' + poly((x + w * .52, y + h * .62), (x + w * .66, y + h * .55), (x + w * 1.08, y + h * .98), (x + w * .92, y + h * 1.05))
def L_5(x, y, w, h, t):
    R = h * .3; r = R - t; cx = x + w - R - .1; cy = y + h - R
    return ' '.join([rect(x + .2, y, w - .2, t), rect(x + .2, y, t, h * .45), rect(x + .2, cy - R, cx - x - .2 + .01, t),
                     arcband(cx, cy, R, r, -90, 140)])
LET = {'C': L_C, 'E': L_E, 'D': L_D, 'B': L_B, 'A': L_A, '1': L_1, '0': L_0, 'Q': L_Q, '5': L_5}

def letters(s, cx, cy, h, t, w=None, gap=.9):
    w = w or h * .78
    ws = [w * (.62 if ch in '1' else 1) for ch in s]
    tot = sum(ws) + gap * (len(s) - 1); x = cx - tot / 2; out = []
    for ch, wi in zip(s, ws):
        out.append(LET[ch](x, cy - h / 2, wi, h, t)); x += wi + gap
    return ' '.join(out)

# ---------- vitaminy: tableta s písmenem ----------
def vitamin(s, h=8.4, t=2.0):
    return {'f': circle(12, 12, 9.6), 's': ring(12, 12, 9.6, 8.2),
            'c': letters(s, 12, 12.2, h, t), 'h': 'M5 9.4c.9-2.4 2.8-4.2 5.2-4.9-1.9 1.2-3.6 2.9-5.2 4.9z'}
for s in ('A', 'B', 'C', 'D', 'E'):
    G['vit' + s] = vitamin(s)
# panthenol = provitamin B5: kapka s „B5“
G['panth'] = {'f': 'M12 1.8C15.6 6.4 19 10.2 19 14.6a7 7 0 0 1-14 0C5 10.2 8.4 6.4 12 1.8z',
              'c': letters('B5', 12, 15.0, 6.6, 1.6, w=4.6, gap=.7),
              'h': 'M7.2 13.2c.3-2.2 1.4-4.2 3.2-6-1 2-1.8 3.9-2.2 6z'}
# Q10: molekula – kroužek s „Q10“
G['q10'] = {'f': circle(12, 12, 9.8), 's': ring(12, 12, 9.8, 8.4),
            'c': letters('Q10', 12, 12, 6.6, 1.6, w=4.4, gap=.6),
            'h': 'M4.8 9.6c.9-2.4 2.8-4.2 5.2-4.9-1.9 1.2-3.6 2.9-5.2 4.9z'}
# minerály: broušený krystal
G['mineral'] = {'f': poly((12, 2.2), (19.6, 7.2), (19.6, 16.6), (12, 21.8), (4.4, 16.6), (4.4, 7.2)),
                's': poly((12, 2.2), (19.6, 7.2), (12, 9.8)) + ' ' + poly((19.6, 7.2), (19.6, 16.6), (15.2, 14.4), (15.2, 11.2), (12, 9.8)) + ' ' +
                     poly((12, 21.8), (15.2, 14.4), (19.6, 16.6)),
                'c': poly((12, 9.8), (15.2, 11.2), (15.2, 14.4), (12, 16), (8.8, 14.4), (8.8, 11.2)),
                'h': poly((4.4, 7.2), (12, 2.2), (8.8, 11.2))}
# kyselina hyaluronová: kapka s řetízkem molekul
G['hyal'] = {'f': 'M12 1.8C15.6 6.4 19 10.2 19 14.6a7 7 0 0 1-14 0C5 10.2 8.4 6.4 12 1.8z',
             'c': ' '.join(circle(x, y, 1.35) for x, y in ((9.2, 16.8), (12, 13.2), (14.8, 16.8), (12, 9.6))),
             'l2': 'M9.2 16.8L12 13.2L14.8 16.8 M12 13.2V9.6 M9.2 16.8h5.6',
             'h': 'M7.2 13.2c.3-2.2 1.4-4.2 3.2-6-1 2-1.8 3.9-2.2 6z'}
# kolagen: trojitá šroubovice
def helix(phase, amp=4.2, x0=12, y0=2.2, y1=21.8, n=60):
    ps = []
    for i in range(n + 1):
        y = y0 + (y1 - y0) * i / n
        ps.append((x0 + amp * math.sin(2 * math.pi * (y - y0) / 9.8 + phase), y))
    return ps
def band(ps, w):
    L, R = [], []
    for i in range(len(ps)):
        a = ps[max(0, i - 1)]; b = ps[min(len(ps) - 1, i + 1)]
        dx, dy = b[0] - a[0], b[1] - a[1]; d = math.hypot(dx, dy) or 1
        nx, ny = -dy / d, dx / d
        L.append((ps[i][0] + nx * w / 2, ps[i][1] + ny * w / 2)); R.append((ps[i][0] - nx * w / 2, ps[i][1] - ny * w / 2))
    return 'M' + 'L'.join(pt(p) for p in L + R[::-1]) + 'z'
G['collagen'] = {'f': band(helix(0), 2.0) + ' ' + band(helix(2 * math.pi / 3), 2.0),
                 's': band(helix(4 * math.pi / 3), 2.0),
                 'h': 'M7.6 4.4c.6-.8 1.4-1.4 2.2-1.6-.6.6-1.2 1.2-2.2 1.6z'}
# heřmánek: kopretinovité kvítky (světlé okvětí, tmavý střed) + menší kvítek
def daisy(c, n, L, W, rc, rot0=0):
    pet = ' '.join(petal(c, rot0 + i * 360 / n, L, W, W * .8) for i in range(n))
    return pet, circle(c[0], c[1], rc)
p1, c1 = daisy((10.2, 10.2), 12, 8.2, 1.35, 3.1)
p2, c2 = daisy((18.6, 17.8), 10, 4.6, .95, 1.8, 10)
G['chamomile'] = {'f': p1 + ' ' + p2, 's': c1 + ' ' + c2,
                  'h': circle(9.2, 9.2, .9) + ' ' + circle(18, 17.2, .55),
                  'l': 'M14.6 16.4C16 18.2 16.8 20.2 17 22.6'}
# arnika: méně širších okvětních lístků se zoubkem na špičce + listy
def notched(c, ang, L, W):
    a = math.radians(ang); u = (math.cos(a), math.sin(a)); v = (-u[1], u[0])
    P = lambda k, m: (c[0] + k * L * u[0] + m * v[0], c[1] + k * L * u[1] + m * v[1])
    return ('M' + pt(c) + 'C' + pt(P(.3, W)) + ' ' + pt(P(.75, W * 1.1)) + ' ' + pt(P(1, W * .7)) +
            'L' + pt(P(.9, 0)) + 'L' + pt(P(1, -W * .7)) + 'C' + pt(P(.75, -W * 1.1)) + ' ' + pt(P(.3, -W)) + ' ' + pt(c) + 'z')
ac = (12, 10)
G['arnica'] = {'f': ' '.join(notched(ac, -90 + i * 360 / 9, 8.4, 1.6) for i in range(9)) + ' ' +
                    leaf((12, 21.4), (4.4, 17.6), 1.6) + ' ' + leaf((12, 21.4), (19.6, 17.6), 1.6),
               's': circle(ac[0], ac[1], 2.6), 'c': ' '.join(circle(ac[0] + 1.2 * math.cos(math.radians(a)), ac[1] + 1.2 * math.sin(math.radians(a)), .35) for a in range(0, 360, 60)),
               'l': 'M12 18.4V22.6'}
# měsíček: plný květ se dvěma řadami lístků
mc = (12, 11.6)
G['calendula'] = {'f': ' '.join(petal(mc, i * 360 / 16, 9.6, 1.25, 1.1) for i in range(16)),
                  's': ' '.join(petal(mc, 11.25 + i * 360 / 16, 6.4, 1.1, .9) for i in range(16)) + ' ' + circle(mc[0], mc[1], 2.6),
                  'c': circle(mc[0], mc[1], 1.4)}
# třapatka: vysoký střed (kužel), lístky skloněné dolů, stonek
G['echinacea'] = {'f': ' '.join(petal((12, 9.2), a, 8.6, 1.5, 1.2) for a in (170, 150, 128, 104, 76, 52, 30, 10)),
                  's': 'M7.4 9.2c0-3.6 2-6.4 4.6-6.4s4.6 2.8 4.6 6.4c-1.4.8-3 1.2-4.6 1.2s-3.2-.4-4.6-1.2z',
                  'c': ' '.join(circle(x, y, .45) for x, y in ((10, 6.4), (12, 5.2), (14, 6.4), (11, 8.2), (13, 8.2), (12, 4))),
                  'l': 'M12 10.4V22.6'}
# růže: květ s točitými lístky
G['rose'] = {'f': 'M12 3.4c4.6 0 8 3.2 8 7.6 0 4.6-3.6 7.6-8 7.6s-8-3-8-7.6c0-4.4 3.4-7.6 8-7.6z',
             'l2': 'M12 7.2c2.2 0 3.6 1.4 3.6 3.2s-1.6 3.2-3.6 3.2-3-1.2-3-2.6 1-2.4 2.4-2.4 2 .8 2 1.8-.6 1.4-1.4 1.4 M8 5.6c-1.6 1.4-2.4 3.2-2.2 5.4 M16 5.6c1.6 1.4 2.4 3.2 2.2 5.4 M7 15.4c1.6 1.4 3.2 1.8 5 1.8s3.4-.4 5-1.8',
             's': leaf((12, 18.4), (4.4, 21.4), 1.5) + ' ' + leaf((12, 18.4), (19.6, 21.4), 1.5),
             'h': 'M6.2 9.6c.4-2.2 1.8-3.8 3.8-4.6-1.5 1.2-2.8 2.7-3.8 4.6z'}
# šípek: dvě oválné šípky s kalichem na větvičce
def hip(cx, cy, rx, ry, a):
    pts_ = [rot((cx + rx * math.cos(t), cy + ry * math.sin(t)), (cx, cy), a) for t in [i * 2 * math.pi / 40 for i in range(40)]]
    return 'M' + 'L'.join(pt(p) for p in pts_) + 'z'
G['rosehip'] = {'f': hip(8.6, 14.6, 3.4, 5.4, -20) + ' ' + hip(16.2, 15.6, 3.2, 5.0, 18),
                's': ' '.join(poly(rot((x, y - ry - .2), (x, y), a), rot((x - 2.2, y - ry - 2.4), (x, y), a), rot((x, y - ry - 1.2), (x, y), a), rot((x + 2.2, y - ry - 2.4), (x, y), a))
                              for x, y, ry, a in ((8.6, 14.6, 5.4, -20), (16.2, 15.6, 5.0, 18))) + ' ' + leaf((12.4, 4.4), (20.6, 2.2), 1.4),
                'l': 'M6.6 8.8C8 6 10 4.6 12.4 4.4 M17.8 10.4C17 7.2 15 5.2 12.4 4.4',
                'h': hip(7.4, 12.8, .7, 1.6, -20) + ' ' + hip(15.2, 13.8, .65, 1.5, 18)}
# levandule: tři klasy z drobných kvítků
def spike(base, top, n, r0):
    out = []
    for i in range(n):
        k = i / (n - 1)
        x = base[0] + (top[0] - base[0]) * k; y = base[1] + (top[1] - base[1]) * k
        rr = r0 * (1 - .45 * k)
        off = (1 if i % 2 else -1) * rr * .55
        out.append(circle(x + off, y, rr))
    return ' '.join(out)
G['lavender'] = {'f': spike((7.6, 12.4), (5.4, 2.4), 6, 1.35) + ' ' + spike((12, 11.2), (12, 1.4), 6, 1.4) + ' ' + spike((16.4, 12.4), (18.6, 2.4), 6, 1.35),
                 'l': 'M7.6 13.4C8.6 16.8 10.4 19.6 12 22.4 M12 12.2V22.4 M16.4 13.4C15.4 16.8 13.6 19.6 12 22.4',
                 's': leaf((11.6, 19.4), (5.8, 17.4), .9) + ' ' + leaf((12.4, 19.4), (18.2, 17.4), .9)}
# eukalyptus: větvička s kulatými párovými listy
def roundleaf(c, r, a):
    return hip(c[0], c[1], r, r * .82, a)
eu = [((7.4, 17.4), 3.4, -30), ((16.6, 14.4), 3.4, 30), ((7.8, 9.8), 3.0, -30), ((16.2, 6.8), 2.8, 30), ((11.6, 3.2), 2.3, 0)]
G['eucalyptus'] = {'f': ' '.join(roundleaf(c, r, a) for c, r, a in eu),
                   'l': 'M12 22.8C12 17 12 11 11.6 5 M12 17.6L10.2 17.4 M12 14.6L13.6 14.4 M12 10.2L10.4 10 M11.9 7.2L13.6 7',
                   'l2': ' '.join('M' + pt(rot((c[0] - r * .7, c[1]), c, a)) + 'L' + pt(rot((c[0] + r * .7, c[1]), c, a)) for c, r, a in eu)}
# rozmarýn: větvička s hustým jehlicovitým listím
rz = []
for i in range(9):
    y = 20 - i * 2.0; s = 1 if i % 2 else -1
    rz.append(leaf((12, y), (12 + s * (5.2 - i * .25), y - 2.2), .55))
    rz.append(leaf((12, y - .6), (12 - s * (4.4 - i * .2), y - 2.6), .5))
G['rosemary'] = {'f': ' '.join(rz) + ' ' + leaf((12, 3.2), (12, .8), .55), 'l': 'M12 23V2.4'}
# šalvěj: tři měkké oválné listy se síťkou žilek
G['sage'] = {'f': leaf((12, 13.6), (12, 1.4), 3.6) + ' ' + leaf((11.6, 15.8), (2.4, 9.8), 3.2) + ' ' + leaf((12.4, 15.8), (21.6, 9.8), 3.2),
             'l': 'M12 22.6V13',
             'l2': 'M12 13.2V3 M12 6.4L9.8 4.8 M12 6.4L14.2 4.8 M12 9.4L9.4 7.6 M12 9.4L14.6 7.6 M11.6 15.6L3.6 10.4 M7.8 13.2L7.4 10.6 M12.4 15.6L20.4 10.4 M16.2 13.2L16.6 10.6',
             'h': 'M9.4 9.6c-.4-2.6 0-5 1.4-7.2-.6 2.4-1 4.8-1.4 7.2z'}
# tymián: rozvětvené stonky s drobnými oválnými lístky
ty = []
for (bx, by, tx, ty_) in ((12, 22.4, 12, 2.6), (12, 15, 5.4, 6.4), (12, 13, 18.6, 5.4)):
    for k in (.25, .45, .65, .85):
        x = bx + (tx - bx) * k; y = by + (ty_ - by) * k
        ty.append(hip(x - 1.5, y + .2, 1.45, .85, -25)); ty.append(hip(x + 1.5, y + .2, 1.45, .85, 25))
G['thyme'] = {'f': ' '.join(ty) + ' ' + circle(12, 2.4, .9) + ' ' + circle(5.2, 6.2, .8) + ' ' + circle(18.8, 5.2, .8),
              'l': 'M12 22.6V3 M12 15L5.6 6.6 M12 13L18.4 5.6'}
# jalovec: bobule + jehlice
G['juniper'] = {'f': ' '.join(circle(x, y, 2.3) for x, y in ((9.2, 15.4), (13.8, 16.8), (11.4, 19.6), (15.2, 12.6))),
                'h': ' '.join(circle(x - .8, y - .8, .6) for x, y in ((9.2, 15.4), (13.8, 16.8), (11.4, 19.6), (15.2, 12.6))),
                's': ' '.join(leaf((x, y), (x + dx, y + dy), .45) for x, y, dx, dy in
                              ((6, 13, -2.6, -3.6), (8, 10.6, -.6, -4.8), (10.4, 8.2, 1.6, -4.6), (12.6, 6, 3.2, -3.8), (14.8, 4, 4.6, -2.4),
                               (8, 10.6, 3.6, -1.6), (10.4, 8.2, 4.2, -.2), (12.6, 6, 4.6, 1.2))),
                'l': 'M3.4 16.6C7 12.6 11 7.6 18.6 2.6'}
# tea tree: úzké listy na větvičce + kapka oleje
G['teatree'] = {'s': ' '.join(leaf((x, y), (x + dx, y + dy), .55) for x, y, dx, dy in
                              ((7, 15, -4, -2), (7, 15, -1.4, -4.4), (9.6, 12, -2.6, -4.2), (9.6, 12, 1, -4.6), (12.4, 9, -1, -5), (12.4, 9, 3, -3.6),
                               (15, 6, 1.6, -4.4), (15, 6, 4.6, -1.6))),
                'l': 'M3.2 19C7.6 14.8 12 10 17.6 3.6',
                'f': 'M17.4 11.4c1.8 2.4 3.4 4.4 3.4 6.4a3.4 3.4 0 0 1-6.8 0c0-2 1.6-4 3.4-6.4z',
                'h': 'M15.2 17.4c.2-1.2.8-2.2 1.6-3.2-.4 1-.8 2-1.6 3.2z'}
# zelený čaj: vršek čajovníku – dva listy a pupen
G['tealeaf'] = {'f': serr_leaf((12, 16), (3, 9.2), 3.4, 5, .3) + ' ' + serr_leaf((12, 14), (20.6, 6.4), 3.2, 5, .3) + ' ' + leaf((12, 12.2), (12.6, 1.6), 1.7),
                'l': 'M12 22.6V12',
                'l2': 'M12 16L4.2 10 M12 14L19.4 7.2 M12 12L12.5 3',
                'h': 'M4.6 11.6c1.8-1.8 4-2.6 6.4-2.4-2.3.4-4.4 1.2-6.4 2.4z'}
# zázvor: hlízovitý kořen se sukovitými výběžky
G['ginger'] = {'f': 'M3.2 14.6c-.6-2 .6-3.6 2.4-3.6.8-2 2.8-2.6 4.2-1.6.4-2.4 2.4-3.8 4.4-3.2 1.6.4 2.2 2 1.8 3.4 1.8-.8 3.8 0 4.2 1.8.4 1.4-.4 2.8-1.6 3.2 1.4.8 1.8 2.6.8 3.8-1.2 1.4-3.2 1-4.2 0-.8 1.6-2.6 2.4-4.2 1.8-1.2-.4-1.8-1.4-1.8-2.4-1.4.8-3.4.6-4.2-.8-.6-1-.4-2 .4-2.4-1.2 0-2.2-.6-2.4-2z',
               'l2': 'M7.4 12.6c.6 1 .6 2 0 3 M12.2 9.4c.8.8 1 1.8.6 2.8 M15.6 13.8c.8.6 1.2 1.6.8 2.6 M10.6 16.2c.6.4 1 .9 1 1.6',
               's': 'M14.4 6.2c.2-1.6 1.2-3 2.8-3.6-.4 1.4-.6 2.8-.4 4.2z',
               'h': 'M5 13.2c.6-.9 1.4-1.4 2.4-1.6-.7.5-1.5 1-2.4 1.6z'}
# kokos: půlka s dužinou + celý ořech
G['coconut'] = {'f': circle(15.8, 7.2, 5.4) + ' ' + 'M2.8 14.4A9.2 9.2 0 0 0 21.2 14.4z',
                'c': 'M2.8 14.4a9.2 3.2 0 1 0 18.4 0a9.2 3.2 0 1 0-18.4 0z',
                's': 'M5.2 14.4a6.8 2.2 0 1 0 13.6 0a6.8 2.2 0 1 0-13.6 0z ' + ' '.join(circle(x, y, .75) for x, y in ((14.2, 5.6), (17.4, 5.4), (15.8, 8.2))),
                'h': 'M4.6 17.6c1 2 2.6 3.4 4.6 4.1-1.9-.2-3.6-1.6-4.6-4.1z M11.6 5.2c.6-1.6 1.8-2.8 3.4-3.3-1.2.9-2.4 1.9-3.4 3.3z'}
# kakao: lusk s žebry + bob
G['cacao'] = {'f': hip(11, 10.4, 5.6, 8.6, 32),
              'l2': ' '.join('M' + pt(rot((11 + dx, 10.4 - 7.6), (11, 10.4), 32)) + 'Q' + pt(rot((11 + dx * 1.7, 10.4), (11, 10.4), 32)) + ' ' + pt(rot((11 + dx, 10.4 + 7.6), (11, 10.4), 32)) for dx in (-2.4, 0, 2.4)),
              's': hip(18.4, 18.6, 2.6, 3.6, -30) + ' M5.6 3.6l-1.6-1.8 .9-.8 1.8 1.8z',
              'c': 'M' + pt(rot((18.4, 15.6), (18.4, 18.6), -30)) + 'Q' + pt(rot((17.8, 18.6), (18.4, 18.6), -30)) + ' ' + pt(rot((18.4, 21.6), (18.4, 18.6), -30)) + 'Q' + pt(rot((18.9, 18.6), (18.4, 18.6), -30)) + ' ' + pt(rot((18.4, 15.6), (18.4, 18.6), -30)) + 'z',
              'h': hip(7.6, 7.6, .8, 2.4, 32)}
# mandle: tři mandle (kapkovitý tvar s rýhováním)
def almond(c, a, L=4.6, W=2.6):
    x, y = c
    p = ('M' + pt(rot((x, y - L), c, a)) + 'C' + pt(rot((x + W * 1.1, y - L * .5), c, a)) + ' ' + pt(rot((x + W, y + L * .7), c, a)) + ' ' + pt(rot((x, y + L * .9), c, a)) +
         'C' + pt(rot((x - W, y + L * .7), c, a)) + ' ' + pt(rot((x - W * 1.1, y - L * .5), c, a)) + ' ' + pt(rot((x, y - L), c, a)) + 'z')
    ln = ' '.join('M' + pt(rot((x + dx, y - L * .4), c, a)) + 'Q' + pt(rot((x + dx * 1.3, y + L * .1), c, a)) + ' ' + pt(rot((x + dx * .8, y + L * .6), c, a)) for dx in (-.9, .5))
    return p, ln
a1, l1 = almond((6.8, 14.2), -28, 5.8, 3.2); a2, l2_ = almond((17.2, 14.2), 28, 5.8, 3.2); a3, l3 = almond((12, 9.2), 0, 6.2, 3.4)
G['almond'] = {'f': a1 + ' ' + a2 + ' ' + a3, 'l2': ' '.join([l1, l2_, l3]),
               'h': 'M10.6 7.4c.2-1.4.8-2.4 1.4-3.2-.3 1-.6 2-1.4 3.2z'}
# oliva: větvička se dvěma olivami
G['olive'] = {'s': ' '.join(leaf((x, y), (x + dx, y + dy), 1.05) for x, y, dx, dy in
                            ((6.4, 16.4, -3.6, -4.8), (9.2, 13.4, 4.6, -3.6), (11.8, 10.6, -4.4, -3.6), (14.4, 7.8, 4.8, -2.6), (16.8, 5, 1.6, -4.2))),
              'l': 'M3.4 20.6C8 15.6 12.6 10.6 18.6 3.6 M9.2 13.4C10 15 10.6 16.4 10.8 17.6 M14.4 7.8C15.8 9.6 16.8 11.4 17.2 13.2',
              'f': hip(11.4, 19.4, 2.6, 3.4, -25) + ' ' + hip(17.8, 15.6, 2.4, 3.2, -25),
              'h': hip(10.5, 18.2, .6, 1.2, -25) + ' ' + hip(16.9, 14.4, .55, 1.1, -25)}
# jojoba: dvě semena (žaludovitá) a dva protilehlé listy
G['jojoba'] = {'f': hip(9, 15.8, 3.2, 4.6, -15) + ' ' + hip(15.6, 15.4, 3.0, 4.4, 15),
               's': leaf((12, 8.6), (3.2, 4.6), 1.7) + ' ' + leaf((12, 8.6), (20.8, 4.6), 1.7) + ' ' +
                    ' '.join(poly(rot((x - 2.2, y - 3.2), (x, y), a), rot((x, y - 4.8), (x, y), a), rot((x + 2.2, y - 3.2), (x, y), a), rot((x, y - 2.4), (x, y), a))
                             for x, y, a in ((9, 15.8, -15), (15.6, 15.4, 15))),
               'l': 'M12 2.4V9.6 M12 9.6L9.6 11.6 M12 9.6L14.8 11.4',
               'h': hip(7.8, 15.4, .6, 1.8, -15) + ' ' + hip(14.5, 15, .55, 1.7, 15)}
# argan: plody (oválné) na trnité větvičce + kapka oleje
G['argan'] = {'f': hip(7.6, 9.4, 2.6, 3.6, -20) + ' ' + hip(13.2, 7.2, 2.4, 3.4, 15) + ' M16.6 12.4c1.9 2.6 3.6 4.6 3.6 6.8a3.6 3.6 0 0 1-7.2 0c0-2.2 1.7-4.2 3.6-6.8z',
              's': leaf((10.6, 3.6), (3.6, 2.4), 1.0) + ' ' + leaf((10.6, 3.6), (18.6, 2), 1.0),
              'l': 'M2.6 21C5.4 14.6 8 9.6 10.6 3.6 M7.4 13.4L4 14.2 M5.2 17.4L8.2 18.6',
              'h': 'M14.6 18.6c.2-1.3.8-2.4 1.7-3.4-.4 1.1-.9 2.2-1.7 3.4z'}
# bambucké máslo: miska se zmrzlinovou „čepicí“ másla a ořech
G['shea'] = {'f': 'M3 13.6h18a9 9 0 0 1-18 0z',
             'c': 'M5.6 13.6c-.4-2.2 1.2-3.8 3.4-3.4.4-2 2.4-3.2 4.4-2.4 1.6-1.2 4.2-.4 4.6 1.8 1.6.6 2.4 2.2 1.8 4z',
             's': 'M3 13.6h18v.9H3z ' + hip(17.4, 5.2, 2.2, 3.0, 35),
             'l2': 'M8.4 12.4c1.4-1 2.8-1 4.2 0 M12.6 10.4c1.2-.8 2.4-.8 3.6 0',
             'h': 'M5.4 16.2c.6 1.8 1.8 3.2 3.4 4-1.4-.4-2.6-1.6-3.4-4z'}
# mentol: šestiboký krystal a lísteček máty
G['menthol'] = {'f': poly((9, 4), (13.4, 6.4), (13.4, 13.6), (9, 16), (4.6, 13.6), (4.6, 6.4)) + ' ' + poly((16.4, 12.2), (19.4, 13.8), (19.4, 18.6), (16.4, 20.2), (13.4, 18.6), (13.4, 13.8)),
                's': poly((9, 4), (13.4, 6.4), (9, 8.8)) + ' ' + poly((13.4, 6.4), (13.4, 13.6), (9, 11.2), (9, 8.8)) + ' ' + poly((16.4, 12.2), (19.4, 13.8), (16.4, 15.4)),
                'f2': serr_leaf((14.4, 9.6), (21.6, 2.8), 2.2, 3, .3),
                'l2': 'M14.4 9.6L20 4.4',
                'h': poly((4.6, 6.4), (9, 4), (7, 9.4))}

for g in G.values():
    if 'f2' in g: g['f'] = g['f'] + ' ' + g.pop('f2')

if __name__ == '__main__':
    json.dump(G, open(sys.argv[1], 'w'), ensure_ascii=False, indent=1)
    print(len(G), 'glyfů:', ', '.join(G))
