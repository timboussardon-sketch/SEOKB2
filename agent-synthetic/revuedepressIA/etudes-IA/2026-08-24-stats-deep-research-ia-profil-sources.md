---
type: query
skill: seo-page-statistiques
status: draft
title: "Deep Research IA : Gemini cite 2,7 fois plus de sources qu'OpenAI, mais OpenAI cite 6 points plus juste — trois objets que les benchmarks confondent (2025-2026)"
tags: [deep-research, citations-ia, chatgpt, gemini, perplexity, benchmarks, hallucination, seo, geo]
created: 2026-08-24
updated: 2026-08-24
sources: 9
confidence: medium
---

# Deep Research IA : Gemini cite 2,7 fois plus de sources qu'OpenAI, mais OpenAI cite 6 points plus juste (2025-2026)

Le mode Deep Research produit des rapports avec 111 sources effectives pour Gemini contre 41 pour OpenAI — pourtant la précision des citations va dans le sens inverse. Ce paradoxe n'est pas un accident. Il reflète trois objets de mesure distincts que les benchmarks publiés en 2025-2026 confondent systématiquement, et dont la réconciliation change la lecture des chiffres.

---

## Les chiffres clés (vérifiés à la source)

### Volume de citations par rapport

**DeepResearch Bench — FACT framework (100 tâches de niveau PhD, 22 domaines)**

| Mode / Moteur | Citations effectives (moy.) |
|---|---|
| Gemini-2.5-Pro Deep Research | 111,21 |
| OpenAI Deep Research | 40,79 |
| Claude-3.7-Sonnet w/Search | 32,48 |
| Gemini-2.5-Pro Grounding | 32,88 |
| Perplexity Deep Research | 31,26 |
| Grok Deeper Search | 8,15 |

Source : DeepResearch Bench, deepresearch-bench.github.io, consulté août 2026.

### Précision et cohérence des citations

**ReportBench — arXiv 2508.15804 (évaluation sur tâches de synthèse académique)**

| Modèle | Réf. par rapport | Match rate (cohérence) | Précision | Rappel |
|---|---|---|---|---|
| OpenAI Deep Research | 9,89 | **78,87 %** | **0,385** | 0,033 |
| claude-4-sonnet | 6,74 | 73,67 % | 0,337 | 0,021 |
| Gemini Deep Research | 32,42 | 72,94 % | 0,145 | **0,036** |
| openai-o3 (base) | 12,26 | 31,43 % | 0,299 | 0,031 |
| gemini-2.5-pro (base) | 4,27 | — | — | — |

Énoncés cités par rapport : Gemini Deep Research génère 96,2 énoncés cités et 49,6 non-cités ; OpenAI Deep Research 88,2 cités et 38,9 non-cités ; o3 seul 16,16 cités.

Source : ReportBench, Li et al., arXiv:2508.15804, consulté août 2026.

### Précision de citation dans DeepResearch Bench (FACT)

| Moteur | Précision de citation |
|---|---|
| Claude-3.7-Sonnet w/Search | 93,68 % |
| Perplexity Deep Research | **90,24 %** (meilleur parmi les DRA) |
| Gemini-2.5-Pro Grounding | 81,81 % |

### Score qualité global (RACE framework — DeepResearch Bench)

| Moteur | Score RACE |
|---|---|
| Gemini Deep Research | 48,88 |
| OpenAI Deep Research | 46,98 |
| Perplexity Deep Research | 42,25 |
| Claude w/Search | 40,67 |

### Hallucinations d'URL dans les agents Deep Research

Rao, Wong & Callison-Burch (University of Pennsylvania, arXiv:2604.03173, avril 2026) ont évalué 10 modèles sur DRBench (53 090 URLs) et 3 modèles sur ExpertQA (168 021 URLs, 32 domaines académiques) :

- 3 à 13 % des URLs citées sont fabriquées (jamais indexées par la Wayback Machine).
- 5 à 18 % sont non-résolvables au total (fabricées + lien mort).
- Les agents Deep Research hallucinent les URLs à des taux plus élevés que les modèles standards avec recherche web, malgré une meilleure performance sur les tâches de synthèse.
- Variation par domaine : 5,4 % (Affaires) à 11,4 % (Théologie).
- Dotés d'un outil de vérification (urlhealth), les modèles réduisent les URLs non-résolvables de 6 à 79 fois, sous 1 %.

Source : arXiv:2604.03173, Rao, Wong, Callison-Burch, University of Pennsylvania, avril 2026.

