# Algorithme, édition du 25 août 2026

## Résumé en 3 points

- **Recherche agentique** : Google transfère A2A à l'Agentic AI Foundation le 20 août, aux côtés du MCP d'Anthropic, ce qui met les deux protocoles agentiques les plus adoptés sous la même gouvernance neutre soutenue par AWS, Google, Microsoft, OpenAI, Anthropic, Bloomberg, Block et Cloudflare.
- **Niche SEO (éducation)** : Google a lancé le 19 août des outils d'étude natifs dans Search et Gemini (visualisations interactives, simulations 3D, quiz personnalisés, hub étudiant), en positionnant explicitement Gemini contre Knowt, Gauth et les autres plateformes edtech de tutorat.
- **Business SEO (e-commerce)** : Le Content API for Shopping de Google est arrivé à extinction le 18 août 2026, sans période de transition ; tout marchand qui n'a pas basculé sur la Merchant API voit ses appels ignorés, avec impact direct sur les listings, l'inventaire et Google Shopping.

---

## Info du jour, pilier Recherche agentique

### Google transfère A2A à l'Agentic AI Foundation, la stack agent converge sous une gouvernance unique

Le 20 août 2026, le Linux Foundation Directed Fund à l'origine de l'Agentic AI Foundation (AAIF) a annoncé le transfert du protocole Agent2Agent (A2A) de Google Cloud vers l'AAIF ([Yahoo/Forkast, 22 août](https://tech.yahoo.com/ai/gemini/articles/google-a2a-protocol-joins-aaif-020554895.html) ; [Axios, 17 août](https://www.axios.com/2026/08/17/a2a-agentic-ai-foundation-open-ai-standards) ; [Techzine, 17 août](https://www.techzine.eu/news/devops/143659/google-transfers-a2a-to-the-agentic-ai-foundation/) ; [AI Magazine](https://aimagazine.com/news/why-did-googles-a2a-join-the-agentic-ai-foundation) ; [Forbes/Janakiram MSV, 19 août](https://www.forbes.com/sites/janakirammsv/2026/08/19/agent2agent-joins-the-agentic-ai-foundation-alongside-mcp/) ; [DEVOPSdigest, 20 août](https://www.devopsdigest.com/google-agent2agent-protocol-joins-aaif)). A2A rejoint ainsi le Model Context Protocol (MCP) d'Anthropic, transféré au même véhicule en décembre 2025 lors de la création de l'AAIF, plus goose (Block) et AGENTS.md (OpenAI).

Les deux protocoles ne se recouvrent pas. MCP standardise la connexion verticale entre un agent et ses outils ou sources de données (base, API, fichier, moteur de recherche). A2A standardise la communication horizontale entre agents (négociation de tâche, échange d'identité, maintien d'état). La phrase du board relayée par Yahoo résume la répartition sans ambiguïté : « Where A2A fits is at the collaborative edge; where MCP fits is at the tool integration edge. »

L'AAIF passe de 49 membres fondateurs en décembre 2025 à plus de 250 membres à la date du transfert (source : [Yahoo/Forkast](https://tech.yahoo.com/ai/gemini/articles/google-a2a-protocol-joins-aaif-020554895.html) et [AI Magazine](https://aimagazine.com/news/why-did-googles-a2a-join-the-agentic-ai-foundation)). Les huit membres Platinum sont AWS, Anthropic, Block, Bloomberg, Cloudflare, Google, Microsoft, OpenAI. Le communiqué du Linux Foundation sur le premier anniversaire d'A2A avait déjà documenté l'adoption : 150+ organisations, intégration Azure AI Foundry et Copilot Studio (Microsoft), Amazon Bedrock AgentCore Runtime (AWS), Google Cloud, 22 000+ étoiles GitHub, SDK dans cinq langages ([Linux Foundation, 9 avril 2026](https://www.linuxfoundation.org/press/a2a-protocol-surpasses-150-organizations-lands-in-major-cloud-platforms-and-sees-enterprise-production-use-in-first-year)).

