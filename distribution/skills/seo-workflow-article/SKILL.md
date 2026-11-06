---
name: seo-workflow-article
description: "Rédaction d'article SEO en 8 étapes, 2000-2500 mots. « workflow article », « aide-moi à écrire un article sur »."
---

# Skill — Workflow Création Article Complet (8 étapes)

## Quand utiliser ce skill

Pipeline de rédaction d'article SEO en 8 étapes séquentielles. Chaque étape alimente la suivante : Surprise Gap → Ancrage local → Données chiffrées → Inversions expertes → Architecture narrative → Rédaction principale → FAQ micro-intentions → Compilation finale. Produit un article 2000-2500 mots en prose continue, avec passage ancré (150-200 mots) et bloc authorship (~50 mots extractible Position 0).

TOUJOURS utiliser ce skill quand l'utilisateur dit : "créer un article", "rédiger un contenu", "workflow article", "pipeline éditorial", "article de A à Z", "aide-moi à écrire un article sur [sujet]", "lance les 8 étapes", "applique le workflow rédaction".

Ce skill est invoqué seul pour rédiger un article à partir d'un brief simple. Pour un pipeline complet incluant le décodage sémantique RRF en amont et la checklist fact-check en aval, utiliser plutôt `article-engine-pipeline` qui appelle ce skill comme phase 4.

Frameworks intégrés : Surprise Score (Titans/MIRAS), Grounding Score (Triade SERP), Anti-AI Writing, E-E-A-T local. Temps estimé : 1h30 à 2h30 selon complexité.

## Quand déclencher

Pipeline complet A→Z pour produire un article SEO différenciant et prêt à publier. Chaque étape alimente la suivante — impossible de sauter une étape sans dégrader le résultat.

**Triggers** : "créer un article", "rédiger un contenu", "workflow article", "pipeline éditorial", "article de A à Z", "aide-moi à écrire un article sur [sujet]".

**Temps estimé** : 1h30 à 2h30 selon complexité.

## Input requis (avant de commencer)

```
MOT-CLÉ      : [mot-clé principal]
STRUCTURE HN : [hiérarchie H1/H2/H3]
IDÉES        : [angles, données, points à ne pas oublier]
LOCALISATION : [zone géographique]
SECTEUR      : [secteur d'activité]
AUDIENCE     : [qui va lire]
```

Si ces variables ne sont pas fournies par l'utilisateur, les demander AVANT de commencer. Ne pas deviner.

## Process en 4 phases validées (règle l'utilisateur, 2026-10-21) — prime sur tout le reste

Consigne de l'utilisateur : « TOUJOURS RESPECTER, TOUJOURS : brief, structure Hn, ensuite ajoute data dans le Hn, puis rédaction. Chaque phase doit être validée par le consultant. »

| Phase | Livrable montré au consultant | Étapes du skill mobilisées |
|---|---|---|
| 1. Brief | Brief (skill `seo-brief-contenu`) : requête, intention, angle, cible, Surprise Gap | Input requis + étape 1 (Surprise Gap) |
| 2. Structure Hn | H1/H2/H3 seuls, sans prose (skill `seo-structure-hn-v2`) | Étape 5 (architecture narrative), réduite aux Hn |
| 3. Data dans les Hn | La même structure Hn, avec sous chaque H2/H3 les chiffres, sources, verbatims, cas et inversions qui le nourrissent ; trou = `[MATIÈRE MANQUANTE]` | Étapes 2 (ancrage), 3 (données chiffrées), 4 (inversions) rangées sous chaque Hn |
| 4. Rédaction | Texte rédigé à partir de la phase 3 validée, rien d'autre | Étapes 6, 7, 8 |

