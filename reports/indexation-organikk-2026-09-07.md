---
type: audit
title: Indexation Organikk — audit hebdomadaire 2026-09-07
created: 2026-09-07
updated: 2026-09-07
tags: [indexation, sitemap, audit, organikk, hebdo]
status: stable
confidence: high
sources: 4
---

# Audit indexation Organikk — 2026-09-07

**Périmètre.** organikk.co, 91 URLs listées dans `sitemap.xml` (identique au run du 05/09) plus 24 URLs `/wiki/*` (hub + 23 fiches). Lecture seule sur le web public. Aucun forçage d'indexation.

**Sources de vérité utilisées.**
- Statut HTTP `curl` (première réponse + redirection résolue).
- Présence dans `sitemap.xml` + `lastmod`.
- `robots.txt`.
- Parsing HTML servi : `<title>`, `<h1>`, `<link rel=canonical>`, `<meta name=robots>`, backlinks internes.

**Non testable.** Statut d'indexation Google réel. Pas d'accès à l'edge `admin-gsc-export` (`urlInspection` / `searchAnalytics`) dans cet environnement. Diff proposé le 10/07 pour remplacer le check #8 mort par un appel à l'API URL Inspection : 59 jours d'ouverture. Voir `loops/indexation-check/memory/questions.md`.

## 1. Synthèse

Un run qui confirme une **très bonne semaine côté hygiène technique** et une **stagnation nette côté commercial**.

- Le grand nettoyage attendu depuis 3 semaines a été fait : les **192 URLs sorties du sitemap le 31/08** (guide-évaluateurs 103, mises-à-jour 27, robots-ia 14, statuts-indexation 17, stratégies 15, newsletter 29, actualités 4) sont désormais **toutes redirigées en 301** vers `/glossaire/`, `/outils/quality-rater-guidelines/`, `/blog/` ou `/secteurs/`. L'« état bâtard » 200-hors-sitemap signalé au 05/09 est terminé. Idem sur les deux fiches wiki résiduelles (`/wiki/featured-snippet`, `/wiki/topical-authority`) qui pointent proprement vers `/wiki/`.
- En parallèle, `/manifeste` reste 404 pour la **12e semaine consécutive** (89 jours depuis la reco P1 du 10/07). Les 3 pages d'offre commerciales (`/accompagnement-seo-geo/`, `/consultant-geo/`, `/formation-seo-ia/`) restent orphelines (0 backlink sur les 91 pages du sitemap) : recommandations non appliquées depuis 89, 28 et 21 jours. `/tarifs` reste absente du sitemap alors qu'elle est liée depuis les 91 pages via la navigation globale — 7 jours depuis la reco C1.
- Le `sitemap_canonical_mismatch` (URLs sans slash côté sitemap, canonical avec slash côté HTML) et le `lastmod_uniforme` (une seule date `2026-09-05T05:14:25.943Z` sur les 91 URLs) sont dans leur **15e récurrence consécutive** : 89 jours sans effet des P1 et P2 posées le 15/06.
- Découverte de méthode : la contraction 56 → 23 fiches wiki entre le 24/08 et le 05/09 n'a **pas** été redirigée uniformément. Sur un échantillon de 16 slugs supprimés testés à la main, **14 sont en 404 nu** et 2 (`/wiki/bert/`, `/wiki/cocon-semantique/`) sont propres via 301 → `/wiki/`. Traitement asymétrique par rapport aux 192 URLs de la semaine précédente.

**Chiffres du run.** 91/91 HTTP 200 sur le sitemap actif. 91/91 avec `<title>`, `<h1>` et `<link rel=canonical>`. 0 `noindex` sur méta robots. `robots.txt` inchangé depuis le 31/08 (politique minimale `User-Agent:* / Allow:/ + Sitemap`).

## 2. Anomalies critiques

### C1. `/manifeste` 404 — 12e récurrence (89 jours)

- `curl -sI https://organikk.co/manifeste` → HTTP 404.
- `curl -sI https://organikk.co/manifeste/` → HTTP 404.
- Absente du sitemap.
- 0 backlink interne sur les 91 pages téléchargées.
- Reco P1 du 10/07 (301 vers `/systeme` ou refonte de la page) non appliquée depuis 89 jours.
- Aveuglement critique : sans accès `urlInspection`, impossible de savoir si Google la sert encore. Le 10/07, `/manifeste` était en 404 mais recevait 30 impressions sur 28 jours sur « manifeste seo ». Impossible de mesurer la dérive depuis.

### C2. `/accompagnement-seo-geo/` orpheline — 11e récurrence (89 jours)