Ce que ce transfert change dans la mécanique d'un consultant SEO, GEO ou business search :

1. La question « faut-il miser sur A2A ou sur MCP » n'a plus de réponse binaire. Les deux couches sont hébergées par la même fondation neutre, sous le même Governing Board et le même Technical Committee, avec les mêmes bailleurs Platinum. Un marchand qui construit une intégration agent-first pour ChatGPT, Gemini, Copilot ou Claude peut prévoir la même couche transport et la même couche identité pour les quatre.

2. La négociation devient un critère d'infrastructure standard, pas un choix propriétaire de plateforme. Concrètement, un site qui expose déjà un endpoint MCP pour donner accès à ses données (catalogue produit, disponibilités, tarifs) devra prévoir un endpoint A2A pour interagir avec des agents extérieurs qui viennent négocier une transaction ou lever une identité. La fiche [[concepts/agentic-search]] du vault décrit déjà ce déplacement de l'objet à optimiser depuis « être affiché » vers « être sélectionné par un agent pour accomplir une tâche ». L'unification A2A + MCP sous une gouvernance unique valide cette lecture : la surface qu'un consultant travaille pour l'agentique n'est plus la page, c'est le contrat machine.

3. Le risque de fragmentation entre écosystèmes propriétaires baisse mais ne disparaît pas. OpenAI a co-fondé l'AAIF avec Anthropic et Block, ce qui rend crédible l'idée d'un socle commun. Deux points restent ouverts : l'AP2 (Agent Payments Protocol, adossé à A2A) n'est pas encore consolidé dans l'AAIF au même titre, et les extensions verticales d'ACP (Agentic Commerce Protocol de Stripe/OpenAI) et de goose (Block) coexistent. Attendre au moins un signal de convergence côté paiement avant de considérer la stack agent comme figée. Prédiction : l'AP2 est absorbé par l'AAIF avant fin 2026, ou reste en gouvernance Google Cloud avec une passerelle documentée vers A2A/MCP (à échéance 2026-12-31, confiance 0,55).

L'impact pour la doctrine du vault : le pilier Recherche agentique passe d'une phase où chaque grand acteur poussait son protocole (A2A côté Google, MCP côté Anthropic, ACP côté OpenAI, AGENTS.md côté OpenAI aussi) à une phase où la communication inter-agents et l'accès aux outils sont sous gouvernance neutre commune. C'est un fait structurel, pas une annonce produit. Le déplacement mérite une note d'extension pour [[concepts/agentic-search]] : ajouter une section « socle protocolaire commun A2A+MCP sous AAIF » avec la répartition collaborative edge / tool integration edge et la liste des huit membres Platinum. À valider en revue hebdo, pas d'écriture automatique.

Réserve doctrine [[concepts/tabou-visibilite]] : le transfert de gouvernance ne mesure pas la présence effective d'un site dans les réponses des agents. Un contrat machine standardisé rend possible l'intégration technique, il n'augmente pas mécaniquement le taux de citation. La mesure de citation reste à faire par site.

Prédictions ouvertes ajoutées ce run :
- P-2026-08-25-1 : l'AP2 (Agent Payments Protocol) rejoint formellement l'AAIF sous une convention d'hébergement identique à celle d'A2A avant le 2026-12-31 (confiance 0,55).
- P-2026-08-25-2 : au moins un des trois grands du search (Google, Bing/Microsoft, Perplexity) publie avant le 2026-12-31 une documentation d'intégration commune A2A + MCP pour son moteur agentique consommateur (confiance 0,60).

---

## Brèves

### Brève 1, pilier Niche SEO (éducation)

**Google a lancé le 19 août 2026 des outils d'étude natifs dans Search et Gemini, en concurrence explicite avec Knowt et Gauth**

