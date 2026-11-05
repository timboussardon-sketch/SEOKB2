---
type: revue-presse
title: "Algorithme — 14 octobre 2026 v2 : la bataille juridique de l'accès au contenu entre dans sa phase Washington"
date: 2026-10-14
version: v2-apres-midi
pilier_info_du_jour: Agentic Search
piliers_breves: [GEO / search IA, Business SEO, Actualité SEO]
tags: [agentic-search, stealth-bot-prohibition-act, hr-9915, news-media-alliance, previsible, cloudflare-pay-per-use, semrush, ai-crawl, mesure-visibilite]
created: 2026-10-14
updated: 2026-10-14
status: draft
---

# Algorithme — 14 octobre 2026 v2

## Résumé en tête

- Plus de 300 cadres de la presse (Condé Nast, Hearst, USA Today, Seattle Times) sont allés défendre à Washington le Stealth Bot Prohibition Act (H.R. 9915), déposé fin juillet 2026 par Foushee, Lee et Bilirakis à la commission Energy and Commerce.
- Le texte définit un stealth bot comme un robot qui accède à un site sans déclarer son identité ni son usage (indexation, entraînement IA, retrieval augmented generation). Sanction FTC jusqu'à 53 000 USD par infraction, action possible des procureurs généraux d'État, prise d'effet 180 jours après signature.
- La News/Media Alliance avance que les stealth bots représentent plus de 50 pour cent du trafic sur certains sites éditeurs. Chiffre lobby, non recoupé.
- Previsible publie une troisième édition de son étude trafic IA : 6,77 millions de sessions IA sur 166 sites, novembre 2024 à mai 2026. ChatGPT concentre 92,4 pour cent des référents LLM mesurables, Claude multiplié par 64, trafic AI Overviews et AI Mode supérieur à l'ensemble des assistants LLM réunis.
- Cloudflare bascule sa monétisation du crawl : Pay Per Crawl reste en bêta fermée, nouveau modèle Pay Per Use annoncé en août 2026, premier déploiement avec Ceramic.ai pour rémunérer les éditeurs quand leur contenu apparaît dans les réponses IA.

## Info du jour — Stealth Bot Prohibition Act : la presse américaine pousse un cadre fédéral sur l'accès des bots IA au contenu

Plus de 300 cadres d'éditeurs ont fait le déplacement à Washington ces dernières semaines pour défendre auprès du Congrès le Stealth Bot Prohibition Act, référencé H.R. 9915. Parmi les présents : des responsables de Condé Nast, Hearst Magazines, USA Today Co. et The Seattle Times ([Digiday, Condé Nast, Hearst among 300 media execs to push federal 'bad bots' bill on AI scraping](https://digiday.com/media/conde-nast-hearst-among-300-media-execs-to-push-federal-bad-bots-bill-on-ai-scraping/)).

