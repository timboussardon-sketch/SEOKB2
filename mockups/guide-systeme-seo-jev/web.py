"""Version web interactive du guide. Même source que le PDF : texte.txt / texte.en.txt.
Le texte courant vient de ces fichiers. Les blocs propres au web (scoring, schémas, arborescence,
relevé Jev) reprennent les images de Tim ou des relevés de sa base ; ils sont déclarés ici."""
import html, json, pathlib, re, sys

LANG = sys.argv[1] if len(sys.argv) > 1 else 'fr'
FR = LANG == 'fr'
DEPLOY = len(sys.argv) > 2 and sys.argv[2] == 'deploy'
SITE = 'https://organikk.co/guides/systeme-seo-obsidian-jev-claude/'
PRE = '../' if DEPLOY and not FR else ''
SRC, OUT, OTHER = {'fr': ('texte.txt', 'index.html', ('index.en.html', 'EN')),
                   'en': ('texte.en.txt', 'index.en.html', ('index.html', 'FR'))}[LANG]
T = {
    'fr': dict(toc='Sommaire', show='Afficher le skill complet', hide='Replier le skill', copy='Copier', copied='Copié',
               lines='lignes', count='skills copiés', next='Aller au prochain skill à copier', pick='Clique sur un dossier ou un fichier.',
               example='Extrait de ma base', tree='Arborescence de la base', read='Lecture', tools='Skills', mode='Affichage',
               left='min restantes', dl='.md', dlall='Tout télécharger (.zip)', fill='Ta consigne', copyc='Copier la consigne',
               play='Voir la sortie', out='sortie du skill', resume='Reprendre la lecture', close='Fermer', zoom='Agrandir l’image',
               sections='Sections du skill', menu='Ouvrir le sommaire', start='Début',
               score=('Score', 'Barre', '/100', 'Pb', 'Diagnostic'), scorecap='Scoring GEO, par paragraphe',
               jev_cap='verifier.py sur un brouillon de 193 phrases, le 21/09/2026', jev_score='Score', jev_fill='dont remplissage',
               s1='Claude Code · tes notes', s2='Obsidian · tes notes', s1alt='Six outils reliés à Claude Code et à tes notes',
               s2alt='Cinq sources reliées à Obsidian', zipname='skills-seo.zip', q_title='Où en est ton système ?', q_tiers=[[34, 'Tu démarres. Pose d’abord la base : raw/ et wiki/.'], [67, 'La base est posée. Passe aux skills.'], [100, 'Ton système tourne. Il reste {n} à couvrir.'], [101, 'Tout est en place.']], q_pt=['point', 'points'], q_open='Fais le test', q_yes='Oui', q_no='Non', q_back='Question précédente', q_in='en place', q_next='Ta prochaine étape', q_also='À mettre en place ensuite', q_tips='Conseils tirés de ma base', q_again='Refaire le test', q_name='Test : où en est ton système'),
    'en': dict(toc='Contents', show='Show the full skill', hide='Collapse the skill', copy='Copy', copied='Copied',
               lines='lines', count='skills copied', next='Go to the next skill to copy', pick='Click a folder or a file.',
               example='Excerpt from my base (in French)', tree='Base folder tree', read='Reading', tools='Skills', mode='View',
               left='min left', dl='.md', dlall='Download all (.zip)', fill='Your instruction', copyc='Copy the instruction',
               play='See the output', out='skill output', resume='Resume reading', close='Close', zoom='Enlarge the image',
               sections='Skill sections', menu='Open the contents', start='Start',
               score=('Score', 'Bar', '/100', 'Pb', 'Diagnosis'), scorecap='GEO scoring, per paragraph',
               jev_cap='verifier.py on a 193-sentence draft, 2026-09-21', jev_score='Score', jev_fill='of which filler',
               s1='Claude Code · your notes', s2='Obsidian · your notes', s1alt='Six tools connected to Claude Code and your notes',
               s2alt='Five sources connected to Obsidian', zipname='seo-skills.zip', q_title='Where is your system at?', q_tiers=[[34, 'You’re starting. Set up the base first: raw/ and wiki/.'], [67, 'The base is set. Move on to the skills.'], [100, 'Your system runs. {n} left to cover.'], [101, 'Everything is in place.']], q_pt=['point', 'points'], q_open='Take the test', q_yes='Yes', q_no='No', q_back='Previous question', q_in='in place', q_next='Your next step', q_also='To set up after that', q_tips='Advice from my base', q_again='Retake the test', q_name='Test: where is your system at'),
}[LANG]

