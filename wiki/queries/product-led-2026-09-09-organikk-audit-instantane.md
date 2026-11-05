---
type: query
title: "Organikk : audit SEO instantané par URL, sans Search Console"
aliases: [audit-instantane-organikk, product-led-organikk-2026-09, audit-seo-url-organikk]
tags: [organikk, product-led, geo, aeo, mots-cles-decisionnels, pseo, outils]
created: 2026-09-09
updated: 2026-09-09
sources: 4
confidence: medium
status: draft
---

# Organikk : audit SEO instantané par URL, sans Search Console

Skill `seo-product-led-seo`. Demande de Tim le 2026-09-09 : un outil gratuit sur organikk.co, l'utilisateur colle une URL et reçoit un audit complet, sans connecter Search Console.

## Décision de routing : le garde-fou Fusionn/Organikk ne s'applique pas ici

[[queries/product-led-2026-07-07-organikk-anti-chatgpt]] posait un garde-fou anti-cannibalisation : Fusionn plateforme d'outils gratuits, Organikk limité à des démos courtes qui renvoient vers Fusionn pour la version connectée. Ce binôme (avec [[queries/pseo-2026-07-07-organikk-corpus]]) est passé `stale` le 2026-08-07 ([[revue-hebdo/2026-W32]], point 5), exécution d'une date de mort posée pour absence de publication, pas une invalidation de doctrine.

Le crawl du repo `organikk-next` montre que la pratique a déjà divergé de ce garde-fou avant même cette session : `src/app/outils/` héberge 7 outils complets en production, pas des démos (`analyse-geo`, `ctr-par-position-google`, `generateur-donnees-structurees`, `probabilite-citation-llm`, `quality-rater-guidelines`, `simulateur-roi-seo`, `zero-clic-par-intention`). Interrogé le 2026-09-09 sur le routing du nouvel audit, Tim tranche explicitement : outil complet sur Organikk, pas une démo qui renvoie vers Fusionn. Décision consignée ici. À faire remonter en revue hebdo pour réconcilier ou clore formellement le garde-fou de juillet, qui ne décrit plus l'état réel du site.

## Constat annexe : /outils/analyse-geo affirme un raisonnement Claude qu'il n'exécute pas

En lisant `src/components/AnalyseGEO.tsx` pour cadrer la stack technique disponible : les 7 scores GEO de la page en production sont calculés par du regex et du comptage, entièrement côté client (occurrences de mots clichés, présence de chiffres, longueur du texte, mots techniques). Aucun appel à Claude, aucune route API détectée dans `src/app/api`. Or la FAQ de `src/app/outils/analyse-geo/page.tsx` affirme : « Le contenu que vous collez passe par Claude pour le raisonnement IA », et le meta description dit « évalué par IA ». Ça contredit la règle jamais mentir sur des fonctionnalités vérifiées. À corriger : soit brancher un vrai appel Claude sur cette page, soit réécrire la FAQ et le meta pour décrire fidèlement un scoring heuristique déterministe. Signalé à Tim en chat, pas encore traité.

## 1. Analyse de la thématique

- **Produit et service** : Organikk vend le système de Tim (vault, skills, preuves terrain), positionnement anti-agence, accompagnement SEO/GEO.
- **Données propriétaires disponibles** : doctrine GEO/AEO du vault, grille anti-AI-writing, méthode [[concepts/score-sante-site]] (dépend de la Search Console du client, donc hors scope pour un audit sur simple URL), corpus de méthode mots-clés décisionnels.
- **Ressources techniques** : repo `organikk-next` (Next.js, export statique dans `out/`), 7 outils déjà en prod dans `/outils/`, aucune route API serveur détectée à ce jour (tout le calcul observé est client-side ou heuristique), PageSpeed Insights API disponible gratuitement côté Google avec une clé.
- **Objectif de conversion** : capter un lead qui vient de coller son URL, vers l'accompagnement ou le bootcamp.

## 2. Micro-intentions "Do" identifiées

- Auditer : où j'en suis techniquement sur mon site
- Auditer : mon contenu est-il prêt pour les moteurs génératifs
- Générer : les mots-clés business que mon site cible ou devrait cibler
- Comparer : mon site face à un site comparable que je choisis moi-même
- Planifier : un plan d'action priorisé plutôt qu'un diagnostic brut

