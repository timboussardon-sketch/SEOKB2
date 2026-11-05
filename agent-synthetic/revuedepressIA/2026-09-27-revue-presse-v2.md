---
title: "Search Console applique un aplatissement de bloc aux AI Overviews : tous les liens du bloc partagent la même position, ce que ça change dans la lecture d'un rapport GSC"
date: 2026-09-27
pilier_info_du_jour: GEO / search IA
piliers_breves: [Niche SEO, Business SEO]
edition: 68
---

# Search Console applique un aplatissement de bloc aux AI Overviews : tous les liens du bloc partagent la même position, ce que ça change dans la lecture d'un rapport GSC

*Édition Algorithme — 27 septembre 2026 (v2, soir) — SyntheticBrain*

- John Mueller confirme sur Reddit entre le 10 et le 13 septembre 2026 que Google Search Console traite chaque AI Overview comme un bloc unique : tous les liens à l'intérieur héritent de la position du bloc, indépendamment de leur emplacement réel dans la réponse ([Antonio Fernandez, Relevant Audience, 13 sept](https://www.relevantaudience.com/seo/mueller-search-console-ai-overview-position-counted-as-block/) et [Dan Taylor, Search Engine Journal, 24 sept](https://www.searchenginejournal.com/search-console-uses-block-flattening-for-aios-forget-position-focus-on-outcomes/589582/)).
- Conséquence directe : une page citée en position 1 dans un AI Overview et en position 19 dans les résultats organiques classiques ressort à une position moyenne de 10 dans le rapport GSC, ce qui masque l'écart réel de visibilité.
- La distinction entre lien affiché sous la première phrase de la réponse IA et lien caché derrière un « Show more » disparaît côté rapport : les deux sont enregistrés à la même position.
- Barry Schwartz documente le 17 septembre 2026 que Google convertit certains local knowledge panels en AI Overview avec un bouton « Show more » qui ouvre une conversation AI Mode, changement observé par Ben Fisher sur LinkedIn puis reproduit sur RustyBrick ([Search Engine Roundtable](https://www.seroundtable.com/google-local-knowledge-panel-ai-overview-42105.html) et [recap 17 sept](https://www.seroundtable.com/recap-09-17-2026-42108.html)).
- Tom Jackson, CTO de News UK, déclare le 10 septembre 2026 à la Future of Media Technology Conference que 20 pourcent du trafic des sites du groupe sur six mois est non humain et 6 pourcent bloqué activement, données rapportées par Charlotte Tobitt le 23 septembre ([Press Gazette](https://pressgazette.co.uk/publishers/digital-journalism/fifth-of-news-uk-website-traffic-was-non-human-in-past-six-months/)).

## Info du jour — GEO / search IA — L'aplatissement de bloc dans Search Console, la mécanique exacte que confirme John Mueller, et ce que ça retire à une lecture GEO du rapport AI Overviews

John Mueller a confirmé entre le 10 et le 13 septembre 2026, en répondant sur Reddit à un fil qui résumait les règles de comptage des AI Overviews dans Search Console, que le résumé du contributeur était exact. Antonio Fernandez, Relevant Audience, publie l'analyse le 13 septembre ([Relevant Audience](https://www.relevantaudience.com/seo/mueller-search-console-ai-overview-position-counted-as-block/)). Dan Taylor, dans un article publié le 24 septembre sur Search Engine Journal, reprend la mécanique et la nomme « block flattening » ([Search Engine Journal](https://www.searchenginejournal.com/search-console-uses-block-flattening-for-aios-forget-position-focus-on-outcomes/589582/)).

La règle, telle que la formule l'article SEJ, est la suivante : « Instead of checking where an individual link sits inside an AI summary, Google just looks at the overview box as a whole and gives it one overall rank. » Mueller précise pour sa part que la mesure de position à l'intérieur d'une surface IA est « hard to do in a way that makes it useful », et que la logique héritée du « position 1 - 10 » sur les liens bleus est « hard to map or make useful for site owners » sur ces nouvelles surfaces.

Quatre points techniques précis découlent de la règle.

Un, chaque AI Overview occupe une position dans les résultats servis, et Google attribue cette position uniformément à chaque lien cité dans le bloc. Une page qui apparaît deux fois dans le même bloc (une fois en carte de citation prominente sous la première phrase, une fois en lien caché derrière un « Show more ») compte pour une seule occurrence à la position du bloc. La différenciation d'exposition, réelle côté utilisateur, disparaît côté rapport.

Deux, l'impression est comptée dès l'apparition du bloc AI Overview sur la page de résultats servie, que l'utilisateur ait scrollé jusqu'au lien ou non. Les liens placés derrière une expansion « Show more » ne sont pas comptés tant que l'utilisateur n'a pas déplié le bloc, ce qui introduit une asymétrie mesurable entre les liens toujours visibles et les liens cachés par défaut.

Trois, le rapport « Generative AI » de Search Console est une vue filtrée du rapport Web, pas un rapport indépendant. Additionner les impressions du rapport IA aux impressions Web totales revient à double-compter les impressions du bloc AI Overview quand il apparaît sur la même page de résultats servie que les liens bleus organiques.

Quatre, la métrique « Average Position » dans le rapport IA est un artefact de moyenne à partir de deux mesures très différentes. L'exemple que donne Dan Taylor illustre le biais : une page qui figure en position 1 dans un AI Overview et en position 19 dans les résultats organiques classiques ressort à une position moyenne de 10 dans le rapport, ce qui suggère un classement médian là où la réalité est deux extrêmes.

La conséquence pour un consultant GEO ou SEO qui appuie une recommandation client sur un rapport Search Console est directe, et elle demande de reformuler l'usage du rapport.

Un, la position moyenne n'est pas un indicateur de placement dans une réponse IA. Le rapport confirme la présence, il ne confirme ni la prominence ni l'ordre de citation. Une page à « position 1 » dans le rapport IA peut être un lien caché sous un « Show more » qu'aucun utilisateur n'a déplié, ou une carte de citation en tête de bloc, sans que la donnée le distingue.

Deux, la mesure fidèle de la valeur d'une citation IA ne passe pas par Search Console. Elle passe par la mesure du signal aval : visites réelles depuis le référant AI Overview, engagement, conversion, ou par un outil GEO tiers qui reconstruit une part de citation en interrogeant l'AI Overview lui-même. Dan Taylor écrit : « prioritize actual visits and conversions », et cette recommandation n'est pas cosmétique. C'est le seul contournement disponible tant que Google ne publie pas une métrique de citation intérieure au bloc.

Trois, la comparaison inter-périodes de la position moyenne dans le rapport IA peut refléter davantage la composition du mix (AI Overview seul, AI Overview plus organique, AI Overview plus autre feature SERP) que la vraie évolution de la visibilité de la page. Une hausse de la position moyenne peut être un artefact de bascule de mix, une baisse peut cacher un renforcement de la présence sur les blocs IA sans corrélat clic.

Quatre, la métrique de CTR dans le rapport IA est à lire avec la même prudence. Une étude Seer Interactive reprise par plusieurs éditeurs sur 2026 rapporte une chute de 61 pourcent du CTR sur les requêtes AI Overview et un recul d'environ 38 pourcent des clics organiques quand un AI Overview est présent. Le rapport IA de Search Console ne distingue pas la nature du clic (lien de citation IA vs lien organique cité aussi), ce qui rend l'agrégation par requête peu discriminante pour un diagnostic.

Cinq, la donnée de position dans le rapport reste un signal binaire utile : est-ce que la page est présente dans un bloc AI Overview pour cette requête, oui ou non. C'est un signal de couverture, pas un signal de placement. Un tableau de bord GEO client peut le conserver comme indicateur « éligibilité citation IA » sans chercher à en tirer un rang au sens historique.

Trois concepts doctrine s'articulent. [[concepts/metriques-visibilite-geo]] gagne une contrainte de mesure explicite : la position dans une réponse IA n'est pas mesurable depuis Search Console, et un pipeline de mesure GEO qui s'appuierait sur la métrique « Average Position » du rapport IA construit une lecture biaisée du placement. La fiche doit intégrer que Search Console mesure la présence, un outil GEO tiers mesure le placement, et le clic aval mesure la valeur. [[concepts/structural-information-geo]] rappelle qu'une citation dans un moteur IA est fonction d'une chaîne d'appels et d'un rendu, pas d'un attribut de page ; la règle d'aplatissement confirme que la mesure côté propriétaire est structurellement en retard sur ce que le moteur produit côté utilisateur. [[concepts/agentic-search]] hérite d'une conséquence : quand un moteur IA remplace une liste ordonnée par une réponse synthétisée avec liens, la notion héritée de « classement » disparaît côté rapport propriétaire ; l'utilisateur voit une hiérarchie, le propriétaire voit une position unique.

Cinq réserves méthodologiques.

Un, John Mueller s'exprime sur Reddit, pas dans une publication officielle Google Search Central. La formulation exacte est un « pretty much it » validant le résumé d'un contributeur, complété par des commentaires additionnels. La règle est donc confirmée par Google mais pas documentée dans les pages officielles Search Central au moment de l'édition. La documentation Search Console Help sur les impressions, la position et les clics reste antérieure à cette précision.

Deux, la formule exacte de calcul de la position moyenne dans le rapport Generative AI (moyenne arithmétique, pondérée par les impressions, comportement en cas d'occurrences multiples de la même page sur la même requête) n'est pas publiée par Google. Le raisonnement de Dan Taylor sur l'exemple 1 et 19 qui donne 10 suppose une moyenne arithmétique simple ; cette hypothèse n'est pas vérifiée par la documentation Google.

Trois, l'article Search Engine Journal donne l'exemple d'un CTR AI Overview en chute de 61 pourcent et d'un CTR organique en recul d'environ 38 pourcent quand un AIO est présent, en s'appuyant sur des mesures Seer Interactive. Le périmètre exact de cette mesure (échantillon de requêtes, période, verticales) n'est pas repris ici, et un consultant qui reprendrait ces chiffres devrait remonter à l'étude source avant de les intégrer à un livrable client.

Quatre, la règle d'aplatissement décrite s'applique au rapport « Generative AI » de Search Console, qui filtre les données Web. La règle ne s'applique pas au rapport Web classique où la position d'un lien bleu organique reste calculée sur les positions individuelles. Un tableau de bord qui compare position IA et position Web sur la même page doit tenir compte de cet écart de méthodologie.

Cinq, la règle ne préjuge pas de la valeur commerciale de la citation. Un lien à la position du bloc peut recevoir un volume de clic très différent selon qu'il est carte de citation visible ou lien caché sous « Show more », et cette valeur commerciale n'apparaît que dans les données aval de trafic et de conversion, jamais dans Search Console.

Trois prédictions vérifiables datées.

- P-2026-09-27-v2-1 : d'ici le 31 mars 2027, Google Search Central publie une page de documentation officielle décrivant explicitement le comportement d'aplatissement de bloc dans le rapport Generative AI (confiance 0,45).
- P-2026-09-27-v2-2 : d'ici le 31 décembre 2026, au moins un outil GEO tiers (Peec AI, Otterly, Profound, Athena HQ, Semrush, Ahrefs) publie une étude comparant la position déclarée par Search Console dans un AIO et le placement intérieur au bloc mesuré par ses propres crawls, sur au moins 1 000 requêtes (confiance 0,55).
- P-2026-09-27-v2-3 : d'ici le 30 juin 2027, la métrique « Average Position » du rapport Generative AI de Search Console reste calculée sur la position du bloc et non sur le placement intérieur (confiance 0,80).

## Brève 1 — Niche SEO — Google convertit des local knowledge panels en AI Overviews avec un bouton « Show more » qui ouvre AI Mode : ce que ça retire à une fiche Google Business Profile bien renseignée

Barry Schwartz publie le 17 septembre 2026 sur Search Engine Roundtable la reproduction d'un comportement d'abord signalé par Ben Fisher sur LinkedIn : sur certaines requêtes de marque locale, Google remplace l'affichage habituel du local knowledge panel (horaires, téléphone, photos, épingle sur la carte) par un label « AI Overview » et un bouton « Show more » qui ouvre une interface conversationnelle AI Mode ([Search Engine Roundtable](https://www.seroundtable.com/google-local-knowledge-panel-ai-overview-42105.html)). Schwartz reproduit le rendu sur sa propre entreprise RustyBrick et note que la description générée mentionne « niche solutions » à partir de contenu ancien de son site corporate, sans que la fiche Business Profile elle-même ait servi de source unique.

La citation directe de Schwartz dans l'article : « Google is turning the local knowledge panels, your Google Business Profile, into an AI Overview listing. » Son évaluation personnelle : « I am honestly not a fan of this, but I know Google is AIing every experience, so I am not surprised. » Il ajoute que Google teste des variations de ce type depuis début 2025, sans publication officielle Search Central sur le comportement observé le 17 septembre 2026.

Ce que ça change pour une prestation Niche SEO ou local SEO qui repose sur une fiche Business Profile bien remplie. La fiche Business Profile n'est plus la source unique de ce que voit l'internaute en recherche de marque. Le modèle qui rédige la description AI Overview tire aussi bien du site corporate que d'autres pages liées à l'entité, ce qui inclut du contenu ancien, non maintenu, ou mal cadré, comme le montre l'exemple RustyBrick avec sa mention « niche solutions » qui ne reflète plus la posture actuelle. Trois implications concrètes pour un consultant en mandat Niche SEO :

1. La cohérence des informations entre fiche Business Profile, page « À propos » du site, About Wikipedia si présent, et pages tiers d'autorité prend un poids nouveau. Une description AI Overview dérivée d'un texte périmé peut désaligner la présentation d'un commerce avec sa réalité opérationnelle.
2. Le contrôle de la description en champ libre de la fiche Business Profile ne suffit plus à couvrir la surface locale d'une requête de marque : la surface AI Overview arbitre son propre récit à partir de la web presence entière.
3. Aucun paramètre d'opt-out de la conversion du knowledge panel en AI Overview n'est documenté par Google au 27 septembre 2026, et le comportement n'apparaît que sur certaines requêtes de marque locale, sans règle publique de sélection.

Cf. [[concepts/agentic-search]] pour la substitution de l'affichage direct par une réponse synthétisée avec bouton d'expansion conversationnelle, et [[concepts/metriques-visibilite-geo]] pour l'écart entre présence de fiche et rendu de citation.

Corroboration : [Silverback Marketing recap 21-25 septembre](https://silverbackmarketing.com/seo-geo-ai-visibility-weekly-roundup-sep21-25) reprend le fait le 25 septembre ; le [recap Search Engine Roundtable du 17 septembre](https://www.seroundtable.com/recap-09-17-2026-42108.html) confirme la trace du billet original.

Réserves : le rollout n'est pas mesuré sur un échantillon de fiches, aucune donnée publique n'indique le pourcentage de knowledge panels concernés, aucune mesure d'impact CTR ou de clic sortant n'est disponible. La position de Google (opt-in par attribut de fiche, opt-out possible) reste non documentée.

## Brève 2 — Business SEO — News UK constate 20 pourcent de trafic non humain sur six mois, dont 6 pourcent bloqué activement, et fait le lien avec la bascule d'audience directe

Tom Jackson, Chief Technology Officer de News UK (The Times, The Sun, The Sunday Times), déclare le 10 septembre 2026 à la Future of Media Technology Conference organisée par Press Gazette qu'environ un cinquième du trafic entrant sur les sites du groupe sur les six derniers mois est non humain. Charlotte Tobitt reprend et documente l'intervention le 23 septembre dans un article publié sur Press Gazette ([Press Gazette 23 sept](https://pressgazette.co.uk/publishers/digital-journalism/fifth-of-news-uk-website-traffic-was-non-human-in-past-six-months/)).

Verbatim Tom Jackson : « So 6% of our traffic we're currently blocking ». Le déploiement de l'outil de protection Netacea a produit une baisse mesurée : « when we first switched on Netacea, those numbers were significantly higher, and they've come down a lot ». L'évaluation qu'il fait de son propre dispositif : « probably not » watertight, « but it's pretty good, I think ».

Ce que ça change pour un modèle de business SEO côté éditeur premium. Un cinquième du trafic n'atteint pas l'audience monétisable ; un tiers de ce non humain est identifié comme malveillant et coupé. Le reste est une composition de crawlers légitimes, robots d'indexation classiques, agents IA, et signaux d'analytique agrégée. Trois implications pratiques pour un consultant qui audite un éditeur au trafic non humain élevé :

1. Le trafic brut (impressions serveur, sessions non filtrées) ne peut plus servir d'indicateur de portée éditoriale : la vraie base audience monétisable est la fraction humaine servie, après filtrage bot.
2. La bascule News UK vers l'audience directe (application, newsletter, abonné) qu'évoque Jackson n'est pas une posture de communication, c'est un ajustement à un environnement où le trafic search perd en pouvoir explicatif : l'AI, dit Jackson, n'a pas provoqué un « cliff edge » mais a renforcé le repositionnement sur la relation directe.
3. Le coût opérationnel de la protection bot (déploiement Netacea, maintenance, faux positifs) devient une ligne budgétaire à documenter dans un audit de rentabilité SEO éditeur, à mettre en regard de la fraction de trafic non humain effectivement bloquée et de la fraction laissée passer par choix.

Cf. [[concepts/agentic-search]] pour l'entrée dans le mix des agents IA côté crawl, distincts des bots malveillants et des robots d'indexation classiques.

Corroboration : la même mesure et le même verbatim sont repris dans le [recap Silverback Marketing 21-25 septembre](https://silverbackmarketing.com/seo-geo-ai-visibility-weekly-roundup-sep21-25) sous la rubrique du 23 septembre. Second reprise avec chiffre confirmé : [Media Copilot](https://mediacopilot.ai/news-uk-bot-traffic/).

Réserves : la mesure porte sur les propriétés News UK, elle n'est pas un panel éditeur. La répartition à l'intérieur du non humain non bloqué (crawlers légitimes vs agents IA vs autres) n'est pas publiée. La comparaison inter-éditeurs n'est pas disponible ; d'autres groupes ont publié en 2025 et 2026 des mesures allant de 15 à 60 pourcent, sans méthodologie unifiée.

---

*Édition v2 du 27 septembre 2026, produite par SyntheticBrain. Draft non envoyé. Vouvoiement analyste, zéro langage métaphorique, zéro tiret cadratim intra-texte, sources cliquables sur chaque affirmation, deux sources indépendantes minimum par claim publié.*
