---
type: audit
title: Indexation Organikk — audit hebdomadaire 2026-10-05
created: 2026-10-05
updated: 2026-10-05
tags: [indexation, sitemap, audit, organikk, hebdo]
status: stable
confidence: high
sources: 3
---

# Audit indexation Organikk — 2026-10-05

**Périmètre.** organikk.co, 30 URLs listées dans `sitemap.xml` (delta 0 vs 28/09). Lecture seule sur le web public. Aucun forçage d'indexation.

**Sources de vérité utilisées.**
- Statut HTTP `curl` (première réponse + `redirect_url` résolu).
- Présence dans `sitemap.xml` + `lastmod`.
- `robots.txt`.
- Parsing HTML servi : `<title>`, `<h1>` (inner tags strippés), `<link rel=canonical>`, `<meta name=robots>`, graphe interne reconstruit à partir des seuls `<a href>` (hreflang `<link rel=alternate>` exclu).

**Non testable.** Statut d'indexation Google réel. Pas d'accès à l'edge `admin-gsc-export` (`urlInspection` / `searchAnalytics`) dans cet environnement. Diff proposé le 10/07 pour remplacer le check #8 mort par un appel à l'API URL Inspection : **87 jours d'ouverture**. Test témoin relancé ce run (URL inexistante `/cette-page-nexiste-absolument-pas-xyz19146/`) : organikk.co répond HTTP 404 directement, et Google renvoie HTTP 200 / 92 308 octets sur `?q=site%3Aorganikk.co` avec 0 marqueur de blocage, texte visible = « Please click here if you are not redirected within a few seconds », 1 seule occurrence du domaine (écho de la requête). Couche B non testable **8e run consécutif**. Voir `loops/indexation-check/memory/questions.md`.

## 1. Synthèse

Semaine très calme sur la structure du sitemap (0 delta), mais trois mouvements structurels à noter : (1) premier article `/blog/*` à passer en 301, (2) découverte d'une URL hors sitemap servie en 200 avec `noindex, follow` réel linkée depuis toute la nav, (3) la Couche B reste morte pour la 8e semaine.

- **Sitemap 30 → 30 URLs (delta 0).** Trajectoire 115j : 169-136-143-143-146-146-330-330-332-333-334-334-142-91-91-88-28-29-30-**30**. Stabilisation après 2 semaines de légère expansion.
- **Premier article `/blog/*` redirigé.** `/blog/9-skills-seo-claude` → 301 → `/skills/`. 7/8 autres articles-poteaux testés (`process-seo-b2b-2026`, `information-gain-geo`, `wiki-ia-obsidian-claude`, et 5 nouveaux slugs probés ce run) répondent toujours 404 nu. Rupture du pattern uniform-404 observé sur 3 runs ; pas un blanket, une 301 unitaire.
- **`/systeme-seo/` découverte** — HTTP 200, 29 236 mots de HTML servi, `<meta name="robots" content="noindex, follow"/>`, canonical auto-référent, linkée depuis **24/30 pages du sitemap** (nav globale, titre « Automatiser 80 % de son SEO : accompagnement de 6 mois »). **Hors sitemap**. Premier `noindex` réel sur balise mesuré sur ce domaine ; cette URL n'a jamais été remontée dans les audits précédents.
- **`/manifeste{,/}` toujours 404.** 16e récurrence hebdo, **117 jours** depuis la reco P1 du 10/07. 0 lien `<a>` entrant sur les 30 pages téléchargées. Toujours hors du blanket 301 wiki.
- **Wiki 301 blanket → raffinement partiel stable.** 8/8 slugs testés redirigent 301 : `passage-ranking` et `agentic-search` → `/systeme/#audit` (2/8), `rrf`, `e-e-a-t`, `grounding-score`, `aeo`, `geo`, `sge` → `/systeme/` nu (6/8). Même proportion que la mesure 2/4 du 28/09, pas d'extension à de nouvelles ancres.
- **`/audit-seo/` reste orpheline, 90 mots.** 3e run consécutif dans le sitemap avec 0 lien `<a>` interne entrant, contre `/audit/` hors sitemap qui porte toujours 26 liens de nav. Split intact. Prédiction `pred-2026-09-23-audit-split` (resolve 23/10) reste ouverte, 12 jours restants.
- **`/tarifs/` toujours hors sitemap** — 7e récurrence, **37 jours** depuis la sortie du sitemap le 05/09. HTTP 200, canonical auto-référent, 1 seul lien `<a>` entrant (`/coaching-seo-lyon/`).
- **`sitemap_canonical_mismatch` : fix tient (3e semaine).** 28/30 URLs portent le slash canonique dans `<loc>`, 2 exceptions `.html` correctes. 30/30 HTTP 200 direct, 0 redirect.
- **`lastmod_uniforme` continue.** 30/30 URLs partagent `2026-10-05T05:48:51.615Z`. 20e récurrence hebdo, **117 jours** que le sitemap émet l'horodatage de build à la place du lastmod éditorial par URL.
- **`/skills/` 68 mots** (vs 57 mesurés au 28/09, +11 mots). Toujours la page la plus fine servie. 26 backlinks `<a>` entrants, aucune meta robots : hypothèse rendu client-side Next.js toujours ouverte.
- **`/audit-seo/` 90 mots** (vs 80 au 28/09, +10 mots). Deuxième plus fine. Pas d'enrichissement structurel.