Le texte a été déposé à la Chambre fin juillet 2026 par Valerie Foushee (D-NC), Laurel Lee (R-FL) et Gus Bilirakis (R-FL), et il est actuellement devant la commission Energy and Commerce ([AdExchanger, A new bill targets 'bad bots' that scrape websites without permission](https://www.adexchanger.com/ai/a-new-bill-targets-bad-bots-that-scrape-websites-without-permission) ; [News/Media Alliance, Stealth Bot Prohibition Act resource center](https://www.newsmediaalliance.org/digital-programs-and-advocacy/stealth-bot-prohibition-act-resource-center/)). La News/Media Alliance a salué publiquement l'introduction du texte et pilote la coordination des éditeurs ([News/Media Alliance, Alliance Applauds AI Bot Transparency Bill Introduction](https://www.newsmediaalliance.org/?p=18523)).

Ce que définit le texte, selon les relais de MediaPost et The Next Web : un stealth bot est un robot qui accède à un site sans déclarer qui il est et à quoi il sert. La déclaration doit couvrir la finalité (indexation de recherche, entraînement de modèles IA, retrieval augmented generation). Le texte interdit aussi l'usage de bots qui dégradent ou surchargent un site, et interdit à un bot IA de se faire passer pour un humain ([MediaPost, Bipartisan Bill Targets AI Stealth Bots](https://www.mediapost.com/publications/article/416769/bipartisan-bill-targets-ai-stealth-bots.html) ; [The Next Web, 300 publishers take their fight against AI stealth bots to Congress](https://thenextweb.com/news/publishers-congress-stealth-bot-prohibition-act-ai-scraping)).

Les sanctions prévues : la Federal Trade Commission peut rechercher des pénalités civiles jusqu'à 53 000 USD par infraction, ajustées de l'inflation. Les procureurs généraux d'État peuvent engager une action en justice pour obtenir des dommages pour les résidents de leur État. Les règles prendraient effet 180 jours après la signature du texte en loi. Le texte doit encore passer les examens de commission et les votes en séance plénière à la Chambre et au Sénat avant d'être présenté au Président ([AdExchanger](https://www.adexchanger.com/ai/a-new-bill-targets-bad-bots-that-scrape-websites-without-permission)).

Un texte équivalent, le Stealth Crawler Prohibition Act, a été adopté à New York en juin 2026, et sert de modèle au texte fédéral ([Digiday](https://digiday.com/media/conde-nast-hearst-among-300-media-execs-to-push-federal-bad-bots-bill-on-ai-scraping/)).

La News/Media Alliance avance que les stealth bots représentent plus de 50 pour cent du trafic sur certains sites éditeurs. Cette estimation est portée par la lobby elle-même et n'est pas recoupée dans les relais consultés.

Pour un professionnel SEO ou GEO, trois lectures opérationnelles se dégagent, chacune avec sa portée et sa réserve.

**Rattachement doctrine [[concepts/agentic-search]].** Le texte opère une distinction juridique explicite entre trois usages d'un même robot : indexation pour résultats de recherche, entraînement de modèle, retrieval augmented generation. C'est la première fois qu'une proposition fédérale américaine formalise cette distinction au niveau de l'intention déclarée. Un robot qui aujourd'hui est traité uniformément via robots.txt deviendrait, si le texte passe, un objet à trois statuts juridiques distincts selon ce qu'il affiche. Les fichiers de contrôle d'accès actuels (robots.txt, Google-Extended, GPTBot, ClaudeBot, Common Crawl) ne couvrent pas cette granularité en pratique. Pour un éditeur, l'exercice revient à mapper quels bots existants prétendent faire quoi, et à documenter l'écart avec ce qu'ils font réellement en pratique côté logs.

**Rattachement doctrine [[concepts/base-publique]] et [[concepts/data-proprietaire]].** L'enjeu de fond n'est pas la protection d'un contenu derrière un paywall, mais la contrepartie accordée pour un contenu publié librement et que la base publique de référence (ex-Google) remplace progressivement par la génération. Un cadre fédéral qui sanctionne le prélèvement non-déclaré ferme une porte juridique mais n'ouvre pas de contrepartie économique. Les éditeurs qui comptent sur ce texte doivent documenter en parallèle ce que leur contenu apporte en citations IA mesurables (via [[concepts/metriques-visibilite-geo]]), pour que la négociation de licence qui suivra une adoption éventuelle ait des chiffres à mettre en face.

**Rattachement doctrine [[concepts/boucle-sortie-mesure]].** L'estimation de la News/Media Alliance (plus de 50 pour cent du trafic sur certains sites) est opératoire pour un éditeur à condition d'avoir instrumenté ses logs pour distinguer bots déclarés, bots camouflés en navigateur, et visites humaines. Sans cette instrumentation, le chiffre reste un argument de communication. Pour un consultant qui audite un éditeur, l'opportunité est d'ajouter à l'audit une ligne "part du trafic imputable à des bots non déclarés" sur les 30 derniers jours, à partir des logs serveur, pas à partir de GA4 (qui perd le signal). Cadrage [[concepts/data-proprietaire]] : cette mesure a une valeur en elle-même, indépendamment du destin du texte au Congrès.

Les réserves qui tiennent cette lecture :

1. Le texte est au stade commission, pas voté. Il peut mourir à ce stade comme la plupart des textes déposés.
2. Les 50 pour cent avancés par la News/Media Alliance sont une statistique de lobby, sans méthodologie publiée dans les sources consultées. Pas de ventilation par type de site ni de panel documenté.
3. Les relais sont tous des médias trade (Digiday, AdExchanger, MediaPost, The Next Web). Pas de commentaire d'un acteur IA cité dans la couverture consultée. L'opposition n'est pas documentée.
4. L'adoption à New York en juin ne garantit pas la trajectoire fédérale. Les scopes et définitions peuvent diverger au cours des amendements.
5. Les 180 jours entre signature et application laisseraient un intervalle pendant lequel les acteurs IA ajusteraient leur déclaration bot. L'effet pratique sur les logs d'un éditeur est donc différé.

Trois prédictions datées sortent de ce fait.

1. **P-2026-10-14-v2-1** : d'ici le 31 mars 2027, le Stealth Bot Prohibition Act (H.R. 9915) n'aura pas été voté par la Chambre des Représentants. Confiance 0,65. Résolution par consultation du registre législatif Congress.gov à cette date.
2. **P-2026-10-14-v2-2** : d'ici le 30 juin 2027, au moins un éditeur américain parmi les 300 ayant lobbyé au Congrès publiera des données chiffrées propres sur la part de son trafic imputable à des bots camouflés en navigateur, avec méthodologie publique. Confiance 0,45. Résolution par publication d'un rapport technique ou d'un billet détaillé.
3. **P-2026-10-14-v2-3** : d'ici le 31 décembre 2026, un acteur IA parmi OpenAI, Anthropic, Google ou Perplexity publiera une déclaration publique d'accord ou d'opposition explicite au texte, ou à son équivalent New York adopté en juin. Confiance 0,40. Résolution par billet officiel sur blog, communication investisseur, ou témoignage à audience publique.

## Brève 1 — GEO / search IA : Previsible 2026 State of AI Discovery, 6,77 millions de sessions sur 166 sites

Previsible a publié le 6 juillet 2026 la troisième édition de son étude trafic IA. Elle couvre novembre 2024 à mai 2026 et analyse 6,77 millions de sessions IA sur 166 sites ([Previsible press release relayée via Las Vegas Sun, Previsible's 2026 State of AI Discovery Report](https://lasvegassun.com/news/2026/jul/06/previsibles-2026-state-of-ai-discovery-report-find/) ; [Martech Series, 6.77 million AI-driven search sessions](https://martechseries.com/?p=403459) ; [Martech Cube, Previsible Finds Google Dominates AI Discovery](https://www.martechcube.com/?p=310019)).

Les chiffres clés rapportés. Google AI Overviews et AI Mode produisent plus de trafic IA-influencé que l'ensemble des assistants LLM standalone combinés. Parmi les assistants standalone, ChatGPT concentre 92,4 pour cent du trafic référent mesurable. Gemini multiplié par 3,2x sur la période, Claude multiplié par 64x et passe devant Perplexity en mars 2026. Le trafic référent IA sur e-commerce multiplié par 37x.

Le fait neuf pour la pratique : l'écart entre Google (AI Overviews + AI Mode) et l'ensemble des LLM assistants n'est pas une variation incrémentale, c'est un ordre de grandeur. Pour un consultant GEO qui alloue du budget d'optimisation entre moteurs, la lecture opérationnelle est que l'optimisation pour AI Overviews et AI Mode continue de porter l'essentiel du trafic, et que ChatGPT concentre à lui seul la quasi-totalité de ce qui reste côté assistants autonomes. Rattachement [[concepts/metriques-visibilite-geo]] : la mesure Previsible porte sur du trafic référent, pas sur du Imp_wc ni du Imp_pos, donc elle ne dit rien sur la part de phrase citée par moteur ; elle dit où le clic sortant arrive. Les deux grandeurs ne sont pas interchangeables.

Deux réserves méthodologiques. Les 166 sites ne sont pas listés et le mix vertical n'est pas publié dans les reprises consultées. L'attribution "trafic IA-influencé" côté Google combine présumément les visites arrivées via un snippet AI avec les visites ordinaires sans distinction fine : la méthode exacte n'est pas documentée dans les relais, et Previsible n'a pas publié de livre blanc dans les sources consultées.

## Brève 2 — Business SEO : Cloudflare bascule vers Pay Per Use, Ceramic.ai premier déploiement

Cloudflare a présenté en août 2026 un nouveau modèle économique pour l'accès des IA aux contenus hébergés sur son réseau : Pay Per Use remplace la logique précédente Pay Per Crawl, qui reste en bêta fermée ([Press Gazette, Cloudflare says bot blocking is fueling publisher AI deals](https://pressgazette.co.uk/platforms/cloudflare-says-bot-blocking-is-fueling-publisher-ai-deals/) ; [IT Brief UK, Cloudflare tightens AI crawler controls for publishers](https://itbrief.co.uk/story/cloudflare-tightens-ai-crawler-controls-for-publishers)).

Le principe du modèle Pay Per Use : rémunérer l'éditeur quand son contenu apparaît dans une réponse IA, pas seulement quand il est crawlé. Le premier partenariat annoncé associe Cloudflare à Ceramic.ai : les éditeurs participants sont payés quand leur contenu apparaît dans les résultats du moteur IA de Ceramic.ai, et reçoivent en retour des données sur les requêtes, les citations et le classement. Un tableau de bord Attribution Business Insights (visibilité IA) complète le dispositif en montrant quelles pages attirent le plus d'attention bot et combien de trafic humain revient réellement vers le site.

Chiffres cités par Cloudflare dans la coverage. Le crawler Google aurait scrapé les sites hébergés 14 fois pour chaque référent envoyé. Un ancien chiffre interne mettait le ratio OpenAI à 1500 crawls par visite humaine (chiffre antérieur, non actualisé par Cloudflare dans les sources consultées). Plus de 50 accords de licence entre éditeurs et plateformes IA ont été signés sur les douze derniers mois, selon Cloudflare.

Le fait exploitable pour un consultant SEO côté éditeur : Pay Per Use réoriente la négociation. Le ratio crawls/référent devient le chiffre à documenter avant toute discussion de licence, et Cloudflare offre maintenant une couche d'instrumentation adaptée à cette négociation. Rattachement doctrine [[concepts/data-proprietaire]] : cette donnée est propriétaire à l'éditeur et n'a pas d'équivalent côté éditeur IA. Rattachement [[concepts/tabou-visibilite]] : "visibilité IA" dans l'outil Cloudflare veut dire apparition dans une réponse, pas conversion ni revenu ; nommer la métrique précisément dans tout reporting.

Réserves. Pay Per Use est décrit par Cloudflare lui-même comme "very early stage". Pay Per Crawl reste en bêta fermée, sans grille publique. Les 50 accords mentionnés ne sont pas listés ni ventilés par taille d'éditeur. Un seul partenaire IA (Ceramic.ai) est documenté publiquement au stade du reporting consulté.

## Brève 3 — Actualité SEO : la donnée Semrush actualise la part Google dans les référents ChatGPT à 21,6 pour cent

Semrush a publié une étude basée sur plus d'un milliard de lignes de données clickstream US, panel 200 millions d'utilisateurs, période octobre 2024 à février 2026 ([Semrush, New Semrush Study Reveals ChatGPT Search Trends: Insights from 80 Million Clickstream Records](https://www.semrush.com/news/379285-new-semrush-study-reveals-chatgpt-search-trends-insights-from-80-million-clickstream-records/) ; relais [Search Engine Land, ChatGPT growing as a traffic referrer](https://searchengineland.com/chatgpt-growing-traffic-referrer-changing-search-behavior-451525)).

Les chiffres principaux. Le trafic référent envoyé par ChatGPT a progressé de 206 pour cent en glissement annuel, en comparant janvier 2025 à janvier 2026. Google concentre 21,6 pour cent de l'ensemble du trafic référent ChatGPT. Les neuf domaines suivants portent le top 10 à un peu plus de 30 pour cent du trafic référent ChatGPT. ChatGPT déclenche une recherche web en direct sur 34,5 pour cent de ses requêtes, en baisse par rapport à 46 pour cent fin 2024.

Le fait exploitable : la concentration des référents sur Google (21,6 pour cent) et sur le top 10 (à peine plus de 30 pour cent) donne une image inverse de celle d'un moteur de recherche classique, où la longue traîne est beaucoup plus distribuée. Pour un éditeur hors top-10 cité par ChatGPT, le volume référent attendu est très faible, et le signal "présence dans une réponse" doit se mesurer autrement que par le trafic sortant. Rattachement doctrine [[concepts/metriques-visibilite-geo]] et [[concepts/tabou-visibilite]] : parler de "trafic ChatGPT" sans distinguer top 10 vs reste reproduit le biais que le lexique anti-euphémisme signale.

Réserves. Panel US uniquement, pas d'équivalent FR, EU ou autre géographie dans l'étude consultée. La baisse de la recherche web live (46 vers 34,5 pour cent) peut refléter un changement de produit côté OpenAI (routage interne vers d'autres sources) autant qu'un changement de comportement utilisateur, les deux lectures ne sont pas départageables dans les relais consultés.

---

*Édition SyntheticBrain v2 du 14 octobre 2026. Pilier info du jour : Agentic Search. Brèves : GEO / search IA, Business SEO, Actualité SEO. Vouvoiement analyste, pas de métaphore, pas de personnification, chiffres sourcés, prédictions datées. Draft non envoyé.*
