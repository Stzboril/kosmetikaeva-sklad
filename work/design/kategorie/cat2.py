# Kresby dalších 34 kategorií – slonovina a zlato, jemná linka (100×100, jako lux2.py; rámeček dodá seal2.py)
import math
from lux2 import M, D, O, BGF, spark, leaf, roundleaf
F = 'fill="url(#gold)"'
def P(d, a=M): return f'<path d="{d}" {a}/>'
def C(x, y, r, a=M): return f'<circle cx="{x}" cy="{y}" r="{r}" {a}/>'
def E(x, y, rx, ry, a=M, rot=0): return f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" transform="rotate({rot} {x} {y})" {a}/>'
def G(t, s): return f'<g transform="{t}">{s}</g>'
def drop(x, y, s=1, a=F):  # kapka se špičkou nahoře, (x,y) = špička
    return P(f'M{x} {y}c{1.7*s:.2f} {2.3*s:.2f} {3*s:.2f} {3.8*s:.2f} {3*s:.2f} {5.3*s:.2f}a{3*s:.2f} {3*s:.2f} 0 0 1-{6*s:.2f} 0c0-{1.5*s:.2f} {1.3*s:.2f}-{3*s:.2f} {3*s:.2f}-{5.3*s:.2f}z', a)
def slender(x, y, ang, l, w, a=D, vein=True):  # úzký list (olivový, čajový)
    s = f'<path d="M0 0Q{l*.5} {-w} {l} 0Q{l*.5} {w} 0 0Z" {a}/>'
    if vein: s += f'<path d="M1 0H{l*.85}" {D} opacity=".6"/>'
    return G(f'translate({x} {y}) rotate({ang})', s)
def bean(x, y, ang, s=1):  # kávové zrno
    return G(f'translate({x} {y}) rotate({ang}) scale({s})', E(0, 0, 4.2, 6, O) + P('M0 -5.4C-1.8 -2 1.8 2 0 5.4', D))
def flower5(x, y, r):  # pětilistý kvítek
    return ''.join(G(f'rotate({a} {x} {y})', E(x, y - r, r * .55, r * .9, D)) for a in range(0, 360, 72)) + C(x, y, r * .35, O)

I = {}

# ---------- KOSMETIKA ----------
# Ruce a nehty – lahvička laku na nehty a tuba krému na ruce
tube = (P('M-2 -6.4H0V6.4H-2z', O) + P('M0 -6.2L21 -4.6Q24.6 -4 25.4 -2.6V2.6Q24.6 4 21 4.6L0 6.2Z', O) +
        P('M25.4 -2.8H32V2.8H25.4z', O) + P('M3 -2.4H17 M3 1H13', D) + P('M-1 -6.4V6.4', D, ))
I['Ruce a nehty'] = (
    G('translate(28 70) rotate(-48)', tube) +
    P('M55 52h16a3 3 0 0 1 3 3v19a4 4 0 0 1-4 4H56a4 4 0 0 1-4-4V55a3 3 0 0 1 3-3z', O) +
    P('M58.6 47h8.8v5h-8.8z', O) + P('M58 25.6a2 2 0 0 1 2-2h6a2 2 0 0 1 2 2V47H58z', O) +
    P('M61.4 27v17 M64.6 27v17', D) + P('M55.4 70h17', D) + P('M56.4 58v12', D, ) +
    drop(63, 60, .8) + spark(36, 34, 2.4) + spark(78, 36, 1.6) + spark(30, 46, 1.2))
# Nohy a chodidla – noha z boku štětcovou linkou, kvítek, hladina
from taper import brush
I['Nohy a chodidla'] = (
    brush('M46 16C46 30 47 42 50.4 50C53.8 58 60.4 63.8 70 67.6C74.6 69.4 79 70 80.6 72.6', 1.9, start=.04, end=.08) +
    brush('M80.6 72.6C81.4 75.2 78.4 76.4 74.6 76C67 75.2 59 76.4 52 77.4C45.6 78.4 39.6 79 37 75.6C34.4 72.2 35.6 65 36.2 58C37 46 37.4 30 37 16', 1.9, start=.06, end=.04) +
    brush('M74.6 70.2C75.8 71.6 76 73.4 75.2 75.2', .7, start=.2, end=.2) + brush('M70.6 68.8C71.6 70.4 71.6 72.6 70.8 74.6', .6, start=.2, end=.2) +
    brush('M40.6 57.4C42 55.6 43.8 55.6 45.2 57.4', .6, start=.2, end=.2) +
    P('M30 84c5-2 10-2 15 0s10 2 15 0 10-2 15 0', D) + flower5(26, 66, 3.4) + leaf(24.4, 72, 120, 6, 2.2) +
    spark(64, 34, 2.4) + spark(72, 46, 1.4))
