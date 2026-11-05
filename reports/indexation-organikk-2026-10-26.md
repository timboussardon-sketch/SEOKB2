---
type: audit
title: Indexation Organikk - audit hebdomadaire 2026-10-26
created: 2026-10-26
updated: 2026-10-26
tags: [indexation, sitemap, audit, organikk, hebdo]
status: stable
confidence: high
sources: 3
---

# Audit indexation Organikk - 2026-10-26

**Périmètre.** organikk.co, 33 URLs listées dans `sitemap.xml` (delta +2 vs 2026-10-19 : +2 entrées `/blog/` et `/x-ray/`, 0 sortie). Lecture seule sur le web public. Aucun forçage d'indexation.

**Sources de vérité utilisées.**
- Statut HTTP `curl -sIL` (code final + chaîne de redirections + `x-robots-tag`).
- Présence dans `sitemap.xml` + `lastmod`.
- `robots.txt`.
- Parsing HTML servi : `<title>`, `<h1>` (tags enfants strippés, décodage entités), `<link rel=canonical>`, `<meta name=robots>`, graphe interne reconstruit à partir des seuls `<a href>` (hreflang `<link rel=alternate>` exclu, durcissement du 2026-10-05).

**Non testable.** Statut d'indexation Google réel. Pas d'accès à `urlInspection` / `searchAnalytics` dans cet environnement. Témoin obligatoire relancé : `/cette-page-nexiste-pas-xyz-2026-10-26/` renvoie HTTP 404 côté organikk, `https://www.google.com/search?q=site%3Aorganikk.co` renvoie HTTP 200 / 93 179 octets, aucune SERP sans JS, 0 marqueur recaptcha. Couche B non testable, **11e run consécutif**. Diff `urlInspection` du 2026-07-10 toujours ouvert dans `memory/questions.md` : **108 jours**.

## 1. Synthèse

Semaine de restructuration du maillage interne de grande ampleur, à contre-sens de la densification de la semaine passée. Six mouvements principaux :

1. **Chute brutale du maillage interne total.** `<a>` sitemap→sitemap passe de **613 → 396 arêtes (-217 arêtes, -35 %)** en 7 jours. Casse frontale de la trajectoire éditoriale enrichissante du 2026-10-19 (+100 arêtes alors).
2. **+2 URLs au sitemap : `/blog/` et `/x-ray/`.** `/blog/` HTTP 200 avec seulement **32 mots** dans le HTML servi (hub thin, pattern identique à `/audit-seo/` et `/skills/`). `/x-ray/` HTTP 200, **1 385 mots**, 28 inbound dès entrée (nav-linkée).
3. **Effondrement du canal nav vers `/systeme-seo/`.** La page `noindex, follow` hors sitemap passe de **77 → 30 inbound** (-47 inbound). `/audit/` hors sitemap passe aussi de **63 → 30 inbound**. Nav globale restructurée : le canal privilégié `/systeme-seo/` et `/audit/` qui aspirait le PageRank interne vers des URLs désindexées est désormais réduit à 30 pages chacune.
4. **Orphelines strict `<a>` identiques au 2026-10-19 : les mêmes 5** (`/audit-seo/`, `/en/agent-seo/`, les 2 guides `.html`, `/plan-du-site/`). **6e récurrence**, aucun lien `<a>` entrant n'a été posé en 7 jours.
5. **`/wiki/*` : fin du raffinement par ancre `#audit`.** 4/4 slugs testés redirigent uniformément vers `/systeme-seo/` nu (fin du raffinement du 2026-09-28 qui pointait 2/4 slugs vers `/systeme-seo/#audit`). Simplification.
6. **`/audit-seo/` : trajectoire oscillante en 5 runs** `80 → 90 → 47 → 123 → 55`. Reste orphelin strict et dans sitemap avec canonical auto-ref.

Autres signaux :