MARK = '<svg class="mark" viewBox="0 0 96 96" aria-hidden="true"><path d="M0.0 92.84C40.85 54.96 57.38 54.05 96.0 57.49L53.09 91.05Q47.05 96.0 38.78 96.0L3.81 96.0A3.81 3.3 0 0 1 0.0 92.84Z" fill="currentColor"/><path d="M0.0 36.86C0.0 15.68 45.14 0.0 46.73 0.0L49.91 0.0A1.91 1.65 0 0 1 51.81 1.65L51.81 50.06C53.25 62.39 32.2 59.09 0.0 91.87Z" fill="currentColor"/></svg>'
SVG = lambda cls, d: f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{d}</svg>'
I_COPY = SVG('i-copy', '<rect x="9" y="9" width="11" height="11" rx="2.5"/><path d="M15 9V6.5A2.5 2.5 0 0 0 12.5 4h-6A2.5 2.5 0 0 0 4 6.5v6A2.5 2.5 0 0 0 6.5 15H9"/>')
I_OK = SVG('i-ok', '<path d="M5 12.5l4.5 4.5L19 7.5"/>')
I_DL = SVG('i', '<path d="M12 4v11"/><path d="M7.5 11l4.5 4.5 4.5-4.5"/><path d="M5 20h14"/>')
I_PLAY = SVG('i', '<path d="M8 5.5v13l10.500-6.500z"/>')
I_CHEV = SVG('chev', '<path d="M9 6l6 6-6 6"/>')
I_ARROW = SVG('i', '<path d="M5 12h14"/><path d="M13 6l6 6-6 6"/>')
I_MENU = SVG('i', '<path d="M4 7h16"/><path d="M4 12h16"/><path d="M4 17h10"/>')
I_X = SVG('i', '<path d="M6 6l12 12"/><path d="M18 6L6 18"/>')
COPYBTN = lambda cls, lbl: f'<button class="btn {cls}" type="button" data-copy="{lbl}" data-copied="{T["copied"]}"><span class="ic">{I_COPY}{I_OK}</span><span class="lbl">{lbl}</span></button>'

# Tableau de scoring : valeurs lues sur l'image de Tim.
SCORING = [
    ('Surprise', 28, 5, 'Répète le consensus, aucune donnée propriétaire', 'Repeats the consensus, no proprietary data'),
    ('Grounding', 41, 7, '0,7 preuve / 100 mots, seuil à 2', '0.7 proof / 100 words, threshold at 2'),
    ('Content Effort', 34, 3, 'Synthèse générique, aucun test mené', 'Generic synthesis, no test run'),
    ('Alignement RRF' if FR else 'RRF Alignment', 62, 4, 'Prix et intégrations non traités', 'Pricing and integrations not covered'),
    ('RAG Structurer', 52, 4, 'Réponse à 78 mots après le H2 « Comment choisir »', 'Answer 78 words after the H2 "How to choose"'),
    ('Freshness Guard', 15, 2, 'Dernière date citée : 2023', 'Last date cited: 2023'),
    ('Action Engine', 38, 3, "Explique sans permettre d'agir", 'Explains without letting you act'),
]
# Schémas : libellés lus sur les images de Tim.
S1_LEFT, S1_RIGHT = ['Search Console', 'Keyword Planner', 'YouTube'], ['Lighthouse', 'Analytics', 'Trends']
S2 = ['Call client', 'Ticket SAV', 'Stratégie SEO précédente', 'Réflexions', 'Vidéo'] if FR else ['Client call', 'Support ticket', 'Previous SEO strategy', 'Thinking', 'Video']
# Relevé Jev : loops/jev/outputs/verifier-…-2026-09-21.md (totaux seulement, aucune phrase du brouillon).
JEV = [('Appuyées', 'Backed', 71, 'ja'), ('Déduites', 'Deduced', 58, 'jb'), ('Absentes du corpus', 'Absent from the corpus', 58, 'jc'), ('Hors source', 'Outside the sources', 6, 'jd')]
JEV_FILL, JEV_SCORE = 19, 16