# Dekorativní kosmetika – rtěnka, kulatý pudr se zrcátkem, štětec
I['Dekorativní kosmetika'] = (
    P('M31 52h12v26a2 2 0 0 1-2 2h-8a2 2 0 0 1-2-2z', O) + P('M32 45h10v7H32z', O) + P('M33.6 45V34.4L40.4 30v15', O) +
    P('M31 58h12', D) +
    C(63, 66, 13, O) + C(63, 66, 9.4, D) + P('M57.6 62.4c1.6-2 3.8-3 6.4-3', D) +
    G('rotate(38 66 34)', P('M64.6 40h2.8v18h-2.8z', O) + P('M64 34.6h4v5.4h-4z', O) + P('M66 22.4C69.4 25.4 70 31 68 34.6H64C62 31 62.6 25.4 66 22.4z', O)) +
    spark(26, 32, 2.2) + spark(80, 46, 1.5))
# Péče o ústa a zuby – zub, lístky máty
I['Péče o ústa a zuby'] = (
    P('M39 27C32.4 27 29.6 33 30.6 39.6C31.6 46.2 35 50.4 36.2 58.6C37.4 66.8 39 74.6 42.6 74.6C46.2 74.6 46.4 65 50 60.6C53.6 65 53.8 74.6 57.4 74.6C61 74.6 62.6 66.8 63.8 58.6C65 50.4 68.4 46.2 69.4 39.6C70.4 33 67.6 27 61 27C56.4 27 54.4 30.2 50 30.2C45.6 30.2 43.6 27 39 27Z', O) +
    P('M36.4 35.4c.6-2.6 2.4-4 4.6-4.2', D) + leaf(66, 74, -60, 10, 4) + leaf(68, 76, -5, 9, 3.6) +
    spark(74, 26, 2.6) + spark(80, 38, 1.4) + spark(26, 58, 1.4))
# Sprchové gely a pěny – sprchová hlavice, proudy vody, kapky
I['Sprchové gely a pěny'] = (
    P('M26 22H38C43 22 46 25 46 31', M) + P('M24.6 19.6v5', M) +
    P('M33 41Q46 26 59 41Z', O) + P('M42 36.6h8', D) +
    ''.join(C(round(36.5 + i * 3.8, 1), 43.4, .55, F) for i in range(6)) +
    ''.join(P(f'M{36.5 + i * 3.8:.1f} 47L{33 + i * 5:.1f} {62 + (i % 2) * 6}', D + ' stroke-dasharray="2.4 2.2"') for i in range(6)) +
    drop(36, 70, .9) + drop(50, 74, .7) + drop(60, 69, .8) +
    P('M26 82C36 78 48 78 58 81C64 82.6 70 82.4 76 80', D) + spark(70, 26, 2.4) + spark(78, 38, 1.3))
# Tekutá mýdla – baňatý dávkovač s pumpičkou, kapka mýdla, levandule
I['Tekutá mýdla'] = (
    P('M42 48C32 52 30 60 30 66C30 76 38 82 47 82H53C62 82 70 76 70 66C70 60 68 52 58 48Z', O) +
    P('M45 41h10v7H45z', O) + P('M43.4 36.6h13.2v4.4H43.4z', O) + P('M48.6 36.6v-5h2.8v5', M) +
    P('M44 30.4h12v1.4H44z', O) + P('M56 31h9.4v4.6', M) +
    drop(65.4, 39, .75) + P('M34 64c5-2.4 9-2.4 13 0s8 2.4 13 0 6-2.2 6-2.2', D) +
    P('M76 80C77 70 77.4 62 76.6 54', D) +
    ''.join(E(x, y, 1.2, 2, D, a) for x, y, a in [(76.6, 55, 0), (75, 58, -25), (78.2, 59.4, 25), (74.8, 62.6, -25), (78.2, 64, 25)]) +
    spark(28, 34, 2.4) + spark(72, 28, 1.6))
