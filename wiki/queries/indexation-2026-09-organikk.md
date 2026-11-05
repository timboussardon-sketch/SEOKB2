---
type: audit
title: "Audit indexation Organikk - 2026-09-05 (sitemap 142 -> 91, wiki elague 56 -> 23, /tarifs hors sitemap)"
date: 2026-09-05
perimetre: "https://organikk.co - 91 URLs du sitemap + verification des sections sorties depuis le 31/08"
sources_de_verite: ["HTTP status (curl -sIL, 91/91 URLs du sitemap + 21 URLs de controle)", "https://organikk.co/sitemap.xml", "https://organikk.co/robots.txt", "DOM meta robots / canonical / h1 / title (91 pages telechargees)", "wordcount HTML body methode C (script/style/noscript/nav/footer/header enleves)", "graphe interne calcule sur les 91 pages telechargees", "echantillon X-Robots-Tag sur 2 URLs"]
indexation_google_estimee: "non testable ce run (methode site: invalidee par test temoin, cf. Limites)"
pages_testees: 91
anomalies_critiques: 4
anomalies_mineures: 4
tags: [seo, indexation, organikk, sitemap, audit]
created: 2026-09-05
updated: 2026-09-05
sources: 1
confidence: high
status: stable
loop: indexation-check
---

# Audit indexation Organikk - 2026-09-05

## Synthese

**Le sitemap continue de se contracter : 142 URLs au 31/08, 91 aujourd'hui, soit -51 en cinq jours.** Trajectoire sur 82 jours : 136 / 143 / 143 / 146 / 146 / 330 / 330 / 332 / 333 / 334 / 334 / 142 / **91**. Le corpus declare a perdu 73 % de son volume depuis le pic du 24/08.

Mais la nature du phenomene a change, et c'est le point important de ce run. **La semaine derniere, les 192 URLs sorties du sitemap repondaient toutes en HTTP 200 : rien n'avait ete depublie, seul le sitemap avait bouge. Cette semaine, les pages sorties renvoient 404.**

Verifie sur un echantillon de 10 fiches wiki presentes au 31/08 et absentes aujourd'hui : `/wiki/e-e-a-t/`, `/wiki/needs-met/`, `/wiki/quality-rating/`, `/wiki/budget-crawl/`, `/wiki/canonical/`, `/wiki/helpful-content/`, `/wiki/llms-txt/`, `/wiki/schema-org/` renvoient **404**. Le hub `/wiki` ne liste plus que 23 fiches, le sitemap en declare 23, et les 23 repondent 200. Hub, sitemap et pages sont coherents entre eux.

Cette coherence change le diagnostic. Un build sitemap casse produit un sitemap appauvri avec des pages toujours servies, ce qui etait le tableau du 31/08. Ici le hub a ete mis a jour en meme temps que le sitemap et que les pages. **La signature est celle d'un elagage editorial volontaire, pas d'une regression technique.** L'hypothese C1 posee le 31/08 doit etre revue en consequence.

Deux reserves toutefois. Sur les 10 fiches testees, deux repondent encore 200 : `/wiki/featured-snippet/` et `/wiki/topical-authority/`. Elles ne sont ni dans le hub, ni dans le sitemap, et restent servies. Ce sont des restes d'elagage. Par ailleurs les 17 pages `/statuts-indexation-google/*` sont toujours en HTTP 200 et toujours hors sitemap depuis le 31/08, tout comme les six sections sorties la semaine derniere (`/guide-evaluateurs-google/`, `/newsletter/`, `/mises-a-jour-google/`, `/strategies/`, `/robots-ia/`, `/actualites/`), verifiees 200 aujourd'hui.

**Anomalie nouvelle et couteuse : `/tarifs` est absente du sitemap.** La page repond 200, porte un canonical propre vers elle-meme, un `robots: index, follow`, 797 mots, un `<h1>` commercial, et elle est liee depuis **les 91 pages du site** (navigation ou pied de page). C'est la page de prix, la plus proche de la conversion, et le sitemap ne la declare pas.

**Fondamentaux techniques tenus sur les 91 URLs restantes** : 91/91 en HTTP 200 final, 91/91 avec canonical strictement egal a l'URL finale, aucun `noindex` en meta, aucun `X-Robots-Tag` sur echantillon, `<title>` present et unique sur 91/91, `<h1>` present sur 91/91, aucune page bloquee par `robots.txt`. **Cinquieme semaine consecutive sans regression technique sur les URLs presentes.**

**Verifications validees** (91 pages)
- HTTP 200 final : 91 / 91
- Absence de `noindex` en meta : 91 / 91
- Absence de `X-Robots-Tag` : echantillon 2 URLs
- `<link rel=canonical>` egal a l'URL finale : 91 / 91
- `<title>` present, aucun doublon : 91 / 91
- `<h1>` present : 91 / 91
- Non bloque par `robots.txt` : 91 / 91

