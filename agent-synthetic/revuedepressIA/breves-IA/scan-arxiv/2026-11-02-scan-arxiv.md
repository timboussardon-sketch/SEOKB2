# Scan arXiv SEO/GEO, 2026-11-02

*Scan hebdomadaire de la littérature arXiv pertinente SEO/GEO/AEO. Collecte déterministe (API arXiv) + scoring /50. Aucun envoi, sous-doc de brèves.*

## Verdict de la semaine

5 candidats publiés entre le 25/10 et le 02/11, 3 retenus. Les trois mesurent la même chose sous trois angles : ce que les moteurs génératifs citent ne correspond ni aux résultats classiques, ni au trafic. Les AI Overviews santé citent 44,4 % du top 5 organique. Les citations IA d'actualité sont jusqu'à 2,08 fois plus concentrées que le trafic. Un modèle ouvert de 4B prédit la part de citation d'une page, mais seulement quand les sources sont déjà sélectionnées.

## Études retenues

### 1. AI Overviews santé : 56,7 % des affirmations citées sont appuyées par leur source (`Score : 37/50`)

**Source** : https://arxiv.org/abs/2610.39339
**Signal** : 🟡 À surveiller
**Impact business en 1 ligne** : sur une requête santé, être dans le top 5 organique donne moins d'une chance sur deux d'être cité dans l'AI Overview, et les éditeurs commerciaux passent devant les sources institutionnelles.

3 611 questions santé de benchmark, chaque AI Overview comparé aux cinq premiers résultats classiques de la même requête. Un AI Overview s'affiche sur 96,4 % des questions. Seuls 44,4 % des résultats du top 5 sont cités par l'AI Overview correspondant, qui surreprésente WebMD et Healthline face à Cleveland Clinic ou au NHS. Les pages citées obtiennent un score inférieur aux résultats classiques sur quatre des six critères de crédibilité testés. Après correction de l'erreur du classifieur, 56,7 % des affirmations citées sont appuyées par la page citée, et 20,8 % des affirmations sont des faits sans aucune citation. Notés sur des grilles rédigées par des médecins, les AI Overviews obtiennent 38,2 % des points, et leur exactitude n'a aucun lien avec l'ancrage dans les sources. Code et données publiés.

**Lien avec la doctrine du vault** : confirme sur la santé le constat du scan du 15 avril (moins de longue traîne, sources moins crédibles, [[sources/2026-04-15-scan-arxiv-15-avril]]) et ajoute deux chiffres absents du vault : le recouvrement AIO / top 5 et le taux d'affirmations appuyées. Touche [[concepts/grounding-score]] et [[concepts/e-e-a-t]] : être cité ne veut pas dire que la phrase qui cite dit ce que dit la page.

---

### 2. Prédire quelle page un moteur génératif va citer : un modèle ouvert de 4B (`Score : 34/50`)

**Source** : https://arxiv.org/abs/2610.38090
**Signal** : 🟢 Opportunité
**Impact business en 1 ligne** : un scoreur ouvert et gratuit de part de citation existe désormais, utilisable pour comparer plusieurs versions d'un passage avant publication.

229 requêtes GEO-Bench, dix moteurs qui reçoivent les mêmes cinq sources dans leur prompt. Le label d'une source est sa part de citation dans la réponse. Les moteurs sont d'accord entre eux à une corrélation de Spearman de 0,704 : c'est le plafond de référence. Jev et deux modèles de décision ouverts de 27B, sans entraînement, atteignent 0,575 à 0,578. Le modèle distillé publié (GEO Citation Ranker 4B, sur Hugging Face) atteint 0,542 à 0,549 sur trois seeds, écart avec Jev non distinguable de zéro sur 229 requêtes.

Limites lues dans le PDF : aucun moteur ne fait sa propre recherche : chaque source est réduite à ses 320 premiers mots et fournie dans le prompt. Le modèle prédit donc la citation une fois la page retrouvée, pas le fait d'être retrouvé. Les deux auteurs sont salariés de TW3 Partners, qui vend des services de visibilité générative sous le nom Citead, ce que le paper déclare.

**Lien avec la doctrine du vault** : Jev est l'outil de tri du vault (`jev/README.md`, TypeSafe System One, version 1.13 citée dans le paper). Le paper donne une mesure externe de Jev sur une tâche GEO, utile pour `jev/calibrer.py`. Relève de [[concepts/metriques-visibilite-geo]] et [[concepts/geo]].

---

### 3. Les citations IA d'actualité sont jusqu'à 2,08 fois plus concentrées que le trafic (`Score : 31/50`)

**Source** : https://arxiv.org/abs/2610.40164
**Signal** : 🔴 Menace
**Impact business en 1 ligne** : les moteurs génératifs redistribuent l'attention vers moins d'acteurs que le search classique, au détriment des petits éditeurs.

Base de propriété de 9 761 sites d'actualité construite depuis Wikipedia et Wikidata, indices de concentration pondérés par le trafic pour 77 pays, sept systèmes d'IA. Les distributions de citations des grands systèmes d'IA sont jusqu'à 2,08 fois plus concentrées que le trafic. Si les AI Overviews médiatisaient toute la recherche organique aux États-Unis, la hausse de concentration serait plusieurs fois celle associée aux fusions de médias fortement régulées. Interrogés dans la langue du pays, les systèmes citent de préférence les médias contrôlés par l'État. Jeu de données publié.

Périmètre limité à l'actualité. Rien dans l'abstract sur les requêtes commerciales ou B2B.

**Lien avec la doctrine du vault** : donnée mesurée pour un argument de [[concepts/geo]] : la part de citation se concentre davantage que la part de trafic.

---

## Écartés

- `2610.41124` : Quand les LLM déclenchent une recherche web (score 29/50) : 400 questions, 5 LLM commerciaux ; GPT-5 mini et Grok 4 Fast cherchent sur plus de 90 % des questions post-cutoff et 1 % des questions de culture générale, et l'absence d'indice temporel fait tomber le score de 0,72 à 0,57-0,58. Signal utile pour [[concepts/fraicheur-contenu]] et [[concepts/query-fan-out]], mais échantillon réduit, deux auteurs, pas de venue.
- `2610.39610` : GistRank, compression de passages pour le ranking listwise (score 22/50) : gain d'inférence ×14, aucune conséquence pour un consultant.

## Candidats à ingestion complète

`2610.39339` (AI Overviews santé) en priorité : chiffres neufs pour le vault, code et données publics, utile en prospection YMYL. `2610.38090` ensuite, surtout pour la mesure externe de Jev. Décision à Tim (§6.1 AGENTS.md).

## Candidat INFO DU JOUR newsletter Algorithme

Oui : `2610.39339`. Angle possible : « Google cite moins d'une page sur deux de son propre top 5 dans les AI Overviews santé ».
