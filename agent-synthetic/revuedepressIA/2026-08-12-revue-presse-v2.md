---
date: 2026-08-12
edition: 2026-08-12-v2
pilier_info_du_jour: GEO
piliers_breves: [Recherche agentique]
capture_mode: native
draft: true
---

# Algorithme — édition du 12 août 2026 (v2)

*Draft SyntheticBrain. Analyste search / IA. Rien n'a été envoyé.*

## En 3 points

- Kevin Indig publie sur [Search Engine Land le 12 août 2026 à 8h00 ET une analyse de 35 000 URL de citations de ChatGPT](https://searchengineland.com/community-signals-ai-largest-third-party-source-484606) (données Profound, décembre 2025, US, 3 177 prompts SaaS classés en 4 étapes de parcours d'achat) qui documente que les plateformes communautaires (Wikipedia, Reddit, LinkedIn) captent 17,1 % des citations de domaines tiers dans la réponse générée, contre 4,0 % pour la presse et 7,4 à 13,2 % pour les sites d'avis selon l'étape.
- Wikipedia, Reddit et LinkedIn représentent [99 % des citations communautaires](https://www.growth-memo.com/p/community-signals-are-ais-largest) dans l'échantillon, dont Wikipedia pour 10,1 à 14,0 points de pourcentage sur le plancher de 17 points, avec un caveat de méthode : l'étude porte sur une seule surface générative (ChatGPT), un seul mois (décembre 2025), un seul marché (US) et un seul verticale (prompts SaaS).
- Cloudflare a annoncé le 4 août 2026, pendant sa Agents Week, deux produits distincts de son pay-per-crawl de 2025 : [Cloudflare Wallets, portefeuille de stablecoins pour agents IA, et cloudflare.pay, identifiant lisible qui rattache un agent à une organisation](https://www.searchenginejournal.com/cloudflare-gives-ai-agents-wallets-that-pay-for-what-they-access/584959/) ; le règlement passe par le code HTTP 402 (protocole x402 dont Visa, Mastercard, American Express, Google, Shopify et Stripe sont membres au sein d'une fondation Linux).

## Info du jour — GEO : Kevin Indig chiffre à 17 % la part des plateformes communautaires dans les citations de ChatGPT sur des prompts SaaS

Kevin Indig a publié le [10 août 2026 sur Growth Memo](https://www.growth-memo.com/p/community-signals-are-ais-largest) une analyse conduite en février 2026 pour G2 sur environ 35 000 URL de citations extraites via l'outil de suivi Profound. La version [republiée sur Search Engine Land le 12 août 2026 à 8h00 ET](https://searchengineland.com/community-signals-ai-largest-third-party-source-484606) reprend le contenu à l'identique, sans donnée nouvelle. Une [reprise Optimixed du même jour](https://www.optimixed.com/the-free-tools-seo-strategy-how-to-rank-with-calculators-converters-and-generators/) est un simple relais éditorial, à considérer comme non indépendante.

### Ce que l'échantillon mesure et ne mesure pas

Le jeu de données couvre une seule surface (ChatGPT), un seul marché (États-Unis), un seul mois (décembre 2025) et un seul verticale (prompts formulés autour de vendeurs SaaS). 3 177 prompts sont classés en quatre étapes du parcours d'achat, avec une répartition très inégale : 376 en découverte, 1 179 en exploration, 1 367 en évaluation, 255 en évaluation restreinte. La déduplication retient une URL par exécution, par intention et par domaine.

L'étude sépare deux masses de citations : le domaine du vendeur cité par la réponse (part majoritaire, 66,7 à 71,8 % selon l'étape), et les citations tierces (domaines autres que le vendeur). Le résultat marquant porte sur cette seconde masse.

### Les chiffres à retenir

Les citations communautaires (UGC, contenu produit par les utilisateurs) captent 17,1 % du total tiers, contre 4,0 % pour la presse. Le rapport est donc supérieur à 4 pour 1 en défaveur de la presse.

La comparaison plus fine avec les sites d'avis, qui sont les concurrents directs de Wikipedia et Reddit pour la caution de pairs, donne quatre points de mesure par étape :

- Découverte : 17,8 % communautaire contre 7,4 % avis.
- Exploration : 18,2 % communautaire contre environ 9,5 % avis.
- Évaluation : 15,1 % communautaire contre 13,2 % avis (l'étape où l'écart entre les deux masses est le plus faible).
- Évaluation restreinte : 17,2 % communautaire contre 8,4 % avis.

À aucune étape le contenu produit par des sites d'avis ne dépasse le contenu communautaire, y compris à l'étape d'évaluation où la caution de pair est théoriquement la plus concentrée sur les plateformes d'avis.

Dans la masse communautaire, Wikipedia, Reddit et LinkedIn représentent 99 % des citations. Wikipedia pèse à elle seule entre 10,1 et 14,0 points de pourcentage sur le plancher de 17 points, selon l'étape. Le reste (YouTube, Quora, forums spécialisés, Discord) tient dans le pour cent restant.

Un chiffre secondaire est utile pour cadrer le canal payé : plus de la moitié des prompts SaaS analysés emploient un vocabulaire commercial (comparaison, alternative, meilleure solution), mais seuls 1,5 % nomment explicitement un vendeur.

### Ce que le fait déplace pour un consultant SEO ou GEO en mandat SaaS

Trois enseignements se dégagent, à sourcer dans un rapport client avec les caveats méthodologiques ci-dessus.

1. La doctrine [[concepts/arbitrage-plateforme-publication]] reçoit une extension AI answer engines chiffrée. La règle « regarde la SERP avant de choisir la plateforme » gagne un corollaire pour la réponse générative d'un moteur IA sur prompts commerciaux SaaS : « regarde quelles plateformes sont citées avant de choisir où publier ». Sur ChatGPT US décembre 2025 sur SaaS, la réponse quantifiée est : d'abord Wikipedia, ensuite Reddit et LinkedIn. Un consultant qui recommande un plan éditorial d'entreprise SaaS sans thread Reddit à valeur ajoutée, sans post LinkedIn signé par un opérateur, sans fiche Wikipedia à jour quand elle est éligible, laisse hors de son plan 17 % du plancher de citation tiers documenté.

2. La doctrine [[concepts/data-proprietaire]] doit distinguer deux types de propriété. La donnée propriétaire au sens Tim (chiffre de terrain, étude commandée, benchmark interne) reste la ressource la plus difficile à reformuler par un moteur génératif. Mais la donnée propriétaire au sens communautaire (post signé de l'équipe sur LinkedIn, réponse d'un ingénieur sur Reddit, mise à jour d'entrée Wikipedia quand elle est légitime) est la ressource qui compose les 17 % communautaires mesurés. Une politique de contenu qui n'adresse que la première laisse la seconde à des tiers non contrôlés.

3. La doctrine [[concepts/metriques-visibilite-geo]] gagne un plancher de comparaison utile : à jour de décembre 2025, un consultant qui construit un tableau de mesure GEO d'entreprise SaaS peut viser comme cible de reporting « part des citations tierces qui viennent de Wikipedia + Reddit + LinkedIn » et la remonter chaque semaine. Un plancher de 17 % dans un échantillon indépendant donne un point de référence à défendre en revue de direction.

### Limites explicites

L'étude est cadrée sur SaaS et n'est pas transposable telle quelle en e-commerce, en édition médias, en services professionnels réglementés (santé, finance, juridique) où la répartition des citations tierces peut différer largement. La couverture est mono-moteur (ChatGPT) : ni Perplexity, ni Gemini, ni AI Overviews Google, ni Copilot, ni Claude, ni Meta AI ne sont mesurés dans le même exercice. La période (décembre 2025) date de neuf mois à la date de l'édition ; l'instabilité mensuelle des citations documentée par Profound et SparkToro (40 à 60 % de variation d'un mois à l'autre selon les mesures) impose une reproduction sur un mois récent avant de figer le chiffre comme référence client. La commande de l'étude vient d'un vendeur (G2) qui bénéficie commercialement à ce que la valeur des sites d'avis soit remise en cause ; l'analyse est traçable via Profound, mais le lecteur qui utilise ces chiffres doit citer l'origine.

### Prédictions datées (`predictions.jsonl`)

- **P-2026-08-12-v2-1** : Un cabinet tiers indépendant (Profound, Peec AI, Ahrefs Brand Radar, Semrush AI Toolkit, Similarweb) publie avant le 30 juin 2027 une reproduction de l'étude Indig avec un échantillon multi-moteur (au moins ChatGPT plus un second moteur parmi AI Overviews, Perplexity, Gemini) qui confirme un plancher communautaire supérieur à 12 % dans au moins une seconde surface. Confiance 0,55.
- **P-2026-08-12-v2-2** : Une étude tierce publiée avant le 31 décembre 2026 mesure la même répartition sur un verticale hors SaaS (e-commerce, presse, services réglementés) et documente une inversion (sites d'avis > communautaire) sur au moins un verticale. Confiance 0,60.
- **P-2026-08-12-v2-3** : Un outil GEO grand public (Ahrefs Brand Radar, Semrush AI Toolkit, Otterly, Peec AI) ajoute avant le 31 mars 2027 une colonne de reporting explicite « part communautaire des citations tierces » ou équivalent segmentée par source (Wikipedia, Reddit, LinkedIn), au-delà de la simple mention de citations en volume. Confiance 0,40.

---

## Brève 1 — Recherche agentique : Cloudflare ajoute une couche de portefeuille et d'identité pour agents IA, distincte du pay-per-crawl

Cloudflare a présenté le 4 août 2026, pendant sa Agents Week, deux produits que [Search Engine Journal reprend le 12 août 2026](https://www.searchenginejournal.com/cloudflare-gives-ai-agents-wallets-that-pay-for-what-they-access/584959/) sous la signature de Slobodan Manic. Ils s'ajoutent au pay-per-crawl lancé le 1er juillet 2025 (couvert par plusieurs éditions précédentes), sans le remplacer.

### Le contenu de l'annonce

Le premier produit, **Cloudflare Wallets**, s'adresse aux acheteurs. Un compte détenu par un humain (Account Wallet) contient des fonds en stablecoins. Cet humain crée des portefeuilles virtuels (Virtual Wallets) qu'il attribue à des agents IA via une clé API, avec trois limites paramétrables : une allocation totale, une liste blanche de destinataires autorisés, et un plafond par transaction. L'agent règle en pair à pair sur le portefeuille du vendeur, sans intermédiation par Cloudflare comme marchand de dossier (Merchant of Record).

Le second produit, **cloudflare.pay**, est un identifiant lisible optionnel. Un agent peut se déclarer sous la forme `research.example.cloudflare.pay`, ce qui rattache le portefeuille virtuel à une organisation nommée. L'identifiant s'appuie sur les paires de clés du protocole Web Bot Auth (draft IETF, standardisé par Cloudflare et Google en 2025). Un site marchand peut exiger la déclaration ou l'accepter comme information sans la rendre bloquante.

Le règlement passe par le code HTTP 402 « Payment Required » et le protocole associé **x402**, standardisé au sein d'une fondation dont les membres publics annoncés comprennent Visa, Mastercard, American Express, Google, Shopify, Stripe.

L'ouverture des réservations d'identifiants `cloudflare.pay` date du 4 août 2026 ; la mise en production de la couche de paiement n'a pas de date publique, la documentation renvoie à des sorties « prochaines » (« soon », « in the coming months »). Aucune date de disponibilité générale, aucun stablecoin, aucun réseau blockchain, aucun partenaire de garde des actifs (custody) nommés à date.

### Ce qui distingue ce lancement du pay-per-crawl 2025

Le pay-per-crawl offrait trois options au marchand par crawler : autoriser gratuitement, facturer au prix configuré à l'échelle du domaine, ou bloquer. C'était une infrastructure côté vendeur, applicable au seul crawl. La couche Wallets + cloudflare.pay étend le modèle à trois dimensions :

- Elle passe du seul crawl à toute forme d'accès à une ressource (page, API, endpoint).
- Elle ajoute un mécanisme côté acheteur (le portefeuille attribué à l'agent) au mécanisme côté vendeur qui existait déjà.
- Elle passe de la facturation carte à l'échelle du domaine à des micropaiements en stablecoins réglés en pair à pair à l'échelle de la requête.

### Ce que le fait déplace pour un consultant SEO ou GEO en mandat éditeur ou marchand

Deux points de méthode sont à intégrer dès maintenant dans les audits, indépendamment de la date de mise en production complète.

Un éditeur ou marchand qui active demain la couche Wallets accepte des paiements en stablecoins réglés en pair à pair via HTTP 402. Cette architecture ne passe pas par un acquéreur cartes ni par une plateforme de paiement classique, ce qui change la comptabilité, la conformité KYC et la fiscalité par rapport à un panier standard. Un audit qui recommande d'activer la couche doit remonter au directeur financier avant l'équipe SEO, pas l'inverse.

L'identifiant cloudflare.pay permet à un agent de se déclarer comme représentant d'une organisation. Un site marchand peut construire une politique différenciée par déclaration : autoriser gratuitement les agents d'une liste blanche (partenaires connus, agents éditoriaux légitimes), facturer les agents génériques, bloquer les agents non identifiés. Cette politique se pilote côté serveur, elle est indépendante des règles `robots.txt`, et elle appelle une doctrine d'identification des agents que peu de sites ont formalisée à date. La fiche [[concepts/agentic-search]] gagne une variable de politique explicite au-delà de l'autorisation binaire (autoriser / bloquer) : autoriser sous condition d'identification vérifiée.

### Limites explicites

Aucune date publique de disponibilité générale du règlement en stablecoins. Le protocole x402 est standardisé au sein d'une fondation, mais aucune implémentation en production à large échelle n'est documentée à date par un marchand hors du périmètre Cloudflare. Le mécanisme de garde des actifs (qui détient les stablecoins des Account Wallets, sous quel régime réglementaire) n'est pas explicité dans la communication de Cloudflare. La liste des membres x402 (Visa, Mastercard, American Express, Google, Shopify, Stripe) atteste d'un engagement de gouvernance, elle ne préjuge pas d'un déploiement en production chez chacun de ces acteurs.

---

*Draft SyntheticBrain. Rien n'a été envoyé.*
