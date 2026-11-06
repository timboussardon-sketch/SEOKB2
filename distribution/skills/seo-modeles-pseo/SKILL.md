---
name: seo-modeles-pseo
description: "Modèles de pages satellites décisionnelles autour d'une Money Page. « modèles pSEO », « Money Page + Spokes »."
---

# Skill — Modèles de pages pSEO (Money Page + Spokes)

## Quand utiliser ce skill

Conception des "modèles" de pages satellites décisionnelles (Spokes) autour d'une Money Page : génération de requêtes Ultra Business (Do) réellement tapées par un humain en situation de décision, classification a posteriori en catégories de page, scoring déterministe Proximité × Intention × Faisabilité. Pipeline en 5 étapes : cadrer la Money Page + son point de conversion → générer les requêtes par intention (jamais par catégorie) → filtre de requêtabilité humaine → scorer et dédupliquer → tableau priorisé des modèles de Spokes. Règle anti-hallucination : aucun volume inventé, le décisionnel se repère aux modificateurs.

TOUJOURS utiliser ce skill quand l'utilisateur dit : "modèles pSEO", "pages satellites", "Money Page + Spokes", "génère mes modèles de pages", "architecture money page", "pages décisionnelles autour de [mot-clé]", "Spokes BoFu", "quelles pages business créer autour de mon offre", "modèles de pages programmatiques décisionnelles".

## Quand déclencher

Concevoir les **modèles de pages satellites décisionnelles** (Spokes) qui entourent une Money Page : à partir d'un mot-clé seed et d'une offre, sortir les requêtes Ultra Business qui méritent chacune leur page autonome, scorées et priorisées.

