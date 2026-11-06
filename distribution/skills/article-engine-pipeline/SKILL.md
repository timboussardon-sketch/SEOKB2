---
name: article-engine-pipeline
description: "Article SEO complet depuis un brief en Hn : RRF, FAQ, rédaction 8 étapes, fact-check. « rédige un article », « j'ai un brief prêt »."
---

# Article Engine Pipeline — Rédaction SEO complète en 5 phases

## Quand utiliser ce skill

Pipeline complet de rédaction d'article SEO en 5 phases automatisées. L'utilisateur fournit un brief structuré par Hn (avec mots-clés, idées, data par section), et le skill enchaîne : décodage sémantique RRF de la requête → génération FAQ stratégique FM → workflow rédaction 8 étapes (Surprise Gap, Ancrage, Données, Inversions, Architecture, Rédaction, FAQ, Compilation) → checklist de fact-check pour vérification manuelle.

TOUJOURS utiliser ce skill quand l'utilisateur mentionne : "rédige un article", "lance le pipeline de rédaction", "article engine", "article complet", "j'ai un brief prêt", "voilà mes Hn", "lance la rédaction à partir de mon brief", "rédaction SEO complète", "pipeline article", "workflow rédaction complet", "article de A à Z", ou quand il fournit une structure Hn avec des idées/data et veut un article complet. Utiliser aussi quand l'utilisateur dit "améliore cet article avec le workflow" ou "passe cet article dans le pipeline".

## Process en 4 phases validées (règle Tim, 2026-10-21) — prime sur tout le reste

Consigne de Tim : « TOUJOURS RESPECTER, TOUJOURS : brief, structure Hn, ensuite ajoute data dans le Hn, puis rédaction. Chaque phase doit être validée par le consultant. »

| Phase | Livrable montré au consultant | Étapes du skill mobilisées |
|---|---|---|
| 1. Brief | Brief (skill `seo-brief-contenu`) : requête, intention, angle, cible, Surprise Gap | Phase 1 (brief) + phase 2 (décodage RRF) qui l'alimente |
| 2. Structure Hn | H1/H2/H3 seuls, sans prose (skill `seo-structure-hn-v2`) | Étape 5 de `seo-workflow-article`, réduite aux Hn |
| 3. Data dans les Hn | La même structure Hn, avec sous chaque H2/H3 les chiffres, sources, verbatims, cas et inversions qui le nourrissent ; trou = `[MATIÈRE MANQUANTE]` | Étapes 2, 3, 4 de `seo-workflow-article` rangées sous chaque Hn |
| 4. Rédaction | Texte rédigé à partir de la phase 3 validée, rien d'autre | Étapes 6, 7, 8 + phase 3 (FAQ) + phase 5 (fact-check) |

Règles :
- **Une phase par tour.** Livrer la phase, puis s'arrêter et demander la validation. Jamais deux phases dans la même réponse, même si la suite paraît évidente.
- **Validation = accord explicite du consultant** sur cette phase. Le silence, un « ok continue » donné sur une autre phase, ou un brief fourni par l'utilisateur sans mot de validation ne valent pas validation.
- **Une correction relance la même phase** : on la corrige, on la remontre, on attend l'accord. On ne passe pas à la suivante avec les corrections « intégrées en route ».
- **Matière fournie par l'utilisateur** (brief ou Hn déjà prêts) : la présenter comme livrable de la phase correspondante et demander la validation avant de passer à la suivante.
- **Aucune phase sautée**, y compris pour un article court ou urgent. La rédaction n'utilise que la data posée et validée en phase 3 : une info absente de la phase 3 n'entre pas dans le texte.
- Sauvegarder chaque phase validée dans le fichier de travail, avec la date de validation.

## Vue d'ensemble

Ce pipeline prend un brief structuré par Hn et produit un article SEO complet, prêt à publier, avec une FAQ stratégique FM et une checklist de fact-check.

