"""Nové glyfy pro ke-ikony-v8.js (23. 10. 2026) – složky séra Just Infiore / VJ:
protěž alpská, alpská růže (pěnišník rezavý), bakuchiol (semena babči), acmella.
Vrstvy jako v GL: f výplň (vínový gradient), s tmavá, h lesk, c světlá, l čáry tmavé, l2 čáry světlé. Plátno 24×24.
Výstup: v8-glyfy.json, v8-ikony.json (seznam [klíč, glyf, CZ, SK, CZ popisek, SK popisek])."""
import json, math

def f(x):
    s = ('%.2f' % x).rstrip('0').rstrip('.')
    return '0' if s in ('-0', '') else s

def pt(p):
    return f(p[0]) + ' ' + f(p[1])

def circle(cx, cy, r):
    return 'M%s %sa%s %s 0 1 1 0 %sa%s %s 0 1 1 0 -%sz' % (f(cx), f(cy - r), f(r), f(r), f(2 * r), f(r), f(r), f(2 * r))

def ellipse(cx, cy, rx, ry):
    return 'M%s %sa%s %s 0 1 1 0 %sa%s %s 0 1 1 0 -%sz' % (f(cx), f(cy - ry), f(rx), f(ry), f(2 * ry), f(rx), f(ry), f(2 * ry))

def polar(c, ang, r):
    a = math.radians(ang)
    return (c[0] + r * math.cos(a), c[1] + r * math.sin(a))

def frame(base, tip):
    bx, by = base; tx, ty = tip
    dx, dy = tx - bx, ty - by; L = math.hypot(dx, dy)
    u = (dx / L, dy / L); v = (-u[1], u[0])
    return lambda k, m: (bx + k * dx + m * v[0], by + k * dy + m * v[1])

def lance(base, tip, half, base_half=.35):
    """plstnatý listen protěže: úzká báze, nejširší ve 45 %, krátce zašpičatělý konec"""
    P = frame(base, tip)
    return ('M' + pt(P(0, base_half)) + 'C' + pt(P(.22, half)) + ' ' + pt(P(.62, half * .95)) + ' ' + pt(tip) +
            'C' + pt(P(.62, -half * .95)) + ' ' + pt(P(.22, -half)) + ' ' + pt(P(0, -base_half)) + 'z')

def leaf(base, tip, bulge):
    P = frame(base, tip)
    return ('M' + pt(base) + 'C' + pt(P(.25, bulge * 1.25)) + ' ' + pt(P(.75, bulge * 1.1)) + ' ' + pt(tip) +
            'C' + pt(P(.75, -bulge * 1.1)) + ' ' + pt(P(.25, -bulge * 1.25)) + ' ' + pt(base) + 'z')

G = {}

# --- Protěž alpská: hvězdice plstnatých listenů, uprostřed shluk drobných úborů ---
C = (12, 12.2)
bracts = [(-90, 10.9, 2.3), (-50, 9.9, 2.2), (-11, 10.7, 2.3), (29, 9.7, 2.2), (68, 10.6, 2.3),
          (108, 9.8, 2.2), (148, 10.7, 2.3), (188, 9.7, 2.2), (228, 10.5, 2.3)]
G['edelweiss'] = {
    'f': ' '.join(lance(polar(C, a, 1.6), polar(C, a, L), w) for a, L, w in bracts) + ' ' + circle(C[0], C[1], 3.7),
    'l2': ' '.join('M' + pt(polar(C, a, 4.5)) + 'L' + pt(polar(C, a, L - 3.0)) for a, L, w in bracts),
    'c': circle(C[0], C[1], 1.0) + ' ' + ' '.join(circle(*polar(C, a, 2.2), .92) for a in range(-90, 270, 60)),
    'h': 'M6.1 5.6c1.2 1.1 2.3 2.4 3.1 3.9-1.3-1-2.4-2.3-3.1-3.9z',
}

# --- Alpská růže (pěnišník rezavý): okolík pěti nálevkovitých květů, dva kožovité listy ---
U = (12, 12.6)
def funnel(ang, r1=7.6, r0=1.4, w0=.55, w1=2.9, lobes=5):
    P = frame(polar(U, ang, r0), polar(U, ang, r1))
    s = 'M' + pt(P(0, w0)) + 'C' + pt(P(.5, w0 * 1.4)) + ' ' + pt(P(.7, w1 * .75)) + ' ' + pt(P(1, w1))
    # zubatý okraj ústí (laloky)
    n = lobes
    for i in range(n):
        m0 = w1 - 2 * w1 * i / n; m1 = w1 - 2 * w1 * (i + 1) / n; mm = (m0 + m1) / 2
        s += 'Q' + pt(P(1.1, mm)) + ' ' + pt(P(1, m1))
    s += 'C' + pt(P(.7, -w1 * .75)) + ' ' + pt(P(.5, -w0 * 1.4)) + ' ' + pt(P(0, -w0)) + 'z'
    return s
flowers = [(-142, 8.0), (-90, 8.7), (-38, 8.0)]
G['alpenrose'] = {
    'f': ' '.join(funnel(a, L) for a, L in flowers) + ' ' + leaf((12, 17.6), (3.2, 20.6), 2.2) + ' ' + leaf((12, 17.6), (20.8, 20.6), 2.2),
    's': ' '.join(ellipse(*polar(U, a, L - .35), 1.0, .45) for a, L in []),
    'l': 'M12 22.8V13.4',
    'l2': ' '.join('M' + pt(polar(U, a, 3.0)) + 'L' + pt(polar(U, a, L - 1.2)) for a, L in flowers) +
          ' M11 18.1L5.2 20.2 M13 18.1L18.8 20.2',
    'h': 'M10.9 6.1c.2-.6.6-1.1 1.1-1.4-.3.5-.5 1-.6 1.6-.2.2-.4.1-.5-.2z',
}
G['alpenrose'].pop('s')

