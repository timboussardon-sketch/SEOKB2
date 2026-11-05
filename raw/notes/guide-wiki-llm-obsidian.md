---
type: source
source_type: note
title: "Guide : ma base SEO dans Obsidian, ouverte"
created: 2026-09-23
updated: 2026-09-23
tags: [guide, obsidian, wiki-llm, pattern-karpathy, lead-magnet, kb, ingest, query, lint]
sources: 8
confidence: high
status: draft
---

# Ma base SEO dans Obsidian

## Je l'ouvre et je montre comment elle tourne

> Tous les chiffres, sorties de terminal et diffs de ce guide viennent de ma base réelle, relevés le 2026-09-23.

# Ce que j'ai construit

En avril 2026 j'ai créé un dossier vide et un fichier `AGENTS.md`.

Au 23 septembre 2026, ce dossier contient 692 fichiers markdown dans `raw/` et 502 pages dans `wiki/`. Dont 136 fiches source, 77 entités et 69 concepts. Git compte 1 660 commits.

Je n'ai pas écrit ces 502 pages. Claude les écrit, et il les tient à jour.

Moi je dépose des fichiers, je pose des questions, et je relis.

Claude Code et ChatGPT Memory gardent des préférences entre sessions. Claude Code charge 200 lignes de `MEMORY.md` au démarrage, c'est documenté par Anthropic. Ça sert l'IA à mieux te répondre.

Ça ne te donne pas un document que tu ouvres, que tu navigues et que tu versionnes.

Le pattern vient d'un gist d'Andrej Karpathy, LLM Wiki. Sa formule tient en une ligne.

> « Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase »

# À quoi ressemble ma base

Trois choses à la racine. `raw/`, `wiki/`, et `AGENTS.md`.

`raw/`, ce sont mes sources. Des articles clippés, des transcripts de calls, des exports Search Console, mes notes de journal.

Claude y lit, et il n'y écrit jamais. C'est la seule règle que je n'ai pas assouplie en cinq mois.

La raison tient en une phrase. Le jour où l'agent reformule une source pour la rendre plus claire, tu perds la trace de ce que l'auteur avait écrit. Tu ne peux plus le citer, et tu ne peux plus le vérifier.

Les 2 709 fichiers de `raw/` ne sont pas tous du texte. `raw/data/` porte 1 722 fichiers, presque tous des exports Search Console.

`wiki/` est le domaine de Claude. Trois types de pages portent l'essentiel.

Une fiche source par document ingéré. Elle porte le contexte, les chiffres relevés, les limites de la source, et l'angle que j'ai demandé à creuser.

Une entité par objet nommé : un algo Google, un outil, un prospect, un moteur de réponse.

Les concepts portent les mécaniques. Le passage ranking, le grounding score, l'information gain : une page chacun, qui s'enrichit à chaque source qui en parle.

Les pages se citent entre elles avec des wikilinks, et ces liens forment le graphe qu'Obsidian affiche.

`AGENTS.md` est la configuration. Claude le lit au démarrage de chaque session.

Le mien fait 594 lignes aujourd'hui. Le journal montre qu'il est passé en v2.1 puis v2.2 dès le premier jour, le 11 avril. Chaque fois qu'une session dérape, j'y ajoute une ligne.

# Ce qui se passe quand j'ajoute une source

Un cas réel, le 19 juin 2026.

J'avais écrit un playbook Reddit, un document de doctrine, jamais rangé nulle part. Je l'ai déposé dans `raw/reddit-playbook/`.

Claude lit le fichier en entier, puis il me résume les points et me demande quel angle je veux creuser. À ce stade il n'a encore rien écrit dans le wiki, et c'est voulu : je corrige sa lecture avant qu'elle parte dans quinze fichiers.

Je réponds. Il écrit.

Trois pages créées : la fiche source, l'entité `reddit`, le concept `parasite-seo`.

Quatre pages modifiées, dont deux que je n'aurais jamais pensé à rouvrir.

Regarde celle de `perplexity`. Une seule ligne change. Deux wikilinks ajoutés dans la section « Pages liées ».

Ça n'a l'air de rien. C'est pourtant le travail qu'un humain abandonne au bout de trois mois, parce qu'il faut rouvrir une page qu'on n'avait aucune raison d'ouvrir.

> « Humans abandon wikis because the maintenance burden grows faster than the value »

Le LLM ne s'ennuie pas.

Total de cet ingest : 8 fichiers touchés, 305 lignes ajoutées. Karpathy annonce généralement 10 à 15 pages touchées par source. C'est un chiffre d'expérience, aucun benchmark ne le soutient. Chez moi ça va plutôt de 4 à 15, selon la densité du document déposé.

Puis Claude écrit une ligne dans le journal.

Une source à la fois. Le batch existe, je m'en sers pour les lots de veille. Sur un document qui compte, je veux voir ce qu'il a compris avant qu'il écrive.

# Comment j'interroge ensuite ma base

Deux usages différents, selon que je cherche un fichier ou une réponse.

Quand je cherche où c'est rangé, j'ai une commande.

Chaque résultat donne le score, le fichier, son type et l'extrait. Je sais où aller lire.

