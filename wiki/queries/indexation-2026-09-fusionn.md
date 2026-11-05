---
type: audit
title: "Audit indexation fusionn.co - 2026-09-05 (premier run, 47 URLs, rendu client bloquant)"
date: 2026-09-05
perimetre: "https://fusionn.co - 47 URLs du sitemap + comparaison HTML servi / HTML rendu"
sources_de_verite: ["HTTP status (curl -sIL, 47/47 URLs)", "https://fusionn.co/sitemap.xml", "https://fusionn.co/robots.txt", "DOM servi (curl, 47 pages)", "DOM rendu (Chrome headless --dump-dom, 4 pages)", "graphe interne calcule sur DOM servi ET DOM rendu"]
indexation_google_estimee: "non testable ce run (methode site: invalidee par test temoin, cf. Limites)"
pages_testees: 47
anomalies_critiques: 2
anomalies_mineures: 4
tags: [seo, indexation, fusionn, spa, geo, audit]
created: 2026-09-05
updated: 2026-09-05
sources: 1
confidence: high
status: stable
loop: indexation-check
---

# Audit indexation fusionn.co - 2026-09-05

## Synthese

Premier run sur ce domaine. Aucun historique de comparaison.

Les fondamentaux repondent : **47/47 URLs du sitemap en HTTP 200**, aucun `noindex` en meta HTML, aucun `X-Robots-Tag` server-side sur echantillon, aucune URL bloquee par `robots.txt`, `<link rel=canonical>` present sur 47/47.

Le probleme est ailleurs, et il est structurel. **45 des 47 pages servent un HTML stricitement identique** : 86 658 octets, 1 216 mots, meme `<title>`, meme `<h1>`, et surtout **`<link rel="canonical" href="https://fusionn.co/">` pointant vers la page d'accueil**. Le contenu editorial n'existe pas dans le HTML servi : il est injecte par React apres chargement. Seules `/a-propos` et `/contact` sont prerendues correctement.

Verifie par comparaison servi / rendu sur `/listes-mots-cles/agence-seo` :

| | HTML servi (curl) | HTML rendu (Chrome headless) |
|---|---|---|
| canonical | `https://fusionn.co/` | `https://fusionn.co/listes-mots-cles/agence-seo` |
| title | *Outil pour trouver vos mots-cles SEO...* | *Liste des mots-cles pour agence SEO : cartographie complete* |
| h1 | *L'agent qui trouve vos meilleurs mots-cles...* | *Liste des mots-cles pour agence SEO* |
| mots de contenu | 0 | 1 814 |

`react-helmet` (`data-rh="true"` sur les balises) corrige tout cote client. Googlebot execute le JS et finit par voir la version correcte. Le risque n'est donc pas une desindexation mecanique, mais il reste materiel, et il porte precisement sur le positionnement du produit.

**Verifications validees** (47 pages)
- HTTP 200 final : 47 / 47
- Absence de `noindex` en meta : 47 / 47
- Absence de `X-Robots-Tag` : echantillon 2 URLs
- `<link rel=canonical>` present : 47 / 47
- `<title>` present : 47 / 47
- `<h1>` present : 47 / 47
- Non bloque par `robots.txt` : 47 / 47

**Verifications avec anomalies**
- Pages servant le shell d'accueil au lieu de leur contenu : **45 / 47**
- Pages dont le canonical servi pointe vers l'accueil au lieu d'elles-memes : **44 / 47**
- Pages vivantes liees depuis l'accueil mais absentes du sitemap : **4**
- `lastmod` > 6 mois : **7 / 47**
- Incoherence trailing slash : **2 / 47**

## Anomalies CRITIQUES

### C1. 44 URLs servent un canonical vers la page d'accueil

Les 44 pages concernees couvrent la quasi-totalite de la surface SEO du site : les **24 pages `/listes-mots-cles/*`** (le corpus pSEO), les **8 articles de blog**, les **pages outils** (`/generateur-mots-cles-gratuit`, `/explorateur-questions-seo`, `/comparateur-volume-business-seo`, `/score-semantique`, `/clusteriser-mots-cles`, `/structure-h2-h3-seo`, `/test-citation-ia-gemini`, `/mots-cles-qui-convertissent`), plus `/blog`, `/glossaire` et les pages legales.

Consequences a separer clairement :

**Sur Google** : le crawl initial lit un canonical qui dit « cette URL est un doublon de l'accueil ». La correction n'arrive qu'apres passage dans la file de rendu, differee et non garantie page par page. Tant que le rendu n'a pas eu lieu, le signal envoye est une instruction de consolidation vers `/`.

**Sur les moteurs de reponse** : c'est la ou l'impact est direct. La majorite des crawlers de LLM (GPTBot, ClaudeBot, PerplexityBot) n'executent pas JavaScript. Ils lisent donc, sur les 44 URLs, la meme page d'accueil : meme titre, meme h1, zero contenu specifique. Pour un produit dont la promesse est *« trouver vos mots-cles pour Google, ChatGPT et les IA »*, le corpus qui doit demontrer cette competence est invisible aux moteurs qu'il cible. Les 24 pages `/listes-mots-cles/*` sont exactement le materiau citable, et c'est celui qui ne sort pas.

