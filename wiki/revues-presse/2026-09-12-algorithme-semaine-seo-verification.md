---
type: audit
title: "Vérification de la semaine SEO du 12 septembre 2026"
tags: [algorithme, fact-check, newsletter]
created: 2026-09-12
updated: 2026-09-12
sources: 8
confidence: medium
status: draft
---

# Vérification de l’édition n° 001

Édition : [[revues-presse/2026-09-12-algorithme-semaine-seo]]. Format : [[methodes/format-algorithme-semaine-seo]]. Version complète locale demandée par Tim, sans publication externe. Le pilote précédent est conservé dans les fichiers pilote.html, pilote.md et pilote-verification.md du dossier assets.

## Traçabilité depuis le vault

- `agent-synthetic/revuedepressIA/2026-09-11-revue-presse-v2.md` : sélection Similarweb, nouvelle ouverture du dossier.
- `agent-synthetic/MediaSEO/2026-09-09-MediaSEO.md` : bloc comparateurs.
- `agent-synthetic/MediaSEO/2026-09-11-MediaSEO.md` : Web Search Service API.
- `agent-synthetic/MediaSEO/2026-09-10-MediaSEO.md` : entretien INfluencia avec Louis Dreyfus.
- `agent-synthetic/MediaSEO/2026-09-08-MediaSEO.md` : analyse Common Crawl.
- [[sources/2026-09-10-algorithme-leads-ia-7-conseils]] et [[sources/2026-09-08-algorithme-ne-plus-vendre-audit-seo]] : positionnement et ressources Tim.
- [[concepts/requete-cliquable-vs-clic]] : cadre des pages décisionnelles.

## Sources vérifiées le 12 septembre

| Sujet | Source originale | Traitement |
|---|---|---|
| Usage conjoint IA et recherche : 89 % | [Communiqué Similarweb, 10 septembre](https://ir.similarweb.com/news-events/press-releases/detail/160/similarweb-state-of-ecommerce-2026-report-details-how-ai-is-changing-shopper-journey) | Dénominateur explicité, aucune extrapolation à tous les acheteurs. Les estimations du fournisseur ne sont pas une preuve causale. |
| Referrals IA : 0,4 % ; croissance annuelle 203 % | [Présentation du rapport](https://www.similarweb.com/corp/reports/state-of-ecommerce-2026/) | Deux métriques de trafic direct, pas de ventes. Même producteur que le communiqué, pas une corroboration indépendante. |
| Comparateurs dans l’EEE | [Google Search Central](https://developers.google.com/search/docs/appearance/aggregator-unit) | Dernière mise à jour 11 septembre, pas une date de lancement déduite. Fournisseur développé par défaut, destination comparateur, éligibilité. |
| API sous accord partenaire | [Google](https://developers.google.com/web-search-service/overview) | Documentation datée du 9 septembre ; ni accès universel ni tarif inventé. |
| Audiences Le Monde | [INfluencia, 8 septembre](https://www.influencia.net/louis-dreyfus-nous-navons-pas-constate-dimpact-dai-overviews-sur-nos-audiences/) | Déclaration attribuée, pas un audit des résultats ni une causalité établie. |
| llms.txt : 584 107 fichiers ; 22,56 % sans lien | [Common Crawl, 31 août](https://commoncrawl.org/blog/a-content-analysis-of-llms-txt-files-from-the-july-2026-crawl-archive) | Lecture antérieure repérée cette semaine. Ne mesure pas les performances SEO/IA. |

## Choix éditoriaux et exclusions

Le dossier ne reprend pas l’interprétation causale des recommandations de marques dans la note Similarweb. Aucun taux de visite ultérieure n’est assimilé à un achat. Le parcours hôtelier est explicitement illustratif. L’exercice sur dix prospects recueille des indications qualitatives et n’est pas présenté comme un échantillon représentatif.

Les affirmations du vault sur une fermeture de Content API et de nouveaux indicateurs Merchant Center datés de septembre n’ont pas trouvé de confirmation dans les pages officielles consultées : elles sont exclues. La brève pSEO de John Mueller n’est pas retenue, la vérification du message original étant incomplète. Tailwind est retiré pour recentrer la sélection sur le SEO.

Les chiffres de performance clients et gains de temps des éditions Tim ne sont pas repris.

## Visuels et contrôle

Illustration d’ouverture générée par IA conservée et légendée. Graphique HTML à 89 % proportionnel, responsive et avec dénominateur explicite. Parcours client en trois étapes, identifié comme exemple. Captures originales des titres Similarweb, INfluencia, Common Crawl et de la condition d’accès API Google. Le schéma de comparateur est l’illustration officielle Google, créditée CC BY 4.0, pas une capture de SERP personnelle.

Métadonnées des nouvelles captures : `assets/algorithme-semaine-seo-2026-09-12/captures-edition.json`. Métadonnées des précédentes : `captures-extraits.json`. Chrome capture le DOM original sans substitution de texte.

Contrôle sur Chrome séparé : largeurs 1440 et 390 px, images chargées, débordement horizontal, erreurs JavaScript et ouverture/fermeture du zoom au clavier. Résultats : `qa-rendu.json`. Captures desktop et mobile inspectées. Le navigateur intégré n’était pas disponible.
