---
type: audit
title: Indexation Organikk — audit hebdomadaire 2026-09-14
created: 2026-09-14
updated: 2026-09-14
tags: [indexation, sitemap, audit, organikk, hebdo]
status: stable
confidence: high
sources: 3
---

# Audit indexation Organikk — 2026-09-14

**Périmètre.** organikk.co, 88 URLs listées dans `sitemap.xml` (delta -3 vs 07/09 : 91 → 88). Lecture seule sur le web public. Aucun forçage d'indexation.

**Sources de vérité utilisées.**
- Statut HTTP `curl` (première réponse + redirection résolue).
- Présence dans `sitemap.xml` + `lastmod`.
- `robots.txt`.
- Parsing HTML servi : `<title>`, `<h1>`, `<link rel=canonical>`, `<meta name=robots>`, graphe interne (hrefs internes).

**Non testable.** Statut d'indexation Google réel. Pas d'accès à l'edge `admin-gsc-export` (`urlInspection` / `searchAnalytics`) dans cet environnement. Diff proposé le 10/07 pour remplacer le check #8 mort par un appel à l'API URL Inspection : **66 jours d'ouverture**. Voir `loops/indexation-check/memory/questions.md`.

## 1. Synthèse

Semaine marquée par **un refactoring de la navigation globale** et **l'apparition d'une nouvelle section `/skills/`**. La contraction éditoriale continue (91 → 88 URLs sitemap) et les récurrences chroniques ne bougent pas.

- **Nouveauté nav.** La navigation globale a été refactorée : seules 3 URLs sont désormais présentes sur les 88/88 pages (`/`, `/mentions-legales`, `/bootcamp-candidature`). Au 07/09, `/tarifs` était linkée depuis 91/91 pages via la nav ; ce run, elle n'a plus qu'**1 backlink interne** (depuis `/coaching-seo-lyon/`). C'est un changement structurel majeur : l'ancienne nav portait l'essentiel du maillage, la nouvelle est presque nue.
- **Nouvelle section `/skills/`** dans le sitemap, HTTP 200 direct, seule URL du sitemap qui porte le slash canonique (les 87 autres restent sans slash côté `<loc>` et redirigent 301 vers version avec slash — 16e récurrence du `sitemap_canonical_mismatch`). Contenu servi de 66 mots seulement : c'est une page thin dans son état servi.
- `/manifeste` reste 404 pour la **13e semaine consécutive** (96 jours depuis la reco P1 du 10/07). Les 3 pages d'offre commerciales (`/accompagnement-seo-geo/`, `/consultant-geo/`, `/formation-seo-ia/`) restent orphelines à 0 backlink interne : recommandations non appliquées depuis 96, 35 et 28 jours. `/tarifs` reste absente du sitemap (14 jours depuis la reco C1) et vient de perdre son maillage nav.
- **Progrès net sur le nettoyage wiki.** Sur 27 slugs `/wiki/*` linkés depuis les fiches mais absents du sitemap (ex. `bert`, `cocon-semantique`, `eeat`, `similarite-cosinus`, `titans-architecture`, `quality-rater-guidelines`, `rankbrain`), **27/27 redirigent proprement en 301 → `/wiki/`**. En parallèle, les **22 slugs wiki testés au 07/09 en 404 nu restent 22/22 en 404 nu ce run** (`e-e-a-t`, `needs-met`, `quality-rating`, `budget-crawl`, `canonical`, `helpful-content`, `llms-txt`, `schema-org`, `helpful-content-update`, `sge`, `core-update`, `mum`, `passage-index`, `answer-engine`, `crawler-ia`, `embeddings`, `hallucination`, `rag`, `semantic-triple`, `entity-first`, `knowledge-graph`, `attribution-metric`). L'asymétrie signalée au 07/09 se confirme : deux mécaniques différentes selon la couche de suppression.
- `lastmod_uniforme` toujours en 16e récurrence : 88/88 URLs partagent `2026-09-11T15:00:32.306Z`.

**Chiffres du run.** 88/88 HTTP 200 après redirection (86/88 via 301 slash-canonical, 2/88 en 200 direct). 88/88 avec `<title>`, `<h1>` et `<link rel=canonical>` auto-référent. 0 `noindex` sur méta robots. `robots.txt` inchangé (politique minimale `User-Agent:* / Allow:/ + Sitemap`).

