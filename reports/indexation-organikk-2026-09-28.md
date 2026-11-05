---
type: audit
title: Indexation Organikk — audit hebdomadaire 2026-09-28
created: 2026-09-28
updated: 2026-09-28
tags: [indexation, sitemap, audit, organikk, hebdo]
status: stable
confidence: high
sources: 3
---

# Audit indexation Organikk — 2026-09-28

**Périmètre.** organikk.co, 30 URLs listées dans `sitemap.xml` (delta +2 vs 21/09 : 28 → 30 ; +1 vs 23/09 : 29 → 30). Lecture seule sur le web public. Aucun forçage d'indexation.

**Sources de vérité utilisées.**
- Statut HTTP `curl` (première réponse + redirection résolue), passe série.
- Présence dans `sitemap.xml` + `lastmod`.
- `robots.txt`.
- Parsing HTML servi : `<title>`, `<h1>`, `<link rel=canonical>`, `<meta name=robots>`, graphe interne (hrefs internes normalisés).

**Non testable.** Statut d'indexation Google réel. Pas d'accès à l'edge `admin-gsc-export` (`urlInspection` / `searchAnalytics`) dans cet environnement. Diff proposé le 10/07 pour remplacer le check #8 mort par un appel à l'API URL Inspection : **80 jours d'ouverture**. Test témoin relancé ce run (URL inexistante `/cette-page-nexiste-absolument-pas-xyz{RAND}/`) : Google renvoie HTTP 200, 92 065 octets, 0 marqueur de blocage, texte visible « Please click here if you are not redirected within a few seconds » — la SERP n'est plus servie sans JS. Couche B non testable 7e run consécutif. Voir `loops/indexation-check/memory/questions.md`.

## 1. Synthèse

Semaine calme sur la structure. +2 URLs sitemap depuis le run local 21/09 : `/audit-seo/` (déjà signalée dans le run 23/09 externe) et `/consultant-seo-geo-lyon/` (nouvelle cette semaine).

- **Sitemap 28 → 30 URLs (+2).** Trajectoire 108j : 169-136-143-143-146-146-330-330-332-333-334-334-142-91-91-88-28-29-**30**. Deuxième semaine de légère expansion après 3 contractions consécutives.
- **`/consultant-seo-geo-lyon/` entre au sitemap.** 608 mots, `index, follow`, canonical auto-référent. Un seul lien entrant depuis le sitemap : `/plan-du-site/`. Le hub `/plan-du-site/` a donc été mis à jour pour inclure la nouvelle page géo, mais rien n'a bougé sur les 5 pages commerciales orphelines chroniques.
- **`/audit-seo/` reste orpheline, 80 mots.** 2e run consécutif dans le sitemap avec 0 lien interne entrant, contre `/audit/` hors sitemap qui porte toujours 26 liens de nav. Le split reste entier. Prédiction `pred-2026-09-23-audit-split` (resolve 2026-10-23) reste ouverte.
- **`/blog/*` toujours 404 nu.** Racine `/blog{,/}` = 404. 4/4 anciens articles-poteaux testés = 404 sans redirection. Rien n'a bougé en 7 jours. 3e run consécutif sans pipeline de 301.
- **`/manifeste{,/}` toujours 404.** 15e récurrence hebdo, **110 jours** depuis la reco P1 du 10/07. Toujours hors du blanket 301 wiki qui a été posé sur les 49 slugs `/wiki/*`.
- **`/wiki/*` folded en 301 blanket → `/systeme/` mais avec 2 ancres ciblées.** 4/4 slugs testés (`passage-ranking`, `rrf`, `e-e-a-t`, `agentic-search`) redirigent 301 : `passage-ranking` → `/systeme/#audit`, `agentic-search` → `/systeme/#audit`, `rrf` et `e-e-a-t` → `/systeme/` nu. Confirmation d'un raffinement partiel vs le blanket brut du 21/09.
- **`/tarifs/` toujours hors sitemap** — 6e récurrence, **30 jours** depuis la sortie du sitemap le 05/09. HTTP 200, canonical auto-référent, 1 seul lien entrant depuis les 30 pages téléchargées (`/coaching-seo-lyon/`).
- **`sitemap_canonical_mismatch` : fix tient.** 28/30 URLs portent le slash canonique dans `<loc>` (2 exceptions `.html` correctes ainsi). 30/30 servies en HTTP 200 direct, 0 redirect. Fin de la récurrence 16 semaines confirmée pour la 2e semaine.
- **`lastmod_uniforme` continue.** 30/30 URLs partagent `2026-09-28T05:45:27.499Z`. 19e récurrence hebdo, **110 jours** que le sitemap émet l'horodatage de build à la place du lastmod éditorial par URL.
- **`/skills/` gagne 10 mots** (47 → 57 en 7 jours) mais reste la page la plus fine du site. 26 backlinks entrants, aucune meta robots, contenu quasi absent en HTML servi : hypothèse rendu client-side Next.js toujours ouverte.
- **`/audit-seo/` = 80 mots**, la plus fine des 30 URLs. Landing du produit outil, contenu textuel volontairement minimal, mais absence totale de maillage interne pose problème pour la découverte crawler.

