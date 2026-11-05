# Algorithme — édition du 3 septembre 2026

## Résumé (3 à 5 points capitaux)

- Google a déployé le 2 septembre 2026 Gemini 3.8 Flash dans AI Mode pour les abonnés Google AI Pro et Ultra, avec un pricing introductif à 0,75 dollar par million de tokens en entrée et 3,75 dollars en sortie jusqu'au 31 décembre 2026 ([Search Engine Land](https://searchengineland.com/gemini-3-8-flash-rolling-out-in-google-search-486630), [9to5Google](https://9to5google.com/2026/09/02/gemini-3-8-flash-launch/)).
- Le modèle qui produit les réponses AI Mode change pour la troisième fois en trois mois ; côté GEO, cela redémarre la fenêtre d'observation des citations et rend caducs les benchmarks de citation antérieurs au 2 septembre.
- Perplexity a activé le 1er septembre 2026 un mode Hybrid Compute sur son application Mac qui exécute une partie de chaque tâche Perplexity Computer en local sur Apple Silicon (Gemma 4 E4B, Qwen3.6 35B-A3B, un modèle Perplexity dédié) et le reste dans le cloud, sous contrôle d'un classifieur de confidentialité ([9to5Mac](https://9to5mac.com/2026/09/01/perplexity-launches-privacy-minded-hybrid-compute-ai-feature-for-mac/), [Engadget](https://www.engadget.com/2248548/perplexitys-hybrid-compute-splits-sensitive-tasks-between-cloud-and-local-ai/)).
- Lily Ray, VP SEO et AI Search chez Amsive, a publié le 2 septembre 2026 dans Search Engine Land une entrevue 20 for 20 où elle transpose la leçon Penguin d'août 2012 aux tactiques de raccourci GEO actuelles et énonce : « the single best and most sustainable and important thing you can do for AI search visibility is good SEO » ([Search Engine Land](https://searchengineland.com/lily-ray-search-engine-land-20-for-20-interview-486614)).
- Bing teste le 2 septembre 2026 l'affichage de ses snippets sans nom de site, avec favicon plus URL, un test comparable à celui que Google avait mené en mai 2025 ([Search Engine Roundtable](https://www.seroundtable.com/bing-search-snippets-without-sitenames-41990.html)).

---

## Info du jour — Gemini 3.8 Flash déployé dans AI Mode trois semaines après 3.7 Flash (pilier GEO / search IA)

**Le fait.** Google a annoncé le 2 septembre 2026 que Gemini 3.8 Flash est disponible dans AI Mode pour les abonnés Google AI Pro et Ultra dans le monde. L'annonce vient de Robby Stein, VP of Product chez Google Search, dans un post sur X repris le 2 septembre à 11h56 ET par Barry Schwartz sur Search Engine Land ([Search Engine Land](https://searchengineland.com/gemini-3-8-flash-rolling-out-in-google-search-486630)). Verbatim Robby Stein : « Gemini 3.8 Flash has landed in Search […] It's our most intelligent workhorse model yet, delivering significant improvements from 3.7 Flash across software engineering, agentic tasks, and multi-step reasoning ». Le modèle se sélectionne via l'icône (+) dans le menu déroulant de modèle d'AI Mode.

**Ce que la source primaire dit du modèle lui-même.** 9to5Google, sous la signature d'Abner Li le 2 septembre 2026, restitue la position officielle de Google : Gemini 3.8 Flash « delivers substantial gains » sur son prédécesseur 3.7 Flash et « often approaching the performance of higher-cost frontier models » ([9to5Google](https://9to5google.com/2026/09/02/gemini-3-8-flash-launch/)). Trois benchmarks cités : DeepSWE v1.1 (résolution autonome de tâches d'ingénierie logicielle où Google dit dépasser la plupart des modèles frontier de taille supérieure), Vals Finance Agent V2 et Harvey's Legal Agent Benchmark (analyse quantitative et professionnelle), et HLE-Verified où Gemini 3.8 Flash atteint 54,9 pour cent sur un ensemble multi-domaines. Pricing d'introduction : 0,75 dollar par million de tokens en entrée et 3,75 dollars par million de tokens en sortie jusqu'au 31 décembre 2026 ; au-delà, les deux tarifs doublent à 1,50 et 7,50 dollars. Disponibilité produits : Gemini app (Pro et Ultra), AI Mode dans Google Search, Google Sheets, Google AI Studio, et Gemini API. Knowledge cutoff annoncé à mars 2026, avec certains domaines limités à janvier 2025.

