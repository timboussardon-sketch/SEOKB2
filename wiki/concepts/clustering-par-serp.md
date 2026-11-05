---
type: concept
title: Clustering par partage de SERP
aliases: [clustering-par-serp, serp-overlap, partage-de-serp]
tags: [seo, clustering, mots-cles, serp, cannibalisation]
created: 2026-10-30
updated: 2026-10-30
sources: 2
confidence: medium
status: draft
---

# Clustering par partage de SERP

Deux mots-clés vont sur la même page quand Google affiche le même top 10 pour les deux. Le critère vient du skill `seo-clustering-mots-cles` (`~/.claude/skills/seo-clustering-mots-cles/SKILL.md`, ligne 19) : même SERP, même intention, une seule page. La proximité sémantique seule ne suffit pas (ligne 20).

## Le proxy et sa limite

Sans SERP réelle, le skill regroupe par intention identique et même tête sémantique (ligne 37). Sa sortie est alors une hypothèse, « à valider par overlap réel » (ligne 79).

Les cinq études du 25/09 ([[keywords/index]]) sont dans ce cas : relevé hors Google, `statut_decision: HYPOTHÈSE`, « validation SERP Google requise ». C'est l'objet de [[contradictions#C-014]].

**Marge d'erreur du proxy : non mesurée.** Aucune comparaison entre clusters proxy et overlap Google n'existe dans le vault.

## Garde-fou

Aucun cluster issu d'un relevé hors Google ne sort du statut HYPOTHÈSE sans overlap Google relevé (règle de pré-décision : [[methodes/rapport-mots-cles-format]]).

## Mesure possible

Le dépôt `~/Code/serp-vitrine` lit le top 10 Google FR sans clé depuis le 2026-10-21. Il permet de relever l'overlap réel sur les requêtes des cinq études et de mesurer l'écart avec les clusters proxy. Tant que ce relevé n'est pas fait, la page reste `draft`.

Pages liées : [[concepts/triade-serp]] · [[contradictions]]
