---
type: guide
tags: [agents, claude-code, skills, linkedin, organikk]
created: 2026-10-16
sources: [~/.claude/skills (SKILL.md de chaque agent), post LinkedIn du 2026-10-15]
confidence: élevée (descriptif tiré des fichiers de chaque agent)
status: v1, à relire avant diffusion
---

# 16 agents SEO commandés depuis un chat

> Le doc promis dans le post du 15 octobre 2026. La liste des 16 agents, ce que chacun prend en entrée, ce qu'il rend, et la phrase à taper pour le lancer. Vérifié sur les fichiers d'agents en service le 16 octobre 2026.

## En résumé (à lire en premier)

Un agent = un dossier avec un fichier `SKILL.md`.

Le fichier décrit la tâche, les étapes, les règles, et les phrases qui le déclenchent.

Tu le déposes dans `~/.claude/skills/`. Claude Code le voit au prochain démarrage.

Tu tapes une phrase dans le chat. L'agent qui porte cette phrase se lance.

Les données viennent de Google : Search Console, Lighthouse, crawl du site. Aucun outil payant.

Aucun chiffre estimé. Une donnée absente s'écrit `[À SOURCER]`.

Chaque agent d'audit rend un rapport de pré-décision : diagnostic, preuves, actions P1 à P3 avec confiance, effort et risque.

Les 16 se répartissent en cinq familles : audit technique, données Search Console, mots-clés, contenu, avant-vente.

## 1. Audit technique

### 1. audit-complet-v2

Audit SEO complet d'un site en 9 phases, dans l'ordre.

Il ne contient pas la méthode. Il appelle les agents dédiés un par un : indexation, Core Web Vitals, gains rapides, structure Hn, pertinence du contenu, cannibalisation, maillage.

Données : Search Console, crawl, Lighthouse, CrUX. Aucun outil tiers.

Règle : un fait mesuré n'est pas un frein SEO démontré. Chaque constat s'écrit en trois temps, observation prouvée, conséquence justifiée, bénéfice attendu.

Sortie : un rapport de pré-décision (diagnostic, 3 à 5 chiffres, 3 problèmes maximum, plan 30 jours avec 3 P1 maximum, ce que les données ne permettent pas de conclure) et un tableau de bord HTML à 8 onglets.

> « Fais l'audit SEO complet de [site] »

### 2. indexation-check

Audit d'indexation sans outil payant, sur des sites de 30 à 1 000 pages.

9 points vérifiés par URL : statut HTTP, blocages techniques, noindex, présence dans le sitemap, lastmod, cohérence du sitemap, liens internes entrants, longueur de contenu, statut d'indexation Google estimé.

Il distingue « non indexée » et « non testable » quand Google limite les requêtes.

Lecture seule. Aucune demande d'indexation forcée.

Sortie : anomalies critiques en tête, anomalies mineures, recommandations priorisées.

Il tourne en ponctuel ou en routine mensuelle.

> « Vérifie l'indexation de [site] » ou dépose un `urls.txt`

### 3. seo-core-web-vitals

Audit LCP, CLS, TBT via Lighthouse en local, mobile d'abord, sur un échantillon d'URL tiré du sitemap.

Sortie : scores par URL, problèmes récurrents à l'échelle du site, plan de correction pour les 5 pires pages.

> « Audit Core Web Vitals de [site] »

### 4. seo-geo-audit

Audit d'une page ou d'un texte pour les moteurs génératifs (AI Overview, ChatGPT, Perplexity).

7 scores : Surprise, Grounding, Content Effort, alignement RRF, structure RAG, fraîcheur, Action Engine.

Problèmes localisés dans le texte, score global, corrections priorisées, plan de réécriture.

> « Pourquoi ChatGPT ne me cite pas sur cette page ? »

### 5. audit-report

Transforme les sorties des agents d'audit en un rapport à deux onglets.

Onglet Résumé : diagnostic, 4 chiffres, 3 priorités, plan 30 jours, 3 opportunités.

Onglet Analyse technique.

Six passes de raisonnement avant d'écrire, puis une passe critique.

Jamais de note sur 10. Jamais de 301 ni de fusion décidée automatiquement.

> « Écris le rapport d'audit »

## 2. Données Search Console

### 6. seo-quick-win

Pages en position 3 à 12, impressions élevées, CTR sous la moyenne.

