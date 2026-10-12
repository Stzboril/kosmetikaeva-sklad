"""Sestaví ke-styl.css (ostrý) a ke-styl-nahled.css (jen pro přihlášeného správce)
s písmem Montserrat vloženým jako data URI (Správce souborů Shoptetu nepovoluje .woff)."""
import base64, re, os
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer
from fontTools import subset
SRC='/tmp/claude-0/-home-claude-kosmetikaeva-sklad/379fed50-5b74-5ed0-aa4f-c4a66db5392e/scratchpad/gf/ofl/montserrat/Montserrat[wght].ttf'
chars=set(range(0x20,0x7F))|set(range(0xA0,0x100))
chars|={ord(c) for c in 'ÁČĎÉĚÍŇÓŘŠŤÚŮÝŽáčďéěíňóřšťúůýžÄĹĽÔŔäĺľôŕŁłŐőŰűĆćŚśŹźŻżĄąĘę'}
chars|={0x2013,0x2014,0x2018,0x2019,0x201A,0x201C,0x201D,0x201E,0x2026,0x2022,0x20AC,0x2122,0x2192,0x2605,0x2713,0x2039,0x203A}
faces=[]
for w in (400,600,700):
    f=TTFont(SRC); inst=instancer.instantiateVariableFont(f,{'wght':w})
    o=subset.Options(); o.flavor='woff'; o.layout_features=['kern','liga','lnum','pnum','tnum','ccmp','locl','mark','mkmk','case']; o.notdef_outline=True; o.name_IDs=[1,2]
    s=subset.Subsetter(options=o); s.populate(unicodes=sorted(chars)); s.subset(inst)
    inst.flavor='woff'; p=f'fonts/montserrat-{w}.woff'; inst.save(p)
    b64=base64.b64encode(open(p,'rb').read()).decode()
    faces.append("@font-face{font-family:'Montserrat';font-style:normal;font-weight:%s;font-display:swap;src:url(data:font/woff;base64,%s) format('woff')}"%(w if w!=400 else '400 500',b64))
    print(w, os.path.getsize(p))
css=open('ke-styl.css',encoding='utf-8').read()
css=re.sub(r'@font-face\{[^}]*\}\s*','',css)
css=css.replace("/* ---------- Písmo Montserrat (OFL), uložené v e-shopu ---------- */","/* ---------- Písmo Montserrat (OFL, SIL Open Font License) – vložené přímo do stylu ---------- */\n"+"\n".join(faces))
open('ke-styl.min.css','w',encoding='utf-8').write(css)

def scope_sel(sel):
    out=[]
    for part in [p.strip() for p in re.split(r',(?![^(]*\))',sel)]:
        if not part: continue
        if part.startswith(':root'): out.append('body.admin-logged'+part[5:])
        elif re.match(r'body\b',part): out.append('body.admin-logged'+part[4:])
        else: out.append('body.admin-logged '+part)
    return ','.join(out)
def scope(block):
    res=''; i=0
    while i<len(block):
        j=block.find('{',i)
        if j<0: res+=block[i:]; break
        head=block[i:j]; pre=''
        m=re.match(r'(\s*(?:/\*[\s\S]*?\*/\s*)*)([\s\S]*)',head); pre,sel=m.group(1),m.group(2).strip()
        depth=1; k=j+1
        while depth:
            if block[k]=='{': depth+=1
            elif block[k]=='}': depth-=1
            k+=1
        body=block[j+1:k-1]
        if sel.startswith('@font-face'): res+=pre+sel+'{'+body+'}'
        elif sel.startswith('@media') or sel.startswith('@supports'): res+=pre+sel+'{'+scope(body)+'}'
        else: res+=pre+scope_sel(sel)+'{'+body+'}'
        i=k
    return res
open('ke-styl-nahled.css','w',encoding='utf-8').write(scope(re.sub(r'/\*[\s\S]*?\*/','',css)))
print(len(css), os.path.getsize('ke-styl-nahled.css'))
