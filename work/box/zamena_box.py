import html, re
ICON = ('<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#c9361f" '
        'stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
        '<rect x="10" y="2" width="4" height="3" rx="0.5"/><path d="M9.5 5h5v3h-5z"/><rect x="5" y="8" width="14" height="13" rx="3.5"/>'
        '<path d="M8.5 14.5c1.2-1.4 2.4-1.4 3.5 0s2.3 1.4 3.5 0"/></svg>')
LABEL = {'cs': 'Naši zákazníci tuto vůni nejčastěji zaměňují za:', 'sk': 'Naši zákazníci si túto vôňu najčastejšie zamieňajú s:'}
def box(name, lang):
    n = html.escape(name, quote=False)
    return ('<div class="zamena-vune" style="display:flex;align-items:center;gap:14px;background:#fff;border-left:4px solid #c9361f;'
            'border-radius:10px;box-shadow:0 2.5px 10px rgba(0,0,0,.1);padding:14px 18px;margin:14px 0 18px;max-width:640px">'
            '<span style="flex:0 0 44px;width:44px;height:44px;border-radius:50%;background:#fbe9e6;display:flex;align-items:center;justify-content:center">'
            + ICON + '</span><span style="line-height:1.45"><span style="display:block;color:#555">' + LABEL[lang] +
            '</span><strong style="font-size:16px;color:#000">' + n + '</strong></span></div>')
def odstran(desc):
    return re.sub(r'<div class="zamena-vune".*?</strong></span></div>\s*', '', desc or '', flags=re.S)
def insert(desc, name, lang):
    d = odstran(desc)
    b = box(name, lang)
    if re.search(r'</h2>', d): return re.sub(r'</h2>', '</h2>\n' + b, d, count=1)
    return b + '\n' + d
