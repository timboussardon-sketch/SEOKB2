"""texte.txt (texte de Tim, verbatim, une balise @@ par ligne) -> HTML autoportant.
Aucun mot n'est écrit ici : tout le contenu vient de texte.txt."""
import base64, html, pathlib, re, sys

LANG = sys.argv[1] if len(sys.argv) > 1 else 'fr'
SRC, OUT = {'fr': ('texte.txt', 'skills-seo-claude.html'), 'en': ('texte.en.txt', 'seo-skills-claude.html')}[LANG]

MARK = '<svg class="mark" viewBox="0 0 96 96" aria-hidden="true"><path d="M0.0 92.84C40.85 54.96 57.38 54.05 96.0 57.49L53.09 91.05Q47.05 96.0 38.78 96.0L3.81 96.0A3.81 3.3 0 0 1 0.0 92.84Z" fill="#ffffff"/><path d="M0.0 36.86C0.0 15.68 45.14 0.0 46.73 0.0L49.91 0.0A1.91 1.65 0 0 1 51.81 1.65L51.81 50.06C53.25 62.39 32.2 59.09 0.0 91.87Z" fill="#ffffff"/></svg>'

COPY = '<button class="copy" type="button" aria-label="Copier le skill"><svg class="i-copy" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="11" height="11" rx="2.5"/><path d="M15 9V6.5A2.5 2.5 0 0 0 12.500 4h-6A2.500 2.500 0 0 0 4 6.500v6A2.500 2.500 0 0 0 6.500 15H9"/></svg><svg class="i-ok" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.500l4.500 4.500L19 7.500"/></svg></button>'

COPY_JS = """<script>
document.querySelectorAll('.copy').forEach(function(b){
  b.addEventListener('click',function(){
    var t=b.nextElementSibling.textContent;
    var done=function(){b.classList.add('ok');setTimeout(function(){b.classList.remove('ok')},1500)};
    if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(t).then(done)}
    else{var a=document.createElement('textarea');a.value=t;document.body.appendChild(a);a.select();document.execCommand('copy');a.remove();done()}
  });
});
</script>"""

EXTRA_CSS = """
.cover h1{font-size:31pt;max-width:160mm}
h2.grad{font-size:24pt;line-height:1.08;letter-spacing:-.025em;font-weight:600;margin:0 0 8mm;max-width:160mm;break-after:avoid}
h2.arg{font-size:19pt;margin:14mm 0 0}
h3.sub3{color:var(--c-top)}
h4.dir{font-family:"Geist Mono",monospace;font-size:11pt;font-weight:600;color:var(--c-top);margin:8mm 0 3mm;break-after:avoid}
p.lab{font-family:"Geist Mono",monospace;font-size:7.5pt;letter-spacing:.22em;text-transform:uppercase;color:var(--c-top);margin:9mm 0 3mm;break-after:avoid}
p.b{font-weight:600;margin:7mm 0 2mm;break-after:avoid}
.imgslot{border:.8pt dashed #b9c8ff;border-radius:3mm;background:var(--wash);color:var(--ink-2);font-family:"Geist Mono",monospace;font-size:8pt;letter-spacing:.2em;text-transform:uppercase;text-align:center;padding:22mm 0;margin:6mm 0;break-inside:avoid}
.shot{margin:7mm 0;break-inside:avoid}
p:has(+ .shot){break-after:avoid}
h2 + .shot{margin-top:9mm}
.shot img{display:block;width:100%;height:auto;border:.5pt solid var(--tint);border-radius:3mm}
.skill{margin:3mm 0 0;position:relative}
.skill pre{padding-right:17mm}
.cons{position:relative}
.cons pre{padding-right:17mm}
.copy{position:absolute;top:3.5mm;right:3.5mm;width:8mm;height:8mm;padding:0;display:flex;align-items:center;justify-content:center;border:.5pt solid var(--tint);border-radius:2mm;background:#fff;color:var(--c-top);cursor:pointer}
.copy svg{width:4.2mm;height:4.2mm}
.copy .i-ok{display:none}
.copy.ok{background:var(--c-top);border-color:var(--c-top);color:#fff}
.copy.ok .i-copy{display:none}
.copy.ok .i-ok{display:block}
.skill pre{font-size:7.6pt;line-height:1.6;white-space:pre-wrap;overflow-wrap:anywhere;break-inside:auto}
.final h2{max-width:150mm}
.cons{margin:2mm 0 4mm;break-inside:avoid}
.cons pre{padding:3.5mm 17mm 3.5mm 5mm;font-size:8.6pt;line-height:1.5;white-space:pre-wrap;overflow-wrap:anywhere;margin:0}
p.lnk{font-size:9pt;margin:1.5mm 0;break-before:avoid}
ul:has(+ p.lnk),p:has(+ p.lnk),p.lab + p{break-after:avoid}
p.lnk a{color:var(--c-top);text-decoration:none;border-bottom:.5pt solid var(--tint)}
h3.sub3{font-size:19pt;margin-top:10mm;break-after:avoid}
.part > h3.sub3:first-child{margin-top:0}
.final .url{color:#fff;border-bottom:.5pt solid rgba(255,255,255,.6);font-size:13pt}
"""