- **Sitemap 33 URLs**. Trajectoire 136j : `169-136-143-143-146-146-330-330-332-333-334-334-142-91-91-88-28-29-30-30-31-31-`**`33`**.
- **`/methode/` et `/bootcamp/` toujours HTTP 410** + `x-robots-tag: noindex`. **3e récurrence, 21 jours**. Signalétique de retrait stable.
- **`/manifeste{,/}` toujours 404** avec `meta robots: noindex` sur page d'erreur. **19e récurrence, 138 jours** depuis la reco P1 du 2026-06-10.
- **`lastmod_uniforme`** : 33/33 URLs partagent `2026-10-26T04:40:43.496Z`. **23e récurrence, 138 jours**.
- **`/tarifs/`** toujours hors sitemap avec `index, follow` et 5 inbound (identique au 2026-10-19). **10e récurrence, 58 jours**.
- **Blog slugs** : 1/4 slugs testés redirige stable (`9-skills-seo-claude` → `/skills/`), 3/4 toujours 404 nu (`process-seo-b2b-2026`, `information-gain-geo`, `wiki-ia-obsidian-claude`). **7e récurrence**, 0 nouvelle 301 cette semaine.
- **Couche B morte 11e run consécutif**. `urlInspection` : 108 jours.

**Chiffres du run.** 33/33 HTTP 200 direct (0 redirect dans le sitemap). 33/33 avec `<title>`, `<h1>` et `<link rel=canonical>` auto-référent égal à la `<loc>`. **27/33** avec `<meta name="robots">` explicite `index, follow` ; 6 sans meta (`/agent-seo/`, `/en/agent-seo/`, `/skills/`, les 2 guides `.html`, **nouveau `/x-ray/`** — famille gabarit léger). **0 `noindex` sur balise dans le sitemap**. `robots.txt` inchangé (`User-Agent:* / Allow:/ + Sitemap`). Graphe interne reconstruit sur 33 HTML téléchargés : **396 arêtes `<a>` inbound vers URLs du sitemap** (hors self-ref). **28/33 title ≠ h1** après nettoyage du suffixe nom de site.

## 2. Anomalies critiques

### C1. Effondrement du maillage interne : 613 → 396 arêtes (-217, -35 %) en 7 jours

- Mesure stricte `<a href>` (hreflang `<link rel=alternate>` exclu depuis 2026-10-05).
- **613 arêtes au 2026-10-19 → 396 arêtes au 2026-10-26.** Chute uniforme, pas de rebalancement sectoriel : la plupart des pages du sitemap perdent du maillage entrant.
- Pages les plus touchées :
  - `/consultant-geo/` : 48 → 28 inbound (**-20**). URL rachetée la semaine dernière de son statut chronique sous-maillée, perd 42 % de son maillage en 7 jours.
  - `/consultants-seo/` : 44 → 28 (**-16**).
  - `/consultant-seo-saas/` : 46 → 28 (**-18**).
  - `/consultant-seo-lyon/` : 48 → 28 (**-20**).
  - `/consultant-seo-geo-lyon/` : 48 → 28 (**-20**).
  - `/accompagnement-seo-geo/` : 11 → 1 (**-10**).
  - `/formation-seo-ia/` : 11 → 1 (**-10**).
  - `/consultant-lead-seo/` : 11 → 1 (**-10**).
  - `/accompagnement-1-1-30-jours/` : 10 → 9 (**-1**).
  - Pages nav-linkées globales stables à 28-30 (`/`, `/agent-seo/`, `/blog/`, `/skills/`, `/x-ray/`, `/bootcamp-candidature/`, `/mentions-legales/`, `/politique-confidentialite/`).
