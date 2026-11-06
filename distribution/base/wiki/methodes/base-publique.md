---
type: concept
title: Base publique
aliases: [base-publique, corpus-de-confiance, public-trust-corpus]
tags: [seo-ia, geo, eeat, entites, maillage, corroboration-externe]
created: 2026-08-29
updated: 2026-08-29
sources: 1
confidence: high
status: stable
---

# Base publique

Corpus public, structuré et crawlable de réponses fiables et vérifiables sur une marque, construit pour être découvert, recoupé et cité par les moteurs de recherche classiques ET par les systèmes de recherche IA (Google AI Overview, ChatGPT, Perplexity, Gemini). Ce n'est **pas** une base de données à laquelle un moteur IA aurait un accès privilégié — c'est l'empreinte publique de la marque sur les questions de confiance de son secteur.


## Le principe général (au-delà du cas RGPD)

Toute marque a des **questions de confiance** propres à son secteur — les questions qu'un acheteur ou un décideur se pose avant de choisir, et auxquelles il veut une réponse vérifiable, pas une affirmation marketing. Pour un AI Notetaker, c'est le RGPD, l'hébergement, les sous-traitants IA. Mais le mécanisme est générique :

| Secteur / site | Question de confiance type |
|---|---|
| SaaS B2B, données sensibles | Conformité réglementaire, hébergement, sous-traitants, sécurité |
| E-commerce, marketplace | Politique de retour, authenticité produit, délais réels, avis vérifiés |
| Formation, coaching | Méthode, résultats mesurés, certification, retours d'anciens élèves |
| Service local (coach, artisan) | Zone d'intervention réelle, tarifs, avis vérifiables, disponibilité |
| Contenu / média / directory | Méthodologie de sélection, sources, indépendance, fraîcheur des données |

La base publique répond à ces questions avec des pages dédiées, sourcées, datées — pas avec une page « Confiance » ou « Sécurité » unique qui affirme sans prouver.

## Architecture en 3 niveaux

1. **Niveau 1 — 10 pages stratégiques.** Les grandes requêtes au croisement produit × sujet de confiance (« meilleur [catégorie produit] + [critère de confiance] »). Ce sont les pages qui captent la recherche.
2. **Niveau 2 — 50 à 100 questions FAQ ultra-précises.** Chaque sous-sujet du niveau 1 décliné en question tapable et isolément citable (une question = une page ou une entrée FAQ, jamais un paragraphe noyé). Le niveau 2 nourrit le niveau 1.
3. **Niveau 3 — preuves et sources.** Contrats types, certifications, architecture technique, politiques publiées, comparatifs factuels, mentions externes indépendantes. Le niveau 3 crédibilise les niveaux 1 et 2 — sans lui, les niveaux 1 et 2 ne sont que des affirmations.

## Trois fonctions de page à ne jamais fusionner

| Fonction | Rôle | Exemple |
|---|---|---|
| **Page SEO** | Attire la recherche | « Quel est le meilleur [produit] pour [critère] ? » |
| **Page de preuve** | Apporte la preuve vérifiable | « Où sont hébergées les données ? », contrat, certification |
| **Page produit** | Explique la solution | « Sécurité chez [marque] » |

Chaîne type : recherche → page SEO/comparative → page produit → page de preuve → certification/contrat. Chaque maillon manque = la chaîne de confiance se rompt avant la conversion.

## Maillage hub-satellite + graphe d'entités

Le maillage interne suit le modèle hub/satellite déjà posé dans [[concepts/maillage-systeme]] : chaque page de preuve pointe vers la page pilier de son sujet, et réciproquement.

En plus du maillage, la marque doit constituer un **graphe d'entités explicite** que les moteurs IA peuvent lire en relations, pas seulement en mots-clés : `Marque → est → [catégorie] ; Marque → cible → [audience] ; Marque → traite → [objet] ; Marque → conformité → [référentiel] ; Marque → hébergement → [zone] ; Marque → certification → [norme] ; Marque → intègre → [écosystème]`. Plus ces relations sont cohérentes d'une page à l'autre du site, plus elles sont faciles à extraire pour un système qui raisonne en entités plutôt qu'en chaînes de caractères — voir [[concepts/entites-vectorielles]].

