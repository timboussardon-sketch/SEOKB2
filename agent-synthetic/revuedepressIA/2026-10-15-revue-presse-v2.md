---
type: revue-presse
title: "Trois infrastructures de checkout agentique annoncées en une semaine : Constructor, TikTok, Rezolve"
pilier: agentic-search
date: 2026-10-15
version: v2
sources_count: 10
confidence: medium
status: draft
---

# Trois infrastructures de checkout agentique annoncées en une semaine : Constructor, TikTok, Rezolve

## À retenir en quatre points et deux réserves

- Trois acteurs indépendants ont annoncé en six jours (5 au 9 octobre 2026) une infrastructure permettant à un agent IA de finaliser un achat sans sortir du contexte conversationnel. Les architectures diffèrent : Constructor branche Stripe sur l'agent onsite du retailer, TikTok ouvre une couche plateforme avec plusieurs backends, Rezolve propose un protocole merchant-side utilisable par n'importe quel agent consommateur.
- Constructor annonce le 5 octobre que son agent de shopping onsite accepte désormais les paiements via Link by Stripe, dispositif disponible globalement. Stripe cite 250 millions de clients Link actifs et déclare que 80 % de son panel a utilisé un agent conversationnel au cours du mois précédent.
- Rezolve Ai (NASDAQ : RZLV) a présenté le 9 octobre RezolvePay, démontré avec un cas d'ordre en ligne via l'agent Meta Muse pour retrait en magasin. L'architecture est présentée comme protocole-aligné, ouvert à tout agent IA via intégration merchant approuvée.
- La couche vendeur se bouscule sur la même fenêtre : la Salesforce State of Commerce du 28 juillet 2026 indique une croissance de 200 % en un an de l'« agentic search » comme première étape du parcours d'achat, et une progression du trafic référencé depuis les chats IA comprise entre 150 % et 428 % en glissement annuel sur chaque trimestre mesuré.
- Réserve 1 : les trois annonces sont des communiqués d'acteurs vendeurs. Aucun chiffre d'adoption marchande indépendant, aucune mesure externe de conversion ou de volume ne corrobore pour l'instant ce que ces infrastructures produisent en pratique.
- Réserve 2 : les architectures restent fragmentées. Un marchand qui veut être atteignable par un agent OpenAI, un agent Meta Muse, un agent Google UCP et un agent TikTok doit intégrer plusieurs rails techniques, chacun avec sa gestion de la fraude, des remboursements et de l'attribution. L'une des trois annonces (Constructor) laisse non documentés les frais additionnels, la responsabilité de la fraude et les premiers résultats merchants.

## Info du jour — Agentic Search

Trois annonces publiques distinctes, publiées entre le 5 et le 9 octobre 2026, décrivent chacune une manière de finaliser un achat dans un contexte piloté par un agent IA plutôt que par un navigateur et un formulaire. Les trois acteurs ne couvrent pas la même partie de la chaîne et n'ont pas le même modèle de distribution. Prises ensemble, elles cadrent la question opérationnelle qu'un consultant SEO doit poser à un marchand ce trimestre : où placer l'intégration pour être atteignable par un agent, étant donné que la couche d'infrastructure n'est pas unifiée.

**Constructor et Stripe, agent onsite au retailer**

Le 5 octobre, Constructor a annoncé Agentic Checkout, une fonction permettant à son agent de shopping, déjà déployé en onsite chez des retailers, d'accepter directement un paiement via Link by Stripe ou d'autres méthodes supportées par Stripe. L'acheteur reste dans le dialogue avec l'agent du retailer pour la recherche, la comparaison et le paiement. Constructor déclare la disponibilité globale et présente l'opération comme la première intégration de Stripe dans un agent de shopping onsite ([PR Newswire](https://www.prnewswire.com/news-releases/constructor-launches-agentic-checkout-powered-by-stripeletting-shoppers-go-from-product-discovery-to-purchase-within-a-single-ai-agent-experience-302898353.html), [PYMNTS](https://www.pymnts.com/news/retail/2026/constructor-teams-with-stripe-to-debut-agentic-checkout-tool/), [Retail Tech Innovation Hub](https://retailtechinnovationhub.com/home/2026/10/4/constructor-claims-a-first-as-it-launches-agentic-checkout-solution-powered-by-stripe)).

