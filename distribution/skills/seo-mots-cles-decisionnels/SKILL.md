---
name: seo-mots-cles-decisionnels
description: "Isole les mots-clés transactionnels qui convertissent. « mots-clés décisionnels », « mots-clés qui convertissent »."
---

# Skill — Mots-Clés Décisionnels

## Quand utiliser ce skill

Isole les mots-clés décisionnels — les requêtes transactionnelles et bas de funnel qui convertissent, par opposition aux requêtes informationnelles qui ne font que du trafic. Pipeline en 5 étapes : définir l'offre et le point de conversion → repérer les signaux décisionnels → classer par étage de décision → scorer le potentiel de conversion → shortlist priorisée avec page et format recommandés. Part d'une liste existante ou d'une thématique.

TOUJOURS utiliser ce skill quand l'utilisateur dit : "mots-clés décisionnels", "mots-clés transactionnels", "mots-clés qui convertissent", "requêtes bas de funnel", "requêtes Do", "mots-clés bottom funnel", "quels mots-clés rapportent", "trie ma liste par potentiel de conversion", "mots-clés commerciaux".

## Quand déclencher

Isoler, dans une liste ou une thématique, les requêtes qui amènent un client — pas seulement du trafic.

## Doctrine

- Le trafic n'est pas l'objectif, la conversion l'est. Un mot-clé à 10 000 vues/mois sans intention d'achat vaut moins qu'un mot-clé à 80 vues qui amène un client.
- Un mot-clé décisionnel = l'internaute est en train de choisir, comparer ou acheter. Il a mentalement sorti la carte bleue.
- Le décisionnel se repère à ses **modificateurs**, pas à son volume.
- Bas de funnel ≠ forcément faible volume : "meilleur [catégorie]" peut peser lourd.
- Le décisionnel se traite en priorité : c'est le ROI le plus court du SEO.

## Input requis

| Source | Obligatoire |
|--------|-------------|
| Liste de mots-clés OU thématique | Oui |
| Offre : ce qu'on vend, prix, point de conversion (formulaire, achat, démo, appel) | Oui |
| Audience / persona | Oui |
| Autres acteurs du marché (pour les requêtes branded) | Recommandé |

## Signaux décisionnels (table de modificateurs)

