---
type: query
skill: seo-page-statistiques
title: "Noyaux thématiques et clusters de contenu dans les citations IA : trois effets confondus, zéro étude contrôlée (2025-2026)"
tags: [seo, ia, geo, aeo, citabilite, cluster, maillage-interne, topical-authority]
created: 2026-09-24
updated: 2026-09-24
status: draft
sources: 6
confidence: medium
---

# Noyaux thématiques et clusters de contenu dans les citations IA : trois effets confondus, zéro étude contrôlée (2025-2026)

Les pages citées par Google AI Overviews couvrent en médiane 62 % de faits en plus que les pages non citées. Ce chiffre provient d'une étude de Surfer SEO sur 57 253 URLs (novembre 2025) et c'est l'un des rares chiffres disponibles sur la citabilité thématique qui soit vérifiable à la source primaire. Le reste — les "3,2×" et "2,7×" attribués à un prétendu Yext Cluster Study — est une déformation d'une étude sur un sujet différent. Le tour complet de la question "un cluster est-il cité plus qu'une page isolée ?" révèle surtout l'état de la mesure : insuffisant pour trancher.

## Les chiffres clés (vérifiés à la source)

**Couverture factuelle et citabilité Google AI Overviews**

Surfer SEO a analysé 57 253 URLs uniques sur 1 591 mots-clés en novembre 2025 :

- Pages citées de manière systématique (core sources) : 42 % de couverture factuelle
- Pages citées de manière occasionnelle : 34 % de couverture factuelle
- Pages jamais citées : 23 % de couverture factuelle
- Médiane : les articles cités couvrent 62 % de faits de plus que les non-cités
- 28 % de toutes les pages analysées couvrent moins de 10 % des faits clés de leur sujet

L'étude note que les AI Overviews "ne copient pas des phrases — ils reconstruisent des réponses en assemblant des énoncés factuels puisés dans plusieurs sources".

**Signaux topicaux dans la documentation interne de Google (fuite de mai 2024)**

La fuite de la documentation Google Search API (code commis le 13 mars 2024, révélé publiquement le 27-28 mai 2024 par Erfan Azimi et Rand Fishkin, authenticité confirmée par Google le 29 mai 2024) expose trois signaux dans le module QualityNsrNsrData (Normalized Site Rank) :

- `siteFocusScore` : mesure la cohérence thématique globale d'un site
- `siteRadius` : mesure l'écart entre une page individuelle et le thème central du site (via embeddings vectoriels)
- `site2vecEmbeddingEncoded` : représentation vectorielle compressée de l'ensemble du contenu du site, analogue à Word2vec appliqué au niveau site

Ces signaux confirment que Google mesure algorithiquement la spécialisation thématique. Leurs pondérations dans le classement final restent non divulguées.

**Facteur trafic de domaine dans Google AI Mode (SE Ranking, 2026)**

Une étude SE Ranking basée sur 2 328 533 pages et 500 000+ prompts (résultats vérifiés, publiés en 2026) a modélisé les facteurs de citation dans Google AI Mode via un modèle XGBoost avec scores SHAP. Le trafic organique du domaine obtient un score SHAP de 0,63 — premier facteur mesuré. Ce trafic est interprété dans l'étude comme un indicateur indirect de profondeur thématique : les sites très trafiqués sur un sujet ont tendance à couvrir ce sujet de manière plus extensive.

**Fan-out et multiplication des points d'entrée (AirOps, 2025)**

AirOps a analysé 548 534 pages issues de 50 553 réponses (données vérifiées dans une étude précédente [[wiki/sources/]]). Résultat : 32,9 % des pages finalement citées n'ont été récupérées que via des sous-requêtes fan-out — des requêtes dérivées que le moteur génère automatiquement depuis le prompt initial. Ce chiffre signifie qu'une page citée sur trois n'est accessible à l'IA que via un angle thématique adjacent, pas via la requête principale. Un cluster multiplie le nombre d'angles couverts, donc le nombre de sous-requêtes potentiellement satisfaites.

**Le chiffre "86 %" de Yext : ce qu'il dit vraiment**

