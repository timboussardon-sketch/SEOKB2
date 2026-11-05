---
title: "Google ouvre un portail de dépôt pour les apps à faire apparaître dans Search et Gemini"
date: 2026-10-29
pilier_info_jour: agentic-search
breves_piliers: [actualite-seo, niche-seo, business-seo]
sources_count: 7
status: draft
---

# Google ouvre un portail de dépôt pour les apps à faire apparaître dans Search et Gemini

## Résumé

- Google a mis en préversion le 28 octobre 2026 un Connected Apps Platform qui transforme l'intégration d'apps tierces dans Gemini et Search en une procédure publique via un Connected Console.
- Les développeurs branchent un serveur MCP distant ou un MCP Android avec les AppFunctions APIs, enregistrent l'app, choisissent la cible (Search, Gemini ou les deux), passent une revue, et suivent trafic, latence et erreurs.
- Plus de cinquante apps sont déjà en ligne dans Gemini, dont Adobe, Experian, Localiza et Peloton, et doivent apparaître dans Search dans les prochaines semaines ; Calm démarre sur les deux surfaces.
- La politique de sélection, de routage entre apps concurrentes et de mesure côté annonceur reste non documentée dans la préversion.
- Trois brèves ferment l'édition : extension des publicités AI Mode à dix pays et format multiturn aux États-Unis, contrôles de retrait des agrégateurs de commande dans Google Business Profile, résultats trimestriels Google et Microsoft avec Search Ads en croissance à deux chiffres.

## Info du jour — Agentic Search

Pilier : [[concepts/agentic-search]].

Chips Mistry, Group Product Manager Search, et Mai Lowe, Group Product Manager de l'app Gemini, ont publié sur le blog officiel Google, le 28 octobre 2026, la préversion du Connected Apps Platform. Google décrit la préversion comme « a unified way for more app developers to bring their capabilities directly into Gemini and Search », avec la promesse pour les développeurs de « build once and reach high-intent users across both Search and the Gemini app » ([New Connected Apps Platform launches for developers](https://blog.google/innovation-and-ai/technology/developers-tools/connected-apps-one-place/)).

La procédure publiée est précise. Le développeur intègre son app via un serveur MCP distant (Model Context Protocol, protocole ouvert) ou via l'Android MCP qui s'appuie sur les AppFunctions APIs. Il passe ensuite par le Google Connected Console pour enregistrer, tester, soumettre, et choisir, avant revue, si l'app apparaîtra dans Search, dans l'app Gemini, ou dans les deux. Après mise en ligne, la console remonte le trafic, la latence et les taux d'erreur, et contient les contrôles de marque, dont les logos vérifiés et les comptes authentifiés ([developers.google.com/connected-apps](https://developers.google.com/connected-apps)). Pour les apps Android qui s'exécutent en local sur l'appareil, le chemin passe par le SDK Jetpack AppFunctions, l'autorisation côté utilisateur se fait en OAuth 2.1 côté serveur distant, et le serveur MCP distant doit utiliser le transport Streamable HTTP et un certificat TLS d'une autorité publique ([documentation développeur Connected Apps](https://developers.google.com/connected-apps)).

