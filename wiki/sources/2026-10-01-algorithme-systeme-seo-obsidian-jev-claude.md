---
type: source
source_type: article
title: J'ai créé un système SEO avec Obsidian, Jev et Claude (ça marche!)
aliases: [systeme-seo-obsidian-jev-claude]
tags: [algorithme, tim, claude, obsidian, jev, data-proprietaire]
created: 2026-10-01
updated: 2026-10-06
sources: 1
confidence: high
status: stable
---

# J'ai créé un système SEO avec Obsidian, Jev et Claude (ça marche!)

**Auteur** : Timothée Boussardon (algorithme.substack.com)
**Type** : newsletter
**URL** : https://algorithme.substack.com/p/jai-cree-un-systeme-seo-avec-obsidian
**Date publication** : 2026-10-01

## Contexte

Sous-titre : « (sans outil SEO) ». Tim défend deux arguments : le système Obsidian + Claude a vocation à remplacer les outils SEO, et le SEO se gagne sur la data propriétaire. Il publie en clair quatre skills (`seo-mots-cles-business`, `seo-pre-audit`, `maillage-systeme`, `seo-donnees-structurees`), le prompt de l'agent indexation, et présente Jev comme couche de tri.

## Chiffres / faits clés

- Setup : modèle LLM wiki attribué à Andrej Karpathy, vault séparé en `raw/` (appels clients, exports Search Console, articles ; jamais modifié par Claude) et `wiki/` (organisé par Claude).
- 4 avantages revendiqués : mémoire permanente, modèle « exponentiel » (vendre le système plutôt que du TJM), base stable face aux nouveaux modèles, process standardisés.
- Mots-clés : « 80 % » de la recherche est de la commodité que l'IA fait aussi bien qu'un outil ; « 20 % » de vrai travail (Reddit, X, expérience réelle). Un corpus par client + une base SEO commune à tous les projets.
- `seo-mots-cles-business` : 3 portes (offre, intention business, opportunité démontrée), 5 décisions (POUSSER, CRÉER, CONSOLIDER, ÉCARTER, À VALIDER). Demande « Forte » = 5 variantes Suggest ou plus, 7 mentions en calls ou plus ; seules 20 impressions Search Console ou plus confirment la demande. Export GSC de 3 à 6 mois, 3 actions maximum, aucun score sur 10.
- `seo-pre-audit` : URL + données publiques seules, 7 questions dont 2 ou 3 tranchées, 4 à 6 modèles de pages, roadmap 90 jours, résumé en 3 à 5 phrases.
- `maillage-systeme` : un lien présent sur 80 % des pages ou plus est un lien de gabarit et ne compte pas ; 3 ancres par lien (exacte, partielle, sémantique) ; insertion par lots de 10 à 20 ; critère de fin = zéro page d'offre orpheline. Le maillage fait partie de la technique « à 80 % automatisée ».
- `seo-donnees-structurees` : JSON-LD dérivé du contenu, une seule source (`lib/schema.ts`), entités référencées par `@id`.
- Agent indexation : 9 contrôles en lecture seule (HTTP, robots.txt, noindex, sitemap avec lastmod < 6 mois, cohérence, maillage, longueur < 300 mots, `site:` ou API GSC, soft 404 sur 3 URL inexistantes).
- Jev : modèle de vérification et de classement, pas de rédaction, environ 0,8 seconde par appel. Trois scripts : `verifier.py`, `liens.py`, `matiere.py`. Aucune automatisation tant que l'accord avec Tim n'atteint pas 80 % sur au moins 30 cas.
- Audits : « ne se vendent plus », à inclure ou automatiser ; chaque audit alimente l'historique du site.

## Citations marquantes

> "On entre dans un jeu de data, et rien d'autre." (Tim, 2026-10-01)

> "JEV trie mais la décision finale me revient toujours." (Tim, 2026-10-01)

## Angle SEO à retenir

- Inversion : l'enjeu n'est pas d'être cité par les IA mais de trouver des mots-clés « qui ne seront pas mangés par les LLM dans les 5 prochaines années ».
- Les seuils de demande (5 variantes Suggest, 7 mentions en calls, 20 impressions GSC) remplacent le volume comme critère de décision.
- Le post rend publics des skills du vault : il sert de point de référence datée de leur état au 2026-10-01.

## Limites

Texte intégral public récupéré par curl (pas de paywall). Une capture d'écran (agent de scoring GEO) n'est pas lisible dans le scrape. Les seuils et les 80 % sont des règles de Tim, pas des mesures ; le gain d'efficacité n'est pas chiffré.

## Pages liées

**Entity** : [[entities/obsidian]], [[entities/karpathy]], [[entities/gsc]], [[entities/reddit]]
**Concepts** : [[concepts/data-proprietaire]], [[concepts/maillage-systeme]], [[concepts/persistent-wiki-vs-rag]], [[concepts/zero-volume-business]]
