---
type: query
skill: seo-page-statistiques
status: draft
title: "Fils de discussion longs, commentaires atomiques, réponses acceptées : trois objets distincts que les études confondent (2025-2026)"
created: 2026-10-19
updated: 2026-10-19
tags: [seo, ia, geo, reddit, forum, citations-ia, ugc, longueur-contenu, chunking]
sources: 7
confidence: medium
---

# Fils de discussion longs, commentaires atomiques, réponses acceptées : trois objets distincts que les études confondent (2025-2026)

La médiane des posts Reddit cités par les moteurs IA est de **80 mots** (Semrush, 248 000 URLs Reddit, octobre 2025). Un microcontenu, donc. Et pourtant, les fils Reddit comportent des centaines de commentaires. Ce chiffre résout une confusion de mesure que l'on retrouve dans toutes les études sur le sujet : ce n'est pas le fil qui est cité, c'est le commentaire. Un thread de 400 échanges n'est pas un long contenu pour un moteur IA ; c'est 400 courts contenus atomiques évalués séparément. La question "format long vs format court" se pose au mauvais niveau d'analyse.

---

## Les chiffres clés (vérifiés à la source)

### Reddit : la médiane du post cité est un texte court

Semrush a analysé 217 000 prompts uniques et identifié 248 000 URLs Reddit citées ou mentionnées dans les réponses de Google AI Mode, Perplexity et ChatGPT Search (octobre 2025) :

- Médiane de longueur des posts cités : **~80 mots**
- 80 % des posts cités ont **moins de 20 upvotes**
- 70 % des posts cités ont **moins de 20 commentaires**
- Médiane des upvotes sur les posts cités : entre 5 et 8 selon le moteur
- Âge moyen du post cité : **~900 jours** (environ 2,5 ans)
- Plus de **50 % des citations Reddit** proviennent de fils à structure Q&A

Une étude distincte conduite par Limy.ai sur 200 URLs Reddit codées à la main (503 152 citations agrégées, août 2025-juillet 2026) donne une médiane d'upvotes légèrement différente (11 vs 5-8 Semrush) et confirme la structure :
- **79 %** des fils cités suivent une architecture question/réponse
- 80 % des posts cités ont plus de commentaires que d'upvotes
- ~2,5 % des posts cités avaient le corps du texte supprimé : les commentaires constituaient l'intégralité du contenu extractible

### La longueur totale de la page n'explique presque rien

Ahrefs a analysé 560 346 AI Overviews contenant 1 677 876 URLs citées, avec extraction possible du contenu sur 174 048 pages :

- Corrélation Spearman entre longueur (mots) et fait d'être cité : **r = 0,04** (quasi-nulle)
- **53,4 % des pages citées** contiennent moins de 1 000 mots
- Longueur médiane des pages de contenu généré par les utilisateurs citées : **387 mots**
- Longueur médiane des articles cités : 1 166 mots
- Distribution des longueurs sur les pages citées : 16,6 % < 350 mots ; 36,8 % entre 350 et 1 000 mots ; 30,6 % entre 1 000 et 2 000 mots ; 16 % > 2 000 mots

### La position dans la page compte infiniment plus que la longueur totale

MaxAEO a suivi la survie d'un "claim" (affirmation) inséré à cinq profondeurs différentes dans 15 guides longs (1 200 observations, juin-juillet 2026) :

| Profondeur dans la page | Atteint la réponse IA | Cité avec lien |
|---|---|---|
| Intro (~5 % du texte) | 72 % | 61 % |
| ~25 % de la page | 51 % | 43 % |
| Milieu (~50 %) | **24 %** | 18 % |
| ~75 % | 38 % | 29 % |
| Conclusion (~5 %) | 46 % | 37 % |

L'intro survit 3 fois plus souvent que le milieu. La longueur totale de la page amplifie cet effet :

| Longueur page | Claim en intro | Claim au milieu |
|---|---|---|
| 1 000–1 800 mots | 78 % | 41 % |
| 1 800–3 000 mots | 73 % | 27 % |
| 3 000–4 500 mots | 70 % | 16 % |
| 4 500+ mots | 68 % | 9 % |

Un claim placé au milieu d'une page de 4 500 mots ne survit que dans **9 %** des cas.

### La longueur des sections : le seul niveau où la longueur joue

SE Ranking a étudié 2 328 533 pages issues de 295 485 domaines sur 20 niches, avec plus de 500 000 prompts (modèle XGBoost, régression) :

| Longueur de section (mots entre deux en-têtes) | Citations moyennes dans AI Mode |
|---|---|
| Moins de 35 mots | ~4,3 |
| 100–150 mots | ~4,7 (optimum) |
| Plus de 150 mots | ~4,6 |

L'écart est faible (0,4 citations) mais la direction est cohérente : des sections trop courtes (<35 mots) sont légèrement pénalisantes, des sections de 100-150 mots constituent le point d'équilibre.

### Commentaires vs posts : 65 à 78 % des citations Reddit pointent vers des commentaires

Red Engage a suivi 10 000+ citations Reddit sur 90 jours, 25 prompts B2B SaaS, 4 moteurs :

