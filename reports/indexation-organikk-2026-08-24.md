---
type: audit
title: "Audit indexation Organikk - 2026-08-24 (site complet, sitemap 334 URLs, densification massive des pSEO)"
date: 2026-08-24
perimetre: "https://organikk.co - 334 URLs du sitemap (site entier)"
sources_de_verite: ["HTTP status (curl -sIL, 334/334 URLs)", "https://organikk.co/sitemap.xml", "https://organikk.co/robots.txt", "DOM meta robots / canonical / h1 / title (334 pages telechargees)", "wordcount HTML body via strip regex methode C (script+style+noscript enleves, meme methode qu'au 2026-08-17)", "graphe interne calcule sur les 334 pages telechargees", "echantillon X-Robots-Tag sur 11 URLs"]
indexation_google_estimee: "non mesuree ce run (pas d'acces GSC dans cet environnement, cf. Limites)"
pages_testees: 334
anomalies_critiques: 4
anomalies_mineures: 5
loop: indexation-check
---

# Audit indexation Organikk - 2026-08-24

## Synthese

Sitemap a **334 URLs (delta 0 vs 2026-08-17)**. Trajectoire 70 jours : 136 / 143 / 143 / 146 / 146 / 330 / 330 / 332 / 333 / 334 / 334. Premiere semaine sans ajout de page depuis le 27/07. **Aucun nouveau contenu publie**, mais **densification editoriale massive** sur trois sections pSEO simultanement et sur le corpus wiki.

Fondamentaux techniques tenus au meme niveau que la semaine derniere : **334/334 en HTTP 200 final, 334/334 avec `<link rel=canonical>` present et strictement egal a l'URL finale, aucun `noindex` en meta HTML sur 334/334, aucun `X-Robots-Tag` server-side sur echantillon 11 URLs, `<title>` present sur 334/334, `<h1>` present sur 334/334**, aucune page bloquee par `robots.txt`. **Troisieme semaine consecutive sans regression technique.**