## 3. Les 5 concepts

| Solution Produit | Micro-intention "Do" | Surprise Gap | Confidence Score (Preuves) | Action de conversion |
|---|---|---|---|---|
| Audit SEO instantané multi-couches : URL en entrée, sortie = technique + performance + qualitatif + mots-clés inférés | « audit seo gratuit », « analyser mon site seo », « audit seo en ligne » | Couche qualitative LLM qui juge l'intention et la lisibilité IA plutôt qu'une liste de cases cochées technique (le commodity du marché) | PageSpeed API et parsing HTML/robots/sitemap sont du terrain connu (méthode [[concepts/score-sante-site]] déjà bâtie sur du crawl et des seuils vérifiables) | Rapport complet + PDF par email, gate sur l'analyse qualitative détaillée → accompagnement |
| Diagnostic de lisibilité IA (GEO readiness) d'une page publiée | « mon site est-il lisible par chatgpt », « optimiser pour les ia génératives » | Grille [[entities/seo-geo-audit]] (7 scores) appliquée à une URL crawlée au lieu d'un texte collé à la main | Skill `seo-geo-audit` déjà documenté et utilisé en prestation ; corrige au passage l'écart constaté sur `/outils/analyse-geo` | Résultat partiel visible, page complète (7 scores détaillés) par email |
| Générateur de mots-clés business inférés du contenu crawlé | « quels mots-clés cibler pour mon site », « trouver mes mots-clés seo » | Méthode [[concepts/mots-cles-decisionnels]] appliquée à une lecture de site plutôt qu'à un brief client | Skill `seo-mots-cles-decisionnels` déjà utilisé en prestation, mais jamais automatisé sur un crawl externe | Liste complète (au-delà du top 10 affiché) par email → recherche de mots-clés en prestation |
| Comparateur deux sites : l'URL de l'utilisateur face à un site comparable qu'il choisit, sur les mêmes dimensions techniques | « comparer mon site à un site comparable », « pourquoi ce site est mieux placé que le mien » | Réutilise le moteur de crawl du concept 1 sur deux URLs, écart affiché dimension par dimension | Dépend entièrement du concept 1 (même moteur, deuxième URL) | Rapport comparatif par email → audit approfondi |
| Roadmap 90 jours générée depuis le résultat d'un audit | « plan d'action seo pour mon site », « par où commencer en seo » | Le plan reprend l'ossature de [[project_roadmap_prestation]] plutôt qu'une checklist générique | Playbook de prestation déjà tenu et appris en continu chez Organikk | Roadmap détaillée par email → accompagnement système |

## 4. Faisabilité

