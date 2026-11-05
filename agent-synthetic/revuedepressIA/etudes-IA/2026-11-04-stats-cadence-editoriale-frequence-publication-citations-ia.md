---
type: query
skill: seo-page-statistiques
title: "Cadence éditoriale et fréquence de publication dans les citations IA : rythme régulier contre haute densité ponctuelle (2025-2026)"
tags: [geo, aeo, citations-ia, cadence-editoriale, fraicheur-contenu, topical-authority, chatgpt, perplexity, gemini, ai-overviews]
created: 2026-11-04
updated: 2026-11-04
sources: 7
confidence: medium
status: draft
---

# Cadence éditoriale et fréquence de publication dans les citations IA — 2026-11-04

Publier plus souvent produit-il plus de citations dans les moteurs IA ? La vraie réponse est : personne ne le sait, faute d'étude contrôlée. Ce que les données révèlent est plus utile : la cadence de mise à jour des pages existantes surpasse la publication de nouveaux articles comme signal de fraîcheur, les citations ont une durée de vie médiane de 4,5 semaines, et l'autorité de domaine confond toutes les mesures au point de rendre la fréquence seule non mesurable.

---

## Les chiffres clés (vérifiés à la source)

**Fraîcheur comme variable de publication**

- Pages citées par les IA mises à jour dans l'année : **72 %** (par date de mise à jour) contre **42 %** par date de publication — Seer Interactive, 7 683 pages citées, 47 097 citations sur ChatGPT, Gemini et Perplexity, mars-juin 2026.
- Pages "fraîches de l'ancien" (mises à jour dans l'année mais publiées il y a 2+ ans) : **plus d'un quart** de toutes les pages "fraîches" citées. Taux par moteur : ChatGPT 28 %, Perplexity 28 %, Gemini 27 % — même source.
- Pages citées mises à jour dans les 2 derniers mois : **5,0 citations en moyenne** contre **3,9** pour les pages non modifiées depuis 2+ ans — SE Ranking, 2 328 533 pages, plus de 500 000 prompts, analyse XGBoost, 2026.
- Âge médian du contenu cité selon le moteur (fenêtre de 6 mois) : Claude **5,1 mois**, Google AI **6,0 mois**, Gemini **7,8 mois**, ChatGPT **8,0 mois** — Discovered Labs, 2 millions de citations, 10 000 pages, 2026.

**Poids de la fraîcheur vs. autorité de domaine**

- Valeur SHAP de la fraîcheur dans le modèle AI Mode : **0,071** ; de ChatGPT : **0,018** — SE Ranking XGBoost (même étude).
- Valeur SHAP du trafic de domaine (AI Mode) : **0,63** — soit **9× la fraîcheur** dans ce modèle — même source.
- Autorité de domaine perçue par l'IA : SHAP moyen absolu **0,38**, soit **6× le facteur page-level le plus fort** (hors autorité) — Discovered Labs, 2 millions de citations, 2026.

**Demi-vie des citations : pourquoi la cadence compte**

- Demi-vie médiane d'une citation IA (toutes surfaces) : **4,5 semaines** — Scrunch/Stacker, 3,5 millions d'événements de citation, septembre 2025 – mars 2026, 120 000+ domaines, 8 secteurs.
- Par moteur : ChatGPT **3,4 semaines** (rotation la plus rapide), AI Mode **4,3 semaines**, AI Overviews **4,7 semaines**, Gemini **4,8 semaines**, Perplexity **5,8 semaines** (plus stable) — même source.
- Contenu distribué via réseau éditorial : demi-vie de **~10 semaines** contre 4,5 semaines hors réseau, soit **2,1×** — même source.

**Couverture thématique comme proxy de cadence**

- Corrélation (Spearman, intra-topic) entre couverture thématique d'un site et ses citations sur d'autres questions du même sujet : Google AI Overviews **0,29**, AI Mode **0,28**, Perplexity **0,25**, Gemini **0,20**, ChatGPT **0,13** — Wellows, 9 471 questions en anglais, 198 360 paires site-sujet, 92 112 sites, janvier-mai 2026.
- Note : l'étude précise explicitement que ces corrélations décrivent où les citations se concentrent, pas ce qui se passe quand on publie davantage.

---

## Pourquoi ces chiffres posent plus de questions qu'ils n'en résolvent

**Le vide expérimental central**

Aucune étude publiée en 2025-2026 ne mesure directement la fréquence de publication (articles par semaine ou par mois) comme variable contre les taux de citation des IA. Ce n'est pas un angle négligé : c'est un vide structurel documenté dans les études les plus rigoureuses (Wellows, Discovered Labs, SE Ranking). L'état des connaissances en novembre 2026 s'arrête à des proxies — fraîcheur de page, couverture thématique, demi-vie des citations — sans expérience contrôlée comparant "3 articles/semaine pendant 6 mois" vs "50 articles en 2 semaines" à qualité équivalente.

**Le facteur confondant principal : l'autorité de domaine**

Les grands sites publient plus de contenu ET bénéficient d'une autorité de domaine supérieure. SHAP 0,63 (trafic de domaine) contre 0,071 (fraîcheur) chez SE Ranking rend impossible d'isoler l'effet de la cadence : un site qui publie 3 fois par semaine voit ses citations progresser, mais la part attribuable à la fréquence seule reste non mesurable dans les corpus disponibles.

**Mise à jour > nouvelle publication comme signal de fraîcheur**

La données Seer Interactive tranche sur un point adjacent mais central : 72 % des pages citées sont fraîches par date de mise à jour contre seulement 42 % par date de publication. Autrement dit, maintenir un catalogue existant produit plus de pages "fraîches" aux yeux des IA qu'un rythme de publication soutenu. Les "fraîches de l'ancien" représentent plus d'un quart du stock cité. Sur ce seul critère, une stratégie de révision mensuelle d'un catalogue de 50 articles produit davantage de contenu citeable qu'un rythme de publication de 2 articles/semaine pendant 6 mois.

**La demi-vie de 4,5 semaines comme contrainte de cadence implicite**

La demi-vie médiane Scrunch/Stacker introduit une contrainte de cadence par l'arrière : si la moitié des citations disparaissent en 4,5 semaines, un site souhaitant maintenir un volume stable de citations doit renouveler son stock régulièrement. ChatGPT (3,4 semaines) est le moteur le plus exigeant en cadence ; Perplexity (5,8 semaines) tolère davantage l'espacé. Cette contrainte vaut pour le renouvellement du stock, pas pour la publication en rafale : une rafale de 50 articles créée en 2 semaines subit la même demi-vie que 50 articles publiés sur 6 mois, avec le même risque de cannibalisation interne.

---

## Nos propres chiffres (données de première main)

Le coffre ne dispose pas d'observations longitudinales permettant de comparer deux rythmes de publication à qualité de contenu constante. Les pages organikk.co suivies dans le vault (3 impressions à J+30 pour les pages outil, position 15 sur les requêtes correspondantes) n'ont pas été publiées selon deux cadences distinctes et ne peuvent pas répondre à la question posée.

Le vide de données de première main sur ce sujet spécifique est lui-même un signal : le problème de la mesure de la cadence pure (isolée de la qualité et de l'autorité) est un défi méthodologique non résolu même à l'échelle d'un consultant SEO qui contrôle ses propres publications.

---

## Contre-analyse

**La corrélation couverture thématique/citations n'implique pas la causalité**

Wellows (9 471 questions) trouve des corrélations 0,13 à 0,29 entre couverture thématique et citations sur un sujet. Ces corrélations décrivent où les citations se concentrent — les sites déjà cités sur un sujet le sont plus souvent sur d'autres questions du même sujet. Publier davantage de pages sur un sujet ne produit pas mécaniquement une couverture au sens Wellows, qui mesure les citations effectives, pas le nombre de pages publiées.

**Le contenu "evergreen" résiste sans cadence élevée**

Discovered Labs (2 millions de citations) documente une β = +0,05 pour l'âge de la page — un effet de compoundage graduel favorable aux pages établies. Les pages avec une forte couverture factuelle et une autorité de domaine suffisante persistent dans les citations sans mise à jour fréquente, ce qui contredit l'idée que toute stratégie de citation nécessite un rythme soutenu de publication.

**La demi-vie varie de 3,4 à 10 semaines selon la distribution**

La contrainte de cadence implicite de 4,5 semaines ne s'applique pas uniformément : le contenu distribué via un réseau éditorial tient ~10 semaines, soit 2,1×. La variable pertinente pour allonger la durée de vie d'une citation n'est pas le rythme de publication, mais la distribution via des mentions tierces — ce que les données Scrunch/Stacker mesurent directement.

**Biais de qualité non contrôlé dans toutes les études**

L'absence d'étude contrôlée sur la cadence tient précisément à ce problème : les sites à haute fréquence de publication ont souvent des budgets éditoriaux plus importants, des processus qualité plus robustes et une autorité de domaine supérieure. Isoler "plus de publications" comme variable causale dans les corpus observationnels disponibles reste non résolu.

---

## FAQ

**Quelle cadence de publication maximise les citations IA ?**
Aucune étude contrôlée ne répond à cette question en 2026. Les recommandations disponibles (2 à 15 articles/mois selon les sources) sont déduites des demi-vies de citations ou de l'expérience terrain de vendors, sans test comparatif rigoureux.

**Vaut-il mieux mettre à jour des anciens articles ou publier de nouveaux ?**
Sur le seul critère de fraîcheur, les mises à jour l'emportent : 72 % des pages citées sont fraîches par date de mise à jour contre 42 % par date de publication (Seer Interactive, 7 683 pages). Plus d'un quart des pages "fraîches" citées ont été publiées il y a 2+ ans.

**Quel moteur est le plus sensible à la cadence de publication ?**
ChatGPT a la demi-vie de citation la plus courte (3,4 semaines), impliquant un besoin de renouvellement plus fréquent. Perplexity est le plus tolérant (5,8 semaines). Les deux récompensent davantage l'autorité de domaine que la fraîcheur dans les modèles SHAP disponibles.

**La topical authority nécessite-t-elle un volume élevé de publications ?**
Pas directement. Wellows (9 471 questions) mesure la topical authority comme couverture thématique dans les citations effectives, pas dans le nombre de pages publiées. La corrélation topical coverage/citations (0,13-0,29) ne prouve pas qu'augmenter le volume de publication améliore la couverture.

**La fréquence de publication figure-t-elle dans les modèles ML de citabilité ?**
Pas comme variable indépendante. SE Ranking (XGBoost, 2,3 M pages) mesure la fraîcheur de mise à jour comme facteur (SHAP 0,071 AI Mode), pas la fréquence de publication. Discovered Labs (2M citations) ne teste pas la cadence.

---

## [À SOURCER]

- Comparaison contrôlée directe "cadence régulière vs rafale" à qualité équivalente : vide structurel, aucune étude publiée
- Effet de la fréquence de publication isolée de l'autorité de domaine : non mesuré
- 3,2× citations pour le contenu mis à jour dans les 30 derniers jours (attribué à ConvertMate 2026 par AuthorityTech) : non retrouvé dans la source primaire ConvertMate
- 200× plus rapide en visibilité IA à 12+ articles/mois optimisés (AuthorityTech) : chiffre non vérifié, source primaire non retrouvée
- Données France / français sur la cadence éditoriale et les citations IA
- 25,7 % de fraîcheur supplémentaire du contenu cité par IA vs organique Google (Ahrefs, 17M citations) : vérifié seulement via sources secondaires dans cette session
- Effet de la cadence de publication sur Claude et Copilot désagrégé

---

## Sources

| Intitulé | Organisme | Date | URL | Consulté |
|---|---|---|---|---|
| Study: Content Recency's Impact on AI Visibility in 2026 | Seer Interactive | 2026 | https://www.seerinteractive.com/insights/study-content-recencys-impact-on-ai-visibility-in-2026 | 2026-11-04 |
| How to Optimize for AI Mode (XGBoost, 2,3 M pages) | SE Ranking | 2026 | https://seranking.com/blog/how-to-optimize-for-ai-mode/ | 2026-11-04 |
| What actually drives AI citations: a statistical analysis of 2M AI citations across 10K pages | Discovered Labs | 2026 | https://discoveredlabs.com/research/what-drives-ai-citations | 2026-11-04 |
| Source Decay Research: The Stacker Network Effect on AI Citation Persistence | Scrunch/Stacker | 2026 | https://stacker.com/blog/source-decay-research-the-stacker-network-effect-on-ai-citation-persistence | 2026-11-04 |
| Does Topical Authority Show Up in AI Citations? What 9,471 Questions Reveal | Wellows | 2026 | https://wellows.com/research/topical-authority-ai-citations-study/ | 2026-11-04 |
| Content Formats for AI Citations: Ranked by Real Citation Data | MaxAEO | 2026 | https://maxaeo.ai/blog/content-formats-ai-citations/ | 2026-11-04 |
| AI Citation Half-Life Platform Refresh Playbook 2026 | AuthorityTech | 2026 | https://authoritytech.io/curated/ai-citation-half-life-platform-refresh-playbook-2026 | 2026-11-04 |