**Anomalies critiques : quatre cette semaine, meme perimetre qu'au 17/08.**
- `/manifeste{,/}` reste en `HTTP 404` (8e recurrence, **45 jours d'ouverture**). Prediction `pred-2026-08-17-manifeste-404-continue` confirmee (hit).
- `/accompagnement-seo-geo/` reste orpheline sur les 334 pages (8e recurrence, **45 jours**).
- `/consultant-geo/` reste orpheline (3e recurrence, **14 jours**).
- `/formation-seo-ia/` reste orpheline (2e recurrence, **7 jours**). Prediction `pred-2026-08-17-formation-seo-ia-orphaned` confirmee (hit).

**Recurrences structurelles atteignent leur 12e occurrence** : `sitemap_canonical_mismatch` (333/334 URLs redirigent en 301 vers leur variante slash final) et `lastmod_uniforme` (334/334 a `2026-08-24T04:40:28.030Z`, date du dernier build). Les P1 et P2 sont ouvertes depuis le 15/06, soit **70 jours** sans effet observable.

**Nouveaute positive du run : densification editoriale massive sur trois sections pSEO** (mise en oeuvre de la reco de fond du 20/07, arbitrage vendredi 2026-08-22 possible) :
- `/robots-ia/` : les 13 pages enfant passent de **245-295 mots** (10/08 et 17/08, 5 runs consecutifs sous 300) a **376-426 mots** (24/08). Aucune sous 300, 10/13 encore sous 400.
- `/statuts-indexation-google/` : les 16 pages enfant passent de **282-352 mots** (16/16 sous 400 au 17/08) a **397-469 mots**. Deux pages encore sous 400 (`soft-404` 397, `erreur-de-redirection` 399).
- `/mises-a-jour-google/` : moyenne 596 mots (contre 470 au 17/08), min 512 (contre 389). **Zero page sous 400 mots** (contre 3/27 au 17/08). Prediction `pred-2026-08-10-mises-a-jour-thin-drift` (drift vers >=5/27 sous 400 au 31/08) : trajectoire mesuree inverse a J+14, prediction en voie de miss anticipe.

**Corpus wiki egalement densifie** : moyenne 690 mots par fiche (contre 574 au 17/08), min 546 (contre 408). Toutes les fiches restent au-dessus de 400. Six semaines consecutives sans fiche wiki sous 400.

**Deux pages d'offre orphelines densifiees mais toujours sans lien entrant** :
- `/consultant-geo/` : **2900 mots** (contre 2650 au 17/08, +250). Orpheline depuis 14 jours.
- `/formation-seo-ia/` : **893 mots** (contre 761 au 17/08, +132). Orpheline depuis 7 jours.
- `/accompagnement-seo-geo/` : **1741 mots** (contre 1533, +208). Orpheline depuis 45 jours.

Le pattern « nouvelle page publiee sans plan de maillage » (soulève au 17/08) **n'a pas ete corrige structurellement**, mais aucun nouveau contenu n'a ete publie cette semaine, donc le pattern ne s'est pas reproduit. Prediction `pred-2026-08-17-pattern-new-orphan` reste ouverte (mesure au 14/09).

**Robots.txt modifie** : nouvelle section `Disallow: /stats-gsc-organikk-private-2026` ajoutee, portant a **4 sections privees** bloquees (contre 3 aux 11 runs precedents). Aucune URL publique impactee.

Statut d'indexation Google : **non teste ce run** (pas d'acces a l'edge `admin-gsc-export` depuis cet environnement d'execution). Derniere mesure fiable : 10/07 (49/146 confirmees, 97 indeterminees). Sur les 334 URLs actuelles, aucune ne peut etre declaree "non indexee" (`non testable` != `non indexee`, cf. Limites). Le diff `urlInspection API` reste en attente dans `memory/questions.md` depuis le 10/07 : **45 jours d'ouverture pour ce debloqueur systeme**.

Verifications validees sur 334/334 pages telechargees :
- `HTTP 200` final apres redirections (mesure sur 334/334 URLs via `curl -sIL`)
- Absence de `noindex` en `meta` HTML
- Absence de `X-Robots-Tag` server-side dans l'echantillon (11 URLs, dont racine, wiki, guide, robots-ia, statuts, blog, newsletter, mises-a-jour, consultant-geo, methode, formation-seo-ia)
- `<link rel=canonical>` present et strictement egal a l'URL finale
- `<title>` present et non vide
- `<h1>` present
- Non bloque par `robots.txt`

