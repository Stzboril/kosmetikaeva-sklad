"""Nové glyfy pro ke-ikony-v4.js (24×24, vrstvy jako v GL: f výplň, s tmavá, h lesk, c světlá, l čáry tmavé, l2 čáry světlé)."""
import json, math

def f(x):
    s = ('%.2f' % x).rstrip('0').rstrip('.')
    return '0' if s in ('-0', '') else s

def pt(p):
    return f(p[0]) + ' ' + f(p[1])

def petal(c, ang, L, W, w2=None):
    """Lístek od středu c ve směru ang (stupně), délka L, šířka W."""
    w2 = W if w2 is None else w2
    a = math.radians(ang)
    u = (math.cos(a), math.sin(a)); v = (-u[1], u[0])
    P = lambda k, m: (c[0] + k * L * u[0] + m * v[0], c[1] + k * L * u[1] + m * v[1])
    T = P(1, 0)
    return ('M' + pt(c) + 'C' + pt(P(.3, W)) + ' ' + pt(P(.8, w2)) + ' ' + pt(T) +
            'C' + pt(P(.8, -w2)) + ' ' + pt(P(.3, -W)) + ' ' + pt(c) + 'z')

def circle(cx, cy, r):
    return 'M%s %sa%s %s 0 1 1 0 %sa%s %s 0 1 1 0 -%sz' % (f(cx), f(cy - r), f(r), f(r), f(2 * r), f(r), f(r), f(2 * r))

G = {}

# --- Máta: lodyha se třemi páry vejčitých lístků s žilkou ---
def leaf(base, tip, bulge):
    """lístek od báze k špičce, vyboulení na obě strany (bulge = poloviční šířka)"""
    bx, by = base; tx, ty = tip
    dx, dy = tx - bx, ty - by; L = math.hypot(dx, dy)
    u = (dx / L, dy / L); v = (-u[1], u[0])
    P = lambda k, m: (bx + k * dx + m * v[0], by + k * dy + m * v[1])
    return ('M' + pt(base) + 'C' + pt(P(.25, bulge * 1.25)) + ' ' + pt(P(.75, bulge * 1.1)) + ' ' + pt(tip) +
            'C' + pt(P(.75, -bulge * 1.1)) + ' ' + pt(P(.25, -bulge * 1.25)) + ' ' + pt(base) + 'z')

def serr_leaf(base, tip, half, teeth=4, depth=.45):
    """lístek se zoubkovaným okrajem (máta): obrys z bodů, zoubky střídavě ven/dovnitř"""
    bx, by = base; tx, ty = tip
    dx, dy = tx - bx, ty - by; L = math.hypot(dx, dy)
    u = (dx / L, dy / L); v = (-u[1], u[0])
    N = 2 * teeth * 3
    side = []
    for i in range(N + 1):
        k = i / N
        w = half * math.sin(math.pi * k ** .8) * (1 - .15 * k)
        if 0 < i < N and i % 3 == 1:
            w += depth * (1 - k * .5)
        side.append((k, w))
    P = lambda k, m: (bx + k * dx + m * v[0], by + k * dy + m * v[1])
    pts_ = [P(k, w) for k, w in side] + [P(k, -w) for k, w in reversed(side)][1:]
    return 'M' + 'L'.join(pt(p) for p in pts_) + 'z'

mint_leaves = [((11.5, 16.4), (2.2, 12.8), 3.4), ((12.5, 16.4), (21.8, 12.8), 3.4),
               ((11.6, 10.6), (4.6, 7.0), 2.7), ((12.4, 10.6), (19.4, 7.0), 2.7)]
G['mint'] = {
    'f': ' '.join(serr_leaf(b, t, w) for b, t, w in mint_leaves) + ' ' + serr_leaf((12, 7.8), (12, 1.6), 2.0, 3, .35),
    'l': 'M12 22.4V8',
    'l2': ' '.join('M' + pt(b) + 'L' + pt((b[0] + (t[0] - b[0]) * .8, b[1] + (t[1] - b[1]) * .8)) for b, t, w in mint_leaves) +
          ' M12 7.4L12 3',
    'h': 'M3.8 12.3c1.8-1.3 4-1.7 6-1-2-.1-4 .3-6 1z',
}

# --- Sporýš (verbena): štíhlé klasy s drobnými kvítky, dva kopinaté listy dole ---
fl_main = [(12.6, 1.9), (11.4, 3.7), (12.9, 5.3), (11.6, 7.0), (12.9, 8.6)]
fl_side = [(20.0, 5.0), (18.2, 6.0), (19.6, 7.6), (17.6, 8.8)]
G['verbena'] = {
    'f': ' '.join(circle(x, y, 1.4) for x, y in fl_main + fl_side) + ' ' +
         serr_leaf((12.2, 19.6), (2.0, 15.4), 2.5, 4, .4) + ' ' + serr_leaf((12.4, 16.2), (21.6, 12.4), 2.3, 4, .4),
    'c': ' '.join(circle(x, y, .5) for x, y in fl_main + fl_side),
    'l': 'M12.2 22.6C12.1 17 12.3 13 12.4 9.8 M12.4 13.4C14.2 11.6 15.8 10.4 17.2 9.4',
    'l2': 'M12.2 19.6L3.8 16.2 M12.4 16.2L19.8 13.2',
}

