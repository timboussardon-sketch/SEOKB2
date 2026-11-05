---
type: query
skill: seo-page-statistiques
status: draft
created: 2026-10-30
updated: 2026-10-30
sources: 7
confidence: medium
tags: [statistiques, citations-ia, open-access, arxiv, pubmed, academic, paywall, formation-llm, retrieval]
---

# Publications académiques en libre accès vs revues fermées dans les citations IA (2026-10-30)

PubMed Central occupe 14,40 % du corpus d'entraînement The Pile d'EleutherAI, ArXiv en occupe 8,96 %. Ces deux plateformes en libre accès représentent ensemble 23,36 % du texte sur lequel les grands modèles de langage ont appris à raisonner. Malgré cette présence massive à l'entraînement, leur part dans les citations en temps réel reste minoritaire et mal mesurée. La raison n'est pas le statut d'accès libre des revues scientifiques — c'est la distinction entre mémoire paramétrique (ce que le modèle a appris) et retrieval runtime (ce qu'il récupère au moment de la requête). Ces deux objets sont confondus dans presque toutes les analyses du secteur.

---

## Les chiffres clés (vérifiés à la source)

**Corpus d'entraînement The Pile (EleutherAI, arXiv:2101.00027, 825 GiB total)**

- PubMed Central : 14,40 % du corpus (180,55 GiB) — XML/HTML structuré, texte intégral en accès libre
- ArXiv : 8,96 % (112,42 GiB) — sources LaTeX, pas les PDFs rendus
- PubMed Abstracts : 3,07 % (38,53 GiB)
- Total académique et biomédical dans The Pile : environ 26,43 %

Ces chiffres concernent The Pile (2021), le corpus public le mieux documenté. Les corpus d'entraînement des modèles commerciaux (GPT-5, Claude 4, Gemini 3) ne sont pas publics.

**Hallucinations de citations académiques — GhostCite (arXiv:2602.06718, 2026)**

Audit de 13 modèles de langage sur 56 381 articles issus de conférences d'intelligence artificielle, d'apprentissage automatique et de cybersécurité (2020-2025) :

- Taux d'hallucination : entre 14,23 % et 94,93 % selon le modèle
- 1,07 % des 56 381 articles contiennent au moins une citation invalide en 2025, soit une hausse de 80,9 % sur un an
- 76,7 % des relecteurs ne vérifient pas sérieusement les références générées par IA
- 87,2 % des 97 chercheurs interrogés utilisent des outils d'IA pour écrire ou référencer
- Filtrage multi-modèles : un consensus de plus de 3 modèles citant la même référence atteint 95,6 % de précision

**Profil des sources sur les requêtes médicales — Outcomes Rocket (août 2025)**

Analyse de 5 472 citations générées par ChatGPT, Claude, Gemini et Perplexity sur des requêtes de santé :

- PubMed Central : 385 citations, premier domaine cité toutes plateformes confondues (~7 % du total)
- Médias santé (WebMD, Healthline, etc.) : 30,7 %
- Sources académiques (revues, journaux) : ~23 % de l'ensemble
- Claude : 28,9 % de sources académiques (proportion la plus élevée des 4 modèles)
- ChatGPT : ~23 % de sources académiques, 35,8 % de médias santé
- Contenu généré par les utilisateurs et réseaux sociaux : 1,6 %

Note : cette étude est une source secondaire relayée par Digital Information World (26 septembre 2025). Les données brutes de l'étude primaire Outcomes Rocket n'ont pas été vérifiées par fetch direct.

**Biais d'autorité dans la recherche académique IA (arXiv:2609.00248, EMNLP 2026)**

Jinadu et al. ont testé 8 modèles de langage utilisés comme moteurs de recherche académique. En faisant varier uniquement les métadonnées d'autorité (nom d'auteur, revue, nombre de citations) tout en conservant titres et résumés identiques :

- Le biais d'autorité est « substantiel » et directionnel dans tous les modèles testés
- Un débiaisage par prompt réduit la mention de l'autorité dans les réponses mais corrige beaucoup moins bien les inversions de recommandation (écart entre "dire" et "faire")
- L'audit de surface sous-estime donc systématiquement le biais comportemental réel

**Couverture des outils de recherche académique à accès libre uniquement (Lau & Golder, 2025)**

Selon des résultats de recherche secondaires, les outils d'intelligence artificielle restreints aux sources en accès libre atteignent une sensibilité de 39,5 %, contre 94,5 % pour une recherche bibliographique complète traditionnelle. Ce chiffre concerne les outils spécialisés de recension de la littérature, pas les moteurs génératifs généralistes.

Note : source secondaire non vérifiée par fetch direct — voir section [À SOURCER].

