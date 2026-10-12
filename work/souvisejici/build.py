import json, re, collections, math
d=json.load(open('/home/claude/work/katalog.json'))
vis=[x for x in d if x[4]=='visible' and x[0]]
BR=('Eurona','Essens','LR','Just','Nahrin','wellU')
STOP=set('''pro prostředek aloe vera parfém gel mýdlo aromatikum prostorové tekuté praní aviváž parfémová sašetka přírodní čisticí univerzální olej aroma
kondicionér prací úklidový čistič sprchový nádobí jemný ženy kondicionérem hydratační pečující ruční roll-on sprej mytí olejový tyčinka muže tuhé
designová designový tekutý new šampon krém ochranný svíčka vonná tělový aktivní prádla speciální bio delikatesa raw vysavače dámský pánský set
parfémovaný stravy doplněk refill rty esenciální soft lesk oční matná tekutá tužka klasická luxusní kapsle série edp signature plus měsíce sérum
maska balzám mléko deo vlasy koupel esence care opalovací spf for the and with s se na do od a v z k ke ve ze bez pod nad při pro-
difuzér aroma-difuzér aromadifuzér svíčka parfémový sáček pohlcovač pachů pachu čaj sypaný perlivý ledový medová granola nápoj káva zrnková
doplňky kapslí tablet tablety sada dárková edice vánoční balení ks gelový krémový tělové tělo obličej obličejový pleťové pleťový pleťová
denní noční péče voda spray mist drink zubní pasta kartáček proti ochrana vlasů typy všechny barvené suché vlasové pěna holení po
prostředkem pečující vonný olejový parfémem parfém-ve zdarma zdravá zdraví active elixír intenzivní regenerační vyživující čistící
jemné jemná detská dětský dětská miminka pro-miminka ml g kg cm mini maxi velký malý duo trio mix'''.split())
def norm(n):
    n=n.lower().replace('´',"'").replace('`',"'")
    n=re.sub(r'\d+[.,]?\d*\s*(ml|g|kg|l|ks|tablet|tbl|kapslí|cps|x)\b',' ',n)
    return n
def toks(x):
    b=x[3]; n=norm(x[2]).replace(b.lower(),' ')
    w=re.findall(r"[a-z0-9áčďéěíňóřšťúůýž'+-]+", n)
    w=[t.strip("-'") for t in w]
    t=set(t for t in w if len(t)>2 and t not in STOP and not t.isdigit())
    # bigrams for multiword lines
    ws=[t for t in w if t not in STOP]
    return t
def base(x):  # product identity without size
    return re.sub(r'\s+',' ',re.sub(r'[\d.,]+\s*(ml|g|kg|l|ks|x)\b','',x[2].lower())).strip(' ,')
by=collections.defaultdict(list)
for x in vis:
    if x[3] in BR: by[x[3]].append(x)
stock=lambda x: float(x[8] or 0) > 0 or any(float((v.split('/')[1] or 0))>0 for v in x[11])
rel={}
for b,items in by.items():
    T={x[0]:toks(x) for x in items}
    df=collections.Counter(t for v in T.values() for t in v)
    N=len(items)
    for x in items:
        if x[9]: continue  # už má související
        bx=base(x); cand=[]
        for y in items:
            if y[0]==x[0] or base(y)==bx: continue
            sh=T[x[0]]&T[y[0]]
            sh={t for t in sh if 2<=df[t]<=max(25,N//15)}
            if not sh: continue
            s=sum(math.log(N/df[t]) for t in sh)
            # stejný typ výrobku jen jinou velikostí/vůní se nepočítá jako souvisejicí: penalizace, když se liší jen v jednom tokenu
            if len(T[x[0]]^T[y[0]])<=1: continue
            s += 0.5 if stock(y) else -2
            cand.append((s,y[0],y[2]))
        cand.sort(reverse=True)
        top=[c for c in cand if c[0]>=2.5][:4]
        if top: rel[x[0]]=top
json.dump({k:[[c[1],c[2],round(c[0],1)] for c in v] for k,v in rel.items()}, open('/home/claude/work/souvisejici/navrh.json','w'), ensure_ascii=False, indent=0)
names={x[0]:x[2] for x in vis}
print('produktů s návrhem', len(rel), 'z', sum(len(v) for v in by.values()))
import random; random.seed(3)
for k in random.sample(sorted(rel),25):
    print('\n'+names[k]); [print('   ->',c[2],c[0]) for c in [(c[1],c[2],round(c[0],1)) for c in rel[k]]]
