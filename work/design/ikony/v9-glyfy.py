"""Nové glyfy pro ke-ikony-v9.js (23. 10. 2026, majitel: „projdi celý web a ikony podoplňuj“, „i u ostatních výrobků“).
Vrstvy jako v GL: f výplň (vínový gradient), s tmavá, h lesk, c světlá, l čáry tmavé, l2 čáry světlé. Plátno 24×24.
Výstup: v9-glyfy.json, v9-ikony.json (seznam [klíč, glyf, CZ, SK, CZ popisek, SK popisek])."""
import json, math

def f(x):
    s = ('%.2f' % x).rstrip('0').rstrip('.')
    return '0' if s in ('-0', '') else s

def pt(p):
    return f(p[0]) + ' ' + f(p[1])

def circle(cx, cy, r):
    return 'M%s %sa%s %s 0 1 1 0 %sa%s %s 0 1 1 0 -%sz' % (f(cx), f(cy - r), f(r), f(r), f(2 * r), f(r), f(r), f(2 * r))

def ellipse_rot(cx, cy, rx, ry, rot, n=28):
    a = math.radians(rot)
    pts = []
    for i in range(n):
        t = 2 * math.pi * i / n
        x, y = rx * math.cos(t), ry * math.sin(t)
        pts.append((cx + x * math.cos(a) - y * math.sin(a), cy + x * math.sin(a) + y * math.cos(a)))
    return 'M' + 'L'.join(pt(p) for p in pts) + 'z'

def polar(c, ang, r):
    a = math.radians(ang)
    return (c[0] + r * math.cos(a), c[1] + r * math.sin(a))

def frame(base, tip):
    bx, by = base; tx, ty = tip
    dx, dy = tx - bx, ty - by; L = math.hypot(dx, dy)
    u = (dx / L, dy / L); v = (-u[1], u[0])
    return lambda k, m: (bx + k * dx + m * v[0], by + k * dy + m * v[1])

def leaf(base, tip, bulge):
    P = frame(base, tip)
    return ('M' + pt(base) + 'C' + pt(P(.25, bulge * 1.25)) + ' ' + pt(P(.75, bulge * 1.1)) + ' ' + pt(tip) +
            'C' + pt(P(.75, -bulge * 1.1)) + ' ' + pt(P(.25, -bulge * 1.25)) + ' ' + pt(base) + 'z')

G = {}

# --- Kolostrum: mléčná kapka se srdcem ---
G['colostrum'] = {
    'f': 'M12 2.2C14.2 6 18 9.4 18 14a6 6 0 0 1 -12 0C6 9.4 9.8 6 12 2.2z',
    'c': 'M12 18.4c-2.3-1.5-3.8-2.9-3.8-4.6 0-1.2 1-2.1 2.1-2.1.7 0 1.3.4 1.7.9.4-.5 1-.9 1.7-.9 1.2 0 2.1.9 2.1 2.1 0 1.7-1.5 3.1-3.8 4.6z',
    'h': 'M8.2 13.2c.1-2 1-3.8 2.2-5.4-.6 1.8-1 3.6-1.2 5.4-.3.5-.8.5-1 0z',
}

# --- Sléz: pět srdčitých (vykrojených) korunních lístků s žilkami, střední sloupek ---
M = (12, 12)
def mallow_petal(ang, L=9.4, W=3.5):
    P = frame(polar(M, ang, .6), polar(M, ang, L))
    return ('M' + pt(P(0, .55)) + 'C' + pt(P(.3, W)) + ' ' + pt(P(.72, W * 1.12)) + ' ' + pt(P(.95, W * .62)) +
            'Q' + pt(P(1.03, W * .2)) + ' ' + pt(P(.86, 0)) + 'Q' + pt(P(1.03, -W * .2)) + ' ' + pt(P(.95, -W * .62)) +
            'C' + pt(P(.72, -W * 1.12)) + ' ' + pt(P(.3, -W)) + ' ' + pt(P(0, -.55)) + 'z')