Le 19 août 2026, Google a annoncé une série d'outils d'étude intégrés à Search et à Gemini ([TechCrunch, 19 août](https://techcrunch.com/2026/08/19/google-launches-new-study-tools-for-students-across-search-and-gemini/) ; [The AI Insider, 20 août](https://theaiinsider.tech/2026/08/20/google-rolls-out-new-ai-study-tools-across-search-and-gemini/) ; [The Next Web](https://thenextweb.com/news/google-students-free-ai-pro-gemini-study-tools) ; [ground.news](https://ground.news/article/google-launches-new-study-tools-for-students-across-search-and-gemini)).

Côté Search : visualisations interactives générées dans les AI Overviews (par exemple diagrammes d'échelle pH), simulations 3D pour les sujets complexes, quiz personnalisés en science, mathématiques, humanités et langues étrangères depuis une simple requête, création de documents d'étude à partir de PDF, présentations ou notes uploadées, intégration Lens pour la résolution guidée de problème (roll out « in the coming weeks »).

Côté Gemini : rapports de recherche multi-étape via Gemini Live avec discussion conversationnelle, simulations 3D fonctionnelles (par exemple visualisation ADN qu'on peut faire tourner et zoomer), hub d'apprentissage dédié combinant notebooks, flashcards et quiz. Google offre aussi une année de AI Pro gratuite aux étudiants US du supérieur, avec 5 To de stockage Google AI Pro pour les Américains et 400 Go pour les utilisateurs AI Plus internationaux. TechCrunch précise l'intention concurrentielle : « The launch of the new study features marks Google's latest effort to make Gemini the AI assistant that students turn to when learning and studying », en citant explicitement Knowt et Gauth comme cibles.

Le fait qui compte pour le pilier Niche SEO éducation : Google n'ajoute pas des liens vers Knowt, Gauth, Quizlet, Chegg ou Course Hero ; il génère des composants équivalents directement dans Search et dans Gemini. Pour un site edtech de tutorat ou de flashcards, ce n'est pas un ajout dans la SERP, c'est un remplacement partiel de la fonctionnalité qui faisait l'intérêt du site. Le pilier [[concepts/product-led-seo]] du vault décrit ce mécanisme comme la substitution d'une page-outil par une page-outil générée à la demande.

Trois lectures opérationnelles pour un consultant travaillant une niche edu :

1. Distinguer ce que Google fait bien en generative UI (visualisation d'un concept scolaire cadré, quiz sur une leçon donnée) et ce qu'il ne fait pas (parcours d'apprentissage longitudinal, correction d'exercice avec explication personnalisée sur historique élève, notation adaptative, préparation examen avec base d'annales locale). La défense d'une niche edu passe par l'accès à des données propriétaires ([[concepts/data-proprietaire]]) que Google ne peut pas générer à la demande.

2. Considérer la citation dans AI Overviews et AI Mode comme un canal distinct du clic. Un site edu qui fournit une explication canonique cité dans une AI Overview peut voir sa marque monter en notoriété sans clic mesurable. Ce n'est pas un revenu direct, c'est un signal amont ([[concepts/metriques-visibilite-geo]]).

3. Le passage en programme gratuit AI Pro d'un an pour les étudiants US du supérieur change la conversion sur les segments payants Chegg, Quizlet Plus, Course Hero. Prédiction P-2026-08-25-3 : au moins un de ces trois acteurs edu publie un chiffre de baisse de conversion (>10 %) attribué à l'offre Gemini avant le 2026-12-31, ou l'un d'eux annonce une contre-offre d'accès gratuit similaire (confiance 0,50).

Réserve : Google n'a publié aucun chiffre d'usage ni d'impact au 25 août 2026 sur ces nouveaux outils. Les métriques disponibles restent le contexte général AI Overviews (48 % des requêtes en mars 2026 selon la doc Google reprise plusieurs fois cet été). L'article TechCrunch ne cite aucun benchmark de qualité pédagogique. À traiter comme un fait de plateforme, pas comme une mesure d'impact.

### Brève 2, pilier Business SEO (e-commerce)

**Le Content API for Shopping de Google est arrivé à extinction le 18 août 2026, sans période de transition, tout marchand non migré vers Merchant API est coupé**

Google a fermé le 18 août 2026 le Content API for Shopping, remplacé par la Merchant API ([Google Merchant Center Help](https://support.google.com/merchants/answer/16493611?hl=en) ; [Productsup](https://www.productsup.com/blog/google-merchant-api-migration-what-changes-before-the-august-2026-deadline-and-how-to-prepare/) ; [WebProNews](https://www.webpronews.com/google-retires-content-api-for-shopping-in-2026-migration-essential/) ; [Yoma](https://yomadigital.com/moving-from-content-api-to-merchant-api-before-the-august-2026-deadline/) ; [Producthero](https://www.producthero.com/post/google-is-sunsetting-the-content-api-for-shopping-what-you-need-to-know) ; [Etavrian](https://www.etavrian.com/news/merchant-api-primary-content-api-sunset-2026) ; [Ekamoira](https://www.ekamoira.com/blog/migrating-from-content-api-to-merchant-api-v1-the-complete-developer-guide-for-2026)).

Sept jours après le sunset, un état précis :

- Les applications qui appellent encore le Content API après le 18 août 2026 ne reçoivent plus de réponse. Google n'a pas prévu de période de transition au-delà de cette date.
- Le périmètre affecté est spécifiquement les intégrations API. Les uploads manuels de fichier, les scheduled fetches et les feeds Google Sheets continuent à fonctionner sans modification.
- Toute intégration ecommerce, plateforme de gestion de flux, outil de feed management ou intégration custom qui reposait sur le Content API doit être basculée sur la Merchant API pour éviter la disruption des product listings, des mises à jour d'inventaire et des campagnes Google Shopping.
- La Merchant API expose des sous-API modulaires (products, inventory, promotions, reviews, accounts, reports) qui remplacent les endpoints monolithiques du Content API.

Ce que ça implique concrètement pour un consultant business SEO sur un compte marchand :

1. La première action est un audit d'intégration : identifier chaque système qui appelait le Content API (ERP, PIM, extension CMS, connecteur, script custom), vérifier son état de migration et son statut de production. Un marchand qui n'a pas fait l'audit avant le 18 août avait déjà perdu de la remontée de données au moment où cette brève est publiée.

2. Le second point de vigilance est la nouvelle segmentation du reporting Merchant Center annoncée par Google pour le 24 août 2026, qui sépare le trafic YouTube affiliate du trafic organique avec effet rétroactif au 1er juillet 2026 (fait déjà couvert dans l'édition matinale du 24 août). Un marchand qui subit à la fois la coupure du Content API et la restatement rétroactive du trafic YouTube affiliate voit ses métriques Google Shopping bouger pour deux causes distinctes, à ne pas confondre dans l'analyse.

3. La bascule sur Merchant API ouvre aussi Product Studio, la couche générative de fiches produit annoncée dans le nouveau kit d'outils. Ce n'est pas un remplacement du travail SEO merchandising ; c'est un accélérateur pour les catalogues qui n'ont pas les ressources pour rédiger des descriptions à la main. À traiter comme un outil, pas comme une source de vérité (la data produit et le journal serveur restent la source de vérité, cf. [[concepts/data-proprietaire]]).

Prédiction P-2026-08-25-4 : au moins un acteur tiers publie avant le 2026-12-31 un chiffre agrégé sur la part des marchands qui étaient encore sur Content API au 18 août 2026 (échantillon >1 000 marchands, source Productsup, DataFeedWatch ou équivalent), confiance 0,55.

Réserve : Google n'a pas publié de chiffre de marchands impactés au 18 août. Les alertes des feed management vendors (Productsup, DataFeedWatch, GoDataFeed) datent principalement de juillet et début août. La mesure du volume affecté reste à faire.

---

*Édition SyntheticBrain 2026-08-25. Rien n'a été envoyé. Draft dans `agent-synthetic/revuedepressIA/`.*
