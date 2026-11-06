---
name: seo-needs-met-rrf
description: "Reverse engineering sémantique d'une requête pour viser Fully Meets. « Needs Met », « Fully Meets », « score RRF »."
---

# Skill — Needs Met & RRF (Reverse Engineering Sémantique)

## Quand utiliser ce skill

Reverse engineering sémantique d'une requête pour viser Highly Meets (HM) ou Fully Meets (FM) au sens des Quality Raters, et maximiser le score RRF (Reciprocal Rank Fusion) du cluster. Pipeline en 3 phases : décodage lexical (entités, intentions, signaux RRF de base) → reverse engineering du vecteur sémantique (concepts pondérés + cluster fan-out priorisé P1/P2/P3) → vecteurs multimodaux et piliers E-E-A-T requis pour FM (spécifications de page).

TOUJOURS utiliser ce skill quand l'utilisateur dit : "reverse engineering sémantique", "Needs Met", "Highly Meets", "Fully Meets", "HM/FM", "score RRF", "Reciprocal Rank Fusion", "vecteur sémantique de la requête", "quelles pages pour satisfaire l'intention", "Quality Raters", "cluster RRF", "quels formats multimodaux pour cette requête".

## Quand déclencher

Décoder une requête pour cartographier entités/intentions/signaux HM-FM, simuler son vecteur sémantique, déployer un cluster optimisé RRF, et spécifier ce qui manque (y compris hors texte) pour décrocher Fully Meets.

## Rôle

Expert SEO & ingénieur IA spécialisé en reverse engineering sémantique, optimisation RRF et satisfaction d'intention (Needs Met). Objectif : livrables actionnables visant HM ou FM et maximisant le score RRF du cluster sémantique.

## Concepts clés

- **Needs Met / Quality Raters** — échelle Google (Fails to Meet → Slightly → Moderately → Highly Meets → Fully Meets) qui juge si une page satisfait entièrement l'intention derrière une requête.
- **RRF (Reciprocal Rank Fusion)** — méthode de fusion de classements ; un cluster qui couvre toutes les sous-intentions avec des pages diversifiées et pertinentes remonte mieux qu'une page isolée.
- **Vecteur sémantique / embedding conceptuel** — représentation pondérée des concepts qu'une page doit couvrir pour s'aligner avec l'intention réelle.
- **Vecteurs multimodaux** — preuves non textuelles (schémas, vidéo, simulateur, tableaux, datasets) parfois indispensables pour passer de HM à FM.

## Entrées

- **REQUETE** (obligatoire) — la requête à décoder.
- **PAYS/LANGUE** (optionnel, défaut FR/FR).
- **PERSPECTIVE_UTILISATEUR** (optionnel) — persona / contexte d'usage.
- **CONTRAINTE_BUSINESS** (optionnel) — transactionnel / lead gen / informationnel.

## Pipeline (3 phases)

### Phase 1 — Décodage lexical, entités & intentions (base RRF)

**1.1 Entités & relations**
- Entités primaires (marque, produit, norme, lieu, public, tâche)
- Entités secondaires (synonymes, variantes, contraintes légales/techniques)
- Relations sémantiques (hiérarchie, partie-tout, cause-effet, procédure)

**1.2 Intentions utilisateur**
- Intention primaire (visible) : informationnelle / navigationnelle / transactionnelle / locale
- Intentions secondaires (latentes) : 3 à 5 besoins implicites (risques, coûts, délais, conformité, comparaisons)
- Needs Met cible : HM ou FM + justification — quels critères concrets font basculer HM→FM

**1.3 Signaux RRF de base**
- Types de pages attendues (guide, check-list, devis, comparatif, outil…)
- Ressources concurrentes probables (typologies, jamais de noms de marques concurrentes — cf. [[feedback_jamais_parler_concurrent]])
- Hypothèses de features qui fusionnent bien en RRF (FAQ ciblées, schémas, outil interactif, preuves)

### Phase 2 — Reverse engineering des vecteurs sémantiques

**2.1 Vecteur principal (embedding conceptuel)**
- Top concepts pondérés (5 à 10), poids relatif 0–1
- Contexte d'utilisation (avant / pendant / après l'action)
- Contraintes (légales, techniques, coûts, délais, compétences)

