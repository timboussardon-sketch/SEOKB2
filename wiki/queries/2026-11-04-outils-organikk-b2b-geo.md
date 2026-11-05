---
type: query
title: Outils mobilisables pour la visibilité B2B et GEO d’Organikk
aliases: [outils-organikk-b2b-geo]
tags: [organikk, seo, b2b, geo, outils, skills]
created: 2026-11-04
updated: 2026-11-04
sources: 6
confidence: medium
status: draft
---

# Outils pour la visibilité B2B et GEO d’Organikk

Périmètre retenu : outils et skills de travail pour améliorer la visibilité du site. Inventaire documentaire, sans nouvel audit, relevé de position ni appel payant. Références : [[moc/doctrine-seo-reference]] et [[clusters/2026-10-19-organikk-consultant-seo-b2b-saas]].

## Données et applications

| Outil | Rôle | État de vérification |
|---|---|---|
| Google Search Console / gsc-simcity | Requêtes, pages, clics et impressions réellement observés | Données historiques documentées ; pas de nouvel export |
| Google Ads Keyword Planner via Qadence | Demande et enchères sur les requêtes candidates | Intégration documentée ; aucun appel aujourd’hui |
| Recherche Google et lecture de SERP | Vérifier l’intention et le format des pages concurrentes | À réaliser avec marché et localisation explicites |
| Citations IA / geo-citations | Mentions, recommandations, URL citées et sources concurrentes | Relevé Organikk historique sur Gemini ; accès actuel aux moteurs non testé |
| chatgpt-tracker | Panel de questions figées et historique des réponses | La note du 05/10 indique un moteur Claude, pas ChatGPT ; configuration à vérifier |
| Audit JEV / maillage | Crawl, graphe, liens entrants et opportunités de maillage | Application documentée ; non lancée ici |
| Lighthouse | Performance des pages | Disponible à travers le workflow CWV ; non exécuté |
| Obsidian / seo-kb / ./kb | Réunir preuves, verbatims, doctrine et décisions | Recherche locale exécutée ; modèle vectoriel indisponible, repli lexical utilisé |

Sources : [[queries/product-led-2026-10-13-organikk-outils-gratuits]], [[queries/geo-citations-organikk-2026-10-23]], [[syntheses/memoire-s5-outils-seo-internes-et-skills]], [[raw/notes/memoire-claude/project_chatgpt_tracker]].

## Skills mobilisables

Listing de capacités, pas déclenchement de ces workflows.

| Besoin | Skills |
|---|---|
| Cadrage SEO et IA | `strategie-geo` |
| Stratégie d’un mot-clé | `strategie-mot-cle` |
| Roadmap commune et suivi | `roadmap-seo` |
| Recherche et qualification | `seo-recherche-mots-cles`, `seo-mots-cles-decisionnels`, `seo-clustering-mots-cles` ; workflow local `workflow-mots-cles-complet` |
| Objections et questions d’achat | `seo-peurs-objections`, `seo-faq-query` |
| Pages et architecture | `strategie-contenu`, `seo-cluster-aeo`, `seo-modeles-pseo` |
| Diagnostic technique | `audit-complet-v2`, `indexation-check`, `seo-core-web-vitals`, `seo-cannibalisation` |
| Optimisation de l’existant | `seo-quick-win`, `maillage-systeme`, `maillage-interne-gsc`, `seo-donnees-structurees` |
| Observation et diagnostic GEO | `geo-citations`, `seo-geo-audit` |
| Préparation et rédaction | `seo-preparation-semantique`, `seo-entites-vectorielles`, `seo-brief-contenu`, `seo-workflow-article`, `ton-de-voix-tim` |
| Implémentation Organikk | `organikk-site`, `organikk-blog-article` |
| Mesure après publication | `preuves-feedback`, `gsc-watcher` |

Présence des skills vérifiée dans le catalogue de session et, pour les workflows locaux complémentaires, par listing de `~/.claude/skills/`. Aucune exécution de ces skills attestée par ce seul inventaire. Les scores doctrinaux GEO ne constituent pas des probabilités de citation validées : [[queries/2026-11-04-briques-outil-audit-geo-doctrine]].

## Outils publics et prototypes

Le sitemap public `https://organikk.co/sitemap.xml`, récupéré le 04/11/2026 par HTTP, contient :

- `/audit-seo/` : expérience d’audit documentée.
- `/outils/calculateur-budget-seo/` : calculateur budget SEO.
- `/outils/calculateur-cout-lead-seo/` : calculateur coût du lead SEO.
- `/skills/` et `/skills-seo/` : pages de skills.
- `/bootcamp-quiz/` : quiz.
- `/pre-audit-seo-geo/` : demande de pré-audit, formulaire plutôt qu’analyse autonome.

La présence au sitemap ne démontre ni le fonctionnement de chaque outil ni son indexation. Les calculateurs sont aussi présents dans les routes locales du dépôt Organikk.

Prototypes ou propositions historiques : top des mots-clés business, Micro-intentions Finder, analyse complète URL → mots-clés/clusters/questions, benchmark d’audit, couche GEO de l’audit, détecteur de patterns d’écriture IA, carte de maillage et analyseur CSV GSC. Leur mise en production n’est pas établie ici. [[queries/product-led-2026-10-13-organikk-outils-gratuits]]

## Proposition d’ordre d’utilisation

GSC → vérification des SERP et des rôles des pages B2B/GEO → cadrage des questions IA → relevé de citations après validation du coût → diagnostic et propositions sur les pages et sources tierces → mesure. C’est une proposition ; aucun chantier d’optimisation n’est lancé. Le relevé Gemini historique ne démontre aucune causalité entre attribut de page et citation. [[queries/geo-citations-organikk-2026-10-23]]

## Provenance et limites

Skill `kb-semantic-search` lu et recherche locale exécutée ; lectures ciblées et suivi des liens effectués. Recherche vectorielle indisponible, repli lexical effectif. Sitemap récupéré par `curl` ; tentative d’ouverture via l’outil web en échec. Aucun appel aux API de mesure ou aux moteurs IA. Le registre de santé disponible est daté du 01/11 : il ne prouve pas leur état actuel. [[ops/sante-automatisations]]
