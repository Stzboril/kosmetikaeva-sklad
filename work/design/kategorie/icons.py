# Ilustrované ikony kategorií – styl „duotón“ (vínová, růžová, med), 100×100
DEFS='''<defs>
<linearGradient id="w" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#bf4b3a"/><stop offset="1" stop-color="#86271c"/></linearGradient>
<linearGradient id="wd" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#8e2c20"/><stop offset="1" stop-color="#5e1610"/></linearGradient>
<linearGradient id="r" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f6cfc5"/><stop offset="1" stop-color="#e3a194"/></linearGradient>
<linearGradient id="g" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f6c75a"/><stop offset="1" stop-color="#d98d1e"/></linearGradient>
<radialGradient id="bg" cx=".38" cy=".3" r=".8"><stop offset="0" stop-color="#fff8f6"/><stop offset="1" stop-color="#f8e6e1"/></radialGradient>
</defs>'''
BG='<circle cx="50" cy="50" r="48" fill="url(#bg)"/>'
def star(x,y,s,fill="#e39a8d"):
    return f'<path d="M{x} {y-s}C{x+s*.18} {y-s*.18} {x+s*.18} {y-s*.18} {x+s} {y}C{x+s*.18} {y+s*.18} {x+s*.18} {y+s*.18} {x} {y+s}C{x-s*.18} {y+s*.18} {x-s*.18} {y+s*.18} {x-s} {y}C{x-s*.18} {y-s*.18} {x-s*.18} {y-s*.18} {x} {y-s}Z" fill="{fill}"/>'
def leaf(x,y,ang,sc=1,fill="#e39a8d",vein="#fbf3f1"):
    return (f'<g transform="translate({x} {y}) rotate({ang}) scale({sc})"><path d="M0 0C4-7 13-9 20-7C17 0 8 4 0 0Z" fill="{fill}"/>'
            f'<path d="M1 -.4C7-3 12-4.5 17-6" fill="none" stroke="{vein}" stroke-width=".9" stroke-linecap="round"/></g>')
HL='fill="#fff" opacity=".42"'
I={}
I['Obličej']=(BG+'<path d="M14 66C24 56 40 54 52 62C40 64 26 70 14 66Z" fill="#f3d9d1"/>'
 '<path d="M60 22C67 26 69 34 67.6 40.4C69 43.6 72 47.4 73.6 50.4C72.6 52.4 69.6 52.6 67.6 53.4C68.6 55 69.2 56.6 68.6 57.8C67.6 58.8 67.2 59.4 67.8 60.6C68.6 62.2 67.6 64 65.6 65C65.2 68.2 64 70.6 61.8 72C59.2 73.6 56.6 74.6 56.2 77L58 90H40C41.6 84 41.6 78 39.6 73.6C32.6 65.6 29.6 57 30.6 46.6C32 31.6 44 21.4 60 22Z" fill="url(#r)"/>'
 '<path d="M59.6 22.6C46.6 19.6 31.6 28 30.2 44.6C29.2 56.6 32.8 65 39.8 73C43.4 67 44.6 60.6 43.6 53C43 46.6 46.8 40.4 53 37.4C57.6 35 60.2 30.4 59.6 22.6Z" fill="url(#w)"/>'
 '<circle cx="32.5" cy="25.5" r="9.5" fill="url(#w)"/>'
 '<path d="M27 22.5C28.5 19.6 31.6 18.2 34.6 18.8C31.8 19.8 29.8 21.4 28.6 24Z" '+HL+'/>'
 '<path d="M36.5 34C40 28.6 46 26 52 26.4C46.4 28 41.6 31 38.4 36Z" '+HL+'/>'
 '<path d="M57.6 42.6C59.6 44.6 62.4 44.8 64.4 43" fill="none" stroke="#6a1912" stroke-width="1.5" stroke-linecap="round"/>'
 '<path d="M58.4 43.8l-1.2 1.6 M60.4 44.6l-.6 1.9 M62.6 44.6l-.1 2" fill="none" stroke="#6a1912" stroke-width="1" stroke-linecap="round"/>'
 '<path d="M66.9 57.6C68 58 68.4 58.7 67.6 59.3C67.2 59.7 67.2 60.2 67.9 60.8C67.3 61.8 65.4 61.6 65 60.4C64.7 59.4 65.4 57.4 66.9 57.6Z" fill="#a3392a"/>'
 '<path d="M66 50.6C67 51.4 68 51.6 69 51.4" fill="none" stroke="#c97a6c" stroke-width="1" stroke-linecap="round"/>'
 +star(80,28,6)+star(86,42,3.2,"#f0b9ad")+leaf(16,74,-30,1.1))
