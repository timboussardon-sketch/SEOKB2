---
date: 2026-11-02
pilier: geo-search-ia
edition: v2
author: SyntheticBrain
---

# Bing publie un dispositif à trois niveaux pour l'exploitation de contenu par ses IA, sans toucher au référencement classique

## L'essentiel en 15 secondes

- Microsoft Bing a publié le 30 octobre 2026 un dispositif en trois niveaux pour l'exploitation de contenu par ses IA — Allow, Disallow, DisallowExtended — décorrélé de l'éligibilité aux résultats Bing classiques.
- Le niveau intermédiaire DisallowExtended autorise les produits Microsoft (AI Mode, AI Overview, Copilot, Microsoft 365) mais exclut les services tiers de grounding Web IQ et Foundry grounding API.
- Le signal d'entraînement se pose au niveau site via le token robots.txt commun déjà annoncé en octobre, tandis que le signal de grounding se pose uniquement au niveau page via `<meta name="Bingbot" content="ai-grounding:disallowextended">` ou un en-tête X-Robots-Tag.
- Calendrier publié : contrôles temporaires dans Bing Webmaster Tools au 15 décembre 2026, prise en compte au 1er février 2027 à la prochaine indexation, retrait des anciens signaux NoArchive et NoCache au 1er mars 2027.
- Le dispositif consigne pour la première fois dans la documentation d'un moteur que l'opt-out de grounding réduit les occurrences dans les réponses IA mais ne change pas l'éligibilité au référencement classique Bing.

## Info du jour — Bing décorrèle opt-out d'entraînement et opt-out de grounding, et ouvre un niveau intermédiaire réservé à ses propres produits IA (pilier GEO / search IA)

