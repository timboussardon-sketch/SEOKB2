---
name: seo-peurs-objections
description: "Freins et objections d'une audience B2B, verbatims et contenus à produire. « objections », « peurs prospects »."
---

# Skill — Peurs & Objections B2B

## Quand utiliser ce skill

Identification des freins psychologiques d'une audience B2B pour créer du contenu à haute conversion et des verbatims "Haute Surprise". Pipeline en 4 étapes : définir contexte (thématique + persona + expériences négatives) → tableau d'analyse 10 lignes (pain point + verbatim Haute Surprise + preuve atomique) → prioriser les 3 objections critiques → recommandations de contenu (format + emplacement + CTA). Sortie obligatoire : une section de pré-décision (statut RAW / HYPOTHÈSE / VALIDÉ / OBSOLÈTE / BLOQUÉ, pré-décision URL par cluster ou raison de non-décision, score business sur 5, documents du vault, matière qualifiée, SERP) qui nourrit le rapport de pré-décision du workflow mots-clés ; sans elle le skill n'a pas terminé.

TOUJOURS utiliser ce skill quand l'utilisateur dit : "objections clients", "peurs prospects", "pain points", "freins à l'achat", "pourquoi ils n'achètent pas", "qu'est-ce qui bloque mes prospects", "comment convaincre un prospect échaudé", "verbatims B2B".

## Quand déclencher

Identifier les freins psychologiques d'une audience B2B pour créer du contenu à haute conversion et des verbatims "Haute Surprise".

## Utilisation

- Avant de rédiger une page de vente ou landing page
- Pour créer du contenu de réassurance (FAQ, témoignages, garanties)
- Pour briefer une équipe commerciale
- Pour identifier les angles de différenciation face aux concurrents

## Pipeline (4 étapes)

1. **Définir le contexte** — thématique/produit/service + persona cible (fonction, taille entreprise, secteur) + expériences négatives connues
2. **Générer le tableau d'analyse** (10 lignes minimum) :

| Micro-intention / Pain Point | Verbatim "Haute Surprise" | Preuve Atomique attendue |
|---|---|---|
| Nom précis du frein | Citation experte et rare — zéro cliché | Donnée binaire/chiffrée format Sujet + Verbe + Donnée |

3. **Prioriser les 3 objections critiques** — fréquence × intensité × différenciation
4. **Recommandations de contenu** — format idéal (case study, calculateur, FAQ) + emplacement + CTA

## Règles Verbatims "Haute Surprise"

- Frustration experte ou technique rarement verbalisée
- Vocabulaire spécifique au métier du persona
- Connaissance terrain que seul un initié possède
- Pas de clichés : "je veux du ROI", "je veux des résultats concrets"

**Transformation :**
- Cliché : "Je veux voir des résultats concrets"
- Verbatim Haute Surprise : "La dernière agence m'envoyait des rapports de 40 pages où le seul KPI lisible était le nombre de backlinks, sans jamais croiser ça avec mon CRM"

## Règles Preuves Atomiques

Format : **Sujet + Verbe + Donnée**
- "Notre méthodologie génère +47% de leads qualifiés en moyenne sur 6 mois" — OK
- "100% de nos clients ont accès à un dashboard temps réel connecté à leur CRM" — OK
- "Nous offrons un excellent accompagnement" — non vérifiable, refusé

## Règles absolues

- Pas de clichés sectoriels dans les verbatims
- Pas de preuves atomiques non vérifiables (superlatifs vagues)
- Ce skill génère du contenu stratégique, pas du contenu final prêt à publier
- Les preuves atomiques doivent être validées par l'entreprise avant publication

## Sauvegarde

Output dans `wiki/queries/peurs-YYYY-MM-DD-slug.md` selon hook §7 AGENTS.md.

## Concepts liés

`preuve-atomique` · `surprise-gap` · `e-e-a-t` · `grounding-score` · `fully-meets`

## Sortie de pré-décision (obligatoire)

Ce skill est une étape du workflow mots-clés complet (`.seokb/base/wiki/methodes/workflow-mots-cles-complet.md`). Sa sortie porte un `statut_decision` (RAW, HYPOTHÈSE, VALIDÉ, OBSOLÈTE, BLOQUÉ) et nourrit le rapport de pré-décision, seule sortie visible du workflow ; toute sortie de ce skill qui contredit ce rapport devient OBSOLÈTE. Format complet : `.seokb/base/wiki/methodes/rapport-mots-cles-format.md`.

Ce que le rapport de pré-décision rend, et que ce skill doit rendre possible sur son périmètre :

1. Diagnostic en trois lignes.
2. Pré-décision par marché (5 max) : Marché / Page / Score business sur 5 (intention 0-2, proximité offre 0-2, conversion directe 0-1) / Docs du vault (documents qui traitent le sujet, par type : transcripts, clients, notes, wiki) / Matière qualifiée (objection, cas, méthode, preuve, résultat, verbatim) / SERP (compatible, à vérifier, non vérifiée) / Pré-décision (utiliser, renforcer l'existant, créer, conserver et enrichir, analyser avant restauration, candidat avec validation SERP requise, bloqué, attendre).
3. Ce qui est bloqué, et par quoi : statut, raison, actions autorisées, actions interdites ; « décision stratégique requise » quand c'est le positionnement (c'est la décision de Tim) ; « pré-décision impossible avant analyse SERP de N requêtes » sinon. Jamais « à trancher ».
4. À ne pas produire maintenant.
5. Fiabilité, une ligne ; analyse technique derrière ; logs du workflow en annexe.

Règles : signaux de demande séparés (Suggest, Search Console, calls, acteurs), jamais agrégés en verdict, aucun volume estimé ; matière comptée en documents du vault puis qualifiée par lecture, jamais en occurrences d'un mot ; « cannibalisation » interdit sans SERP ni conflit GSC, « chevauchement potentiel à vérifier » ; une requête secondaire sert à repérer une sous-intention, jamais à placer un title, un H2 ou une FAQ par défaut ; aucune page sans validation SERP + matière suffisante ; aucun brief avant une pré-décision URL VALIDÉ ; un cas ou un relevé réel par page programmatique ; scores /10 en backend ; Faible / Moyen / Élevé, jamais d'anglais ; la certitude affichée ne dépasse jamais la couverture des données.