I['Tělo']=(BG+'<path d="M18 80C30 66 54 64 82 74C64 84 38 88 18 80Z" fill="#f3d9d1"/>'
 '<path d="M48 21H36a3.4 3.4 0 0 0-3.4 3.4V27h4.2v-2h11.2z" fill="url(#wd)"/>'
 '<rect x="43" y="21" width="5" height="10" rx="1.2" fill="url(#wd)"/>'
 '<rect x="38.5" y="30" width="14" height="8" rx="2" fill="url(#wd)"/>'
 '<path d="M36 38h19a6 6 0 0 1 6 6v34a6 6 0 0 1-6 6H36a6 6 0 0 1-6-6V44a6 6 0 0 1 6-6z" fill="url(#w)"/>'
 '<rect x="34.5" y="42" width="3.2" height="36" rx="1.6" '+HL+'/>'
 '<rect x="38" y="52" width="16" height="20" rx="3" fill="#fbf3f1"/>'
 +leaf(41,67,-50,.7,"#e39a8d","#fbf3f1")+leaf(46,67,-120,.55,"#c97a6c","#fbf3f1")+
 '<path d="M60 60h22a4 4 0 0 1 4 4v14a7 7 0 0 1-7 7H63a7 7 0 0 1-7-7V64a4 4 0 0 1 4-4z" fill="url(#r)"/>'
 '<rect x="57" y="53" width="30" height="9" rx="3.5" fill="url(#wd)"/>'
 '<rect x="60" y="54.6" width="20" height="1.8" rx=".9" '+HL+'/>'
 '<rect x="59.5" y="65" width="2.6" height="14" rx="1.3" '+HL+'/>'
 '<path d="M66 70c3-3 8-3 11 0" fill="none" stroke="#fbf3f1" stroke-width="1.6" stroke-linecap="round"/>'
 +star(80,30,5.5)+star(72,22,2.8,"#f0b9ad"))
I['Parfémy']=(BG+'<ellipse cx="50" cy="84" rx="26" ry="5" fill="#f3d9d1"/>'
 '<rect x="40" y="18" width="20" height="15" rx="4" fill="url(#r)"/>'
 '<rect x="42.5" y="20" width="3" height="11" rx="1.5" '+HL+'/>'
 '<rect x="44" y="32" width="12" height="9" rx="1.5" fill="url(#wd)"/>'
 '<path d="M36 40h28a8 8 0 0 1 8 8v28a8 8 0 0 1-8 8H36a8 8 0 0 1-8-8V48a8 8 0 0 1 8-8z" fill="url(#w)"/>'
 '<path d="M38 46h24a4 4 0 0 1 4 4v24a4 4 0 0 1-4 4H38a4 4 0 0 1-4-4V50a4 4 0 0 1 4-4z" fill="#c75747" opacity=".55"/>'
 '<path d="M34 50l6-4 M66 50l-6-4 M34 74l6 4 M66 74l-6 4" stroke="#6a1912" stroke-width=".8" opacity=".5"/>'
 '<rect x="31.5" y="45" width="3.2" height="32" rx="1.6" '+HL+'/>'
 '<path d="M42 52c4-3 9-3.4 13-1.6" fill="none" stroke="#fff" stroke-width="1.6" stroke-linecap="round" opacity=".5"/>'
 '<circle cx="50" cy="62" r="6.5" fill="#fbf3f1" opacity=".9"/>'
 +star(50,62,3.6,"#c75747")+star(78,28,6.5)+star(22,40,4,"#f0b9ad")+star(81,52,3,"#e39a8d"))
