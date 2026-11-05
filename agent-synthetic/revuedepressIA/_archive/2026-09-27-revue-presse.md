---
title: "Perplexity retire l'API Sonar aujourd'hui : sonar-pro et sonar-reasoning-pro disparaissent, cascade attendue sur les outils GEO tiers"
date: 2026-09-27
pilier_info_du_jour: Recherche agentique
piliers_breves: [Product-Led SEO, Actualité SEO]
edition: 67
---

# Perplexity retire l'API Sonar aujourd'hui : sonar-pro et sonar-reasoning-pro disparaissent, cascade attendue sur les outils GEO tiers

*Édition Algorithme — 27 septembre 2026 — SyntheticBrain*

- Perplexity retire aujourd'hui, 27 septembre 2026, son API Sonar Chat Completions. Le blog officiel du 13 août l'annonçait à 45 jours : « on September 27, 2026, the Agent API becomes the main surface for this work, and Sonar tiers retire on the same date » (sources [Perplexity blog](https://ai-watch-blog.vercel.app/en/posts/2026-08-13-perplexity-agent-api-launch/) et [LLM Gateway](https://llmgateway.io/blog/perplexity-sonar-api-retirement)).
- `sonar-pro` et `sonar-reasoning-pro` cessent d'être routables à partir d'aujourd'hui, sans équivalent 1:1 dans l'Agent API : le rewrite « preset » ne conserve ni le modèle sous-jacent, ni la fenêtre de contexte 200K, ni le pricing.
- Le modèle de coût change : la facturation au token pur laisse place à des frais par appel d'outil (2,50 $ / 1 000 recherches web, 0,50 $ / 1 000 fetches, 5 $ / 1 000 requêtes finance ou people).
- Chartbeat publie le 24 septembre son 2026 Publisher Playbook : le trafic Google Search vers les éditeurs a chuté de 40,2 % en glissement annuel (juillet 2025-juillet 2026), contre 21,9 % l'année précédente ([Search Engine Journal, 24 sept](https://www.searchenginejournal.com/google-search-decline-publishers-chartbeat/590681/)).
- PSOhub publie avec The Rank Masters une étude de cas 90 jours (16 avril-14 juillet 2026, révisée le 15 septembre) où un système de contenu ICP-led obtient 12 pages sur 18 en première page Google, 54 citations dans des réponses IA et 50 visites réelles ([case study TRM](https://www.therankmasters.com/insights/benchmarks/psohub-ai-visibility-aeo-seo-case-study)).

## Info du jour — Recherche agentique — Perplexity retire l'API Sonar aujourd'hui : ce qui casse, ce qui migre, et pourquoi les outils GEO qui interrogent Perplexity doivent avoir migré avant ce soir

Perplexity retire aujourd'hui, 27 septembre 2026, son API Sonar Chat Completions. La date figure dans le billet officiel de Perplexity « Agent API: One Place to Build with LLMs, the Web, and Agents » publié le 13 août 2026, verbatim reproduit par plusieurs sources indépendantes ([AI Watch Station](https://ai-watch-blog.vercel.app/en/posts/2026-08-13-perplexity-agent-api-launch/), [Ecorpit](https://ecorpit.com/perplexity-sonar-retirement-september-27-agent-api-migration-2026/), [LLM Gateway](https://llmgateway.io/blog/perplexity-sonar-api-retirement)) : « on September 27, 2026, the Agent API becomes the main surface for this work, and Sonar tiers retire on the same date ». La fenêtre de préavis pour un endpoint de production est de 45 jours.

La conséquence technique est double, et elle n'est pas symétrique entre les modèles.

Pour `sonar` (modèle de base), la bascule s'est faite le 25 septembre côté LLM Gateway. La documentation du gateway précise : « perplexity/sonar moves to Perplexity's Agent API on September 25 ». Le point d'appel reste `/v1/chat/completions`, la forme des requêtes est identique, le streaming, le JSON schema output et le tableau `search_results` continuent de fonctionner. Chaque requête déclenche toujours une recherche web, désormais via un outil `web_search` attaché automatiquement. Le tarif effectif tombe (LLM Gateway parle d'une requête « grounded » mesurée « about a third cheaper » sur son banc), et le coût de la recherche apparaît séparément dans `cost_details.web_search_cost`.

Pour `sonar-pro` et `sonar-reasoning-pro`, la rupture est nette. LLM Gateway écrit noir sur blanc : « perplexity/sonar-pro and perplexity/sonar-reasoning-pro stop being routable » à partir du 27 septembre. L'Agent API de Perplexity « rejects both model ids outright », il n'existe pas d'alias qui pointerait vers un modèle équivalent. La table de correspondance publiée par Perplexity elle-même mappe :

- `sonar` → preset `fast`
- `sonar-pro` → preset `low`
- `sonar-reasoning-pro` → preset `medium`
- `sonar-deep-research` → preset `high`

Mais un preset n'est pas un modèle. Un preset combine un modèle sous-jacent, un system prompt, une configuration d'outils, un effort de raisonnement et un budget de tokens. LLM Gateway explique pourquoi il refuse de rediriger silencieusement : « the Agent presets that could stand in for them run a different underlying model with different search behavior and different pricing ». Concrètement, un client qui appelait `sonar-pro` pour sa fenêtre de contexte 200K et son comportement de citation particulier ne retrouve rien de comparable côté Agent : la fenêtre 200K n'est pas documentée sur les presets Agent, et le contrat de citation change.

Le troisième point est le pricing. Sonar facturait un forfait par requête, indépendamment du nombre de recherches déclenchées à l'intérieur. Agent API ajoute une facturation à l'appel d'outil, superposée à la facturation token. Les tarifs publiés sont : 2,50 $ par tranche de 1 000 appels de recherche web, 0,50 $ pour 1 000 fetches, 5,00 $ pour 1 000 appels finance ou people search. Pour un pipeline qui déclenche 5 recherches par question, l'addition change de forme. L'incident probable des prochains jours n'est pas la panne d'API, c'est l'écart entre facture attendue et facture reçue en fin de mois.

Le quatrième point est la limite de débit. LLM Gateway documente un plateau de 33 requêtes par seconde sur les paliers Tier 4 (1 000 $ cumulé) et Tier 5 (5 000 $ cumulé). Dépenser plus ne rend pas plus rapide. Pour un outil GEO qui interroge Perplexity en batch pour mesurer des citations d'une marque sur des milliers de prompts, ce plafond fixe déplace le goulot d'étranglement du budget vers la parallélisation.

Le cinquième point est un décalage documentaire qui aggrave le passage. Le billet de blog Perplexity du 13 août et la bannière d'avertissement dans les docs mentionnent bien la date du 27 septembre. Mais le guide de migration lui-même, celui vers lequel Perplexity oriente les équipes en pratique, indique que « Sonar remains supported » et ne mentionne aucune date de retrait. Ecorpit note : « the linked migration guide contains no retirement date and states Sonar remains supported ». Les équipes qui suivent leurs déprécations en diffant les changelogs (pratique standard) ratent le 27 septembre : la date n'apparaît nulle part dans le changelog officiel Perplexity, elle est archivée dans une entrée « July 2026 » sans date.

Ce que ça change pour un consultant SEO ou GEO qui suit la chaîne d'outils de mesure de citations IA.

Un, les outils GEO tiers qui interrogent Perplexity pour mesurer la part de citations d'une marque (Peec AI, Otterly, Profound, Athena HQ, Scrunch, tryprofound, BrightEdge Copilot, RankAI, Rankscale, Siftly, Xfunnel AI) doivent avoir migré leur intégration vers Agent API avant ce soir. Aucun de ces éditeurs n'a publié à ce jour un statut public de migration effective, ce qui est le point à surveiller cette semaine. La question opérationnelle est : mes séries temporelles de citations Perplexity, du 25 au 30 septembre, sont-elles reconstruites sur une base de mesure comparable ?

Deux, le contrat de citation dans le champ `search_results` reste stable côté `sonar`, mais un champ `annotations` (au format `url_citation` standard des modèles search-grounded) s'ajoute sur le message assistant. Un parseur de citations existant peut fonctionner sans changement, mais un parseur qui s'appuierait sur le nouveau champ standard récupère un contrat aligné avec les autres providers. Ce sujet est mineur en surface, il compte à l'échelle d'une entreprise qui interroge plusieurs moteurs derrière un même code de collecte.

Trois, la disparition de `sonar-pro` sans équivalent 200K impose un choix d'architecture. Un cas d'usage qui envoyait au modèle une longue liste de documents (par exemple, un corpus produit complet pour une requête de comparaison agentique) doit soit passer à `sonar` (contexte plus court, deep search moins agressive), soit reconstruire son prompt en découpant le corpus. Il n'y a pas de « choix par défaut » sans arbitrage.

Quatre, la Search API de Perplexity, qui est un produit distinct des chat completions, n'est pas touchée. Elle continue de fonctionner sans changement. Une intégration qui s'était appuyée sur la Search API pour récupérer des résultats bruts avec citations n'a rien à migrer.

Cinq, l'écart entre le billet blog et le guide de migration illustre un motif propre à cette période : les fournisseurs de moteurs IA font évoluer leurs surfaces plus vite qu'ils ne mettent leurs documents à jour de manière cohérente. Pour un consultant, l'implication opérationnelle est simple : la source de vérité sur une déprécation n'est pas le guide, c'est le changelog daté, et la bannière produit à côté du guide.

Trois concepts doctrine s'articulent. [[concepts/agentic-search]] gagne une matérialisation concrète du coût d'une couche agentique : les outils qui délèguent la sélection de sources à un endpoint tiers portent le risque de fournisseur, y compris quand le fournisseur retire une brique sans y renvoyer explicitement dans son guide de migration. [[concepts/metriques-visibilite-geo]] s'enrichit d'une contrainte de continuité : une mesure de citation IA n'a de valeur que si la chaîne d'interrogation est stable ou si les ruptures sont datées et documentées. Aujourd'hui, l'un des maillons casse, un consultant qui prend une décision sur une série temporelle Perplexity de septembre doit isoler avant et après le 27. [[concepts/structural-information-geo]] rappelle que la citation dans un moteur IA n'est pas une propriété d'une page, c'est une fonction d'une chaîne d'appels. Cette chaîne bouge sans préavis client-visible.

Cinq réserves méthodologiques.

Un, aucun communiqué officiel Perplexity n'a été publié à ce jour au moment de l'édition sur l'ampleur des migrations effectives réalisées par ses clients entreprise. Les données publiques disponibles sont : le billet blog du 13 août, l'entrée changelog de juillet, la table de correspondance modèle-preset. L'ampleur des incidents production éventuels post-retrait ne peut être mesurée qu'à partir de fin septembre.

Deux, la table de correspondance modèle-preset publiée par Perplexity comporte des écarts avec les données de benchmark publiées. Le billet blog affirme que le preset `low` délivre « roughly a 7x improvement on BrowseComp compared to Sonar Pro at approximately $0.05 per query ». Les benchmarks publiés par Perplexity indiquent un score de 40,00 pour `low` contre 7,33 pour `sonar-pro`, soit un facteur 5,46x, à 0,0679 $ par requête. L'annonce marketing est plus généreuse que la donnée.

Trois, la comparaison de coût entre `sonar-deep-research` et le preset `high` reste ambiguë. Le billet officiel affirme que les presets « can match Sonar Deep Research at a fraction of the cost », mais les benchmarks publiés montrent que `high` coûte plus cher que Deep Research sur deux des trois bancs (BrowseComp et WideSearch). La rhétorique de la migration cache un mix de gains et de pertes.

Quatre, aucun cas terrain public d'outil GEO tiers documentant sa propre migration au 27 septembre n'a été trouvé lors de la veille du matin. Les GitHub issues repérées (Canonry #1202, langgenius/dify #3942, artwork-archive #111, maximhq/bifrost #7236) sont des projets développeurs isolés, pas des éditeurs commerciaux de mesure GEO. La question de la continuité côté outils de mesure reste ouverte.

Cinq, le nombre d'utilisateurs entreprise de Sonar tiers pro n'est pas publié par Perplexity. L'ampleur macro-économique de la migration ne peut pas être chiffrée.

## Brève 1 — Product-Led SEO — PSOhub publie une étude 90 jours mesurant citations IA et vraies visites : 18 pages, 54 citations, 50 visites, 3 clics de démo

PSOhub, éditeur d'un CRM projet, publie avec The Rank Masters (TRM) une étude de cas 90 jours ([The Rank Masters](https://www.therankmasters.com/insights/benchmarks/psohub-ai-visibility-aeo-seo-case-study), publiée le 17 juillet 2026, révisée le 15 septembre 2026). L'expérimentation couvre 18 pages, mesurées sur une fenêtre glissante 16 avril-14 juillet 2026. Trois sources de mesure : Google Search Console (rankings et impressions), Google Analytics 4 (trafic et conversions), et la couche de visibilité IA de Semrush (citations sur ChatGPT, AI Overviews Google, AI Mode, Gemini).

Les chiffres rapportés en verbatim.

- « 12 of 18 pages reached page 1 of Google inside the window, the content earned 133,000 search impressions »
- « 12 pages were cited across 54 AI-answer prompts worldwide »
- « AI engines sent 50 real human visits (roughly 1 in 5 of all page views) »
- 6 pages ont produit au moins un clic sortant vers une page de démo produit ; 3 clics de démo et 1 inscription attribués à ces pages dans la fenêtre.

Ce que cette étude documente pour un praticien Product-Led SEO. La structure éditoriale testée n'est pas un calculateur, ni un simulateur, ni un générateur : c'est un système de contenu explicitement structuré autour d'une ICP (persona cible), avec des sections « answer-first » extractibles par un LLM (tableau, blocs scannables, réponse directe en tête). La documentation revendique une conception simultanée pour classement Google et retrieval LLM. Cf. [[concepts/product-led-seo]] et [[concepts/aeo]] pour le cadre.

Deux limites explicites.

Un, l'échantillon est de 18 pages sur un seul client B2B SaaS PSOhub, secteur project management. La transposition à un autre vertical n'est pas testée. Le taux de citation « 54 sur combien de prompts interrogés ? » n'est pas publié, la métrique de dénominateur (coverage) manque.

Deux, la fenêtre de mesure (16 avril-14 juillet 2026) est antérieure à plusieurs événements importants pour la citation IA : externalisation des liens dans AI Overviews (26,2 % en septembre), déploiement français d'AI Overviews (23 septembre), guerre des standards de commerce agentique (été 2026). Le résultat s'applique à un régime déjà daté.

## Brève 2 — Actualité SEO — Chartbeat mesure une chute de 40,2 % du trafic Google Search vers les éditeurs sur un an, sans que le trafic IA ne compense

Chartbeat publie le 24 septembre 2026 son 2026 Publisher Playbook. La reprise éditoriale de référence est celle de [Matt G. Southern dans Search Engine Journal](https://www.searchenginejournal.com/google-search-decline-publishers-chartbeat/590681/), avec verbatim et reprise indépendante par [Relevant Audience](https://www.relevantaudience.com/seo/chartbeat-google-search-publisher-traffic-down-40-percent/).

Chiffres verbatim :

- « 40.2% year-over-year decline for Google Search across its publisher network from July 2025 to July 2026 »
- Comparaison N-1 : « 21.9% decline » (juillet 2024 à juillet 2025). La pente s'aggrave.
- Part de Google Search dans le total des pages vues : « 9% of all pageviews » en juillet 2024 → « 5% » en juillet 2026.
- Google Discover : progresse de « 6.6% in the first year to 34.3% in the second » ; sur deux ans, la baisse cumulée est de « nearly 46% ».
- Trafic IA : « AI referrals grew 8x over two years and made up 0.01% of traffic ». Chartbeat note en outre que le trafic IA « declining across ChatGPT, Claude, Perplexity, Microsoft Copilot, and Gemini in 2026 ». Il baisse au moment où on le mesure.

Le total des pages vues mensuel reste stable à 31,1 milliards, porté par le trafic loyal (visiteurs venus au moins 8 des 16 derniers jours). Les nouveaux visiteurs baissent de 14 %, les visiteurs récurrents de 8 %.

Deux réserves. Un, l'échantillon Chartbeat penche vers les éditeurs presse et médias, la donnée ne se transpose pas mécaniquement à un site e-commerce ou un blog SaaS. Deux, le rapport ne détaille pas si les baisses en pourcentage portent sur des volumes bruts ou des parts, ce que Search Engine Journal indique explicitement dans ses réserves.

## Prédictions vérifiables

- **P-2026-09-27-1** — D'ici le 15 octobre 2026, au moins un éditeur d'outil GEO tiers parmi Peec AI, Otterly, Profound, Athena HQ, Scrunch, tryprofound, BrightEdge Copilot, RankAI, Rankscale, Siftly, Xfunnel AI publie un statut public documentant sa migration effective de Sonar vers l'Agent API de Perplexity, avec ou sans interruption de service. Confiance : 0,70.
- **P-2026-09-27-2** — D'ici le 31 décembre 2026, Perplexity publie soit une communication officielle sur le taux de migration effectif de ses clients entreprise (nombre ou pourcentage), soit un billet reconnaissant un besoin de compatibilité 200K sur l'Agent API. Confiance : 0,30.
- **P-2026-09-27-3** — D'ici le 31 mars 2027, un cabinet SEO ou GEO indépendant publie une reproduction du cadre PSOhub / TRM (18 pages, mesure trois sources GSC + GA4 + outil GEO tiers, fenêtre 90 jours) sur un vertical distinct (fintech, retail, edtech, e-commerce), avec chiffres publiés page par page. Confiance : 0,35.

## Sources

Info du jour — Perplexity Sonar retirement :

- [AI Watch Station — Perplexity Launches Agent API, Will Retire Sonar Endpoints in September (13 août 2026)](https://ai-watch-blog.vercel.app/en/posts/2026-08-13-perplexity-agent-api-launch/)
- [Ecorpit — Perplexity Sonar retires 27 September 2026](https://ecorpit.com/perplexity-sonar-retirement-september-27-agent-api-migration-2026/)
- [LLM Gateway blog — The Perplexity Sonar API Retirement: What Changes](https://llmgateway.io/blog/perplexity-sonar-api-retirement)
- [LLM Gateway changelog — Perplexity Sonar Changes September 25](https://llmgateway.io/changelog/perplexity-sonar-changes)
- [Dev.to (Kashif Manzer) — Two AI APIs die this weekend](https://dev.to/kashif_manzer/two-ai-apis-die-this-weekend-perplexity-sonar-sep-27-and-appsmith-ai-sep-30-599h)
- [Perplexity docs — Changelog](https://docs.perplexity.ai/docs/resources/changelog)
- GitHub issues corroborantes : [Canonry #1202](https://github.com/Canonry/canonry/issues/1202), [langgenius/dify-official-plugins #3942](https://github.com/langgenius/dify-official-plugins/issues/3942), [JuergenB/artwork-archive #111](https://github.com/JuergenB/artwork-archive/issues/111), [maximhq/bifrost #7236](https://github.com/maximhq/bifrost/issues/7236)

Brève 1 — PSOhub :

- [The Rank Masters — PSOhub AEO & SEO Case Study: AI Citation Wins](https://www.therankmasters.com/insights/benchmarks/psohub-ai-visibility-aeo-seo-case-study)

Brève 2 — Chartbeat Publisher Playbook :

- [Search Engine Journal — Google Search Decline Steepened To 40% YoY For Publishers (24 sept 2026)](https://www.searchenginejournal.com/google-search-decline-publishers-chartbeat/590681/)
- [Relevant Audience — Chartbeat: Google Search Publisher Traffic Down 40% YoY](https://www.relevantaudience.com/seo/chartbeat-google-search-publisher-traffic-down-40-percent/)
- [Chartbeat — 2026 Publisher Playbook (landing officielle)](https://lp.chartbeat.com/2026-publisher-playbook-chartbeat)
