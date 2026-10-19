# Luxusní linkové ilustrace kategorií v2 – slonovina a zlato, jemná „rytina“ (100×100)
import math
BGF='#fbf6ec'   # výplň pro překrytí čar (barva pozadí uprostřed)
DEFS=('<defs><radialGradient id="bgg" cx=".38" cy=".3" r=".85"><stop offset="0" stop-color="#fffdf8"/><stop offset="1" stop-color="#f2e8d6"/></radialGradient>'
      '<linearGradient id="gold" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#d9b86e"/><stop offset=".5" stop-color="#ad8433"/><stop offset="1" stop-color="#7f5b1d"/></linearGradient></defs>')
FRAME=('<circle cx="50" cy="50" r="48" fill="url(#bgg)"/>'
       '<circle cx="50" cy="50" r="45.2" fill="none" stroke="url(#gold)" stroke-width=".9"/>'
       '<circle cx="50" cy="50" r="43.4" fill="none" stroke="url(#gold)" stroke-width=".35"/>')
M='fill="none" stroke="url(#gold)" stroke-width="1.25" stroke-linecap="round" stroke-linejoin="round"'
D='fill="none" stroke="url(#gold)" stroke-width=".8" stroke-linecap="round" stroke-linejoin="round"'
O=f'fill="{BGF}" stroke="url(#gold)" stroke-width="1.25" stroke-linecap="round" stroke-linejoin="round"'
def spark(x,y,s): return f'<path d="M{x} {y-s}Q{x} {y} {x+s} {y}Q{x} {y} {x} {y+s}Q{x} {y} {x-s} {y}Q{x} {y} {x} {y-s}Z" fill="url(#gold)"/>'
def leaf(x,y,ang,l=9,w=3.4,vein=True):
    p=f'<g transform="translate({x} {y}) rotate({ang})"><path d="M0 0Q{l*.45} {-w} {l} 0Q{l*.45} {w} 0 0Z" {D}/>'
    if vein: p+=f'<path d="M.8 0H{l*.8}" {D} opacity=".7"/>'
    return p+'</g>'
def roundleaf(x,y,r): return f'<circle cx="{x}" cy="{y}" r="{r}" {D}/><path d="M{x-r*.6} {y+r*.2}Q{x} {y-r*.2} {x+r*.6} {y-r*.5}" {D} opacity=".6"/>'
I={}
# Obličej – kelímek krému a sérum s pipetou, větvička
I['Obličej']=(
 f'<path d="M24 74C26 60 31 49 39 41" {D}/>'+''.join(leaf(x,y,a,8,3) for x,y,a in [(27.2,64,-100),(27.6,64,-20),(31,54,-108),(31.6,54,-28),(35.6,46,-115),(36,46,-35)])+
 f'<path d="M66 44h10a2.4 2.4 0 0 1 2.4 2.4V80a2.6 2.6 0 0 1-2.6 2.6h-9.6a2.6 2.6 0 0 1-2.6-2.6V46.4A2.4 2.4 0 0 1 66 44z" {O}/>'
 f'<path d="M66.4 39h9.2v5h-9.2z" {O}/><path d="M67.6 39v-6.6a3.4 3.4 0 0 1 6.8 0V39" {O}/><path d="M71 44v28" {D} stroke-dasharray="1.4 1.4"/><path d="M71 72v3" {D}/>'
 f'<path d="M66 50h12" {D} opacity=".6"/>'
 f'<path d="M30 62h32v15a5.5 5.5 0 0 1-5.5 5.5h-21A5.5 5.5 0 0 1 30 77z" {O}/>'
 f'<path d="M28.6 55.4a2.4 2.4 0 0 1 2.4-2.4h30a2.4 2.4 0 0 1 2.4 2.4V62H28.6z" {O}/>'
 +''.join(f'<path d="M{31.6+i*2.6:.1f} 54.6v5.8" {D} opacity=".55"/>' for i in range(12))+
 f'<path d="M34 68.6h24 M38 73h16" {D}/>'+spark(46,70.8,1.4)+spark(70,24,2.6)+spark(80,34,1.6))
# Tělo – vysoká lahvička s pumpičkou, eukalyptus
I['Tělo']=(
 f'<path d="M60 84C66 66 70 52 72 34" {D}/>'+''.join(roundleaf(x,y,r) for x,y,r in [(65.6,72,3.6),(70.4,64,3.4),(66.6,58,3),(72.2,50,3.2),(68.8,44,2.8),(73,37,2.6)])+
 f'<path d="M40.4 42.6Q39 44.4 39 47v31a5 5 0 0 0 5 5h12a5 5 0 0 0 5-5V47q0-2.6-1.4-4.4L56.6 39H43.4z" {O}/>'
 f'<path d="M45 33h10v6H45z" {O}/><path d="M43.4 27.4h13.2v5.6H43.4z" {O}/><path d="M56.6 29H63q3 0 3 3v1.6" {M}/><path d="M48.6 27.4V22h2.8v5.4" {M}/>'
 f'<path d="M43.6 55h12.8v15H43.6z" {D}/><path d="M46.4 60h7.2 M47.6 64.6h4.8" {D}/>'+spark(50,58,1.1)+
 f'<path d="M41.6 48v26" {D} opacity=".5"/>'+spark(28,30,2.6)+spark(31,42,1.4))