angs = [-90 + 72 * k for k in range(5)]
G['mallow'] = {
    'f': ' '.join(mallow_petal(a) for a in angs),
    'l2': ' '.join('M' + pt(polar(M, a, 2.6)) + 'L' + pt(polar(M, a, 7.4)) + ' M' + pt(polar(M, a - 9, 3.2)) + 'L' + pt(polar(M, a - 13, 6.6)) +
                   ' M' + pt(polar(M, a + 9, 3.2)) + 'L' + pt(polar(M, a + 13, 6.6)) for a in angs),
    'c': circle(12, 12, 1.9),
    's': '',
    'h': 'M6.1 7.4c.9-.9 2-1.5 3.2-1.7-.9.6-1.8 1.2-2.6 2-.3.1-.6 0-.6-.3z',
}
G['mallow'].pop('s')

# --- Oves: lata s převislými klásky na obloukovém stéble, dole travní list ---
stem = 'M12 22.8C11.6 16.6 11.4 9.6 12.4 2.6'
spik = [((12.3, 4.4), (15.0, 5.0), (16.8, 11.4)), ((12.1, 7.6), (9.0, 8.2), (7.2, 14.6)),
        ((11.9, 11.2), (14.8, 11.8), (16.4, 18.0)), ((12.4, 2.6), (12.5, 2.4), (13.0, 8.4))]
G['oat'] = {
    'f': ' '.join(leaf(b, t, 2.05) for a, b, t in spik) + ' ' + leaf((11.8, 19.8), (4.0, 17.6), 1.15),
    'l': stem + ' ' + ' '.join('M' + pt(a) + 'L' + pt(b) for a, b, t in spik[:3]),
    'h': ' '.join('M' + pt(frame(b, t)(.3, 1.0)) + 'Q' + pt(frame(b, t)(.5, 1.5)) + ' ' + pt(frame(b, t)(.7, .9)) + 'Q' + pt(frame(b, t)(.5, 1.1)) + ' ' + pt(frame(b, t)(.3, 1.0)) + 'z' for a, b, t in spik),
}

# --- Vinná réva: hrozen (6 bobulí), stopka, list, úponek ---
berries = [(7.7, 9.4), (12, 9.2), (16.3, 9.4), (9.8, 13.2), (14.2, 13.2), (12, 17.0), (8.0, 13.0 + 99)]
berries = berries[:6]
G['grape'] = {
    'f': ' '.join(circle(x, y, 2.3) for x, y in berries) + ' ' + leaf((12.8, 5.4), (20.2, 3.0), 2.0),
    'h': ' '.join(circle(x - .8, y - .8, .55) for x, y in berries),
    'l': 'M12 7C12 5.4 12.6 4.2 13.6 3.4 M11.4 6.2c-1.6-.1-2.6-1.1-2.5-2.3.1-.9 1.1-1.3 1.8-.7',
    'l2': 'M13.6 5.1L18.9 3.4',
}

# --- Řasy: tři zvlněné stélky z kamene ---
def blade(x0, y0, x1, y1, amp, w, waves, n=26):
    L = math.hypot(x1 - x0, y1 - y0); u = ((x1 - x0) / L, (y1 - y0) / L); v = (-u[1], u[0])
    cen = []; wid = []
    for i in range(n + 1):
        t = i / n
        o = amp * math.sin(t * waves * math.pi) * t
        c = (x0 + t * (x1 - x0) + o * v[0], y0 + t * (y1 - y0) + o * v[1])
        cen.append(c); wid.append(w * (math.sin(math.pi * min(t * 1.15, 1)) ** .55) * (1 - .25 * t) + .35 * (1 - t))
    left = [(c[0] + ww * v[0], c[1] + ww * v[1]) for c, ww in zip(cen, wid)]
    right = [(c[0] - ww * v[0], c[1] - ww * v[1]) for c, ww in zip(cen, wid)]
    poly = left + right[::-1]
    mid = 'M' + 'L'.join(pt(c) for c in cen[3:-4])
    return 'M' + 'L'.join(pt(p) for p in poly) + 'z', mid
