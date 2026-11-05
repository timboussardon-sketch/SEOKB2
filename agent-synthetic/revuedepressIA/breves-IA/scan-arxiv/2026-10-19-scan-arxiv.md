# Scan ArXiv SEO/GEO, 2026-10-19

*Scan hebdomadaire de la littérature arXiv pertinente SEO/GEO/AEO. Collecte déterministe (API arXiv, script `arxiv-fetch.py`) + scoring /50 par candidat. Aucun envoi, sous-doc de brèves (`breves-IA/scan-arxiv/`).*

## Verdict de la semaine

Fenêtre élargie à 25 jours : aucun rapport depuis le 2026-09-25, les runs du lundi ont sauté. 10 candidats examinés, 4 retenus. Deux papers indépendants arrivent au même mécanisme : ChatGPT ne cite que ce que sa propre recherche a remonté, sur des sous-requêtes qu'il réécrit lui-même. Les propriétés de la page (FAQ, schema, vitesse) pèsent peu à l'intérieur d'un même site.

Couverture incomplète : la requête `abs:"citation" AND abs:"large language model"` a échoué aux deux tentatives (connexion coupée, puis HTTP 429). Des papers sur la citation par les LLM ont pu passer à travers.

## Études retenues

### 1. ChatGPT cite ce que sa recherche a trouvé, et nomme les marques dont il se souvient · `Score : 43/50`

**Source** : https://arxiv.org/abs/2610.15033
**Signal** : 🟢 Opportunité
**Impact business en 1 ligne** : Le levier GEO principal est d'être remonté par les sous-requêtes que le moteur réécrit, pas d'ajouter FAQ ou données structurées.

Deux collectes de 90 jours sur des questions commerciales dans deux marchés contrastés : 158 099 réponses, 468 037 citations (ChatGPT, Gemini, Perplexity). À l'intérieur d'un même site, un seul facteur de contenu joue : les pages dont le titre et les paragraphes correspondent aux questions posées sont plus citées. FAQ, données structurées, encadrés de synthèse et vitesse ne semblent efficaces qu'en comparant des sites différents. En rejouant les questions via les API, chaque page citée par ChatGPT a été retrouvée par sa propre recherche ; ce qui est retrouvé, sur des sous-requêtes réécrites à chaque réponse et qui coïncident rarement avec les résultats de Google ou Bing, explique 32 % de la variation, contre 2,8 % pour les propriétés de la page. ChatGPT injecte dans ses recherches les marques qu'il connaît, préfère les sites qu'il connaît, et nomme des marques sans page à l'appui ; des expériences contrôlées montrent que le nom de marque réordonne le classement de produits aux caractéristiques identiques. Résultats répliqués sur un marché de petits fournisseurs B2B. Données et code publiés.