**Verifications avec anomalies**
- Sitemap contracte : **91 URLs** (contre 142 au 31/08, delta -51)
- Page commerciale vivante et maillee absente du sitemap : **1** (`/tarifs`)
- Page critique en 404 : **1** (`/manifeste`)
- Pages orphelines (0 lien entrant sur les 91) : **4**
- Sitemap declarant des URLs non canoniques : **91 / 91**
- `lastmod` uniforme : **91 / 91** (`2026-09-04`)
- Contenu sous 300 mots : **4 / 91**
- Pages vivantes hors sitemap identifiees : **au moins 21** (17 `/statuts-indexation-google/*` + 2 restes wiki + `/tarifs` + `/wiki/featured-snippet/`)

## Anomalies CRITIQUES

### C1. `/tarifs` absente du sitemap alors qu'elle est liee depuis les 91 pages

| Signal | Valeur |
|---|---|
| HTTP | 200 |
| canonical | `https://organikk.co/tarifs/` |
| meta robots | `index, follow` |
| `<title>` | *Tarifs Organikk : prestation SEO/GEO et accompagnement 1:1* |
| `<h1>` | *Nos tarifs pour une prestation SEO complete.* |
| mots | 797 |
| liens internes entrants | **91 / 91** |
| present dans le sitemap | **non** |

Tout est propre sur la page. Seul le sitemap l'ignore. Le maillage sitewide fait que Google la decouvrira de toute facon, donc l'impact n'est pas une absence totale d'indexation, mais la page de conversion est la seule page commerciale du site a ne pas beneficier du signal de decouverte et de recrawl que recoivent les 91 autres.

Detectee via `/plan-du-site` : sur les 58 liens que cette page expose, 57 sont dans le sitemap, `/tarifs` est le seul absent.

Action : ajouter `/tarifs` a la generation du sitemap. Une ligne. Verifier dans la foulee la regle qui l'a exclue, puisqu'elle a laisse passer 57 URLs sur 58.

### C2. Le sitemap continue de se contracter, et cette fois par depublication reelle

Detail du delta 142 -> 91 par section :

| Section | 31/08 | 05/09 | Delta |
|---|---|---|---|
| `/wiki/*` | 56 | 23 | **-33** |
| `/statuts-indexation-google/*` | 17 | 0 | **-17** |
| `/glossaire/*` | 7 | 4 | -3 |
| `/blog/*` | 29 | 28 | -1 |
| `/outils/*` | 5 | 4 | -1 |
| `/secteurs/*` | 3 | 2 | -1 |

Les 33 fiches wiki sorties ne sont pas seulement dereferencees : l'echantillon montre qu'elles sont **supprimees** (8 sur 10 en 404). Le hub `/wiki` a ete mis a jour en consequence. C'est coherent, donc probablement voulu.

Ce qui reste a arbitrer :

- **Les 404 ne sont pas redirigees.** Trente-trois URLs qui existaient il y a cinq jours renvoient une erreur. Si certaines avaient des positions ou des liens entrants, le signal est perdu sec. Une redirection 301 vers la fiche survivante la plus proche, ou vers `/wiki`, coute une ligne par URL et preserve ce qui existait.
- **Les 17 pages `/statuts-indexation-google/*` sont dans un etat batard** : vivantes, servies en 200, mais hors sitemap et hors hub depuis le 31/08. Soit elles restent et il faut les redeclarer, soit elles partent et il faut les rediriger. L'etat actuel ne sert ni l'un ni l'autre.
- **Deux restes d'elagage** : `/wiki/featured-snippet/` et `/wiki/topical-authority/` repondent 200 sans etre listees nulle part. Meme arbitrage.

Note de revision : le 31/08, ce rapport avait pose l'hypothese d'une regression du build sitemap. Les elements de ce run ne la soutiennent plus pour la partie wiki, ou la depublication est nette et coherente. Elle reste ouverte pour les 192 URLs du 31/08, qui sont toujours servies en 200 et toujours hors sitemap une semaine plus tard.

### C3. `/manifeste` toujours en 404 : 10e recurrence, 57 jours

`curl -sIL https://organikk.co/manifeste/` renvoie **404**. Meme reponse sans slash final. La page n'est pas dans le sitemap et aucun `<a href>` des 91 pages telechargees ne pointe vers elle.

La recommandation P1 du 10/07 (redirection 301 vers `/methode/`) n'est pas appliquee. **57 jours d'ouverture.** Au 10/07, la GSC comptait 30 impressions sur 28 jours sur cette URL, deuxieme page du site en impressions.

