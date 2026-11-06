import re, pathlib, sys, importlib
# usage : python3 assemble.py <slug-site> <module-vues> <sortie.html>
# le module de vues expose SITE, DATE, SOUS_TITRE, GSC (bool) et V[0..7]
S = pathlib.Path(__file__).parent
sys.path.insert(0, str(S)); sys.path.insert(0, str(pathlib.Path(sys.argv[2]).parent))
VV = importlib.import_module(pathlib.Path(sys.argv[2]).stem)
SITE, DATE, SOUS = VV.SITE, VV.DATE, getattr(VV, "SOUS_TITRE", "")
base = (S / "base-reference.html").read_text(encoding="utf-8")

# ── coque : nom du site, date, onglet 4, chip sources ─────────────────────────
h = base
from cartes import CSS_MINIS
h = h.replace("/* ── avert", CSS_MINIS + "\n/* ── avert", 1)
h = h.replace("/* ── avert", ".dashwrap .profil .av.score{background:none;color:var(--c-top);font-size:56px;font-weight:700;letter-spacing:-.04em;width:auto;height:auto;border-radius:0;position:relative}\n.dashwrap .profil .av.score .aide{position:absolute;right:-22px;top:6px}\n/* ── avert", 1)
h = h.replace("/* ── avert", ".dashwrap details.repli{margin-top:28px;border:1px solid var(--line);border-radius:var(--r-md);padding:14px 18px;background:var(--paper)}\n.dashwrap details.repli summary{cursor:pointer;font-weight:600;color:var(--c-top);font-size:14.5px}\n.dashwrap details.repli[open] summary{margin-bottom:8px}\n/* ── avert", 1)
h = h.replace("/* ── avert", """
/* ── retouche visuelle 28/09 : cartes sans soulignement, chiffres en gros, légendes courtes ── */
.dashwrap a.card,.dashwrap a.card *{text-decoration:none!important}
.dashwrap a.card{color:var(--ink)}
.dashwrap .card{border-radius:20px;border-color:#e6e8ee;box-shadow:0 1px 2px rgba(17,24,39,.03),0 14px 36px -26px rgba(33,55,157,.22)}
.dashwrap a.card:hover{border-color:#cdd8f8;box-shadow:0 18px 40px -22px rgba(33,55,157,.28);transform:translateY(-2px)}
.dashwrap .kpi{min-height:186px;padding:22px 22px 20px}
.dashwrap .kpi .t{font-size:14px;font-weight:600;color:var(--ink);letter-spacing:-.01em;padding-right:52px;line-height:1.35}
.dashwrap .kpi .n{font-size:44px;margin-top:18px;letter-spacing:-.035em}
.dashwrap .kpi .n .aide{margin-left:8px;vertical-align:middle;position:relative;top:-14px}
.dashwrap .kpi .l{font-size:13.5px;color:var(--ink-2);margin-top:8px;font-weight:500}
.dashwrap .kpi .src{font-family:var(--sans);font-size:12.5px;color:var(--ink-3);margin-top:10px;line-height:1.5;letter-spacing:0}
.dashwrap .kpi .ico-rond{top:20px;right:20px;width:36px;height:36px;border-radius:12px}
.dashwrap .profil .card-head{width:100%;justify-content:center}
.dashwrap .profil .ring{margin-top:16px}
.dashwrap .profil .av.score{font-size:52px}
.dashwrap .profil b{font-size:21px;letter-spacing:-.02em}
.dashwrap .profil .role{font-size:12.5px;line-height:1.45;max-width:26ch}
.dashwrap .chips{gap:6px;margin-top:18px}
.dashwrap .chip{font-size:12px;padding:5px 11px;background:#fff;border-color:#e6e8ee;color:var(--ink-2);box-shadow:0 1px 2px rgba(17,24,39,.03)}
.dashwrap .chip b{color:var(--ink);font-weight:600;margin-right:2px}
.dashwrap .chip i{width:7px;height:7px}
.dashwrap .sources{padding:20px 22px;background:#f7f9ff;border-color:#e3e9ff}
.dashwrap .sources b{font-size:14px}
.dashwrap .sources span{font-size:12.5px;line-height:1.5}
.dashwrap .card-head h3{font-size:15.5px}
.dashwrap .card > .card-head + .note,.dashwrap .card .note{font-size:13.5px;line-height:1.6}
.dashwrap .barres .jauge i{background:linear-gradient(90deg,var(--c-top),var(--c-bottom))}
.dashwrap .barres .n{color:var(--ink);font-weight:600}
.dashwrap table{font-size:13.5px}
.dashwrap thead th{background:#f6f7fb}
.dashwrap .rangee > .col{align-content:start}
.dashwrap .sources{align-self:start}
.dashwrap .profil .chips{flex-direction:column;align-items:stretch;gap:8px;width:100%}
.dashwrap .profil .chip{display:flex;align-items:flex-start;justify-content:flex-start;gap:10px;text-align:left;border-radius:12px;padding:9px 12px;line-height:1.4}
.dashwrap .profil .chip i{margin-top:5px;flex:none}
.dashwrap .profil .chip span{min-width:0}
/* ── avert""", 1)
h = h.replace("<title>Audit fusionn.co</title>", f"<title>Audit {SITE}</title>")
h = h.replace('<span class="fs-site-avatar">f</span><div class="fs-site-identity"><small>Site audité</small><strong>fusionn.co</strong></div>',
              f'<span class="fs-site-avatar">{SITE[0]}</span><div class="fs-site-identity"><small>Site audité</small><strong>{SITE}</strong></div>')
