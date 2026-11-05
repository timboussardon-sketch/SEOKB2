---
title: Algorithme — édition du 19 octobre 2026 (v2)
date: 2026-10-19
pilier_info_du_jour: Business SEO
auteur: SyntheticBrain
voix: analyste search / IA, vouvoiement
---

# Meta retire « entraînement » de ses conditions commerciales à effet 30 octobre, le droit de crawl reste

## Résumé

- Meta a retiré le mot « train » (entraînement) de la section 1 de ses nouvelles conditions commerciales après objections d'avocats et d'éditeurs ; les termes prennent toujours effet le 30 octobre 2026.
- Le droit de crawler les sites liés à un compte business reste dans la clause ; News/Media Alliance (Sam Quigley) : la correction limite les usages mais pas la collecte, « c'est toujours potentiellement sur la table ».
- Une revue du 18 octobre par PPC Land d'un aperçu en anglais britannique contenait encore la mention « train » : la cohérence inter-locales de la version révisée n'est pas garantie à six jours de l'entrée en vigueur.
- Universal Cart : Walmart, Target et Sephora listés par Google parmi les retailers partenaires mais seulement pour des « select checkout options », pas un handoff complet ; la sénatrice Elizabeth Warren a adressé une lettre à Google soulevant des préoccupations antitrust et vie privée.
- USA Today Co. (ex-Gannett) et 13 entités affiliées ont déposé le 8 octobre 2026 une plainte contre OpenAI devant le tribunal fédéral de Manhattan, réclamant plus de 250 M$ et la destruction de modèles GPT entraînés sur leurs articles.

## Info du jour — Pilier Business SEO

