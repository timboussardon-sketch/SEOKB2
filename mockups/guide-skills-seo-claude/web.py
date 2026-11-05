"""Version web du guide. Même source que le PDF : texte.txt / texte.en.txt.
Aucun mot du guide n'est écrit ici : le texte vient de ces fichiers, seuls les libellés d'interface sont déclarés."""
import html, json, pathlib, re, sys

LANG = sys.argv[1] if len(sys.argv) > 1 else 'fr'
FR = LANG == 'fr'
DEPLOY = len(sys.argv) > 2 and sys.argv[2] == 'deploy'
SITE = 'https://organikk.co/guides/skills-seo-claude/'
PRE = '../' if DEPLOY and not FR else ''
SRC, OUT, OTHER = {'fr': ('texte.txt', 'index.html', ('index.en.html', 'EN')),
                   'en': ('texte.en.txt', 'index.en.html', ('index.html', 'FR'))}[LANG]
T = {
    'fr': dict(toc='Sommaire', copied='Copié', copyc='Copier', copy='Copier', left='min restantes', resume='Reprendre la lecture',
               close='Fermer', menu='Ouvrir le sommaire', start='Début', show='Afficher le skill complet', hide='Replier le skill',
               lines='lignes', count='skills copiés', next='Aller au prochain skill à copier', read='Lecture', tools='Skills',
               mode='Affichage', dl='.md', dlall='Tout télécharger (.zip)', sections='Sections du skill', zipname='skills-seo.zip', mw_t='Ton email, et le fichier est à toi.', mw_s='On déteste les SPAMS, donc on ne le fera jamais !', mw_algo='(Tu recevras aussi Algorithme, la newsletter SEO lue par 5 000+ lecteurs.)', mw_ph='ton@email.fr', mw_aria='Ton adresse email', mw_back='Revenir au skill', mw_copy='Copier le skill', mw_dl='Télécharger'),
    'en': dict(toc='Contents', copied='Copied', copyc='Copy', copy='Copy', left='min left', resume='Resume reading',
               close='Close', menu='Open the contents', start='Start', show='Show the full skill', hide='Collapse the skill',
               lines='lines', count='skills copied', next='Go to the next skill to copy', read='Reading', tools='Skills',
               mode='View', dl='.md', dlall='Download all (.zip)', sections='Skill sections', zipname='seo-skills.zip', mw_t='Your email, and the file is yours.', mw_s='We hate spam, so we will never send any!', mw_algo='(You will also receive Algorithme, the French SEO newsletter read by 5,000+ readers.)', mw_ph='you@email.com', mw_aria='Your email address', mw_back='Back to the skill', mw_copy='Copy the skill', mw_dl='Download'),
}[LANG]

MARK = '<svg class="mark" viewBox="0 0 96 96" aria-hidden="true"><path d="M0.0 92.84C40.85 54.96 57.38 54.05 96.0 57.49L53.09 91.05Q47.05 96.0 38.78 96.0L3.81 96.0A3.81 3.3 0 0 1 0.0 92.84Z" fill="currentColor"/><path d="M0.0 36.86C0.0 15.68 45.14 0.0 46.73 0.0L49.91 0.0A1.91 1.65 0 0 1 51.81 1.65L51.81 50.06C53.25 62.39 32.2 59.09 0.0 91.87Z" fill="currentColor"/></svg>'
SVG = lambda cls, d: f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{d}</svg>'
I_COPY = SVG('i-copy', '<rect x="9" y="9" width="11" height="11" rx="2.5"/><path d="M15 9V6.5A2.5 2.5 0 0 0 12.5 4h-6A2.5 2.5 0 0 0 4 6.5v6A2.5 2.5 0 0 0 6.5 15H9"/>')
I_OK = SVG('i-ok', '<path d="M5 12.5l4.5 4.5L19 7.5"/>')
I_DL = SVG('i', '<path d="M12 4v11"/><path d="M7.5 11l4.5 4.5 4.5-4.5"/><path d="M5 20h14"/>')
I_ARROW = SVG('i', '<path d="M5 12h14"/><path d="M13 6l6 6-6 6"/>')
I_MENU = SVG('i', '<path d="M4 7h16"/><path d="M4 12h16"/><path d="M4 17h10"/>')
I_X = SVG('i', '<path d="M6 6l12 12"/><path d="M18 6L6 18"/>')
COPYB = lambda cls, lbl: f'<button class="btn {cls}" type="button" data-copy="{lbl}" data-copied="{T["copied"]}"><span class="ic">{I_COPY}{I_OK}</span><span class="lbl">{lbl}</span></button>'
COPYBTN = f'<button class="btn copyc" type="button" data-copy="{T["copyc"]}" data-copied="{T["copied"]}"><span class="ic">{I_COPY}{I_OK}</span><span class="lbl">{T["copyc"]}</span></button>'