I['Vlasy']=(BG+'<path d="M16 72C28 62 50 62 76 70C58 80 34 82 16 72Z" fill="#f3d9d1"/>'
 '<path d="M44 14C64 18 70 36 58 48C46 60 46 74 62 86C40 84 28 72 32 58C35 48 47 42 47 31C47 24 46 19 44 14Z" fill="url(#w)"/>'
 '<path d="M38 18C50 24 52 34 44 42C36 50 34 62 42 74C30 68 26 56 30 46C33 39 39 34 38 18Z" fill="url(#wd)"/>'
 '<path d="M48 22C57 27 60 36 54 44" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" opacity=".45"/>'
 '<path d="M50 56C46 63 48 72 54 78" fill="none" stroke="#fff" stroke-width="1.6" stroke-linecap="round" opacity=".35"/>'
 '<g transform="rotate(-28 70 64)"><rect x="52" y="58" width="38" height="8" rx="3" fill="url(#r)"/>'
 +''.join(f'<rect x="{55+i*3.3:.1f}" y="65.4" width="1.8" height="9" rx=".9" fill="#e3a194"/>' for i in range(10))+
 '<rect x="54" y="59.5" width="34" height="1.6" rx=".8" '+HL+'/></g>'
 +star(80,24,5.5)+star(24,30,3,"#f0b9ad"))
I['Esenciální oleje']=(BG+'<path d="M20 82C32 72 56 72 80 80C62 88 38 90 20 82Z" fill="#f3d9d1"/>'
 '<path d="M44 21a5 5 0 0 1 10 0v13H44z" fill="url(#r)"/>'
 '<rect x="45.6" y="22" width="2.2" height="10" rx="1.1" '+HL+'/>'
 '<rect x="41" y="33" width="16" height="9" rx="2" fill="url(#wd)"/>'
 '<path d="M38 42h22a6 6 0 0 1 6 6v30a6 6 0 0 1-6 6H38a6 6 0 0 1-6-6V48a6 6 0 0 1 6-6z" fill="url(#w)"/>'
 '<rect x="35.5" y="46" width="3" height="33" rx="1.5" '+HL+'/>'
 '<rect x="38" y="54" width="22" height="18" rx="3" fill="#fbf3f1"/>'
 '<path d="M49 57c2.4 3.2 4.2 5.2 4.2 7.4a4.2 4.2 0 0 1-8.4 0c0-2.2 1.8-4.2 4.2-7.4z" fill="#c75747"/>'
 '<path d="M76 52c2.2 3 3.8 4.8 3.8 6.8a3.8 3.8 0 0 1-7.6 0c0-2 1.6-3.8 3.8-6.8z" fill="url(#g)"/>'
 '<path d="M74.6 57.6a1.6 1.6 0 0 0 1 2" stroke="#fff" stroke-width="1" fill="none" stroke-linecap="round" opacity=".7"/>'
 '<path d="M22 70C24 56 28 44 34 34" fill="none" stroke="#c97a6c" stroke-width="1.6" stroke-linecap="round"/>'
 +''.join(leaf(x,y,a,.42,"#e39a8d","#fbf3f1") for x,y,a in [(23,62,-70),(23.6,62,-135),(26,52,-62),(26.6,52,-128),(29.6,43,-56),(30.4,43,-122)])
 +star(80,30,5)+star(70,20,2.6,"#f0b9ad"))
I['Pro děti']=(BG+'<path d="M14 74C26 68 40 70 50 74C62 78 76 76 88 70" fill="none" stroke="#e8b9ae" stroke-width="2.4" stroke-linecap="round"/>'
 '<path d="M20 82C32 78 44 80 52 83C62 86 74 84 82 80" fill="none" stroke="#f0cfc7" stroke-width="2" stroke-linecap="round"/>'
 '<path d="M26 58C26 48 34 44 44 46C50 47 54 48 58 46C66 42 76 46 76 56C76 66 66 72 52 72H40C32 72 26 66 26 58Z" fill="url(#r)"/>'
 '<circle cx="62" cy="34" r="13" fill="url(#r)"/>'
 '<path d="M73 34c5-.6 9 .4 11 2.4c-2.2 1.8-6.6 2.6-11 1.6z" fill="url(#w)"/>'
 '<circle cx="66" cy="31" r="2.2" fill="#5e1610"/><circle cx="66.7" cy="30.3" r=".7" fill="#fff"/>'
 '<path d="M36 56C42 52 50 53 54 58C48 62 40 62 36 56Z" fill="#e3a194"/>'
 '<path d="M52 24C55 21.4 59 20.6 62 21.4C58 22.4 55.6 23.6 53.6 26Z" '+HL+'/>'
 '<path d="M30 54C31 49.6 34.6 47.4 39 47.4C35.4 48.6 33 50.6 31.6 55Z" '+HL+'/>'
 '<circle cx="24" cy="30" r="4.2" fill="none" stroke="#e39a8d" stroke-width="1.4"/><circle cx="31" cy="20" r="2.6" fill="none" stroke="#f0b9ad" stroke-width="1.2"/><circle cx="82" cy="58" r="3" fill="none" stroke="#e39a8d" stroke-width="1.2"/>')