h = h.replace("<span>Structure des titres</span>", "<span>Contenu et pertinence</span>").replace("<span>Maillage interne</span>", "<span>Liens internes</span>")
h = h.replace('<strong>Audit du 26/09/2026 · Claude</strong><small>fusionn.co</small>', f'<strong>Audit du {DATE} · Claude</strong><small>{SITE}{SOUS}</small>')
h = h.replace('<span class="kchat-project-name" title="fusionn.co">fusionn.co</span>', f'<span class="kchat-project-name">{SITE}</span>')  # sans title : la coque met cursor:help sur [title], un « ? » au survol du nom
if not getattr(VV, "GSC", False):
    h = h.replace('<div class="kchat-sources" title="Search Console vérifiée, 6 mois de données"><span>Avec Search Console</span></div>', '<div class="kchat-sources" title="Aucun accès à la Search Console : je ne vois ni l’indexation, ni les recherches, ni les clics"><span>Sans Search Console</span></div>')
    # sans Search Console, l'indexation réelle n'est pas observée : l'onglet mesure l'indexabilité
    h = h.replace('<span>Indexation</span><i class="num">2</i>', '<span>Indexabilité</span><i class="num">2</i>')



def view(n, inner):
    """remplace le contenu d'une vue data-view=n en gardant l'enveloppe kchat-msg/dashwrap ou markdown"""
    global h
    pat = re.compile(r'(<div class="kchat-msg(?: home on)?" data-view="%d"><div class="(?:markdown|dashwrap)">)(.*?)(</div></div>\n\n<!-- ═══|</div></div>\n\n\n        </div>)' % n, re.S)
    m = pat.search(h); assert m, n
    h = h[:m.start(2)] + inner + h[m.end(2):]


for n in range(8):
    view(n, VV.V[n])

# ── sans Search Console, le dire en clair dans le Résumé (Tim, 29/09/2026) ────
# Un audit mené sans accès à la Search Console est moins précis : l'indexation
# réelle, les recherches, les clics et les conversions ne sont pas observés.
# La phrase est dans la coque plutôt que dans chaque vues.py, pour qu'elle
# descende dans tous les audits au réassemblage.
_SANS_GSC = ("""<div class="sansgsc">"""
  """<b>Cet audit est moins précis qu'il pourrait l'être : je n'ai pas eu accès à votre Search Console.</b>"""
  """<p>Sans elle, je ne vois pas ce que Google indexe, ni les recherches sur lesquelles vous apparaissez, """
  """ni les clics, ni les pages qui amènent des clients. Je mesure ce que le site donne à voir, pas ce qu'il obtient.</p>"""
  """<p>Un accès en lecture à la propriété, ou un export sur 3 à 6 mois avec toutes les requêtes et toutes les pages, """
  """fait monter la précision de cet audit et permet de trancher ce qui reste ouvert.</p>"""
  """</div>""")
