# -*- coding: utf-8 -*-
# Contenu des huit vues du dashboard organikk.co (5 pages).
# Ton : un consultant qui vient de finir son audit et explique à son client.
# Constat le plus important d'abord, les chiffres qui le font comprendre, pourquoi c'est un problème
# seulement si ce n'est pas évident, puis ce qu'il faut faire. Une idée par phrase.

def aide(t, bas=False):
    return f'<button type="button" class="aide{" bas" if bas else ""}" data-aide="{t}" aria-label="{t}">?</button>'

V = {}

RESUME_TXT = """AUDIT SEO de organikk.co, 5 pages, releve du 28/09/2026

PERIMETRE
5 pages lues et mesurees : accueil, /methode/, /systeme/, /bootcamp/, /audit-seo/.
30 pages du sitemap inspectees dans Google. 103 anciennes adresses controlees.

CE QUI VA BIEN
Les 5 pages sont indexees, Google les lit correctement et elles sont rapides
pour vos visiteurs (2,20 s sur mobile).

CE QUI POSE PROBLEME
1. Presque aucune page du site ne fait de lien vers vos pages d'offre.
   /audit-seo/ n'a aucun lien. /bootcamp/ en a un seul. Le menu « Bootcamp »
   envoie vers le formulaire de candidature, pas vers la presentation.
2. /methode/ et /systeme/ apparaissent dans Google sans etre cliquees :
   147 affichages en 90 jours, position 5 a 6, zero clic. Les deux pages
   racontent la meme offre.
3. 8 pages du sitemap sur 30 ne sont pas indexees, dont 2 pages d'offre.
4. 76 anciennes adresses d'articles redirigent vers /systeme/, la page de l'offre.
5. La page d'accueil met 4 a 6 s a s'afficher en test (image du bandeau).

A FAIRE, DANS L'ORDRE
1. Ajouter des liens vers /audit-seo/ depuis /methode/ et /systeme/.
   Faire pointer le menu « Bootcamp » vers /bootcamp/.
2. Donner un role distinct a /methode/ et /systeme/. Pas de fusion pour l'instant.
3. Faire indexer les 2 pages d'offre manquantes (liens, puis nouvelle inspection).
4. Verifier les chiffres qui different d'une page a l'autre (100+ entreprises /
   14 missions, 1 000 articles / 2 000 contenus) et les ecrire pareil partout.
5. Reprendre les 76 anciennes adresses : rediriger vers une page equivalente,
   sinon repondre « introuvable ».

SCORE : 74/100 (partiel : 5 pages lues, 30 inspectees). Confiance 83 %.
Indexation 63 (30 %) · Vitesse 88 (20 %) · Contenu 71 (20 %) · Liens 58 (15 %)
Titres 100 (10 %) · Donnees structurees 100 (5 %)

CE QUE JE NE SAIS PAS
Sur quelles recherches apparaissent /methode/, /systeme/ et /audit-seo/ : elles
ne remontent pas. Ce que ces pages rapportent en demandes : pas de donnees.
Les liens que d'autres sites vous font : non regardes.

Mesures automatiques et lecture par une intelligence artificielle : des erreurs
sont possibles."""

# ═══ 0. FICHE D'IDENTITÉ ══════════════════════════════════════════════════════
V[0] = """
<h2>organikk.co : 5 pages étudiées en détail, 30 dans le sitemap</h2>
<p>Organikk est le site de Timothée B., consultant SEO à Lyon. Il vend un accompagnement SEO sur 6 mois, un bootcamp de quatre semaines pour consultants et un kit de skills pour Claude Code. Il propose aussi un audit SEO instantané en ligne.</p>
<p>J'ai choisi les cinq pages les plus vues dans Google sur les 90 derniers jours : l'accueil et quatre pages d'offre. Le sitemap déclare 30 pages. Sur la période, 125 adresses du site ont été affichées au moins une fois dans Google, dont 103 qui ne sont plus dans le sitemap : ce sont pour l'essentiel d'anciens articles retirés.</p>
<p class="note">Quand un chiffre porte sur 5 pages, c'est ce que j'ai lu et mesuré. Quand il porte sur 30, c'est le sitemap. Quand il porte sur 125, c'est la Search Console.</p>

<h4>Ce que le site dit de lui-même</h4>
<table>
<thead><tr><th>Élément</th><th style="width:62%">Relevé sur le site</th></tr></thead>
<tbody>
<tr><td>Promesse</td><td>« Des leads, pas du trafic » (accueil)</td></tr>
<tr><td>Offres</td><td>accompagnement SEO + GEO sur 6 mois · bootcamp SEO IA (4 semaines, 10 places) · kit de skills · audit SEO en direct</td></tr>
<tr><td>Chiffres affichés</td><td>« 7+ ans d'XP », « 1 000 articles de blog » (accueil) · « 100+ entreprises accompagnées », « +2 000 contenus produits » (/systeme/, /methode/) · « 14 missions B2B » (/resultats/)</td></tr>
<tr><td>Accès pour Google</td><td>robots.txt ouvert, sitemap déclaré</td></tr>
<tr><td>Données structurées</td><td>le même bloc sur les 5 pages : Organization / ProfessionalService, WebSite, Person</td></tr>
</tbody>
</table>

<h4>Vos objectifs</h4>
<p>Je les ai lus sur le site, vous ne me les avez pas confirmés. Offres prioritaires : l'accompagnement et le bootcamp. Clients visés : PME et consultants SEO francophones, Lyon comme base. Ce que vous attendez d'un visiteur : un rendez-vous (Cal.com) ou une candidature au bootcamp. Je n'ai aucune donnée sur les demandes reçues ou les ventes.</p>

<h4>Les 5 pages</h4>
<table>
<thead><tr><th>Page</th><th style="width:34%">Rôle</th><th class="num">Affichages 90 j</th><th class="num">Clics</th><th class="num">Position</th></tr></thead>
<tbody>
<tr><td class="mono">/</td><td>accueil, offre globale</td><td class="num">467</td><td class="num">82</td><td class="num">30,4</td></tr>
<tr><td class="mono">/methode/</td><td>la méthode en 4 étapes</td><td class="num">91</td><td class="num">0</td><td class="num">5,0</td></tr>
<tr><td class="mono">/bootcamp/</td><td>présentation du bootcamp</td><td class="num">85</td><td class="num">1</td><td class="num">28,9</td></tr>
<tr><td class="mono">/systeme/</td><td>l'accompagnement en 3 étapes</td><td class="num">56</td><td class="num">0</td><td class="num">5,6</td></tr>
<tr><td class="mono">/audit-seo/</td><td>outil d'audit instantané</td><td class="num">11</td><td class="num">0</td><td class="num">1,1</td></tr>
</tbody>
</table>

<div class="sources">Sources : Search Console, propriété https://organikk.co/, 30/06 au 27/09/2026 et les 90 jours précédents · inspection Google des 30 pages du sitemap et de 3 anciennes adresses, 28/09 · lecture des 30 pages et de leurs liens, 28/09 · code de chaque page avant et après JavaScript · Lighthouse 13.3.0 mobile · PageSpeed Insights, données réelles des visiteurs (CrUX), 28/09 · résultats Google sur 3 recherches, depuis les États-Unis · Google Keyword Planner, 25/09 (top 20).</div>
"""

