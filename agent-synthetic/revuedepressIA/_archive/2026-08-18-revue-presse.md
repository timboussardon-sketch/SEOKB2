---
type: revue-presse
title: "Algorithme — 18 août 2026"
date: 2026-08-18
edition: 2026-08-18-revue-presse
pilier_info_du_jour: Actualite SEO
piliers_breves: [Business SEO, Actualite SEO]
tags: [revue-presse, actualite-seo, microsoft-copilot, deep-research, business-seo, merchant-api, content-api-shopping, shopify]
status: draft
---

# Algorithme — édition du 18 août 2026

## À retenir

- Microsoft retire aujourd'hui trois fonctions de son application Copilot grand public : Deep Research bascule derrière l'abonnement Microsoft 365 Premium, Podcasts disparaît sans option d'export et Group Chat se replie sur des conversations un-à-un. Deep Research reste accessible en payant sous le nom Researcher, les autres non.
- La deadline officielle de sunset de l'API Content for Shopping tombe aussi ce 18 août 2026. Google Ads Liaison Ginny Marvin a reconnu publiquement sur LinkedIn le bug de réécriture d'identifiants produit dans l'app Google & YouTube pour Shopify, sans annoncer de correctif. Google a ouvert un formulaire d'extension de délai.
- Trois canaux gratuits de recherche IA « profonde » perdent une pièce visible ce lundi côté Microsoft : la trajectoire courte pour un utilisateur qui tenait à Deep Research est le repli sur ChatGPT Deep Research en free tier, Perplexity Pro Search ou Google AI Mode, chacun avec un plafond ou une méthodologie distincts.
- Une centaine de marchands Shopify qui utilisent l'app officielle Google & YouTube pour syncer leur catalogue doivent choisir entre reinstaller (et perdre l'historique de performance produit) ou passer à un outil de feed management tiers (Channable, Feedonomics, DataFeedWatch) qui préserve les IDs.

---

## Info du jour — Actualité SEO : Microsoft retire aujourd'hui Deep Research, Podcasts et Group Chat du Copilot grand public