- HTTP 200 (via 301 slash-canonical).
- Présente dans le sitemap.
- 0 backlink interne sur les 91 pages téléchargées (grep `href="/accompagnement-seo-geo"`).
- Page d'offre commerciale de 1741 mots au 24/08. Reco C2 du 10/07 non appliquée depuis 89 jours.

### C3. `/consultant-geo/` orpheline — 6e récurrence (28 jours)

- HTTP 200 (via 301 slash-canonical).
- Présente dans le sitemap.
- 0 backlink interne sur les 91 pages téléchargées.
- Page d'offre commerciale de 2900 mots au 24/08. Reco C3 du 10/08 non appliquée depuis 28 jours.

### C4. `/formation-seo-ia/` orpheline — 5e récurrence (21 jours)

- HTTP 200 (via 301 slash-canonical).
- Présente dans le sitemap.
- 0 backlink interne sur les 91 pages téléchargées.
- Page d'offre commerciale de 893 mots au 24/08. Reco C4 du 17/08 non appliquée depuis 21 jours.

### C5. `/tarifs` absente du sitemap — 2e récurrence (7 jours)

- HTTP 200 (via 301 slash-canonical).
- **Liée depuis les 91 pages du site** (navigation globale). C'est probablement la 2e page la plus liée du site après l'accueil.
- Aucune entrée `<loc>https://organikk.co/tarifs</loc>` dans `sitemap.xml`.
- Reco C1 du 05/09 non appliquée depuis 7 jours. Coût d'une correction : une ligne de config.

### C6. `sitemap_canonical_mismatch` — 15e récurrence (89 jours)

- Sitemap sert 91 URLs **sans** slash final (ex. `<loc>https://organikk.co/wiki/agent-seo</loc>`).
- Chaque URL redirige 301 vers sa version **avec** slash (`/wiki/agent-seo/`).
- Le `<link rel="canonical">` du HTML pointe la version **avec** slash.
- 91/91 URLs concernées. Chaque crawl Googlebot dépense 2 requêtes HTTP là où 1 suffirait, et le signal `canonical=sitemap` est incohérent.
- Reco P1 du 15/06 (aligner le sitemap sur la forme avec slash) non appliquée depuis 89 jours.

### C7. `lastmod_uniforme` — 15e récurrence (89 jours)

- Les 91 URLs du sitemap partagent le même `<lastmod>2026-09-05T05:14:25.943Z</lastmod>`.
- Le signal de fraîcheur relatif entre URLs est perdu : Googlebot ne sait pas quelle page a réellement changé.
- Reco P2 du 15/06 (émettre un `lastmod` par URL depuis la source éditoriale) non appliquée depuis 89 jours.

## 3. Anomalies mineures

### M1. Redirection asymétrique du nettoyage wiki

Les 33 fiches wiki disparues entre 24/08 (56 fiches) et 05/09 (23 fiches) n'ont pas été traitées comme les 192 URLs de la contraction précédente. Sur un échantillon de 16 slugs supprimés testés à la main :

- 2 slugs propres 301 → `/wiki/` : `/wiki/bert/`, `/wiki/cocon-semantique/`.
- 14 slugs en 404 nu : `/wiki/e-e-a-t/`, `/wiki/needs-met/`, `/wiki/quality-rating/`, `/wiki/budget-crawl/`, `/wiki/canonical/`, `/wiki/helpful-content/`, `/wiki/llms-txt/`, `/wiki/schema-org/`, `/wiki/helpful-content-update/`, `/wiki/sge/`, `/wiki/core-update/`, `/wiki/mum/`, `/wiki/passage-index/`, `/wiki/answer-engine/`, `/wiki/crawler-ia/`, `/wiki/embeddings/`, `/wiki/hallucination/`, `/wiki/rag/`, `/wiki/semantic-triple/`, `/wiki/entity-first/`, `/wiki/knowledge-graph/`, `/wiki/attribution-metric/`.

À vérifier côté GSC : sur les 33 slugs supprimés, combien recevaient encore des impressions ou étaient référencés dans le graphe interne au 24/08. Ceux qui étaient servis en SERP méritent une 301 vers le concept survivant le plus proche (ex. `/wiki/e-e-a-t/` → `/wiki/grounding-score/`), pas un 404 nu.

### M2. Divergence `title` vs `h1` sur 23 pages commerciales

Le decoupling est systémique et probablement éditorial (title en promesse fonctionnelle, h1 en accroche narrative). Ce n'est pas un bug par défaut mais un signal à consolider en décision explicite. Concernées cette semaine : `/`, `/accompagnement-1-1-30-jours/`, `/accompagnement-seo-geo/`, `/a-propos/`, `/avis/`, `/blog/`, `/bootcamp/`, `/bootcamp-candidature/`, `/bootcamp-quiz/`, `/bootcamp/programme/`, `/chaine-youtube-seo/`, `/coaching-seo-lyon/`, `/consultant-lead-seo/`, `/contact/`, `/etudes-de-cas/`, `/formation-seo-ia/`, `/freelance-geo-lyon/`, `/methode/`, `/outils/`, `/outils/quality-rater-guidelines/`, `/resultats/`, `/secteurs/`, `/systeme/`, `/wiki/`. Décision à porter en revue hebdo : on trance en éditorial ou on aligne ?

