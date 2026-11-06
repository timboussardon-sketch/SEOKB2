---
name: seo-clustering-mots-cles
description: "Regroupe une liste de mots-clés en pages par partage de SERP. « cluster mes mots-clés », « keyword clustering »."
---

# Skill — Clustering de Mots-Clés

## Quand utiliser ce skill

Regroupe une liste brute de mots-clés en clusters exploitables — 1 cluster = 1 page. Critère de regroupement : le partage de SERP (deux mots-clés qui affichent le même top 10 = la même intention = une seule page). Pipeline en 5 étapes : importer la liste → normaliser (dédoublonner, nettoyer) → regrouper par intention de SERP → nommer chaque cluster et désigner le mot-clé pivot → affecter 1 cluster = 1 page avec détection de cannibalisation.

TOUJOURS utiliser ce skill quand l'utilisateur dit : "cluster mes mots-clés", "groupe cette liste de mots-clés", "keyword clustering", "regroupe mes requêtes", "j'ai 200 mots-clés à organiser", "quels mots-clés vont sur la même page", "transforme ma liste en pages".

## Quand déclencher

Transformer une liste brute de N mots-clés en clusters exploitables, où chaque cluster devient une page.

## Doctrine

- Le vrai critère de clustering SEO = le **partage de SERP**. Si Google affiche le même top 10 pour deux requêtes, il les traite comme la même intention → une seule page.
- La proximité sémantique seule ne suffit pas. "Assurance auto pas chère" et "tarif assurance auto" se ressemblent mais peuvent avoir des SERP distinctes.
- 1 cluster = 1 page = 1 mot-clé pivot. Deux pages sur le même cluster = cannibalisation programmée.
- Sans accès aux SERP réelles, l'IA cluster par intention + sémantique **en proxy** : la sortie est une hypothèse à valider, jamais une vérité.

## Input requis

| Source | Obligatoire |
|--------|-------------|
| La liste brute de mots-clés (collage, CSV, sortie de `seo-recherche-mots-cles`) | Oui |
| Intention + volume par mot-clé | Recommandé |
| Données de SERP overlap d'un outil (Keyword Insights, Ahrefs "Parent topic") | Recommandé — rend le clustering fiable |
| Le site / l'offre (pour orienter le nommage et détecter la cannibalisation) | Recommandé |

## Pipeline (5 étapes)

1. **Importer la liste** — accepter un collage brut, un CSV ou la sortie de `seo-recherche-mots-cles`.
2. **Normaliser** — dédoublonner, retirer le bruit (mots-clés sans intention, branded concurrent hors scope), fusionner les variantes orthographiques strictes (singulier/pluriel, accents).
3. **Regrouper** — critère #1 : SERP overlap si la donnée est fournie. Sinon proxy : intention identique + même tête sémantique. Chaque groupe = un cluster.
4. **Nommer + pivot** — pour chaque cluster : nom (head term), intention dominante (Know-Simple / Know / Do), mot-clé pivot (le plus représentatif, plus fort volume) + mots-clés secondaires.
5. **Affecter** — 1 cluster = 1 page. Détecter les clusters qui recoupent une page existante → risque de cannibalisation, renvoyer vers `seo-cannibalisation`.

## Sortie de pré-décision (obligatoire)

Ce skill est une étape du workflow mots-clés complet (`.seokb/base/wiki/methodes/workflow-mots-cles-complet.md`). Sa sortie porte un `statut_decision` (RAW, HYPOTHÈSE, VALIDÉ, OBSOLÈTE, BLOQUÉ) et nourrit le rapport de pré-décision, seule sortie visible du workflow ; toute sortie de ce skill qui contredit ce rapport devient OBSOLÈTE. Format complet : `.seokb/base/wiki/methodes/rapport-mots-cles-format.md`.

Ce que le rapport de pré-décision rend, et que ce skill doit rendre possible sur son périmètre :

1. Diagnostic en trois lignes.
2. Pré-décision par marché (5 max) : Marché / Page / Score business sur 5 (intention 0-2, proximité offre 0-2, conversion directe 0-1) / Docs du vault (documents qui traitent le sujet, par type : transcripts, clients, notes, wiki) / Matière qualifiée (objection, cas, méthode, preuve, résultat, verbatim) / SERP (compatible, à vérifier, non vérifiée) / Pré-décision (utiliser, renforcer l'existant, créer, conserver et enrichir, analyser avant restauration, candidat avec validation SERP requise, bloqué, attendre).
3. Ce qui est bloqué, et par quoi : statut, raison, actions autorisées, actions interdites ; « décision stratégique requise » quand c'est le positionnement (c'est la décision de Tim) ; « pré-décision impossible avant analyse SERP de N requêtes » sinon. Jamais « à trancher ».
4. À ne pas produire maintenant.
5. Fiabilité, une ligne ; analyse technique derrière ; logs du workflow en annexe.

