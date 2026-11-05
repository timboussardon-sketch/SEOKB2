---
date: 2026-10-01
pilier_info_du_jour: Recherche agentique
piliers_breves: [Actualité SEO, Actualité SEO]
format: digest
version: v1
---

# Algorithme — Édition du 1er octobre 2026

**Points capitaux**

- OpenAI DevDay 2026 (29 septembre) ouvre ChatGPT comme plateforme de distribution bidirectionnelle : agents persistants Dots côté utilisateur, plugin extensions et Marketplace de 32 partenaires côté éditeur.
- Pour un consultant SEO/GEO, la surface de choix se déplace encore d'un cran : page web → citation dans une réponse générative → agent persistant → plugin natif distribué par OpenAI.
- GPT-6.1 Sol à 2 USD/million de tokens en entrée et 10 USD/million en sortie, soit un cinquième des prix d'Astra, abaisse le coût unitaire d'un appel LLM pour un agent et rend plausibles des fan-outs plus larges par requête.
- Google September 2026 spam update : la fenêtre de déploiement annoncée atteint deux semaines, soit la plus longue des quatre spam updates de 2026.
- Search Central Live Deep Dive Europe à Barcelone (30 septembre – 2 octobre) : jour 2 aujourd'hui, consacré à l'indexation avancée, au rendering et au parsing JavaScript, par Gary Illyes et Cherry Prommawin.

---

## Info du jour — Recherche agentique

### ChatGPT devient une plateforme de distribution : ce que DevDay 2026 déplace pour un consultant SEO/GEO

**Les faits.** Le 29 septembre 2026, à Fort Mason à San Francisco, OpenAI a tenu son DevDay annuel. Le résumé officiel liste plus de vingt annonces, articulées autour de deux versants.

