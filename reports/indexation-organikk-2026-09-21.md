---
type: audit
title: Indexation Organikk — audit hebdomadaire 2026-09-21
created: 2026-09-21
updated: 2026-09-21
tags: [indexation, sitemap, audit, organikk, hebdo]
status: stable
confidence: high
sources: 3
---

# Audit indexation Organikk — 2026-09-21

**Périmètre.** organikk.co, 28 URLs listées dans `sitemap.xml` (delta -60 vs 14/09 : 88 → 28). Lecture seule sur le web public. Aucun forçage d'indexation.

**Sources de vérité utilisées.**
- Statut HTTP `curl` (première réponse + redirection résolue).
- Présence dans `sitemap.xml` + `lastmod`.
- `robots.txt`.
- Parsing HTML servi : `<title>`, `<h1>`, `<link rel=canonical>`, `<meta name=robots>`, graphe interne (hrefs internes).

**Non testable.** Statut d'indexation Google réel. Pas d'accès à l'edge `admin-gsc-export` (`urlInspection` / `searchAnalytics`) dans cet environnement. Diff proposé le 10/07 pour remplacer le check #8 mort par un appel à l'API URL Inspection : **73 jours d'ouverture**. Voir `loops/indexation-check/memory/questions.md`.

## 1. Synthèse

Semaine de **restructuration majeure** : le sitemap se contracte de 88 → 28 URLs (-60, -68 %). Deux sections entières disparaissent : le namespace `/wiki/*` (folded en 301 blanket → `/systeme/`) et le blog (`/blog/*` réponds désormais 404 nu, sans redirection).

- **Sitemap divisé par trois en 7 jours.** 28 URLs restent : 22 landing pages (`/`, `/systeme/`, `/methode/`, `/etudes-de-cas/`, `/chaine-youtube-seo/`, `/contact/`, `/resultats/`, `/guides/`, `/avis/`, `/plan-du-site/`, `/accompagnement-seo-geo/`, `/accompagnement-1-1-30-jours/`, `/consultant-lead-seo/`, `/consultant-geo/`, `/formation-seo-ia/`, `/bootcamp/programme/`, `/bootcamp-quiz/`, `/skills/`, `/coaching-seo-lyon/`, `/a-propos/`, `/bootcamp/`, `/bootcamp-candidature/`), 2 pages légales, 2 pages `/agent-seo/` (FR + EN), 2 guides `.html` (FR + EN). Trajectoire sitemap 105j : 169-136-143-143-146-146-330-330-332-333-334-334-142-91-91-88-**28**.
- **`/blog/*` massivement 404.** Test spot sur 4 anciens articles-poteaux du maillage (`/blog/process-seo-b2b-2026/`, `/blog/information-gain-geo/`, `/blog/9-skills-seo-claude/`, `/blog/wiki-ia-obsidian-claude/`) : 4/4 en HTTP 404 nu, aucune redirection posée. La racine `/blog{,/}` répond aussi 404. Le blog était le pilier de linkjuice interne (22, 21, 15, 11 backlinks sur les 4 articles-poteaux au 14/09). Tout est perdu sans 301.
- **`/wiki/*` folded en 301 blanket → `/systeme/`.** Les 49 slugs testés (22 anciens 404 nu + 27 déjà 301 la semaine dernière) redirigent tous 301 vers `/systeme/`. La reco P3a du 14/09 (poser une 301 par slug vers le concept survivant le plus proche) est **partiellement appliquée en blanket** : la redirection existe mais elle est uniforme, pas ciblée. Toute la sémantique par-concept est perdue à l'atterrissage.
- **`sitemap_canonical_mismatch` résolu.** 26/28 URLs portent le slash final dans `<loc>` (les 2 exceptions sont les `.html` littérales, correctes ainsi). Les 28/28 sont servies en HTTP 200 direct, plus aucun 301 slash-canonical. **Fin d'une récurrence de 16 semaines / 96 jours.**
- **`/manifeste` reste 404** pour la **14e semaine consécutive** (103 jours depuis la reco P1 du 10/07).
- **Pages commerciales toujours orphelines** : `/accompagnement-seo-geo/`, `/consultant-geo/`, `/consultant-lead-seo/`, `/formation-seo-ia/`, `/plan-du-site/` conservent chacune **0 backlink interne réel** sur les 28 pages téléchargées (leur unique « backlink » est leur propre canonical/URL dans leur propre HTML — auto-référent, sans valeur de maillage).
- **`/tarifs` toujours hors sitemap** (4e récurrence, 21 jours) mais servie 200 avec 1 seul backlink externe (`/coaching-seo-lyon/` → `/tarifs/`).
- **`lastmod_uniforme` continue** : 28/28 URLs partagent `2026-09-21T03:16:06.868Z` (17e récurrence, 103 jours).

