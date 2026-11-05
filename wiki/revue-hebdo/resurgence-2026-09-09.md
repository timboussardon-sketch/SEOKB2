---
type: register
title: Résurgence — Ingénierie Sémantique Inversée — 2026-09-09
tags: [resurgence, doctrine-tim]
created: 2026-09-09
updated: 2026-09-09
status: stable
---

# Résurgence — [[concepts/ingenierie-semantique-inversee]] — 2026-09-09

## Pourquoi celui-là

`updated: 2026-04-11` — le plus ancien de tous les concepts `stable` du vault, jamais touché depuis sa création il y a 5 mois. Jamais ressorti en résurgence (les 7 éditions précédentes ont couvert data-proprietaire, grounding-score, surprise-gap, information-gain, persistent-wiki-vs-rag, programmatique-pseo, aeo). Poids réel : 20+ backlinks, c'est le framework-mère dont découlent [[concepts/surprise-gap]], [[concepts/grounding-score]], [[concepts/surprise-metric]], [[concepts/weight-decay]], et il structure H-001 dans [[hypotheses]] — littéralement l'hypothèse fondatrice de toute la doctrine post-SGE.

## État vs aujourd'hui

La page dit encore, telle quelle depuis avril : *"Aucune source tierce ne le confronte ni ne le mesure."* Cinq mois plus tard, c'est toujours vrai au sens strict — aucune source externe n'a challengé le transfert Titans/MIRAS → Google Search en prod. Mais la situation a changé sur un point qu'elle ne reflète pas :

- Le vault a depuis formalisé ce transfert en **H-001** dans [[hypotheses]] (`heuristique`, jamais `validé`/`invalidé`), avec une décision explicite : on l'assume comme heuristique parce que cohérente avec des observations indépendantes (GEO Aggarwal 2024, biais de récence Metehan, QRG p.42), pas parce qu'elle est prouvée. C'est une nuance de statut importante — "aucune confrontation" (ce que dit la page) est différent de "confrontation actée en heuristique assumée, faute de mieux" (ce que dit le registre).
- La page ne pointe vers **aucune ligne de [[hypotheses]]**, alors qu'elle en est la source conceptuelle directe. Le lien inverse existe (H-001 cite la page), mais pas le lien direct depuis la page vers le registre.
- Les briques opérationnalisées depuis (surprise-gap: `updated 2026-06-26`, grounding-score: `2026-07-13`, information-gain: `2026-07-17`) ont chacune évolué avec des preuves terrain partielles ([[preuves/2026-07-17-organikk-directories-guide-google]] pour H-011, adjacent). Le framework-mère, lui, n'a capitalisé aucun de ces retours : il reste figé à l'état "thèse posée en avril", sans trace des débuts de validation en aval.
- Pas de drift de wording détecté (pas de mot banni, pas de violation anti-AI-writing).

## Verdict proposé pour la revue hebdo

- [x] À mettre à jour : ajouter un lien direct vers [[hypotheses]] (H-001) dans la section "Statut dans la KB", et reformuler "aucune source tierce ne le confronte" en précisant le statut réel — assumé `heuristique`, pas validé, avec la raison (cohérence indirecte, pas preuve directe). Ajouter aussi une mention du niveau d'avancement des briques filles (surprise-gap, grounding-score, information-gain) pour que le framework-mère cesse d'être une photo figée d'avril pendant que ses dérivés évoluent.

## Log

Résurgence 2026-09-09 : concepts/ingenierie-semantique-inversee — verdict : à mettre à jour (lien direct vers hypotheses H-001 + reformulation du statut de confrontation) (à arbitrer en revue hebdo)
