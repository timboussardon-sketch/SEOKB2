---
date: 2026-08-19
edition: 2026-08-19-revue-presse
pilier_info_du_jour: recherche-agentique
pilier_breve: recherche-agentique
format: 2-sections
capture_mode: native
---

# Query fanout de ChatGPT modifié le 8 août : la part de Reddit dans les citations tombe de 3,8 % à 0,5 % en une semaine

**Résumé**
- La part de Reddit dans les citations de ChatGPT Search passe de 3,83 % de moyenne quotidienne du 18 juillet au 7 août 2026 à 0,52 % de moyenne quotidienne du 14 au 17 août, soit une baisse relative de 86,4 % en une semaine, mesurée par Promptwatch sur un corpus de plus de 26 milliards de citations, prompts et réponses collectés directement sur les principales interfaces génératives.
- La chute brutale intervient le 14 août 2026, la baisse s'amorce le 8 août au moment où ChatGPT modifie son mécanisme de query fanout, c'est-à-dire l'étape qui décompose une question utilisateur en plusieurs sous-requêtes envoyées à un index de recherche.
- Google AI Overviews (baisse relative de 11,3 %) et Google AI Mode (baisse relative de 30,5 %) enregistrent sur la même période un recul graduel de Reddit, sans point de rupture net à une date donnée. L'événement est spécifique à OpenAI et non un mouvement général sur les sources communautaires.
- La longueur moyenne d'une sous-requête fanout est passée d'environ 6 mots en octobre 2025 à environ 12 mots en janvier 2026, avec un pic à environ 16 mots en semaine 49, mesuré par Peec AI sur 20 millions de sous-requêtes. Le nombre de sous-requêtes par prompt est resté stable. Chaque sous-requête est plus précise, elle n'est pas plus nombreuse.
- ChatGPT 5.4 a masqué les sous-requêtes de fanout dans les fichiers de conversation exposés côté navigateur. Les outils d'inspection publics cessent de renvoyer la donnée, l'accès reste possible via l'API OpenAI, ce qui déplace le seuil d'observabilité du mécanisme vers un accès programmatique payant.

## Info du jour, pilier Recherche agentique

