---
name: seo-programmatique-pseo
description: "Système de pages programmatiques : 1 template + 1 variable. « pSEO », « programmatique », « pages scalables »."
---

# Skill — SEO Programmatique (pSEO)

## Quand utiliser ce skill

Conception de systèmes de contenu programmatique : 1 template + 1 variable = des centaines/milliers de pages qui rankent chacune sur une longue traîne. Pipeline en 5 étapes : identifier modèles scalables (min 5) → matrice de priorisation → mots-clés par modèle → plan d'exécution 90 jours → résumé exécutif. 7 règles non-négociables (anti-thin content, données terrain, sourcing, canonical, maillage différenciant, Surprise Score, Grounding Score). Sortie obligatoire : une section de pré-décision (statut RAW / HYPOTHÈSE / VALIDÉ / OBSOLÈTE / BLOQUÉ, pré-décision URL par cluster ou raison de non-décision, score business sur 5, documents du vault, matière qualifiée, SERP) qui nourrit le rapport de pré-décision du workflow mots-clés ; sans elle le skill n'a pas terminé.

TOUJOURS utiliser ce skill quand l'utilisateur dit : "programmatic SEO", "pSEO", "pages scalables", "template + variable", "créer des centaines de pages", "base de données + SEO", "growth engineering SEO".

## Quand déclencher

Concevoir des systèmes de contenu programmatique : un template + une variable = N pages organiques uniques.

## Principe fondamental

```
Template (fixe) + Variable (base de données) = N pages organiques uniques
```

Raisonner comme un ingénieur produit (data → template → pages) ET comme un SEO senior (intent → SERP → conversion).

## Input requis

- URL + description du site (3-5 phrases, positionnement, preuve sociale)
- **Données disponibles en base** (carburant du programmatique) : catalogue, FAQ, cas clients, données réglementaires, clusters identifiés
- Pages existantes (piliers, services, blog)
- 3-5 concurrents
- Objectifs business + persona + contraintes

## Pipeline (5 étapes)

1. **Identifier les modèles scalables** (minimum 5) :
   - Architecture : pattern URL + head term + modificateur + nb pages possibles + source de données
   - Template de page : H1 avec variable + sections + CTA + Schema.org
   - SEO & Intent : phase funnel + intention + 10 exemples de requêtes + compétition
   - Avantage compétitif : ce que les concurrents ne peuvent pas copier

2. **Matrice de priorisation** — pages possibles × effort × impact SEO × potentiel conversion × données disponibles

3. **Mots-clés par modèle** — 10-15 longues traînes par modèle (requête + intention + funnel + compétition)

4. **Plan d'exécution 90 jours** — semaine par semaine, prérequis techniques

5. **Résumé exécutif** — 5 phrases + modèle #1 à lancer en premier

## 7 Règles non-négociables

1. **Anti-thin content** — chaque variable change le contenu réel (pas juste le H1). Max 30% texte identique entre deux pages.
2. **Données terrain** — zéro hallucination, zéro chiffre inventé. Placeholder : `[DONNÉE À SOURCER]`
3. **Sourcing obligatoire** — chaque chiffre = source + organisme + année
4. **Canonical propre** — une URL = un contenu = une canonical
5. **Maillage différenciant** — chaque page pointe vers un ensemble différent de pages internes
6. **Surprise Score** — au moins 1 élément High Surprise par section
7. **Grounding Score** — 1 passage ancré 150-200 mots + bloc authorship ~50 mots par page

## Variantes (cf. KB)

Pour les sites avec offre produit/service (e-commerce, SaaS) → utiliser la variante "produit/service" du méga-prompt pSEO.
Pour les sites média/éditoriaux/communautaires → utiliser la variante "non-produit" qui ajoute un Test de Substitution LLM en Étape 0 obligatoire.

## Règles absolues