**Lien avec la doctrine du vault** : chiffre `[[concepts/query-fan-out]]` avec une mesure à grande échelle (aujourd'hui la page ne repose que sur une source). Met en doute la part du schema et des FAQ dans `[[concepts/structural-information-geo]]` et `[[concepts/metriques-visibilite-geo]]`.

---

### 2. Un agent qui lit le site recommande 1,9 fois plus souvent l'entreprise · `Score : 39/50`

**Source** : https://arxiv.org/abs/2609.34951
**Signal** : 🟢 Opportunité
**Impact business en 1 ligne** : Être lisible par un agent qui ouvre le site pèse plus que d'être mentionné sur des forums et des listicles.

37 927 parcours d'agent, chacun une question d'acheteur sur une entreprise, sur 4 harnais indépendants et 1 056 entreprises réelles, appariées sur notoriété, connaissance préalable du modèle et deux indicateurs AEO, puis séparées selon leur niveau d'« agent experience » (AX). 7 à 10 % de la réponse finale vient des connaissances d'entraînement du modèle, que le site soit lisible ou non. Pour les entreprises « agent-ready », la réponse est construite à partir de leurs propres pages dans 78 % des cas contre 56 %, et elles sont clairement recommandées 1,9 fois plus souvent. À entreprise, harnais et question fixés, les réponses construites depuis le site sont 41 % plus exactes. L'échec dominant est l'omission : les réponses construites depuis le reste du web ont 3,7 fois plus de chances de ne contenir aucun des faits demandés. Le taux de recommandation varie d'un facteur 7 entre harnais, l'écart se maintient dans chacun.

Limites : papier de position (« We argue »), sans venue. L'abstract ne définit pas le critère AX et ne donne pas l'affiliation des auteurs. À vérifier dans le PDF avant toute citation client.

**Lien avec la doctrine du vault** : premier chiffrage de la lisibilité par agent pour `[[concepts/agentic-search]]`. Contredit en partie le paper n°1 sur le poids de la mémoire du modèle (7-10 % ici, marques injectées dans les recherches là-bas) : les deux mesurent des choses différentes, à ne pas opposer sans lecture des PDF.

---

### 3. Les lecteurs du Washington Post avec réponses IA consomment plus de sujets peu lus · `Score : 37/50`

**Source** : https://arxiv.org/abs/2609.38946
**Signal** : 🟡 À surveiller
**Impact business en 1 ligne** : Sur la recherche interne d'un éditeur, les réponses IA citées n'ont pas réduit la consommation d'articles par lecteur.

Expérience randomisée de terrain sur 37 561 lecteurs du Washington Post. Les deux groupes cherchent dans la même archive ; le groupe traité reçoit en plus une réponse IA avec citations d'articles au-dessus des résultats classiques. La consommation devient moins concentrée et se déplace vers des sujets moins populaires. Les lecteurs passent des clics sur résultats classiques vers les articles cités et les recherches de relance. Ils cherchent plus souvent, ce qui compense la baisse d'articles par recherche : la consommation d'articles par lecteur augmente légèrement.

Limite de transfert : c'est la recherche interne d'un éditeur, pas Google. Le résultat ne dit rien du trafic qu'un AI Overview renvoie vers un site tiers.

**Lien avec la doctrine du vault** : argument pour un client éditeur qui envisage une recherche IA sur son propre site.

---

### 4. Google et l'API OpenAI ne retrouvent qu'un quart des URL que ChatGPT cite · `Score : 34/50`

**Source** : https://arxiv.org/abs/2610.15382
**Signal** : 🟡 À surveiller
**Impact business en 1 ligne** : Un outil de suivi GEO qui passe par Google ou l'API OpenAI rate environ trois quarts des URL réellement citées par ChatGPT.

Étude observationnelle de quatre réglages ChatGPT Web, de GPT-5.2 à 5.5, en modes Instant et Thinking, aux niveaux URL, nom d'hôte et entité. Les modes Instant font surtout un seul tour de recherche ; GPT-5.4 Thinking en fait souvent plusieurs. Sur des exécutions répétées, une page plus souvent retrouvée est plus souvent citée. Google Search et l'API Responses servent de proxys : ils correspondent mieux à ChatGPT Web au niveau du nom d'hôte et de l'entité qu'au niveau de l'URL exacte, et même combinés ne retrouvent qu'environ un quart des URL citées. Un modèle supervisé combinant ces signaux atteint une AUC supérieure à 0,74 pour GPT-5.3 et GPT-5.5. L'abstract ne donne pas la taille de l'échantillon.

**Lien avec la doctrine du vault** : même mécanisme que le paper n°1 (retrouvé avant d'être cité), obtenu par une autre équipe. Pour `[[concepts/metriques-visibilite-geo]]` : mesurer au niveau du domaine et de l'entité plutôt que de l'URL, et refaire les mesures quand le modèle déployé change.

---

## Écartés

Sous le seuil malgré un sujet dans le périmètre :
- 2609.40069 : Conversational Capture, une source citée tôt dans une conversation est re-citée ensuite (score 28/50 : modèle théorique, illustration simulée sans donnée empirique ; accepté à HAI '26)
- 2610.21330 : VoteGEO-Bench, GEO appliqué aux élections US 2024 et Japon 2026 (score 28/50 : domaine électoral ; à noter : réorganiser la page ou renforcer l'argumentation rapporte plus qu'ajouter des preuves)
- 2610.20162 : Gap Detection, recherche d'angles non couverts dans un espace d'embeddings (score 25/50 : volet GEO marginal, gains faibles, proche de `[[concepts/surprise-gap]]`)

Hors périmètre :
- 2610.17243 : EneMonIE-Backend, extraction d'information sur l'énergie
- 2609.37311 : ReMem, agents de recommandation par OCR et mémoire
- 2609.33722 : BOReFT, optimisation bayésienne sur états cachés

## Candidats à ingestion complète

2610.15033 (What Drives AI Citations?) et 2609.34951 (AX is the New AEO). Les deux touchent directement `[[concepts/query-fan-out]]`, `[[concepts/structural-information-geo]]` et `[[concepts/agentic-search]]`, et leurs conclusions se recoupent mal sur le poids de la mémoire du modèle : une ingestion avec lecture des PDF trancherait. À décider par Tim.

## Candidat INFO DU JOUR newsletter Algorithme

Oui : 2610.15033. Angle possible : « ChatGPT cite ce qu'il a trouvé, pas ce que vous avez balisé » (32 % contre 2,8 %). Second choix : 2609.34951, angle « lisible par l'agent plutôt que mentionné partout », sous réserve de vérifier la définition AX et l'affiliation des auteurs.
