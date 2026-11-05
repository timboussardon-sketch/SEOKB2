---
type: audit
title: Indexation Organikk - audit hebdomadaire 2026-10-19
created: 2026-10-19
updated: 2026-10-19
tags: [indexation, sitemap, audit, organikk, hebdo]
status: stable
confidence: high
sources: 3
---

# Audit indexation Organikk - 2026-10-19

**Périmètre.** organikk.co, 31 URLs listées dans `sitemap.xml` (delta +1 vs 2026-10-12 : +1 entrée `/consultant-seo-saas/`, -1 sortie `/systeme/` passée en 301). Lecture seule sur le web public. Aucun forçage d'indexation.

**Sources de vérité utilisées.**
- Statut HTTP `curl -sIL` (code final + chaîne de redirections).
- Présence dans `sitemap.xml` + `lastmod`.
- `robots.txt`.
- Parsing HTML servi : `<title>`, `<h1>` (balises enfants strippées, décodage entités), `<link rel=canonical>`, `<meta name=robots>`, graphe interne reconstruit à partir des seuls `<a href>` (hreflang `<link rel=alternate>` exclu, durcissement P2 du 2026-10-05).

**Non testable.** Statut d'indexation Google réel. Pas d'accès à `urlInspection` / `searchAnalytics` dans cet environnement. Témoin obligatoire relancé : `/cette-page-nexiste-absolument-pas-xyz<ts>/` renvoie HTTP 404 côté organikk, `https://www.google.com/search?q=site%3Aorganikk.co` renvoie HTTP 200 / 92 765 octets, 1 occurrence du domaine (écho de la requête), 0 marqueur recaptcha, aucune SERP sans JS. Couche B non testable, **10e run consécutif**. Diff `urlInspection` du 2026-07-10 toujours ouvert dans `memory/questions.md` : **101 jours**.

## 1. Synthèse

Semaine de consolidation après la restructuration du 2026-10-12. Six mouvements principaux :