- Gouvernance des pré-décisions (24 septembre, `.seokb/base/wiki/methodes/rapport-mots-cles-format.md`) : une pré-décision finale par cluster avec statut VALIDÉ / À VÉRIFIER / BLOQUÉ / REJETÉ ; les sorties de ce skill sont des HYPOTHÈSES tant que le rapport n'a pas tranché, et deviennent OBSOLÈTES si elles le contredisent ; aucune page créée sans validation SERP + matière suffisante ; aucun brief avant une pré-décision URL VALIDÉ ; un candidat à la création reste « validation SERP requise » ; les scores /10 restent en backend, le rapport lit adéquation offre, intention, preuve, SERP, décision.
- Règle centrale, pas une note finale : un cas client ou un relevé réel par page, sinon la page n'existe pas. Un template ne justifie rien ; ne proposer que les secteurs avec demande observée, SERP compatible, vraie matière, offre réelle et preuve propre au secteur.
- Pas deux modèles sur le même angle (anti-cannibalisation)
- Pas de modèle sans données propriétaires disponibles
- Pas de pages sans CTA vers une offre
- Prioriser : compétition faible + données propriétaires

## Sauvegarde

Output dans `wiki/queries/pseo-YYYY-MM-DD-slug.md` selon hook §7 AGENTS.md.

## Concepts liés

`surprise-gap` · `grounding-score` · `rrf` · `e-e-a-t` · `cannibalisation` · `maillage-interne` · `test-substitution-llm` · `product-led-seo`

## Sortie de pré-décision (obligatoire)

Ce skill est une étape du workflow mots-clés complet (`.seokb/base/wiki/methodes/workflow-mots-cles-complet.md`). Sa sortie porte un `statut_decision` (RAW, HYPOTHÈSE, VALIDÉ, OBSOLÈTE, BLOQUÉ) et nourrit le rapport de pré-décision, seule sortie visible du workflow ; toute sortie de ce skill qui contredit ce rapport devient OBSOLÈTE. Format complet : `.seokb/base/wiki/methodes/rapport-mots-cles-format.md`.

Ce que le rapport de pré-décision rend, et que ce skill doit rendre possible sur son périmètre :

1. Diagnostic en trois lignes.
2. Pré-décision par marché (5 max) : Marché / Page / Score business sur 5 (intention 0-2, proximité offre 0-2, conversion directe 0-1) / Docs du vault (documents qui traitent le sujet, par type : transcripts, clients, notes, wiki) / Matière qualifiée (objection, cas, méthode, preuve, résultat, verbatim) / SERP (compatible, à vérifier, non vérifiée) / Pré-décision (utiliser, renforcer l'existant, créer, conserver et enrichir, analyser avant restauration, candidat avec validation SERP requise, bloqué, attendre).
3. Ce qui est bloqué, et par quoi : statut, raison, actions autorisées, actions interdites ; « décision stratégique requise » quand c'est le positionnement (c'est la décision de Tim) ; « pré-décision impossible avant analyse SERP de N requêtes » sinon. Jamais « à trancher ».
4. À ne pas produire maintenant.
5. Fiabilité, une ligne ; analyse technique derrière ; logs du workflow en annexe.

Règles : signaux de demande séparés (Suggest, Search Console, calls, acteurs), jamais agrégés en verdict, aucun volume estimé ; matière comptée en documents du vault puis qualifiée par lecture, jamais en occurrences d'un mot ; « cannibalisation » interdit sans SERP ni conflit GSC, « chevauchement potentiel à vérifier » ; une requête secondaire sert à repérer une sous-intention, jamais à placer un title, un H2 ou une FAQ par défaut ; aucune page sans validation SERP + matière suffisante ; aucun brief avant une pré-décision URL VALIDÉ ; un cas ou un relevé réel par page programmatique ; scores /10 en backend ; Faible / Moyen / Élevé, jamais d'anglais ; la certitude affichée ne dépasse jamais la couverture des données.

