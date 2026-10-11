import json, csv, io, re
def load():
    d = json.load(open('/home/claude/work/export_texty.json'))
    rows = []
    for man, t in d.items():
        r = list(csv.reader(io.StringIO(t), delimiter=';'))
        h = r[0]
        for x in r[1:]:
            if not x or not x[0]: continue
            o = dict(zip(h, x)); o['man'] = {'31':'LR','35':'Eurona','41':'Essens'}[man]
            rows.append(o)
    return rows
