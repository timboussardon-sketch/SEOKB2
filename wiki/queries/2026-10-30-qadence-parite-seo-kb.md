---
type: query
title: QADENCE — parité de fonctionnement avec seo-kb
tags: [qadence, agents, kb, architecture]
created: 2026-10-30
updated: 2026-10-30
sources: 0
confidence: medium
status: draft
---

# QADENCE — parité de fonctionnement avec seo-kb

Proposition de conception à valider. La référence est [[moc/moc-methode-kb]] et la doctrine [[moc/doctrine-seo-reference]]. Le code local de QADENCE a été lu ; la configuration et les données de production n'ont pas été vérifiées.

## Comportement attendu

Chaque projet dispose d'une base persistante. Avant une réponse ou une tâche planifiée, l'agent lit les décisions, sources et travaux pertinents, leur date et leurs limites. Après une exécution terminée, il propose les changements aux fiches concernées, enregistre les sources et outils effectivement utilisés, puis journalise le résultat. Les décisions engageant le client attendent sa validation. Les exécutions incomplètes gardent une trace de l'échec et ne produisent pas de constat présenté comme validé.

## Structure cible par projet

| Objet | Contenu et liens |
|---|---|
| Source brute | Original ou instantané daté, provenance, auteur, empreinte, accès et version. Une mise à jour crée une version. |
| Fiche source | Résumé, passages et limites ; références à la version brute et aux extraits. |
| Fiche de connaissance | Concept, entité, synthèse ou livrable ; contenu versionné, statut, confiance, liens et références aux preuves. |
| Registre | Hypothèses, contradictions, décisions, actions et preuves de résultats, reliées aux fiches et exécutions. |
| Journal | Événement daté par opération : agent, projet, méthode et version, outils réellement appelés, résultat et modifications. |
| Index | Recherche lexicale et sémantique filtrée par projet, type, date, statut et source ; liens entrants et sortants. |

Une base de doctrine et de méthodes commune est versionnée séparément des données privées des projets. Chaque exécution conserve la version utilisée. L'accès aux données est contrôlé pour chaque compte et projet. Les données existantes sont reprises avec leur provenance disponible ; une origine absente reste indiquée comme inconnue.

## Cycle d'un agent

1. Identifier le projet, la demande, la méthode et les données nécessaires. Charger l'état et les sources pertinents.
2. Exécuter les outils nécessaires et conserver leurs résultats, dates, périmètre et erreurs.
3. Produire une réponse qui distingue mesure, fait sourcé, hypothèse et recommandation. Une donnée indisponible reste signalée.
4. Préparer les changements de fiches, liens, registres et index. Détecter les conflits et conserver l'historique des versions.
5. Enregistrer le résultat et la trace ; appliquer les validations humaines prévues par le workflow avant de faire avancer son état.
6. Permettre à un autre agent de retrouver les changements et les preuves lors de sa prochaine tâche.

## Entretien continu

Reprendre les boucles de [[decisions/0001-fermeture-boucles-systeme]] : sources en attente de traitement, revue des hypothèses et contradictions, mesure des résultats, revue des décisions et résurgence des connaissances anciennes. Chaque routine possède une cadence, une dernière exécution réussie, une dernière sortie et un état de fraîcheur. Une routine attendue sans exécution ou sans sortie est signalée. Les cadences et activations par projet restent à définir lors de l'implémentation.

## Écart constaté dans le code local

`supabase/functions/agent-auto/index.ts` conserve la réponse dans une conversation et journalise le run ; il appelle `seo-agent`, qui peut écrire certaines mémoires, mais ce chemin ne garantit pas une mise à jour structurée commune après chaque exécution. `distill-session` écrit journal, mémoire et état à la fermeture d'une conversation. `project-sources` traite des passages sourcés. `agents-health` et `cron-agents-watchdog` agrègent des exécutions et erreurs ; le watchdog lu ne détecte pas à lui seul une absence totale de runs attendus. Ces observations concernent les fichiers locaux, pas la production.

## Ordre d'exécution proposé