Règles :
- **Une phase par tour.** Livrer la phase, puis s'arrêter et demander la validation. Jamais deux phases dans la même réponse, même si la suite paraît évidente.
- **Validation = accord explicite du consultant** sur cette phase. Le silence, un « ok continue » donné sur une autre phase, ou un brief fourni par l'utilisateur sans mot de validation ne valent pas validation.
- **Une correction relance la même phase** : on la corrige, on la remontre, on attend l'accord. On ne passe pas à la suivante avec les corrections « intégrées en route ».
- **Matière fournie par l'utilisateur** (brief ou Hn déjà prêts) : la présenter comme livrable de la phase correspondante et demander la validation avant de passer à la suivante.
- **Aucune phase sautée**, y compris pour un article court ou urgent. La rédaction n'utilise que la data posée et validée en phase 3 : une info absente de la phase 3 n'entre pas dans le texte.
- Sauvegarder chaque phase validée dans le fichier de travail, avec la date de validation.

## Structure V2 (skill `seo-structure-hn-v2`)

En phase 2 (structure Hn, étape 5), charger `seo-structure-hn-v2` avant de poser le plan : H2 = question utile pour décider, chaque section = réponse directe, preuve, détails utiles, limite ; article de méthode = pattern 3 (mini-formation, un cas qui avance, un résultat par section). Section sans matière : supprimée, pas remplie.

## Pipeline (8 étapes)

| Étape | Nom | Output |
|-------|-----|--------|
| 1 | **Surprise Gap** | 5 angles saturés + 5 infos sous-exploitées classées par gradient d'information |
| 2 | **Ancrage local** | Signaux E-E-A-T géographiques précis (autorité locale, OPCO, tissu éco) |
| 3 | **Données chiffrées** | 8-12 stats sourcées (chiffre + source + argument + contexte) |
| 4 | **Inversions expertes** | 5 croyances fausses + réalité + pourquoi l'erreur persiste + formulation |
| 5 | **Architecture narrative** | Plan section par section (rappel + contenu + surprise) |
| 6 | **Rédaction principale** | Prose 2000-2500 mots, pattern Tension → Résolution → Preuve |
| 7 | **FAQ micro-intentions** | 6-8 questions bas de funnel (non traitées dans le corps) |
| 8 | **Compilation finale** | Article complet + checklist qualité |

L'agent ne saute AUCUNE étape. L'ordre d'exécution suit les 4 phases validées : 1 (brief) → 5 (Hn) → 2, 3, 4 (data rangée dans les Hn) → 6, 7, 8 (rédaction). Arrêt et validation du consultant après chaque phase.

## Frameworks intégrés

| Framework | Étapes mobilisées | Fonction |
|-----------|-------------------|----------|
| Surprise Score (Titans/MIRAS) | 1, 4, 5, 6 | Élément High Surprise au début et à la fin de chaque section |
| Grounding Score (Triade SERP) | 5, 6, 8 | Passage ancré 150-200 mots + bloc authorship ~50 mots extractible Position 0 |
| Anti-AI Writing | 6, 8 | Élimination des patterns IA détectables |
| E-E-A-T local | 2 | Signaux géographiques précis, acteurs nommés |

## Règles de rédaction absolues

**Obligatoire** :
- Prose continue — aucun bullet point dans le corps de l'article
- Pattern Tension → Résolution → Preuve sur chaque idée
- Zéro phrase creuse
- Longueur : 2000-2500 mots minimum
- Passage ancré 150-200 mots dans les 300 premiers mots
- Bloc d'authorship ~50 mots extractible en Position 0
- Chaque chiffre cité a sa source explicite

