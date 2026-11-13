---
name: sauvegarde-coffre
description: "Sauvegarde le coffre hors de l'ordinateur (archive ZIP dans un dossier synchronisé) et teste la restauration. « sauvegarde le coffre »."
---

# Sauvegarde du coffre

## Quand utiliser ce skill

« /sauvegarde-coffre », « sauvegarde le coffre », « backup », « restaure la sauvegarde ».

Une sauvegarde ne compte que si elle quitte l'ordinateur. Un dépôt git non poussé ou un dossier `_backups/` sur le même disque ne survivent pas à sa perte.

## Sauvegarder

Demander le dossier de destination : un dossier synchronisé (iCloud Drive, Google Drive, OneDrive, Dropbox) ou un disque externe. Ne jamais choisir à la place de l'utilisateur.

```
python -X utf8 .seokb/runtime/sauvegarde.py --destination "<dossier>"
```

Le script archive `raw/`, `wiki/`, `.claude/`, `CLAUDE.md`, `AGENTS.md` et l'historique git s'il existe, contrôle l'archive en la relisant, puis garde les 7 dernières (`--garder N` pour changer). Il exclut `.seokb/base/` et `.seokb/runtime/` (réinstallables par la mise à jour), `_backups/`, `node_modules/` et les fichiers `.env*`.

L'archive n'est pas chiffrée. Si le coffre contient des données clients, choisir une destination dont l'accès est restreint, ou chiffrer l'archive avec l'outil du système.

## Restaurer

```
python -X utf8 .seokb/runtime/sauvegarde.py --restaurer "<archive.zip>" --vers "<dossier vide>"
```

Puis `python -X utf8 .seokb/runtime/install.py --target "<dossier>"` pour remettre la bibliothèque commune.

## Contrôle

Après la première sauvegarde, restaurer une fois dans un dossier vide et ouvrir une note : c'est la seule preuve que la sauvegarde sert. Planifier ensuite la commande avec l'outil du système (cron, Planificateur de tâches Windows) si tu veux une sauvegarde quotidienne : rien n'est planifié par SEOKB2.
