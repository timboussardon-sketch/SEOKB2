---
name: seo-entites-vectorielles
description: "Entités sémantiques qu'une page doit couvrir pour coller à l'intention. « entités sémantiques », « Grounding Score »."
---

# Skill — Entités Vectorielles SEO

## Quand utiliser ce skill

Cartographie des entités sémantiques nécessaires pour qu'une page s'aligne mathématiquement avec l'intention de recherche ciblée (similarité cosinus / Grounding Score). Pipeline en 4 étapes : définir requête cible → générer tableau d'entités (4 catégories : techniques, preuves quantitatives, vecteurs multimodaux, divergence/Haute Surprise) → analyser gap concurrentiel → recommandations d'implémentation par zone (H1, corps, FAQ). Sortie obligatoire : une section de pré-décision (statut RAW / HYPOTHÈSE / VALIDÉ / OBSOLÈTE / BLOQUÉ, pré-décision URL par cluster ou raison de non-décision, score business sur 5, documents du vault, matière qualifiée, SERP) qui nourrit le rapport de pré-décision du workflow mots-clés ; sans elle le skill n'a pas terminé.

TOUJOURS utiliser ce skill quand l'utilisateur dit : "entités sémantiques", "vecteurs SEO", "Grounding Score", "similarité cosinus", "quels termes inclure dans ma page", "optimisation sémantique", "NLP SEO", "embeddings SEO".

## Quand déclencher

Cartographier les entités sémantiques nécessaires pour qu'une page s'aligne mathématiquement avec l'intention de recherche ciblée.

## Concepts clés

- **Grounding Score** (Similarité Cosinus) — mesure l'alignement entre le vecteur de la page et le vecteur de l'intention
- **Recherche vectorielle** (Muvera, etc.) — les moteurs comparent sémantiquement les pages aux requêtes via embeddings
- **Surprise Gap** — éléments Haute Surprise qui forcent la mémorisation des modèles IA

## Pipeline (4 étapes)

1. **Définir la requête cible** — requête principale + type d'intention + niveau d'expertise audience
2. **Générer le tableau des entités** (10 termes/concepts par catégorie) :

| Entités Techniques | Preuves Quantitatives | Vecteurs Multimodaux | Divergence (Haute Surprise) |
|---|---|---|---|
| Termes obligatoires >80% top 10 | Statistiques sourcées format [Chiffre+Unité+Contexte] | Formats attendus (images, outils, vidéos) | Concepts présents chez <10% des concurrents |

3. **Analyser le gap concurrentiel** — entités manquantes / opportunités de divergence / quick wins
4. **Recommandations d'implémentation** — où placer chaque entité (H1, corps, FAQ, sidebar)

## Règles par catégorie

**Preuves Quantitatives** — format obligatoire :
- "73% des entreprises B2B" / "ROI moyen de 4,2x sur 12 mois" — OK
- "beaucoup d'entreprises" — non quantifié, refusé

**Divergence (Haute Surprise)** — test :
- Si un concurrent peut copier le concept en 5 min → pas de Haute Surprise

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
Analyse vectorielle — Requête : "[Requête]"
Intention : [Type]

| Entités Techniques | Preuves Quantitatives | Vecteurs Multimodaux | Divergence |
|---|---|---|---|

Gap concurrentiel :
- Manquant : ...
- Opportunité : ...
- Quick win : ...

Implémentation recommandée :
- H1/H2 : entités techniques principales
- Corps : preuves quantitatives contextualisées
- FAQ : éléments de divergence
```

## Règles absolues

- Pas d'entités listées artificiellement (keyword stuffing)
- Qualité d'intégration > quantité
- Mettre à jour régulièrement (les vecteurs évoluent)
- Toujours sourcer les preuves quantitatives

## Sauvegarde

Output dans `wiki/queries/entites-YYYY-MM-DD-slug.md` selon hook §7 AGENTS.md.

## Concepts liés

`grounding-score` · `surprise-gap` · `vecteurs-semantiques` · `passage-ranking` · `e-e-a-t`