# Speciální péče – kelímek krému s víčkem, list aloe
def aloe_leaf(x, y, ang, l, w):
    # souměrný dužnatý list: široká báze, špička; drobné zoubky po okraji
    teeth = ''.join(C(round(l * t, 2), round(-w * (1 - t) * 1.0 - .5, 2), .3, F) for t in (.35, .6))
    return G(f'translate({x} {y}) rotate({ang})', P(f'M0 {-w}C{l*.4} {-w} {l*.75} {-w*.45} {l} 0C{l*.75} {w*.45} {l*.4} {w} 0 {w}Z', O) + P(f'M1.4 0H{l*.8}', D) + teeth)
def chamomile(cx, cy, r):
    return ''.join(G(f'rotate({k*30} {cx} {cy})', E(cx, round(cy - r * .62, 2), r * .2, r * .42, O)) for k in range(12)) + C(cx, cy, r * .3, O) + C(cx, cy, r * .3 * .45, F)
I['Speciální péče'] = (
    P('M30 82C30 70 31 60 34 50', D) + P('M33 82C34 74 36 68 40 62', D) + leaf(31.2, 70, -150, 8, 2.8) + leaf(35.4, 72, -40, 8, 2.8) +
    chamomile(34, 44, 10) + chamomile(42, 58, 7.4) +
    P('M48 58h30v14a6 6 0 0 1-6 6H54a6 6 0 0 1-6-6z', O) + P('M46 51.4a2 2 0 0 1 2-2h30a2 2 0 0 1 2 2V58H46z', O) +
    P('M52 64h22 M56 69h14', D) + spark(63, 66.6, 1.3) + spark(70, 30, 2.6) + spark(78, 42, 1.4))
# Pro muže – štětka na holení a klasický holicí strojek
I['Pro muže'] = (
    P('M38 81h14l-1.8-14H39.8z', O) + P('M38.6 62.6h12.8V67H38.6z', O) +
    P('M40 62.6C34.6 52 36.6 36 45 33C53.4 36 55.4 52 50 62.6Z', O) + P('M41 58C39.6 50 41 42 45 37.6 M49 58C50.4 50 49 42 45 37.6 M45 60V39', D) +
    G('rotate(24 68 56)', P('M66.6 44h2.8v34h-2.8z', O) + P('M59 38.6h18v5.4H59z', O) + P('M60.6 36.4h14.8', D) + P('M67 50h2 M67 54h2 M67 58h2 M67 62h2', D) + C(68, 80, 1.6, O)) +
    spark(28, 30, 2.4) + spark(78, 26, 1.6))
# Opalování – slunce s paprsky, lahvička s krémem, vlny
I['Opalování'] = (
    C(64, 34, 8, O) + ''.join(P(f'M{64 + 11 * math.cos(a):.2f} {34 + 11 * math.sin(a):.2f}L{64 + (16 if i % 2 == 0 else 14) * math.cos(a):.2f} {34 + (16 if i % 2 == 0 else 14) * math.sin(a):.2f}', D) for i, a in enumerate([k * math.pi / 6 for k in range(12)])) +
    P('M30 50h16l2 6v20a4 4 0 0 1-4 4H32a4 4 0 0 1-4-4V56z', O) + P('M32 43.6h12V50H32z', O) + P('M33.6 43.6v-4h8.8v4', M) +
    P('M31 62h14 M33 67h10', D) + spark(38, 72.6, 1.2) +
    P('M54 70c3-2.4 6-2.4 9 0s6 2.4 9 0 6-2.4 6-2.4 M56 77c3-2.4 6-2.4 9 0s6 2.4 9 0', D) + spark(80, 56, 1.5))
# CBD – list konopí, lahvička s kapátkem
def hemp(cx, cy):
    s = ''
    for ang, l in [(-90, 30), (-62, 25), (-118, 25), (-34, 18), (-146, 18), (-10, 11), (-170, 11)]:
        w = l * .17
        s += G(f'translate({cx} {cy}) rotate({ang})', P(f'M0 0Q{l*.45} {-w} {l} 0Q{l*.45} {w} 0 0Z', O) + P(f'M1.4 0H{l*.85}', D) +
               ''.join(P(f'M{l*t:.1f} {-w*.55:.2f}l1.4 -.8', D) for t in (.35, .55, .75)))
    return s + P(f'M{cx} {cy}C{cx-1} {cy+6} {cx-2} {cy+10} {cx-3} {cy+16}', M)