```
INPUT : Brief structuré (Hn + mots-clés + idées + data par section)
  │
  ├─► Phase 1 — BRIEF (fourni par l'utilisateur)
  │     L'utilisateur donne ses Hn avec mots-clés intégrés,
  │     ses idées, points clés et data pour chaque section.
  │
  ├─► Phase 2 — DÉCODAGE SÉMANTIQUE RRF
  │     Décoder la requête principale : entités, intentions,
  │     cluster sémantique, vecteurs multimodaux, specs FM.
  │     → Utilise le prompt "Query requête" (references/query-requete.md)
  │
  ├─► Phase 3 — FAQ STRATÉGIQUE FM
  │     Générer 5-7 questions FAQ stratégiques.
  │     Chaque question = 1 vecteur sémantique distinct.
  │     → Utilise le prompt "FAQ Query" (references/faq-query.md)
  │
  ├─► Phase 4 — WORKFLOW RÉDACTION 8 ÉTAPES
  │     Surprise Gap → Ancrage → Données chiffrées → Inversions
  │     → Architecture narrative → Rédaction → FAQ intégrée → Compilation
  │     → Utilise le skill `seo-workflow-article`
  │
  ├─► Phase 5 — CHECKLIST FACT-CHECK
  │     Liste chaque chiffre, source, et ce qu'il faut vérifier.
  │     L'utilisateur vérifie manuellement (Grok ou autre).
  │
  OUTPUT : Article complet (.md) + Checklist fact-check
```

---

## Comment l'utilisateur fournit son brief

L'utilisateur arrive avec un document structuré qui ressemble à ça :

```
H1: [Titre avec mot-clé principal]

H2: [Sous-titre avec mot-clé]
- Idée 1
- Data point X
- Angle à explorer

H2: [Sous-titre avec mot-clé]
- Point clé
- Statistique Y
- Mon avis sur Z

H2: [Sous-titre avec mot-clé]
...
```

Les mots-clés sont déjà dans les Hn. Les idées/data sont en vrac sous chaque Hn. C'est le matériau brut que le pipeline va transformer.

L'agent doit collecter ces variables si elles ne sont pas explicites dans le brief :

```
REQUÊTE CIBLE     : [extraite du H1 ou demandée]
PAYS/LANGUE       : [FR/FR par défaut]
PERSPECTIVE       : [B2B ou B2C + rôle + contexte]
OBJECTIF          : [Lead Gen / Conversion / Expertise FM]
SECTEUR           : [secteur d'activité]
AUDIENCE          : [qui va lire]
LOCALISATION      : [zone géographique si pertinent, sinon "N/A"]
```

Si ces infos manquent, les demander à l'utilisateur AVANT de lancer le pipeline. Ne pas deviner.

---

## Phase 2 — Décodage sémantique RRF

Objectif : avant de rédiger quoi que ce soit, comprendre en profondeur ce que Google et les moteurs IA attendent pour cette requête. Sans ce décodage, on écrit à l'aveugle.

Lire et exécuter le prompt complet dans `references/query-requete.md`.

Le prompt se déploie en 3 phases :
1. **Décodage lexical** — entités, relations, intentions (primaire + latentes), signaux RRF
2. **Reverse engineering des vecteurs sémantiques** — top concepts pondérés, cluster sémantique avec micro-intentions, priorisation P1/P2/P3
3. **Vecteurs multimodaux & Effort** — formats non textuels requis pour FM, piliers E-E-A-T, spécifications de page FM

Variables à injecter dans le prompt :
- `{{requete}}` → la requête cible extraite du H1
- `{{FR/FR}}` → pays/langue
- `{{persona/contexte}}` → perspective utilisateur
- `{{transactionnel/lead gen/informationnel}}` → contrainte business

Livrable : un document structuré avec le décodage complet. Ce document sert d'input pour les phases suivantes — le Surprise Gap et l'architecture narrative s'appuient dessus.

---

## Phase 3 — FAQ stratégique FM

Objectif : générer 5 à 7 questions FAQ qui renforcent le score RRF et éliminent la nécessité de requête secondaire.

Lire et exécuter le prompt complet dans `references/faq-query.md`.

Ce prompt est strict :
- Chaque question active un vecteur sémantique unique
- Zéro chevauchement entre questions
- Exclure toute question pédagogique ou générique
- Chaque réponse est courte, actionnable, citable isolément (AI Overview ready)
- Verrouillage B2B/B2C selon la perspective définie en phase 1

Variables à injecter :
- `{{requete}}` → la requête cible
- `{{B2B ou B2C + rôle + contexte}}` → perspective utilisateur (OBLIGATOIRE)
- `{{Lead Gen / Conversion / Expertise FM}}` → objectif stratégique

Livrable : 5-7 questions avec réponses et vecteur sémantique couvert pour chacune. Ces questions seront intégrées à l'étape 7 du workflow rédaction.

---

