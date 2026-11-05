---
type: audit
title: Indexation Organikk - audit hebdomadaire 2026-10-12
created: 2026-10-12
updated: 2026-10-12
tags: [indexation, sitemap, audit, organikk, hebdo]
status: stable
confidence: high
sources: 3
---

# Audit indexation Organikk - 2026-10-12

**Périmètre.** organikk.co, 31 URLs listées dans `sitemap.xml` (delta +1 vs 30/09-10-05 ; +3 entrées, -2 sorties). Lecture seule sur le web public. Aucun forçage d'indexation.

**Sources de vérité utilisées.**
- Statut HTTP `curl -sIL` (code final + chaîne de redirections `redirect_url`).
- Présence dans `sitemap.xml` + `lastmod`.
- `robots.txt`.
- Parsing HTML servi : `<title>`, `<h1>` (balises enfants strippées), `<link rel=canonical>`, `<meta name=robots>`, graphe interne reconstruit à partir des seuls `<a href>` (hreflang `<link rel=alternate>` exclu, cf. durcissement P2 du 2026-10-05).

**Non testable.** Statut d'indexation Google réel. Pas d'accès à `urlInspection` / `searchAnalytics` (edge `admin-gsc-export`) dans cet environnement. Témoin obligatoire relancé ce run : `/cette-page-nexiste-absolument-pas-xyz1791789470/` renvoie HTTP 404 côté organikk, et Google `?q=site%3Aorganikk.co` renvoie HTTP 200 / 93 450 octets, 1 occurrence du domaine (écho de la requête), 0 marqueur recaptcha, texte visible = « Google Search » + payload JS, aucune SERP. Couche B non testable, **9e run consécutif**. Diff `urlInspection` du 10/07 toujours ouvert dans `memory/questions.md` : **94 jours**.

## 1. Synthèse

Semaine la plus structurelle depuis la restructuration du 2026-09-21. Quatre mouvements lourds, dont trois nouveaux marqueurs techniques :

