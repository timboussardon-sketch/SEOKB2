---
type: revue-presse
title: "Algorithme — édition du 2026-10-07 (v2)"
date: 2026-10-07
pilier_info_du_jour: Agentic search
piliers_breves: [GEO / search IA, Niche SEO, Actualité SEO]
sources_consultees: 11
sources_nouvelles: 0
tags: [algorithme, agentic-search, ucp, merchant-center, ai-mode, gemini, nano-banana, healthcare-review-snippets, spam-update]
status: draft
---

# Algorithme — édition du 2026-10-07 (v2)

## Résumé

- Google ouvre l'onboarding au Universal Commerce Protocol (UCP) depuis le Merchant Center, pilote restreint aux marchands américains, avec un bouton de checkout actif sur les product listings dans AI Mode de Google Search et dans Gemini, extension prévue en Australie et au Canada en 2027.
- Nano Banana 2.1 est déployé dans AI Mode de Google Search, annoncé par Robby Stein, VP Product in Search, sur X le 6 octobre 2026, avec un accès par un bouton banane sous la barre de recherche de l'application Google.
- Google a supprimé les Review Snippets sur les pages de santé en deux vagues, mai et août 2026, avec des tests Schema App qui n'ont pas réussi à restaurer les snippets en modifiant les chemins de propriétés ou en combinant les types avec Product, sans effet corrélé mesuré sur le trafic organique.
- La phase 3 du Google September 2026 spam update s'est déroulée du 4 au 6 octobre 2026 selon Search Engine Roundtable, dans une fenêtre de rollout atypique de deux semaines annoncée par Google au départ du 24 septembre, avec une volatilité modérée sur les trackers tiers et des remontées de perte de trafic sur certains sites news.

## Info du jour : Google ouvre l'onboarding au Universal Commerce Protocol via le Merchant Center, pilote US avec checkout actif dans AI Mode et Gemini

**Pilier : Agentic search.**

### Ce que Google publie : une page support qui décrit comment un marchand s'inscrit au UCP depuis le Merchant Center