# ═══ 1. RÉSUMÉ ════════════════════════════════════════════════════════════════
V[1] = """
<button type="button" id="copie-claude" class="copie-claude"><svg viewBox="0 0 24 24" aria-hidden="true" width="14" height="14"><g fill="currentColor"><rect x="11.1" y="2" width="1.8" height="20" rx=".9"/><rect x="11.1" y="2" width="1.8" height="20" rx=".9" transform="rotate(45 12 12)"/><rect x="11.1" y="2" width="1.8" height="20" rx=".9" transform="rotate(90 12 12)"/><rect x="11.1" y="2" width="1.8" height="20" rx=".9" transform="rotate(135 12 12)"/></g></svg><span>Copier le résumé pour Claude</span></button>
<script type="text/plain" id="resume-claude">""" + RESUME_TXT + """</script>

<div class="dash">
  <div class="col">

    <div class="rangee">
      <div class="card profil">
        <div class="card-head"><h3>Site</h3></div>
        <div class="ring"><svg viewBox="0 0 170 170"><circle cx="85" cy="85" r="78" fill="none" stroke="#eef0f5" stroke-width="9"/><circle cx="85" cy="85" r="78" fill="none" stroke="url(#scoreGrad)" stroke-width="9" stroke-linecap="round" stroke-dasharray="362.7 490.1"/></svg>
          <span class="av score">74""" + aide("Score pondéré : Indexation 30 %, Vitesse 20 %, Contenu 20 %, Liens internes 15 %, Titres 10 %, Données structurées 5 %. Seuls les problèmes prouvés retirent des points. 63 × 0,30 + 88 × 0,20 + 71 × 0,20 + 58 × 0,15 + 100 × 0,10 + 100 × 0,05 = 74,4. Partiel : 5 pages lues, 30 inspectées. Confiance 83 %.", True) + """</span></div>
        <b>organikk.co</b>
        <span class="role">relevé du 28/09/2026 · 5 pages lues, 30 inspectées</span>
        <span class="role">le score dit l'état de ces 5 pages, pas la part de marché du site</span>
        <div class="chips">
          <span class="chip r"><i></i><span><b>0 clic</b> sur 147 affichages, /methode/ et /systeme/</span></span>
          <span class="chip r"><i></i><span><b>0 lien</b> vers /audit-seo/</span></span>
          <span class="chip b"><i></i><span><b>8 / 30</b> pages du sitemap non indexées</span></span>
        </div>
      </div>
      <div class="col">
        <div class="kpis">
          <a href="#" data-vue="2" class="card kpi vert"><span class="ico-rond"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="7"/><path d="M20 20l-3.5-3.5"/></svg></span><span class="t">Indexation</span><b class="n">22 / 30""" + aide("Statut demandé à Google le 28/09 pour les 30 pages du sitemap : 22 indexées, 7 détectées mais non indexées, 1 inconnue. Les 5 pages étudiées sont toutes indexées.") + """</b><span class="l">pages du sitemap indexées</span><span class="src">8 manquantes dont 2 pages d'offre · 76 anciennes adresses redirigées vers /systeme/</span></a>
          <a href="#" data-vue="4" class="card kpi orange"><span class="ico-rond"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M6 4h9l4 4v12H6z"/><path d="M9 12h6M9 16h6"/></svg></span><span class="t">Contenu</span><b class="n">2 / 5""" + aide("Pages qui répondent au bon besoin, avec des chiffres appuyés, un rôle propre et un titre cohérent : l'accueil et /audit-seo/.") + """</b><span class="l">pages sans rien à corriger</span><span class="src">/methode/ et /systeme/ se recouvrent · des chiffres à aligner · titre de /bootcamp/ daté</span></a>
        </div>
        <div class="card sources">
          <div><b>Mesures utilisées</b><br><span>Search Console (6 mois), inspection Google, lecture des 30 pages et de leurs liens, code des pages avant et après JavaScript, Lighthouse mobile, PageSpeed Insights (visiteurs réels), résultats Google</span></div>
        </div>
      </div>
    </div>

    <div class="kpis">
      <a href="#" data-vue="3" class="card kpi rouge"><span class="ico-rond"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M10 14a4 4 0 0 0 5.7 0l3-3a4 4 0 0 0-5.7-5.7l-1.5 1.5"/><path d="M14 10a4 4 0 0 0-5.7 0l-3 3a4 4 0 0 0 5.7 5.7l1.5-1.5"/></svg></span><span class="t">Liens internes</span><b class="n">11""" + aide("Liens placés dans le texte des 30 pages (hors menu et pied de page) qui mènent aux 5 pages : /methode/ 8, /systeme/ 2, /bootcamp/ 1, /audit-seo/ 0, accueil 0 (mais 53 liens de menu).") + """</b><span class="l">liens dans le texte vers les 5 pages</span><span class="src">0 vers /audit-seo/ · le menu « Bootcamp » envoie vers la candidature</span></a>
      <a href="#" data-vue="5" class="card kpi vert"><span class="ico-rond"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 6a8 8 0 0 0-8 8h4a4 4 0 0 1 8 0h4a8 8 0 0 0-8-8z"/><path d="M12 14l3.5-3.5"/></svg></span><span class="t">Vitesse</span><b class="n">2,20 s""" + aide("Temps d'affichage chez vos visiteurs réels sur mobile (75e percentile, 28 jours, mesure Google à l'échelle du site). Bon sous 2,5 s. Mise en page stable. Réactivité non mesurable : pas assez d'interactions.") + """</b><span class="l">affichage chez vos visiteurs, mobile</span><span class="src">accueil 5,72 s et 4,01 s en test · les 4 autres pages sous 3,1 s</span></a>
      <a href="#" data-vue="6" class="card kpi bleu"><span class="ico-rond"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="6" rx="2"/><rect x="3" y="14" width="8" height="6" rx="2"/><rect x="15" y="14" width="6" height="6" rx="2"/></svg></span><span class="t">Données structurées</span><b class="n">5 / 5""" + aide("Balisage lisible sans erreur sur les 5 pages. Le même bloc partout, rien de propre à chaque page.") + """</b><span class="l">pages avec un balisage valide</span><span class="src">le même bloc sur les 5 · un balisage Course pour le bootcamp à étudier</span></a>
      <a href="#" data-vue="7" class="card kpi orange"><span class="ico-rond"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4 18h16"/><path d="M7 18V9M12 18V5M17 18v-6"/></svg></span><span class="t">Mots-clés business</span><b class="n">1 / 24""" + aide("24 recherches visibles pour les 5 pages sur 90 jours, hors votre nom. Une seule correspond à l'offre : « bootcamp seo », 50 affichages, position 28,7, 0 clic. Les recherches de /methode/, /systeme/ et /audit-seo/ ne remontent pas.") + """</b><span class="l">recherche commerciale visible</span><span class="src">« bootcamp seo », position 28,7, 0 clic · 3 pages sur 5 sans recherche visible</span></a>
    </div>

    <div class="card">
      <div class="card-head"><div><h3>Ce que j'ai trouvé</h3></div></div>
      <p class="note">Vos cinq pages sont en bon état. Elles sont indexées, Google les lit correctement et elles s'affichent vite chez vos visiteurs.</p>
      <p class="note">Le problème est ailleurs. Presque aucune page du site ne fait de lien vers elles. <code>/audit-seo/</code> n'a aucun lien. <code>/bootcamp/</code> en a un seul, depuis le plan du site. Le menu « Bootcamp » envoie vers le formulaire de candidature, pas vers la page qui présente le programme.</p>
      <p class="note">Ensuite, deux pages d'offre apparaissent dans Google sans jamais être cliquées. <code>/methode/</code> et <code>/systeme/</code> ont été affichées 147 fois en 90 jours, en position 5 à 6, pour zéro clic. Les deux pages racontent la même offre.</p>
      <p class="note">Sur les 30 pages du sitemap, 8 ne sont pas indexées. Deux sont des pages d'offre. Et 76 anciennes adresses d'articles redirigent vers <code>/systeme/</code>, la page de l'offre.</p>
      <p class="note">Ces trois points se corrigent sans toucher au contenu de vos pages. Les actions sont listées plus bas.</p>
    </div>

    <div class="card">
      <div class="card-head"><div><h3>Ce qui progresse et ce qui recule</h3><p class="sous">Du 30/06 au 27/09/2026, comparé aux 90 jours précédents.</p></div></div>
      <table>
      <thead><tr><th>Page</th><th class="num">Affichages</th><th class="num">Clics</th><th class="num">Position</th><th>Depuis quand</th><th>Ce que la page doit obtenir</th></tr></thead>
      <tbody>
      <tr><td class="mono">/</td><td class="num">391 → 467</td><td class="num">67 → 82</td><td class="num">6,0 → 30,4</td><td>1er août</td><td>un rendez-vous</td></tr>
      <tr><td class="mono">/bootcamp/</td><td class="num">108 → 85</td><td class="num">0 → 1</td><td class="num">11,1 → 28,9</td><td>fin juillet</td><td>une candidature</td></tr>
      <tr><td class="mono">/methode/</td><td class="num">101 → 91</td><td class="num">0 → 0</td><td class="num">6,4 → 5,0</td><td>stable</td><td>un rendez-vous</td></tr>
      <tr><td class="mono">/systeme/</td><td class="num">12 → 56</td><td class="num">0 → 0</td><td class="num">5,3 → 5,6</td><td>en hausse</td><td>un rendez-vous</td></tr>
      <tr><td class="mono">/audit-seo/</td><td class="num">0 → 11</td><td class="num">0 → 0</td><td class="num">n/a → 1,1</td><td>nouvelle</td><td>une adresse de site, puis un rendez-vous</td></tr>
      </tbody>
      </table>
      <p class="note">La position de l'accueil passe de 6 à 30. Ce n'est pas une perte : ses clics montent de 67 à 82. Google l'affiche en plus, très bas, sur des noms d'autres agences et des villes que vous ne servez pas, héritage de l'ancienne page annuaire. Sur votre nom, la page reste en position 4 avec 20 clics. Rien à corriger.</p>
      <p class="note"><code>/bootcamp/</code> a été affichée 67 fois en juillet, 6 fois en août, 12 fois en septembre. La chute date de la dernière semaine de juillet. Les données ne disent pas pourquoi. À surveiller avant d'agir, et à rapprocher de la date de la dernière modification de la page.</p>
      <p class="note">Je n'ai pas de données sur les demandes ou les ventes. L'importance de chaque page est estimée d'après l'offre.</p>
    </div>

    <div class="card">
      <div class="card-head"><div><h3>Score SEO</h3><p class="sous">Chaque sujet part de 100. Seul un problème prouvé retire des points. Une cause compte une fois, pas une fois par page.</p></div></div>
      <p class="note">Score : 74/100. Plusieurs freins à corriger, aucun blocage. Confiance 83 % : plus basse sur la vitesse (données réelles à l'échelle du site seulement) et sur le contenu (recherches non disponibles pour 3 pages sur 5).</p>
      <table>
      <thead><tr><th>Sujet</th><th class="num" style="width:14%">Score</th><th class="num" style="width:12%">Poids</th><th class="num" style="width:16%">Contribution</th><th class="num" style="width:16%">Confiance</th></tr></thead>
      <tbody>
      <tr><td>Indexation</td><td class="num">63""" + aide("100 − 25 − 12 = 63. Deux problèmes : 8 pages du sitemap non indexées dont 2 pages d'offre (−25) ; 76 anciennes adresses redirigées vers /systeme/, une page sans rapport (−12). Pas de points retirés pour l'écart sitemap / adresses affichées ni pour le compteur « 0 indexée » (champ obsolète de l'API).") + """</td><td class="num">30 %</td><td class="num">18,9</td><td class="num">95 %""" + aide("30 pages inspectées dans Google, 30 contrôles techniques, code comparé avant et après JavaScript sur les 5 pages, 103 anciennes adresses contrôlées. Il manque : les alertes de sécurité et la cause exacte de la non-indexation.") + """</td></tr>
      <tr><td>Vitesse</td><td class="num">88""" + aide("100 − 12 = 88. Un problème : l'accueil dépasse 4 s en test sur deux passages (5,72 s et 4,01 s). Pas plus lourd parce que vos visiteurs réels mesurent 2,20 s à l'échelle du site.") + """</td><td class="num">20 %</td><td class="num">17,6</td><td class="num">70 %""" + aide("Les données réelles ne sont pas disponibles page par page, la réactivité n'est pas mesurable, et 1,7 s d'écart entre deux passages de test sur l'accueil.") + """</td></tr>
      <tr><td>Contenu</td><td class="num">71""" + aide("100 − 12 − 12 − 5 = 71. /methode/ et /systeme/ racontent la même offre (−12) ; des chiffres qui diffèrent entre pages et des affirmations du bootcamp sans appui (−12) ; titre et description de /bootcamp/ datés d'aujourd'hui (−5).") + """</td><td class="num">20 %</td><td class="num">14,2</td><td class="num">75 %""" + aide("Les 5 pages lues en entier. Mais les recherches de 3 pages sur 5 ne remontent pas, et les résultats Google ont été lus depuis les États-Unis.") + """</td></tr>
      <tr><td>Liens internes</td><td class="num">58""" + aide("100 − 25 − 12 − 5 = 58. /audit-seo/ sans aucun lien (−25) ; /bootcamp/ avec un seul lien et un menu qui envoie vers la candidature (−12) ; 6 liens sur 8 vers /methode/ avec le même texte (−5).") + """</td><td class="num">15 %</td><td class="num">8,7</td><td class="num">85 %""" + aide("Les liens des 30 pages du sitemap lus en entier. Il manque les liens venant des anciennes adresses.") + """</td></tr>
      <tr><td>Structure des titres</td><td class="num">100""" + aide("Rien à retirer : un titre principal unique et une hiérarchie complète sur les 30 pages.") + """</td><td class="num">10 %</td><td class="num">10,0</td><td class="num">90 %""" + aide("Titres relevés sur les 30 pages, identiques avant et après JavaScript.") + """</td></tr>
      <tr><td>Données structurées</td><td class="num">100""" + aide("Rien à retirer : balisage valide sur les 5 pages. Observations sans pénalité : slogan balisé différent du slogan affiché, rien de propre à chaque page.") + """</td><td class="num">5 %</td><td class="num">5,0</td><td class="num">80 %""" + aide("Validité et correspondance avec le contenu contrôlées sur les 5 pages. Pas de passage au test des résultats enrichis de Google.") + """</td></tr>
      <tr><td class="strong">Global</td><td></td><td></td><td class="num strong">74""" + aide("18,9 + 17,6 + 14,2 + 8,7 + 10,0 + 5,0 = 74,4, arrondi à 74. Aucun plafond : pas de blocage d'indexation généralisé, ni d'accueil ou de page d'offre majeure bloquée.") + """</td><td class="num strong">83 %""" + aide("95 × 0,30 + 70 × 0,20 + 75 × 0,20 + 85 × 0,15 + 90 × 0,10 + 80 × 0,05 = 83,25. La confiance dit à quel point les preuves couvrent le sujet, pas la qualité du site.") + """</td></tr>
      </tbody>
      </table>
    </div>

    <div class="card">
      <div class="card-head"><div><h3>Où en est chaque sujet</h3></div></div>
      <table>
      <thead><tr><th>Sujet</th><th style="width:22%">État</th><th style="width:48%">En une phrase</th></tr></thead>
      <tbody>
      <tr><td>Liens internes</td><td><span class="etat e-crit">Critique</span></td><td>les pages d'offre ne reçoivent presque aucun lien</td></tr>
      <tr><td>Contenu</td><td><span class="etat e-ame">À améliorer</span></td><td>deux pages d'offre disent la même chose, des chiffres diffèrent d'une page à l'autre</td></tr>
      <tr><td>Vitesse</td><td><span class="etat e-ame">À améliorer</span></td><td>bonne chez vos visiteurs, accueil lente en test</td></tr>
      <tr><td>Mots-clés business</td><td><span class="etat e-ame">Diagnostic partiel</span></td><td>une seule recherche d'offre visible, sans clic</td></tr>
      <tr><td>Indexation</td><td><span class="etat e-ame">À améliorer</span></td><td>les 5 pages sont indexées ; 8 pages du sitemap ne le sont pas</td></tr>
      <tr><td>Structure des titres</td><td><span class="etat e-ok">Rien à signaler</span></td><td>un titre principal par page, hiérarchie complète</td></tr>
      <tr><td>Données structurées</td><td><span class="etat e-ok">Rien à signaler</span></td><td>balisage valide, le même partout</td></tr>
      </tbody>
      </table>
    </div>

    <div class="card">
      <div class="card-head"><div><h3>À faire maintenant</h3></div></div>
      <p class="note"><b>1. Ajouter des liens vers les pages Audit SEO et Bootcamp.</b></p>
      <p class="note">Sur les 30 pages du site, aucune ne contient de lien vers <code>/audit-seo/</code>. Pourtant, la page <code>/methode/</code> présente déjà l'audit comme la première étape de l'accompagnement : c'est un endroit logique pour proposer au lecteur de découvrir cette offre. Pour le Bootcamp, le seul lien vers <code>/bootcamp/</code> vient du plan du site, et le menu « Bootcamp », présent sur 26 pages, envoie directement vers la candidature sans passer par la page de présentation.</p>
      <p class="note">Je recommande donc d'ajouter un lien vers l'audit depuis <code>/methode/</code> et <code>/systeme/</code>, puis de faire pointer le menu vers <code>/bootcamp/</code>. Ces modifications peuvent être faites dès maintenant. Une fois les liens ajoutés, on relancera le crawl pour vérifier qu'ils pointent bien vers les bonnes pages.</p>
      <p class="note"><b>2. Comprendre pourquoi /methode/ et /systeme/ apparaissent sans être cliquées.</b></p>
      <p class="note">Ces deux pages ont été affichées 91 et 56 fois en 90 jours, en position 5 et 6, sans un clic. Même chose sur les 90 jours précédents. Les recherches sur lesquelles elles apparaissent ne remontent pas dans les données, et si Google les a anonymisées, l'interface Search Console ne les montrera pas non plus.</p>
      <p class="note">On peut déjà donner un rôle clair à chaque page : l'une explique la méthode, l'autre présente l'offre. Pour le reste, il faut d'abord savoir sur quelles recherches elles apparaissent. Pas de fusion ni de réécriture des titres avant ça. Après modification, on comparera les clics des 28 jours suivants aux 28 jours précédents.</p>
      <p class="note"><b>3. Aligner les chiffres d'une page à l'autre.</b></p>
      <p class="note">Le site annonce « 100+ entreprises accompagnées » sur <code>/methode/</code> et <code>/systeme/</code>, et « 14 missions B2B » sur <code>/resultats/</code>. Il annonce « 1 000 articles de blog » sur l'accueil et « +2 000 contenus produits » sur <code>/systeme/</code>. Ces chiffres ne sont pas forcément contradictoires, mais un lecteur qui compare les pages ne sait pas ce que chacun recouvre.</p>
      <p class="note">Sur <code>/bootcamp/</code>, « jusqu'à 25 h par mois », « 80 % de l'opérationnel » et « 5,0 / 5 sur 5 avis vérifiés » sont affirmés sans exemple ni lien vers les avis. Un exemple concret (une tâche, le temps avant, le temps après) et un lien vers les avis suffiraient.</p>
      <p class="note">Je recommande de vérifier ce que recouvre chaque chiffre, puis de l'écrire de la même façon partout. C'est rapide dès que les valeurs exactes sont en main.</p>
    </div>

    <div class="card">
      <div class="card-head"><div><h3>Ce qui pèse le plus sur le score</h3></div></div>
      <ul class="barres">
        <li><span class="nom">/audit-seo/ n'a aucun lien vers elle<span>Liens internes</span></span><span class="jauge"><i style="width:100%"></i></span><span class="n">−25""" + aide("Aucun chemin vers cette page depuis le site, ni dans le texte ni dans le menu. Une seule page, mais celle qui recueille l'adresse d'un site à auditer.", True) + """</span></li>
        <li><span class="nom">8 pages du sitemap non indexées, dont 2 pages d'offre<span>Indexation</span></span><span class="jauge"><i style="width:100%"></i></span><span class="n">−25""" + aide("7 pages détectées mais non indexées et 1 inconnue de Google, sur 30. Aucun affichage sur ces 8. Les versions FR/EN qui répondent différemment comptent comme une cause de ce problème, pas comme un second.", True) + """</span></li>
        <li><span class="nom">/bootcamp/ reçoit un seul lien, le menu envoie vers la candidature<span>Liens internes</span></span><span class="jauge"><i style="width:48%"></i></span><span class="n">−12""" + aide("La page qui apparaît sur « bootcamp seo » reçoit un lien dans le texte. Le menu envoie 26 pages vers la candidature. La page reste indexée et atteignable.", True) + """</span></li>
        <li><span class="nom">/methode/ et /systeme/ racontent la même offre<span>Contenu</span></span><span class="jauge"><i style="width:48%"></i></span><span class="n">−12""" + aide("Deux pages d'offre qui décrivent la même chose, 0 clic sur 147 affichages. Leurs recherches ne remontent pas : la part du recouvrement dans l'absence de clic reste une hypothèse.", True) + """</span></li>
        <li><span class="nom">des chiffres qui diffèrent entre pages, des affirmations sans appui<span>Contenu</span></span><span class="jauge"><i style="width:48%"></i></span><span class="n">−12""" + aide("Deux paires de chiffres à vérifier et trois affirmations du bootcamp sans appui. Une seule cause comptée.", True) + """</span></li>
        <li><span class="nom">l'accueil au-dessus de 4 s en test<span>Vitesse</span></span><span class="jauge"><i style="width:48%"></i></span><span class="n">−12""" + aide("Deux passages à 5,72 s et 4,01 s. Le temps se perd dans l'image du bandeau et la réponse du serveur. Vos visiteurs réels mesurent 2,20 s à l'échelle du site.", True) + """</span></li>
        <li><span class="nom">76 anciennes adresses redirigées vers /systeme/<span>Indexation</span></span><span class="jauge"><i style="width:48%"></i></span><span class="n">−12""" + aide("76 adresses d'articles retirés (glossaire, guides, newsletter, wiki…) renvoient vers la page d'offre. Google recommande de rediriger vers la page qui remplace le contenu, sinon de répondre « introuvable ».", True) + """</span></li>
      </ul>
    </div>

    <div class="card">
      <div class="card-head"><div><h3>Ce que chaque étape a donné</h3></div></div>
      <table>
      <thead><tr><th>Étape</th><th style="width:22%">Résultat</th><th style="width:50%">Où le lire</th></tr></thead>
      <tbody>
      <tr><td>Ce que le site vise</td><td><span class="etat e-ame">Diagnostic partiel</span></td><td>onglet Mots-clés business</td></tr>
      <tr><td>Indexation</td><td><span class="etat e-ok">Résultats</span></td><td>onglet Indexation ; pénalités manuelles et alertes de sécurité non vérifiées, elles demandent l'interface Search Console</td></tr>
      <tr><td>Vitesse</td><td><span class="etat e-ok">Résultats</span></td><td>onglet Vitesse</td></tr>
      <tr><td>Gains rapides</td><td><span class="etat e-ame">Aucun retenu</span></td><td>deux pages apparaissent sans clic (/methode/, /systeme/) : à comprendre avant de toucher aux titres</td></tr>
      <tr><td>Contenu et titres</td><td><span class="etat e-ok">Résultats</span></td><td>onglet Contenu et pertinence</td></tr>
      <tr><td>Pages qui se marchent dessus</td><td><span class="etat e-ok">Aucun conflit prouvé</span></td><td>/methode/ et /systeme/ à distinguer ; /audit-seo/ et /audit/ à vérifier</td></tr>
      <tr><td>Liens internes</td><td><span class="etat e-ok">Résultats</span></td><td>onglet Liens internes</td></tr>
      <tr><td>Synthèse et score</td><td><span class="etat e-ok">Résultats</span></td><td>ce résumé</td></tr>
      </tbody>
      </table>
      <p class="note">Deux analyses complémentaires restent à faire : la présence locale (le site cite Lyon, votre fiche Google Business Profile n'a pas été vérifiée) et les versions FR/EN (2 pages en anglais au sitemap, balises de langue non contrôlées). Les liens que d'autres sites vous font n'ont pas été regardés.</p>
    </div>

    <div class="card">
      <div class="card-head"><div><h3>Ce que je ne sais pas</h3></div></div>
      <p class="note">Sur quelles recherches apparaissent <code>/methode/</code>, <code>/systeme/</code> et <code>/audit-seo/</code>. Elles ne remontent pas dans les données. Je ne toucherai pas à leurs titres sans les connaître.</p>
      <p class="note">Ce que ces pages vous rapportent en demandes ou en ventes. Je n'ai reçu aucune donnée (GA4, CRM, formulaire).</p>
      <p class="note">Le poids des liens que d'autres sites vous font. La position 28 de <code>/bootcamp/</code> sur « bootcamp seo » peut venir du contenu, des liens internes ou des sites qui vous précèdent.</p>
      <p class="note">Les 25 autres pages du sitemap ont été inspectées, pas lues. Les résultats Google ont été lus depuis les États-Unis : ce qu'un internaute voit en France peut différer.</p>
    </div>

  </div>
</div>
"""