**Chiffres du run.** 30/30 HTTP 200 direct. 30/30 avec `<title>`, `<h1>` et `<link rel=canonical>` auto-référent. **25/30** avec `<meta name="robots">` explicite `index, follow` ; 5 sans meta (mêmes 5 que les 2 runs précédents : `/skills/`, `/agent-seo/`, `/en/agent-seo/`, les 2 guides `.html` FR+EN — absence = indexable par défaut). **0 `noindex` sur balise dans le sitemap**. `robots.txt` inchangé (`User-Agent:* / Allow:/ + Sitemap`). Graphe interne reconstruit sur 30 fichiers HTML téléchargés — **248 arêtes uniques `<a>` par source** (hors self-ref), 436 avant restriction au `<a>` (donc 188 arêtes venaient uniquement de `<link rel=alternate>` hreflang). **26/30 title ≠ h1** après nettoyage du suffixe marque (28/30 au 28/09 ; léger relâchement du pattern éditorial, 2 pages se sont alignées : `/skills/` et le guide EN `.html`).

## 2. Anomalies critiques

### C1. `/blog/*` 404 nu — 4e run consécutif, mais premier 301 ponctuel apparu

- `curl -sI https://organikk.co/blog{,/}` → HTTP 404 nu (racine blog).
- Sur 8 slugs articles-poteaux testés : **1/8 redirigé** (`9-skills-seo-claude` → 301 → `/skills/`), **7/8 toujours 404 nu** (`process-seo-b2b-2026`, `information-gain-geo`, `wiki-ia-obsidian-claude`, `audit-seo-technique`, `aeo-geo`, `seo-chatgpt`, `maillage-interne-seo`).
- Le 301 unitaire sur `9-skills-seo-claude` → `/skills/` est cohérent avec le pattern du blanket wiki (où 2 slugs sur 8 pointent vers `/systeme/#audit`) : rediriger un article vers la landing éditoriale qui a repris son sujet.
- Reco P2 du 21/09 (décision URL par URL depuis la sauvegarde du repo) **partiellement amorcée** après 14 jours. Rythme : 1 URL traitée sur 1 semaine → le rattrapage prendra plusieurs mois à cette cadence.
- Impact SEO : linkjuice historique perdu sur 7+ URLs, aucun signal de réallocation pour Google côté `/blog/*`.

### C2. `/manifeste{,/}` 404 — 16e récurrence (117 jours)

- HTTP 404 sur les deux variantes.
- Hors sitemap. 0 lien `<a>` entrant sur les 30 pages téléchargées.
- Reco P1 du 10/07 (301 vers `/systeme/` ou 410 documenté) non appliquée depuis **117 jours**.
- Le 301 unitaire posé sur `9-skills-seo-claude` cette semaine prouve que l'opération est faisable au cas par cas. L'absence de traitement sur `/manifeste` devient plus explicable comme oubli que comme choix.

### C3. `lastmod_uniforme` 30/30 — 20e récurrence (117 jours)

