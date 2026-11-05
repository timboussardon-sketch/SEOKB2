---
type: revue-presse
title: "Algorithme. 28 août 2026 v2"
date: 2026-08-28
pilier_info_du_jour: GEO
piliers_breves: [Actualité SEO]
tags: [seo, ia, aeo, geo, revue-presse, citations-ia, reddit-chatgpt-perplexity]
sources_count: 8
confidence: high
status: draft
---

# Algorithme. 28 août 2026 v2

## À retenir

- Naqui Shaikh publie le 24 août sur Pierview.ai un jeu de données de 44 488 citations Reddit extraites de 50 000 prompts sur six moteurs de réponse IA, fenêtre du 1er juillet au 19 août 2026.
- Sur cet ensemble, ChatGPT réduit ses citations Reddit de 250 par jour début août à 16 par jour après le 14 août, Perplexity augmente ses citations Reddit d'environ 512 par jour début juillet à 988 par jour début août, Gemini reste à un niveau à peu près constant sur toute la fenêtre.
- Perplexity porte 71 % des 44 488 citations Reddit mesurées (31 640 citations), ChatGPT et Gemini se partagent le reste ; le fait divergent isole la cause au niveau retrieval de chaque moteur, pas au niveau du contenu Reddit lui-même.
- Une étude complémentaire par The Happy Cat, agence AI visibility à Manchester, publie le 20 août 30 réponses des trois assistants sur dix requêtes acheteur : 104 sources uniques citées, 11 sources reprises plus d'une fois, 3 entreprises recommandées par les trois moteurs.
- Microsoft Bing teste sur mobile le renommage de la boîte Copilot Search en « AI Overviews », spotté par Sachin Patel et relayé le 26 août par Barry Schwartz sur Search Engine Roundtable.

## Info du jour. Pilier GEO. Trois moteurs de réponse IA font trois choix différents sur Reddit sur la même fenêtre

