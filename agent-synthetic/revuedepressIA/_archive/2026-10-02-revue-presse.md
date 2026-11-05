---
date: 2026-10-02
pilier_info_du_jour: GEO / search IA
piliers_breves: [Business SEO, Niche SEO]
format: digest
version: v1
---

# Algorithme — Édition du 2 octobre 2026

**Points capitaux**

- Une expérience de terrain préenregistrée de l'University of Pennsylvania et de Northeastern University (N=1 100, publiée sur arXiv le 18 août 2026) mesure que l'exposition forcée à AI Mode réduit le taux de clic vers les sites tiers de 18,8 points de pourcentage, pendant que supprimer AI Overviews et AI Mode l'augmente de 8,8 points.
- Les sites les plus perdants dans la condition AI Mode sont les sites de presse, Reddit et Wikipédia, et les utilisateurs exposés à AI Mode se tournent davantage vers des moteurs concurrents, un effet second rare dans la littérature publique.
- Depuis le 31 août 2026, Google diffuse en direct des publicités Shopping sous forme de carrousel inline dans les réponses d'AI Mode, avec une éligibilité déterminée entièrement par le flux Merchant Center, sans texte publicitaire rédigé par l'annonceur.
- Nextdoor a lancé en septembre 2026 une rubrique Local Faves avec une recherche IA qui synthétise 15 ans de posts voisins pour classer les commerces locaux, un canal de découverte local hors Google Business Profile.
- Le fil directeur reste la montée des surfaces de réponse qui consomment des contenus sans renvoyer vers eux, aussi bien côté éditeur (AI Mode) que côté marchand (Shopping carousels dans AI Mode) ou côté local (Nextdoor Local Faves).

---

## Info du jour — GEO / search IA

### Une expérience préenregistrée mesure l'effet causal d'AI Mode sur le trafic éditeur, et le résultat change l'ampleur attendue

**Les faits.** Le 18 août 2026, trois chercheurs de l'University of Pennsylvania et de Northeastern University ont publié sur arXiv (identifiant 2608.18352v1) le papier « AI in Search Reduces Publisher Referrals Without Improving User Experience: Experimental Evidence » ([alphaxiv.org/abs/2608.18352v1](https://alphaxiv.org/abs/2608.18352v1)). Il s'agit d'un essai de terrain préenregistré avec 1 100 participants adultes basés aux États-Unis, utilisateurs réguliers de Google Chrome et de Google Search. Les participants ont été recrutés entre le 17 et le 19 mars 2026 et répartis au hasard dans trois conditions via une extension de navigateur dédiée : condition « No AI » qui masque AI Overviews et AI Mode, condition « Default » qui laisse l'expérience Google habituelle, condition « AI Mode » qui redirige toutes les requêtes vers AI Mode.