b1 = blade(12, 21.4, 12.4, 2.2, 1.6, 1.7, 3)
b2 = blade(10.2, 21.4, 4.6, 6.4, 1.3, 1.45, 2.5)
b3 = blade(13.8, 21.4, 19.4, 7.6, 1.3, 1.45, 2.5)
G['seaweed'] = {
    'f': ' '.join(b[0] for b in (b1, b2, b3)),
    's': 'M6.2 23c1.4-2.2 3.6-2.9 5.8-2.9s4.4.7 5.8 2.9z',
    'l2': ' '.join(b[1] for b in (b1, b2, b3)),
}

# --- Peptidy: řetízek pěti „aminokyselin“ (kuličky spojené vazbami) ---
beads = [(4.2, 16.8, 2.5), (8.2, 7.6, 2.8), (12.2, 16.4, 2.6), (16.0, 7.2, 2.8), (19.8, 16.0, 2.5)]
def bond(a, b):
    (x0, y0, r0), (x1, y1, r1) = a, b
    L = math.hypot(x1 - x0, y1 - y0); u = ((x1 - x0) / L, (y1 - y0) / L)
    return 'M' + pt((x0 + u[0] * (r0 - .2), y0 + u[1] * (r0 - .2))) + 'L' + pt((x1 - u[0] * (r1 - .2), y1 - u[1] * (r1 - .2)))
G['peptide'] = {
    'f': ' '.join(circle(x, y, r) for x, y, r in beads),
    'h': ' '.join(circle(x - r * .35, y - r * .35, r * .3) for x, y, r in beads),
    'l': ' '.join(bond(beads[i], beads[i + 1]) for i in range(4)),
    'c': circle(8.2, 7.6, .8) + ' ' + circle(16.0, 7.2, .8),
}

# --- Kurkuma: oddenek s výběžky a plátek s letokruhy ---
G['turmeric'] = {
    'f': 'M2.6 12.8C2.2 10.8 3.6 9.4 5.4 9.6 6.4 8.2 8 7.4 9.6 7.2 10.4 5.6 12 4.6 13.6 5 15.2 5.4 15.8 7 15.1 8.3 14.5 9.4 13.2 10 11.8 10.2 11.2 11.6 9.8 12.6 8.2 12.8 7.2 14.2 5.4 14.8 4 14.3 3.2 14 2.7 13.5 2.6 12.8z ' +
         'M7.2 9.2C6.8 7.4 7 5.6 8 4.4 8.6 3.8 9.4 4.1 9.4 4.9 9.3 6.2 9.4 7.2 9.8 8.2z ' + circle(16.6, 16.4, 4.8),
    'c': circle(16.6, 16.4, 3.4),
    'l': circle(16.6, 16.4, 1.7) + ' ' + circle(16.6, 16.4, .3),
    'h': 'M4.2 11c.6-.6 1.4-.9 2.2-.9-.6.3-1.2.6-1.7 1.1-.2.1-.5 0-.5-.2z',
}

# --- Avokádo: rozpůlený plod s peckou ---
G['avocado'] = {
    'f': 'M12 2.2c2.7 0 4.1 2.7 4.7 5.5.5 2.4 2.5 4.1 2.5 7.6 0 4-3.2 6.8-7.2 6.8s-7.2-2.8-7.2-6.8c0-3.5 2-5.2 2.5-7.6.6-2.8 2-5.5 4.7-5.5z',
    'c': 'M12 4.6c1.9 0 2.9 2.1 3.3 4.2.4 1.9 2 3.3 2 6.1 0 3-2.4 5.1-5.3 5.1s-5.3-2.1-5.3-5.1c0-2.8 1.6-4.2 2-6.1.4-2.1 1.4-4.2 3.3-4.2z',
    'l': circle(12, 14.6, 2.55) + ' ' + circle(12, 14.6, 1.6) + ' ' + circle(12, 14.6, .7),
    'h': 'M8.4 12.4c.2-1.8.8-3.4 1.6-4.6-.3 1.5-.6 3-.8 4.6-.2.4-.6.4-.8 0z',
}

