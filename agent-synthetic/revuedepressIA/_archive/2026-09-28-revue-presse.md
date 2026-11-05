---
title: "Google Research publie R4T-Diffusion, un compilateur de fan-out qui rend la génération de sous-requêtes 12 à 20 fois plus rapide : ce que ça change dans la mécanique de sélection des sources par la recherche IA"
date: 2026-09-28
pilier_info_du_jour: Actualité SEO
piliers_breves: [Product-Led SEO, Recherche agentique]
edition: 69
---

# Google Research publie R4T-Diffusion, un compilateur de fan-out qui rend la génération de sous-requêtes 12 à 20 fois plus rapide : ce que ça change dans la mécanique de sélection des sources par la recherche IA

*Édition Algorithme — 28 septembre 2026 (matin) — SyntheticBrain*

- Google Research publie le 15 septembre 2026 un billet documentant un framework, « Retrieve-for-Train », qui remplace la génération autoregressive de sous-requêtes par un modèle de diffusion de 53,9 millions de paramètres entraîné hors ligne par renforcement, avec un gain de vitesse annoncé de 12 à 20 fois sur la couche de fan-out ([Google Research](https://research.google/blog/bypassing-inference-bottlenecks-accelerating-complex-ai-search-with-retrieve-for-train/), reprise par [Roger Montti, Search Engine Journal, 24 septembre](https://www.searchenginejournal.com/google-announces-new-query-fan-out-framework-r4t-diffusion/590700/)).
- Le papier « Efficient, Property-Aligned Fan-Out Retrieval via RL-Compiled Diffusion » est un poster ICML 2026 (poster 66354, arXiv 2603.06397), la publication n'est pas un déploiement en production, elle est présentée comme « production-ready » côté billet Google Research.
- Trois propriétés au niveau de l'ensemble des sous-requêtes sont optimisées explicitement dans l'entraînement : diversité (Vendi Score), ancrage (distance à la variété de la base), alignement. Cette formulation retire la garantie que chaque sous-requête isolée maximise un signal classique de pertinence individuelle.
- Ryan Law, Ahrefs, publie le 16 juillet 2026 une analyse de la stratégie des free tools comportant huit cas chiffrés de calculateurs, convertisseurs et générateurs qui rankent, avec un pic à environ 508 826 visites mensuelles US pour un hub de templates Canva ([Ahrefs](https://ahrefs.com/blog/the-free-tools-seo-strategy/)).
- Depuis le 15 septembre 2026, la valeur par défaut de Cloudflare bloque deux catégories de bots IA (Training et Agent) sur les pages qui affichent de la publicité, tandis que la catégorie Search reste autorisée ([Cloudflare Blog, 1er juillet](https://blog.cloudflare.com/content-independence-day-ai-options/) pour l'annonce ; [rapport TechnologyChecker, 3 septembre](https://technologychecker.io/blog/robots-txt-ai-crawlers-blocking-report) pour la mesure d'adoption des directives robots.txt tierce).

## Info du jour — Actualité SEO — R4T-Diffusion et la mécanique de fan-out des moteurs IA : ce que la publication Google Research déplace dans la chaîne de sélection des sources

Google Research publie le 15 septembre 2026 un billet signé Pengcheng Jiang, Student Researcher, et Judith Yue Li, Senior Research Engineer, qui documente une architecture appelée Retrieve-for-Train, abrégée R4T ([Google Research](https://research.google/blog/bypassing-inference-bottlenecks-accelerating-complex-ai-search-with-retrieve-for-train/)). Le billet renvoie à un poster ICML 2026, poster 66354, titré « Efficient, Property-Aligned Fan-Out Retrieval via RL-Compiled Diffusion », arXiv 2603.06397 ([ICML 2026](https://icml.cc/virtual/2026/poster/66354)). Roger Montti reprend l'annonce sur Search Engine Journal le 24 septembre ([Search Engine Journal](https://www.searchenginejournal.com/google-announces-new-query-fan-out-framework-r4t-diffusion/590700/)). MarkTechPost publie une analyse technique le 16 septembre ([MarkTechPost](https://www.marktechpost.com/2026/09/16/google-research-introduces-retrieve-for-train-r4t-an-rl-compiled-diffusion-retriever-for-12x-to-20x-faster-query-fan-out/)). L'événement est donc corroboré par une source primaire officielle Google et par plusieurs sources secondaires indépendantes.

La mécanique du framework, telle que la décrit le billet Google Research, tient en trois étapes.

Un, un modèle de langage fan-out est entraîné par renforcement avec une récompense composite formulée au niveau de l'ensemble des sous-requêtes : trois propriétés sont pénalisées ou récompensées, la diversité (mesurée par le Vendi Score sur l'ensemble des sous-requêtes générées), l'ancrage nommé « Groundedness » (distance à la variété de la base documentaire, formulation retenue par le billet : « Groundedness: Penalizes distance to the database manifold »), et l'alignement à l'intention initiale.

Deux, ce modèle coûteux en calcul sert à produire des paires d'entraînement synthétiques qui incorporent ces optimisations au niveau ensemble.

Trois, un modèle de diffusion léger de 53,9 millions de paramètres apprend à mapper un embedding de requête vers un ensemble d'embeddings cibles en une seule passe non autoregressive, sans passer par la génération de tokens de chaîne de raisonnement. Le billet formule ce contournement ainsi : « bypassing the need for text-based CoT reasoning tokens ». Le résultat annoncé côté latence est un gain de 12 à 20 fois par rapport à l'approche autoregressive, avec une latence autoregressive proche de 50 secondes sous larges batches et une latence R4T comprise entre la sous-seconde et quelques secondes.

Le vocabulaire technique du papier importe pour lire correctement ce que ça change côté sélection de sources. Le fan-out de requêtes est le mécanisme par lequel un moteur IA décompose une intention de départ en un ensemble de sous-requêtes distinctes, qui sont ensuite exécutées séparément contre la base d'index, avant que les résultats soient agrégés dans la réponse générée. La fiche interne [[concepts/query-fan-out]] documente cette mécanique. La documentation Google Search sur AI Overviews confirme que le fan-out est une opération standard, la publication de R4T-Diffusion documente désormais une méthode d'accélération dédiée à cette étape.

Cinq lectures opérationnelles pour un consultant SEO ou GEO qui suit la question de la sélection des sources par les moteurs IA.

Un, la propriété récompensée à l'entraînement est un score composite au niveau de l'ensemble, pas un score de pertinence individuelle sous-requête par sous-requête. Un moteur IA qui exploiterait ce type de fan-out ne cherche pas une sous-requête « optimale » isolée, il cherche un ensemble diversifié, ancré et aligné. Une page qui matche parfaitement une seule sous-requête mais qui produit un ensemble redondant avec d'autres candidates peut être remplacée par une page moins ciblée qui contribue à la diversité de l'ensemble.

Deux, le paramètre « Groundedness » pénalise explicitement la distance à la variété documentaire de la base. Le papier ne détaille pas quelle base est utilisée à l'entraînement, ni si un moteur en production utiliserait la même formulation. Un consultant qui recommande de « couvrir tout le champ sémantique » d'un sujet peut néanmoins tirer une lecture directionnelle : contribuer à la variété plutôt qu'occuper un pic isolé, avec un ancrage dans un corpus documenté par ailleurs.

Trois, la génération en une seule passe non autoregressive retire une étape traçable de la chaîne de raisonnement. Une chaîne de tokens de raisonnement est lisible et inspectable côté sortie textuelle ; un embedding produit par un modèle de diffusion l'est nettement moins. Ça déplace la question de l'auditabilité côté producteur du contenu : ce qui a déclenché la sélection d'une page dans un ensemble de sous-requêtes générées par diffusion sera moins explicable par verbatim d'une chaîne de raisonnement, davantage explicable par proximité vectorielle à un embedding cible.

Quatre, la vitesse annoncée est une variable de coût côté moteur. Un fan-out qui passait à 50 secondes sous grands batches devient sous-seconde à quelques secondes. Ça n'implique pas mécaniquement plus de sous-requêtes, mais ça élargit la faisabilité économique d'un fan-out plus riche. Un moteur qui, pour des raisons de coût, se limitait à trois sous-requêtes peut techniquement en générer dix. Le billet Google Research fait explicitement mention de dix sous-requêtes générées simultanément dans son évaluation. La conséquence côté consultant est une hypothèse à surveiller : si un déploiement effectif suit cette recherche, la longue traîne conversationnelle traitée par le moteur augmentera, avec une pression supplémentaire sur la couverture d'un sujet et non sur la seule intention primaire.

Cinq, le statut du travail est un poster de recherche ICML 2026 accompagné d'un billet blog qui utilise l'expression « production-ready ». Le déploiement effectif au sein d'AI Overviews, AI Mode ou d'un autre produit Google n'est pas confirmé par un billet Google Search Central ni par un billet officiel The Keyword. Traiter la publication comme un signal directionnel sur les prochains déplacements de la couche de fan-out est raisonnable ; traiter la publication comme une modification en cours d'AI Overviews serait prématuré.

Trois concepts doctrine s'articulent. [[concepts/query-fan-out]] gagne une variable technique de production : la couche de fan-out peut désormais tourner sous-seconde grâce à une distillation vers un modèle de diffusion léger, ce qui déplace le plafond économique du nombre de sous-requêtes. La fiche doit intégrer la distinction entre fan-out autoregressive (traçable en texte) et fan-out par diffusion (traçable en espace vectoriel), et la conséquence côté auditabilité. [[concepts/structural-information-geo]] gagne une confirmation : la sélection de sources par un moteur IA est le résultat d'une chaîne d'appels dont chaque étage optimise pour ses propres propriétés, pas d'un attribut de la page seule ; ici la couche fan-out optimise pour la diversité et l'ancrage d'un ensemble, pas pour la pertinence individuelle. [[concepts/agentic-search]] hérite d'une conséquence côté coût : la couche fan-out devient économiquement compatible avec un fan-out plus riche, ce qui pousse davantage de chaînes d'appels à composer une réponse à partir d'un plus grand nombre de sources, avec un poids relatif de chaque source qui baisse mécaniquement.

Cinq réserves méthodologiques.

Un, le papier utilise des datasets d'évaluation fashion et musique avec des modèles open source (Gemma3-4B, Qwen3-4B). L'extrapolation au fan-out d'un moteur IA de recherche générale, sur du contenu web hétérogène, avec un modèle propriétaire Google, est une inférence, pas un fait documenté dans le papier. Le billet Google Research ne publie pas d'évaluation sur Search.

Deux, le gain annoncé de 12 à 20 fois porte sur la latence de la couche fan-out isolée. Il ne mesure pas l'impact bout en bout sur la latence d'une requête AI Overview, qui inclut le fan-out mais aussi la récupération, la re-ranking, la synthèse et le rendu. Un consultant qui reprendrait le chiffre pour caractériser la latence d'AI Overviews en général surinterpréterait la mesure.

Trois, le papier documente un modèle diffusion de 53,9 millions de paramètres. Ce chiffre caractérise le modèle de la publication de recherche, pas nécessairement un modèle éventuellement déployé côté Google Search. Un modèle en production peut être plus grand ou plus petit selon les contraintes de latence et de qualité.

Quatre, la formulation « production-ready » côté billet Google Research est un jugement de l'équipe recherche, pas une confirmation d'intégration à un produit. Roger Montti sur Search Engine Journal note explicitement que le statut de déploiement n'est pas confirmé officiellement par Google.

Cinq, les récompenses composites au niveau ensemble supposent une définition explicite de la base documentaire cible et de la métrique de diversité (Vendi Score dans le papier). Une équipe côté moteur qui déploierait cette famille de méthodes conserve une latitude de calibrage : la diversité peut être plus ou moins pénalisée, l'ancrage plus ou moins strict. La lecture opérationnelle pour un consultant reste directionnelle, pas quantitative.

Trois prédictions vérifiables datées.

- P-2026-09-28-1 : d'ici le 31 mars 2027, ni Google Search Central ni The Keyword ne publient un billet confirmant l'intégration effective de R4T-Diffusion à AI Overviews ou AI Mode (confiance 0,70).
- P-2026-09-28-2 : d'ici le 31 décembre 2026, au moins un outil GEO tiers (Peec AI, Otterly, Profound, Athena HQ) publie une mesure du nombre médian de sous-requêtes générées par AI Overviews sur un panel de 1 000 requêtes ou plus, avec ou sans citation explicite de R4T (confiance 0,45).
- P-2026-09-28-3 : d'ici le 30 juin 2027, la publication R4T inspire au moins un papier ou un billet technique documentant une architecture similaire chez un moteur IA concurrent (Perplexity, OpenAI, Anthropic, xAI), fan-out non autoregressive par distillation vers un modèle léger (confiance 0,55).

## Brève 1 — Product-Led SEO — Ryan Law, Ahrefs : huit cas chiffrés de free tools qui rankent, et ce que la doctrine confirme à l'aune du filtre substitution UI générative

Ryan Law, Director of Content Marketing chez Ahrefs, publie le 16 juillet 2026 sur le blog Ahrefs un long article titré « The Free Tools SEO Strategy: How to Rank With Calculators, Converters, and Generators » ([Ahrefs](https://ahrefs.com/blog/the-free-tools-seo-strategy/)). L'article documente le sous-dossier writing-tools d'Ahrefs, monté à partir de zéro mi-2023, qui a atteint près d'un million de visites organiques US par mois à son pic et se stabilise dans les centaines de milliers. L'article liste huit cas concrets, chacun avec le mot-clé cible, l'outil et le trafic organique US mensuel : Omni Calculator (margin calculator, 49 169 visites), Gusto (hourly paycheck calculator, 17 776), Shopify (profit margin calculator, 4 550), Clockify (military time converter, 31 391), Adobe (PDF-to-Word converter, 402 101), FreeConvert (video compressor, 259 715), HubSpot (email signature generator, 54 653) et Canva (templates hub, 508 826).

Trois lectures pour une prestation Product-Led SEO conduite en 2026.

Un, la stratégie free tools continue de tenir sur des requêtes procédurales où l'utilisateur attend un output, pas un article. Le mot-clé « pdf to word » ou « email signature » ne se résout pas par une définition ni par une comparaison, il se résout par un rendu. La doctrine [[concepts/product-led-seo]] rappelle cette distinction, en cohérence avec la catégorie « Do » de [[concepts/know-simple-know-do]] : un moteur, IA ou classique, qui rend un outil ne remplace pas un outil, il le référence.

Deux, le test de substitution codifié dans [[concepts/test-substitution-llm]] s'applique frontalement. Un article qui explique comment convertir un PDF en Word peut être 80 % substituable par une réponse IA générée à la volée ; un outil qui convertit réellement le PDF en Word ne l'est pas. La différence n'est pas mineure, elle décide de la durabilité de la page face à AI Overviews et AI Mode. Un consultant qui recommande un investissement free tools en 2026 doit vérifier que le mot-clé cible est un mot-clé « Do » au sens strict, pas un « Know » déguisé qui produirait une page procédurale substituable.

Trois, la publication Google Research R4T-Diffusion documentée dans l'info du jour renforce la doctrine dans un sens précis. Si le fan-out d'un moteur IA gagne en richesse (10 sous-requêtes plutôt que 3, latence sous-seconde), les requêtes conversationnelles couvertes par une réponse générée s'élargissent. Les pages procédurales substituables sont plus exposées à cette expansion. Les pages qui offrent un rendu réel (calculateur, générateur, convertisseur, simulateur) ne le sont pas au même degré : elles restent une destination, pas un contenu à résumer.

Trois réserves.

Un, l'article Ahrefs date du 16 juillet 2026, dix semaines avant cette édition. Les chiffres de trafic reflètent une capture antérieure à la fenêtre de bilan post-core update de mai et à la bascule des défauts Cloudflare du 15 septembre. Un free tool en Q4 2026 opère dans un contexte de crawlers plus contrôlés et d'AI Overviews plus riches en sous-requêtes.

Deux, Ryan Law travaille pour Ahrefs, qui commercialise elle-même des free tools. L'article documente un cas où l'entreprise éditrice a un intérêt direct dans le résultat qu'elle rapporte. Les huit autres cas cités sont indépendants d'Ahrefs, ce qui limite le biais, mais la sélection des cas reste à la main de l'auteur.

Trois, le trafic organique US mensuel cité par outil est un chiffre Ahrefs, produit par le crawler et l'estimateur d'Ahrefs. La comparaison avec un chiffre GA4 ou GSC de l'éditeur des pages référencées ne peut pas être faite à la lecture de l'article seul.

Cf. [[concepts/product-led-seo]], [[concepts/test-substitution-llm]] et [[concepts/know-simple-know-do]] pour l'articulation doctrinale.

## Brève 2 — Recherche agentique — Depuis le 15 septembre 2026, Cloudflare bloque par défaut deux catégories de bots IA sur les pages avec publicité : le paramètre par défaut, le périmètre effectif, et ce que ça retire à la couverture d'un site

Cloudflare annonce le 1er juillet 2026, dans un billet signé sur son blog corporate, une modification des paramètres par défaut de gestion des bots IA, effective le 15 septembre 2026 ([Cloudflare Blog](https://blog.cloudflare.com/content-independence-day-ai-options/)). Le billet documente trois catégories distinctes : Search, Agent, Training. Deux catégories, Agent et Training, sont bloquées par défaut sur les pages qui affichent de la publicité. La catégorie Search reste autorisée par défaut. Un rapport tiers publié par TechnologyChecker le 3 septembre 2026 mesure l'adoption des directives robots.txt et documente les tendances d'accès pour août 2026 ([TechnologyChecker](https://technologychecker.io/blog/robots-txt-ai-crawlers-blocking-report)).

Trois points factuels précis.

Un, le changement s'applique aux nouveaux clients Cloudflare, aux nouveaux sites ajoutés par les clients existants, et à tous les clients existants sur l'offre gratuite. Les clients payants existants ont été notifiés en amont et peuvent opter hors de ce comportement dans leur zone security settings. Cloudflare héberge plus de 20 % des domaines web selon le billet du 1er juillet.

Deux, le rapport TechnologyChecker du 3 septembre, qui s'appuie sur l'API Cloudflare Radar et sur un snapshot de 4 223 fichiers robots.txt au 31 août 2026, mesure les ratios blocage/autorisation par user-agent : GPTBot ratio 2,33 pour 1, ClaudeBot ratio 2,39 pour 1, Bytespider ratio 5,80 pour 1, OAI-SearchBot ratio 0,94 pour 1 (donc légèrement plus autorisé que bloqué). Le rapport formule la lecture d'ensemble ainsi : « Publishers are not blocking "AI". They are blocking training and allowing answering — and they are doing it to the same companies. » Le taux de code HTTP 403 sur les crawlers IA atteint 12,92 % la semaine du 27 juillet 2026, contre 9,64 % en moyenne juillet.

Trois, le sous-ensemble Agent recouvre les bots qui exécutent une action pour un utilisateur (agent shopping, agent d'assistance), distinct des Training bots qui collectent du contenu pour l'entraînement de modèles. La documentation Cloudflare détaille cette distinction dans ses pages « Block AI Bots ».

Trois lectures pour une prestation SEO ou GEO qui couvre la surface d'un site.

Un, la couverture d'un site par un bot Agent peut désormais échouer par défaut sur les pages monétisées par publicité, sans que le propriétaire ait explicitement changé son robots.txt. Un consultant qui audite pourquoi une marque n'apparaît pas dans les réponses d'un agent shopping (Perplexity Comet, ChatGPT Atlas) doit désormais vérifier le paramètre Cloudflare du domaine, pas seulement le robots.txt du site.

Deux, la distinction Search / Agent / Training remplace le raisonnement binaire « autoriser ou bloquer un bot ». Un bot OpenAI OAI-SearchBot qui remonte dans le rapport TechnologyChecker à 0,94 pour 1 traduit une acceptation dominante côté éditeurs pour la surface answer, tandis qu'un GPTBot à 2,33 pour 1 traduit un refus dominant côté surface training. Un consultant qui recommande une politique bot doit énoncer clairement quelle catégorie il autorise ou bloque, pas juste un opérateur.

Trois, l'écart entre le comportement d'un bot Agent conforme aux directives et celui d'un bot masqué en user-agent Chrome documenté par Cloudflare mi-2025 pour Perplexity Comet reste un angle mort du paramètre par défaut. Un blocage Cloudflare des bots Agent déclarés ne bloque pas mécaniquement une session Comet qui se présente comme un navigateur Chrome depuis Browserbase. La couverture effective par les agents dépend donc à la fois du paramètre bot Cloudflare et de la politique de détection browser côté fournisseur.

Trois réserves.

Un, la mesure TechnologyChecker porte sur un snapshot robots.txt de 4 223 fichiers, pas sur l'univers Cloudflare complet. L'extrapolation à l'ensemble des domaines Cloudflare est une inférence, pas une mesure directe. Le rapport donne des ratios sur les fichiers publiés, pas sur le trafic couvert.

Deux, le paramètre par défaut Cloudflare s'applique aux pages avec publicité, pas à toutes les pages d'un site. Le périmètre « pages avec publicité » n'est pas défini de façon opérationnelle dans le billet Cloudflare du 1er juillet ; la documentation renvoie à la détection automatique par Cloudflare.

Trois, un consultant qui recommande à un client de changer son statut Cloudflare doit vérifier si le client est bien sur une offre gratuite ou nouveau client (concerné par le défaut) ou sur une offre payante existante (statut inchangé sauf action explicite). Le message opérationnel côté client dépend directement de ce statut.

Cf. [[concepts/agentic-search]] pour la distinction agent / training / search côté surface d'accès et [[concepts/structural-information-geo]] pour la conséquence côté sélection de sources.

---

*SyntheticBrain, 28 septembre 2026, matin. Aucune publication. Draft.*

**Sources primaires citées** :
- [Google Research, 15 septembre 2026](https://research.google/blog/bypassing-inference-bottlenecks-accelerating-complex-ai-search-with-retrieve-for-train/)
- [ICML 2026 poster 66354](https://icml.cc/virtual/2026/poster/66354)
- [Cloudflare Blog, 1er juillet 2026](https://blog.cloudflare.com/content-independence-day-ai-options/)

**Sources secondaires citées** :
- [Roger Montti, Search Engine Journal, 24 septembre 2026](https://www.searchenginejournal.com/google-announces-new-query-fan-out-framework-r4t-diffusion/590700/)
- [MarkTechPost, 16 septembre 2026](https://www.marktechpost.com/2026/09/16/google-research-introduces-retrieve-for-train-r4t-an-rl-compiled-diffusion-retriever-for-12x-to-20x-faster-query-fan-out/)
- [Ryan Law, Ahrefs, 16 juillet 2026](https://ahrefs.com/blog/the-free-tools-seo-strategy/)
- [TechnologyChecker, 3 septembre 2026](https://technologychecker.io/blog/robots-txt-ai-crawlers-blocking-report)
