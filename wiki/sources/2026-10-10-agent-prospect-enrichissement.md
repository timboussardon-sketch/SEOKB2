---
type: source
source_type: test-terrain
title: Enrichissement de la base Agent Prospect du 10 octobre 2026
aliases: [enrichissement-agent-prospect-2026-10-10]
tags: [prospection, avocats, donnees, agents]
created: 2026-10-10
updated: 2026-10-10
sources: 1
confidence: high
status: stable
---

# Enrichissement de la base Agent Prospect

À la demande de Tim, l’inventaire existant de contacts nominatifs a été rapproché de PostgreSQL `agent_avocats`. Le projet actif est `~/Code/prospection/agent-avocats`, dashboard http://localhost:3456/recap. Le projet séparé `agent-prospection`, arrêté, n’a pas été modifié.

## Résultat mesuré

L’import transactionnel a ajouté 131 cabinets, 161 emails nominatifs et 144 interlocuteurs. Les totaux après import sont 1 117 cabinets, 1 051 contacts et 2 775 interlocuteurs. Les 131 nouveaux prospects appartiennent à la campagne `19faa86f-6cd8-4f4b-8209-4b47a793c373`, laissée DRAFT, avec qualification PENDING et envoi bloqué. Aucun brouillon n’a été créé. Le nombre d’envois enregistrés est inchangé avant et après.

Preuve : `~/Code/prospection/agent-avocats/prospection-avocats/enrichissement-2026-10-10/`, fichiers `avant.json`, `entree.json`, `plan.json`, `resultat.json` et `rapport.md`. Les identifiants de chaque ajout et les sources de chaque contact sont archivés dans `resultat.json`. L’événement PostgreSQL `DATA_ENRICHMENT_IMPORT` trace l’opération.

## Limites et exceptions

Parmi les 300 lignes d’entrée, 78 ont un envoi retrouvé dans l’historique local. Les 43 lignes exclues de l’import correspondent à quatre sites remplacés par une URL d’annuaire, deux rattachements ambigus et 37 contacts déjà écartés. Les exclusions existantes ont été préservées.

Les 300 domaines email ont répondu avec un MX au contrôle préparatoire. Lors du second relevé, 297 ont répondu et trois ont atteint le délai d’attente : MAJJ Avocats, Sequoia Avocats et Barthélémy Avocats. Leur dernier relevé reste indéterminé. Un MX ne confirme pas l’existence d’une boîte. Les pages sources n’ont pas été relues pendant cet import et les 279 tailles de cabinets restant à confirmer n’ont pas été contrôlées.

## Observation réutilisable

Dans ce lot, un email nominatif sourcé peut coexister avec un site d’annuaire ou une exclusion déjà enregistrée. Le rapprochement par domaine et adresse, puis la conservation des exclusions, ont empêché leur import automatique. Cette observation concerne le lot archivé ; aucune règle de l’agent n’a été modifiée.

Pages liées : [[agents/agent-avocats]] · [[methodes/apprentissage-continu]].

## Correction de cadence demandée ensuite

Le 10 octobre, Tim demande « tu dois corriger à 100 ». Dans le projet actif, `.env.local` et `.env.example` portent désormais `DAILY_SENDS=100`, `MAX_SENDS_PER_DAY=100` et `SEND_SPACING_MINUTES=4`. La plage reste les jours ouvrés de 9 h à 17 h, heure de Paris. Le worker et le serveur web ont été rechargés ; la mission du jour en base affiche un objectif de 100. Contrôle HTTP de `/missions` et simulation des créneaux depuis les fonctions de production : 100 passages autorisés dans la plage. Aucun email réel envoyé par cette vérification. La sélection exclusivement nominative reste à corriger avant les prochains envois.
