---
type: source
source_type: note
title: "Guide : Installer tes skills de SEO technique"
aliases: [guide installation skills, installer-skills-seo-technique-claude]
tags: [guide, seo-technique, claude, skills, organikk]
created: 2026-08-21
updated: 2026-08-21
sources: 0
confidence: high
status: published
---

# Guide « Installer tes skills de SEO technique »

Guide Organikk publié le 2026-08-21. DA Organikk (Geist, couverture en dégradé bleu, feuille blanche, A4), reprise de la CSS du lead magnet `6-taches-seo-technique-claude.html`.

Portage du guide d'installation qui n'existait que sur qadence.io (`qadence/public/agent-seo-technique/guide/`, DA fanzine). Le contenu source parle de six « modules » livrés en zip avec l'offre Qadence. La version Organikk parle de six skills et renvoie à l'article `organikk.co/blog/6-taches-seo-technique-claude`, qui publie les six `SKILL.md` en entier. Aucun zip n'est distribué sur organikk.co.

Fichiers dans ce dossier : `installer-skills-seo-technique-claude.html` (copie) et `installer-skills-seo-technique-claude.pdf`.
**Source canonique : `~/Code/organikk-next/public/guides/installer-skills-seo-technique-claude.html`.** Toute modification se fait là-bas, puis on recopie ici. Carte publique : organikk.co/guides (teinte rose, 1er guide de la liste).

## Structure du guide (8 étapes)

- À lire en premier : ce que l'installation fait, ce qu'elle ne fait pas, dix minutes dont huit d'installation d'outils.
- 1. Ce qu'il te faut : Claude Code, un terminal, Node.js, un accès Search Console pour deux skills sur six.
- 2. Déposer les six skills : `mkdir -p ~/.claude/skills/`, un dossier par skill, le `SKILL.md` copié depuis l'article des 6 tâches.
- 3. Vérifier que Claude Code les voit : `ls ~/.claude/skills/`, les six noms, redémarrage de Claude Code.
- 4. Installer Lighthouse et jq : pour le seul skill Core Web Vitals, avec l'alternative `npx lighthouse`.
- 5. Sortir un export Search Console propre : trois mois pour la cannibalisation, six mois pour le maillage, onglets Pages et Requêtes, CSV jamais réenregistré depuis un tableur.
- 6. La première demande : aucune commande, six phrases en langage naturel, commencer par l'indexation.
- 7. Lire le rapport : markdown, critique en tête, « non testable » ≠ « non indexée », seul le skill données structurées écrit dans le code.
- 8. Les pannes fréquentes : six erreurs, chacune avec sa cause unique.

## Les six skills couverts

`indexation-check` · `seo-core-web-vitals` · `seo-donnees-structurees` · `maillage-systeme` · `maillage-interne-gsc` · `seo-cannibalisation`

## À faire ensuite

- Version EN si le guide EN d'audit (`public/guides/en/`) trouve son public.
- Le guide suppose que l'article des 6 tâches reste en ligne : si son URL change, corriger les deux liens du chapitre 2.
