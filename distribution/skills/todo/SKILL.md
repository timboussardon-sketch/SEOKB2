---
name: todo
description: "Reconstruit ta todo depuis les transcripts Claude Code des 7 derniers jours. « ma todo », « où j'en suis »."
---

# Skill — Todo depuis transcripts Claude Code

## Quand utiliser ce skill

Reconstruit une todo personnelle à partir des transcripts Claude Code locaux (7 derniers jours). Distingue ce qui est ✅ FAIT, 🔄 EN COURS, 📋 À FAIRE (priorisé sur récence × fréquence × blocage). Snapshot frais, overwrite d'un fichier unique (pas d'archivage par date).

Le skill ne te demande pas de te souvenir de ta todo : il la *reconstruit* depuis ce que tu as réellement fait dans Claude Code. Pas d'inférence, pas de tâche fantôme, pas de fluff.

TOUJOURS utiliser ce skill quand l'utilisateur dit : "ma todo", "fais-moi la todo", "où j'en suis", "qu'est-ce qu'il me reste", "actualise ma todo", "reprends ma todo", "bilan de la semaine", "récupère ce que j'ai fait cette semaine", "/todo", ou quand il enchaîne plusieurs sessions Claude Code et veut un point clair.

## Automatiser avec `/schedule` (à lire en premier)

Ce skill est utile en one-shot (« fais-moi le point »), mais il devient puissant quand il tourne **chaque matin à 8h, automatiquement**, pour t'ouvrir ta journée avec une todo fraîche reconstruite depuis tes sessions Claude Code de la veille.

**Setup en 3 étapes** :

1. Dans Claude Code, tape `/schedule`
2. Choisis « Créer une routine » et configure :
   - **Cron** : `0 8 * * 1-5` (du lundi au vendredi à 8h)
   - **Repo** : le repo Obsidian / vault où la todo doit être écrite (ex. `seo-kb`)
   - **Prompt** : `/todo` (sans paramètre, scan auto des 7 derniers jours)
3. Active la routine

**Ce que ça change vs un cron local** :
- La routine tourne sur l'infra Anthropic, pas sur ta machine. Tu pars en weekend, ta todo de lundi matin est quand même prête.
- Commit auto dans le repo cible (si configuré). Pas de bug type « le launchd a tourné mais le commit a foiré ».
- Tu pilotes depuis `/schedule list` (modifier le cron, suspendre, supprimer).

**Quand préférer un launchd local** : si ton vault Obsidian n'est pas sous Git (typique iCloud Obsidian) — `/schedule` ne peut pas y écrire. Soit tu mets ton vault sous Git, soit tu passes par launchd local + sync iCloud.

## Logique

Tu travailles déjà dans Claude Code tous les jours. Tes transcripts JSONL contiennent l'historique exact de ce que tu as livré, débuggé, différé. Le skill lit ces transcripts pour reconstruire ta todo, sans que tu aies à la maintenir à la main.

**3 catégories** :
- ✅ FAIT — livraisons concrètes (fichiers écrits, commits, validations)
- 🔄 EN COURS — sessions ouvertes, plans validés mais pas implémentés, multi-étapes incomplètes
- 📋 À FAIRE — intentions explicites de Tim, deadlines reportées, tasks pending

## Étape 1 — Récupérer les transcripts

Les transcripts JSONL Claude Code sont dans :

```
~/.claude/projects/-Users-<user>-<chemin-repo>/*.jsonl
```

Le chemin du repo est encodé : les `/` deviennent `-`. Exemple : `/Users/toi/Code/mon-projet` → `-Users-toi-Code-mon-projet`.

Demande à l'utilisateur quels repos il veut scanner si ce n'est pas évident depuis le `pwd` courant ou si plusieurs projets sont actifs.

Date du jour :
```bash
date +%Y-%m-%d
```

Fenêtre : 7 derniers jours.

```bash
find ~/.claude/projects/ -name "*.jsonl" -mtime -7 2>/dev/null
```

## Étape 1bis — Scanner les tâches manuelles (`raw/journal/`)

En plus des transcripts, les journaux quotidiens (`raw/journal/YYYY-MM-DD.md`, générés par `/recap-jour`) portent une section manuelle `## 📋 Tâches` où Tim note ce qui ne passe pas par Claude Code (calls, relances, admin). Cette section n'est jamais générée par `/recap-jour` — c'est écrit à la main.

```bash
find raw/journal/ -name "*.md" -mtime -7 2>/dev/null
```

Pour chaque fichier trouvé, extraire le bloc entre `## 📋 Tâches` et le prochain `##`, puis parser les lignes checkbox :

- `- [ ] texte` → 📋 À FAIRE, source `(journal YYYY-MM-DD)`
- `- [/] texte` → 🔄 EN COURS, source `(journal YYYY-MM-DD)`
- `- [x] texte` → ✅ FAIT, daté de la date du fichier journal (pas de date de complétion précise si non annotée)
- `- [-] texte` → annulée, ne pas reporter dans la todo

**Priorité de fusion** : une tâche écrite à la main dans un journal est un signal plus fort qu'une tâche inférée d'un transcript. Si un intitulé quasi identique apparaît dans les deux sources, garder une seule ligne avec la source `(journal)`.

## Étape 2 — Parser chaque transcript