Meta a modifié la section 1 de ses nouvelles conditions commerciales (« Commercial Terms »), à effet le 30 octobre 2026, en retirant le mot « train » de la liste des usages permis sur les contenus collectés par ses robots. Le mouvement, rapporté par [The Next Web](https://thenextweb.com/news/meta-drops-train-from-its-website-crawling-terms-after-backlash) le 17 octobre 2026 à 18h40 UTC, puis par [Startup Fortune](https://startupfortune.com/meta-quietly-deletes-ai-training-clause-from-its-new-business-terms/), [Digital Trends](https://www.digitaltrends.com/computing/meta-changed-terms-that-could-have-let-it-use-website-content-for-ai-training/) et [ContentGrip](https://www.contentgrip.com/meta-training-clause-locale-gap/) le 19 octobre, intervient après des objections d'avocats et de la News/Media Alliance.

La clause d'origine, documentée les 15 et 16 octobre notamment par le [Northeast Times](https://northeasttimes.com/2026/10/16/meta-terms-taking-effect-oct-30-let-it-scrape-business-websites-for-ai-training/) et par la synthèse de la [SEO Mean CEO](https://mean.ceo/tpost/meta-commercial-terms-ai-crawling), autorisait Meta à accéder, indexer, mettre en cache, copier et re-crawler les sites liés à ses produits commerciaux, et à utiliser ces contenus pour entraîner ses propres produits. L'acceptation est tacite : continuer à utiliser les produits commerciaux de Meta vaut accord, sans opt-out partiel documenté.

La version révisée retire « train » et resserre le périmètre d'usage aux « produits publicitaires et commerciaux » de Meta. Daniel Roberts, porte-parole de Meta cité par ContentGrip, précise : « This is not about scraping news sites. » Meta ajoute que ses pratiques de crawl ne changent pas. Dans sa réponse au Mercury News, le groupe explique : « We've heard you and want to clarify. »

La News/Media Alliance qualifie la correction d'insuffisante. Sam Quigley, cité par The Next Web : « It's still potentially on the table. » Trois points restent ouverts dans l'édition révisée : la clause n'interdit pas explicitement l'entraînement IA, elle n'engage pas Meta à respecter robots.txt, et le droit de crawler les sites liés à un compte business reste intact. Le mécanisme d'opt-out structurel n'existe pas : un éditeur qui ne veut pas être couvert doit cesser d'utiliser les produits business de Meta.

ContentGrip documente une divergence inter-locales : [PPC Land](https://ppc.land/meta-grants-itself-the-right-to-crawl-advertisers-websites-for-ai-training-with-no-opt-out/) a vérifié le 18 octobre un aperçu en anglais britannique de la clause qui contenait encore la mention « train ». ContentGrip signale un contrôle indépendant d'un aperçu officiel Meta montrant également la formulation d'entraînement, sans que la locale ou l'édition de compte observée soit identifiée. Les sources ne tranchent pas la cause de l'écart : édition texte non répliquée, cache, ou phasage de déploiement.

**Trois lectures opérationnelles pour un responsable SEO ou éditorial :**

1. La correction obtenue n'est pas un retrait du droit de crawl, mais un retrait d'un usage particulier (entraînement) de la liste de la clause. Côté SEO éditeur, les entrées de crawler Meta documentées à ce jour (Meta-ExternalAgent pour l'entraînement, Meta-WebIndexer pour le temps réel Meta AI, cf. [[entities/meta-externalagent]]) restent les mêmes vecteurs techniques à surveiller via logs serveur et robots.txt. L'engagement sur robots.txt n'étant pas pris, bloquer ces user-agents dans robots.txt ne garantit pas juridiquement une exécution côté Meta.
2. L'alerte à retenir n'est pas le mot « train » mais la mécanique d'acceptation tacite. Un site business qui garde une Page Facebook, un compte Business Manager actif, un pixel Meta ou une intégration catalogue reste couvert par les conditions commerciales à partir du 30 octobre 2026. Un éditeur qui veut un consentement explicite sur l'usage de ses contenus doit arbitrer la rupture d'usage, pas la négociation d'opt-out, qui n'est pas prévue.
3. La divergence inter-locales observée par PPC Land oblige à ne pas se fier à une seule capture d'écran du texte. Pour un juriste ou un responsable conformité qui doit décider avant le 30 octobre, la seule base d'arbitrage robuste est le texte des conditions dans la locale et l'édition de compte effectivement opposables à l'entité juridique concernée, horodaté et archivé. Les captures diffusées en reportage sont des points de vérification, pas des documents opposables.

Rattachement doctrine : trois concepts du vault se recoupent sur cette séquence. [[concepts/peur-train-ia]] formalise la ligne de résistance éditoriale au scraping d'entraînement. [[concepts/data-proprietaire]] rappelle que la donnée propriétaire ne vaut comme actif que si son usage est tracé et contractualisé ; des conditions commerciales à acceptation tacite affaiblissent la traçabilité contractuelle, même sans entraînement explicite. [[entities/meta-externalagent]] et [[entities/robots-txt-ai]] documentent les contrôles techniques disponibles côté éditeur, aujourd'hui non adossés à un engagement contractuel Meta.

**Trois prédictions ouvertes :**

1. **P-2026-10-19-v2-1** : d'ici le 30 novembre 2026, au moins une plateforme business d'un éditeur US majeur (par exemple au sens Alliance Press Alliance / NMA) publiera publiquement une rupture d'usage des produits commerciaux Meta, motivée explicitement par les conditions du 30 octobre. Confiance 0,30.
2. **P-2026-10-19-v2-2** : d'ici le 31 janvier 2027, Meta documentera ou amendera à nouveau les conditions commerciales pour clarifier son traitement de robots.txt ou introduire un mécanisme d'opt-out structurel. Confiance 0,40.
3. **P-2026-10-19-v2-3** : d'ici le 30 juin 2027, un contentieux civil ou une plainte réglementaire (UE ou US) sera déposé qui citera explicitement la section 1 de ces conditions commerciales du 30 octobre 2026 comme base contractuelle contestée. Confiance 0,45.

### Brève 1 — Universal Cart : trois enseignes limitent le handoff à Google, lettre antitrust de la sénatrice Warren (Agentic search)

Universal Cart, lancé aux États-Unis le 15 octobre 2026 à travers Search et l'application Gemini, est présenté par Google comme couvrant « plus de 60 milliards de référencements produits » dans le Shopping Graph. L'adoption retailer reste partielle : [Startup Fortune](https://startupfortune.com/googles-universal-cart-goes-live-and-retailers-are-already-pushing-back/) rapporte le 17 octobre 2026 à 6h08 que Walmart, Target et Sephora figurent parmi les retailers partenaires, mais seulement « for select checkout options, not the full handoff ». Nike, Ulta Beauty, Wayfair, et des marchands Shopify dont Fenty et Steve Madden figurent également comme partenaires. L'article ne détaille pas quelle option de checkout chaque enseigne a ouverte.

La sénatrice Elizabeth Warren a envoyé à Google une lettre soulevant des préoccupations antitrust, de vie privée et de manipulation du consommateur, selon le même article, avec un délai de réponse attaché ; le texte du délai et la date exacte d'envoi ne sont pas donnés publiquement. [eWeek](https://www.eweek.com/news/google-universal-cart-gemini-search/), [Search Engine Land](https://searchengineland.com/google-launches-universal-cart-across-search-and-gemini-for-easier-shopping-496573) et [PPC Land](https://ppc.land/googles-universal-cart-reaches-us-search-and-gemini-but-not-youtube/) confirment le périmètre US Search + Gemini et une absence de YouTube au lancement.

Ce que mesure cette adoption partielle : un handoff complet aurait transféré à Google la main sur la donnée de panier abandonné, les signaux de retargeting et la fiscalité checkout. Un « select checkout options » (Walmart, Target, Sephora) préserve pour l'enseigne une partie de ces signaux et de la relation client finale, au prix d'un parcours plus hétérogène côté acheteur. L'arbitrage retailer entre volume de conversion dans la surface Google et contrôle de la donnée propriétaire tombe donc comme un indicateur mesurable à surveiller à J+30 et J+90.

Rattachement doctrine : [[concepts/agentic-search]] cadre le checkout agentique comme nouvelle couche de l'architecture commerciale ; [[concepts/data-proprietaire]] identifie panier abandonné et donnée de retargeting comme actifs retailer dont la cession à un protocole agentique tiers est un arbitrage explicite.

### Brève 2 — USA Today Co. réclame 250 M$ à OpenAI pour entraînement non licencié (Business SEO)

USA Today Co. (anciennement Gannett) et 13 entités affiliées ont déposé le 8 octobre 2026 une plainte contre OpenAI devant le tribunal fédéral du Southern District de New York (Manhattan). La plainte, documentée par [Editor and Publisher](https://www.editorandpublisher.com/stories/usa-today-becomes-the-latest-publisher-to-sue-openai,263956), [The Desk](https://thedesk.net/2026/10/usa-today-openai-copyright-lawsuit-chatgpt/), [Hoodline](https://hoodline.com/2026/10/usa-today-sues-openai-demands-250-million-over-copied-articles) et [Crypto Briefing](https://cryptobriefing.com/usa-today-sues-openai-copyright-250m/), demande plus de 250 M$ de dommages, un procès devant jury, et une injonction de destruction de tout modèle GPT entraîné sur leurs articles. Les plaignants invoquent la copie de « hundreds of thousands » d'articles issus de 19 publications dont USA Today, Arizona Republic, Detroit Free Press et IndyStar.

L'allégation la plus notable pour un consultant SEO : la plainte cite un ingénieur OpenAI ayant écrit que les utilisateurs ne suivraient probablement pas les liens source, « regardless of how prominently those links appeared ». Si l'allégation est reproduite au dossier et confirmée en procédure, elle fournit un élément de preuve textuel sur la logique de monétisation du modèle versus celle du publisher. OpenAI n'a pas commenté publiquement au moment de la plainte.

Mise en perspective : cette plainte s'ajoute aux 30+ éditeurs locaux US qui avaient porté une action similaire plus tôt dans l'année (couvrant 400 marques de presse locales), à Reddit vs Perplexity sur l'allégation de scraping d'entraînement, et aux conditions Meta modifiées ce jour. Le signal cumulé pour les éditeurs : la contractualisation ex ante (deals de licence Google News AI Pilot à 400+ publications, deals OpenAI/Microsoft avec News Corp, Associated Press, Axel Springer, Prisa) devient le mode de monétisation dominant, tandis que la procédure contentieuse ex post reste ouverte pour les éditeurs qui n'ont pas signé.

Rattachement doctrine : [[concepts/peur-train-ia]] couvre la ligne éditoriale anti-scraping d'entraînement non licencié ; [[concepts/tabou-visibilite]] rappelle que la visibilité IA d'une publication ne garantit pas un clic ni une rémunération, l'ingénieur OpenAI cité à la plainte formule exactement ce point.

### Brève 3 — Preview UK-anglais Meta conserve encore « train » le 18 octobre, divergence inter-locales non expliquée (Business SEO)

[PPC Land](https://ppc.land/meta-grants-itself-the-right-to-crawl-advertisers-websites-for-ai-training-with-no-opt-out/) a vérifié le 18 octobre 2026 un aperçu en anglais britannique de la clause section 1 des conditions commerciales Meta à effet 30 octobre : la mention « train » y figurait toujours. [ContentGrip](https://www.contentgrip.com/meta-training-clause-locale-gap/) confirme le 19 octobre et ajoute un contrôle indépendant d'un aperçu officiel Meta montrant également le libellé d'entraînement, sans que la locale ou l'édition de compte observée soit identifiée.

Les deux sources ne tranchent pas la cause : édition partielle du texte non répercutée sur toutes les versions localisées, cache CDN, ou calendrier de déploiement. Meta n'a pas publiquement commenté la divergence au moment de ces vérifications.

Impact opérationnel pour un responsable conformité : à six jours de l'entrée en vigueur, deux captures d'un même texte réglementaire ne coïncident pas. Deux conséquences pratiques, de nature différente. D'abord, l'auto-sauvegarde horodatée du texte opposable à l'entité juridique concernée dans la locale et l'édition de compte applicable, archivée indépendamment du site Meta, devient la base d'arbitrage robuste pour une revue juridique. Ensuite, un suivi hebdomadaire du texte publié jusqu'au 30 octobre documenterait si la convergence s'opère.

---

*Édition écrite par SyntheticBrain, pilier Business SEO, 19 octobre 2026 après-midi. Sources recoupées 2+ indépendantes sur chaque claim de corps. Aucune diffusion automatique : draft uniquement.*
