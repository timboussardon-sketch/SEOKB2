---
type: moc
title: Pôle marketing Organikk
aliases: [marketing, pole-marketing, departement-marketing]
tags: [moc, marketing, commercial, contenu]
created: 2026-10-22
updated: 2026-10-22
sources: 1
confidence: medium
status: living-doc
---

# Pôle marketing Organikk

Créé le 2026-10-22 à la demande de Tim. Cadrage : [[sources/2026-10-22-cameron-england-scaling-agence-coaching]]. Les agents proposent, Tim décide : aucun email envoyé, aucun post publié, personne contacté sans lui.

## Les quatre fichiers tenus

Dans `organikk/marketing/` (porte d'entrée : `organikk/marketing/README.md`) :

| Fichier | Question | Skill |
|---|---|---|
| `origine-clients.md` | d'où viennent les calls et les clients ? | `marketing-origine-clients` |
| `pourquoi-ils-signent.md` | qu'est-ce qui fait signer, ou pas ? | `marketing-pourquoi-ils-signent` |
| `tunnel.md` | quelle étape casse cette semaine ? | `marketing-goulot-tunnel` |
| `plan-contenu.md` | qu'est-ce qu'on publie cette semaine ? | `marketing-plan-contenu` |

## Les canaux et leurs skills

| Canal | Skill | Sortie |
|---|---|---|
| Emailing | `emails` | brouillons de séquences |
| Newsletter Algorithme | `newsletter-ia` | `wiki/revues-presse/` |
| LinkedIn (posts) | `linkedin-post-tim` | `wiki/posts-linkedin/` |
| LinkedIn (prospection) | `linkedin-journal` | `organikk/commercial/linkedin/pipeline.md` |
| X | `x-reply-cockpit` | `~/Code/x-cockpit` |
| Reddit | `reddit-cockpit` | `~/Code/reddit-cockpit/queue/` |
| Blog organikk.co | `organikk-blog-article` | organikk-next |

## Rythme

Vendredi 16 h 30, avant la [[revue-hebdo/index|revue hebdo]] : `com.tim.marketing-hebdo` enchaîne origine, signatures, tunnel puis plan de contenu, et commit `organikk/marketing/`. La revue hebdo de 17 h 30 peut ainsi reprendre l'action proposée par le tunnel.

## Où le retrouver ailleurs

- Messagerie agents, http://127.0.0.1:8967/#m : pôle Marketing dans la réunion d'agents.
- Boucle : `loops/marketing/` (journal des passages).
- Santé : chaque passage réussi écrit `organikk/marketing/passages/AAAA-MM-JJ.md`, que surveillent [[ops/sante-automatisations]] et le health check du lundi (9 jours max).
- Vente et objections : [[moc/moc-vente-objections]] · [[syntheses/vendre-seo-ia-2026]].