### Benchmarks de raisonnement et de récupération

**Humanity's Last Exam (HLE)** — 2 500 questions de niveau expert, 100+ domaines :

| Modèle | Score HLE |
|---|---|
| OpenAI Deep Research (o3) | **26,6 %** |
| Perplexity Deep Research | 21,1 % |
| OpenAI o3-mini (high) | 13,0 % |
| DeepSeek-R1 | 9,4 % |
| OpenAI o1 | 9,1 % |
| Gemini Thinking (fév. 2025) | 6,2 % |
| GPT-4o | 3,3 % |

**GAIA benchmark — OpenAI Deep Research :**
Niveau 1 : 78,66 % / Niveau 2 : 73,21 % / Niveau 3 : 58,03 % / Moyenne : 72,57 %.
Précédent SOTA toutes sources : 63,64 %. GPT-4 avec plugins : 15 %.

Sources : helicone.ai (fetché), Wikipedia ChatGPT Deep Research (fetché), Perplexity X post @perplexity_ai (vérifié), openai.com/index/introducing-deep-research (403 — chiffres confirmés via sources secondaires).

---

## Chronologie du déploiement

Gemini a lancé Deep Research le 11 décembre 2024, exclusivement pour les abonnés Gemini Advanced (Google One AI Premium, 20 $/mois), dans plus de 100 pays et 45 langues. OpenAI et Perplexity ont tous deux lancé leur version en février 2025. À partir de mi-2025, le mode est disponible chez tous les grands opérateurs (ChatGPT, Gemini, Perplexity, Claude, Grok). Début 2026, OpenAI passe le modèle sous-jacent de o3 à GPT-5.2.

Quotas actuels ChatGPT (juin 2025) : Pro (200 $/mois) — 250 requêtes/mois ; Plus/Team/Enterprise/Edu — 25 requêtes/mois ; Gratuit — 5 requêtes/mois.

Sources : TechCrunch dec 2024 (Gemini Deep Research), Wikipedia ChatGPT Deep Research (fetché).

---

## Volume de sources par session

Presenc.ai a collecté des données sur environ 50 requêtes représentatives par mode (mai 2026) :

| Moteur | Sources consultées | Durée |
|---|---|---|
| OpenAI Deep Research | 50 – 200 | 10 – 30 min |
| Gemini Deep Research | 30 – 150 | 5 – 15 min |
| Claude (mode recherche) | 20 – 100 | 5 – 20 min |
| Perplexity Deep Research | 40 – 100 | 3 – 10 min |
| Grok Deeper Search | 30 – 80 | 3 – 12 min |

Source : Presenc.ai, Deep Research Mode Comparison 2026 (fetché, mai 2026).

L'API Gemini Deep Research confirme un ordre de grandeur : ~80 requêtes web par tâche standard, ~160 pour la variante Max (avec ~900 000 tokens en entrée et ~80 000 en sortie). La durée maximale est de 60 minutes, la plupart des tâches s'achèvent sous 20 minutes.

Source : ai.google.dev/gemini-api/docs/interactions/deep-research (fetché).

---

## Pourquoi ces chiffres divergent — transformation originale

### Les trois objets que les études mesurent sans le dire

Les deux grands benchmarks publiés en 2025-2026 — DeepResearch Bench et ReportBench — mesurent des choses différentes sous le même label "citations" :

**Objet 1 — Citations effectives (DeepResearch Bench / FACT)** : nombre de sources effectivement récupérées, déduplicées et intégrées dans le rapport final. Gemini mène (111,21) parce que son architecture favorise la collecte large avant la synthèse.

**Objet 2 — Cohérence sémantique des énoncés cités (ReportBench / Match Rate)** : pour chaque affirmation citée dans le rapport, la source citée correspond-elle sémantiquement à l'affirmation ? OpenAI mène (78,87 %) parce que son modèle filtre davantage avant de citer.

