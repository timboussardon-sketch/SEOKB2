# Algorithme — édition du 3 septembre 2026 (v2)

## Résumé (3 à 5 points capitaux)

- Étude Kevin Indig publiée le 31 août 2026 sur 3 000 listicles courants : après contrôle des variables, la fraîcheur est le seul signal statistique robuste qui sépare les positions top 3 des positions 8-10 ([Growth Memo](https://www.growth-memo.com/p/what-makes-a-good-listicle), [Search Engine Land](https://searchengineland.com/what-makes-good-listicle-486330)).
- Fraîcheur : 66,6 pour cent des pages en top 3 portent une date des deux dernières années contre 57,3 pour cent en positions 8-10, et une date ancienne ou illisible est associée à 56 pour cent de chances en moins d'être en top 3.
- Malgré la démotion Google de janvier 2026, les listicles auto-promotionnels ont gagné 38 pour cent de trafic médian entre janvier et août 2026 sur les requêtes commerciales ([PPC Land](https://ppc.land/vendor-listicles-gain-38-median-traffic-since-googles-january-demotion/)).
- Suite du dossier Gemini 3.8 Flash : Gagan Ghotra et Glenn Gabe observent depuis le 3 septembre que le modèle cite et lie moins de sources que le modèle par défaut, screenshots à l'appui ([Search Engine Roundtable](https://www.seroundtable.com/google-ai-mode-gemini-38-no-links-42011.html)).
- Google Merchant Center étend ses rapports AI performance insights à l'Australie, au Canada, à l'Inde et à la Nouvelle-Zélande, en plus des États-Unis où la fonction était lancée en juillet 2026 ([Search Engine Roundtable](https://www.seroundtable.com/google-expands-merchant-center-ai-performance-insights-42005.html)).

---

## Info du jour — Étude Indig sur 3 000 listicles : la fraîcheur est le seul signal statistique qui tient après contrôle des variables (pilier Actualité SEO)

**Le fait.** Kevin Indig a publié le 31 août 2026 sur Growth Memo une analyse quantitative de 3 000 listicles sur 15 verticaux ([Growth Memo](https://www.growth-memo.com/p/what-makes-a-good-listicle)). L'étude a été relayée le 2 septembre 2026 à 9h ET sur Search Engine Land sous la propre signature d'Indig ([Search Engine Land](https://searchengineland.com/what-makes-good-listicle-486330)). Elle prolonge une analyse du 24 août 2026 sur la démotion des listicles couverte par PPC Land ([PPC Land](https://ppc.land/vendor-listicles-gain-38-median-traffic-since-googles-january-demotion/)).

**La méthodologie.** L'étude combine deux jeux de données. Le premier est un crawl SE Ranking de 60 000 requêtes Google desktop US-English sur 15 verticaux, 5,32 millions de lignes de résultats organiques collectées sur une fenêtre de 47 heures en août 2026. Le second est un échantillon équilibré de 3 000 listicles (200 par vertical, moitié listicles chiffrés dans le titre, moitié roundups éditoriaux) crawlés pour leurs signaux objectifs : nombre de mots, images, titres H2, dates, canonicals, données structurées. Le protocole compare pages du top 3 à pages en positions 8 à 10 via des modèles ajustés qui contrôlent le vertical, le libellé de la requête, le type de listicle, la répétition d'un même domaine, et la fréquence de publication.

**Les cinq chiffres à retenir.**

1. Fraîcheur : 66,6 pour cent des pages en top 3 affichent une date des deux dernières années, contre 57,3 pour cent en positions 8-10 ; une date ancienne ou illisible est associée à 56 pour cent de chances en moins d'être en top 3.
2. Longueur : les pages en top 3 ont 21,5 pour cent de mots en plus (médiane) et 38,9 pour cent d'images en plus que les pages en positions 8-10.
3. Format chiffré : les listicles avec un compteur explicite dans le titre gagnent 56,8 pour cent de leurs confrontations directes contre les roundups éditoriaux ; position moyenne 3,77 pour les listicles chiffrés contre 4,59 pour les roundups.
4. Numéro dans le titre : les listicles à 51-100 items en titre ont une position moyenne de 4,11 contre 5,85 pour les listicles à 2-5 items.
5. Vendor listicles : 74,7 pour cent des comparatifs B2B écrits par un éditeur qui vend un produit placent leur propre produit en première position, et 90,4 pour cent de ces pages ont gagné du trafic entre janvier et août 2026, avec un gain médian de 186 pour cent pour les pages déjà classées avant janvier.

**Ce que l'étude conclut, verbatim.**

- Sur les signaux : « Only freshness predicted top-three rankings ».
- Sur les listicles auto-promotionnels : « Self-serving listicles are well and alive ».
- Sur l'effet des AI Overviews : « AI Overviews change that. In AI Overviews, you get a clear recommendation for brands […] It's a philosophical shift » qui rend selon Indig la valeur des listicles « even more questionable ».

**Ce que l'étude n'a pas trouvé.** Le pré-résultat le plus important est ce qui n'a pas survécu au contrôle des variables. Les signaux souvent avancés dans la littérature SEO comme prédicteurs de rang sur listicles — présence d'un author bio, marquage schema Article ou HowTo, densité de headings H2, structured data spécifiques — n'ont pas montré de corrélation statistique robuste après ajustement dans le modèle d'Indig. Sur les sections en particulier : une augmentation d'un écart-type du nombre de headings est associée à 29 pour cent de chances en moins d'être en top 3, résultat contre-intuitif qui suggère que la fragmentation excessive nuit plus qu'elle n'aide.

**Trois lectures opérationnelles pour un consultant SEO.**

1. Sur un listicle qui existe déjà, la première action à impact est de tenir la date de mise à jour à jour, avec une date parsable par un crawler et cohérente entre le HTML visible, le marqueur `datePublished` ou `dateModified`, et le contenu. Refonte annuelle a minima, refresh trimestriel sur les verticaux à obsolescence rapide (B2B software, consumer tech, gaming). C'est cohérent avec [[concepts/fraicheur-contenu]] déjà tenu par le vault comme levier de citation IA.
2. Sur la structure : privilégier un compteur explicite dans le titre (« 12 outils… », pas « les meilleurs outils… ») et viser un nombre d'items élevé quand la matière le permet, tout en évitant la sur-segmentation en sous-parties H2. Le signal contre-intuitif sur les headings suggère qu'une prose dense sur chaque item vaut mieux qu'une architecture profonde qui découpe artificiellement le contenu.
3. Sur les listicles auto-promotionnels vendor : la démotion de janvier 2026 n'a pas empêché ces pages de gagner du trafic sur la fenêtre suivante, avec 90,4 pour cent des pages en croissance et un gain médian de 186 pour cent sur celles qui étaient déjà classées. Pour un client B2B software qui publie des comparatifs où son propre produit est cité, la question stratégique n'est pas de purger le biais mais de rendre l'auto-citation défendable au niveau du contenu (méthodologie explicite, critères comparables, mentions honnêtes des concurrents). C'est cohérent avec [[concepts/e-e-a-t]] compris comme jugement externe, pas comme déclaration côté page.

**Angle GEO.** Indig écrit que les AI Overviews rendent la valeur des listicles « even more questionable » parce qu'une réponse générée avec recommandation de marque intégrée court-circuite l'intention de comparaison. Le signal implicite : sur une requête « best X », l'utilisateur peut recevoir une recommandation directe sans jamais cliquer sur un listicle. C'est cohérent avec [[concepts/metriques-visibilite-geo]] et avec le constat que l'impression AI Mode se dissocie du clic organique.

**Réserves de fact-check.**

- Étude à auteur unique, méthodologie publique et détaillée mais data non ré-analysée par un chercheur tiers.
- L'intervalle de confiance à 95 pour cent du signal « self-promotion » va de 51 pour cent en moins à 120 pour cent en plus, avec p-value 0,91 sur cette variable spécifique : le gain de 186 pour cent de trafic médian sur les pages vendor déjà classées est un fait, mais son attribution à l'auto-promotion elle-même comme signal causal n'est pas établie statistiquement.
- Le protocole est US-English desktop uniquement. Rien n'est mesuré sur mobile, sur autres langues, ou sur d'autres marchés que les États-Unis.
- Le crawl a été fait sur une fenêtre de 47 heures, ce qui capture un état instantané et pas une tendance. Les résultats peuvent différer d'un mois à l'autre.

**Prédictions datées.**

- P-2026-09-03-5 : au moins une réplication indépendante de l'étude Indig sur un corpus non US ou non anglophone sera publiée avant le 31 mars 2027, avec au moins un des signaux (fraîcheur, compteur en titre, sections) mesuré dans le même sens. Confiance 0,50.
- P-2026-09-03-6 : Google publiera avant le 30 juin 2027 une communication Search Central qui reprend explicitement l'idée que la fraîcheur des listicles influe sur leur classement, sans citer l'étude Indig. Confiance 0,35.

**Ancrage doctrine.** [[concepts/fraicheur-contenu]] (l'étude Indig quantifie le signal fraîcheur sur un corpus de listicles avec une méthodologie ajustée, ce qui donne un chiffre de référence pour le vault : 56 pour cent de chances en moins d'être en top 3 avec une date ancienne, à comparer avec le chiffre de citation IA déjà tenu dans la fiche), [[concepts/information-gain]] (le signal « compteur dans le titre » et l'observation contre-intuitive sur les headings pointent vers un contenu dense avec information gain effectif plutôt qu'une architecture fragmentée), [[concepts/e-e-a-t]] (les vendor listicles qui gagnent 186 pour cent de trafic médian illustrent que l'E-E-A-T est un jugement externe sur la substance du contenu, pas une case à cocher sur la présence d'un author bio), [[concepts/metriques-visibilite-geo]] (le passage cité verbatim d'Indig sur les AI Overviews qui court-circuitent l'intention de comparaison confirme que la mesure de visibilité GEO doit se distinguer du classement organique classique).

---

## Brèves

### Brève 1 — Ghotra et Gabe observent que Gemini 3.8 Flash cite moins de sources dans AI Mode (pilier GEO / search IA)

**Le fait.** Le 3 septembre 2026 à 7h41 ET, Barry Schwartz a publié sur Search Engine Roundtable une observation partagée sur X par Gagan Ghotra et corroborée par Glenn Gabe : Gemini 3.8 Flash, déployé la veille dans AI Mode pour les abonnés Google AI Pro et Ultra, cite moins de sources et affiche moins de liens sortants que le modèle par défaut ([Search Engine Roundtable](https://www.seroundtable.com/google-ai-mode-gemini-38-no-links-42011.html)). Ghotra a documenté quatre requêtes informationnelles pour lesquelles AI Mode en 3.8 Flash renvoie une réponse sans aucune citation ni lien, screenshots à l'appui. Gabe verbatim : « Whoa, Gagan is right. See below between default model and 3.8 Flash. What is going on here? ».

**Ce que ça change côté mesure.** Cette observation, si elle est confirmée sur un échantillon plus large, contredit la lecture faite dans l'édition matinale sur Gemini 3.8 Flash : le modèle ne bougeait pas seulement sur les benchmarks de raisonnement, il change aussi la mécanique de citation elle-même. Un outil GEO tiers qui échantillonne AI Mode via un compte Pro depuis le 2 septembre mesurerait, sur ce point, un pipeline dont la couche de citation vient d'être re-paramétrée. Toute baseline de taux de citation ou de dark matter rate captée avec 3.8 Flash sur des requêtes informationnelles risque de faire baisser artificiellement le score de sites qui étaient bien cités par 3.7 Flash sur les mêmes requêtes.

**Réserves.** Observation qualitative isolée, quatre screenshots de requêtes chez un seul observateur (Ghotra) plus deux captures comparatives chez un second (Gabe). Pas de mesure agrégée, pas d'échantillon documenté, pas de statement Google au 3 septembre 2026. Barry Schwartz lui-même écrit : « I am not sure why this would be and I hope this is something that Google can fix soon », ce qui laisse ouvert le fait que ce soit un bug transitoire, un choix produit, ou un artefact du pipeline en cours de rodage.

**Ce qu'un consultant SEO / GEO peut faire dans la fenêtre.** Sur un audit GEO qui échantillonne AI Mode cette semaine, ajouter au protocole une variable « modèle utilisé » (3.8 Flash sélectionné via le menu + vs modèle par défaut) et mesurer les deux en parallèle sur le même set de requêtes. Si l'écart de citations est mesurable au-delà des observations qualitatives Ghotra/Gabe, produire pour le client une note qui distingue baseline pré-2 septembre, mesure en 3.8 Flash, et mesure sur modèle par défaut, avec date explicite.

**Ancrage doctrine.** [[concepts/metriques-visibilite-geo]] (le fait relayé par Ghotra et Gabe illustre concrètement que la métrique « nombre de citations dans AI Mode » est fonction du modèle qui produit la réponse, pas seulement du contenu source ni du classement organique ; c'est un rappel que la surface GEO est un pipeline multi-composants), [[concepts/arbitrage-plateforme-publication]] (deux modèles disponibles sur la même surface AI Mode via un menu utilisateur produisent des sorties structurellement différentes, cas d'arbitrage à documenter dans un rapport client).

### Brève 2 — Google étend les rapports AI performance insights de Merchant Center à quatre nouveaux marchés (pilier GEO / search IA)

**Le fait.** Le 3 septembre 2026, Barry Schwartz a rapporté sur Search Engine Roundtable que Google a étendu ses rapports AI performance insights dans Merchant Center à l'Australie, au Canada, à l'Inde et à la Nouvelle-Zélande, en plus des États-Unis où la fonction avait été lancée en juillet 2026 ([Search Engine Roundtable](https://www.seroundtable.com/google-expands-merchant-center-ai-performance-insights-42005.html)). La documentation Google mise à jour précise que les rapports couvrent « English-language queries for Merchant Center accounts in Australia, Canada, India, New Zealand, and the United States ». Google écrit : « With these insights, you can better understand how your brands show up in conversational queries ».

**Ce que la fonction mesure.** Le rapport donne aux marchands une vue de l'apparition de leurs produits et marques dans les requêtes conversationnelles avec intention d'achat sur AI Mode et AI Overviews. Il permet de suivre la visibilité de la marque à différentes étapes du parcours d'achat et d'ajuster la donnée produit en fonction des motifs de découverte observés. C'est un outil de mesure natif Google, distinct des outils GEO tiers qui échantillonnent AI Mode sans accès aux logs de Google.

**Ce que ça change pour un consultant e-commerce en France.** Rien à court terme sur le marché francophone : la limite « English-language queries » exclut de facto la France, la Belgique, la Suisse et le Québec dans les configurations Merchant Center rattachées à ces marchés. Un consultant qui accompagne un e-commerce français reste sur la mesure indirecte via outils tiers ou via Search Console AI performance reports (déployés globalement fin août 2026 selon Search Engine Land). Pour un client français qui a une entité canadienne ou australienne rattachée à Merchant Center dans ces marchés, la fonction devient exploitable dès aujourd'hui.

**Réserves.** Google ne publie pas la méthodologie exacte de calcul de la métrique de visibilité conversationnelle, ni la fenêtre temporelle exacte ni la granularité de requête. La comparabilité inter-marchés (États-Unis vs Canada par exemple) sur la même marque n'est pas discutée dans la doc au 3 septembre 2026.

**Ancrage doctrine.** [[concepts/metriques-visibilite-geo]] (Google construit progressivement une couche de mesure GEO first-party accessible côté marchand, distincte des outils tiers ; c'est une évolution du paysage de mesure qui va peser sur la doctrine de mesure GEO du vault dans les mois qui viennent), [[concepts/data-proprietaire]] (les données de citation conversationnelle par marque produites par Google Merchant Center deviennent une donnée de mesure côté client, à croiser avec la mesure organique classique et avec la mesure des outils tiers).

---

*Édition rédigée par SyntheticBrain. Rien n'a été envoyé.*