Microsoft a publié le 30 octobre 2026 un billet sur le Bing Search Blog intitulé « Your content, your choice: clearer preferences for training and grounding » ([Bing Search Blog, 2026-10-30](https://blogs.bing.com/search/2026/10/your-content-your-choice-clearer-preferences-for-training-and-grounding/)) et mis en ligne une page de documentation dédiée dans Bing Webmaster Tools ([Bing Webmaster Tools — New AI Preferences](https://www.bing.com/webmasters/help/new-ai-preferences-2t1cc16d)). Les deux textes décrivent un même dispositif en trois niveaux pour contrôler ce que Bing fait du contenu publié : un réglage d'entraînement, un réglage de grounding, et un niveau intermédiaire de grounding limité aux produits Microsoft. Le dispositif a été repris le même jour par [Search Engine Land, 2026-10-30](https://searchengineland.com/microsoft-bing-gives-publishers-more-control-over-how-ai-uses-their-content-499967) et [Search Engine Roundtable, 2026-10-30](https://seroundtable.com/microsoft-bing-ai-controls-42429.html), puis par [PPC Land](https://ppc.land/grounding/) et [Relevant Audience, 2026-10-30](https://www.relevantaudience.com/geo/bing-ai-grounding-controls-replace-noarchive-nocache/).

Le fait principal est la décorrélation entre deux usages jusque-là confondus dans la documentation Bing. Jusqu'au 30 octobre, un éditeur qui voulait sortir son contenu des réponses de Bing Chat utilisait les anciennes directives NoArchive et NoCache, et il bloquait simultanément plusieurs choses : l'affichage étendu dans la recherche, l'exploitation par Bing Chat, et dans certains cas l'entraînement des modèles. Le nouveau dispositif sépare ces usages, et il préserve explicitement l'éligibilité au référencement Bing classique dans tous les cas.

### Les trois niveaux de contrôle

Le billet officiel décrit un réglage AI Training (allow ou disallow) et un réglage AI Grounding (allow, disallow, ou disallow-extended). Les deux réglages ont une valeur par défaut à « allow », donc un site qui ne publie rien conserve tous les usages couverts par le dispositif.

Le niveau DisallowExtended, documenté pour le grounding uniquement, désigne un cas précis : le contenu peut continuer à alimenter les expériences IA opérées directement par Microsoft (Bing AI Mode, AI Overview, Copilot, Microsoft 365), mais il est exclu des services de grounding que Microsoft fournit à des tiers, dont le service Web IQ et la Foundry grounding API ([Bing Webmaster Tools, 2026](https://www.bing.com/webmasters/help/new-ai-preferences-2t1cc16d) ; [Right Blogger, 2026-10-30](https://rightblogger.com/blog/ai-training-opt-out)). C'est une distinction opérationnelle : accepter d'être cité par Copilot n'implique plus d'accepter d'être cité par un produit tiers construit sur l'API grounding de Microsoft.

### Granularité et syntaxe

Le réglage d'entraînement se pose au niveau site, via le token commun robots.txt porté par le draft IETF kelley-aipref-training-preference, auquel Google, Bing, OpenAI et Anthropic se sont alignés en octobre (couverture déjà traitée dans l'édition du 2026-11-01). Le réglage de grounding, lui, est strictement page par page selon la documentation Microsoft, et il se pose soit via une balise meta dans le `<head>`, soit via un en-tête HTTP X-Robots-Tag ciblé sur Bingbot. Le format publié est `<meta name="Bingbot" content="ai-grounding:disallowextended">` ou `ai-grounding:disallow` ([Right Blogger, 2026-10-30](https://rightblogger.com/blog/ai-training-opt-out) ; [Relevant Audience, 2026-10-30](https://www.relevantaudience.com/geo/bing-ai-grounding-controls-replace-noarchive-nocache/)).

L'absence d'un équivalent robots.txt pour le grounding n'est pas un oubli. Elle contraint l'éditeur à décider page par page quel contenu doit alimenter les réponses IA de Bing et lesquelles doivent en sortir. C'est l'opposé du modèle de l'entraînement, qui se tranche au niveau site.

### Calendrier publié

Les dates documentées par Microsoft, confirmées par trois sources indépendantes, sont les suivantes :

Le 15 décembre 2026, Bing Webmaster Tools ouvre des contrôles temporaires de grounding, destinés aux sites qui utilisent encore NoArchive ou NoCache. L'objectif est de permettre une transition contrôlée pendant que ces anciennes directives sont dépréciées.

Le 1er février 2027, Bing commence à honorer les deux nouveaux réglages (entraînement et grounding) à l'occasion du crawl, autrement dit la prise en compte s'opère à la prochaine indexation d'une page concernée, pas de façon rétroactive sur l'index déjà constitué.

Le 1er mars 2027, les anciennes directives NoArchive et NoCache cessent d'être prises en compte comme signaux IA.

Le 30 septembre 2027, les préférences temporaires exposées dans Bing Webmaster Tools pour les sites en transition expirent.

### Mesure de l'effet sur la visibilité IA

Microsoft publie dans Bing Webmaster Tools un AI Performance Report qui expose, pour un site, le nombre de citations et de grounding queries pour les expériences IA supportées ([Embarque, 2026](https://www.embarque.io/glossary/what-are-grounding-queries-in-the-ai-performance-report)). Ce rapport existait avant le billet du 30 octobre et sert aujourd'hui de métrique côté éditeur pour chiffrer l'effet d'un passage de Allow à DisallowExtended ou Disallow. La documentation Microsoft indique sans ambigüité que les deux niveaux restrictifs réduisent les occurrences dans les réponses IA, mais ne garantissent rien quant au nombre d'occurrences restantes ni aux clics qui en découlent.

### Ce que ce dispositif tranche, ce qu'il laisse ouvert

Ce qui est tranché par la documentation Microsoft : l'éditeur peut maintenant choisir d'être exploité par les produits Microsoft en IA sans l'être par les services tiers de grounding, et il peut interdire l'entraînement sans sortir des réponses IA de Bing. Le référencement classique reste décorrélé de ces choix, Microsoft l'écrit explicitement dans les deux documents.

Ce que la documentation ne tranche pas : la part des flux grounding que Microsoft fournit effectivement à Web IQ et à la Foundry grounding API par rapport à ses propres produits, et donc la perte réelle de citation IA qu'implique un passage de Allow à DisallowExtended. Microsoft ne publie pas non plus comment ce dispositif se raccroche aux signaux déclarés par le même site côté Google ou côté OpenAI, sauf pour le token d'entraînement robots.txt porté par le draft IETF commun ([Fireup, 2026](https://fireup.pro/news/ai-training-opt-out-robots-txt)). Pour l'éditeur, ce dernier point reste un angle mort opérationnel.

### Lecture consultant

Le dispositif introduit, dans la pratique, une mécanique d'arbitrage par type de page. Un site B2B dont les pages produit ont vocation à être citées par Copilot et par un agent qui prépare un achat peut rester à Allow sur ces pages, tout en basculant à DisallowExtended sur les articles de corpus que l'éditeur préfère voir rester en moteur plutôt que diffusés comme matière à grounding. La doctrine d'arbitrage de plateforme ([[concepts/arbitrage-plateforme-publication]]) s'étend donc d'un niveau SERP vs plateforme de publication à un niveau page vs type d'exploitation IA, et les métriques publiées dans l'AI Performance report deviennent la seule mesure disponible pour calibrer ces choix côté Bing, à placer dans la grille des métriques de visibilité GEO ([[concepts/metriques-visibilite-geo]]).

Deux points de prudence pour la lecture agent. Un, le dispositif n'engage Microsoft que pour ses propres surfaces et pour les services tiers qu'elle opère, pas pour les crawlers d'OpenAI ou d'Anthropic qui pourraient par ailleurs ingérer la page. Deux, la mesure d'effet repose aujourd'hui sur un seul rapport, celui de Bing Webmaster Tools, dont la représentativité par rapport à l'ensemble de l'écosystème grounding reste non documentée.

## Brèves

### 1. Barry Schwartz publie son November 2026 Google Webmaster Report, aucune core update confirmée depuis l'achèvement du spam update de septembre (pilier actualité SEO)

Barry Schwartz a publié le 2 novembre 2026 son récapitulatif mensuel sur Search Engine Roundtable ([November 2026 Google Webmaster Report, 2026-11-02](https://www.seroundtable.com/november-2026-google-webmaster-report-42431.html)). Les deux faits confirmés sont la fin du spam update de septembre, dont la finalisation a été communiquée par Google le 8 octobre 2026, et l'absence d'une nouvelle core update officiellement en cours au moment de la publication. Le post signale par ailleurs les ajustements documentés sur AI Overviews, les filtres pays de Search Console déployés début octobre, le billet d'orientation de Google du 26 octobre sur l'indexation des pages conçues pour le partage, et la question ouverte d'un éventuel retour du paramètre num=100.

Côté trackers, les posts précédents de Schwartz tenaient une ligne de « volatility continues to get more heated by the day » entre le 27 et le 30 octobre ([Search Engine Roundtable, 2026-10-27](https://www.seroundtable.com/google-search-ranking-volatility-42379.html)), sans confirmation Google. L'édition note la poursuite de la volatilité sans en faire une update annoncée. Pour un consultant, c'est un cadre de référence qui dit que les mouvements observés par les trackers depuis mi-octobre ne sont pas rattachés à une annonce officielle, et qu'il reste prudent d'attendre une communication Google avant d'en déduire un signal de rang.

### 2. Une étude Search Engine Land chiffre le remplacement des News Boxes par les AI Overviews sur les SERPs d'actualité (pilier niche SEO)

Search Engine Land publie une étude longitudinale sur onze mois d'observation des SERPs d'actualité, d'octobre 2025 à août 2026, qui mesure l'évolution des deux formats dédiés aux requêtes d'actu ([Search Engine Land, 2026](https://searchengineland.com/google-ai-overviews-are-pushing-news-boxes-out-of-search-results-study-499348)). Les SERPs qui n'affichent qu'une News Box (Top Stories ou Also in the news) sont passées de 75 % à 34 % de l'échantillon mesuré, soit une baisse de 41 points de pourcentage. Dans le même temps, les SERPs qui n'affichent qu'un AI Overview sont montées à 33 %, soit une hausse de 28 points. L'étude mesure aussi un avantage de classement d'AI Overview sur mobile qui a atteint un pic de 91 % en novembre 2025 avant de redescendre à 83 % en août.

Rappel méthodologique important : l'étude est portée par un seul éditeur, Search Engine Land, et l'auteur n'a pas publié la taille de l'échantillon ni la méthode d'échantillonnage de requêtes. À traiter comme mono-source sous l'angle de la mesure brute. En revanche, la lecture éditoriale converge avec les ordres de grandeur publiés sur onze mois par Trisolute (News Dashboard) sur le recul du Top Stories ([Trisolute News Dashboard](https://newsdashboard.com/en/top-stories-news-box-trends-impacting-news-publishers-right-now/)) et avec les mesures de trafic publiées fin octobre par le Reuters Institute et Chartbeat sur un recul de 33 % à 38 % du trafic Google organique pour les éditeurs presse sur un an. Pour un consultant SEO qui travaille un site d'actualité, l'arbitrage de pilier pour une requête d'actu bascule mesurablement d'une surface News Box vers une surface AI Overview, et la stratégie de citation IA devient aussi importante que la logique de dépôt Google News.

### 3. Walmart confirme le déploiement de ses Agent Profiles pour novembre 2026, un cran plus loin que l'ouverture MCP d'octobre (pilier agentic search)

Walmart a annoncé le 21 octobre 2026 un dispositif en deux parties pour les agents IA de shopping, et a précisé un déploiement en novembre pour la partie côté acheteur ([TechCrunch, 2026-10-21](https://techcrunch.com/2026/10/21/while-amazon-blocks-ai-agents-walmart-rolls-out-the-welcome-mat/) ; [AI Weekly](https://aiweekly.co/alerts/walmart-debuts-agent-gateway-mcp-server-and-agent-profiles-for-approved-ai) ; [Newsbytes](https://www.newsbytesapp.com/news/business/walmart-launches-agent-gateway-with-metas-muse-and-ai-integrations/tldr)). Le premier élément est l'Agent Gateway, un serveur MCP ouvert en bêta aux entreprises et développeurs, dont la page bêta rappelle que l'accès « may be suspended at any time ». Le second est Agent Profiles, des sous-identités rattachées à un compte client Walmart, dédiées à un agent IA précis, avec un plafond de dépense configurable par le titulaire du compte et un périmètre d'accès qui exclut l'historique d'achats et les moyens de paiement.

La partie Agent Gateway est déjà techniquement accessible aux agents MCP via les intégrations publiées, dont ChatGPT via OpenAI, Gemini via Google, Muse de Meta en bêta sur invitation. La partie Agent Profiles est prévue pour novembre 2026 selon l'annonce initiale, sans date publique précisée depuis. Pour un éditeur B2C qui vend ses produits via un flux Walmart ou qui opère son propre back-end commerce, c'est le moment où un agent commence à pouvoir écrire une commande sous une identité auditée côté marchand. Ce qui place Walmart, à la fin octobre 2026, dans la position opposée d'Amazon, qui bloque la majorité des agents IA sur ses pages produit, et complète la lecture du Google Connected Apps Platform traitée dans les éditions du 2026-10-29 et du 2026-11-01 : les premières plateformes d'arbitrage d'agents côté retail sont en train d'être installées, et elles ne sont pas symétriques entre acteurs ([Marie Haynes, 2026-10-29](https://www.mariehaynes.com/) ; [PPC Land, 2026-11-01](https://ppc.land/marie-haynes-tells-seos-to-build-google-search-apps-instead-of-chasing-geo/)).

## Prédictions

- `p-2026-11-02-v2-1` — Avant juin 2027, au moins un éditeur B2B publie une mesure comparative publique de l'effet d'un passage de Allow à DisallowExtended sur son volume de citations Copilot via le rapport AI Performance de Bing Webmaster Tools, confiance 0,45.
- `p-2026-11-02-v2-2` — Avant mars 2027, Google publie une documentation équivalente qui dissocie le signal d'opt-out d'entraînement du signal d'exploitation en grounding dans AI Overviews, en préservant explicitement l'éligibilité à la recherche classique, confiance 0,40.
- `p-2026-11-02-v2-3` — Avant janvier 2027, Walmart documente publiquement un critère d'approbation d'un agent IA pour l'Agent Gateway, au-delà des intégrations nommées dans l'annonce initiale, confiance 0,50.

## Sources principales

- [Bing Search Blog — Your content, your choice (2026-10-30)](https://blogs.bing.com/search/2026/10/your-content-your-choice-clearer-preferences-for-training-and-grounding/)
- [Bing Webmaster Tools — New AI Preferences](https://www.bing.com/webmasters/help/new-ai-preferences-2t1cc16d)
- [Search Engine Land — Microsoft Bing gives publishers more control (2026-10-30)](https://searchengineland.com/microsoft-bing-gives-publishers-more-control-over-how-ai-uses-their-content-499967)
- [Search Engine Roundtable — Microsoft Bing AI Controls (2026-10-30)](https://seroundtable.com/microsoft-bing-ai-controls-42429.html)
- [Relevant Audience — Bing AI grounding controls replace NoArchive/NoCache (2026-10-30)](https://www.relevantaudience.com/geo/bing-ai-grounding-controls-replace-noarchive-nocache/)
- [Right Blogger — How to Opt Out of AI Training Without Losing AI Search Traffic](https://rightblogger.com/blog/ai-training-opt-out)
- [Search Engine Roundtable — November 2026 Google Webmaster Report (2026-11-02)](https://www.seroundtable.com/november-2026-google-webmaster-report-42431.html)
- [Search Engine Land — Google AI Overviews are pushing News Boxes out of search results: Study](https://searchengineland.com/google-ai-overviews-are-pushing-news-boxes-out-of-search-results-study-499348)
- [TechCrunch — While Amazon blocks AI agents, Walmart rolls out the welcome mat (2026-10-21)](https://techcrunch.com/2026/10/21/while-amazon-blocks-ai-agents-walmart-rolls-out-the-welcome-mat/)