# ═══ 2. INDEXATION ════════════════════════════════════════════════════════════
V[2] = """
<h2>Indexation : 8 pages du sitemap ne sont pas indexées, dont 2 pages d'offre</h2>
<p>Dans l'ensemble, l'indexation du site est bonne. Sur les 30 pages présentes dans le sitemap, 22 sont indexées.</p>
<p>Aucun problème technique ne bloque Google : les 30 pages répondent correctement, aucune n'est bloquée par le robots.txt, et les 5 pages analysées en détail sont indexées et lues telles que vos visiteurs les voient.</p>
<p>Le problème concerne surtout 8 pages du sitemap qui ne sont toujours pas indexées. Deux sont des pages d'offre, donc je commencerais par celles-ci.</p>
<p>Il y a aussi un problème à corriger sur les versions FR/EN : 3 pages ne répondent pas de la même manière selon la langue du navigateur.</p>
<p>Enfin, 76 anciennes adresses redirigent aujourd'hui vers une page d'offre sans rapport avec leur ancien contenu. Il faudra revoir ces redirections plutôt que de toutes les envoyer au même endroit.</p>

<h3>À faire</h3>
<ol>
<li>Vérifier pourquoi les 2 pages d'offre ne sont pas indexées et les traiter en priorité.</li>
<li>Corriger le comportement des versions FR/EN.</li>
<li>Reprendre les 76 anciennes adresses et décider lesquelles doivent être redirigées, supprimées ou conservées.</li>
</ol>
<p>Sur les 30 pages du sitemap, 22 sont donc correctement indexées. Le problème existe, mais il est concentré sur quelques groupes de pages bien identifiés.</p>

<h3>Les 8 pages non indexées</h3>
<p>Les cas ne sont pas les mêmes. Les données permettent déjà de les séparer.</p>
<div class="tablewrap"><table>
<thead><tr><th>Page</th><th>Rôle</th><th>Ce qu'on observe</th><th>Ce que je ferais</th></tr></thead>
<tbody>
<tr><td class="mono">/formation-seo-ia/</td><td>offre</td><td>aucun lien vers elle</td><td>ajouter des liens depuis les pages d'offre indexées, puis demander une nouvelle inspection</td></tr>
<tr><td class="mono">/consultant-seo-geo-lyon/</td><td>offre</td><td>un seul lien, depuis le plan du site</td><td>la relier depuis l'accueil, /methode/ et /a-propos/, puis réinspecter</td></tr>
<tr><td class="mono">/bootcamp/programme/</td><td>offre, page fille</td><td>un lien depuis /bootcamp/ ; Google ne la connaît plus</td><td>la relier aussi depuis la candidature, puis réinspecter</td></tr>
<tr><td class="mono">/bootcamp-quiz/</td><td>page fille</td><td>un lien depuis /bootcamp/</td><td>idem</td></tr>
<tr><td class="mono">/accompagnement-1-1-30-jours/</td><td>offre</td><td>12 liens depuis 10 pages, et pourtant non indexée</td><td>les liens ne sont pas en cause. Vérifier si Google la voit comme un doublon de <code>/coaching-seo-lyon/</code>, indexée, sur le même sujet</td></tr>
<tr><td class="mono">/en/agent-seo/</td><td>version anglaise</td><td>aucun lien ; renvoie vers la version française quand le navigateur est en français</td><td>voir les versions FR/EN</td></tr>
<tr><td class="mono">/guides/audit-seo-technique-claude.html</td><td>guide</td><td>aucun lien ; renvoie vers la version anglaise quand le navigateur est en anglais</td><td>voir les versions FR/EN</td></tr>
<tr><td class="mono">/guides/en/audit-seo-technique-claude.html</td><td>guide, version anglaise</td><td>aucun lien ; renvoie vers la version française quand le navigateur est en français</td><td>voir les versions FR/EN</td></tr>
</tbody></table></div>
<p>Ces huit pages répondent normalement et n'interdisent rien à Google. Elles n'ont simplement reçu aucun affichage sur la période. Pour <code>/bootcamp/programme/</code>, Google la connaissait encore le 26/09 ; le 28, il ne la connaît plus.</p>
<p>Les liens peuvent être ajoutés tout de suite. On demandera ensuite une nouvelle inspection et on saura dans trois semaines si le statut a bougé. S'il ne bouge pas, on cherchera ailleurs : contenu, doublon entre versions, gabarit.</p>

<h3>Les versions FR/EN</h3>
<p>Quand on ouvre <code>/agent-seo/</code> avec un navigateur en anglais, le site renvoie vers <code>/en/agent-seo/</code>. Quand on ouvre <code>/en/agent-seo/</code> en français, il renvoie vers <code>/agent-seo/</code>. Les deux guides font la même chose. Les autres pages testées répondent toujours pareil.</p>
<p>Google reçoit donc une réponse différente pour la même adresse selon la langue de sa requête. Il peut ne voir une version que comme une redirection. Google déconseille cette redirection automatique : chaque version doit rester accessible, reliées entre elles par les balises de langue. Les trois pages non indexées de ce lot sont exactement les trois versions concernées.</p>
<p>Je recommande de servir chaque version dans sa langue, quel que soit le navigateur, et de proposer le changement de langue dans la page. C'est une modification de configuration du site : on la décide ensemble avant de la faire.</p>

<h3>Les 76 anciennes adresses</h3>
<p>Sur les 103 anciennes adresses qui ont été affichées dans Google sur la période, 76 renvoient aujourd'hui vers <code>/systeme/</code> : glossaire, guides, newsletter, actualités, wiki. 19 répondent « page introuvable ». 6 sont encore en ligne. 2 renvoient vers une page qui reprend leur sujet.</p>
<p>Rediriger un ancien article de glossaire vers la page de l'offre ne donne pas au visiteur ce qu'il cherchait. Google recommande de rediriger seulement vers la page qui reprend le contenu, sinon de répondre « introuvable ». C'est aussi la règle du site. À noter, sans qu'on puisse relier les deux : <code>/systeme/</code> est passée de 12 à 56 affichages sans aucun clic.</p>
<p>Je recommande de répondre « introuvable » pour les contenus retirés sans équivalent, et de garder la redirection quand une page reprend vraiment le sujet, comme l'ancien article des skills vers <code>/skills/</code>. On décide ensemble avant de toucher quoi que ce soit.</p>

<h3>Ce qui ne pose pas de problème</h3>
<p>125 adresses ont été affichées dans Google sur la période, 23 seulement sont dans le sitemap. Cet écart n'est pas un problème d'indexation : la Search Console décrit ce qui s'est passé sur 90 jours, et la plupart de ces adresses sont d'anciens articles retirés depuis. Reste à décider quelles pages doivent figurer au sitemap : <code>/audit/</code>, <code>/tarifs/</code>, l'étude de cas et les PDF sont en ligne et n'y sont pas.</p>
<p>Le compteur « 30 envoyées, 0 indexée » vient d'un champ de l'API que Google déclare obsolète. Je ne l'utilise pas.</p>
<p>Deux anciens sitemaps erronés sont encore listés dans votre propriété (<code>/sitemap</code>, <code>/sitemap.%20xml</code>). À retirer par propreté, sans effet sur l'indexation.</p>
<p class="note">Les pénalités manuelles et les alertes de sécurité n'ont pas été vérifiées : il faut ouvrir les rapports correspondants dans l'interface Search Console. Les anciennes adresses n'ont pas été inspectées dans Google, sauf trois.</p>

<details class="repli"><summary>Le détail · ce que Google dit de chacune des 30 pages du sitemap</summary>
<div class="tablewrap"><table>
<thead><tr><th>Page</th><th>Verdict Google</th><th>Dernier passage</th><th>Sitemap signalé</th><th>Pages référentes renseignées</th></tr></thead>
<tbody>
<tr><td class="mono">/</td><td><span class="etat e-ok">Indexée</span></td><td>28/09/2026</td><td>non renseigné</td><td>/bootcamp, /accompagnement</td></tr>
<tr><td class="mono">/methode/</td><td><span class="etat e-ok">Indexée</span></td><td>21/08/2026</td><td>oui</td><td>sitemap.xml</td></tr>
<tr><td class="mono">/systeme/</td><td><span class="etat e-ok">Indexée</span></td><td>24/09/2026</td><td>oui</td><td>/systeme</td></tr>
<tr><td class="mono">/bootcamp/</td><td><span class="etat e-ok">Indexée</span></td><td>20/08/2026</td><td>oui</td><td>sitemap.xml</td></tr>
<tr><td class="mono">/audit-seo/</td><td><span class="etat e-ok">Indexée</span></td><td>23/09/2026</td><td>oui</td><td>aucune renseignée</td></tr>
<tr><td class="mono">/etudes-de-cas/</td><td><span class="etat e-ok">Indexée</span></td><td>11/09/2026</td><td>oui</td><td>aucune renseignée</td></tr>
<tr><td class="mono">/chaine-youtube-seo/</td><td><span class="etat e-ok">Indexée</span></td><td>21/08/2026</td><td>oui</td><td>aucune renseignée</td></tr>
<tr><td class="mono">/contact/</td><td><span class="etat e-ok">Indexée</span></td><td>20/09/2026</td><td>oui</td><td>aucune renseignée</td></tr>
<tr><td class="mono">/resultats/</td><td><span class="etat e-ok">Indexée</span></td><td>27/07/2026</td><td>oui</td><td>/plan-du-site/</td></tr>
<tr><td class="mono">/guides/</td><td><span class="etat e-ok">Indexée</span></td><td>29/08/2026</td><td>non renseigné</td><td>/guides</td></tr>
<tr><td class="mono">/avis/</td><td><span class="etat e-ok">Indexée</span></td><td>21/08/2026</td><td>oui</td><td>aucune renseignée</td></tr>
<tr><td class="mono">/plan-du-site/</td><td><span class="etat e-ok">Indexée</span></td><td>20/08/2026</td><td>non renseigné</td><td>aucune renseignée</td></tr>
<tr><td class="mono">/accompagnement-seo-geo/</td><td><span class="etat e-ok">Indexée</span></td><td>06/07/2026</td><td>oui</td><td>aucune renseignée</td></tr>
<tr><td class="mono">/accompagnement-1-1-30-jours/</td><td><span class="etat e-crit">Détectée, non indexée</span></td><td>aucun</td><td>oui</td><td>/blog/</td></tr>
<tr><td class="mono">/consultant-lead-seo/</td><td><span class="etat e-ok">Indexée</span></td><td>27/08/2026</td><td>oui</td><td>aucune renseignée</td></tr>
<tr><td class="mono">/consultant-geo/</td><td><span class="etat e-ok">Indexée</span></td><td>30/08/2026</td><td>oui</td><td>aucune renseignée</td></tr>
<tr><td class="mono">/consultant-seo-geo-lyon/</td><td><span class="etat e-crit">Détectée, non indexée</span></td><td>aucun</td><td>oui</td><td>aucune renseignée</td></tr>
<tr><td class="mono">/formation-seo-ia/</td><td><span class="etat e-crit">Détectée, non indexée</span></td><td>aucun</td><td>oui</td><td>aucune renseignée</td></tr>
<tr><td class="mono">/bootcamp/programme/</td><td><span class="etat e-crit">Inconnue de Google</span></td><td>aucun</td><td>non renseigné</td><td>aucune renseignée</td></tr>
<tr><td class="mono">/bootcamp-quiz/</td><td><span class="etat e-crit">Détectée, non indexée</span></td><td>aucun</td><td>oui</td><td>/guides/de-0-a-1-seo-claude.pdf</td></tr>
<tr><td class="mono">/skills/</td><td><span class="etat e-ok">Indexée</span></td><td>10/09/2026</td><td>non renseigné</td><td>aucune renseignée</td></tr>
<tr><td class="mono">/coaching-seo-lyon/</td><td><span class="etat e-ok">Indexée</span></td><td>21/09/2026</td><td>oui</td><td>/coaching-seo-lyon, sitemap.xml</td></tr>
<tr><td class="mono">/a-propos/</td><td><span class="etat e-ok">Indexée</span></td><td>27/09/2026</td><td>oui</td><td>aucune renseignée</td></tr>
<tr><td class="mono">/bootcamp-candidature/</td><td><span class="etat e-ok">Indexée</span></td><td>28/09/2026</td><td>oui</td><td>aucune renseignée</td></tr>
<tr><td class="mono">/mentions-legales/</td><td><span class="etat e-ok">Indexée</span></td><td>11/09/2026</td><td>oui</td><td>sitemap.xml</td></tr>
<tr><td class="mono">/politique-confidentialite/</td><td><span class="etat e-ok">Indexée</span></td><td>11/09/2026</td><td>oui</td><td>sitemap.xml</td></tr>
<tr><td class="mono">/agent-seo/</td><td><span class="etat e-ok">Indexée</span></td><td>18/09/2026</td><td>oui</td><td>aucune renseignée</td></tr>
<tr><td class="mono">/en/agent-seo/</td><td><span class="etat e-crit">Détectée, non indexée</span></td><td>aucun</td><td>oui</td><td>/agent-seo/</td></tr>
<tr><td class="mono">/guides/audit-seo-technique-claude.html</td><td><span class="etat e-crit">Détectée, non indexée</span></td><td>aucun</td><td>oui</td><td>aucune renseignée</td></tr>
<tr><td class="mono">/guides/en/audit-seo-technique-claude.html</td><td><span class="etat e-crit">Détectée, non indexée</span></td><td>aucun</td><td>oui</td><td>aucune renseignée</td></tr>
</tbody></table></div>
<p class="note">Google donne l'état de la version qu'il connaît, à la date de son dernier passage. « Aucune renseignée » ne veut pas dire qu'aucune page ne mène à celle-ci : Google ne remplit cette information que parfois. Le vrai nombre de liens est dans l'onglet Liens internes. Trois anciennes adresses ont aussi été inspectées : <code>/blog/9-skills-seo-claude/</code> indexée (aujourd'hui redirigée vers /skills/), <code>/audit/</code> indexée, <code>/wiki/</code> indexée (aujourd'hui redirigée vers /systeme/).</p>
</details>

<details class="repli"><summary>Le détail · contrôles techniques</summary>
<div class="tablewrap"><table><tbody>
<tr><td class="strong">Réponse des pages</td><td>les 30 pages répondent normalement, sans redirection</td></tr>
<tr><td class="strong">Interdictions à Google</td><td>aucune balise ni en-tête noindex</td></tr>
<tr><td class="strong">robots.txt</td><td>aucune interdiction ; Google confirme l'accès sur les 22 pages indexées</td></tr>
<tr><td class="strong">Adresse de référence (canonical)</td><td>les 5 pages se désignent elles-mêmes, avant comme après JavaScript, et Google a retenu la même adresse</td></tr>
<tr><td class="strong">Pages inexistantes</td><td>3 adresses inventées renvoient bien « introuvable »</td></tr>
<tr><td class="strong">Sitemap</td><td>30 adresses, aucune redirigée, lu par Google le 26/09/2026</td></tr>
</tbody></table></div>
</details>

<details class="repli"><summary>Le détail · ce que Google lit de chaque page (5 pages)</summary>
<p>J'ai comparé le code que le serveur envoie et la page une fois le JavaScript exécuté. La comparaison porte sur le texte principal et sur la destination de chaque lien du texte.</p>
<div class="tablewrap"><table>
<thead><tr><th>Page</th><th>Texte principal</th><th>Liens du texte</th><th>Titre</th><th>Directives</th><th>Adresse de référence</th></tr></thead>
<tbody>
<tr><td class="mono">/</td><td>identique</td><td>identiques (2)</td><td>identique</td><td>identiques</td><td>identique</td></tr>
<tr><td class="mono">/methode/</td><td>identique</td><td>identiques (3)</td><td>identique</td><td>identiques</td><td>identique</td></tr>
<tr><td class="mono">/systeme/</td><td>identique</td><td>identiques (2)</td><td>identique</td><td>identiques</td><td>identique</td></tr>
<tr><td class="mono">/bootcamp/</td><td>identique</td><td>identiques (3)</td><td>identique</td><td>identiques</td><td>identique</td></tr>
<tr><td class="mono">/audit-seo/</td><td>identique</td><td>identiques (0)</td><td>identique</td><td>identiques</td><td>identique</td></tr>
</tbody></table></div>
<p class="note">Rien ne change après JavaScript sur ces cinq pages. Les cinq répondent aussi pareil en français et en anglais.</p>
</details>

<details class="repli"><summary>Le détail · les 103 anciennes adresses, état au 28/09/2026</summary>
<div class="tablewrap"><table>
<thead><tr><th>État aujourd'hui</th><th class="num">Adresses</th><th>Familles</th></tr></thead>
<tbody>
<tr><td>redirigées vers <code>/systeme/</code></td><td class="num">76</td><td>glossaire, guide des évaluateurs Google, statuts d'indexation, mises à jour Google, newsletter, stratégies, secteurs, actualités, statistiques, services, wiki, robots-ia</td></tr>
<tr><td>« introuvable »</td><td class="num">19</td><td>blog (index et 11 articles), outils, manifeste</td></tr>
<tr><td>encore en ligne</td><td class="num">6</td><td>3 PDF de guides, <code>/audit/</code>, <code>/etudes-de-cas/appart-hotel/</code>, <code>/tarifs/</code></td></tr>
<tr><td>redirigées vers une page de même sujet</td><td class="num">2</td><td><code>/blog/9-skills-seo-claude/</code> → <code>/skills/</code> ; <code>/agences-seo-b2b-ethique/</code> → <code>/accompagnement-seo-geo/</code></td></tr>
</tbody></table></div>
</details>
"""