| Catégorie | Modificateurs |
|-----------|---------------|
| **Achat direct** | acheter, commander, prix, tarif, devis, abonnement, s'inscrire |
| **Comparaison** | meilleur, top, vs, comparatif, alternative à, lequel choisir |
| **Évaluation** | avis, test, retour d'expérience, fiable, arnaque |
| **Local / immédiat** | près de moi, [ville], en ligne, livraison, ouvert |
| **Marque** | [ta marque], [ta marque] avis/prix, [nom d'outil] alternative |

## Étages de décision

- **Do — Achat** : l'internaute veut transformer maintenant.
- **Do — Comparatif** : il choisit entre options, toi inclus.
- **Do — Local** : intention d'achat + contrainte géographique.
- **Do — Marque** : il te connaît déjà, ou connaît un autre acteur du marché.
- **Know commercial** : "comment choisir un X" — pré-décision, à capter tôt.

## Pipeline (5 étapes)

1. **Définir l'offre** — ce qu'on vend, le prix, le point de conversion réel.
2. **Repérer les signaux** — passer la liste ou la thématique au filtre des modificateurs décisionnels.
3. **Classer par étage de décision** — ranger chaque mot-clé retenu.
4. **Scorer le potentiel de conversion** — proximité à l'offre (1-5) × intention d'achat (1-5) × faisabilité de ranker (1-5), produit ramené sur une **échelle 0-10 (arrondi entier)**. Flag les requêtes branded sur un autre acteur pour vérifier la légitimité.
5. **Livrable** — shortlist priorisée ; pour chaque mot-clé : page cible (landing, comparatif, page produit, page locale), format, CTA.

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
MOTS-CLÉS DÉCISIONNELS — '[Offre]'

| Mot-clé | Étage | Score conv. /10 | Page cible | Format | CTA |
|---|---|---|---|---|---|
| ... | Do — Comparatif | 5/10 | Page comparatif | Tableau + verdict | Devis |

Top 3 à attaquer en premier : [liste + justification]

RAPPORT DE DÉCISION (obligatoire, voir « Sortie de pré-décision ») : diagnostic, chiffres, état, P1/P2/P3 avec preuve, confiance, effort, risque. Aucun score affiché.
```

## Règles absolues

- Deux scores affichés par mot-clé ou cluster (`.seokb/base/wiki/methodes/rapport-mots-cles-format.md`) : score business sur 5 avec ses composantes (intention 0-2, proximité offre 0-2, conversion directe 0-1) et score matière = nombre de documents du vault qui traitent le sujet (≥ 3 occurrences du champ lexical), par type de source (transcripts, clients, notes, wiki). Le comptage dit où chercher ; le verdict de matière vient de la lecture par type. Zéro document = pas de page.
- Gouvernance des pré-décisions (24 septembre, `.seokb/base/wiki/methodes/rapport-mots-cles-format.md`) : une pré-décision finale par cluster avec statut VALIDÉ / À VÉRIFIER / BLOQUÉ / REJETÉ ; les sorties de ce skill sont des HYPOTHÈSES tant que le rapport n'a pas tranché, et deviennent OBSOLÈTES si elles le contredisent ; aucune page créée sans validation SERP + matière suffisante ; aucun brief avant une pré-décision URL VALIDÉ ; un candidat à la création reste « validation SERP requise » ; les scores /10 restent en backend, le rapport lit adéquation offre, intention, preuve, SERP, décision.
- Sortie finale du workflow (règles du 24 septembre, `.seokb/base/wiki/methodes/rapport-mots-cles-format.md`) : une pré-décision URL par cluster (utiliser / renforcer l'existant / créer / conserver / analyser avant restauration / à confirmer après validation SERP) ou la raison explicite pour laquelle on ne peut pas encore décider (« Décision stratégique requise » pour le positionnement, « Pré-décision impossible avant analyse SERP de N requêtes ») ; jamais « à trancher ». Signaux de demande affichés séparément, jamais agrégés en verdict. Matière qualifiée par type (objection, cas concret, méthode, preuve, résultat, verbatim), jamais comptée en occurrences. « Cannibalisation » interdit sans SERP ni conflit GSC : « chevauchement potentiel à vérifier ». Une requête secondaire sert à repérer une sous-intention, jamais à placer un title, un H2 ou une FAQ par défaut.
- Chaque cluster ou mot-clé retenu porte ses signaux de demande séparés (méthode `audit-complet-v2/demande-observee.md`) à côté de l'intention et de la matière : intention forte + demande faible = terrain vide, « demande à confirmer » et mesure GSC à J+90, jamais une priorité présentée comme acquise.
- Le rapport de pré-décision fait partie de la sortie. Sans lui, le skill n'a pas terminé. Il se rédige à partir du tableau, aucune phrase sans mot-clé ou chiffre derrière, aucun score affiché.
- Ne jamais classer décisionnel un mot-clé purement informationnel pour gonfler la liste.
- Requête branded sur un autre acteur → vérifier la légitimité : page comparative honnête, aucune tromperie.
- Chaque mot-clé décisionnel pointe vers une page avec offre + CTA, sinon il ne convertit pas.
- Prioriser proximité à l'offre + faisabilité, pas le volume brut.

## Enchaînement workflow

Après `seo-recherche-mots-cles` ou `seo-clustering-mots-cles` → alimente `seo-product-led-seo` (outils pour les requêtes Do) et `seo-brief-contenu` (pages de conversion).

## Sauvegarde

Output dans `wiki/keywords/decisionnels-YYYY-MM-DD-slug.md` selon hook §7 AGENTS.md.

## Concepts liés

`know-simple-know-do` · `funnel` · `product-led-seo` · `fully-meets` · `cannibalisation` · `e-e-a-t`