I['CBD'] = (hemp(40, 62) +
    P('M64 50v5a10 10 0 1 0 8 0v-5z', O) + P('M62.6 45.4h10.8V50H62.6z', O) + P('M64.4 45.4v-6a3.6 3.6 0 0 1 7.2 0v6', O) +
    drop(68, 60, .8) + spark(76, 30, 2.2) + spark(80, 42, 1.3))

# ---------- DOPLŇKY STRAVY ----------
# Imunitní systém – třapatka (echinacea), tobolka
def echinacea(cx, cy):
    s = ''
    for k in range(9):
        a = -10 + k * 22.5  # okvětní lístky visí dolů a do stran
        s += G(f'translate({cx} {cy}) rotate({a})', P('M3 0C8 1.6 14 3.6 17.4 7.4C14 8.2 8.6 6 3 2.6Z', O))
    s += P(f'M{cx-7} {cy+1}C{cx-7} {cy-9} {cx+7} {cy-9} {cx+7} {cy+1}Z', O)
    s += ''.join(C(round(cx + dx, 1), round(cy + dy, 1), .55, F) for dx, dy in [(-4, -1), (-1.4, -3.6), (1.6, -3.6), (4, -1), (0, -1), (-2.6, -6), (2.6, -6)])
    return s
I['Imunitní systém'] = (
    P('M44 84C44 74 45 62 46 46', M) + leaf(44.6, 70, -150, 12, 4) + leaf(45.4, 62, -30, 11, 3.6) + echinacea(46, 42) +
    G('rotate(-35 70 66)', P('M64 62h6v8h-6a4 4 0 0 1 0-8z', O) + P('M70 62h6a4 4 0 0 1 0 8h-6z', O) + P('M66 64.4h2', D)) +
    spark(72, 28, 2.4) + spark(26, 34, 1.6) + spark(78, 40, 1.2))
# Koření – hmoždíř s paličkou, badyán, kuličky pepře
def star_anise(cx, cy, r):
    s = ''
    for k in range(8):
        s += G(f'rotate({k*45} {cx} {cy})', P(f'M{cx} {cy}C{cx-2.4} {cy-r*.4} {cx-1.8} {cy-r*.9} {cx} {cy-r}C{cx+1.8} {cy-r*.9} {cx+2.4} {cy-r*.4} {cx} {cy}Z', O) + C(cx, round(cy - r * .62, 2), .5, F))
    return s + C(cx, cy, 1.3, O)
I['Koření'] = (
    G('rotate(28 60 48)', P('M57.6 22h4.8v34h-4.8z', O) + P('M57.6 22a2.4 2.4 0 0 1 4.8 0', O)) +
    P('M28 56H72C72 70 63 78 50 78C37 78 28 70 28 56Z', O) + P('M26.4 52.6h47.2V56H26.4z', O) + P('M42 78l-1.4 4h18.8L58 78', O) +
    P('M33 62c4 9 30 9 34 0', D, ) + star_anise(30, 34, 9) + C(46, 38, 1.6, O) + C(50.4, 34, 1.4, O) + C(44, 30, 1.2, O) +
    spark(78, 30, 2.2))
# Aloe Vera gel – rostlina aloe, sklenice s nápojem
I['Aloe Vera gel'] = (
    aloe_leaf(38, 76, -90, 40, 5) + aloe_leaf(35, 77, -116, 30, 4.6) + aloe_leaf(41, 77, -64, 30, 4.6) + aloe_leaf(33, 78, -142, 18, 3.8) + aloe_leaf(43, 78, -38, 18, 3.8) +
    P('M28 79.6Q38 76.6 48 79.6', D) +
    P('M58 46h18l-2.4 32a2 2 0 0 1-2 1.8h-9.2a2 2 0 0 1-2-1.8z', O) + P('M59 56h16', D) + P('M59.6 62c3 1.4 5.6 1.4 7.6 0s4.6-1.4 7.4 0', D) +
    drop(67, 64.6, .7) + spark(74, 30, 2.4) + spark(80, 40, 1.3))
