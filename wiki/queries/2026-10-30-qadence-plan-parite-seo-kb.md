---
type: query
title: Plan complet de parité QADENCE et seo-kb
tags: [qadence, agents, architecture, connaissance]
created: 2026-10-30
updated: 2026-10-30
sources: 0
confidence: medium
status: draft
---

# Plan complet de parité QADENCE et seo-kb

Objectif demandé par Tim : obtenir le même niveau de fonctionnement, de mise à jour et de qualité des réponses que seo-kb pour chaque projet et chaque agent QADENCE. Référence de conception : [[queries/2026-10-30-qadence-parite-seo-kb]]. La parité reste à démontrer sur des cas réels.

## État au départ

Le code local possède des sources par projet, une mémoire, un journal, des traces de workflow et plusieurs chemins d'agents. La copie isolée `/private/tmp/qadence-kb-consolidation` contient un prototype de partage des résultats terminés et deux tests unitaires. Il ne crée pas de fiches sourcées ni de registres : ce n'est pas une parité. Aucun changement du prototype n'est intégré dans le dépôt QADENCE. La production n'a pas été inspectée.

## Plan de réalisation

| Étape | Travail concret | Terminé quand |
|---|---|---|
| 1. Inventaire | Cartographier les agents conversationnels, planifiés et squad ; leurs outils, skills, sources, écritures, cadences et points de lecture. Comparer les versions du dépôt, du serveur et de la base. | Chaque chemin a un responsable, une entrée et une sortie identifiés ; écarts et inconnues documentés. |
| 2. Modèle commun | Concevoir les objets projet : source et versions, fiche source, concept, entité, synthèse, livrable, hypothèse, contradiction, décision, preuve, événement et liens. Définir accès, version, provenance, statut et historique. | Schéma et migration réversible vérifiés sur une base de test ; aucune donnée client perdue. |
| 3. Sources et ingestion | Conserver l'original et ses versions ; analyser, sélectionner les passages, relier les citations aux fiches ; suivre le backlog et les erreurs. Réutiliser `project-sources`. | Une source ajoutée est consultable jusqu'au passage exact ; une source modifiée conserve son historique. |
| 4. Contexte partagé | Construire la recherche filtrée par projet et la récupération des décisions, fiches et preuves utiles. Associer la version de doctrine et des skills à chaque exécution. | Deux agents retrouvent le même fait sourcé sans accéder aux données d'un autre projet. |
| 5. Écriture des agents | Raccorder `seo-agent`, `agent-auto`, `seo-squad` et les autres agents réellement actifs à un contrat commun. Consolider les propositions, conserver les traces et empêcher les doublons. | Chaque exécution terminée produit une trace et des mises à jour attribuées ; toute erreur est visible et rejouable. |
| 6. Décisions et validation | Distinguer constat, hypothèse, recommandation et décision ; conserver les corrections, les versions et les contradictions. Maintenir les validations humaines des workflows. | Une proposition ne devient pas une décision sans validation ; une correction est visible au prochain travail. |
| 7. Boucles de mise à jour | Mettre en place backlog, revue des hypothèses et contradictions, mesures GSC et preuves, revue périodique et résurgence. Définir cadence, déclenchement et limites par projet. | Une source, un résultat et une contradiction traversent leurs boucles avec une sortie datée. |
| 8. Santé des routines | Comparer les échéances, dernières exécutions et dernières sorties ; détecter les échecs, absences et données périmées. Réutiliser la surveillance existante. | Un agent silencieux et une source GSC figée sont signalés avec date et cause si connue. |
| 9. Qualité des réponses | Comparer QADENCE et seo-kb sur des cas de référence : sources, doctrine, contexte client, outils réellement appelés, limites, décisions et mise à jour. Corriger les écarts observés. | Chaque cas a un verdict et ses preuves ; aucune parité annoncée sur la seule base de prompts ou de tests unitaires. |
| 10. Intégration et livraison | Revoir les modifications du dépôt, exécuter les tests, préparer migrations, séquence de déploiement et retour arrière ; vérifier le fonctionnement sur un projet contrôlé. | Code intégré, tests pertinents réussis et exécution réelle vérifiée. Une mise en production nécessite une autorisation explicite distincte. |

## Tests de bout en bout

- Une source est ajoutée, un agent crée une fiche reliée aux passages, puis un autre agent la retrouve et cite la source.
- Une donnée contradictoire ouvre une contradiction ; la correction d'un utilisateur est conservée et prise en compte à la session suivante.
- Un outil indisponible ou une exécution tronquée produit un état incomplet, sans décision validée ni fait présenté comme vérifié.
- Un travail relancé ne crée pas de doublons. Une écriture interrompue est détectée et peut être reprise.
- Deux comptes et deux projets ne peuvent pas lire ou modifier leurs données respectives.
- Un agent planifié qui cesse de produire et une source de données périmée sont détectés.
- Les mêmes questions et données sont soumises à seo-kb et à QADENCE ; un relevé conserve les différences de sources, raisonnement, limites, décisions et mises à jour.

## Dépendances et contrôles

Vérifier les migrations et fonctions effectivement déployées avant toute modification distante. Identifier la source de vérité des skills et les versions actives. Prévoir un retour arrière pour les migrations et une sauvegarde des données concernées. La base commune de doctrine doit être séparée des données privées des clients. Les sorties d'un modèle restent attribuées à leur exécution et ne deviennent pas des preuves indépendantes.

## Suivi

| Lot | Statut | Preuve |
|---|---|---|
| Conception de principe | Validée par Tim | [[queries/2026-10-30-qadence-parite-seo-kb]] |
| Inventaire local | En cours | Cartographie partielle dans la conception |
| Prototype de mémoire | En cours | Copie isolée ; contrôle TypeScript et deux tests unitaires réussis |
| Production | Non vérifiée | Aucun appel ni déploiement attesté |
| Parité | Non démontrée | Tests de bout en bout et comparaison à réaliser |

Pages liées : [[moc/moc-methode-kb]] · [[ops/sante-automatisations]] · [[moc/doctrine-seo-reference]].