6 étapes : filtrer (positions 3 à 15, hors requêtes de nom et page d'accueil), trier par impressions, calculer l'écart de CTR, croiser avec l'intention, prioriser, lister les leviers.

Leviers : balise title, meta description, H1, FAQ en haut de page, densification du passage qui répond.

Il se lance dès qu'un export Search Console est déposé.

> « Gains rapides sur cet export GSC »

### 7. seo-cannibalisation

Pages du même site qui se disputent les mêmes requêtes.

4 types de conflit : mot-clé exact, même intention, proximité sémantique, triade SERP.

Action recommandée par cas : 301, fusion, différenciation, maillage croisé, ou rien quand Google affiche volontairement plusieurs pages du site.

> « Je rankais mieux avant sur [requête] »

### 8. maillage-interne-gsc

Maillage interne lu dans les données Search Console.

Hiérarchie page mère, fille, petite-fille.

5 étapes : récupérer la GSC, diagnostiquer (mères potentielles, pages sous-maillées, orphelines), construire le plan avec la règle Know vers Do, prioriser par urgence, rendre les recommandations.

Chaque recommandation donne la page source, la page de destination, l'ancre et le contexte de la phrase.

> « Maillage interne depuis cet export GSC »

### 9. maillage-systeme

Même sujet, sans Search Console.

Il raisonne sur la structure éditoriale : piliers, hub et satellites, ancres entrantes diversifiées, pages orphelines, pages sans lien sortant.

Utilisable avant le lancement d'un site, quand aucune donnée de trafic n'existe.

> « Plan de maillage pour cette liste d'articles »

## 3. Mots-clés

Les trois agents s'enchaînent. La sortie de l'un nourrit le suivant.

Le volume s'affiche uniquement s'il vient d'une donnée réelle. La difficulté n'est jamais inventée.

### 10. seo-recherche-mots-cles

Part d'une thématique ou de quelques mots-clés de départ.

5 étapes : cadrer, étendre sémantiquement, qualifier (intention, difficulté), filtrer le bruit, prioriser.

Sortie : tableau priorisé, chaque mot-clé avec son intention.

> « Trouve-moi des mots-clés sur [thème] »

### 11. seo-clustering-mots-cles

Découpe une liste brute en pages. 1 groupe = 1 page.

Critère : deux mots-clés qui affichent le même top 10 ont la même intention, donc une seule page.

5 étapes : importer, dédoublonner, grouper par SERP, nommer le groupe et son mot-clé pivot, affecter une page par groupe avec détection de cannibalisation.

> « J'ai 200 mots-clés à organiser »

### 12. seo-mots-cles-decisionnels

Isole les requêtes qui convertissent, bas de funnel, par opposition à l'informationnel qui fait du trafic.

5 étapes : définir l'offre et le point de conversion, repérer les signaux de décision, classer par étage, scorer le potentiel de conversion, sortir une liste courte avec page et format recommandés.

> « Quels mots-clés rapportent dans cette liste ? »

## 4. Contenu

### 13. seo-brief-contenu

Brief éditorial avec structure Hn pour le Passage Ranking.

7 étapes : décoder la requête, vecteurs sémantiques, micro-intentions, structure Hn, contenu par H2, signaux E-E-A-T, format multimédia.

Il ne copie pas les pages en place. Il cherche ce qu'elles n'ont pas dit.

> « Brief sur [requête] »

### 14. seo-faq-query

FAQ d'une page, 5 à 7 questions maximum.

Chaque question active un vecteur sémantique distinct. Chaque réponse se lit seule et part dans le balisage FAQPage.

Perspective verrouillée, B2B ou B2C. Les questions qui n'aident pas à décider sont retirées.

> « Fais la FAQ de cette page »

## 5. Avant-vente

### 15. seo-pre-audit

Pré-audit d'un prospect à partir de sa seule URL. Données publiques, aucune Search Console.

Grille de 7 insights business.

Sortie : diagnostic, angle, état SEO, stratégie de pages par axes, roadmap 90 jours, notes de call.

Aucun volume, aucune position, aucun trafic inventé.

> « Prépare le pré-call sur [site] »

### 16. prospection-scraping

Liste de prospection à partir d'annuaires publics.

Cible : des sociétés en activité, avec un site et un blog, à trafic faible mais réel.

6 phases : cadrage, collecte sur plusieurs annuaires, dédoublonnage, contrôle automatique (site en ligne, blog présent), enrichissement (dirigeant, LinkedIn, trafic, fraîcheur), consolidation scorée.

Sortie par ligne : URL, dirigeant ou responsable marketing, profil LinkedIn.

Jamais de nom, d'URL LinkedIn ni de chiffre de trafic inventé. Scraping autorisé uniquement.

> « Trouve-moi des startups à prospecter »

## 6. Ce que les 16 ont en commun

Les règles accumulées vivent dans un fichier `CLAUDE.md` à la racine. Tous les agents le lisent.

Les données propres à chaque client vivent dans un coffre Obsidian, un dossier par client.

[MATIÈRE MANQUANTE : la liste des branchements de données (Search Console, GA4, PageSpeed) et le mode d'installation, à sortir du guide d'installation existant]

## Sources

- Les fichiers `SKILL.md` des 16 agents, relus le 16 octobre 2026.
- Post LinkedIn du 15 octobre 2026.
