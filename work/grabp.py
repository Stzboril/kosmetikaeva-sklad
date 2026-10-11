import sys, re, glob, os, base64, gzip, json
parts = {}
for f in glob.glob('/root/.claude/projects/*/*/tool-results/*'):
    d = open(f, encoding='utf-8', errors='ignore').read()
    for m in re.finditer(r'GZP(\d+):([A-Za-z0-9+/=]+):ENDP', d):
        parts[int(m.group(1))] = (os.path.getmtime(f), m.group(2))
n = int(sys.argv[2])
b = ''.join(parts[i][1] for i in range(1, n + 1))
raw = gzip.decompress(base64.b64decode(b))
open(sys.argv[1], 'wb').write(raw)
print(len(raw))
