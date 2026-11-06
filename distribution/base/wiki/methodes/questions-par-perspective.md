---
type: methode
title: Questions par perspective, réponses ancrées dans le vault
aliases: [storm-vault, perspectives-sourcees, multi-perspective]
tags: [methode, angle, recherche, brief, redaction]
created: 2026-10-18
updated: 2026-10-18
sources: 1
confidence: medium
status: draft
---

# Questions par perspective, réponses ancrées dans le vault

Étape commune aux skills qui cherchent un angle avant d'écrire. Elle complète le [[concepts/surprise-gap]] : le Surprise Gap compare ce que disent les concurrents, les perspectives cherchent ce qu'aucun d'eux n'a regardé.

## Origine

STORM (Shao et al., Stanford OVAL, NAACL 2024, arXiv 2402.14207) découvre des perspectives sur un sujet, fait poser des questions depuis chacune, et va chercher chaque réponse dans des sources. Évalué par des éditeurs Wikipédia, il gagne 25 % d'organisation et 10 % de couverture en absolu sur une base RAG guidée par un plan. Les auteurs relèvent deux défauts : le biais des sources se transmet au texte, et des faits sans lien sont associés.

Ces chiffres portent sur des articles de type Wikipédia. Rien ne dit encore qu'ils tiennent sur un brief SEO ou une propale.

Décision de Tim du 2026-10-18 : brancher l'étape sur les skills d'angle (liste en bas), sous forme d'une méthode unique.

## Ce qu'on ne reprend pas

Les versions « 4 prompts » qui circulent font jouer cinq experts au modèle, sans aller chercher de sources. On obtient des opinions inventées : interdit ici (AGENTS §5.4).

L'auto-notation de 1 à 10 en fin de prompt n'est pas reprise non plus. La relecture critique passe par `verificateur-livrable` et `jev verifier`, qui ne relisent pas leur propre texte.

## Les perspectives et où les chercher

| Perspective | Question type | Sources |
|---|---|---|
| Praticien | Qu'est-ce qui se passe vraiment quand on le fait ? | Coffre client (tickets, verbatims, transcripts), `raw/clients/`, `raw/transcripts/`, fiches `wiki/preuves/` |
| Recherche | Que disent les études et la doc officielle ? | `wiki/sources/` de type `paper` et `doc-google`, `raw/papers/` |
| Sceptique | Quel est le contre-argument le plus solide ? | [[contradictions]], colonne Contre-argument de [[hypotheses]], sources qui contredisent la thèse |
| Voix externes | Qui, dans le métier, a pris position ? | `raw/auteurs/`, attribution obligatoire (AGENTS §13) |
| Argent | Qui gagne quoi sur cette requête ? | SERP réelle : qui se positionne, ce qu'il vend, affiliation, annonces |
| Acheteur | Qu'est-ce qui le fait hésiter ou renoncer ? | Requêtes Search Console, sorties `seo-peurs-objections`, verbatims d'achat |

Choisir les perspectives que le livrable demande, pas les six d'office. Si le corpus porte une perspective absente du tableau (un régulateur, un installateur, un concurrent), l'ajouter.

## Procédure

1. Pour chaque perspective retenue, écrire deux ou trois questions qu'elle poserait sur le sujet.
2. Chercher chaque réponse : `./kb search`, coffre client, SERP ou WebSearch. Une réponse = un extrait + sa source. Sans source : `[MATIÈRE MANQUANTE]`, et la question reste dans le tableau.
3. Croiser :
   - **désaccord** entre deux perspectives sourcées : angle candidat. S'il touche la doctrine, il part dans [[contradictions]] ;
   - **accord** de toutes les perspectives : socle de la page, il ne différencie rien ;
   - **question sans réponse** dans aucune source : trou. Il part en demande au client, en test ou en étude, jamais en paragraphe rédigé.
4. Sortie, dans le livrable du skill appelant :

```
## Perspectives
| Perspective | Question | Réponse | Source |
|---|---|---|---|

Désaccords : …
Consensus : …
Trous : …
```

Les angles retenus par le skill viennent des désaccords et des trous, chacun avec sa source.

## Format court

Pour la revue de presse quotidienne et les posts LinkedIn : trois perspectives au plus, une question chacune, et seulement les lignes « Désaccords » et « Trous ». Le tableau reste dans les notes de travail, il ne passe pas dans le texte publié.

## Skills branchés

`seo-brief-contenu`, `seo-workflow-article` (et donc `article-engine-pipeline`), `revue-presse-quotidienne`, `linkedin-post-tim`, `strategie-geo`, `audit-pre-call`, `propale-organikk`, `seo-peurs-objections`, `hypotheses-validation`.

Pas branchés : maillage, cannibalisation, quick-win, indexation, Core Web Vitals, hygiène du vault. Ces skills partent de la data, pas d'un angle.

## Mesure

À la revue hebdo qui suit dix usages : combien de désaccords ou de trous sourcés ont fini dans un livrable publié, et combien de lignes `[MATIÈRE MANQUANTE]`. Si l'étape ne fait que confirmer le Surprise Gap, la retirer des skills où elle fait doublon ([[methodes/apprentissage-continu]]).
