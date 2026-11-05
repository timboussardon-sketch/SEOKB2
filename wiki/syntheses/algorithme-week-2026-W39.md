---
type: synthese
title: "Algorithme : Récap semaine 39 (2026-09-20 au 2026-09-26)"
date: 2026-09-27
week: 2026-W39
tags: [synthese, algorithme, recap-hebdo, ia, seo, geo]
status: draft
sources_count: 6
---

# Récap semaine 39 : la mesure casse partout, les citations IA ne paient toujours pas

> Synthèse des 6 revues de presse Algorithme entre le 2026-09-20 et le 2026-09-26. Le 25/09 n'a pas produit d'édition ; [[ops/sante-automatisations]] (relevé du 2026-09-26) confirme la revue de presse à jour, cadence 1 j, dernière sortie le 26/09 — ce n'est pas une panne.

## Tendance dominante

Quatre histoires de la semaine racontent la même chose sous quatre angles : la mesure standard ne dit plus ce qu'elle prétend dire. Les outils de suivi de positions perdent jusqu'à 80 % de leurs données depuis que Google a durci le tri robots/humains le 13/09 (21/09). Une étude Semrush sur 771 000 mentions IA de Boeing montre que le nombre de citations et le nombre de visites n'ont presque aucun rapport (22/09). Un survey de 45 études confirme qu'aucun score de présence IA ne se transfère d'un moteur à l'autre — 84,9 % des paires ChatGPT/Copilot/Google/Perplexity ne partagent pas une seule URL citée (24/09). Et le spam update du 24/09 prend jusqu'à 14 jours à se déployer, sept fois plus long que celui de juin, sans que Google explique pourquoi (26/09). Dans les quatre cas, le symptôme est le même : le chiffre qu'on vous vend (position, score de visibilité IA, cause d'une baisse de trafic) est devenu plus dur à vérifier, au moment précis où Google et OpenAI s'installent comme intermédiaires transactionnels — paiement natif dans Gemini activé par défaut sans consentement du marchand (23/09), Sponsored Agents d'OpenAI (24/09), fiches d'établissement réécrites par l'IA (21/09). On mesure moins bien un système qui décide de plus en plus à votre place.

## Pilier dominant : IA, 54 % du volume (14/26)

Quatorze items sur vingt-six relèvent de l'IA générative (citations, GEO, commerce agentique, publicité conversationnelle), douze du SEO classique (algo, outils, spam, données structurées). L'écart est faible, mais le sens du basculement compte plus que le ratio : les items SEO de la semaine (blocage des rank trackers, spam update, note vendeur, avis gelés) sont presque tous des dommages collatéraux de l'infrastructure IA en construction, pas des ajustements de pertinence classiques.

## Ce qui fait consensus

- **Une citation ou une mention dans une réponse IA ne se traduit pas en visite.** Confirmé par trois sources indépendantes : l'étude Agarwal & Sen sur 1 065 utilisateurs (clics organiques de 0,62 à 0,37 par recherche avec AI Overviews, seuls 7,1 % des clics sortants viennent des liens cités — 21/09) ; Semrush sur les sites industriels US (0,48 % des sessions viennent des assistants IA et du Mode IA, deux domaines seulement communs entre le top 15 des plus cités et le top 15 des plus visités — 22/09) ; le survey GEO de Martinez et l'étude de divergence cross-moteurs (0 % de recouvrement du top 5 sur 60 comparaisons entre ChatGPT, Copilot, Google et Perplexity — 24/09).
- **La mesure standard devient plus lente et plus opaque à vérifier.** Les outils de rang perdent jusqu'à 80 % de leurs données depuis le 13/09 (Nozzle, Sistrix, Search Engine Roundtable — 21/09), et le spam update du 24/09 s'annonce sur 14 jours contre 19h30 à 3 jours pour les trois précédents de l'année, sans qu'un site puisse distinguer cette cause d'une autre avant le 8/10 au plus tôt (ppc.land, ceci confirmé par Google Search Status Dashboard — 26/09).
- **Le contenu produit à l'échelle sans donnée propre au site reste la cible n°1 des systèmes anti-spam.** John Mueller sur un cas de pSEO combinant technologie/domaine/attribut : les systèmes de Google perdent confiance dans le site entier, pas seulement dans les pages fautives (Google Search Central — 20/09). Le spam update de septembre vise nommément l'abus de réputation de site et les domaines expirés rachetés pour leur ancienneté (documentation spam policies Google — 26/09).

## Ce qui fait débat

- **Tim corrige lui-même un chiffre qu'il a cité.** Le "+41 % de citations" en optimisant pour le GEO, répété depuis 2024, vient en réalité d'une seule configuration de test en laboratoire (contexte à 5 documents, papier Aggarwal et al.), pas d'une martingale généralisable — le survey de Martinez le documente, Tim le signale contre sa propre doctrine passée (24/09). Pas de désaccord entre deux experts nommés cette semaine, mais un exemple net de correction publique plutôt que de silence.
- Le chiffre de Search Engine Journal sur le State of Search 2027 (39 % de SEO qui perdent du trafic mais gardent leurs leads) circule sans nombre de répondants, période ni profil précisés — Tim le garde comme ordre de grandeur, pas comme fait établi (22/09).

## Signaux faibles à surveiller

- **Sponsored Agents d'OpenAI** — cité une fois (24/09), mais la régie publicitaire à agents atteint un rythme annualisé d'un milliard de dollars en moins de 200 jours, avec Shopify et HubSpot comme partenaires de lancement. À creuser : c'est la première publicité conversationnelle documentée dans un moteur de réponse, angle direct pour un article GEO/business.
- **Le catalogue "Agentic Resource Discovery" dans Lighthouse** — cité une fois (22/09), spécification signée Google, Microsoft et Hugging Face, déployée dans Chrome 156 sous deux semaines. Aujourd'hui un sujet de développeur, potentiellement le premier audit technique standard pour l'agentic commerce demain.
- **ChatGPT classé "Très Grande Plateforme de Recherche" par l'UE** — cité une fois (24/09, DSA, 159,1 millions d'utilisateurs actifs mensuels dans l'UE). À partir de décembre 2026, OpenAI devra publier un registre des publicités montrées aux Européens : première fenêtre publique sur les stratégies concurrentes en ChatGPT Ads.

## Angles à creuser semaine prochaine

### Angle 1 : Le score de visibilité IA que vous payez ne mesure rien
**Pourquoi maintenant** : trois études indépendantes cette semaine (Agarwal & Sen, Semrush, survey Martinez + étude de divergence cross-moteurs) démontrent chacune sous un angle différent qu'aucune métrique de présence IA ne prédit ni le trafic ni la citation sur un autre moteur. C'est la preuve la plus dense réunie à ce jour pour la position que Tim défend depuis le bootcamp : on ne vend plus du trafic, on vend de la performance, et le mot "visibilité" reste banni des propales ([[concepts/tabou-visibilite]]).
**Format suggéré** : article.

### Angle 2 : Votre fiche produit est la seule chose qu'un agent regarde avant d'acheter à votre place
**Pourquoi maintenant** : le paiement natif dans Gemini a été activé par défaut sur les boutiques Shopify US le 22/09, sans action du marchand, avec extension annoncée à l'hôtellerie et la restauration. L'angle est actionnable dès maintenant : un audit du flux Merchant Center (titre, prix, stock, retours) pour vérifier s'il y a assez d'éléments pour être préféré par la machine qui choisit.
**Format suggéré** : quick-win ou post LinkedIn.

---

## Index des éditions de la semaine

- [[raw/revue-de-presse/2026-09-20-revue-presse|2026-09-20]] — 0,05 sur 3 : le vrai score du llms.txt selon 130 experts
- [[raw/revue-de-presse/2026-09-21-revue-presse|2026-09-21]] — Vos rapports de positions mentent depuis le 13 septembre
- [[raw/revue-de-presse/2026-09-22-revue-presse|2026-09-22]] — Cité 771 000 fois par l'IA, 0,48 % de visites
- [[raw/revue-de-presse/2026-09-23-revue-presse|2026-09-23]] — Google a activé le bouton Acheter sur vos produits sans vous le demander
- [[raw/revue-de-presse/2026-09-24-revue-presse|2026-09-24]] — 85 % des citations IA ne se répètent sur aucun autre moteur
- [[raw/revue-de-presse/2026-09-26-revue-presse|2026-09-26]] — Le spam update de septembre dure 14 jours, Google ne vous préviendra pas

---

*Récap auto-généré chaque dimanche soir à partir de `raw/revue-de-presse/`. Pour traiter les angles : ouvre wiki/queries/ et créé un brief, ou wiki/posts-linkedin/ pour un draft.*