## 2. Anomalies critiques

### C1. `/manifeste` 404 — 13e récurrence (96 jours)

- `curl -sI https://organikk.co/manifeste` → HTTP 404.
- `curl -sI https://organikk.co/manifeste/` → HTTP 404.
- Absente du sitemap.
- 0 backlink interne sur les 88 pages téléchargées.
- Reco P1 du 10/07 (301 vers `/systeme/` ou refonte) non appliquée depuis 96 jours.
- Aveuglement critique : sans accès `urlInspection`, impossible de savoir si Google la sert encore. Au 10/07, `/manifeste` recevait encore 30 impressions sur 28 jours sur « manifeste seo ».

### C2. Refactoring nav : `/tarifs` perd son maillage — nouveau

- HTTP 200 (via 301 slash-canonical).
- **Absente du sitemap** (3e récurrence, 14 jours depuis C1 du 05/09).
- **1 seul backlink interne** ce run (`/coaching-seo-lyon/`), contre 91/91 backlinks nav au 07/09.
- La nav globale a été réduite à 3 URLs (`/`, `/mentions-legales`, `/bootcamp-candidature`). Impact mécanique : `/tarifs` passe de « URL la plus liée après l'accueil » à « URL quasi-orpheline hors sitemap ».
- Combinaison la plus coûteuse : hors sitemap + hors nav globale = double invisibilité aux crawlers.

### C3. `/accompagnement-seo-geo/` orpheline — 12e récurrence (96 jours)

- HTTP 200 (via 301 slash-canonical).
- Présente dans le sitemap.
- 0 backlink interne sur les 88 pages téléchargées (grep `href="/accompagnement-seo-geo"`).
- Page d'offre commerciale. Reco C2 du 10/07 non appliquée depuis 96 jours.

### C4. `/consultant-geo/` orpheline — 7e récurrence (35 jours)

- HTTP 200 (via 301 slash-canonical).
- Présente dans le sitemap.
- 0 backlink interne sur les 88 pages téléchargées.
- Reco C3 du 10/08 non appliquée depuis 35 jours.

### C5. `/formation-seo-ia/` orpheline — 6e récurrence (28 jours)

- HTTP 200 (via 301 slash-canonical).
- Présente dans le sitemap.
- 0 backlink interne sur les 88 pages téléchargées.
- Reco C4 du 17/08 non appliquée depuis 28 jours.

### C6. Nouvelles orphelines : `/consultant-lead-seo/` et `/plan-du-site/`

- `/consultant-lead-seo/` HTTP 200, présente dans le sitemap, **0 backlink interne** sur 88 pages. C'est la première fois qu'elle apparaît en orpheline dans le run (0 impressions mesurables sans GSC).
- `/plan-du-site/` HTTP 200, présente dans le sitemap depuis ce run (nouveau), **0 backlink interne**. Une page plan-du-site sans backlink entrant est un contre-emploi : sa fonction est d'être linkée depuis le footer ou l'accueil.
- Effet direct du refactoring nav C2 : la nav minimaliste retire ces pages du graphe interne.

### C7. `sitemap_canonical_mismatch` — 16e récurrence (96 jours)

- 87/88 URLs sont **sans** slash final dans `<loc>` (ex. `<loc>https://organikk.co/wiki/agent-seo</loc>`).
- 86/88 redirigent 301 vers leur version avec slash ; 2/88 sont servies en 200 direct (`/` et `/skills/`).
- Le `<link rel="canonical">` du HTML pointe systématiquement la version avec slash.
- Chaque crawl Googlebot dépense 2 requêtes HTTP là où 1 suffirait sur 86/88 URLs.
- Reco P1 du 15/06 (aligner `<loc>` sur la forme avec slash) non appliquée depuis 96 jours.
- **Note.** `/skills/` est la première URL du sitemap à porter le slash canonique dès `<loc>`. Le canonical du build a donc changé sur cette page précise mais pas sur le reste.

### C8. `lastmod_uniforme` — 16e récurrence (96 jours)