1. **Consolidation de la famille `/systeme/*` sur une seule URL `noindex`.** `/systeme/` sort du sitemap et bascule en 301 vers `/systeme-seo/` (hors sitemap, `noindex, follow`). `/systeme-seo-ia/` fait de même (301 → `/systeme-seo/`). Les trois variantes servent désormais le même HTML (4161 mots) via la même URL finale désindexée. Lecture : Google va suivre le 301 jusqu'à une page `noindex` et retirer `/systeme/` de l'index. **Décision assumée côté template.**
2. **+1 URL au sitemap : `/consultant-seo-saas/`** (1 821 mots, 46 inbound nav-linkée dès l'entrée). Pattern cohérent avec les 3 landings geo entrées au sitemap les semaines précédentes.
3. **Enrichissement éditorial généralisé.** 17 pages du sitemap sur 31 gagnent ≥ 90 mots de contenu dans le HTML servi. `/consultant-geo/` passe de 1 642 à 3 570 mots (+1 928) **et** de 2 à 48 inbound. L'URL était chronique de sous-maillage, elle est maintenant nav-linkée.
4. **Maillage total `<a>` sitemap→sitemap : 613 arêtes** (vs 513 au 2026-10-12, **+100 arêtes en 7 jours**). Confirme un passage éditorial global.
5. **Orphelines strict `<a>` stables à 5/31** : exactement les 5 chroniques du 2026-10-12. Aucune n'a reçu de lien `<a>` entrant cette semaine.
6. **`/audit-seo/` rebondit : 123 mots** (vs 47 au 2026-10-12, vs 90 au 2026-10-05). Trajectoire cassée. Reste orpheline strict.

Autres signaux :

- **Sitemap 31 URLs**. Trajectoire 129j : `169-136-143-143-146-146-330-330-332-333-334-334-142-91-91-88-28-29-30-30-31-`**`31`**.
- **`/methode/` et `/bootcamp/` toujours HTTP 410** + `x-robots-tag: noindex`. **2e récurrence, 14 jours**. Signalétique de retrait stable.
- **`/manifeste{,/}` toujours 404** avec `meta robots: noindex` sur la page d'erreur. **18e récurrence, 131 jours** depuis la reco P1 du 2026-06-10.
- **`lastmod_uniforme`** : 31/31 URLs partagent `2026-10-19T06:05:37.123Z`. **22e récurrence, 131 jours**.
- **`/tarifs/`** toujours hors sitemap avec `index, follow` et 5 inbound (vs 3 au 2026-10-12). **9e récurrence, 51 jours**.
- **`/systeme-seo/`** : 77 inbound depuis le sitemap (vs 74 au 2026-10-12). **3e récurrence**, poursuite du canal nav vers une URL `noindex`.
- **Couche B morte 10e run consécutif**. `urlInspection` : 101 jours.
- **Blog** : 0 nouveau 301 cette semaine. 1/8 slugs toujours 301 (`9-skills-seo-claude → /skills/`), 7/8 toujours 404 nu. **6e récurrence**.

**Chiffres du run.** 31/31 HTTP 200 direct (0 redirect dans le sitemap). 31/31 avec `<title>`, `<h1>` et `<link rel=canonical>` auto-référent égal à la `<loc>`. **26/31** avec `<meta name="robots">` explicite `index, follow` ; 5 sans meta (`/agent-seo/`, `/en/agent-seo/`, `/skills/`, les 2 guides `.html` — famille gabarit léger stable depuis 4 runs). **0 `noindex` sur balise dans le sitemap**. `robots.txt` inchangé (`User-Agent:* / Allow:/ + Sitemap`). Graphe interne reconstruit sur 31 HTML téléchargés : **613 arêtes `<a>` inbound vers URLs du sitemap** (hors self-ref). **27/31 title ≠ h1** après nettoyage du suffixe nom de site (identique au 2026-10-12).

## 2. Anomalies critiques

### C1. Consolidation `/systeme/*` : 3 variantes convergent vers une URL `noindex`

- `/systeme/` : passe de HTTP 200 dans le sitemap (378 mots, 1 inbound au 2026-10-12) à **HTTP 301** cette semaine, location `/systeme-seo/`. **Retiré du sitemap**.
- `/systeme-seo-ia/` : HTTP 200 noindex, follow au 2026-10-12 (hors sitemap). Cette semaine, **HTTP 301** également vers `/systeme-seo/`.
- `/systeme-seo/` : HTTP 200, `noindex, follow`, hors sitemap. **77 inbound depuis le sitemap** (vs 74). 4 161 mots.
- Les trois URLs servent désormais le même HTML (4 161 mots) via la même URL finale désindexée.
- Lecture système : décision assumée de consolider toute la famille produit « système SEO » sur une seule landing que Google n'indexera pas. Logique conversion-first qui absorbe le PageRank interne (77 inbound = plus que n'importe quelle page nav sauf la home).
- **Point de vigilance** : `/systeme/` était dans le sitemap depuis au moins le 2026-09-07 (donc probablement indexée). Google va suivre le 301 jusqu'à `/systeme-seo/`, voir `noindex`, et retirer de l'index. Si `/systeme/` portait des impressions mesurées, elles vont tomber.
- Non mesurable sans `urlInspection` + `searchAnalytics`.

### C2. `/consultant-seo-saas/` entre au sitemap, pattern geo-landing continu

- HTTP 200, canonical auto-ref, `index, follow`.
- **1 821 mots**, title = « Consultant SEO SaaS : inscriptions, démos, revenus », h1 = « Consultant SEO SaaS pour trouver des utilisateurs ».
- **46 inbound nav-linkée** dès son entrée au sitemap (confirmation du pattern geo-landing : la page apparaît déjà dans la nav globale au moment où elle entre).
- 4e landing geo/vertical entrée au sitemap en 4 semaines : `/consultant-seo-geo-lyon/`, `/consultant-seo-lyon/`, `/consultants-seo/`, `/consultant-seo-saas/`.
- Lecture : programme éditorial actif, dédié aux requêtes commerciales ciblées. Chaque entrée arrive déjà intégrée nav, pas de phase « orpheline en période de rodage ».

### C3. `/manifeste{,/}` 404 — 18e récurrence (131 jours), signal cumulatif

- HTTP 404 sur les deux variantes avec et sans slash. Page d'erreur sert `<title>` vide, `<h1>404</h1>`, `<meta name="robots" content="noindex"/>`. Pas de soft 404.
- 0 lien `<a>` entrant depuis les 31 pages du sitemap. Toujours hors du blanket wiki 301.
- Reco P1 du 2026-06-10 (301 vers `/systeme/` ou 410 documenté) non appliquée depuis **131 jours**.
- Note couplée C1 : désormais `/systeme/` n'est plus une cible 301 valide (elle-même 301 vers `/systeme-seo/`). La reco P1 doit être réécrite : soit 301 `/manifeste/` directement vers `/systeme-seo/`, soit 410 (le site sait émettre du 410 propre, cf. preuve posée au 2026-10-12).