Naqui Shaikh publie le 24 août 2026 sur [Pierview.ai](https://www.pierview.ai/guides/reddit-citations-chatgpt-perplexity-decline-2026) une analyse de 44 488 citations Reddit extraites d'un corpus de 50 000 prompts adressés à six moteurs de réponse IA entre le 1er juillet et le 19 août 2026. Cette publication étend, sur une fenêtre plus longue et un échantillon plus large, le premier signalement documenté le 19 août par [Promptwatch et repris sur Search Engine Land par Amanda Zantal-Wiener le 20 août](https://searchengineland.com/reddit-chatgpt-search-citations-fall-report-485473), qui portait sur la seule chute de la part de citations Reddit dans ChatGPT Search. La contribution neuve de Pierview.ai tient dans la ventilation par moteur de la même fenêtre temporelle.

La mesure sur ChatGPT reproduit et prolonge l'effet documenté par Promptwatch. Les citations Reddit passent d'une moyenne d'environ 250 citations par jour sur la fenêtre du 18 juillet au 7 août 2026 à environ 16 citations par jour sur la fenêtre du 14 au 17 août 2026, soit une baisse relative d'environ 94 % en six jours. La bascule intermédiaire est datée du 8 août par Promptwatch, avec la montée de l'opérateur `site:` dans les fan-out queries de ChatGPT Search de 0,37 % à 16,8 % de l'ensemble des fan-out en un jour, puis 23 à 24 % à mi-août. Un opérateur `site:` intégré à une fan-out interroge une seule adresse nommée au lieu d'un index général, ce qui exclut structurellement les plateformes de discussion à large surface éditoriale.

La mesure sur Perplexity va dans le sens opposé sur la même fenêtre. Les citations Reddit augmentent d'environ 512 par jour début juillet à environ 988 par jour début août. Perplexity porte 71 % des 44 488 citations Reddit du corpus, soit 31 640 citations, et maintient ce niveau après le 14 août alors que ChatGPT chute. Ce n'est donc pas une réponse partagée à un événement Reddit, c'est une divergence de configuration de retrieval entre deux moteurs sur la même période.

La mesure sur Gemini reste à un niveau à peu près constant sur toute la fenêtre du 1er juillet au 19 août. Gemini fonctionne ici comme variable de contrôle : la stabilité de son taux de citation Reddit isole la cause de la divergence au niveau du retrieval configuré par ChatGPT et Perplexity, pas au niveau du contenu Reddit ni d'une inaccessibilité côté serveur. C'est le point qui rend cette publication utile pour un consultant GEO : les hypothèses « Reddit dégrade son contenu », « Reddit change son robots.txt » ou « Reddit bloque un crawler » sont écartées par la constance sur Gemini.

Klaas Foppen, cofondateur de Promptwatch cité par Amanda Zantal-Wiener sur SEL, formule la limite avec précaution : l'ampleur de la chute mesurée reste provisoire, une déduplication ou un filtre pourrait expliquer une partie du delta, et Pierview.ai ne se prononce pas sur la date précise du basculement du 14 août. Ces zones d'ombre importent pour un consultant : la magnitude 94 % est bornée par la méthode de collecte de chaque outil de mesure, la magnitude 71 % de captation Perplexity est mesurée sur le corpus Pierview.ai et pas sur l'ensemble de l'écosystème.

Une étude complémentaire publiée le 20 août par The Happy Cat, agence AI visibility de Manchester fondée par Alex Golombeck, [reprise par Pressat](https://pressat.co.uk/releases/study-chatgpt-perplexity-gemini-cited-104-sources-in-30-answers-and-cant-agree-on-any-of-them-1e3f27038c139ff0cacef81fa3511f93/), documente le corollaire sur un échantillon plus petit. Sur 30 réponses des trois assistants (ChatGPT, Perplexity, Gemini) à dix requêtes acheteur identiques du type « best AI visibility agency UK », les trois moteurs citent 104 sources uniques, seulement 11 sources sont reprises plus d'une fois, et seulement trois entreprises sont recommandées par les trois moteurs à la fois. ChatGPT puise principalement dans les sites de marque avec leurs balises de tracking, Perplexity dans les articles de comparaison tiers, Gemini dans des articles éditoriaux substantiels. Le protocole est déclaratif et l'échantillon petit (30 réponses), donc à traiter comme illustration convergente, pas comme démonstration statistique.

Trois lectures opérationnelles pour un consultant GEO.

Un. La mesure globale du taux de citation d'un contenu ne suffit plus. Une marque, un produit ou un contenu peut avoir une part de citation en hausse dans Perplexity et une part en baisse dans ChatGPT sur la même semaine, sans qu'un signal éditorial ou technique explique l'écart. La [[concepts/metriques-visibilite-geo|couche de mesure GEO]] a besoin d'une dimension additionnelle : la ventilation par moteur, avec état daté du retrieval configuré chez chaque éditeur. Un tableau de suivi qui agrège les citations toutes plateformes confondues cache la divergence et donc rate la variable à ajuster.

Deux. La citation sur Reddit reste un vecteur mesurable via Perplexity pour l'instant, elle ne l'est plus via ChatGPT. Un contenu ancré sur un fil Reddit vérifié par la communauté conserve une chance élevée d'apparaître dans une réponse Perplexity et une chance très réduite d'apparaître dans une réponse ChatGPT sur la fenêtre observée. La [[concepts/tabou-visibilite|mesure de valeur d'un contenu par un taux de citation IA agrégé]] ne rend pas ce fait. Un consultant qui recommande à un client de miser sur Reddit doit préciser lequel des moteurs de réponse concerne l'objectif du client, et vérifier périodiquement la stabilité de cette configuration.

Trois. La configuration de retrieval d'un moteur de réponse IA est une variable indépendante des signaux éditoriaux classiques. Un fan-out qui utilise `site:` sur une adresse précise ne se contrôle pas depuis un site éditeur : rien dans les balises HTML, dans robots.txt, dans le schéma, dans le maillage interne d'un contenu ne change ce qu'un moteur de réponse choisit d'interroger. Cela conforte la lecture [[concepts/arbitrage-plateforme-publication|chaque plateforme éditoriale IA fait des choix distincts sur la même fenêtre]] et rend inopérante l'idée qu'un contenu unique peut être « optimisé » de la même manière pour tous les moteurs. La stratégie de citation IA devient une matrice contenu × moteur, pas un vecteur unique.

Trois réserves à poser franchement. Un, la fenêtre du 14 août reste sans cause publique identifiée par OpenAI : Promptwatch écrit qu'aucun changement documenté côté ChatGPT n'explique la bascule à cette date précise, une hypothèse d'artefact de collecte n'est pas écartée. Deux, aucune source publiée à ce jour ne mesure une éventuelle rétribution Perplexity vers Reddit (traffic, revenus, licence), la captation à 71 % est un fait de citation, pas de valeur retournée à la plateforme citée. Trois, la mesure Pierview.ai porte sur 50 000 prompts et 44 488 citations Reddit, ce qui reste un échantillon particulier ; une reproduction indépendante sur un panel plus large et différentes verticales est nécessaire pour graduer la portée du finding.

Trois prédictions binaires datées, critère binaire.

P-2026-08-28-v2-1 : d'ici le 30 novembre 2026, au moins un outil de mesure GEO grand public (Semrush AI Visibility Toolkit, Ahrefs Brand Radar, Otterly.ai, Peec) publiera une ventilation par moteur de réponse IA du taux de citation Reddit sur un panel d'au moins 500 domaines, restituant la divergence ChatGPT/Perplexity/Gemini. Confiance 0,55.

P-2026-08-28-v2-2 : d'ici le 30 juin 2027, ni OpenAI ni Perplexity ne publieront une explication officielle du changement de configuration de retrieval sur Reddit observable sur la fenêtre du 8 au 14 août 2026. Confiance 0,70.

P-2026-08-28-v2-3 : d'ici le 31 mars 2027, aucun contrat de licence public entre Perplexity et Reddit ne sera annoncé (Perplexity poursuit sa captation à 71 % sans accord formel). Confiance 0,55.

Lien avec la doctrine. Ce fait renforce [[concepts/metriques-visibilite-geo|la nécessité d'une mesure GEO ventilée par moteur]], précédemment articulée pour d'autres dimensions (persistance, nommage, référent scraper) et enrichie ici d'une dimension nouvelle : la configuration de retrieval côté moteur, indépendante du contenu et des signaux éditeur. Il rejoint [[concepts/tabou-visibilite|la limite du taux de citation IA agrégé]] comme métrique unique de performance GEO. Il illustre [[concepts/arbitrage-plateforme-publication|la divergence de choix de plateforme sur une même fenêtre]], appliquée cette fois à des moteurs conversationnels et non plus à des éditeurs de contenu. Il précise enfin [[concepts/agentic-search|le périmètre observable de la couche de réponse générative]] : les canaux d'attribution mesurables côté site ne suffisent pas à reconstituer les décisions internes de retrieval des moteurs.

## Brève. Pilier Actualité SEO. Microsoft Bing teste le renommage de Copilot Search en AI Overviews sur mobile

Sachin Patel a partagé sur X, autour du 25 août 2026, des captures d'écran de l'interface mobile de Bing où la boîte de réponse IA placée en haut des résultats de recherche porte l'étiquette « AI Overviews » au lieu de « Copilot Search ». Barry Schwartz reprend l'observation le 26 août sur [Search Engine Roundtable](https://www.seroundtable.com/bing-testing-copilot-search-ai-overviews-41953.html) (URL confirmée par le fil du recap quotidien du 27 août sur SE Roundtable, article original en accès restreint depuis certaines IP). Le logo Copilot reste affiché à côté de la nouvelle étiquette, seule la mention textuelle change.

Le fait est cadré par Schwartz comme un test A/B mobile, pas comme un déploiement général. Aucun communiqué Microsoft ne confirme ce changement à la date de rédaction, ni sur le blog Bing ni sur Microsoft Advertising Blog.

Trois lectures pour un consultant SEO ou GEO.

Un. Le naming des surfaces génératives converge sur le vocabulaire de Google. « AI Overviews » est le terme officiel Google depuis mai 2024, adopté par la CMA UK dans son opt-out toggle du 3 juin 2026, puis par le rapport Search Console Generative AI performance déployé sur Search en juin. Microsoft testant ce terme sur Bing indique une pression concurrentielle sur la vocabulaire, pas seulement sur la fonction. Le rapport Bing Webmaster Tools continue lui d'utiliser un vocabulaire distinct sur la partie « Copilot Search », un désalignement à surveiller.

Deux. Le suivi d'une visibilité IA multi-moteurs suppose une nomenclature stable dans les rapports Bing équivalents à Search Console pour Google. Si Bing renomme la surface mais ne renomme pas le rapport Webmaster Tools associé, un consultant qui mesure les impressions dans un compte Bing tiers doit vérifier que le rapport suit le nom actuel de la surface et pas le nom historique. Le risque de désalignement de comptage entre l'annonce produit et le rapport de mesure est réel, il a déjà été documenté pour la première extension de la GSC Generative AI performance report en juin.

Trois. Ce test isolé ne constitue pas une bascule stratégique de Microsoft vers l'écosystème Google, il indique plutôt une reconnaissance que le nom « AI Overviews » est devenu la catégorie de fait dans laquelle les utilisateurs classent une boîte de réponse IA en tête de résultats. Pour un consultant qui rédige un rapport client, le terme reste ambigu : préciser toujours le moteur d'origine (Google AI Overviews, Bing AI Overviews en test) et éviter d'utiliser « AI Overviews » sans qualifieur.

Une réserve importante : le test est actuellement mobile-only, aucune source publique ne confirme un déploiement desktop ou une extension à d'autres marchés que celui observé par Patel. Un consultant qui rédige aujourd'hui une note client sur cette évolution doit la présenter comme un signal de convergence lexicale sans engagement de déploiement.

Une prédiction binaire datée suit.

P-2026-08-28-v2-4 : d'ici le 31 décembre 2026, Microsoft publiera un billet officiel confirmant ou infirmant l'adoption du terme « AI Overviews » pour la boîte de réponse IA de Bing. Confiance 0,35.

Lien doctrine. Ce fait touche à [[concepts/metriques-visibilite-geo|la mesure d'une visibilité IA par moteur]] : si le vocabulaire converge côté interface publique mais reste distinct côté rapport de mesure, le consultant doit maintenir une matrice d'équivalences entre les termes affichés à l'utilisateur et les termes utilisés dans les outils d'observation. Il rejoint aussi [[concepts/arbitrage-plateforme-publication|la question du nommage des surfaces IA]] comme variable indépendante du fonctionnement technique de ces surfaces.

---

*Draft SyntheticBrain, 28 août 2026 v2. Aucun envoi. Ce fichier est une revue de presse produite par un agent auto-apprenant.*
