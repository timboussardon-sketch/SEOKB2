---
name: seo-cluster-aeo
description: "Cluster ou cocon sémantique pour moteurs de réponse depuis un mot-clé pilier. « cluster », « cocon », « pages satellites »."
---

# Skill — Clusters Sémantiques AEO / Agentic Search

## Quand utiliser ce skill

Construction d'architecture de contenu (cluster/cocon sémantique) optimisée pour les moteurs de réponse (SGE, Perplexity, ChatGPT) et les agents IA autonomes. Utilise le framework Know-Simple/Know/Do (remplace TOFU/MOFU/BOFU) et le principe MECE. Pipeline en 5 étapes : mot-clé pilier → mapping intentions → tableau cluster (15+ pages satellites) → maillage interne → priorisation roadmap. Sortie obligatoire : une section de pré-décision (statut RAW / HYPOTHÈSE / VALIDÉ / OBSOLÈTE / BLOQUÉ, pré-décision URL par cluster ou raison de non-décision, score business sur 5, documents du vault, matière qualifiée, SERP) qui nourrit le rapport de pré-décision du workflow mots-clés ; sans elle le skill n'a pas terminé.

TOUJOURS utiliser ce skill quand l'utilisateur dit : "cluster sémantique", "cocon SEO", "AEO", "Agentic Search", "quelles pages créer autour de [mot-clé]", "topical authority", "maillage thématique", "architecture de contenu", "cluster AEO".

## Quand déclencher

Construire une architecture de contenu optimisée pour les moteurs de réponse et les agents IA autonomes.

## Concepts clés

- **AEO** (Answer Engine Optimization) — optimisation pour les moteurs qui génèrent des réponses directes
- **Agentic Search** — agents IA autonomes qui effectuent des recherches et actions
- **RRF** (Reciprocal Rank Fusion) — un cluster couvrant toutes les sous-intentions améliore le score global
- **Principe MECE** — Mutuellement Exclusif, Collectivement Exhaustif

## Framework : Know-Simple / Know / Do (remplace TOFU/MOFU/BOFU)

| Type | Définition | Format idéal | Distribution |
|------|-----------|--------------|-------------|
| **Know-Simple** | Questions factuelles, réponse <50 mots | Définition, chiffre, FAQ courte | 20-30% |
| **Know** | Explication approfondie avec preuves | Guide, tutoriel, comparatif | 40-50% |
| **Do** | Micro-tâches à accomplir (ou exécutables par un agent) | Calculateur, simulateur, générateur, audit | 20-30% |

## Pipeline (5 étapes)

1. **Définir le mot-clé pilier** — requête principale + secteur + ressources disponibles
2. **Mapper les intentions** selon Know-Simple / Know / Do
3. **Générer le tableau du cluster** — minimum 15 pages satellites
4. **Définir le maillage interne** — liens entrants/sortants + ancres par page
5. **Prioriser et roadmap** — volume + difficulté + potentiel conversion + effort

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
Cluster sémantique — '[Mot-clé pilier]'

| Requête cible | Intention | Format | Schema.org | Priorité |
|---|---|---|---|---|
| ... | Know-Simple | FAQ + définition | FAQPage | Haute |
| ... | Do | Calculateur interactif | WebApplication | Haute |

Maillage interne : [schéma connexions]
Roadmap : Mois 1 → Know-Simple | Mois 2 → Know | Mois 3 → Do + pilier
```

## Règles absolues

- Gouvernance des pré-décisions (24 septembre, `.seokb/base/wiki/methodes/rapport-mots-cles-format.md`) : une pré-décision finale par cluster avec statut VALIDÉ / À VÉRIFIER / BLOQUÉ / REJETÉ ; les sorties de ce skill sont des HYPOTHÈSES tant que le rapport n'a pas tranché, et deviennent OBSOLÈTES si elles le contredisent ; aucune page créée sans validation SERP + matière suffisante ; aucun brief avant une pré-décision URL VALIDÉ ; un candidat à la création reste « validation SERP requise » ; les scores /10 restent en backend, le rapport lit adéquation offre, intention, preuve, SERP, décision.
- Ne pas utiliser TOFU/MOFU/BOFU — obsolète pour l'AEO
- Pas deux pages sur le même angle (principe MECE)
- Pages "Do" = outils interactifs, pas du contenu textuel
- Pages Know pointent systématiquement vers une page Do (maillage intentionnel)
- Réviser le cluster tous les 6 mois

## Sauvegarde

Output dans `wiki/clusters/YYYY-MM-DD-slug.md` selon hook §7 AGENTS.md.

## Concepts liés

`aeo` · `agentic-search` · `rrf` · `maillage-interne` · `topical-authority` · `fully-meets`
