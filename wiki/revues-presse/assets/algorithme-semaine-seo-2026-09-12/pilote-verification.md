---
type: audit
title: "Vérification de l'édition pilote hebdomadaire du 12 septembre 2026"
tags: [algorithme, fact-check, newsletter]
created: 2026-09-12
updated: 2026-09-12
sources: 8
confidence: medium
status: draft
---

# Vérification de l'édition pilote

Édition : [[revues-presse/2026-09-12-algorithme-semaine-seo]]. Format : [[methodes/format-algorithme-semaine-seo]]. Vérification Web effectuée le 12 septembre 2026 sur les sources identifiées dans le vault.

## Origines locales

- `agent-synthetic/MediaSEO/2026-09-11-MediaSEO.md` : Wikipedia, Web Search Service API, étude Ahrefs.
- `agent-synthetic/MediaSEO/2026-09-10-MediaSEO.md` : entretien Le Monde et annonce Tailwind.
- `agent-synthetic/MediaSEO/2026-09-09-MediaSEO.md` : blocs comparateurs Google.
- [[sources/2026-09-10-algorithme-leads-ia-7-conseils]] : priorité aux décisions et à la conversion.
- [[sources/2026-09-08-algorithme-ne-plus-vendre-audit-seo]] : ressource complémentaire sur le modèle de prestation.
- [[concepts/requete-cliquable-vs-clic]] et [[concepts/data-proprietaire]] : cadre d'analyse, sans reprendre leurs statistiques ou leurs extrapolations sur les algorithmes.

## Vérifications et limites

