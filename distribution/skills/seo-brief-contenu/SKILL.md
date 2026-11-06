---
name: seo-brief-contenu
description: "Brief éditorial avec structure Hn pour le Passage Ranking. « brief », « plan de rédaction SEO », « brief éditorial »."
---

# Skill — Brief de Contenu & Structure Hn

## Quand utiliser ce skill

Brief éditorial complet avec structure Hn optimisée pour le Passage Ranking, basé sur les vecteurs sémantiques attendus par Google. Ne copie jamais les concurrents — au contraire identifie ce qu'ils n'ont pas dit. Pipeline en 7 étapes : décodage requête → vecteurs sémantiques → micro-intentions → structure Hn → contenu par H2 → signaux E-E-A-T → format multimodal. Sortie obligatoire : une section de pré-décision (statut RAW / HYPOTHÈSE / VALIDÉ / OBSOLÈTE / BLOQUÉ, pré-décision URL par cluster ou raison de non-décision, score business sur 5, documents du vault, matière qualifiée, SERP) qui nourrit le rapport de pré-décision du workflow mots-clés ; sans elle le skill n'a pas terminé.

TOUJOURS utiliser ce skill quand l'utilisateur dit : "brief", "structure Hn", "plan de page", "quels H2 mettre", "plan de rédaction SEO", "brief éditorial", "structure d'article SEO".

## Quand déclencher

Produire un brief éditorial complet avec structure Hn optimisée pour le Passage Ranking, basé sur les vecteurs sémantiques — sans copier les concurrents.

## Doctrine

- La structure Hn est la colonne vertébrale du ranking. Mauvais plan = mauvais contenu.
- On regarde les concurrents pour identifier ce qu'ils **n'ont pas dit**, pas pour copier.
- Le brief est rédigé en premier par l'humain. L'IA améliore, elle ne crée pas.
- Chaque H2 = un vecteur sémantique attendu par Google.
- Au moins 1 H2 doit générer un Surprise Gap (contre-intuitif ou différenciant).

## Input requis

| Source | Obligatoire |
|--------|-------------|
| Mot-clé principal + cluster de requêtes | Oui |
| Micro-intentions / FAQ patterns | Oui |
| Contexte E-E-A-T (cas concrets, données propriétaires) | Recommandé |
| Type de page (landing, article, pilier) | Recommandé |

## Structure V2 (skill `seo-structure-hn-v2`)

L'étape « structure Hn » du pipeline suit `seo-structure-hn-v2` : modèle Hn (pattern 1), contenu par section réponse directe / preuve / détails / limite (pattern 2), article de méthode en mini-formation (pattern 3). Brief : une section sans matière qualifiée est marquée `[MATIÈRE MANQUANTE]`.

## Pipeline (7 étapes)

1. **Décoder la requête** — intention primaire (Info/Trans/Nav/Déc) + intentions latentes
2. **Lister les vecteurs sémantiques** — entités, co-occurrences, vocabulaire expert
3. **Identifier les micro-intentions** — avant/pendant/après la décision
3 bis. **Questions par perspective** — appliquer `.seokb/base/wiki/methodes/questions-par-perspective.md` (praticien, recherche, sceptique, argent, acheteur ; chaque réponse sourcée, sinon `[MATIÈRE MANQUANTE]`). Les désaccords et les trous donnent les H2 différenciants ; le tableau « Perspectives » va dans le brief
4. **Construire la structure Hn** — H1 avec différenciateur + H2 vecteurs + H3 micro-intentions + H2 FAQ
5. **Définir le contenu par H2** — type, longueur, éléments obligatoires
6. **Identifier les signaux E-E-A-T** — expérience, expertise, autorité, confiance
7. **Définir le format multimodal** — vidéo, tableau, calculateur, template

## Sortie de pré-décision (obligatoire)

Ce skill est une étape du workflow mots-clés complet (onglet Mots-clés du dashboard). Sa sortie porte un `statut_decision` (RAW, HYPOTHÈSE, VALIDÉ, OBSOLÈTE, BLOQUÉ) et nourrit le rapport de pré-décision, seule sortie visible du workflow ; toute sortie de ce skill qui contredit ce rapport devient OBSOLÈTE. Format complet : `.seokb/base/wiki/methodes/rapport-mots-cles-format.md`.

Ce que le rapport de pré-décision rend, et que ce skill doit rendre possible sur son périmètre :

1. Diagnostic en trois lignes.
2. Pré-décision par marché (5 max) : Marché / Page / Score business sur 5 (intention 0-2, proximité offre 0-2, conversion directe 0-1) / Docs du vault (documents qui traitent le sujet, par type : transcripts, clients, notes, wiki) / Matière qualifiée (objection, cas, méthode, preuve, résultat, verbatim) / SERP (compatible, à vérifier, non vérifiée) / Pré-décision (utiliser, renforcer l'existant, créer, conserver et enrichir, analyser avant restauration, candidat avec validation SERP requise, bloqué, attendre).
3. Ce qui est bloqué, et par quoi : statut, raison, actions autorisées, actions interdites ; « décision stratégique requise » quand c'est le positionnement (c'est ta décision) ; « pré-décision impossible avant analyse SERP de N requêtes » sinon. Jamais « à trancher ».
4. À ne pas produire maintenant.
5. Fiabilité, une ligne ; analyse technique derrière ; logs du workflow en annexe.

