---
type: methode
title: "Format du rapport mots-clés : une pré-décision URL par cluster"
slug: rapport-mots-cles-format
created: 2026-09-24
status: stable
confidence: high
tags: [mots-cles, methode, rapport]
---

# Format du rapport mots-clés

Corrections de l'expert de Tim, 24 septembre 2026, sur le rapport organikk. Complète `audit-complet-v2/rapport-audit-seo-format.md` (synthèse en 5 sections, analyse technique) pour le workflow mots-clés.

## Ce que le rapport doit rendre

Une étude de mots-clés arrive à : les marchés SEO à attaquer (5 maximum) ; l'URL à utiliser pour chacun ; les URL à ne surtout pas créer ; les pré-décisions qu'on ne peut pas encore prendre. Le moteur rend **une pré-décision URL par cluster, ou déclare explicitement pourquoi il ne peut pas encore décider**. Jamais « à trancher ».

Pour chaque marché : URL (existante ou nouvelle), Décision (utiliser / renforcer l'existant / créer / conserver et enrichir / analyser avant restauration / à confirmer après validation SERP), Pourquoi (deux ou trois faits), Manque (ce qu'il faut pour décider quand la décision est ouverte). Puis une roadmap URL (URL / Décision / Action), la liste « À ne pas produire maintenant », et les pré-décisions ouvertes, chacune typée : **Décision stratégique requise** (positionnement, branding : ce n'est pas une décision de mot-clé) ou **Pré-décision impossible avant analyse SERP de N requêtes**.

## Ce que le rapport ne fait plus

- **Compter des occurrences comme matière.** « 20 transcripts mentionnent ChatGPT » ne vaut rien. La matière se qualifie par type : objection client, cas concret, méthode, preuve, résultat, verbatim exploitable. Une cellule vide est une absence constatée.
- **Agréger les signaux de demande en verdict.** 96 variantes Suggest ne sont pas 96 demandes (formulations proches) ; 5 acteurs mesurent la présence concurrentielle. Les signaux s'affichent séparément (Suggest, impressions GSC, calls, acteurs, PAA, YouTube, Trends quand disponibles) ; seules les impressions GSC disent qu'une requête est tapée. Aucun « demande observée : forte » sorti d'un mélange opaque.
- **Écrire « cannibalisation forte » sans SERP ni conflit GSC.** Sans validation SERP et sans requête GSC partagée, c'est un **chevauchement potentiel à vérifier**.
- **Transformer les secondaires en placements.** « Intégrer les requêtes secondaires en title, H2, FAQ » est interdit par défaut. Une requête secondaire sert à repérer une sous-intention ou une information à couvrir ; elle n'a pas automatiquement besoin d'un H2 ou d'une FAQ.
- **Poser une décision de positionnement comme priorité mot-clé.** Consultant, agence ou hybride : « Décision stratégique requise », remontée à part.
- **Répéter le rapport dans le plan.** Le plan est une roadmap URL, pas la liste des priorités reformulée.
- **Prouver qu'on a beaucoup travaillé.** Pas de « 96 Suggest, 20 transcripts, 5 acteurs, 8 clusters, 11 requêtes » en synthèse : les chiffres restent dans l'analyse technique, en preuve d'une décision.

## Quality gate

Le rapport ne sort pas si : un cluster prioritaire n'a ni pré-décision URL ni raison de non-décision ; « à trancher » apparaît ; un verdict de demande agrégé apparaît ; « cannibalisation » est écrit sans SERP ni conflit GSC ; la matière est comptée en occurrences ; une action dit « placer en title / H2 / FAQ » ; une décision de positionnement est classée priorité mot-clé.

## Gouvernance des pré-décisions (correction du 24 septembre, seconde passe)

Une seule pré-décision finale par cluster, avec un statut : **VALIDÉ**, **À VÉRIFIER**, **BLOQUÉ**, **REJETÉ**. Objet de pré-décision, un par audit mots-clés :

```json
{"cluster":"SEO IA / GEO","url":"/consultant-geo/","matiere":"incomplète","serp":"à vérifier","statut":"BLOQUÉ","reason":"SERP overlap non vérifié + positionnement non tranché","allowed_actions":["analyse SERP","décision de positionnement"],"forbidden_actions":["créer une page","publier le brief"]}
```

Hiérarchie des sorties : RAW, HYPOTHÈSE, VALIDÉ, PRÉ-DÉCISION FINALE, OBSOLÈTE. Une fois la pré-décision finale prise, chaque sortie amont incompatible est marquée OBSOLÈTE (bannière en tête, `statut_decision` en frontmatter) ; aucun skill aval ne peut la contredire. Aucune page ne peut être créée sans validation SERP + matière suffisante ; aucun brief n'est généré tant que la pré-décision URL n'est pas VALIDÉ ; un cluster « candidat » reste « validation SERP requise » tant que le type de SERP, l'overlap, les pages qui rankent et la spécialisation attendue ne sont pas lus.

Le rapport visible se réduit au tableau Marché / Page / Matière / SERP / Décision, aux blocages avec leur raison, aux autorisés et interdits, et à « à ne pas produire ». Les scores /10 restent en backend ; le rapport lit adéquation offre, intention, preuve, SERP, décision. « Résistant / absorbé » devient « probabilité de conserver un clic après réponse IA : forte / moyenne / faible ». Le pSEO ne propose que les secteurs avec demande observée, SERP compatible, vraie matière, offre réelle et preuve propre au secteur : un cas ou un relevé réel par page, sinon la page n'existe pas. La section « skills du workflow et leurs sorties » sort du rapport : c'est un log, en annexe.

## Deux scores affichés (demande de Tim, 24 septembre)

- **Score business sur 5**, composantes visibles : intention (0 à 2 : informationnel 0, considération 1, décision 2), proximité avec l'offre (0 à 2), conversion directe vers le point de conversion (0 ou 1). C'est le seul score visible ; les scores /10 des skills restent en backend.
- **Score matière** : nombre de documents du vault qui traitent le sujet, trois occurrences ou plus du champ lexical du cluster (pas un mot isolé), par type de source : transcripts, dossiers clients, notes et articles, wiki. Le comptage dit où chercher ; le verdict de matière vient de la lecture par type (objection, cas, méthode, preuve, résultat, verbatim). Un score élevé ne décide rien : beaucoup de documents sans preuve = matière incomplète. Zéro document = pas de page, la demande part au client ou en collecte (règle « on ne part jamais de zéro »).

Script de calcul : signaux en entrée, deux colonnes en sortie, dans le tableau de décision et dans `annexes/scores-*.json`.
