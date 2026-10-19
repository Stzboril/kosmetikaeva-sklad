# Luxusní linkové ilustrace kategorií – zlatá kresba (100×100). Paleta se volí v PAL.
PAL={
 'cerna':dict(bg0='#3a2530',bg1='#1b1015',ring='url(#gold)',g0='#f8e7b0',g1='#d6b062',g2='#a47a2e',fill='#d6b062',fillop='.16',name='Zlato na tmavé'),
 'slonovina':dict(bg0='#fffdf8',bg1='#f3eadb',ring='url(#gold)',g0='#e3c47a',g1='#b8913f',g2='#8a6420',fill='#c9a24b',fillop='.14',name='Zlato na slonovině'),
 'smaragd':dict(bg0='#1d5446',bg1='#0c2f27',ring='url(#gold)',g0='#f8e7b0',g1='#d6b062',g2='#a47a2e',fill='#d6b062',fillop='.16',name='Zlato na smaragdové'),
}
def defs(p):
    return (f'<defs><radialGradient id="bgg" cx=".35" cy=".28" r=".85"><stop offset="0" stop-color="{p["bg0"]}"/><stop offset="1" stop-color="{p["bg1"]}"/></radialGradient>'
            f'<linearGradient id="gold" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{p["g0"]}"/><stop offset=".5" stop-color="{p["g1"]}"/><stop offset="1" stop-color="{p["g2"]}"/></linearGradient></defs>')
def frame(p):
    return ('<circle cx="50" cy="50" r="48" fill="url(#bgg)"/>'
            '<circle cx="50" cy="50" r="45" fill="none" stroke="url(#gold)" stroke-width=".9" opacity=".85"/>'
            '<circle cx="50" cy="50" r="43.2" fill="none" stroke="url(#gold)" stroke-width=".35" opacity=".6"/>')
S='fill="none" stroke="url(#gold)" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"'
T='fill="none" stroke="url(#gold)" stroke-width="1.1" stroke-linecap="round" stroke-linejoin="round"'
def F(p): return f'fill="{p["fill"]}" fill-opacity="{p["fillop"]}"'
def star(x,y,s):
    return f'<path d="M{x} {y-s}C{x+s*.16} {y-s*.16} {x+s*.16} {y-s*.16} {x+s} {y}C{x+s*.16} {y+s*.16} {x+s*.16} {y+s*.16} {x} {y+s}C{x-s*.16} {y+s*.16} {x-s*.16} {y+s*.16} {x-s} {y}C{x-s*.16} {y-s*.16} {x-s*.16} {y-s*.16} {x} {y-s}Z" fill="url(#gold)"/>'
def leafo(x,y,ang,sc=1):
    return (f'<g transform="translate({x} {y}) rotate({ang}) scale({sc})"><path d="M0 0C4-7 13-9 20-7C17 0 8 4 0 0Z" {T}/>'
            f'<path d="M1.5 -.6C7-3 12-4.6 17-6.2" {T}/></g>')