### C4. `/audit-seo/` rebondit à 123 mots — trajectoire cassée, reste orpheline

- `/audit-seo/` (dans sitemap) : **123 mots** dans le HTML servi (vs 47 au 2026-10-12, 90 au 2026-10-05, 80 au 2026-09-28). Trajectoire : **80 → 90 → 47 → 123** en 4 semaines, pente négative cassée.
- Toujours 0 lien `<a>` interne entrant depuis les 31 pages du sitemap. Canonical auto-ref. `index, follow`.
- `/audit/` (hors sitemap) : 309 mots dans le HTML servi (vs 255), **63 liens `<a>` entrants** (vs 57), canonical auto-ref, pas de meta robots. Nav globale.
- Le split persiste mais `/audit-seo/` reçoit du contenu éditorial au lieu de perdre. Deux lectures :
  - **Réinvestissement éditorial** : la page est maintenue, le wordcount remonte, à terme peut rejoindre `/audit/` ou devenir la version indexable canonique.
  - **Simple rebond** : le gabarit a été corrigé mais la famille `/audit*` reste doublée (une dans sitemap sans nav, une hors sitemap avec nav).
- `pred-2026-10-12-audit-seo-wordcount` (prédiction : ≤ 100 au 2026-10-19) : **MISS**. 123 mots mesurés. Erreur de prédiction logguée en mistakes.
- `pred-2026-10-12-audit-split` (prédiction continuation du split) : **HIT** (le split persiste).

### C5. `/systeme-seo/` : 77 inbound vers URL `noindex`, canal nav stable

- HTTP 200, 4 161 mots, canonical auto-ref, `noindex, follow` confirmé sur balise.
- **77 liens `<a>` entrants depuis le sitemap** (vs 74 au 2026-10-12). Hors sitemap.
- Désormais, 2 autres URLs (`/systeme/` et `/systeme-seo-ia/`) redirigent 301 vers elle (cf. C1). Donc tout linkjuice interne du territoire « système » converge sur une URL désindexée.
- Lecture confirmée (contexte C1) : **intentionnel**. Landing conversion volontairement désindexée, absorbant PageRank interne et laissant les URLs sitemap sans concurrence côté index. Trade-off : le site renonce à l'indexation de cette offre pour maximiser la conversion sur le canal direct.
- `pred-2026-10-12-systeme-seo-noindex` (prédiction ≥ 60 inbound + `noindex, follow`) : **HIT**. 77 mesurés.

### C6. Orphelines strict : 5/31 pages du sitemap à 0 lien `<a>` entrant — 5e récurrence stable

Comptage strict sur `<a href>`, `<link rel="alternate">` exclu. Mêmes 5 pages qu'au 2026-10-12 :

| URL | Récurrence | Jours observés | Mots | Note |
|-----|-----------|-----------------|------|------|
| `/audit-seo/` | 5e | 26 | 123 | Thin content qui rebondit, cf. C4 |
| `/en/agent-seo/` | 5e | 26 | 3 368 | Hreflang bidirectionnel détecté, 0 lien `<a>` éditorial |
| `/guides/audit-seo-technique-claude.html` | 5e | 26 | 5 329 | Hub `/guides/` ne lie que PDF + pages site (M3) |
| `/guides/en/audit-seo-technique-claude.html` | 5e | 26 | 5 162 | Idem |
| `/plan-du-site/` | 7e | 35 | 151 | Hub maillant mais lui-même orphelin |