# ═══ 3. LIENS INTERNES ════════════════════════════════════════════════════════
V[3] = """
<h2>Liens internes : vos pages d'offre ne reçoivent presque aucun lien</h2>
<p>Le site fait 284 liens internes sur ses 30 pages. Seuls 64 sont placés dans le texte ; les autres sont dans le menu ou le pied de page. Et sur ces 64, très peu mènent aux pages qui vendent.</p>
<p><code>/audit-seo/</code> ne reçoit aucun lien, ni dans le texte ni dans le menu. Elle ne mène nulle part non plus. Un visiteur n'a aucun chemin vers l'outil.</p>
<p><code>/bootcamp/</code> reçoit un seul lien dans le texte, depuis le plan du site. Le menu « Bootcamp », présent sur 26 pages, envoie vers le formulaire de candidature au lieu de la page de présentation. C'est pourtant <code>/bootcamp/</code> qui apparaît dans Google sur « bootcamp seo ».</p>
<p><code>/methode/</code> est la page la mieux reliée : 8 liens, mais 6 portent le même texte, « Voir la méthode ».</p>
<p>Plus largement, 12 pages sur 30 ne reçoivent aucun lien dans le texte, dont <code>/formation-seo-ia/</code>, <code>/accompagnement-seo-geo/</code>, <code>/consultant-lead-seo/</code>, <code>/skills/</code>. Cinq des huit pages que Google n'indexe pas sont dans ce lot.</p>

<h3>À faire</h3>
<ol>
<li>Ajouter un lien vers <code>/audit-seo/</code> depuis <code>/methode/</code> (étape « Audit »), <code>/systeme/</code> (« On commence par regarder l'existant ») et l'accueil. Un texte différent à chaque fois : « lancer l'audit de votre site », « voir votre site sous tous les angles ».</li>
<li>Faire pointer le menu « Bootcamp » vers <code>/bootcamp/</code>, et proposer la candidature depuis cette page. Une modification, 26 pages corrigées.</li>
<li>Varier les textes des liens vers <code>/methode/</code> au fil des prochaines mises à jour : « la méthode en 4 étapes », « comment se déroulent les 6 mois ». Pas urgent.</li>
</ol>
<p>Les deux premiers points se font tout de suite. On relancera ensuite le crawl pour vérifier que les liens sont en place.</p>

<h3>Ce que reçoivent les 5 pages</h3>
<div class="tablewrap"><table>
<thead><tr><th>Page</th><th class="num">Liens dans le texte</th><th class="num">Pages d'origine</th><th>Textes des liens</th><th class="num">Liens de menu</th><th class="num">Liens qu'elle fait</th></tr></thead>
<tbody>
<tr><td class="mono">/</td><td class="num">0</td><td class="num">0</td><td>aucun</td><td class="num">53 (27 pages)</td><td class="num">4</td></tr>
<tr><td class="mono">/methode/</td><td class="num">8</td><td class="num">8</td><td>« Voir la méthode » ×6, « détaillée ici », « Méthode »</td><td class="num">1</td><td class="num">3</td></tr>
<tr><td class="mono">/systeme/</td><td class="num">2</td><td class="num">2</td><td>« Voir le système », « Services »</td><td class="num">0</td><td class="num">2</td></tr>
<tr><td class="mono">/bootcamp/</td><td class="num">1</td><td class="num">1</td><td>« Bootcamp » (plan du site)</td><td class="num">1</td><td class="num">3</td></tr>
<tr><td class="mono">/audit-seo/</td><td class="num">0</td><td class="num">0</td><td>aucun</td><td class="num">0</td><td class="num">0</td></tr>
</tbody></table></div>
<p class="note">Que l'accueil ne reçoive aucun lien dans le texte est normal : le menu s'en charge. Les pages légales ne sont pas comptées comme un problème.</p>

<h3>Ce que la Search Console ajoute</h3>
<p>Google ne cite comme page référente que le sitemap pour <code>/methode/</code> et <code>/bootcamp/</code>, et rien pour <code>/audit-seo/</code>. Pour <code>/methode/</code>, les 8 liens existent bien : Google n'en avait retenu aucun lors de son dernier passage, le 21/08. Sur 90 jours contre 90, <code>/bootcamp/</code> recule (108 → 85 affichages, position 11 → 29), <code>/systeme/</code> monte (12 → 56), <code>/methode/</code> est stable.</p>
<p class="note">Je n'ai pas lu les liens venant des anciennes adresses hors sitemap. Et ces chiffres ne disent pas quelle part les liens internes prennent dans la position 28 de <code>/bootcamp/</code>.</p>
"""