# Arborescence : libellés repris de l'image de Tim, extraits repris de sa base (guide « Ma base SEO dans Obsidian »).
TREE = [
    (0, 'AGENTS.md', 'la configuration, lue à chaque session', 'the configuration, read at each session', """## 3. Architecture — 3 couches

raw/    ← sources immuables (lecture seule pour l'agent)
wiki/   ← domaine de l'agent (écriture exclusive)

**Règle d'or** : `raw/` est immuable. L'agent lit, ne modifie jamais.

## 5.4 Citations et sourcing (DOCTRINE)

- **Toute donnée chiffrée a une source** : [[sources/...]]
- **Pas de source = pas d'affirmation**
- Quand une source est vague, marquer `confidence: low`
- Jamais d'invention de chiffres, benchmarks ou pourcentages"""),
    (0, 'raw/', 'tes sources, IMMUABLES', 'your sources, IMMUTABLE', ''),
    (1, 'articles/', 'veille, clippings web', 'monitoring, web clippings', ''),
    (1, 'data/', 'exports Search Console, crawls', 'Search Console exports, crawls', ''),
    (1, 'clients/', 'notes client, briefs reçus', 'client notes, briefs received', ''),
    (1, 'notes/', 'tes notes, tes transcripts de calls', 'your notes, your call transcripts', ''),
    (0, 'wiki/', "le domaine de l'agent", "the agent's domain", ''),
    (1, 'index.md', 'le catalogue de toutes les pages', 'the catalog of all pages', """- [[sources/2026-04-25-organikk-reddit-pour-geo]] — Reddit pour citations IA
  sans ban (ratio 9-1-1, 44 % citations sociales AI Overviews)
- [[sources/2026-05-08-organikk-ranker-chatgpt-2026]] — Ranker dans ChatGPT :
  cite humains+sources, décisionnel d'abord (900M WAU)
- [[sources/2026-05-13-algorithme-process-verifier-indexation]] — Audit
  indexation piloté par skill Claude, 9 points/URL, sans outil payant"""),
    (1, 'log.md', 'le journal, en ajout seul', 'the log, append-only', """## [2026-06-19] ingest | Playbook Reddit (SEO + GEO)
- source_type: doctrine
- source: [[sources/2026-06-19-playbook-reddit-seo-geo]]
- entities touchées: 2 (création [[entities/reddit]], maj [[entities/perplexity]])
- concepts touchés: 1 (création [[concepts/parasite-seo]])
- pages créées: 3 / mises à jour: 2 (perplexity + index)
- contradictions: N
- angle SEO identifié: priorité GEO > parasite SEO > insights ; trou FR
  (pas de communauté SEO FR, pas d'étude de cas FR chiffrée) = cible étude
  first-party"""),
    (1, 'hypotheses.md', 'les convictions pas encore prouvées', 'the convictions not proven yet', """H-001 | Google Search utilise en prod une mémoire type Titans / MIRAS
      | statut : heuristique
      | contre-argument : papier de recherche DeepMind, pas une confirmation
        de prod. Transfert non observable de l'extérieur.

H-004 | Une page « style wiki » est mieux citée en SGE qu'une page statique
      | statut : ouvert
      | contre-argument : à chercher (prochaine revue mensuelle)"""),
    (1, 'sources/', 'une fiche par source ingérée', 'one sheet per ingested source', ''),
    (1, 'entities/', 'les objets nommés : algos, outils, acteurs', 'the named objects: algorithms, tools, players', """wiki/entities/perplexity.md

## Pages liées
… [[sources/2026-04-13-call-04]] · [[sources/2026-06-19-playbook-reddit-seo-geo]]
  · [[concepts/aeo]] · [[concepts/data-proprietaire]] · [[entities/reddit]]
  · [[entities/chatgpt-search]] · [[entities/google-ai-mode]]"""),
    (1, 'concepts/', 'les idées et les mécaniques', 'the ideas and the mechanics', """---
type: concept
title: Wiki persistant vs RAG
aliases: [wiki-vs-rag]
tags: [pattern-kb, rag, meta]
created: 2026-04-11
updated: 2026-08-07
sources: 1
confidence: high
status: stable
---"""),
    (1, 'queries/', 'les questions filées en pages', 'the questions filed as pages', """wiki/queries/2026-04-12-wiki-pattern-vs-grounding-score.md

---
type: query
sources: 8
confidence: medium
status: stable
---

# Le pattern wiki persistant optimise-t-il structurellement le Grounding Score ?

**Réponse courte.** Oui, mais de façon indirecte et non validée empiriquement."""),
]