**Chiffres du run.** 30/30 HTTP 200 direct. 30/30 avec `<title>`, `<h1>` et `<link rel=canonical>` auto-référent. 25/30 avec `<meta name="robots">` explicite `index, follow` ; 5 sans meta (les mêmes 5 qu'au 21/09 : `/skills/`, `/agent-seo/`, `/en/agent-seo/`, `/guides/*.html` FR+EN — absence = indexable par défaut). 0 `noindex` sur balise. `robots.txt` inchangé (`User-Agent:* / Allow:/ + Sitemap`). Graphe interne construit sur 30 fichiers HTML téléchargés, 165 arêtes uniques après normalisation, auto-références exclues. 28/30 title vs h1 divergents après nettoyage du suffixe marque (pattern éditorial persistant : title = requête cible, h1 = accroche narrative).

## 2. Anomalies critiques

### C1. `/blog/*` toujours 404 nu — 3e run consécutif

- `curl -sI https://organikk.co/blog{,/}` → HTTP 404, 4/4 articles-poteaux testés (`process-seo-b2b-2026`, `information-gain-geo`, `9-skills-seo-claude`, `wiki-ia-obsidian-claude`) → HTTP 404 sans redirection.
- Écart persistant avec le traitement `/wiki/*` (blanket 301 + 2 ancres ciblées cette semaine sur `#audit`).
- Impact SEO : linkjuice historique perdu, aucun signal de réallocation pour Google.
- Reco P2 du 21/09 (décision URL par URL depuis la sauvegarde du repo) non appliquée. **7 jours.**

### C2. `/manifeste{,/}` 404 — 15e récurrence (110 jours)

- HTTP 404 sur les deux variantes.
- Hors sitemap. 0 lien entrant sur les 30 pages téléchargées.
- Reco P1 du 10/07 (301 ou 410 documenté) non appliquée depuis **110 jours**.
- N'a pas été absorbée par le blanket 301 wiki, contrairement à ce qu'on aurait pu attendre.

### C3. `lastmod_uniforme` 30/30 — 19e récurrence (110 jours)

- `grep -c '<lastmod>2026-09-28T05:45:27.499Z</lastmod>' sitemap.xml` = 30.
- `grep -c '<lastmod>' sitemap.xml` = 30. **1 seul lastmod distinct.**
- Le sitemap continue d'émettre l'horodatage de build à la place du lastmod éditorial par URL. Signal fraîcheur perdu depuis 110 jours.
- Reco P2 du 21/09 non appliquée.

### C4. `/audit-seo/` (dans sitemap) vs `/audit/` (hors sitemap) — split intact, 2e récurrence

- `/audit-seo/` = 80 mots, 0 lien interne entrant, 2 sortants (vers `/methode/` et `/skills/`). Canonical auto-référent.
- `/audit/` = hors sitemap mais 26 liens entrants (tout le maillage nav global). Canonical auto-référent aussi.
- Deux URLs qui servent la même surface produit avec deux régimes contradictoires. Aucune 301 croisée, aucun canonical croisé.
- Prédiction `pred-2026-09-23-audit-split` (resolve 2026-10-23) : reste ouverte, pas de mouvement en 5 jours.

### C5. Orphelines commerciales persistantes — 9/30 pages du sitemap à 0 lien interne entrant

Sur les 30 URLs du sitemap :

| URL | Récurrence | Jours observés | Mots | Note |
|-----|-----------|-----------------|------|------|
| `/accompagnement-seo-geo/` | 15e | 110 | 1423 | Reco P1 depuis 10/07 |
| `/consultant-geo/` | 10e | 49 | 2392 | 3e page en volume du site |
| `/formation-seo-ia/` | 9e | 42 | 651 | Apparue au 17/08 sans maillage |
| `/consultant-lead-seo/` | 4e | 14 | 1127 | Apparue au 14/09 sans maillage |
| `/plan-du-site/` | 4e | 14 | 214 | Auto-hub censé mailler, orphelin lui-même |
| `/audit-seo/` | 2e | 5 | 80 | Cf. C4 |
| `/en/agent-seo/` | 2e | 5 | 3368 | Hreflang vers `/agent-seo/`, aucun lien FR→EN |
| `/guides/audit-seo-technique-claude.html` | 2e | 5 | 5329 | Hub `/guides/` ne lie que les PDF |
| `/guides/en/audit-seo-technique-claude.html` | 2e | 5 | 5162 | Idem |

- **13 360 mots cumulés** sur les 3 pages orphelines longues jamais mesurées avant le 23/09 (les 2 guides `.html` + `/en/agent-seo/`).
- Le hub `/plan-du-site/` a été mis à jour pour inclure `/consultant-seo-geo-lyon/` (nouvelle cette semaine) — donc le fichier est éditable — mais aucune des 9 orphelines chroniques n'y figure pourtant.

Prédiction `pred-2026-09-23-orphelines-commerciales` (resolve 2026-10-23) : reste ouverte, aucun mouvement en 5 jours.

### C6. Couche B non testable — méthode `site:` invalide 7e run

- Test témoin obligatoire (URL volontairement inexistante) relancé ce run : HTTP 200, 92 065 octets, 0 marqueur de blocage recaptcha, 1 occurrence du domaine (écho de la requête), texte visible = « Please click here if you are not redirected within a few seconds ».
- Confirmation stricte : Google ne sert plus de SERP sans JS aux clients HTTP. La distinction « non indexée » / « non testable » reste tenue : **aucun statut d'indexation Google publié dans ce rapport**.
- Diff `urlInspection` du 10/07 dans `memory/questions.md` : **80 jours d'ouverture**. Impact particulièrement lourd cette semaine sur C1 (blog 404), C4 (split audit), C5 (3 orphelines jamais mesurées) — sans `urlInspection`, impossible de dire si Google sert encore quoi que ce soit de tout ça.

## 3. Anomalies mineures

### M1. Hors sitemap servies en 200 — 3 URLs

- `/tarifs/` : 778 mots, 1 lien entrant (`/coaching-seo-lyon/`), canonical auto-référent, `index, follow`. **6e récurrence, 30 jours.** Cette page porte la conversion coaching et reste doublement invisible.
- `/systeme-seo-ia/` : 1328 mots, 1 lien entrant (`/methode/`), canonical auto-référent, `index, follow`. **2e récurrence.**
- `/audit/` : ~200 mots, 26 liens entrants (nav globale), canonical auto-référent, `index, follow`. **2e récurrence.** Cf. C4.

Verdict : `/tarifs/` mérite une décision (récurrence à 30 jours, page commerciale). `/systeme-seo-ia/` et `/audit/` : à vérifier, pas d'action recommandée sans arbitrage éditorial.

### M2. `/plan-du-site/` — hub incomplet, 4e récurrence

- 19 liens sortants uniques dont 18 vers le sitemap + 1 vers `/audit/` (hors sitemap) + 1 vers `/skills/`.
- Cette semaine, `/plan-du-site/` a **ajouté** `/consultant-seo-geo-lyon/` (nouvelle sitemap), preuve que le hub est éditable et maintenu.
- **N'adresse toujours pas** : `/audit-seo/`, `/accompagnement-seo-geo/`, `/consultant-geo/`, `/consultant-lead-seo/`, `/formation-seo-ia/`, `/tarifs/`, `/systeme-seo-ia/`, `/bootcamp/programme/`, `/bootcamp-quiz/`. Soit 8 des 9 pages du site les plus mal maillées.
- Reco P1 (couvrir les 5 commerciales) répétée pour la 4e semaine.

### M3. `/guides/` hub ne lie que les 7 PDF — 2e récurrence

- Extraction des `<a href>` de `/guides/` : 7 PDF (`5-skills-seo-technique-claude.pdf`, `agent-seo-claude.pdf`, `audit-seo-technique-claude.pdf`, `de-0-a-1-seo-claude.pdf`, `installer-skills-seo-technique-claude.pdf`, `maillage-interne-claude.pdf`, `playbook-reddit-seo-geo.pdf`), 0 lien vers les 2 pages `.html` du sitemap.
- Les 2 pages `.html` cumulent 10 491 mots servis (5329 FR + 5162 EN).
- Cause isolée au run 23/09 (hub_ne_lie_pas_ses_cibles), toujours vraie.
- Prédiction `pred-2026-09-23-guides-hub` (resolve 2026-10-23) : reste ouverte.

### M4. Meta robots hétérogène — 5 pages sans meta (2e récurrence)

- 25/30 pages portent `<meta name="robots" content="index, follow">`.
- 5 sans meta : `/agent-seo/`, `/en/agent-seo/`, `/skills/`, `/guides/audit-seo-technique-claude.html`, `/guides/en/audit-seo-technique-claude.html`. Absence = indexable par défaut, aucun risque `noindex`.
- Mappe **exactement** sur la famille de gabarit léger impliquée dans C4 (audit-seo) et C5 (orphelines longues). Marqueur de gabarit, pas anomalie en soi.

### M5. Title vs h1 divergents 28/30 — pattern éditorial persistant, 2e récurrence

- Après nettoyage du suffixe marque, 28/30 titles diffèrent de leur h1.
- Pattern lisible : title = requête cible SEO (« Consultant GEO : ranker sur ChatGPT et les IA »), h1 = accroche narrative (« Consultant GEO pour ranker vos projets tech sur ChatGPT et les IA génératives »).
- Décision éditoriale probable, pas anomalie technique.

## 4. Points méthode / faux positifs

### P1. Grep plein texte `noindex` — faux positif attendu

- `grep -i noindex` matche 4/30 pages : `/agent-seo/` (5 occurrences), `/en/agent-seo/` (5), `/guides/audit-seo-technique-claude.html` (9), `/guides/en/audit-seo-technique-claude.html` (9). Copie éditoriale SEO qui parle de la directive.
- Vérification balise par balise (meta robots + X-Robots-Tag) : 0 directive `noindex` réelle sur ces 4 pages.
- Cause déjà documentée au run 23/09 (durcir le check #3 pour extraire la balise). Rien de nouveau, pas d'anomalie.

## 5. Résolution des prédictions du 21/09 (resolve_by 2026-09-28)

| ID | Verdict | Détail |
|---|---|---|
| `pred-2026-09-21-manifeste-404` | HIT | 15e récurrence, 110 jours sans action |
| `pred-2026-09-21-orphans-persist` | HIT | 5 pages commerciales toujours à 0 lien interne entrant réel |
| `pred-2026-09-21-blog-404` | HIT | 4/4 articles-poteaux toujours 404 nu, aucune redirection |
| `pred-2026-09-21-tarifs-sitemap` | HIT | 5e/6e récurrence, /tarifs/ toujours hors sitemap |
| `pred-2026-09-21-wiki-301-blanket` | HIT partiel | 4/4 slugs testés redirigent 301, MAIS 2/4 vers ancre ciblée `#audit` (`passage-ranking`, `agentic-search`), 2/4 vers `/systeme/` nu (`rrf`, `e-e-a-t`) — raffinement partiel du blanket |
| `pred-2026-09-21-lastmod-uniforme` | HIT | 30/30, 19e récurrence, 110 jours |
| `pred-2026-09-21-canonical-fix-persist` | HIT | 28/30 canoniques avec slash final, 2 `.html` exceptions correctes, 0 URL sans slash |

## 6. Recommandations priorisées

**P1 — dette maillage aggravée par la nouvelle géo.**
- Ajouter les **9 pages orphelines** au hub `/plan-du-site/` en une passe (5 commerciales + `/audit-seo/` + `/en/agent-seo/` + 2 guides `.html`). Preuve d'éditabilité : `/consultant-seo-geo-lyon/` y a été ajoutée cette semaine.
- Pointer le hub `/guides/` vers les 2 pages `.html` (1 ligne d'ancre chacune), ou retirer les 2 URLs du sitemap.
- Cause C5 = 8/9 orphelines chroniques + M2 hub incomplet + M3 hub ne lie pas ses cibles. Trois anomalies, une cause commune : personne ne mailla `plan-du-site` et `guides` au moment d'ajouter les pages produit.

**P2 — décisions structurelles à trancher.**
- `/blog/*` : décider URL par URL depuis la sauvegarde du repo (C1). Un blanket dossier→dossier serait haut-risque, mais 3 semaines sans plan est aussi coûteux.
- `/audit-seo/` vs `/audit/` : trancher laquelle est la canonique et poser une 301 de l'autre, ou un `link rel=canonical` croisé (C4). Le split intact = double indexation risque à 2 semaines.
- `/manifeste{,/}` : 301 vers `/systeme/` (blanket wiki) ou 410 documenté (C2). Aucune raison structurelle de la laisser en dehors du blanket.
- `/tarifs/` : réintroduire au sitemap (M1) et rétablir 1 backlink nav minimum. Page commerciale à 30 jours d'invisibilité.

**P3 — signal fraîcheur.**
- `lastmod_uniforme` (C3) : émettre le `lastmod` éditorial par URL au lieu de l'horodatage de build. 110 jours de perte de signal.

**P4 — méthode boucle (Tim tranche).**
- Diff `urlInspection` du 10/07 dans `memory/questions.md` : 80 jours d'ouverture. Sans ça, la Couche B reste morte et 6 anomalies critiques ce run ne peuvent pas être mesurées côté Google (C1, C4, C5). Cf. `memory/questions.md`.

## 7. Nouvelles prédictions (resolve_by 2026-10-05)

- `pred-2026-09-28-manifeste-404` : `/manifeste{,/}` encore HTTP 404 au run du 2026-10-05 (16e récurrence).
- `pred-2026-09-28-blog-404` : 4/4 articles-poteaux du blog encore 404 nu au run du 2026-10-05.
- `pred-2026-09-28-orphans-9pages` : les 9 pages orphelines de C5 resteront à 0 lien interne entrant au run du 2026-10-05.
- `pred-2026-09-28-tarifs-sitemap` : `/tarifs/` restera hors sitemap au run du 2026-10-05 (7e récurrence).
- `pred-2026-09-28-lastmod-uniforme` : 30+/30+ URLs sitemap partageront un unique `<lastmod>` au run du 2026-10-05 (20e récurrence).
- `pred-2026-09-28-audit-split` : `/audit/` restera hors sitemap ET `/audit-seo/` restera dans le sitemap au run du 2026-10-05, sans 301 ni canonical croisé (3e récurrence, prédiction plus fine que celle du 23/09 à 30 jours).