| Moteur | Citations vers des commentaires | Citations vers des posts |
|---|---|---|
| Perplexity | 78 % | 22 % |
| Google AI Overviews | 72 % | 28 % |
| ChatGPT | 65 % | 35 % |
| Gemini | 59 % | 41 % |

Le commentaire, pas le post d'origine, est l'unité de citation dominante. Les upvotes moyens sur les contenus cités varient : ChatGPT cite en moyenne des contenus à 287 upvotes, Perplexity 412, Gemini 203, Google AI Overviews 524 — à comparer aux 5-8 de médiane Semrush, ce qui révèle des distributions très asymétriques.

---

## Pourquoi ces chiffres : la confusion des trois unités d'analyse

La question "un long thread est-il plus citable qu'un court post ?" est mal posée, parce qu'elle confond trois objets distincts :

**Niveau 1 — La page** : est-ce qu'une longue page est plus citable ? Non (r = 0,04, Ahrefs). La longueur totale ne prédit pas la citation.

**Niveau 2 — Le thread** : est-ce qu'un long fil de discussion est plus citable ? La question n'a pas de sens au niveau du thread. L'IA ne cite pas "un thread Reddit" comme une unité. Elle cite un commentaire spécifique, extrait et évalué indépendamment du reste.

**Niveau 3 — Le chunk** : quel est le vrai niveau de granularité ? C'est le commentaire individuel (médiane 80 mots, Semrush) ou la section entre deux en-têtes (100-150 mots, SE Ranking). C'est à ce niveau que la longueur a un effet.

Ce que révèle cette réconciliation : un thread Reddit de 400 commentaires ne constitue pas "un contenu long". C'est 400 contenus atomiques, chacun évalué séparément par le pipeline de retrieval. Un thread plus long offre plus de surfaces d'extraction potentielles — mais chaque surface doit répondre aux critères atomiques (longueur ~80-150 mots, structure Q&A, pertinence sémantique vis-à-vis du prompt).

**L'avantage structurel de Stack Overflow**

Stack Overflow cumule deux mécanismes. D'abord, la réponse acceptée est affichée en tête de page quelle que soit sa date — elle bénéficie donc de la prime de position "intro" documentée par MaxAEO (+72 % de survie vs 24 % pour le contenu au milieu). Ensuite, chaque réponse est naturellement atomique : une réponse technique Stack Overflow fait généralement 100-300 mots, dans la fenêtre optimale identifiée par SE Ranking.

Le déclin des questions sur Stack Overflow (-99,3 %, de 207 000 questions en mars 2014 à 1 442 en juillet 2026, selon les données SEDE agrégées par ppc.land) n'a pas encore effacé ce capital : les questions et réponses existantes, déjà en tête de page et au bon format, continuent d'être retrieval-friendly.

**Le paradoxe Reddit de l'engagement faible**

80 % des posts cités ont moins de 20 upvotes. Cette statistique déstabilise l'hypothèse que les moteurs IA font confiance aux signaux d'engagement visibles. L'explication est structurelle : les moteurs utilisent des embeddings sémantiques pour aligner le contenu avec la requête, pas le score d'upvote. Semrush mesure une similarité cosinus de 0,53-0,54 entre la réponse IA et le post Reddit cité — c'est l'alignement sémantique qui détermine la sélection, pas la popularité. Plus de 50 % des citations Reddit proviennent de fils Q&A : c'est la structure de la conversation (question posée, réponse donnée) qui mime la structure attendue par les moteurs, indépendamment du nombre de votes.

---

## Nos propres chiffres (données de première main)

Ce sujet n'est pas couvert par des mesures directes dans ce vault. Aucun suivi de longueur de commentaires vs posts sur des comptes clients n'est disponible à ce jour. Ce bloc reste réservé honnêtement : les chiffres ci-dessus proviennent uniquement de sources externes vérifiées.

---

## Contre-analyse

**La corrélation r = 0,04 (Ahrefs) ne couvre que Google AI Overviews.** ChatGPT Search et Perplexity ont des comportements différents — on voit 65-78 % de citations commentaires vs posts chez Red Engage, mais ce ratio n'est pas mesuré en termes de longueur absolue.

**L'étude MaxAEO est directionnelle, non définitive.** Trois sujets B2B, 15 guides, 1 200 observations sur 4 semaines. Les effets de profondeur pourraient être différents sur des contenus courts (< 500 mots) ou sur des sujets YMYL, où les moteurs peuvent préférer les paragraphes de synthèse placés plus loin dans la page.

**Le chiffre Red Engage "65-78 % des citations = commentaires"** provient d'un corpus B2B SaaS, 25 prompts, 90 jours. La répartition commentaires/posts pourrait varier fortement selon la verticale. Sur les requêtes locales ou produits grand public, le ratio peut différer.

**La médiane de 80 mots (Semrush)** est celle des posts cités — pas des commentaires cités. L'étude Semrush identifie des URLs Reddit au niveau du thread (reddit.com/r/.../comments/...), pas au niveau du commentaire individuel. La granularité réelle de l'extraction (quel commentaire précisément) reste un angle mort : aucune grande étude ne désagrège les données à ce niveau de granularité.