def icons(p):
    f=F(p); I={}
    I['Obličej']=(
     f'<path d="M58 22C66 26 68 34 66.6 40.4C68 43.6 71 47.4 72.6 50.4C71.6 52.4 68.6 52.6 66.6 53.4C67.6 55 68.2 56.6 67.6 57.8C66.6 58.8 66.2 59.4 66.8 60.6C67.6 62.2 66.6 64 64.6 65C64.2 68.2 63 70.6 60.8 72C58.2 73.6 55.6 74.6 55.2 77L56.6 86" {S}/>'
     f'<path d="M58 22C45 19 31 28 30 44C29 56 33 64 40 72L41.6 86" {S}/>'
     f'<path d="M58 22C45 19 31 28 30 44C29 56 33 64 40 72C43.4 66 44.6 60 43.6 52.6C43 46.4 46.6 40.4 52.6 37.4C57 35 59.4 30 58 22Z" {f}/>'
     f'<path d="M55.4 26.6C47.6 26.4 40.4 32.4 38.4 43.4 M52.6 31.6C46 34.6 41.8 41.6 41.8 51.6C41.8 59 40 65 36.6 69.6 M48 25C42 26.4 36.4 31 34.2 38" {T}/>'
     f'<circle cx="33" cy="24" r="8.6" {S}/><circle cx="33" cy="24" r="8.6" {f}/>'
     f'<path d="M33 17.4C38 18.4 39.4 24.6 35 27.4C31.8 29.4 28 27 29 23.6" {T}/>'
     f'<path d="M57.4 42.6C59.4 44.6 62.2 44.8 64.2 43" {T}/><path d="M58.4 43.8l-1.1 1.5 M60.4 44.6l-.5 1.8 M62.5 44.6l-.1 1.9" {T}/>'
     '<path d="M66.6 57.6C67.7 58 68 58.7 67.3 59.3C66.9 59.7 66.9 60.2 67.6 60.8C67 61.7 65.2 61.5 64.8 60.4C64.5 59.4 65.2 57.4 66.6 57.6Z" fill="url(#gold)"/>'
     +star(79,29,5.6)+star(85,41,2.8)+
     f'<path d="M14.6 76C19 70 25 66.6 31.6 65.4" {T}/>'+leafo(16.4,73,-58,.5)+leafo(20.6,69.2,-62,.5)+leafo(25.6,66.6,-70,.45)+leafo(19,72,-150,.42)+leafo(24,68,-150,.4))
    I['Tělo']=(
     f'<path d="M47.6 21H36.6a3 3 0 0 0-3 3v2.6" {S}/><path d="M43.4 21v9" {S}/><rect x="38.6" y="30" width="13.8" height="8" rx="2" {S}/>'
     f'<path d="M36 38h19a6 6 0 0 1 6 6v34a6 6 0 0 1-6 6H36a6 6 0 0 1-6-6V44a6 6 0 0 1 6-6z" {S}/><path d="M36 38h19a6 6 0 0 1 6 6v34a6 6 0 0 1-6 6H36a6 6 0 0 1-6-6V44a6 6 0 0 1 6-6z" {f}/>'
     f'<rect x="37.6" y="52" width="16" height="20" rx="2.6" {T}/><path d="M34 44.6v30" {T} opacity=".6"/>'
     +leafo(41.6,67.4,-55,.55)+leafo(45.6,64,-118,.42)+
     f'<path d="M60 61h22a4 4 0 0 1 4 4v13a7 7 0 0 1-7 7H63a7 7 0 0 1-7-7V65a4 4 0 0 1 4-4z" {S}/><path d="M60 61h22a4 4 0 0 1 4 4v13a7 7 0 0 1-7 7H63a7 7 0 0 1-7-7V65a4 4 0 0 1 4-4z" {f}/>'
     f'<rect x="57.4" y="53.4" width="29.2" height="7.6" rx="3" {S}/><path d="M61 57.2h22" {T} opacity=".7"/>'
     f'<path d="M64.6 72.6c3-3.2 8.4-3.2 11.4 0" {T}/>'+star(80,30,5.4)+star(71.6,22.4,2.6))
    I['Parfémy']=(
     f'<rect x="40.6" y="18" width="18.8" height="14.6" rx="3.4" {S}/><path d="M44.2 21.4v8 M47.6 21.4v8 M51 21.4v8 M54.4 21.4v8" {T} opacity=".7"/>'
     f'<path d="M44.4 32.6h11.2v7.6H44.4z" {S}/>'
     f'<path d="M36 40h28a8 8 0 0 1 8 8v28a8 8 0 0 1-8 8H36a8 8 0 0 1-8-8V48a8 8 0 0 1 8-8z" {S}/><path d="M36 40h28a8 8 0 0 1 8 8v28a8 8 0 0 1-8 8H36a8 8 0 0 1-8-8V48a8 8 0 0 1 8-8z" {f}/>'
     f'<path d="M38.4 46.6h23.2a3.8 3.8 0 0 1 3.8 3.8v23.2a3.8 3.8 0 0 1-3.8 3.8H38.4a3.8 3.8 0 0 1-3.8-3.8V50.4a3.8 3.8 0 0 1 3.8-3.8z" {T}/>'
     f'<path d="M28.4 46l6.2 4.4 M71.6 46l-6.2 4.4 M28.4 78l6.2-4.4 M71.6 78l-6.2-4.4" {T}/>'
     f'<circle cx="50" cy="62" r="7" {T}/>'+star(50,62,3.8)+star(79,26,6)+star(21,38,3.4)+star(83,50,2.6))
    I['Vlasy']=(
     f'<path d="M44 14C64 18 70 36 58 48C46 60 46 74 62 86" {S}/><path d="M38.4 17.6C50.6 24 52.6 34.4 44.4 42.4C36.4 50.4 34.6 62 42.4 74" {S}/>'
     f'<path d="M41.4 15.6C57.6 21.2 61.6 35.6 51.2 45.4C41.4 55 40.2 67.6 51 80" {T}/><path d="M47.4 15.2C64 22 67.4 37.6 55.4 49.4C44.2 60.4 44.4 72 56.4 83" {T} opacity=".75"/>'
     f'<path d="M35.4 22C44.2 29 45.4 37.4 38.8 44.6C33 51 31.8 59.6 35.6 68" {T} opacity=".75"/>'
     '<g transform="rotate(-28 70 64)">'
     f'<rect x="52" y="57.6" width="38" height="8.4" rx="3" {S}/><rect x="52" y="57.6" width="38" height="8.4" rx="3" {f}/>'
     +''.join(f'<path d="M{55.6+i*3.3:.1f} 66v8.6" {T}/>' for i in range(10))+'</g>'
     +star(80,24,5.4)+star(24,30,2.8))
    I['Esenciální oleje']=(
     f'<path d="M44 34V21a5 5 0 0 1 10 0v13" {S}/><path d="M44 21a5 5 0 0 1 10 0v13H44z" {f}/><path d="M46.6 23.4v7" {T} opacity=".7"/>'
     f'<rect x="41" y="34" width="16" height="8" rx="2" {S}/>'
     f'<path d="M38 42h22a6 6 0 0 1 6 6v30a6 6 0 0 1-6 6H38a6 6 0 0 1-6-6V48a6 6 0 0 1 6-6z" {S}/><path d="M38 42h22a6 6 0 0 1 6 6v30a6 6 0 0 1-6 6H38a6 6 0 0 1-6-6V48a6 6 0 0 1 6-6z" {f}/>'
     f'<rect x="38" y="54" width="22" height="18" rx="2.6" {T}/>'
     '<path d="M49 57.4c2.3 3.1 4 5 4 7.1a4 4 0 0 1-8 0c0-2.1 1.7-4 4-7.1z" fill="url(#gold)"/>'
     f'<path d="M76.4 51.6c2.2 3 3.8 4.8 3.8 6.8a3.8 3.8 0 0 1-7.6 0c0-2 1.6-3.8 3.8-6.8z" {T}/><path d="M76.4 44.6v3 M76.4 41v1" {T} opacity=".7"/>'
     f'<path d="M21.6 74C23.4 58 27.6 44.6 34.4 33" {T}/>'
     +''.join(leafo(x,y,a,.42) for x,y,a in [(22.6,64,-72),(23.2,64,-140),(25.4,53.6,-64),(26.2,53.6,-132),(29,44.4,-58),(30,44.4,-126),(32.4,36.6,-52)])
     +star(81,30,5)+star(70.6,20.6,2.6))
    I['Pro děti']=(
     f'<path d="M14 75C26 69 40 71 50 75C62 79 76 77 88 71" {T}/><path d="M20 82.6C32 78.6 44 80.6 52 83.6C62 86.6 74 84.6 82 80.6" {T} opacity=".7"/>'
     f'<path d="M26 58C26 48 34 44 44 46C50 47 54 48 58 46C66 42 76 46 76 56C76 66 66 72 52 72H40C32 72 26 66 26 58Z" {S}/><path d="M26 58C26 48 34 44 44 46C50 47 54 48 58 46C66 42 76 46 76 56C76 66 66 72 52 72H40C32 72 26 66 26 58Z" {f}/>'
     f'<circle cx="62" cy="34" r="12.6" {S}/><circle cx="62" cy="34" r="12.6" {f}/>'
     f'<path d="M73.6 33.4c5-.6 9 .4 11 2.4c-2.2 1.8-6.6 2.6-11 1.6z" {S}/><path d="M74 36h9.4" {T} opacity=".7"/>'
     '<circle cx="66" cy="31" r="1.9" fill="url(#gold)"/>'
     f'<path d="M36 56C42 52 50 53 54 58C48 62 40 62 36 56Z" {T}/><path d="M40 57.4c3 1 7 1.2 10 .4" {T} opacity=".7"/>'
     f'<circle cx="23" cy="29" r="4.2" {T}/><circle cx="31" cy="19.6" r="2.6" {T}/><circle cx="82.6" cy="57.6" r="3" {T}/>'+star(84,22,3.4))
    I['Praní prádla']=(
     f'<rect x="25" y="19" width="50" height="63" rx="8.6" {S}/><rect x="25" y="19" width="50" height="63" rx="8.6" {f}/><path d="M25 33h50" {S}/>'
     '<circle cx="32.6" cy="26.2" r="1.9" fill="url(#gold)"/><circle cx="39.4" cy="26.2" r="1.9" fill="url(#gold)"/>'
     f'<rect x="55.6" y="24.6" width="13" height="3.2" rx="1.6" {T}/>'
     f'<circle cx="50" cy="57.4" r="16.8" {S}/><circle cx="50" cy="57.4" r="12.6" {T}/>'
     f'<path d="M38 60c4-2.8 8-2.8 12 0s8 2.8 12 0" {T}/><path d="M42.4 50.4c2.2-2.6 5-3.8 8-3.8" {T} opacity=".75"/>'
     f'<path d="M30 77.6h40" {T} opacity=".6"/>'
     f'<circle cx="80.6" cy="30" r="4.8" {T}/><circle cx="85.4" cy="43.4" r="2.8" {T}/><circle cx="17.6" cy="40" r="3.4" {T}/>'+star(18,58,2.6))
    I['Medové speciality']=(
     ''.join(f'<path d="M{x} {y}l4.6 2.7v5.3l-4.6 2.7-4.6-2.7v-5.3z" {T} opacity=".7"/>' for x,y in [(19.6,22.6),(28.8,22.6),(24.2,30.6),(15,30.6)])+
     f'<path d="M33 44h34a5 5 0 0 1 5 5v24a11 11 0 0 1-11 11H39a11 11 0 0 1-11-11V49a5 5 0 0 1 5-5z" {S}/><path d="M33 44h34a5 5 0 0 1 5 5v24a11 11 0 0 1-11 11H39a11 11 0 0 1-11-11V49a5 5 0 0 1 5-5z" {f}/>'
     f'<path d="M27.6 39.6c8 3 37 3 45 0l-1.6 5.6c-10 2.4-32 2.4-42 0z" {S}/><rect x="30" y="34.6" width="40" height="5.6" rx="2.4" {S}/>'
     f'<path d="M30.4 45.8c1.6 1.4 1.6 3.4.2 5" {T}/>'
     f'<rect x="38" y="56" width="24" height="16" rx="3.6" {T}/><path d="M50 59.4l3.6 2.1v4.2L50 67.8l-3.6-2.1v-4.2z" fill="url(#gold)"/>'
     '<g transform="rotate(32 70 34)">'
     f'<path d="M68 40V12a2 2 0 0 1 4 0v28" {S}/><rect x="65" y="34" width="10" height="13" rx="4.5" {S}/><path d="M65 37.6h10 M65 41h10 M65 44.4h10" {T}/></g>'
     f'<path d="M63 50c1.6 3 1.6 6 0 8.4" {S}/>'
     f'<g transform="translate(79 66)"><ellipse cx="0" cy="0" rx="5" ry="3.8" {S}/><path d="M-1.8 -3.6v7.2 M1.6 -3.7v7.4" {T}/>'
     f'<ellipse cx="-2" cy="-6" rx="3" ry="2" {T} transform="rotate(-20)"/><ellipse cx="2.6" cy="-5.6" rx="2.6" ry="1.8" {T} transform="rotate(18)"/><circle cx="5.6" cy="-.4" r="1.4" fill="url(#gold)"/></g>')
    return I