# Conseils par palier : conseils.json (un tableau par palier, chaque conseil avec sa raison et ses étapes).

# Test de fin : chaque question reprend un point du guide ; la cible est la section ou le skill qui le traite.
QUIZ = [
    ('Tu gardes tes sources brutes (appels clients, exports Search Console, articles) dans un dossier raw/ sur Obsidian ?', 'Do you keep your raw sources (client calls, Search Console exports, articles) in a raw/ folder in Obsidian?', 's3'),
    ('Claude écrit et maintient un wiki/ qui connecte ces sources ?', 'Does Claude write and maintain a wiki/ that connects these sources?', 's3'),
    ('Tu construis un corpus ou une base de données par client pour tes recherches de mots-clés ?', 'Do you build a corpus or a database per client for your keyword research?', 's5'),
    ('Un skill trie tes mots-clés par intention business ?', 'Does a skill sort your keywords by business intent?', 'skill1'),
    ('Un skill prépare ton pré-audit avant un call, depuis la seule URL ?', 'Does a skill prepare your pre-audit before a call, from the URL alone?', 'skill2'),
    ('Le système te propose les liens internes, tu ne les cherches plus à la main ?', 'Does the system suggest internal links, so you no longer look for them by hand?', 'skill3'),
    ('Un skill vérifie que ton JSON-LD correspond à ce que la page affiche ?', 'Does a skill check that your JSON-LD matches what the page displays?', 'skill4'),
    ('Un skill vérifie si tes pages sont indexées ?', 'Does a skill check whether your pages are indexed?', 'skill5'),
    ('Un modèle comme Jev trie et vérifie tes brouillons avant ta relecture ?', 'Does a model like Jev sort and verify your drafts before you review them?', 's8'),
]

here = pathlib.Path(__file__).parent
e = lambda s: html.escape(s, quote=False)
ea = lambda s: html.escape(s, quote=True)
lines = (here / SRC).read_text().split('\n')
if DEPLOY:
    OUT = 'deploy/index.html' if FR else 'deploy/en/index.html'
    OTHER = ('en/', 'EN') if FR else ('../', 'FR')


def scoring_html():
    h = T['score']
    rows = ''.join(
        f'<tr style="--i:{i}"><th scope="row">{e(n)}</th><td class="bar"><span class="track"><span class="fillbar" style="--v:{v / 100}"></span></span></td>'
        f'<td class="num" data-v="{v}">{v}</td><td class="pb">{pb}</td><td class="diag">{e(fr if FR else en)}</td></tr>'
        for i, (n, v, pb, fr, en) in enumerate(SCORING))
    return (f'<div class="scoring reveal"><table><caption>{T["scorecap"]}</caption><thead><tr><th scope="col">{h[0]}</th><th scope="col" class="bar">{h[1]}</th>'
            f'<th scope="col" class="num">{h[2]}</th><th scope="col" class="pb">{h[3]}</th><th scope="col" class="diag">{h[4]}</th></tr></thead><tbody>{rows}</tbody></table></div>')