**Cadence.** La sortie du 2 septembre 2026 est la troisième mise à jour du modèle Flash en trois mois selon 9to5Google, et intervient trois semaines après le déploiement de Gemini 3.7 Flash ([9to5Google](https://9to5google.com/2026/09/02/gemini-3-8-flash-launch/)). Les précédentes traces internes du vault confirment la présence de Gemini 3.5 Flash et 3.7 Flash dans said_index : le passage à 3.8 est le troisième changement de modèle Flash tracé dans l'année. Search Engine Land note par ailleurs que le déploiement à l'ensemble des utilisateurs sur plans gratuits est attendu « dans les semaines ou mois qui viennent » sans date engagée.

**Ce qui n'est pas dit.** Google ne publie ni changement quantifié du taux de citation dans AI Mode ni évaluation comparée sur les tâches de search retrieval (requêtes de recherche, extraction de passages) entre 3.7 et 3.8. Les benchmarks cités portent sur ingénierie logicielle, agents et raisonnement multi-étapes, pas sur la mécanique de sélection de sources qui structure AI Mode. Aucune roadmap n'est publiée pour l'extension aux utilisateurs Free ; aucune donnée agrégée par pays ou par langue au 2 septembre.

**Trois lectures opérationnelles pour un consultant SEO / GEO.**

1. Les benchmarks de citation menés sur AI Mode avant le 2 septembre 2026 mesurent un pipeline dont le modèle de génération vient de changer. Toute analyse de taux de citation, de dark matter rate ou de citation retention rate qui repose sur des captures antérieures au 2 septembre est à requalifier en baseline pré-3.8. Un consultant qui livre une mesure GEO à un client cette semaine doit soit dater explicitement la période mesurée avant 2 septembre, soit relancer une capture sur la fenêtre 2-8 septembre à même méthode pour comparer.

2. Le passage 3.7 → 3.8 est technique et incrémental côté modèle, mais il opère sur la même mécanique de fan-out queries + retrieval + génération d'AI Mode. Les leviers structurels côté site (passage-ranking, densité d'entités, données propriétaires citables, marquage structuré) restent les mêmes ; ce qui peut bouger, c'est la sélection de passages à profondeur constante, pas les règles éditoriales.

3. La disponibilité initiale « Pro et Ultra worldwide » vs Free ultérieur est une variable de mesure : les outils GEO tiers qui échantillonnent AI Mode via des comptes gratuits mesurent, jusqu'au déploiement complet, un modèle antérieur. C'est cohérent avec [[concepts/arbitrage-plateforme-publication]] : la même surface Google Search sert des réponses générées par des modèles différents selon la tier d'abonnement.

**Réserves de fact-check.**

- Le pricing 0,75/3,75 dollars par million de tokens et le doublement au 1er janvier 2027 ne sont pas confirmés dans le post X de Robby Stein cité par Search Engine Land ; ils sont attribués par 9to5Google à la communication officielle Google associée au lancement.
- Le score HLE-Verified de 54,9 pour cent n'est pas comparé dans les sources consultées à celui de 3.7 Flash ; l'amélioration relative n'est donc pas chiffrable ici.
- Le nombre exact d'utilisateurs Pro et Ultra concernés n'est pas publié.

**Prédictions datées.**

- P-2026-09-03-1 : au moins un outil GEO tiers (Otterly, Profound, Ahrefs Brand Radar, seoClarity ou équivalent) publiera avant le 31 octobre 2026 une comparaison chiffrée du taux de citation AI Mode ou du dark matter rate avant / après le 2 septembre 2026 sur un panel de plus de 500 requêtes. Confiance 0,55.
- P-2026-09-03-2 : Google déploiera Gemini 3.8 Flash aux utilisateurs Free d'AI Mode avant le 15 novembre 2026, cohérent avec la cadence trois semaines observée entre 3.7 et 3.8 Flash. Confiance 0,50.
- P-2026-09-03-3 : Google publiera un billet ou une doc Search Central qui associe Gemini 3.8 Flash à un changement de comportement mesurable d'AI Mode (extraits, longueur des réponses, structure des citations) avant le 31 mars 2027. Confiance 0,30.

**Ancrage doctrine.** [[concepts/geo]], [[concepts/metriques-visibilite-geo]] (les mesures GEO agrégées sur AI Mode reposent sur un pipeline dont un composant vient de changer, ce qui affecte la comparabilité temporelle des chiffres publiés ; toute métrique Imp_wc ou Imp_pos calculée avant / après la bascule doit être datée), [[concepts/arbitrage-plateforme-publication]] (la même surface AI Mode sert deux modèles distincts pendant la fenêtre de déploiement selon la tier d'abonnement, cas d'arbitrage à surveiller côté mesure).

---

## Brèves

### Brève 1 — Perplexity active Hybrid Compute sur Mac le 1er septembre 2026 (pilier GEO / search IA)

**Le fait.** Le 1er septembre 2026, Perplexity a activé Hybrid Compute sur son application Mac. Aravind Srinivas, cofondateur et CEO, a annoncé la mise en service dans un post sur X ([9to5Mac](https://9to5mac.com/2026/09/01/perplexity-launches-privacy-minded-hybrid-compute-ai-feature-for-mac/), [Engadget](https://www.engadget.com/2248548/perplexitys-hybrid-compute-splits-sensitive-tasks-between-cloud-and-local-ai/), [Unite.AI](https://www.unite.ai/perplexity-launches-hybrid-compute-on-mac-with-local-privacy-gate/)). Le mode divise chaque tâche Perplexity Computer entre modèles frontier dans le cloud et modèle local sur la machine.

**Mécanique.** Cloud : reasoning frontier, web search, planning. Local : traitement des fichiers privés, des informations sensibles et des actions sur l'appareil. Un classifieur de confidentialité intégré scanne chaque envoi ou upload et flague ce qui doit rester local. Trois modèles locaux : Gemma 4 E4B, Qwen3.6 35B-A3B, plus un modèle Perplexity post-trained pour Perplexity Computer. Prérequis : Apple Silicon, macOS 15 ou supérieur, 24 GB de mémoire unifiée minimum. Disponibilité : abonnés Perplexity Pro, Max et Enterprise. Installation automatique des modèles, sans terminal, avec compteurs CPU / GPU / mémoire / tokens en temps réel.

**Trois lectures pour un consultant SEO / GEO.**

1. Côté indexation et citation publique par Perplexity sur web ouvert, rien ne change : les fichiers privés de l'utilisateur ne participent pas au corpus public. Le fait relève de l'agentic search côté client (comment un agent traite des documents locaux) plus que du canal de citation Perplexity côté site source.

2. Il devient plus difficile à un outil GEO tiers de reconstituer ce que l'agent a effectivement lu, puisqu'une part de la chaîne s'exécute sur la machine de l'utilisateur sans trace serveur Perplexity. Cohérent avec [[concepts/agentic-search]] : la mesure externe atteint sa limite dès qu'une partie de la décision d'agent est locale.

3. Pour un éditeur qui vise la citation Perplexity, la valeur du contenu web ouvert et lisible par un crawler reste la même. Rien dans l'annonce ne modifie la manière dont Perplexity fetche et cite des sources externes en ligne.

**Réserves.** Aucun chiffre d'adoption publié au 3 septembre. Le classifieur de confidentialité n'est pas documenté publiquement dans son fonctionnement interne ; sa précision et son rappel ne sont pas mesurés par un tiers indépendant.

**Ancrage doctrine.** [[concepts/agentic-search]] (la mesure externe d'un agent est bornée par ce qui remonte au serveur du moteur ; un split cloud/local rend structurellement invisible une part de l'activité d'agent), [[concepts/data-proprietaire]] (les fichiers privés traités en local restent des données propriétaires côté utilisateur ; ils n'entrent pas dans le corpus d'entraînement ni dans l'index Perplexity).

### Brève 2 — Lily Ray dans Search Engine Land : « the single best and most sustainable […] is good SEO » (pilier Actualité SEO)

**Le fait.** Search Engine Land a publié le 2 septembre 2026 à 11h23 ET, sous la signature de Danny Goodwin, une interview 20 for 20 de Lily Ray, VP SEO et AI Search chez Amsive ([Search Engine Land](https://searchengineland.com/lily-ray-search-engine-land-20-for-20-interview-486614)). L'interview traite d'un parallèle historique entre le comportement des acteurs à la veille de Penguin (août 2012) et la période GEO actuelle.

**Ce que Lily Ray déclare, verbatim.**

- Sur Penguin : « I think it was August 2012. Went to work that day and all of our rankings disappeared ».
- Sur la pression actuelle : « Everyone's looking for shortcuts, and I get it. There's a lot of pressure right now ».
- Sur l'urgence : « I actually think trying to drive results quickly is one of the worst things you can do ».
- Sur le volume de contenu : « Less is more. I don't think that the best way to achieve SEO success right now is to create as much content as possible » et « The sites that try to create as much content as possible eventually get burned ».
- Sur la relation SEO / AI search : « If you understood how AI search works, you would understand that SEO is more important than ever » et « the single best and most sustainable and important thing you can do for AI search visibility is good SEO ».
- Sur E-E-A-T : « You don't have like, 'I have good E-E-A-T'. It's not just what you say on your website ».
- Sur la Helpful Content Update : « I would say like maybe 40 pct of the sites that they went after were really trying to do things right ».

**Deux lectures pour un consultant SEO / GEO.**

1. La déclaration « good SEO = AI search visibility » n'est pas nouvelle ; elle a été soutenue par Lily Ray dans plusieurs formats (webinars AirOps, podcast BuzzStream, keynote Affiliate Summit 2026 courant 2025-2026). Son originalité ici est la mise en parallèle explicite avec l'expérience Penguin, adressée à des équipes qui optimisent aujourd'hui pour AI Overviews et AI Mode via des tactiques automatisées. La position corrobore la doctrine data propriétaire déjà tenue dans le vault.

2. La statistique 40 pour cent des sites touchés par la Helpful Content Update qui « essayaient vraiment de bien faire » est une estimation de Lily Ray à partir de son propre travail d'audit chez ses clients, pas une mesure publiée sur échantillon documenté. C'est une opinion d'expert, à traiter comme telle et non comme un chiffre reproductible.

**Réserves.** Interview mono-source côté publication (Search Engine Land) ; les positions relayées sont corroborées par des interventions antérieures de Lily Ray mais ne sont pas indépendamment cross-sourcées sur le fond dans une autre publication en date du 2 septembre 2026.

**Prédiction datée.**

- P-2026-09-03-4 : Google déclenchera au moins une action manuelle spam publique documentée sur un site utilisant intensivement des tactiques GEO automatisées (production d'articles à volume pour se citer en AI Overviews ou AI Mode) avant le 30 juin 2027. Confiance 0,45.

**Ancrage doctrine.** [[concepts/e-e-a-t]] (la position Lily Ray sur E-E-A-T comme cadre externe, non déclaratif, rejoint la lecture du vault : E-E-A-T n'est pas une case à cocher côté page mais un jugement produit par le moteur à partir de signaux externes), [[concepts/data-proprietaire]] (le levier durable pour AI search visibility reste, chez Lily Ray comme dans la doctrine Tim, la donnée et l'angle qu'un site est seul à produire).

### Brève 3 — Bing teste des snippets sans nom de site (pilier Actualité SEO)

**Le fait.** Bing teste depuis le 1er septembre 2026 l'affichage de ses snippets de résultats sans nom de site, en montrant à la place le favicon suivi de l'URL avec breadcrumbs ([Search Engine Roundtable](https://www.seroundtable.com/bing-search-snippets-without-sitenames-41990.html)). Le test a été repéré par Sachin Patel, relayé par Search Engine Watch ([Search Engine Watch](https://searchenginewatch.com/bing-tests-removing-site-names-from-search-results/)), puis documenté avec captures d'écran par Barry Schwartz sur Search Engine Roundtable le 2 septembre 2026. Microsoft n'a pas publié de statement officiel au 2 septembre.

**Contexte.** Le test reproduit ce que Google avait testé en mai 2025 avant de reculer. Le titre affiché reste le title du document ; ce qui change, c'est la ligne d'attribution au-dessus du titre : nom de site remplacé par URL.

**Trois lectures.**

1. Il s'agit d'un test A/B, pas d'un déploiement. Rien n'indique la part de traffic Bing soumise au test, ni un calendrier de généralisation ou d'arrêt.

2. Un consultant qui optimise pour Bing (site verticaux BtoB, marchés US où Bing conserve une part significative) n'a rien à changer côté balise ou marquage : le sitename officiel reste défini via structured data WebSite avec la propriété name, mais Bing n'affiche pas cette valeur pendant le test.

3. Pour un site à marque faible, l'affichage URL peut réduire la reconnaissabilité au clic ; pour un site à URL très descriptif (site nom-de-marque-clair.com), l'effet est plus neutre. Impact concret non mesuré au 2 septembre 2026.

**Réserves.** Test observationnel isolé, pas d'échantillon publié. Google avait testé la même chose en mai 2025 puis avait rétabli les noms de site après quelques semaines ; il est possible que Bing suive la même trajectoire.

**Ancrage doctrine.** [[concepts/arbitrage-plateforme-publication]] (les surfaces de résultats sur Bing et Google évoluent séparément ; le nommage d'une marque dans les SERP est une variable produit, pas une variable éditoriale côté site).

---

*Édition rédigée par SyntheticBrain. Rien n'a été envoyé.*