Côté utilisateur, Dots. OpenAI décrit Dots comme des agents persistants qui, selon la reprise de [Learnetto](https://learnetto.com/openai-devday-2026-announcements), « apprennent ce qui compte pour vous et gèrent les responsabilités courantes en votre nom ». Powered par le modèle Astra, les Dots se branchent, selon [benchlm.ai](https://benchlm.ai/blog/posts/openai-devday-2026), à « more than 4,000 apps » et opèrent avec des bornes d'accès définies par l'utilisateur. [Runtimewire](https://runtimewire.com/article/everything-openai-announced-at-the-devday-2026-keynote) ajoute qu'ils sont accessibles depuis ChatGPT, Slack et Teams, appels vocaux inclus. Disponible pour Pro et Business Premium.

Côté éditeur, plugin extensions et Marketplace OpenAI. Les plugin extensions, selon [runtimewire](https://runtimewire.com/article/everything-openai-announced-at-the-devday-2026-keynote), ajoutent des barres latérales et panneaux interactifs à ChatGPT, avec Figma et Photoshop démontrés sur scène. Le Marketplace OpenAI compte 32 partenaires initiaux. [Learnetto](https://learnetto.com/openai-devday-2026-announcements) les répartit en cinq segments (créativité, expérience client, juridique, cybersécurité, infrastructure de modèles). Les partenaires nommés par [runtimewire](https://runtimewire.com/article/everything-openai-announced-at-the-devday-2026-keynote) incluent Adobe, Figma, Sierra, Decagon, Salesforce, ServiceNow, Harvey, Legora, Palo Alto Networks, CrowdStrike et Baseten.

En parallèle, GPT-6.1 Sol. Nouvelle version du modèle économique, décrite par [benchlm.ai](https://benchlm.ai/blog/posts/openai-devday-2026) comme offrant « near-Astra capability at a fifth of the price » : 2 USD par million de tokens en entrée, 10 USD en sortie, avec, selon [learnetto](https://learnetto.com/openai-devday-2026-announcements), 95 % de réduction sur les tokens d'entrée mis en cache. Un palier de vitesse Ultrafast, annoncé à 300 tokens par seconde, livre jusqu'à 8× la cadence standard dans Codex et jusqu'à 6× dans l'API. Enfin, un abonnement Pro 500 à 500 USD par mois.

À noter en marge : OpenAI a renoncé à publier GPT-6.1 Astra ce jour-là, en citant des réserves de sécurité, et a mis en avant Sol à sa place. L'information est reprise par [learnetto](https://learnetto.com/openai-devday-2026-announcements).

**Ce que ça déplace pour un consultant SEO/GEO.** Cinq lectures opérationnelles.

Premièrement, la surface de choix pour un acheteur, un internaute ou un donneur d'ordre interne se déplace encore d'un cran. On avait déjà le ranking web, puis la citation dans une réponse générative (AI Overviews, AI Mode, ChatGPT, Perplexity), puis l'achat via un agent de checkout. S'y ajoute maintenant un agent persistant tiers (Dot) qui garde une mémoire et choisit un outil ou un marchand dans une liste de 4 000 et une distribution native en plugin dans l'interface où la requête part. Ces deux circuits ne sont pas interchangeables avec un ranking web.

Deuxièmement, être retenu par un Dot relève d'une mécanique différente d'être cité par ChatGPT. Un Dot a une mémoire persistante, consomme des APIs d'applications, applique des bornes définies par l'utilisateur, et peut privilégier l'application que l'utilisateur a déjà installée. Pour un marchand ou un éditeur, c'est une couche de « choix outil » qui s'ajoute à la couche « choix source dans la réponse ». Les outils de mesure de visibilité GEO (Peec AI, Otterly, Profound, Semrush AI Visibility, Ahrefs Brand Radar) ne couvrent pas, à ce jour, cette couche.

Troisièmement, le plugin extension est un déplacement net de surface. Le produit n'est plus une page web citée, c'est une interface interactive à l'intérieur de ChatGPT, installée par le Marketplace. Pour un consultant Product-Led SEO, la question se dédouble : optimiser la page web qui vit en search, et conditionner la distribution plugin, qui demande une admission au Marketplace OpenAI, une architecture d'app native à ChatGPT et une maintenance d'intégration. Ce ne sont pas les mêmes compétences.

Quatrièmement, l'arrivée de Sol à un cinquième du prix d'Astra abaisse le coût unitaire d'un appel LLM d'un agent. Combiné à l'Ultrafast à 300 tokens par seconde, ça rend plausibles des fan-outs plus larges par requête utilisateur (plus de sous-requêtes dérivées, plus d'appels d'outils par étape). Pour un éditeur de contenu, ça pousse dans la direction d'une sélection par un agent qui compare davantage de sources et de ressources avant de choisir.

Cinquièmement, la couche « marché de plugins » installée par OpenAI (32 partenaires au départ, dont Adobe, Figma, Salesforce, Palo Alto Networks, CrowdStrike) est un pattern connu d'App Store. Elle introduit, dans la distribution logicielle via ChatGPT, les questions classiques d'un marché : critères d'admission, politique de ranking interne au Marketplace, part des revenus, exclusivités. Ces questions, OpenAI n'y a pas répondu publiquement à ce jour.

**Réserves.** Trois réserves à tenir.

Les sources exploitées pour ce run sont des reprises éditoriales, pas la vidéo du keynote ni la transcription officielle. Le billet de recap d'OpenAI (openai.com/index/devday-2026-recap/) retourne 403 sur un fetch non authentifié ce matin. Les chiffres de prix, de partenaires et de capacités de Dots sont corroborés sur [learnetto](https://learnetto.com/openai-devday-2026-announcements), [benchlm.ai](https://benchlm.ai/blog/posts/openai-devday-2026) et [runtimewire](https://runtimewire.com/article/everything-openai-announced-at-the-devday-2026-keynote), mais les verbatim « ipsissima verba » d'Altman n'y figurent pas et ne doivent donc pas être inventés.

Aucune métrique d'adoption de Dots, de Marketplace OpenAI ou de plugin extensions n'a été publiée au jour de l'édition. Les mécaniques décrites ouvrent un déplacement plausible de surface, pas un fait de résultat.

Enfin, un plugin extension et un Dot sont des produits OpenAI. La portée du déplacement dépend du maintien de ChatGPT comme interface dominante parmi les moteurs génératifs. Les mesures publiques de parts d'usage en recherche IA restent partagées entre ChatGPT, Google AI Mode / AI Overviews, Perplexity, Gemini et Claude ; aucune n'écrase les autres.

**Lien doctrine.** Les trois concepts du vault les plus directement articulés par ces annonces sont [[agentic-search]], [[product-led-seo]] et [[test-substitution-llm]]. La fiche agentic-search isole la couche « choix d'outil par un agent persistant » comme variable à ne pas confondre avec la couche « choix de source par une réponse générative » ; les Dots d'OpenAI matérialisent cette couche de choix d'outil en consommateur grand public. La fiche product-led-seo pose le filtre du calculateur/simulateur/générateur comme surface de référencement ; les plugin extensions proposent une variante où le produit n'est plus la page web mais l'interface interactive distribuée au cœur de ChatGPT. La fiche test-substitution-llm interroge quand la page n'a plus de raison d'être parce que le LLM peut rendre la fonction en direct ; une interface plugin installée dans ChatGPT est une forme de substitution plutôt qu'une page concurrente.

**Prédictions.**

- P-2026-10-01-1 — D'ici le 31 décembre 2026, au moins un outil de mesure de visibilité GEO (Peec AI, Otterly, Profound, Semrush AI Visibility, Ahrefs Brand Radar, Athena HQ) ajoute un champ ou une vue dédiée à la présence sur le Marketplace OpenAI, distinct de la présence en citation dans une réponse générative. Confiance 0,45.
- P-2026-10-01-2 — D'ici le 30 juin 2027, le Marketplace OpenAI dépasse 100 partenaires actifs, confirmant un pattern d'adoption rapide côté éditeur. Confiance 0,55.
- P-2026-10-01-3 — D'ici le 31 décembre 2026, aucun marchand majeur ne publie publiquement un chiffre de conversions mesurées attribuable précisément à un Dot ou à un plugin extension, distinct d'une attribution à ChatGPT dans son ensemble. Confiance 0,55.

---

## Brève 1 — Actualité SEO

### Google September 2026 spam update : fenêtre de déploiement portée à deux semaines, la plus longue des quatre spam updates de 2026

Google a mis en route sa September 2026 spam update le mercredi 24 septembre à 09h15 PDT. L'annonce officielle sur le [Search Status Dashboard](https://status.search.google.com/) indique une fenêtre de déploiement potentielle de deux semaines. [PPC Land](https://ppc.land/googles-september-spam-update-gets-a-two-week-rollout-its-longest-yet/) note que c'est, à ce jour, la plus longue fenêtre annoncée des quatre spam updates confirmés en 2026, et compare avec les précédentes : l'update de mars avait fini en 19 heures et demie, celle de juin en 48 heures, celle d'août en trois jours. Toutes avaient été présentées avec une fenêtre de « quelques jours ». Pour la September 2026, la fenêtre poussée à deux semaines porte la clôture attendue autour du 8 octobre.

Google n'a publié ni billet dédié, ni liste de signaux ciblés, ni part de requêtes affectées. [Techwyse](https://www.techwyse.com/google-begins-rolling-out-september-2026-spam-update-fourth-of-the-year-two-week-rollout-expected/) et [Search Engine Journal](https://www.searchenginejournal.com/google-september-2026-spam-update/590828/) relaient le même constat : la communication se limite à la fenêtre de déploiement et au périmètre global, toutes langues et toutes régions.

Lecture opérationnelle pour un consultant SEO : une fenêtre de deux semaines rend inopérante la lecture de volatilité au jour le jour. Les mesures de visibilité (Sistrix, Semrush Sensor, Mozcast, AccuRanker) ne pourront attribuer un effet à l'update qu'après la fin annoncée, soit à partir du 8-11 octobre.

Réserve : la fenêtre annoncée est une borne haute, pas une mesure. Les clôtures effectives des trois updates précédentes avaient été plus courtes que leur fenêtre théorique.

---

## Brève 2 — Actualité SEO

### Search Central Live Deep Dive Europe à Barcelone, jour 2 aujourd'hui, indexation avancée

Le Search Central Live Deep Dive Europe 2026 se tient à Barcelone du 30 septembre au 2 octobre. Le programme officiel publié par Gary Illyes et Cherry Prommawin sur le [blog Google Search Central](https://developers.google.com/search/blog/2026/07/search-central-live-deep-dive-europe-2026) découpe l'événement en trois jours. Jour 1, le 30 septembre : « The Foundation and Crawling », démarrage sur les systèmes search et IA, mécaniques de crawl, exercice GSC pour diagnostiquer un problème de crawl ou de découverte. Jour 2, aujourd'hui, 1er octobre : « Advanced Indexing and Beyond », rendering, parsing d'éléments non texte et JS-lourd, point d'entrée de l'IA dans le pipeline d'indexation. Jour 3, le 2 octobre : « Serving, ranking, and uncovering content trends… and some AI ».

[PPC Land](https://ppc.land/google-picks-barcelona-over-five-rivals-for-first-eu-search-deep-dive/) rappelle que c'est la première édition européenne de ce format Deep Dive, après l'édition initiale à Bangkok en juillet 2025, et que Barcelone a été retenue à l'issue d'un vote public de 18 jours entre six villes candidates.

Lecture opérationnelle : le format Deep Dive est séquencé pour que les participants construisent une compréhension incrémentale du pipeline search Google, du crawling au serving. Pour un consultant, les éléments techniques intéressants des reprises publiques attendues (Aleyda Solis, Barry Schwartz, JC Chouinard, Cyrus Shepard, Lily Ray) tomberont au fil des trois jours, pas en bloc. Il faut attendre la fin de l'événement pour une lecture consolidée.

Réserve : au moment où cette édition se publie, le jour 2 n'a pas encore livré ses sessions publiques. Les reprises verbatim des conférenciers tiers ne sont pas disponibles. Le programme ci-dessus est la seule source officielle à ce stade.

---

*Édition rédigée par SyntheticBrain le 2026-10-01 au matin. Rien n'est envoyé.*

## Sources principales

- [OpenAI DevDay 2026 recap](https://openai.com/index/devday-2026-recap/) — site OpenAI (billet officiel, 403 au fetch non authentifié)
- [Learnetto — OpenAI DevDay 2026 announcements](https://learnetto.com/openai-devday-2026-announcements)
- [benchlm.ai — OpenAI DevDay 2026 Announcements: Dots, GPT-6.1 Sol, Ultrafast, and Codex Cloud](https://benchlm.ai/blog/posts/openai-devday-2026)
- [runtimewire — Everything OpenAI announced at the DevDay 2026 keynote](https://runtimewire.com/article/everything-openai-announced-at-the-devday-2026-keynote)
- [Axios — The 5 biggest announcements from OpenAI's blockbuster AI conference](https://www.axios.com/2026/09/29/openai-dev-day-2026-dots-space-sol)
- [CNBC — OpenAI DevDay 2026 recap](https://www.cnbc.com/2026/09/29/openai-devday-2026-live-updates.html)
- [PPC Land — Google's September spam update gets a two-week rollout, its longest yet](https://ppc.land/googles-september-spam-update-gets-a-two-week-rollout-its-longest-yet/)
- [Techwyse — Google begins rolling out September 2026 spam update](https://www.techwyse.com/google-begins-rolling-out-september-2026-spam-update-fourth-of-the-year-two-week-rollout-expected/)
- [Search Engine Journal — Google September 2026 spam update](https://www.searchenginejournal.com/google-september-2026-spam-update/590828/)
- [Google Search Central Blog — Search Central Live Deep Dive Europe 2026](https://developers.google.com/search/blog/2026/07/search-central-live-deep-dive-europe-2026)
- [PPC Land — Google picks Barcelona over five rivals for first EU search Deep Dive](https://ppc.land/google-picks-barcelona-over-five-rivals-for-first-eu-search-deep-dive/)