## La règle non négociable : la corroboration externe

**Une affirmation de la marque sur elle-même ne suffit jamais.** L'objectif n'est pas seulement de publier la base publique sur le domaine de la marque — c'est de la faire confirmer, reformuler et recouper par des sources tierces indépendantes : médias spécialisés, comparateurs, experts du secteur, partenaires d'intégration, clients qui témoignent, podcasts, avis. Une association mentale (« [marque] = [critère de confiance] ») n'a de valeur pour la recherche IA que si plusieurs sources indépendantes la répètent — jamais si elle n'existe que sur le site propriétaire.

Ce point distingue la base publique d'un simple netlinking ou d'une campagne de RP : il ne s'agit pas d'obtenir des liens, mais de faire exister le **même fait vérifiable** à plusieurs endroits indépendants du web.

## Comparatifs factuels : le point de jonction le plus puissant

Un comparatif (« [marque] vs [concurrent] : [critère] ») relie en une seule page la marque, le concurrent, le produit et le critère de confiance — c'est la page qui active le plus de relations du graphe d'entités en une fois. Condition stricte : rester factuel et vérifiable sur les deux marques, ton mesuré, jamais accusateur — doctrine déjà en place côté commercial chez Tim (comparatifs neutres, jamais dénigrer un concurrent nommément), appliquée ici en plus strict encore parce que la page sert justement à établir la confiance. Voir skill `comparatif-neutre` pour la rédaction.

## Cadence de fraîcheur

Sur les sujets qui évoluent (réglementation, IA, hébergement, certifications, prix), chaque page de niveau 1 ou 3 affiche une date de dernière mise à jour et, si possible, un responsable et une prochaine revue. La fraîcheur est elle-même un signal de confiance sur ces sujets, pas un détail cosmétique — recoupe [[concepts/weight-decay]] côté mécanique de mémorisation des moteurs IA.

## Différenciation avec les skills existants

La base publique n'est pas un skill de plus qui fait la même chose qu'un autre — c'est l'architecture qui orchestre plusieurs briques déjà outillées séparément :

| Skill existant | Ce qu'il couvre | Ce qu'il ne couvre pas |
|---|---|---|
| `seo-cluster-aeo` | Cluster Know-Simple/Know/Do autour d'**un** mot-clé pilier | La couche preuve/corroboration externe, le graphe d'entités marque |
| `seo-modeles-pseo` | Money Page + Spokes décisionnels (conversion) | Les pages de confiance non transactionnelles (conformité, sécurité, méthode) |
| `seo-entites-vectorielles` | Entités sémantiques pour **une page donnée** | Le graphe d'entités au niveau de la marque entière |
| `seo-faq-query` | FAQ stratégique d'**une page** (5-7 questions) | Le corpus FAQ complet du niveau 2 (50-100 questions, plusieurs pages) |
| `maillage-systeme` | Architecture hub/satellite du maillage interne | Le maillage externe (corroboration tierce) |
| `comparatif-neutre` | Rédaction d'un comparatif factuel | Le placement du comparatif dans l'architecture 3 niveaux |

`seo-base-publique` doit orchestrer ces briques (les invoquer si besoin) plutôt que les dupliquer : cadrer les 3 niveaux, identifier les questions de confiance du secteur, désigner ce qui relève de la corroboration externe (hors périmètre de production directe — c'est une stratégie de RP/mentions, pas une page à écrire), et livrer l'architecture complète prête à exécuter avec les skills spécialisés.

## Limites

- Concept posé sur une seule réflexion source (2026-08-29), pas encore confronté à un cas exécuté et mesuré. `confidence: high` sur la cohérence de la mécanique (elle recoupe des doctrines déjà validées : [[concepts/maillage-systeme]], [[concepts/e-e-a-t]], [[concepts/entites-vectorielles]]), pas sur un résultat chiffré.
- La corroboration externe n'est pas actionnable par la seule production de contenu on-site — elle dépend de relations presse/partenaires que le skill peut cadrer mais pas exécuter seul.

## Pages liées

[[concepts/maillage-systeme]] · [[concepts/e-e-a-t]] · [[concepts/entites-vectorielles]] · [[concepts/grounding-score]] · [[concepts/weight-decay]]
