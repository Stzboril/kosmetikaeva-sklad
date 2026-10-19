# Kresby 20 hlubších podkategorií (Parfémy, Dekorativní kosmetika, Praní prádla, Mytí nádobí) – stejný styl jako cat2.py
import math
from lux2 import M, D, O, BGF, spark, leaf, roundleaf
from cat2 import F, P, C, E, G, drop, slender, flower5
from taper import brush

def tshirt(cx, cy, s=1, a=O):  # tričko (střed hrudi cx, cy)
    k = lambda v: f'{v * s:.2f}'
    d = (f'M{cx - 7*s:.2f} {cy - 15*s:.2f}C{cx - 4*s:.2f} {cy - 11*s:.2f} {cx + 4*s:.2f} {cy - 11*s:.2f} {cx + 7*s:.2f} {cy - 15*s:.2f}'
         f'L{cx + 17*s:.2f} {cy - 10*s:.2f}L{cx + 21*s:.2f} {cy - 1*s:.2f}L{cx + 13*s:.2f} {cy + 2*s:.2f}V{cx * 0 + cy + 19*s:.2f}'
         f'H{cx - 13*s:.2f}V{cy + 2*s:.2f}L{cx - 21*s:.2f} {cy - 1*s:.2f}L{cx - 17*s:.2f} {cy - 10*s:.2f}Z')
    return P(d, a) + P(f'M{cx - 7*s:.2f} {cy - 15*s:.2f}C{cx - 4*s:.2f} {cy - 8*s:.2f} {cx + 4*s:.2f} {cy - 8*s:.2f} {cx + 7*s:.2f} {cy - 15*s:.2f}', D)
def rose(cx, cy, r):  # stylizovaná růže (spirála okvětí)
    return (C(cx, cy, r, O) + P(f'M{cx} {cy - r*.15}c{r*.35:.2f} 0 {r*.45:.2f} {r*.45:.2f} {r*.1:.2f} {r*.6:.2f}s{-r*.7:.2f} {-r*.1:.2f} {-r*.6:.2f} {-r*.6:.2f}{r*.5:.2f} {-r*.55:.2f} {r*.95:.2f} {-r*.3:.2f}', D) +
            P(f'M{cx - r*.9:.2f} {cy + r*.1:.2f}C{cx - r*.6:.2f} {cy + r*.8:.2f} {cx + r*.6:.2f} {cy + r*.8:.2f} {cx + r*.9:.2f} {cy + r*.1:.2f}', D))
def bottle_round(cx, top, w=20, h=24):  # kulatý flakon
    r = w / 2
    return (P(f'M{cx - 3} {top + 7}C{cx - r - 2} {top + 9} {cx - r} {top + h} {cx} {top + h + 2}C{cx + r} {top + h} {cx + r + 2} {top + 9} {cx + 3} {top + 7}Z', O) +
            P(f'M{cx - 3.4} {top + 3}h6.8v4.4h-6.8z', O) + P(f'M{cx - 4.6} {top - 4}h9.2v7h-9.2z', O) + P(f'M{cx - r + 3} {top + 16}c{r*.6:.1f} 2 {r*1.4:.1f} 2 {2*r - 6:.1f} 0', D))
def bottle_square(cx, top, w=20, h=22):  # hranatý flakon
    return (P(f'M{cx - w/2} {top + 8}h{w}v{h}h{-w}z', O) + P(f'M{cx - w/2 + 3} {top + 11}h{w - 6}v{h - 6}h{-(w - 6)}z', D) +
            P(f'M{cx - 3} {top + 3}h6v5h-6z', O) + P(f'M{cx - 6} {top - 4}h12v7h-12z', O))

I = {}
# ---------- PARFÉMY ----------
I['Parfémy dámské'] = (bottle_round(44, 34, 24, 30) + P('M70 84C70 76 69 70 68 64', D) + flower5(68, 60, 5.4) + flower5(76, 72, 3.4) + leaf(66, 76, 150, 8, 3) + leaf(70, 74, 30, 7, 2.6) + spark(70, 30, 2.6) + spark(30, 40, 1.6) + spark(78, 44, 1.2))
I['Parfémy pánské'] = (bottle_square(44, 32, 24, 32) +
    P('M64 82C66 70 68 58 72 46', D) + ''.join(slender(x, y, a, 9, 1.6) for x, y, a in [(65, 72, -150), (66, 70, -40), (67.4, 62, -155), (68.4, 60, -35), (69.8, 53, -160), (70.6, 51, -30)]) +
    spark(70, 30, 2.6) + spark(28, 44, 1.6) + spark(78, 38, 1.2))
