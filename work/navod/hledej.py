import json,re,html,sys
d=json.load(open('/home/claude/work/navod/shop_usage.json'))
def t(h): return re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>',' ',h))).strip()
for q in sys.argv[1:]:
    rx=re.compile(q,re.I)
    hits=[x for x in d if rx.search(x['name'])]
    print(f'=== {q}: {len(hits)}')
    for x in hits[:4]:
        for u in x['use'][:2]:
            print(f"  [{x['code']}|{x['vis']}] {x['name'][:60]} :: {u['t']} :: {t(u['c'])[:420]}")
