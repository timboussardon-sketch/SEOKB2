---
name: strategie-mot-cle
description: "Stratégie d'un seul mot-clé business en trois étapes validées. « stratégie mot clé X », « quoi faire pour le mot clé X »."
---

# Stratégie d'un mot-clé business

## Quand utiliser ce skill

Agent principal de toute stratégie autour d'un seul mot-clé dans le coffre courant. Déclencheurs : « stratégie mot clé X », « stratégie contenu pour mot clé X », « stratégie de contenu pour X », « strat mot clé », « quoi faire pour le mot clé X » et leurs variantes. « Juste pour X » reprend ce workflow quand le contexte porte déjà sur cette stratégie. Qualifie le besoin business, cherche les micro-intentions et questions du terrain, puis note les preuves propriétaires. Trois livrables validés séparément ; cinq intentions et quinze questions sont des objectifs souples.

Travaille dans le coffre de la conversation (`pwd`), jamais dans un autre coffre par défaut. Un lancement concerne un seul mot-clé business, son offre et son audience. Si le mot-clé manque, demande-le. Lis la doctrine locale et les conventions du coffre avant de créer le dossier `wiki/strategie-mot-cle/`. Le workflow demeure une pré-décision soumise à l'utilisateur.

## Routage principal

Prends la mission principale dès que la demande porte sur la stratégie d'un mot-clé unique, y compris « stratégie contenu pour X » ou « quoi faire pour le mot clé X ». « Juste pour X » hérite du contexte actif ; sans contexte permettant d'identifier la mission ou le mot-clé, pose une seule question de clarification. N'interprète pas tout « pour X » isolé comme une demande de stratégie. Une recherche de mots-clés, un brief ou une rédaction explicitement demandés gardent leurs propres workflows.

Le workflow a trois étapes. **Une étape par réponse, puis arrêt.** Une correction refait l'étape en cours. Le silence, « continue » sans référence au livrable, ou une validation d'une autre étape ne valent pas accord. N'appelle `approve` qu'après validation explicite de l'utilisateur sur le livrable affiché. Ne pré-valide aucune étape et ne passe jamais de 1 à 3.

## Plusieurs mots-clés

Un lancement = un mot-clé. Cinq mots-clés donnent cinq stratégies indépendantes, chacune avec son état, ses sources et ses trois validations. Une validation d'un autre mot-clé ne vaut pas validation de celui-ci.

## Méthodes à charger réellement

1. Étape 1 : la méthode micro-intentions, dans `references/methode-micro-intentions.md` de ce skill. Conserve Know-Simple / Know / Do, la formulation naturelle et le filtrage business. Les règles ci-dessous priment sur ses quotas.
2. Étape 2 : le skill `geo-citations` du système (`../geo-citations/SKILL.md`). Applique ses règles de provenance et sa distinction présence/recommandation uniquement à un éventuel usage GEO. Le livrable courant est la liste des questions réelles des acheteurs. Préserve leurs formulations ; ne les transforme pas toutes en « quel prestataire recommandes-tu ? » ou en prompts ChatGPT. Une adaptation en panel GEO sera une sortie ultérieure distincte, sur demande de l'utilisateur. Aucun relevé payant ni cron n'est déclenché.
3. Étape 3 : relis les pièces du coffre liées à chaque intention et question. Qualifie leur pertinence et leur qualité avant de compter leurs catégories.

Si une des deux méthodes est absente ou illisible, arrête l'étape concernée et nomme le fichier manquant. `load-method` note le chemin et l'empreinte SHA-256 de chaque méthode dans le suivi ; ne présente pas une méthode simplement mentionnée comme une méthode chargée.

## Livrables et validation

Initialise le suivi avec `python3 <dossier du skill strategie-mot-cle>/scripts/workflow.py init --vault . --keyword "MOT-CLÉ"`. La commande indique les chemins du JSON de suivi et de la page Markdown. Si un état existe déjà pour ce mot-clé ce jour-là, reprends-le avec `status --state CHEMIN` ; ne repars pas de zéro. Avant chaque étape 1 ou 2, appelle `load-method --state CHEMIN --phase N` et lis sa sortie : le script charge les vrais fichiers sources, affiche leur méthode et enregistre leur empreinte. Produis les données de l'étape courante dans un JSON temporaire, puis appelle `submit --state CHEMIN --phase N --input FICHIER`. La remise est refusée si la méthode de l'étape n'a pas été chargée ou a changé. Le script valide aussi les nombres, les rattachements, les catégories et les preuves, puis régénère la page Markdown. Présente uniquement l'étape courante et attends l'utilisateur. Après son accord explicite, appelle `approve --state CHEMIN --phase N --message "ACCORD EXACT DE L'UTILISATEUR" --user-approved`.

### Étape 1 — qualification business puis micro-intentions

Avant toute proposition, retrouve dans le coffre : l'offre à vendre, le prospect à convertir, le problème concret résolu, l'action attendue et l'intérêt de ce mot-clé pour l'activité. Vérifie les URL existantes dans les inventaires et contenus disponibles. Si un point indispensable manque, pose une question groupée et reste à cette étape. « Aucune URL trouvée dans le périmètre vérifié » ne signifie pas « aucune URL n'existe ».

