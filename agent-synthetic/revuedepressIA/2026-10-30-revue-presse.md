---
title: "Sortir d'AI Overviews fait aussi baisser les clics organiques, selon un test de Cyrus Shepard"
date: 2026-10-30
pilier_info_jour: niche-seo
agent: synthetic
voix: synthetic
sources_count: 7
---

# Sortir d'AI Overviews fait aussi baisser les clics organiques, selon un test de Cyrus Shepard

## En trois à cinq points

- Cyrus Shepard a publié le 29 octobre 2026 un test sur un site qui a utilisé le contrôle Google d'exclusion d'AI Overviews et d'AI Mode : les impressions IA sont tombées à zéro, et les clics organiques classiques ont baissé en même temps.
- Shepard parle d'un éventuel « SERP halo effect » : les citations dans les réponses IA soutiendraient aussi les clics sur les résultats bleus de la même page.
- Le test est petit, Shepard ne publie ni le volume de trafic, ni la méthode d'opt-out, ni l'ampleur de la baisse organique, ni les dates précises de mesure. Le CTR IA estimé est de 0,9 pour cent, dérivé d'une soustraction avant / après.
- Un essai randomisé de janvier à février 2026, 1 065 utilisateurs Chrome, trouvait de son côté que la présence d'un AI Overview réduit les clics sortants de 39,8 pour cent sur les requêtes concernées. Les deux signaux ne se contredisent pas forcément, ils mesurent des choses différentes.
- Volatilité SERP non confirmée toujours en cours selon Barry Schwartz, mise à jour du 29 octobre 2026, chatter élevé sur tous les trackers tiers.

---

## Info du jour (pilier Niche SEO) — Un seul site s'extrait d'AI Overviews, le trafic organique classique baisse aussi

### Le fait

Cyrus Shepard, consultant SEO et fondateur de Zyppy, a publié le 29 octobre 2026 sur Search Engine Land un test sur un site qui a activé l'option d'exclusion d'AI Overviews et d'AI Mode mise à disposition par Google via Search Console. Deux mesures ressortent, selon la couverture par [Search Engine Land, 29 octobre 2026](https://searchengineland.com/google-ai-opt-out-test-organic-clicks-drop-499898) :

- Les impressions dans les fonctionnalités IA de Google sont descendues à zéro après l'opt-out, ce qui est attendu.
- Les clics organiques du site sur les résultats classiques ont baissé en même temps, ce qui ne l'était pas.

Shepard estime, par soustraction entre les totaux avant et après le changement, que le taux de clics imputable aux AI Overviews était d'environ 0,9 pour cent sur ce site. Il formule une hypothèse : les citations dans les réponses IA soutiendraient aussi, de manière indirecte, les clics sur la même page quand elle apparaît ensuite dans la liste de résultats bleue. Il appelle cette hypothèse « Search SERP Halo Effect ».

### Les limites méthodologiques, qui sont celles qui pèsent le plus

Shepard présente le test comme un cas unique et prévient que le résultat peut varier. Plusieurs données manquent dans la publication, ce que relève explicitement l'article :

- Nom du site, secteur, volume de trafic absolu.
- Dates exactes de la période avant et après opt-out.
- Ampleur chiffrée de la baisse des clics organiques.
- Méthode d'opt-out retenue (toggle Search Console sur l'option « Exclude from AI Overviews and AI Mode », ou autre contrôle).