# Parfémy – broušený flakon se zátkou a střapcem
I['Parfémy']=(
 f'<path d="M41 49H59L65 55V71L59 77H41L35 71V55Z" {O}/><path d="M43.2 53H56.8L61 57.2V68.8L56.8 73H43.2L39 68.8V57.2Z" {D}/>'
 f'<path d="M41 49L43.2 53 M59 49L56.8 53 M65 55L61 57.2 M65 71L61 68.8 M59 77L56.8 73 M41 77L43.2 73 M35 71L39 68.8 M35 55L39 57.2" {D}/>'
 f'<path d="M46 49v-5h8v5" {M}/><path d="M44.4 44h11.2v-2.8H44.4z" {O}/>'
 f'<path d="M50 20L56.4 29.6 53.2 41.2H46.8L43.6 29.6Z" {O}/><path d="M50 20V41.2 M43.6 29.6H56.4 M46.8 41.2L50 29.6 53.2 41.2" {D}/>'
 f'<path d="M55.6 42.6C61 43 64.6 46 65.6 50.6" {D}/><circle cx="65.8" cy="52" r="1.5" {D}/>'
 +''.join(f'<path d="M{64.2+i*.8:.1f} 53.4L{63.4+i*1.1:.1f} 61" {D}/>' for i in range(5))+
 f'<path d="M50 59.4l2.2 3.6L50 66.6 47.8 63Z" {D}/>'+spark(29,31,2.4)+spark(73,30,1.6))
# Vlasy – vlnitý pramen jemných linek a sponka s perlou
def strand(dx,k):
    p=[(40,17),(62,21),(66,40),(54,50),(42,60),(44,74),(60,84)]
    q=[(x+dx*(1-.3*abs(y-50)/34),y) for x,y in p]
    return f'M{q[0][0]:.1f} {q[0][1]}C{q[1][0]:.1f} {q[1][1]} {q[2][0]:.1f} {q[2][1]} {q[3][0]:.1f} {q[3][1]}C{q[4][0]:.1f} {q[4][1]} {q[5][0]:.1f} {q[5][1]} {q[6][0]:.1f} {q[6][1]}'
I['Vlasy']=(
 ''.join(f'<path d="{strand(dx,0)}" {M if dx in (-7,7) else D}/>' for dx in (-7,-4.6,-2.3,0,2.3,4.6,7))+
 f'<path d="M58 30.6L76 23.4" {M}/><path d="M58.6 32.6L74.8 26.2" {D}/><circle cx="78" cy="22.6" r="2.6" {O}/><path d="M77 21.6a1.2 1.2 0 0 1 1.3-.7" {D}/>'
 +spark(27,40,2.2)+spark(74,70,2.6)+spark(79,61,1.3))
# Esenciální oleje – lékárenská lahvička s kapátkem, levandule
I['Esenciální oleje']=(
 f'<path d="M46 40v7.4a15 15 0 1 0 8 0V40z" {O}/><path d="M44.4 34.6h11.2V40H44.4z" {O}/><path d="M46.6 34.6v-6.4a3.4 3.4 0 0 1 6.8 0v6.4" {O}/>'
 f'<path d="M50 40v15.6" {D} stroke-dasharray="1.4 1.4"/>'
 f'<path d="M41.4 70.6a10 10 0 0 0 17.2 0" {D} opacity=".6"/>'
 f'<path d="M50 59.6c1.7 2.3 3 3.8 3 5.3a3 3 0 0 1-6 0c0-1.5 1.3-3 3-5.3z" fill="url(#gold)"/>'
 f'<path d="M26 84C29 70 32 58 38 44" {D}/><path d="M30 84C31 74 33 66 36 58" {D}/>'
 +''.join(f'<ellipse cx="{x:.1f}" cy="{y:.1f}" rx="1.3" ry="2.1" transform="rotate({a} {x:.1f} {y:.1f})" {D}/>' for x,y,a in [(36.6,46,-25),(39.4,47.6,25),(35.2,50.4,-25),(38.2,52,25),(34,55,-25),(37,56.6,25),(32.8,59.6,-25),(35.8,61.2,25),(38.2,42.2,0)])
 +leaf(29.4,74,-140,7,2.4)+leaf(30.4,70,-35,7,2.4)+spark(72,32,2.4)+spark(76,44,1.3))
# Pro děti – měsíček, hvězdička na nitce, obláček
def crescent(cx,cy,R,cx2,cy2,r):
    d=math.hypot(cx2-cx,cy2-cy); a=(R*R-r*r+d*d)/(2*d); h=math.sqrt(R*R-a*a)
    ux,uy=(cx2-cx)/d,(cy2-cy)/d; px,py=cx+a*ux,cy+a*uy
    p1=(px-h*uy,py+h*ux); p2=(px+h*uy,py-h*ux)
    return f'M{p1[0]:.2f} {p1[1]:.2f}A{R} {R} 0 1 1 {p2[0]:.2f} {p2[1]:.2f}A{r} {r} 0 1 0 {p1[0]:.2f} {p1[1]:.2f}Z'