if not getattr(VV, "GSC", False):
    h = h.replace('<div class="kchat-msg home on" data-view="1"><div class="dashwrap">',
                  '<div class="kchat-msg home on" data-view="1"><div class="dashwrap">' + _SANS_GSC, 1)
    h = h.replace("/* ── avert", """.dashwrap .sansgsc{margin:0 0 30px;padding:18px 20px;border-radius:16px;border:1px solid #e3e9ff;background:#f7f9ff}
.dashwrap .sansgsc b{display:block;font-size:14.5px;line-height:1.5;color:var(--c-top);margin-bottom:10px}
.dashwrap .sansgsc p{margin-top:12px!important;font-size:13.5px;line-height:1.65;color:var(--ink-2)}
/* ── avert""", 1)
out = pathlib.Path(sys.argv[3])
# ── pied de barre latérale : une seule ligne, bouton Système SEO (organikk.co/systeme-seo/) + X + Substack (Tim, 06/10/2026 ; avant : Call vers Cal.com)
_PIED = ('<div class="fs-contact">'
  '<a class="rdv" href="https://organikk.co/systeme-seo/" target="_blank" rel="noreferrer">'
  '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3 3 8l9 5 9-5-9-5z"/><path d="m3 13 9 5 9-5"/><path d="m3 17.5 9 5 9-5"/></svg>'
  '<span><b>Système SEO</b></span></a>'
  '<a class="ic" href="https://x.com/Timseo_" target="_blank" rel="noreferrer" aria-label="X"><svg viewBox="0 0 24 24" width="15" height="15" fill="currentColor" aria-hidden="true"><path d="M18.24 2.25h3.31l-7.23 8.26 8.5 11.24h-6.66l-5.22-6.82-5.97 6.82H1.66l7.73-8.83L1.24 2.25h6.83l4.71 6.23 5.46-6.23zm-1.16 17.52h1.83L7.08 4.13H5.11l11.97 15.64z"/></svg></a>'
  '<a class="ic" href="https://algorithme.substack.com/" target="_blank" rel="noreferrer" aria-label="Substack"><svg viewBox="0 0 24 24" width="15" height="15" fill="currentColor" aria-hidden="true"><path d="M22.54 8.24H1.46V5.41h21.08v2.83zM1.46 10.81V24L12 18.11 22.54 24V10.81H1.46zM22.54 0H1.46v2.83h21.08V0z"/></svg></a>'
  '</div>')
h = re.sub(r'<div class="fs-suite">.*?</ul>', _PIED, h, count=1, flags=re.S)
# règle de Tim du 06/10/2026, « pour les prochains toujours le bouton Système SEO, toujours » : jamais de Call ni de Cal.com
assert 'href="https://organikk.co/systeme-seo/"' in h and "cal.com" not in h.lower(), "pied de barre : bouton Système SEO manquant ou lien Cal.com présent"
h = h.replace("/* ── avert", """.fs-contact{display:flex;align-items:stretch;gap:8px;padding:0 0 14px}
.fs-contact a{cursor:pointer;position:relative;isolation:isolate;display:inline-flex;align-items:center;justify-content:center;border-radius:12px;background:#fff;border:1px solid rgba(47,79,224,.18);color:#2f4fe0;text-decoration:none;box-shadow:0 1px 2px -1px rgba(27,62,143,.1);transition:transform .22s cubic-bezier(.2,0,0,1),color .22s,border-color .22s,box-shadow .22s}
.fs-contact a::before{content:"";position:absolute;inset:0;z-index:-1;border-radius:inherit;background:linear-gradient(135deg,#2f4fe0 0%,#4f78ff 55%,#7fa0ff 100%);opacity:0;transition:opacity .22s cubic-bezier(.2,0,0,1)}
.fs-contact a:hover,.fs-contact a:focus-visible{color:#fff;transform:translateY(-2px);border-color:transparent;box-shadow:0 14px 26px -14px rgba(47,79,224,.55)}
.fs-contact a:hover::before,.fs-contact a:focus-visible::before{opacity:1}
.fs-contact .rdv{flex:1;min-width:0;justify-content:flex-start;gap:9px;padding:9px 11px;font-size:11.5px;font-weight:500;line-height:1.3;text-align:left}
.fs-contact .rdv svg{flex:none}
.fs-contact .rdv span{display:flex;flex-direction:column;min-width:0}
.fs-contact .rdv b{font-weight:600;font-size:12px;white-space:nowrap}
.fs-contact .rdv small{font-size:10px;color:#6b7280;line-height:1.25}
.fs-contact .rdv:hover small{color:rgba(255,255,255,.85)}
.fs-contact .ic{width:38px;flex:none}
.fs-contact svg{display:block}
/* ── avert""", 1)

out.write_text(h, encoding="utf-8")
print("écrit", out, len(h), "octets")