- `grep -c '<lastmod>2026-10-05T05:48:51.615Z</lastmod>' sitemap.xml` = 30.
- `grep -c '<lastmod>' sitemap.xml` = 30. **1 seul lastmod distinct.**
- Le sitemap continue d'émettre l'horodatage de build à la place du lastmod éditorial par URL. Signal fraîcheur perdu depuis 117 jours.
- Reco P2 du 21/09 non appliquée (3 semaines).

### C4. `/audit-seo/` (dans sitemap) vs `/audit/` (hors sitemap) — split intact, 3e récurrence

- `/audit-seo/` = 90 mots, 0 lien `<a>` interne entrant depuis les 30 pages du sitemap, 2 sortants. Canonical auto-référent. `index, follow`.
- `/audit/` = hors sitemap, 26 liens `<a>` entrants (toute la nav globale). Canonical auto-référent. **Pas de meta robots** → indexable par défaut.
- Deux URLs qui servent la même surface produit avec deux régimes contradictoires. Aucune 301 croisée, aucun canonical croisé. 12 jours restants sur `pred-2026-09-23-audit-split` (resolve 23/10) : à cette cadence (0 mouvement en 2 semaines sur ce couple), la prédiction va résoudre HIT.

### C5. `/systeme-seo/` — nouvelle découverte, URL hors sitemap avec `noindex` réel sur balise, linkée depuis la nav

- **Première fois mesurée dans un audit indexation Organikk.** HTTP 200, 581 044 octets servis, 29 236 mots de HTML (ratio texte/HTML signalant du contenu rich).
- `<meta name="robots" content="noindex, follow"/>` — **seul `noindex` sur balise de tout le mesurable**, détecté sur une URL servie et nav-linkée.
- Canonical auto-référent (`https://organikk.co/systeme-seo/`).
- 24 pages du sitemap sur 30 pointent vers cette URL via `<a href>` (nav globale ou footer). Title « Automatiser 80 % de son SEO : accompagnement de 6 mois ».
- Lecture plausible : ancienne landing commerciale conservée active pour le flux conversion depuis la nav, désindexée volontairement pour éviter la concurrence avec `/systeme/` (indexable, dans sitemap, 413 mots). Si c'est intentionnel : la cohabitation vaut d'être documentée. Si c'est un reliquat : la 24-link-nav fuit du PageRank vers une page que Google n'indexera jamais.
- La règle `noindex, follow` fait que les 24 liens `<a>` sortants de cette page restent crawlables (notamment vers les commerciales et les cas), mais la page elle-même ne figurera jamais en SERP. À arbitrer avec Tim.

### C6. Orphelines strict — 9/30 pages du sitemap à 0 lien `<a>` interne entrant (identique au 28/09)

Comptage strict sur les seuls `<a href>` éditoriaux, hreflang `<link rel=alternate>` exclu. Résultat identique à la mesure 09/28 :

| URL | Récurrence | Jours observés | Mots | Note |
|-----|-----------|-----------------|------|------|
| `/accompagnement-seo-geo/` | 16e | 117 | 1489 | Reco P1 depuis 10/07 |
| `/consultant-geo/` | 11e | 56 | 2465 | 3e page en volume du site |
| `/formation-seo-ia/` | 10e | 49 | 661 | Apparue au 17/08 sans maillage |
| `/consultant-lead-seo/` | 5e | 21 | 1152 | Apparue au 14/09 sans maillage |
| `/plan-du-site/` | 5e | 21 | 226 | Auto-hub censé mailler, orphelin lui-même |
| `/audit-seo/` | 3e | 12 | 90 | Cf. C4 |
| `/en/agent-seo/` | 3e | 12 | 3351 | Hreflang bidirectionnel détecté ce run (`<link rel=alternate>` depuis `/agent-seo/`), **aucun `<a>` éditorial FR→EN** |
| `/guides/audit-seo-technique-claude.html` | 3e | 12 | 5338 | Hreflang bidirectionnel détecté entre les deux `.html` ; hub `/guides/` ne lie que les PDF |
| `/guides/en/audit-seo-technique-claude.html` | 3e | 12 | 5172 | Idem |

