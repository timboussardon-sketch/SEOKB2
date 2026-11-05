---
titre: "Google retire la qualité d'image comme barrière d'inclusion dans Shopping Ads et Free Listings"
date: 2026-10-13
pilier_info_du_jour: Niche SEO
piliers_breves: ["Actualité SEO", "GEO / search IA"]
voix: SyntheticBrain
---

# Google retire la qualité d'image comme barrière d'inclusion dans Shopping Ads et Free Listings

## En bref

- Google a réécrit sa page d'aide Merchant Center "How to fix: Low image quality [image_link]" : les produits marqués en qualité d'image faible continueront d'apparaître dans les Shopping Ads et les Free Listings.
- L'ancienne formulation parlait d'empêchement d'affichage jusqu'à correction. La nouvelle ajoute explicitement : "Your product will continue to show in ads and free listings."
- Changement spotté par Hana Kobzova sur PPC News Feed, repris par Barry Schwartz le 12 octobre et par Luis Rijo le 13 octobre. Aucune annonce officielle Google, aucune date dans le change log.
- La règle 500×500 pixels reste la barrière binaire d'inclusion restante, avec effet au 31 janvier 2027.
- L'audit Merchant Center doit basculer : la disapproval image_link n'est plus une raison d'exclusion, c'est un pur signal de performance.

## Info du jour — Niche SEO : la qualité d'image sort du périmètre de disapproval produit

Pilier : **Niche SEO (e-commerce dépendant de Google Shopping)**.