# --- Limetka: půlkolečko se segmenty, slupka, lísteček ---
cx, cy, R, r = 13.4, 18.6, 8.6, 6.3
seg = ' '.join('M%s %sL%s' % (f(cx), f(cy), pt((cx + r * math.cos(math.radians(t)), cy - r * math.sin(math.radians(t)))))
               for t in (150, 120, 90, 60, 30))
# celá limetka (ovál se špičkou) vzadu vlevo nahoře + list, vpředu půlkolečko
# celá limetka (protáhlý ovál se špičkami, šikmo) vzadu, vpředu kolečko se segmenty a tmavým obrysem
def rot(p, c, a):
    a = math.radians(a); x, y = p[0] - c[0], p[1] - c[1]
    return (c[0] + x * math.cos(a) - y * math.sin(a), c[1] + x * math.sin(a) + y * math.cos(a))
LC, LA = (10.0, 8.4), -20
def L_(x, y): return pt(rot((LC[0] + x, LC[1] + y), LC, LA))
lime_path = ('M' + L_(-8.4, 0) + 'C' + L_(-7.6, -.5) + ' ' + L_(-6.4, -5.8) + ' ' + L_(0, -5.8) +
             'C' + L_(6.4, -5.8) + ' ' + L_(7.6, -.5) + ' ' + L_(8.4, 0) +
             'C' + L_(7.6, .5) + ' ' + L_(6.4, 5.8) + ' ' + L_(0, 5.8) +
             'C' + L_(-6.4, 5.8) + ' ' + L_(-7.6, .5) + ' ' + L_(-8.4, 0) + 'z')
SC2, SR, Sr = (16.4, 16.4), 6.4, 4.5
G['lime'] = {
    'f': lime_path + ' ' + circle(SC2[0], SC2[1], SR),
    's': circle(SC2[0], SC2[1], Sr),
    'l': circle(SC2[0], SC2[1], SR + .1),
    'l2': ' '.join('M' + pt(SC2) + 'L' + pt((SC2[0] + (Sr - .3) * math.cos(math.radians(a)), SC2[1] + (Sr - .3) * math.sin(math.radians(a))))
                   for a in range(0, 360, 45)) + ' ' + circle(SC2[0], SC2[1], Sr),
    'h': 'M' + L_(-5.6, -2.6) + 'Q' + L_(-2, -5) + ' ' + L_(2.4, -4.6) + 'Q' + L_(-1.6, -3.8) + ' ' + L_(-5.6, -2.6) + 'z',
}

# --- Jasmín: pět protáhlých okvětních lístků, střed, poupě na stonku ---
jc = (10.4, 10.2)
JA = (-100, -28, 44, 116, 188)
G['jasmine'] = {
    'f': ' '.join(petal(jc, a, 8.8, 3.3, 2.9) for a in JA) + ' ' +
         petal((19.6, 15.0), -100, 4.6, 1.5, 1.2) + ' ' + leaf((17.4, 20.6), (22.8, 17.0), 1.6),
    'c': circle(jc[0], jc[1], 1.9),
    's': ' '.join(circle(jc[0] + 1.1 * math.cos(math.radians(a + 36)), jc[1] + 1.1 * math.sin(math.radians(a + 36)), .38)
                  for a in JA),
    'l': 'M15.4 16.6C17.2 18.4 18.4 20.4 19 22.6 M18.2 19.6C18.8 18 19.4 16.6 19.6 15',
    'l2': ' '.join('M' + pt((jc[0] + 2.6 * math.cos(math.radians(a)), jc[1] + 2.6 * math.sin(math.radians(a)))) +
                   'L' + pt((jc[0] + 6.8 * math.cos(math.radians(a)), jc[1] + 6.8 * math.sin(math.radians(a))))
                   for a in JA),
}

# --- Cedr: šiška se šupinami, stopka ---
def scallops(x0, x1, y, n, d=1.5):
    w = (x1 - x0) / n
    return 'M%s %s' % (f(x0), f(y)) + ''.join('q%s %s %s 0' % (f(w / 2), f(d), f(w)) for _ in range(n))