EXTRA_CSS = """
article h3{scroll-margin-top:90px}
article h3 .slug{display:block;font-family:"Geist Mono",monospace;font-size:13px;font-weight:500;letter-spacing:0;color:var(--ink-2);margin-top:6px}
.try.solo{margin:8px 0 24px}
.lnk{margin:6px 0;font-size:15px}
.lnk a{color:var(--c-top);text-decoration:none;border-bottom:1px solid var(--tint)}
.lnk a:hover{border-bottom-color:var(--c-top)}
.mailbox{width:min(440px,calc(100vw - 32px));max-width:none;padding:36px 28px 22px;border:0;border-radius:24px;background:#fff;color:var(--ink);box-shadow:0 30px 80px rgba(20,30,110,.28)}
.mailbox::backdrop{background:rgba(16,20,48,.45);backdrop-filter:blur(4px)}
.mailbox[open]{animation:mw-in .28s var(--ease) both}
@keyframes mw-in{from{opacity:0;transform:translateY(10px) scale(.98)}}
.mw-in{display:flex;flex-direction:column;align-items:center;text-align:center}
.mw-mark{width:48px;height:48px;color:var(--c-top);margin-bottom:18px}
.mw-t{font-size:22px;font-weight:600;letter-spacing:-.02em;margin:0}
.mw-s{margin:10px 0 0;font-size:14px;line-height:1.55;color:var(--ink-2)}
.mw-algo{margin:4px 0 0;font-size:12px;line-height:1.4;color:var(--ink-2)}
.mw-pot{position:absolute;left:-9999px;width:1px;height:1px;overflow:hidden}
.mw-field{display:flex;flex-wrap:wrap;gap:8px;width:100%;margin-top:22px}
.mw-mail{flex:1 1 200px;min-width:0;height:48px;padding:0 14px;border:1px solid var(--tint);border-radius:12px;font:inherit;font-size:16px;color:var(--ink);background:#fff;outline:none}
.mw-mail:focus{border-color:var(--c-top);box-shadow:0 0 0 3px rgba(47,79,224,.15)}
.mailbox.bad .mw-mail{border-color:#d33;animation:mw-non .3s}
@keyframes mw-non{25%{transform:translateX(-5px)}75%{transform:translateX(5px)}}
.mw-go{flex:1 1 auto;display:inline-flex;align-items:center;justify-content:center;gap:8px;height:48px;padding:0 18px;border:0;border-radius:12px;background:var(--c-top);color:#fff;font:inherit;font-size:15px;font-weight:600;cursor:pointer}
.mw-go:hover{filter:brightness(1.07)}
.mw-go svg{width:17px;height:17px}
.mw-back{margin-top:14px;padding:6px 10px;border:0;border-radius:8px;background:none;color:var(--ink-2);font:inherit;font-size:13px;cursor:pointer}
.mw-back:hover{color:var(--ink)}
.shot{margin:28px 0 32px}
.shot img{display:block;width:100%;height:auto;border-radius:20px}
article p.b{font-weight:600;margin:32px 0 6px}
.toc ol ol,.sheet ol ol{margin:4px 0 8px;padding-left:12px}
.toc ol ol a,.sheet ol ol a{font-size:13px;padding-top:3px;padding-bottom:3px}
"""

here = pathlib.Path(__file__).parent
e = lambda s: html.escape(s, quote=False)
ea = lambda s: html.escape(s, quote=True)
lines = (here / SRC).read_text().split('\n')
if DEPLOY:
    OUT = 'deploy/index.html' if FR else 'deploy/en/index.html'
    OTHER = ('en/', 'EN') if FR else ('../', 'FR')

TOKEN = re.compile(r'(\[[^\]]*\])')


def consigne_html(text, key):
    out, k = [], 0
    for j, part in enumerate(TOKEN.split(text)):
        if j % 2 == 0:
            out.append(e(part))
            continue
        label = part[1:-1]
        out.append(f'<input class="fill" type="text" data-ph="{ea(part)}" data-k="{key}-{k}" placeholder="{ea(label)}" aria-label="{ea(label)}" size="{max(len(label), 4)}" autocomplete="off" autocapitalize="off" spellcheck="false">')
        k += 1
    return ''.join(out)


