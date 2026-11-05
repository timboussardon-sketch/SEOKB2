---
type: audit
title: Indexation Organikk - audit hebdomadaire 2026-11-02
created: 2026-11-02
updated: 2026-11-02
tags: [indexation, sitemap, audit, organikk, hebdo]
status: stable
confidence: high
sources: 3
---

# Audit indexation Organikk - 2026-11-02

**Périmètre.** organikk.co, 38 URLs listées dans `sitemap.xml` (delta +5 vs 2026-10-26 : +5 entrées `/glossaire/`, `/etudes-de-cas-seo-b2b/`, `/outils/calculateur-budget-seo/`, `/outils/calculateur-cout-lead-seo/`, `/skills-seo/`, 0 sortie). Lecture seule sur le web public. Aucun forçage d'indexation.

**Sources de vérité utilisées.**
- Statut HTTP `curl -sIL` (code final + chaîne de redirections + `x-robots-tag`).
- Présence dans `sitemap.xml` + `lastmod`.
- `robots.txt`.
- Parsing HTML servi : `<title>`, `<h1>`, `<link rel=canonical>`, `<meta name=robots>`, graphe interne reconstruit à partir des seuls `<a href>` (hreflang `<link rel=alternate>` exclu, durcissement du 2026-10-05).

**Non testable.** Statut d'indexation Google réel. Pas d'accès à `urlInspection` / `searchAnalytics` dans cet environnement. Témoin obligatoire relancé : `/cette-page-nexiste-pas-xyz-2026-11-02/` renvoie HTTP 404 côté organikk, `https://www.google.com/search?q=site%3Aorganikk.co` renvoie HTTP 200 / 93 023 octets, aucune SERP sans JS, 0 marqueur recaptcha. Couche B non testable, **12e run consécutif**. Diff `urlInspection` du 2026-07-10 toujours ouvert dans `memory/questions.md` : **115 jours**.

## 1. Synthèse

Semaine de rebond éditorial et de maillage, à contre-sens frontal du mouvement de la semaine dernière. Six mouvements principaux :

1. **Rebond massif du maillage interne total.** `<a>` sitemap→sitemap passe de **396 → 1 063 arêtes (+667 arêtes, +168 %)** en 7 jours. Sur les 33 URLs communes aux deux runs : **396 → 885 arêtes (+489, +124 %)**. La restructuration -217 arêtes du 2026-10-26 est intégralement inversée, et dépassée.
2. **+5 URLs au sitemap** (plus gros ajout en une semaine depuis le début du suivi) : `/glossaire/` (1 345 mots, 59 inbound dès entrée), `/etudes-de-cas-seo-b2b/` (3 724 mots, 2 inbound), `/outils/calculateur-budget-seo/` (2 351 mots, 58 inbound), `/outils/calculateur-cout-lead-seo/` (1 818 mots, 58 inbound), `/skills-seo/` (**9 187 mots**, 1 inbound seulement).
3. **Les 3 pages d'offre tombées à 1 inbound le 2026-10-26 restent à 1 inbound.** `/accompagnement-seo-geo/`, `/formation-seo-ia/`, `/consultant-lead-seo/` : 1 → 1. La vague de rebond général du maillage ne les a pas touchées : classe de pages exclue de la nav restaurée.
4. **Nav restaurée en version horizontale enrichie.** La page racine lie désormais 15 URLs uniques du sitemap (vs ~12 estimés au 2026-10-26). `/plan-du-site/` liste **32 ancres sortantes** (vs ≈11 au 2026-10-26, 41 au 2026-10-12) : restauration partielle du hub.
5. **5 orphelines strict identiques au 2026-10-26 : 7e récurrence.** `/plan-du-site/`, `/audit-seo/`, `/en/agent-seo/`, les 2 guides `.html`. Toujours 0 lien `<a>` entrant.
6. **`/audit/` (hors sitemap) rebond fort.** 30 → **83 inbound** (+53). `/systeme-seo/` (hors sitemap, `noindex, follow`) : 30 → **99 inbound** (+69). Les deux canaux nav vers URLs hors sitemap sont restaurés et dépassent le niveau du 2026-10-19.