DEFS = '<defs><linearGradient id="g{n}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#2f4fe0"/><stop offset=".45" stop-color="#2f4fe0"/><stop offset="1" stop-color="#7fa0ff"/></linearGradient></defs>'
STAR = ''.join(f'<line x1="0" y1="-5" x2="0" y2="-17" transform="rotate({a})"/>' for a in range(0, 360, 30))
GEM = '<path d="M-3 -19 L9 -11 L14 6 L5 19 L-9 16 L-14 2 Z" fill="#fff"/><path d="M-3 -19 L1 -2 L14 6 M1 -2 L-9 16 M1 -2 L-14 2" stroke="#b9c8ff" stroke-width="1.2" fill="none"/>'


def wire(d, i):
    return f'<path class="wire" pathLength="1" d="{d}" style="--i:{i}"/><path class="spark" pathLength="1" d="{d}" style="--i:{i}"/>'


def schema1():
    ys, tgt = [40, 160, 280], [148, 160, 172]
    w = ''.join(wire(f'M225 {y} C270 {y},262 {t},295 {t}', i) for i, (y, t) in enumerate(zip(ys, tgt)))
    w += ''.join(wire(f'M535 {y} C490 {y},498 {t},465 {t}', i + 3) for i, (y, t) in enumerate(zip(ys, tgt)))
    lab = ''.join(f'<text x="215" y="{y + 6}" text-anchor="end">{e(n)}</text>' for n, y in zip(S1_LEFT, ys))
    lab += ''.join(f'<text x="545" y="{y + 6}">{e(n)}</text>' for n, y in zip(S1_RIGHT, ys))
    return (f'<figure class="schema reveal"><svg viewBox="0 0 760 320" role="img" aria-label="{T["s1alt"]}">{DEFS.format(n=1)}{w}'
            f'<rect class="core" x="295" y="114" width="170" height="92" rx="26" fill="url(#g1)"/>'
            f'<g transform="translate(338 160)" stroke="#fff" stroke-width="3.2" stroke-linecap="round">{STAR}</g>'
            f'<line x1="380" y1="134" x2="380" y2="186" stroke="rgba(255,255,255,.35)"/><g transform="translate(422 160)">{GEM}</g>'
            f'<text class="cap" x="380" y="238" text-anchor="middle">{T["s1"]}</text>{lab}</svg></figure>')


def schema2():
    ys = [15 + 72 * i for i in range(5)]
    tgt = [165, 175, 185, 195, 205]
    w = ''.join(wire(f'M270 {y + 25} C400 {y + 25},420 {t},540 {t}', i) for i, (y, t) in enumerate(zip(ys, tgt)))
    chips = ''.join(f'<rect class="chip" x="20" y="{y}" width="250" height="50" rx="16"/><text x="38" y="{y + 31}">{e(n)}</text>' for n, y in zip(S2, ys))
    return (f'<figure class="schema reveal"><svg viewBox="0 0 760 380" role="img" aria-label="{T["s2alt"]}">{DEFS.format(n=2)}{w}{chips}'
            f'<rect class="core" x="540" y="135" width="180" height="100" rx="26" fill="url(#g2)"/><g transform="translate(630 185) scale(1.25)">{GEM}</g>'
            f'<text class="cap" x="630" y="268" text-anchor="middle">{T["s2"]}</text></svg></figure>')