1. **Premiers HTTP 410 Gone** sur ce domaine. `/methode/` et `/bootcamp/` sortent du sitemap et répondent 410 + `X-Robots-Tag: noindex`. Signal explicite de retrait vers Google, aucune 301 posée. `/methode/` portait 18 668 mots et 9 inbound il y a 7 jours.
2. **Trois URLs entrent au sitemap** : `/consultant-seo-lyon/` (3 770 mots, 48 inbound dès l'intro, nav-linkée), `/consultants-seo/` (95 mots, 44 inbound) et `/strategie-seo-b2b/` (2 941 mots, 3 inbound).
3. **Maillage de `/plan-du-site/` fortement enrichi**. Le hub ajoute cette semaine 15 ancres sortantes (vs 19 au 2026-10-05 ; passe à 41 sorties internes dont 33 sitemap). 4 orphelines sur 9 du run précédent résolues sur ce seul geste (`/accompagnement-seo-geo/`, `/consultant-geo/`, `/consultant-lead-seo/`, `/formation-seo-ia/` toutes au moins 1 inbound).
4. **Nav restructurée vers `/systeme-seo/` (hors sitemap, `noindex, follow`)** : 74 pages du sitemap sur 31 pointent dessus en strict `<a>` (vs 24 au 2026-10-05). Chaque page sitemap y lie 2 à 3 fois. L'URL que Google n'indexera jamais reçoit maintenant plus de linkjuice que la totalité de la nav.

Autres signaux :

- **Sitemap 30 → 31 URLs**. Trajectoire 122j : `169-136-143-143-146-146-330-330-332-333-334-334-142-91-91-88-28-29-30-30-`**`31`**.
- **`sitemap_canonical_mismatch` : fix tient (4e semaine).** 31/31 canonicals auto-référents strictement égaux à la `<loc>`.
- **Orphelines strict passent de 9 à 5** sur les URLs du sitemap (`-4`). Les 5 qui restent sont les mêmes chroniques : `/audit-seo/`, `/en/agent-seo/`, les 2 guides `.html`, `/plan-du-site/` lui-même.
- **`/audit-seo/` se dégrade** : 47 mots cette semaine, contre 90 au 2026-10-05 et 80 au 2026-09-28. Thin content qui empire, 0 lien `<a>` entrant, orpheline sitemap 4e récurrence.
- **`/manifeste{,/}` toujours 404** avec `meta robots: noindex` sur la page d'erreur. **17e récurrence, 124 jours** depuis la reco P1 du 10/07.
- **`lastmod_uniforme`** : 31/31 URLs partagent `2026-10-12T05:36:08.198Z`. **21e récurrence, 124 jours**. Le sitemap émet toujours l'horodatage de build à la place du lastmod éditorial par URL.
- **Couche B morte 9e run consécutif**. `urlInspection` : 94 jours.

**Chiffres du run.** 31/31 HTTP 200 direct (0 redirect dans le sitemap). 31/31 avec `<title>`, `<h1>` et `<link rel=canonical>` auto-référent égal à la `<loc>`. **26/31** avec `<meta name="robots">` explicite `index, follow` ; 5 sans meta (`/agent-seo/`, `/en/agent-seo/`, `/skills/`, les 2 guides `.html`, famille gabarit léger stable depuis 3 runs). **0 `noindex` sur balise dans le sitemap**. `robots.txt` inchangé (`User-Agent:* / Allow:/ + Sitemap`). Graphe interne reconstruit sur 31 HTML téléchargés : **513 arêtes `<a>` inbound vers URLs du sitemap** (hors self-ref). **27/31 title ≠ h1** après nettoyage du suffixe nom de site (26/30 au 2026-10-05 ; les 2 nouvelles pages du sitemap qui ont title=h1 : `/consultant-seo-lyon/` et `/consultants-seo/`).

## 2. Anomalies critiques

### C1. Premier retrait assumé via 410 Gone sur `/methode/` et `/bootcamp/`

- `curl -sI https://organikk.co/methode/` : **HTTP 410**, `content-type: text/plain; charset=utf-8`, `x-content-type-options: nosniff`, **`x-robots-tag: noindex`**. Idem pour `/bootcamp/`.
- Les deux URLs étaient dans le sitemap au 2026-10-05. `/methode/` portait 18 668 mots, 9 inbound depuis le sitemap, canonical `https://organikk.co/methode/` (données du tsv du 2026-10-05).
- Aucune 301 posée vers une page de remplacement. La 410 est le signal explicite « cette ressource existait et a été retirée », asymétrique du 404 (« inconnue »).
- Lecture : décision éditoriale assumée. Google retirera les deux URLs de l'index au prochain crawl. 410 reste la bonne réponse si aucune page ne reprend précisément le même contenu.
- Interprétation côté système : le site sait **émettre** du 410 (preuve technique faite ce run), donc l'absence de 410 ou 301 sur `/manifeste` depuis 124 jours (C3) devient un choix d'inaction, plus un blocage technique.
- **Point de vigilance** : si ces deux pages portaient du trafic organique mesuré (impressions > 0 sur les 90 derniers jours), relever les ancres entrantes externes avant que l'index ne se nettoie. Non mesurable sans `urlInspection` + `searchAnalytics`.

### C2. Trois URLs entrent au sitemap, dont une à 95 mots

- **`/consultant-seo-lyon/`** : HTTP 200, 3 770 mots, 48 liens `<a>` entrants depuis le sitemap, canonical auto-ref, `index, follow`, title = h1 = « Consultant SEO à Lyon ». Nav-linkée dès son entrée.
- **`/strategie-seo-b2b/`** : HTTP 200, 2 941 mots, 3 inbound (depuis `/plan-du-site/`, `/consultant-seo-lyon/` et une 3e), canonical auto-ref, `index, follow`. Pas de maillage nav, uniquement liée par hub + éditorial sur 2 pages voisines.
- **`/consultants-seo/`** : HTTP 200, **95 mots**, 44 inbound (nav globale), canonical auto-ref, `index, follow`, title = h1 = « Agence de consultants SEO ». 95 mots sur une page nav-linkée = thin content servie **par défaut** du gabarit, le texte éditorial n'est pas descendu dans le HTML initial.
- Lecture : les 3 pages suivent la trajectoire déjà vue pour `/consultant-seo-geo-lyon/` fin septembre (geo-specific landing poussée au sitemap). Deux sur trois correctement rédigées. `/consultants-seo/` à 95 mots partage le même gabarit que `/skills/` (54 mots, 28 inbound, meta robots absente) et `/audit-seo/` (47 mots, 0 inbound) : famille de pages servies vides et probablement complétées en client-side (hypothèse rendu Next.js ouverte depuis 2026-09-07, jamais tranchée).

### C3. `/manifeste{,/}` 404 - 17e récurrence (124 jours), preuve de faisabilité posée ce run

- HTTP 404 sur les deux variantes avec et sans slash. Page d'erreur sert `<title>` vide, `<h1>404</h1>`, `<meta name="robots" content="noindex"/>` : page d'erreur propre, pas de soft 404.
- 0 lien `<a>` entrant depuis les 31 pages du sitemap. Toujours hors du blanket wiki 301.
- Reco P1 du 10/07 (301 vers `/systeme/` ou 410 documenté) non appliquée depuis **124 jours**.
- Le run de cette semaine prouve que le site sait émettre du 410 propre (cf. C1). L'absence d'arbitrage sur `/manifeste` depuis 124 jours est donc un choix d'inaction, pas un blocage technique.

### C4. `/audit-seo/` thinne de 90 à 47 mots en 7 jours - 4e récurrence du split

- `/audit-seo/` (dans sitemap) : 47 mots dans le HTML servi (vs 90 au 2026-10-05, 80 au 2026-09-28). Trajectoire : **80 → 90 → 47 mots en 3 semaines**, pente négative accentuée. 0 lien `<a>` interne entrant. Canonical auto-ref. `index, follow`.
- `/audit/` (hors sitemap) : 255 mots dans le HTML servi, **57 liens `<a>` entrants** (vs 26 au 2026-10-05), canonical auto-ref, **pas de meta robots** (indexable par défaut). Nav globale sur l'ensemble du site.
- Le split s'intensifie : le site redirige activement toute sa nav interne vers `/audit/` tout en laissant `/audit-seo/` dans le sitemap avec un HTML qui perd du contenu chaque semaine. Hypothèse la plus probable : erreur de build qui réémet `/audit-seo/` au sitemap alors que l'URL n'a plus de contenu éditorial attribué.
- `pred-2026-09-23-audit-split` (resolve 2026-10-23) : **HIT par anticipation**. 11 jours restants, le couple est intact.
- Prédiction `pred-2026-10-05-audit-split` : HIT.

### C5. `/systeme-seo/` : nav restructurée, 74 inbound de pages sitemap vers une URL `noindex`

- HTTP 200, 723 848 octets servis (vs 581 044 au 2026-10-05, **+25 %**). `<meta name="robots" content="noindex, follow"/>` confirmé sur balise. Canonical auto-ref.
- **74 liens `<a>` entrants depuis le sitemap** (vs 24 au 2026-10-05). Chaque page du sitemap pointe en moyenne 2,4 fois vers `/systeme-seo/` (nav + ancres contextuelles).
- Hors sitemap. Donc Google ne l'indexera pas, mais 80 % du linkjuice interne du site y est désormais acheminé.
- Deux lectures possibles, à trancher avec Tim :
  - **Intentionnel** : landing conversion volontairement désindexée, qui absorbe PageRank interne et laisse `/systeme/` (dans sitemap, 378 mots, 1 inbound) sans concurrence côté index. Problème : `/systeme/` reçoit **1 inbound** et `/systeme-seo/` en reçoit **74**, donc Google va mesurer que `/systeme/` est éditorialement enterrée par rapport à `/systeme-seo/`.
  - **Reliquat** : nav pas mise à jour quand `/systeme/` a été poussée comme canonique. Dans ce cas, poser une 301 `/systeme-seo/` → `/systeme/` récupère l'autorité interne et aligne nav + sitemap.
- `pred-2026-10-05-systeme-seo-noindex` : **HIT** (prédit ≥ 20 pages, mesuré 74).

### C6. Orphelines strict : 5/31 pages du sitemap à 0 lien `<a>` entrant

Comptage strict sur `<a href>`, `<link rel="alternate">` exclu. Résultat passe de 9 à 5 pages (**-4**) :

| URL | Récurrence | Jours observés | Mots | Note |
|-----|-----------|-----------------|------|------|
| `/audit-seo/` | 4e | 19 | 47 | Thin content en pente négative, cf. C4 |
| `/en/agent-seo/` | 4e | 19 | 3208 | Hreflang bidirectionnel détecté, 0 lien `<a>` éditorial |
| `/guides/audit-seo-technique-claude.html` | 4e | 19 | 5165 | Hub `/guides/` ne lie que les 7 PDF + pages site (M3) |
| `/guides/en/audit-seo-technique-claude.html` | 4e | 19 | 4991 | Idem |
| `/plan-du-site/` | 6e | 28 | 87 | Hub maillant mais lui-même orphelin, 1 inbound non sitemap (passe à 0 strict `<a>`) |

- 4 orphelines du 2026-10-05 résolues cette semaine grâce à `/plan-du-site/` élargi (confirme la cause commune : la hub nav n'adressait pas ces pages). `/accompagnement-seo-geo/` (1 inbound), `/consultant-geo/` (2), `/consultant-lead-seo/` (1), `/formation-seo-ia/` (1) sortent de la zone 0-inbound.
- Les 5 restantes sont les cas structurellement différents : thin content (`/audit-seo/`), variante EN (`/en/agent-seo/`), format `.html` (2 guides), hub lui-même (`/plan-du-site/`).
- `pred-2026-10-05-orphans-9pages` (prédiction : les 9 resteraient à 0) : **MISS**. 4 pages sur 9 sont sorties de la zone 0-inbound. Erreur de prédiction logguée en mistakes.

### C7. `lastmod_uniforme` 31/31 - 21e récurrence (124 jours)

- `grep -c '<lastmod>2026-10-12T05:36:08.198Z</lastmod>' sitemap.xml` = 31.
- `grep -c '<lastmod>' sitemap.xml` = 31. **1 seul `lastmod` distinct**.
- Le sitemap continue d'émettre l'horodatage de build à la place du lastmod éditorial par URL. Signal fraîcheur perdu depuis 124 jours, incluant les 3 pages ajoutées cette semaine (qui portent toutes `2026-10-12T05:36:08.198Z` au lieu de leur date de publication).
- Impact spécifique : les deux URLs retirées cette semaine (`/methode/` et `/bootcamp/` passées en 410) ne sont évidemment plus listées, mais aucune URL en revenant ne porte un lastmod distinct, donc Google n'a pas de signal « page récemment modifiée » pour prioriser le crawl des 3 nouvelles entrées.

### C8. Couche B non testable - 9e run consécutif, `urlInspection` ouvert 94 jours

- Témoin obligatoire relancé : organikk répond HTTP 404 sur URL inexistante, Google renvoie HTTP 200 sans SERP exploitable sans JS. 0 marqueur de blocage recaptcha, 1 occurrence du domaine (écho requête).
- Conséquence directe : impossible de mesurer si Google a déjà retiré `/methode/` et `/bootcamp/` de son index après la 410 (C1), ni si `/systeme-seo/` fuit effectivement du linkjuice sans retour (C5), ni si l'index sert encore des URLs `/blog/*` 404 (C9).
- Diff `urlInspection` dans `memory/questions.md` : **94 jours d'ouverture**. Impact lourd sur 4 anomalies de ce run (C1, C4, C5, C9).

### C9. `/blog/*` 404 nu - 5e run consécutif, aucun nouveau 301 cette semaine

- `curl -sI https://organikk.co/blog{,/}` : HTTP 404 nu. Racine blog toujours sans page.
- 8 slugs articles-poteaux retestés : **1/8 redirigé** (`9-skills-seo-claude` → 301 → `/skills/`, stable depuis le 2026-10-05), **7/8 toujours 404 nu** (`process-seo-b2b-2026`, `information-gain-geo`, `wiki-ia-obsidian-claude`, `audit-seo-technique`, `aeo-geo`, `seo-chatgpt`, `maillage-interne-seo`). Pas de nouveau 301 cette semaine.
- Prédiction `pred-2026-10-05-blog-cadence` (« au plus 1 nouvelle URL `/blog/*` passera en 301 ») : **HIT** (0 nouvelle 301 mesurée).
- Cadence réelle : 1 URL traitée en 3 semaines. Reco P2 (décision URL par URL) toujours ouverte.
- Note couplée C1 : le site sait émettre du 410, donc le choix d'un 404 nu sur 7+ URLs plutôt qu'un 410 (ressource existante retirée) ou un 301 (contenu équivalent présent) reste à documenter.

## 3. Anomalies mineures

### M1. Pages hors sitemap servies en 200 ou 410 - 7 URLs identifiées cette semaine (+3 nouvelles)

| URL | HTTP | meta robots | Inbound sitemap | Récurrence | Note |
|-----|------|-------------|-----------------|------------|------|
| `/tarifs/` | 200 | `index, follow` | 3 (vs 1) | 8e, 44 j | Page conversion, inbound augmente mais toujours hors sitemap |
| `/audit/` | 200 | (absent) | 57 (vs 26) | 4e | Nav globale, canonical auto-ref, cf. C4 |
| `/systeme-seo/` | 200 | `noindex, follow` | 74 (vs 24) | 2e | Cf. C5 |
| `/systeme-seo-ia/` | 200 | `index, follow` | (via /plan-du-site/) | 4e | Variante produit |
| `/systeme-ia/` | 200 | `index, follow` | (via /plan-du-site/) | 1re | **Découverte via hub élargi** |
| `/communaute-seo/` | 200 | `noindex, nofollow` | (via /plan-du-site/) | 1re | **Découverte**, désindexée volontairement par balise + nofollow |
| `/etudes-de-cas/appart-hotel/` | 200 | `index, follow` | (via /plan-du-site/) | 1re | **Découverte**, cas client probable |

Trois découvertes ce run via l'enrichissement de `/plan-du-site/` : `/systeme-ia/`, `/communaute-seo/`, `/etudes-de-cas/appart-hotel/`. `/communaute-seo/` est correctement signalée désindexable (`noindex, nofollow`). Les deux autres sont **servies 200 `index, follow` hors sitemap** : à arbitrer (indexation voulue ou pas).

### M2. `/plan-du-site/` : hub élargi mais toujours orphelin lui-même, 6e récurrence

- 41 ancres sortantes (vs 19 au 2026-10-05). Ajouts cette semaine : `/accompagnement-seo-geo/`, `/accompagnement-1-1-30-jours/`, `/consultant-geo/`, `/consultant-lead-seo/`, `/consultant-seo-lyon/`, `/consultants-seo/`, `/formation-seo-ia/`, `/strategie-seo-b2b/`, `/tarifs/`, `/systeme-seo/`, `/systeme-seo-ia/`, `/systeme-ia/`, `/communaute-seo/`, `/etudes-de-cas/appart-hotel/`.
- **N'adresse toujours pas** 3 URLs du sitemap : `/audit-seo/`, `/en/agent-seo/`, les 2 guides `.html`. Mapping exact des orphelines strict restantes de C6 (hors `/plan-du-site/` elle-même).
- Reco P1 (« couvrir les 5 commerciales ») partiellement appliquée : 4/5 des commerciales ajoutées en 1 geste. Confirme que l'enrichissement du hub était bien le levier à activer.
- Elle-même reste à 0 lien `<a>` entrant depuis les 31 pages du sitemap.

### M3. `/guides/` hub lie maintenant des pages site, mais toujours pas les 2 `.html` du sitemap

- Extraction `<a href>` de `/guides/` : 7 PDF + 11 pages du site (`/accompagnement-1-1-30-jours/`, `/audit/`, `/bootcamp-candidature/`, `/consultant-seo-geo-lyon/`, `/consultant-seo-lyon/`, `/consultants-seo/`, `/mentions-legales/`, `/politique-confidentialite/`, `/systeme-seo/`, `/agent-seo/`, `/skills/`).
- **0 lien** vers les 2 pages `.html` qui sont dans le sitemap. Les 2 `.html` cumulent 10 156 mots servis (5 165 FR + 4 991 EN).
- Prédiction `pred-2026-09-23-guides-hub` (resolve 2026-10-23) : **HIT par anticipation** (11 jours restants).
- Prédiction `pred-2026-10-05-guides-hub` : **HIT**.
- 2 options restent cohérentes : soit ajouter 2 ancres `<a href>` dans `/guides/` vers chaque `.html`, soit retirer les 2 `.html` du sitemap.

### M4. Meta robots hétérogène - 5 pages sans meta (4e récurrence)

- 26/31 pages portent `<meta name="robots" content="index, follow">`.
- 5 sans meta : `/agent-seo/`, `/en/agent-seo/`, `/skills/`, `/guides/audit-seo-technique-claude.html`, `/guides/en/audit-seo-technique-claude.html`. Absence = indexable par défaut, aucun risque `noindex` accidentel.
- Mapping stable : exactement la famille de gabarit léger (= pages qui portent aussi le thin content servi côté serveur ou la variante EN).
- Marqueur de gabarit, pas anomalie en soi.

### M5. Title vs h1 divergents 27/31 - pattern éditorial persistant, 4e récurrence

- Après nettoyage du suffixe nom de site, 27/31 titles diffèrent de leur h1 (26/30 au 2026-10-05).
- Les 4 égalités cette semaine : `/consultant-seo-lyon/`, `/consultants-seo/`, `/mentions-legales/`, `/politique-confidentialite/`.
- Pattern lisible : title = requête cible SEO, h1 = accroche narrative. Les 2 nouvelles pages (`/consultant-seo-lyon/`, `/consultants-seo/`) adoptent le pattern unifié title=h1 des pages dont le titre marketing est aussi le sujet unique. Décision éditoriale cohérente.

## 4. Points méthode / faux positifs

### P1. Grep plein texte `noindex` - faux positif attendu, 4e récurrence

- `grep -i noindex` matche 4/31 pages : `/agent-seo/` (5 occurrences), `/en/agent-seo/` (5), `/guides/audit-seo-technique-claude.html` (9), `/guides/en/audit-seo-technique-claude.html` (9). Copie éditoriale SEO qui parle de la directive, pas directive effective.
- Vérification balise par balise : **0 directive `noindex` réelle** sur ces 4 pages (meta robots absente ou `index, follow`, aucun header `X-Robots-Tag`).
- Rien de nouveau. Cause déjà documentée depuis 2026-09-23.

### P2. Méthode durcie confirmée - compteur orphelines sur `<a href>` seul

- Confirmé ce run : 513 arêtes `<a>` inbound sitemap vs 436 arêtes brutes `href` au 2026-10-05, méthode stable sur les 3 nouvelles pages (qui ne reçoivent pas de hreflang bidirectionnel). Pas de régression.
- Les 3 orphelines « .html + en/ » restent orphelines strict (confirmé 4e semaine). Pas d'autre page avec `<link rel="alternate" hreflang>` discordant.
- Durcissement P2 reste à inscrire dans le skill (`memory/questions.md` section Q5).

### P3. Mesure 410 - première occurrence sur ce domaine

- Première fois que l'audit mesure un code HTTP 410. Les 2 URLs concernées étaient dans le sitemap au 2026-10-05, donc le signal est inter-run cohérent : le sitemap retire l'URL **et** le serveur répond 410 (pas 404 nu). Signalétique propre.
- À coder dans le checker : les codes 410 doivent sortir en catégorie « retrait assumé », distincts des 404 nu (« peut-être oublié »).

## 5. Résolution des prédictions du 2026-10-05 (resolve_by 2026-10-12)

| ID | Verdict | Détail |
|---|---|---|
| `pred-2026-10-05-manifeste-404` | HIT | 17e récurrence, 124 jours sans action |
| `pred-2026-10-05-blog-cadence` | HIT | 0 nouvelle 301 `/blog/*` cette semaine (prédit « au plus 1 ») |
| `pred-2026-10-05-orphans-9pages` | MISS | 4/9 orphelines sorties de la zone 0-inbound (prédit : les 9 restent orphelines) ; cf. mistake logguée |
| `pred-2026-10-05-tarifs-sitemap` | HIT | 8e récurrence, `/tarifs/` toujours hors sitemap |
| `pred-2026-10-05-lastmod-uniforme` | HIT | 31/31 lastmod uniforme, 21e récurrence |
| `pred-2026-10-05-audit-split` | HIT | `/audit-seo/` dans sitemap + `/audit/` hors sitemap, aucune 301 ni canonical croisé ; le split s'intensifie |
| `pred-2026-10-05-systeme-seo-noindex` | HIT | 74 nav inbound (prédit ≥ 20) + `noindex, follow` confirmé |
| `pred-2026-10-05-guides-hub` | HIT | `/guides/` ne lie toujours pas les 2 `.html` (le hub a été élargi mais pas sur ce point) |

## 6. Recommandations priorisées

**P1 - couvrir les 4 dernières orphelines strict et trancher `/audit-seo/`.**
- Ajouter les 2 ancres `<a href>` dans `/guides/` pointant vers les 2 pages `.html` du sitemap. 1 ligne par ancre, preuve d'éditabilité posée par les 11 nouveaux liens ajoutés dans `/guides/` cette semaine.
- Ajouter `/en/agent-seo/` au `plan-du-site` ou poser 1 lien éditorial depuis `/agent-seo/` (hreflang suffit pour la découverte Google mais pas pour le linkjuice interne).
- Trancher `/audit-seo/` : la trajectoire 80 → 90 → 47 mots en 3 semaines sur une URL orpheline du sitemap plaide pour un retrait du sitemap (puisque `/audit/` capte toute la nav et le linkjuice). Alternative : rapatrier le contenu éditorial sur `/audit-seo/` et retirer `/audit/` du site. Choix binaire à documenter.

**P1 - arbitrer `/systeme-seo/` (74 inbound, hors sitemap, `noindex`).**
- Si intentionnel (landing conversion désindexée) : accepter la fuite PageRank et documenter dans le repo. Mais `/systeme/` (dans sitemap, 378 mots, 1 inbound) va porter l'image éditoriale enterrée par rapport à `/systeme-seo/` côté Google.
- Si reliquat de nav : poser une 301 `/systeme-seo/` → `/systeme/`, retirer les 74 inbound ou les rediriger côté template nav.
- Cette semaine le ratio nav est passé de 24 à 74 : la nav a été restructurée **en aggravant** l'asymétrie. Le moment pour décider.

**P2 - propager le pattern 410 aux cas déjà identifiés.**
- `/methode/` et `/bootcamp/` ont basculé en 410 cette semaine. Le site sait émettre du 410 propre (header `x-robots-tag: noindex`, content-type text/plain, pas de HTML résiduel). Appliquer le même traitement à `/manifeste{,/}` (ou poser une 301 vers `/systeme/`) après 124 jours.
- Pour les 7 `/blog/*` 404 nu, choisir URL par URL entre 410 (contenu définitivement retiré) et 301 (contenu équivalent sur une landing éditoriale). Le pattern `9-skills-seo-claude → /skills/` montre que l'option 301 unitaire est faisable.

**P2 - décider sur `/tarifs/` (44 j hors sitemap) et sur `/strategie-seo-b2b/` (3 inbound dans le sitemap).**
- `/tarifs/` : 3 inbound mesurés cette semaine (vs 1), toujours hors sitemap depuis 44 jours, HTTP 200 `index, follow`. Ajouter au sitemap si la page est maintenue, retirer et poser 301 vers `/accompagnement-seo-geo/` ou `/consultant-seo-geo-lyon/` sinon.
- `/strategie-seo-b2b/` : 2 941 mots entrés au sitemap avec seulement 3 inbound. Pousser 2 ancres nav pour la sortir de sous-maillage avant le crawl.

**P3 - signal fraîcheur.**
- `lastmod_uniforme` (C7) : émettre le `lastmod` éditorial par URL au lieu de l'horodatage de build. 124 jours de perte de signal, aggravé cette semaine par 3 nouvelles pages qui portent la même date que les 28 autres. Priorité réaffirmée.

**P4 - méthode boucle (Tim tranche).**
- Diff `urlInspection` du 2026-07-10 dans `memory/questions.md` : **94 jours**. Sans ça, la Couche B reste morte et 5 anomalies critiques de ce run ne peuvent pas être mesurées côté Google (C1, C4, C5, C8, C9).
- Durcissement P2 (compteur orphelines sur `<a href>` strict) : inscrire dans le skill. Comportement déjà appliqué ce run, décision formelle attendue.
- **Nouveau** : prévoir une catégorie « retrait assumé » (code 410) distincte de « 404 nu », pour que les futures 410 ne fassent plus crier le checker de la même manière que les 404 oubliées.

## 7. Nouvelles prédictions (resolve_by 2026-10-19)

- `pred-2026-10-12-manifeste-404` : `/manifeste{,/}` encore HTTP 404 au run du 2026-10-19 (18e récurrence).
- `pred-2026-10-12-410-stable` : `/methode/` et `/bootcamp/` toujours HTTP 410 + `x-robots-tag: noindex` au run du 2026-10-19 (2e récurrence attendue).
- `pred-2026-10-12-audit-seo-wordcount` : `/audit-seo/` restera dans le sitemap avec un wordcount ≤ 100 au run du 2026-10-19 (5e récurrence, prolongation de la trajectoire négative).
- `pred-2026-10-12-tarifs-sitemap` : `/tarifs/` restera hors sitemap au run du 2026-10-19 (9e récurrence).
- `pred-2026-10-12-lastmod-uniforme` : 31+/31+ URLs sitemap partageront un unique `<lastmod>` au run du 2026-10-19 (22e récurrence).
- `pred-2026-10-12-orphans-5pages` : les 5 orphelines strict `<a>` de C6 (`/audit-seo/`, `/en/agent-seo/`, les 2 `.html`, `/plan-du-site/`) resteront à 0 inbound strict au run du 2026-10-19.
- `pred-2026-10-12-systeme-seo-noindex` : `/systeme-seo/` restera HTTP 200 + `noindex, follow` + ≥ 60 inbound depuis le sitemap au run du 2026-10-19 (3e récurrence).
- `pred-2026-10-12-blog-cadence` : au plus 1 nouvelle URL `/blog/*` passera en 301 d'ici le 2026-10-19 (cadence actuelle 0-1 URL/semaine).
- `pred-2026-10-12-strategie-b2b-maillage` : `/strategie-seo-b2b/` restera à ≤ 5 inbound au run du 2026-10-19 (prédit un rythme lent d'ajout nav).

## 8. Limites du rapport

- **Statut d'indexation Google réel** : non testable. Pas d'accès à `urlInspection` ni `searchAnalytics`. Les 31 URLs du sitemap peuvent toutes être indexées ou pas, aucun chiffre n'est donné dans ce rapport sur ce point.
- **Trafic organique mesuré** : non accessible dans cet environnement. Les retraits C1 (`/methode/`, `/bootcamp/`) et le thin content C4 (`/audit-seo/`) seraient à qualifier par leurs impressions sur les 90 derniers jours, non mesurées ici.
- **Rendu client-side** : le HTML servi est le HTML initial (`curl -sL`). Les pages à 47-95 mots (`/audit-seo/`, `/consultants-seo/`, `/skills/`) portent peut-être du contenu complémentaire injecté en JS. Hypothèse ouverte depuis 2026-09-07, non tranchée ce run.
- **Actions manuelles et sécurité** : non vérifiées (Search Console inaccessible).
- **Backlinks externes** : non mesurés. Les URLs retirées cette semaine (`/methode/`, `/bootcamp/`) peuvent porter du linkjuice externe perdu si aucune 301 n'a été préparée.
