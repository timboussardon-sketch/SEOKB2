---
type: query
skill: seo-page-statistiques
title: "Profondeur topicale vs autorité de domaine dans les citations IA : quatre études, quatre mesures, quatre réponses différentes (2025-2026)"
tags: [ia, seo, geo, citations-ia, topical-authority, domain-authority, aio, chatgpt, perplexity, shap, se-ranking]
created: 2026-08-21
updated: 2026-08-21
sources: 6
confidence: medium
status: draft
---

# Profondeur topicale vs autorité de domaine dans les citations IA : quatre études, quatre mesures, quatre réponses différentes (2025-2026)

Le trafic du domaine — pas son autorité — est le premier prédicteur de citation dans Google AI Mode, selon l'analyse SE Ranking portant sur 2,3 millions de pages. La différence entre sites avec moins de 2 700 visiteurs mensuels (2,4 citations) et plus de 1,16 million de visiteurs (6,4 citations) représente un écart de 2,67 fois. Ce chiffre semble donner raison aux grands domaines généralistes. Mais la corrélation entre le score d'autorité du domaine (métrique Moz ou Ahrefs) et la fréquence de citation par les moteurs IA est, elle, quasi nulle : Spearman -0,051 dans l'analyse Surfer SEO portant sur 5 millions d'adresses URL citées.

Ces deux résultats coexistent. Ils ne mesurent pas la même chose.

---

## Les chiffres clés (vérifiés à la source)

### SE Ranking — trafic et liens entrants comme premier signal

SE Ranking a modélisé 2 328 533 pages issues de 295 485 domaines uniques répartis sur 20 niches, en utilisant un modèle XGBoost avec analyse SHAP (méthode d'attribution de Shapley) pour quantifier la contribution de chaque facteur à la prédiction du nombre de citations dans Google AI Mode. La variable cible est la fréquence de citation calculée sur plus de 500 000 prompts.

Les valeurs SHAP sont les suivantes :
- Trafic du domaine : 0,63 (premier facteur, AI Mode)
- Domaines référents : 0,56 (AI Mode) contre 1,21 (ChatGPT) — l'autorité pèse deux fois plus sur ChatGPT
- Longueur de contenu : 0,20
- Score de confiance de la page : 0,12
- Signaux sémantiques (URL, métadonnées) : 0,06 à 0,07

En valeurs absolues de citation : un domaine à moins de 2 700 visiteurs mensuels cumule en moyenne 2,4 citations ; un domaine à plus de 1,16 million de visiteurs en cumule 6,4 (écart 2,67 fois). Un domaine avec moins de 300 domaines référents cumule 2,5 citations ; avec plus de 24 000, il monte à 6,8.

La profondeur topicale n'apparaît pas comme variable distincte dans ce modèle. Elle est probablement absorbée par le trafic du domaine — un site très vertical avec beaucoup de contenu sur un seul sujet génère du trafic sur ce sujet précisément. Source : SE Ranking, décembre 2025, publié et mis à jour en 2026.

### Surfer SEO — autorité de domaine proche de zéro

Surfer SEO a analysé 5 millions d'adresses URL citées issues de 20 000 prompts sur trois mois, couvrant Google AI Mode, Google AI Overviews, ChatGPT et Perplexity. La corrélation Spearman entre le score de domaine et la fréquence de citation est de -0,051 sur l'ensemble des données ; après suppression des 5 % de domaines au score le plus élevé (Wikipedia, Reddit, YouTube), elle tombe à -0,005. Sur le seul segment des articles de blog, la corrélation remonte à +0,011 — positive mais imperceptible.

La conclusion des auteurs : le score de domaine corrèle négativement avec la fréquence de citation, mais à un niveau proche du bruit. Ce résultat indique que les moteurs IA ne trient pas les pages par autorité globale du domaine. Source : Surfer SEO, juillet 2026.

### Attrifast — 200 sites, 192 000 observations

Attrifast a instrumenté 200 sites réels entre janvier et avril 2026, en soumettant 80 prompts à intention commerciale (déclinés sur 4 moteurs, 3 passages chacun) pour chaque site, soit 192 000 observations au total. L'intervalle de confiance est de ±0,7 point de pourcentage par site.

Le coefficient de corrélation entre le score DR (Ahrefs Domain Rating) et le taux de citation est de 0,46, ce qui explique 21 % de la variance — un effet réel, mais largement minoritaire. Le facteur qui explique davantage de variance est la taille de l'entreprise mesurée par l'effectif : taux médian de 1,4 % pour les structures de 0 à 10 personnes, contre 11,4 % pour les organisations de plus de 500 personnes, soit un écart de 8 fois.

L'écart selon le moteur dépasse l'effet de l'autorité : un même site obtient en médiane 8,2 % de taux de citation sur Perplexity et 1,9 % sur Gemini dans la même semaine, soit un facteur 4,3. Source : Attrifast, mai 2026.

### Ahrefs — 75 000 marques, liens vs mentions

L'analyse Ahrefs portant sur 75 000 marques (publiée le 4 juillet 2026, corpus croisé de 76,7 millions d'AI Overviews, 957 000 prompts ChatGPT, 953 000 prompts Perplexity) hiérarchise les signaux par corrélation de Spearman :
- Mentions YouTube : 0,737
- Mentions web de la marque : 0,660 à 0,710
- Texte d'ancrage brandé : 0,511 à 0,628
- Volume de recherche de marque : 0,352 à 0,466
- Domain Rating : 0,266 à 0,326
- Liens entrants bruts : 0,218