Autres signaux :

- **Sitemap 38 URLs**. Trajectoire 143j : `169-136-143-143-146-146-330-330-332-333-334-334-142-91-91-88-28-29-30-30-31-31-33-`**`38`**. 6e semaine d'expansion consécutive.
- **`/methode/` et `/bootcamp/` toujours HTTP 410** + `x-robots-tag: noindex`. **4e récurrence, 28 jours**. Signalétique de retrait stable.
- **`/manifeste{,/}` toujours 404** avec `meta robots: noindex` sur page d'erreur. **20e récurrence, 145 jours** depuis la reco P1 du 2026-06-10.
- **`lastmod_uniforme`** : 38/38 URLs partagent `2026-11-02T06:00:55.354Z`. **24e récurrence, 145 jours**.
- **`/tarifs/`** toujours hors sitemap avec `index, follow` et 7 inbound (vs 5 au 2026-10-26). **11e récurrence, 65 jours**.
- **Blog slugs** : 1/4 slugs testés redirige stable (`9-skills-seo-claude` → `/skills/`), 3/4 toujours 404 nu (`process-seo-b2b-2026`, `information-gain-geo`, `wiki-ia-obsidian-claude`). **8e récurrence**, 0 nouvelle 301 cette semaine.
- **Wiki slugs** : 4/4 slugs testés redirigent uniformément vers `/systeme-seo/` nu (fin du raffinement `#audit` confirmée pour la 2e semaine).
- **Couche B morte 12e run consécutif**. `urlInspection` : 115 jours.

**Chiffres du run.** 38/38 HTTP 200 direct (0 redirect dans le sitemap). 38/38 avec `<title>`, `<h1>` et `<link rel=canonical>` auto-référent égal à la `<loc>`. **32/38** avec `<meta name="robots">` explicite `index, follow` ; 6 sans meta (`/agent-seo/`, `/en/agent-seo/`, `/skills/`, `/x-ray/`, les 2 guides `.html` — famille gabarit léger inchangée). **0 `noindex` sur balise dans le sitemap**. `robots.txt` inchangé. Graphe interne reconstruit sur 38 HTML téléchargés : **1 063 arêtes `<a>` inbound vers URLs du sitemap** (hors self-ref). **31/38 title ≠ h1** après nettoyage du suffixe nom de site.

## 2. Anomalies critiques

### C1. Rebond massif du maillage interne : 396 → 1 063 arêtes (+667, +168 %) en 7 jours

- Mesure stricte `<a href>` (hreflang `<link rel=alternate>` exclu depuis 2026-10-05).
- **396 arêtes au 2026-10-26 → 1 063 arêtes au 2026-11-02.** Rebond de +667 arêtes.
- Comparable sur les 33 URLs communes aux deux runs : **396 → 885 arêtes (+489, +124 %)**.
- Pages les plus restaurées (sur base 33 communes) :
  - `/` : 30 → **135 inbound** (+105). La page racine est lue comme cible primaire par la plupart des pages (navbar + crédits footer).
  - `/politique-confidentialite/` : 29 → 67 (+38).
  - `/bootcamp-candidature/` : 28 → 66 (+38).
  - `/consultant-seo-geo-lyon/` : 28 → 64 (+36).
  - `/consultant-seo-lyon/` : 28 → 63 (+35).
  - `/agent-seo/` : 28 → 63 (+35).
  - `/consultant-geo/` : 28 → 62 (+34).
  - `/mentions-legales/` : 29 → 62 (+33).
  - `/blog/` : 25 → 58 (+33).
  - `/x-ray/` : 28 → 60 (+32).
  - `/consultants-seo/` : 28 → 60 (+32).
  - `/consultant-seo-saas/` : 28 → 59 (+31).
