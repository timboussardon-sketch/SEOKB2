"""Version web du guide « Construis ton propre agent SEO avec Claude ».

Source : guide-final.md (texte final de Tim du 26/10, repris mot pour mot).
Sortie : un dossier statique pour organikk-next/public/guides/<slug>/.
Le corps du guide reste masqué derrière le mur email : POST /api/skill-emails,
la même base que les autres guides du site (filtre à faux comptes côté serveur).

Usage : python3 build_web.py [dossier-de-sortie]
"""
import html, pathlib, re, shutil, sys

ICI = pathlib.Path(__file__).parent
SLUG = 'construire-agent-seo-claude'
URL = f'https://organikk.co/guides/{SLUG}/'
OUT = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else ICI / 'web' / SLUG

MARK = ('<svg class="mark" viewBox="0 0 96 96" aria-hidden="true">'
        '<path d="M0.0 92.84C40.85 54.96 57.38 54.05 96.0 57.49L53.09 91.05Q47.05 96.0 38.78 96.0L3.81 96.0A3.81 3.3 0 0 1 0.0 92.84Z" fill="#fff"/>'
        '<path d="M0.0 36.86C0.0 15.68 45.14 0.0 46.73 0.0L49.91 0.0A1.91 1.65 0 0 1 51.81 1.65L51.81 50.06C53.25 62.39 32.2 59.09 0.0 91.87Z" fill="#fff"/></svg>')


def inline(t):
    """Gras, code et liens d'une ligne markdown. Le code est mis de côté avant le
    gras, puis remis : un gras peut contenir du code (« **… `raw/`.** »)."""
    codes = []
    def garde(m):
        codes.append('<code>' + html.escape(m.group(1)) + '</code>')
        return f'\x00{len(codes) - 1}\x00'
    t = re.sub(r'`([^`]+)`', garde, t)
    t = html.escape(t, quote=False)
    t = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t)
    t = re.sub(r'(https?://[^\s<]+)', r'<a href="\1">\1</a>', t)
    return re.sub(r'\x00(\d+)\x00', lambda m: codes[int(m.group(1))], t)


def blocs(lignes):
    """Découpe le markdown en blocs : (type, contenu)."""
    i, n = 0, len(lignes)
    while i < n:
        l = lignes[i]
        if not l.strip():
            i += 1
            continue
        if l.startswith('```'):
            j = i + 1
            while not lignes[j].startswith('```'):
                j += 1
            yield 'pre', '\n'.join(lignes[i + 1:j])
            i = j + 1
            continue
        m = re.match(r'(#{1,3}) (.*)', l)
        if m:
            yield 'h' + str(len(m.group(1))), m.group(2)
            i += 1
            continue
        if l.strip() == '---':
            yield 'hr', ''
            i += 1
            continue
        if l.startswith('|'):
            j = i
            while j < n and lignes[j].startswith('|'):
                j += 1
            yield 'table', lignes[i:j]
            i = j
            continue
        if l.startswith('> '):
            yield 'quote', l[2:]
            i += 1
            continue
        if re.match(r'(- |\d+\. )', l):
            ordonnee = bool(re.match(r'\d+\. ', l))
            j, items = i, []
            while j < n and re.match(r'(- |\d+\. )', lignes[j]):
                items.append(re.sub(r'^(- |\d+\. )', '', lignes[j]))
                j += 1
            yield ('ol' if ordonnee else 'ul'), items
            i = j
            continue
        yield 'p', l
        i += 1


def rendu(b):
    t, c = b
    if t == 'p':
        if c.startswith('**À la fin de cette phase :**'):
            return f'<div class="bilan"><p>{inline(c)}</p></div>'
        return f'<p>{inline(c)}</p>'
    if t == 'h2':
        return f'<h3>{inline(c)}</h3>'
    if t == 'h3':
        return f'<h4>{inline(c)}</h4>'
    if t == 'hr':
        return '<hr>'
    if t == 'quote':
        return f'<blockquote><p>{inline(c)}</p></blockquote>'
    if t == 'pre':
        return f'<pre><code>{html.escape(c)}</code></pre>'
    if t in ('ul', 'ol'):
        return f'<{t}>' + ''.join(f'<li>{inline(x)}</li>' for x in c) + f'</{t}>'
    if t == 'table':
        cellules = lambda l: [x.strip() for x in l.strip().strip('|').split('|')]
        tete, corps = cellules(c[0]), [cellules(l) for l in c[2:]]
        th = ''.join(f'<th>{inline(x)}</th>' for x in tete)
        tr = ''.join('<tr>' + ''.join(f'<td>{inline(x)}</td>' for x in r) + '</tr>' for r in corps)
        return f'<div class="tw"><table><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></div>'
    raise ValueError(t)


src = (ICI / 'guide-final.md').read_text().splitlines()
tout = list(blocs(src))

# En-tête : titre, sous-titre, signature (les trois premiers blocs du texte de Tim)
assert tout[0][0] == 'h1' and tout[1][0] == 'p' and tout[2][0] == 'p'
titre, sous_titre, signature = tout[0][1], tout[1][1].strip('*'), tout[2][1]
reste = tout[3:]

# Fin : le dernier « --- » ouvre l'appel au rendez-vous, rendu en panneau
k = max(i for i, b in enumerate(reste) if b[0] == 'hr')
corps, fin = reste[:k], reste[k + 1:]

sections, cur = [], None
for b in corps:
    # « ## Introduction » est au même niveau que les « # » qui suivent : il ouvre une section
    if b[0] == 'h1' or (b[0] == 'h2' and cur is None):
        cur = [f'<h2>{inline(b[1])}</h2>']
        sections.append(cur)
    elif b[0] == 'hr':
        continue
    else:
        cur.append(rendu(b))
corps_html = '\n'.join('<section>\n' + '\n'.join(s) + '\n</section>' for s in sections)

assert fin[0][0] == 'h2'
fin_html = [f'<h2>{inline(fin[0][1])}</h2>']
for b in fin[1:]:
    if b[0] == 'p' and b[1].startswith('**Réserver un créneau :**'):
        lien = re.search(r'https?://\S+', b[1]).group(0)
        fin_html.append(f'<a class="cta" href="{lien}">Réserver un créneau<span class="u">{html.escape(lien.split("//")[1])}</span></a>')
    elif b[0] == 'p' and b[1] == 'organikk.co':
        fin_html.append(f'<div class="foot">{MARK}<span>organikk.co</span></div>')
    else:
        fin_html.append(rendu(b))
fin_html = '\n'.join(fin_html)

page = (ICI / 'web-template.html').read_text()
for cle, val in {
    '__TITRE__': html.escape(titre),
    '__SOUS_TITRE__': html.escape(sous_titre),
    '__SIGNATURE__': html.escape(signature),
    '__URL__': URL,
    '__SLUG__': 'guide-' + SLUG,
    '__MARK__': MARK,
    '__CORPS__': corps_html,
    '__FIN__': fin_html,
}.items():
    page = page.replace(cle, val)
assert '__' not in re.sub(r'<pre>.*?</pre>', '', page, flags=re.S), 'jeton non remplacé'

OUT.mkdir(parents=True, exist_ok=True)
(OUT / 'index.html').write_text(page)
for f in ('geist.woff2', 'geist-mono.woff2'):
    shutil.copy(ICI / f, OUT / f)
print(OUT / 'index.html', len(page) // 1024, 'Ko,', len(sections), 'sections')