def jev_html():
    tot = sum(v for *_, v, _ in JEV)
    seg = ''.join(f'<span class="seg {c}" style="flex:{v}"></span>' for _, _, v, c in JEV)
    leg = ''.join(f'<li><span class="dot {c}"></span><b>{v}</b> {e(fr if FR else en)}</li>' for fr, en, v, c in JEV)
    return (f'<figure class="jev reveal"><div class="stack" role="img" aria-label="{tot}">{seg}</div><ul>{leg}</ul>'
            f'<p class="jl"><b>{JEV_FILL}</b> {T["jev_fill"]} · {T["jev_score"]} <b>{JEV_SCORE}</b>/100</p><figcaption>{T["jev_cap"]}</figcaption></figure>')


def tree_html():
    out, panels, open_kids = [], [], False
    for i, (depth, name, fr, en, ex) in enumerate(TREE):
        folder = depth == 0 and name.endswith('/')
        if depth == 0 and open_kids:
            out.append('</div></div>')
            open_kids = False
        exp = ' aria-expanded="true"' if folder else ''
        out.append(f'<button class="node d{depth}{" folder" if folder else ""}" type="button" data-i="{i}"{exp}>{I_CHEV if folder else ""}<span class="nm">{e(name)}</span></button>')
        if folder:
            out.append('<div class="kids"><div class="kin">')
            open_kids = True
        ex_html = f'<p class="exl">{T["example"]}</p><pre>{e(ex)}</pre>' if ex else ''
        panels.append(f'<div class="pane" id="p{i}" hidden><p class="pn">{e(name)}</p><p class="pd">{e(fr if FR else en)}</p>{ex_html}</div>')
    if open_kids:
        out.append('</div></div>')
    return (f'<div class="tree reveal"><div class="nodes" aria-label="{T["tree"]}"><p class="root">ma-base/</p>{"".join(out)}</div>'
            f'<div class="panes" aria-live="polite"><p class="pick">{T["pick"]}</p>{"".join(panels)}</div></div>')


TOKEN = re.compile(r'(\[[^\]]*\]|https://(?:monsite\.fr|mysite\.com)|(?:monsite\.fr|mysite\.com))')


def consigne_html(text, key):
    parts, out, k = TOKEN.split(text), [], 0
    for j, part in enumerate(parts):
        if j % 2 == 0:
            out.append(e(part))
            continue
        if part.startswith('[') and part != '[...]':
            label = part[1:-1]
        elif part == '[...]':
            m = re.search(r'(\w+)\s?:\s?$', parts[j - 1])
            label = m.group(1) if m else '…'
        else:
            label = part
        out.append(f'<input class="fill" type="text" data-ph="{ea(part)}" data-k="{key}-{k}" placeholder="{ea(label)}" aria-label="{ea(label)}" size="{max(len(label), 4)}" autocomplete="off" autocapitalize="off" spellcheck="false">')
        k += 1
    return ''.join(out)


def skill_parts(text):
    ls = text.split('\n')
    cons = [l[2:] for l in ls if l.startswith('> ')]
    if not cons:
        cons = [l.strip('«» "“”') for l in ls if re.match(r'^[«"“]', l) and '[' in l][-1:]
    outs, i = [], next((i for i, l in enumerate(ls) if re.match(r'## (\d+\. )?(Sortie|Output)$', l)), None)
    if i is not None:
        for l in ls[i + 1:]:
            if l.startswith('## '):
                break
            if l.startswith('- '):
                outs.append(l[2:])
    else:
        a = next((i for i, l in enumerate(ls) if l in ('Format markdown avec :', 'Markdown format with:')), None)
        b = next((i for i, l in enumerate(ls) if l in ('Garde-fous', 'Guardrails')), None)
        if a is not None and b is not None:
            outs = [l for l in ls[a + 1:b] if l.strip()]
    m = re.search(r'^(?:Enregistre|Save).*`([^`]+\.md)`', text, re.M)
    return cons, outs, (m.group(1) if m else '')


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


n_skill, last_h3 = 0, ''