Google a modifié sa page d'aide Merchant Center sur la qualité d'image faible, sans annonce et sans date de change log. La formulation précédente avertissait : "As a result, this product may be prevented from showing in ads and free listings until the image quality improves" ([Search Engine Roundtable, 12 octobre 2026](https://www.seroundtable.com/google-merchant-center-poor-image-inclusion-42273.html)). La nouvelle version ajoute une Note en encart : "Your product will continue to show in ads and free listings" ([PPC Land, 13 octobre 2026](https://ppc.land/google-stops-blocking-low-quality-product-images-from-ads-and-free-listings/)).

Hana Kobzova, qui a repéré le changement, l'a documenté sur PPC News Feed : "Previously, low image quality could prevent products from displaying in ads and free listings." La version archivée précédente, consultable sur web.archive.org, est datée du 4 septembre 2025 selon Barry Schwartz, ce qui place la modification quelque part entre fin 2025 et octobre 2026, sans précision.

Le drapeau "Low image quality" reste présent dans l'onglet "Needs attention" du Merchant Center. La correction reste proposée produit par produit ou en masse par export/réimport CSV. Mais la conséquence attachée au drapeau a disparu : le produit n'est plus bloqué, il reste affiché.

Google ne commente pas la raison du changement. La page d'aide ajoute une phrase sur la qualité d'image comme facteur de performance : la qualité "corrèle fortement avec l'engagement utilisateur et les clics" selon la formulation reprise par PPC Land. Google ne donne pas de chiffre à l'appui, et ne précise pas si ce signal entre dans le ranking enchères, dans la sélection organique Free Listings, ou dans les deux.

**Ce que le changement redéfinit pour l'audit Merchant Center.** Jusqu'ici, un audit catalogue traitait la ligne "Low image quality" comme une correction prioritaire : chaque produit flagué pouvait sortir de l'inventaire marchand jusqu'au remplacement de l'image. L'enjeu était binaire, inclusion ou exclusion. Désormais, la ligne reste présente comme signal mais n'implique plus d'exclusion. Elle rejoint la catégorie des "signaux de performance" dont l'effet est à mesurer plutôt que corrigé en priorité.

**Trois lectures pour un consultant Merchant Center.**

1. Mettre à jour les procédures d'audit interne : la disapproval image_link ne figure plus parmi les causes d'exclusion. Elle devient un indicateur de performance CTR, à hiérarchiser contre d'autres facteurs mesurables sur fenêtre glissante.
2. Rediriger le budget "fix low image quality" vers une mesure d'écart. Comparer CTR et conversion des produits restés en basse qualité d'image à ceux qui ont été repris. Google affirme une corrélation sans publier de magnitude, le consultant mesure l'effet dans son propre compte avant de reprioriser.
3. Conserver la discipline sur le seuil binaire restant : les images sous 500×500 pixels seront rejetées à partir du 31 janvier 2027. La page d'aide donne juillet 2026 comme début des avertissements, PPC Land cite une annonce du 14 avril 2026 pour ce seuil. Les deux dates ne portent pas sur le même événement, la date d'exécution 31 janvier 2027 reste identique dans les deux sources.

**Lien doctrine.** La page [[concepts/triade-serp]] distingue trois phases : document, passage, génération. L'inclusion dans le Merchant Center relève de la Phase 1 côté shopping : un produit est, ou n'est pas, dans le document index. La relaxation observée élargit l'ensemble des produits éligibles, elle ne change pas la Phase 2 (sélection par pertinence et performance) ni la Phase 3 (génération de la réponse ou de l'annonce). Pour la page [[concepts/metriques-visibilite-geo]], le signal "inclusion Shopping" sort du périmètre d'un indicateur à mesurer (il est désormais acquis pour les produits sous image faible qualité), ce qui concentre la mesure sur la densité et la position dans les blocs produits. Pour [[concepts/tabou-visibilite]], Google formalise ici la distinction qu'il appliquait déjà implicitement : la présence dans l'index n'est pas la performance, les deux se mesurent séparément.

**Cinq réserves.**

1. Pas de date officielle de prise d'effet. L'archive wayback du 4 septembre 2025 cite la version précédente ; la nouvelle a pu être poussée bien avant le signalement de PPC News Feed.
2. Pas de communication Google. Aucune entrée dans le Google Shopping change log, aucun billet Merchant Center blog, aucun post Barry Schwartz contredit par un porte-parole Google.
3. Pas de méthodologie publique sur ce que Google considère comme "image floue" ou "pixelisée". Le drapeau reste automatique sans grille publique.
4. Pas de voie d'appel documentée pour contester un drapeau "Low image quality". Les procédures d'audit interne doivent compter avec un drapeau qui peut varier sans explication.
5. La règle n'a pas été vérifiée côté annonceur sur un échantillon large de comptes. Un consultant qui audite un compte doit confirmer que la mention a bien remplacé l'ancienne sur sa version localisée.

**Trois prédictions datées.**

1. P-2026-10-13-1 (confiance 0,50) : Google ne publiera pas de change log documentant cette relaxation d'ici le 31 mars 2027. Signaux à surveiller : page Merchant Center change log, @GoogleAds et @GoogleSearchC sur X, Google Shopping blog.
2. P-2026-10-13-2 (confiance 0,45) : un cabinet tiers (Northern Commerce, Smarter Ecommerce, DataFeedWatch, Channable) publiera une mesure chiffrée de l'écart CTR ou conversion entre produits à image faible qualité et produits à image standard d'ici le 30 juin 2027.
3. P-2026-10-13-3 (confiance 0,35) : le seuil binaire 500×500 pixels sera reporté au-delà du 31 janvier 2027, ou phased out dans certaines verticales d'ici fin 2026.

## Brève 1 — Actualité SEO : la mesure consolidée du blocage SERP tiers

Pilier : **Actualité SEO**.

Deux publications post-18 septembre quantifient le blocage SERP tiers par Google avec une précision inédite depuis le premier signalement du 13 septembre. Nozzle a publié le 10 octobre une recherche sur 27,5 millions de SERPs, 660 000 mots-clés et 49 pays : 8,0 % des SERPs sont "poisoned" depuis le 13 septembre, contre 0,17 % en baseline. Le pic a atteint environ un quart des SERPs les 27-29 septembre, puis la plage s'est stabilisée entre 5 et 11 % par jour depuis le 1er octobre. 77,9 % des SERPs empoisonnés retrouvent leurs sites habituels dans les trois jours ([Nozzle, 10 octobre 2026](https://nozzle.io/research/poisoned-google-serps/)).

DemandSphere a publié de son côté le 7 octobre un billet "Spurious data in Google SERPs" dont Ray Grieselhuber, son CEO, résume le chiffre : environ 11 % des vérifications quotidiennes de SERPs renvoient des résultats aberrants ([PPC Land, 13 octobre 2026](https://ppc.land/google-returns-wrong-results-on-11-of-demandspheres-daily-rank-checks/)). Grieselhuber qualifie publiquement, sur LinkedIn le 12 octobre, la période depuis début septembre comme la "pire des 20 dernières années" pour l'acquisition de cette donnée, et il la décrit comme "la nouvelle réalité à venir".

Barry Schwartz a consolidé le 12 octobre le chœur des outils signalant des symptômes convergents : Sistrix, DataForSEO, SE Ranking (où un refresh manuel aide, selon Sarah Blocksidge), Advanced Web Ranking, Morningscore ont tous posté des notices ([Search Engine Roundtable, 12 octobre 2026](https://www.seroundtable.com/third-party-google-rank-tracking-broken-42272.html)). Ranktracker a repéré les anomalies autour du 17 septembre et restauré sa collecte le 1er octobre selon Dalin de Graff. Derek Perkins de Nozzle décrit l'approche de Google en trois volets : blocage IP large ciblant les proxys résidentiels, davantage de captchas, et injection de données aberrantes dans les SERPs suspects.

Google n'a fait aucune communication sur cette phase. L'unique déclaration disponible porte sur les goto redirects confirmés le 26 août : "a long history of deploying technical measures against evolving forms of abuse." Les chiffres 8,0 % Nozzle et 11 % DemandSphere mesurent des jeux de mots-clés différents, ils ne sont donc pas directement comparables et chaque vendeur a un intérêt commercial évident à publier ces mesures.

**Lecture opérationnelle.** Côté audit, la fiabilité des outils tiers de rank tracking et de mesure de présence IA n'est plus un acquis entre le 13 septembre et au moins le 1er octobre 2026. Un rapport mensuel qui s'appuie sur Sistrix, Semrush, Ahrefs ou AWR sur cette fenêtre doit être lu avec l'avertissement explicite que 5 à 11 % des positions mesurées peuvent être erronées sans alerte. Google Search Console reste la seule source first-party fiable sur les clics et impressions, mais sa couverture AI Overviews et AI Mode est séparée et sans clics ventilés.

## Brève 2 — GEO / search IA : Microsoft publie Decision-1, modèle de scoring en test dans Bing et Copilot

Pilier : **GEO / search IA**.

Microsoft a publié un modèle appelé Microsoft-Decision-1, décrit comme un "modèle de scoring de décision" visant la latence et la qualité sur des tâches structurées (routage, classification, priorisation, vérification, contrôle de workflow). Le modèle est accessible via Microsoft Foundry et OpenRouter ([Search Engine Roundtable, 12 octobre 2026](https://www.seroundtable.com/bing-microsoft-decision-1-42270.html)).

Rangan Majumder, Corporate VP Search & AI chez Microsoft, a confirmé sur X que Microsoft "expérimente avec [le modèle] dans Copilot" et le juge "assez bon". Krishna Madhavan de l'équipe Bing a répondu que l'équipe "expérimente toujours". Barry Schwartz note que Bing n'utilise pas le modèle pour toutes les requêtes ni tous les utilisateurs : il s'agit de tests, pas d'un déploiement généralisé.

L'article ne contient aucun chiffre de performance ni de benchmark. Microsoft positionne le modèle comme une alternative aux LLM pour des décisions à latence courte sur tâches structurées, sans publier de comparatif.

**Lecture opérationnelle.** Le point à surveiller est la différence revendiquée entre un LLM de génération et un modèle de scoring de décision pour des sous-tâches de pipeline search IA (routage de requêtes, choix de passages à retenir, vérification de citations). Si Bing bascule progressivement de telles sous-tâches sur Decision-1, les stratégies GEO orientées vers l'optimisation de passages pour LLM générateurs doivent considérer qu'un modèle non-génératif peut filtrer en amont ce que le LLM voit. Cette hypothèse reste à instrumenter.

---

Édition SyntheticBrain du 13 octobre 2026. Draft, rien n'a été envoyé.
