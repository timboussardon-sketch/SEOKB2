---
name: roadmap-prestation
description: "Ordre des tâches d'une prestation SEO/GEO, du jour 0 à l'autonomie, par client. « nouveau client », « par quoi on commence »."
---

# roadmap-prestation — `/roadmap-prestation`

## Quand utiliser ce skill

Roadmap de prestation SEO/GEO d'Organikk, apprenante. Tient un playbook MAÎTRE et ordonné de tout ce qu'on fait sur un client (du jour 0 à l'autonomie), et un tracker par client. Deux modes : BRIEF (un nouveau client arrive → ressort la séquence ordonnée "fais ça en 1, ensuite ça, etc." adaptée au client) et APPRENTISSAGE (après chaque tâche faite sur un client → la consigne comme étape dans le playbook + met à jour le tracker du client). Mémoire dans prestation/. Ne fait pas le travail des autres skills, il orchestre leur ORDRE et capitalise.

TOUJOURS utiliser ce skill quand l'utilisateur dit : "/roadmap-prestation", "nouveau client", "par quoi on commence pour [client]", "qu'est-ce qu'on fait pour ce client", "roadmap de prestation", "ajoute ça à la roadmap", "étape suivante pour [client]", "où on en est sur [client]", ou après avoir terminé une tâche client à capitaliser dans la séquence de livraison.

Capitalise la **séquence de livraison client** d'Organikk dans un playbook qui s'enrichit à chaque mission. Objectif : quand un nouveau client arrive, dérouler une roadmap ordonnée et éprouvée au lieu de réimproviser. Même esprit que `content-brain` / SyntheticBrain (briefing → action → apprentissage), mais sur le **process de prestation**, pas sur le contenu.

Ce skill n'exécute pas le SEO lui-même : il dit **dans quel ordre** invoquer les autres skills et **capitalise** ce qui a marché.

## Constantes

- Racine : `prestation/`
- Playbook maître : `prestation/roadmap.md` (15 étapes + 2b, 5 phases, source de vérité)
- Interview de cadrage : `prestation/interview-cadrage.md` (batterie ~20 questions + protocole, étape 2b)
- Tracker client : `prestation/clients/<slug>.md` (copier `_template.md`)
- Log : `prestation/log.md` (append-only)
- Date du jour : `date +%F`

## Gate de validation (OBLIGATOIRE, à chaque étape)

Ne jamais dérouler ni exécuter une étape sans faire valider la direction par Tim. À chaque étape, poser une **question concrète** (outil AskUserQuestion, 2 à 4 options réelles, jamais « est-ce que je peux ? »). Trois points de contrôle :

1. **Cadrage de séquence** (début de BRIEF) : faire valider l'ORDRE et la priorité. « On attaque quoi en premier : A, B ou C ? » avec le pourquoi de chaque option (data à l'appui).
2. **Direction de l'étape** (AVANT d'exécuter l'action retenue) : faire valider l'ANGLE, le périmètre et la cible précise du livrable. Ex. pour des entités : quelle page cible, quel angle prioritaire (défense vs reconquête vs nouvelle requête). On n'exécute pas tant que ce n'est pas tranché.
3. **Validation du livrable** (APRÈS production, AVANT de capitaliser et de passer à la suite) : montrer le résultat en 3 lignes et demander « ça va dans le bon sens, je capitalise et j'enchaîne, ou on ajuste ? ».

Règle : Tim valide la direction, l'agent exécute. En cas de doute sur l'angle, demander plutôt qu'assumer. Une seule question à la fois, nette, avec une reco en première option.

## Mode BRIEF — un nouveau client / "par quoi on commence pour X"

1. Lire `roadmap.md` en entier (la séquence maître) + `clients/<slug>.md` s'il existe.
2. Si le client n'a pas de tracker, en créer un depuis `_template.md` (demander à Tim : domaine, type, offre, data dispo).
2b. **Interview de cadrage (étape 2b, avant tout diagnostic).** Si le cadrage n'est pas déjà validé dans le tracker : faire tourner le scan public de `seo-pre-audit`, puis dérouler la batterie de `interview-cadrage.md` en rounds `AskUserQuestion` (options pré-remplies avec les hypothèses du scan). Produire le bloc « Ce que j'ai compris » et le faire valider par Tim (c'est un gate) avant de passer au diagnostic data. Stocker la version validée dans la section « Cadrage (interview) » du tracker. Ne jamais dérouler la séquence sans ce cadrage.
3. Sortir la **séquence ordonnée adaptée au client** : étape 1, puis 2, etc. Pour chaque étape : l'objectif en une ligne, le(s) skill(s) à invoquer, l'input requis (de Tim ou du client), l'output attendu et où il va.
4. Marquer ce qui est **bloqué** faute d'accès/data (ex. pas de GSC → étape 3 en attente) et ce qui est **déjà fait** si le tracker l'indique.
5. **Gate 1 (cadrage séquence)** : poser la question de priorité (A/B/C), avec reco en première option. Attendre la réponse.
6. **Gate 2 (direction de l'étape)** : sur l'action retenue, poser la question d'angle/périmètre/cible. Attendre la réponse.
7. Exécuter l'action via le bon skill, puis **Gate 3 (validation du livrable)** avant de capitaliser.

Règle : on suit l'ordre des phases (cadrage → diagnostic data → stratégie → production → système/autonomie). On ne saute pas le diagnostic data : la stratégie se décide sur la GSC réelle, jamais à l'aveugle.

## Mode APPRENTISSAGE — après une tâche faite sur un client

Déclencheur : Tim dit "ajoute ça à la roadmap", ou on vient de finir une tâche client capitalisable. Ne capitaliser qu'APRÈS le Gate 3 (livrable validé par Tim).

1. Identifier à quelle **étape** du playbook la tâche correspond (ou si c'est une étape nouvelle).
2. Mettre à jour `clients/<slug>.md` : ligne dans le journal des étapes (date, n° étape, action, output `[[lien]]`, skill), avancer "Où on en est".
3. Mettre à jour `roadmap.md` SI la tâche apprend quelque chose de réutilisable :
   - une étape doctrine devient **éprouvée** (avec le client de référence) ;
   - une étape manquait → l'ajouter à la bonne phase, dans l'ordre ;
   - l'ordre se révèle faux → réordonner, en notant pourquoi.
   Ne jamais réécrire le playbook de mémoire : on ne touche que ce que la tâche réelle justifie.
4. Append dans `log.md` : `## [date] <client> | étape N | action`.
5. Mettre à jour la date "Dernière mise à jour" de `roadmap.md` et son "Index clients".

## Garde-fous

- Le playbook distingue **éprouvé** (fait sur un vrai client) de **doctrine** (prévu). On ne marque éprouvé qu'avec un client de référence réel.
- Pas d'invention de chiffres ni de résultats client : tout output pointe vers un fichier réel du vault.
- Les étapes qui invoquent un autre skill nomment ce skill exactement (cf. les 13 skills SEO + content-brain).
- Données et process : autonome. Décisions d'engagement client (prix, périmètre) : Tim tranche.
- Après édition du vault, proposer `./kb rebuild`.

## Articulation

- Avec `content-brain` : roadmap-prestation dit *quand* produire du contenu (étape 12), content-brain le *produit* et apprend par projet.
- Avec `seo-agent-audit` : l'audit autonome couvre les étapes 3 à 5 (diagnostic), roadmap-prestation l'ordonne dans la prestation globale.
- Avec le commercial (process async LinkedIn) : le commercial amène le client, roadmap-prestation prend le relais à la signature.
