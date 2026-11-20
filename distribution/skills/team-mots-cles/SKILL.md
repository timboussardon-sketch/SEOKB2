---
name: team-mots-cles
description: >-
  Pilote de la team mots-clés : la session pilote lance six agents spécialisés sur les
  14 étapes du workflow mots-clés complet, conserve l'état du projet et soumet cinq
  livrables à l'accord de l'utilisateur (cadrage, données, mots-clés business, clusters, rapport).
  Déclencheurs : « recherche de mots-clés », « recherche mots-clés », « keyword research »,
  « kw research », « trouve-moi des mots-clés », « quels mots-clés cibler », « quel mot-clé
  attaquer », « quels mots-clés attaquer », « sur quels mots-clés se positionner », « sur quoi
  se positionner », « stratégie mots-clés », « stratégie mot-clé » sans terme précis,
  « strat mots-clés », « audit mots-clés », « liste de mots-clés pour [client] », « team mots-clés », « lance mots-clés », « workflow mots-clés
  complet », « les 14 étapes », « rapport de pré-décision mots-clés ». « C'est quoi la
  suite ? » reprend le projet mots-clés identifiable. Un terme précis (« stratégie mot clé
  X », « quoi faire pour le mot clé X ») va à strategie-mot-cle ; une étape demandée seule
  garde son skill (seo-clustering-mots-cles, seo-brief-contenu…).
---

# Team mots-clés — pilote

## Routage

Toute demande de recherche de mots-clés ou de choix des mots-clés à attaquer pour un site ou un client passe par cette team : « recherche de mots-clés », « quel mot-clé attaquer », « stratégie mots-clés », « audit mots-clés »… Ne pas la traiter par `seo-recherche-mots-cles` ou `kw-research-workflow` seuls : ce sont des étapes de la team.

Exceptions : un terme déjà nommé (« stratégie mot clé X ») va à `strategie-mot-cle` ; une stratégie SEO/GEO complète va à `team-strategie` ; une étape demandée explicitement seule (« juste le clustering de cette liste ») garde son skill.

Tu es le pilote. Tu cadres, tu lances les agents, tu lis leurs livrables, tu les montres à l'utilisateur, tu enregistres ses accords. Tu ne fais pas le travail d'un agent à sa place, sauf le cadrage et le rapport, qui sont à toi.

La méthode reste `.claude/skills/workflow-mots-cles-complet/SKILL.md` et le fichier `.seokb/base/raw/bootcamp4/workflow-mots-cles-complet.md`. Lis-les en entier avant la première phase, avec `.seokb/base/wiki/methodes/rapport-mots-cles-format.md`. Cette team change qui fait quoi et où l'utilisateur valide, pas la méthode.

## La team

| Phase | Agent (`.claude/agents/`) | Étapes | Accord de l'utilisateur |
|---|---|---|---|
| cadrage | pilote | — | oui |
| collecte | `mots-cles-collecte` | 1 Keyword Planner, 2 Search Console | oui |
| recherche | `mots-cles-recherche` | 3 Overview, 4 Recherche, 5 Résistants IA | non |
| business | `mots-cles-business` | 6 Filtre des 4 piliers | oui |
| architecture | `mots-cles-architecture` | 7 Clustering, 8 Décisionnels, 9 Cluster AEO, 10 pSEO | oui |
| audience | `mots-cles-audience` | 11 Peurs et objections, 12 Entités | non |
| briefs | `mots-cles-brief` | 13 Un brief par cluster validé | non |
| rapport | pilote | 14 Rapport, annexes, contrôles | oui |

`architecture` et `audience` partent en même temps, dans un seul message, dès que `business` est validé. Les agents sont installés dans `.claude/agents/` du coffre. Tu les lances avec l'outil Agent, `subagent_type` = le nom de l'agent.

## L'état

Script : `python3 .seokb/runtime/teams/etat.py`. Le dossier du projet est `<wiki>/keywords/team-<slug>/` dans le coffre où la passe écrit (le coffre du client).