Les chiffres cités dans le communiqué proviennent de Stripe : 250 millions de clients Link, 80 % du panel de Stripe ayant utilisé un agent conversationnel sur le mois précédent. Ces chiffres relèvent de la communication vendeur et n'ont pas été recoupés par une mesure indépendante. Stellagent note que le communiqué ne précise ni les frais additionnels éventuels ni la répartition de la responsabilité en cas de fraude ou de chargeback, et ne publie aucun résultat de retailer intégré ([Stellagent](https://stellagent.ai/insights/constructor-agentic-checkout-stripe)). Forkast rapporte que Sephora, Under Armour et The Very Group activeraient ces transactions en agent via Stripe, information non confirmée par une source indépendante.

L'architecture Constructor place le checkout dans l'agent du retailer, pas dans un agent tiers consommateur. La porte d'entrée reste le site du retailer. L'intérêt pour le retailer est de ne pas perdre l'acheteur au moment du passage en caisse, puisque la finalisation ne demande plus de redirection vers un parcours de paiement classique.

**TikTok, couche plateforme avec plusieurs backends**

Le même 5 octobre, à l'occasion d'Advertising Week New York, TikTok a présenté deux outils agentic : un assistant conversationnel qui répond aux questions produit, taille, expédition et disponibilité sur les pages produit des marchands dans son navigateur interne, et un dispositif « Buy Direct » qui déclenche un paiement en un clic depuis le flux For You avec les méthodes de paiement et adresses déjà stockées sur la plateforme ([TechRepublic](https://www.techrepublic.com/article/news-tiktok-ai-shopping-assistant-one-click-checkout/), [PYMNTS](https://www.pymnts.com/commerce/social-commerce/2026/tiktok-kicks-off-agentic-commerce-push-with-ai-shopping-assistant/), [Unite.ai](https://unite.ai/tiktok-unveils-buy-direct-checkout-and-ai-shopping-assistant/)).

L'infrastructure backend est fournie par quatre partenaires : Salesforce, Shopify, Shoplazza et Stripe. L'outil est disponible aux annonceurs via un programme de tests éligibles, pas en déploiement général. Les premières ouvertures sont réservées aux utilisateurs et marques des États-Unis. TikTok a également introduit un outil adjacent, « Agentic Leads », pour la génération de leads.

L'angle structurant de l'annonce est le choix de ne pas fournir le modèle de bout en bout, mais de connecter l'écosystème marchand existant (Shopify, Salesforce Commerce Cloud, Shoplazza) à une surface conversationnelle TikTok. Un marchand qui a déjà une plateforme Shopify ou Salesforce peut être atteignable par l'agent TikTok sans refonte, mais l'intégration spécifique reste à documenter côté partenaire. Les sources ne précisent pas de date de disponibilité générale.

**Rezolve Ai et RezolvePay, protocole merchant-side ouvert à tout agent**

Le 9 octobre, Rezolve Ai (NASDAQ : RZLV) a annoncé RezolvePay, présenté comme une couche de paiement et de commerce destinée à permettre à n'importe quel agent IA consommateur d'acheter chez les marchands intégrés. La démonstration mobilise l'agent Meta Muse interagissant avec l'agent RezolvePay d'un coffee shop pour finaliser une commande en ligne avec retrait en magasin ([GlobeNewswire](https://www.globenewswire.com/news-release/2026/10/09/3378056/0/en/rezolve-ai-opens-retail-to-any-ai-shopping-agent-with-rezolvepay-targeting-a-multi-trillion-dollar-commerce-opportunity.html), [AI Magazine](https://aimagazine.com/globenewswire/3378056)).

Rezolve présente l'approche comme protocole-aligné, destinée à autoriser un éventail large d'agents IA à déclencher des actions commerciales de manière contrôlée, auditable et validée côté marchand. L'annonce cite une estimation de McKinsey selon laquelle les agents IA pourraient intermédier 3 à 5 billions de dollars de commerce consommateur mondial à l'horizon 2030, chiffre à traiter comme projection cabinet et pas comme donnée observée.

L'orientation est symétrique à celle de Constructor : au lieu de placer l'agent côté retailer, Rezolve place une couche côté marchand qui expose les capacités commerce à tout agent consommateur conforme au protocole. L'annonce ne publie aucun chiffre de merchants intégrés en production, ni de résultats de ventes mesurées.

**Lecture consolidée : la couche agentique a trois positions distinctes**

Les trois annonces de la semaine du 5 octobre couvrent trois positions architecturales différentes dans la chaîne d'achat agentique :

1. **Agent du retailer** (Constructor) : l'acheteur reste client du retailer, l'agent est propriété du retailer, le paiement est intégré au dialogue.
2. **Couche plateforme** (TikTok Buy Direct + Shopping Assistant) : le réseau social fournit l'interface agentique, les backends marchands sont connectés via partenaires existants.
3. **Protocole merchant-side ouvert** (Rezolve RezolvePay) : le marchand expose une interface commerce consommable par tout agent consommateur tiers.

Ces trois positions ne sont pas mutuellement exclusives. Un retailer pourrait, à horizon 2027, être présent dans les trois : agent onsite Constructor pour la visite directe, intégration TikTok pour le trafic social, exposition RezolvePay (ou protocole équivalent) pour les agents OpenAI, Google UCP, Meta Muse. L'arbitrage opérationnel se joue sur le coût d'intégration par rail, la gestion de la fraude et la mesure de l'attribution.

**Trois lectures opérationnelles pour un consultant SEO**

Première lecture. L'audit « est-ce que mon client est atteignable par un agent » doit se décliner par rail. Un marchand entièrement intégré UCP Google peut rester invisible pour un agent Meta Muse ou TikTok. L'audit demande désormais de lister les agents cibles et de documenter la présence du marchand sur chacun.

Deuxième lecture. La position architecturale conditionne le ROI mesurable. Un agent du retailer (Constructor) produit de l'attribution propre côté retailer. Une couche plateforme (TikTok) attribue au canal social. Un protocole merchant-side ouvert (Rezolve) oblige à mesurer par agent entrant, instrumentation que la plupart des marchands ne tiennent pas encore. Le consultant SEO qui pousse un marchand vers l'une des trois positions sans discuter la mesure dépose une dépendance opérationnelle.

Troisième lecture. Les trois annonces sont des communiqués de vendeurs, publiés sur fils de presse (PR Newswire, GlobeNewswire) et relayés par PYMNTS, TechRepublic, Unite.ai, Retail Tech Innovation Hub. Aucun chiffre indépendant de volume, de conversion ou d'adoption marchande ne consolide pour l'instant la lecture. Un diagnostic produit à ce stade sur ces infrastructures doit être qualifié de prospectif, pas de retour terrain.

**Lien doctrine**

Cette lecture confirme la description de [[concepts/agentic-search]] : le SEO devient « être sélectionné par l'agent pour accomplir une tâche ». Les trois annonces structurent la couche « accomplir », pas la couche « sélectionner », et nouent la deuxième à la première par l'intégration technique. Un marchand sélectionné par l'agent mais non intégré techniquement n'est pas atteignable. L'écart entre les deux couches était jusqu'ici théorique, il devient opérationnel ce trimestre.

L'article [[concepts/metriques-visibilite-geo]] indique que la mesure de présence IA doit distinguer la citation (apparition dans la réponse) de la sélection (choix par l'agent). Les trois annonces ajoutent une troisième dimension à mesurer : la capacité technique d'intégration du marchand au rail de finalisation. Un marchand peut être cité, sélectionné, puis échouer à la finalisation faute de rail intégré.

## Brèves

### GEO / search IA — Salesforce State of Commerce : agentic search +200 % en un an, trafic référencé depuis les chats IA jusqu'à +428 % par trimestre

La 4e édition de la Salesforce State of Commerce (publiée le 28 juillet 2026) rapporte que l'« agentic search » comme première étape du parcours d'achat a progressé de 200 % en un an. Le trafic référencé depuis les chats IA a progressé entre 150 % et 428 % en glissement annuel sur chaque trimestre mesuré, pendant que le trafic global des sites marchands progressait à un chiffre ou en bas de la plage à deux chiffres. 28 % des organisations commerce utilisent déjà de l'IA agentique, 44 % supplémentaires prévoient d'adopter dans les six mois. Le rapport s'appuie sur un sondage de 3 450 professionnels commerce et 4 690 consommateurs, plus des données comportementales sur plus de 1,5 milliard d'acheteurs ([Salesforce newsroom](https://www.salesforce.com/news/stories/agentic-search-growth/), [Shopifreaks relais](https://www.shopifreaks.com/shoppers-now-open-purchase-journeys-in-ai-chats-200-more-than-a-year-ago-according-to-salesforces-state-of-commerce-report/)).

**Réserve** : les 200 % mesurent la croissance en glissement annuel de l'usage de l'agentic search comme première étape, pas une part de marché. Les éditions régionales publient des chiffres partiellement divergents (44 % global vs 52 % APAC pour l'intention d'adoption dans les six mois).

**Angle consultant** : une mesure cabinet non-vendeur sur un échantillon équivalent reste à venir. L'adoption marchande à 28 % place le consultant SEO face à des clients qui n'ont pas encore d'instrumentation agentique, et à qui il faudra documenter la mesure avant la mise en œuvre.

### Business SEO — Les trois annonces d'infrastructure fragmentent la question du choix de rail

Le marchand qui veut être atteignable par un agent IA se trouve devant une matrice qui n'existait pas il y a trois mois. Google UCP (annoncé NRF janvier 2026, étendu Google I/O mai 2026, couvre Amazon et Walmart parmi les partenaires de lancement selon un relais Shopappy), ChatGPT Instant Checkout (ouverture Etsy puis extension), Microsoft Copilot Checkout (lancé début 2026 aux US avec PayPal, Shopify, Stripe), auxquels s'ajoutent cette semaine Constructor, TikTok et Rezolve ([Shopappy analyse](https://shopappy.com/payments/card-networks/agentic-checkout-holiday-2026)).

Chacune de ces couches a sa gestion de la fraude, son attribution et son coût d'intégration. Pour un marchand mid-market, l'arbitrage « où intégrer en priorité » devient un projet SEO-GEO à part entière, pas un chantier IT isolé. Un cabinet indépendant qui publierait une matrice d'intégration marchand (coût, délai, part du trafic agentique capturé) serait précieux. Aucun n'a publié ce document à la date du 15 octobre.

**Réserve** : la source Shopappy est un relais analytique secondaire. Les détails de partenariat UCP (Amazon, Walmart) relèvent de communications vendeurs antérieures, à vérifier auprès de Google avant toute déclaration client.

### Actualité SEO — Rezolve Ai cite une projection McKinsey de 3 à 5 billions USD, à cadrer comme projection cabinet

Le communiqué Rezolve du 9 octobre cite McKinsey : les agents IA pourraient intermédier 3 à 5 billions USD de commerce consommateur mondial à l'horizon 2030. Ce chiffre est à cadrer comme projection cabinet, pas comme donnée mesurée. Il repose sur un scénario d'adoption qui dépend de l'intégration marchande, précisément ce que les trois annonces de la semaine commencent à instrumenter.

Pour un consultant SEO, l'usage prudent de ce type de projection est de la citer avec sa borne basse et sa borne haute, sa date d'origine (publication McKinsey 2025, source dans le communiqué Rezolve), et le fait qu'elle est reprise par un acteur vendeur ayant un intérêt commercial direct à la narration d'un marché multi-billion ([Rezolve release](https://www.globenewswire.com/news-release/2026/10/09/3378056/0/en/rezolve-ai-opens-retail-to-any-ai-shopping-agent-with-rezolvepay-targeting-a-multi-trillion-dollar-commerce-opportunity.html)).

**Réserve** : la projection McKinsey originale n'est pas liée dans le communiqué Rezolve. Un consultant qui l'utilise doit retrouver la source primaire avant publication client.

## Prédictions datées

Trois prédictions ouvertes ce run :

1. **P-2026-10-15-v2-1** (confiance 0,55, échéance 2027-03-31) : au moins l'un des trois acteurs annoncés cette semaine (Constructor, TikTok Buy Direct + Shopping Assistant, Rezolve RezolvePay) publiera un chiffre indépendant d'adoption marchande (nombre de retailers intégrés en production, volume de transactions traité) avant le 31 mars 2027.
2. **P-2026-10-15-v2-2** (confiance 0,45, échéance 2027-06-30) : un cabinet indépendant non-vendeur publiera une matrice d'intégration marchand couvrant au moins quatre rails agentic checkout (incluant UCP, ChatGPT Instant Checkout, Copilot Checkout, Rezolve ou équivalent) avant le 30 juin 2027.
3. **P-2026-10-15-v2-3** (confiance 0,35, échéance 2026-12-31) : les trois acteurs resteront dans le périmètre « vendor claims only » sans mesure externe de conversion ou d'attribution agentique avant le 31 décembre 2026.

---

*Édition v2 — 15 octobre 2026. Rien n'est envoyé.*