- Les 88 URLs du sitemap partagent le même `<lastmod>2026-09-11T15:00:32.306Z</lastmod>` (mise à jour globale du 11/09 sur toutes les URLs, indépendamment de leur date d'édition réelle).
- Le signal de fraîcheur relatif entre URLs reste perdu.
- Reco P2 du 15/06 (émettre un `lastmod` par URL depuis la source éditoriale) non appliquée depuis 96 jours.

## 3. Anomalies mineures

### M1. `/skills/` thin en HTML servi

- Nouvelle URL du sitemap, HTTP 200 direct, canonical auto-référent, title et h1 propres.
- **66 mots dans le HTML servi** (méthode article body). C'est la page la plus fine du site en HTML statique. Deux hypothèses concurrentes : (a) contenu rendu côté client par Next.js (React hydration), non visible aux crawlers légers ; (b) landing page volontairement légère avec liste externe. À trancher par test headless (Chrome `--dump-dom`) sur le prochain run.

### M2. Nettoyage wiki confirmé asymétrique (M1 09/07 reconfirmé)

- **22/22 slugs wiki testés au 07/09 en 404 nu restent 22/22 en 404 nu ce run** (7 jours plus tard) : `e-e-a-t`, `needs-met`, `quality-rating`, `budget-crawl`, `canonical`, `helpful-content`, `llms-txt`, `schema-org`, `helpful-content-update`, `sge`, `core-update`, `mum`, `passage-index`, `answer-engine`, `crawler-ia`, `embeddings`, `hallucination`, `rag`, `semantic-triple`, `entity-first`, `knowledge-graph`, `attribution-metric`.
- **27 autres slugs `/wiki/*` linkés depuis les fiches survivantes redirigent proprement 301 → `/wiki/`** : `ai-overviews`, `audit-seo`, `bert`, `bm25`, `chatgpt-search`, `clustering-semantique`, `cocon-semantique`, `core-web-vitals`, `dpr-dense-passage-retrieval`, `eeat`, `featured-snippet`, `google-ai-mode`, `intention-de-recherche`, `llm-large-language-model`, `maillage-interne`, `miras-framework`, `muvera`, `perplexity-ai`, `pillar-page`, `programmatic-seo`, `quality-rater-guidelines`, `rag-retrieval-augmented-generation`, `rankbrain`, `similarite-cosinus`, `titans-architecture`, `topical-authority`, `weight-decay`.
- Deux mécaniques de nettoyage cohabitent : celle qui produit des 301 propres (probablement `_redirects` Netlify tenu à jour manuellement) et celle qui laisse 404 nu (probablement suppression brute du fichier source). L'asymétrie signalée au 07/09 est confirmée sur 7 jours. Note : `eeat` (301) coexiste avec `e-e-a-t` (404 nu) : la version hyphénée n'a pas été redirigée.

### M3. Aveuglement `urlInspection` — 66 jours

- Le run continue de fonctionner sur les couches A (HTTP) et C (maillage/contenu) mais reste aveugle sur la couche B (statut d'indexation Google réel). Cela fait 66 jours que le diff est en attente dans `memory/questions.md`.
- Impact particulièrement lourd ce run : impossible de savoir si les 22 slugs wiki 404 nu (M2) sont encore servis en SERP, ni si `/tarifs` récupère du trafic malgré la double invisibilité (C2).

### M4. Trois pages ultra-fines dans le sitemap

- `/skills/` 66 mots, `/contact/` 233 mots, `/resultats/` 288 mots, `/glossaire/serp-ranking/` 335 mots, `/glossaire/ia-llm/` 390 mots. 5 pages sous 400 mots méthode `<body>` servi.
- `/contact/` et `/resultats/` sont fonctionnelles par nature (pas de contenu long attendu). `/skills/` et les 2 fiches glossaire méritent inspection : si le contenu est réellement fin (pas d'hydratation JS), c'est un signal de faible utilité côté crawler.

### M5. Divergence `title` vs `h1` sur 82 pages

- Méthode stricte (comparaison directe : title débarrassé du suffixe `· Organikk` ou similaire vs h1) : **82/88 pages divergent**. Seules 6 pages ont un title et un h1 identiques.
- Le decoupling est vraisemblablement éditorial (title = promesse fonctionnelle avec suffixe de marque, h1 = accroche narrative). Ce n'est pas un bug par défaut mais un pattern à trancher en revue hebdo.
- Le run du 07/09 comptait 24 divergents avec une méthode moins agressive. À réaligner en une méthode unique pour comparer trajectoire.

## 4. Positifs

- **Fondamentaux techniques stables au meilleur niveau.** 88/88 HTTP 200 (résolus), `title`, `h1`, `canonical` auto-référent, 0 `noindex`. **7e semaine consécutive sans régression** sur les URLs présentes.
- **Progrès concret sur le nettoyage wiki.** 27/27 slugs `/wiki/*` linkés depuis les fiches survivantes mais absents du sitemap redirigent proprement en 301 → `/wiki/`. La mécanique de redirect fonctionne bien sur cette couche et ferme le risque de dead-end via le graphe interne.
- **Pages `/systeme-seo-ia/` et similaires servies.** Test spot : `/systeme-seo-ia/` (linkée depuis `/methode/`) répond 200 malgré l'absence du sitemap. Le site continue de servir des landing pages non déclarées.
- **`/secteurs` proprement redirigée.** `/secteurs` redirige désormais 301 → `/systeme/`. Fin de la double-vie 200-hors-sitemap sur cette URL.

## 5. Recommandations priorisées

### Priorité 1 — Fermer les récurrences chroniques

- **P1a.** Trancher `/manifeste` : 301 vers `/systeme/` (ou refonte). **13e semaine sans action, blocage d'audit permanent.**
- **P1b.** Réparer `sitemap_canonical_mismatch` : émettre les 87 `<loc>` restantes avec le slash final dans le build, comme `/skills/` déjà l'est. Une ligne de config. **96 jours sans action.**
- **P1c.** Réparer `lastmod_uniforme` : émettre le `lastmod` réel par page depuis la source éditoriale. **96 jours sans action.**

### Priorité 2 — Restaurer le maillage sur les pages commerciales

- **P2a.** Décision explicite sur la nouvelle nav : est-ce que la réduction à 3 URLs (`/`, `/mentions-legales`, `/bootcamp-candidature`) est intentionnelle ? Si oui, `/tarifs`, `/systeme`, `/methode`, `/blog`, `/wiki` ne bénéficient plus du signal nav sur 88 pages et doivent être maillées autrement.
- **P2b.** Ajouter `<loc>https://organikk.co/tarifs</loc>` au sitemap. La page perd son maillage nav (C2) : sans entrée sitemap, elle passe en double-invisibilité. **14 jours sans action.**
- **P2c.** Injecter 3 à 5 backlinks depuis des pages fortes vers chacune de :
  - `/accompagnement-seo-geo/` (96 jours orpheline)
  - `/consultant-geo/` (35 jours)
  - `/formation-seo-ia/` (28 jours)
  - `/consultant-lead-seo/` (nouveau ce run)
  - `/plan-du-site/` (nouveau ce run — a besoin d'un lien depuis le footer minimum).
  Candidates fortes : blog posts les plus liés (`/blog/process-seo-b2b-2026/` 21 backlinks, `/blog/information-gain-geo/` 22, `/blog/9-skills-seo-claude/` 15, `/blog/wiki-ia-obsidian-claude/` 11).

### Priorité 3 — Compléter le nettoyage wiki (M2)

- **P3a.** Sur les 22 slugs wiki 404 nu, poser une 301 vers le concept survivant le plus proche (ex. `e-e-a-t` → `grounding-score`, `sge` → `agentic-search`, `helpful-content` → `information-gain`, `mum` → `agentic-search`, `bert` → `passage-ranking`, `rag` → `information-gain`, `schema-org` → `passage-ranking`, `rankbrain` → `passage-ranking`, `answer-engine` → `answer-first-pattern`, `crawler-ia` → `agentic-search`, `passage-index` → `passage-ranking`, `hallucination` → `confidence-score`, `entity-first` → `dataset-proprietaire`, `semantic-triple` → `dataset-proprietaire`, `attribution-metric` → `confidence-score`, `knowledge-graph` → `dataset-proprietaire`, `budget-crawl` → `/wiki/`, `canonical` → `/wiki/`, `llms-txt` → `/wiki/`, `needs-met` → `fully-meets`, `quality-rating` → `fully-meets`, `helpful-content-update` → `information-gain`).
- **P3b.** Aligner le pipeline de suppression pour qu'il émette systématiquement une 301 par slug supprimé (comme sur les 27 déjà propres et les 192 URLs du grand nettoyage du 07/09).

### Priorité 4 — Décision `/skills/` (M1)

- **P4.** Vérifier via test headless si `/skills/` sert du contenu client-side non capturé par curl. Si oui, décider si on l'expose côté SSR pour donner du grain aux crawlers légers.

### Priorité 5 — Débloquer la mesure GSC (M3)

- **P5.** Statuer sur le diff `urlInspection` proposé le 10/07 dans `memory/questions.md`. Alternative : autoriser le brain à appeler directement l'edge `admin-gsc-export` depuis cet environnement (secret + URL). Sans cela, on continue à naviguer à vue sur la couche B après **66 jours d'ouverture**.

## 6. Trajectoire sitemap (98 jours)

169 → 136 → 143 → 143 → 146 → 146 → 330 → 330 → 332 → 333 → 334 → 334 → 142 → 91 → 91 → **88**.

- 15/06 → 27/06 : léger réajustement.
- 06/07 → 27/07 : passage au périmètre site entier + scale-up massif +184 URLs le 20/07.
- 27/07 → 24/08 : palier stable autour de 332-334.
- 31/08 : contraction -192 (sitemap tombe à 142).
- 05/09 → 07/09 : palier à 91.
- 07/09 → 14/09 : **-3 URLs (91 → 88)**. Delta net : ajout de `/skills/` et retrait de `/secteurs`, `/outils/analyse-geo`, `/systeme-seo-ia` (URLs à retracer précisément au prochain diff sitemap versionné).

## 7. Predictions posées ce run

- `pred-2026-09-14-manifeste-404` — Sans redirection 301 posée, `/manifeste{,/}` sera encore en HTTP 404 au run du 2026-09-21 (14e récurrence). Resolve_by 2026-09-21.
- `pred-2026-09-14-orphans-persist` — Sans action de maillage cette semaine, les 3 pages d'offre orphelines historiques (`/accompagnement-seo-geo/`, `/consultant-geo/`, `/formation-seo-ia/`) resteront à 0 lien interne entrant sur les 88 pages du sitemap actif au run du 2026-09-21. Resolve_by 2026-09-21.
- `pred-2026-09-14-canonical-mismatch-fix` — Sans intervention sur le build, `sitemap_canonical_mismatch` sera dans sa 17e récurrence au run du 2026-09-21 (au moins 85/88 URLs sans slash). Resolve_by 2026-09-21.
- `pred-2026-09-14-wiki-404-nu` — Sur les 22 slugs wiki testés en 404 nu ce run, au moins 20 seront encore en 404 nu au run du 2026-09-21. Resolve_by 2026-09-21.
- `pred-2026-09-14-tarifs-sitemap` — `/tarifs` restera absente du sitemap au run du 2026-09-21 (4e récurrence). Resolve_by 2026-09-21.
- `pred-2026-09-14-nav-refactor-persist` — La nav globale minimaliste (3 URLs sur 88/88) restera en place au run du 2026-09-21 sauf décision explicite. Resolve_by 2026-09-21.

## 8. Predictions résolues ce run

- `pred-2026-09-07-manifeste-404` : **hit** — 13e récurrence, 96 jours sans action.
- `pred-2026-09-07-orphans-persist` : **hit** — 3 pages toujours à 0 backlink (96, 35 et 28 jours d'inaction).
- `pred-2026-09-07-canonical-mismatch-fix` : **hit** — 16e récurrence, 87/88 URLs concernées (progression : `/skills/` seul avec slash dans `<loc>`).
- `pred-2026-09-07-wiki-404-nu` : **hit fort** — 22/22 slugs testés restent 404 nu (prédiction disait au moins 18/22).
- `pred-2026-09-07-tarifs-sitemap` : **miss** — `/tarifs` toujours absente du sitemap, correction non appliquée.