- **Précision méthode ce run** : les 3 orphelines « .html + en/ » ont bien un `<link rel="alternate" hreflang>` entre elles et avec leur variante FR, ce qui donne 1 inbound « non éditorial » chacune. Ces liens hreflang ne portent pas de linkjuice de contenu, donc la mesure strict `<a>` les exclut correctement. **Rien n'a changé côté maillage éditorial**.
- 13 861 mots cumulés sur les 3 pages orphelines longues jamais mesurées avant le 23/09 (/en/agent-seo/ + 2 guides `.html`).
- Le hub `/plan-du-site/` reste muet sur ces 9 pages — pas d'édition ce run (lui-même reste à 1 lien entrant depuis l'intérieur du sitemap).

Prédiction `pred-2026-09-23-orphelines-commerciales` (resolve 23/10) : reste ouverte, aucun mouvement en 12 jours.

### C7. Couche B non testable — 8e run consécutif

- Test témoin obligatoire (URL volontairement inexistante `/cette-page-nexiste-absolument-pas-xyz19146/`) : organikk répond HTTP 404 directement. Google (`?q=site%3Aorganikk.co`) renvoie HTTP 200, 92 308 octets, 0 marqueur de blocage recaptcha, 1 occurrence de `organikk.co` (écho de la requête), texte visible = « Please click here if you are not redirected within a few seconds ».
- Confirmation stricte : Google ne sert plus de SERP sans JS aux clients HTTP. **Aucun statut d'indexation Google publié dans ce rapport**.
- Diff `urlInspection` du 10/07 dans `memory/questions.md` : **87 jours d'ouverture**. Impact particulièrement lourd cette semaine sur C1 (blog mixte 301+404), C4 (split audit), C5 (page nav-linkée avec noindex), C6 (orphelines longues jamais mesurées) — sans `urlInspection`, impossible de dire si Google sert encore quoi que ce soit de tout ça.

## 3. Anomalies mineures

### M1. Hors sitemap servies en 200 — 4 URLs (dont la nouvelle `/systeme-seo/`)

- `/tarifs/` : 1 lien entrant (`/coaching-seo-lyon/`), canonical auto-référent, `index, follow`. **7e récurrence, 37 jours.** Page conversion coaching doublement invisible.
- `/systeme-seo-ia/` : 1 lien entrant (`/methode/`), canonical auto-référent, `index, follow`. **3e récurrence.**
- `/audit/` : 26 liens entrants (nav globale), canonical auto-référent, pas de meta robots (= indexable par défaut). **3e récurrence.** Cf. C4.
- `/systeme-seo/` : **24 liens entrants** (nav globale), canonical auto-référent, **`noindex, follow` réel**. Cf. C5. 1re récurrence.

Verdict : `/tarifs/` reste à trancher (7e récurrence, page commerciale). Les 3 autres sont des décisions produit à documenter plutôt que des erreurs techniques.

### M2. `/plan-du-site/` — hub incomplet, 5e récurrence

- Toujours la même structure : 19 liens sortants dont 18 vers le sitemap + 1 vers `/audit/` (hors sitemap) + 1 vers `/skills/`.
- Pas d'ajout cette semaine (au 28/09, `/consultant-seo-geo-lyon/` avait été ajoutée).
- **N'adresse toujours pas** : `/audit-seo/`, `/accompagnement-seo-geo/`, `/consultant-geo/`, `/consultant-lead-seo/`, `/formation-seo-ia/`, `/tarifs/`, `/systeme-seo-ia/`, `/bootcamp/programme/`, `/bootcamp-quiz/`. Soit 8 des 9 pages du site les plus mal maillées.
- Reco P1 (couvrir les 5 commerciales) répétée pour la 5e semaine.

### M3. `/guides/` hub ne lie que les 7 PDF — 3e récurrence

- Extraction des `<a href>` de `/guides/` : 7 PDF, 0 lien vers les 2 pages `.html` du sitemap.
- Les 2 pages `.html` cumulent 10 510 mots servis (5338 FR + 5172 EN).
- Prédiction `pred-2026-09-23-guides-hub` (resolve 23/10) : reste ouverte, 12 jours restants.