- `pred-2026-10-12-orphans-5pages` : **HIT**. Les 5 restent à 0 inbound strict.
- Observation : les 4 pages sorties de la zone 0-inbound au 2026-10-12 (via l'enrichissement de `/plan-du-site/`) sont **restées hors zone 0** cette semaine. L'enrichissement a tenu. 3 d'entre elles ont même gagné du maillage nav direct : `/consultant-geo/` (2 → 48), `/consultant-lead-seo/` (?), `/accompagnement-seo-geo/` (1 → 1 — stable).

### C7. `lastmod_uniforme` 31/31 — 22e récurrence (131 jours), 3 variantes `/systeme/*` ignorées

- `grep -c '<lastmod>2026-10-19T06:05:37.123Z</lastmod>' sitemap.xml` = 31.
- `grep -c '<lastmod>' sitemap.xml` = 31. **1 seul `lastmod` distinct**.
- Impact spécifique de cette semaine : `/consultant-seo-saas/` entre au sitemap avec le même `lastmod` que les 30 autres pages, incluant les 17 pages qui ont reçu +90 à +1 928 mots d'édition. Google ne reçoit aucun signal « 3 pages fortement modifiées cette semaine ».
- Le sitemap continue d'émettre l'horodatage de build à la place du lastmod éditorial par URL. Signal fraîcheur perdu depuis 131 jours.

### C8. Couche B non testable — 10e run consécutif, `urlInspection` ouvert 101 jours

- Témoin obligatoire relancé : organikk répond HTTP 404 sur URL inexistante, Google renvoie HTTP 200 / 92 765 octets sans SERP exploitable sans JS. 0 marqueur de blocage recaptcha, 1 occurrence du domaine (écho requête).
- Conséquence directe : impossible de mesurer (a) si Google a déjà retiré `/methode/` et `/bootcamp/` de son index après 14 jours de 410, (b) si la bascule 301 de `/systeme/` et `/systeme-seo-ia/` vers une page `noindex` a été prise en compte, (c) si l'index sert encore les 7 URLs `/blog/*` 404 nu.
- Diff `urlInspection` dans `memory/questions.md` : **101 jours d'ouverture**. Impact lourd sur 5 anomalies critiques (C1, C3, C4, C5, C9).

### C9. `/blog/*` 404 nu — 6e récurrence, 0 nouveau 301 cette semaine

- `curl -sI https://organikk.co/blog{,/}` : HTTP 404 nu. Racine blog toujours sans page.
- 8 slugs articles-poteaux retestés : **1/8 redirigé** (`9-skills-seo-claude → 301 → /skills/`, stable depuis le 2026-10-05, **3 semaines**), **7/8 toujours 404 nu** (`process-seo-b2b-2026`, `information-gain-geo`, `wiki-ia-obsidian-claude`, `audit-seo-technique`, `aeo-geo`, `seo-chatgpt`, `maillage-interne-seo`).
- `pred-2026-10-12-blog-cadence` (prédit « au plus 1 nouvelle 301 ») : **HIT** (0 nouvelle 301 mesurée).
- Cadence réelle : 1 URL traitée en 4 semaines. Reco P2 (décision URL par URL) toujours ouverte.
- Rappel C1 : le site sait émettre du 410 propre (preuve 2026-10-12). Le choix d'un 404 nu sur 7+ URLs plutôt qu'un 410 (ressource retirée) ou un 301 (contenu équivalent) reste à documenter.

## 3. Anomalies mineures

### M1. Pages hors sitemap servies en 200, 301 ou 410 — 10 URLs identifiées

| URL | HTTP | meta robots | Inbound sitemap | Récurrence | Note |
|-----|------|-------------|-----------------|------------|------|
| `/tarifs/` | 200 | `index, follow` | 5 (vs 3) | 9e, 51 j | Page conversion, inbound augmente mais toujours hors sitemap |
| `/audit/` | 200 | (absent) | 63 (vs 57) | 5e | Nav globale, cf. C4 |
| `/systeme-seo/` | 200 | `noindex, follow` | 77 (vs 74) | 3e | Cf. C1, C5 |
| `/systeme-seo-ia/` | 301 | — | 0 strict | 5e | **Nouvelle 301** → `/systeme-seo/`. Était HTTP 200 noindex au 2026-10-12 |
| `/systeme-ia/` | 200 | `index, follow` | 1 | 2e | Variante produit, maintenue indexable |
| `/systeme/` | 301 | — | 0 strict | 1re | **Nouvelle 301** → `/systeme-seo/`. **Retrait du sitemap**. Était dans sitemap au 2026-10-12 (378 mots, 1 inbound) |
| `/communaute-seo/` | 200 | `noindex, nofollow` | 1 | 2e | Désindexée volontairement par balise + nofollow |
| `/etudes-de-cas/appart-hotel/` | 200 | `index, follow` | 2 | 2e | Cas client, pas intégrée nav |
| `/methode/` | 410 | `x-robots-tag: noindex` | 0 | 2e | 14 jours de 410 stable |
| `/bootcamp/` | 410 | `x-robots-tag: noindex` | 0 | 2e | 14 jours de 410 stable |

Nouveauté de la semaine : 2 URLs supplémentaires rejoignent la famille des 301 vers `/systeme-seo/` (consolidation C1).

### M2. `/plan-du-site/` : hub maillant mais toujours orphelin lui-même, 7e récurrence

- Hub actif (ancres sortantes vers l'ensemble du sitemap + les hors-sitemap tolérés).
- 151 mots dans le HTML servi (vs 87 au 2026-10-12 — doublement).
- **0 lien `<a>` entrant** depuis les 31 pages du sitemap. Reste accessible uniquement via sitemap et redirect blanket wiki.
- Reco (poser 1 ancre nav vers `/plan-du-site/` dans le footer) toujours ouverte.

### M3. `/guides/` hub : 0 lien vers les 2 `.html` du sitemap — 5e récurrence

- Extraction `<a href>` de `/guides/` : 7 PDF + 11 pages du site.
- **0 lien** vers les 2 pages `.html` qui sont dans le sitemap. Les 2 `.html` cumulent 10 491 mots servis (5 329 FR + 5 162 EN, en hausse de ~ +170 mots chacune cette semaine).
- Prédiction `pred-2026-10-12-guides-hub` : HIT (par continuité du 2026-10-05, à défaut d'avoir été re-posée explicitement cette semaine).
- 2 options restent cohérentes : soit ajouter 2 ancres `<a href>` dans `/guides/` vers chaque `.html`, soit retirer les 2 `.html` du sitemap.

### M4. Meta robots hétérogène — 5 pages sans meta (5e récurrence)

- 26/31 pages portent `<meta name="robots" content="index, follow">`.
- 5 sans meta : `/agent-seo/`, `/en/agent-seo/`, `/skills/`, `/guides/audit-seo-technique-claude.html`, `/guides/en/audit-seo-technique-claude.html`. Absence = indexable par défaut.
- Mapping stable : exactement la famille de gabarit léger. Marqueur de gabarit, pas anomalie en soi.

### M5. Title vs h1 divergents 27/31 — 5e récurrence stable

- Après nettoyage du suffixe nom de site, **27/31** titles diffèrent de leur h1 (identique au 2026-10-12).
- Les 4 égalités : `/consultant-seo-lyon/`, `/consultants-seo/`, `/mentions-legales/`, `/politique-confidentialite/`. **Même mapping qu'au 2026-10-12** malgré l'arrivée de `/consultant-seo-saas/` (title = « Consultant SEO SaaS : inscriptions, démos, revenus » ≠ h1 = « Consultant SEO SaaS pour trouver des utilisateurs »).
- Pattern lisible : title = requête commerciale ciblée, h1 = accroche narrative. Décision éditoriale cohérente.

## 4. Points méthode / faux positifs

### P1. Grep plein texte `noindex` — faux positif attendu, 5e récurrence

- `grep -i noindex` matche 4/31 pages : `/agent-seo/`, `/en/agent-seo/`, `/guides/audit-seo-technique-claude.html`, `/guides/en/audit-seo-technique-claude.html`. Copie éditoriale SEO qui parle de la directive, pas directive effective.
- Vérification balise par balise : **0 directive `noindex` réelle** sur ces 4 pages.
- Rien de nouveau depuis 2026-09-23.

### P2. Méthode durcie confirmée — compteur orphelines sur `<a href>` seul

- 613 arêtes `<a>` inbound sitemap vs 513 au 2026-10-12. Méthode stable, pas de régression.
- Les 5 orphelines strict restent orphelines (confirmé 5e semaine). Pas d'autre page avec `<link rel="alternate" hreflang>` discordant.
- Durcissement P2 reste à inscrire dans le skill (`memory/questions.md` section Q5).

### P3. Catégorie « retrait assumé » (410) — à distinguer de « 404 nu » dans le checker

- 2e semaine de mesure 410. Les deux URLs concernées (`/methode/`, `/bootcamp/`) sont stables : HTTP 410, `x-robots-tag: noindex`, `content-type: text/plain`. 0 régression vers 404 nu, 0 reconstitution en 200.
- Confirme la demande d'ouvrir dans le skill une catégorie « retrait assumé » distincte de « 404 nu ».

## 5. Résolution des prédictions du 2026-10-12 (resolve_by 2026-10-19)

| ID | Verdict | Détail |
|---|---|---|
| `pred-2026-10-12-manifeste-404` | HIT | 18e récurrence, 131 jours sans action |
| `pred-2026-10-12-410-stable` | HIT | `/methode/` et `/bootcamp/` toujours 410 + `x-robots-tag: noindex`, 14 jours stable |
| `pred-2026-10-12-audit-seo-wordcount` | **MISS** | Prédit ≤ 100 mots, mesuré **123 mots** (rebond de 47 → 123). Mistake logguée |
| `pred-2026-10-12-tarifs-sitemap` | HIT | 9e récurrence, `/tarifs/` toujours hors sitemap |
| `pred-2026-10-12-lastmod-uniforme` | HIT | 31/31 lastmod uniforme, 22e récurrence |
| `pred-2026-10-12-orphans-5pages` | HIT | Les 5 orphelines strict identiques au run précédent, 0 inbound strict |
| `pred-2026-10-12-systeme-seo-noindex` | HIT | 77 inbound (prédit ≥ 60) + `noindex, follow` confirmé |
| `pred-2026-10-12-blog-cadence` | HIT | 0 nouveau 301 cette semaine (prédit « au plus 1 ») |
| `pred-2026-10-12-strategie-b2b-maillage` | HIT | `/strategie-seo-b2b/` à 3 inbound (prédit ≤ 5) |

**Score : 8 HIT / 1 MISS.** Mistake unique : trajectoire thin content non monotone.

## 6. Recommandations priorisées

**P1 — Rechaîner la reco `/manifeste/` sur `/systeme-seo/` ou poser un 410.**
- Depuis la consolidation C1, `/systeme/` n'est plus une cible 301 valide (elle-même 301). La reco P1 ouverte depuis 131 jours doit être réécrite : soit 301 `/manifeste/` → `/systeme-seo/`, soit 410 (preuve de faisabilité posée au 2026-10-12 : le site sait émettre un 410 propre).
- Choix binaire à documenter côté éditorial avant d'instrumenter.

**P1 — Trancher `/audit-seo/` (123 mots, orpheline 5e récurrence).**
- Le rebond de wordcount suggère un réinvestissement éditorial, mais la page reste orpheline strict et doublée par `/audit/` qui porte 63 inbound nav. Options :
  - **Garder `/audit-seo/`** et poser 2-3 ancres éditoriales depuis les landings commerciales (`/consultant-seo-lyon/`, `/consultant-seo-saas/`, `/strategie-seo-b2b/`) pour la sortir du zéro-maillage.
  - **Retirer `/audit-seo/` du sitemap** et poser 301 vers `/audit/` (`/audit/` n'a pas de meta robots donc est indexable par défaut).
- La semaine qui vient dira si le wordcount continue à monter (réinvestissement) ou retombe (gabarit instable).

**P1 — Décider sur `/tarifs/` (51 j hors sitemap, 5 inbound).**
- 5 inbound mesurés cette semaine (vs 3 au 2026-10-12), toujours hors sitemap depuis 51 jours, HTTP 200 `index, follow`. Signal de maintenance active (inbound monte, contenu stable à 857 mots) sans l'étape ajout sitemap.
- Deux options : ajouter au sitemap si la page est maintenue (le signal nav indique qu'elle l'est), ou poser 301 vers `/consultant-seo-lyon/` ou `/consultant-seo-saas/` sinon.

**P2 — Documenter la consolidation `/systeme/*` et préparer le post-mortem.**
- `/systeme/` était indexée (dans sitemap jusqu'au 2026-10-12). La bascule 301 → `/systeme-seo/` (noindex) va provoquer le retrait de l'index au prochain crawl.
- Préparer : (a) relever les impressions/clics de `/systeme/` sur les 90 derniers jours avant qu'elles ne tombent (nécessite `searchAnalytics`), (b) documenter dans le repo la logique « landing conversion volontairement désindexée », (c) décider si une URL de remplacement indexable doit être poussée (ex. `/systeme-ia/` qui est à `index, follow` et à 710 mots).

**P2 — Propager le pattern 410 aux cas déjà identifiés.**
- `/methode/` et `/bootcamp/` ont 2 semaines de 410 stable. Appliquer le même traitement à `/manifeste{,/}` (cf. P1) et éventuellement aux 7 `/blog/*` 404 nu.
- Pour les 7 `/blog/*`, choisir URL par URL entre 410 (contenu retiré) et 301 (contenu équivalent). Le pattern `9-skills-seo-claude → /skills/` montre que l'option 301 unitaire est faisable mais a été appliquée une seule fois en 4 semaines.

**P3 — Signal fraîcheur.**
- `lastmod_uniforme` (C7) : émettre le `lastmod` éditorial par URL au lieu de l'horodatage de build. 131 jours de perte de signal, aggravé cette semaine par 17 pages fortement enrichies qui portent toutes la même date que les 14 autres. Priorité réaffirmée.

**P4 — Méthode boucle (Tim tranche).**
- Diff `urlInspection` du 2026-07-10 dans `memory/questions.md` : **101 jours**. Sans ça, 5 anomalies critiques de ce run restent côté sortie (C1, C3, C4, C5, C8) sans mesure de l'effet Google.
- Durcissement P2 (compteur orphelines sur `<a href>` strict) : inscrire dans le skill. Comportement stable depuis 3 runs, décision formelle attendue.
- Catégorie « retrait assumé » (410) distincte de « 404 nu » : à ouvrir dans le checker (2e run avec mesure stable).

## 7. Nouvelles prédictions (resolve_by 2026-10-26)

- `pred-2026-10-19-manifeste-404` : `/manifeste{,/}` encore HTTP 404 au run du 2026-10-26 (19e récurrence).
- `pred-2026-10-19-410-stable` : `/methode/` et `/bootcamp/` toujours HTTP 410 + `x-robots-tag: noindex` au run du 2026-10-26 (3e récurrence).
- `pred-2026-10-19-systeme-301` : `/systeme/` et `/systeme-seo-ia/` toujours HTTP 301 → `/systeme-seo/` au run du 2026-10-26 (2e récurrence attendue).
- `pred-2026-10-19-tarifs-sitemap` : `/tarifs/` restera hors sitemap au run du 2026-10-26 (10e récurrence).
- `pred-2026-10-19-lastmod-uniforme` : 31+/31+ URLs sitemap partageront un unique `<lastmod>` au run du 2026-10-26 (23e récurrence).
- `pred-2026-10-19-orphans-5pages` : les 5 orphelines strict `<a>` de C6 resteront à 0 inbound strict au run du 2026-10-26.
- `pred-2026-10-19-systeme-seo-inbound` : `/systeme-seo/` restera `noindex, follow` + ≥ 70 inbound depuis le sitemap au run du 2026-10-26 (4e récurrence).
- `pred-2026-10-19-blog-cadence` : au plus 1 nouvelle URL `/blog/*` passera en 301 d'ici le 2026-10-26 (cadence 0-1/semaine confirmée sur 4 semaines).
- `pred-2026-10-19-audit-seo-wordcount` : `/audit-seo/` restera dans le sitemap avec un wordcount compris entre 50 et 250 mots au run du 2026-10-26 (nouvelle fourchette post-rebond).
- `pred-2026-10-19-sitemap-size` : sitemap entre 30 et 33 URLs au run du 2026-10-26 (cadence +1/semaine observée depuis 2026-10-05).

## 8. Limites du rapport

- **Statut d'indexation Google réel** : non testable. Pas d'accès à `urlInspection` ni `searchAnalytics`. Les 31 URLs du sitemap peuvent toutes être indexées ou pas, aucun chiffre n'est donné dans ce rapport sur ce point.
- **Trafic organique mesuré** : non accessible. Les bascules C1 (`/systeme/` → `/systeme-seo/` noindex) et le rebond C4 (`/audit-seo/`) seraient à qualifier par leurs impressions sur les 90 derniers jours, non mesurées ici.
- **Rendu client-side** : le HTML servi est le HTML initial (`curl -sL`). Les pages à 102-187 mots (`/skills/`, `/consultants-seo/`, `/audit-seo/`, `/plan-du-site/`) portent peut-être du contenu complémentaire injecté en JS. Hypothèse ouverte depuis 2026-09-07, non tranchée.
- **Actions manuelles et sécurité** : non vérifiées (Search Console inaccessible).
- **Backlinks externes** : non mesurés. Les URLs qui basculent cette semaine (`/systeme/`, `/systeme-seo-ia/` passées en 301 vers `noindex`) peuvent porter du linkjuice externe redirigé vers une page désindexée.