Règles : signaux de demande séparés (Suggest, Search Console, calls, acteurs), jamais agrégés en verdict, aucun volume estimé ; matière comptée en documents du vault puis qualifiée par lecture, jamais en occurrences d'un mot ; « cannibalisation » interdit sans SERP ni conflit GSC, « chevauchement potentiel à vérifier » ; une requête secondaire sert à repérer une sous-intention, jamais à placer un title, un H2 ou une FAQ par défaut ; aucune page sans validation SERP + matière suffisante ; aucun brief avant une pré-décision URL VALIDÉ ; un cas ou un relevé réel par page programmatique ; scores /10 en backend ; Faible / Moyen / Élevé, jamais d'anglais ; la certitude affichée ne dépasse jamais la couverture des données.

## Output obligatoire

```
BRIEF — '[Mot-clé principal]'

## Intention
- Primaire : [Type] — [Description]
- Latentes : [Liste]

## Vecteurs sémantiques clés
[Entités, co-occurrences, vocabulaire expert]

## Structure Hn
H1 : [Titre + différenciateur]
H2 : [Vecteur 1 — Gradient de Surprise si applicable]
  H3 : [Micro-intention]
H2 : FAQ décisionnelle
  H3 : [Question bas de funnel]

## Signaux E-E-A-T à injecter
## Format multimodal requis
```

## Patron — Page Marque / Solution (SaaS / B2B)

Principalement pour les SaaS ou entreprises B2B.

```
H1 — [Catégorie de solution] pour [besoin principal]

INTRODUCTION
Problème concret du lecteur.
Réponse immédiate au besoin.
Présentation : [Marque] est [catégorie] qui permet de [fonction précise].
Une preuve pertinente, si disponible.

H2 — Dans quels cas utiliser [solution] ?
    H3 — Pour [besoin concret / profil 1]
    H3 — Pour [besoin concret / profil 2]
    H3 — Quand une autre solution est plus adaptée

H2 — Comment [obtenir le résultat recherché] avec [marque] ?
    H3 — [Première étape concrète]
    H3 — [Deuxième étape concrète]
    H3 — [Résultat obtenu et utilisation]

H2 — [Question sur le principal critère de choix]
    H3 — [Ce qui est possible et dans quelles conditions]
    H3 — [Restrictions ou limites à connaître]

H2 — Quels résultats avons-nous observés sur [usage précis] ?
    H3 — [Méthode et conditions du test]
    H3 — [Résultats mesurés et limites observées]

H2 — [Marque] ou [alternatives] : quelles différences ?
    Tableau comparatif sur les mêmes critères.
    Sources, offres concernées et date de vérification.

H2 — Combien coûte [solution] et que comprend le prix ?
    Prix, unité de facturation, engagement et restrictions.

H2 — Questions pratiques sur [sujet]
    H3 — [Question importante non traitée dans la page]
    H3 — [Objection restante]
    H3 — [Cas particulier pertinent]
```

### Contenu type d'un H2 — question

```
H2 — Une question précise du lecteur

RÉPONSE DIRECTE
Répondre immédiatement, en quelques phrases.
Nommer la solution ou le sujet concerné.
Préciser les conditions importantes.

PREUVE
Ajouter un résultat mesuré, un exemple réel,
une démonstration ou une source vérifiable.

DÉTAILS UTILES
Développer uniquement ce qui aide à comprendre ou décider.
Utiliser des H3 si plusieurs sous-questions le justifient.

LIMITE
Indiquer ce qui n'est pas couvert, ce qui dépend de l'offre,
ou ce qui nécessite une vérification humaine.
```

## Règles absolues

- Gouvernance des pré-décisions : une pré-décision finale par cluster avec statut VALIDÉ / À VÉRIFIER / BLOQUÉ / REJETÉ ; les sorties de ce skill sont des HYPOTHÈSES tant que le rapport n'a pas tranché, et deviennent OBSOLÈTES si elles le contredisent ; aucune page créée sans validation SERP + matière suffisante ; aucun brief avant une pré-décision URL VALIDÉ ; un candidat à la création reste « validation SERP requise » ; les scores /10 restent en backend, le rapport lit adéquation offre, intention, preuve, SERP, décision.
- Aucun brief n'est généré tant que la pré-décision URL du cluster n'est pas VALIDÉ dans le rapport mots-clés ; un cluster BLOQUÉ ou À VÉRIFIER donne un fichier marqué BLOQUÉ, pas un brief.
- Ne pas copier la structure des 3 premiers résultats Google
- Pas de H2 génériques : "Introduction", "Conclusion", "Notre avis"
- Pas de plan sans FAQ ni sous-angles
- Toujours justifier chaque H2 par un vecteur sémantique identifié

## Sauvegarde

Output dans `wiki/briefs/YYYY-MM-DD-slug.md` selon hook §7 AGENTS.md.

## Concepts liés

`vecteurs-semantiques` · `surprise-gap` · `passage-ranking` · `grounding-score` · `e-e-a-t` · `fully-meets`

## Vérification finale (obligatoire)

Avant de présenter le livrable comme terminé : lancer le skill `verification-livrable` (demande de l'utilisateur, tous les skills utilisés, livrables, sources, contraintes). Corriger les ❌, relancer le vérificateur sur la nouvelle version, recopier le dernier tableau dans la réponse. Un hook refuse la fin de la réponse tant que ce n'est pas fait.