# ═══ 4. CONTENU ET PERTINENCE ═════════════════════════════════════════════════
V[4] = """
<h2>Contenu : deux pages d'offre disent la même chose, et des chiffres diffèrent d'une page à l'autre</h2>
<p>Deux pages sur cinq n'ont rien à corriger : l'accueil et <code>/audit-seo/</code>.</p>
<p>Le principal problème, c'est que <code>/methode/</code> et <code>/systeme/</code> racontent la même offre. Un accompagnement par étapes sur 6 mois, en 4 étapes d'un côté et 3 de l'autre, avec les mêmes chiffres. Chacune renvoie vers l'autre. Dans Google, elles apparaissent 91 et 56 fois en 90 jours, en position 5 et 6, sans un clic. Un lecteur qui compare ne sait pas laquelle lire.</p>
<p>Ensuite, des chiffres diffèrent selon la page. « 100+ entreprises accompagnées » sur <code>/methode/</code> et <code>/systeme/</code>, « 14 missions B2B » sur <code>/resultats/</code>. « 1 000 articles de blog » sur l'accueil, « +2 000 contenus produits » sur <code>/systeme/</code>. Ce n'est pas forcément contradictoire, mais le lecteur ne sait pas ce que chaque chiffre recouvre.</p>
<p>Sur <code>/bootcamp/</code>, trois affirmations n'ont pas d'appui : « jusqu'à 25 h par mois », « 80 % de l'opérationnel », « 5,0 / 5 sur 5 avis vérifiés ». Pas d'exemple, pas de lien vers les avis.</p>
<p>Enfin, le titre de <code>/bootcamp/</code> dans Google dit « 10 places » et sa description « démarrage le 28 septembre 2026 », c'est-à-dire aujourd'hui. Dès demain, Google affichera une session déjà commencée. Il ne repasse pas tous les jours sur cette page : dernier passage le 20/08.</p>

<h3>À faire</h3>
<ol>
<li>Donner un rôle distinct à <code>/methode/</code> et <code>/systeme/</code> : une page qui explique la méthode, une page qui vend l'offre avec son déroulé, son prix ou sa fourchette, et comment démarrer. Pas de fusion ni de redirection : rien ne montre que ces pages se pénalisent dans Google, et on ne connaît pas leurs recherches.</li>
<li>Vérifier ce que recouvre chaque chiffre, puis l'écrire pareil sur toutes les pages. Pour le bootcamp, remplacer « jusqu'à 25 h » par un exemple concret (une tâche, le temps avant, le temps après) et relier les avis.</li>
<li>Retirer la date et le nombre de places du titre et de la description de <code>/bootcamp/</code>. Les garder dans le corps de la page. Quelques minutes.</li>
</ol>

<h3>Page par page</h3>
<div class="tablewrap"><table>
<thead><tr><th>Page</th><th>Ce que Google affiche sur la recherche visée</th><th>La page</th><th>Question sans réponse</th><th>Affirmations sans appui</th><th>Apporte quelque chose de propre ?</th><th>Titre / description</th><th>Verdict</th></tr></thead>
<tbody>
<tr><td class="mono">/</td><td>votre nom : Google attend le site lui-même</td><td>offre, 884 mots</td><td>aucune</td><td>« 7+ ans d'XP », « 1 000 articles » : cohérents avec l'à-propos, non sourcés</td><td>oui, la seule qui montre le parcours complet</td><td>clairs</td><td><span class="etat e-ok">Rien à corriger</span></td></tr>
<tr><td class="mono">/methode/</td><td>recherches non disponibles</td><td>méthode, 1 547 mots</td><td>le prix : la page parle de « coût par lead » sans en donner</td><td>« 100+ entreprises »</td><td>peu, face à /systeme/</td><td>clairs</td><td><span class="etat e-ame">À améliorer</span></td></tr>
<tr><td class="mono">/systeme/</td><td>recherches non disponibles</td><td>offre, 380 mots</td><td>ce qui distingue « le système » de « la méthode »</td><td>« +2 000 contenus », « 100+ entreprises »</td><td>peu : reprend /methode/ en plus court</td><td>clairs</td><td><span class="etat e-ame">À améliorer</span></td></tr>
<tr><td class="mono">/bootcamp/</td><td>« bootcamp seo » : des pages de formation et de programme</td><td>présentation, 1 655 mots, bon format</td><td>le prix</td><td>« 25 h par mois », « 80 % », « 5,0 / 5 »</td><td>oui</td><td>datés d'aujourd'hui</td><td><span class="etat e-ame">À améliorer</span></td></tr>
<tr><td class="mono">/audit-seo/</td><td>« audit seo gratuit en ligne » : des outils</td><td>un outil, 47 mots, bon format</td><td>ce que couvre l'audit, et ce qui se passe après</td><td>aucune</td><td>à vérifier face à <code>/audit/</code> (18 affichages, hors sitemap)</td><td>clairs</td><td><span class="etat e-ok">Rien à corriger</span></td></tr>
</tbody></table></div>
<p class="note">Résultats Google lus depuis les États-Unis sur 3 recherches. Les recherches de 3 pages sur 5 ne remontent pas.</p>

<h3>Ce que je n'ai pas retenu</h3>
<p>Le titre principal de l'accueil est un slogan (« Des leads, pas du trafic. »). La ligne suivante dit ce que fait le site. La page se comprend.</p>
<p><code>/audit-seo/</code> fait 47 mots. C'est un outil, le nombre de mots n'est pas un problème.</p>

<h3>La structure des titres</h3>
<p>Rien à corriger. Sur les 30 pages du sitemap : un titre principal par page, une hiérarchie complète, aucun intitulé creux. Un seul sous-titre est partagé par 3 pages, « Parlons de votre projet. », un appel à l'action du gabarit.</p>
<div class="tablewrap"><table>
<thead><tr><th>Page</th><th>Titre principal</th><th class="num">Titres</th><th>Lecture</th></tr></thead>
<tbody>
<tr><td class="mono">/</td><td>Des leads, pas du trafic.</td><td class="num">13</td><td>un slogan, le sous-titre dit ce que fait le site</td></tr>
<tr><td class="mono">/methode/</td><td>La méthode Organikk en 4 étapes.</td><td class="num">13</td><td>clair</td></tr>
<tr><td class="mono">/systeme/</td><td>Passer d'un SEO de visibilité à un SEO de conversion.</td><td class="num">10</td><td>clair</td></tr>
<tr><td class="mono">/bootcamp/</td><td>Intégrer l'IA à ses process SEO pour gagner jusqu'à 25 h par mois…</td><td class="num">15</td><td>clair ; porte le « 25 h » sans appui</td></tr>
<tr><td class="mono">/audit-seo/</td><td>Ton site, sous tous les angles.</td><td class="num">2</td><td>clair pour un outil</td></tr>
</tbody></table></div>
"""

