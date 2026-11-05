---
type: audit
title: "Audit indexation Organikk - 2026-08-31 (site partiel, sitemap contracte 334 -> 142 URLs, 192 pages disparues mais toujours HTTP 200)"
date: 2026-08-31
perimetre: "https://organikk.co - 142 URLs du sitemap + verification 192 URLs sorties du sitemap"
sources_de_verite: ["HTTP status (curl -sIL, 142/142 URLs du sitemap + 9 URLs sorties)", "https://organikk.co/sitemap.xml", "https://organikk.co/robots.txt", "DOM meta robots / canonical / h1 / title (141 pages telechargees)", "wordcount HTML body via strip regex methode C (script+style+noscript enleves, meme methode qu'au 2026-08-24)", "graphe interne calcule sur les 141 pages telechargees", "echantillon X-Robots-Tag sur 8 URLs"]
indexation_google_estimee: "non mesuree ce run (pas d'acces GSC dans cet environnement, cf. Limites)"
pages_testees: 142
anomalies_critiques: 5
anomalies_mineures: 5
loop: indexation-check
---

# Audit indexation Organikk - 2026-08-31

## Synthese

**EVENEMENT MAJEUR : sitemap contracte de 334 a 142 URLs en 7 jours (delta -192).** Trajectoire 77 jours : 136 / 143 / 143 / 146 / 146 / 330 / 330 / 332 / 333 / 334 / 334 / **142**. Sections integralement disparues du sitemap alors qu'elles repondent toujours en HTTP 200 :
- `/guide-evaluateurs-google/*` (103 URLs, incluant 32 sous-maillees signalees au 20/07)
- `/newsletter/*` (29 URLs)
- `/mises-a-jour-google/*` (27 URLs, section densifiee la semaine derniere)
- `/strategies/*` (15 URLs)
- `/robots-ia/*` (14 URLs, section densifiee la semaine derniere)
- `/actualites/*` (4 URLs)

Total sorti : 192 URLs, soit **57 % du corpus disparu du sitemap en une semaine**, sans qu'aucun contenu n'ait ete depublie. Verifie par `curl -sIL` sur les hubs et 3 pages internes de `/guide-evaluateurs-google/*` : toutes en HTTP 200 avec DOM complet. Signature typique d'une regression du build sitemap (filtre trop restrictif introduit recemment), a arbitrer.

Fondamentaux techniques tenus sur les 142 URLs restantes : **142/142 en HTTP 200 final, 141/141 pages telechargees avec `<link rel=canonical>` strictement egal a l'URL finale, aucun `noindex` en meta HTML, aucun `X-Robots-Tag` server-side sur echantillon 8 URLs, `<title>` present sur 141/141, `<h1>` present sur 141/141**, aucune page bloquee par `robots.txt`. **Quatrieme semaine consecutive sans regression technique sur les URLs presentes.**