- Lecture système : passage d'une nav verticale enrichie (49 ancres par pied-de-page, hub `/plan-du-site/` injectait 41 ancres) à une nav plate (menu principal uniquement). `/plan-du-site/` passe de **151 → 94 mots**, 41 → ? ancres sortantes (hub élagué).
- **Hypothèse alternative à poser** : refactoring intentionnel pour éviter la dilution du PageRank interne (concentrer sur 28 pages nav-linkées), ou régression de template non intentionnelle. Les deux lectures sont compatibles avec les mesures de ce run.
- Non mesurable sans `urlInspection` + `searchAnalytics` : impact sur impressions des 10 pages perdant du maillage.

### C2. `/blog/` entre au sitemap avec 32 mots dans le HTML servi

- HTTP 200 direct, canonical auto-ref, `index, follow`, lastmod `2026-10-26T04:40:43.496Z`.
- **32 mots** dans le HTML servi méthode C (strip script/style/nav/header/footer/aside). Pattern identique à `/audit-seo/` (55 mots), `/skills/` (66 mots), `/consultants-seo/` (89 mots), `/plan-du-site/` (94 mots).
- **25 inbound** depuis le sitemap dès entrée (nav-linkée).
- `/blog/*` articles toujours 404 nu (3/4 testés) : la hub éditoriale `/blog/` entre au sitemap sans que ses articles soient restaurés. Soit une page hub propre à construire côté éditorial, soit un placeholder temporaire.
- Lecture : hypothèse « rendu côté client Next.js » toujours ouverte sur cette famille (mesure HTML initial servi ≠ DOM rendu), mais 5 pages du sitemap partagent désormais ce profil « < 100 mots en HTML servi ».

### C3. `/x-ray/` entre au sitemap, pattern geo-landing continu

- HTTP 200, canonical auto-ref. `<meta name=robots>` **absente** (indexable par défaut, mappe sur la famille gabarit léger).
- **1 385 mots**, title = « Audit SEO X-Ray à 1 000€ offert », h1 = « X-Ray SEO : la radio complète qui révèle les trois raisons pour lesquelles ton site ne décolle pas ».
- **28 inbound** dès son entrée au sitemap. Pattern cohérent avec les 4 landings geo/vertical entrées depuis le 2026-09-28 : la page apparaît déjà intégrée dans la nav globale au moment de son entrée.
- 2e nouvelle URL de la semaine après `/blog/`, 5e nouvelle entrée au sitemap en 5 semaines (`/consultant-seo-geo-lyon/`, `/consultant-seo-lyon/`, `/consultants-seo/`, `/consultant-seo-saas/`, puis `/blog/` + `/x-ray/`).

### C4. `/manifeste{,/}` 404 — 19e récurrence (138 jours)

- HTTP 404 sur les deux variantes avec et sans slash. Page d'erreur sert `<title>` vide, `<h1>404</h1>`, `<meta name="robots" content="noindex"/>`.
- 0 lien `<a>` entrant depuis les 33 pages du sitemap. Toujours hors du blanket wiki 301.
- Reco P1 du 2026-06-10 non appliquée depuis **138 jours**.
- Note couplée : la cible 301 recommandée doit rester `/systeme-seo/` ou `410` (le site sait émettre du 410 propre : preuve stable sur `/methode/` et `/bootcamp/` depuis 21 jours).

### C5. 5 orphelines strict `<a>` identiques au 2026-10-19 — 6e récurrence

- `/audit-seo/` (**6e récurrence**, dans sitemap, 55 mots)
- `/en/agent-seo/` (**6e récurrence**, dans sitemap, 3 143 mots, hreflang vers `/agent-seo/` seulement)
- `/guides/audit-seo-technique-claude.html` (**6e récurrence**, 5 227 mots)
- `/guides/en/audit-seo-technique-claude.html` (**6e récurrence**, 4 992 mots)
- `/plan-du-site/` (**8e récurrence** hub orphelin, 94 mots, lui-même liste 11 ancres sortantes vs ≈41 au 2026-10-12)
- Aucune n'a reçu de lien `<a>` entrant en 7 jours. Le hub `/plan-du-site/` a été **élagué** cette semaine (passage de 41 à ≈11 ancres), contredisant le mouvement d'enrichissement du 2026-10-12.