I['Parfémy unisex'] = (bottle_round(36, 38, 18, 24) + bottle_square(62, 34, 18, 28) +
    spark(50, 22, 2.4) + spark(26, 30, 1.4) + spark(78, 28, 1.4))
# ---------- DEKORATIVNÍ KOSMETIKA ----------
I['Make-up obličej'] = (  # make-up v lahvičce s pumpičkou, houbička, štětec na pudr
    P('M30 46h16v32a3 3 0 0 1-3 3H33a3 3 0 0 1-3-3z', O) + P('M33 40h10v6H33z', O) + P('M35.6 34h4.8v6h-4.8z', O) + P('M40.4 36h6', M) +
    P('M31 58h14', D) + drop(38, 62, .8) +
    P('M58 82C51 82 49 76 51 70C53 63 57 58 60 54C63 58 67 63 69 70C71 76 69 82 62 82Z', O) + P('M54 74c1.4 3 4 4.4 7 4', D) +
    G('rotate(35 66 36)', P('M64.8 40h2.4v18h-2.4z', O) + P('M64.4 35h3.2v5h-3.2z', O) + P('M66 22C70 25 71 31 68 35H64C61 31 62 25 66 22Z', O)) +
    spark(26, 30, 2.2) + spark(78, 50, 1.4))
I['Make-up oči'] = (  # oko s řasami, řasenka
    brush('M24 46C32 36 48 34 60 42', 1.6, start=.1, end=.2) + brush('M24 46C32 54 48 56 60 48', 1.1, start=.1, end=.2) +
    C(42, 45.4, 6.6, O) + C(42, 45.4, 2.8, F) + C(43.6, 43.8, .9, f'fill="{BGF}"') +
    ''.join(brush(f'M{x0} {y0}C{x0 + dx*.4:.1f} {y0 - 3} {x0 + dx*.8:.1f} {y0 - 5} {x0 + dx} {y0 - 7}', .7, start=0, end=.6) for x0, y0, dx in [(28, 41.4, -2), (33, 38.4, -1), (38.6, 36.8, 0), (44.6, 36.6, 1), (50.4, 37.8, 2), (55.4, 40, 3)]) +
    G('rotate(-35 66 66)', P('M64.6 44h2.8v14h-2.8z', D) + ''.join(P(f'M{63.2} {44 + i * 1.6:.1f}h5.6', D) for i in range(9)) + P('M63.8 58h4.4v6h-4.4z', O) + P('M63.6 64h4.8v18h-4.8z', O)) +
    spark(72, 28, 2.4) + spark(30, 70, 1.4))
I['Make-up rty'] = (  # rty a rtěnka
    brush('M24 50C28 47 32 43 36 43C39 43 41 45 43 45C45 45 47 43 50 43C54 43 58 47 62 50', 1.8, start=.05, end=.05) +
    brush('M24 50C30 58 36 61 43 61C50 61 56 58 62 50', 1.8, start=.05, end=.05) + brush('M27 50.4C35 52.6 51 52.6 59 50.4', .8, start=.1, end=.1) +
    P('M64 62h10v20h-10z', O) + P('M65 56h8v6h-8z', O) + P('M66.2 56V46l5.6-3.6V56', O) +
    spark(36, 30, 2.4) + spark(76, 34, 1.6) + spark(26, 70, 1.3))
I['Make-up nehty'] = (  # otevřený lak se štětečkem, nehty
    P('M30 56h16a3 3 0 0 1 3 3v17a4 4 0 0 1-4 4H31a4 4 0 0 1-4-4V59a3 3 0 0 1 3-3z', O) + P('M33.6 51h8.8v5h-8.8z', O) + P('M31 72h14', D) +
    G('rotate(25 56 40)', P('M53 18a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v14h-8z', O) + P('M56 32h2v10h-2z', O) + P('M55.2 42h3.6l-.6 4.6h-2.4z', F)) +
    G('rotate(-40 68 66)', P('M65.6 48h4.8a2.4 2.4 0 0 1 2.4 2.4V80a3.2 3.2 0 0 1-3.2 3.2h-3.2A3.2 3.2 0 0 1 63.2 80V50.4A2.4 2.4 0 0 1 65.6 48z', O) +
      ''.join(P(f'M64.4 {52 + i * 2.6:.1f}l6.8 2.4', D) for i in range(8))) +
    drop(60, 50, .7) + spark(26, 34, 2.2) + spark(78, 40, 1.4))
