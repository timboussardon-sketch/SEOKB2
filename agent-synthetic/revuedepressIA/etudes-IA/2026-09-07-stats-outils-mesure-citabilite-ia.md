---
type: query
skill: seo-page-statistiques
title: "Outils de mesure de la citabilité IA : quatre définitions, une métrique introuvable (2025-2026)"
tags: [geo, aeo, citabilite-ia, outils-seo, methodologie, profound, peec-ai, semrush, otterly]
created: 2026-09-07
updated: 2026-09-07
sources: 12
confidence: medium
status: draft
---

# Outils de mesure de la citabilité IA : quatre définitions, une métrique introuvable (2026-09-07)

Profound, Peec AI, Semrush et Otterly.ai ont alimenté la quasi-totalité des études publiées sur les citations IA en 2025-2026. Chaque chiffre produit par ces outils est présenté comme une mesure de "visibilité" ou de "citabilité". Problème documenté : aucun des quatre ne mesure la même chose sous ces mots. Un point de départ pour lire les études sectorielles sans les avaler entières.

## Les chiffres clés (vérifiés à la source)

### Tailles de corpus déclarés

Profound déclare 1,5 milliard de prompts réels dans son corpus total (collecte via panels double opt-in, anonymisés, conformes au RGPD), 400 millions de conversations dans le Profound Index, et 100 millions de requêtes IA traitées par mois [[sources/profound-index-2026]]. C'est le seul outil qui s'appuie sur des requêtes d'utilisateurs réels plutôt que sur des prompts synthétiques.

Semrush revendique plus de 100 millions de prompts LLM dans sa base de suivi mondiale [[sources/semrush-ai-toolkit-2026]]. La composition de ce corpus n'est pas publiée.