**Chiffres du run.** 28/28 HTTP 200 direct (0 redirect sur les URLs sitemap). 28/28 avec `<title>`, `<h1>` et `<link rel=canonical>` auto-référent. 23/28 avec `<meta name="robots">` explicite `index, follow` (les 5 sans meta robots sont `/skills/`, `/agent-seo/`, `/en/agent-seo/`, `/guides/*.html` FR+EN). 0 `noindex` sur méta robots. `robots.txt` inchangé (politique minimale `User-Agent:* / Allow:/ + Sitemap`).

## 2. Anomalies critiques

### C1. `/blog/*` entièrement 404 sans redirection — nouveau MAJEUR

- `curl -sI https://organikk.co/blog{,/}` → HTTP 404.
- Test échantillon sur 4 anciens articles-poteaux (les plus liés au 14/09) :
  - `/blog/process-seo-b2b-2026/` → 404 (21 backlinks internes au 14/09).
  - `/blog/information-gain-geo/` → 404 (22 backlinks au 14/09).
  - `/blog/9-skills-seo-claude/` → 404 (15 backlinks au 14/09).
  - `/blog/wiki-ia-obsidian-claude/` → 404 (11 backlinks au 14/09).
- Aucune redirection posée. Le blog complet a été supprimé de l'arborescence, sans pipeline de 301 vers `/guides/` ou `/systeme/`.
- Impact SEO : perte sèche du linkjuice historique. Toutes les URLs qui ont capitalisé des backlinks externes ou des positions SERP renvoient un signal « page absente » à Google, sans instruction sur où réallouer le score.
- Reco P2c du 14/09 s'appuyait explicitement sur `/blog/process-seo-b2b-2026/` et `/blog/information-gain-geo/` comme candidates fortes pour mailler les pages commerciales orphelines. Ces candidates n'existent plus.
- Aveuglement critique sans accès `urlInspection` : impossible de mesurer combien de trafic ou de citations IA sont perdus.

### C2. `/manifeste` 404 — 14e récurrence (103 jours)

- `curl -sI https://organikk.co/manifeste{,/}` → HTTP 404.
- Absente du sitemap.
- 0 backlink interne sur les 28 pages téléchargées.
- Reco P1 du 10/07 (301 vers `/systeme/` ou refonte) non appliquée depuis 103 jours.
- Note : dans le grand refactoring wiki en 301-blanket → `/systeme/`, la même règle aurait dû s'appliquer ici. Elle ne l'a pas été.

### C3. `/wiki/*` folded en 301 blanket → `/systeme/` — reco P3a partiellement appliquée

