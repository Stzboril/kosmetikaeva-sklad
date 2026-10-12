import json, re, collections
d=json.load(open('/home/claude/work/katalog.json'))
vis=[x for x in d if x[4]=='visible' and x[0]]
def stock(x):
    try:
        return float(x[8] or 0) > 0 or any(float(v.split('/')[1] or 0)>0 for v in x[11])
    except ValueError: return False
def low(n): return n.lower().replace('´',"'").replace('–','-')
def base(x): return re.sub(r'\s+',' ',re.sub(r'[\d.,]+\s*(ml|g|kg|l|ks|x)\b','',low(x[2]))).strip(' ,-')
def typ(x):
    n=low(x[2])
    for t in ['aviváž','prací gel','prací prostředek','parfémová sašetka','parfémový sáček','prostorové aromatikum','tekuté mýdlo','univerzální úklidový','parfém na praní','parfém do vysavače','parfém do vodního vysavače','žehlička','svíčka','difuzér','aromadifuzér','aroma parfém','esenciální olej','sprchový gel','tělový olej','olejový parfém','parfém','šampon','kondicionér','pěna do koupele','balzám','krém','sérum','tonikum','mléko','peeling','zubní pasta','ústní voda','sprej','kartáček','gel','mýdlo','set','sada']:
        if t in n: return t
    return n.split()[1] if len(n.split())>1 else n
groups=collections.defaultdict(list)
# A) Essens čísla vůní
for x in vis:
    if x[3]=='Essens':
        m=re.search(r'\b([wmu]\d{2,3}[a-z]?)\b', low(x[2]))
        if m: groups['ess_'+m.group(1)].append(x)
# B) Eurona vůně (CZ/EN synonyma)
SCENT={'adine':['adine'],'aiwysnow':['aiwysnow'],'amethis':['amethis','améthis'],'diwa vivien':['diwa vivien'],'diwa romantica':['diwa romantica'],
 'snowy white':['snowy white'],'angel rose':['angel rose'],'key to miracles':['key to miracles'],'enchanted beauty':['enchanted beauty'],
 'black grape':['black grape','černý hrozen'],'ice wind':['ice wind','ledový vítr'],'green':['green','zelená'],'lavender':['lavender','levandule'],
 'neria':['neria'],'lemon grass':['lemon grass','citronová tráva'],'amber vanilla':['amber vanilla','vanilková ambra'],'vesper':['vesper','večernice'],
 'black pearl':['black pearl','černá perla'],'spring aloe':['spring aloe','pramen aloe'],'apricot fayre':['apricot fayre','meruňková kráska'],
 'gia mena':['gia mena'],'lucky bells':['lucky bells'],"o'jingle":["o'jingle",'o´jingle','o--jingle','o jingle'],'garden of dreams':['garden of dreams'],
 'thought magic':['thought magic'],'faith magic':['faith magic'],'hope magic':['hope magic'],'moment magic':['moment magic'],
 'float ice':['float ice','ledová tříšť'],'ocean glow':['ocean glow','mořská záře'],'crystal flower':['crystal flower'],'raspberry mint':['raspberry & mint','raspberry mint'],
 'auri skye':['auri skye'],'cerny lavender':['cerny lavender']}
for x in vis:
    if x[3]!='Eurona': continue
    n=low(x[2]).replace('´',"'")
    keys=[k for k,syn in SCENT.items() if any(s in n for s in syn)]
    if 'green' in keys and any(w in n for w in ('neony','herbalist','velvet')): keys.remove('green')
    if 'cerny lavender' in keys and 'lavender' in keys: keys.remove('lavender')
    for k in keys: groups['eur_vune_'+k].append(x)
# C) Eurona řady
SER=[r'pure ways for her \w+', r'pure ways for him \w+', 'new uniqua', 'brilliant condition', 'delicate condition', 'nature condition', 'eco mimi', 'pure mimi',
     'go spunky', 'pinky frou', 'man zone', 'chlap v tísni', 'deep purify', 'vital essentia', 'sensitive clinic', r'eyos \w+', r'neony go\S* \w+ \w+', 'přírodní peelingy', 'pet zone']
for x in vis:
    if x[3]!='Eurona': continue
    n=low(x[2])
    for s in SER:
        m=re.search(s, n)
        if m: groups['eur_rada_'+m.group(0)].append(x)
# D) LR řady
for x in vis:
    if x[3]!='LR': continue
    n=low(x[2])
    for s in ['beauty diamonds','nutri-repair','mint & melon','zeitgard beauty','microsilver','aloe vera men','aloe vera kids','nanogold']:
        if s in n: groups['lr_'+s].append(x)
# E) Just
for x in vis:
    if x[3]!='Just': continue
    n=low(x[2])
    for s in ['eucasol','lamelloderm','bodyfresh','tea tree','manuk','rosalin','levandul','alpsk','tymián','slézov','san´activ',"san'activ",'calmoderm']:
        if s in n: groups['just_'+s].append(x)
rel=collections.defaultdict(list)
for g,items in groups.items():
    if len(items)<2: continue
    for x in items:
        if x[9]: continue
        for y in items:
            if y[0]==x[0] or base(y)==base(x): continue
            if typ(y)==typ(x) and not g.startswith('ess_'): continue  # stejný druh jen jiná vůně/velikost
            rel[x[0]].append((y, g))
# F) Křížové doplňky
code2={x[0]:x for x in vis}
def add(cond, targets):
    for x in vis:
        if x[9] or not cond(x): continue
        for t in targets:
            if t in code2 and t!=x[0]: rel[x[0]].append((code2[t],'doplnek'))
add(lambda x: x[3]=='Eurona' and ('univerzální úklidový' in low(x[2]) or 'koncentrát' in low(x[2])) and '1000' in x[2], ['4001','4050'])
add(lambda x: x[3]=='Eurona' and ('angelic lights' in low(x[2]) or 'esenciální olej' in low(x[2])), ['CA0175'])
names={x[0]:x[2] for x in vis}
out={}
for k,lst in rel.items():
    seen=set(); res=[]; types=set()
    lst.sort(key=lambda t:(not stock(t[0]), t[1]=='doplnek'))
    for y,g in lst:
        if y[0] in seen: continue
        if typ(y) in types and len(lst)>4: continue
        seen.add(y[0]); types.add(typ(y)); res.append(y[0])
        if len(res)==4: break
    out[k]=res
json.dump(out, open('/home/claude/work/souvisejici/navrh2.json','w'), ensure_ascii=False, indent=0)
print('produktů se souvisejícími', len(out))
print(collections.Counter(g.split('_')[0]+'_'+g.split('_')[1] for g in groups if len(groups[g])>1))
import random; random.seed(5)
for k in random.sample(sorted(out),30):
    print('\n'+names[k]); [print('   ->',names[c]) for c in out[k]]