# ═══ 5. VITESSE ═══════════════════════════════════════════════════════════════
V[5] = """
<h2>Vitesse : le site est rapide pour vos visiteurs, la page d'accueil est lente en test</h2>
<p>Chez vos visiteurs réels, le site s'affiche en 2,20 s sur mobile et 1,84 s sur ordinateur, sans décalage de mise en page. C'est dans la zone que Google considère comme bonne. C'est sur ces mesures que Google évalue la vitesse d'un site.</p>
<p>En test, quatre pages sur cinq s'affichent en moins de 3,1 s. La page d'accueil met 5,72 s sur un passage et 4,01 s sur un autre. Le temps se perd dans l'image du bandeau : 0,8 s de réponse serveur, 0,44 s avant que le navigateur découvre l'image, 1,14 s pour la charger, 0,77 s pour la dessiner. C'est la page la plus vue du site (467 affichages, 82 clics).</p>
<p>La réponse du serveur, entre 350 et 750 ms selon la page, est le seul poste commun aux cinq pages. Vos visiteurs ne s'en ressentent pas : je la note à surveiller, sans en faire un chantier.</p>

<h3>À faire</h3>
<ol>
<li>Annoncer l'image du bandeau de l'accueil dès le début du code de la page, avec une priorité haute, dans un format et une taille adaptés au mobile. Il faut la main sur le code du bandeau.</li>
<li>Remesurer la page trois fois en test après correction.</li>
</ol>
<p>Les quatre autres pages n'appellent aucune correction.</p>

<h3>Chez vos visiteurs</h3>
<div class="tablewrap"><table>
<thead><tr><th>Mesure (75e percentile, 28 jours, tout le site)</th><th class="num">Mobile</th><th class="num">Ordinateur</th><th>Lecture</th></tr></thead>
<tbody>
<tr><td class="strong">Affichage du contenu principal (LCP)</td><td class="num">2,20 s</td><td class="num">1,84 s</td><td>bon, sous 2,5 s</td></tr>
<tr><td class="strong">Stabilité de la mise en page (CLS)</td><td class="num">0,00</td><td class="num">0,09</td><td>bon, sous 0,1</td></tr>
<tr><td class="strong">Réactivité (INP)</td><td class="num">non disponible</td><td class="num">non disponible</td><td>pas assez d'interactions enregistrées</td></tr>
</tbody></table></div>
<p class="note">Google ne fournit ces mesures qu'à l'échelle du site, pas page par page. Elles ne disent donc pas ce que vivent les visiteurs de l'accueil en particulier. J'ai regardé l'ordinateur aussi parce que 128 des 156 affichages français de l'accueil viennent d'un ordinateur.</p>

<h3>En test, page par page</h3>
<div class="tablewrap"><table>
<thead><tr><th>Page</th><th class="num">Score</th><th class="num">Affichage (LCP)</th><th class="num">Stabilité (CLS)</th><th class="num">Blocage (TBT)</th><th class="num">Réponse serveur</th><th>Ce qui s'affiche en dernier</th></tr></thead>
<tbody>
<tr><td class="mono">/</td><td class="num">63</td><td class="num">5,72 s</td><td class="num">0,001</td><td class="num">61 ms</td><td class="num">657 ms</td><td>l'image du bandeau</td></tr>
<tr><td class="mono">/methode/</td><td class="num">94</td><td class="num">2,81 s</td><td class="num">0,000</td><td class="num">16 ms</td><td class="num">747 ms</td><td>le texte d'introduction</td></tr>
<tr><td class="mono">/systeme/</td><td class="num">95</td><td class="num">2,79 s</td><td class="num">0,000</td><td class="num">2 ms</td><td class="num">597 ms</td><td>le titre</td></tr>
<tr><td class="mono">/bootcamp/</td><td class="num">91</td><td class="num">3,02 s</td><td class="num">0,000</td><td class="num">23 ms</td><td class="num">350 ms</td><td>le titre</td></tr>
<tr><td class="mono">/audit-seo/</td><td class="num">96</td><td class="num">2,27 s</td><td class="num">0,000</td><td class="num">18 ms</td><td class="num">648 ms</td><td>le titre</td></tr>
</tbody></table></div>
<p class="note">Lighthouse 13.3.0 mobile, un passage par page, plus le passage de PageSpeed. Deux passages sur l'accueil à quelques minutes d'écart ont donné 5,72 s puis 4,01 s : un score de test ne se lit pas au point près. Ce qui tient, c'est que l'accueil dépasse 4 s les deux fois et que les autres pages restent sous 3,1 s.</p>
"""