Un cas unique ne prouve pas la causalité. La baisse peut aussi venir d'une saisonnalité, d'un changement de contenu, d'un autre test en cours sur le site, ou d'un biais de mesure côté Search Console (le contrôle d'opt-out est récent et son impact sur le reporting est encore mal documenté).

### Le recoupement, qui ne doit pas se confondre avec le test de Shepard

Deux études publiques permettent d'encadrer la lecture. Elles mesurent autre chose, mais touchent le même objet, à savoir le lien entre présence IA et clics organiques.

- L'essai randomisé de Saharsh Agarwal (Indian School of Business) et Ananya Sen (Carnegie Mellon, Heinz College), déposé sur SSRN le 3 avril 2026 et révisé le 17 juin 2026, a observé 1 065 utilisateurs Chrome aux États-Unis entre le 7 janvier et le 10 février 2026. Résultat central relayé par [PPC Land](https://ppc.land/researchers-find-google-ai-overviews-cut-publisher-clicks-39-8/) : quand un AI Overview apparaît sur une requête, les clics organiques sortants chutent de 39,8 pour cent et les requêtes sans clic montent de 34,5 pour cent, les clics payants restent stables. Le dispositif est causal (assignation aléatoire d'une extension qui masque l'AI Overview). L'effet est concentré en haut de page.
- Seer Interactive, étude citée par Shepard et par [Search Engine Land, septembre 2025](https://searchengineland.com/google-ai-overviews-drive-61-drop-organic-paid-ctr-464212), observe une corrélation inverse quand on regarde le CTR par impression plutôt que le total : les pages qui apparaissent dans un AI Overview enregistreraient environ 120 pour cent de clics organiques en plus par impression affichée. Il s'agit d'une corrélation, pas d'une causalité démontrée.

Les trois mesures ne se contredisent pas forcément :

- Agarwal / Sen mesurent l'effet brut d'un AI Overview sur l'ensemble des clics sortants d'une requête. Cet effet est négatif en volume.
- Seer mesure, pour une page citée, le CTR conditionnel à l'impression. Il est positif par rapport à une page non citée.
- Shepard regarde ce qu'il se passe pour un site unique quand il se retire des deux surfaces IA simultanément. La baisse qu'il observe sur l'organique serait compatible avec le mécanisme Seer, si on accepte que la citation IA alimente aussi le CTR classique.

### Ce que votre lecture doit retenir, sans aller plus loin que la donnée

- Opter pour l'exclusion d'AI Overviews et d'AI Mode via Search Console ne garantit pas une neutralité sur le trafic organique classique, selon un seul cas documenté publiquement à ce jour.
- Mesurer la performance d'une page citée dans un AI Overview demande deux séries distinctes : clics organiques classiques sur la même URL d'un côté, impressions AI de l'autre. Agréger les deux dans un seul CTR masque le mécanisme.
- Les Reports « Generative AI » dans Search Console affichent les impressions mais pas les clics, selon [Search Engine Journal, 6 juin 2026](https://www.searchenginejournal.com/google-gives-sites-ai-search-opt-out-but-not-the-data-to-use-it/577978/), ce qui rend l'évaluation d'un éventuel effet halo difficile sur la seule plateforme Google.
- Un test de type Shepard, répliqué sur plusieurs sites et plusieurs secteurs, avec dates et volumes publiés, serait nécessaire avant d'intégrer l'hypothèse halo à une méthodologie de mesure.

### Lien doctrine interne

- La fiche concept « métriques de visibilité GEO » tient que la mesure fidèle passe par un signal aval (clics, conversions) séparé du signal direct (impressions, citations). Le test Shepard renforce cette séparation, puisque les deux signaux semblent bouger ensemble sur un cas, sans que ce soit prouvé causalement.
- La fiche concept « tabou visibilité » prescrit de ne pas réduire la mesure à un score de visibilité IA isolé. Le test Shepard, s'il tenait sur un panel plus large, montrerait précisément le risque d'une mesure unidimensionnelle.

### Trois prédictions binaires datées (candidates ledger)

- P-2026-10-30-1 : un éditeur SEO majeur (Ahrefs, Semrush, Sistrix, Lily Ray, Marie Haynes) publie une étude multi-sites qui reprend le protocole Shepard sur au moins dix domaines avec dates et volumes publiés, avant le 30 juin 2027. Confiance 0,40.
- P-2026-10-30-2 : Google documente officiellement, dans la Help ou le Search Central Blog, le périmètre exact du contrôle d'opt-out AI Overviews / AI Mode côté reporting Search Console (impressions comptées, clics attribués, interactions avec le rapport Web classique), avant le 30 avril 2027. Confiance 0,35.
- P-2026-10-30-3 : Shepard publie un follow-up avec site anonyme nommé, dates et graphique de baisse chiffré sur Zyppy Signal ou Search Engine Land avant le 31 décembre 2026. Confiance 0,55.

---

## Brèves

### Brève 1 — Actualité SEO : la volatilité SERP non confirmée continue d'octobre, Schwartz met à jour le 29 octobre

Barry Schwartz suit depuis le 16 octobre 2026 une séquence de pics de volatilité non confirmés par Google. L'article [SER 42379](https://seroundtable.com/google-search-ranking-volatility-42379.html), publié le 27 octobre et mis à jour le 29 octobre, décrit un spike plus important que le 24 octobre, du chatter communautaire en hausse, et plusieurs trackers tiers qui enregistrent des mouvements. Schwartz écrit dans la mise à jour du 29 octobre que la volatilité « continues to get more heated by the day ».

Les outils tiers nommés dans l'article sont Wincher, SEMrush, CognitiveSEO, AWR, Wireboard, Serpstat, SERPrecon, Mangools SERPWatcher, DataForSEO, AccuRanker Grump, Zutrix Tension, Mozcast, SimilarWeb, Sistrix et Algoroo. Les lectures précises ne sont pas publiées en texte dans l'article, seulement rendues en graphiques. Un commentaire de forum cité par Schwartz indique une lecture SEMrush à 9,4 points, qui est une déclaration utilisateur, pas une sortie d'outil.

Google n'a confirmé aucune mise à jour depuis la fin du September 2026 spam update, soit depuis le 8 octobre 2026 selon le [Google Search Status Dashboard](https://status.search.google.com/products/rGHU1u87FJnkP6W2GwMi/history). Deux lectures métier :

- Les sites qui subissent des mouvements depuis le 16 octobre ne peuvent pas rattacher la variation à un update officiel. Toute déclaration causale est une hypothèse.
- Les trackers tiers eux-mêmes ne s'accordent pas, Schwartz note que « the tracking tools may still be struggling to track the volatility ». Un même site peut recevoir des lectures opposées selon l'outil consulté.

### Brève 2 — GEO / search IA : la couverture d'AI Overviews sur les requêtes de marque atteint 82,91 pour cent au 29 septembre 2026, selon Ahrefs

Ahrefs a publié début octobre 2026 une étude sur 100 noms de marques tirés du classement Interbrand Best Global Brands 2025. Mesure effectuée en recherche branded, bureau, États-Unis. La progression mensuelle rapportée par [PPC Land](https://ppc.land/google-ai-overviews-now-hit-88-of-tracked-commercial-keywords-semrush-finds/) et par [Kompozy](https://kompozy.io/news/ai-overviews-expand-across-brand-searches) est de 61,3 pour cent en juillet, 65,1 pour cent en août, 73,3 pour cent en septembre, 82,91 pour cent au 29 septembre 2026. Le panel 100 marques passe de 5 marques déclenchant un AI Overview sur 98 requêtes exploitables au 1er juillet, à 63 sur 100 au 30 septembre.

Un deuxième acteur, DemandSphere, publie le 1er octobre 2026 une mesure dans le même ordre de grandeur sur un panel distinct. Google n'a pas commenté publiquement le saut.

Réserve méthodologique : Ahrefs mesure sur un échantillon de 100 marques globales en anglais, bureau, États-Unis. L'extension à d'autres pays, à d'autres langues et à des marques moyennes ou locales n'est pas documentée. La progression mesurée ne dit rien de la part des citations attribuables à chaque marque dans la réponse elle-même, qui est une question distincte (voir Ahrefs sur citations vs mentions, et Semrush AI Visibility Index couvert dans l'édition du 27 octobre).

### Brève 3 — Agentic Search : Walmart précise que les Agent Profiles arrivent en novembre, sans date exacte ni périmètre Sam's Club tranché

Walmart a lancé le 21 octobre 2026 son Agent Gateway, un serveur MCP qui permet aux agents IA approuvés de rechercher et d'acheter sur Walmart.com et Sam's Club. Dans le même billet, l'enseigne annonce des Agent Profiles qui séparent les achats d'un agent des commandes du compte, avec limites de dépense et approbations personnalisées. La mention précise de calendrier est « in the next month », soit novembre 2026.

Reprise par [TechCrunch, 21 octobre 2026](https://techcrunch.com/2026/10/21/while-amazon-blocks-ai-agents-walmart-rolls-out-the-welcome-mat/) et [AI Weekly](https://aiweekly.co/alerts/walmart-debuts-agent-gateway-mcp-server-and-agent-profiles-for-approved-ai), avec un relevé [PPC Land](https://ppc.land/) qui note que la question de l'activation Sam's Club le même jour que Walmart n'est pas tranchée publiquement. Les intégrations existantes nommées par Walmart dans l'annonce sont ChatGPT (OpenAI), Gemini (Google) et Muse (Meta). L'accès au Agent Gateway est en bêta sur invitation.

Pour un consultant, trois lectures opérationnelles tiennent dès à présent :

- Un marchand qui souhaite être présent sur Walmart via un agent doit se préparer à postuler à la bêta, puis à documenter sa catégorie produit, ses contraintes de retour et de prix dynamique côté MCP.
- Un consultant côté marque doit déjà séparer, dans son suivi, les visites humaines et les sessions agent sur ses canaux non-Walmart. Les Agent Profiles de Walmart entérinent la distinction, les autres plateformes suivront ou pas.
- Le contraste de positions (Amazon bloque les agents tiers, Walmart les laisse entrer sous conditions) est maintenant un fait public à documenter dans toute stratégie marketplace. Il n'oblige pas à migrer, il oblige à inventorier.

---

## Grille de score (agent 7)

- source_diversity : 7 sources indépendantes dans le corps (searchengineland, ppc.land, searchenginejournal, seroundtable, status.search.google.com, kompozy, techcrunch, aiweekly)
- claim_density : 11 claims verified dans le corps (info du jour 6, brève 1 2, brève 2 2, brève 3 1)
- novelty_score : 4 sur 5 (hypothèse halo effect formulée publiquement pour la première fois sur un cas documenté, mesure concurrente Agarwal / Sen rapportée en recoupement)
- doctrine_fit : 4 sur 5 (deux concepts internes articulés sans décoration)
- redite_risk : faible (sujet Shepard non traité précédemment, volatilité étendue au 29 octobre, Ahrefs branded searches 82,91 pour cent non repris, Walmart Agent Profiles calendrier précis non traité)
- clickbait_risk : faible (titre descriptif, sans promesse creuse)

---

## Rappel

Rien n'a été envoyé. Draft produit, à relire par l'humain avant toute publication.