here = pathlib.Path(__file__).parent
if LANG == 'en':
    COPY = COPY.replace('Copier le skill', 'Copy the skill')
lines = (here / SRC).read_text().split('\n')
e = html.escape

cover, by, body, final = {}, [], [], ''
ul_open = False
in_skill, skill = False, []
section_open = False
h3_seen = False

def close_ul():
    global ul_open
    if ul_open:
        body.append('</ul>')
        ul_open = False

def open_section(cls=''):
    global section_open
    close_ul()
    if section_open:
        body.append('</section>')
    body.append(f'<section{cls}>')
    section_open = True

for raw in lines:
    if in_skill:
        if raw == '@@end':
            body.append('<div class="skill">' + COPY + '<pre>' + e('\n'.join(skill), quote=False) + '</pre></div>')
            in_skill, skill = False, []
        else:
            skill.append(raw)
        continue
    if not raw.strip():
        continue
    m = re.match(r'@@(\S+) ?(.*)', raw)
    tag, txt = (m.group(1), m.group(2)) if m else ('p', raw)
    t = e(txt, quote=False)
    if tag != 'li':
        close_ul()
    if tag == 'h1': cover['h1'] = t
    elif tag == 'sub': cover['sub'] = t
    elif tag == 'by': by.append(t)
    elif tag == 'open': open_section()
    elif tag == 'h2': h3_seen = False; open_section(' class="part"'); body.append(f'<h2 class="grad">{t}</h2>')
    elif tag == 'h2n': body.append(f'<h2 class="grad arg">{t}</h2>')
    elif tag == 'h3':
        if h3_seen: open_section(' class="part"')
        h3_seen = True
        body.append(f'<h3 class="sub3">{t}</h3>')
    elif tag == 'h4': body.append(f'<h4 class="dir">{t}</h4>')
    elif tag == 'k': body.append(f'<p class="lab">{t}</p>')
    elif tag == 'b': body.append(f'<p class="b">{t}</p>')
    elif tag == 'img': body.append(f'<div class="imgslot">{t}</div>')
    elif tag == 'image':
        path, _, pct = txt.partition(' ')
        data = base64.b64encode((here / path).read_bytes()).decode()
        style = f' style="width:{pct}%;margin-left:auto;margin-right:auto"' if pct else ''
        body.append(f'<figure class="shot"{style}><img src="data:image/png;base64,{data}" alt=""></figure>')
    elif tag == 'skill': in_skill = True
    elif tag == 'q': body.append('<div class="cons">' + COPY + '<pre>' + t + '</pre></div>')
    elif tag == 'a':
        lab, _, url = txt.partition(' | ')
        body.append(f'<p class="lnk">{e(lab)} : <a href="{e(url)}">{e(url.replace("https://", ""))}</a></p>')
    elif tag == 'final':
        m2 = re.match(r'(.*?:) (https\S+)', txt)
        label, url = m2.group(1), m2.group(2)
        final = f'<h2>{e(label)}</h2><p><a class="url" href="{e(url)}">{e(url)}</a></p>'
    elif tag == 'li':
        if not ul_open:
            body.append('<ul>')
            ul_open = True
        body.append(f'<li>{t}</li>')
    else:
        body.append(f'<p>{t}</p>')
close_ul()
body.append('</section>')

head = (here / 'head.html').read_text()
head = head.replace('<html lang="fr">', f'<html lang="{LANG}">')
head = re.sub(r'<title>.*?</title>', f"<title>{cover['h1']}</title>", head)
head = head.replace('</style>', EXTRA_CSS + '</style>', 1)
for tok, f in (('__FONT_GEIST__', 'geist.woff2'), ('__FONT_MONO__', 'geist-mono.woff2')):
    head = head.replace(tok, 'data:font/woff2;base64,' + base64.b64encode((here / f).read_bytes()).decode())

doc = f"""{head}
<body>
<div class="cover panel">
  {MARK}
  <div>
    <h1>{cover['h1']}</h1>
    <p class="sub">{cover['sub']}</p>
  </div>
  <div class="foot"><span>{by[0]}</span><span></span></div>
</div>
{chr(10).join(body)}
<section class="final panel">
  <div>{final}</div>
  <div class="foot">{MARK}<span></span></div>
</section>
{COPY_JS}
</body>
</html>
"""
out = here / OUT
out.write_text(doc)
print(out.name, len(doc) // 1024, 'Ko')