Quand je pose une vraie question, je laisse Claude faire le tour lui-même. Il lit d'abord `index.md` pour repérer les pages concernées, il en ouvre cinq à huit, puis il répond en posant un wikilink sur chaque affirmation.

Une affirmation sans wikilink, je la refuse. Sans le lien je ne peux pas vérifier, donc je ne peux pas la mettre dans un livrable client.

Ce qui change tout, c'est ce qu'on fait de la réponse.

En avril, j'ai demandé si le pattern du wiki améliorait structurellement le grounding score. La réponse tenait en cinq mécanismes, appuyés sur huit sources déjà ingérées.

Elle est devenue une page permanente : `wiki/queries/2026-04-12-wiki-pattern-vs-grounding-score.md`.

Le registre des hypothèses la cite. Cinq mois plus tard elle sert encore.

Une réponse qui reste dans le chat, tu la redemandes dans six semaines.

J'ai 28 pages dans `queries/`. Aucune ne vient d'une source externe. Elles viennent toutes de questions que j'ai posées.

# Comment j'évite que 500 pages deviennent ingérables

Six mécanismes. Aucun n'est compliqué, et tous sont ennuyeux à tenir.

## index.md

Le catalogue. Une ligne par page, avec sa description en dix mots.

Claude le lit avant de répondre. Sans index, l'étape « ouvre les huit bonnes pages » ne marche pas.

## log.md

Chronologique et en ajout seul. Une entrée déjà écrite n'est pas retouchée plus tard.

Quand un résultat me surprend trois semaines après, je remonte le journal au lieu de deviner.

## Le frontmatter

Obligatoire, sur `raw/` comme sur `wiki/`.

Sans lui, le fichier reste trouvable au texte. Il sort de tous les filtres : type, tag, statut, confiance.

## Git

Chaque session se commit. 1 660 commits à ce jour.

C'est comme ça que j'ai ressorti le diff d'ingest de juin, trois mois après.

## Les contradictions et les hypothèses

Quand un ingest contredit une page existante, Claude le signale et la ligne va dans un registre.

Trois statuts comptent : ouverte, résolue, acceptée. Acceptée veut dire qu'on arrête de la re-discuter.

Ma doctrine contient aussi des paris. Ils sont listés, avec le contre-argument cherché en face.

Une hypothèse ne passe jamais « validée » sur un ressenti. Il faut une fiche preuve adossée à de la data réelle.

## Le lint

Une fois par semaine, un audit sort un rapport. Il ne répare rien tout seul.

Celui du 20 septembre : 1 669 fichiers scannés, 11 684 wikilinks, 167 cibles cassées. Soit 1,97 %.

Sur ces 167, 59 seulement sont référencées depuis `wiki/`. Le reste vient d'espaces de travail hors périmètre. Même chose pour les orphelins : 747 au total, 29 dans `wiki/`.

Il m'a aussi trouvé une catégorie d'erreur que je ne voyais pas. Des pages qui pointent vers des slugs de la mémoire Claude, qui ne résoudront jamais dans Obsidian.

Je ne répare pas tout. Je trie, et j'accepte de laisser des liens cassés dans les dossiers qui ne sont pas le wiki.

# Ce qui change quand la base devient grosse

Karpathy annonce un seuil. Vers cent sources, `index.md` ne suffit plus à router vers les bonnes pages.

Chez moi le seuil est tombé le 7 août 2026, à 110 sources. L'outil était déjà là : j'avais ajouté une recherche vectorielle locale le 26 mai.

ChromaDB, embeddings `paraphrase-multilingual-mpnet-base-v2`, en local et gratuit. Un chunk par section H2. Le fichier de base pèse 231 Mo.

C'est là que le frontmatter paie. Chaque morceau de texte indexé garde les champs de son fichier d'origine, donc le filtre passe d'abord sur le type, le tag et le statut. La recherche sémantique ne travaille ensuite que sur ce qui reste.

`index.md` n'a pas disparu pour autant. Le wiki compile une fois, le moteur retrouve à chaque question.

Le graphe se mesure aussi. `data-proprietaire` est cité par 268 fichiers et pointe vers 34 pages.

Cette page-là non plus, je ne l'ai pas écrite.

# Ce que tu dois mettre en place chez toi

Compte quinze minutes pour l'installation. Le premier ingest prend plus de temps que les suivants, parce que tu corriges ce que Claude a compris.

## Installer

Obsidian est gratuit. Claude coûte environ 20 € par mois. Un SaaS SEO coûte plutôt 50 à 300 € par mois (relevé avril 2026).

## Poser l'arborescence

Crée `index.md` et `log.md` vides tout de suite.

## Écrire AGENTS.md

Six sections suffisent pour commencer : la mission, ta doctrine, l'arborescence, les types de pages, les conventions, les workflows.

Voilà le minimum qui tient debout. Tu le feras grossir tout seul.

## Ingérer la première source

Pas n'importe laquelle. Prends celle qui compte : un transcript de call, un export Search Console, ton meilleur audit.

## Poser la première question

Regarde les wikilinks de la réponse. Si Claude affirme sans lier, ta doctrine n'est pas assez dure, ou ta base est encore vide.

Le réseau, lui, commence à la deuxième source.
