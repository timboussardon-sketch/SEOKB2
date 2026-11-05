---
type: methode
title: "Bootcamp : dupliquer le vault ClaudeSEO pour un client"
aliases: [bootcamp-dupliquer-vault, dupliquer-projet-bootcamp]
tags: [bootcamp, claude-code, obsidian, vault, formation]
created: 2026-10-14
updated: 2026-10-14
sources: 2
confidence: high
status: draft
---

# Bootcamp : dupliquer le vault ClaudeSEO pour un client

> Objectif : passer du vault de formation à un vault par client, en trois étapes dictées en séance. Rédigé le 2026-10-14 à partir de l'onglet Mise à jour du dashboard bootcamp (version 1.4.0) et du CLAUDE.md du coffre ClaudeSEO.

## En résumé (à lire en premier)

Mets d'abord le système à jour en 1.4.0.

Ensuite, demande à Claude de dupliquer ton vault à l'identique dans un dossier client.

Enfin, ouvre ce nouveau dossier dans une nouvelle session Claude Code.

Chaque client a son vault.

## 1. Mettre le système à jour en 1.4.0

Ouvre ton dashboard bootcamp, onglet Mise à jour.

Télécharge le ZIP `organikk-seo-system.zip`, version 1.4.0.

Depuis la 1.4.0, le ZIP est un coffre Obsidian complet : CLAUDE.md, les skills dans `organikk-seo-system/`, la doctrine, les méthodes et les workflows dans `wiki/`, les sources d'Organikk dans `raw/organikk/`.

Ouvre le terminal dans ton vault. Remplace `ClaudeSEO` par le nom de ton propre dossier.

> Mac
> ```
> cd ~/Documents/ClaudeSEO
> claude
> ```

> Windows PowerShell
> ```
> cd "$HOME\Documents\ClaudeSEO"
> claude
> ```

Colle le prompt de mise à jour de l'onglet dans Claude Code.

Claude sauvegarde l'ancien système dans `_backups/systeme-seo/`, remplace les dossiers du système, et rend un tableau de contrôles.

Le contrôle qui compte : `organikk-seo-system/.claude-plugin/plugin.json` affiche 1.4.0.

Ferme la conversation. Les skills mis à jour se chargent à la prochaine ouverture.

## 2. Dupliquer le vault pour un client

Reste dans ton dossier ClaudeSEO. Ouvre une nouvelle conversation.

Colle ce prompt. Remplace `ClaudeSEO` par le nom de ton vault, et `NomDuClient` par le nom du client.

> Tu vas dupliquer pixel perfect le vault ClaudeSEO, le dossier actuellement ouvert.
>
> Tu vas créer un nouveau dossier pour le client NomDuClient : `~/Documents/ClaudeSEO-NomDuClient`. Duplique tout dedans, et je vais ajouter la data du client.
>
> Règles :
> - Copie l'intégralité du dossier : CLAUDE.md, organikk-seo-system/, wiki/, raw/, .obsidian/ s'il existe.
> - Ne copie pas `_backups/`.
> - Ne modifie rien dans le dossier d'origine.
> - Ne fais ni commit ni push.
>
> À la fin, montre-moi : le chemin exact du nouveau dossier, le nombre de fichiers dans l'original et dans la copie, et la version affichée par `organikk-seo-system/.claude-plugin/plugin.json` dans la copie.
>
> Termine en me donnant la commande exacte pour ouvrir une nouvelle session dans ce dossier, sur ce modèle :
> ```
> cd ~/Documents/ClaudeSEO-NomDuClient
> claude
> ```

Les deux nombres de fichiers doivent être égaux, à `_backups/` près.

Si la version n'affiche pas 1.4.0, reviens à l'étape 1.

## 3. Ouvrir le vault client dans une nouvelle session

Ferme la conversation en cours.

Ouvre un nouveau terminal. Remplace `NomDuClient` par le nom choisi à l'étape 2.

> Mac
> ```
> cd ~/Documents/ClaudeSEO-NomDuClient
> claude
> ```

> Windows PowerShell
> ```
> cd "$HOME\Documents\ClaudeSEO-NomDuClient"
> claude
> ```

Claude lit le CLAUDE.md du dossier ouvert. Les skills et la doctrine sont ceux de la copie.

Dépose la data du client dans `raw/` de ce vault. Tout ce que Claude produit va dans `wiki/` de ce vault.

Pour revenir au vault de formation, refais la commande avec `ClaudeSEO`.

## Sources

- Onglet Mise à jour du dashboard bootcamp, `organikk-next/dashboard-src/bootcamp-app.jsx`, constante SYSTEME_VERSION 1.4.0 et prompt de mise à jour (2026-10-13).
- CLAUDE.md du coffre ClaudeSEO, `organikk-next/scripts/pack-systeme-seo/CLAUDE.md` (2026-10-13).
- [[methodes/tableau-de-bord-par-projet-seo]] : un projet SEO = un coffre dédié.