# šiška = elipsa, šupiny = mřížka šikmých oblouků uvnitř elipsy
ECX, ECY, ERX, ERY = 12.0, 11.4, 7.0, 9.8
def chord(x0, y0, dx, dy, shrink=.55):
    """úsečka přímky (x0,y0)+t(dx,dy) uvnitř elipsy, mírně zkrácená"""
    a = (dx / ERX) ** 2 + (dy / ERY) ** 2
    b = 2 * ((x0 - ECX) * dx / ERX ** 2 + (y0 - ECY) * dy / ERY ** 2)
    c = ((x0 - ECX) / ERX) ** 2 + ((y0 - ECY) / ERY) ** 2 - 1
    D = b * b - 4 * a * c
    if D <= 0: return ''
    t1 = (-b - math.sqrt(D)) / (2 * a); t2 = (-b + math.sqrt(D)) / (2 * a)
    L = (t2 - t1) * math.hypot(dx, dy)
    if L < 2.2: return ''
    s = shrink / math.hypot(dx, dy)
    p1 = (x0 + (t1 + s) * dx, y0 + (t1 + s) * dy); p2 = (x0 + (t2 - s) * dx, y0 + (t2 - s) * dy)
    # lehké prohnutí dolů = vypouklost šišky
    m = ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2 + .9)
    return 'M' + pt(p1) + 'Q' + pt(m) + ' ' + pt(p2)
lat = []
for k in range(-6, 7):
    y0 = ECY + k * 2.9
    lat.append(chord(ECX, y0, 1, .62)); lat.append(chord(ECX, y0, -1, .62))
G['cone'] = {
    'f': 'M%s %sa%s %s 0 1 1 0 %sa%s %s 0 1 1 0 -%sz' % (f(ECX), f(ECY - ERY), f(ERX), f(ERY), f(2 * ERY), f(ERX), f(ERY), f(2 * ERY)),
    's': 'M10.9 20.6h2.2v2.6h-2.2z',
    'l2': ' '.join(x for x in lat if x),
    'h': 'M6.4 9.4c.5-3 2-5.4 4.2-6.6-1.7 1.9-3 4.1-4.2 6.6z',
}

# --- Rakytník: větvička s úzkými listy a hroznem kulatých bobulí ---
berries = [(8.2, 13.4), (10.8, 12.6), (9.6, 15.8), (12.4, 15.0), (7.0, 16.6), (10.6, 18.6), (13.4, 17.6), (8.2, 19.4)]
G['buckthorn'] = {
    'f': ' '.join(circle(x, y, 1.75) for x, y in berries),
    'h': ' '.join(circle(x - .6, y - .6, .5) for x, y in berries),
    's': ' '.join([leaf((11.6, 10.6), (3.6, 2.6), 1.7), leaf((14.0, 8.4), (12.8, .6), 1.6),
                   leaf((16.2, 6.4), (23.2, 2.4), 1.55), leaf((14.0, 8.4), (22.6, 10.6), 1.6)]),
    'l': 'M3.4 22.4C8.6 16.6 13 11.2 20.4 3.4',
    'l2': 'M11.6 10.6L5 4 M14 8.4L13 2 M16.2 6.4L21.8 3.2 M14 8.4L21 10.2',
}

# --- Sacha inchi: hvězdicovitá tobolka s pěti zaoblenými cípy a švy ---
sc = (12.0, 12.6); RO, RI, A0 = 11.0, 5.8, -90
pts = []
for i in range(10):
    a = math.radians(A0 + i * 36)
    rr = RO if i % 2 == 0 else RI
    pts.append((sc[0] + rr * math.cos(a), sc[1] + rr * math.sin(a)))
def mid(p, n): return ((p[0] + n[0]) / 2, (p[1] + n[1]) / 2)
path = 'M' + pt(mid(pts[-1], pts[0]))
for i in range(10):
    path += 'Q' + pt(pts[i]) + ' ' + pt(mid(pts[i], pts[(i + 1) % 10]))
path += 'z'
# tmavé plošky: pravá polovina každého cípu (střed → špička → vnitřní bod) = plastický lusk
sh = lambda p, k: (sc[0] + (p[0] - sc[0]) * k, sc[1] + (p[1] - sc[1]) * k)
fac = ' '.join('M' + pt(sc) + 'L' + pt(sh(pts[i], .8)) + 'Q' + pt(sh(mid(pts[i], pts[(i + 1) % 10]), .97)) + ' ' +
               pt(sh(pts[(i + 1) % 10], .97)) + 'z' for i in range(0, 10, 2))
G['sacha'] = {
    'f': path,
    's': fac,
    'c': circle(sc[0], sc[1], 1.5),
    'h': 'M6.6 10.4c1.2-.3 2.4-.3 3.6 0-1.2.1-2.4.1-3.6 0z',
}

if __name__ == '__main__':
    import sys
    json.dump(G, open(sys.argv[1], 'w'), ensure_ascii=False, indent=1)
    print('glyfy:', ', '.join(G))