def hl(line, sid, heads):
    esc = e(line)
    if line.startswith('## '):
        hid = f'{sid}h{len(heads)}'
        heads.append((hid, re.sub(r'^## (\d+\. )?', '', line)))
        return f'<span class="h" id="{hid}">{esc}</span>'
    if line.startswith('# '): return f'<span class="h">{esc}</span>'
    if line.startswith('> '): return f'<span class="q">{esc}</span>'
    if line.startswith('|'): return f'<span class="t">{esc}</span>'
    esc = re.sub(r'^(name|description):', r'<span class="k">\1:</span>', esc)
    esc = re.sub(r'^(- |\d+\. )', r'<span class="m">\1</span>', esc)
    return re.sub(r'`[^`]+`', lambda m: f'<span class="c">{m.group(0)}</span>', esc)


def skill_html(text, n):
    sid = f'skill{n}'
    m = re.search(r'^name: (\S+)', text, re.M)
    name = m.group(1) if m else sid
    heads = []
    pre = '\n'.join(hl(l, sid, heads) for l in text.split('\n'))
    chips = ''.join(f'<button class="chipb" type="button" data-t="{hid}">{e(x)}</button>' for hid, x in heads)
    chips = f'<div class="chips" aria-label="{T["sections"]}">{chips}</div>' if heads else ''
    return (f'<section class="skillbox" id="{sid}" data-name="{ea(name)}"><div class="sbar"><span class="sname">{e(name)}</span><span class="smeta">{text.count(chr(10)) + 1} {T["lines"]}</span>'
            f'<button class="btn dl" type="button" aria-label="{T["dl"]} {ea(name)}">{I_DL}<span>{T["dl"]}</span></button>{COPYB("copy", T["copy"])}</div>'
            f'{chips}<div class="swrap"><pre id="{sid}pre">{pre}</pre></div>'
            f'<button class="more" type="button" aria-expanded="false" aria-controls="{sid}pre" data-show="{T["show"]}" data-hide="{T["hide"]}">{T["show"]}</button></section>')


cover, by, body, toc, final = {}, [], [], [], ''
ul_open, n_sec, n_q, n_skill, in_skill, skill = False, 0, 0, 0, False, []


def close_ul():
    global ul_open
    if ul_open:
        body.append('</ul>')
        ul_open = False


for raw in lines:
    if in_skill:
        if raw == '@@end':
            n_skill += 1
            body.append(skill_html('\n'.join(skill), n_skill))
            in_skill, skill = False, []
        else:
            skill.append(raw)
        continue
    if not raw.strip():
        continue
    m = re.match(r'@@(\S+) ?(.*)', raw)
    tag, txt = (m.group(1), m.group(2)) if m else ('p', raw)
    t = e(txt)
    if tag != 'li':
        close_ul()
    if tag == 'h1': cover['h1'] = t
    elif tag == 'sub': cover['sub'] = t
    elif tag == 'by': by.append(t)
    elif tag == 'open': pass
    elif tag == 'h2':
        n_sec += 1
        toc.append((f's{n_sec}', t, []))
        body.append(f'<h2 id="s{n_sec}" class="reveal">{t}</h2>')
    elif tag == 'h3':
        name, _, slug = txt.partition(' · ')
        sid = slug or re.sub(r'\W+', '-', name.lower())
        if toc: toc[-1][2].append((sid, e(name)))
        body.append(f'<h3 id="{ea(sid)}">{e(name)}<span class="slug">{e(slug)}</span></h3>')
    elif tag == 'h4': body.append(f'<h4 class="dir">{t}</h4>')
    elif tag == 'k': body.append(f'<h4>{t}</h4>')
    elif tag == 'image':
        path, _, pct = txt.partition(' ')
        body.append(f'<figure class="shot"><img src="{PRE}{path}" alt="" loading="lazy"></figure>')
    elif tag == 'b': body.append(f'<p class="b">{t}</p>')
    elif tag == 'skill': in_skill = True
    elif tag == 'q':
        n_q += 1
        body.append(f'<div class="try solo"><div class="crow"><p class="cons">{consigne_html(txt, f"q{n_q}")}</p>{COPYBTN}</div></div>')
    elif tag == 'a':
        lab, _, url = txt.partition(' | ')
        body.append(f'<p class="lnk">{e(lab)} : <a href="{ea(url)}">{e(url.replace("https://", ""))}</a></p>')
    elif tag == 'final':
        m2 = re.match(r'(.*?:) (https\S+)', txt)
        final = f'<h2>{e(m2.group(1))}</h2><a class="cta" href="{ea(m2.group(2))}"><span>{e(m2.group(2).replace("https://", "").rstrip("/"))}</span>{I_ARROW}</a>'
    elif tag == 'li':
        if not ul_open:
            body.append('<ul>')
            ul_open = True
        body.append(f'<li>{t}</li>')
    else:
        body.append(f'<p>{t}</p>')