### C6. `lastmod_uniforme` 23e récurrence (138 jours)

- 33/33 URLs partagent `2026-10-26T04:40:43.496Z` (dont les 2 nouvelles entrées `/blog/` et `/x-ray/`).
- P2 du 2026-06-15 toujours sans effet. Impact mécanique : signal de fraîcheur perdu sur 33 URLs y compris les 2 vraies nouveautés.

### C7. Couche B morte 11e run consécutif — `urlInspection` 108 jours d'ouverture

- Témoin HTTP : `/cette-page-nexiste-pas-xyz-2026-10-26/` renvoie 404 côté organikk, cohérent.
- `https://www.google.com/search?q=site%3Aorganikk.co` : HTTP 200, 93 179 octets, aucune SERP sans JS.
- Diff `urlInspection` posé le 2026-07-10 dans `memory/questions.md` toujours en attente de décision Tim.
- Impact particulièrement lourd cette semaine : le mouvement C1 (-217 arêtes de maillage interne) va probablement se refléter dans `searchAnalytics` à J+14/J+28, non mesurable sans accès.

### C8. `/audit-seo/` wordcount oscille — 55 mots (vs 123 au 2026-10-19)

- Trajectoire 5 runs : **80 → 90 → 47 → 123 → 55**. Rebond du 2026-10-19 non tenu, retour en zone thin.
- Toujours 0 lien `<a>` entrant depuis les 33 pages du sitemap. Canonical auto-ref. `index, follow`.
- `/audit/` (hors sitemap) : **219 mots** (vs 309 au 2026-10-19), **30 inbound** (vs 63). Les deux URLs perdent du contenu et du maillage.
- Lecture : le split `/audit/` (hors sitemap, nav-linkée) vs `/audit-seo/` (dans sitemap, orpheline strict) persiste, mais les deux subissent une régression simultanée. Hypothèse rendu client-side ouverte.

### C9. `/blog/*` 404 nu — 7e récurrence, 1/4 slugs redirige stable

- Testés : `9-skills-seo-claude` → **301** vers `/skills/` (stable depuis 2026-10-05, 3 semaines).
- 3/4 toujours **404 nu** sans redirection : `process-seo-b2b-2026`, `information-gain-geo`, `wiki-ia-obsidian-claude`.
- 0 nouvelle 301 cette semaine (cadence 1 URL en 5 semaines).
- Asymétrie persistante avec `/wiki/*` : 4/4 slugs testés redirigent uniformément (blanket 301 maintenu), mais fin du raffinement par ancre `#audit`.

### C10. Pages d'offre nav-linkées perdent 80-90 % de leur maillage entrant

- `/accompagnement-seo-geo/` : 11 → 1 inbound (**-10**, -91 %).
- `/formation-seo-ia/` : 11 → 1 (**-10**, -91 %).
- `/consultant-lead-seo/` : 11 → 1 (**-10**, -91 %).
- `/consultant-geo/` : 48 → 28 (**-20**, -42 %).
- Toutes servies HTTP 200, canonical auto-ref, `index, follow` — rien de cassé côté page. C'est le canal entrant qui a été coupé (hypothèse C1 : nav restructurée vers une version plate).
- Récurrence chronique : ces pages avaient été rachetées via l'enrichissement du 2026-10-12 (`/plan-du-site/` enrichi 19 → 41 ancres) puis via le passage éditorial du 2026-10-19 (+100 arêtes). Les deux mouvements correctifs sont désormais inversés.

## 3. Anomalies mineures

### M1. 28/33 title ≠ h1 — 6e récurrence

- Méthode stricte (nettoyage suffixe nom de site). Pattern éditorial stable : title = requête commerciale, h1 = accroche narrative.
- 5 pages où title ≈ h1 : `/`, `/mentions-legales/`, `/politique-confidentialite/`, `/consultant-seo-lyon/`, `/consultants-seo/`.
- Les 2 nouvelles entrées `/blog/` et `/x-ray/` adoptent le pattern divergent.

