---
title: Workflow mots-clés complet, 14 étapes, sortie = rapport de pré-décision
version: "24 septembre 2026"
principe: "Aucun volume estimé. Signaux de demande séparés. Matière qualifiée par type. Une pré-décision URL par cluster ou la raison de la non-décision. Tim décide."
related:
  - "[[methodes/rapport-mots-cles-format]]"
  - "[[skill-workflow-mots-cles]]"
---

# Workflow mots-clés complet

Chaque étape appelle un skill, écrit un fichier dans le wiki avec son `statut_decision` (RAW, HYPOTHÈSE, VALIDÉ, OBSOLÈTE, BLOQUÉ), et nourrit la suivante. La dernière étape rend le **rapport de pré-décision**, seule sortie visible : toute sortie amont qui le contredit devient OBSOLÈTE. Référence exécutée : [[keywords/2026-09-23-organikk-rapport-decision]].

| Ordre | Skill | Rôle | Sortie (wiki) | Statut à la sortie |
|---|---|---|---|---|
| 1 | `kw-research-workflow` | cadrage, Keyword Planner ou Suggest, Search Console (quick wins, cannibalisation, content gaps), DeepSearch web en 4 recherches, verbatims des transcripts, modèles pSEO, tableau scoré avec signaux de demande séparés, synthèse 5 lignes | `queries/kw-research-YYYY-MM-DD-slug.md` + CSV | RAW |
| 2 | Search Console (`seo-quick-win` + content gaps) | les requêtes que Google montre déjà, business / marque / héritées | `keywords/YYYY-MM-DD-slug-search-console.md` | RAW |
| 3 | `seo-mots-cles-overview` | matrice objectifs × secteurs sur le terme-pilier | `keywords/YYYY-MM-DD-slug-overview.md` | HYPOTHÈSE |
| 4 | `seo-recherche-mots-cles` | liste qualifiée : intention, difficulté, funnel, signaux de demande | `keywords/recherche-YYYY-MM-DD-slug.md` | HYPOTHÈSE |
| 5 | `seo-mots-cles-resistants-ia` | probabilité de conserver un clic après réponse IA : forte / moyenne / faible | `keywords/YYYY-MM-DD-slug-resistants-ia.md` | HYPOTHÈSE |
| 6 | mots-clés business, filtre des 4 piliers (Surprise Gap, Grounding, pSEO, AEO) | les 3 à 5 requêtes qui entrent dans la roadmap | `keywords/YYYY-MM-DD-slug-mots-cles-business.md` | HYPOTHÈSE |
| 7 | `seo-clustering-mots-cles` | un cluster = une page candidate ; chevauchements potentiels à vérifier, jamais « cannibalisation » sans SERP | `keywords/clusters-YYYY-MM-DD-slug.md` | HYPOTHÈSE |
| 8 | `seo-mots-cles-decisionnels` | étage de décision, page cible, CTA ; scores /10 en backend | `keywords/decisionnels-YYYY-MM-DD-slug.md` | HYPOTHÈSE |
| 9 | `seo-cluster-aeo` | cocon autour du pilier retenu | `clusters/YYYY-MM-DD-slug.md` | HYPOTHÈSE, BLOQUÉ si le pilier l'est |
| 10 | `seo-modeles-pseo` + `seo-programmatique-pseo` | spokes et modèles ; un cas ou un relevé réel par page, sinon la page n'existe pas | `queries/pseo-YYYY-MM-DD-slug.md` | HYPOTHÈSE |
| 11 | `seo-peurs-objections` | freins des prospects, verbatims des transcripts, cellules vides = absence constatée | `queries/peurs-YYYY-MM-DD-slug.md` | VALIDÉ si verbatims réels |
| 12 | `seo-entites-vectorielles` | entités de la page pilote | `queries/entites-YYYY-MM-DD-slug.md` | HYPOTHÈSE |
| 13 | `seo-brief-contenu` | brief Hn ; produit seulement si la pré-décision URL est VALIDÉ, sinon fichier marqué BLOQUÉ | `briefs/YYYY-MM-DD-slug.md` | BLOQUÉ ou VALIDÉ |
| 14 | rapport de pré-décision | la seule sortie visible | `keywords/YYYY-MM-DD-slug-rapport-decision.md` + `keywords/annexes/decisions-*.json` + `scores-*.json` | PRÉ-DÉCISION FINALE |

## Étape 14 : le rapport de pré-décision

Format complet : [[methodes/rapport-mots-cles-format]]. Résumé de ce qu'il rend, dans l'ordre :

1. **Diagnostic** en trois lignes : conclusion en gras, démonstration, priorité en gras.
2. **Pré-décision par marché** (5 marchés max) : tableau Marché / Page / Score business sur 5 / Docs du vault / Matière qualifiée / SERP / Pré-décision (utiliser, renforcer l'existant, créer, conserver et enrichir, analyser avant restauration, candidat avec validation SERP requise, bloqué, attendre).
3. **Ce qui est bloqué, et par quoi** : statut, raison, actions autorisées, actions interdites. Les pré-décisions ouvertes sont typées : « décision stratégique requise » (positionnement, c'est celle de Tim) ou « pré-décision impossible avant analyse SERP de N requêtes ». Jamais « à trancher ».
4. **À ne pas produire maintenant.**
5. **Fiabilité de l'analyse**, une ligne.
6. Analyse technique : lecture par marché (adéquation offre, intention, preuve, SERP, pré-décision), scores business et matière avec composantes et documents par type, signaux de demande séparés, matière par type, recouvrements (chevauchements potentiels), probabilité de conserver un clic, pages programmatiques restantes, ce qui a changé par rapport aux sorties amont.
7. Logs du workflow : les 13 sorties amont avec leur statut, en annexe, jamais dans le rapport visible.

Objet de pré-décision, un par cluster :

```json
{"cluster":"…","url":"…","score_business":5,"docs_vault":{"transcripts":5,"clients":15,"notes":113,"wiki":99},"matiere":"incomplète","serp":"à vérifier","statut":"BLOQUÉ","reason":"…","allowed_actions":["…"],"forbidden_actions":["créer une page","publier le brief"]}
```

Règles dures : une pré-décision finale par cluster ; aucune sortie aval ne contredit le statut ; aucune page sans validation SERP + matière suffisante ; aucun brief avant une pré-décision URL VALIDÉ ; signaux de demande séparés, jamais agrégés en verdict ; matière comptée en documents du vault par type puis qualifiée par lecture (objection, cas, méthode, preuve, résultat, verbatim), jamais en occurrences d'un mot ; « cannibalisation » interdit sans SERP ni conflit GSC ; une requête secondaire ne se place jamais en title, H2 ou FAQ par défaut ; scores /10 en backend, seuls le score business sur 5 et les docs du vault sont visibles.

## Quality gate

Le rapport ne sort pas si : un cluster prioritaire n'a ni pré-décision URL ni raison de non-décision ; « à trancher » apparaît ; un verdict de demande agrégé apparaît ; « cannibalisation » sans SERP ; matière en occurrences ; une action « placer en title / H2 / FAQ » ; une décision de positionnement classée priorité mot-clé ; un brief produit sur un cluster non VALIDÉ ; une sortie amont contradictoire non marquée OBSOLÈTE ; un identifiant technique ou un mot anglais dans la synthèse.