# Vitamíny a minerály – plátek citrusu, tobolka, tablety
def citrus(cx, cy, r):
    s = C(cx, cy, r, O) + C(cx, cy, r - 2, D)
    for k in range(8):
        a = math.radians(k * 45 + 22.5)
        s += P(f'M{cx} {cy}L{cx + (r-2.6)*math.cos(a):.2f} {cy + (r-2.6)*math.sin(a):.2f}', D)
    return s + C(cx, cy, 1, F)
I['Vitamíny a minerály'] = (
    citrus(36, 38, 13) +
    G('rotate(-40 60 58)', P('M48 52h12v12H48a6 6 0 0 1 0-12z', O) + P('M60 52h12a6 6 0 0 1 0 12H60z', O) + P('M50 55.6a3 3 0 0 0-1.6 2.6', D)) +
    C(36, 70, 6.4, O) + P('M31.4 70h9.2', D) + E(52, 78, 6.4, 3.6, O) + P('M47.6 77h8.8', D) +
    spark(72, 30, 2.6) + spark(80, 42, 1.4))
# Oleje – láhev se zátkou, olivová větvička
I['Oleje'] = (
    P('M43.6 44C39.4 48 38.6 52 38.6 56V78a3 3 0 0 0 3 3h14.8a3 3 0 0 0 3-3V56c0-4-.8-8-5-12V36H43.6Z', O) +
    P('M42.6 31.6c0-2 1.4-3.6 3.6-3.6h5.6c2.2 0 3.6 1.6 3.6 3.6V36H42.6z', O) +
    P('M39.4 60c3-1.6 6-1.6 9.6 0s6.6 1.6 9.6 0', D) + P('M42 64v12', D, ) +
    P('M58 44C66 40 72 34 76 24', D) +
    slender(61, 42.4, -70, 9, 2.2) + slender(64, 40.6, 10, 9, 2.2) + slender(68, 36.8, -80, 8, 2) + slender(71, 33.4, 0, 8, 2) +
    E(66.6, 46.6, 2.2, 3, O, -20) + E(73.4, 39, 2, 2.8, O, -20) + spark(28, 30, 2.4) + spark(26, 44, 1.2))
# Sypané čaje – šálek s podšálkem, pára, čajové lístky
I['Sypané čaje'] = (
    P('M30 50H64C64 64 58 72 47 72C36 72 30 64 30 50Z', O) + P('M64 54c6 0 8 3.4 6.6 7-1.2 3-4.4 4.4-8.6 4', M) +
    P('M22 74.6C30 80 64 80 72 74.6', M) + P('M30 76.6C38 79.4 56 79.4 64 76.6', D) +
    P('M38 44c-3-3.4 3-6.4 0-10 M47 44c-3-3.4 3-6.4 0-10 M56 44c-3-3.4 3-6.4 0-10', D) +
    P('M33 56c4 6 24 6 28 0', D, ) + slender(70, 40, -30, 11, 3) + slender(72, 44, 20, 10, 2.8) +
    spark(26, 32, 2.2) + spark(76, 28, 1.6))
# Káva – French press, kávová zrna
I['Káva'] = (
    P('M40 38h22v38a3 3 0 0 1-3 3H43a3 3 0 0 1-3-3z', O) + P('M38.6 33.4h24.8V38H38.6z', O) + P('M50 33.4V22', M) + C(50, 20.4, 1.8, O) +
    P('M62 44h4a4 4 0 0 1 4 4v18a4 4 0 0 1-4 4h-4', M) + P('M41 50h20', D) + P('M41.4 54c4 1.6 8 1.6 10 0s6-1.6 9.4 0', D) +
    P('M44 41v34', D, ) + bean(28, 66, -25, 1) + bean(25, 54, 20, .8) + bean(30, 76, 70, .75) +
    spark(74, 28, 2.4) + spark(78, 80, 1.3))
# Swissycandy – zabalený bonbon, protěž, bylinky
def edelweiss(cx, cy, r):
    s = ''
    for k in range(8):
        rr = r if k % 2 == 0 else r * .78
        s += G(f'rotate({k*45} {cx} {cy})', P(f'M{cx} {cy}C{cx-2.4} {cy-rr*.45} {cx-1.4} {cy-rr*.9} {cx} {cy-rr}C{cx+1.4} {cy-rr*.9} {cx+2.4} {cy-rr*.45} {cx} {cy}Z', O))
    return s + ''.join(C(round(cx + dx, 1), round(cy + dy, 1), 1.1, O) for dx, dy in [(0, 0), (-2, -1.6), (2, -1.6), (-2, 1.6), (2, 1.6)])
