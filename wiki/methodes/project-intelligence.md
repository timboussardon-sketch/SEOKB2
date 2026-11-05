---
type: methode
title: Project Intelligence — reprendre un projet
aliases: [recap-projet, project-intelligence-utilisation]
tags: [projet, pilotage, terminal, suivi]
created: 2026-10-24
updated: 2026-10-24
sources: 3
confidence: high
status: stale
---
# Reprendre un projet

> Annulé à la demande de Tim le 24 octobre 2026. Document historique : le moteur et ses commandes ont été retirés. Le suivi actif est le simple [[pilotage/recap]].


Le récap montre le projet courant, ses résultats documentés, ses attentes et trois prochaines actions au maximum. Le détail garde les preuves et l’historique. L’architecture a été validée par Tim dans la conversation du 24 octobre, puis implémentée ; son audit reste dans [[pilotage/project-intelligence-audit-architecture]].

## Ouvrir le suivi

Depuis seo-kb :

```bash
./kb recap
./kb recap --project organikk
./kb recap --project stopclope --detail
./kb recap --changes
./kb recap --decisions
./kb recap --history
./kb recap --all
```

Pour utiliser le nom court dans le terminal courant :

```bash
source /Users/timothee/Code/seo-kb/recap-shell.sh
recap --project stopclope
```

Ce chargement ne modifie pas la configuration permanente du shell. Sans lui, le lanceur absolu `/Users/timothee/Code/seo-kb/recap` et `./kb recap` fonctionnent. La recherche vectorielle, son environnement Python et le réseau ne sont pas nécessaires.

À la racine seo-kb, le suivi par défaut concerne le système partagé. `--project` choisit un site. Le dossier `wiki/projets/courrier/` identifie Courrier automatiquement. Une attribution ambiguë demande un choix explicite.

Cinq périmètres sont enregistrés : système partagé SEO KB, site Organikk, StopClope, Algorithme et Courrier. `--all` signifie tous les projets enregistrés ; il ne prétend pas couvrir tous les dossiers de l’ordinateur. Les autres projets, dont Qadence, nécessitent leur propre enregistrement et l’examen de leurs pièces.

## Ce que la vue affiche

La vue rapide présente la situation, les changements depuis la dernière vue rapide affichée, les arbitrages ouverts et les prochaines actions. `--detail` déroule les huit blocs : situation, changements, résultats, décisions attendues, blocages, prochaines actions, vigilances et mémoire des décisions.

`--decisions` donne le contexte, les options, la recommandation et ce que chaque choix débloque. `--history` suit les générations conservées et les décisions passées. `--json` fournit les faits structurés avec leur provenance.

Les fichiers modifiés sont détectés même sans entrée au journal. Un changement de fichier n’est pas automatiquement une décision ou une réalisation métier : l’agent doit lire le contenu et mettre à jour les propositions sourcées du contexte. Les sorties des anciens workflows sont importées sans réécrire ces workflows.

## Entretenir le contexte

Le registre `wiki/pilotage/projets.json` associe chaque projet à son dossier, ses sources et son `contexte.json`. Les sources sont explicites, avec des motifs de fichiers lorsque nécessaire. Le journal commun est filtré par entrées attribuées ; ses commits globaux ne sont pas présentés comme des changements du client.

Dans le contexte, conserver les identifiants des actions, leur origine, leur raison, le responsable connu, les dépendances, les blocages et les étapes applicables. Une prochaine action suggérée par l’agent reste une proposition. Une date de revue dépassée déclenche une vigilance ; aucune ancienneté n’est inventée lorsque la date n’est pas connue.

Une action sans identifiant en reçoit un dans le contexte, une fois. Les états de stratégie sont identifiés par leur fichier et leur phase ; les actions de roadmap gardent leur identifiant et leur fichier d’origine. Une proposition refusée garde sa version ; sa reprise utilise le même identifiant et une nouvelle version.

Une déclaration « terminé » sans preuve reste non vérifiée. Un article peut être produit sans être validé, publié ou mesuré. Un blocage, un report, un abandon ou un échec n’efface pas les étapes déjà acquises. Les étapes non applicables exigent une justification.

## Rattacher les preuves

La présence du livrable établit sa production, pas son efficacité. Les contrôles, accords, mises à disposition et mesures exigent des preuves distinctes et versionnées. Chaque référence est relative au projet, autorisée dans ses sources et assortie de son empreinte pour justifier une étape acquise.

Les enregistrements de preuve JSON utilisent :

- `type` : `check`, `approval`, `deployment` ou `measurement` ;
- `subject` et `revision` : action et version concernées ;
- `at` : date d’observation ;
- `targets` : chemin et empreinte de chaque livrable concerné.

Un contrôle ajoute sa commande et son code de sortie. Un accord ajoute l’auteur, son message exact et `approved: true`. Une mise à disposition ajoute son lieu et `observed: true`. Une mesure ajoute sa période, sa source et son résultat, même nul. Une proposition sans livrable utilise `subject_sha256` pour identifier son contenu.

Une décision utilise `type: decision`, son identifiant, sa version, l’empreinte de son contenu, l’issue acceptée ou refusée, l’auteur et le message. Une référence historique n’atteste pas une version nouvelle. Les anciens accords de stratégie sans empreinte restent dans la mémoire, avec cette limite explicite.

Le moteur contrôle les enregistrements locaux ; il ne remplace pas l’observation externe à l’origine d’une preuve. L’agent ne crée pas de capture fictive ni de résultat de test inventé pour faire passer un état.

## Conserver la reprise

Chaque projet conserve son contexte et ses propositions, son état courant, les observations et différences de chaque génération, ses rapports et le repère du dernier passage. Les générations sont conservées dans `wiki/pilotage/projets/<identifiant>/generations/` et le pointeur dans `courant.json`.

Les écritures sont verrouillées et le pointeur ne change qu’après une génération complète. Une interruption laisse l’état précédent utilisable. Si le contexte devient inaccessible, le dernier état complet reste affichable avec un avertissement ; il n’est pas présenté comme actuel.

Une collecte ou une vue ciblée ne consomme pas le dernier passage. Seule une vue rapide affichée avec succès le fait. Une ancienne lecture qui se termine tard ne ramène pas le repère en arrière. Les états identiques ne créent pas de fausse activité.

## Page locale

Le serveur existant affiche les mêmes faits que le terminal, sans le menu latéral du vieux récap :

- http://localhost:8966/ — système partagé ;
- http://localhost:8966/?project=organikk — Organikk ;
- http://localhost:8966/?project=stopclope — StopClope ;
- ajouter `&view=detail` pour les huit blocs.

Le rapport manuel précédent est conservé dans [[pilotage/recap-manuel-2026-10-24]]. Le pilotage ne publie, ne transmet et ne lance aucune tâche métier à lui seul. Les validations de rédaction restent celles de [[moc/doctrine-seo-reference]].