Microsoft applique ce 18 août 2026 le retrait annoncé le 21 juillet dernier par [Paul Thurrott (Thurrott.com, 21 juillet 2026)](https://www.thurrott.com/a-i/microsoft-copilot-a-i/339475/microsoft-is-retiring-copilot-deep-research-and-podcasts) et confirmé sur les [pages officielles Microsoft Support](https://support.microsoft.com/en-us/microsoft-365-copilot/learning/changes-microsoft-copilot-app) : trois fonctions de l'app Copilot grand public sont retirées à cette date.

**1. Deep Research**, la fonction qui produisait des rapports longs et cités depuis des sources web multiples, est retirée du tier gratuit. Verbatim Microsoft rapporté par Thurrott : « Deep Research is being retired in the Copilot app for consumers starting August 18, 2026. » Les rapports Deep Research déjà générés restent accessibles dans l'historique de conversation et exportables au format Word, mais aucun nouveau rapport ne peut être créé sans abonnement Microsoft 365 Premium à 19,99 dollars par mois, qui donne accès à une fonction équivalente rebaptisée Researcher.

**2. Podcasts**, la fonction qui synthétisait automatiquement des discussions audio à partir de sites et de documents, disparaît complètement. Verbatim Microsoft : « Podcasts is being retired in the Copilot app for consumers starting on August 18, 2026. » Aucun mécanisme d'export n'est proposé : les utilisateurs ont 29 jours pour ré-écouter les fichiers audio générés, sans possibilité de les sauvegarder par une voie officielle. La fonction Podcasts n'a pas d'équivalent premium annoncé.

**3. Group Chat**, la fonction qui permettait à plusieurs utilisateurs de tenir une conversation collaborative avec Copilot, est basculée en conversations un-à-un. Les messages, images et artefacts créés collaborativement restent visibles dans l'historique mais ne peuvent plus être prolongés en groupe. Les contributions apportées par des collaborateurs distincts du propriétaire deviennent inaccessibles après la migration ([GBHackers, 21 juillet 2026](https://gbhackers.com/microsoft-copilot-update-merges-chats-retires-podcast/) ; [WindowsCentral, 21 juillet 2026](https://www.windowscentral.com/artificial-intelligence/microsoft-copilot/microsoft-begins-unified-copilot-app-rollout-reveals-major-plan-to-merge-copilot-and-microsoft-365-copilot-across-all-platforms-along-with-updated-branding)).

Le fait éditorial neuf, pour un consultant SEO ou GEO, n'est pas le retrait en soi. C'est la composition résiduelle des poches gratuites de recherche IA « profonde » après ce lundi, et ce que cette composition implique pour un utilisateur qui produisait des rapports Deep Research chez Microsoft :

- **ChatGPT Deep Research** reste accessible en tier gratuit sur OpenAI mais avec un plafond mensuel documenté à un petit nombre de rapports (variable selon les changements de politique) et une méthodologie de retrieval désormais documentée par l'étude RESONEO du 17 août 2026 (voir édition [Algorithme du 17 août 2026 (v2)](https://think.resoneo.com/chatgpt-retrieval/) : trois couches, cache lu, ChatGPT-User).
- **Google AI Mode** propose ses réponses de synthèse gratuites globalement, avec Gemini 3.5 Flash comme modèle par défaut depuis I/O 2026 (source [blog.google I/O 2026](https://blog.google/products-and-platforms/products/search/search-io-2026/)), et un bouton Think étendu au free tier qui ouvre 35 URL en moyenne par requête, contre 15 en mode instant.
- **Perplexity Pro Search** reste gratuit avec un plafond quotidien de requêtes profondes, distinct de Deep Research qui reste réservé aux abonnés Perplexity Pro à 20 dollars par mois.

Trois lectures opérationnelles se dégagent.

- **Le volume de recherche IA « profonde » gratuit ne disparaît pas ce lundi, il se redistribue.** La part exacte d'utilisateurs Deep Research côté Microsoft Copilot n'a pas été publiée par Microsoft. Pour un consultant SEO qui suit les positions de son client dans les plateformes de réponse IA gratuites, la conséquence attendue est un déplacement mesurable de requêtes vers ChatGPT, Google AI Mode et Perplexity au troisième et quatrième trimestre 2026. Métrique utile à suivre côté serveur : le compte de hits User-Agent ChatGPT-User, GoogleOther-User et PerplexityBot-User sur les pages du client, avec la baisse attendue de BingBot-related fetches sur les mêmes pages.
- **La bascule d'une fonction « recherche IA profonde » du gratuit vers un abonnement à 19,99 dollars mensuel est un cas d'école d'arbitrage plateforme-publication côté utilisateur.** Cohérent avec [[concepts/arbitrage-plateforme-publication]] : le coût d'entrée à la recherche IA profonde devient explicite, et le choix de plateforme se fait sur le rapport prix/qualité/périmètre de sources plutôt que sur la disponibilité seule. Un cabinet SEO qui vend un service de veille IA doit désormais lister les 4 offres avec plafond gratuit, prix payant, méthodologie de retrieval (quand elle est publiée) et périmètre de sources indexées.
- **Les rapports Deep Research déjà générés par les utilisateurs de l'app Copilot forment un corpus verrouillé chez Microsoft.** Contenu exportable en Word, mais non-migrable vers un autre fournisseur en état. Pour un consultant qui a produit des rapports Deep Research pour un client, l'exportation Word doit être exécutée avant le 18 août ou dans les 29 jours qui suivent selon les fonctions, sans quoi le format brut de restitution disparaît. C'est un cas concret de [[concepts/data-proprietaire]] : la conservation des sorties analytiques dépend de la discipline de l'utilisateur, pas du fournisseur.

Trois caveats à publier avec ce corps de faits. Un : le retrait ne s'applique qu'à l'app Copilot grand public. La version Microsoft 365 Copilot Enterprise, distincte, garde Deep Research et ses variantes sous l'abonnement d'entreprise correspondant, sans changement annoncé à cette date. Deux : le prix de 19,99 dollars par mois cité correspond à l'abonnement Microsoft 365 Premium ; il inclut d'autres fonctions Microsoft 365 et n'est pas un tarif de « Researcher seul ». Trois : la baisse attendue de fetches BingBot-related n'est pas mesurée à date, c'est une hypothèse à vérifier par observation logs serveur post-transition.

Trois prédictions vérifiables ouvertes à date. **P-2026-08-18-1** : sur un corpus de 20 sites SEO ayant publié des logs serveur avant/après le 18 août 2026, la baisse mesurée de hits User-Agent BingBot dans les 60 jours qui suivent est supérieure à 15 %, avant le 31 décembre 2026, confiance 0,45. **P-2026-08-18-2** : Microsoft publie une justification chiffrée du retrait (nombre d'utilisateurs Deep Research, coût par requête, taux d'abandon) au trimestre 3 ou 4 2026, avant le 31 mars 2027, confiance 0,20. **P-2026-08-18-3** : un outil de tracking GEO grand public (Otterly, Profound, AthenaHQ, Semrush) expose une colonne « report parity Microsoft Copilot vs Researcher » comparant la couverture de sources sur mêmes requêtes avant le 30 juin 2027, confiance 0,25.

---

## Brève 1 — Business SEO : Content API Shopping sunset effective aujourd'hui, Google reconnaît le bug Shopify sans correctif

Le sunset de l'[API Content for Shopping](https://support.google.com/merchants/answer/16493611?hl=en) devient effectif ce 18 août 2026. Google publie en primaire : « we will provide access to the Content API until August 18, 2026 », après quoi « the Content API will be shut down ». La bascule vers la Merchant API v1, disponible depuis mai 2024 et GA depuis l'été 2025, est obligatoire pour toute intégration API-based. Les uploads manuels de fichier, fetch programmés et Google Sheets feeds continuent de fonctionner sans changement.

Le fait éditorial neuf par rapport aux brèves précédentes du 7 juillet et du 6 août 2026, c'est la reconnaissance publique par Google du bug de réécriture d'identifiants produit dans l'app Google & YouTube pour Shopify, sans annonce de correctif à date. Ginny Marvin, Google Ads Liaison, a répondu sur LinkedIn en confirmant que l'équipe enquête sur le problème signalé par Emmanuel Flossie depuis janvier 2026 ([ppcnewsfeed, 11 juillet 2026](https://ppcnewsfeed.com/ppc-news/2026-07/google-youtube-shopify-app-sync-may-reset-product/) ; [DigitalPhablet, 18 août 2026](https://digitalphablet.com/digital-marketing/google-youtube-shopify-app-sync-issues-post-august-18-api-update/)). Aucune date de résolution n'est annoncée.

Le mécanisme du bug : quand un marchand Shopify désinstalle et réinstalle l'app Google & YouTube dans le cadre de la migration Content API → Merchant API, les identifiants produit passent d'un format `Shopify_US_12345_67890` (avec code pays) à `Shopify_ZZ_12345_67890` (avec le code générique ZZ). Google traite les nouveaux IDs comme des produits neufs, l'historique de performance disparaît côté Merchant Center, et les campagnes Performance Max qui pilotent ces produits doivent ré-apprendre à zéro. La perte d'historique n'est pas partielle, elle est totale sur les IDs concernés.

Le second fait neuf : Google a ouvert un formulaire de demande d'extension d'accès à la Content API après le 18 août ([Elsop Insights, 4 août 2026](https://www.elsop.com/content-api-shopping-sunset/)). L'invitation officielle est « apply for extended access to Content API for Shopping ». Alex Savich note dans le même billet un caveat opérationnel : le formulaire est « a plan built on a form, not a commitment », l'approbation d'une demande d'extension n'est pas garantie. Aucun taux d'approbation n'est publié à date.

Deux lectures pour un consultant SEO ou e-commerce qui accompagne un annonceur Shopify.

- **La recommandation partagée par Matinique Roelse (LinkedIn), reprise dans [ProductHero](https://www.producthero.com/post/google-is-sunsetting-the-content-api-for-shopping-what-you-need-to-know) et [Feedshield](https://feedshield.ai/blog/content-api-sunset-what-to-do), consiste à cesser d'utiliser l'app Shopify pour le flux produit avant la migration et à passer à un outil de feed management tiers** (Channable, Feedonomics, DataFeedWatch, GoDataFeed). Ces outils contrôlent leurs propres IDs produit et ne subissent pas la réécriture. Le coût mensuel de ces outils démarre à quelques centaines de dollars pour les PME et devient un poste rentable dès qu'un marchand a plus de 500 produits actifs et une campagne Performance Max active. Un cas concret de [[concepts/data-proprietaire]] : garder le contrôle des IDs produit chez soi vs le déléguer à une app tierce dépendante d'une plate-forme.
- **Pour les marchands déjà sur l'app Shopify sans budget pour un outil tiers, la seule voie qui préserve l'historique est le formulaire d'extension Google, avec le risque de refus.** Le fallback intermédiaire consiste à attendre l'annonce d'un correctif Google avant de désinstaller/réinstaller l'app, sachant que les intégrations existantes cesseront de fonctionner après le 18 août. C'est une position d'attente inconfortable mais moins destructive que la réinstallation à cru.

Un caveat à publier. La proportion réelle de marchands Shopify utilisant l'app officielle Google & YouTube par rapport aux marchands passés à un outil de feed management tiers n'est pas publiée par Google. L'impact absolu du bug sur le marché e-commerce US n'est donc pas quantifiable ce lundi. La couverture presse SEO estime le nombre de marchands impactés en dizaines de milliers, sans source primaire.

Prédiction ouverte **P-2026-08-18-4** : Google publie une communication officielle sur le bug d'ID Shopify avec un correctif ou un mécanisme de préservation d'historique avant le 30 septembre 2026, confiance 0,45.

---

## Brève 2 — Actualité SEO : deux deadlines Google Merchant Center coïncident, l'une technique, l'autre commerciale

Au-delà du sunset Content API Shopping traité en brève 1, deux deadlines annexes Google Merchant Center coïncident aujourd'hui ce 18 août 2026, documentées par [Search Engine Roundtable](https://www.seroundtable.com/august-2026-google-webmaster-report-41804.html) dans son webmaster report d'août :

- **Conversion-based customer lists** : Google Ads active à cette date le traitement des données pour les listes clients basées sur les conversions, une fonction annoncée pour le 17 juin 2026 avec une bascule progressive. Les données de conversion des annonceurs deviennent à partir d'aujourd'hui utilisables pour construire des audiences customer match, sauf opt-out explicite au niveau du compte.
- **Google & YouTube Shopify app sync** : les marchands qui ne migrent pas avant aujourd'hui verront leur sync Merchant Center dégrader progressivement, avec risque de disparition de produits du catalogue Google Shopping et perte de campagnes Performance Max active sur les produits concernés.

Le fait éditorial neuf est la coïncidence de calendrier. Trois deadlines Google d'écosystème Merchant Center et une deadline Microsoft de recherche IA (Copilot Deep Research + Podcasts + Group Chat, voir info du jour) tombent le même jour. Pour un annonceur qui gère à la fois catalogue Google Shopping et présence Microsoft Copilot, le 18 août 2026 est un point d'inflexion multiple qui appelle une revue technique d'infrastructure ce lundi ou demain.

Deux lectures pour un consultant qui audite les stacks e-commerce clients ce mois-ci.

- **Les deadlines Google Ads sont documentées mais fragmentées entre trois canaux** : la page [Merchant Center Help](https://support.google.com/merchants) pour l'API, les [pages Google Ads Help](https://support.google.com/google-ads) pour customer match, et les recap Search Engine Roundtable pour la coordination. Une checklist stack e-commerce client au 18 août 2026 doit lister les 3 points en séquence, plus le formulaire d'extension Google si la migration API n'est pas prête, plus le point de contrôle serveur qui expose les IDs produit avant et après la réinstallation le cas échéant.
- **La bascule customer lists en conversion-based augmente la valeur des données de conversion propres du marchand pour Google Ads.** Cohérent avec [[concepts/data-proprietaire]] : un annonceur qui capture et stocke ses propres conversions dans un CRM externe conserve l'usage même si la plate-forme Google change ses politiques d'audience. Le risque inverse : un annonceur qui laisse Google Ads reconstruire les audiences depuis son côté sans backup externe se retrouve enfermé dans une dépendance à la mesure Google.

Prédiction ouverte **P-2026-08-18-5** : Google publie avant le 31 décembre 2026 une note sur l'usage effectif des conversion-based customer lists trois à six mois après activation, avec un chiffre d'adoption par verticale, confiance 0,35.

---

## Sources nouvelles ce run (explore)

- [thurrott.com](https://www.thurrott.com/a-i/microsoft-copilot-a-i/339475/microsoft-is-retiring-copilot-deep-research-and-podcasts) — trust initial 0,72 (Paul Thurrott, journaliste tech Microsoft de référence, historique éditorial long, candidate exploit si couverture Microsoft régulière confirmée).
- [gbhackers.com](https://gbhackers.com/microsoft-copilot-update-merges-chats-retires-podcast/) — trust initial 0,55 (site sécurité/tech, corroboration secondaire indépendante).
- [windowscentral.com](https://www.windowscentral.com/artificial-intelligence/microsoft-copilot/microsoft-begins-unified-copilot-app-rollout-reveals-major-plan-to-merge-copilot-and-microsoft-365-copilot-across-all-platforms-along-with-updated-branding) — trust initial 0,70 (média Windows/Microsoft de référence, candidate exploit si couverture Microsoft AI régulière).
- [digitalphablet.com](https://digitalphablet.com/digital-marketing/google-youtube-shopify-app-sync-issues-post-august-18-api-update/) — trust initial 0,50 (site digital marketing tiers, corroboration secondaire).
- [ppcnewsfeed.com](https://ppcnewsfeed.com/ppc-news/2026-07/google-youtube-shopify-app-sync-may-reset-product/) — trust initial 0,55 (média PPC secondaire, source de première mention Ginny Marvin sur LinkedIn).
- [elsop.com](https://www.elsop.com/content-api-shopping-sunset/) — trust initial 0,55 (Alex Savich, blog Elsop Insights, note primaire sur formulaire d'extension Google).
- [producthero.com](https://www.producthero.com/post/google-is-sunsetting-the-content-api-for-shopping-what-you-need-to-know) — trust initial 0,60 (agence feed management, source primaire sur workaround).
- [feedshield.ai](https://feedshield.ai/blog/content-api-sunset-what-to-do) — trust initial 0,55 (agence feed management, corroboration secondaire).

## Sources connues ré-utilisées

- [support.google.com](https://support.google.com/merchants/answer/16493611?hl=en) — source primaire Google Merchant Center Help, verbatim sunset date.
- [support.microsoft.com](https://support.microsoft.com/en-us/microsoft-365-copilot/learning/changes-microsoft-copilot-app) — source primaire Microsoft Support pour retraits Copilot.
- [seroundtable.com](https://www.seroundtable.com/august-2026-google-webmaster-report-41804.html) — Barry Schwartz webmaster report août 2026, corroboration deadline customer lists.
- [blog.google](https://blog.google/products-and-platforms/products/search/search-io-2026/) — annonce I/O 2026 Google Search, contexte AI Mode.

## Ce que cette édition ajoute au vault

- Un point d'inflexion daté (18 août 2026) sur la disponibilité gratuite de la recherche IA « profonde » côté Microsoft, avec conséquences prévisibles de redistribution vers ChatGPT, Google AI Mode et Perplexity. Utile pour ancrer [[concepts/arbitrage-plateforme-publication]] sur un cas d'arbitrage utilisateur (choix de plateforme de recherche IA) plutôt qu'éditeur ou marchand.
- La reconnaissance publique par Google, via Ginny Marvin, du bug d'ID Shopify sans annonce de correctif à la date de sunset. Fait procédural neuf sur un sujet couvert deux fois en brève auparavant (07-07 et 08-06), justifie l'inscription dans le registre des cas où une plate-forme casse la mesure côté annonceur sans compensation.
- Une checklist stack e-commerce implicite pour un consultant qui audite un client ce mois-ci : Content API sunset, customer lists activation, app Shopify sync. Utile pour compléter [[concepts/data-proprietaire]] avec la nuance « garder le contrôle des IDs produit chez soi vs déléguer à une app tierce dépendante ».

---

Draft SyntheticBrain. Rien n'a été envoyé.