Pour chaque fichier JSONL, lis-le avec Read (utiliser offset/limit si gros — les fichiers peuvent dépasser plusieurs Mo). Chaque ligne est un objet JSON : entrée user, message assistant, tool_use, tool_result.

### A) ✅ FAIT

Signaux à chercher :
- Tool calls `Write` / `Edit` réussis → fichier créé / modifié
- Tool calls `Bash` avec `git commit` réussis
- Messages assistant qui annoncent une livraison concrète : « j'ai créé X », « j'ai publié Y », « sauvegardé dans Z »
- Phrases user qui valident une livraison : « parfait », « ok merci », « tu valides », « ça marche », « nickel »

Format : `[YYYY-MM-DD] Action concrète (source : nom-repo)` — ou `(source : journal)` pour une case cochée manuellement dans un journal.

### B) 🔄 EN COURS

Signaux :
- Sessions dont la dernière entrée est un travail non clôturé (pas de validation user, pas de commit final)
- Phrases user : « je vais faire », « je dois finir », « on continue demain », « je reprends ça plus tard »
- `TaskCreate` avec tasks `pending` non clôturées dans la session
- Plans validés (`ExitPlanMode`) mais pas exécutés

Format : `[démarrée YYYY-MM-DD] Action — où ça en est`

### C) 📋 À FAIRE (priorisé)

Signaux :
- Case `- [ ]` ou `- [/]` sous `## 📋 Tâches` dans un journal (Étape 1bis) — signal manuel explicite, priorité sur l'inférence
- Tim dit explicitement : « à faire », « TODO », « il faudra », « je dois », « prochaine étape », « rappelle-moi de », « note-toi de »
- Fins de session avec « next steps » listés mais non exécutés
- Décisions différées : « on verra plus tard », « pour l'instant on laisse », « pas urgent »
- `TaskCreate` pending non clôturées entre sessions

Format : `- [ ] Action (raison de la prio si déductible)`

**Priorité** :
- **P1** = mentionnée dans la session la plus récente OU deadline proche OU bloque autre chose
- **P2** = mentionnée dans plusieurs sessions
- **P3** = mentionnée une seule fois, ancienne

## Étape 3 — Fusion avec la todo existante

Lis le fichier todo cible (par défaut `raw/todo/todo-actuelle.md`, ou chemin demandé par l'utilisateur) s'il existe.

Logique de fusion :
- **À FAIRE non datés ou plus anciens que la fenêtre 7j, toujours présents dans l'existant** → conserver tels quels (Tim ne les a pas faits, ils restent valides)
- **À FAIRE de l'existant qui apparaissent maintenant en FAIT** → déplacer en FAIT (avec la date où ils ont été faits, lue dans les transcripts)
- **Annotations manuelles** (`✅ done manuel`, commentaires Tim) → préserver telles quelles

Si le fichier n'existe pas → repartir de zéro.

## Étape 4 — Rédiger le fichier

Format final (overwrite total) :

```markdown
# Todo — MAJ YYYY-MM-DD HH:MM

> Source : transcripts Claude Code locaux (7 derniers jours)
> Reconstruit via skill `todo`

## ✅ Fait récemment (7 derniers jours)

- [YYYY-MM-DD] Action complétée (source : repo)
- [YYYY-MM-DD] Action complétée (source : repo)
...

## 🔄 En cours

- [démarrée YYYY-MM-DD] Action — où ça en est
- [démarrée YYYY-MM-DD] Action — où ça en est
...

## 📋 À faire

### P1 (cette semaine)
- [ ] Action (raison)
- [ ] Action

### P2 (mois)
- [ ] Action
- [ ] Action

### P3 (backlog)
- [ ] Action
```

Chemin par défaut : `raw/todo/todo-actuelle.md` (cohérent avec la structure vault Tim). Adapter si l'utilisateur précise un autre chemin.

## Règles absolues

- **Overwrite, pas d'archivage daté.** Un seul fichier vivant. Si Tim veut un historique → c'est git, pas un fichier par date.
- **Pas d'inférence créative.** Si tu n'arrives pas à classifier proprement, mets en `🔄 En cours` plutôt que d'inventer une priorité. Exception : une case cochée manuellement dans `## 📋 Tâches` d'un journal est prise verbatim, jamais réinterprétée.
- **Pas de tâche fantôme.** Ne pas écrire « à faire : X » si X n'est mentionné nulle part dans les transcripts. Le skill rapporte ce qu'il voit, il n'imagine pas.
- **Date du jour systématique** dans les timestamps : `date +%Y-%m-%d`.
- **Pas d'emoji autre que les 3 catégories** (✅ 🔄 📋). On garde sec.
- **Si > 7 jours sans aucune session Claude Code détectée** → le signaler en haut du fichier (« ⚠️ Aucune session récente, snapshot peut être périmé »).

## Variante : todo par projet

Si l'utilisateur ne veut la todo que pour UN projet (ex. seo-kb seul, ou organikk-next seul), filtrer les transcripts au scan initial — ne lire que `~/.claude/projects/-Users-<user>-<projet>/*.jsonl`.

Format alors : `raw/todo/todo-actuelle-[projet].md`.

## Enchaînement

- Pas d'amont, pas d'aval. Skill autonome.
- Peut être branché en cron quotidien (ex. tous les matins à 8h) pour un snapshot frais à l'ouverture de la session.