I['Swissycandy'] = (
    P('M20 54L34 34L41 43L50 28L62 46L68 40L80 54', D) + P('M30.6 38.6L34 34L37.4 38.4L35.6 37.4L34 39.2L32.4 37.4Z M45.6 34.6L50 28L54.6 34.8L52.4 33.6L50 35.8L47.8 33.6Z', F) +
    G('rotate(-24 50 64)', E(50, 64, 11.6, 8, O) + P('M38.6 64L28.6 57.4V70.6Z', O) + P('M61.4 64L71.4 57.4V70.6Z', O) +
      P('M31.6 60v8 M34.6 61.4v5.2 M68.4 60v8 M65.4 61.4v5.2', D) + P('M43 61c3-2 11-2 14 0 M44 67c3 1.6 9 1.6 12 0', D)) +
    leaf(72, 74, -30, 9, 3.2) + leaf(71, 76, 40, 8, 3) + spark(76, 28, 2.2) + spark(26, 70, 1.4))

# ---------- DOMÁCNOST ----------
# Mytí nádobí – talíř, sklenka na víno, třpytky
I['Mytí nádobí'] = (
    C(40, 58, 19, O) + C(40, 58, 13, D) + P('M30.6 50c2.4-4 6-6.4 10.4-7', D) +
    P('M58 28h22C80 42 76 50 69 50C62 50 58 42 58 28Z', O) + P('M69 50v22', M) + P('M61 74.6C63 72.4 75 72.4 77 74.6Z', O) +
    P('M60.6 36c2 2 14.8 2 16.8 0', D) + spark(32, 28, 2.6) + spark(52, 34, 1.4) + spark(80, 60, 1.8))
# Kuchyně – hrnec s pokličkou a párou
I['Kuchyně'] = (
    P('M30 52H70V72a6 6 0 0 1-6 6H36a6 6 0 0 1-6-6z', O) + P('M30 56h-5a2 2 0 0 1 0-4h5 M70 56h5a2 2 0 0 0 0-4h-5', M) +
    P('M27 52Q50 38 73 52Z', O) + P('M46 44.6v-3.4a4 4 0 0 1 8 0v3.4', O) + P('M33 62h34', D) +
    P('M40 34c-3-3.4 3-6.4 0-10 M50 32c-3-3.4 3-6.4 0-10 M60 34c-3-3.4 3-6.4 0-10', D) + spark(24, 30, 2.2) + spark(78, 28, 1.6))
# Koupelny – vana na nožkách s baterií
I['Koupelny'] = (
    P('M22 52H78V56C78 67 70 72 60 72H40C30 72 22 67 22 56Z', O) + P('M20.6 49.4h58.8V52H20.6z', O) +
    P('M32 71.4c-.4 3-1.6 5.4-3.6 7 M68 71.4c.4 3 1.6 5.4 3.6 7', M) + P('M27 78.6h3 M70 78.6h3', M) +
    P('M30 49.4V34a5 5 0 0 1 10 0v2', M) + P('M37.6 36h4.8', M) + drop(40, 39.4, .55) + P('M28 58c8 6 36 6 44 0', D) +
    spark(62, 30, 2.6) + spark(72, 40, 1.4) + spark(52, 40, 1.1))
# Okna a zrcadla – zrcadlo s obloukem, odlesky
I['Okna a zrcadla'] = (
    P('M34 80V40a16 16 0 0 1 32 0v40Z', O) + P('M38 76V40.6a12 12 0 0 1 24 0V76Z', D) +
    P('M44 52l10-10 M44 60l14-14 M46 66l12-12', D) + P('M30 80h40', M) +
    spark(74, 30, 2.6) + spark(78, 44, 1.4) + spark(26, 40, 1.8))
# WC, toalety, odpady – záchod z boku
I['WC, toalety, odpady'] = (
    P('M30 26h16a2 2 0 0 1 2 2v22H28V28a2 2 0 0 1 2-2z', O) + P('M33.4 31h9.2', D) + 
    P('M26 50H74C74 60 66 66 58 68L60 80H40L42 68C34 66 26 60 26 54Z', O) + P('M26 54.4h48', D) +
    P('M38 22.6h6v3.4h-6z', O) + drop(64, 30, .9) + spark(74, 38, 2.2) + spark(58, 24, 1.3))
