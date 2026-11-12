---
type: methode
title: Utiliser la team stratégie SEO GEO
aliases: [mode-emploi-team-strategie]
tags: [seo, geo, agents, workflow]
created: 2026-11-12
updated: 2026-11-12
sources: 1
confidence: high
status: stable
---

# Utiliser la team stratégie SEO GEO

Dashboard : `python -X utf8 .seokb/runtime/team/server.py --port 0`, puis ouvrir l'adresse localhost imprimée. Il affiche les projets et les livrables. Les ordres passent par la conversation avec l'agent. Présentation et parcours : [[agents/team-strategie]].

## Prérequis

Claude Code (commande `claude`) ou Codex (commande `codex`, connexion ChatGPT) dans le PATH. Sans réglage, Claude Code est choisi. Variables d'environnement facultatives :

| Variable | Effet |
|---|---|
| `SEOKB_TEAM_AGENT` | `claude` ou `codex` impose l'agent |
| `SEOKB_TEAM_MODEL` | Modèle passé à Claude Code (`sonnet`, `opus`…) |
| `SEOKB_TEAM_MAX_BUDGET_USD` | Plafond de dépense par mission, Claude Code |
| `SEOKB_TEAM_MAX_TURNS` | Nombre maximal de tours par mission, 40 par défaut |
| `SEOKB_TEAM_TIMEOUT` | Délai maximal par mission en secondes, 900 par défaut |

Chaque mission est un appel de l'agent sur l'accès de l'utilisateur : une vague de `run-ready` avec `--max-jobs 3` lance jusqu'à trois appels. Le coût et le modèle de chaque appel sont enregistrés dans la trace de la mission.

Un dossier d'opportunités chiffré passe par un validateur qui requiert `python -m pip install jsonschema`. Sans estimation chiffrée, rien à installer.

## Entrée du projet

Donner le client, le site, les offres, les objectifs, le coffre et les sources disponibles. Les mots-clés sont facultatifs ; s'ils sont fournis, ils servent de pistes d'exploration.

Exemple : « Lance la stratégie SEO GEO complète pour [client], à partir de [site et coffre]. »

Pour reprendre : « C'est quoi la suite pour [client] ? ». L'agent retrouve les validations, les blocages et la prochaine tâche. Une ambiguïté entre projets conduit à demander lequel.

## Commandes du pilote

Depuis la racine du coffre (`python` désigne `python3`, `python` ou `py -3` selon le poste) :

```sh
python -X utf8 .seokb/runtime/team/team.py status
python -X utf8 .seokb/runtime/team/team.py start wiki/projets/team-strategie/data/briefs/client.json
python -X utf8 .seokb/runtime/team/team.py next ID_PROJET
python -X utf8 .seokb/runtime/team/team.py prepare ID_PROJET
python -X utf8 .seokb/runtime/team/team.py run-ready ID_PROJET --max-jobs 3 --workers 3
python -X utf8 .seokb/runtime/team/team.py approve ID_MISSION SHA --message "Accord exact" --user-approved
python -X utf8 .seokb/runtime/team/team.py revise ID_MISSION --message "Correction exacte"
python -X utf8 .seokb/runtime/team/team.py retry ID_MISSION
python -X utf8 .seokb/runtime/team/team.py recover ID_MISSION
```

Le brief est un objet JSON : `name`, `site`, `objective`, `request`, `mode: seo|seo-geo`, `vault` absolu (le coffre actuel par défaut), `keywords` facultatif, `sources`, contexte et contraintes. Le coffre doit exister avec un fichier AGENTS.md. `web: true` autorise la recherche publique utile au mandat, pas une dépense API.

`prepare` crée les missions dont les prérequis sont validés. `run-ready` lance une vague bornée sans franchir de validation humaine. Une correction se reprend avec `revise`, un échec technique avec `retry` après diagnostic. `recover` exige que le processus propriétaire soit arrêté. Les résultats et accords précédents restent conservés.

## Fichiers

`wiki/projets/team-strategie/data/` contient la base `team.sqlite3`, les briefs, les workspaces (prompt, événements et réponse de chaque appel) et les livrables en Markdown. Le dashboard écoute uniquement localhost et ne déclenche aucune mission. Les sources originales du coffre client restent référencées, jamais copiées ni modifiées.

[[agents/team-strategie]] · [[methodes/strategie-mot-cle-par-etapes]]
