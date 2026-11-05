---
type: revue-presse
title: "OpenAI écrit que robots.txt peut ne pas s'appliquer à ChatGPT-User, Gemini 3.7 Flash arrive dans AI Mode, une mesure indique un facteur 33 quand une marque figure dans la requête interne de ChatGPT"
date: 2026-08-15
edition: 2026-08-15-revue-presse-v2
tags: [algorithme, revue-presse, seo, ia, geo, agentic-search, syntheticbrain]
pilier_info_du_jour: Recherche agentique
piliers_breves: [GEO, GEO]
status: draft
---

# OpenAI écrit que robots.txt peut ne pas s'appliquer à ChatGPT-User, Gemini 3.7 Flash arrive dans AI Mode, une mesure indique un facteur 33 quand une marque figure dans la requête interne de ChatGPT

**À retenir en 15 secondes**

- OpenAI écrit dans sa documentation crawler que ChatGPT-User n'est pas soumis à robots.txt quand l'action est initiée par un utilisateur, position primaire sortie publiquement le 14 août 2026 via [Search Engine Journal](https://www.searchenginejournal.com/openai-says-robots-txt-may-not-apply-to-chatgpts-fetch-bot/585864/).
- Le rapport TollBit *State of the Bots* pour le premier semestre 2026, cité le 14-15 août, mesure 15 pct des fetches d'agents IA européens sur des URL explicitement interdites, avec ChatGPT-User, Bytespider et Youbot touchant chacun près de la moitié des sites européens qui les listent.
- Google a déployé Gemini 3.7 Flash dans AI Mode le 14 août 2026 pour les abonnés AI Pro et Ultra en anglais, à demi-tarif du modèle 3.6 Flash, avec un objectif publié de meilleure exécution des instructions dans les réponses génératives.
- Une mesure publiée par Suganthan Mohanadasan le 14 août 2026 indique un taux de citation de 68.9 pct pour les marques que ChatGPT écrit lui-même dans ses requêtes internes avant fetch, contre 2.1 pct pour les marques uniquement récupérées ensuite, soit un facteur 33 sur un échantillon de 57 conversations et 3 554 pages fetch.

---

## Info du jour — Recherche agentique : OpenAI publie sa position sur robots.txt pour ChatGPT-User, TollBit chiffre le contournement effectif en Europe

Le 14 août 2026, Matt G. Southern écrit sur [Search Engine Journal](https://www.searchenginejournal.com/openai-says-robots-txt-may-not-apply-to-chatgpts-fetch-bot/585864/) que la documentation crawler d'OpenAI (developers.openai.com/api/docs/bots) contient désormais la phrase : ChatGPT-User visite une page quand un utilisateur ChatGPT pose une question, et parce que ces actions sont initiées par un utilisateur, les règles robots.txt peuvent ne pas s'appliquer. La formulation est signée par OpenAI dans sa propre doc technique, elle n'est pas une lecture externe. C'est la première fois qu'un éditeur d'agent IA écrit noir sur blanc qu'un de ses bots de fetch n'est pas gouverné par le protocole standard de contrôle d'accès pour les crawlers.

Le lendemain, le 15 août 2026, [PPC Land](https://ppc.land/15-of-ai-page-fetchers-in-europe-reached-disallowed-urls-tollbit-finds/) reprend la position d'OpenAI et la met en regard du rapport *State of the Bots* de TollBit pour le premier semestre 2026. Trois chiffres sortent de ce rapport, corroborés dans les deux couvertures :

- 15 pct des fetches d'agents IA identifiés sur des sites européens atterrissent sur des URL que ces sites ont explicitement interdites dans leur robots.txt.
- ChatGPT-User, Bytespider (ByteDance) et Youbot touchent chacun près de 50 pct des sites européens qui les listent nommément dans robots.txt.
- Asymétrie régionale : 9 pct des sites européens interdisent Claude-User contre 26 pct des sites nord-américains ; 13 pct des sites européens interdisent Perplexity-User contre 26 pct des sites nord-américains. Cette asymétrie règle-t-elle ce qui est réellement mesuré ? Non, elle contextualise seulement l'ampleur du problème.

Un chiffre historique cité par [Mediacopilot](https://mediacopilot.ai/ai-scrapers-bypassing-publisher-protections/) sur le rapport TollBit précédent (données quatrième trimestre 2025, publié début 2026) indiquait déjà un taux de non-conformité de 42 pct pour ChatGPT-User. Le rapport actuel confirme et détaille l'échelle du phénomène, tout en documentant l'écart entre la doctrine officielle du protocole robots.txt et la pratique côté agents IA.

**Ce que cette édition ajoute (pour un consultant SEO qui suit un portefeuille de sites éditeurs)**. Trois éléments qui n'étaient pas encore consolidés jusqu'ici.

D'abord, la position d'OpenAI transforme une controverse empirique en position doctrinale explicite. Avant le 14 août, on pouvait argumenter que le taux de non-conformité était un défaut d'implémentation. Après le 14 août, on doit argumenter avec un éditeur d'agent IA qui écrit dans sa doc que le protocole ne s'applique pas dans le cas où un utilisateur pose la question. Le débat change de nature : ce n'est plus un débat technique, c'est un débat de standards. La fiche [[concepts/agentic-search]] doit se voir ajouter une troisième catégorie de politique d'autorisation : la politique unilatérale de l'éditeur d'agent, à côté du blocage universel et de l'autorisation conditionnée à une identification vérifiable (Web Bot Auth, cloudflare.pay).

Ensuite, la mesure TollBit rend la politique visible côté serveur. Un consultant qui audite un éditeur peut mesurer, dans ses propres logs, la part de ses URL protégées effectivement fetchées par chaque agent IA nommé, et donc décider par chiffre. C'est la dimension mesure que [[concepts/metriques-visibilite-geo]] doit reconnaître comme distincte des dimensions apparition et densité de citation : la dimension politique d'accès mesurée en amont de toute citation. La brève 08-14 morning sur Microsoft Clarity avait déjà documenté cette dimension ; le rapport TollBit y ajoute le contrepoint mesuré côté agents.

Enfin, la mécanique change l'arbitrage éditeur. [[concepts/arbitrage-plateforme-publication]] disait : publier là où Google envoie le clic. Le cas OpenAI-robots.txt ajoute une couche : ne pas seulement choisir la plateforme d'origine du trafic, mais aussi la politique d'accès des agents IA au contenu, sachant que le blocage déclaratif seul ne suffit plus. La combinaison utile n'est pas robots.txt seul, c'est robots.txt + identification cryptographique (Web Bot Auth, cf. édition 06-06 sur le draft IETF Cloudflare-Google) + éventuellement une politique payante (Cloudflare pay-per-crawl, HTTP 402).

**Ce qu'on ne sait pas encore**. Le rapport TollBit ne publie pas la taille exacte de l'échantillon de sites européens sondés (indiquée seulement comme « sites listant les bots »), ni la méthodologie de détection des bots (fingerprint IP, user-agent, chaîne comportementale). OpenAI n'a pas explicité si la formulation « peuvent ne pas s'appliquer » vaut engagement, dérogation partielle ou reconnaissance d'un fait observé. La couverture presse actuelle est mono-primaire (rapport TollBit) et deux secondaires indépendants (SEJ et PPC Land) ; une reprise par une autorité tierce (CMA, Presse Gazette, News/Media Alliance) transformerait le sujet en dossier de politique publique.

**Trois prédictions vérifiables datées**.

- P-2026-08-15-v2-1 : OpenAI publie une mise à jour de sa documentation crawler qui clarifie ou révise la formulation « robots.txt may not apply » à ChatGPT-User avant le 31 mars 2027 (probabilité 0.30).
- P-2026-08-15-v2-2 : Un régulateur européen (CMA, Autorité de la concurrence, Bundeskartellamt) ou une association d'éditeurs (News/Media Alliance, Digital Content Next, APIG) cite le rapport TollBit *State of the Bots* premier semestre 2026 dans un texte de saisine, position officielle ou consultation publique avant le 31 mars 2027 (probabilité 0.45).
- P-2026-08-15-v2-3 : Un second rapport indépendant de mesure de non-conformité robots.txt par agents IA, publié par une organisation autre que TollBit avec échantillon ≥ 500 sites, avant le 31 décembre 2026 (probabilité 0.55).

---

## Brève 1 — GEO : Google déploie Gemini 3.7 Flash dans AI Mode le 14 août 2026 pour les abonnés AI Pro et Ultra en anglais

Google a introduit Gemini 3.7 Flash dans AI Mode le 14 août 2026, trois semaines après avoir annoncé Gemini 3.6 Flash le 21 juillet 2026. La bascule concerne les abonnés AI Pro et AI Ultra en anglais, avec un déploiement global couvrant les régions où AI Mode est disponible. Sources cross-source : [Search Engine Land](https://searchengineland.com/gemini-3-7-flash-rolling-out-in-google-search-485058), [Search Engine Journal](https://www.searchenginejournal.com/google-brings-gemini-3-7-flash-to-ai-mode-in-search/585923/), [9to5Google](https://9to5google.com/2026/08/13/gemini-3-7-flash-launch/), et [Bloomberg](https://www.bloomberg.com/news/articles/2026-08-13/google-debuts-new-gemini-flash-while-top-ai-model-still-delayed).

Deux faits objectifs sortent de la couverture.

D'abord, le tarif introductif est de 0.75 USD par million de tokens d'entrée et 3.75 USD par million de tokens de sortie via l'API, soit la moitié du tarif du modèle 3.6 Flash au lancement. Cette baisse tarifaire réduit le coût unitaire d'exécution des agents IA construits sur Gemini Flash, ce qui recoupe la mécanique documentée dans la brève du 15 juin 2026 sur Claude Agent SDK où Anthropic avait au contraire relevé les coûts effectifs par utilisateur.

Ensuite, Google communique un gain « instruction-following » et « intent-understanding » dans AI Mode. C'est une revendication éditoriale, pas un chiffre indépendant. Un consultant GEO doit surveiller si le passage de 3.6 à 3.7 Flash déplace le pattern de citation dans AI Mode, en particulier sur les surfaces déjà mesurées : Preferred Sources (édition 06-07), Highly Cited (édition 06-07), et hidden pipelines de query fan-out (éditions 07-09 et 09 juillet). La question ouverte est de savoir si Google mesure et publiera à terme un delta de citation par surface entre les modèles Flash.

**Ce qu'on ne sait pas encore**. Ni SEJ ni SEL ne publient de mesure indépendante du delta de citation entre 3.6 et 3.7 Flash dans AI Mode. Google n'annonce pas de date pour le déploiement en français ou en dehors de la sphère anglophone. Bloomberg précise que Gemini 3.5 Pro reste retardé, sans calendrier public. La prédiction utile serait donc : quel sera le premier verticale ou site à documenter publiquement un changement mesuré de citation entre Flash 3.6 et Flash 3.7 ?

---

## Brève 2 — GEO : Suganthan Mohanadasan publie une mesure indiquant un facteur 33 entre les marques pré-écrites par ChatGPT dans ses requêtes internes et les marques uniquement récupérées ensuite

Le 14 août 2026, Suganthan Mohanadasan publie sur [son blog](https://suganthan.com/blog/chatgpt-decides-before-it-searches/) et sur [Search Engine Journal](https://www.searchenginejournal.com/chatgpt-already-knows-who-itll-recommend-before-it-searches/585162/) une mesure qui étend son étude de juillet 2026 sur les hidden pipelines de ChatGPT (couverte le 09 juillet 2026, brève GEO Green + Mohanadasan). L'objet de la mesure : le champ `search_queries` (renommé début août 2026, anciennement `search_model_queries`) qui contient les requêtes internes que ChatGPT construit avant de fetcher le web.

Résultats mesurés :

- Échantillon : 57 conversations, 3 554 pages fetch, période 24-25 juillet 2026, compte Dubai, méthodologie basée sur l'analyse du trafic réseau via DevTools et lecture des JSON de réponse.
- Taux de citation des marques déjà écrites dans les requêtes internes de ChatGPT avant fetch : 68.9 pct.
- Taux de citation des marques uniquement récupérées ensuite (sans être pré-nommées dans une requête interne) : 2.1 pct.
- Ratio : facteur 33.
- Contexte : 21 des 27 conversations de test contenaient au moins une marque pré-écrite dans les requêtes internes de ChatGPT.
- Une observation complémentaire : le nombre de fan-outs (requêtes internes par réponse) est passé de 12 à 4 en captures après le renommage début août, ce qui suggère un changement dans la logique de query rewriting d'OpenAI.

**Statut du claim**. Fragile mono-analyste. Suganthan Mohanadasan a un historique dans les ledgers SyntheticBrain (études juillet 2026 sur les pipelines cachés, méthodologie DevTools/JSON) mais aucune reprise indépendante n'a encore mesuré le ratio 33 avec méthodologie comparable à date. À traiter comme piste de mesure, pas comme fait consolidé. Un consultant GEO qui priorise ses actions doit tester d'abord le pattern « marque déjà dans la requête interne » sur ses propres cas avant d'en tirer une doctrine de mise en marché.

**Doctrine touchée**. Si le résultat se reproduit, il consolide l'angle [[concepts/data-proprietaire]] : la présence d'une marque comme entité connue dans les représentations internes des modèles LLM (via corpus d'entraînement, mentions tierces multi-plateforme, données propriétaires publiées en format extractible) devient un prédicteur direct de citation, distinct de la performance sur la page fetch elle-même. C'est aussi une extension de [[concepts/agentic-search]] : l'agent qui décide sa requête avant de fetcher est un cas de pré-sélection avant retrieval, distinct de l'agent qui exécute une action après retrieval.

**Prédiction complémentaire à P-2026-08-15-v2-2**. P-2026-08-15-v2-4 : Une seconde étude indépendante (analyste ou éditeur d'outil GEO type Gauge, Profound, AthenaHQ, Semrush AI Visibility Index) reproduit un ratio de citation ≥ 10x entre marques pré-nommées dans les requêtes internes ChatGPT et marques uniquement fetchées avant le 31 mars 2027 (probabilité 0.55).

---

**Sources nouvelles ce run**. [tollbit.com](https://tollbit.com/blog/) via son rapport *State of the Bots* premier semestre 2026, entrée en explore avec trust initial 0.75 (source primaire de mesure de trafic IA côté serveur, méthodologie non entièrement publiée). [ppc.land](https://ppc.land) déjà connue et confirmée exploit (voir edition 08-14 morning et 08-15 morning), utilisée à nouveau ici comme source secondaire indépendante. La couverture Bloomberg de Gemini 3.7 Flash entre en explore avec trust initial 0.85 (source presse financière de référence, mais spécialisation search/IA à surveiller sur la fréquence de retour).

**Ce que cette édition ajoute par rapport au flux de couverture presse existant**. La position OpenAI sur robots.txt était éparse et implicite jusqu'ici ; le repérage d'une formulation explicite dans la doc technique change la nature de la conversation avec les éditeurs. Le rapport TollBit apporte une mesure côté serveur qui complète la mesure côté citation (Suganthan) et la mesure côté trafic (Microsoft Clarity Scrape-to-Referral, brève 08-14 morning). Les trois angles cumulés couvrent le cycle fetch → pré-sélection → citation → référence de trafic de façon plus complète qu'une couverture par angle isolé.

---

*Draft SyntheticBrain. Rien n'a été envoyé.*