Le DR arrive cinquième. Il corrèle avec les citations, mais trois fois moins que les mentions web de la marque. Cela ne mesure pas la profondeur topicale — mais cela indique que la notoriété construite sur des sites tiers (mentions, citations tierces) prime l'autorité structurelle du domaine propriétaire. Source : Ahrefs, juillet 2026.

---

## Pourquoi ces données semblent se contredire

Les quatre études mesurent des objets distincts. Aligner leurs résultats exige de distinguer :

**Premier objet : le trafic du domaine** (SE Ranking, SHAP 0,63). Il n'est pas synonyme d'autorité au sens métrique (DR, DA). Un site hypervertical — par exemple, 200 articles sur la nutrition sportive — peut cumuler un trafic organique important sur ce seul sujet avec un DR de 30. Un généraliste DR 70 avec cinq articles sur la nutrition sportive attire moins de trafic sur cette niche. Le trafic du domaine est le meilleur proxy disponible de la profondeur de couverture d'un sujet dans un modèle qui ne mesure pas directement la topical authority.

**Deuxième objet : le score d'autorité de domaine comme métrique Moz/Ahrefs** (Surfer SEO, corrélation -0,051). Ce score synthétise le profil de liens entrants global du domaine. Il est quasi nul comme prédicteur de citation parce qu'il ne discrimine pas les pages pertinentes pour une requête donnée : un DR 80 sur un domaine de presse généraliste n'indique rien sur la qualité d'un article de nutrition sportive.

**Troisième objet : le taux de citation agrégé par site sur des prompts à intention commerciale** (Attrifast, r=0,46). Ici, le DR explique 21 % de la variance parce que les sites plus gros ont tendance à avoir à la fois un DR plus élevé et plus de ressources éditoriales, c'est-à-dire plus de profondeur topicale réelle. C'est un effet confondant, pas une relation causale directe entre DR et sélection par les moteurs IA.

**Quatrième objet : les mentions web de la marque** (Ahrefs, r=0,664). Ce signal capte la notoriété externe de la marque — indépendante de l'autorité du domaine propriétaire. Il explique pourquoi la taille de l'entreprise (Attrifast) prime le DR : les grandes entreprises ont plus de mentions sur des sites tiers, indépendamment de leur profil de liens.

La question initiale — un site DR 30 avec 200 articles sur un sujet peut-il dépasser un généraliste DR 70 ? — n'a pas de réponse dans une expérience contrôlée. Les données convergent vers une réponse conditionnelle : oui sur AI Mode et Perplexity (où le trafic organique niche prime l'autorité structurelle), probablement non sur ChatGPT seul (où les domaines référents pèsent deux fois plus, SHAP 1,21 vs 0,56).