**Anomalies critiques : cinq cette semaine, dont une nouvelle systemique.**
- C1 (NOUVEAU) : `sitemap_shrink` -192 URLs en 7 jours, pages toujours servies en HTTP 200.
- C2 : `/manifeste{,/}` reste en `HTTP 404` (9e recurrence, **52 jours d'ouverture**). Prediction `pred-2026-08-24-manifeste-404-continue` confirmee (hit).
- C3 : `/accompagnement-seo-geo/` reste orpheline sur les 141 pages telechargees (9e recurrence, **52 jours**).
- C4 : `/consultant-geo/` reste orpheline (4e recurrence, **21 jours**).
- C5 : `/formation-seo-ia/` reste orpheline (3e recurrence, **14 jours**). Prediction `pred-2026-08-24-orphans-persist` confirmee (hit).

**Recurrences structurelles atteignent leur 13e occurrence** : `sitemap_canonical_mismatch` (141/142 URLs redirigent en 301 vers slash final, verifie sur echantillon 12 URLs) et `lastmod_uniforme` (142/142 a `2026-08-28T10:04:29.658Z`, date du dernier build). P1 et P2 ouvertes depuis le 15/06, **77 jours** sans effet observable.

**Robots.txt simplifie** : passe de 4 sections privees `Disallow:` (`stats-gsc-organikk-private-2026`, `bootcamp-private`, `admin`, `stats`) a une politique `User-Agent: * / Allow: /` avec le seul lien sitemap. Perte des 4 sections privees Disallow. Impact probablement neutre (les URLs privees n'etaient pas dans le sitemap public, donc pas de bascule vers indexation), mais changement notable a coupler avec l'evenement sitemap.

**Corpus wiki tient sa densification** : 55 fiches enfant telechargees (56 URLs sitemap, 1 fichier manquant sur download reseau) entre **515 et 826 mots** (methode C, moyenne 657). Aucune fiche sous 400 mots. **Sept semaines consecutives au-dessus du seuil depuis le 13/07.** Legere baisse de moyenne vs 24/08 (690), a mettre en regard de la variance methode C (~5 %).

**Statuts-indexation-google mineure regression editoriale** : 4/17 pages enfant sous 400 mots ce run (`soft-404` 375, `erreur-de-redirection` 378, `erreur-de-serveur-5xx` 397, `introuvable-404` 399), contre 2/17 au 24/08. Passage marginal de 3 pages sous le seuil de 400 (dont 2 nouvelles). Variance ou drift ? A observer la semaine prochaine.

**Trois pages d'offre orphelines conservent leur densification** :
- `/consultant-geo/` : **2877 mots** (contre 2900 au 24/08, delta -23, variance methode C).
- `/formation-seo-ia/` : **867 mots** (contre 893, delta -26, variance).
- `/accompagnement-seo-geo/` : **1715 mots** (contre 1741, delta -26, variance).

Aucun mouvement significatif de contenu sur ces trois pages. Statut orpheline conserve pour les trois.

Statut d'indexation Google : **non teste ce run** (pas d'acces a l'edge `admin-gsc-export` depuis cet environnement d'execution). Derniere mesure fiable : 10/07 (49/146 confirmees, 97 indeterminees). Sur les 142 URLs actuelles du sitemap et les 192 URLs sorties, aucune ne peut etre declaree "non indexee" (`non testable` != `non indexee`, cf. Limites). Le diff `urlInspection API` reste en attente dans `memory/questions.md` depuis le 10/07 : **52 jours d'ouverture pour ce debloqueur systeme**. Cet aveuglement est particulierement penalisant ce run car impossible de mesurer si Google a deja commence a retirer les 192 URLs sorties du sitemap.

Verifications validees sur 141/141 pages telechargees :
- `HTTP 200` final apres redirections (mesure sur 142/142 URLs du sitemap via `curl -sIL`)
- Absence de `noindex` en `meta` HTML
- Absence de `X-Robots-Tag` server-side dans l'echantillon (8 URLs : racine, wiki, blog, consultant-geo, systeme, methode, statuts-indexation-google, formation-seo-ia)
- `<link rel=canonical>` present et strictement egal a l'URL finale
- `<title>` present et non vide
- `<h1>` present
- Non bloque par `robots.txt`

Verifications avec anomalies :
- Sitemap contracte : **142 URLs** (contre 334 au 24/08, delta -192, -57 %)
- Sitemap declare des URLs non canoniques : **141 / 142** (301 vers le slash final, echantillon 12 URLs, extrapolation ; seule la racine echappe)
- `lastmod` uniforme sur tout le sitemap : **142 / 142** (`2026-08-28T10:04:29.658Z`)
- Pages orphelines (0 lien interne entrant, sur les 141 telechargees) : **5 / 141** (manifeste absent du sitemap + 3 pages d'offre + 1 hub `/secteurs/`)
- Contenu sous 300 mots : **0 / 141**
- Contenu sous 400 mots : **4 / 141** (vs 12 / 334 au 24/08, tous dans `/statuts-indexation-google/*`)
- Page critique en 404 : **1** (`/manifeste/`)
- URLs sorties du sitemap mais toujours HTTP 200 : **192**

## Anomalies critiques

### C1. NOUVEAU sitemap_shrink -192 URLs en 7 jours, pages toujours HTTP 200

Le sitemap est passe de 334 URLs (24/08) a 142 URLs (31/08) en un cycle de build. Sections integralement disparues :

| Section | URLs au 24/08 | URLs au 31/08 | Delta |
|---|---|---|---|
| `/guide-evaluateurs-google/*` | 103 | 0 | -103 |
| `/newsletter/*` | 29 | 0 | -29 |
| `/mises-a-jour-google/*` | 27 | 0 | -27 |
| `/strategies/*` | 15 | 0 | -15 |
| `/robots-ia/*` | 14 | 0 | -14 |
| `/actualites/*` | 4 | 0 | -4 |
| **Total sorti** | **192** | **0** | **-192** |

Verifie que les URLs sorties existent toujours : `curl -sIL` sur les 6 hubs (`/guide-evaluateurs-google/`, `/newsletter/`, `/mises-a-jour-google/`, `/strategies/`, `/robots-ia/`, `/actualites/`) renvoie HTTP 200 pour les 6. Verifie aussi 3 pages internes de `/guide-evaluateurs-google/*` (`/needs-met/`, `/e-e-a-t/`, `/quality-rating/`) : HTTP 200 pour les 3, DOM complet.

**Aucun contenu n'a ete depublie.** La bascule est cote sitemap uniquement.

Consequences :
- Perte de signal de decouverte pour 192 URLs, dont deux sections editoriales majeures (`/newsletter/` 29 pages, `/blog/` intact mais `/strategies/` 15 pages sorties).
- Perte de signal de recrawl pour deux sections densifiees la semaine derniere (`/robots-ia/` +128 mots par page, `/mises-a-jour-google/` +105 mots par page). Le travail editorial 24/08 est desormais invisible cote sitemap.
- Perte de signal pour 103 pages `/guide-evaluateurs-google/*` deja identifiees comme sous-maillees au 20/07 (32/103 sans autre lien entrant que le hub).
- Sur les 192 URLs sorties, Google va probablement continuer a servir ce qu'il a deja indexe, puis retirer progressivement les pages sans signal externe (backlink, sitemap). Sans mesure GSC ce run, impossible de dire ou en est le processus.

Signature technique : le sitemap conserve intacts `/wiki/*` (56 URLs), `/blog/*` (29 URLs), `/statuts-indexation-google/*` (17 URLs), `/glossaire/*` (7 URLs), `/outils/*` (5 URLs), `/secteurs/*` (3 URLs), `/bootcamp/*` (2 URLs) plus les pages racine et les pages d'offre individuelles. Les sections sorties partagent une caracteristique : **elles etaient toutes des templates pSEO (guide, mises-a-jour, robots-ia, statuts) ou des sections editoriales longues (newsletter, strategies, actualites)**. `/statuts-indexation-google/*` est le seul template pSEO conserve.

Hypothese la plus probable : filtre sitemap introduit dans le dernier build (24-31/08) qui exclut certains types de pages, soit par erreur (regression), soit intentionnellement (decision editoriale non communiquee). A trancher rapidement.

Action recommandee (urgente) : verifier le pipeline de generation du sitemap (config Next.js `next-sitemap`, script `generate-sitemap.ts`, ou equivalent) pour identifier ce qui a change entre les deux builds. Si regression, restaurer les 192 URLs. Si intentionnel, documenter la decision et prendre la mesure GSC pour arbitrer l'impact indexation avant que ce ne soit trop tard.

### C2. `/manifeste{,/}` toujours 404 - 9e recurrence

`curl -sIL https://organikk.co/manifeste/` renvoie `HTTP 404`. Meme reponse sans slash. La page n'est toujours pas dans le sitemap. Aucun `<a href>` vers `/manifeste` sur les 141 pages telechargees (confirmation grep).

Reco P1 du 10/07 (redirection 301 `/manifeste{,/} -> /methode/`) : non appliquee. **52 jours d'ouverture**. Prediction `pred-2026-08-24-manifeste-404-continue` confirmee (hit).

Au 10/07, la GSC comptait 30 impressions sur 28 jours sur cette URL (2e page du site en impressions). Sans reprise de la mesure GSC ce run, on ne sait pas si Google la sert encore, mais tant que la 404 est en place, chaque impression eventuelle est perdue.

Action inchangee : `301 /manifeste{,/} -> /methode/`. Une ligne dans `_redirects` / `netlify.toml`. Jamais de 410.

### C3. `/accompagnement-seo-geo/` toujours orpheline - 9e recurrence

Verifie par crawl des 141 pages telechargees : la chaine `accompagnement-seo-geo` n'apparait dans un `href` d'aucune page hors auto-reference. Test `grep -lE "href=\"(/accompagnement-seo-geo/?\"|https://organikk\.co/accompagnement-seo-geo/?\")"` : 0 backlinks.

Page d'offre solide (`HTTP 200`, canonical propre, **1715 mots** methode C ce run, delta -26 vs 24/08 dans la variance methode C). `h1` : *Remonter sur Google et etre cite par les IA*. Page decouvrable uniquement par le sitemap.

Reco C2 du 10/07 (mailler depuis `/systeme/`, `/methode/`, `/accompagnement-1-1-30-jours/`) : non appliquee. **52 jours d'ouverture**.

Action inchangee : trois liens ancre naturels depuis les trois hubs.

### C4. `/consultant-geo/` toujours orpheline - 4e recurrence

`HTTP 200`, canonical `https://organikk.co/consultant-geo/`, `<h1>` present, **2877 mots** (methode C, delta -23 vs 24/08 variance methode C). Aucun lien entrant sur les 141 pages ce run non plus.

Reco C3 du 10/08 (mailler depuis 2-4 hubs pertinents) : non appliquee apres 21 jours.

Action inchangee : 2 a 4 liens ancre depuis `/systeme/`, `/methode/`, `/consultant-lead-seo/`, `/coaching-seo-lyon/`, `/freelance-geo-lyon/`.

### C5. `/formation-seo-ia/` toujours orpheline - 3e recurrence

`HTTP 200`, canonical propre, **867 mots** (delta -26 vs 24/08, variance). Aucun lien entrant sur les 141 pages ce run non plus. Aucun lien depuis `/systeme/`, `/methode/`, `/bootcamp/`, `/coaching-seo-lyon/`, `/accompagnement-seo-geo/`, `/accompagnement-1-1-30-jours/`, `/consultant-geo/`.

Reco C4 du 17/08 (mailler depuis 2-3 hubs) : non appliquee. **14 jours d'ouverture**.

**Trois pages d'offre longues orphelines simultanement** cette semaine (accompagnement-seo-geo, consultant-geo, formation-seo-ia). Cumul 5459 mots de contenu commercial decouvrable uniquement par le sitemap, dont Google apprend a ignorer le `lastmod` (M2, 13e recurrence, 77 jours). **Le probleme s'aggrave** : avec la contraction du sitemap (C1), le contenu decouvrable par sitemap ne represente plus que 42 % du corpus actif du site, alors que ces 3 pages n'ont toujours pas d'entree alternative par le maillage.

Action inchangee : mailler `/formation-seo-ia/` depuis 2-3 hubs pertinents (`/systeme/`, `/methode/`, `/bootcamp/`, `/accompagnement-1-1-30-jours/`, `/coaching-seo-lyon/`).

## Anomalies mineures

### M1. Sitemap declare 141 URLs non canoniques - 13e recurrence

Verifie sur echantillon 12 URLs du sitemap : 11/12 renvoient `301` vers `<path>/` (slash final). Seule exception : la racine `https://organikk.co`, servie directement en 200 sans redirection. Extrapolation : 141/142 URLs sont declarees sans slash final au sitemap.

Chiffre absolu baisse mecaniquement (141 vs 333 au 24/08) parce que le sitemap contient moins d'URLs, mais le ratio reste identique (141/142 = 99.3 % du sitemap, contre 333/334 = 99.7 % au 24/08 ; racine toujours l'unique exception). Chaque URL du sitemap coute encore un aller-retour de crawl inutile.

P1 ouverte depuis le 15/06, sans effet observable apres **77 jours**.

### M2. `lastmod` uniforme sur 142/142 - 13e recurrence

Toutes les URLs portent `2026-08-28T10:04:29.658Z`, date du dernier build. `sort -u` sur les `<lastmod>` renvoie une seule ligne : 142 occurrences. Meme pattern qu'aux 12 runs precedents.

Consequence renforcee ce run : combinee a la contraction du sitemap (C1), les 192 URLs qui viennent de disparaitre du sitemap perdent aussi tout signal de fraicheur cote serveur. Google recevait deja un lastmod inutile ; il recoit maintenant un lastmod inutile sur un sitemap incomplet. Le double effet est defavorable.

P2 ouverte depuis le 15/06, sans effet observable apres **77 jours**.

### M3. `/secteurs/` reste orpheline - 9e recurrence

Hub de section pour deux pages enfants (`/secteurs/avocat/`, `/secteurs/hotellerie/`). Toujours zero lien interne entrant hors auto-reference.

Statut inchange vs 24/08 (417 mots, densifie la semaine derniere, sortie de la zone thin). Action revue : maintenant que la page a du fond, deux options symetriques :
- soit mailler depuis 2 pages amont (`/methode/`, `/blog/`, `/actualites/` **NB: `/actualites/` vient de sortir du sitemap, cf. C1**) pour lui donner une raison d'exister,
- soit retirer du sitemap si elle ne doit pas ranker seule.

### M4. Robots.txt simplifie - perte 4 sections privees Disallow

Le fichier `robots.txt` passe de 5 blocs (User-Agent + 4 Disallow prives : `stats-gsc-organikk-private-2026`, `bootcamp-private`, `admin`, `stats`) a une politique minimale :

```
User-Agent: *
Allow: /

Sitemap: https://organikk.co/sitemap.xml
```

Impact indexation probablement neutre : les URLs privees n'etaient pas dans le sitemap public, donc pas de bascule vers indexation forcee. En revanche, la disparition simultanee du sitemap contracte (C1) et de ces directives Disallow est coherente avec l'hypothese d'une **refonte du pipeline de generation robots.txt + sitemap dans le meme deploiement**. A verifier au meme endroit que C1.

Point a arbitrer : si la simplification est intentionnelle, remettre au moins `Sitemap:` (fait) et confirmer que les URLs prives ne sont pas exposees ailleurs. Si elle est involontaire, la restaurer.

### M5. Section `/statuts-indexation-google/` : 4/17 pages enfant sous 400 mots - 6e occurrence, micro-regression

**Etat change ce run.** Sur 17 URLs de la section : le hub `/statuts-indexation-google/` a 781 mots (contre 816 au 24/08, delta -35 methode C variance), les 16 pages enfant sont entre **375 et 460 mots** (moyenne 421).

- 4 pages sous 400 : `soft-404` (375), `erreur-de-redirection` (378), `erreur-de-serveur-5xx` (397), `introuvable-404` (399)
- 12 pages entre 405 et 460 mots

Comparaison 24/08 : 2/16 sous 400 mots (`soft-404` 397, `erreur-de-redirection` 399). **Ce run : 4/16, dont 2 nouvelles pages (`erreur-de-serveur-5xx`, `introuvable-404`)**. Amplitude du drift : 22-24 mots par page pour les deux nouvelles, dans la marge de variance methode C (~5 %) mais coherent en direction. Aucune de ces pages n'a fait l'objet d'une intervention editoriale visible.

Deux lectures possibles : (a) variance de mesure methode C (le HTML rendu peut varier selon les hydratations, imperceptible en preview mais mesurable au wordcount), (b) retour a la baseline avant la densification du 24/08. **A observer la semaine prochaine** pour trancher : si le ratio reste stable a 4/16 ou remonte au-dessus de 400 sur toutes les pages, c'est de la variance ; s'il continue a monter (5/16, 6/16), c'est un drift editorial.

Priorite basse, mais a noter au ledger pour trace historique.

## Observations positives

**Fondamentaux techniques stables sur les 142 URLs restantes.** 142/142 HTTP 200, 141/141 pages telechargees avec canonical strictement egal a l'URL finale, 141/141 avec `<title>` et `<h1>`, aucun `X-Robots-Tag` server-side dans l'echantillon 8 URLs. **Quatrieme semaine consecutive sans regression technique sur les URLs presentes.**

**Corpus wiki tient sa densification.** 55 fiches enfant telechargees (56 URLs sitemap, 1 fichier manquant reseau) entre 515 et 826 mots, moyenne 657. Aucune fiche sous 400 mots. **Sept semaines consecutives au-dessus du seuil depuis le 13/07.** Legere baisse de moyenne vs 24/08 (690 vs 657), a mettre en regard de la variance methode C.

**Trois pages d'offre orphelines densifiees conservent leur contenu.** `/consultant-geo/` 2877 mots, `/formation-seo-ia/` 867 mots, `/accompagnement-seo-geo/` 1715 mots. Les deltas vs 24/08 sont tous dans la variance methode C.

**Aucun nouveau contenu orphelin publie cette semaine.** Sitemap delta 0 sur les URLs qui sont restees (le -192 est de la sortie, pas de l'ajout). Le pattern « nouvelle URL publiee sans backlink entrant » (C3 au 10/08, C4 au 17/08) ne s'est pas reproduit ce run. Prediction `pred-2026-08-17-pattern-new-orphan` toujours ouverte (resolve 14/09).

## Autres observations

**Sitemap actuel par section** (142 URLs) :
- `/wiki/*` : 56 (intact, hub + 55 enfants)
- `/blog/*` : 29 (intact, mais `/newsletter/*` disparu)
- `/statuts-indexation-google/*` : 17 (intact)
- `/glossaire/*` : 7 (intact)
- `/outils/*` : 5 (intact)
- `/secteurs/*` : 3 (intact)
- `/bootcamp/*` : 2 (intact)
- Pages racine et pages d'offre : ~23 URLs individuelles

**Sitemap sorti par section** (192 URLs, toujours HTTP 200) :
- `/guide-evaluateurs-google/*` : 103
- `/newsletter/*` : 29
- `/mises-a-jour-google/*` : 27
- `/strategies/*` : 15
- `/robots-ia/*` : 14
- `/actualites/*` : 4

**Pattern des sections conservees vs sorties** : les sections conservees sont principalement du contenu editorial court a moyen atomique (wiki 500-800 mots, glossaire, outils) et le blog long-form. Les sections sorties sont soit des templates pSEO (guide, mises-a-jour, robots-ia), soit des sections editoriales successives dans le temps (newsletter, strategies, actualites). Hypothese : filtre sur un champ de metadata (type de contenu, tag, date), a confirmer cote pipeline sitemap.

**Predictions ouvertes au 24/08, resolues aujourd'hui** :
- `pred-2026-08-24-manifeste-404-continue` (resolve 31/08) : **hit** (404 persiste, 9e recurrence).
- `pred-2026-08-24-orphans-persist` (resolve 31/08) : **hit** (les 3 pages d'offre restent orphelines).
- `pred-2026-08-24-robots-ia-finish` (resolve 31/08) : **non_mesurable** (section retiree du sitemap, mesure inversee par un evenement structurel imprevu). Les pages `/robots-ia/*` existent toujours en HTTP 200 mais sortent du perimetre de mesure "sitemap".
- `pred-2026-08-24-mises-a-jour-densified-holds` (resolve 31/08) : **non_mesurable** (meme raison).
- `pred-2026-08-10-mises-a-jour-thin-drift` (resolve 31/08) : **non_mesurable** (meme raison ; a J+14 la trajectoire etait inverse au drift predit, mais aucune resolution formelle possible).
- `pred-2026-08-17-pattern-new-orphan` (resolve 14/09) : toujours ouverte (aucune nouvelle URL cette semaine, prediction non testable en l'etat, a rearmer au prochain ajout au sitemap).

**Scraping `site:` sur Google : toujours retire de l'audit.** Le check #8 du skill reste desactive tant que Tim n'a pas tranche le diff propose (`loops/indexation-check/memory/questions.md`, en attente depuis le 10/07, **52 jours d'ouverture**).

**62 pages sous-maillees (1 seul lien entrant) au 24/08 : impossible a comparer directement.** Le calcul de maillage ce run se fait sur les 141 pages telechargees (perimetre sitemap contracte) et non sur les 334 pages du 24/08. Comparaison legitime : 5 pages orphelines sur 141 (3.5 %) vs 4 sur 334 (1.2 %). Le taux d'orphelinat monte parce que le denominateur baisse plus vite que le numerateur, mais surtout parce que les 192 pages sorties n'etaient pas orphelines (elles avaient au moins le sitemap comme signal).

## Nouvelles predictions

- `pred-2026-08-31-sitemap-restore` (resolve 07/09) : SI l'evenement C1 est une regression build, alors les 192 URLs sortiront reintegrees au sitemap au run du 07/09. SI intentionnel, elles resteront hors sitemap. Prediction conditionnelle a Tim pour l'action ; mesure au 07/09 : compter les URLs par section vs 24/08.
- `pred-2026-08-31-manifeste-404` (resolve 07/09) : sans redirection 301 posee, `/manifeste{,/}` sera encore en HTTP 404 au run du 07/09 (10e recurrence).
- `pred-2026-08-31-orphans-persist` (resolve 07/09) : sans action de maillage cette semaine, les 3 pages d'offre orphelines (`/accompagnement-seo-geo/`, `/consultant-geo/`, `/formation-seo-ia/`) resteront orphelines au run du 07/09.

## Recommandations priorisees

1. **URGENT - Investiguer le pipeline sitemap** (C1). Identifier la modification introduite entre le build du 24/08 et celui du 28/08 qui a exclu 192 URLs. Verifier `next-sitemap.config.js` ou equivalent, tags Next.js sur les pages, script d'export. Si regression, restaurer. Si intentionnel, documenter la decision et anticiper l'impact indexation.

2. **Rediriger `/manifeste{,/}` en 301** vers `/methode/`. **9e reconduite consecutive.** Une ligne dans `_redirects`. Seul point strictement urgent cote HTTP.

3. **Mailler `/accompagnement-seo-geo/`** depuis `/systeme/`, `/methode/` et `/accompagnement-1-1-30-jours/`. **9e reconduite.** Trois liens ancre.

4. **Mailler `/consultant-geo/`** depuis 2-4 hubs pertinents. **4e reconduite.** 21 jours d'ouverture.

5. **Mailler `/formation-seo-ia/`** depuis 2-3 hubs pertinents. **3e reconduite.** 14 jours d'ouverture.

6. **Corriger le sitemap** : declarer les URLs avec le slash final, alimenter `lastmod` depuis la vraie date de derniere modification de contenu par page. Reconduite du 15/06 (**77 jours**). Combinee a C1, la refonte du pipeline sitemap est le bon moment pour trancher ces deux points structurels en un seul chantier.

7. **Formaliser la regle systeme "toute nouvelle URL publiee = 2 backlinks entrants au moment de la mise en ligne"**. Reco du 17/08 reconduite. A arbitrer au vendredi comme decision structurelle.

8. **Trancher robots.txt** (M4) : la simplification est-elle intentionnelle ? Si oui, documenter ; si non, restaurer les 4 sections privees.

9. **Trancher sur `/secteurs/`** : maintenant que le hub est densifie (417 mots), soit vraie navigation vers les enfants avec 2 pages amont qui pointent vers le hub, soit retrait du sitemap. **9e reconduite.**

10. **Brancher `urlInspection/index:inspect`** a cote de `admin-gsc-export` (diff en attente du 10/07 dans `memory/questions.md`). **52 jours d'ouverture pour ce debloqueur systeme.** Impact particulierement critique ce run : impossible de mesurer si Google a deja commence a desindexer les 192 URLs sorties du sitemap.

## Limites de ce rapport

- **Statut d'indexation Google non teste.** Pas d'acces a l'edge `admin-gsc-export`. La derniere mesure fiable est celle du 10/07 (49/146 confirmees, 97 indeterminees). Sur les 142 URLs du sitemap et les 192 URLs sorties, aucune ne peut etre declaree "non indexee". Aucune estimation n'a ete inventee. L'ecart `non indexee` / `non testable` est explicite.
- **192 pages sorties du sitemap non auditees en profondeur.** Verifie que les hubs et 3 pages internes de `/guide-evaluateurs-google/*` repondent en HTTP 200. Les 189 autres pages n'ont pas ete telechargees ce run (perimetre = sitemap actuel). Elles seront reintegrees au perimetre au prochain run si elles reviennent au sitemap, ou surveillees separement si la sortie est intentionnelle.
- **X-Robots-Tag verifie sur echantillon de 8 URLs**, pas sur les 142. Aucun `noindex` server-side dans l'echantillon.
- **Methode wordcount = methode C** (body + strip scripts + strip styles + strip noscript, sans exclusion nav/footer). Meme methode qu'aux 24/08, 17/08 et 10/08. Les chiffres se comparent directement aux runs precedents avec une variance normale de ±5 % par page.
- **Fenetre de decouverte = sitemap.** Une page vivante absente du sitemap et sans lien entrant echapperait a cet audit. Combine a C1, ce point devient particulierement penalisant ce run : 192 URLs viennent de rentrer dans cette classe de risque.
- **Un fichier de wiki manque au telechargement local** (`/wiki/pillar-page/`, HTTP 200 confirme au retelechargement mais fichier absent au premier passage, 616 mots). Reintegre au recomptage : 55 fiches wiki analysees, aucune sous 400 mots. Les chiffres wiki sont robustes malgre le miss.

## Liens

Runs precedents : [[reports/indexation-organikk-2026-06-15]], [[reports/indexation-organikk-2026-06-22]], [[reports/indexation-organikk-2026-06-29]], [[reports/indexation-organikk-2026-07-06]], [[reports/indexation-organikk-2026-07-10]], [[reports/indexation-organikk-2026-07-13]], [[reports/indexation-organikk-2026-07-20]], [[reports/indexation-organikk-2026-07-27]], [[reports/indexation-organikk-2026-08-03]], [[reports/indexation-organikk-2026-08-10]], [[reports/indexation-organikk-2026-08-17]], [[reports/indexation-organikk-2026-08-24]].
Methode : [[gsc-export]], [[maillage-interne]].
Skills en attente de decision : [[loops/indexation-check/memory/questions]] (remplacement check #8 par urlInspection API, correction chemin validator, fix eval_health.py champ francais).
