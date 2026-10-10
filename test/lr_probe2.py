import re
from curl_cffi import requests as cr
out=[]
urls=["https://www.lr-czech.com/parfemy-damske","https://shop.lrworld.com/","https://shop.lrworld.com/cz/cs","https://shop.lrworld.com/home/cz/cs","https://www.lrworld.com/","https://www.lr-czech.com/robots.txt"]
for imp in ("chrome","safari","firefox"):
    for u in urls[:1]+urls[-1:]:
        try:
            r=cr.get(u,impersonate=imp,timeout=30)
            out.append(f"{imp} {u} {r.status_code} len={len(r.text)} title={re.search(r'<title>(.*?)</title>',r.text,re.S).group(1)[:60] if '<title>' in r.text else ''}")
        except Exception as e: out.append(f"{imp} {u} ERR {e!r}"[:200])
for u in urls[1:5]:
    try:
        r=cr.get(u,impersonate="chrome",timeout=30, allow_redirects=True)
        t=r.text
        out.append(f"chrome {u} -> {r.url} {r.status_code} len={len(t)} title={re.search(r'<title>(.*?)</title>',t,re.S).group(1).strip()[:80] if '<title>' in t else ''} skladem={len(re.findall('(?i)skladem|in stock|out of stock|availability',t))}")
        out.append("   "+re.sub(r'\s+',' ',t[:400]))
    except Exception as e: out.append(f"chrome {u} ERR {e!r}"[:200])
open("test/lr_vysledek2.txt","w").write("\n".join(out)+"\n"); print("\n".join(out))