**Objet 3 — Validité des URLs (arXiv 2604.03173)** : les adresses URL effectivement référencées pointent-elles vers des pages existantes ? Tous les agents Deep Research échouent plus que les modèles standards sur ce point (3-13 % d'URLs fabriquées).

L'inversion : Gemini maximise l'objet 1 au détriment de l'objet 2 (précision 0,145 vs 0,385 OpenAI). Perplexity sacrifie le volume (31,26 citations effectives, le plus bas parmi les DRA) pour la précision des URLs (90,24 %, le meilleur parmi les DRA). OpenAI occupe la position médiane sur le volume mais domine sur la cohérence sémantique.

Pour la pratique SEO/GEO, cela signifie trois choses distinctes :
- Être récupéré par un agent Deep Research (objet 1) dépend de la visibilité web et de la couverture thématique.
- Être cité dans le rapport final (objet 2) dépend de la correspondance sémantique entre la source et l'affirmation produite — un problème de densité informationnelle, pas de popularité.
- L'URL réellement affichée dans le rapport (objet 3) peut être une fabrication à 3-13 %, indépendamment de la qualité du contenu.

### Le paradoxe du volume : plus de sources ne réduit pas les hallucinations d'URL

La corrélation intuiton → données est ici inversée : les agents Deep Research, qui consultent 50 à 200 sources par requête, hallucinent les URLs à des taux plus élevés que les modèles standards avec recherche web simple. L'explication proposée par Rao et al. est mécanique : plus un rapport cite de sources, plus le modèle génère de références depuis sa mémoire paramétrique quand la source exacte est hors de portée dans la fenêtre de contexte. Le volume amplifie l'exposition au risque d'hallucination.

---

## Nos propres données de première main

Ce bloc est honnêtement réservé. Le portefeuille de propriétés mesuré dans ce vault ne dispose pas de données isolant spécifiquement le trafic et les citations provenant de requêtes Deep Research versus requêtes standard. L'instrumentation GA4 distingue les sources IA au niveau du domaine référent (chatgpt.com, perplexity.ai), pas au niveau du mode. Des mesures par mode seraient possibles via les journaux des serveurs combinés à la signature User-Agent des crawlers, mais aucun protocole n'a été activé à ce jour sur ce sujet.

---

## Contre-analyse

**La source de Perplexity est son avantage structurel, pas son modèle.** Perplexity maintient un index web en temps réel. Sa vitesse (2-4 minutes) et sa précision d'URL (90,24 %) viennent de son architecture de retrieval native, pas d'un modèle de langage supérieur. Sur les benchmarks de raisonnement (HLE : 21,1 % vs 26,6 % OpenAI), OpenAI garde l'avantage.

**Les benchmarks ne couvrent pas le contenu en français.** DRBench, ReportBench et arXiv:2604.03173 travaillent tous sur des corpus anglais. Les taux de hallucination et les profils de citation peuvent différer sur des requêtes francophones — notamment parce que le corpus d'entraînement anglophone est mécaniquement plus riche pour les grands modèles.

**Le paradoxe des quotas.** L'utilisateur ChatGPT Plus dispose de 25 requêtes Deep Research par mois. Dans la pratique, Deep Research et la recherche standard ne se comparent pas sur les mêmes tâches : les utilisateurs mobilisent Deep Research pour des synthèses longues, pas pour des requêtes brèves. Les benchmarks mesurent la qualité intrinsèque des deux modes sur des tâches identiques, ce que les utilisateurs ne font pas.

**La hausse du score HLE masque les limites réelles.** Que le meilleur modèle de Deep Research obtienne 26,6 % sur HLE signifie qu'il se trompe sur 73,4 % des questions de niveau expert. Ce score record est présenté comme une avancée majeure ; il reste loin de la performance humaine dans les domaines concernés (~90 %).

**La qualité RACE ne garantit pas la fiabilité factuelle.** Le score RACE mesure préférence utilisateur (instruction-following, complétude, qualité rédactionnelle). Gemini mène (48,88) mais affiche la précision de citation la plus faible (0,145). Un rapport complet et bien écrit peut contenir davantage d'erreurs factuelles qu'un rapport plus court et plus précis.

---

## FAQ

**Quelle différence entre Deep Search et Deep Research ?**
Deep Search fait plusieurs requêtes itératives et synthétise une réponse en quelques secondes à une minute. Deep Research planifie une stratégie, exécute des dizaines à centaines de requêtes web sur 3 à 30 minutes, et produit un rapport structuré de plusieurs pages avec des références numérotées. La distinction est de degré (temps, profondeur, format) et non de nature.

**Quel moteur cite le plus juste ?**
Cela dépend de ce qu'on mesure. Sur la cohérence sémantique entre affirmations et sources (ReportBench), OpenAI mène (78,87 %). Sur la précision des URLs (DRBench), Perplexity mène (90,24 %). Sur le score qualité global (RACE, DRBench), Gemini mène (48,88).

**Le mode Deep Research cite-t-il des domaines différents du mode standard ?**
Aucune étude primaire disponible à ce jour ne compare systématiquement le profil de domaines cités (académique, presse, forums, UGC) entre le mode Deep Research et le mode standard d'un même moteur. Ce bloc reste en [À SOURCER].

**Les agents Deep Research fabriquent-ils des citations ?**
Oui. Rao et al. (arXiv:2604.03173) montrent que 3 à 13 % des URLs produites par les agents Deep Research n'existent pas ou n'ont jamais existé. Ce taux est plus élevé que chez les modèles standards augmentés de recherche web. La correction par un outil de vérification d'URL ramène ce taux sous 1 %.

**Le Deep Research de Gemini est-il meilleur en 2026 ?**
Gemini 3 Deep Think (sorti le 12 février 2026) obtient 48,4 % sur HLE [À SOURCER — chiffre issu de sources secondaires uniquement, score primaire Google non fetché], contre 26,6 % pour OpenAI Deep Research (o3, début 2025). La progression est réelle, mais les architectures et les tâches ne sont pas identiques d'une version à l'autre.

---

## [À SOURCER]

- **Profil de domaines cités par mode (DR vs standard)** : aucune étude disponible ne compare la distribution des types de sources (académique / presse / UGC / forums) entre Deep Research et recherche standard pour le même moteur. Donnée absente des benchmarks existants.
- **Données francophones** : les benchmarks disponibles (DRBench, ReportBench, HLE) sont exclusivement anglophone. Les taux d'hallucination, la précision de citation et le profil de sources pour des requêtes en français restent non mesurés.
- **Gemini 3 Deep Think, 48,4 % sur HLE** : chiffre issu de sources secondaires (MarkTechPost, Remio.ai, Vellum.ai). Le post primaire Google/DeepMind n'a pas été fetchable directement pour valider le chiffre exact.
- **Taux d'hallucination par moteur individuellement** : arXiv:2604.03173 donne une fourchette globale (3-13 %) mais ne désagrège pas par moteur de façon publiée dans l'abstract (données complètes dans le PDF complet).
- **Comportement post-GPT-5.2** : OpenAI a mis à jour Deep Research de o3 vers GPT-5.2 en février 2026. Aucun benchmark équivalent à DeepResearch Bench n'est disponible sur cette version.
- **Quota Deep Research France** : les limites d'usage citées concernent le marché US/global. Les conditions d'accès pour les abonnés français peuvent différer.

---

## Sources

| Intitulé | Organisme | Date | URL | Consulté |
|---|---|---|---|---|
| DeepResearch Bench — FACT & RACE frameworks, 100 tâches PhD | deepresearch-bench.github.io | 2025 | https://deepresearch-bench.github.io/ | août 2026 |
| ReportBench: Evaluating Deep Research Agents via Academic Survey Tasks (arXiv:2508.15804) | Li et al. | août 2025 | https://arxiv.org/abs/2508.15804 | août 2026 |
| Detecting and Correcting Reference Hallucinations in Commercial LLMs and Deep Research Agents (arXiv:2604.03173) | Rao, Wong, Callison-Burch, UPenn | avril 2026 | https://arxiv.org/abs/2604.03173 | août 2026 |
| OpenAI Deep Research — annonce officielle | OpenAI | février 2025 | https://openai.com/index/introducing-deep-research/ | août 2026 (403) |
| ChatGPT Deep Research — article Wikipedia | Wikimedia Foundation | 2025-2026 | https://en.wikipedia.org/wiki/ChatGPT_Deep_Research | août 2026 |
| OpenAI Deep Research: How it Compares to Perplexity and Gemini | Helicone | 2025 | https://www.helicone.ai/blog/openai-deep-research | août 2026 |
| Perplexity Deep Research — 21,1 % sur HLE | @perplexity_ai sur X | février 2025 | https://x.com/perplexity_ai/status/1890452359773405675 | août 2026 |
| Deep Research Mode Comparison 2026 (50 requêtes par mode) | Presenc.ai | mai 2026 | https://presenc.ai/research/deep-research-mode-comparison-2026 | août 2026 |
| Gemini Deep Research Agent — documentation API | Google AI for Developers | 2026 | https://ai.google.dev/gemini-api/docs/interactions/deep-research | août 2026 |
| Google Gemini can now do more in-depth research (lancement déc. 2024) | TechCrunch | 11 déc. 2024 | https://techcrunch.com/2024/12/11/gemini-can-now-research-deeper/ | août 2026 |