I['Pro děti']=(
 f'<path d="{crescent(46,52,20,55,45,17)}" {O}/><path d="{crescent(46,52,16.6,52.6,47.4,14.6)}" {D} opacity=".55"/>'
 f'<path d="M66 21v15" {D}/><path d="M66 36.4l1.6 3.4 3.7.5-2.7 2.6.7 3.7-3.3-1.8-3.3 1.8.7-3.7-2.7-2.6 3.7-.5z" {O}/>'
 f'<path d="M30 80.4h34a5 5 0 0 0 0-10a7 7 0 0 0-12.6-3.2a6 6 0 0 0-10 3.6a4.8 4.8 0 0 0-11.4 4.8A2.4 2.4 0 0 0 30 80.4z" {O}/>'
 +spark(76,56,2.4)+spark(28,34,1.8)+spark(80,30,1.3)+spark(35,24,1.2))
# Praní prádla – složené ručníky, levandule
def towel(y,w,x0):
    return (f'<path d="M{x0+4} {y}H{x0+w}V{y+9}H{x0+4}A4.5 4.5 0 0 1 {x0+4} {y}Z" {O}/>'
            f'<path d="M{x0+5} {y+6.6}H{x0+w-2}" {D} stroke-dasharray="1.2 1.6"/><path d="M{x0+w-6} {y}V{y+9}" {D} opacity=".6"/>')
I['Praní prádla']=(towel(73,42,27)+towel(64,40,29)+towel(55,38,31)+
 f'<path d="M34 51.6C44 47 56 43 68 39" {D}/>'
 +''.join(f'<ellipse cx="{x:.1f}" cy="{y:.1f}" rx="1.2" ry="2" transform="rotate({a} {x:.1f} {y:.1f})" {D}/>' for x,y,a in [(58.8,40.4,-60),(60.4,43.6,15),(62.6,38.6,-60),(64.2,41.8,15),(66.4,37,-60),(68,40.2,15),(70.6,37.6,-40)])
 +leaf(40,50,-110,7,2.4)+leaf(44,48.4,-30,7,2.4)
 +f'<path d="M73 48c1.4 1.9 2.4 3.1 2.4 4.3a2.4 2.4 0 0 1-4.8 0c0-1.2 1-2.4 2.4-4.3z" {D}/>'+spark(28,36,2.2)+spark(76,64,1.4))
# Medové speciality – naběračka s kapkou, rytá včela, plástev
def hexa(x,y,r): return 'M'+' '.join(f'{x+r*math.cos(math.radians(60*i+30)):.2f} {y+r*math.sin(math.radians(60*i+30)):.2f}' for i in range(6))+'Z'
I['Medové speciality']=(
 ''.join(f'<path d="{hexa(x,y,4.6)}" {D} opacity=".55"/>' for x,y in [(66,70),(74,70),(70,77),(62,77),(78,77),(70,63)])+
 '<g transform="rotate(38 50 52)">'
 f'<path d="M48.6 18h2.8v26h-2.8z" {O}/><circle cx="50" cy="16.6" r="2.2" {O}/>'
 f'<path d="M44 44h12a2 2 0 0 1 2 2v1.4q-3 1.8 0 3.6v1.6q-3 1.8 0 3.6v1.6q-3 1.8 0 3.6V63a2 2 0 0 1-2 2H44a2 2 0 0 1-2-2v-1.6q3-1.8 0-3.6v-1.6q3-1.8 0-3.6v-1.6q3-1.8 0-3.6V46a2 2 0 0 1 2-2z" {O}/>'
 f'<path d="M44 49.2h12 M44 54.4h12 M44 59.6h12" {D}/></g>'
 f'<path d="M41.6 63.6c.6 2.6.4 5-.6 6.8" {M}/><path d="M40.8 73c1.5 2 2.6 3.3 2.6 4.6a2.6 2.6 0 0 1-5.2 0c0-1.3 1.1-2.6 2.6-4.6z" fill="url(#gold)"/>'
 '<g transform="translate(29 31) rotate(-20)">'
 f'<ellipse cx="0" cy="0" rx="6.4" ry="4.2" {O}/><path d="M-2.4 -4v8 M.8 -4.2v8.4 M3.8 -3.4v6.8" {D}/>'
 f'<circle cx="-8" cy="-.4" r="2.4" {O}/><path d="M-9.4 -2.4l-2.2-3 M-8.2 -2.8l-.6-3.6" {D}/><path d="M6.4 0l2.2 .4" {M}/>'
 f'<path d="M-2 -4C-5 -12 2 -14 2.6 -5" {D}/><path d="M1.4 -4.4C3 -11.6 9.6 -10 4.6 -3.6" {D}/></g>'
 +spark(72,30,2.4)+spark(78,44,1.3))