# Podlahy – mop, podlaha s odleskem
I['Podlahy'] = (
    P('M36 18L55.6 62', M) + P('M38.4 16.4L35.4 18', M) +
    P('M44 61h24a2 2 0 0 1 2 2v3H42v-3a2 2 0 0 1 2-2z', O) + ''.join(P(f'M{43.6 + i * 3:.1f} 66v6', D) for i in range(9)) +
    P('M22 78H78', M) + P('M30 82h10 M48 82h22', D) + spark(72, 32, 2.6) + spark(78, 46, 1.4) + spark(28, 48, 1.6))
# Univerzální čisticí prostředky – rozprašovač
I['Univerzální čisticí prostředky'] = (
    P('M44 46h16l4 9v23a3 3 0 0 1-3 3H43a3 3 0 0 1-3-3V55z', O) + P('M46 40h12v6H46z', O) +
    P('M42 28h20l2 8a2 2 0 0 1-2 2.4H46l-4-3.4H34V30a2 2 0 0 1 2-2z', O) + P('M56 38.4c-1 4-1 6.4 1.4 9', M) +
    ''.join(C(round(30 - 3 * k * math.cos(math.radians(a)), 1), round(31.6 - 3 * k * math.sin(math.radians(a)), 1), .55, F) for k in (1, 2, 3) for a in (-25, 0, 25)) +
    P('M44 60h16v12H44z', D) + leaf(52, 69.6, -70, 7, 2.6, False) + spark(74, 34, 2.4) + spark(78, 60, 1.4))
# Speciální čisticí prostředky – kartáč na drhnutí, třpytky
I['Speciální čisticí prostředky'] = (
    P('M30 50h36a8 8 0 0 1 0 16H30a6 6 0 0 1 0-12', O) + P('M27.6 50.6C26 53 26 60 30 66', O) +
    C(60, 58, 2.6, D) + ''.join(P(f'M{31 + i * 4:.0f} 66v7', D) for i in range(10)) + P('M26 76h48', D, ) +
    spark(36, 32, 2.8) + spark(50, 28, 1.6) + spark(64, 36, 2.2) + spark(76, 28, 1.3))
# Koberce a vysavače – koberec s ornamentem a třásněmi
I['Koberce a vysavače'] = (
    P('M30 40h40v40H30z', O) + P('M34 44h32v32H34z', D) + P('M50 48l10 12-10 12-10-12z', D) + P('M50 54l5 6-5 6-5-6z', D) +
    ''.join(P(f'M{32 + i * 4:.0f} 40v-5 M{32 + i * 4:.0f} 80v5', D) for i in range(10)) +
    spark(76, 30, 2.4) + spark(24, 52, 1.4))
# Osvěžovače vzduchu a textilií – aroma difuzér s tyčinkami
I['Osvěžovače vzduchu a textilií'] = (
    P('M42 58C33 62 32 70 34 75C36 80 42 82 50 82C58 82 64 80 66 75C68 70 67 62 58 58V52H42Z', O) + P('M41 49.4h18V52H41z', O) +
    P('M47 50L36 20 M49 50L44 17 M51 50L56 17 M53 50L64 20 M50 50L50 16', D) +
    P('M36 66c5 3 23 3 28 0', D) + P('M30 28c-3-3 1-6-2-9 M70 26c3-3-1-6 2-9 M62 12c2-1.6 4-1.6 6 0', D) +
    spark(24, 40, 1.6) + spark(78, 40, 2.2))
# Odpuzovače hmyzu – náramek s přívěskem lístku, citronová tráva, odlétající komár
I['Odpuzovače hmyzu'] = (
    P('M26 84C26 66 24 52 20 40 M30 84C31 68 32 56 36 46', D) +
    C(48, 62, 15, O) + C(48, 62, 10.6, O) + C(48, 62, 12.8, D + ' stroke-dasharray="1.6 1.8"') +
    P('M48 77v3', M) + G('translate(48 80) rotate(90)', P('M0 0Q4 -3 8 0Q4 3 0 0Z', O) + P('M1 0H6.6', D)) +
    G('translate(72 30) rotate(-20)', E(0, 0, 4, 1.8, O) + C(-5, 0, 1.6, O) + P('M-6.4 .4l-3.4 1.6', D) + P('M-1 -1.6C-3 -6 -.4 -8 1.6 -2 M1 -1.6C2 -6 5.6 -6.4 3 -1.4', D) + P('M-2 1.6l-2 4 M1 1.6l0 4.4 M3 1.4l2 4', D)) +
    P('M64 38c-3 3-6 5-10 6', D + ' stroke-dasharray="1.2 2"') + spark(78, 52, 1.6) + spark(30, 30, 1.4))
