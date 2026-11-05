---
type: moc
title: Doctrine SEO de référence
aliases: [doctrine-seo, reference-doctrine-seo]
tags: [seo, doctrine, reference, skills, audit, mots-cles, maillage, indexation]
created: 2026-09-30
updated: 2026-10-21
sources: 6
confidence: high
status: stable
---

# Doctrine SEO de référence

> Document à ouvrir en premier dès qu'une question porte sur la doctrine SEO de Tim : comment on choisit un mot-clé, comment on audite, comment on maille, comment on lit l'indexation, ce que Claude décide et ce que Tim garde. Fixé par Tim le 30/09/2026.

## Règle fondamentale : dashboard de chaque projet

Consigne explicite de Tim du 3 octobre 2026. Chaque nouveau coffre de projet doit intégrer seo-kb et disposer d'un dashboard local créé, lancé, vérifié et présenté dans la même tâche. À chaque ouverture ou reprise de projet, proposer à Tim de consulter son dashboard et envoyer systématiquement le lien localhost cliquable. Vérifier la disponibilité et signaler un éventuel blocage.

Application : [[methodes/tableau-de-bord-par-projet-seo]].

## Règle fondamentale : rédaction en 4 phases validées

Consigne de Tim du 21 octobre 2026 : « TOUJOURS RESPECTER, TOUJOURS : brief, structure Hn, ensuite ajoute data dans le Hn, puis rédaction. Chaque phase doit être validée par le consultant. »

| Phase | Livrable | Avant de passer à la suivante |
|---|---|---|
| 1. Brief | Requête, intention, angle, cible | Validation du consultant |
| 2. Structure Hn | H1, H2, H3 seuls | Validation du consultant |
| 3. Data dans les Hn | Chiffres, sources, verbatims et cas sous chaque Hn ; trou = `[MATIÈRE MANQUANTE]` | Validation du consultant |
| 4. Rédaction | Texte tiré de la seule data validée en phase 3 | Validation du consultant |

Une phase par réponse, puis arrêt. Le silence ne vaut pas validation ; une correction relance la même phase.

Application : AGENTS.md §12, skills `seo-workflow-article` et `article-engine-pipeline`.

## Les fichiers de référence

- [[raw/guide-seo-obsidian-claude/matiere-par-section|Matière par section]] : faits, chiffres et process datés sur organikk.co, section par section.
- [[raw/guide-seo-obsidian-claude/skills/seo-mots-cles-business/SKILL|seo-mots-cles-business]] : mots-clés par intention, trois portes, cinq décisions.
- [[raw/guide-seo-obsidian-claude/skills/seo-pre-audit/SKILL|seo-pre-audit]] : pré-audit avant call, données publiques seulement.
- [[raw/guide-seo-obsidian-claude/skills/maillage-systeme/SKILL|maillage-systeme]] : maillage sans Search Console, script de crawl.
- [[raw/guide-seo-obsidian-claude/skills/maillage-interne-gsc/SKILL|maillage-interne-gsc]] : maillage avec Search Console.
- [[raw/guide-seo-obsidian-claude/skills/indexation-check/SKILL|indexation-check]] : audit d'indexation, 9 contrôles.

## Positions arrêtées (tirées de ces fichiers)

- Claude pré-décide, Tim décide. Jamais « décision » dans un livrable de Claude.
- Aucun volume, position ou CPC inventé. Sans donnée : demande observée Faible / Moyenne / Forte avec ses signaux nommés.
- Une requête à fort volume hors offre finit ÉCARTÉE, avec sa raison écrite.
- Aucun score sur 10 pour trier des mots-clés : trois portes (offre, intention business, opportunité démontrée).
- La Search Console ne représente pas tout le marché.
- Jamais de recommandation automatique de fusion, 301, suppression, réécriture ou création de page.
- 404 traitées URL par URL. Jamais une 301 de dossier à dossier.
- `site:` est un indice non exhaustif. « Non testé » n'est pas « non indexé ». « Rien de confirmé » est une réponse autorisée.
- Hors sitemap = constat, pas blocage.
- Maillage : pas de score numérique, priorité par rang justifié. Page d'offre orpheline d'abord.
- Une ancre qui boite à voix haute sans le lien est rejetée. Lots de 10 à 20 liens, crawl relancé après chaque lot.
- Balisage : chaque valeur balisée existe telle quelle sur la page.
- Un rapport : une cause structurante, 3 problèmes au plus, 3 P1 au plus, et ce que les données ne permettent pas de conclure.

## En cas de contradiction

Une règle plus récente dans `~/.claude/skills/` ou dans [[methodes/rapport-audit-seo-format]] prime sur les copies distribuables. Signaler l'écart à Tim, ne pas trancher seul.

Voir aussi [[moc-maillage]], [[moc-aeo-geo]].
