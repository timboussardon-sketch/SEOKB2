---
name: seo-contenu-pertinence
description: "Audit de la pertinence du contenu des pages business : intention, questions, preuves, title, meta. « audit de contenu »."
---

# Skill — Contenu et pertinence

## Quand utiliser ce skill

Audit de la qualité et de la pertinence du contenu réel des pages business d'un site. Pas la structure des titres (`seo-structure-hn` s'en charge, en sous-contrôle), mais la réponse elle-même : la page répond-elle à la bonne intention dans le bon format, couvre-t-elle les questions qui comptent pour la décision du lecteur, ses affirmations importantes sont-elles crédibles et vérifiables, apporte-t-elle une valeur propre ou une reformulation lexicale d'une page déjà en ligne. Contrôle systématique des balises title et meta description sur les pages prioritaires, jusqu'ici seulement un levier quand `seo-quick-win` détecte un gap CTR, jamais un contrôle en soi. Périmètre : pages business prioritaires + échantillon motivé des autres familles de pages, jamais l'exhaustivité du sitemap. Brique de l'onglet « Contenu et pertinence » de `audit-complet-v2`, chaînée avec `seo-structure-hn` ; alimente la dimension « Contenu & adéquation business » (20 pts) du Score SEO global, qui n'avait aucun protocole de mesure avant ce skill. Sortie obligatoire en plus du tableau : un rapport de pré-décision (diagnostic, preuves typées, état Critique / À améliorer / Sain, actions P1-P3 avec confiance, effort et risque, jamais de score affiché) ; sans lui le skill n'a pas terminé.

TOUJOURS utiliser ce skill quand l'utilisateur dit : "la page répond-elle à la question", "audit de contenu", "qualité du contenu", "cette page a-t-elle de la valeur", "utilité du contenu", "cette page répond-elle à l'intention", "contrôle des title et meta", "le contenu est-il crédible", ou comme brique de l'onglet « Contenu et pertinence » de `audit-complet-v2`.

## Quand déclencher

- Brique de l'onglet « Contenu et pertinence » de `audit-complet-v2`, chaînée avec `seo-structure-hn` (le Hn y reste, en sous-contrôle)
- Diagnostic d'une page au Hn sain et à la structure propre qui ne ranke ni ne convertit : la charpente peut être bonne et la réponse vide
- Avant une réécriture, pour savoir QUOI réécrire, pas « plus de mots »

Diffère de `seo-structure-hn` (qui audite la charpente : H1-H6, hiérarchie, gabarit) : ici on audite ce qu'il y a DANS la charpente, la réponse apportée.

Diffère de `seo-brief-contenu` (qui construit un brief AVANT rédaction) : ici on audite un contenu qui EXISTE déjà.

## Doctrine 

Créé parce que le Score SEO global de `audit-complet-v2` pèse « Contenu & adéquation business » à 20 pts, la deuxième dimension la plus lourde après l'indexation, sans qu'aucun protocole ne l'ait jamais mesurée. L'onglet qui portait ce rôle (« Structure des titres ») ne contrôlait que les Hn, les micro-intentions GSC et la sélection des mots-clés business : jamais la réponse du contenu lui-même.

- On ne compte pas les mots. La question n'est jamais « la page fait-elle assez long » mais « quelle question importante reste sans réponse ».
- Une page commerciale, un comparatif, un outil et un guide ne répondent pas au même besoin, même sur un mot-clé proche. Le format attendu se lit sur les résultats réellement présents dans la SERP visée, dans le marché ciblé, pas déduit du mot-clé seul.
- Les affirmations importantes se vérifient : exemples, démonstrations, sources, expérience réelle, conditions et limites. Seulement ce qui est pertinent pour le sujet, jamais une liste E-E-A-T cochée par principe ni transformée en score.
- Une page doit apporter une valeur propre : une information, une démonstration, une méthode, des données, une aide à la décision. Une reformulation lexicale d'une autre page du site n'en est pas une.
- Le title et la meta description se contrôlent systématiquement sur les pages prioritaires : descriptifs, distinctifs des autres pages du site, cohérents avec le contenu réellement servi. Pas seulement proposés comme levier quand un gap CTR apparaît.

## Input requis