Le fait mesuré. [Promptwatch](https://promptwatch.com/data/reddit-citations-are-dropping-in-chatgpt), qui suit la part de citations de chaque domaine dans les principaux moteurs génératifs à partir d'un corpus de plus de 26 milliards de citations, prompts et réponses collectés directement sur ChatGPT, Gemini, Perplexity, Claude, Google AI Overviews et AI Mode, publie le 18 août 2026 la mesure suivante : la part quotidienne de reddit.com dans les citations de ChatGPT Search est restée stable à 3,83 % de moyenne du 18 juillet au 7 août 2026, puis a chuté sous 1 % le 14 août et se maintient à 0,52 % de moyenne du 14 au 17 août 2026. En relatif, c'est une baisse de 86,4 % en une semaine. La reprise éditoriale sort dans la journée. [Yash Thakker sur explainx.ai](https://explainx.ai/blog/reddit-citations-chatgpt-search-drop-august-2026) publie le 18 août avec les mêmes chiffres et la même chronologie. [Crypto Briefing](https://cryptobriefing.com/reddit-chatgpt-search-citations-drop/) publie le même jour, avec la même série de mesures.

Le mécanisme suspecté. La chronologie fait apparaître deux dates. Le 8 août 2026, la part quotidienne de Reddit passe de la fourchette 3,5 à 4 % à la fourchette 2 à 3 %. C'est le jour où ChatGPT modifie son mécanisme de query fanout, c'est-à-dire l'étape qui décompose une question utilisateur en plusieurs sous-requêtes envoyées en parallèle à un index de recherche, dont les résultats sont ensuite fusionnés pour composer la réponse. Puis, le 14 août, la part de Reddit tombe sous 1 % et s'y stabilise. Klaas Foppen, cofondateur de Promptwatch, attribue le décrochage à un changement de logique de sélection des sources dans ChatGPT, tout en indiquant que la mesure est provisoire et qu'un artefact de collecte de données ou un changement de filtre de déduplication ne peut pas être exclu à ce stade. Le fait mesuré est solide, trois sources indépendantes publient les mêmes chiffres sur la même chronologie. L'interprétation causale reste marquée comme provisoire par la source primaire elle-même.

Ce qui change dans le fanout. L'observation contextuelle est documentée par [Peec AI](https://peec.ai/blog/country-analysis-20-million-search-qfos) sur un corpus de 20 millions de sous-requêtes issues de ChatGPT. La longueur moyenne d'une sous-requête est passée d'environ 6 mots en octobre 2025 à environ 12 mots en janvier 2026, avec un pic à environ 16 mots en semaine 49. Le nombre de sous-requêtes par prompt est resté stable sur la période. Chaque sous-requête est plus précise, elle n'est pas plus nombreuse. Une sous-requête plus longue et plus qualifiée récupère un ensemble de pages différent : moins de fils de discussion communautaires, plus de pages qui répondent frontalement à la question qualifiée. Le format éditorial de Reddit, une page-fil avec plusieurs réponses hétérogènes autour d'une question courte, s'aligne mal avec ce type de récupération. La modification du 8 août 2026, si elle prolonge cette trajectoire de qualification croissante des sous-requêtes, produit exactement le type de redistribution observé.

Le comparatif Google. Sur la même période mesurée par Promptwatch, la part de Reddit dans Google AI Overviews passe de 2,37 % au début juillet à 2,10 % fin août, soit une baisse relative de 11,3 %, et dans Google AI Mode de 2,22 % à 1,54 %, soit une baisse relative de 30,5 %. Ces reculs existent, ils ne sont pas nuls, mais leur allure est progressive, sans point de rupture net à une date donnée. Cela indique que l'événement du 8 au 14 août est spécifique à OpenAI et non un mouvement général sur la valeur des sources communautaires.

Ce qui n'est pas dans le fait. Reddit lui-même n'a pas publié de commentaire opérationnel sur la mesure. OpenAI n'a pas documenté publiquement de changement de logique de sélection des sources à la date du 8 août. La corrélation temporelle entre la modification du fanout et la chute de la part de Reddit reste corrélationnelle, aucune source primaire OpenAI ne la valide. Un artefact de collecte, un changement de filtre de déduplication, ou un blocage réseau ponctuel côté ChatGPT en direction de reddit.com sont des explications alternatives que Promptwatch garde ouvertes.

Trois lectures pour un consultant SEO ou GEO qui suit un portefeuille de sites présents dans les moteurs génératifs.

Un, mesurer la part de citations de son propre domaine sur ChatGPT Search, ChatGPT AI Mode, Google AI Overviews et Google AI Mode sur des fenêtres roulantes de 7 jours plutôt que sur des moyennes mensuelles. Une chute concentrée sur 6 jours passe sous le radar d'une mesure mensuelle. Les outils de suivi de citations publient des courbes journalières, utiliser cette granularité est désormais nécessaire pour capter ce type d'événement.

Deux, analyser l'exposition de son propre corpus aux fanouts longs. Une page qui répond frontalement à une question longue et qualifiée bénéficie du nouveau régime. Une page-fil communautaire ou une page qui agrège plusieurs sujets sous un H1 court subit le même type de recul que Reddit. Le format éditorial devient une variable de recherche agentique, pas seulement de recherche organique classique.

Trois, ne pas dépendre d'un seul moteur pour la portée générative. La chute de Reddit dans ChatGPT ne s'observe pas dans les surfaces Google. Un domaine qui aurait construit sa présence générative via un seul moteur porte le même type de risque que Reddit sur ChatGPT.

Lien doctrine. Le fait s'inscrit dans [[concepts/agentic-search]] et [[concepts/arbitrage-plateforme-publication]]. Chaque moteur génératif est une surface distincte, gouvernée par une chaîne de récupération qui lui est propre. La modification d'une chaîne, ici le fanout de ChatGPT, redistribue les positions de citations en jours, pas en trimestres. La mesure côté serveur du crawler et la mesure côté outil GEO de la part de citations sont deux dimensions à combiner. [[concepts/metriques-visibilite-geo]] et [[concepts/data-proprietaire]] restent les référentiels de mesure.

Sources primaires et secondaires citées dans le corps :
- [Promptwatch, Reddit citations are dropping in ChatGPT, 18 août 2026](https://promptwatch.com/data/reddit-citations-are-dropping-in-chatgpt), source primaire, données quotidiennes, corpus 26 milliards de citations.
- [explainx.ai, Reddit ChatGPT Citations Drop 86 % (August 2026), Yash Thakker, 18 août 2026](https://explainx.ai/blog/reddit-citations-chatgpt-search-drop-august-2026), source secondaire.
- [Crypto Briefing, Reddit's ChatGPT Search citations drop 86 % in August, 18 août 2026](https://cryptobriefing.com/reddit-chatgpt-search-citations-drop/), source secondaire.
- [Peec AI, ChatGPT fan-outs have doubled in length in 4 months](https://peec.ai/blog/country-analysis-20-million-search-qfos), source primaire, données 20 millions de fanouts.

## Brève, pilier Recherche agentique

ChatGPT 5.4 masque ses sous-requêtes de fanout dans le navigateur. La deuxième moitié de la journée est moins visible dans les chiffres mais tout aussi mesurable. Depuis la mise à jour ChatGPT 5.4, les sous-requêtes générées par le mécanisme de query fanout ne sont plus exposées dans les fichiers de conversation lisibles côté navigateur. [Nectiv Digital](https://nectivdigital.com/blog/chatgpt-5-4-has-hidden-fan-out-queries-you-can-still-get-them-via-the-api-python-script-included), [Little Green Agency](https://littlegreenagency.co.uk/blog/chatgpt-has-hidden-its-fan-out-queries-heres-how-to-get-them-back-with-n8n/) et [Quolity](https://quolity.ai/chatgpt-search-query-extractor/) documentent, chacun de leur côté, la même observation. Les outils d'inspection qui lisaient jusque-là les fanouts dans le HTML de la conversation ne renvoient plus rien. Les fanouts restent extractibles via l'API OpenAI, ce qui déplace le seuil d'observabilité du mécanisme vers un accès programmatique payant.

Le fait est directement utile pour un consultant SEO ou GEO qui suit les fanouts d'une requête pour construire son plan de contenu ou pour analyser la sélection des sources par ChatGPT sur une requête cible. La méthode par extension navigateur ou script front-end cesse de produire de la donnée exploitable. La méthode API reste disponible mais suppose un compte OpenAI actif et une consommation de tokens facturés. La conjonction avec la mesure de Promptwatch est notable : le mécanisme dont l'impact devient chiffré (redistribution du 8 au 14 août) devient au même moment moins accessible à l'inspection publique.

Aucune annonce OpenAI ne documente le changement. Il est constaté a posteriori par les praticiens qui exploitaient ces sous-requêtes.

Sources :
- [Nectiv Digital, ChatGPT 5.4 Has Hidden Fan-Out Queries](https://nectivdigital.com/blog/chatgpt-5-4-has-hidden-fan-out-queries-you-can-still-get-them-via-the-api-python-script-included)
- [Little Green Agency, ChatGPT Has Hidden Its Fan-Out Queries](https://littlegreenagency.co.uk/blog/chatgpt-has-hidden-its-fan-out-queries-heres-how-to-get-them-back-with-n8n/)
- [Quolity, ChatGPT Search Query Extractor](https://quolity.ai/chatgpt-search-query-extractor/)

---

Draft SyntheticBrain. Rien n'a été envoyé.