Action inchangee : `301 /manifeste{,/} -> /methode/`. Une ligne dans `_redirects` ou `netlify.toml`. Jamais de 410.

### C4. Quatre pages orphelines, dont trois pages d'offre

Calcul sur les 91 pages telechargees, hors auto-reference :

| URL | Liens entrants | Mots | Recurrence |
|---|---|---|---|
| `/accompagnement-seo-geo` | 0 | 1 715 | **10e** (57 jours) |
| `/consultant-geo` | 0 | 2 877 | **5e** (26 jours) |
| `/formation-seo-ia` | 0 | 867 | **4e** (19 jours) |
| `/secteurs` | 0 | 144 | **9e** |

Les trois premieres sont des pages d'offre substantielles, decouvrables uniquement par le sitemap. `/secteurs` est un hub de 144 mots qui lie deux pages enfant sans etre lui-meme lie.

Action : lier les trois pages d'offre depuis `/methode`, `/systeme` ou la navigation principale. Lier `/secteurs` depuis le pied de page ou `/plan-du-site`.

## Anomalies mineures

- **`sitemap_canonical_mismatch` : 14e recurrence.** Les 91 URLs du sitemap sont declarees sans slash final et redirigent toutes en 301 vers la version avec slash, qui est la forme canonique. Le sitemap fait donc traverser une redirection a chaque URL. Recommandation P1 ouverte depuis le 15/06, **82 jours**.
- **`lastmod_uniforme` : 14e recurrence.** Les 91 URLs portent `2026-09-04`, date du dernier build, et non la date de derniere modification reelle. Le `lastmod` ne porte aucune information exploitable pour la priorisation de recrawl. Recommandation P2 ouverte depuis le 15/06, **82 jours**.
- **Quatre pages sous 300 mots** : `/secteurs` (144), `/contact` (179), `/resultats` (224), `/glossaire/serp-ranking` (270). `/resultats` et `/secteurs` sont des pages a vocation commerciale, donc les deux qui meritent l'arbitrage. Contre 4/141 au 31/08 : la proportion monte mecaniquement avec la reduction du corpus, le volume absolu est stable.
- **`robots.txt` toujours reduit** a `User-Agent: * / Allow: /` plus la directive `Sitemap`. Les quatre sections privees en `Disallow` disparues au 31/08 ne sont pas revenues. Impact probablement neutre, ces URLs n'etant pas dans le sitemap public, mais l'ecart avec l'etat anterieur reste non explique.

## Recommandations priorisees

1. **Ajouter `/tarifs` au sitemap et auditer la regle d'exclusion** : effort trivial, impact fort. C'est la page de prix.
2. **Arbitrer l'elagage wiki : rediriger les 33 URLs supprimees** vers la fiche survivante la plus proche ou vers `/wiki` : effort moyen, impact moyen a fort selon les positions perdues. A faire vite, la valeur d'une 301 decroit avec le temps.
3. **Trancher le sort des 17 `/statuts-indexation-google/*`** et des 2 restes wiki : redeclarer ou rediriger : effort faible, impact moyen.
4. **Appliquer la 301 `/manifeste` -> `/methode`** : effort trivial, impact faible mais ouvert depuis 57 jours.
5. **Lier les trois pages d'offre orphelines** depuis la navigation ou les pages de methode : effort faible, impact moyen.

## Limites de ce rapport

- **Statut d'indexation Google non mesure.** La methode de scraping `site:` a ete invalidee par un test temoin ce run : l'URL inexistante `/cette-page-nexiste-absolument-pas-xyz123/` ressort « indexee » avec le meme score qu'une URL reelle, la chaine du domaine etant presente dans la requete que Google reaffiche. Une requete sur trois a par ailleurs ete bloquee en rate-limit. Aucune URL ne peut donc etre declaree indexee ni non indexee ce run. **Non testable n'est pas non indexee.**
- L'acces `urlInspection API` reste en attente dans `memory/questions.md` depuis le 10/07, soit **57 jours**. Derniere mesure fiable d'indexation : 10/07 (49/146 confirmees). Cet aveuglement est particulierement penalisant ce run : impossible de mesurer ce que Google a deja retire des 33 fiches wiki supprimees ni des 192 URLs sorties le 31/08.
- Le diff wiki 56 -> 23 repose sur un echantillon de 10 slugs testes, les rapports precedents ne conservant pas la liste des URLs. Le comptage par section (56 puis 23) est exact, l'identification nominale des 33 fiches disparues ne l'est pas. **Recommandation systeme : persister la liste des URLs de chaque run pour rendre les diffs exacts.**
- Le caractere volontaire de l'elagage est une inference tiree de la coherence hub / sitemap / HTTP, pas une information confirmee par Tim.