**Anti-patterns IA à bannir** :
- "il est important de noter", "dans un monde en pleine évolution"
- "crucial", "groundbreaking", "comprehensive", "landscape", "pivotal"
- La règle de 3 systématique
- Bold excessif sur les premiers mots de chaque paragraphe
- Listes à puces dans le corps du texte
- Conclusion-résumé qui répète ce qui vient d'être dit
- Méta-introduction ("Dans cet article, nous allons voir...")
- Émojis (sauf si l'utilisateur demande explicitement)

## Détail des 8 étapes

### Étape 1 — Surprise Gap

Identifier ce que 80 % des articles existants disent (angles saturés) vs ce qui manque (infos sous-exploitées). Classer les 5 infos sous-exploitées par gradient d'information décroissant.

Output : tableau à 2 colonnes (saturé / sous-exploité) avec 5 entrées chacune, scoré.

Puis appliquer `.seokb/base/wiki/methodes/questions-par-perspective.md` : les infos sous-exploitées se cherchent aussi dans les désaccords et les trous entre perspectives sourcées. Si le brief source contient déjà un tableau « Perspectives », le reprendre au lieu de le refaire.

### Étape 2 — Ancrage local

Identifier les signaux E-E-A-T géographiques précis pour le secteur et la localisation. Citer des acteurs réels (OPCO, fédérations professionnelles, écosystèmes locaux), des chiffres locaux, des références régionales.

Output : 5-10 signaux d'ancrage local prêts à intégrer.

### Étape 3 — Données chiffrées

Collecter 8-12 statistiques sourcées via WebSearch ou KB. Chaque chiffre = source + argument + contexte. Ne JAMAIS inventer un chiffre. Marquer `[DONNÉE À SOURCER]` si une stat est utile mais non vérifiée.

Output : tableau structuré chiffre / source / argument / contexte.

### Étape 4 — Inversions expertes

Identifier 5 croyances fausses largement répandues sur le sujet, et formuler la réalité + pourquoi l'erreur persiste + formulation prête à intégrer dans l'article.

Output : tableau à 4 colonnes (croyance / réalité / cause persistance / formulation).

### Étape 5 — Architecture narrative

Construire le plan section par section. Pour chaque section : rappel de la précédente (Low Surprise contextuelle) + contenu nouveau (High Surprise informationnelle).

Pas de transition artificielle entre sections : deux sections peuvent s'enchaîner sans phrase de liaison (règle mère, ton-de-voix § 0).

Intégrer le passage ancré (150-200 mots) dans les 300 premiers mots, et le bloc authorship (~50 mots) extractible.

Output : plan structuré complet avec longueurs cibles par section.

### Étape 6 — Rédaction principale

Rédiger la prose complète selon le plan. Pattern Tension → Résolution → Preuve sur chaque idée. Vérifier en continu l'absence d'anti-patterns IA (cf. règles ci-dessus).

Output : prose 2000-2500 mots.

### Étape 7 — FAQ micro-intentions

Générer 6-8 questions bas de funnel non traitées dans le corps de l'article. Chaque question = 1 micro-intention distincte. Réponse courte, actionnable, citable isolément (AI Overview ready).

Output : section FAQ avec 6-8 questions/réponses.

### Étape 8 — Compilation finale

Assembler les 7 outputs précédents en un article complet. Vérifier fluidité, supprimer répétitions, contrôler une dernière fois les anti-patterns IA. Produire la checklist qualité.

Output : article complet + checklist qualité.

## Critère de qualité

L'article est bon si toutes ces conditions sont réunies :
- Surprise Gap identifié et exploité (au moins 3 des 5 infos sous-exploitées intégrées)
- Ancrage local réel (acteurs nommés, pas génériques)
- 8-12 données sourcées intégrées dans le corps
- 3+ inversions expertes citées
- Passage ancré 150-200 mots présent dans les 300 premiers mots
- Bloc authorship ~50 mots extractible
- Zéro pattern IA détectable
- FAQ 6-8 questions intégrée
- 2000+ mots en prose continue (zéro bullet décoratif)

## Sauvegarde

Le livrable final est un fichier markdown unique sauvegardé avec le format :
`article-[slug-du-titre]-YYYY-MM-DD.md`

## Ce que ce skill ne fait PAS

- Pas de décodage sémantique RRF en amont (utiliser `article-engine-pipeline` pour ça)
- Pas de FAQ stratégique FM en parallèle (utiliser `article-engine-pipeline` phase 3)
- Pas de checklist fact-check en aval (utiliser `article-engine-pipeline` phase 5)
- Pas d'invention de chiffres — toujours sourcer ou marquer `[DONNÉE À SOURCER]`