### M4. Meta robots hétérogène — 5 pages sans meta (3e récurrence)

- 25/30 pages portent `<meta name="robots" content="index, follow">`.
- 5 sans meta : `/agent-seo/`, `/en/agent-seo/`, `/skills/`, `/guides/audit-seo-technique-claude.html`, `/guides/en/audit-seo-technique-claude.html`. Absence = indexable par défaut, aucun risque `noindex`.
- Mappe **exactement** sur la famille de gabarit léger impliquée dans C4 (audit-seo) et C6 (orphelines longues). Marqueur de gabarit, pas anomalie en soi.

### M5. Title vs h1 divergents 26/30 — pattern éditorial persistant, 3e récurrence

- Après nettoyage du suffixe marque, 26/30 titles diffèrent de leur h1 (28/30 au 28/09 ; `/skills/` et le guide EN `.html` se sont alignés cette semaine).
- Pattern lisible : title = requête cible SEO, h1 = accroche narrative. Décision éditoriale probable.
- Les 4 égalités : `/skills/`, `/mentions-legales/`, `/politique-confidentialite/`, `/guides/en/audit-seo-technique-claude.html` — toutes des pages où le titre marketing = sujet unique.

## 4. Points méthode / faux positifs

### P1. Grep plein texte `noindex` — faux positif attendu, 3e récurrence

- `grep -i noindex` matche 4/30 pages : `/agent-seo/` (5 occurrences), `/en/agent-seo/` (5), `/guides/audit-seo-technique-claude.html` (9), `/guides/en/audit-seo-technique-claude.html` (9). Copie éditoriale SEO qui parle de la directive.
- Vérification balise par balise (meta robots + HTTP `X-Robots-Tag`) : **0 directive `noindex` réelle** sur ces 4 pages.
- `curl -sI` sur les 4 URLs : aucun header `X-Robots-Tag`.
- Cause déjà documentée aux runs 23/09 et 28/09. Rien de nouveau, pas d'anomalie.

### P2. Nouveau check à durcir — compter les inbound sur `<a>` seulement, pas sur `<link rel=alternate>`

- Ce run est le premier à distinguer explicitement : 436 edges totaux `href` → 248 edges `<a>` seulement. Les 188 edges supprimés sont des hreflang alternates.
- Sans cette distinction, les 3 orphelines `/en/agent-seo/` + 2 guides `.html` auraient été comptées « 1 inbound ✓ » cette semaine, et un lecteur aurait conclu à une amélioration du maillage. **Il n'y a pas eu d'amélioration** — seulement une mesure plus précise.
- À inscrire dans le skill : *le compteur orphelines doit filtrer `<a href>` et exclure `<link rel="alternate">`.*

## 5. Résolution des prédictions du 28/09 (resolve_by 2026-10-05)

| ID | Verdict | Détail |
|---|---|---|
| `pred-2026-09-28-manifeste-404` | HIT | 16e récurrence, 117 jours sans action |
| `pred-2026-09-28-blog-404` | HIT partiel | 7/8 articles-poteaux testés toujours 404 nu, MAIS **1/4 des articles de la pred originale (`9-skills-seo-claude`) est passé en 301 → `/skills/`** — premier mouvement en 3 semaines |
| `pred-2026-09-28-orphans-9pages` | HIT | 9/9 orphelines du 28/09 restent orphelines strict `<a>` (hreflang alternates mesurés mais exclus par méthode durcie) |
| `pred-2026-09-28-tarifs-sitemap` | HIT | 7e récurrence, `/tarifs/` toujours hors sitemap |
| `pred-2026-09-28-lastmod-uniforme` | HIT | 30/30, 20e récurrence, 117 jours |
| `pred-2026-09-28-audit-split` | HIT | `/audit-seo/` dans sitemap + `/audit/` hors sitemap, pas de 301 ni canonical croisé |

## 6. Recommandations priorisées

