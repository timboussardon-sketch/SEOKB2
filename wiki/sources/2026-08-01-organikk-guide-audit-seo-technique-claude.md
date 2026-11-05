---
type: source
source_type: article
title: L'audit SEO technique avec Claude (guide Organikk)
aliases: [guide-audit-seo-technique-claude, audit-7-phases-claude]
tags: [organikk, tim, seo, claude, audit, skills, maillage, indexation]
created: 2026-08-01
updated: 2026-09-22
sources: 1
confidence: high
status: stable
---

# L'audit SEO technique avec Claude (guide Organikk)

**Auteur** : Timothée Boussardon (organikk.co/guides)
**Type** : guide long-form HTML (existe aussi en PDF et en version EN)
**URL** : https://organikk.co/guides/audit-seo-technique-claude.html
**Date publication** : août 2026 (le site affiche « 08/2026 », pas de jour)

## Contexte

Guide complet pour mener un audit SEO technique avec Claude, sans outil SEO payant. Six chapitres : cadre du SEO en 2026 (trois filtres indexation → structure → sémantique), définition d'un skill, définition d'un workflow, organisation du dossier CLAUDE local, les cinq skills d'audit, puis l'audit en sept phases. Il remplace l'ancien blog `/blog/` d'organikk.co, disparu du site (les anciennes URL renvoient 404 au 2026-09-22).

## Chiffres / faits clés

- 7 phases d'audit dans un ordre fixe, 5 skills couvrant 4 phases, 3 phases sur prompt seul.
- 0 outil SEO payant requis ; 3 à 4,5 h par site selon le nombre d'URL.
- `indexation-check` : 9 points de contrôle par URL ; espacement de 3 à 5 s entre requêtes pour éviter le blocage.
- Fiabilité de l'indexation observée par requête : 40 à 60 % ; 100 % avec la variante API URL Inspection (quota officiel : 2 000 inspections par jour).
- Rendu client side : compter 30 s par URL en navigateur headless.
- Seuils de contenu : 300 mots minimum, 800 mots comme repère.
- Quick wins : positions 3 à 12, écart de CTR de 1,5 point comme seuil de priorisation.
- Fraîcheur : lastmod de moins de 6 mois.
- Maillage : 5 liens internes maximum par 1 000 mots ; phase cannibalisation à partir de 10 URL.
- Groupe bootcamp cité : 720 messages en 10 jours.
- Plan d'action en trois horizons : déblocage semaines 1-2, optimisation mois 1, création mois 2-3.

## Thèses

- Les trois filtres s'éliminent en cascade : une page non indexée ne ranke jamais ; la structure décide de l'extractibilité par les moteurs de réponse ; la pertinence sémantique ne joue qu'ensuite.
- Le Passage Ranking rend l'arborescence Hn décisive pour ce qui peut être cité.
- Un skill = module de compétence réutilisable déclenché par contexte ; un workflow = orchestration séquentielle de plusieurs skills. Conseil : garder les skills isolés et orchestrer à la main au début.
- La valeur n'est pas dans le fichier skill mais dans les données qu'on y injecte.
- Cannibalisation : classifier avant d'agir (requête exacte, même intention, proximité sémantique, triade SERP).
- Maillage : architecture Know → Do avant la data GSC, en deux passes (`maillage-systeme` puis `maillage-interne-gsc`).
- Une seule conversation par projet client.

## Citations marquantes

> "Une page non indexée ne ranke jamais, quelle que soit sa qualité." (attribution : Tim, août 2026)

> "L'arborescence Hn décide de ce qui peut être cité." (attribution : Tim, août 2026)

> "Un skill se copie en dix secondes. Les données que tu y injectes, non." (attribution : Tim, août 2026)

## Angle SEO à retenir

- L'audit devient un pipeline reproductible en skills, pas une prestation : cohérent avec [[sources/2026-09-08-algorithme-ne-plus-vendre-audit-seo]].
- L'inversion : la valeur d'un consultant est dans les seuils et données injectés (CTR 1,5 pt, 5 liens / 1 000 mots), pas dans le prompt.

## Limites

- Scrape via extraction résumée : les fichiers complets des skills (`indexation-check`, `seo-quick-win`, `seo-cannibalisation`) ne sont pas reproduits ici.
- Les seuils (300 / 800 mots, 1,5 pt CTR, 5 liens / 1 000 mots) sont des règles de Tim, pas des benchmarks sourcés dans le guide.
- Date au mois près.

## Pages liées

**Entity** : [[entities/gsc]], [[entities/organikk-co]], [[entities/bootcamp-seo-ia]]
**Concepts** : [[concepts/passage-ranking]], [[concepts/cannibalisation]], [[concepts/maillage-systeme]], [[concepts/maillage-interne]], [[concepts/know-simple-know-do]], [[concepts/triade-serp]]