```bash
E="python3 .seokb/runtime/teams/etat.py"
$E liste                                   # tous les projets des teams
$E init mots-cles <dossier> --nom "<client>" --site <site>
$E status <dossier>                        # phases, ce qui attend l'utilisateur, ce qui est prêt
$E demarre <dossier> <phase>               # avant de lancer l'agent
$E livre <dossier> <phase> <fichiers>...   # après lecture du livrable
$E valide <dossier> <phase> --message "<mots exacts de l'utilisateur>"
$E corrige <dossier> <phase> --message "<correction exacte de l'utilisateur>"
```

`valide` refuse un fichier modifié depuis `livre` : relivre, remontre. `corrige` remet la phase à refaire et passe ses dépendantes « à revoir ».

## Déroulé

1. **Reprendre avant de créer.** `$E liste`. Un projet existe pour ce client : `status`, et tu dis où il en est. Plusieurs projets possibles : demande lequel. Jamais le dernier par défaut.
2. **Cadrage.** Une seule question groupée sur ce qui manque : site, offre et conversion, marché ou ville, coffre du client, données (export Keyword Planner, accès Search Console, transcripts). Ne redemande pas ce que le coffre dit déjà. Fixe slug et date. Écris `<dossier>/cadrage.md`, puis `init`, `livre cadrage`, et montre-le.
3. **Chaque phase d'agent.** `demarre`, puis l'agent avec le brief ci-dessous. À son retour, ouvre chaque fichier qu'il dit avoir écrit et vérifie : il existe, il porte `statut_decision`, il ne contient aucun volume sans fichier source. Mets à jour le fichier de logs `keywords/YYYY-MM-DD-slug-workflow-complet.md`. Puis `livre`.
4. **Phase avec accord.** Montre à l'utilisateur le livrable : chemins, ce qui est retenu, ce qui est BLOQUÉ et par quoi. Puis arrête-toi. Une phase par réponse.
5. **Phase sans accord.** Enchaîne sur la phase prête suivante dans la même réponse.
6. **Rapport.** Tu l'écris selon `rapport-mots-cles-format.md`, avec les annexes `decisions-*.json` et `scores-*.json`. Passe les sorties amont contredites à OBSOLÈTE. Lance `python3 .claude/skills/workflow-mots-cles-complet/controle-rapport.py <rapport>` (0 BLOQUANT) et `node .claude/skills/redaction-anti-ia/slop.mjs <rapport>`. Commit des 13 sorties, des logs et des annexes, sans push. `livre rapport`, montre-le.

## Brief d'un agent

Chaque agent démarre sans l'historique. Son prompt contient :

```
PROJET : <client>, <site>, slug <slug>, date <YYYY-MM-DD>
COFFRE : <chemin absolu du wiki où écrire>
CADRAGE : <chemin de cadrage.md>
PHASE : <id> — étapes <n>
ENTRÉES : <chemins absolus des sorties amont validées ou livrées>
DONNÉES : <exports, accès, transcripts disponibles ; ce qui manque>
CORRECTION DE L'UTILISATEUR : <mots exacts, seulement si la phase est refaite>
```

## Règles

- Accord = mots explicites de l'utilisateur sur la phase montrée. Le silence, « c'est quoi la suite ? », un accord sur une autre phase ne valent pas accord. Tu recopies ses mots dans `--message`.
- Une correction relance la même phase, avec le même agent et la correction dans son brief. Les dépendantes repassent après.
- Aucun volume estimé, nulle part. Un volume vient d'un export Keyword Planner ou de la Search Console, fichier cité ; sinon « non mesuré ».
- Une étape sans donnée n'est pas sautée : son fichier sort en BLOQUÉ, avec la donnée qui manque.
- Mots-clés business lus dans le coffre, jamais déduits.
- Aucun appel payant sans le go de l'utilisateur sur son coût.
- `raw/` immuable. Commit par chemin, jamais de push.

## Réponse à l'utilisateur

À chaque phase : la phase, le livrable (chemins cliquables), ce qui est retenu, ce qui est bloqué et par quoi, l'accord attendu. Au rapport : le diagnostic en trois lignes, le tableau de pré-décision par marché, ce qui attend sa décision et ce qui attend une lecture de SERP.