Yext a publié en septembre 2025 une étude portant sur 6,8 millions de citations issues de 1,6 million de requêtes par modèle (ChatGPT, Gemini, Perplexity), sur 20 820 domaines de citation uniques, entre juillet et août 2025, dans quatre secteurs (retail, services financiers, santé, restauration). Le chiffre mis en avant : **86 % des citations IA proviennent de sources contrôlées par les marques** (sites en propre + fiches d'établissements). Ce résultat porte sur la nature des sources citées — brand-owned vs. tiers — non sur l'architecture de contenu. L'étude Yext ne mentionne pas les clusters, les architectures hub-satellite, ni le maillage interne. Les chiffres "3,2×" et "2,7×" attribués à une prétendue "Yext AI Citation Study 2025 sur les clusters" sont absents de l'étude réelle et ne trouvent aucune source primaire accessible.

## Pourquoi ces chiffres ne permettent pas de répondre à la question

### L'effet cluster est en réalité trois effets empilés

Aucune étude disponible à ce jour ne répond à la question propre : "en contrôlant la qualité du contenu et l'autorité du domaine, une architecture hub + satellites avec maillage interne dense est-elle citée plus souvent qu'une page isolée équivalente ?"

Les études disponibles mesurent des effets qui se superposent et sont difficiles à démêler.

**Effet 1 — Volumétrique (quantitatif)** : plus un cluster comporte de pages, plus il multiplie les points d'entrée potentiels. Les 32,9 % de pages citées uniquement via fan-out (AirOps) confirment que chaque page supplémentaire ouvre des angles supplémentaires. C'est un effet de surface, pas de qualité.

**Effet 2 — Signal topical (architectural)** : les signaux `siteFocusScore` et `siteRadius` de la fuite Google mesurent la cohérence thématique à l'échelle du site. Un site spécialisé sur un sujet bénéficierait structurellement d'un meilleur score. Mais ces signaux concernent Google Search — leur transposition directe aux moteurs IA génératifs (ChatGPT, Perplexity) n'a pas été démontrée.

**Effet 3 — Couverture factuelle (qualitatif)** : les 62 % de faits supplémentaires (Surfer SEO) mesurent la densité factuelle des pages citées. Un cluster bien construit couvre naturellement plus de faits qu'une page isolée — mais c'est parce qu'il comporte plus de contenu, non parce qu'il est structuré en cluster. Une seule page très dense pourrait théoriquement atteindre le même score de couverture factuelle.

La transformation originale de cette étude est précisément là : les trois effets sont systématiquement confondus dans les contenus sur la "stratégie cluster pour l'IA", et aucune étude contrôlée (A/B test cluster vs. page isolée à qualité et autorité équivalentes) n'a été publiée ou rendue publique.

## Nos propres données (premières main)

Le vault documente dans `wiki/concepts/maillage-systeme.md` l'architecture en piliers de Tim Boussardon : un hub par thème (article le plus stratégique, vocabulaire central) + N satellites, avec un système de maillage sur trois axes — topique (cohérence sémantique), vectoriel (alignement embedding entre ancre et passage cible), cognitif (intention de navigation de l'utilisateur). Cette architecture est conçue pour optimiser simultanément le SEO classique et la citabilité IA.

Aucun test contrôlé sur ce cluster n'a encore produit de données suffisantes pour être intégré comme preuve : pas de comparaison cluster vs. page isolée mesurée sur un même sujet avec un délai suffisant. Ce bloc est réservé honnêtement.

## Contre-analyse

**La profondeur topicale n'est pas directement mesurable**

L'étude SE Ranking XGBoost (2,328,533 pages) montre que le trafic organique du domaine est le premier facteur — pas la structure interne. Or, ce trafic est lui-même une résultante de décisions éditoriales accumulées, dont la construction de clusters fait partie. On est dans un problème de variable confondante circulaire : les sites qui construisent des clusters tendent à avoir plus de trafic, et plus de trafic tend à entraîner plus de citations IA.

**Le contenu peut contrebalancer l'architecture**

La recherche de Jin et al. (arXiv 2602.03608, vérifiée dans une étude précédente [[wiki/sources/]]) montre que l'optimisation du contenu peut renverser les classements dans 80 % des cas sans modifier les liens entrants. Ce résultat suggère que la qualité du contenu (couverture factuelle, structure des réponses) prime souvent sur l'architecture.

**Le fan-out est un effet de plateforme, pas un effet d'architecture**

Les sous-requêtes fan-out sont générées par le moteur, pas par la structure du site. Un site avec une seule page exhaustive peut répondre à plusieurs sous-requêtes si sa densité factuelle est suffisante. L'avantage du cluster sur le fan-out est réel mais quantitativement non isolé.