# --- Bakuchiol: kapka rostlinné látky nad třemi ledvinovitými semeny babči ---
def bean(cx, cy, rx, ry, rot):
    """ledvinovité semeno: elipsa s mělkým zářezem na jedné straně"""
    a = math.radians(rot); u = (math.cos(a), math.sin(a)); v = (-u[1], u[0])
    P = lambda x, y: (cx + x * u[0] + y * v[0], cy + x * u[1] + y * v[1])
    return ('M' + pt(P(-rx, 0)) + 'C' + pt(P(-rx, -ry * 1.35)) + ' ' + pt(P(rx, -ry * 1.35)) + ' ' + pt(P(rx, 0)) +
            'C' + pt(P(rx, ry * 1.15)) + ' ' + pt(P(rx * .35, ry * 1.05)) + ' ' + pt(P(0, ry * .55)) +
            'C' + pt(P(-rx * .35, ry * 1.05)) + ' ' + pt(P(-rx, ry * 1.15)) + ' ' + pt(P(-rx, 0)) + 'z')
seeds = [(6.4, 17.9, 3.0, 2.15, -28), (17.6, 17.9, 3.0, 2.15, 28), (12, 20.4, 3.1, 2.15, 0)]
def seed_arc(cx, cy, rx, ry, rot):
    """světlý lesk na hřbetu semene"""
    a = math.radians(rot); u = (math.cos(a), math.sin(a)); v = (-u[1], u[0])
    P = lambda x, y: (cx + x * u[0] + y * v[0], cy + x * u[1] + y * v[1])
    return 'M' + pt(P(-rx * .6, -ry * .45)) + 'Q' + pt(P(0, -ry * 1.15)) + ' ' + pt(P(rx * .6, -ry * .45))

def seed_hl(cx, cy, rx, ry, rot):
    """bílý lesk (srpek) na hřbetu semene"""
    a = math.radians(rot); u = (math.cos(a), math.sin(a)); v = (-u[1], u[0])
    P = lambda x, y: (cx + x * u[0] + y * v[0], cy + x * u[1] + y * v[1])
    return ('M' + pt(P(-rx * .62, -ry * .38)) + 'Q' + pt(P(-rx * .1, -ry * 1.05)) + ' ' + pt(P(rx * .45, -ry * .62)) +
            'Q' + pt(P(-rx * .1, -ry * .7)) + ' ' + pt(P(-rx * .62, -ry * .38)) + 'z')
G['bakuchiol'] = {
    'f': 'M12 1.8C13.4 4.6 16.6 7.4 16.6 10.6a4.6 4.6 0 0 1 -9.2 0C7.4 7.4 10.6 4.6 12 1.8z ' +
         ' '.join(bean(*s) for s in seeds),
    'h': 'M9.6 9.4c.2-1.6 1-2.9 2-4-.5 1.3-1 2.6-1.2 4.2-.2.5-.6.4-.8-.2z ' + ' '.join(seed_hl(*s) for s in seeds),
}

# --- Acmella: knoflíkovitý vejčitý úbor bez paprsků s tmavší špičkou, dva vstřícné listy ---
G['acmella'] = {
    'f': 'M12 2C14.7 3.9 16.1 7.3 15.8 10.3Q12 12.6 8.2 10.3C7.9 7.3 9.3 3.9 12 2z ' +
         leaf((12, 16.8), (3.4, 13.8), 2.35) + ' ' + leaf((12, 16.8), (20.6, 13.8), 2.35),
    's': 'M12 2C13.1 2.8 13.9 3.8 14.4 4.9Q12 4.3 9.6 4.9C10.1 3.8 10.9 2.8 12 2z',
    'c': ' '.join(circle(x, y, .4) for x, y in
                  [(11.1, 6.0), (12.9, 6.0), (10.1, 7.6), (12, 7.5), (13.9, 7.6),
                   (9.5, 9.3), (11.2, 9.3), (12.8, 9.3), (14.5, 9.3)]),
    'l': 'M12 11.6V22.8',
    'l2': 'M11.2 16.5L5.2 14.4 M12.8 16.5L18.8 14.4',
    'h': 'M9.2 7.4c.3-1.3.9-2.4 1.7-3.2-.4 1-.7 2.1-.9 3.2-.2.4-.6.4-.8 0z',
}

IK = [
    ['s_protez', 'edelweiss', 'Protěž alpská', 'Plesnivec alpínsky',
     'Obsahuje extrakt z protěže alpské.', 'Obsahuje extrakt z plesnivca alpínskeho.'],
    ['s_alpruze', 'alpenrose', 'Alpská růže', 'Alpská ruža',
     'Obsahuje alpskou růži (pěnišník rezavý).', 'Obsahuje alpskú ružu (rododendron hrdzavý).'],
    ['s_bakuch', 'bakuchiol', 'Bakuchiol', 'Bakuchiol',
     'Obsahuje bakuchiol – rostlinnou látku ze semen babči.', 'Obsahuje bakuchiol – rastlinnú látku zo semien babči.'],
    ['s_acmella', 'acmella', 'Acmella', 'Acmella',
     'Obsahuje extrakt z acmelly.', 'Obsahuje extrakt z acmelly.'],
]

json.dump(G, open('v8-glyfy.json', 'w'), ensure_ascii=False, indent=1)
json.dump(IK, open('v8-ikony.json', 'w'), ensure_ascii=False, indent=1)
print('glyfy:', ', '.join(G), '| ikony:', ', '.join(r[0] for r in IK))