---

## ArXiv : deux états selon le pipeline, non deux sources

ArXiv occupe 8,96 % du corpus The Pile. PubMed Central en occupe 14,40 %. Ces deux bases sont en accès libre. Pourtant, les études de citabilité IA les traitent comme des sources comparables à n'importe quel site web.

Un détail technique annule cette comparaison. Dans The Pile, ArXiv n'est pas ingéré en PDF : le corpus utilise les sources LaTeX (.tex) pour extraire le texte. PubMed Central est fourni en XML/HTML structuré. Les PDFs en tant que fichiers binaires sont sous-représentés dans les données d'entraînement réelles.

En retrieval runtime, la situation s'inverse. Les pages abs/ d'ArXiv (par exemple arxiv.org/abs/2602.06718) sont des pages HTML accessibles, indexables, à forte autorité de domaine. Les crawlers IA récupèrent ces pages et les intègrent dans leurs réponses. Les PDFs ArXiv, eux, ne sont presque jamais cités comme URLs .pdf dans les réponses génératives — ce que l'étude sur les PDFs du 25 août 2026 a documenté.

Le même article ArXiv existe donc dans deux états selon le pipeline :
- État 1 — mémoire paramétrique : le modèle a "lu" le texte LaTeX à l'entraînement. Il connaît le contenu.
- État 2 — retrieval runtime : la page abs/ est crawlée et récupérée comme source HTML.