- Classe non-restaurée : les 3 pages d'offre tombées à 1 inbound le 2026-10-26 (`/accompagnement-seo-geo/`, `/formation-seo-ia/`, `/consultant-lead-seo/`) restent à **1 inbound** chacune (prédiction `pred-2026-10-26-pages-offre-recovery` HIT). La restauration touche la nav horizontale et le footer, pas la liste verticale des offres.
- Lecture système : la restructuration -217 arêtes du 2026-10-26 était bien une régression temporaire (ou test A/B), inversée en 7 jours. Les deux hypothèses « intentionnel » / « régression » du run précédent restent compatibles : la restauration ressemble à un rollback.
- Non mesurable sans `urlInspection` + `searchAnalytics` : impact (dans les deux sens) sur impressions.

### C2. +5 URLs au sitemap — expansion la plus large du suivi

- `/glossaire/` : 1 345 mots, 59 inbound dès entrée (nav + footer-linkée), `title: "Glossaire SEO/GEO"` ≠ h1.
- `/etudes-de-cas-seo-b2b/` : 3 724 mots, 2 inbound seulement, title = h1 = "Études de cas SEO B2B publiées par des consultants".
- `/outils/calculateur-budget-seo/` : 2 351 mots, 58 inbound (nav-linkée).
- `/outils/calculateur-cout-lead-seo/` : 1 818 mots, 58 inbound (nav-linkée).
- `/skills-seo/` : **9 187 mots** (plus gros contenu du sitemap), 1 inbound seulement. Page sous-maillée à l'entrée. Pattern déjà vu sur `/consultant-geo/` fin septembre (chronique sous-maillée).
- Cadence 6 semaines : +0, +1, +1, +1, +2, +5. Accélération, non ralentissement.

### C3. Les 3 pages d'offre à 1 inbound ne sont pas rachetées par le rebond

- `/accompagnement-seo-geo/` : 1 → 1 inbound (identique).
- `/formation-seo-ia/` : 1 → 1 inbound (identique).
- `/consultant-lead-seo/` : 1 → 1 inbound (identique).
- Toutes servies HTTP 200, canonical auto-ref, `index, follow`. Côté page, rien de cassé.
- Lecture : la nav restaurée n'inclut pas cette classe de pages d'offre. Le lien unique vient probablement du menu burger ou d'une page de regroupement.
- Récurrence : ces pages avaient 11 inbound chacune au 2026-10-19 (après enrichissement `/plan-du-site/` du 2026-10-12), 1 au 2026-10-26, 1 au 2026-11-02. **2e semaine à 1 inbound**.

### C4. `/manifeste{,/}` 404 — 20e récurrence (145 jours)

- HTTP 404 sur les deux variantes. Page d'erreur sert `<title>` vide, `<h1>404</h1>`, `<meta name="robots" content="noindex"/>`.
- 0 lien `<a>` entrant depuis les 38 pages du sitemap.
- Reco P1 du 2026-06-10 non appliquée depuis **145 jours**.
- Cible 301 recommandée reste `/systeme-seo/` ou `410` (`/methode/` et `/bootcamp/` fournissent la preuve de faisabilité sur 28 jours stables).

### C5. 5 orphelines strict `<a>` identiques au 2026-10-26 — 7e récurrence

- `/audit-seo/` (**7e récurrence**, dans sitemap, 57 mots).
- `/en/agent-seo/` (**7e récurrence**, dans sitemap, 3 036 mots, hreflang vers `/agent-seo/` seulement).
- `/guides/audit-seo-technique-claude.html` (**7e récurrence**, 5 173 mots).
- `/guides/en/audit-seo-technique-claude.html` (**7e récurrence**, 5 000 mots).
- `/plan-du-site/` (**9e récurrence** hub orphelin, 104 mots, mais passe de 11 → 32 ancres sortantes, restauration partielle).
- Aucune n'a reçu de lien `<a>` entrant en 7 jours. Le rebond C1 ne les a pas touchées.

### C6. `lastmod_uniforme` 24e récurrence (145 jours)

- 38/38 URLs partagent `2026-11-02T06:00:55.354Z` (dont les 5 nouvelles entrées).
- P2 du 2026-06-15 toujours sans effet. Impact amplifié par 5 vraies nouveautés dont la fraîcheur est écrasée.