Diffère de `seo-cluster-aeo` (qui bâtit une architecture Know-Simple/Know/Do complète autour d'un pilier) et de `seo-programmatique-pseo` (qui industrialise template + variable). Ici on se concentre sur la **couche décisionnelle** : la Money Page et sa ceinture de Spokes Do.

## Doctrine

- Une **Money Page** capte l'intention de conversion principale ; les **Spokes** sont des pages satellites qui captent chacune une requête décisionnelle distincte et renvoient le link equity et l'utilisateur vers la Money Page.
- Le trafic n'est pas l'objectif, la **conversion** l'est. Une requête à faible volume mais à forte intention d'achat vaut mieux qu'une requête à fort volume sans intention.
- Le décisionnel se repère à ses **modificateurs**, jamais à son volume. Ne jamais scorer une requête sur un volume estimé.
- **Génération par intention, jamais par catégorie.** On génère d'abord les requêtes telles qu'un humain les taperait, on les classe ensuite. Créer une requête pour "remplir une catégorie" est interdit.
- Un Spoke = une requête Do qui justifie une page autonome avec offre + CTA. Sinon ce n'est pas un Spoke, c'est du contenu Know.

## Input requis

| Source | Obligatoire |
|--------|-------------|
| Mot-clé seed / thématique de la Money Page | Oui |
| Offre : ce qu'on vend, prix, point de conversion réel (devis, achat, démo, appel) | Oui |
| Audience / persona décideur | Oui |
| Contexte business spécifique (situation, contraintes) | Recommandé |
| Concurrents (pour les requêtes branded et les comparatifs) | Recommandé |

## Filtre de requêtabilité humaine (bloquant)

Avant tout scoring, chaque requête passe ce test :

> « Un décideur humain, seul, sous pression business, taperait-il exactement cette requête dans Google ? »

Si NON → rejet immédiat, même si la requête active une catégorie autorisée, contient des signaux business forts ou obtiendrait un score élevé.

Chaque requête retenue doit être : formulée comme une vraie requête humaine, porteuse d'une tension décisionnelle explicite, linguistiquement naturelle (phrase ou quasi-phrase).

- Rejeté : `prix accompagnement qualiopi audit` · `comparatif solution qualiopi` · `test service qualiopi` (labels SEO, structures artificielles).
- Accepté : `prix d'un accompagnement qualiopi pour un audit de surveillance` · `quel accompagnement qualiopi choisir pour sécuriser sa certification` · `erreurs à éviter avant de choisir un accompagnement qualiopi`.

## Signaux décisionnels (table des modificateurs)

Une requête est décisionnelle si elle contient au moins un modificateur de cette table :

| Catégorie | Modificateurs |
|-----------|---------------|
| **Achat direct** | acheter, commander, prix, tarif, coût, budget, devis, abonnement, souscrire, payer, s'inscrire |
| **Comparaison** | meilleur, top, vs, comparatif, alternative à, lequel choisir, quelle solution choisir |
| **Évaluation** | avis, test, retour d'expérience, fiable, arnaque |
| **Local / immédiat** | près de moi, [ville], en ligne, livraison, ouvert |
| **Marque** | [ta marque], [ta marque] avis/prix, [concurrent] alternative |
| **Délégation** | accompagnement, prise en charge, clé en main, externaliser, prestataire, agence, expert |

## Catégories de modèles de Spokes (classification a posteriori)

Les catégories servent uniquement à classer une requête déjà générée, jamais à la générer. Une catégorie n'est utilisée que si la requête est réellement requêtable et a un intérêt business crédible pour le seed.

Pricing / Cost · Comparaison de prix · Reviews / Avis · Best option (choix du prestataire) · Comparatif de solutions · Pièges à éviter · Étapes du service/produit · Test du service/produit · Outil / Solution · Roadmap / Plan d'action · Use case client · Transition « passer de X à Y » · Installation / Mise en place · Annulation / Sortie.

## Scoring déterministe — Score Business

Le score n'est **pas une somme pondérée**, c'est un **produit de trois facteurs**. Si un facteur est faible, le score s'effondre : un Spoke ne convertit que si les trois sont réunis.

**Score Business = Proximité à l'offre × Intention d'achat × Faisabilité de ranker**

- **Proximité à l'offre** — à quel point la requête colle à ce qu'on vend et à son point de conversion réel.
- **Intention d'achat** — à quel point l'internaute est prêt à payer, comparer, choisir ou déléguer ; mesurée par les modificateurs présents, jamais par le volume.
- **Faisabilité de ranker** — à quel point on peut raisonnablement se positionner.

Noter chaque facteur de **1 à 5**, multiplier les trois, ramener le résultat sur une **échelle 0-10 (arrondi entier)**. Scoring strictement déterministe, aucune interprétation manuelle.

## Déduplication sémantique

Les termes prix / coût / tarif / budget sont des synonymes business. Deux requêtes sont des doublons si elles déclenchent la même décision business et répondent à la même question implicite — seule la formulation SEO diffère. Conserver la requête la plus naturelle, la plus générique commercialement, la plus stable (canonique). Interdiction de créer deux Spokes sur des synonymes stricts.

## Pipeline (5 étapes)

1. **Cadrer la Money Page** — définir le mot-clé seed, l'offre, le prix, le point de conversion réel et le persona. La Money Page est la cible vers laquelle tous les Spokes maillent.
2. **Générer les requêtes par intention** — produire 15 à 25 requêtes telles qu'un décideur humain sous pression les taperait. Exclure tout Know-Simple/Know pur, toute requête sans décision immédiate possible, toute requête ambiguë. Chaque requête doit porter au moins un modificateur décisionnel. Si une année est nécessaire : 2026 ou ultérieur.
3. **Filtre de requêtabilité humaine** — appliquer le test bloquant ; rejeter sans pitié les labels SEO et structures artificielles.
4. **Scorer et dédupliquer** — calculer le Score Business (produit des 3 facteurs ramené sur 0-10, arrondi entier) ; dédupliquer les synonymes business ; classer chaque requête a posteriori dans une catégorie de modèle.
5. **Livrable** — tableau des modèles de Spokes trié par Score Business décroissant ; pour chacun : catégorie, requête cible, intention, score, format de page recommandé et ancre de maillage vers la Money Page.

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
MODÈLES pSEO — Money Page : '[Mot-clé seed / offre]'
Point de conversion : [devis / achat / démo / appel]

| Catégorie | Requête cible | Intention | Score Business /10 | Format de page | Ancre → Money Page |
|---|---|---|---|---|---|
| Pricing / Cost | prix d'un accompagnement qualiopi pour un audit de surveillance | Connaître le budget avant de déléguer | 8 | Page tarif + simulateur | "accompagnement qualiopi" |
| Best option | quel accompagnement qualiopi choisir pour sécuriser sa certification | Choisir un prestataire | 7 | Page comparatif + verdict | "notre accompagnement" |
| ... | ... | ... | ... | ... | ... |

Top 3 Spokes à créer en premier : [liste + justification]
Maillage : chaque Spoke pointe vers la Money Page ; la Money Page liste les Spokes en cross-sell.
```

## Règle anti-hallucination (absolue)

- Ne jamais inventer ni afficher un volume de recherche : une requête est décisionnelle par ses modificateurs, pas par sa popularité supposée.
- Si une donnée chiffrée est nécessaire (prix de marché, statistique), placeholder `[À SOURCER]`.
- Ne pas inventer de marque concurrente : utiliser les concurrents réellement fournis.

## Règles absolues

- Gouvernance des pré-décisions (24 septembre, `.seokb/base/wiki/methodes/rapport-mots-cles-format.md`) : une pré-décision finale par cluster avec statut VALIDÉ / À VÉRIFIER / BLOQUÉ / REJETÉ ; les sorties de ce skill sont des HYPOTHÈSES tant que le rapport n'a pas tranché, et deviennent OBSOLÈTES si elles le contredisent ; aucune page créée sans validation SERP + matière suffisante ; aucun brief avant une pré-décision URL VALIDÉ ; un candidat à la création reste « validation SERP requise » ; les scores /10 restent en backend, le rapport lit adéquation offre, intention, preuve, SERP, décision.
- Règle centrale, pas une note finale : un cas client ou un relevé réel par page, sinon la page n'existe pas. Un template ne justifie rien ; ne proposer que les secteurs avec demande observée, SERP compatible, vraie matière, offre réelle et preuve propre au secteur.
- Exclure toute requête Know-Simple ou Know pure : ce skill ne produit que des Spokes décisionnels Do.
- Aucune requête générée pour remplir une catégorie — les catégories classifient, jamais ne génèrent.
- Chaque Spoke pointe vers une page avec offre + CTA, et maille vers la Money Page, sinon il ne convertit pas.
- Requête branded concurrent → vérifier la légitimité : page comparative honnête, aucune tromperie.
- Prioriser proximité à l'offre + faisabilité, jamais le volume brut.
- Pas deux Spokes sur des synonymes stricts (cannibalisation).

## Enchaînement workflow

En amont : `seo-mots-cles-decisionnels` (isole les requêtes Do d'une liste), `seo-cluster-aeo` (l'architecture Know-Simple/Know/Do dont la couche Do alimente les Spokes). En aval : `seo-product-led-seo` (pour les Spokes au format outil), `seo-brief-contenu` (briefer chaque Spoke), `maillage-systeme` (formaliser le maillage Spokes → Money Page).

## Sauvegarde

Output dans `wiki/clusters/modeles-pseo-YYYY-MM-DD-slug.md` selon hook §7 AGENTS.md.

## Concepts liés

`know-simple-know-do` · `funnel` · `aeo` · `rrf` · `product-led-seo` · `maillage-interne` · `cannibalisation` · `surprise-gap` · `e-e-a-t`