1. Cartographier les chemins réels des agents, les données et automatismes déployés, les méthodes actives et leur version ; relever les écarts avec la cible.
2. Définir le modèle de données, les droits et la migration réversible depuis les tables existantes.
3. Brancher lecture commune, écritures versionnées et journal sur tous les chemins d'agents, avec suivi des échecs.
4. Ajouter les boucles d'entretien et leur surveillance, puis la recherche et les liens entre connaissances.
5. Comparer les réponses et les mises à jour de QADENCE à des cas de référence seo-kb, avant toute mise en production.

## Inventaire du code local — 30 octobre

Le registre `seo-agent/agents16.ts` déclare les missions suivantes : audit, indexation, vitals, GEO, rapport, gains, cannibalisation, maillage GSC, maillage structure, mots-clés, clustering, décisionnels, brief, FAQ et pré-audit. Chaque mission nomme un skill principal et un livrable. Le nombre réellement actif et les versions en base restent à vérifier. `agent-auto` définit des tâches et cadences pour ces missions ; il appelle le même moteur `seo-agent`, écrit dans le fil de l'agent et enregistre un run. Le travail de l'agent peut aussi appeler des outils de mémoire ; la mise à jour complète de la base ne constitue pas une étape obligatoire de ce chemin.

| Chemin local | Lecture ou écriture observée | Travail à préparer |
|---|---|---|
| `seo-agent` | Lit mémoire, état et journal ; trace les outils et la version du skill ; écrit des faits et décisions via ses outils. | Contexte commun récupérable par objet et preuve ; écriture structurée et contrôle de complétude. |
| `agent-auto` | Appelle `seo-agent` ; conserve fil, statut du run et notification. | Déclencher la consolidation partagée après succès et tracer les échecs de consolidation. |
| `seo-squad` | Le chargeur de skill lit la mémoire projet. | Cartographier chaque agent et brancher le même contrat de contexte et de mise à jour. |
| `distill-session` | Produit journal, faits et état projet à partir d'une conversation. | Préserver les preuves et versions ; distinguer fait, proposition et décision validée. |
| `project-sources` | Traite des passages avec citations, sélection utilisateur et recherche. | Relier les passages retenus aux fiches, hypothèses et livrables qui les utilisent. |
| `agents-health` et watchdog | Agrègent les runs et les erreurs observés. | Comparer chaque échéance active à sa dernière exécution et sa dernière sortie. |

La table locale décrite par `20261024093000_agent_execution_traces.sql` prévoit déjà la version du skill, les outils et le statut du workflow. La réutiliser après vérification du schéma déployé, plutôt que créer une deuxième trace concurrente. Les documents historiques d'audit ne prouvent pas l'état actuel des crons ni des skills en production.

## Préparation du premier changement

Le premier changement proposé est un contrat partagé de consolidation : une exécution terminée transmet son identifiant de trace, son périmètre projet, les sources et les modifications proposées à un seul point d'écriture. Celui-ci enregistre les versions et les liens, puis indique explicitement succès ou échec. Les appels répétés avec le même identifiant ne doivent pas dupliquer les écritures. Les traitements partiels ne valident aucune décision. Les chemins `seo-agent`, `agent-auto` et `seo-squad` doivent y être raccordés après cartographie détaillée de leurs sorties.

Vérifications prévues : reprise après erreur, absence de doublon, isolation entre projets et comptes, suivi des sources, visibilité d'une contradiction et réutilisation par un autre agent. Avant migration ou déploiement, comparer le schéma et les fonctions réellement en production avec les fichiers locaux.

## Critères d'acceptation

Sur un projet de test, un agent ingère une source et crée une fiche reliée aux passages exacts ; un second agent retrouve ces informations et les cite dans sa réponse. Une contradiction est conservée et signalée ; une correction utilisateur se retrouve dans le travail suivant. Une tâche incomplète reste visible comme telle. Une routine attendue mais absente apparaît en retard. Un autre compte ne peut pas lire le projet. Une comparaison sur des cas identiques vérifie la qualité des réponses, la provenance, les versions et les limites ; la parité n'est annoncée qu'après ce contrôle.

Pages liées : [[moc/moc-methode-kb]] · [[ops/sante-automatisations]] · [[moc/doctrine-seo-reference]].