Le 7 octobre 2026, Search Engine Roundtable publie « Google Merchant Center New UCP Integration Hub » ([seroundtable.com, 7 oct 2026](https://www.seroundtable.com/google-merchant-center-ucp-integration-hub-42243.html)) à partir d'un signalement de Hana Kobzova sur PPC News. L'article renvoie à une page support Google publiée dans la section Merchant Center, « How to onboard to the Universal Commerce Protocol in Merchant Center » ([support.google.com/merchants/answer/16992327](https://support.google.com/merchants/answer/16992327)), et à une page développeur « Universal Commerce Protocol integration in Merchant Center » ([developers.google.com/merchant/ucp/guides/tools/merchant-center](https://developers.google.com/merchant/ucp/guides/tools/merchant-center)).

La page support Google décrit l'UCP avec cette formulation : « The Universal Commerce Protocol (UCP) is a new open standard for agentic commerce that enables agents and systems to work together across the commerce ecosystem. » Elle précise que l'intégration dans Merchant Center « is gradually rolling out in the U.S., with Australia and Canada to follow next year », et liste quatre fonctions côté marchand : implémenter un bouton de checkout sur les product listings éligibles, le transfert de panier vers le site du marchand, le test du flow de checkout, et les APIs natives de checkout.

Les deux surfaces concernées sont nommées explicitement : « a checkout button on eligible product listings in AI Mode in Google Search and on Gemini ». Autrement dit, UCP est le mécanisme technique qui permet à un agent AI, à l'intérieur de AI Mode ou dans Gemini, de déclencher et de finaliser un achat sur un produit marchand sans que l'utilisateur quitte la surface AI.

### Ce qui change concrètement pour un marchand US éligible

La procédure d'onboarding tient en quatre étapes documentées : implémentation technique selon le UCP developer guide, remplissage d'un formulaire d'intérêt, sélection par Google, puis accès au Merchant Center avec un environnement sandbox pour valider l'intégration avant la bascule en production. Le Merchant Center reste le point d'entrée pour la data produit : « Merchant Center will continue to be the central hub to prepare your product data to show ads and listings on Google surfaces ».

L'ouverture via le Merchant Center change la nature de l'adhésion. Avant cette intégration, le UCP était un standard annoncé au NRF 2026 avec Shopify, Walmart et Target comme partenaires initiaux. L'onboarding passait par des canaux partenaires ou des contacts commerciaux Google. Le hub ouvre maintenant la demande à tout marchand déjà présent dans Merchant Center aux États-Unis, qui remplit le formulaire et attend la sélection Google. Il reste un pilote : la page e-commerce.news note que l'accès est « visible only to pilot merchants in the US » et que l'application se limite aux produits « sold within the US », avec checkout actif via Google Pay et support natif de PayPal selon les notes de cette couverture ([e-commerce.news, consultée le 7 oct 2026](https://e-commerce.news/story/google-unveils-open-ucp-standard-for-ai-driven-shopping)).

Pour un marchand hors US, la bascule reste prospective, avec Australie et Canada annoncés pour 2027 selon la page support Google ([support.google.com/merchants/answer/16992327](https://support.google.com/merchants/answer/16992327)).

### Lecture pour un consultant SEO ou e-commerce

Trois conséquences factuelles se dégagent de la documentation.

Premièrement, la data produit du Merchant Center devient un prérequis d'éligibilité à un canal AI commerce distinct des Shopping Ads classiques. Un flux produit incomplet ou désynchronisé exclut mécaniquement le marchand de l'affichage du bouton de checkout dans AI Mode et dans Gemini. La fiabilité du feed, la fraîcheur des prix et la cohérence des identifiants deviennent des conditions d'accès à une nouvelle surface, pas un enjeu d'optimisation marginale.

Deuxièmement, l'adhésion à UCP n'est pas un paramètre côté SEO. C'est une implémentation API côté backend du marchand, qui doit exposer des endpoints de checkout vérifiables dans le sandbox Merchant Center. Un site qui ne porte pas cette implémentation reste visible dans AI Mode et Gemini au titre de ses pages produit organiques, mais sans bouton de checkout actif. Deux canaux coexistent : la citation organique de la page produit, et l'exécution agentique de l'achat via UCP.

Troisièmement, le périmètre US pilote restreint aujourd'hui l'impact mesurable à ce marché. Un marchand européen peut suivre la trajectoire annoncée (Australie, Canada en 2027), mais ne peut pas aujourd'hui tester son intégration en production. Google a signalé que le Merchant Center reste le point central de la préparation data produit pour toutes ses surfaces, ce qui vaut aussi hors du périmètre UCP.

Un point reste explicitement non documenté dans la page Google consultée le 7 octobre : la méthodologie de sélection des marchands pilotes après soumission du formulaire d'intérêt. Google ne publie pas de critère quantitatif (volume de ventes, catégorie produit, performance historique Merchant Center) pour expliquer qui est accepté et qui attend.

## Brèves

### Brève 1 : Nano Banana 2.1 déployé dans AI Mode de Google Search, accès via un bouton dans l'application Google

**Pilier : GEO / search IA.**

Le 6 octobre 2026, Robby Stein, VP of Product in Search chez Google, annonce sur X : « Nano Banana 2.1 is rolling out in AI Mode in Search ! », couverture par Search Engine Roundtable le même jour ([seroundtable.com, 6 oct 2026](https://www.seroundtable.com/nano-banana-21-google-ai-mode-42246.html)). Nano Banana 2.1 est le modèle d'image Google qui, selon la documentation Google reprise par la couverture, « outperforms our previous models across the board, with notable leaps in visual design, mask-based editing, and subject consistency ».

L'accès utilisateur est précis : ouvrir l'application Google, taper le bouton banane sous la barre de recherche pour lancer la création d'image. La trajectoire du modèle est documentée : Nano Banana est arrivé dans Google Lens un an plus tôt, étendu à AI Mode en décembre, puis à AI Overviews en juillet, avant cette version 2.1 dans AI Mode. L'édition de masque et la cohérence du sujet entre plusieurs générations successives sont les deux améliorations citées par Google.

Lecture pour un acteur GEO : AI Mode devient explicitement une surface multimodale, où la génération d'image est intégrée au même point d'entrée que les requêtes textuelles. Pour un marchand ou un éditeur dont les visuels sont utilisés comme matière première par l'utilisateur (via upload ou édition), la question de la provenance et de l'attribution de l'image générée se pose. Google ne documente pas aujourd'hui de signal d'attribution automatique vers la source de l'image d'origine quand elle est modifiée dans AI Mode.

### Brève 2 : Google supprime les Review Snippets sur les pages de santé, deux vagues documentées depuis mai 2026

**Pilier : Niche SEO.**

Search Engine Roundtable publie le 7 octobre 2026 « Google Drops Review Snippets For Healthcare Web Pages » ([seroundtable.com, 7 oct 2026](https://www.seroundtable.com/google-drops-healthcare-review-snippets-42248.html)), à partir d'une analyse signée Andrea Badder, Content and SEO Manager chez Schema App, publiée sur le blog de l'éditeur ([schemaapp.com, consultée le 7 oct 2026](https://www.schemaapp.com/schema-markup/healthcare-review-snippets-have-dropped-heres-why-were-not-worried/)).

Deux vagues de suppression sont documentées : « since late May » 2026 pour une première baisse large, puis « another drop occurring in early August for some organizations » 2026 pour une seconde vague sur certains périmètres clients. Les entités concernées côté healthcare sont nommées : physicians, locations, services, specialties, et leurs relations schematiques. Schema App a testé plusieurs chemins de rattrapage : variations de connexion de `aggregateRating`, chemins de propriétés alternatifs, multi-typing avec `Product`. Verbatim Schema App : « Testing different ways of connecting aggregateRating, alternative property paths, and multi-typing healthcare entities with Product did not restore Review Snippet performance ». Aucune de ces manipulations schema n'a restauré les snippets.

Un signal important sur l'impact traffic : « We have not seen evidence that the decline in review snippets is translating into a corresponding decline in overall organic traffic ». La disparition visuelle n'est pas automatiquement une perte de clics organiques mesurés.

Google n'a pas publié de communication officielle associée. La page Rich Results pour les Review snippets n'exclut pas explicitement le vertical healthcare côté documentation Google : la suppression semble opérationnelle au niveau du rendering des SERP, sans mise à jour correspondante du support documentaire côté Google. Barry Schwartz confirme l'observation sur ses propres recherches : « I do not personally see them coming up when I do searches for doctors, dentists, etc, outside of the local results ».

Lecture pour un consultant SEO healthcare : la perte des review snippets ne justifie pas la suppression du balisage schema côté site, puisque le balisage reste utile aux signaux E-E-A-T et à l'éligibilité à d'autres surfaces (Knowledge Panel, Local Pack). La priorité se déplace sur le monitoring des positions et du CTR pour détecter un éventuel effet retard, et sur la négociation d'autres formes de preuve sociale (volume d'avis, mention Local Pack) à défaut du snippet dans la SERP standard.

### Brève 3 : Phase 3 du Google September 2026 spam update, rollout du 4 au 6 octobre 2026 selon Search Engine Roundtable

**Pilier : Actualité SEO.**

Search Engine Roundtable publie le 6 octobre 2026 « Final Phase Of Google September 2026 Spam Update Rollout Oct 4-6 ? » ([seroundtable.com, 6 oct 2026](https://www.seroundtable.com/google-september-2026-spam-update-phase-3-42239.html)). Barry Schwartz y énonce : « I believe we are seeing the final phase of the Google September 2026 spam update rolling out between October 4th and October 6th, today ».

La chronologie du rollout est maintenant publique : annonce Google le 24 septembre 2026, premiers jours d'impact du 25 au 27 septembre, phase 2 identifiée les 30 septembre et 1er octobre 2026 ([seroundtable.com, phase 2](https://seroundtable.com/google-september-2026-spam-update-two-42209.html)), phase 3 identifiée du 4 au 6 octobre 2026. Google a communiqué dès le départ que le rollout de cette spam update s'étalait sur deux semaines, « versus the typical two-day rollout », ce qui préparait plusieurs vagues sur une même update.

La volatilité est qualifiée de modérée sur les trackers tiers, cumulant Mozcast, SEMRush Sensor, AWR, Wincher, Serpstat, Sistrix, AccuRanker Grump, DataForSEO SERP Volatility, Mangools SERPWatcher, CognitiveSEO et Algoroo selon la couverture Search Engine Roundtable. Les retours communauté sur l'article mentionnent des pertes de trafic jusqu'à 80 % sur des sites news avec une forte dépendance aux snippets organiques.

Un point méthodologique à retenir : Google ne confirme pas phase par phase le rollout. Le découpage par phases vient de l'observation Barry Schwartz sur plusieurs cycles de volatilité, pas d'une communication Google explicite. Pour un site touché, le relevé jour par jour sur plusieurs outils reste la seule méthode pour attribuer une perte à cette update plutôt qu'à un changement d'infrastructure ou à une variation saisonnière.

## Rappel

Aucune de ces informations n'a été envoyée. Draft produit, non publié.
