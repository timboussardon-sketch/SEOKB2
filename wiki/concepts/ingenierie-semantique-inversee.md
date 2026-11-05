---
type: concept
title: Ingénierie Sémantique Inversée (framework Tim)
aliases: [ingenierie-semantique-inversee, reverse-semantic-engineering, framework-tim]
tags: [doctrine-tim, seo-ia, geo, framework, strategie]
created: 2026-04-11
updated: 2026-09-25
sources: 1
confidence: medium
status: stable
---

# Ingénierie Sémantique Inversée (framework Tim)

**Framework propriétaire de Tim** pour l'optimisation SEO/GEO à l'ère des moteurs génératifs. Référencé dans [[sources/2026-04-11-seo-ia-tim]] comme le cadre conceptuel qu'il applique et met à jour à la lumière de [[entities/titans]].

## Composants identifiables (via la source Tim)

La source ne donne pas une définition canonique complète — elle en présente la **mise à jour** Titans/MIRAS :

| Brique du framework | Concept SEO | Évolution Titans |
|---|---|---|
| Vecteurs Sémantiques | Proximité intention ↔ contenu | → **Vecteurs de Surprise** (divergence, pas juste pertinence) |
| Document Ranking | Classement des pages | → **Neural Memory Entry** (High Gradient début + fin) |
| Micro-Intentions | Découpage fin d'intention | → **Outlier Handling (YAAD)** : data structurée impeccable |
| Cluster Sémantique | Cocon thématique | → **Associative Memory Chain** (chaînes Low/High surprise) |

## La thèse centrale

Le SEO post-Titans n'est plus "répondre à la question" — l'IA le fait déjà via sa Persistent Memory. C'est **apporter l'information manquante** qui force le modèle à mettre à jour ses poids. Cf. [[concepts/surprise-gap]].

## Ce que vaut le transfert Titans

La mise à jour Titans/MIRAS du framework est une heuristique assumée, faute de mieux : [[hypotheses#H-001]] la classe `heuristique` et non `validé`, parce que Titans/MIRAS est un papier Google DeepMind Research et non une confirmation de ce que Google Search exécute en production. Rien dans la colonne de droite du tableau ci-dessus n'est observable de l'extérieur. Ce qui se teste, ce sont les prédictions opérationnelles qui en descendent, pas les internals — H-002 à H-008.

Le framework est la maille la plus haute, et c'est celle qui reste la moins mesurée. Ses briques filles sont opérationnalisées et instrumentées une par une ([[concepts/surprise-gap]] sous H-002, [[concepts/grounding-score]] sous H-003, [[concepts/weight-decay]] sous H-006) ; le cadre qui les relie, lui, n'a aucune fiche preuve et n'en aura pas — il n'énonce rien de falsifiable en propre. Il se juge sur la tenue de ses briques.

## Couche exécution : le workflow 8 étapes

Le framework est désormais opérationnalisé par le [[concepts/workflow-redaction-8-etapes]] (Article Engine) — un pipeline séquentiel en 8 prompts qui traduit les principes stratégiques en actions de rédaction. Détail complet dans [[sources/2026-03-31-tim-workflow-redaction]].

Le bot [[entities/fusionn-io]] est la **version commercialisée** de ce framework — il donne accès aux mêmes concepts (Demand Score, micro-intentions, cosine similarity, Score GEO) via une interface SaaS [[sources/2026-03-31-tim-prompt-systeme-fusionn]].

## Statut dans la KB

Bien documenté (4 sources). Le framework est décrit stratégiquement ([[sources/2026-04-11-seo-ia-tim]]), opérationnellement ([[sources/2026-03-31-tim-workflow-redaction]]), et commercialement ([[sources/2026-03-31-tim-prompt-systeme-fusionn]]). Aucune source **tierce** ne le confronte ni ne le mesure.

## Pages liées

[[sources/2026-04-11-seo-ia-tim]] · [[concepts/surprise-metric]] · [[concepts/surprise-gap]] · [[concepts/grounding-score]] · [[concepts/weight-decay]] · [[entities/titans]]