## Phase 4 — Workflow rédaction 8 étapes

C'est le coeur du pipeline. Lire et exécuter le skill `seo-workflow-article` dans son intégralité.

Les 8 étapes sont séquentielles — chaque étape alimente la suivante :

1. **Surprise Gap** — identifier ce que 80% des articles disent vs ce qui manque. Utiliser le décodage RRF de la phase 2 pour alimenter le diagnostic.
2. **Ancrage local/sectoriel** — signaux E-E-A-T géographiques et sectoriels précis
3. **Données chiffrées** — 8-12 statistiques sourcées, argumentatives pas décoratives. Utiliser WebSearch pour chercher des données récentes. Chaque chiffre = source + argument + contexte.
4. **Inversions expertes** — 5 croyances fausses corrigées avec preuves
5. **Architecture narrative** — plan Low→High Surprise section par section. Intégrer le passage ancré (150-200 mots) et le bloc authorship (~50 mots).
6. **Rédaction principale** — prose 2000-2500 mots, pattern Tension→Résolution→Preuve. Anti-patterns IA vérifiés.
7. **FAQ intégrée** — reprendre les questions de la phase 3 et les intégrer en fin d'article. Ajuster les réponses si le corps de l'article a déjà traité certains points.
8. **Compilation finale** — tout assembler, vérifier fluidité, supprimer répétitions, contrôler anti-patterns IA.

L'input du brief utilisateur (ses idées, points, data par Hn) doit être intégré dans chaque étape pertinente. Ce n'est pas du contenu à ignorer — c'est la matière première de l'article.

### Style de rédaction

Avant de rédiger, lire le fichier `references/style-timothee.md` pour le ton et le style.

Points non négociables :
- Ton conversationnel direct, phrases courtes
- Vouvoiement pour le groupe, tutoiement pour les apartés personnels
- Opinions tranchées, jamais neutre
- Apartés entre parenthèses avec ton décontracté
- Zéro superlatif, zéro formule creuse, zéro pattern IA
- Formulations signatures : "Le vrai sujet c'est...", "J'en parle depuis un moment", "C'est tant mieux", "c'est OK"

---

## Phase 5 — Checklist fact-check

Objectif : permettre à l'utilisateur de vérifier chaque affirmation chiffrée sur Grok ou un autre outil.

Générer un tableau/liste structurée avec pour chaque chiffre cité dans l'article :

```
CHIFFRE : [la stat exacte telle qu'écrite dans l'article]
SOURCE CITÉE : [nom de la source]
URL SOURCE : [si disponible, sinon "à chercher"]
CE QU'IL FAUT VÉRIFIER : [question précise à poser à Grok]
CONFIANCE : [haute / moyenne / basse — selon la qualité de la source]
```

Classer par niveau de confiance (basse en premier — ce sont les priorités de vérification).

Ajouter en fin de checklist :
- Nombre total de chiffres à vérifier
- Nombre de sources uniques
- Nombre de chiffres "confiance basse" (prioritaires)

---

## Orchestration du pipeline

L'agent ne saute AUCUNE phase. L'ordre est strict : 2 → 3 → 4 → 5.

Entre chaque phase du process en 4 phases validées (brief → structure Hn → data dans les Hn → rédaction), l'agent produit le livrable de la phase, s'arrête et attend la validation explicite du consultant. Il ne passe jamais à la phase suivante sans cet accord (règle Tim du 2026-10-21, remplace l'ancien enchaînement sans validation).

Le livrable final est un fichier markdown unique contenant l'article complet, sauvegardé dans le dossier outputs avec le format :
`article-[slug-du-titre]-YYYY-MM-DD.md`

La checklist fact-check est sauvegardée séparément :
`factcheck-[slug-du-titre]-YYYY-MM-DD.md`

---

## Ce que l'agent NE FAIT PAS

- Ne pas inventer de données chiffrées — tout doit être sourcé ou marqué `[DONNÉE À SOURCER]`
- Ne pas sauter le Surprise Gap — c'est ce qui empêche d'écrire un article de plus
- Ne pas ignorer le brief utilisateur — ses idées/data par Hn SONT le matériau de l'article
- Ne pas copier la structure des concurrents
- Ne pas produire de bullet points dans le corps de l'article (prose uniquement)
- Ne pas ajouter d'intro méta ("Dans cet article, nous allons voir...")
- Ne pas ajouter de conclusion-résumé qui répète ce qui vient d'être dit