### C7. Couche B morte 12e run consécutif — `urlInspection` 115 jours d'ouverture

- Témoin HTTP : `/cette-page-nexiste-pas-xyz-2026-11-02/` renvoie 404 côté organikk, cohérent.
- `https://www.google.com/search?q=site%3Aorganikk.co` : HTTP 200, 93 023 octets, aucune SERP sans JS, 0 marqueur recaptcha.
- Diff `urlInspection` posé le 2026-07-10 dans `memory/questions.md` : **115 jours en attente**.
- Impact particulièrement lourd ce run : le rebond C1 (+667 arêtes) et l'ajout de 5 URLs ne peuvent pas être mesurés en SERP. Deux semaines consécutives (-217 puis +667) sans mesure d'impact.

### C8. `/skills-seo/` entre au sitemap avec 9 187 mots et 1 inbound

- HTTP 200, canonical auto-ref, `index, follow`, lastmod `2026-11-02T06:00:55.354Z`.
- **9 187 mots** : contenu le plus volumineux du sitemap, devant les 2 guides `.html` (5 173 + 5 000 mots) et `/consultant-seo-lyon/` (3 776 mots).
- **1 inbound** seulement dès entrée. Pattern déjà observé sur `/consultant-geo/` fin septembre (richesse éditoriale + nav manquante).
- Risque : page lourde en contenu, invisible au maillage interne, probable sous-crawl par Googlebot.

### C9. `/audit-seo/` wordcount reste en zone basse — 57 mots (vs 55 au 2026-10-26)

- Trajectoire 6 runs : **80 → 90 → 47 → 123 → 55 → 57**. Palier bas confirmé depuis 2 semaines.
- Toujours 0 lien `<a>` entrant depuis les 38 pages du sitemap. Canonical auto-ref. `index, follow`.
- `/audit/` (hors sitemap, nav-linkée) : **237 mots** (vs 219 au 2026-10-26, 309 au 2026-10-19), **83 inbound** (vs 30 au 2026-10-26, 63 au 2026-10-19).
- Split `/audit/` (hors sitemap, nav-linkée, +53 inbound ce run) vs `/audit-seo/` (dans sitemap, orpheline strict chronique) toujours actif. L'écart s'est creusé : la nav restaurée a privilégié `/audit/` et laissé `/audit-seo/` à 0 inbound.

### C10. `/blog/*` 404 nu — 8e récurrence, cadence 1/5 semaines maintenue

- Testés : `9-skills-seo-claude` → **301** vers `/skills/` (stable depuis 2026-10-05, 4 semaines).
- 3/4 toujours **404 nu** sans redirection : `process-seo-b2b-2026`, `information-gain-geo`, `wiki-ia-obsidian-claude`.
- 0 nouvelle 301 cette semaine (cadence 1 URL en 6 semaines).

## 3. Anomalies mineures

### M1. 31/38 title ≠ h1 — 7e récurrence

- Méthode stricte (nettoyage suffixe nom de site). Pattern éditorial stable : title = requête commerciale, h1 = accroche narrative.
- 7 pages où title ≈ h1 : `/etudes-de-cas-seo-b2b/`, `/consultants-seo/`, `/skills/`, `/skills-seo/`, `/mentions-legales/`, `/politique-confidentialite/`, `/guides/en/audit-seo-technique-claude.html`.
- Les 5 nouvelles entrées se répartissent 2 title=h1 (`/etudes-de-cas-seo-b2b/`, `/skills-seo/`) et 3 title≠h1 (`/glossaire/`, les 2 calculateurs). Pas de pattern unique côté nouvelle entrée.

### M2. 6/38 pages sans `<meta name=robots>` — 7e récurrence stable

- Mapping gabarit léger stable : `/agent-seo/`, `/en/agent-seo/`, `/skills/`, `/x-ray/`, les 2 guides `.html`.
- Les 5 nouvelles entrées de la semaine portent toutes `<meta name=robots content="index, follow">`. Le gabarit léger n'est plus utilisé pour les nouvelles pages.

