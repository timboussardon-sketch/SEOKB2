---
type: query
skill: seo-page-statistiques
status: draft
title: "Grok 4 Heavy, Perplexity Deep Research, ChatGPT o3 DR : trois moteurs, trois logiques de citation en mode recherche approfondie (2025-2026)"
tags: [deep-research, grok-4, perplexity, chatgpt-o3, citations-ia, benchmarks, precision-citation, seo, geo, aeo]
created: 2026-09-08
updated: 2026-09-08
sources: 10
confidence: medium
---

# Grok 4 Heavy récupère 190 pages mais n'en cite que 8 efficacement : le paradoxe des moteurs Deep Research en 2025-2026

Grok 4 Heavy est le premier modèle à dépasser 50 % sur l'examen Humanity's Last Exam (sous-ensemble texte). Son mode de recherche approfondie, "DeeperSearch", récupère jusqu'à 190 pages web par requête, soit 4 fois plus qu'OpenAI Deep Research sur les mêmes questions. Pourtant, en termes de citations effectives, Grok Deeper Search produit en moyenne 8,15 citations par rapport, contre 40,79 pour OpenAI Deep Research et 31,26 pour Perplexity Deep Research. Ce n'est pas un bug : c'est la conséquence d'une architecture qui optimise le volume de récupération, pas la sélection finale. Trois objets distincts — raisonnement, récupération brute, citation précise — donnent trois classements inversés.

---

## Les chiffres clés (vérifiés à la source)

### Raisonnement : Grok 4 Heavy en tête

| Modèle | HLE texte seul | HLE (avec outils) | Date |
|---|---|---|---|
| Grok 4 Heavy (multi-agent) | **50,7 %** (1er à franchir 50 %) | 44,4 % (full) | Juil. 2025 |
| OpenAI Deep Research (o3) | — | 26,6 % | Fév. 2025 |
| Perplexity Deep Research | — | 21,1 % | Fév. 2025 |

Source HLE Grok 4 Heavy : xAI, x.ai/news/grok-4, juillet 2025.
Source HLE OpenAI et Perplexity : résultats officiels Humanity's Last Exam, déjà documentés dans l'étude [[sources/2026-08-24-stats-deep-research-ia-profil-sources]].

Note méthodologique : "texte seul" exclut les questions avec images ; les 44,4 % Grok Heavy et 26,6 % OpenAI sont sur l'ensemble complet avec outils. Les trois chiffres mesurent des populations de questions partiellement différentes.

---

### Qualité globale des rapports : classement DeepResearch Bench