# ═══ 6. DONNÉES STRUCTURÉES ═══════════════════════════════════════════════════
V[6] = """
<h2>Données structurées : un balisage valide, le même sur toutes les pages</h2>
<p>Les données structurées sont le bloc de code qui décrit la page à Google : l'entreprise, la personne, le type de contenu. Vos 5 pages en portent un, lisible sans erreur. Rien à corriger d'urgence.</p>
<p>Le bloc est identique sur les 5 pages. Il décrit l'entreprise et la personne, pas la page. Rien ne décrit l'offre sur les pages d'offre, ni le bootcamp comme une formation.</p>
<p>Un détail : le slogan dans le code est « Ingénierie de visibilité SEO &amp; AEO ». L'accueil affiche « Des leads, pas du trafic ». Sans conséquence connue, mais un balisage doit dire la même chose que la page.</p>

<h3>À faire</h3>
<ol>
<li>Aligner le slogan du code sur celui de la page, quand on touchera au balisage. Une ligne.</li>
<li>Étudier un balisage de formation (Course) pour le bootcamp. L'affichage existe pour certains sites de formation ; rien ne dit qu'il s'appliquerait au vôtre.</li>
</ol>
<p class="note">Baliser les questions de <code>/bootcamp/</code> n'apporterait rien : Google a retiré l'affichage enrichi des FAQ le 7 mai 2026.</p>

<h3>Le détail</h3>
<div class="tablewrap"><table>
<thead><tr><th>Question</th><th>Réponse sur les 5 pages</th></tr></thead>
<tbody>
<tr><td class="strong">Le balisage se lit-il sans erreur ?</td><td>Oui. Un bloc par page, en trois parties : l'entreprise (Organization / ProfessionalService), le site (WebSite) et la personne (Person). Nom, adresse du site et logo présents.</td></tr>
<tr><td class="strong">Dit-il la même chose que la page ?</td><td>Sa description, « Consultant SEO Lyon depuis 2020 », correspond à l'à-propos. Son slogan ne correspond pas au titre de l'accueil.</td></tr>
<tr><td class="strong">Y a-t-il un balisage propre à chaque page ?</td><td>Non. Dates, places et prix du bootcamp ne sont pas dans le code.</td></tr>
<tr><td class="strong">Un affichage particulier dans Google est-il visé ?</td><td>Aucun aujourd'hui.</td></tr>
</tbody></table></div>
"""