Verifications avec anomalies :
- Sitemap declare des URLs non canoniques : **333 / 334** (301 vers le slash final ; seule la racine echappe)
- `lastmod` uniforme sur tout le sitemap : **334 / 334** (`2026-08-24T04:40:28.030Z`)
- Pages orphelines (0 lien interne entrant) : **4 / 334** (identique au 17/08 : 3 pages d'offre + 1 hub `/secteurs/`)
- Pages sous-maillees (1 seul lien entrant) : **62 / 334** (18.6 %, identique aux 6 runs precedents)
- Contenu sous 300 mots : **0 / 334** (contre 18 / 334 au 17/08)
- Contenu sous 400 mots : **12 / 334** (contre 34 / 334 au 17/08)
- Page critique en 404 : **1** (`/manifeste/`)

## Anomalies critiques

### C1. `/manifeste{,/}` toujours 404 - 8e recurrence

`curl -sIL https://organikk.co/manifeste/` renvoie `HTTP 404`. Meme reponse sans slash. La page n'est pas dans le sitemap. Aucun `<a href>` vers `/manifeste` sur les 334 pages telechargees (0 lien interne pointe encore vers cette URL, confirmation grep sur toutes les pages).

Reco P1 du 10/07 (redirection 301 `/manifeste{,/} -> /methode/`) : non appliquee. **45 jours d'ouverture**. Prediction `pred-2026-08-17-manifeste-404-continue` confirmee (hit).

Au 10/07, la GSC comptait 30 impressions sur 28 jours sur cette URL (2e page du site en impressions). Sans reprise de la mesure GSC ce run, on ne sait pas si Google la sert encore, mais tant que la 404 est en place, chaque impression eventuelle est perdue et chaque backlink externe pointant vers `/manifeste` tombe dans le vide.

Action inchangee : `301 /manifeste{,/} -> /methode/`. Une ligne dans `_redirects` / `netlify.toml`. Jamais de 410.

### C2. `/accompagnement-seo-geo/` toujours orpheline - 8e recurrence

Verifie par crawl des 334 pages : la chaine `accompagnement-seo-geo` n'apparait que sur sa propre page (auto-reference).

Page d'offre solide (`HTTP 200`, canonical propre, `1741 mots` methode C ce run, `+208` mots vs 17/08). `h1` : *Remonter sur Google et etre cite par les IA*. Densification en cours mais la page reste decouvrable uniquement par le sitemap.

Reco C2 du 10/07 (mailler depuis `/systeme/`, `/methode/`, `/accompagnement-1-1-30-jours/`) : non appliquee. **45 jours d'ouverture**.

Action inchangee : trois liens ancre naturels depuis les trois hubs.

### C3. `/consultant-geo/` toujours orpheline - 3e recurrence

`HTTP 200`, canonical `https://organikk.co/consultant-geo/`, `<h1>` present, **2900 mots** (methode C, contre 2650 au 17/08). Aucun lien entrant sur les 334 pages ce run non plus.

Reco C3 du 10/08 (mailler depuis 2-4 hubs pertinents) : non appliquee apres 14 jours. Prediction `pred-2026-08-17-formation-seo-ia-orphaned` confirmee sur analogue (hit).

Le cas reste parallele a C2 : pages d'offre longues, densifiees, isolees, publiees successivement sans plan de maillage. **Signal repete : l'emission d'une reco critique ne suffit toujours pas a la faire executer** apres 14 jours. Point deja remonte au vendredi.

Action inchangee : 2 a 4 liens ancre depuis `/systeme/`, `/methode/`, `/consultant-lead-seo/`, `/coaching-seo-lyon/`, `/freelance-geo-lyon/`.

### C4. `/formation-seo-ia/` toujours orpheline - 2e recurrence

`HTTP 200`, canonical propre, **893 mots** (contre 761 au 17/08, +132). Verification maillage : la chaine `formation-seo-ia` n'apparait dans un `<a href>` d'aucune des 334 pages telechargees (auto-reference exceptee). Aucun lien depuis `/systeme/`, `/methode/`, `/bootcamp/`, `/coaching-seo-lyon/`, `/accompagnement-seo-geo/`, `/accompagnement-1-1-30-jours/`, `/consultant-geo/`.

Reco C4 du 17/08 (mailler depuis 2-3 hubs) : non appliquee. Prediction `pred-2026-08-17-formation-seo-ia-orphaned` confirmee (hit).

**Trois pages d'offre longues orphelines simultanement** cette semaine (accompagnement-seo-geo, consultant-geo, formation-seo-ia). Cumul 3234 + 2900 + 893 + 1741 = **7268 mots de contenu commercial** decouvrable uniquement par le sitemap, dont Google apprend a ignorer le `lastmod` (M2, 12e recurrence, 70 jours). Sur un site dont 20 % des URLs (68 pages orphelines + sous-maillees) manquent deja de signal de decouverte, isoler la totalite du contenu de conversion est un choix structurel qui appelle une decision explicite.

Action inchangee : mailler `/formation-seo-ia/` depuis 2-3 hubs pertinents (`/systeme/`, `/methode/`, `/bootcamp/`, `/accompagnement-1-1-30-jours/`, `/coaching-seo-lyon/`).

## Anomalies mineures

### M1. Sitemap declare 333 URLs non canoniques - 12e recurrence

333 des 334 `<loc>` du sitemap sont declares sans slash final. Le serveur renvoie `301` vers `<path>/` sur ces 333. Seule exception : la racine `https://organikk.co`, servie directement en 200 sans redirection.

Le canonical du DOM pointe correctement vers la version avec slash sur 334/334. Aucun risque d'indexation duale, mais chaque URL du sitemap coute un aller-retour de crawl inutile. **333 requetes 301 inutiles par cycle de crawl**, chiffre stable.

P1 ouverte depuis le 15/06, sans effet observable apres **70 jours**.

### M2. `lastmod` uniforme sur 334/334 - 12e recurrence

Toutes les URLs portent `2026-08-24T04:40:28.030Z`, date du dernier build. `sort -u` sur les `<lastmod>` renvoie une seule ligne : 334 occurrences. Meme pattern qu'aux 11 runs precedents. Google apprend a ignorer ce champ.

Consequence renforcee cette semaine : sur les trois sections densifiees (`/robots-ia/` 13 pages, `/statuts-indexation-google/` 16 pages, `/mises-a-jour-google/` 26 pages, soit 55 URLs re-editees), **aucun signal serveur ne va dire a Google que ces pages ont ete substantiellement modifiees**. Le vrai travail editorial de la semaine est invisible cote sitemap.

P2 ouverte depuis le 15/06, sans effet observable apres **70 jours**. **Cet impact est desormais tangible** : sans `lastmod` par page, la vague de densification observee ce run ne generera pas de signal de recrawl priorise.

### M3. `/secteurs/` reste orpheline - 8e recurrence

Hub de section pour deux pages enfants (`/secteurs/avocat/`, `/secteurs/hotellerie/`). Toujours zero lien interne entrant.

**Densification observee** : **417 mots** (contre 283 au 17/08, +134). Le hub passe au-dessus du seuil de 400 mots. Le statut "mince" (< 300 mots) est resolu ; le statut "orpheline" persiste (8e recurrence).

Action revue : maintenant que la page a du fond (417 mots), les deux options sont symetriques :
- soit mailler depuis 2 pages amont (`/methode/`, `/blog/`, `/actualites/`) pour lui donner une raison d'exister,
- soit retirer du sitemap si elle ne doit pas ranker seule.

### M5. Section `/robots-ia/` : 10/13 pages enfant sous 400 mots - 6e occurrence, statut evolue

**Etat change ce run.** Sur 14 URLs de la section : le hub `/robots-ia/` a 837 mots (contre 702 au 17/08, +135), les 13 pages enfant sont maintenant entre **376 et 426 mots** (methode C, moyenne 390). Distribution :
- 10/13 pages entre 376 et 400 mots
- 3/13 pages entre 400 et 426 mots (`gptbot` 400, `applebot-extended` 401, `google-extended` 426)

Comparaison 17/08 : 13/13 pages entre 245 et 295 mots (moyenne 262). **Densification de +128 mots par page en moyenne**, la section passe totalement au-dessus de 300 mots. **10 pages restent legerement sous 400** (fourchette resserree 376-399).

C'est la **premiere application partielle de la reco du 20/07** (soit assumer format Know-Simple court, soit densifier a >=400 mots). L'orientation choisie apparait : densification, pas format court. Il manque environ 15-25 mots par page pour franchir les 400. **A trancher au vendredi** : viser >=400 sur les 10 restantes, ou laisser en l'etat.

### M6. Section `/statuts-indexation-google/` : 2/16 pages enfant sous 400 mots - 5e occurrence, statut evolue

**Etat change ce run.** Sur 17 URLs : le hub a 816 mots (contre 673 au 17/08, +143), les 16 pages enfant sont maintenant entre **397 et 469 mots** (moyenne 433).

- 2 pages a 397 et 399 mots (`soft-404` 397, `erreur-de-redirection` 399), a 1-3 mots du seuil de 400
- 14 pages entre 401 et 469 mots

Comparaison 17/08 : 16/16 pages sous 400 mots (fourchette 282-352, moyenne autour de 330). **Densification de +80 a +150 mots par page**, la section passe quasi entierement au-dessus de 400 mots.

Meme constat que M5 : densification appliquee, deux pages a moins de 5 mots du seuil. Action naturelle : ajouter 5-10 mots sur `soft-404` et `erreur-de-redirection` pour finir la mise a niveau.

### M7. Section `/mises-a-jour-google/` : 0/26 pages enfant sous 400 mots - 3e occurrence, statut RESOLU

**Etat change ce run.** Sur 27 URLs de la section : moyenne 575 mots (contre 470 au 17/08, +105), min 512 (contre 389), max 670. Le hub a 1146 mots. **Zero page sous 400 mots** (contre 3 au 17/08 : `june-2024-spam-update` 389, `june-2026-spam-update` 390, `march-2026-spam-update` 393). Les trois pages nommees sont maintenant a 512, 514, 520 mots respectivement.

Prediction `pred-2026-08-10-mises-a-jour-thin-drift` (>=5/27 sous 400 mots au 31/08) : trajectoire mesuree inverse a J+14 (0/26 aujourd'hui contre 3/27 au 10/08). **Le drift editorial du template pSEO court ne s'est pas produit** ; la section a ete densifiee. Prediction en voie de miss anticipe, resolution formelle au 31/08.

Statut mineur ferme en positif ce run.

### M8. Divergence title/h1 : `/formation-seo-ia/`, `/accompagnement-1-1-30-jours/`, `/accompagnement-seo-geo/` - 3 cas ouverts

- `/formation-seo-ia/` : title `Formation SEO & IA` (5 mots) / h1 `Ne vous contentez pas d'utiliser l'IA. Construisez votre systeme SEO.` (14 mots). Aucun mot substantif commun. **2e recurrence** (14 jours d'ouverture).
- `/accompagnement-1-1-30-jours/` : title `Coaching SEO` / h1 `Votre systeme SEO proprietaire pour ranker sur Google et les LLM, sans repartir de zero.` **Signale depuis 03/08, 21 jours d'ouverture**.
- `/accompagnement-seo-geo/` : title `Accompagnement SEO + GEO pour PME` / h1 `Remonter sur Google et etre cite par les IA`. **Nouveau ce run** : aucun mot substantif commun releve (`accompagnement`/`SEO`/`GEO`/`PME` d'un cote ; `Remonter`/`Google`/`cite`/`IA` de l'autre). 1re detection ; c'est aussi une des trois pages d'offre orphelines (C2), donc a traiter groupe.

Priorite basse au sens technique (pas d'impact HTTP ou canonical), mais **trois pages commerciales sur trois** avec divergence title/h1 sans mot substantif commun est un signal editorial coherent : le title n'est pas repris du h1 sur la stack commerciale. A grouper en une decision editoriale unique au vendredi.

## Observations positives

**Densification editoriale massive sur trois sections pSEO en une semaine.** Les sections `/robots-ia/` (13 pages), `/statuts-indexation-google/` (16 pages) et `/mises-a-jour-google/` (26 pages) ont ete re-editees simultanement, ajoutant environ +100 a +130 mots par page. C'est la reponse editoriale la plus large observee depuis le debut de l'audit (15/06), et la premiere fois qu'une reco de fond (celle du 20/07) est appliquee sur cette echelle.

**Fondamentaux techniques stables au meilleur niveau depuis le 10/07.** 334/334 en HTTP 200, 334/334 avec canonical strictement egal a l'URL finale, 334/334 avec `<title>` et `<h1>`, 334/334 telechargeables. Aucun `X-Robots-Tag` server-side dans l'echantillon 11 URLs. **Troisieme semaine consecutive sans regression technique.**

**Le corpus wiki continue sa densification.** 56 fiches (identique 17/08), moyenne 690 mots (contre 574 au 17/08), min 546 (contre 408), max 856 sur les enfants (hub `/wiki/` a 2010 mots). Aucune fiche sous 400 mots. Six semaines consecutives au-dessus du seuil depuis le 13/07.

**Trois pages d'offre orphelines densifiees.** `/consultant-geo/` +250 mots, `/formation-seo-ia/` +132 mots, `/accompagnement-seo-geo/` +208 mots. Le fond est traite, meme si le maillage entrant ne suit pas.

**Section `/secteurs/` remontee au-dessus de 400 mots.** 417 mots contre 283 au 17/08. Le statut "mince" est ferme.

## Autres observations

**Aucun nouveau contenu publie cette semaine.** Sitemap delta 0 (334 -> 334). Comptage par section strictement stable :
- wiki 56 / guide 103 / blog 29 / newsletter 29 / mises-a-jour 27 / statuts 17 / strategies 15 / robots-ia 14 / glossaire 7 / outils 5 / actualites 4 / secteurs 3 / bootcamp 2 / etc.

Le run confirme que le pattern « nouvelle page publiee sans plan de maillage » (C3 au 10/08, C4 au 17/08) ne se reproduit pas quand aucune page n'est publiee. Prediction `pred-2026-08-17-pattern-new-orphan` toujours ouverte (resolve 14/09) : elle se resoudra sur la prochaine URL ajoutee au sitemap.

**Robots.txt modifie.** Ajout d'une nouvelle section privee bloquee : `Disallow: /stats-gsc-organikk-private-2026` (avec et sans slash). Le fichier passe de 3 a 4 sections privees. Aucune URL publique du sitemap n'est impactee (les 334 URLs restent autorisees). Observation neutre, a noter pour la trace historique.

**Repartition du wordcount (methode C, meme methode qu'au 17/08)**. Corpus 334 pages, moyenne autour de 1220 mots, fourchette 188 (`/contact/`) - 12655 (article de blog). Trois familles editoriales inchangees, avec bornes basses relevees :
- **Long-form** : `/blog/` (mean 4070), `/strategies/` (mean 4052), `/glossaire/` (mean 1077)
- **Medium** : `/newsletter/` (951), `/methode/` 1798, `/systeme/` 624, pages d'offre uniques (accompagnement 1741, consultant-geo 2900, formation-seo-ia 893)
- **Court/template maintenant releve** : `/robots-ia/` (mean 390 enfants), `/statuts-indexation-google/` (mean 433 enfants), `/mises-a-jour-google/` (mean 575 enfants)

**62 pages sous-maillees (1 seul lien entrant), meme repartition que les six runs precedents** :
- `/guide-evaluateurs-google/*` : 32 sur 103 (le hub distribue vers 103 enfants, mais 32 enfants n'ont *que* ce lien, aucune reference croisee entre chapitres freres)
- `/newsletter/*` : 18 sur 29
- `/strategies/*` : 5 sur 15
- `/actualites/*` : 3 sur 4
- 4 pages isolees (`/resultats/`, `/freelance-geo-lyon/`, `/bootcamp-quiz/`, `/bootcamp/`)

Aucun mouvement sur le maillage transverse en une semaine. Reco 4 (chapitre precedent / suivant sur `/guide-evaluateurs-google/*`) reconduite pour la 6e semaine.

**Divergence title/h1 sur `/accompagnement-1-1-30-jours/` (signalee au 03/08) : toujours presente au 24/08 (21 jours d'ouverture).** Groupee avec les deux autres cas (M8) pour une decision editoriale unique.

**Scraping `site:` sur Google : toujours retire de l'audit.** Le check #8 du skill reste desactive tant que Tim n'a pas tranche le diff propose (`loops/indexation-check/memory/questions.md`, en attente depuis le 10/07, **45 jours d'ouverture**).

**Predictions ouvertes au 17/08, resolues aujourd'hui** :
- `pred-2026-08-17-formation-seo-ia-orphaned` : **hit** (page reste orpheline au 24/08).
- `pred-2026-08-17-manifeste-404-continue` : **hit** (404 persiste, 8e recurrence).

**Predictions ouvertes avec mesure intermediaire** :
- `pred-2026-08-10-mises-a-jour-thin-drift` (resolve 31/08) : mesure intermediaire a J+14 : 0/26 sous 400 mots contre 3/27 au 10/08. **Trajectoire inverse a celle predite** ; le drift ne se produit pas. Miss quasi certain a la resolution du 31/08.
- `pred-2026-08-17-pattern-new-orphan` (resolve 14/09) : aucune nouvelle URL cette semaine, prediction non testable en l'etat. A rearmer au prochain ajout au sitemap.

## Recommandations priorisees

1. **Rediriger `/manifeste{,/}` en 301** vers `/methode/`. **8e reconduite consecutive.** Une ligne dans `_redirects`. Toujours le seul point urgent : la page morte est servie a chaque impression Google (mesuree a 30 imp / 28j au 10/07, non re-mesuree ce run).

2. **Mailler `/accompagnement-seo-geo/`** depuis `/systeme/`, `/methode/` et `/accompagnement-1-1-30-jours/`. **8e reconduite consecutive.** Trois liens ancre.

3. **Mailler `/consultant-geo/`** depuis 2-4 hubs pertinents (`/systeme/`, `/methode/`, `/consultant-lead-seo/`, `/coaching-seo-lyon/`, `/freelance-geo-lyon/`). **3e reconduite.** 14 jours d'ouverture.

4. **Mailler `/formation-seo-ia/`** depuis 2-3 hubs pertinents (`/systeme/`, `/methode/`, `/bootcamp/`, `/accompagnement-1-1-30-jours/`, `/coaching-seo-lyon/`). **2e reconduite.** 7 jours d'ouverture.

5. **Formaliser la regle systeme "toute nouvelle URL publiee = 2 backlinks entrants au moment de la mise en ligne"**. Reco du 17/08 reconduite. Le fait qu'aucune page n'ait ete publiee cette semaine met la reco en pause mesurable mais ne la resout pas. **A arbitrer au vendredi** comme decision structurelle.

6. **Finir la densification des sections `/robots-ia/` et `/statuts-indexation-google/`**. Nouveau. 10 pages `/robots-ia/*` a 376-399 mots (manquent 1-24 mots pour franchir 400). 2 pages `/statuts-indexation-google/*` a 397 et 399 mots. Effort marginal maintenant que la vague de densification a ete faite. Alternative : assumer explicitement que ces pages restent format Know-Simple court et retirer la reco de seuil pour la section.

7. **Corriger le sitemap** : declarer les URLs avec le slash final, alimenter `lastmod` depuis la vraie date de derniere modification de contenu par page. Reconduite du 15/06 (**70 jours d'ouverture**). Impact renforce ce run : la vague de densification observee sur 55 URLs (`/robots-ia/*`, `/statuts-indexation-google/*`, `/mises-a-jour-google/*`) est invisible cote sitemap. Google n'a aucun signal serveur pour recrawler prioritairement ces pages.

8. **Ajouter du maillage transverse dans `/guide-evaluateurs-google/`.** Reconduite du 20/07. Priorite : liens "chapitre precedent / chapitre suivant" (ordre du QRG) sur les 103 pages, plus quelques references croisees explicites entre concepts lies. Ratio inchange en 35 jours.

9. **Trancher sur `/secteurs/`** : maintenant que le hub est densifie (417 mots), soit vraie navigation vers les enfants avec 2 pages amont qui pointent vers le hub, soit retrait du sitemap. **8e reconduite.**

10. **Brancher `urlInspection/index:inspect`** a cote de `admin-gsc-export` (diff en attente du 10/07 dans `memory/questions.md`). **45 jours d'ouverture pour ce debloqueur systeme.** La vague de densification editoriale de cette semaine ne pourra pas etre evaluee en couverture d'indexation reelle sans cet endpoint.

11. **Aligner title et h1 sur `/accompagnement-1-1-30-jours/`, `/formation-seo-ia/`, `/accompagnement-seo-geo/`.** (M8, trois cas ouverts). Trois pages commerciales groupables en une decision editoriale unique. Priorite basse. Trois modifs HTML.

## Limites de ce rapport

- **Statut d'indexation Google non teste.** Pas d'acces a l'edge `admin-gsc-export` depuis cet environnement d'execution. La derniere mesure fiable est celle du 10/07 (49/146 confirmees, 97 indeterminees). Sur les 334 URLs actuelles, aucune ne peut etre declaree "non indexee". Aucune estimation n'a ete inventee. L'ecart `non indexee` / `non testable` est explicite.
- **X-Robots-Tag verifie sur echantillon de 11 URLs**, pas sur les 334. Aucun `noindex` server-side dans l'echantillon.
- **Methode wordcount = methode C** (body + strip scripts + strip styles + strip noscript, sans exclusion nav/footer). Meme methode qu'au 17/08 et 10/08. Les chiffres de ce run se comparent directement aux deux runs precedents.
- **Fenetre de decouverte = sitemap.** Comme aux runs precedents, une page vivante absente du sitemap et sans lien entrant echapperait a cet audit. C'est exactement ce qui s'est passe pour `/manifeste` au 10/07 (rattrapee uniquement par la mesure GSC). Sans reprise de la mesure GSC, cette classe de bug redevient invisible.
- **Maillage calcule sur les 334 pages du sitemap uniquement.** Un lien depuis une page hors sitemap ne serait pas compte. Les 4 pages orphelines pourraient recevoir des liens depuis des pages non listees au sitemap (navigation dynamique JS, blog en preview, etc.) que ce HTML statique ne montre pas.
- **Densification editoriale mesuree par wordcount, pas par qualite.** Le passage de 262 mots a 390 mots sur `/robots-ia/*` (moyenne) est mesurable ; la valeur ajoutee editoriale (est-ce du padding ou du contenu utile ?) n'est pas evaluee ici. C'est le boulot du skill `seo-cluster-aeo` ou d'un audit editorial.
- **Sections pSEO recentes non evaluees qualitativement.** Ce run mesure la sante technique (HTTP, canonical, robots, wordcount, backlinks) mais pas la qualite editoriale ni la differentiation vecteurs des 103 pages `/guide-evaluateurs-google/*` ni des 14 pages `/robots-ia/*` ni des 17 pages `/statuts-indexation-google/*` ni des 27 pages `/mises-a-jour-google/*`.

## Liens

Runs precedents : [[reports/indexation-organikk-2026-06-15]], [[reports/indexation-organikk-2026-06-22]], [[reports/indexation-organikk-2026-06-29]], [[reports/indexation-organikk-2026-07-06]], [[reports/indexation-organikk-2026-07-10]], [[reports/indexation-organikk-2026-07-13]], [[reports/indexation-organikk-2026-07-20]], [[reports/indexation-organikk-2026-07-27]], [[reports/indexation-organikk-2026-08-03]], [[reports/indexation-organikk-2026-08-10]], [[reports/indexation-organikk-2026-08-17]].
Methode : [[gsc-export]], [[maillage-interne]].
Skills en attente de decision : [[loops/indexation-check/memory/questions]] (remplacement check #8 par urlInspection API, correction chemin validator, fix eval_health.py champ francais).