def skill_html(text):
    global n_skill
    n_skill += 1
    sid = f'skill{n_skill}'
    m = re.match(r'name: (\S+)', text)
    name = m.group(1) if m else re.sub(r'[^a-z]+', '-', re.sub(r'^[\d.]+\s*', '', last_h3).lower()).strip('-')
    heads = []
    pre = '\n'.join(hl(l, sid, heads) for l in text.split('\n'))
    chips = ''.join(f'<button class="chipb" type="button" data-t="{hid}">{e(t)}</button>' for hid, t in heads)
    chips = f'<div class="chips" aria-label="{T["sections"]}">{chips}</div>' if heads else ''
    cons, outs, fname = skill_parts(text)
    rows = ''.join(f'<div class="crow"><p class="cons">{consigne_html(c, f"{sid}-{j}")}</p>{COPYBTN("copyc", T["copyc"])}</div>' for j, c in enumerate(cons))
    play = (f'<button class="btn play" type="button">{I_PLAY}<span>{T["play"]}</span></button>'
            f'<div class="term" hidden data-out="{ea(json.dumps(outs, ensure_ascii=False))}" data-file="{ea(fname)}"><div class="tbar">{T["out"]}</div><pre aria-live="polite"></pre></div>') if outs else ''
    return (f'<section class="skillbox" id="{sid}" data-name="{ea(name)}"><div class="sbar"><span class="sname">{e(name)}</span><span class="smeta">{text.count(chr(10)) + 1} {T["lines"]}</span>'
            f'<button class="btn dl" type="button" aria-label="{T["dl"]} {ea(name)}">{I_DL}<span>{T["dl"]}</span></button>{COPYBTN("copy", T["copy"])}</div>'
            f'{chips}<div class="swrap"><pre id="{sid}pre">{pre}</pre></div>'
            f'<button class="more" type="button" aria-expanded="false" aria-controls="{sid}pre" data-show="{T["show"]}" data-hide="{T["hide"]}">{T["show"]}</button>'
            f'<div class="try"><p class="tl">{T["fill"]}</p>{rows}{play}</div></section>')


cover, by, body, toc, final = {}, [], [], [], ''
ul_open = in_skill = False
skill, n_sec = [], 0


def close_ul():
    global ul_open
    if ul_open:
        body.append('</ul>')
        ul_open = False


WIDGETS = {'02-scoring': scoring_html, '04-argument-1': schema1, '05-argument-2': schema2, '06-llm-wiki': tree_html}

for raw in lines:
    if in_skill:
        if raw == '@@end':
            body.append(skill_html('\n'.join(skill)))
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
    elif tag in ('h2', 'h2n'):
        n_sec += 1
        toc.append((n_sec, t))
        body.append(f'<h2 id="s{n_sec}" class="reveal">{t}</h2>')
    elif tag == 'h3': last_h3 = txt; body.append(f'<h3>{t}</h3>')
    elif tag == 'h4': body.append(f'<h4 class="dir">{t}</h4>')
    elif tag == 'k': body.append(f'<h4>{t}</h4>')
    elif tag == 'b': body.append(f'<p class="b">{t}</p>')
    elif tag == 'image':
        path, _, pct = txt.partition(' ')
        w = next((f for k, f in WIDGETS.items() if k in path), None)
        if w is tree_html:
            body.append(f'<figure class="shot"><button class="zoom" type="button" aria-label="{T["zoom"]}"><img src="{PRE}{path}" alt="" loading="lazy"></button></figure>')
            body.append(w())
        elif w:
            body.append(w())
        else:
            style = f' style="max-width:{pct}%"' if pct else ''
            body.append(f'<figure class="shot"{style}><button class="zoom" type="button" aria-label="{T["zoom"]}"><img src="{PRE}{path}" alt="" loading="lazy"></button></figure>')
    elif tag == 'skill': in_skill = True
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
        if re.match(r'verifier ?:', txt):
            body.append(jev_html())
close_ul()

toc_html = ''.join(f'<li><a href="#s{i}">{t}</a></li>' for i, t in toc)
desc = next(l for l in lines if l.strip() and not l.startswith('@@'))
OG = 'og.png' if FR else 'og.en.png'