# ---------- PRANÍ PRÁDLA ----------
I['Bílé prádlo'] = (tshirt(48, 54) + spark(48, 56, 5) + spark(70, 30, 2.6) + spark(28, 30, 1.6) + spark(78, 44, 1.3))
def crescent2(cx, cy, R, dx, r):
    from lux2 import math as _m
    d = dx; a = (R*R - r*r + d*d) / (2*d); h = math.sqrt(R*R - a*a)
    px, py = cx + a, cy
    return f'M{px:.2f} {py - h:.2f}A{R} {R} 0 1 0 {px:.2f} {py + h:.2f}A{r} {r} 0 1 1 {px:.2f} {py - h:.2f}Z'
I['Černé prádlo'] = (tshirt(48, 54) + P(crescent2(48, 56, 6, 3.4, 5), F) + spark(70, 28, 2.4) + spark(76, 40, 1.4) + spark(28, 32, 1.4))
I['Barevné prádlo'] = (tshirt(48, 54) + C(43, 52, 2.2, F) + C(52, 51, 1.8, O) + C(48, 59, 2, O) + C(54, 60, 1.4, F) + C(41, 61, 1.3, O) +
    E(74, 70, 7, 5.4, O) + C(71, 68.6, 1.2, F) + C(75, 67.6, 1.1, O) + C(77.4, 71, 1.2, F) + C(73, 72.6, 1.6, f'fill="{BGF}" stroke="url(#gold)" stroke-width=".8"') +
    spark(70, 28, 2.4) + spark(28, 32, 1.4))
I['Univerzální prací prostředky'] = (  # lahev pracího gelu s uchem a odměrkou
    P('M34 40h20l6 8v30a3 3 0 0 1-3 3H33a3 3 0 0 1-3-3V48z', O) + P('M54 46h3a5 5 0 0 1 5 5v10a5 5 0 0 1-5 5h-1', M) +
    P('M38 33.6h10V40H38z', O) + P('M34 56h20v14H34z', D) + P('M40 63c2-3 6-3 8 0', D) + spark(44, 60, 1.2) +
    P('M64 68h14l-2 13a1.6 1.6 0 0 1-1.6 1.4h-6.8a1.6 1.6 0 0 1-1.6-1.4z', O) + P('M65 73h12', D) +
    spark(70, 30, 2.6) + spark(26, 30, 1.4) + spark(76, 44, 1.2))
I['Aviváže s kondicionérem'] = (  # složený ručník a pírko
    P('M28 58h40a6 6 0 0 1 0 12H28z', O) + P('M28 70h40a6 6 0 0 1 0 12H28z', O) + P('M30 64h34 M30 76h34', D + ' stroke-dasharray="1.2 1.6"') +
    G('rotate(-35 54 36)', P('M54 16C61 22 62 38 54 54C46 38 47 22 54 16Z', O) + P('M54 22V60', D) +
      ''.join(P(f'M54 {y}l{s * 5} -4', D) for y in (30, 36, 42) for s in (-1, 1))) +
    spark(28, 34, 2.4) + spark(76, 46, 1.4))
I['Parfémy na praní'] = (  # lahvička s víčkem, kvítky, vůně
    P('M36 46h20l3 6v25a3 3 0 0 1-3 3H36a3 3 0 0 1-3-3V52z', O) + P('M39 38h14v8H39z', O) + P('M37 58h18v12H37z', D) + flower5(46, 64, 2.6) +
    flower5(70, 62, 4) + flower5(66, 74, 3) + P('M70 66.4C70 72 69 78 68 82', D) +
    P('M58 34c3-3-1-6 2-9 M64 38c3-3-1-6 2-9', D) + spark(28, 32, 2.2) + spark(76, 40, 1.4))
I['Na skvrny'] = (tshirt(46, 54) + P('M41 55c-2-2 0-5 3-4 2-3 6-2 6 1 3 0 4 4 1 5-1 3-5 3-6 1-3 1-5-1-4-3z', D + ' stroke-dasharray="1.4 1.4"') +
    G('rotate(-30 70 34)', P('M66 30h8l2 4v10a2 2 0 0 1-2 2h-8a2 2 0 0 1-2-2V34z', O) + P('M67.4 25h5.2v5h-5.2z', O)) +
    spark(76, 56, 2.2) + spark(68, 64, 1.3) + spark(26, 30, 1.4))