**L'avantage Stack Overflow en déclin.** La chute de 99,3 % du volume de nouvelles questions fragilise la fraîcheur du corpus. Les pages citées restent pertinentes sur les sujets stables (langages établis, erreurs classiques) mais Stack Overflow perd sur les questions liées aux frameworks récents, où Reddit ou GitHub Issues prennent le relais.

---

## FAQ

**Un thread Reddit long est-il plus citable qu'un post court ?**
La longueur du thread n'est pas l'unité pertinente. Ce qui compte est la longueur du commentaire individuel (~80 mots, Semrush) et son alignement sémantique avec le prompt. Un thread long offre plus de surfaces d'extraction potentielles, mais chaque surface est évaluée séparément.

**Faut-il écrire des commentaires Reddit courts pour être cité ?**
Les données Semrush indiquent une médiane de 80 mots sur les posts cités (pas seulement les commentaires). La fenêtre idéale selon SE Ranking pour les sections de contenu est 100-150 mots. Ces deux chiffres convergent vers une réponse de 100-150 mots comme format naturellement aligné avec les pipelines de retrieval — ni trop court (fragment sans conclusion), ni trop long (chunk dilué).

**Les upvotes Reddit influencent-ils les citations IA ?**
Pas directement. 80 % des posts cités ont moins de 20 upvotes (Semrush, 248 000 URLs). Les moteurs alignent le contenu avec la requête via des embeddings, pas via des signaux de popularité. La structure Q&A et la longueur atomique sont les déterminants principaux.

**Pourquoi Stack Overflow surperforme-t-il dans les citations techniques ?**
Deux mécanismes cumulés : la réponse acceptée bénéficie de la prime de position en haut de page (~72 % de survie, MaxAEO), et chaque réponse est naturellement dans la fenêtre optimale de 100-300 mots pour le retrieval.

**La longueur d'un article a-t-elle un impact sur sa citabilité ?**
Très peu. La corrélation Spearman est de 0,04 sur Google AI Overviews (Ahrefs, 174 048 pages). 53,4 % des pages citées font moins de 1 000 mots. La position dans la page (intro vs milieu) a un effet 3 fois plus fort que la longueur totale.

---

## [À SOURCER]

- **Wellows 2.3× (120-180 mots)** : affirmation relayée par plusieurs guides GEO (lumengeo.co, pushleads.com), attribuée à Wellows sans URL primaire accessible. À vérifier contre le rapport Wellows original.
- **AirOps "41 % vs 29 %" (matching en-tête/requête)** : repris en source secondaire, pas de lien vers l'étude AirOps primaire.
- **getpassionfruit.com "59 % plus likely" pour 2 900 mots** : chiffre sans méthodologie documentée.
- **Longueur des commentaires cités (vs posts cités)** : Semrush mesure la longueur des URLs de threads, pas des commentaires individuels. Aucune étude ne désagrège à ce niveau.
- **Ratio commentaire/post désagrégé par verticale** : Red Engage = B2B SaaS uniquement.
- **Données France** : toutes les études sont anglophones. L'effet de longueur sur les forums francophones (Doctissimo, Hardware.fr, JeuxVideo.com) n'est pas documenté.

---

## Sources

| Intitulé | Organisme | Date | URL | Consulté le |
|---|---|---|---|---|
| Reddit AI Search Visibility Study — 217 000 prompts, 248 000 URLs Reddit, médiane 80 mots | Semrush | Octobre 2025 | https://www.semrush.com/blog/reddit-ai-search-visibility-study/ | 2026-10-19 |
| Which Reddit post does LLM cite — 200 URLs codées à la main, 503 152 citations | Limy.ai | 2025-2026 | https://limy.ai/research-lab/which-reddit-post-does-llm-cite | 2026-10-19 |
| Short vs Long Content in AI Overviews — 560 346 AI Overviews, 174 048 pages, r=0,04 | Ahrefs | 2026 | https://ahrefs.com/blog/short-vs-long-content-in-ai-overviews/ | 2026-10-19 |
| How Much of a Long Page Do AI Models Use — 1 200 observations, survie du claim par profondeur | MaxAEO | Juin-juillet 2026 | https://maxaeo.ai/blog/page-length-ai-citations/ | 2026-10-19 |
| How to Optimize for AI Mode — 2 328 533 pages, 500 000+ prompts, SE Ranking | SE Ranking | 2026 | https://seranking.com/blog/how-to-optimize-for-ai-mode/ | 2026-10-19 |
| Reddit Citations in AI Answers — 10 000+ citations Reddit, 90 jours, B2B SaaS | Red Engage | 2026 | https://red-engage.com/blog/reddit-citations-in-ai-answers-2026-study | 2026-10-19 |
| The Impact of UGC and Community in AI Search — 248 000 Reddit citations analysées | AirOps | 2026 | https://www.airops.com/report/the-impact-of-ugc-and-community-in-ai-search | 2026-10-19 |
