---
type: query
title: "Fusionn : onglet Stratégie fondé sur les missions et les boucles du vault"
tags: [fusionn, strategie, agents, automation, doctrine]
created: 2026-09-12
updated: 2026-09-12
sources: 6
confidence: medium
status: draft
---

# Fusionn : onglet Agent

Nom retenu par Tim : **Agent**, en remplacement de Stratégie dans la navigation. Interface sobre : consigne libre, programmation, liste des travaux et volet de lecture. Exemples à la demande ; pas d’avatar, de slogans, de chips de suggestion ni de badges décoratifs. L’ancien identifiant `strategie` ouvre `agent` pour conserver la compatibilité. Aperçu courant : `/preview-agent`.

> Direction corrigée par Tim : « comme dans POLSIA, il faut créer un endroit pour donner des actions à l’agent mot clé ». L’entrée produit est une consigne adressée à l’agent, suivie de son activité et de son résultat. Le parcours de recommandations à réaliser soi-même, exploré ci-dessous, n’est pas l’interface centrale demandée.

Le prototype courant présente un seul agent mots-clés, un champ libre « Que doit faire l’agent ? », des exemples de consignes et une liste des travaux confiés. Dans le projet connecté, l’envoi utilise l’agent mots-clés existant et son suivi reste dans Agent. Le flux affiche les états, détails et horaires disponibles des étapes ; le chat sert notamment à répondre aux demandes de précision. La consigne est marquée dans l’historique pour réapparaître dans cette liste. L’aperçu sans connexion simule l’exécution et la programmation ; aucun cron réel n’est activé. Les anciens plans restent accessibles en second niveau.


## Recherche

Expansion : P1 missions, agents, stratégie, programmation ; P2 mémoire, skills, routines, boucles ; P3 preuves, décisionnel, jugement, fraîcheur. Entités recherchées : Fusionn, Organikk, Qadence, GSC. Recherche lexicale dans index, concepts, synthèses et sources, suivie des liens vers mémoire, data propriétaire et boucle sortie-mesure.

## Synthèse

L'onglet Stratégie doit traduire les quatre composants décrits par Tim : mémoire du site, compétences méthodologiques, routines programmées et boucles de mesure. Une programmation récurrente déclenche un travail ; elle ne suffit pas à faire apprendre l'agent. Chaque mission doit retrouver les observations et décisions précédentes, vérifier ses données puis conserver son résultat. Cette proposition transpose l'architecture du vault dans Fusionn. [[sources/2026-06-11-organikk-construire-agent-seo-claude]]

La mission commence par un objectif explicite : identifier des pages proches de l'offre à renforcer, rechercher des requêtes décisionnelles ou mesurer des contenus modifiés. Les données Search Console, les mesures Google Ads et le contexte propriétaire remplissent des rôles différents. Une hausse de clics ne démontre pas une hausse des ventes ; les résultats commerciaux restent inconnus sans données de conversion. [[concepts/mots-cles-actionnels]]

Le résultat attendu est une décision argumentée, avec ses sources, son périmètre et la date des observations. L'utilisateur peut accepter, reporter ou rejeter une proposition en conservant son motif. L'automatisation prépare et exécute le travail autorisé ; le jugement stratégique reste humain. [[concepts/dette-cognitive]]

Après une modification réellement effectuée, une mission de mesure revient à J+30 puis J+90. Elle compare les observations, conserve les limites de l'analyse et peut conclure que les données sont insuffisantes. Cette boucle évite de régénérer indéfiniment le même plan sans vérifier ses effets. [[concepts/boucle-sortie-mesure]]

L'interface doit enfin distinguer mission programmée, dernière exécution réussie et fraîcheur des données. Une tâche configurée peut ne plus produire, comme le rappelle le registre de surveillance du vault. [[ops/sante-automatisations]]

## Traduction produit proposée