Action : passer les routes publiques en rendu serveur ou en prerendu au build. Le sous-ensemble prioritaire est `/listes-mots-cles/*` (24 pages) et `/blog/*` (8 pages). A defaut de SSR complet, un prerendu statique a la generation suffit pour ces 32 routes. Le fait que `/a-propos` et `/contact` soient deja correctement prerendues indique que le mecanisme existe deja et ne couvre que deux routes.

### C2. Quatre pages vivantes liees depuis l'accueil, absentes du sitemap

| URL | HTTP | Dans le sitemap |
|---|---|---|
| `/documentation` | 200 | non |
| `/generateur-mots-cles-amazon` | 200 | non |
| `/generateur-mots-cles-ia` | 200 | non |
| `/guides` | 200 | non |

Ces quatre pages sont liees depuis la navigation de l'accueil (verifie sur le DOM rendu). Deux d'entre elles sont des outils generateurs, donc des pages a intention transactionnelle. Le sitemap declare 47 URLs et en oublie 4 qui existent et sont maillees.

Action : ajouter les 4 routes a la generation du sitemap. Verifier au passage si d'autres routes de l'application echappent au meme recensement, la source du sitemap semblant desynchronisee du routeur.

## Anomalies mineures

- **Directive `Sitemap:` du `robots.txt` pointe vers un autre domaine.** `https://fusionn.co/robots.txt` declare `Sitemap: https://fusionn.io/sitemap.xml`. Cette URL repond 301 vers `https://fusionn.co/sitemap.xml`. Le fichier est donc atteignable, mais via un saut inter-domaines inutile. Corriger la directive pour pointer directement sur `https://fusionn.co/sitemap.xml`.
- **7 articles de blog avec `lastmod` anterieur a 6 mois** : `/blog/prompts-seo-strategies-workflows`, `/blog/quadrillage-semantique-strategie-seo-face-ia`, `/blog/ma-reflexion-du-moment-sur-le-seo-ia`, `/blog/fin-contenu-genere-humain-opportunite-seo` (2026-01-17), `/blog/trouver-mots-cles-pertinents` (2026-01-21), `/blog/pourquoi-88-pourcent-sites-seo-napparaissent-pas-dans-ia` (2026-01-26), `/blog/google-punit-il-le-contenu-ia` (2026-02-01). Soit 7 des 8 articles du blog.
- **Incoherence trailing slash** : seules `/a-propos` et `/contact` redirigent en 301 vers leur version avec slash final. Les 45 autres URLs sont servies directement. Ce sont aussi les deux seules pages prerendues, donc les deux phenomenes ont probablement la meme cause.
- **Deux pages courtes** parmi les deux seules mesurables : `/contact` (147 mots) et `/a-propos` (330 mots). Le contenu des 45 autres pages n'est pas mesurable sur le HTML servi.

## Point de methode : le maillage interne n'est pas evaluable sur le HTML servi

Le calcul du graphe interne sur les 47 pages servies renvoie 32 pages a zero lien entrant. **Ce chiffre est un artefact de C1, pas une anomalie de maillage.** Le HTML servi ne contient aucun lien interne puisqu'il ne contient pas l'application.

Sur le DOM rendu, le maillage est correct : le hub `/listes-mots-cles` lie ses **24 pages enfant**, le hub `/blog` lie ses **8 articles**. Aucune page orpheline reelle detectee.

Ce que cela dit : le maillage existe pour un crawler qui rend le JS, et n'existe pas pour un crawler qui ne le rend pas. Meme partage que C1.

## Recommandations priorisees

1. **Prerendre ou passer en SSR les 32 routes editoriales** (`/listes-mots-cles/*` et `/blog/*`) : effort moyen (config de build), impact fort. Resout simultanement le canonical errone, l'absence de contenu, l'absence de titres uniques et le maillage que les crawlers sans JS ne peuvent pas suivre.
2. **Ajouter les 4 routes manquantes au sitemap** : effort faible, impact moyen. Deux sont des generateurs, donc des pages a intention Do.
3. **Corriger la directive `Sitemap:` du `robots.txt`** vers `https://fusionn.co/sitemap.xml` : effort trivial, impact faible mais gratuit.
4. **Rafraichir ou dater correctement les 7 articles du blog** : effort faible si les dates sont justes, a traiter comme decision editoriale sinon.

## Limites de ce rapport

- **Statut d'indexation Google non mesure.** La methode de scraping `site:` a ete invalidee par un test temoin : une URL inexistante (`/cette-page-nexiste-absolument-pas-xyz123/`) est ressortie « indexee » avec le meme score qu'une URL reelle, la chaine du domaine etant presente dans la requete reaffichee par Google. Deux requetes sur cinq ont par ailleurs ete bloquees en rate-limit. Aucune URL de ce rapport ne peut donc etre declaree indexee ni non indexee. **Non testable n'est pas non indexee.**
- Comparaison servi / rendu effectuee sur 4 URLs (1 page pSEO, 1 article, 2 hubs), pas sur les 47. L'identite stricte des 45 fichiers servis (meme taille en octets a l'octet pres) rend l'extrapolation solide, mais elle reste une extrapolation.
- Premier run sur ce domaine : aucune trajectoire historique, donc aucune distinction possible entre etat stable et regression recente.
- Le comportement reel de Googlebot sur la file de rendu n'est pas observable sans acces GSC. L'analyse d'impact de C1 sur Google repose sur le fonctionnement documente du rendu differe, pas sur une mesure.