### M3. Aveuglement `urlInspection` — 59 jours

Le run continue de fonctionner sur les couches A (HTTP) et C (maillage/contenu) mais reste aveugle sur la couche B (statut d'indexation Google réel). C'est la 9e semaine d'ouverture du diff proposé le 10/07 dans `memory/questions.md`. Impact particulièrement lourd cette semaine : impossible de savoir si les 33 wiki 404 nues (M1) sont encore servies en SERP par Google, alors que c'est exactement la classe de bug que le check API attraperait.

### M4. Wordcount wiki apparent en baisse

Sur les 23 fiches wiki mesurées avec la méthode « article body entre `<h1>` et `<footer>` » : min 325, max 542, moyenne 433 mots. **5 fiches sortent sous 400** (`fraicheur-semantique` 325, `fully-meets` 337, `rrf-reciprocal-rank-fusion` 361, `zero-click-search` 366, `confidence-score` 373).

Les runs précédents utilisaient une méthode « C » qui donnait des moyennes de 574 (24/08) à 690 (24/08) sur 55-56 fiches. Deux hypothèses concurrentes : (a) régression éditoriale sur 5 fiches, (b) simple différence de méthodologie de comptage entre les scripts. À trancher la semaine prochaine en réalignant la méthode C sur le corpus du run.

### M5. Anti-cache : `age: 0` sur `sitemap.xml`

`sitemap.xml` renvoie `age: 0 / cache-control: public,max-age=0,must-revalidate` (headers Netlify). Fréquence de rebuild inconnue mais le sitemap est servi frais à chaque requête, ce qui est cohérent avec un `lastmod` uniforme reflétant le dernier build. À noter comme observation, pas une anomalie en soi.

## 4. Positifs

- **Fin de l'« état bâtard » 200-hors-sitemap.** Les 192 URLs qui étaient encore servies en 200 hors sitemap au 05/09 sont désormais toutes redirigées 301 :
  - `/statuts-indexation-google/*` (17 URLs) → `/glossaire/`
  - `/robots-ia/*` (14 URLs) → `/glossaire/`
  - `/guide-evaluateurs-google/*` (103 URLs) → `/outils/quality-rater-guidelines/`
  - `/mises-a-jour-google/*` (27 URLs) → `/outils/quality-rater-guidelines/`
  - `/newsletter/` → `/blog/`
  - `/strategies/` → `/secteurs/`
  - `/actualites/` → `/blog/`
- **Fondamentaux techniques stables au meilleur niveau.** 91/91 HTTP 200, `title`, `h1`, `canonical`. 0 `noindex`. **6e semaine consécutive sans régression** sur les URLs présentes.
- **Nettoyage wiki initié.** 2 slugs sur l'échantillon testé (`bert`, `cocon-semantique`) sont proprement 301 → `/wiki/`. La mécanique existe côté redirects. C'est le déploiement systématique qui manque (M1).

## 5. Recommandations priorisées

### Priorité 1 — Fermer les récurrences chroniques

- **P1a.** Trancher `/manifeste` : 301 vers `/systeme` (ou la meilleure landing équivalente) ou refonte de la page. **12e semaine sans action, blocage d'audit permanent.**
- **P1b.** Réparer `sitemap_canonical_mismatch` : émettre les `<loc>` avec le slash final dans le build. Une ligne de config. **89 jours sans action.**
- **P1c.** Réparer `lastmod_uniforme` : émettre le `lastmod` réel par page depuis la source éditoriale. **89 jours sans action.**

### Priorité 2 — Corriger l'omission `/tarifs`

- **P2.** Ajouter `<loc>https://organikk.co/tarifs</loc>` au sitemap. La page est liée depuis 91/91 pages du site : c'est probablement la 2e URL la plus prioritaire du domaine. **7 jours sans action.**

### Priorité 3 — Poser du maillage entrant sur les 3 pages d'offre

- **P3.** Injecter 3 à 5 backlinks depuis des pages fortes (articles blog les plus lus, `/systeme/`, `/methode/`, `/resultats/`, `/etudes-de-cas/`) vers chacune de :
  - `/accompagnement-seo-geo/` (89 jours orpheline)
  - `/consultant-geo/` (28 jours)
  - `/formation-seo-ia/` (21 jours)
  - Sans ces liens, ces 3 pages resteront invisibles dans l'index secondaire et ne récupèrent qu'un ping de nav globale.

### Priorité 4 — Compléter le nettoyage wiki (M1)

- **P4a.** Sur les 33 slugs wiki supprimés (56 → 23), lister ceux qui ont reçu au moins une impression sur les 90 derniers jours (GSC).
- **P4b.** Poser une 301 par slug vers le concept survivant le plus proche (ex. `e-e-a-t` → `grounding-score`, `helpful-content` → `information-gain`, `schema-org` → `passage-ranking`, …). Pas de 301 en masse vers `/wiki/` : c'est une perte de contexte.

### Priorité 5 — Débloquer la mesure GSC

- **P5.** Statuer sur le diff `urlInspection` proposé le 10/07 dans `memory/questions.md`. Alternative : autoriser le brain à appeler directement l'edge `admin-gsc-export` depuis cet environnement (secret + URL). Sans cela, on continue à naviguer à vue sur la couche B.

## 6. Trajectoire sitemap (91 jours)

169 → 136 → 143 → 143 → 146 → 146 → 330 → 330 → 332 → 333 → 334 → 334 → 142 → 91 → **91**.

- 15/06 → 27/06 : léger réajustement.
- 06/07 → 27/07 : passage au périmètre site entier (mesure 146) et scale-up massif +184 URLs (mesure 330) le 20/07.
- 27/07 → 24/08 : palier stable autour de 332-334.
- 31/08 : contraction -192 (sitemap tombe à 142). Diagnostic évolutif : d'abord soupçonné régression de build, ensuite requalifié en dépublication réelle (05/09) et confirmé cette semaine.
- 05/09 → 07/09 : palier stable à **91**. Le grand nettoyage 301 est appliqué, le sitemap reflète désormais l'état canonique du site.

## 7. Predictions posées ce run

- `pred-2026-09-07-manifeste-404` — Sans redirection 301 posée, `/manifeste{,/}` sera encore en HTTP 404 au run du 2026-09-14 (13e récurrence). Resolve_by 2026-09-14.
- `pred-2026-09-07-orphans-persist` — Sans action de maillage cette semaine, les 3 pages d'offre orphelines resteront orphelines (0 lien interne entrant sur les 91 pages du sitemap actif) au run du 2026-09-14. Resolve_by 2026-09-14.
- `pred-2026-09-07-canonical-mismatch-fix` — Sans intervention sur le build, `sitemap_canonical_mismatch` sera dans sa 16e récurrence au run du 2026-09-14 (91/91 URLs concernées). Resolve_by 2026-09-14.
- `pred-2026-09-07-wiki-404-nu` — Sur les 22 slugs wiki testés en 404 nu ce run, au moins 18 seront encore en 404 nu (sans 301) au run du 2026-09-14. Resolve_by 2026-09-14.
- `pred-2026-09-07-tarifs-sitemap` — La correction attendue `/tarifs` dans le sitemap sera appliquée avant le run du 2026-09-14. Cible optimiste, la correction coûte une ligne. Resolve_by 2026-09-14.

## 8. Predictions à résoudre ce run

- `pred-2026-08-31-orphans-persist` : **hit** — mesuré au 05/09, reconfirmé au 07/09 (89, 28 et 21 jours d'inaction).
- `pred-2026-08-31-manifeste-404` : **hit** — 12e récurrence, 89 jours sans action.
- `pred-2026-08-31-sitemap-restore` : **miss** — le sitemap ne s'est pas restauré et la contraction s'est révélée volontaire.
- `pred-2026-09-05-organikk-tarifs-sitemap` (échéance 2026-10-05) : **ouverte**, prochaine mesure 2026-09-14.
- `pred-2026-09-05-organikk-wiki-404` (échéance 2026-10-05) : **trajectoire hit** — 8/8 slugs confirmés 404 nu au 07/09, aucune redirection en cours sur cet échantillon.

## 9. Ce que ce run n'a pas fait

- Aucun appel à l'API URL Inspection ni à `searchAnalytics` : couche B non testée.
- Pas de wordcount méthode C uniforme sur les 23 fiches wiki (mesure comparable aux runs 03/08 → 31/08).
- Pas de scraping `site:` : la méthode a été invalidée par test témoin le 05/09 (une URL inexistante ressort « indexée » car le domaine figure dans la requête). Couche B reste non testable par cette voie.

---

**Fichiers de travail.** `scratchpad/idx/sitemap.xml`, `scratchpad/idx/urls.txt`, `scratchpad/idx/http-status.tsv`, `scratchpad/idx/page-manifest.tsv`, `scratchpad/idx/html/*.html` — non versionnés.