CSS = (here / 'web.css').read_text().replace('url(geist', f'url({PRE}geist')
JS = (here / 'web.js').read_text()

URL = SITE if FR else SITE + 'en/'
HEAD_DEPLOY = (f'<link rel="canonical" href="{URL}">\n<link rel="alternate" hreflang="fr" href="{SITE}">\n<link rel="alternate" hreflang="en" href="{SITE}en/">\n'
               f'<meta property="og:url" content="{URL}">\n<meta property="og:site_name" content="Organikk">\n<meta name="twitter:image" content="{SITE + OG}">\n'
               f'<link rel="icon" href="/icon.svg" type="image/svg+xml">') if DEPLOY else ''
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
<meta property="og:image" content="{SITE + OG if DEPLOY else OG}">
{HEAD_DEPLOY}
<meta name="twitter:card" content="summary_large_image">
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
<section class="qcard panel reveal"><p class="qt">{T['q_title']}</p><p class="qn" data-base="{len(QUIZ)} questions · {T['q_yes']} / {T['q_no']}">{len(QUIZ)} questions · {T['q_yes']} / {T['q_no']}</p><button class="qopen" type="button"><span>{T['q_open']}</span>{I_ARROW}</button></section>
  </article>
</div>
<footer class="end panel"><div class="in">{final}{MARK}</div></footer>
<button class="pill" type="button" aria-label="{T['next']}"><b></b> {T['count']}</button>
<div class="resume" hidden><button class="go" type="button"><span class="rl">{T['resume']}</span><span class="rs"></span></button><button class="rx" type="button" aria-label="{T['close']}">{I_X}</button></div>
<dialog class="sheet" aria-label="{T['toc']}"><div class="sh"><p>{T['toc']}</p><button class="sx" type="button" aria-label="{T['close']}">{I_X}</button></div><ol>{toc_html}</ol></dialog>
<dialog class="quiz" aria-label="{T['q_name']}">
  <div class="qhead"><button class="qback" type="button" aria-label="{T['q_back']}" hidden>{I_ARROW}</button><span class="qstep" aria-live="polite"></span><button class="qx" type="button" aria-label="{T['close']}">{I_X}</button></div>
  <div class="qbar" aria-hidden="true"><i></i></div>
  <div class="qbody">
    <div class="qq"><p class="qtext"></p><div class="qans"><button class="qyes" type="button">{T['q_yes']}</button><button class="qno" type="button">{T['q_no']}</button></div></div>
    <div class="qres" hidden><div class="qscore panel"><p><b></b><span></span></p><div class="qmeter" aria-hidden="true"><i></i></div><p class="qmsg"></p></div>
      <div class="qnext"><p class="ql">{T['q_next']}</p><a class="qgo" href="#"></a></div>
      <div class="qalso"><p class="ql">{T['q_also']}</p><ul></ul></div>
      <div class="qtips"><p class="ql">{T['q_tips']}</p><ul></ul></div>
      <div class="qend"><a class="cta qcta" href="#"></a><button class="btn qagain" type="button">{T['q_again']}</button></div></div>
  </div>
</dialog>
<dialog class="lightbox" aria-label="{T['zoom']}"><button class="lx" type="button" aria-label="{T['close']}">{I_X}</button><img alt=""></dialog>
<script>window.GUIDE={json.dumps({'zip': T['zipname'], 'quiz': [[fr if FR else en, t] for fr, en, t in QUIZ], 'tiers': T['q_tiers'], 'tips': json.loads((here / 'conseils.json').read_text())[LANG], 'pt': T['q_pt'], 'inplace': T['q_in']}, ensure_ascii=False)}</script>
<script>{JS}</script>
</body>
</html>
"""
(here / OUT).parent.mkdir(parents=True, exist_ok=True)
(here / OUT).write_text(doc)
print(OUT, len(doc) // 1024, 'Ko', '·', len(toc), 'sections ·', n_skill, 'skills')