### M3. `/guides/` hub ne lie toujours pas ses 2 `.html` du sitemap — 7e récurrence

- Extraction `<a href>` : liste 7 PDF + pages site, 0 lien vers `/guides/audit-seo-technique-claude.html` et `/guides/en/audit-seo-technique-claude.html` (10 173 mots cumulés).
- Les 2 `.html` restent orphelines strict (C5).

### M4. `/plan-du-site/` restauration partielle : 32 ancres sortantes

- 104 mots (vs 94 au 2026-10-26, 151 au 2026-10-19, 170 au 2026-09-21).
- Ancres sortantes : **32** (vs ≈11 au 2026-10-26, ≈41 au 2026-10-12). Restauration 78 % du maillage sortant.
- Reste orpheline strict (C5) : le hub maillant est lui-même absent du maillage.

### M5. `/systeme-seo/` (hors sitemap, `noindex, follow`) : 99 inbound (vs 30 au 2026-10-26)

- +69 inbound en 7 jours. Dépasse le niveau du 2026-10-19 (77 inbound).
- Page toujours servie HTTP 200, 4 077 mots, `noindex, follow` sur balise.
- Canal nav vers URL noindex restauré et dépassé. Pattern paradoxal persistant : URL hors sitemap `noindex` recevant plus d'inbound que la plupart des pages dans sitemap.

### M6. `/audit/` (hors sitemap) : 83 inbound (vs 30 au 2026-10-26)

- +53 inbound en 7 jours. Dépasse le niveau du 2026-10-19 (63 inbound).
- 237 mots, pas de `<meta name=robots>` (indexable par défaut).
- Canal nav vers URL « audit » clairement privilégié : 83 inbound sur `/audit/` vs 0 sur `/audit-seo/`.

### M7. `/tarifs/` hors sitemap — 11e récurrence (65 jours)

- HTTP 200, canonical auto-ref, `index, follow`, 771 mots.
- **7 inbound** (vs 5 au 2026-10-26). Léger rebond.
- Page commerciale toujours doublement invisible : absente du sitemap et sous-maillée.

### M8. `/wiki/*` : fin du raffinement `#audit` confirmée pour la 2e semaine

- 4/4 slugs testés redirigent uniformément vers `/systeme-seo/` nu : `featured-snippet`, `topical-authority`, `passage-ranking`, `rrf`.
- Pattern stable, aligné avec la nav simplifiée.

## 4. Résolution des prédictions du 2026-10-26

