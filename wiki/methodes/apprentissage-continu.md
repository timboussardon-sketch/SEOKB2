---
type: methode
title: Apprentissage continu du système SEO KB
aliases: [regle-apprentissage-continu]
tags: [meta, apprentissage, preuves, methode]
created: 2026-10-08
updated: 2026-10-24
sources: 1
confidence: high
status: stable
---
# Apprentissage continu du système SEO KB

## Statut et origine

Règle d’organisation demandée explicitement par Tim dans la conversation du 8 octobre 2026 : « non pas de pilote, eccris la regle d'apprentissage continu ». Inscrite dans AGENTS.md §14. Le statut stable porte sur cette consigne de fonctionnement, pas sur la validation de résultats SEO.

## Principe

Chaque tâche, correction ou mesure peut enrichir le système. L’agent recherche un enseignement utile, conserve la preuve et le retrouve lors de la prochaine tâche comparable. Si rien de nouveau n’est établi, il n’ajoute pas de leçon artificielle.

Le chemin est : observation sourcée → hypothèse → confrontation aux preuves → résultat contextualisé → règle validée.

## Enregistrer au bon endroit

| Matière | Destination existante | Traitement |
|---|---|---|
| Fait, résultat ou erreur d’une boucle équipée | `ledgers/` de la boucle | Ajouter une entrée sans effacer l’historique ; respecter son schéma |
| Correction de Tim | [[corrections-recurrentes]] | Appliquer §6.4 ; distinguer occurrence isolée et récurrence |
| Explication non établie | [[hypotheses]] | Garder ouverte avec contre-argument et preuve attendue |
| Performance d’un contenu ou d’une intervention | [[preuves/index]] | Baseline, réalisation effective, source, jalon, résultat et limites |
| Résultat contraire à une règle existante | [[contradictions]] | Référencer la règle et les preuves contradictoires |
| Proposition de changement durable | `memory/questions.md` si la boucle en possède un, sinon [[revue-hebdo/index]] | Présenter une modification précise à Tim |
| Instruction ou arbitrage explicite | [[decisions/index]] si structurant, et [[log]] | Tracer l’autorisation et les fichiers effectivement modifiés |

Ne pas créer un second registre concurrent. Relier les entrées plutôt que recopier les preuves. Préserver les sources originales et les vues générées.

## Distinguer trois niveaux

**Observation** : ce qui s’est passé, avec date, source, contexte, action effectivement réalisée et version concernée lorsqu’elle est connue. Une acceptation ne prouve pas un déploiement. Une absence de retour ne prouve pas une réussite.

**Interprétation** : explication candidate, contre-arguments, autres causes possibles, données manquantes et périmètre supposé. Ne pas présenter une corrélation comme une causalité. Ne pas compter plusieurs résumés de la même source comme plusieurs confirmations.

**Proposition** : au plus une modification par méthode et par revue ; préciser ce qui changerait, pourquoi, où cela s’appliquerait, ce qui compterait comme réussite ou échec et comment revenir à la version précédente. Conserver la méthode validée tant que son remplacement n’est pas autorisé.

## Quand conclure

Les corrections explicites et les erreurs directement vérifiables sont enregistrées pendant la tâche. Les résultats SEO se jugent aux jalons prévus avec des données exploitables ; la fréquence de collecte ne dicte pas la fréquence des conclusions.

Avant d’interpréter un silence, consulter [[ops/sante-automatisations]] et vérifier la collecte concernée. Distinguer échec observé, manque de données et résultat indécidable. Chercher activement les contre-exemples avant toute généralisation. Une réussite locale reste limitée à son contexte tant que son extension n’est pas étayée.

## Contrôle des publications avant la mesure GSC

`wiki/apprentissage/publications.jsonl` conserve des candidats issus des sessions. Une commande de déploiement et une URL citée ne suffisent pas à établir qu'une page a été publiée à la date inscrite. `.claude/bin/apprentissage-preuves.py` construit deux vues régénérables : `publications-verifiees.json` et `publications-refusees.json`. Le calcul des jalons GSC ne lit que la première. Une capture HTTPS au moment de la mise en ligne doit attester le statut 200, l'URL canonique et `article:published_time` ; son empreinte SHA-256 est contrôlée à chaque rejeu. Les refus gardent la référence à la ligne du registre et le motif, sans recopier les URL à paramètres.

La commande de capture et le schéma sont documentés dans `.claude/commands/apprentissage.md`. Les anciens résultats de [[apprentissage/preuves-auto]] ne sont plus des verdicts tant que leur date de publication n'est pas établie. Une capture tardive ne prouve pas rétroactivement cette date. Un registre historique vide de preuves donne donc zéro verdict, ce qui est un état de preuve insuffisante, pas une mesure SEO nulle.

## Faire évoluer la règle

L’agent entretient les faits et prépare les propositions. Tim autorise les changements durables de méthode, de skill ou de doctrine. Une instruction explicite déjà donnée suffit : ne pas redemander la même validation. Les corrections ponctuelles autorisées se traitent immédiatement.

À la prochaine tâche comparable, relire les leçons pertinentes et référencer celles qui sont appliquées. Si un résultat les contredit, rouvrir l’examen et conserver la trace de la révision ; ne pas effacer les échecs ou les anciennes versions pour rendre l’historique plus flatteur.

## Format minimal d’un enseignement

À utiliser dans le registre adapté, en respectant son schéma existant :

- Date, tâche et contexte.
- Observation et lien vers la preuve.
- Version ou action réellement effectuée ; inconnue si non documentée.
- Explication candidate et contre-argument.
- État : observation, hypothèse, proposition ou règle explicitement validée.
- Périmètre, prochaine vérification et enseignement antérieur concerné.
- Autorisation de Tim et référence de la modification, si elle existe.

Cette consigne s’applique aux tâches et revues existantes. Elle ne lance aucun pilote et n’installe aucune automatisation.

Pages liées : [[hypotheses]] · [[preuves/index]] · [[corrections-recurrentes]] · [[revue-hebdo/index]].