| Source | Obligatoire |
|--------|-------------|
| Liste des pages business prioritaires (Phase 0 du workflow / `seo-top20-mots-cles-business`, ou fournie par l'utilisateur) | Oui |
| Accès au contenu réel des pages (Chrome ou `curl`) | Oui |
| Recherche web sur les requêtes prioritaires, pour voir les résultats réellement en SERP | Oui |
| Export GSC (position, impressions par page) | Recommandé : sans lui, on ne priorise pas par exposition réelle |

## Périmètre

Jamais l'exhaustivité du sitemap. Auditer :

1. Toutes les pages business prioritaires (celles de la Phase 0).
2. Un échantillon motivé des autres familles de pages : au moins une page par famille éditoriale identifiée en Fiche d'identité, choisie pour une raison dite (la plus exposée en GSC, la plus représentative du gabarit), jamais un tirage au hasard.

Une première décision utile ne demande pas l'analyse éditoriale de toutes les URL.

## Pipeline (5 étapes)

### Étape 0 — Savoir quelle version de la page on lit

Avant de juger la réponse d'une page, le contrôle du rendu de `indexation-check` doit avoir tourné sur elle ou sur son gabarit (HTML initial → DOM rendu → version vue par Google). Si le contenu principal n'apparaît qu'après rendu, lire le DOM rendu, et le dire dans la ligne du tableau (« lu sur le DOM rendu »). Une page en « suspicion de dépendance au rendu » non vérifiée ne se note pas : elle attend, avec la mention. On ne juge pas une réponse dont on ne sait pas quelle version on a lue.

### Étape 1 — Déterminer l'intention et le format attendu

Pour chaque page du périmètre, recherche web sur sa requête prioritaire : quels types de résultats dominent réellement (page commerciale, comparatif, outil, guide, annuaire, forum) ? Le format attendu vient de ce qui est là, dans le marché ciblé. Ne jamais le déduire du mot-clé.

### Étape 2 — Auditer la page sur 4 contrôles

1. **Intention et format** : la page correspond-elle au format dominant relevé en étape 1 ? Un guide long sur une requête à intention d'achat est hors format, même bien écrit.
2. **Couverture des questions qui comptent** : lister les questions qu'un lecteur en situation de décision se pose sur ce sujet précis, puis nommer celles que la page laisse sans réponse. Pas un comptage de mots.
3. **Crédibilité des affirmations importantes** : chaque affirmation qui pèse sur la décision (prix, méthode, résultat, comparaison, délai) a-t-elle un exemple, une source, une donnée, une expérience réelle documentée à l'appui ? Seulement les affirmations qui comptent pour le sujet, pas une grille E-E-A-T généralisée.
4. **Valeur propre** : la page apporte-t-elle une information, une démonstration, une méthode, une donnée ou une aide à la décision qui n'existe pas déjà, telle quelle, sur une autre page du site ? Si le doute porte sur deux pages précises, lire les deux, puis renvoyer vers `seo-cannibalisation` pour la confirmation GSC.

### Étape 3 — Contrôler title et meta description

Pour chaque page du périmètre, pas seulement celles remontées par `seo-quick-win` : le title est-il descriptif, distinctif des autres pages du site, cohérent avec le contenu réellement servi ? Même question pour la meta description. Un title générique, ou dupliqué sur plusieurs pages d'un même gabarit, est une anomalie de fond, pas un simple levier de CTR.

### Étape 4 — Croiser

- Avec `seo-structure-hn` : une page qui échoue les contrôles 2 à 4 alors que son Hn est sain confirme que le problème est dans la réponse, pas dans la charpente. Le dire tel quel : « H1 cohérent, mais la page ne répond pas à la question principale ».
- Avec `seo-cannibalisation` : deux pages qui échouent le contrôle 4 l'une contre l'autre sont un signal de cannibalisation à vérifier côté GSC, pas une conclusion.
- Avec la Phase 0 : une page qui échoue le contrôle 1 sur une intention à fort enjeu business remonte en priorité haute.

### Étape 5 — Prioriser

Pages business prioritaires en tête. Dans l'échantillon des autres familles, une page qui échoue trois contrôles passe devant une page qui n'en échoue qu'un.

## Sortie de pré-décision (obligatoire)

Ce skill n'a pas terminé tant que le rapport de pré-décision n'est pas écrit. Il fait partie de la sortie, au même titre que le tableau, et il suit `audit-complet-v2/rapport-audit-seo-format.md` (`audit-complet-v2/rapport-audit-seo-format.md`). Fichier : `wiki/audit/YYYY-MM-DD-slug-contenu-pertinence.md` en usage autonome, ou intégré à l'onglet « Contenu et pertinence » en usage via `audit-complet-v2`.

Ce qu'il contient, dans cet ordre :

1. Diagnostic principal : une phrase, la cause structurante, pas une liste d'anomalies
2. Les chiffres à retenir : 3 à 5
3. État : Critique, À améliorer ou Sain, calculé sur l'impact business réel (pages prioritaires touchées), jamais sur le nombre de pages en défaut ; jamais de score sur 10
4. Problèmes (3 maximum) et opportunités (5 maximum), séparés : chacun avec Preuve (2 à 4 données), Pourquoi c'est important, Action, Confiance (forte / moyenne / faible) ; chaque problème s'écrit en trois temps : observation prouvée → conséquence ou risque justifié → bénéfice attendu de la correction (l'observation seule n'est pas un frein SEO démontré)
5. Actions P1 / P2 / P3, 3 P1 maximum : pourquoi, preuve, signal attendu (jamais un résultat chiffré promis), dépendance préalable, test de validation (ce qui distingue « correction appliquée » de « résultat SEO observé »), effort Faible / Moyen / Élevé (jamais en heures), confiance, risque Faible / Moyen / Élevé ; toute réécriture à l'échelle d'un cluster porte « À valider avant déploiement »
6. Ce que les données ne permettent pas de conclure

Règles : chaque contrôle est jugé page par page, jamais fondu dans un score composite ; une page « échoue » un contrôle seulement si la question précise qui manque est nommée, jamais un « contenu insuffisant » vague ; jamais de recommandation automatique de réécriture en masse sans échantillon validé par l'utilisateur d'abord ; Google n'est jamais anthropomorphisé ; phrases courtes, une donnée par diagnostic, aucune des phrases « Il est important de », « Il convient de », « Cela peut potentiellement », « Il est intéressant de noter », « Dans le cadre de ».

Restitution : aucun ID technique ni mot anglais dans le rapport ; Faible / Moyen / Élevé partout ; la certitude affichée ne dépasse jamais la couverture des données (« sur les N pages lues », jamais « le site ») ; limites de longueur : diagnostic 70 mots, 4 chiffres, 3 problèmes de 40 mots, 6 actions, 3 opportunités de 35 mots, le reste dans les détails repliés.

## Sortie obligatoire

```markdown
# Contenu et pertinence — {domaine} — {date}

[Nombre] pages business prioritaires lues + [nombre] pages en échantillon motivé ([familles couvertes]).

## Tableau par page

| URL | Format attendu (SERP) | Format servi | Question(s) sans réponse | Affirmations non étayées | Valeur propre | Title / meta | Verdict |
|---|---|---|---|---|---|---|---|

## Anomalies critiques (en tête)

- {page business qui ne répond pas à la question principale de sa requête}
- {title générique ou dupliqué sur une page prioritaire}
- {page sans valeur propre face à une autre page du site}

## Recommandations par page prioritaire

La question qui manque, nommée. Jamais « enrichir le contenu ».

Exemple de conclusion attendue :

> La page vise une recherche de prix, mais ne donne ni tarif, ni fourchette, ni facteurs de variation. Son H1 est cohérent, mais elle ne répond pas à la question principale. Priorité : rendre le coût compréhensible, pas ajouter des H2.

## Limites

- {échantillon motivé, pas l'exhaustivité du sitemap : dire quelles familles n'ont pas été lues}
- {crédibilité jugée sur ce qui est vérifiable depuis la page, pas sur l'expertise réelle de l'auteur}
- {format attendu relevé sur N recherches web, à la date de l'audit}
```

## Garde-fous (NON-NÉGOCIABLES)

- Jamais un comptage de mots comme substitut au contrôle de couverture.
- Jamais une grille E-E-A-T cochée par principe : seulement les affirmations qui pèsent réellement sur la décision du sujet traité.
- Le format attendu vient de la SERP réellement observée, jamais d'une déduction depuis le seul mot-clé.
- Périmètre = pages prioritaires + échantillon motivé, jamais l'exhaustivité du sitemap, et le dire dans les limites.
- Ne jamais conclure à une valeur propre insuffisante sans avoir lu la page qu'on soupçonne d'être dupliquée.
- Aucun contenu noté sans savoir quelle version a été lue (HTML initial ou DOM rendu) ; une suspicion de dépendance au rendu non vérifiée suspend la note.
- Lecture seule. Pas de modification du site, aucune réécriture appliquée directement.

## Enchaînement workflow

En amont : `seo-top20-mots-cles-business` (Phase 0, fournit les pages prioritaires et leurs intentions), `seo-structure-hn` (le Hn d'une page se vérifie avant ou en parallèle de sa réponse). En aval : `seo-cannibalisation` (deux pages proches en valeur propre), `seo-brief-contenu` (les réécritures se briefent avec lui), `seo-quick-win` (un title corrigé ici devient un gain de CTR mesurable).

## Sauvegarde

Output dans `wiki/audit/YYYY-MM-DD-slug-contenu-pertinence.md` selon hook §7 AGENTS.md ; intégré à l'onglet « Contenu et pertinence » du rapport `audit-complet-v2` sinon.

## Concepts liés

`e-e-a-t` · `passage-ranking` · `surprise-gap` · `grounding-score` · `fully-meets`