| Élément | Source consultée | Verdict et traitement |
|---|---|---|
| Le Monde : absence de baisse soudaine déclarée | [Entretien original, 8 septembre](https://www.influencia.net/louis-dreyfus-nous-navons-pas-constate-dimpact-dai-overviews-sur-nos-audiences/) | Déclaration vérifiée. Résultats internes non audités ; attribution explicite à Louis Dreyfus. Aucun effet causal démontré. |
| Wikipedia : estimations de −5,45 % et −4,82 %, révision du 2 septembre | [arXiv, résumé](https://arxiv.org/abs/2602.18455) et [texte intégral v6](https://arxiv.org/html/2602.18455v6) | Chiffres, comparaisons linguistiques et fenêtre décembre 2023 à décembre 2024 vérifiés. Travail de recherche, pas un taux universel. La révision précède la semaine ; le dossier l'indique comme repérée dans la veille. |
| Google : unités comparateurs dans l'EEE | [Documentation officielle](https://developers.google.com/search/docs/appearance/aggregator-unit) | Fonctionnement vérifié. La date affichée lors de la consultation est le 11 septembre, plus récente que celle notée dans le vault. Aucun impact chiffré sur le trafic repris. |
| Google : API et accord partenaire | [Documentation officielle](https://developers.google.com/web-search-service/overview) | Prérequis et date du 9 septembre vérifiés. Aucune affirmation sur la date de lancement initial, le prix ou une disponibilité générale. |
| Tailwind rejoint Shopify | [Billet d'Adam Wathan, 9 septembre](https://tailwindcss.com/blog/tailwind-is-joining-shopify) | Annonce, licence MIT, fermeture des nouvelles inscriptions commerciales et maintien des accès existants vérifiés. Engagements attribués à l'auteur. Aucun effet SEO prêté à l'opération. |
| Sélection Ahrefs | [Analyse originale du 27 août](https://ahrefs.com/blog/discussions-and-forums-serps/) | Auteur, contributrice, date et objet vérifiés. Ressource ancienne identifiée comme telle. Aucun pourcentage repris. |
| Positions de Tim | Deux fiches sources des éditions des 8 et 10 septembre ci-dessus | Attribution fondée sur les synthèses locales ; liens publics fournis. Les originaux Substack n'ont pas été revérifiés sur le Web pendant ce run. Aucun benchmark ni citation verbatim réutilisé. |
| Exemple hôtel, dix pages, quatre semaines | Proposition éditoriale | Exemple explicitement hypothétique et protocole proposé, pas cas client ni résultat observé. Pas de promesse de gain. |

Deux sources qui reprennent la même annonce ne sont pas une réplication indépendante. Cette édition vérifie l'existence des déclarations et des résultats publiés ; elle ne certifie pas leur validité externe. Le critère de deux preuves indépendantes de chaque effet n'est donc pas satisfait. Statut conservé : exemple local / draft, avec analyses attribuées et limites dans le texte.

## Éléments volontairement écartés

Les chiffres de trafic IA et d'impressions clients de l'édition du 10 septembre ne sont pas repris : la fiche locale signale des sources primaires manquantes et une ambiguïté sur les volumes. Les gains de temps et le pourcentage d'automatisation du 8 septembre ne sont pas utilisés comme benchmarks.

Les ratios de conversion du Monde ne sont pas utilisés, faute de définition et de volumes détaillés dans les éléments consultés. L'estimation de pertes mensuelles de Wikipedia n'est pas reprise ; l'attribution de cette extrapolation au seul média secondaire dans la fiche locale demande une vérification supplémentaire, le texte intégral contenant lui-même une annexe de calculs de trafic.

Le conflit de gouvernance d'Automattic est écarté : il prendrait de la place sans apporter une décision SEO suffisamment étayée pour cette édition.

## Titre et présentation

Titres envisagés : « AI Overviews : quelles visites valent encore le déplacement ? », « Quelles pages méritent encore votre budget SEO ? », « Ce que le trafic global masque dans vos résultats SEO ».

Titre retenu : le premier. Il pose la question précise à laquelle répond le dossier et relie lecture et action.

Version HTML autonome : palette blanc `#ffffff`, bleu pâle `#eaf2ff`, bleu profond `#193761`, texte `#202c40`, secondaire `#53627a`. Titres Avenir Next avec repli système, texte Georgia. Colonne de lecture unique, sommaire latéral sur grand écran, largeur de texte contenue. Pas de blocs de chiffres décoratifs, de fausses commandes audio ni de formulaires d'abonnement inactifs.

Vérification visuelle : navigateur intégré indisponible pendant ce run (aucun navigateur exposé par le runtime). Vérifications structurelles locales uniquement ; ne pas prétendre à une validation par capture d'écran.

## Révision visuelle

À la suite du retour de Tim, ajout d’une illustration générée avec l’outil imagegen intégré, d’un graphique SVG aux proportions exactes (5,45 et 4,82 sur une échelle de 0 à 6), de trois schémas de brèves, d’une décomposition visuelle de la requête et d’une frise du test. Le graphique dispose d’une présentation HTML plus lisible sur mobile. Les cinq fichiers images sont locaux et ont des textes alternatifs. Aucun nouveau résultat chiffré n’est introduit. Illustration inspectée ; contrôle visuel du navigateur indisponible.

Illustration conservée dans `assets/algorithme-semaine-seo-2026-09-12/illustration-ouverture.png`. Génération : outil imagegen intégré, sans CLI. Prompt : illustration éditoriale large en collage de papier et crayon, recherche donnant directement des réponses et site offrant une expérience concrète ; barre de recherche comme porte architecturale, feuilles de connaissance, porte vers une chambre d’hôtel et main qui l’ouvre ; bleu marine, cobalt, bleu pâle, blanc et touches jaunes ; sans texte, logo, robot ni cerveau.

## Captures originales et contrôle visuel final

Le 12 septembre 2026, ajout de quatre extraits capturés dans Chrome : titre arXiv, titre de l’entretien INfluencia, condition Client ID de Google et titre de l’annonce Tailwind. Le DOM et les textes des sources n’ont pas été modifiés ; les captures sont limitées aux extraits concernés. Leurs coordonnées, URL finales et dates sont consignées dans `assets/algorithme-semaine-seo-2026-09-12/captures-extraits.json`.

Le dessin simplifié de la brève Google est remplacé par l’image originale `https://developers.google.com/static/search/docs/images/aggregator-unit.png`, créditée à Google Search Central avec sa licence CC BY 4.0. Il s’agit d’un exemple de présentation fourni par Google, pas d’une recherche terrain personnelle.

La mise en page explique les différences de mesure Wikipedia/Le Monde, les éléments du bloc comparateur et la condition d’accès partenaire. Les légendes distinguent captures, schéma officiel, graphique dérivé et illustration générée. Les images peuvent être agrandies dans une fenêtre accessible au clavier.

Contrôle désormais réalisé dans Chrome local après constat de l’indisponibilité du navigateur intégré : rendu inspecté à 1440 px et 390 px, aucune image cassée, aucun débordement horizontal ni erreur JavaScript ; agrandissement et fermeture par Échap vérifiés. Résultats : `qa-rendu.json`, captures `qa-*.png` dans le dossier des assets. Cette vérification remplace la limitation de contrôle visuel signalée lors des premières versions.