close_ul()

toc_html = ''.join(f'<li><a href="#{i}">{t}</a>' + (('<ol>' + ''.join(f'<li><a href="#{ea(a)}">{b}</a></li>' for a, b in kids) + '</ol>') if kids else '') + '</li>' for i, t, kids in toc)
desc = html.unescape(cover['h1']) + ' ' + next(l[6:] for l in lines if l.startswith('@@sub '))
OG = 'og.png' if FR else 'og.en.png'
CSS = (here / 'web.css').read_text().replace('url(geist', f'url({PRE}geist') + EXTRA_CSS
JS = (here / 'web.js').read_text()
URL = SITE if FR else SITE + 'en/'
HEAD_DEPLOY = ('<meta name="robots" content="noindex, nofollow, noarchive">\n'
               '<link rel="icon" href="/icon.svg" type="image/svg+xml">') if DEPLOY else ''
doc = f"""<!DOCTYPE html>
<html lang="{LANG}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{cover['h1']}</title>
<meta name="description" content="{ea(desc)}">
<meta property="og:type" content="article">
<meta property="og:title" content="{ea(html.unescape(cover['h1']))}">
<meta property="og:description" content="{ea(desc)}">
{HEAD_DEPLOY}
<script>document.documentElement.className='js'</script>
<style>{CSS}</style>
</head>
<body data-lang="{LANG}">
<header class="hero panel">
  <div class="in">
    {MARK}
    <h1>{cover['h1']}</h1>
    <p class="sub">{cover['sub']}</p>
    <p class="by">{by[0]}</p>
  </div>
</header>
<div class="topbar">
  <div class="in">
    <button class="where" type="button" aria-label="{T['menu']}">{I_MENU}<span class="cur">{T['start']}</span></button>
    <span class="time" aria-live="off"><b>0</b> {T['left']}</span>
    <div class="seg2" role="group" aria-label="{T['mode']}"><button type="button" data-mode="read" aria-pressed="true">{T['read']}</button><button type="button" data-mode="tools" aria-pressed="false">{T['tools']}</button></div>
    <a class="lang" href="{OTHER[0]}" hreflang="{OTHER[1].lower()}">{OTHER[1]}</a>
  </div>
  <div class="progress" aria-hidden="true"><i></i></div>
</div>
<div class="wrap">
  <nav class="toc" aria-label="{T['toc']}"><p>{T['toc']}</p><ol>{toc_html}</ol></nav>
  <article>
<div class="toolhead"><button class="btn dlall" type="button">{I_DL}<span>{T['dlall']}</span></button></div>
{chr(10).join(body)}
  </article>
</div>
<footer class="end panel"><div class="in">{final}{MARK}</div></footer>
<button class="pill" type="button" aria-label="{T['next']}"><b></b> {T['count']}</button>
<div class="resume" hidden><button class="go" type="button"><span class="rl">{T['resume']}</span><span class="rs"></span></button><button class="rx" type="button" aria-label="{T['close']}">{I_X}</button></div>
<dialog class="mailbox" aria-label="{T['mw_aria']}"><form class="mw-in" novalidate>{MARK.replace('class="mark"', 'class="mw-mark"')}<h3 class="mw-t">{T['mw_t']}</h3><p class="mw-s">{T['mw_s']}</p><p class="mw-algo">{T['mw_algo']}</p><span class="mw-pot" aria-hidden="true"><input type="text" name="site" tabindex="-1" autocomplete="off"></span><span class="mw-field"><input class="mw-mail" type="email" placeholder="{T['mw_ph']}" autocomplete="email" spellcheck="false" aria-label="{T['mw_aria']}"><button class="mw-go" type="submit"><span class="mw-lab">{T['mw_copy']}</span>{I_ARROW}</button></span><button class="mw-back" type="button">{T['mw_back']}</button></form></dialog>
<dialog class="sheet" aria-label="{T['toc']}"><div class="sh"><p>{T['toc']}</p><button class="sx" type="button" aria-label="{T['close']}">{I_X}</button></div><ol>{toc_html}</ol></dialog>
<script>window.GUIDE={json.dumps({'zip': T['zipname'], 'mw': {'copy': T['mw_copy'], 'dl': T['mw_dl']}}, ensure_ascii=False)}</script>
<script>{JS}</script>
</body>
</html>
"""
(here / OUT).parent.mkdir(parents=True, exist_ok=True)
(here / OUT).write_text(doc)
print(OUT, len(doc) // 1024, 'Ko', '·', len(toc), 'sections ·', n_skill, 'skills')