**2.2 Cluster sémantique RRF (fan-out)**
Pour 3 à 6 sous-thèmes, produire :
- Micro-intentions (≥5 au total, idéalement 8–12) formulées comme requêtes concrètes
- Type d'intention (info / transactionnel / local / comparatif)
- Rôle dans HM/FM (quelle lacune ça comble)
- Hook éditorial (angle / USP)

**2.3 Priorisation RRF**
- **P1 (indispensable)** — pages/sections qui élèvent directement HM→FM
- **P2 (fort levier)** — contenus qui augmentent la diversité utile (RRF) et captent les query-outs
- **P3 (moisson)** — longue traîne & variations multimodales

### Phase 3 — Vecteurs multimodaux & effort (stratégie RRF)

**3.1 Besoins multimodaux**
Évaluer si l'intention exige des artefacts non textuels pour FM. Ne cocher que ce qui est réellement nécessaire :
- Schémas/diagrammes (process, architecture, étape par étape)
- Courte vidéo démo / capture d'écran
- Simulateur / calculateur (scénarios, coûts, délais, conformité)
- Tableaux comparatifs normalisés (critères, normes, tolérances)
- Jeux de données / échantillons / modèles téléchargeables

**3.2 Piliers d'effort (E-E-A-T)**
- **Experience** — cas réels, échantillons, métriques terrain
- **Expertise** — références normatives, sources, auteurs qualifiés
- **Authoritativeness** — mentions/partenariats, validations externes
- **Trust** — conformité (mentions légales, RGPD…), politiques, disclaimers
- **Preuves d'effort** — fraîcheur (dates), profondeur technique, précision factuelle

**3.3 Spécifications de page FM**
- Architecture (H1-H3, ancres, modules réutilisables)
- Sections obligatoires : checklist, risques/erreurs, coûts/ROI, process, critères de choix, FAQ anti-rebond
- UX : TOC sticky, résumé exécutif, CTA alignés à l'intention, schémas au-dessus de la ligne de flottaison
- Données structurées : FAQPage, HowTo, Product, LocalBusiness (si pertinent)

## Output obligatoire

```
Requête : "[REQUETE]" — [PAYS/LANGUE]

PHASE 1 — Décodage
Entités primaires : ...
Entités secondaires : ...
Intention primaire : ...
Intentions secondaires (latentes) : 1. ... 2. ... 3. ...
Needs Met cible : HM / FM — justification : ...
Signaux RRF de base : ...

PHASE 2 — Vecteurs sémantiques
Top concepts pondérés :
| Concept | Poids (0-1) |
|---|---|

Cluster RRF (fan-out) :
| Sous-thème | Micro-intention | Type | Rôle HM/FM | Hook éditorial | Priorité P1/P2/P3 |
|---|---|---|---|---|---|

PHASE 3 — Multimodal & E-E-A-T
Formats multimodaux nécessaires pour FM : ...
Piliers E-E-A-T à activer : Experience / Expertise / Authoritativeness / Trust / Preuves d'effort
Spécifications page FM : architecture / sections obligatoires / UX / données structurées
```

## Règles absolues

- Aucun volume de recherche inventé (cf. [[feedback_pas_colonne_volume]]) — ce skill raisonne en intention et en couverture sémantique, pas en trafic.
- Jamais de nom de marque concurrente (cf. [[feedback_jamais_parler_concurrent]]) — parler en typologies de ressources concurrentes.
- Ne cocher un format multimodal en 3.1 que s'il change réellement l'issue HM→FM, pas par exhaustivité cosmétique.
- P1/P2/P3 doit rester priorisé : ne pas livrer une liste plate de pages sans hiérarchie RRF.
- La justification HM→FM (1.2) doit citer des critères concrets, pas une affirmation vague ("plus complet", "plus qualitatif").

## Sauvegarde

Output dans `wiki/queries/needs-met-rrf-YYYY-MM-DD-slug.md` selon hook §7 AGENTS.md.

## Concepts liés

`needs-met` · `quality-raters` · `rrf` · `grounding-score` · `e-e-a-t` · `vecteurs-semantiques` · `seo-entites-vectorielles` · `seo-cluster-aeo`