**P1 — maillage éditorial sur les 9 orphelines.**
- Ajouter les 9 pages orphelines au hub `/plan-du-site/` en une passe (5 commerciales + `/audit-seo/` + `/en/agent-seo/` + 2 guides `.html`). Preuve d'éditabilité : `/consultant-seo-geo-lyon/` y a été ajoutée le 28/09.
- Pointer le hub `/guides/` vers les 2 pages `.html` (1 ligne d'ancre chacune), ou retirer les 2 URLs du sitemap.
- Cause C6 = 8/9 orphelines chroniques + M2 hub incomplet + M3 hub ne lie pas ses cibles. Trois anomalies, une cause commune : personne ne mailla `plan-du-site` et `guides` au moment d'ajouter les pages produit.

**P1 — arbitrer `/systeme-seo/` (nouvelle).**
- Si intentionnel (landing conversion désindexée) : documenter dans le repo + accepter la fuite de PageRank des 24 nav links.
- Si reliquat : retirer les 24 liens de nav vers `/systeme-seo/` et poser une 301 → `/systeme/`. Évite que 80 % des pages du site envoient du linkjuice vers une URL que Google n'indexera jamais.

**P2 — décisions structurelles à trancher.**
- `/blog/*` : poursuivre le pattern lancé cette semaine (301 unitaire vers landing éditoriale), à cadence > 1/semaine (sinon rattrapage pluri-mensuel sur 7+ URLs). Un blanket serait haut-risque, mais 4 semaines sans plan reste coûteux.
- `/audit-seo/` vs `/audit/` : trancher laquelle est la canonique et poser une 301 de l'autre, ou un `link rel=canonical` croisé (C4). Le split intact = double indexation risque à 3 semaines.
- `/manifeste{,/}` : 301 vers `/systeme/` ou 410 documenté (C2). Preuve de faisabilité posée par le 301 `9-skills-seo-claude` → `/skills/` cette semaine : aucune raison structurelle de laisser `/manifeste` en dehors du blanket.
- `/tarifs/` : réintroduire au sitemap (M1) et rétablir au moins 1 backlink nav. 7e récurrence, 37 jours.

**P3 — signal fraîcheur.**
- `lastmod_uniforme` (C3) : émettre le `lastmod` éditorial par URL au lieu de l'horodatage de build. 117 jours de perte de signal.

**P4 — méthode boucle (Tim tranche).**
- Diff `urlInspection` du 10/07 dans `memory/questions.md` : 87 jours d'ouverture. Sans ça, la Couche B reste morte et 6 anomalies critiques ce run ne peuvent pas être mesurées côté Google (C1, C4, C5, C6). Cf. `memory/questions.md`.
- Durcir le compteur d'inbound dans le skill : filtrer sur `<a href>` et exclure `<link rel="alternate">` (P2 nouveau ce run).

## 7. Nouvelles prédictions (resolve_by 2026-10-12)

- `pred-2026-10-05-manifeste-404` : `/manifeste{,/}` encore HTTP 404 au run du 2026-10-12 (17e récurrence).
- `pred-2026-10-05-blog-cadence` : au plus 1 nouvelle URL `/blog/*` passera en 301 d'ici le 2026-10-12 (cadence actuelle 1 URL/semaine ; prédit la poursuite de ce rythme lent).
- `pred-2026-10-05-orphans-9pages` : les 9 pages orphelines strict `<a>` de C6 resteront à 0 lien `<a>` entrant au run du 2026-10-12.
- `pred-2026-10-05-tarifs-sitemap` : `/tarifs/` restera hors sitemap au run du 2026-10-12 (8e récurrence).
- `pred-2026-10-05-lastmod-uniforme` : 30+/30+ URLs sitemap partageront un unique `<lastmod>` au run du 2026-10-12 (21e récurrence).
- `pred-2026-10-05-audit-split` : `/audit/` hors sitemap ET `/audit-seo/` dans le sitemap au run du 2026-10-12, sans 301 ni canonical croisé (4e récurrence). Résolution de `pred-2026-09-23-audit-split` à 10 jours.
- `pred-2026-10-05-systeme-seo-noindex` : `/systeme-seo/` restera HTTP 200 + `noindex, follow` + nav-linkée depuis ≥ 20 pages du sitemap au run du 2026-10-12 (1re récurrence attendue).
- `pred-2026-10-05-guides-hub` : `/guides/` ne liera toujours pas les 2 `.html` au run du 2026-10-12 (4e récurrence).