- 49/49 slugs `/wiki/*` testés redirigent 301 → `https://organikk.co/systeme/`.
- Réponse à P3a du 14/09 : la mécanique de redirection est corrigée (fin de l'asymétrie 22 slugs 404 nu vs 27 slugs 301). Prédiction `pred-2026-09-14-wiki-404-nu` invalidée.
- **Mais la redirection est uniforme, pas concept-à-concept.** Google atterrit toujours sur la même URL générique, sans indice de continuité thématique par slug. Impact : perte de la spécificité sémantique héritée par chaque slug, dilution du signal de correspondance.
- La reco P3a proposait un mapping ciblé (`e-e-a-t → grounding-score`, `sge → agentic-search`, `bert → passage-ranking`…) qui n'est pas suivi. Choix éditorial ou raccourci de build ? À trancher.

### C4. `/tarifs` toujours hors sitemap — 4e récurrence (21 jours)

- HTTP 200 direct sur `/tarifs/`. Servie fonctionnellement.
- Absente du sitemap depuis le 05/09.
- **1 backlink externe** seulement (`/coaching-seo-lyon/`), contre 91/91 backlinks nav au 07/09.
- La page qui devrait porter la conversion vers l'offre coaching est en double-invisibilité (hors sitemap + quasi hors maillage).
- Reco P2b du 14/09 (ajouter au sitemap) non appliquée depuis 7 jours.

### C5. Pages commerciales orphelines — récurrences chroniques

Backlinks externes réels (hors auto-référence) sur les 28 pages téléchargées :

| Page | Backlinks externes | Récurrence | Jours depuis reco |
|---|---|---|---|
| `/accompagnement-seo-geo/` | 0 | 13e | 103 j |
| `/consultant-geo/` | 0 | 8e | 42 j |
| `/formation-seo-ia/` | 0 | 7e | 35 j |
| `/consultant-lead-seo/` | 0 | 2e | 7 j |
| `/plan-du-site/` | 0 | 2e | 7 j |

- Toutes présentes dans le sitemap, HTTP 200, canonical propre.
- Toutes structurellement invisibles aux crawlers via le graphe interne.
- Reco P2c du 14/09 (3-5 backlinks depuis pages fortes) inapplicable en l'état : les candidates fortes proposées (`/blog/process-seo-b2b-2026/`, etc.) sont maintenant 404. Nouveau donneur de linkjuice à trouver dans le périmètre restant (probablement `/systeme/`, `/methode/`, `/guides/`).
- Note : `/plan-du-site/` est un contre-emploi structurel — une page plan-du-site sans backlink entrant depuis le footer ou l'accueil ne remplit pas sa fonction. Son propre contenu servi ne lie que 17 pages internes (dont 12 sur les 28 du sitemap) — elle ne référence aucune des 5 pages orphelines ci-dessus.

### C6. `lastmod_uniforme` — 17e récurrence (103 jours)

- Les 28 URLs du sitemap partagent le même `<lastmod>2026-09-21T03:16:06.868Z</lastmod>` (mise à jour globale du 21/09 à 03:16 UTC sur toutes les URLs).
- Le signal de fraîcheur relatif entre URLs reste perdu.
- Reco P1c du 14/09 (émettre un `lastmod` par URL depuis la source éditoriale) non appliquée depuis 103 jours.

## 3. Anomalies mineures

### M1. `/skills/` reste thin — 47 mots servis

- HTTP 200 direct, canonical auto-référent, title et h1 propres.
- **47 mots dans le HTML servi** (méthode body strippé de header/footer/scripts), en baisse vs 66 mots au 14/09.
- Seuls 2 liens internes sortants dans le corps (`/agent-seo/`, `/skills/` auto). C'est la page la plus fine du site.
- 25 backlinks entrants (élément de nav globale sur 25/28 pages) : la structure d'accueil pousse fort vers une page qui, servie en curl, n'a presque aucun contenu ni sortie.
- Deux hypothèses concurrentes toujours ouvertes (M1 14/09) : (a) rendu client-side Next.js non capturé par curl ; (b) landing page volontairement légère. À trancher par test headless (Chrome `--dump-dom`) au prochain run.

### M2. Divergence `title` vs `h1` sur 26/28 pages

- Méthode stricte (title débarrassé du suffixe `· Organikk`, `| Organikk` ou similaire vs h1) : **26/28 pages divergent**. Seules `/mentions-legales/` et `/politique-confidentialite/` ont un `title` et un `h1` alignés.
- Le decoupling reste vraisemblablement éditorial (title = promesse fonctionnelle avec suffixe de marque, h1 = accroche narrative). Pas un bug par défaut, mais un pattern à trancher explicitement en revue hebdo.
- Trajectoire : 24 (07/09) → 82 (14/09, méthode stricte) → 26 (21/09). Confirme que la méthode de comptage change les chiffres — la lecture inter-runs doit rester sur une seule méthode.

### M3. `/plan-du-site/` : 170 mots servis, 17 liens internes mais 5 orphelines absentes

- HTTP 200, dans le sitemap.
- 17 liens internes uniques sortants — c'est un plan de site fonctionnel côté navigation.
- **Mais absentes** de ses sorties : `/accompagnement-seo-geo/`, `/consultant-geo/`, `/consultant-lead-seo/`, `/formation-seo-ia/`, `/tarifs/`. Les 5 pages qui devraient bénéficier en priorité d'un lien depuis un plan-de-site n'y figurent pas.
- La fonction éditoriale de la page contredit sa position dans le graphe interne.

### M4. 5 pages sous 400 mots dans le sitemap

- `/skills/` 47 mots, `/contact/` 162 mots, `/plan-du-site/` 170 mots, `/resultats/` 204 mots, `/guides/` 339 mots, `/avis/` 378 mots.
- `/contact/` et `/resultats/` sont fonctionnelles par nature.
- `/skills/` et `/plan-du-site/` méritent inspection (voir M1 et M3).
- `/guides/` 339 mots est une hub-page ; à vérifier qu'elle porte assez d'ancres vers les 2 guides HTML pour justifier son rôle de porte d'entrée sur le contenu long-form.

### M5. Aveuglement `urlInspection` — 73 jours

- Le run continue de fonctionner sur les couches A (HTTP) et C (maillage/contenu) mais reste aveugle sur la couche B (statut d'indexation Google réel). Cela fait 73 jours que le diff est en attente dans `memory/questions.md`.
- Impact particulièrement lourd ce run : impossible de mesurer combien de trafic est perdu sur `/blog/*` (C1), ni si Google sert encore ces URLs en SERP, ni si le blanket 301 `/wiki/* → /systeme/` (C3) fait perdre des positions par slug.

## 4. Positifs

- **`sitemap_canonical_mismatch` résolu.** 26/28 URLs sitemap portent le slash final dans `<loc>`, 2 exceptions correctes (`.html` littérales). 28/28 servies en HTTP 200 direct, plus aucun 301 slash-canonical sur URLs sitemap. **Fin d'une récurrence de 16 semaines.**
- **`/wiki/*` 404 nu fermé.** Les 22 slugs qui restaient en 404 nu au 14/09 redirigent maintenant tous 301 → `/systeme/`. L'asymétrie de pipeline signalée depuis 4 semaines est fermée (même si le mapping reste blanket, cf. C3).
- **Fondamentaux techniques stables au meilleur niveau.** 28/28 HTTP 200, `title`, `h1`, `canonical` auto-référent, 0 `noindex`. **8e semaine consécutive sans régression** sur les URLs présentes.
- **Contraction éditoriale nette et volontaire.** Le site opère un recentrage explicite sur 22 landing pages + 2 pages `/agent-seo/` (FR/EN) + 2 guides HTML. Cohérent avec un pivot de format (blog longform → guides HTML dédiés).

## 5. Recommandations priorisées

### Priorité 1 — Décider explicitement le sort du blog (C1)

- **P1a.** Trancher `/blog/*` : (i) poser des 301 depuis chaque ancien article vers le hub le plus proche (`/guides/`, `/systeme/`, `/methode/`) ou vers un article `/guides/...` équivalent ; (ii) accepter la perte sèche de linkjuice si le recentrage est volontaire ; (iii) restaurer les URLs 404 si la suppression est un accident de build.
- **P1b.** Le choix doit être fait cette semaine — chaque jour de 404 nu perdure la fuite de signal SEO sans instruction.
- **P1c.** Instrumentation minimale requise : lister toutes les URLs `/blog/*` qui étaient dans le sitemap au 14/09 (issue d'un backup ou d'un snapshot) et vérifier laquelle est 200 / 404 / 301 ce jour. À défaut, tirer les URLs `/blog/*` depuis les backlinks entrants historiques (source Ahrefs / GSC).

### Priorité 2 — Fermer les récurrences chroniques

- **P2a.** Trancher `/manifeste` : 301 vers `/systeme/` (ou refonte). **14e semaine sans action, 103 jours.**
- **P2b.** Ajouter `<loc>https://organikk.co/tarifs/</loc>` au sitemap. **21 jours d'absence.**
- **P2c.** Réparer `lastmod_uniforme` : émettre le `lastmod` réel par page depuis la source éditoriale. **103 jours sans action.**

### Priorité 3 — Restaurer le maillage sur les 5 pages commerciales orphelines (C5)

Sans le blog en donneur, redéployer le linkjuice depuis les pages centrales restantes :

- **P3a.** Injecter 3 à 5 backlinks contextuels depuis `/systeme/` (386 mots servi, 3 backlinks entrants — hub pauvre mais central), `/methode/` (10 backlinks entrants), `/etudes-de-cas/` (5 backlinks entrants) vers :
  - `/accompagnement-seo-geo/` (103 jours orpheline)
  - `/consultant-geo/` (42 jours)
  - `/formation-seo-ia/` (35 jours)
  - `/consultant-lead-seo/` (7 jours)
  - `/plan-du-site/` (7 jours — a besoin d'un lien depuis le footer minimum).
- **P3b.** Corriger `/plan-du-site/` : y ajouter les 5 pages absentes de ses sorties. C'est le fix le moins coûteux du run — une ligne par URL.

### Priorité 4 — Ciseler la redirection `/wiki/* → /systeme/` (C3)

- **P4.** Remplacer le blanket 301 uniforme par un mapping ciblé slug-à-slug quand un équivalent thématique existe côté `/systeme/` ou `/guides/`. Ne conserver le fallback `/systeme/` que pour les slugs sans correspondance directe. Coût : un fichier `_redirects` ou une règle `next.config.js`.

### Priorité 5 — Décision `/skills/` (M1)

- **P5.** Vérifier par test headless (Chrome `--dump-dom`) si `/skills/` sert du contenu client-side non capturé par curl. Si oui, décider si on l'expose côté SSR pour donner du grain aux crawlers légers (elle reçoit 25 backlinks internes — la structure d'accueil pousse fort vers une page qui, à 47 mots, ne peut rien restituer).

### Priorité 6 — Débloquer la mesure GSC (M5)

- **P6.** Statuer sur le diff `urlInspection` proposé le 10/07 dans `memory/questions.md`. Alternative : autoriser le brain à appeler directement l'edge `admin-gsc-export` depuis cet environnement (secret + URL). Sans cela, on continue à naviguer à vue sur la couche B après **73 jours d'ouverture** — particulièrement lourd cette semaine sur C1 et C3.

## 6. Trajectoire sitemap (105 jours)

169 → 136 → 143 → 143 → 146 → 146 → 330 → 330 → 332 → 333 → 334 → 334 → 142 → 91 → 91 → 88 → **28**.

- 15/06 → 27/06 : léger réajustement.
- 06/07 → 27/07 : passage au périmètre site entier + scale-up massif +184 URLs le 20/07.
- 27/07 → 24/08 : palier stable autour de 332-334.
- 31/08 : contraction -192 (sitemap tombe à 142).
- 05/09 → 07/09 : palier à 91.
- 07/09 → 14/09 : -3 URLs (91 → 88).
- 14/09 → 21/09 : **-60 URLs (88 → 28)**. Delta net : disparition intégrale du namespace `/wiki/*` (folded en 301 → `/systeme/`), disparition intégrale du namespace `/blog/*` (404 sans redirection), disparition de plusieurs landing pages secondaires (`/outils/analyse-geo/`, `/systeme-seo-ia/` restent servies 200 hors sitemap).

## 7. Predictions posées ce run

- `pred-2026-09-21-manifeste-404` — Sans redirection 301 posée, `/manifeste{,/}` sera encore en HTTP 404 au run du 2026-09-28 (15e récurrence). Resolve_by 2026-09-28.
- `pred-2026-09-21-orphans-persist` — Sans action de maillage cette semaine, les 5 pages commerciales orphelines (`/accompagnement-seo-geo/`, `/consultant-geo/`, `/consultant-lead-seo/`, `/formation-seo-ia/`, `/plan-du-site/`) resteront à 0 backlink externe sur les URLs du sitemap actif au run du 2026-09-28. Resolve_by 2026-09-28.
- `pred-2026-09-21-blog-404` — Sans pipeline de 301 posé, les 4 articles-poteaux du blog testés ce run (`/blog/process-seo-b2b-2026/`, `/blog/information-gain-geo/`, `/blog/9-skills-seo-claude/`, `/blog/wiki-ia-obsidian-claude/`) seront encore en HTTP 404 au run du 2026-09-28. Resolve_by 2026-09-28.
- `pred-2026-09-21-tarifs-sitemap` — `/tarifs` restera absente du sitemap au run du 2026-09-28 (5e récurrence). Resolve_by 2026-09-28.
- `pred-2026-09-21-wiki-301-blanket` — Sans mapping ciblé, les 49 slugs `/wiki/*` testés redirigeront toujours en blanket 301 → `/systeme/` au run du 2026-09-28. Resolve_by 2026-09-28.
- `pred-2026-09-21-lastmod-uniforme` — 28/28 URLs sitemap partageront encore le même `<lastmod>` au run du 2026-09-28 (18e récurrence). Resolve_by 2026-09-28.
- `pred-2026-09-21-canonical-fix-persist` — Le fix `sitemap_canonical_mismatch` tiendra : 0 URL sitemap sans slash final dans `<loc>` (hors `.html`) au run du 2026-09-28. Resolve_by 2026-09-28.

## 8. Predictions résolues ce run

- `pred-2026-09-14-manifeste-404` : **hit** — 14e récurrence, 103 jours sans action.
- `pred-2026-09-14-orphans-persist` : **hit** — 3 pages historiques toujours à 0 backlink externe (103, 42 et 35 jours d'inaction).
- `pred-2026-09-14-canonical-mismatch-fix` : **miss** — le fix a bien été appliqué ce run (26/28 URLs sitemap avec slash canonique en `<loc>`, 2 `.html` correctes). Prédiction disait « au moins 85/88 URLs sans slash au 21/09 ». **Bonne surprise éditoriale.**
- `pred-2026-09-14-wiki-404-nu` : **miss** — les 22 slugs 404 nu redirigent maintenant tous 301 → `/systeme/` (blanket). Prédiction disait « au moins 20/22 encore en 404 nu ». **Bonne surprise éditoriale**, sous réserve du mapping non ciblé (C3).
- `pred-2026-09-14-tarifs-sitemap` : **hit** — `/tarifs` toujours absente du sitemap, correction non appliquée.
- `pred-2026-09-14-nav-refactor-persist` : **hit** — la nav minimaliste reste en place ; ce run confirme que le refactoring nav est un choix éditorial durable, pas un accident.