| ID | Verdict | Détail |
|---|---|---|
| pred-2026-10-26-lastmod-uniforme | **hit** | 38/38 URLs lastmod uniforme `2026-11-02T06:00:55.354Z`, 24e récurrence 145j |
| pred-2026-10-26-orphans-5pages | **hit** | Mêmes 5 orphelines strict (`/plan-du-site/`, `/audit-seo/`, `/en/agent-seo/`, 2 guides `.html`) à 0 inbound |
| pred-2026-10-26-maillage-reversion | **miss** | Prédit [300, 420] arêtes (palier post-restructuration) ; mesure 1 063 arêtes (885 sur 33 URLs communes). Rebond MASSIF à contre-sens, hors fourchette supérieure. Note dans `mistakes.jsonl` |
| pred-2026-10-26-manifeste-404 | **hit** | 20e récurrence 404 nu |
| pred-2026-10-26-blog-cadence | **hit** | 0 nouvelle 301 `/blog/*` cette semaine (prédit ≤ 1), 1/4 slug stable |
| pred-2026-10-26-blog-hub-wordcount | **hit** | `/blog/` wc=73 (prédit ≤100), hub thin confirmé |
| pred-2026-10-26-sitemap-size | **miss** | Prédit [32, 35] URLs ; mesure 38 URLs (+5 d'un coup). Hors fourchette supérieure. Note dans `mistakes.jsonl` |
| pred-2026-10-26-pages-offre-recovery | **hit** | 3 pages d'offre à 1 inbound chacune (prédit ≤5) |

6 hit, 2 miss. Les deux miss (maillage et sitemap-size) révèlent une accélération éditoriale de grande ampleur : la cadence prédit un ralentissement, le site accélère. Pattern à surveiller.

## 5. Recommandations priorisées

### P1 (identique depuis 2026-06-10, 145 jours sans effet) — poser 301 ou 410 sur `/manifeste{,/}`

- Options techniquement prouvées sur ce domaine :
  - **410** : signalétique de retrait stable depuis 28 jours sur `/methode/` et `/bootcamp/` (`HTTP 410` + `x-robots-tag: noindex`).
  - **301** : vers `/systeme-seo/` (page `noindex, follow` mais finie et pérenne).
- Préférence méthodique : 410 si décision éditoriale assumée, sinon 301 vers `/systeme-seo/`.
- Mesure attendue sous J+14 (via `urlInspection` quand le diff sera appliqué) : disparition de l'URL de l'index Google.

### P2 (identique depuis 2026-06-15, 145 jours sans effet) — `lastmod` différencié par URL

- Le lastmod uniforme `2026-11-02T06:00:55.354Z` sur 38/38 URLs écrase le signal de fraîcheur sur les 5 vraies nouveautés de la semaine (`/glossaire/`, `/etudes-de-cas-seo-b2b/`, 2 calculateurs, `/skills-seo/`) et sur les pages réellement modifiées.
- Coût : adaptation du générateur de sitemap pour écrire la mtime effective (ou la date du dernier commit) par URL.

### C3 (nouveau, pages d'offre non rachetées) — brancher les 3 pages d'offre à la nav restaurée

- `/accompagnement-seo-geo/`, `/formation-seo-ia/`, `/consultant-lead-seo/` : toujours à 1 inbound après rebond général.
- La nav restaurée a privilégié `/`, les pages consultant-* et les pages légales. La classe « offres » reste exclue.
- Reco : ajouter une rangée « Offres » dans le footer (déjà porteur de ~15 ancres), ou référencer ces 3 pages depuis `/consultant-geo/`, `/consultant-seo-saas/`, `/consultants-seo/` qui ont 60-65 inbound chacune.

### C8 (nouveau, `/skills-seo/`) — mailler la plus grosse page du site

- 9 187 mots, 1 inbound seulement : plus gros contenu du sitemap, invisible au maillage.
- Pattern déjà vu sur `/consultant-geo/` fin septembre, racheté par `/plan-du-site/` enrichi puis nav restaurée.
- Reco : brancher `/skills-seo/` à `/`, `/plan-du-site/`, `/skills/` (pages à fort inbound actuel) sous J+7.

### P4 (identique depuis 2026-07-10, 115 jours sans effet) — brancher `urlInspection` API

- Diff posé dans `memory/questions.md` toujours en attente.
- Chaque semaine qui passe sans accès rend non mesurable l'impact des mouvements de restructuration.
- Impact 2 semaines consécutives : -217 arêtes (2026-10-26) puis +667 arêtes (2026-11-02), aucun des deux chocs ne peut être mesuré en SERP.

### C5 (7e récurrence) — réparer les orphelines strict chroniques

- `/plan-du-site/` doit se référencer dans la nav ou le pied-de-page (lui-même orphelin alors qu'il porte 32 ancres sortantes restaurées).
- `/guides/` doit lier ses 2 pages `.html` (le hub ne lie que les PDF).
- `/en/agent-seo/` doit recevoir ≥ 1 lien `<a>` depuis `/agent-seo/` (hreflang seul ne suffit pas en comptage strict).
- `/audit-seo/` doit recevoir ≥ 1 lien `<a>` depuis une page nav-linkée, ou être désindexé (meta noindex + sortie sitemap). L'écart avec `/audit/` (83 inbound hors sitemap) rend la situation incohérente.

## 6. Trajectoire sitemap 143 jours

`169-136-143-143-146-146-330-330-332-333-334-334-142-91-91-88-28-29-30-30-31-31-33-38`

(+5 cette semaine après 5 semaines de +1 ou +2, 6e semaine d'expansion consécutive. Cadence qui accélère.)