Les grandeurs mesurées sont publiées de manière directe par les sources tier 2 qui ont lu le papier. Dans la condition AI Mode forcé, le taux de clic externe vers des sites tiers baisse de **18,8 points de pourcentage** par rapport à la condition Default ([relevantaudience.com/geo/ai-mode-field-experiment-clicks-drop-18-8-points](https://www.relevantaudience.com/geo/ai-mode-field-experiment-clicks-drop-18-8-points/)). Dans la condition No AI, où AI Overviews et AI Mode sont masqués, le taux de clic externe augmente de **8,8 points** ([techwyse.com/news/search-seo/google-ai-mode-reduces-publisher-clicks-study-2026](https://www.techwyse.com/news/search-seo/google-ai-mode-reduces-publisher-clicks-study-2026)). Les trois catégories qui perdent le plus de clics dans la condition AI Mode sont les sites de presse, Reddit et Wikipédia. Les auteurs signalent aussi que les utilisateurs exposés à AI Mode « switch more often to competing search engines » (verbatim repris par Techwyse), un effet de second ordre qui déplace le débat au-delà du couple AIO/éditeurs.

Reprises indépendantes : [Scalevise](https://scalevise.com/resources/google-ai-mode-publisher-clicks-search-experiment/), [PPC Land](https://ppc.land/researchers-find-google-ai-overviews-cut-publisher-clicks-39-8/) et le blog [Pebblous](https://blog.pebblous.ai/blog/google-ai-mode-publisher-clicks-experiment/en/). Le papier Agarwal/Google Search AIO référencé par la Toulouse School of Economics ([tse-fr.eu/sites/default/files/TSE/documents/sem2026/eco_platforms/agarwal_google_search_aio.pdf](https://www.tse-fr.eu/sites/default/files/TSE/documents/sem2026/eco_platforms/agarwal_google_search_aio.pdf)) atteste de la circulation de l'étude dans les circuits académiques dédiés à l'économie des plateformes.

**Pilier.** Cette édition s'ancre sur **GEO / search IA**. Un essai de terrain préenregistré change le statut probatoire des chiffres sur l'impact d'AI Mode. Jusqu'ici, la plupart des mesures publiées (Pew juillet 2025 sur AIO, Seer juin 2025 sur CTR, Ahrefs mars 2025 sur CTR position 1) étaient observationnelles et sujettes aux objections classiques (sélection, confusion, saisonnalité). Un essai avec assignation aléatoire et préenregistrement établit un lien causal entre l'exposition à AI Mode et la baisse du clic externe. Le concept [[concepts/metriques-visibilite-geo]] formalise la visibilité dans la réponse générative à travers Imp_wc, Imp_pos, et impression subjective, mais ne contient pas aujourd'hui de métrique dédiée à ce que l'exposition à AI Mode retire au trafic. Le présent papier donne un point de référence quantifié pour cette métrique manquante.

**Lectures opérationnelles pour un consultant SEO/GEO.**

Premièrement, l'ordre de grandeur 18,8 points n'est pas directement comparable aux pourcentages déjà en circulation (58 % Ahrefs, 34 % Pew). Les études antérieures mesurent une baisse relative du CTR position 1 sur des requêtes qui déclenchent AIO. L'étude Penn/Northeastern mesure une baisse absolue du taux de clic externe dans une population redirigée systématiquement vers AI Mode, toutes requêtes confondues. L'écart entre les deux ne reflète pas un désaccord entre les chercheurs, il reflète deux définitions de la variable mesurée. Un consultant qui cite ces chiffres doit préciser laquelle il reprend.

Deuxièmement, l'effet de redirection vers des moteurs concurrents est documenté ici pour la première fois en condition expérimentale. Un éditeur dont la part de trafic vient majoritairement de Google doit anticiper que la perte de clic en provenance de Google ne se compense pas par un simple report sur un autre moteur côté éditeur, elle s'accompagne d'un déplacement du comportement utilisateur hors de Google. Pour les consultants qui travaillent sur la diversification du trafic vers Bing, DuckDuckGo ou des moteurs IA directs (Perplexity, You.com), la condition AI Mode offre un argument : la demande utilisateur se dirige vers ces alternatives sous exposition prolongée à AI Mode. L'ampleur reste à mesurer séparément.

Troisièmement, les trois catégories qui perdent le plus de clics (presse, Reddit, Wikipédia) sont également les sources structurelles les plus citées dans les réponses AI Mode selon la mesure Semrush de 126 millions de prompts analysés entre janvier et avril 2026, qui classe YouTube en première position des citations AIO (83,2 millions), Reddit en deuxième (35,8 millions) et Wikipédia en troisième (32,4 millions) ([businesswire.com/news/home/20260626995770/en/Semrush-Releases-Expanded-2026-AI-Visibility-Index-Analyzing-126-Million-AI-Search-Prompts](https://secure.businesswire.com/news/home/20260626995770/en/Semrush-Releases-Expanded-2026-AI-Visibility-Index-Analyzing-126-Million-AI-Search-Prompts)). Les plus cités sont les plus privés de clic. L'écart entre citation et clic, déjà formalisé par AirOps (85 % des pages récupérées par ChatGPT non citées, publié le 2 juin 2026 et déjà couvert à cette date), se double ici d'un écart entre citation et visite.

Quatrièmement, la condition No AI augmente les clics externes de 8,8 points, soit un ordre de grandeur moitié moins fort que la baisse associée à AI Mode. Ce n'est pas symétrique, et cela a une conséquence pratique pour un consultant qui raisonne sur l'opt-out éditeur. Même si un éditeur parvenait à faire sortir ses pages de l'inclusion dans AI Mode (ce que Google n'offre pas aujourd'hui comme contrôle granulaire sans sortir aussi de la recherche classique), le gain estimé par cette étude serait inférieur en valeur absolue à la perte subie quand le même utilisateur bascule en AI Mode. L'arbitrage opt-in/opt-out est asymétrique.

Cinquièmement, le papier signale une limite méthodologique importante : pendant la période d'étude (mars 2026), Google a modifié la structure HTML d'AI Overviews, ce qui a cassé la logique de masquage de l'extension. En conséquence, les AI Overviews ont été effectivement masqués dans seulement **51,1 %** des cas de la condition No AI, ce qui dilue l'effet mesuré pour cette condition et conduit à sous-estimer l'écart entre les trois conditions. Les 8,8 points mesurés en No AI sont donc un plancher, non un plafond. Les 18,8 points mesurés en AI Mode ne sont pas affectés par ce bug puisqu'il concernait la fonction de masquage, pas de redirection vers AI Mode.

**Réserves méthodologiques.** Le papier est à ce jour un préprint arXiv, pas une publication revue par les pairs. Le recrutement s'est fait sur 1 100 participants états-uniens, utilisateurs Chrome et Google Search exclusivement, ce qui exclut les utilisateurs mobiles sans Chrome et toute population hors États-Unis. La période d'exposition s'étend de la deuxième moitié de mars à l'été 2026, ce qui ne reflète pas les évolutions produit postérieures (introduction de Information Agents à large audience fin septembre 2026, Shopping carousels dans AI Mode fin août 2026). Les grandeurs peuvent avoir évolué depuis. Enfin, un essai contrôlé avec extension de navigateur mesure un comportement observé en situation d'enquête ; la généralisation au comportement spontané en situation naturelle demande une réplication. Aucun des trois chercheurs n'est affilié à Google, ce qui écarte un conflit d'intérêt direct, mais la base de données reste celle d'une population Chrome États-Unis uniquement.

**Lien doctrine.** L'étude articule deux pages du vault. [[concepts/metriques-visibilite-geo]] : les trois métriques existantes mesurent la visibilité dans la réponse générative, pas la perte de clic induite par cette visibilité. L'ordre de grandeur 18,8 points externe donne une référence quantifiée pour la variable manquante « perte de clic sous exposition AI Mode », à adjoindre comme quatrième métrique. [[concepts/boucle-sortie-mesure]] : la boucle sortie publication → mesure terrain repose sur la capacité à relier une publication à son effet réel. Un essai préenregistré est précisément ce dispositif, appliqué au niveau système (AI Mode vs non) plutôt qu'au niveau page. Pour un consultant, c'est un gabarit méthodologique importable à l'échelle d'un client : plutôt que de corréler le trafic avec la bascule AI Mode, assigner expérimentalement des pages A/B à un traitement SEO pour mesurer un effet causal au lieu d'une corrélation.

---

## Brève 1 — Business SEO

### Google diffuse des publicités Shopping en carrousel inline dans AI Mode, éligibilité pilotée uniquement par le flux Merchant Center

Le 31 août 2026, [Search Engine Roundtable](https://seroundtable.com/google-ai-mode-shopping-carousel-ads-41973.html) a documenté que Google diffuse en direct deux formats publicitaires Shopping à l'intérieur des réponses d'AI Mode : un carrousel inline au milieu de la réponse générative, et une unité unique en bas de la réponse. Reprise par [PPC Land](https://ppc.land/google-tests-two-shopping-ad-placements-inside-ai-mode-results/), [Common Thread Collective](https://commonthreadco.com/blogs/coachs-corner/google-ai-mode-now-shows-shopping-ads-inline-what-ecommerce-brands-must-do-right-now) et [Search Engine Watch](https://searchenginewatch.com/?p=146019). Le mécanisme d'éligibilité est documenté précisément : « AI Mode Shopping ads are generated entirely by Google's Gemini AI using your Merchant Center product feed » (verbatim Common Thread Collective à partir de la documentation Google). L'annonce n'est plus un texte publicitaire rédigé par l'annonceur, elle est reconstruite par Gemini à partir des attributs du flux Merchant Center (title, description, images, price, availability). Google détermine au moment de l'enchère si la requête est commerciale et quelle fiche produit insérer.

Pour un consultant Business SEO ou SEA, trois conséquences se dessinent. Un, l'avantage compétitif se déplace de la créativité du copywriting vers la qualité, la complétude et la cohérence du flux Merchant Center. Un flux pauvre en attributs (title court, description générique, images limitées, availability non actualisée) devient invisible dans AI Mode, indépendamment du budget alloué au compte Google Ads. Deux, l'éligibilité étant déterminée par Google et non par l'annonceur, la mécanique rejoint le fonctionnement du Google Shopping organique classique (Shopping tab, free listings), avec la différence que l'exposition se fait maintenant au milieu d'une réponse générative lue plus intégralement par l'utilisateur. Troisième conséquence, le placement adresse « more than 1 billion monthly AI Mode users worldwide » (verbatim Common Thread Collective à partir des chiffres Google), ce qui change l'ordre de grandeur du trafic conversionnel accessible via Merchant Center bien ajusté.

Les concepts du vault articulés sont [[concepts/data-proprietaire]] (le flux Merchant Center est une donnée propriétaire structurée dont la complétude conditionne la sélection par un moteur IA) et [[concepts/agentic-search]] (la couche de découverte produit déplace l'objet à optimiser de la page web vers le flux consommable par un agent). Réserve méthodologique : aucun chiffre indépendant n'a été publié à ce jour sur le CTR effectif ou le taux de conversion de ce format inline. Les métriques d'ampleur du trafic conversionnel resteront à documenter par les premiers rapports d'annonceurs post-septembre 2026.

---

## Brève 2 — Niche SEO

### Nextdoor lance Local Faves avec une recherche IA qui classe les commerces à partir de 15 ans de posts voisins

En septembre 2026, Nextdoor a déployé une rubrique Local Faves, un hub de découverte qui affiche les commerces locaux par catégorie classés selon la « neighbor trust » (confiance exprimée par les voisins dans les posts, mentions et recommandations). D'après [Destination CRM](https://www.destinationcrm.com/Articles/CRM-News/CRM-Across-the-Wire/Nextdoor-Adds-to-the-Essential-Neighborhood-Network-176455.aspx) et [GetCoAI](https://getcoai.com/news/nextdoors-biggest-redesign-adds-3-ai-features-for-100m-users/), la fonction est accompagnée d'une recherche IA qui « summarizes the most relevant insights from 15 years of real neighbor knowledge » (verbatim Destination CRM à partir de la documentation Nextdoor). La refonte produit introduit également des alertes locales IA et un système de recommandations personnalisées pour les 100 millions d'utilisateurs revendiqués par la plateforme ([Neowin](https://www.neowin.net/news/nextdoor-rolls-out-massive-redesign-with-ai-recommendations-and-emergency-alerts/)).

Pour un consultant Local SEO, trois lectures opérationnelles. Un, Local Faves introduit une couche de découverte locale distincte du Google Business Profile et du Local Pack. Le signal de classement n'est ni la complétude GBP ni l'avis Google, mais la densité et la cohérence des mentions dans les posts Nextdoor historiques, ce qui transforme une plateforme sociale locale en moteur de recommandation ranké. Deux, la recherche IA fondée sur 15 ans d'historique de posts favorise structurellement les commerces anciennement mentionnés par les voisins, ce qui désavantage les ouvertures récentes et les enseignes qui n'ont pas incité leurs clients à parler d'eux sur Nextdoor. Trois, la plateforme restant très marquée États-Unis, l'implication est forte pour les consultants qui travaillent des marchés US ou canadiens, et marginale pour les consultants français avant une éventuelle extension européenne.

La fonction s'articule au concept [[concepts/directories-data-ia]] : un annuaire ou une plateforme communautaire dont le contenu alimente directement un moteur de recommandation IA devient une surface d'optimisation à part entière, distincte des annuaires passifs d'ancrage sémantique. Réserve méthodologique : les chiffres publiés par Nextdoor sur « neighbor trust » comme critère de classement proviennent du communiqué produit ; aucune mesure indépendante du ranking ou de l'effet sur la fréquentation des commerces inclus dans Local Faves n'est disponible à ce jour.

---

## Trois prédictions datées

- **P-2026-10-02-1** (0,50, échéance 2027-03-31) — Le papier arXiv 2608.18352v1 fera l'objet d'une tentative de réplication publique, soit par un troisième laboratoire académique, soit par un cabinet indépendant disposant d'un panel comparable, avec publication des résultats avant le 31 mars 2027. Résout par parution d'un rapport nommément identifié reprenant la méthode préenregistrée.
- **P-2026-10-02-2** (0,55, échéance 2026-12-31) — Au moins un rapport public d'annonceur ou d'agence SEA documentera un ratio CTR ou coût par acquisition sur les Shopping carousels AI Mode distinct des performances Shopping classiques, publié avant fin 2026. Résout par parution d'un billet signé, pas d'un livre blanc vendeur.
- **P-2026-10-02-3** (0,30, échéance 2027-06-30) — Nextdoor Local Faves sera étendu hors des États-Unis à au moins un marché européen (France, Royaume-Uni ou Allemagne) avant le 30 juin 2027. Résout par annonce officielle sur nextdoor.com ou presse spécialisée local search tier 1.

---

## Sources utilisées dans cette édition

### Info du jour
- [alphaxiv.org/abs/2608.18352v1](https://alphaxiv.org/abs/2608.18352v1) — préprint arXiv primaire, soumis 18 août 2026, 1 100 participants, Penn + Northeastern.
- [techwyse.com/news/search-seo/google-ai-mode-reduces-publisher-clicks-study-2026](https://www.techwyse.com/news/search-seo/google-ai-mode-reduces-publisher-clicks-study-2026) — reprise tier 2 avec grandeurs clés.
- [relevantaudience.com/geo/ai-mode-field-experiment-clicks-drop-18-8-points](https://www.relevantaudience.com/geo/ai-mode-field-experiment-clicks-drop-18-8-points/) — reprise tier 2, chiffre 18,8 points explicite.
- [scalevise.com/resources/google-ai-mode-publisher-clicks-search-experiment](https://scalevise.com/resources/google-ai-mode-publisher-clicks-search-experiment/) — reprise tier 2.
- [blog.pebblous.ai/blog/google-ai-mode-publisher-clicks-experiment/en](https://blog.pebblous.ai/blog/google-ai-mode-publisher-clicks-experiment/en/) — reprise tier 2.
- [ppc.land/researchers-find-google-ai-overviews-cut-publisher-clicks-39-8](https://ppc.land/researchers-find-google-ai-overviews-cut-publisher-clicks-39-8/) — reprise tier 2.
- [tse-fr.eu/sites/default/files/TSE/documents/sem2026/eco_platforms/agarwal_google_search_aio.pdf](https://www.tse-fr.eu/sites/default/files/TSE/documents/sem2026/eco_platforms/agarwal_google_search_aio.pdf) — circulation académique.
- [secure.businesswire.com/news/home/20260626995770/en/Semrush-Releases-Expanded-2026-AI-Visibility-Index-Analyzing-126-Million-AI-Search-Prompts](https://secure.businesswire.com/news/home/20260626995770/en/Semrush-Releases-Expanded-2026-AI-Visibility-Index-Analyzing-126-Million-AI-Search-Prompts) — chiffres citation AIO contextualisants.

### Brève 1 — Shopping Ads AI Mode
- [seroundtable.com/google-ai-mode-shopping-carousel-ads-41973.html](https://seroundtable.com/google-ai-mode-shopping-carousel-ads-41973.html) — tier 2 référence.
- [ppc.land/google-tests-two-shopping-ad-placements-inside-ai-mode-results](https://ppc.land/google-tests-two-shopping-ad-placements-inside-ai-mode-results/) — tier 2 observation deux placements.
- [commonthreadco.com/blogs/coachs-corner/google-ai-mode-now-shows-shopping-ads-inline-what-ecommerce-brands-must-do-right-now](https://commonthreadco.com/blogs/coachs-corner/google-ai-mode-now-shows-shopping-ads-inline-what-ecommerce-brands-must-do-right-now) — tier 2 synthèse mécanique éligibilité.
- [searchenginewatch.com/?p=146019](https://searchenginewatch.com/?p=146019) — tier 2 reprise.

### Brève 2 — Nextdoor Local Faves
- [destinationcrm.com/Articles/CRM-News/CRM-Across-the-Wire/Nextdoor-Adds-to-the-Essential-Neighborhood-Network-176455.aspx](https://www.destinationcrm.com/Articles/CRM-News/CRM-Across-the-Wire/Nextdoor-Adds-to-the-Essential-Neighborhood-Network-176455.aspx) — tier 2.
- [getcoai.com/news/nextdoors-biggest-redesign-adds-3-ai-features-for-100m-users](https://getcoai.com/news/nextdoors-biggest-redesign-adds-3-ai-features-for-100m-users/) — tier 2.
- [neowin.net/news/nextdoor-rolls-out-massive-redesign-with-ai-recommendations-and-emergency-alerts](https://www.neowin.net/news/nextdoor-rolls-out-massive-redesign-with-ai-recommendations-and-emergency-alerts/) — tier 2.

---

*Édition SyntheticBrain du 2 octobre 2026, pilier info du jour GEO / search IA, brèves Business SEO et Niche SEO. 76e édition consécutive au format 1 info du jour + 2 brèves. Rédigée dans la voix propre de SyntheticBrain (vouvoiement, analyste search/IA, sans emprunt de voix de Tim). Rien n'a été envoyé.*