I['Praní prádla']=(BG+'<rect x="25" y="20" width="50" height="62" rx="9" fill="url(#w)"/>'
 '<rect x="25" y="20" width="50" height="14" rx="9" fill="url(#wd)"/><rect x="25" y="28" width="50" height="6" fill="url(#wd)"/>'
 '<circle cx="33" cy="27" r="2" fill="#f3d9d1"/><circle cx="40" cy="27" r="2" fill="#f3d9d1"/><rect x="56" y="25.6" width="13" height="3" rx="1.5" fill="#f3d9d1"/>'
 '<circle cx="50" cy="57" r="17" fill="#fbf3f1"/><circle cx="50" cy="57" r="13" fill="url(#r)"/>'
 '<path d="M37.4 59.6c4.2-3 8.4-3 12.6 0s8.4 3 12.6 0V60a12.6 12.6 0 0 1-25.2 0z" fill="#c75747" opacity=".85"/>'
 '<path d="M41 50c2.4-3 5.6-4.4 9-4.4" fill="none" stroke="#fff" stroke-width="1.6" stroke-linecap="round" opacity=".7"/>'
 '<rect x="28" y="38" width="2.6" height="38" rx="1.3" '+HL+'/>'
 '<circle cx="80" cy="30" r="5" fill="#fbf3f1" stroke="#e39a8d" stroke-width="1.3"/><circle cx="85" cy="44" r="3" fill="#fbf3f1" stroke="#e39a8d" stroke-width="1.1"/><circle cx="18" cy="40" r="3.6" fill="#fbf3f1" stroke="#e39a8d" stroke-width="1.2"/>'
 '<circle cx="78.6" cy="28.6" r="1.2" fill="#fff"/>')
I['Medové speciality']=(BG+''.join(f'<path d="M{x} {y}l5 2.9v5.8l-5 2.9-5-2.9v-5.8z" fill="none" stroke="#efc9bf" stroke-width="1.2"/>' for x,y in [(20,22),(30,22),(25,30.7),(15,30.7)])+
 '<path d="M33 44h34a5 5 0 0 1 5 5v24a11 11 0 0 1-11 11H39a11 11 0 0 1-11-11V49a5 5 0 0 1 5-5z" fill="url(#g)"/>'
 '<path d="M30 40h40l2 6H28z" fill="url(#r)"/><path d="M27 39c8 3 38 3 46 0l-1 4c-10 2.4-34 2.4-44 0z" fill="#e3a194"/>'
 '<rect x="30" y="35" width="40" height="6" rx="2.5" fill="url(#wd)"/>'
 '<rect x="38" y="56" width="24" height="16" rx="4" fill="#fbf3f1"/>'
 '<path d="M50 59.4l3.6 2.1v4.2L50 67.8l-3.6-2.1v-4.2z" fill="url(#g)"/>'
 '<rect x="31.5" y="49" width="3" height="28" rx="1.5" '+HL+'/>'
 '<g transform="rotate(32 70 34)"><rect x="68" y="10" width="4" height="30" rx="2" fill="#c98a5a"/>'
 '<rect x="65" y="34" width="10" height="13" rx="4.5" fill="#c98a5a"/><path d="M65 37.6h10 M65 41h10 M65 44.4h10" stroke="#a46a40" stroke-width="1.1"/></g>'
 '<path d="M63 50c1.6 3 1.6 6 0 8.4" fill="none" stroke="url(#g)" stroke-width="2.6" stroke-linecap="round"/>'
 '<g transform="translate(78 64)"><ellipse cx="0" cy="0" rx="5" ry="3.8" fill="url(#g)"/><path d="M-2 -3.6v7.2 M1.4 -3.7v7.4" stroke="#5e1610" stroke-width="1.3"/>'
 '<ellipse cx="-1.5" cy="-5.4" rx="3" ry="2" fill="#fff" opacity=".85" transform="rotate(-20)"/><ellipse cx="2.4" cy="-5" rx="2.6" ry="1.8" fill="#fff" opacity=".75" transform="rotate(18)"/><circle cx="5.2" cy="-.4" r="1.6" fill="#5e1610"/></g>')