Peec AI ne constitue pas de corpus global : chaque client définit ses propres prompts à suivre. L'outil utilise un scraping d'interface (pas d'appel API) pour simuler les interactions utilisateurs réelles [[sources/peec-ai-methodology-2026]].

Otterly.ai ne divulgue aucune donnée de corpus. Le rafraîchissement est hebdomadaire, avec un décalage de sept jours [[sources/otterly-methodology-2026]].

### Dérive des citations dans le temps

40 à 60 % des domaines cités par un moteur IA changent d'un mois à l'autre, selon une analyse croisée de plusieurs outils. Désagrégé par plateforme : Google AI Overviews présente 59,3 % de dérive mensuelle, ChatGPT 54,1 %, Microsoft Copilot 53,4 %, Perplexity 40,5 % [[sources/discovered-labs-citation-drift-2026]]. [À SOURCER : source primaire non retrouvée, chiffres issus d'une revue indépendante Discovered Labs, 2026.]

Les LLMs présentent jusqu'à 15 % d'écart de précision entre deux runs identiques au même paramétrage de température (Song et al., 2024) [[sources/song-et-al-2024-llm-variability]]. [À SOURCER : article Song et al. cité via Metricus, source primaire non fetchée.]

### Fiabilité des panels opt-in

Les panels recrutés sur la base du volontariat produisent deux fois l'erreur absolue des échantillons probabilistes. Même le rééchantillonnage le plus soigné ne réduit le biais d'origine que de 30 % (Pew Research, 2024) [[sources/pew-research-opt-in-panels-2024]]. [À SOURCER : source Pew citée via Metricus, source primaire non retrouvée pour la vérification directe.]

### Opacité des méthodes

Aucune des quatre plateformes principales ne publie la méthodologie complète de son score de citabilité : ni les poids, ni les paramètres d'appel LLM, ni la logique d'agrégation (Metricus, 2026) [[sources/metricus-geo-trust-problem-2026]].

## Pourquoi ces chiffres ne se comparent pas entre eux

La transformation originale de cette étude repose sur un tableau que personne n'a encore dressé explicitement : **les quatre outils mesurent quatre objets distincts sous le même nom**.

| Outil | Terme utilisé | Définition opérationnelle publiée | Ce qui n'est pas mesuré |
|---|---|---|---|
| **Profound** | "Mention" | Présence du nom de marque dans la réponse, détectée par extraction d'entité. L'URL n'est pas requise. | URLs consultées en coulisse par le RAG. Citations sans mention textuelle de la marque. |
| **Peec AI** | "Citation" vs "Source" | *Citation* = URL explicitement référencée dans la réponse visible. *Source* = toute URL accédée lors de la génération (en coulisse). Les deux sont suivis séparément. | Mémoire paramétrique. Marques mentionnées sans URL. |
| **Semrush** | "Mention" vs "Citation" | *Mention* = nom de marque sans lien dans l'AI Overview. *Citation* = domaine listé comme source avec lien. | Tous les moteurs hors Google AI Overviews sur les plans de base. |
| **Otterly.ai** | "Mention" et "Citation" | Présence dans la réponse visible. Les deux termes sont utilisés indifféremment dans la documentation. Méthodologie d'extraction non publiée. | Non divulgué. |

Ce tableau explique des divergences qui ont été présentées à tort comme des contradictions entre études. Quand Peec AI publie un taux de "citation" de X % et que Profound publie un taux de "mention" de Y % sur le même sujet, ils ne mesurent pas le même signal.

Il y a aussi une troisième couche absente de tous les dashboards : la mémoire paramétrique. Un LLM peut nommer une marque sans aucun retrieval, uniquement à partir de ce qu'il a appris à l'entraînement. Aucun outil ne distingue cette source de la citation RAG observable.

### La zone aveugle du RAG

Le RAG (retrieval-augmented generation) fonctionne en deux temps : récupération d'URLs pertinentes, puis sélection de passages à citer dans la réponse. Un document peut être lu sans être cité. Seul Peec AI distingue explicitement les deux : "sources" (URLs accédées) vs "citations" (URLs référencées dans la réponse) [[sources/peec-ai-methodology-2026]]. Les trois autres outils ne mesurent que l'étape finale.

Or les études sur le taux de sélection post-récupération montrent que 85 % des pages récupérées ne sont jamais citées (AirOps, 548 534 pages, 2026) [[sources/airops-2026-selection-rate]]. Les outils qui ne mesurent que les citations visibles ratent donc l'influence de 85 % du corpus réellement consulté.

### Les moteurs structurellement absents

Les outils actuels ne couvrent pas plusieurs surfaces majeures :

NotebookLM (Gemini Notebook) opère en mode RAG utilisateur, sans referral, sans Search Console, avec un trafic classé en "direct" dans GA4. Aucun dashboard ne le mesure. L'outil représente 30 millions d'utilisateurs et 600 000 organisations (Google, juillet 2026) [[sources/google-notebooklm-2026]].

Apple Siri AI route les requêtes vers Gemini sans exposer de données de citation. Le trafic Siri est classé "direct" dans GA4 [[sources/apple-intelligence-siri-2026]].

Meta AI (Facebook, Instagram, WhatsApp) génère 51 % des requêtes des crawlers IA selon DataDome (Q2 2026) mais produit un trafic référent quasi nul. Attribution conditionnée par contrats commerciaux [[sources/meta-ai-citations-2026]].

Grok (xAI) est couvert par certains outils mais insuffisamment. Son profil de sources (7 des 10 premiers domaines cités sont des plateformes sociales ou UGC) est structurellement différent de tous les autres moteurs [[sources/grok-citations-profil-2026]].

## Nos propres chiffres (données de première main)

Ce bloc est réservé honnêtement. Le vault ne dispose pas d'abonnement actif à ces quatre outils et n'a pas de mesure directe comparative. Aucun chiffre fabriqué ne sera ajouté.

L'étude [[preuves/SETUP-GSC]] pourrait fournir une base de comparaison indirecte (trafic référent IA observé en GA4 vs chiffres publiés par ces outils pour les mêmes URLs), mais ce croisement n'a pas été effectué à ce jour.

## Contre-analyse

### Le conflit d'intérêts est structurel

Profound, Otterly.ai et Semrush proposent à la fois le tableau de bord de mesure et des recommandations ou services d'optimisation. Vendre l'audit et la remédiation sur la même métrique non publiée est un conflit d'intérêts documenté dans d'autres secteurs. En publicité programmatique, la même configuration a conduit à 26,8 milliards de dollars de dépenses gaspillées annuellement avant que les annonceurs exigent une vérification tierce (ANA, 2024) [[sources/ana-programmatic-waste-2024]]. [À SOURCER : montant ANA cité via Metricus, source primaire non fetchée.]

L'industrie SEO n'a pas encore son équivalent du MRC (Media Rating Council), l'organisme indépendant d'accréditation des panels audience. Aucune des quatre plateformes n'a soumis sa méthodologie à un audit externe comparable (Metricus, 2026).

### Les panels opt-in ne représentent pas les utilisateurs réels

Profound se distingue par l'usage de panels réels (double opt-in) plutôt que de prompts synthétiques. Mais même ce modèle présente une limite : le panel est constitué de personnes qui ont *accepté* de partager leurs conversations IA. Ce biais de volontariat modifie le profil des requêtes par rapport à la population générale des utilisateurs IA (Pew Research, 2024).

Les outils utilisant des prompts synthétiques (définis par leurs équipes internes) sont exposés à un biais de sélection plus fort encore : les prompts reflètent la vision du prestataire de ce que les utilisateurs demandent, pas ce qu'ils demandent réellement.

### La dérive mensuelle des citations rend les snapshots peu fiables

Avec 40 à 60 % de renouvellement mensuel des domaines cités, un audit ponctuel d'une semaine donne un résultat volatile. La communauté SEO converge vers 60 à 90 jours de suivi continu comme fenêtre statistiquement exploitable (Discovered Labs, 2026). Les études sectorielles publiées sur des captures courtes ne permettent pas de conclure sur des tendances structurelles.

### Ce que la croissance du marché n'implique pas

Profound a levé 96 millions de dollars (2026). Peec AI dépasse les 4 millions d'euros de revenus annuels récurrents avec 1 300 clients (novembre 2025) [[sources/peec-ai-revenue-2025]]. [À SOURCER : chiffres issus d'un article Writesonic, source primaire non confirmée.] La croissance commerciale de ces outils valide la demande de mesure, pas la fiabilité de la mesure.

## FAQ

**Les chiffres publiés dans les études Profound ou Semrush sont-ils faux ?**

Non. Ils sont cohérents avec ce que ces outils mesurent. Le problème est que le lecteur ne sait pas toujours ce qui est mesuré précisément. Un taux de "mention" Profound et un taux de "citation" Peec AI ne sont pas interchangeables.

**Quel outil choisir pour suivre sa présence dans les réponses IA ?**

Chaque outil a ses angles morts. Peec AI est le seul à distinguer sources et citations. Profound est le seul à partir de requêtes utilisateurs réels vérifiés. Semrush est le plus accessible mais limité à Google AI Overviews sur les plans standards. Otterly.ai offre six plateformes à bas coût mais avec le rafraîchissement le plus lent (hebdomadaire, 7 jours de lag) et la documentation la moins précise. L'usage de deux outils complémentaires avec des définitions explicitement réconciliées est la pratique la plus rigoureuse.

**Pourquoi les études publiées par ces outils divergent-elles autant ?**

Quatre raisons principales : définition différente de "citation", corpus de requêtes différent (réel vs synthétique, large vs vertical), plateformes couvertes différentes, et fenêtres temporelles différentes. À ces quatre facteurs s'ajoute la dérive naturelle des citations IA elle-même.

**Les audits ponctuels ont-ils une valeur ?**

Comme point de départ, oui. Comme décision stratégique seule, non. La dérive de 40 à 60 % mensuelle implique qu'un audit de deux semaines peut avoir changé significativement avant la fin du mois.

## [À SOURCER]

- Citation drift 59,3 % / 54,1 % / 53,4 % / 40,5 % : chiffres issus d'une analyse Discovered Labs non retrouvés dans la source primaire des outils eux-mêmes
- Song et al. (2024) sur la variabilité LLM à 15 % : cité via Metricus, article primaire non fetchable directement
- Pew Research 2024 sur les panels opt-in (2× erreur absolue) : référencé via Metricus, source Pew primaire non fetchée
- ANA sur les 26,8 milliards gaspillés en programmatique : référencé via Metricus, non vérifié directement
- Peec AI 1 300 clients et 4 M€ ARR : source Writesonic (secondaire), non confirmé par Peec AI officiellement
- Profound 96 M$ levée : cité par AuthorityTech, non vérifié sur source primaire (CP officiel)
- Mesure des surfaces manquantes (Grok proportion X posts vs web, Siri volume exact, Meta AI breakdown) : aucune étude grande échelle disponible
- Données France : aucun des quatre outils ne publie de données désagrégées par marché francophone

## Sources

| Intitulé | Organisme | Date | URL | Consulté le |
|---|---|---|---|---|
| Introducing the Profound Index | Profound | 2026 | https://www.tryprofound.com/blog/introducing-profound-index | 2026-09-07 |
| Profound AI Citation Analysis | Profound | 2026 | https://www.tryprofound.com/features/answer-engine-insights/citations | 2026-09-07 |
| AI Instructions / Methodology | Peec AI | 2026 | https://peec.ai/ai-instructions | 2026-09-07 |
| How to Research and Analyze AI Overviews with Semrush | Semrush | 2026 | https://www.semrush.com/blog/semrush-ai-overview-research/ | 2026-09-07 |
| OtterlyAI Review: Quick Start Guide and Data Validation Framework | Discovered Labs | 2026 | https://discoveredlabs.com/blog/otterlyai-review-quick-start-guide-and-data-validation-framework | 2026-09-07 |
| Peec AI Review: Best for AI Visibility Monitoring? | Discovered Labs | 2026 | https://discoveredlabs.com/blog/peec-ai-review-best-for-ai-visibility-monitoring-use-cases-limits-alternatives | 2026-09-07 |
| AI Visibility Dashboards Grade Their Own Homework | Metricus | 2026 | https://metricusapp.com/blog/ai-visibility-dashboard-trust-problem-black-box-scoring-synthetic-data-vendor-conflict-2026/ | 2026-09-07 |
| AI Visibility Tools 2026: 12 Compared | Writesonic | 2026 | https://writesonic.com/blog/ai-visibility-tools | 2026-09-07 |
| Profound Raised $96M to Track AI Citations | AuthorityTech | 2026 | https://authoritytech.io/curated/profound-96m-ai-citation-tracking-market-validation-2026 | 2026-09-07 |
| Best AI Search Visibility Tracking Software in 2026 | PromptZone | 2026 | https://www.promptzone.com/tara_suzuki/best-ai-search-visibility-tracking-software-in-2026-profound-vs-peec-vs-otterly-pe6 | 2026-09-07 |
| AirOps Fan-Out Study | AirOps | 2026 | non public (cité dans études antérieures du vault) | — |
| Google NotebookLM announcement (30M users) | Google | 2026-07 | https://blog.google (vérifié dans étude 2026-09-06) | 2026-09-06 |
