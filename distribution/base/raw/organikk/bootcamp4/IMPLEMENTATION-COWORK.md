---
title: Brancher le dataset de référence SEO sous Claude Cowork
bootcamp: 4
jour: J5 (semaine 4)
created: 2026-05-26
public: oui (doc à distribuer aux participants)
---

# Brancher mon dataset de référence à ton Cowork

Tu as déjà ton système monté depuis les semaines 1 à 3 : tes skills installés, tes fichiers `about-me` / `my-voice` / `my-rules` remplis. **Ce kit ne remplace rien de tout ça.**

C'est un **dataset de référence** : ma doctrine SEO, mon kit d'accompagnement client, mes newsletters et revues de presse. Tu le branches à côté de ton vault pour que Claude puisse s'appuyer dessus quand tu bosses (modèle de raisonnement, exemples, méthodo).

Pas de réinstallation. Tu récupères le dossier, tu le mets là où Cowork le voit, et tu dis à Claude de l'utiliser.

---

## Étape 1 — Récupérer le dossier

Le repo est **privé** : il faut que Tim t'ait donné accès (invitation GitHub par mail, ou le ZIP sur le Drive).

**Option simple (ZIP)** : récupère le ZIP sur le Drive bootcamp, dézippe-le. Tu obtiens un dossier `seo-kit-starter/`.

**Option Git** (si tu veux les mises à jour via `git pull`) :
```bash
cd ~/Documents
git clone https://github.com/timboussardon-sketch/seo-kit-starter.git
```

---

## Étape 2 — Ce qu'il y a dedans

```
seo-kit-starter/
  AGENTS.md                → L'OS du vault : comment ma doctrine s'articule
  wiki/
    concepts/              → Doctrine SEO (passage ranking, entités, Surprise Score…)
    syntheses/             → Méthodo consolidée
    entities/              → Concepts tech (BERT, MIRAS, SGE, BM25…)
  raw/notes/
    drive-accompagnement/  → Kit d'onboarding client clé en main
    contenu-seo/           → Doctrine de production de contenu
  raw/revue-de-presse/     → Mes éditions revue de presse (exemples de sortie)
  wiki/revues-presse/      → Newsletters Algorithme
```

C'est de la matière de référence (doctrine + kit + exemples). Tes skills, tu les as déjà : ce dataset ne les contient pas, et c'est normal.

---

## Étape 3 — Brancher le dossier à ton Cowork existant

Tu as deux façons de faire, selon comment tu veux t'en servir.

### A. En dossier de référence à côté de ton vault (recommandé)

Garde `seo-kit-starter/` dans `~/Documents/`. Dans Claude Cowork, quand tu démarres une session de travail, ajoute ce dossier à ton contexte (ou ouvre-le comme dossier secondaire). Tu dis à Claude :

> « Pour ce travail, appuie-toi sur la doctrine dans `~/Documents/seo-kit-starter/wiki/` et le kit dans `raw/notes/drive-accompagnement/`. »

### B. Fusionné dans ton propre vault

Si tu veux que ma doctrine vive dans TON vault (et que ton graphe Obsidian la relie au reste), copie les dossiers qui t'intéressent dans ton vault :

```bash
cp -R ~/Documents/seo-kit-starter/wiki/concepts/* ~/ton-vault/wiki/concepts/
cp -R ~/Documents/seo-kit-starter/raw/notes/drive-accompagnement ~/ton-vault/raw/notes/
```

À éviter si tu n'es pas à l'aise : tu risques d'écraser tes propres fichiers. En cas de doute, reste sur l'option A.

---

## Étape 4 — T'en servir

Une fois le dossier visible par Cowork, tu peux demander à Claude :

- « Audite mon article sur X en t'appuyant sur la doctrine `passage-ranking` et `entites-vectorielles` du dataset. »
- « Reprends la structure de mon onboarding client en suivant `drive-accompagnement/`. »
- « Inspire-toi du ton de mes revues de presse de référence pour formater la mienne. » (en gardant TA voix via ton `my-voice`)

Le dataset sert de **modèle de raisonnement et d'exemples**. Ta voix, tes règles, tes skills restent les tiens.

---

## Si tu bloques

- **Claude ne trouve pas la doctrine** → vérifie que le dossier `seo-kit-starter` est bien dans le périmètre que Cowork peut lire (Étape 3A).
- **Tu veux juste lire** → ouvre `seo-kit-starter` comme vault Obsidian secondaire, tu navigues dans le graphe.
- **Reste bloqué** → WhatsApp Tim.

---

## Ce que tu NE reçois PAS dans ce dataset (et pourquoi)

Pas mes données clients (calls, cas, propositions commerciales), ni mes outils business. Confidentialité. Les exemples de doctrine qui citaient des cas réels ont été anonymisés (`Participant A`, `Client X`…). Tu reçois la **méthode** et les **exemples**, pas mes données privées.

---

*Dataset de référence, Bootcamp 4. À distribuer aux participants via le Drive. Timothée Boussardon, mai 2026.*