**Les données de "cluster study" en circulation sont majoritairement invérifiables**

Une vérification effectuée pour cette étude sur les chiffres les plus relayés ("3,2× citations pour les sites avec clusters", "86 % des citations depuis des sites avec 5+ pages connectées", "2,7× gain par liens bidirectionnels") n'a trouvé aucune source primaire accessible. Ces chiffres circulent sur des blogs SEO sans lien vers une étude originale — ils correspondent à des déformations de l'étude Yext réelle, qui porte sur un sujet entièrement différent.

## FAQ

**Un cluster aide-t-il concrètement à être cité par les IA ?**

Probablement oui, mais via trois mécanismes distincts qui ne sont pas tous liés à l'architecture elle-même. La couverture factuelle extensive (Surfer SEO, +62 % de faits) est le mécanisme le mieux documenté — et un cluster produit naturellement plus de faits couverts. La multiplication des points d'entrée via fan-out (AirOps, 32,9 % des citations uniquement via fan-out) est un second bénéfice réel. La contribution spécifique du maillage interne, elle, n'est pas quantifiée de façon isolée.

**Est-ce que le maillage interne compte pour les IA ?**

Il compte pour Google Search (la fuite Google confirme que la cohérence du site est mesurée via siteFocusScore/siteRadius), et les AI Overviews de Google s'appuient sur l'index Google. Pour les moteurs IA non liés à l'index Google (ChatGPT en mode retrieval, Perplexity), l'effet du maillage interne sur la découverte de pages n'est pas documenté expérimentalement.

**Pourquoi les "études cluster" circulent-elles avec des chiffres précis mais invérifiables ?**

C'est un artefact courant dans le secteur SEO : des statistiques construites pour le marketing de contenu sont reprises sans vérification dans d'autres articles. Les "3,2×" attribués à Yext reflètent ce phénomène. Le vrai résultat Yext porte sur la part des citations depuis des domaines brand-owned — un résultat pertinent mais différent.

**La doctrine des 5-7 pages minimum est-elle fondée ?**

Elle circule dans plusieurs guides (Slate, Digital Applied) mais sans source primaire vérifiable. Sa logique est cohérente avec l'effet volumétrique et l'effet de couverture factuelle — mais elle n'est pas appuyée par une expérimentation contrôlée.

## [À SOURCER]

- Mesure directe de l'effet du maillage interne sur la citabilité ChatGPT et Perplexity (aucune étude primaire trouvée)
- Expérimentation contrôlée cluster vs. page isolée à qualité de contenu et autorité équivalentes (inexistante dans la littérature accessible)
- Pondération de siteFocusScore/siteRadius dans les classements Google 2026 (non divulguée)
- Données France/francophone sur la citabilité des clusters
- Transfert de siteFocusScore/siteRadius sur les modèles IA non-Google (mécanisme documentaire manquant)

## Sources

| Intitulé | Organisme | Date | URL | Date de consultation |
|---|---|---|---|---|
| Do Pages With More Key Facts Get Cited in AI Overviews? 57,000+ URLs Analyzed | Surfer SEO | 26 novembre 2025 | https://surferseo.com/blog/do-pages-with-more-key-facts-get-cited-in-ai-overviews | 24 septembre 2026 |
| 2024 Google Search documentation leak | Wikipedia | Mai 2024 (fuite) | https://en.wikipedia.org/wiki/2024_Google_Search_documentation_leak | 24 septembre 2026 |
| Yext Research: 86% of AI Citations Come from Brand-Managed Sources | Yext | Septembre 2025 | https://www.yext.com/about/news-media/ai-citations-release | 24 septembre 2026 |
| The Long Tail: Where Visibility in AI Search is Won (AirOps, fan-out 32,9 %) | AirOps | 2025 | https://www.airops.com/report/the-long-tail-where-visibility-in-ai-search-is-won | 24 septembre 2026 |
| Profondeur topicale vs autorité de domaine : SE Ranking XGBoost (2 328 533 pages) | SE Ranking / SyntheticBrain vault | 2026 | [[wiki/sources/2026-08-21-stats-profondeur-topicale-vs-autorite-domaine-citations-ia]] | — |
| Contenu peut renverser les classements dans 80 % des cas (Jin et al.) | arXiv 2602.03608 | 2026 | Référence interne vault | — |
