import sys, re, json, base64, gzip, glob, os
# usage: grab.py OUTFILE [nth_from_end]
out = sys.argv[1]; nth = int(sys.argv[2]) if len(sys.argv) > 2 else 1
blobs = []
files = glob.glob('/root/.claude/projects/*/*.jsonl') + glob.glob('/root/.claude/projects/*/*/tool-results/*')
files.sort(key=os.path.getmtime)
for f in files:
    try: data = open(f, encoding='utf-8', errors='ignore').read()
    except Exception: continue
    for m in re.finditer(r'GZ:([A-Za-z0-9+/=]+):END', data):
        blobs.append((os.path.getmtime(f), m.group(1)))
# dedupe preserving order
seen = []; 
for t, b in blobs:
    if b not in seen: seen.append(b)
b = seen[-nth]
raw = gzip.decompress(base64.b64decode(b))
open(out, 'wb').write(raw)
print(out, len(raw), 'bytes; blobs found:', len(seen))
