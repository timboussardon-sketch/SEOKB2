---
type: revue-presse
title: "Algorithme — édition du 2026-10-08 v2"
date: 2026-10-08
pilier_info_du_jour: Actualité SEO
piliers_breves: [GEO / search IA, Niche SEO, Actualité SEO]
sources_consultees: 11
sources_nouvelles: 2
tags: [algorithme, actualite-seo, merchant-center, feed-shopping, synthid, visibility-tracker, spam-update, manual-action]
status: draft
---

# Algorithme — édition du 2026-10-08 v2

## Résumé

- Google documente le 27 septembre 2026 que les produits dont le prix ou la disponibilité changent plus d'une fois par jour peuvent être désapprouvés plutôt que mis à jour automatiquement par Merchant Center. Barry Schwartz reproduit la modification le 8 octobre et compare à la version archivée de mars 2026 ([Search Engine Roundtable](https://www.seroundtable.com/google-merchant-center-disapprove-products-chnage-fast-42251.html), [PPC News Feed](https://ppcnewsfeed.com/ppc-news/2026-10/google-warns-fast-changing-products-may-be-disapproved/), [Google Merchant Center Help](https://support.google.com/merchants/answer/12157888)).
- Brett Tabke (Search Engine World, 7-8 octobre 2026) publie un guide d'achat des trackers de visibilité IA après avoir recensé plus de 50 outils, en avoir couvert 33, et tenté d'en construire un en trois semaines ; Semrush annonce son rapport Sources dans Position Tracking le 7 octobre, avec des quotas de 25 à 200+ prompts selon le plan ([Search Engine World](https://www.searchengineworld.com/buyers-guide-to-aio-geo-trackers-mentions-citaions-chatgpt-claude-google-llm), [Semrush Blog](https://www.semrush.com/blog/track-ai-citation-sources-semrush/)).
- Google DeepMind ouvre au grand public le 7 octobre 2026 le site SynthID Detector pour vérifier si une image, une vidéo ou un fichier audio a été produit par un modèle Google ou un partenaire (OpenAI, NVIDIA, Kakao, Apple « bientôt ») ; plus de 180 milliards d'images et vidéos et plus de 240 000 années de contenu audio sont filigranées, avec plus d'un million de requêtes de vérification par jour via Search, Gemini et Chrome ([Google Blog](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/synth-id-ai-content/)).
- Google confirme sur son Search Status Dashboard le 8 octobre à 4h37 ET que la September 2026 spam update est terminée après environ 13,7 jours de déploiement, contre deux à trois jours pour les spam updates précédentes de l'année ([Search Status Dashboard](https://status.search.google.com/incidents/XhUDXP7A67iHCD2kmbVu), [Search Engine Roundtable](https://www.seroundtable.com/google-september-2026-spam-update-done-42235.html)).
- En parallèle, Marie Haynes et Daniel Foley Carter rapportent le 7 octobre une hausse des actions manuelles reçues par des sites établis (thin content, pure spam, scaled content abuse) ; Schwartz dénombre 12 fils actifs sur les forums d'aide Google le 8 octobre ([Search Engine Roundtable](https://www.seroundtable.com/google-search-manual-action-spike-42258.html)).

---

## Info du jour — Actualité SEO : Google documente que les feeds qui changent plus d'une fois par jour peuvent être désapprouvés plutôt que corrigés

**Événement.** Le 27 septembre 2026, Google publie une révision de sa page d'aide Merchant Center « Allow Merchant Center to update product information automatically » ([Google Merchant Center Help](https://support.google.com/merchants/answer/12157888)). La modification est repérée par Hana Kobzová et publiée par PPC News Feed le 7 octobre ([PPC News Feed](https://ppcnewsfeed.com/ppc-news/2026-10/google-warns-fast-changing-products-may-be-disapproved/)), puis reprise et comparée à la version archivée de mars 2026 par Barry Schwartz le 8 octobre ([Search Engine Roundtable](https://www.seroundtable.com/google-merchant-center-disapprove-products-chnage-fast-42251.html)).

**Le passage exact ajouté.** Sous la section « Benefits of automations », trois phrases sont nouvelles par rapport à la version de mars 2026 :

> « Automations may not work for products with frequent price or availability value changes (for example more than once per day). The product may be disapproved instead of updated if we detect a mismatch. We may also stop updates if the total number of detected mismatches becomes too large. »

Le seuil chiffré, « for example more than once per day », n'apparaissait pas dans la version précédente. La page garde par ailleurs un garde-fou pour les prix barrés (plusieurs strikethroughs sur une même page) : Google indique que les mises à jour automatiques de prix ne doivent pas être activées dans ce cas, parce que l'extraction ne peut pas identifier le prix correct.

**Ce que ça change concrètement.** Les automations Merchant Center servaient à corriger les écarts occasionnels entre le feed et la page produit (prix, disponibilité, condition) à partir des données structurées de la page. La nouvelle rédaction documente trois conséquences cumulatives pour les feeds à forte volatilité :

1. L'automation n'est pas garantie de fonctionner si la variation dépasse une occurrence par jour.
2. En cas de mismatch détecté, le produit peut être désapprouvé plutôt que mis à jour.
3. Si le volume de mismatches détectés devient élevé, Google peut stopper les mises à jour pour l'ensemble du compte.

Les trois clauses sont rédigées comme des possibilités (« may »), pas comme des règles déterministes. Google ne publie ni le volume concret de mismatches qui déclenche l'arrêt, ni la fenêtre d'évaluation.

**Les modèles de prix concernés par le seuil.** Le seuil d'une mise à jour par jour touche directement plusieurs catégories de marchands dont le prix bouge par construction :

- Agrégateurs billetterie, hôtellerie, mobilité : prix affiché calculé à partir de disponibilités tiers, souvent recalculé chaque heure.
- Marketplaces de revente luxe et consignation (prix fixé par vendeur, modifiable à chaque session).
- Ventes privées, flash sales et offres à durée limitée dont le prix bascule plusieurs fois par journée.
- Catalogues avec cash-back ou coupons de retailer appliqués dynamiquement selon la session utilisateur ([documentation d'erreur Mismatched product price](https://support.google.com/merchants/answer/12159029)).
- Produits en enchère ou pricing dynamique indexé sur la demande (algorithmes de yield management).

Google ne nomme pas ces catégories dans sa documentation. Le lien se déduit du seuil « plus d'une fois par jour » appliqué au prix et à la disponibilité, deux champs centraux pour ces modèles.

**Pilier Actualité SEO.** Cette révision est une clarification de politique Merchant Center, pas une mise à jour d'algorithme. Elle rentre dans Actualité SEO parce qu'elle change ce que Google considère comme un feed « sain » et parce qu'elle a un effet direct sur l'éligibilité à Google Shopping, aux formats produits de l'AI Mode et à l'affichage dans la Shopping Graph. Elle n'est pas Business SEO au sens du périmètre du vault, puisqu'elle ne crée pas de nouvelle acquisition organique : elle en soustrait pour les modèles qui ne tiennent pas le seuil.

**Les actions documentées côté marchand.** La page d'aide Google décrit ce qui est attendu, sans le présenter comme obligatoire :

- Mettre à jour le feed au rythme réel du prix et de la disponibilité (push ou API) plutôt que de laisser Google corriger les écarts.
- Ajouter des données structurées Product (schema.org price, availability) sur la page produit, source lue par l'automation quand elle fonctionne.
- Ne pas activer l'automation prix si la page produit comporte plusieurs prix barrés visibles.
- Vérifier régulièrement les statuts dans Merchant Center, puisque les automations peuvent être arrêtées en silence quand le volume de mismatches dépasse un seuil non publié.

**Articulation avec Google Shopping et l'AI Mode.** L'éligibilité aux formats Shopping Ads inline carousel dans l'AI Mode, documentée depuis le 31 août 2026 et la mise en avant Merchant Center + Gemini, dépend du statut d'approbation produit dans Merchant Center. Un compte sous arrêt d'automation pour volume de mismatches voit mécaniquement sa surface d'affichage se réduire, dans l'AI Mode comme dans les SERPs classiques. Google n'a pas publié de communication Search Central dédiée au 8 octobre 2026 ni de billet blog.google sur ce changement : la seule trace publique est la page d'aide révisée.

**Lien doctrine.** Le concept [[concepts/boucle-sortie-mesure]] formalise la fermeture du cycle contenu publié → mesure. Dans le cas du Merchant Center, la mesure arrive côté marchand sous forme d'arrêt silencieux d'automation : le feed continue d'exister côté marchand, mais plus d'être lu côté Google. L'alerte doit venir du monitoring Merchant Center, pas de la supposition que « tout va bien parce que la pub tourne ». Lien [[concepts/metriques-visibilite-geo]] pour la mesure côté réponse générative.

**Limites et réserves.**
- Pas de date de dernière mise à jour visible sur la page d'aide (footer © 2026 Google uniquement). La date du 27 septembre 2026 vient de Hana Kobzová telle que rapportée par PPC News Feed. Elle n'est pas confirmée par un changelog Google.
- Google ne publie pas le seuil chiffré de mismatches à partir duquel les mises à jour s'arrêtent.
- La fréquence déclencheuse « plus d'une fois par jour » est présentée comme un exemple (« for example »), pas comme un seuil réglementaire. L'interprétation plus stricte reste à vérifier via des cas marchands documentés.
- Aucune étude cabinet tierce ne quantifie à ce jour l'impact de la révision sur l'approbation des feeds à forte volatilité.

**Prédiction.** Si la révision du 27 septembre reflète un durcissement effectif de la mécanique Merchant Center (et pas seulement une clarification de documentation existante), on devrait voir avant le 2026-12-31 soit un billet Google Search Central ou blog.google explicitant le seuil, soit une analyse cabinet tiers (par exemple DataFeedWatch, Channable, Productsup) chiffrant la hausse des désapprobations sur des feeds à pricing dynamique. Confidence 0,55.

---

## Brève 1 — GEO / search IA : le marché des trackers de visibilité IA ouvre la question du prix unitaire

Deux publications du 7 octobre 2026 décrivent le même marché sous deux angles.

Brett Tabke, fondateur de WebmasterWorld et Pubcon, publie « AI Visibility Tracking: An SEO's Buyer's Guide » sur Search Engine World ([Search Engine World](https://www.searchengineworld.com/buyers-guide-to-aio-geo-trackers-mentions-citaions-chatgpt-claude-google-llm)). Il a recensé plus de 50 outils, en a couvert 33, et détaille des exemples de pricing génériques : plans « 99 $ », « 79 $ », « 59 $ », « 200 $ » avec projets illimités, « 200-300 $ » avec projets illimités. Les unités facturées varient (prompt, prompts × moteurs, crédits, model runs, par domaine/marque/projet, sièges). Un vendeur offre 5 000 prompts inclus, un autre 300. Les volumes de collecte diffèrent : dix clients × 50 prompts × 4 moteurs vérifiés chaque semaine donnent environ 8 600 réponses par mois, et environ 60 000 en vérification quotidienne. Tabke a construit un prototype en environ trois semaines ouvrées (ChatGPT a produit une version fonctionnelle en 15 minutes selon ses mots) ; son propre outil Foo.Red est décrit comme « vaporware ». Sa conclusion : les réponses IA ne sont pas des rankings, l'évaluation porte sur des patterns dans le temps, les sources citées et le mouvement des concurrents sur un jeu de prompts stable. Verbatim : « The value of SEO has moved from doing SEO tasks, to deciding which SEO tasks are worth doing. »

Semrush publie le même jour « How to track your AI citations and sources with Semrush », signé Luke Harsel ([Semrush Blog](https://www.semrush.com/blog/track-ai-citation-sources-semrush/)). L'article décrit le rapport Sources de Prompt Tracking : onglets Sources, Pages, Domains ; sélecteur de plateforme (dont Google AI Mode et ChatGPT) ; widget Sources by Category ; colonnes « Cited for prompts », « Your mentions », « Diff », « Mention rate ». Les quotas par plan sont documentés : 25 prompts pour l'AI Visibility Toolkit, 50 pour Starter, 100 pour Pro+, 200 pour Advanced, custom pour Enterprise. Le cas d'exemple (Amerisleep, 20 prompts) donne 49 pages sources en Google AI Mode (1 réponse mentionne la marque) et 40 en ChatGPT (0 mention). La distribution par catégorie diffère : 76 % de sources e-commerce dans AI Mode contre 38 % dans ChatGPT ; 6 % de bases de connaissances dans AI Mode contre 33 % dans ChatGPT. Verbatim Semrush : « Mention rate refers to the AI answers rather than the source page itself. »

Les deux publications se recouvrent sur un même constat : la mesure de la visibilité IA se segmente par plateforme, et le prix unitaire d'une mesure fiable (prompt × moteur × fréquence × localisation × multi-utilisateurs) rend la comparaison entre outils difficile. Le podcast [Advanced Web Ranking](https://www.advancedwebranking.com/blog/strategic-marketing-for-ai-search) du 5 octobre 2026 avec Gianluca Fiorelli et Emina Demiri-Watson converge sur le même point sous un autre angle : « Track brand presence in AI answers, and pay attention to which brands appear alongside yours. »

Lien doctrine : [[concepts/metriques-visibilite-geo]] rappelle que les scores classiques (position Google) ne mesurent pas la visibilité générative, et que `Imp_wc`, `Imp_pos` et la Subjective Impression sont trois mesures distinctes à ne pas composer naïvement. Articulation avec [[sources/2026-04-13-sageo-arena-2025]] et [[concepts/boucle-sortie-mesure]].

Limites : Tabke n'est pas une étude contrôlée, c'est un article d'opinion basé sur l'hands-on d'un éditeur impliqué commercialement (projet Foo.Red). Le billet Semrush est un contenu éditeur-outil, autopromoteur par construction. Les chiffres cités dans le billet Semrush viennent du cas Amerisleep, pas d'un échantillon représentatif. Le podcast Advanced Web Ranking n'apporte pas de donnée chiffrée.

---

## Brève 2 — Niche SEO : SynthID Detector ouvre au grand public la vérification de contenu généré par IA

Pushmeet Kohli, VP Science and Strategic Initiatives chez Google DeepMind, annonce le 7 octobre 2026 l'ouverture au grand public du site SynthID Detector, accessible sur [synthid.com](https://synthid.com) ([Google Blog](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/synth-id-ai-content/)). L'outil permet de vérifier si une image, une vidéo ou un fichier audio a été produit par un modèle Google ou un partenaire. Les partenaires nommés sont OpenAI, NVIDIA et Kakao, avec Apple « soon ». La version précédente était réservée aux professionnels des médias. L'annonce indique une disponibilité mondiale, en anglais, à partir du 7 octobre 2026.

Les chiffres publiés : SynthID a été lancé en 2023 ; plus de 180 milliards d'images et vidéos ont été filigranées à ce jour ; plus de 240 000 années de contenu audio ont été filigranées ; les vérifications intégrées à Search, à l'application Gemini et à Chrome traitent plus d'un million de requêtes par jour. Le texte ne couvre pas le filigranage ni la détection de texte généré par IA.

Angle Niche SEO. Pour les niches qui vivent de contenu visuel ou audio (publications photo et vidéo, médias d'information, catalogues iconographiques, moteurs de recherche verticale images-vidéos, outils de modération), l'existence d'un détecteur accessible au grand public change la position de défense sur deux points :
1. Elle rend la vérification à la demande d'un visuel suspect disponible sans contrat média.
2. Elle crée une dépendance au périmètre de couverture Google + partenaires : un visuel généré par un modèle hors partenariat (Flux, Midjourney propriétaire, modèles ouverts non filigranés) reste invisible à l'outil.

L'annonce Google ne commente pas les implications SEO ni les politiques Google concernant le contenu généré par IA (Deceptive Authorship doc du 5 octobre dans said_index). Elle ne décrit pas non plus la méthode technique au-delà de la mention « imperceptible watermarks ».

Limites : annonce officielle unique côté Google, pas de reproduction par un cabinet tiers au 8 octobre 2026. Pas de taux publié de faux positifs ou faux négatifs. Pas de couverture Search Engine Land dédiée. Reprise [TechCrunch](https://techcrunch.com/2026/10/07/googles-new-synthid-website-can-identify-ai-generated-media/) existe mais ne corrobore pas de chiffre indépendamment.

---

## Brève 3 — Actualité SEO : la September 2026 spam update termine son déploiement en environ 14 jours, hausse de signalements de manual actions en parallèle

Google confirme sur son Search Status Dashboard le 8 octobre 2026 à 4h37 ET que la September 2026 spam update est terminée ([Search Status Dashboard](https://status.search.google.com/incidents/XhUDXP7A67iHCD2kmbVu)). Verbatim Google : « The rollout was complete as of October 8, 2026. » Rappel du calendrier : lancement le 24 septembre vers 12h ET, phases observées fin septembre (25-27), 30 septembre, puis 4-6 octobre. Durée totale environ 13,7 jours, contre deux à trois jours pour les spam updates précédentes de 2026 (mars, juin, août) ([Search Engine Roundtable](https://www.seroundtable.com/google-september-2026-spam-update-done-42235.html)). Google qualifie l'update de « normal spam update » et indique qu'elle « applies globally and to all languages ». Barry Schwartz note dans son article que la durée est atypique pour un cycle qu'il qualifie de « normal » et ouvre la possibilité qu'un core update suive peu après, sans élément Google à l'appui.

Le même jour, Schwartz publie un second article sur une hausse signalée des actions manuelles ([Search Engine Roundtable](https://www.seroundtable.com/google-search-manual-action-spike-42258.html)). Deux voix externes :

- Marie Haynes, le 7 octobre sur X : les demandes de réexamen qu'elle reçoit sont passées de « essentially no requests to several per week », avec des sites décrits comme établis et légitimes. Types mentionnés : thin content, pure spam, scaled content.
- Daniel Foley Carter, le 7 octobre sur X : les actions manuelles reviennent plus fréquemment depuis quelques mois, avec quinze catégories listées (parmi lesquelles « Back button hijacking », « Site abused with third-party spam », « Thin content with little or no added value », « Unnatural links to your site », « Cloaking and/or sneaky redirects », « Site reputation policy »).

Schwartz dénombre 12 fils actifs sur les forums d'aide Google (par exemple « 3 reconsideration rejections despite 6K+ URL cleanup », « Entire Blog Section Disappeared from Google due to Manual Action »). Il note qu'il a interrogé Gemini et ChatGPT sur les corpus forums : les deux rapportent plus de plaintes qu'avant mais sans « super big spike », avec des courbes qui divergent entre les deux modèles — point qu'il flague comme écart de méthode.

Articulation entre les deux faits. Google ne lie pas publiquement la fin de la spam update à une hausse d'actions manuelles. Deux lectures restent possibles : les actions manuelles ciblent des sites non traités par la couche algorithmique de l'update, ou elles ciblent des sites déjà touchés par l'update dont le contenu reste identifié comme spam après rollout. Les données publiques du 8 octobre ne permettent pas de trancher.

Limites : les signalements de manual action viennent de deux comptes X et d'un échantillon forum manuel. Les deux outils d'analyse (Gemini, ChatGPT) donnent des courbes différentes sur le même corpus, selon Schwartz. Google ne publie pas de statistique officielle de volume d'actions manuelles. Les chiffres cités dans les threads (par exemple « 6K+ URL cleanup », « 4,000 URLs removed ») sont rapportés par les plaignants, sans vérification.

---

## Prédictions logguées

- P-2026-10-08-v2-1 : avant 2026-12-31, Google publie un billet Search Central ou blog.google détaillant le seuil de mismatches qui déclenche l'arrêt d'automation Merchant Center, ou un cabinet tiers (DataFeedWatch, Channable, Productsup) chiffre la hausse des désapprobations sur feeds à pricing dynamique. Confidence 0,55.
- P-2026-10-08-v2-2 : avant 2027-03-31, au moins deux outils de visibilité IA du marché recensé par Tabke changent leur unité tarifaire (passage prompt × moteur → model run, ou l'inverse) sous pression de comparaison acheteur. Confidence 0,45.
- P-2026-10-08-v2-3 : avant 2026-12-31, Google ou un éditeur tiers (Perplexity, OpenAI) publie une politique explicite reliant le filigranage SynthID à un signal de ranking ou de citation IA. Confidence 0,30.

---

## Sources utilisées

- Primaires Google : [support.google.com/merchants/answer/12157888](https://support.google.com/merchants/answer/12157888) ; [support.google.com/merchants/answer/12159029](https://support.google.com/merchants/answer/12159029) ; [status.search.google.com](https://status.search.google.com/incidents/XhUDXP7A67iHCD2kmbVu) ; [blog.google — SynthID Detector](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/synth-id-ai-content/).
- Reprise historique : [seroundtable.com — Merchant Center 42251](https://www.seroundtable.com/google-merchant-center-disapprove-products-chnage-fast-42251.html) ; [seroundtable.com — spam update done 42235](https://www.seroundtable.com/google-september-2026-spam-update-done-42235.html) ; [seroundtable.com — manual action spike 42258](https://www.seroundtable.com/google-search-manual-action-spike-42258.html).
- Analyse éditeur-outil : [semrush.com — track AI citations](https://www.semrush.com/blog/track-ai-citation-sources-semrush/) ; [searchengineworld.com — AI visibility buyer's guide](https://www.searchengineworld.com/buyers-guide-to-aio-geo-trackers-mentions-citaions-chatgpt-claude-google-llm).
- Reprise PPC : [ppcnewsfeed.com — Google warns fast changing products](https://ppcnewsfeed.com/ppc-news/2026-10/google-warns-fast-changing-products-may-be-disapproved/).
- Reprise technologique : [techcrunch.com — SynthID site](https://techcrunch.com/2026/10/07/googles-new-synthid-website-can-identify-ai-generated-media/).
- Podcast : [advancedwebranking.com — Generalist Renaissance](https://www.advancedwebranking.com/blog/strategic-marketing-for-ai-search).

Rien n'a été envoyé. Draft en attente de relecture Tim.