Un article ArXiv est ainsi citable à deux titres distincts que les outils comme Profound, Peec AI ou Semrush ne distinguent pas. Le premier bénéfice est invisible aux mesures. Le second est mesuré mais partiel (seul l'abs/, pas le PDF).

---

## PubMed Central et la santé scientifique

PubMed Central dépasse ArXiv dans The Pile (14,40 % contre 8,96 %). Il représente la plus grande base de textes biomédicaux en accès libre. Pourtant, dans les réponses des moteurs IA sur les requêtes médicales, PubMed Central arrive premier domaine cité mais avec seulement ~7 % du total (385 citations sur 5 472), loin derrière les médias santé généralistes à 30,7 %.

Deux mécanismes expliquent l'écart entre la présence à l'entraînement et la présence dans les citations runtime :

Premièrement, les pages PubMed Central sont structurées pour les chercheurs : identifiants PMC, DOI, métadonnées techniques. Leur densité sémantique immédiatement extractible par un retrieval rapide est plus faible que celle d'un article vulgarisé sur WebMD ou Healthline.

Deuxièmement, la requête d'un utilisateur médical n'est généralement pas une requête de recherche académique. Elle correspond à une intention "Comprendre / Know", pas "Trouver un papier / Research". Les moteurs sélectionnent la source dont le format répond à l'intention, pas nécessairement la plus autoritaire scientifiquement.

Le résultat est une inversion structurelle : PubMed Central est plus présent dans la formation des modèles que la quasi-totalité des médias santé qui le surclassent à l'affichage des citations.

---

## L'avantage libre accès : corrélation ou artefact ?

La théorie courante dans le secteur est simple : un article en accès libre sera plus cité par les moteurs IA qu'un article payant, parce que le crawler peut le lire.

Cette théorie est partiellement vraie et globalement trompeuse.

Elle est vraie pour la presse généraliste. Les études sur les paywalls (données de la présente base, étude du 5 août 2026) montrent que les éditeurs à accès bloqué dur (WSJ, FT, Bloomberg) captent 0 % des citations dans les moteurs IA utilisant la recherche web en temps réel. Les éditeurs en accès libre y obtiennent 91,3 %.

Elle est trompeuse pour la littérature académique. La raison est que le vrai facteur n'est pas le statut d'accès libre de la revue, mais la présence du texte dans les données d'entraînement — qui est largement antérieure à toute restriction de robots.txt. Nature, Science et Elsevier bloquent les crawlers IA depuis 2023-2024. Mais leurs contenus publiés avant ce blocage sont déjà encodés dans les poids des modèles. Le modèle "connaît" un article Nature de 2019 — il ne peut simplement plus le citer comme source fraîche en retrieval runtime.

Il existe aussi un effet de sélection documenté par Jinadu et al. (EMNLP 2026) : les LLMs favorisent les sources à forte autorité perçue (auteur connu, revue reconnue, nombreuses citations). Cet effet de prestige peut surpasser l'effet d'accès libre dans certaines configurations — un article payant très cité est parfois mieux traité qu'un preprint obscur en accès total.

---

## Pourquoi ces chiffres demandent une lecture inverse

La confusion centrale de ce sujet est de traiter "libre accès" comme une catégorie homogène. Elle recouvre au moins quatre objets distincts :

**Objet 1 — Accès libre à l'entraînement** : le texte était disponible quand le modèle a été formé. Exemples : les 22+ millions d'articles PubMed Central (XML depuis 2000), les 2+ millions de préprints ArXiv (LaTeX depuis 1991). Ces textes sont encodés dans les poids du modèle indépendamment de tout robots.txt.

**Objet 2 — Accès libre au runtime retrieval** : la page HTML est crawlable aujourd'hui. C'est ce que mesurent les études de citabilité (Profound, Peec AI, SE Ranking). Les pages abs/ ArXiv et les pages NCBI PubMed Central entrent dans cette catégorie.

**Objet 3 — Paywall éditorial** : les articles derrière abonnement (Nature, Science, Elsevier, ACM Digital Library) ne sont pas crawlés à la requête. Mais le contenu pré-embargo est en mémoire paramétrique.

**Objet 4 — Accès libre formel, crawl bloqué en pratique** : certaines revues en or (gold OA) bloquent les robots IA malgré leur statut d'accès libre. À l'inverse, certains preprints sur serveurs institutionnels (HAL, SSRN) sont techniquement accessibles mais peu indexés.

La "prime à l'accès libre" documentée par la recherche bibliométrique classique (l'article OA reçoit plus de citations humaines) ne se transfère pas mécaniquement à la citabilité IA. Les deux systèmes fonctionnent selon des logiques distinctes.

---

## Nos propres chiffres (données de première main)

Le vault SEO-KB ne dispose pas d'une étude contrôlée sur les citations IA vers des sources académiques en accès libre vs payant. Ce bloc reste en réserve jusqu'à ce qu'un jeu de données propriétaire permette de combler le vide structurel identifié.

Le vide le plus documentable serait une comparaison directe, sur une même requête académique, entre la réponse d'un moteur IA et la source qu'il choisit (ArXiv abs/ vs PDF, PubMed Central vs Wiley Online Library) avec les métadonnées d'accès associées.

---

## Contre-analyse

**L'accès libre ne garantit pas la qualité du contenu récupéré.** L'étude de biais d'autorité (Jinadu et al., EMNLP 2026) montre que les modèles favorisent les sources prestigieuses même quand le contenu est identique. Une revue payante bien connue peut donc surclasser un preprint en accès libre sur des requêtes compétitives.

**Les données d'entraînement ne sont pas publiques pour les modèles récents.** The Pile date de 2021. GPT-5, Claude 4 et Gemini 3 incluent des corpus propriétaires, dont certains résultent de partenariats avec des éditeurs académiques sous licence (Wiley a annoncé un accord avec des acteurs IA en 2024, Springer Nature et Elsevier ont des discussions en cours). La part réelle de contenu académique payant dans les modèles actuels est inconnue.

**La hausse des hallucinations de citations ne concerne pas que le libre accès.** Les 14,23 % à 94,93 % de taux d'hallucination documentés dans GhostCite concernent toutes les citations, académiques ou non. L'accès libre d'une source ne réduit pas le risque qu'un modèle fabrique une référence qui lui ressemble.

**ArXiv subit ses propres problèmes de qualité.** En 2026, ArXiv a introduit une restriction d'un an pour les chercheurs soumettant du contenu entièrement généré par IA sans vérification (The Next Web, 2026). La plateforme doit donc gérer la montée en volume de preprints assistés par IA dans son propre écosystème.

**PubMed Central reste une ressource de premier rang en santé.** Malgré une position secondaire à l'affichage (30,7 % médias santé vs ~7 % PubMed Central), le fait que PubMed Central soit le premier domaine individuel cité reste significatif. Il surclasse tous les autres sites académiques et institutionnels sur les requêtes médicales.

---

## FAQ

**Les moteurs IA citent-ils plus souvent les articles en accès libre ?**
Sur les requêtes médicales, PubMed Central (libre accès) est le premier domaine cité individuellement, mais les médias généralistes de santé le dépassent en volume global. Sur les requêtes généralistes, les études académiques sont peu représentées dans les citations runtime, quel que soit leur statut d'accès.

**ArXiv est-il bien représenté dans les citations IA ?**
ArXiv est massivement présent dans les données d'entraînement (8,96 % de The Pile), ce qui donne aux modèles une connaissance profonde de son contenu. En retrieval runtime, ce sont les pages HTML abs/ qui sont citées — jamais les PDFs. L'étude bibliographique qui cherche à vérifier une citation ArXiv depuis une réponse IA doit donc chercher une URL abs/, pas une URL pdf/.

**Que valent les articles derrière paywall pour les moteurs IA ?**
Leur contenu est souvent en mémoire paramétrique si la publication date d'avant les restrictions de robots.txt (2023-2024). En retrieval runtime, les paywalls durs créent une exclusion totale des citations : 0 % pour WSJ, FT, Bloomberg dans les moteurs IA utilisant la recherche web en direct.

**PubMed Central est-il une source que les modèles hallucinent ?**
Moins que les revues académiques générales. Les pages NCBI sont stables, identifiables et à forte autorité de domaine. Le risque est surtout celui de la fabrication de DOI ou de numéros PMID plausibles mais inexistants — un problème commun à toute citation académique générée par IA.

**Le statut HAL en France change-t-il les résultats ?**
HAL est le serveur de preprints institutionnel français (CNRS, universités). Ses données ne sont pas séparément documentées dans les grandes études de citabilité IA. Son statut est analogue à ArXiv (accès libre total, pages HTML crawlables) mais son autorité de domaine est inférieure. Les données francophones sur ce point font défaut.

---

## [À SOURCER]

- **77,3 % à 91,8 % de citations LLM vers des sources en accès libre** (Naser, arXiv:2603.03299, 2026) — cette plage est apparue dans des extraits de résultats de recherche mais n'a pas été confirmée par le fetch de l'abstract ou du PDF. La méthodologie et la liste exacte des 10 modèles testés restent à vérifier.
- **Lau & Golder — sensibilité 39,5 % pour les outils IA restreints à l'accès libre** — source secondaire, non vérifiée par fetch direct.
- **Impact des partenariats Wiley/Springer/Elsevier avec les acteurs IA sur la composition des corpus d'entraînement récents** — aucune étude publique disponible.
- **Proportion exacte d'ArXiv dans les citations runtime (abs/ vs non-arxiv) par moteur désagrégé** — aucune étude disponible.
- **Données HAL et accès libre français** — absent de toutes les grandes études de citabilité IA.
- **LLM-assisted writing +7,04 % de citations reçues** (étude arXiv 2026, 234 073 papiers) — chiffre issu d'un snippet de résultat de recherche, à confirmer sur la source primaire.

---

## Sources

1. **Gao et al. — "The Pile: An 800GB Dataset of Diverse Text for Language Modeling"** — EleutherAI, arXiv:2101.00027, janvier 2021. Composition du corpus confirmée dans l'étude du vault du 25 août 2026. Consulté le 30 octobre 2026.

2. **GhostCite — "A Large-Scale Analysis of Citation Validity in the Age of Large Language Models"** — arXiv:2602.06718v2, 2026. 56 381 articles IA/ML et cybersécurité, 13 LLM. arxiv.org/html/2602.06718v2 — consulté le 30 octobre 2026.

3. **Naser MZ — "How LLMs Cite and Why It Matters: A Cross-Model Audit of Reference Fabrication in AI-Assisted Academic Writing and Methods to Detect Phantom Citations"** — arXiv:2603.03299, 7 février 2026. 69 557 instances de citations, 10 LLMs, 4 domaines académiques. arxiv.org/abs/2603.03299 — consulté le 30 octobre 2026. Les chiffres de 77,3 % à 91,8 % OA non confirmés par fetch de l'abstract — voir [À SOURCER].

4. **Jinadu et al. — "Authority Bias in Conversational Search Engines for Academic Paper Recommendation"** — arXiv:2609.00248, accepté EMNLP 2026 Main Conference. 8 modèles testés. arxiv.org/abs/2609.00248 — consulté le 30 octobre 2026.

5. **Outcomes Rocket — "AI's Sources of Truth: How Chatbots Cite Health Information"** — 5 472 citations de ChatGPT, Claude, Gemini et Perplexity sur des requêtes de santé, août 2025. Source secondaire via Digital Information World (digitalinformationworld.com/2025/09/ais-sources-of-truth-what-chatbot.html), consulté le 30 octobre 2026. Source primaire non vérifiée par fetch direct.

6. **Étude paywall du vault — "Paywall et citations IA en 2026 : 0 % pour le Wall Street Journal, 91,3 % pour l'open web"** — agent-synthetic/revuedepressIA/etudes-IA/2026-08-05-stats-paywall-citabilite-ia-penalite-mesuree.md — données 5WPR × Everything-PR, juillet 2026. Consulté le 30 octobre 2026.

7. **Étude PDFs du vault — "PDFs et documents non-HTML dans les citations IA"** — agent-synthetic/revuedepressIA/etudes-IA/2026-08-25-stats-pdf-documents-non-html-citations-ia.md — données The Pile (EleutherAI arXiv:2101.00027) et données Common Crawl CC-MAIN-2026-34. Consulté le 30 octobre 2026.