Règles : signaux de demande séparés (Suggest, Search Console, calls, acteurs), jamais agrégés en verdict, aucun volume estimé ; matière comptée en documents du vault puis qualifiée par lecture, jamais en occurrences d'un mot ; « cannibalisation » interdit sans SERP ni conflit GSC, « chevauchement potentiel à vérifier » ; une requête secondaire sert à repérer une sous-intention, jamais à placer un title, un H2 ou une FAQ par défaut ; aucune page sans validation SERP + matière suffisante ; aucun brief avant une pré-décision URL VALIDÉ ; un cas ou un relevé réel par page programmatique ; scores /10 en backend ; Faible / Moyen / Élevé, jamais d'anglais ; la certitude affichée ne dépasse jamais la couverture des données.

## Output obligatoire

```
CLUSTERS — '[Liste / thématique]'

| Cluster | Mot-clé pivot | Secondaires | Intention | Page (nouvelle / existante) | Risque cannibalisation |
|---|---|---|---|---|---|
| ... | ... | ... | Know | Nouvelle | — |

Non clusterisés : [mots-clés orphelins laissés seuls]
À valider : confirmer chaque cluster par un SERP overlap réel (outil ou vérification manuelle).

RAPPORT DE DÉCISION (obligatoire, voir « Sortie de pré-décision ») : diagnostic, chiffres, état, P1/P2/P3 avec preuve, confiance, effort, risque. Aucun score affiché.
```

## Règles absolues

- Deux scores affichés par mot-clé ou cluster (`.seokb/base/wiki/methodes/rapport-mots-cles-format.md`) : score business sur 5 avec ses composantes (intention 0-2, proximité offre 0-2, conversion directe 0-1) et score matière = nombre de documents du vault qui traitent le sujet (≥ 3 occurrences du champ lexical), par type de source (transcripts, clients, notes, wiki). Le comptage dit où chercher ; le verdict de matière vient de la lecture par type. Zéro document = pas de page.
- Gouvernance des pré-décisions (24 septembre, `.seokb/base/wiki/methodes/rapport-mots-cles-format.md`) : une pré-décision finale par cluster avec statut VALIDÉ / À VÉRIFIER / BLOQUÉ / REJETÉ ; les sorties de ce skill sont des HYPOTHÈSES tant que le rapport n'a pas tranché, et deviennent OBSOLÈTES si elles le contredisent ; aucune page créée sans validation SERP + matière suffisante ; aucun brief avant une pré-décision URL VALIDÉ ; un candidat à la création reste « validation SERP requise » ; les scores /10 restent en backend, le rapport lit adéquation offre, intention, preuve, SERP, décision.
- Sortie finale du workflow (règles du 24 septembre, `.seokb/base/wiki/methodes/rapport-mots-cles-format.md`) : une pré-décision URL par cluster (utiliser / renforcer l'existant / créer / conserver / analyser avant restauration / à confirmer après validation SERP) ou la raison explicite pour laquelle on ne peut pas encore décider (« Décision stratégique requise » pour le positionnement, « Pré-décision impossible avant analyse SERP de N requêtes ») ; jamais « à trancher ». Signaux de demande affichés séparément, jamais agrégés en verdict. Matière qualifiée par type (objection, cas concret, méthode, preuve, résultat, verbatim), jamais comptée en occurrences. « Cannibalisation » interdit sans SERP ni conflit GSC : « chevauchement potentiel à vérifier ». Une requête secondaire sert à repérer une sous-intention, jamais à placer un title, un H2 ou une FAQ par défaut.
- Chaque cluster ou mot-clé retenu porte ses signaux de demande séparés (méthode `audit-complet-v2/demande-observee.md`) à côté de l'intention et de la matière : intention forte + demande faible = terrain vide, « demande à confirmer » et mesure GSC à J+90, jamais une priorité présentée comme acquise.
- Le rapport de pré-décision fait partie de la sortie. Sans lui, le skill n'a pas terminé. Il se rédige à partir du tableau, aucune phrase sans mot-clé ou chiffre derrière, aucun score affiché.
- 1 cluster = 1 page = 1 pivot. Jamais deux clusters sur la même intention (principe MECE).
- Un mot-clé n'appartient qu'à un seul cluster.
- Sans donnée SERP, marquer explicitement la sortie « hypothèse — à valider par overlap réel ».
- Ne pas forcer un mot-clé orphelin dans un cluster : le laisser en « non clusterisé ».
- Si un cluster recoupe une page live → flag cannibalisation, ne pas créer de doublon.

## Enchaînement workflow

Après `seo-recherche-mots-cles` → chaque cluster devient un input : `seo-brief-contenu` (1 cluster = 1 brief), ou `seo-cluster-aeo` si le cluster est assez gros pour devenir un pilier. Les clusters d'intention Do → `seo-mots-cles-decisionnels`.

## Sauvegarde

Output dans `wiki/keywords/clusters-YYYY-MM-DD-slug.md` selon hook §7 AGENTS.md.

## Concepts liés

`serp-overlap` · `mece` · `cannibalisation` · `cluster-aeo` · `passage-ranking` · `maillage-interne`
