---
type: methode
title: Stratégie d'un mot-clé business en trois étapes validées
aliases: [strategie-mot-cle-par-etapes]
tags: [seo, mots-cles, geo, methode]
created: 2026-10-24
updated: 2026-10-24
sources: 3
confidence: high
status: stable
---

# Stratégie d'un mot-clé business en trois étapes validées

L'agent `strategie-mot-cle` travaille dans le coffre où la conversation est ouverte. Il part d'un mot-clé business, de l'offre et de l'audience du projet. Il ne réutilise pas les pièces d'un autre client. Sa procédure est dans `.agents/skills/strategie-mot-cle/SKILL.md` ; le contrôle d'ordre est exécuté par `scripts/workflow.py` dans ce même dossier.

Il dirige les demandes « stratégie mot clé X », « stratégie contenu pour mot clé X », « stratégie de contenu pour X », « strat mot clé » et « quoi faire pour le mot clé X ». « Juste pour X » reprend la stratégie du mot-clé dans une conversation où ce contexte est établi. Pour ces demandes, il est prioritaire sur la stratégie de contenu générale ; une phrase isolée sans contexte donne lieu à clarification.

## Ordre de travail

| Étape | Livrable | Validation avant la suite |
|---|---|---|
| 1 | Qualification business, vérification de l'URL existante, puis micro-intentions distinctes et utiles à l'acheteur | Accord explicite de Tim sur le cadrage et les intentions |
| 2 | Questions d'acheteurs recherchées sur le terrain, puis dans les recherches documentées et l'expertise ; hypothèses en complément justifié | Accord explicite de Tim sur les questions |
| 3 | Note de matière `0–5` pour tous les éléments validés, après contrôle des preuves et des données manquantes | Accord explicite de Tim sur la lecture des preuves |

Une réponse livre une seule étape. Une correction relance l'étape courante. Cinq intentions et quinze questions sont des objectifs initiaux souples : un écart doit être justifié, jamais comblé artificiellement. Deux formulations du même besoin sont fusionnées. La notation porte sur le nombre réel d'éléments validés. Aucun nombre de pages ne découle automatiquement de ces listes. [[moc/doctrine-seo-reference]] [[methodes/rapport-mots-cles-format]]

## Qualification business préalable

Avant les intentions, l'agent identifie l'offre à vendre, le prospect à convertir, le problème concret résolu, l'action souhaitée, l'intérêt du mot-clé et une éventuelle URL existante. Il cite les pièces du coffre ou le contexte fourni par Tim. Un point indispensable absent est demandé, sans être deviné. Une intention aide ce prospect à comprendre, comparer, choisir ou acheter ; son lien avec l'offre et sa différence avec les autres besoins sont explicités.

## Recherche des questions

L'ordre est : appels, CRM, SAV et échanges commerciaux ; puis Search Console et recherches documentées ; puis expertise métier ; enfin hypothèses générées pour une lacune nommée. Le journal de recherche conserve les pièces consultées et les absences de données. Une question observée ou issue de l'expertise conserve un extrait vérifiable ; les reformulations sont signalées. Les hypothèses sont présentées après les questions étayées. [[methodes/questions-par-perspective]]

## Méthodes sources

### Trace d'exécution et provenance

Précision globale du 24 octobre 2026, à la suite de la session « consultant SEO Lyon » : annoncer `strategie-mot-cle` et son chemin exact. Le chargement des fichiers Fusionn applique une méthode ; `workflow.py` contrôle et enregistre les étapes. Ces opérations ne sont pas un appel à `generate_micro_intentions` et ne prouvent pas une demande observée. L'indisponibilité de l'outil applicatif est annoncée au lancement.

Dès le premier tableau, préciser pour chaque formulation si elle vient d'une donnée observée, d'une reformulation sourcée ou d'une hypothèse générée. Une hypothèse issue du positionnement commercial reste une hypothèse. Une relance après contestation vérifie l'écart avant de modifier le livrable ; soumettre à nouveau le même JSON n'ajoute aucune observation. La validation d'une étape reste distincte d'une demande de lancer le skill. [[corrections-recurrentes]]

Fusionn fournit le skill `micro_intentions` (`~/Code/newFusionn/scripts/sync-skills.mjs`) et l'outil `generate_micro_intentions` (`~/Code/newFusionn/supabase/functions/generate-micro-intentions/index.ts`). L'agent reprend leur taxonomie et leurs critères de formulation, vérifie les fichiers et trace leur version. L'outil applicatif Fusionn n'est pas exécuté depuis ce coffre ; ses scores prédictifs ne servent pas à noter la matière.

Le skill `geo-citations` (`~/.claude/skills/geo-citations/SKILL.md`) apporte ses règles de provenance et de mesure. Les questions conservent d'abord la formulation et les besoins des acheteurs. Leur transformation en panel de prompts pour les moteurs IA est une adaptation ultérieure distincte. Le suivi de présence et de recommandation requiert des appels API payants et son propre accord. Les hypothèses sont marquées comme telles. [[queries/2026-10-10-geo-citations-consultant-seo-15-questions]]

## Note de matière

Chaque catégorie de preuve propriétaire admissible vaut un point : contexte réel, méthode maison, cas appliqué, verbatim attribué, mesure sourcée. Le score maximum est cinq. Plusieurs pièces d'une catégorie comptent une fois. Chaque preuve nomme l'affirmation précise qu'elle soutient et possède un extrait retrouvé dans le fichier source. Sa pertinence directe, sa fiabilité, son actualité et son exploitabilité sont évaluées et justifiées avant tout comptage. Une preuve indirecte, externe, peu fiable, périmée ou inexploitable est conservée avec la raison de son exclusion et ne marque aucun point.

L'ancienneté est appréciée selon le sujet : une méthode ancienne toujours applicable peut rester actuelle, avec justification. La date source connue, la date du contrôle et les raisons de qualification sont conservées. Une mesure précise sa période ; un verbatim son attribution. Le contrôleur vérifie l'extrait, les évaluations et le calcul ; Tim valide la lecture sémantique et la qualité des pièces.

Une note basse, y compris `1/5`, indique les données à collecter pour bien traiter le sujet. La valeur business de ce sujet reste une dimension indépendante. [[concepts/preuve-atomique]] [[methodes/rapport-mots-cles-format]]