# --- Omega-3: ryba a kapka oleje ---
G['omega'] = {
    'f': 'M5.2 15.2c2.8-3.6 6.6-5.4 10.2-5.4 2.9 0 5.4 1.5 7 3.6-.1.5-.2.9-.4 1.3-1.6 2.3-4 3.7-6.6 3.7-3.6 0-7.4-1.6-10.2-3.2z M5.6 15.2L1.6 11.4C1.4 13.6 1.5 15.6 1.9 17.8z ' +
         'M8.6 1.8c1.1 1.9 2.8 3.4 2.8 5.3a2.8 2.8 0 0 1 -5.6 0c0-1.9 1.7-3.4 2.8-5.3z',
    'c': circle(18.6, 13.4, .85),
    'l2': 'M16.2 11c.8 1.3.9 2.9.2 4.4 M10.6 13.2c.6.6.6 1.4 0 2 M12.8 12.6c.6.6.6 1.4 0 2',
    'h': 'M6.8 6.8c.1-.9.5-1.7 1-2.4-.2.8-.4 1.6-.5 2.4-.1.2-.4.2-.5 0z',
}

# --- Doplněk stravy: lahvička s víčkem, štítek s lístkem ---
G['supplement'] = {
    'f': 'M8.4 6.6h7.2a2.4 2.4 0 0 1 2.4 2.4v10.8a2.4 2.4 0 0 1 -2.4 2.4H8.4A2.4 2.4 0 0 1 6 19.8V9a2.4 2.4 0 0 1 2.4-2.4z',
    's': 'M8.2 2.2h7.6a1 1 0 0 1 1 1v2.6a1 1 0 0 1 -1 1H8.2a1 1 0 0 1 -1-1V3.2a1 1 0 0 1 1-1z',
    'c': 'M8.2 10.4h7.6a.8.8 0 0 1 .8.8v6.4a.8.8 0 0 1 -.8.8H8.2a.8.8 0 0 1 -.8-.8v-6.4a.8.8 0 0 1 .8-.8z',
    'l': 'M10 16.9c.3-2.9 2.2-4.6 5-4.9-.2 2.8-2 4.6-5 4.9z M10.4 16.4L13.2 13.6',
    'l2': 'M9.6 3.2v2.6 M12 3.2v2.6 M14.4 3.2v2.6',
    'h': 'M7.4 9.4c.2-.9.8-1.5 1.6-1.8-.5.5-.9 1.1-1.1 1.8-.2.2-.4.2-.5 0z',
}

IK = [
    ['s_kolos', 'colostrum', 'Kolostrum', 'Kolostrum', 'Obsahuje kolostrum.', 'Obsahuje kolostrum.'],
    ['s_slez', 'mallow', 'Sléz', 'Slez', 'Obsahuje sléz.', 'Obsahuje slez.'],
    ['s_oves', 'oat', 'Oves', 'Ovos', 'Obsahuje oves.', 'Obsahuje ovos.'],
    ['s_reva', 'grape', 'Vinná réva', 'Vinič', 'Obsahuje vinnou révu.', 'Obsahuje vinič.'],
    ['s_rasy', 'seaweed', 'Řasy', 'Riasy', 'Obsahuje řasy.', 'Obsahuje riasy.'],
    ['s_peptid', 'peptide', 'Peptidy', 'Peptidy', 'Obsahuje peptidy.', 'Obsahuje peptidy.'],
    ['s_kurkuma', 'turmeric', 'Kurkuma', 'Kurkuma', 'Obsahuje kurkumu.', 'Obsahuje kurkumu.'],
    ['s_avokado', 'avocado', 'Avokádo', 'Avokádo', 'Obsahuje avokádo.', 'Obsahuje avokádo.'],
    ['s_omega', 'omega', 'Omega-3', 'Omega-3', 'Obsahuje omega-3 mastné kyseliny.', 'Obsahuje omega-3 mastné kyseliny.'],
    ['s_med', 'honey', 'Med', 'Med', 'Obsahuje med.', 'Obsahuje med.'],
    ['d_dopl', 'supplement', 'Doplněk stravy', 'Výživový doplnok', 'Doplněk stravy.', 'Výživový doplnok.'],
]

json.dump(G, open('v9-glyfy.json', 'w'), ensure_ascii=False, indent=1)
json.dump(IK, open('v9-ikony.json', 'w'), ensure_ascii=False, indent=1)
print('glyfy:', ', '.join(G), '| ikony:', ', '.join(r[0] for r in IK))