Vise cinq besoins utiles ; conserve trois ou sept si le dossier les justifie. N'invente jamais une intention pour remplir le quota. Fusionne les formulations qui expriment le même besoin de décision, y compris quand leurs mots diffèrent. Une micro-intention aide ce prospect à **comprendre, comparer, choisir ou acheter** : explique sa relation avec l'offre et sa différence avec les autres. Le simple enrichissement d'une page ne suffit pas. Distingue formulation observée et hypothèse.

Le JSON de phase 1 contient `business` (`offer`, `prospect`, `problem`, `conversion_action`, `keyword_value`, `sources`, et `user_context` si l'utilisateur fournit directement les informations), `existing_url` dans `business` (`status: existing|none_found`, `url`, `check`), `dedup_review`, `count_reason` si le nombre diffère de cinq, puis `micro_intentions`. Chaque intention porte `id: m1…mN`, `query`, `category`, `want`, `business_signal`, `decision_need` (besoin canonique pour dédoublonner), `buyer_task: comprendre|comparer|choisir|acheter`, `business_link`, `distinctness_reason`, `status: observed|hypothesis`, `source` et, si observée, `source_excerpt` exact. Présente le cadrage avec les intentions, puis attends la validation.

### Étape 2 — questions d'acheteurs, terrain d'abord

Après validation de l'étape 1, recherche dans cet ordre :

1. Appels, CRM, SAV et échanges commerciaux : questions, objections et critères de choix réels.
2. Search Console et recherches documentées. Une reformulation reste signalée ; une requête non interrogative peut donner une question dérivée, jamais un verbatim inventé.
3. Expertise métier documentée : fais expliciter le besoin qui motive la question.
4. Hypothèses IA, uniquement pour une lacune précise après les trois recherches précédentes.

Vise quinze questions utiles sans remplissage. Conserve le nombre justifié par les sources, supprime les doublons de besoin et rattache chaque question à une intention validée. La répartition par intention est libre. Dans chaque niveau, préserve le langage des acheteurs et les questions qui changent leur décision.

Le JSON contient `research_log` avec trois entrées ordonnées `tier: terrain|search|expertise`, `sources`, `finding`, et `unavailable_reason` si les pièces sont absentes. Il contient aussi `count_reason` si le nombre diffère de quinze, puis `questions` (`id: q1…qN`, `question`, `micro_id`, `origin: terrain|search|expertise|hypothesis`, `status: observed|expertise|hypothesis`, `source`, `source_excerpt`, `gap` pour toute hypothèse IA). Présente les questions dans cet ordre de priorité. Le statut observed désigne un besoin observé, pas nécessairement une question recopiée mot pour mot : conserve l'extrait original et précise toute reformulation dans la présentation. Arrête-toi pour validation.

### Étape 3 — matière propriétaire pertinente et qualifiée

Note tous les éléments réellement validés, même si leur total diffère de vingt. Une note `0–5` compte les catégories de preuves propriétaires **admissibles** : `contexte`, `methode`, `cas`, `verbatim`, `mesure`. Plusieurs pièces d'une même catégorie apportent des corroborations mais un seul point.

Pour chaque preuve, écris la réponse ou l'affirmation précise qu'elle soutient. Lis l'extrait dans sa source, puis vérifie le lien direct avec cette réponse, la fiabilité de son origine, son actualité pour le sujet et son exploitabilité (précision, contexte, droits ou confidentialité si concernés). Une date ancienne n'invalide pas automatiquement une méthode toujours applicable ; justifie son actualité. Ne déduis pas une date depuis un nom de fichier sans vérification et n'invente pas une période de mesure.

Une preuve indirecte, externe, peu fiable, périmée ou inexploitable reste visible avec la raison de son exclusion et vaut zéro. Une pièce vaguement liée au thème ne compte pas. Le script vérifie que les extraits existent dans les fichiers, exige les évaluations et calcule la note sur les seules catégories admissibles. Le jugement sémantique de pertinence et de qualité reste explicite et soumis à l'utilisateur.

Le JSON contient `scores`, avec les identifiants des intentions puis des questions validées : `id`, `response_target`, `score`, `missing`, `evidence`. Une preuve porte `kind`, `source`, `source_excerpt` exact, `detail`, `supports`, `proprietary` (booléen), `provenance_reason`, `relevance: direct|indirect|unrelated`, `relevance_reason`, puis `quality` : `reliable`, `current`, `usable` (booléens), `reliability_reason`, `freshness_reason`, `usability_reason`, `source_date` (date connue ou null), `checked_at` (date réelle du contrôle). Une mesure retenue précise `period` ; un verbatim retenu précise `attribution`.

Zéro preuve donne `score: 0` et `evidence: []`. Une note `1/5` indique un besoin de collecte pour bien traiter ce sujet ; sa valeur business reste indépendante. Présente notes, preuves retenues et écartées, données à collecter, puis attends validation.

## Règles de sortie

- Sauvegarde le Markdown dans le coffre courant, avec frontmatter local, wikilinks valides et un journal de validation. N'écris jamais dans `raw/`.
- La phase 3 ne déclenche ni brief, ni Hn, ni rédaction, ni création de page. Ces travaux ont leurs propres phases validées.
- Ne recommande aucune URL nouvelle sur le seul score de matière. Sépare la valeur business, la demande observée et la matière disponible.
- Si le coffre manque de preuves, une note basse et une liste de collecte sont le résultat correct.
