"""Visuels de la newsletter Algorithme « J'ai imaginé la stratégie GEO de HubSpot » (skill infographie-schema).
Textes : newsletter collée par Tim le 2026-10-28, archivée dans [[sources/2026-10-27-algorithme-strategie-geo-hubspot]].
Réutilise HEAD et grain() de build.py ; les compositions sont propres à ce sujet.
Version en cases, demandée par Tim le 2026-10-28 (« fais des cases »)."""
import math
from build import grain, page

def box(x, y, w, h, stroke="#0B0B0F", fill="#FFF"):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="{fill}" stroke="{stroke}" stroke-width="1.5"/>'

def blue(x, y, w, h):
    return grain(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6"/>')

# ---------- A : la frontière agents / équipes ----------
fx = 660
auto = ["Maillage interne", "Métadonnées", "Structures Hn", "Audits répétitifs", "Mises à jour techniques"]
skills = ["Créer des agents", "Entraîner un agent", "Faire collaborer plusieurs agents"]
equipe = [("La direction stratégique", "Ce qui mérite d'être fait, plutôt que comment le faire"),
          ("La direction artistique", "Une intention, des références, une identité, des contraintes"),
          ("La direction éditoriale", "Le positionnement, le ton de voix, les messages importants"),
          ("La connaissance du client", "Son métier, ses problèmes, ses contraintes, ses objectifs"),
          ("L'esprit critique", "Repérer les erreurs et les angles morts des agents"),
          ("Savoir critiquer plutôt que produire", "Développer sa capacité d'évaluation")]
o = ['<text class="h" x="60" y="110">Le futur du consulting SEO</text>',
     '<text class="sub" x="60" y="148">Ce que les agents prennent, ce que les équipes gardent</text>',
     '<text class="a" x="60" y="250">I. AUTOMATISÉ</text>']
for i, t in enumerate(auto):
    y = 270 + i*54
    o.append(box(60, y, 520, 44, stroke="#BBBBBB"))
    o.append(f'<text class="s" x="80" y="{y+28}" style="fill:#777;text-decoration:line-through">{t}</text>')
o.append('<text class="a" x="60" y="596">Compétences à développer</text>')
for i, t in enumerate(skills):
    y = 616 + i*62
    o.append(box(60, y, 520, 52))
    o.append(f'<text class="a" x="80" y="{y+33}">0{i+1}</text><text class="t" x="116" y="{y+34}" style="font-size:21px">{t}</text>')
o.append(f'<line class="thin" x1="{fx}" y1="220" x2="{fx}" y2="900"/>')
o.append('<text class="a" x="740" y="250">II. RÉSERVÉ AUX ÉQUIPES</text>')
for i, (t, s) in enumerate(equipe):
    y = 270 + i*100
    if i == 4:
        o.append(blue(740, y, 736, 88))
        o.append(f'<text class="t" x="764" y="{y+38}" style="fill:#FFF">{t}</text><text class="s" x="764" y="{y+68}" style="fill:#FFF">{s}</text>')
    else:
        o.append(box(740, y, 736, 88))
        o.append(f'<text class="t" x="764" y="{y+38}">{t}</text><text class="s" x="764" y="{y+68}">{s}</text>')
o.append('<text class="a" x="60" y="964">Thèse de Tim, newsletter Algorithme.</text>')
page("strategie-geo-hubspot-a-frontiere.svg", o)

# ---------- B : 50 questions convergent vers 5 pages ----------
offres = [("Smart CRM", "CRM pour PME", "/products/crm"),
          ("Marketing Hub", "logiciel marketing automation", "/products/marketing"),
          ("Sales Hub", "logiciel de gestion commerciale", "/products/sales"),
          ("Service Hub", "logiciel service client", "/products/service"),
          ("Content Hub", "logiciel de gestion de contenu", "/products/content")]
ex, x0 = 1130, 520
o = ['<text class="h" x="60" y="110">50 questions, 5 pages business</text>',
     '<text class="sub" x="60" y="148">Les questions qui partagent une intention vont sur la même page, pas sur 50 URL</text>',
     f'<text class="a" x="{x0}" y="236">5 micro-intentions × 2 questions par offre</text>',
     f'<text class="a" x="{ex}" y="236">page business existante</text>']
for r, (nom, req, url) in enumerate(offres):
    y = 320 + r*125
    focus = r == 0
    col = "#0B0B0F" if focus else "#BBBBBB"
    o.append(box(60, y-40, 400, 80, stroke="#0B0B0F" if focus else "#BBBBBB"))
    o.append(f'<text class="t" x="84" y="{y-6}">{nom}</text><text class="s" x="84" y="{y+24}" style="fill:#777">{req}</text>')
    for k in range(10):
        x = x0 + k*30 + (k//2)*24
        dy = y + (k-4.5)*7
        o.append(f'<path d="M{x} {dy:.0f} C{x+160} {dy:.0f}, {ex-160} {y}, {ex} {y}" fill="none" stroke="{col}" stroke-width="1"/>')
        o.append(f'<circle cx="{x}" cy="{dy:.0f}" r="5" fill="{"#0B0B0F" if focus else "#777"}"/>')
    if focus:
        o.append(blue(ex, y-30, 340, 60))
        o.append(f'<text class="v" x="{ex+22}" y="{y+6}" style="fill:#FFF">hubspot.com/products/crm</text>')
    else:
        o.append(box(ex, y-30, 340, 60))
        o.append(f'<text class="s" x="{ex+22}" y="{y+6}">{url}</text>')
o.append('<text class="a" x="60" y="964">Questions : hypothèses éditoriales de départ, à enrichir jusqu\'à 75 avec les demandes réelles des prospects.</text>')
page("strategie-geo-hubspot-b-convergence.svg", o)

# ---------- C : 92 % + une preuve par question ----------
cx, cy, R, sw = 380, 540, 210, 34
a = math.radians(-90 + 360*0.92)
paires = [("Est-ce adapté à mon entreprise ?", "Un cas client du même secteur"),
          ("Combien cela coûte ?", "Des tarifs et un scénario budgétaire"),
          ("Quels résultats attendre ?", "Des données clients documentées"),
          ("Comment ça fonctionne ?", "Une démonstration du produit"),
          ("Est-ce difficile à installer ?", "Un exemple réel de déploiement"),
          ("Quel bénéfice concret ?", "Un avant/après documenté")]
o = ['<text class="h" x="60" y="110">Une preuve par question d\'acheteur</text>',
     '<text class="sub" x="60" y="148">Les pages sectorielles HubSpot, bâties sur de vrais cas clients</text>',
     f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="none" stroke="#F5F5F5" stroke-width="{sw}"/>',
     grain(f'<path d="M{cx} {cy-R-sw/2} A{R+sw/2} {R+sw/2} 0 1 1 {cx + (R+sw/2)*math.cos(a):.1f} {cy + (R+sw/2)*math.sin(a):.1f} '
           f'L{cx + (R-sw/2)*math.cos(a):.1f} {cy + (R-sw/2)*math.sin(a):.1f} A{R-sw/2} {R-sw/2} 0 1 0 {cx} {cy-R+sw/2} Z"/>'),
     f'<text class="big" x="{cx}" y="{cy+30}" text-anchor="middle" style="font-size:120px;letter-spacing:-5px">92 %</text>',
     f'<text class="s" x="{cx}" y="{cy+76}" text-anchor="middle">des pages sectorielles</text>',
     f'<text class="s" x="{cx}" y="{cy+100}" text-anchor="middle">citées par des moteurs de réponse</text>',
     '<text class="a" x="760" y="290">QUESTION</text><text class="a" x="1116" y="290">PREUVE À PRODUIRE</text>']
for i, (q, p) in enumerate(paires):
    y = 312 + i*72
    o.append(box(760, y, 310, 52, stroke="#BBBBBB"))
    o.append(f'<text class="s" x="776" y="{y+32}" style="fill:#777">{q}</text>')
    o.append(f'<line class="thin" x1="1076" y1="{y+26}" x2="1108" y2="{y+26}" marker-end="url(#p)"/>')
    o.append(box(1116, y, 360, 52))
    o.append(f'<text class="v" x="1134" y="{y+32}">{p}</text>')
o += [box(760, 772, 716, 92, stroke="#F5F5F5", fill="#F5F5F5"),
      '<text class="s" x="784" y="812">Les preuves ne servent pas seulement à obtenir des citations.</text>',
      '<text class="s" x="784" y="840">Elles répondent aux objections et facilitent la conversion.</text>',
      '<text class="a" x="60" y="964">92 % : chiffre déclaré par HubSpot dans son étude de cas officielle. Paires question/preuve : méthode Organikk.</text>']
page("strategie-geo-hubspot-c-preuves.svg", o)