| Concept | Complexité technique | Données nécessaires | Différenciation |
|---|---|---|---|
| 1. Audit instantané multi-couches | Élevée : premier crawl serveur du site (aucune route API équivalente en prod aujourd'hui), appel PageSpeed, appel LLM | Aucune donnée externe payante, uniquement du crawl public + une clé PageSpeed gratuite | Forte si la couche qualitative LLM est réellement branchée (voir le constat sur analyse-geo, à ne pas reproduire ici) |
| 2. GEO readiness sur URL | Moyenne : reprend le crawl du concept 1, ajoute la grille des 7 scores en LLM | Même crawl que le concept 1 | Forte, doctrine propriétaire déjà écrite (skill seo-geo-audit) |
| 3. Mots-clés inférés | Moyenne : lecture sémantique du contenu crawlé par LLM | Même crawl que le concept 1 | Moyenne, à bien distinguer du ranking réel pour ne pas induire en erreur |
| 4. Comparateur deux sites | Faible en plus du concept 1 (même moteur, deuxième passage) | Aucune donnée supplémentaire | Moyenne, utile en variante mais pas prioritaire |
| 5. Roadmap 90 jours | Faible : génération de texte structuré à partir des résultats déjà calculés | Aucune donnée supplémentaire | Forte pour la conversion, faible en soi comme différenciateur produit |

## 5. Concept retenu : consolidation 1 + 2 + 3 + 5 dans un seul outil, 4 en variante différée

Les concepts 2, 3 et 5 partagent le même moteur de crawl que le concept 1 et n'ont pas de valeur seuls pour un visiteur qui vient de coller une URL. Ils deviennent des modules d'un seul outil "Audit SEO instantané". Le concept 4 (comparateur) réutilise le même moteur sur une deuxième URL : à traiter en itération suivante, pas dans le premier scope.

### Spécification technique

**Input** : un champ URL. Aucune connexion de compte, aucun OAuth.

**Logique, en 4 étapes** :

1. **Crawl on-page** de l'URL fournie : title, meta description, canonical, meta robots, hreflang, lang, structure Hn, maillage interne de la page, alt manquants, JSON-LD (présence, type, validité), Open Graph et Twitter Card, viewport, HTTPS, code HTTP, redirections.
2. **Crawl niveau site** : `robots.txt` (blocages), `sitemap.xml` (présence, fraîcheur du lastmod, cohérence avec les pages effectivement trouvées).
3. **Performance** : PageSpeed Insights API sur l'URL, Core Web Vitals (LCP, CLS, INP), poids de page, ressources bloquantes.
4. **Couche qualitative LLM**, sur le contenu texte extrait de la page : correspondance à l'intention de recherche perçue, E-E-A-T perçu, lisibilité par une IA (grille [[entities/seo-geo-audit]] : Surprise, Grounding, Effort, RRF, Structure, Freshness, Action), plus une liste de 10 mots-clés business inférés du contenu, explicitement étiquetée « mots-clés ciblés par le contenu » et non « mots-clés positionnés » puisqu'aucune donnée de ranking réelle n'est disponible sans Search Console.

**Hors scope explicite, à afficher comme tel plutôt qu'à approximer** : positions Google réelles, trafic réel, backlinks, statut d'indexation exact à l'échelle (le scraping `site:` est trop fragile et rate-limité par Google pour un endpoint public à trafic variable, cf. [[indexation-check]] qui reste un usage batch/manuel chez Tim).

**Output** :
- Résultat partiel visible immédiatement (score global, 2-3 anomalies critiques, aperçu des mots-clés inférés)
- Rapport complet gate par email : détail des 4 couches + roadmap 90 jours générée à partir des résultats (ossature [[project_roadmap_prestation]])
- CTA final vers l'accompagnement Organikk

**Données** : aucune donnée payante, aucune donnée stockée côté Organikk au-delà de l'email capté pour l'envoi du rapport (à documenter dans une mention RGPD sur la page, cf. [[reference_argumentaire_confidentialite_rgpd]]).

**Stack** : le repo `organikk-next` n'a aujourd'hui aucune route API serveur observée dans `src/app/api`, tous les outils existants calculent en client-side ou au build. Ce nouvel outil demande une vraie route serveur (fetch externe vers l'URL cible, vers PageSpeed, vers Claude), ce qui est un changement d'infra par rapport aux 7 outils existants et doit être cadré avec `organikk-site` avant le développement.

## 6. Priorisation

1. **Corriger le constat annexe sur `/outils/analyse-geo`** avant de lancer un nouvel outil qui promet, lui aussi, une couche IA : soit brancher l'appel Claude réel, soit corriger la FAQ et le meta. Sinon le nouvel audit hérite du même risque de mensonge sur les fonctionnalités.
2. **Construire le moteur de crawl (étapes 1 à 3)** : déterministe, zéro dépendance LLM, testable seul.
3. **Brancher la couche qualitative LLM (étape 4)**, avec le grounding du skill seo-geo-audit.
4. **Générer la roadmap 90 jours** en sortie, réutilisation de l'ossature roadmap-prestation.
5. **Comparateur deux sites (concept 4)** en itération suivante, une fois le moteur de crawl stabilisé sur une seule URL.

Règle du skill à respecter : tester le moteur de crawl en MVP sur quelques sites connus avant d'ouvrir l'outil au public, prévoir une sortie agent-friendly (endpoint JSON) pour l'Agentic SEO.

Liens : [[queries/product-led-2026-07-07-organikk-anti-chatgpt]] · [[queries/pseo-2026-07-07-organikk-corpus]] · [[concepts/score-sante-site]] · [[entities/seo-geo-audit]] · [[project_roadmap_prestation]] · [[concepts/product-led-seo]]