---

## Ce que les moteurs IA traitent différemment

L'écart SHAP entre AI Mode et ChatGPT sur les domaines référents (0,56 vs 1,21) est le résultat le plus opérationnel de l'analyse SE Ranking. Il indique deux philosophies de sélection distinctes.

Google AI Mode s'appuie sur le trafic du domaine comme signal dominant — un proxy indirect de la pertinence topicale d'un site sur un sujet donné. Un site très vertical avec peu de liens entrants mais beaucoup de pages lues sur son sujet sera davantage avantagé sur AI Mode que sur ChatGPT.

ChatGPT pondère les domaines référents deux fois plus que AI Mode. Un site avec beaucoup de liens entrants mais peu de trafic organique sera relativement mieux servi par ChatGPT. Le profil de résultats Attrifast confirme cet écart moteur : Perplexity > ChatGPT > Claude > Gemini en taux de citation médian sur les 200 sites analysés, avec un facteur 4,3 entre Perplexity et Gemini sur un même site.

---

## Données de première main

Le portefeuille suivi ne comporte pas, à ce stade, d'analyse croisée entre niveau de DR et profondeur topicale mesurée en nombre d'articles publiés sur un sujet, avec isolation du signal citation. Une propriété à faible autorité (DR < 20) et forte concentration éditoriale sur une verticale est en cours d'instrumentation, avec mesure prévue à J+30 et J+90 — les premières données sont attendues au quatrième trimestre 2026. Le bloc est donc honnêtement réservé.

---

## Contre-analyse

**L'effet confondant de la taille.** Attrifast montre que l'effectif de l'entreprise explique une part de variance plus grande que le DR. Une petite structure, quelle que soit sa profondeur topicale, affiche un taux médian de 1,4 % contre 11,4 % pour une grande organisation. Cela pourrait refléter l'effet des mentions tierces sur les marques (les grandes entreprises sont plus mentionnées sur le web), indépendamment de l'autorité du domaine ou de la profondeur éditoriale.

**ChatGPT valorise davantage les liens entrants.** Sur ce moteur, le signal SHAP des domaines référents (1,21) est le double de celui d'AI Mode (0,56). Un site hypervertical avec peu de backlinks restera pénalisé sur ChatGPT, même avec une couverture topicale complète. La question DR 30 vs DR 70 n'a donc pas de réponse moteur-agnostique.

**La notion de "topical authority" reste un construit, pas une mesure.** Les chiffres attribués à cette notion (r=0,41 selon des sources secondaires, avantage 2,3 fois pour les pages mieux positionnées topicalement) proviennent d'études dont la méthodologie n'est pas accessible publiquement — ce point est développé dans la section [À SOURCER]. SE Ranking, l'étude la plus transparente sur la méthodologie, ne mesure pas la profondeur topicale comme variable explicite.

**Le contenu l'emporte sur l'autorité à l'échelle de la page.** L'étude CORE (Jin et al., arXiv 2602.03608, UIUC / HKUST / Intel Labs, février 2025) démontre que la modification du texte d'une page peut la faire passer du dernier rang au premier dans 80 % des cas sur GPT-4o, Gemini-2.5, Claude-4 et Grok-3, sans changer son profil de liens. Cela suggère que la sélection finale d'un document dans les moteurs génératifs est davantage déterminée par le contenu que par les signaux d'autorité — mais cela ne résout pas la question de l'entrée dans le pool de retrieval initial.

---

## FAQ

**Un site DR 30 spécialisé sur une niche peut-il être cité plus qu'un DR 70 généraliste ?**
Sur Google AI Mode : probablement oui, si le site DR 30 génère plus de trafic organique sur la niche en question. C'est l'implication directe du SHAP 0,63 pour le trafic du domaine (SE Ranking). Sur ChatGPT : moins probable, car le poids des domaines référents est deux fois plus élevé (SHAP 1,21), favorisant structurellement les sites à fort profil de liens. Aucune étude ne valide cette comparaison dans un protocole contrôlé.