### M2. 6/33 pages sans `<meta name=robots>` — 6e récurrence +1

- Mapping stable gabarit léger : `/agent-seo/`, `/en/agent-seo/`, `/skills/`, 2 guides `.html`, **nouveau `/x-ray/`**.
- Non critique (indexable par défaut), mais le pattern se transmet à chaque nouvelle entrée sur ce gabarit.

### M3. `/guides/` hub ne lie que 7 PDF + 11 pages site, 0 des 2 `.html` du sitemap — 6e récurrence

- Extraction `<a href>` : 7 PDF (`.pdf`) + 11 pages site, 0 lien vers `/guides/audit-seo-technique-claude.html` et `/guides/en/audit-seo-technique-claude.html` (10 491 mots cumulés).
- Les 2 `.html` restent orphelines strict (C5).

### M4. `/plan-du-site/` élagué, 11 ancres sortantes vs ≈41 au 2026-10-12

- 94 mots (vs 151 au 2026-10-19, 170 au 2026-09-21).
- Reste orpheline strict (C5).
- L'enrichissement du 2026-10-12 est inversé.

### M5. `/systeme-seo/` (hors sitemap, `noindex, follow`) : 30 inbound (vs 77 au 2026-10-19)

- -47 inbound en 7 jours. Le canal nav vers URL noindex est largement réduit.
- Page toujours servie HTTP 200, 4 210 mots, `noindex, follow` sur balise.
- Lecture système : si c'est intentionnel (fin de l'arbitrage « nav aspirante vers noindex »), le canal reste anormalement élevé pour une URL désindexée. Si c'est une régression de template, à surveiller la semaine prochaine.

### M6. `/wiki/*` : fin du raffinement par ancre `#audit`

- 4/4 slugs testés redirigent uniformément vers `/systeme-seo/` nu : `featured-snippet`, `topical-authority`, `passage-ranking`, `rrf`.
- Au 2026-09-28, 2/4 slugs testés (`passage-ranking`, `agentic-search`) pointaient vers `/systeme/#audit`. Le raffinement est annulé.
- Pattern cohérent avec C1 (simplification de la nav + simplification des redirections).

### M7. `/tarifs/` hors sitemap — 10e récurrence (58 jours)

- HTTP 200, canonical auto-ref, `index, follow`, 795 mots.
- **5 inbound** depuis le sitemap (identique au 2026-10-19).
- Page commerciale doublement invisible : absente du sitemap et au maillage interne faible.

## 4. Résolution des prédictions du 2026-10-19

| ID | Verdict | Détail |
|---|---|---|
| pred-2026-10-19-lastmod-uniforme | **hit** | 33/33 URLs lastmod uniforme `2026-10-26T04:40:43.496Z`, 23e récurrence 138 jours |
| pred-2026-10-19-orphans-5pages | **hit** | Mêmes 5 orphelines strict (`/audit-seo/`, `/en/agent-seo/`, 2 guides `.html`, `/plan-du-site/`) à 0 inbound |
| pred-2026-10-19-systeme-seo-inbound | **miss** | `noindex, follow` confirmé sur balise, mais 30 inbound seulement (prédit ≥ 70). Chute brutale -47 inbound en 7 jours, cf. M5 + C1 |
| pred-2026-10-19-blog-cadence | **hit** | 0 nouvelle 301 `/blog/*` cette semaine (prédit ≤ 1), 1/4 slugs stable |
| pred-2026-10-19-audit-seo-wordcount | **hit** | 55 mots, dans sitemap, fourchette [50, 250] respectée (de justesse en bas) |
| pred-2026-10-19-sitemap-size | **hit** | 33 URLs, fourchette [30, 33] respectée (plafond) |

5 hit, 1 miss. Le miss (systeme-seo-inbound) révèle le mouvement C1 majeur de ce run. Note dans `mistakes.jsonl`.