DeepResearch Bench évalue 100 tâches de niveau PhD dans 22 domaines, via le score RACE (exhaustivité, profondeur, suivi d'instructions, lisibilité).

**Leaderboard juillet 2026 (juge GPT-5.5, CellCog) :**

| Moteur | Score RACE (juil. 2026) | Score RACE (publi. initiale) |
|---|---|---|
| Gemini 2.5 Pro Deep Research | 49,98 | 48,88 |
| OpenAI Deep Research | 47,84 | 46,98 |
| Perplexity Research | 43,05 | 42,25 |
| Grok Deeper Search | **41,22** | 40,24 |

Source : CellCog, cellcog.ai/compare/best-deep-research-ai, leaderboard actualisé juillet 2026, basé sur DeepResearch Bench (deepresearch-bench.github.io).

Observation : Grok 4 Heavy est absent du leaderboard. Le score 40,24-41,22 correspond à "Grok Deeper Search", version antérieure au lancement de Grok 4 (juillet 2025). xAI n'a pas soumis Grok 4 Heavy à la suite publique DeepResearch Bench à la date de cet article.

---

### Volume de citations et précision : les deux métriques divergent

**Framework FACT, DeepResearch Bench (version initiale, juin 2025) :**

| Moteur | Citations effectives (moy.) | Précision de citation |
|---|---|---|
| Gemini-2.5-Pro Deep Research | 111,21 | 81,44 % |
| OpenAI Deep Research | 40,79 | 77,96 % |
| Perplexity Deep Research | 31,26 | **90,24 %** |
| Grok Deeper Search | **8,15** | 83,59 % |

Source : DeepResearch Bench, deepresearch-bench.github.io, consulté août 2026.

Perplexity Deep Research présente la précision de citation la plus élevée des quatre agents (90,24 %), mais le volume de citations effectives le plus bas parmi les trois agents commerciaux non-Grok. Grok Deeper Search est dernier sur les deux dimensions qui comptent pour les requêtes professionnelles : volume et score RACE.

---

### Volume de récupération brute : Grok 4 Heavy devant

Test indépendant conduit sur trois requêtes professionnelles par interconnects.ai (juillet 2025, comparaison directe Grok 4 Heavy vs OpenAI Deep Research) :

| Requête | Grok 4 Heavy (pages) | OpenAI DR (sources) |
|---|---|---|
| Requête locale complexe | 190 | 49 |
| Requête auto-référentielle | 29 | 24 |
| Requête biographique | 96 | 36 |

Grok 4 Heavy consulte 3 à 4 fois plus de pages brutes qu'OpenAI Deep Research. L'auteur note que ce volume supérieur "ne se traduit pas en rapports meilleurs", et que Grok 4 "échoue sur des points simples comparé à ses pairs comme o3 ou Claude 4 Opus".

Source : interconnects.ai, "Grok 4: an o3 look-alike in search...", juillet 2025.

---

### Profil des sources citées : le biais structurel de Grok

En mode standard (hors Deep Research), Grok cite en moyenne 4,7 sources par réponse en 2026, dont **45 % de posts X**. Aucun autre moteur IA majeur n'approche ce ratio.

| Source citée | Part Grok | Spécificités |
|---|---|---|
| Posts X (comptes vérifiés) | 45 % dont 11 % comptes Premium | Cités à 2,8x le taux des comptes non-vérifiés |
| Publications d'actualité | 22 % | |
| Pages à forte autorité de domaine | 17 % | |
| Sites de marques / entreprises | 9 % | |
| Blogs long-form et Substack | 5 % | |

Posts à plus de 50 000 likes : probabilité de citation multipliée par 11,2. En finance et réglementation, les comptes vérifiés sont cités à 4,7 fois le taux des comptes non-vérifiés (vs 1,4 fois en sport/divertissement).

Grok Standard : 4,7 sources/réponse. Perplexity standard : 5,8 sources/réponse. Google AI Overviews : 4,9 sources/réponse.

Source : Presenc.ai, "Grok Citation Patterns 2026", presenc.ai/research/grok-citation-patterns-2026, 4 400 requêtes, mars-avril 2026.

---

### Performance sur requêtes complexes multi-sauts : Perplexity à la traîne

BrowseComp teste des questions à chaîne de raisonnement multi-sources (1 266 questions). Benchmark Parallel AI, août 2026 :

| Moteur | Exactitude BrowseComp |
|---|---|
| GPT-5 | 38 % |
| O3 | Non listé séparément |
| Perplexity | **6 %** |

Sur le même benchmark Parallel AI, taux de victoire sur DeepResearch Bench (vs référence humaine) :
- GPT-5 : 66 %
- O3 Pro : 30 %
- O3 : 26 %
- Perplexity : 6 %

Source : Parallel AI, parallel.ai/blog/deep-research-benchmarks, 50 tâches DeepResearch Bench + 100 questions BrowseComp, août 2026.

Mise en garde : Parallel AI commercialise ses propres agents de recherche. Ces résultats sont publiés à des fins promotionnelles et n'ont pas été audités par un tiers.

---

## Pourquoi ces chiffres divergent autant : trois objets distincts

### La confusion entre raisonnement, récupération et citation

Quand on compare Grok 4 Heavy, OpenAI Deep Research et Perplexity Deep Research sur la "qualité de la recherche approfondie", on mélange trois mécanismes :

**Objet 1 : le raisonnement du modèle de base.** Grok 4 Heavy domine. Son architecture multi-agents (5 instances Grok 4 en parallèle) produit le meilleur score HLE et un classement très haut sur GPQA, USAMO, ARC-AGI. C'est la capacité à traiter un problème difficile une fois que l'information est disponible.

**Objet 2 : le volume de récupération brute.** Grok 4 Heavy récupère également plus que ses pairs (190 vs 49 pages sur une même requête). Mais récupérer 190 pages ne signifie pas que ces 190 pages sont pertinentes, non redondantes, et sourcées différemment des posts X.

**Objet 3 : la citation précise dans le rapport final.** C'est ici que Grok Deeper Search sort dernier avec 8,15 citations effectives contre 40,79 pour OpenAI DR. "Effective citations" dans le sens du FACT framework = citations qui apportent une information nouvelle et vérifiable dans le rapport. Ce que Grok récupère massivement ne se traduit pas en citations exploitables : le filtre est trop restrictif, ou les sources X ne passent pas la validation du framework.

### La logique X comme filtre de qualité implicite

45 % des citations Grok sont des posts X. Dans les requêtes professionnelles, cela produit un problème structurel : les posts X — même de comptes vérifiés, même très engagés — ne satisfont pas les critères des cadres d'évaluation académiques (lien stable, contenu long-form, vérifiabilité). Résultat : des pages récupérées massivement, peu converties en citations valides.

OpenAI Deep Research et Perplexity Deep Research puisent dans des sources plus diversifiées : publications académiques, documentation technique, médias de référence. Leur volume est inférieur, mais le taux de conversion en citation effective est meilleur.

---

## Nos propres chiffres (données de première main)

Le vault SEO-KB ne dispose pas de données de terrain propres sur l'usage des modes Deep Research dans des workflows professionnels français. Ce bloc est réservé honnêtement : les tests comparatifs internes n'ont pas été conduits sur ce format spécifique.

Ce qui existe en données de première main sur le moteur Grok standard : l'entité [[entities/grok]] confirme le positionnement structurel "data X superposée" qui explique mécaniquement le profil de citation mesuré par Presenc.ai.

---

## Contre-analyse

**Grok 4 Heavy n'a pas été mesuré directement.** DeepResearch Bench et les benchmarks qui en dérivent ont évalué "Grok Deeper Search", une version antérieure. Les scores RACE 40,24-41,22 ne disent rien sur Grok 4 Heavy lancé en juillet 2025. L'absence de soumission officielle de xAI au benchmark public est une lacune, pas une preuve de mauvaise performance.

**Le score RACE récompense ce que les benchmarks choisissent de mesurer.** DeepResearch Bench évalue 100 tâches PhD en anglais, avec une logique académique. Grok 4 Heavy a été entraîné sur un paradigme différent (raisonnement par renforcement, vérifiabilité mathématique). Le RACE score n'est pas neutre sur l'architecture.

**Le biais X peut être un avantage sur certaines requêtes.** Pour des sujets où l'information de référence circule d'abord sur X — analyse de marché, réseaux professionnels, annonces de produits, scoop financier — la capacité de Grok à citer des posts récents et engagés peut surpasser un moteur plus "bibliographique". Le Presenc.ai (4 400 requêtes de mars-avril 2026) ne désagrège pas les performances par type de requête professionnelle.

**Le benchmark Parallel AI est auto-promotionnel.** Les scores catastrophiques de Perplexity (6 % BrowseComp, 6 % win rate DeepResearch Bench) sont publiés par un concurrent direct. Le score de 90,24 % de précision de citation de Perplexity dans DeepResearch Bench (source indépendante) nuance très fortement cette lecture.

**Grok 4.6 (septembre 2026) change peut-être déjà le tableau.** Le modèle étant en itération rapide (Grok 4.1, 4.3, 4.5, 4.6 entre juillet 2025 et septembre 2026), les chiffres de mars-avril 2026 peuvent être obsolètes pour la version en production au moment où cet article est lu.

---

## FAQ

**Grok 4 Heavy est-il utile pour la recherche professionnelle ?**
Pour le raisonnement sur des données déjà disponibles : oui, il est de loin le plus puissant sur les benchmarks de difficulté extrême. Pour l'exploration documentaire diversifiée (sources web larges, académiques, techniques) : non, son mode DeeperSearch produit moins de citations effectives que ses pairs, avec un biais structural vers X. Les deux usages sont distincts.

**Perplexity Deep Research est-il le meilleur moteur de citation ?**
Sur DeepResearch Bench, Perplexity Deep Research affiche la meilleure précision de citation (90,24 %). Sur des tâches complexes à multi-sauts (BrowseComp, Parallel AI), il obtient 6 % — résultat très dégradé, mais mesuré par un concurrent avec intérêt commercial. Le profil de Perplexity est "précis mais limité en volume et en recherche multi-chaînes".

**ChatGPT o3 Deep Research est-il la solution intermédiaire ?**
ChatGPT o3 Deep Research (40,79 citations effectives, RACE 46,98-47,84) offre le meilleur équilibre volume/qualité dans DeepResearch Bench. Sa précision de citation (77,96 %) est la plus basse des trois, mais son score RACE le place en deuxième position. GPT-5 (successeur d'o3 en production) améliore ces résultats : win rate 66 % dans le benchmark Parallel AI vs 26 % pour o3.

**Pourquoi Grok 4 Heavy n'est-il pas soumis aux benchmarks DR publics ?**
xAI ne communique pas d'explication officielle. Hypothèse : le mode DeeperSearch de Grok 4 Heavy est dimensionné pour des requêtes à raisonnement complexe, pas pour la synthèse documentaire académique que mesure DeepResearch Bench. Soumettre Grok 4 Heavy à ce benchmark exposerait probablement un score inférieur à ses performances sur HLE ou ARC-AGI.

---

## [À SOURCER]

- **Grok 4 Heavy sur DeepResearch Bench.** Aucun score RACE ou FACT officiel pour Grok 4 Heavy (uniquement "Grok Deeper Search" pré-juillet 2025).
- **Profil de citations en mode DeeperSearch Grok 4 Heavy.** La proportion 45 % X posts est mesurée sur Grok standard (Presenc.ai, mars-avril 2026). Elle n'est pas désagrégée pour le mode DeeperSearch.
- **Précision de citation ChatGPT o3 en mode Deep Research spécifiquement** (77,96 % provient du FACT framework, pas d'un audit indépendant).
- **Comparaison Grok 4.6 (septembre 2026) vs versions antérieures.** Les benchmarks disponibles sont pré-Grok 4.6.
- **Données francophones.** L'ensemble des benchmarks est conduit en anglais. Le comportement des trois moteurs sur des requêtes professionnelles en français n'est pas mesuré.
- **Grok 4 Heavy HLE full score.** L'écart entre 50,7 % (texte seul, source xAI) et 44,4 % (full HLE avec outils, sources secondaires) n'est pas explicitement réconcilié dans la documentation officielle xAI.

---

## Sources

| Intitulé | Organisme | Date | URL | Consulté |
|---|---|---|---|---|
| Grok 4 Announcement | xAI | Juil. 2025 | x.ai/news/grok-4 | 2026-09-08 |
| DeepResearch Bench Leaderboard | deepresearch-bench.github.io | Juin 2025, mis à jour | deepresearch-bench.github.io | 2026-09-08 |
| DeepResearch Bench Updated Rankings | CellCog | Juil. 2026 | cellcog.ai/compare/best-deep-research-ai | 2026-09-08 |
| Grok 4: an o3 look-alike in search | interconnects.ai | Juil. 2025 | interconnects.ai/p/grok-4-an-o3-look-alike-in-search | 2026-09-08 |
| Grok Citation Patterns 2026 | Presenc.ai | Avr. 2026 | presenc.ai/research/grok-citation-patterns-2026 | 2026-09-08 |
| Deep Research Benchmarks | Parallel AI | Août 2026 | parallel.ai/blog/deep-research-benchmarks | 2026-09-08 |
| AI Hallucination Rate Benchmarks 2026 | Digital Applied | Avr. 2026 | digitalapplied.com/blog/ai-model-hallucination-rate-benchmarks-2026-study | 2026-09-08 |
| DeepResearch Bench paper | Du et al. / arXiv | Juin 2025 | arxiv.org/abs/2506.11763 | 2026-09-08 |
| ReportBench | Li et al. / arXiv | Août 2025 | arxiv.org/abs/2508.15804 | 2026-09-08 |
| Entité Grok (vault) | wiki/entities/grok | 2026 | — | 2026-09-08 |