**La profondeur topicale est-elle mesurable dans les études disponibles ?**
Non directement. Les études disponibles mesurent le trafic du domaine (SE Ranking), le score d'autorité (Surfer SEO, Attrifast, Ahrefs) ou les mentions tierces (Ahrefs). La profondeur topicale — définie comme le ratio d'articles sur un sujet donné dans le corpus total d'un site — n'apparaît pas comme variable explicite dans les études à grande échelle. Les affirmations d'une corrélation r=0,41 pour la "topical authority" ne sont pas étayées par une méthodologie publiée vérifiable.

**Sur quel moteur l'effet de la profondeur topicale est le plus visible ?**
Sur Perplexity, dont le taux de citation médian est 4,3 fois plus élevé que Gemini pour le même site (Attrifast). Et probablement sur Google AI Mode, où le trafic du domaine (proxy indirect de la verticalité) pèse plus que les liens entrants. Gemini semble le plus sensible à d'autres facteurs — probablement l'intégration avec l'index Google et les entités Knowledge Graph.

---

## [À SOURCER]

**r=0,41 pour la "topical authority"** — ce chiffre circule dans plusieurs sources secondaires (ZipTie.dev, Meev.ai, AuthorityTech.io) attribué à "Omniscient Digital" ou à "ZipTie.dev" selon les publications. Aucune publication primaire avec méthodologie, taille d'échantillon ou protocole de mesure n'a pu être identifiée. Le chiffre est noté mais non utilisé comme fait établi.

**Avantage 2,3 fois pour les pages #6-#10 avec forte topical authority vs #1 avec faible topical authority** — même source et même problème de traçabilité. ZipTie.dev se cite elle-même, sans détail de protocole. Ce chiffre ne peut pas être cité comme donnée vérifiée.

**Wellows 750M+ citations, DA r=0,18** — le rapport Wellows est référencé par AuthorityTech.io et Clairon.ai mais sa page primaire n'a pas pu être fetchée pour vérification directe. La corrélation r=0,18 (r²=0,032 soit 3,2 % de variance) est cohérente avec les résultats Surfer SEO (quasi nulle) mais provient d'une source non vérifiée à la source primaire.

**Impact des mises à jour de ChatGPT o3 sur les seuils d'autorité** — non mesuré dans les études disponibles.

**Données France / francophone** — aucune des études citées ne désagrège les résultats par marché.

---

## Sources

| Intitulé | Organisme | Date | URL | Date de consultation |
|---|---|---|---|---|
| How to Optimize for AI Mode (XGBoost SHAP, 2,328,533 pages, 295,485 domaines, 500K+ prompts) | SE Ranking | Décembre 2025, mis à jour 2026 | https://seranking.com/blog/how-to-optimize-for-ai-mode/ | 2026-08-21 |
| We Analyzed 5 Million AI Citations. Domain Authority Didn't Predict Any of Them (5M URLs, 20K prompts, 3 mois) | Surfer SEO | Juillet 2026 | https://surferseo.com/blog/domain-authority-impact-on-ai-citations/ | 2026-08-21 |
| AI Citation Rate Benchmarks by Brand Size 2026 (200 sites, 192K observations, jan.–avr. 2026) | Attrifast | Mai 2026 | https://attrifast.com/blog/ai-citation-rate-benchmarks-by-brand-size | 2026-08-21 |
| AI Search Citation Factors (Ahrefs, 75K marques, 4 juillet 2026) | Machine Relations / Ahrefs | Juillet 2026 | https://machinerelations.ai/research/ai-search-citation-factors-2026 | 2026-08-21 |
| CORE: Controlling Output Rankings in Generative Engines for LLM-based Search (Jin et al., arXiv 2602.03608) | UIUC / HKUST / Intel Labs | Février 2025 | https://arxiv.org/abs/2602.03608 | 2026-08-21 |
| Topical Authority and AI Citation: Why In-Depth Coverage Gets Cited More | ZipTie.dev | 2026 | https://ziptie.dev/blog/why-in-depth-coverage-gets-cited-more/ | 2026-08-21 |