## 5. Recommandations priorisées

### P1 (identique depuis 2026-06-10, 138 jours sans effet) — poser 301 ou 410 sur `/manifeste{,/}`

- Options techniquement prouvées sur ce domaine :
  - **410** : signalétique de retrait stable depuis 21 jours sur `/methode/` et `/bootcamp/` (`HTTP 410` + `x-robots-tag: noindex`).
  - **301** : vers `/systeme-seo/` (page `noindex` mais finie et pérenne).
- Préférence méthodique : 410 si décision éditoriale assumée, sinon 301 vers `/systeme-seo/`.
- Mesure attendue sous J+14 (via `urlInspection` quand le diff sera appliqué) : disparition de l'URL de l'index Google.

### P2 (identique depuis 2026-06-15, 138 jours sans effet) — `lastmod` différencié par URL

- Le lastmod uniforme `2026-10-26T04:40:43.496Z` sur 33/33 URLs écrase le signal de fraîcheur sur les 2 vraies nouveautés de la semaine (`/blog/`, `/x-ray/`) et sur les pages réellement modifiées.
- Coût : adaptation du générateur de sitemap pour écrire la mtime effective (ou la date du dernier commit) par URL.

### C1 (nouveau, lié au mouvement de ce run) — trancher la nature du refactoring maillage

- Question méthode : la chute -217 arêtes en 7 jours est-elle intentionnelle (fin de la nav verticale enrichie, concentration sur 28 pages nav-linkées) ou une régression de template ?
- Diagnostic côté template : vérifier si le pied-de-page sert maintenant 10-12 liens vs 40+ auparavant.
- Si intentionnel : documenter côté éditorial pour que les futures mesures C10 (10 pages d'offre à 1 inbound) ne soient pas re-signalées comme régression.
- Si régression : rétablir la nav enrichie, les pages d'offre doivent récupérer leurs ≥10 inbound sous J+7.

### C2+C3 (hub thin + landings nav-linkées) — critère d'entrée au sitemap

- 2 nouvelles entrées cette semaine avec profils opposés : `/blog/` à 32 mots (hub thin), `/x-ray/` à 1 385 mots (page de contenu).
- Hub thin + rendu client-side Next.js suspecté : si le HTML servi reste < 100 mots, Google indexe du vide (ou pas du tout).
- Reco à poser au vendredi : règle « une page entre au sitemap avec ≥ 300 mots en HTML servi », sinon rendu SSR renforcé ou déclaration différée.

### P4 (identique depuis 2026-07-10, 108 jours sans effet) — brancher `urlInspection` API

- Diff posé dans `memory/questions.md` toujours en attente.
- Chaque semaine qui passe sans accès rend non mesurable l'impact des mouvements de restructuration (sitemap, maillage, 301/410).
- Impact cette semaine : non mesurable l'effet de la chute -217 arêtes de maillage sur le service en SERP des pages touchées.

### C5 (6e récurrence) — réparer les orphelines strict chroniques

- `/plan-du-site/` doit se référencer dans la nav ou le pied-de-page (lui-même orphelin alors qu'il est utilisé comme hub maillant).
- `/guides/` doit lier ses 2 pages `.html` (le hub ne lie que les PDF).
- `/en/agent-seo/` doit recevoir ≥ 1 lien `<a>` depuis `/agent-seo/` (hreflang seul ne suffit pas en comptage strict).
- `/audit-seo/` doit recevoir ≥ 1 lien `<a>` depuis une page nav-linkée, sinon décider sa désindexation (meta noindex + sortie sitemap).

## 6. Trajectoire sitemap 136 jours

`169-136-143-143-146-146-330-330-332-333-334-334-142-91-91-88-28-29-30-30-31-31-33`

(+2 cette semaine après 2 semaines de stabilité à 31, 5e semaine d'expansion après la double contraction du 2026-08-31 et du 2026-09-21.)