Côté partenaires, Adobe, Experian, Localiza et Peloton sont déjà actifs dans Gemini et doivent atteindre Search « in the coming weeks ». Calm démarre sur les deux surfaces. Google indique avoir dépassé cinquante Connected Apps à travers Search et Gemini, dans des verticales présentées comme la productivité, la billetterie d'événements, la santé et le fitness ([Google : New Connected Apps Platform launches for developers](https://blog.google/innovation-and-ai/technology/developers-tools/connected-apps-one-place/)). Le site Search Engine Roundtable confirme la préversion, cite John Mueller qui dit ne pas travailler sur le programme et précise que les apps n'apparaissent pas automatiquement pour un utilisateur : il faut qu'il les ajoute dans ses paramètres de Search ([Developers Can Now Build Apps For Google Search In The Connected Apps Platform](https://www.seroundtable.com/google-connected-apps-platform-42408.html)). L'analyse publiée par PPC Land apporte un recoupement complémentaire : la console transforme ce qui ressemblait à un programme par partenariat en une procédure de dépôt proche d'une candidature, Google gardant la décision finale au stade de la revue ([Google opens preview for third-party apps inside Search and Gemini](https://ppc.land/google-opens-preview-for-third-party-apps-inside-search-and-gemini/)). Le média 9to5Google ajoute que l'accès est ouvert par phases, sans publication de calendrier pays par pays ([Google adding more Connected Apps to Gemini & Search with new dev platform](https://9to5google.com/2026/10/28/gemini-google-connected-apps-platform/)).

Ce qui est franchement neuf par rapport au déploiement grand public du 16 juillet 2026 (Instacart, Canva, YouTube Music, États-Unis, anglais, procédure et protocole alors non publiés) tient en quatre points. Un, la procédure d'intégration est désormais publique et self-service via Connected Console. Deux, le protocole technique est documenté : MCP distant avec Streamable HTTP et TLS public, ou Android MCP avec Jetpack AppFunctions. Trois, le périmètre cible désormais explicitement Search et Gemini en même temps, pas seulement AI Mode dans Search. Quatre, le nombre d'apps référencées passe d'une poignée à plus de cinquante, avec un pipeline de nouveaux partenaires annoncé.

Trois réserves à garder visibles pour un consultant SEO qui lit l'annonce.

Première réserve : la logique de sélection entre apps n'est pas documentée. Si deux apps couvrent la même intention (prendre un rendez-vous santé, réserver une classe de fitness), Google ne précise pas, dans l'annonce du 28 octobre, quel critère active l'une plutôt que l'autre. L'analyste de PPC Land note que ce routage pourrait jouer un rôle proche d'un ranking, mais que l'annonce ne décrit pas ses signaux ([Google opens preview for third-party apps inside Search and Gemini](https://ppc.land/google-opens-preview-for-third-party-apps-inside-search-and-gemini/)). Deuxième réserve : la mesure côté annonceur ne mentionne pas, à ce stade, de pont vers Google Ads, Google Analytics ou vers une attribution de conversion ; les métriques publiées (trafic, latence, erreurs) sont opérationnelles. Troisième réserve : l'utilisateur doit activement ajouter l'app dans ses paramètres Search avant qu'elle ne soit mobilisable, ce qui déplace le travail d'acquisition sur la notoriété de l'app et sur les signaux hors moteur, pas sur un signal « SEO classique » côté URL.

Rattachement à la doctrine. L'arrivée d'une procédure de dépôt publique rend opérationnelle la bascule décrite dans [[concepts/agentic-search]], où « être sélectionné par l'agent pour accomplir une tâche » remplace l'affichage dans une liste de liens. Elle renforce la grille [[concepts/know-simple-know-do]] : les Connected Apps sont des surfaces « Do », pas des pages « Know », et basculent la question de la discoverability vers une inscription à un registre adossé à des APIs. Elle active aussi [[concepts/arbitrage-plateforme-publication]] appliqué non plus à un format de contenu (vidéo, Reddit, Substack, site), mais à un format d'interaction (app connectée vs page web vs vidéo) : si Google Search envoie une partie des intentions « Do » vers des Connected Apps enregistrées, la décision de proposer une app devient un arbitrage de plateforme et non un sous-produit du site existant.

Pour un consultant SEO, trois questions concrètes se posent après le 28 octobre. La marque dispose-t-elle d'une app pertinente, ou doit-elle en financer la construction pour couvrir une intention « Do » que son site ne couvre pas aujourd'hui ? Les équipes produit sont-elles outillées pour servir un MCP distant avec Streamable HTTP et TLS public ou un MCP Android via Jetpack AppFunctions ? La marque a-t-elle les moyens d'inciter l'utilisateur à ajouter l'app dans ses paramètres Search, étape qui conditionne la visibilité réelle ? Ces questions sont actionnables sans attendre la liste publique des critères de routage, qui pourrait rester opaque pendant la préversion.

Prédictions ouvertes à surveiller.

- P-2026-10-29-1 : Google publie, avant le 30 juin 2027, une documentation publique des critères de sélection entre Connected Apps concurrentes sur une même intention (confidence 0,30).
- P-2026-10-29-2 : au moins un éditeur SEO majeur (Ahrefs, Semrush, Sistrix, Moz) publie, avant le 31 mars 2027, une analyse mesurant l'impact des Connected Apps sur le CTR des URL dans AI Mode (confidence 0,45).
- P-2026-10-29-3 : la préversion du Connected Apps Platform reste en préversion limitée au-delà du 30 avril 2027, sans release GA annoncée (confidence 0,55).

## Brèves

### Brève 1 — Actualité SEO : Google étend les publicités AI Mode à dix pays et lance les ads multiturn aux États-Unis

Google a annoncé, le 28 octobre 2026, l'extension des publicités dans AI Mode à l'Australie, le Canada, l'Inde, le Kenya, la Malaisie, la Nouvelle-Zélande, le Nigéria, le Pakistan, les Philippines et Singapour, avec le Brésil, le Mexique et le Royaume-Uni programmés pour T4. En parallèle, Google lance aux États-Unis un format multiturn qui expose des annonces en réponse aux requêtes de suivi dans la même conversation AI Mode. Google précise, selon la citation reprise par Search Engine Roundtable, « Multiturn ads show up on responses to follow-up user queries as users engage in back and forth conversations with AI Mode », et « Ads will be clearly labeled as 'Sponsored' » ([Google Expands Ads In AI Mode To More Countries & Multiturn Ads In U.S.](https://www.seroundtable.com/google-expands-ads-ai-mode-42412.html)). Google ajoute avoir mesuré « click-through rates are already similar between sponsored and organic product list items within AI Mode », une revendication que Barry Schwartz nuance, en notant que la comparaison est faite sur des product listings visuels, pas sur des liens texte ([Google Expands Ads In AI Mode To More Countries & Multiturn Ads In U.S.](https://www.seroundtable.com/google-expands-ads-ai-mode-42412.html)). Le billet officiel se trouve ici : [Ads in AI Mode: global expansion and multiturn](https://blog.google/products/ads-commerce/ads-in-ai-mode-global/).

Rattachement doctrine : [[concepts/arbitrage-plateforme-publication]] prolongé par la question frontière organique/payant dans la réponse générative ; [[concepts/tabou-visibilite]] appelle à prendre le CTR mesuré par Google avec distance, puisque la mesure n'est pas restituée méthode comprise.

### Brève 2 — Niche SEO : Google Business Profile ajoute un contrôle fin des agrégateurs de commande

Lisa Landsman, pour Google, a publié le 28 octobre 2026 un billet LinkedIn relayé par Search Engine Roundtable. Les restaurants peuvent désormais désactiver chaque agrégateur de commande (Uber Eats, DoorDash, Instacart, Grubhub, et d'autres) depuis leur tableau de bord Google Business Profile, partiellement ou totalement, sans passer par un contact direct avec chaque plateforme. Landsman rapporte que ce contrôle fait partie des demandes les plus fréquentes d'opérateurs restaurants ([Google Business Profiles Finally Adds Third-Party Ordering Controls](https://www.seroundtable.com/google-business-profiles-ordering-controls-42411.html)). L'annonce ne précise ni le périmètre géographique ni la date exacte de disponibilité par marché. Les restaurateurs ont intérêt à auditer leurs liens de commande, puisque chaque agrégateur active peut router les commandes vers un menu obsolète ou un périmètre de livraison incorrect.

Rattachement doctrine : la fiche [[entities/gsc]] et plus largement l'écosystème Google Business Profile touchent le canal découverte local, où la gouvernance d'agrégateurs tiers reste un angle mort de la littérature SEO.

### Brève 3 — Business SEO : Search Ads +10,5 % chez Google, Bing Ads +12 % chez Microsoft au trimestre

Google a publié ses résultats Q3 2026 le 28 octobre 2026. Les revenus publicitaires Search ont progressé de 10,5 % à 82 milliards de dollars, et le chiffre d'affaires total est en hausse de 25 % à 127,6 milliards de dollars ([Google Ad Revenue Up 10.5% With Overall Revenue Up 25%](https://www.seroundtable.com/google-earnings-q326-42403.html)). Le même jour, Microsoft a publié ses résultats du trimestre Q1 fiscal 2027. Les revenus Search and News Advertising sont en hausse de 12 %, et le chiffre d'affaires total de 19 % ([Bing Ads Revenue Up 12% With Overall Revenue Up 19%](https://www.seroundtable.com/microsoft-earnings-q127-42404.html)). Ces deux publications fournissent une mesure comparable un même jour, utile pour calibrer le poids relatif des deux moteurs sur l'investissement publicitaire ; elles ne disent rien, à ce stade, de la part des revenus payants qui proviennent spécifiquement d'AI Mode côté Google ou de Copilot côté Microsoft, ce qui limite l'interprétation côté acquisition organique.

Rattachement doctrine : [[concepts/metriques-visibilite-geo]] appelle à distinguer la mesure d'exposition dans l'interface IA d'une mesure strictement financière ; les deux publications trimestrielles ne restituent pas la décomposition par surface IA, ce qui laisse l'écart organique vs payant dans AI Mode non quantifié publiquement.

## Notes de couverture

- Sources primaires : Google (blog.google), Google Developers (developers.google.com/connected-apps).
- Sources secondaires indépendantes : Search Engine Roundtable (Barry Schwartz), 9to5Google (Abner Li), PPC Land (Luís Rijo).
- Dates vérifiées : 28 octobre 2026 pour l'ensemble des annonces reprises.
- Clarification anti-redite : le présent run traite la préversion développeur du Connected Apps Platform (28 octobre 2026), à distinguer du déploiement grand public du 16 juillet 2026 (Instacart, Canva, YouTube Music, États-Unis), traité dans l'édition 2026-07-17.