# ═══ 7. MOTS-CLÉS BUSINESS ════════════════════════════════════════════════════
V[7] = """
<h2>Mots-clés business</h2>
<p>Sur les cinq pages, une seule recherche commerciale apparaît dans vos données : « bootcamp seo ». La page <code>/bootcamp/</code> y est en position 28,7 en moyenne sur 90 jours, sans clic.</p>
<p>Pour les autres pages, on ne sait pas. Les recherches de <code>/methode/</code>, <code>/systeme/</code> et <code>/audit-seo/</code> ne remontent pas dans la Search Console. Si Google les a anonymisées, l'interface ne les montrera pas non plus.</p>
<p>Deux autres pistes existent : la page consultant SEO Lyon et l'audit gratuit. Rien ne permet encore de les classer par potentiel.</p>
<p class="note">Ces données mesurent les affichages de vos pages dans Google, pas la demande du marché ni vos ventes. Aucune candidature ou demande n'est attribuée à ces pages dans ce relevé.</p>

<h3>À faire</h3>
<ol>
<li>Travailler <code>/bootcamp/</code> sur « bootcamp seo » : d'abord les liens qui la soutiennent (un seul aujourd'hui), puis ses preuves (voir Contenu). Le résultat à suivre est la candidature, pas la position.</li>
<li>Faire indexer <code>/consultant-seo-geo-lyon/</code> avant de juger son ciblage. Elle est au sitemap, sans lien, non indexée, 0 affichage.</li>
<li>Décider ce que <code>/audit-seo/</code> doit obtenir : une simple consultation, un contact, une demande d'accompagnement. Tant que ce n'est pas fixé, cette page passe après celles qui vendent.</li>
<li>Donner un rôle distinct à <code>/methode/</code> et <code>/systeme/</code>. Pas de fusion : rien ne montre qu'elles se pénalisent dans Google.</li>
</ol>

<h3>De la recherche au résultat</h3>
<div class="tablewrap"><table>
<thead><tr><th>Recherche</th><th>Ce qu'elle doit vendre</th><th>Résultat attendu</th><th>Ce qu'il reste à établir</th></tr></thead>
<tbody>
<tr><td>Bootcamp SEO</td><td>le bootcamp</td><td>une candidature</td><td>le potentiel de progression, la capacité de la page à convertir</td></tr>
<tr><td>Consultant SEO Lyon</td><td>une prestation</td><td>un rendez-vous ou un devis</td><td>l'indexation de la page, puis sa pertinence</td></tr>
<tr><td>Audit SEO gratuit en ligne</td><td>l'outil, puis les prestations</td><td>un contact après utilisation</td><td>l'objectif de la page</td></tr>
</tbody></table></div>

<h3>Les preuves, par opportunité</h3>
<div class="act">
  <b>Bootcamp SEO</b>
  <p>Deux formulations : « bootcamp seo », 50 affichages, position 28,7 ; « seo bootcamp », 16 affichages, position 54,9. Aucun clic en 90 jours. Dans le temps : 67 affichages en juillet, 6 en août, 12 en septembre. La baisse date de la dernière semaine de juillet, la cause n'est pas connue. Sur cette recherche, Google affiche des pages de formation et de programme : la page est dans le bon format.</p>
</div>
<div class="act">
  <b>Consultant SEO Lyon</b>
  <p>Google affiche neuf pages de consultants indépendants nommés, avec la ville. Vous avez une page dédiée, <code>/consultant-seo-geo-lyon/</code>, au sitemap, sans aucun lien, non indexée, 0 affichage. Sur l'accueil, des recherches « consultant seo + ville » apparaissent, mais pour des villes que vous ne servez pas (Thonon-les-Bains, Bourg-en-Bresse, Val d'Europe), en position 77 à 97.</p>
</div>
<div class="act">
  <b>Audit SEO gratuit en ligne</b>
  <p>Google affiche des outils en ligne (Cocolyze, Semrush, Ahrefs, Alyze). <code>/audit-seo/</code> est un outil de ce type : 11 affichages en position 1,1, recherches inconnues, aucun lien vers elle. Une seconde page d'audit, <code>/audit/</code>, hors sitemap, compte 18 affichages en position 5,9. Son rôle est à vérifier.</p>
</div>
<div class="act">
  <b>/methode/ et /systeme/</b>
  <p><code>/methode/</code> : 91 affichages, position 5,0, aucun clic, ni sur cette période ni sur la précédente. <code>/systeme/</code> : 56 affichages, position 5,6, aucun clic. Les recherches ne remontent pas. Une position moyenne de 5 agrège toutes les apparitions de la page : elle ne veut pas dire que la page est cinquième sur une recherche commerciale précise. Ces chiffres justifient de vérifier le ciblage. Ils ne prouvent pas que le titre en est la cause.</p>
</div>
<div class="act">
  <b>Votre nom</b>
  <p>« timothée boussardon » : 71 affichages, position 4,4, 20 clics. L'accueil répond. Rien à faire.</p>
</div>
"""