# Péče o rostliny – květináč s rostlinou, kapky
I['Péče o rostliny'] = (
    P('M36 60h28l-3.4 20a2 2 0 0 1-2 1.6H41.4a2 2 0 0 1-2-1.6z', O) + P('M34 55.4h32V60H34z', O) +
    P('M50 55.4C50 46 49 38 46 30', M) + leaf(48, 46, -150, 13, 5) + leaf(49.6, 44, -20, 14, 5.2) + leaf(47, 36, -125, 11, 4.2) + leaf(47.6, 33, -55, 10, 3.8) +
    drop(66, 30, .8) + drop(72, 40, .6) + spark(28, 34, 2.4) + spark(74, 62, 1.4))
# Péče o vozidlo – auto z boku, třpytky
I['Péče o vozidlo'] = (
    P('M20 66V60C20 57 22 55.4 25 55L38 53L46 45C49 42 53 41 58 41H64C68 41 71 43 73 46L77 53C80 54 81 56.4 81 59V66H75 M63 66H38 M26 66H20', O) +
    C(32, 66, 5.6, O) + C(32, 66, 2, D) + C(69, 66, 5.6, O) + C(69, 66, 2, D) +
    P('M41.6 53L48 46.6C50 44.6 53 44 56 44V53Z M59 44H63.6C66 44 68 45 69.4 47.4L72.4 53H59Z', D) + P('M24 59.4h4', D) +
    spark(30, 32, 2.6) + spark(78, 32, 1.6) + spark(44, 26, 1.3))
# Dezinfekce – štít s kapkou
I['Dezinfekce'] = (
    P('M50 20L72 28V46C72 62 62 74 50 80C38 74 28 62 28 46V28Z', O) + P('M50 25.4L67.4 31.6V46C67.4 59.4 59.4 69.4 50 74.6C40.6 69.4 32.6 59.4 32.6 46V31.6Z', D) +
    drop(50, 38, 2.2, O) + P('M46.6 55.4c.4 2 1.6 3.4 3.4 3.8', D) + spark(78, 22, 2.2) + spark(22, 30, 1.6))
# Pro zvířata – otisk tlapky, srdíčko
I['Pro zvířata'] = (
    P('M50 52C42 52 34 60 34 68C34 74 38 77 43 76C46 75.4 48 74.4 50 74.4S54 75.4 57 76C62 77 66 74 66 68C66 60 58 52 50 52Z', O) +
    E(34, 46, 4.4, 6, O, -20) + E(44, 37, 4.6, 6.4, O, -6) + E(56, 37, 4.6, 6.4, O, 6) + E(66, 46, 4.4, 6, O, 20) +
    P('M70 26c-1.6-3-6-2.4-6 1 0 2.6 3 4.4 6 6.6 3-2.2 6-4 6-6.6 0-3.4-4.4-4-6-1z', O) + spark(26, 30, 2.2) + spark(30, 80, 1.3))
# Dárkové poukazy – poukaz s mašlí
I['Dárkové poukazy'] = (
    G('rotate(-8 50 58)', P('M26 44h48a2 2 0 0 1 2 2v26a2 2 0 0 1-2 2H26a2 2 0 0 1-2-2V46a2 2 0 0 1 2-2z', O) + P('M28.4 48h43.2v22H28.4z', D) +
      P('M40 44v30', M) + P('M24 56h52', M) + P('M48 62h20 M48 66h14', D) +
      P('M40 44C34 38 28 38 30 42S36 46 40 44C44 38 52 38 50 42S44 46 40 44Z', O) + P('M40 44l-4 6 M40 44l4 6', D)) +
    spark(72, 28, 2.6) + spark(78, 40, 1.4) + spark(28, 28, 1.4))