I['Jemné prádlo'] = (  # hedvábný šátek ve vlnách a pírko
    P('M22 52C30 44 38 44 46 50S62 58 70 50C74 46 77 45 80 46L78 60C74 59 72 60 68 64C60 72 52 68 44 62S30 56 24 64Z', O) +
    P('M26 56C33 50 40 50 47 55S62 63 70 56 M28 60C34 56 41 56 47 60', D) +
    G('rotate(30 56 30)', P('M56 14C61 19 62 30 56 42C50 30 51 19 56 14Z', O) + P('M56 19V46', D)) +
    spark(30, 32, 2.4) + spark(74, 72, 1.4))
I['Speciální prací prostředky'] = (  # klubko vlny s jehlicemi a lahvička
    C(40, 60, 14, O) + P('M28 54C34 50 44 50 52 56 M27 61C34 57 46 57 53 63 M30 68C36 65 46 65 51 70 M36 47C42 51 46 60 46 73', D) +
    P('M30 34L58 74 M34 30L60 70', M) + C(29, 33, 1.6, O) + C(33, 29, 1.6, O) +
    P('M62 46h12l2 5v24a2 2 0 0 1-2 2H62a2 2 0 0 1-2-2V51z', O) + P('M64 40h8v6h-8z', O) + leaf(68, 64, -70, 6, 2.2, False) +
    spark(70, 28, 2.4) + spark(26, 78, 1.3))
I['Na záclony'] = (  # okno se staženými záclonami
    P('M26 22h48', M) + P('M30 26h40v52H30z', D) +
    P('M30 24C34 40 36 50 40 56C36 64 34 72 32 80H26V24Z', O) + P('M70 24C66 40 64 50 60 56C64 64 66 72 68 80H74V24Z', O) +
    P('M28.6 30C31 44 33 50 36 56 M71.4 30C69 44 67 50 64 56', D) + P('M36 56c1.6 1.4 3 1.4 5 0 M59 56c2 1.4 3.4 1.4 5 0', M) +
    P('M50 26v52 M30 52h40', D) + spark(50, 40, 2.2) + spark(56, 66, 1.3))
I['Pro miminka'] = (  # dětské body a srdíčko
    P('M38 26C41 30 47 31 50 31S59 30 62 26L72 32L76 42L68 45V60C68 66 64 70 60 72L56 80H44L40 72C36 70 32 66 32 60V45L24 42L28 32Z', O) +
    P('M38 26C41 34 59 34 62 26', D) + P('M45 78h10', D) + C(47, 77, .8, F) + C(53, 77, .8, F) +
    P('M50 54c-1.4-2.6-5.2-2-5.2.8 0 2.2 2.6 3.8 5.2 5.6 2.6-1.8 5.2-3.4 5.2-5.6 0-2.8-3.8-3.4-5.2-.8z', O) +
    spark(78, 24, 2.2) + spark(22, 26, 1.4) + spark(80, 64, 1.2))
# ---------- MYTÍ NÁDOBÍ ----------
I['Ruční mytí'] = (  # houbička, talíř, kapky
    C(58, 52, 18, O) + C(58, 52, 12.4, D) + P('M49 44c2.4-3.4 5.4-5 9-5.4', D) +
    G('rotate(-18 34 66)', P('M22 60h24a3 3 0 0 1 3 3v4H19v-4a3 3 0 0 1 3-3z', O) + P('M19 67h30v7a3 3 0 0 1-3 3H22a3 3 0 0 1-3-3z', O) +
      ''.join(C(x, y, .7, F) for x, y in [(25, 71), (31, 73), (37, 71), (43, 73), (28, 75), (40, 75)])) +
    drop(76, 70, .8) + drop(70, 78, .6) + spark(30, 30, 2.6) + spark(40, 42, 1.4))
I['Mytí v myčce'] = (  # myčka s otevřenými dvířky, talíře, tableta
    P('M28 22h44v40H28z', O) + P('M28 30h44', D) + C(64, 26, 1.4, D) + P('M34 26h14', D) +
    P('M28 62h44l8 14H20z', O) + P('M30 66h40 M33 70h34', D) +
    C(40, 46, 9, O) + C(40, 46, 5.6, D) + C(58, 48, 7, O) + C(58, 48, 4.2, D) +
    P('M46 58.6h8l1.6 3.4h-11.2z', F) + spark(78, 30, 2.2) + spark(18, 40, 1.4) + spark(80, 50, 1.2))