| Mission | Déclenchement proposé | Résultat |
|---|---|---|
| Revoir les priorités du site | Chaque semaine | Changements depuis le dernier passage et actions proposées |
| Explorer une offre | À la demande ou à une date | Requêtes décisionnelles, regroupements et pages à créer ou renforcer |
| Contrôler le maillage | Chaque mois | Liens internes proposés entre pages pertinentes |
| Mesurer une action réalisée | J+30 et J+90 après sa réalisation | Comparaison datée et conclusion avec limites |
| Préparer la revue stratégique | Chaque semaine | Décisions à arbitrer et résultats à examiner |

Ces missions et cadences sont des propositions produit, pas des fonctionnalités déclarées opérationnelles.

## Sources mobilisées

- [[sources/2026-06-11-organikk-construire-agent-seo-claude]] : architecture mémoire, compétences, routines et boucles.
- [[sources/2026-06-17-algorithme-creez-votre-agent-seo]] : découverte, planification, exécution, vérification et itération.
- [[concepts/mots-cles-actionnels]] : proximité de l'offre et mesure business.
- [[concepts/dette-cognitive]] : place du jugement humain.
- [[concepts/boucle-sortie-mesure]] : retour des résultats à J+30/J+90.
- [[ops/sante-automatisations]] : distinguer tâche configurée et production effective.

## Gaps identifiés

Au moment de cette note, le code de Fusionn relie deux types de travaux aux agents existants : plan de pages et stratégie GEO. Le premier aperçu simulait la programmation. Après le challenge expert fourni par Tim, l’aperçu teste désormais une boucle manuelle centrée sur une action, avec stockage local au navigateur. Le stockage des missions, le déclenchement automatique, les décisions utilisateur persistantes et la boucle de mesure ne sont pas encore branchés. Aucun changement backend n'a été réalisé après le « do it » interrompu.

Le vault fournit la doctrine mais pas le contrat technique de programmation de Fusionn. Gestion des fuseaux, concurrence des exécutions, reprises, coûts et historique doivent être spécifiés lors de l'implémentation. Une mesure de conversions nécessite une source dédiée.

## Questions dérivées

- Quel contrat d'entrée et de sortie doit respecter chaque mission Fusionn ?
- Comment relier une décision acceptée à une modification réalisée puis à sa mesure ?


## Révision après le challenge expert transmis par Tim

L’objet central devient une action identifiable. Parcours : proposée → acceptée, à réaliser → réalisée → en mesure → bilan. Accepter ne démarre jamais le suivi. La déclaration de réalisation conserve sa date, sa description et une référence antérieure. Report et rejet conservent le motif, le périmètre et les conditions de réexamen ; l’historique reste immuable, la décision applicable peut évoluer.

Le cadre de l’entreprise précède les missions : offre, client recherché, objectif, exclusions et capacité. Les missions partagent leurs actions et leurs contraintes. Une relance ne duplique pas les propositions ; créer et renforcer une page sur la même intention exige un arbitrage. Le suivi découle de la réalisation et ne nécessite pas une mission à créer séparément.

Une observation favorable n’est pas une preuve causale ni une règle générale apprise. Les contrôles J+30/J+90 sont des rendez-vous ; ils peuvent conduire à prolonger le suivi ou à un bilan non concluant. Sans source de conversion, aucun gain de clients ne peut être inféré. Le statut des données distingue blocage, couverture partielle, ancienneté, insuffisance et analyse sans recommandation.

Base d’interface retenue pour essai : vue d’ensemble, actions, missions, historique. L’entrée par la vue d’ensemble est une hypothèse de design à tester. Les résultats restent liés aux actions.

Implémentation de démonstration : modèle déterministe de transitions, historique local, arbitrages, réalisation datée, observations et bilans ; 13 tests métier passent. Cela ne valide pas encore l’intégration serveur, les collectes réelles, l’injection par document, la concurrence de deux runs ni le rendu navigateur. Le plafond implémenté est une capacité simultanée ; le quota mensuel et l’application automatique des exclusions restent à construire. Priorité retenue : fermer cette boucle manuelle avant les crons.


Correction visuelle de Tim : aucun trait latéral de sélection ou de notification. La sélection repose sur le fond. Correction du suivi : une demande de précision est « À préciser », jamais « Terminée » ; les réponses de cadrage restent rattachées à la même action. L’aperçu local conserve la mention explicite de simulation.
