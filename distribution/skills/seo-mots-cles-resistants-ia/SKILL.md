---
name: seo-mots-cles-resistants-ia
description: "Trie les mots-clés absorbés par les IA et ceux qui résistent. « mots-clés résistants à l'IA »."
---

# Skill — Mots-clés résistants à l'IA

## Quand utiliser ce skill

Trie une liste de mots-clés ou une thématique en deux camps : ceux que Google AI Overviews, ChatGPT et Perplexity répondent déjà directement sans clic (informationnel, absorbé), et ceux qui résistent parce qu'ils demandent un choix contextualisé qu'une réponse générique ne peut pas trancher (achat, comparaison, avis, local, marque). Extrait du skill seo-mots-cles-decisionnels, mais allégé : pas de scoring de conversion ni de ciblage de page, juste le tri anti-absorption.

TOUJOURS utiliser ce skill quand l'utilisateur dit : "mots-clés pas mangés par l'IA", "mots-clés que ChatGPT n'absorbe pas", "quels mots-clés résistent à l'IA", "trie par risque d'absorption IA", "mots-clés résistants aux AI Overviews", "quels mots-clés vont encore amener du clic".

## Quand déclencher

Trier, dans une liste ou une thématique, les requêtes qui continuent d'amener un clic humain de celles que Google AI Overviews, ChatGPT ou Perplexity répondent déjà à la place du site.

## Doctrine

- Une IA répond bien à « qu'est-ce que X » ou « comment faire X ». Elle répond mal à « je dois choisir entre X et Y pour MON cas, avec MES contraintes ».
- L'absorption touche l'informationnel générique : définitions, tutoriels, chiffres publics, questions à réponse unique et vérifiable. C'est exactement le contenu qu'une réponse de trois phrases épuise.
- Le décisionnel résiste parce qu'il engage un choix contextualisé (budget, secteur, taille d'équipe, contrainte locale) qu'une réponse générique ne couvre pas, et parce qu'il engage une responsabilité : personne ne clique « acheter » sur la foi d'un résumé IA sans vérifier la source.
- Le volume ne dit rien du risque d'absorption. Un mot-clé à fort volume mais purement définitionnel est le plus exposé, pas le moins.
- Le test rapide : une réponse générique et non sourcée de trois phrases satisferait-elle la requête ? Oui → absorbé. Non, il faut comparer, choisir ou vérifier avec du contexte propre → résistant.

## Signaux de résistance (table de modificateurs)

| Catégorie | Modificateurs | Pourquoi ça résiste |
|-----------|---------------|----------------------|
| **Achat direct** | acheter, commander, prix, tarif, devis, abonnement, s'inscrire | Engage une dépense, l'IA ne prend pas la responsabilité |
| **Comparaison** | meilleur, top, vs, comparatif, alternative à, lequel choisir | Le verdict dépend du profil de qui demande |
| **Évaluation** | avis, test, retour d'expérience, fiable, arnaque | Cherche une preuve vécue, pas un résumé |
| **Local / immédiat** | près de moi, [ville], en ligne, livraison, ouvert | Contexte géographique ou temporel que l'IA généralise mal |
| **Marque** | [ta marque], [ta marque] avis/prix, [nom d'outil] alternative | Cherche une confirmation ou une source spécifique |

À l'inverse, signal d'absorption : la requête commence par « qu'est-ce que », « comment », « pourquoi », « définition de », ou porte sur un chiffre/fait unique et stable dans le temps.

## Pipeline (3 étapes)

1. **Lister** — importer la liste de mots-clés, ou explorer la thématique si on part de zéro (variantes, questions associées, longue traîne).
2. **Tester** — appliquer le test de résistance à chaque mot-clé, confirmé par la table de modificateurs.
3. **Trancher** — sortir deux colonnes : absorbés (à ne pas prioriser en acquisition de clic classique) et résistants (prioritaires, ROI le plus sûr).

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
MOTS-CLÉS RÉSISTANTS À L'IA — '[Thématique]'

| Mot-clé | Verdict | Pourquoi |
|---|---|---|
| ... | Résistant | Comparaison, choix contextualisé |
| ... | Absorbé | Définition à réponse unique |

Résistants à prioriser : [liste]
Absorbés à ne pas prioriser en SEO clic (candidats à un traitement GEO citation si la marque veut apparaître comme source) : [liste]
```

## Règles absolues

- Gouvernance des pré-décisions (24 septembre, `.seokb/base/wiki/methodes/rapport-mots-cles-format.md`) : une pré-décision finale par cluster avec statut VALIDÉ / À VÉRIFIER / BLOQUÉ / REJETÉ ; les sorties de ce skill sont des HYPOTHÈSES tant que le rapport n'a pas tranché, et deviennent OBSOLÈTES si elles le contredisent ; aucune page créée sans validation SERP + matière suffisante ; aucun brief avant une pré-décision URL VALIDÉ ; un candidat à la création reste « validation SERP requise » ; les scores /10 restent en backend, le rapport lit adéquation offre, intention, preuve, SERP, décision.
- Le verdict s'écrit « probabilité de conserver un clic après réponse IA : forte / moyenne / faible », jamais « résistant / absorbé » comme une certitude ; c'est une heuristique.
- Ne jamais classer résistant un mot-clé purement informationnel pour gonfler la liste.
- Le verdict se justifie toujours par le modificateur ou le test de résistance, jamais par intuition seule.
- Un mot-clé « absorbé » n'est pas un mot-clé à abandonner : il peut valoir un traitement GEO (citation dans la réponse IA) plutôt qu'un traitement SEO clic. Le dire explicitement dans l'output.

## Enchaînement workflow

Les mots-clés « résistants » → `seo-mots-cles-decisionnels` pour le scoring de conversion et le ciblage de page (landing, comparatif, page produit, page locale).

## Sauvegarde

Output dans `wiki/keywords/resistants-ia-YYYY-MM-DD-slug.md` selon hook §7 AGENTS.md.

## Concepts liés

`know-simple-know-do` · `funnel` · `grounding-score` · `geo` · `mots-cles-decisionnels` · `fully-meets`
