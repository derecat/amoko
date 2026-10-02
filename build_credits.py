import re, os, html

os.chdir('/var/minis/workspace/amoko/logos')

ITEMS = [
    ('Codex',       'codex.svg'),
    ('Claude Code', 'claude.svg'),
    ('Qwen',        'qwen.svg'),
    ('DeepSeek',    'deepseek.svg'),
    ('Gemini',      'gemini.svg'),
    ('Pi',          'pi.svg'),
]

def normalize(path):
    s = open(path, encoding='utf-8').read()
    vb = re.search(r'viewBox="([^"]+)"', s)
    vb = vb.group(1) if vb else '0 0 24 24'
    ds = re.findall(r'<path[^>]*?\sd="([^"]+)"', s)
    if not ds:
        raise SystemExit('no path in ' + path)
    return vb, ds

rows = []
for label, f in ITEMS:
    vb, ds = normalize(f)
    paths = ''.join('<path d="%s"/>' % d for d in ds)
    rows.append(
        '        <li class="credit">\n'
        '          <span class="credit__glyph" aria-hidden="true">'
        '<svg viewBox="%s">%s</svg></span>\n'
        '          <span class="credit__word">%s</span>\n'
        '        </li>' % (vb, paths, html.escape(label))
    )

snippet = '\n'.join(rows)
open('/tmp/credits_list.html', 'w', encoding='utf-8').write(snippet)
print('%d items, %d bytes' % (len(rows), len(snippet)))
