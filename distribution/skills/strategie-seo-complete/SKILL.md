---
name: strategie-seo-complete
description: "Stratégie SEO complète d'un client : audit-complet-v2, workflow mots-clés en 14 étapes, puis roadmap 30/60/90."
---

# Skill : Stratégie SEO complète (routeur des trois pièces existantes)

## Quand utiliser ce skill

Stratégie SEO complète d'un client, du diagnostic au calendrier de production. Ce skill est un routeur de routeurs : il n'invente aucune méthode, il enchaîne dans l'ordre trois pièces déjà validées et déjà documentées ailleurs : `audit-complet-v2` (où en est le site), le workflow mots-clés en 14 étapes du vault `.seokb/base/wiki/methodes/workflow-mots-cles-complet.md` (quoi produire, une pré-décision URL par cluster) et `seo-roadmap-pseo` (comment le séquencer pour le client, calendrier 30/60/90 présentable en rendez-vous). Chaque bloc garde sa propre sortie native ; ce skill ne les duplique pas, il les enchaîne et les fait se nourrir l'une l'autre (les exports GSC de l'audit alimentent l'étape 2 du workflow mots-clés, les clusters VALIDÉ du rapport de pré-décision mots-clés alimentent la Phase 1 de la roadmap). Aucun nouveau document de doctrine : la seule sortie propre à ce skill est une synthèse d'une page qui relie les trois sorties existantes.

## Règle unique, non négociable

Ce skill ne contient aucune méthode propre. Les trois méthodes vivent chacune à leur place, et ce skill se contente de les enchaîner dans l'ordre et de faire passer ce qui doit passer de l'une à l'autre :

1. **Diagnostic**, skill `audit-complet-v2`, qui route lui-même vers `audit-complet-v2/workflow-audit.md` (9 phases).
2. **Quoi produire**, ouvrir `.seokb/base/wiki/methodes/workflow-mots-cles-complet.md` et suivre ses 14 étapes dans l'ordre (chaque étape appelle le skill indiqué dans son tableau, de `kw-research-workflow` jusqu'au rapport de pré-décision mots-clés).
3. **Séquencement client**, skill `seo-roadmap-pseo`.

Ne jamais improviser un raccourci entre ces trois pièces, ne jamais sauter le rapport de pré-décision d'une étape pour gagner du temps sur la suivante : chaque bloc est un gate pour le suivant (voir plus bas).

## Carte des trois blocs

| Bloc | Skill / fichier | Entrée nécessaire | Sortie obligatoire |
|---|---|---|---|
| 1 · Diagnostic | `audit-complet-v2` | URL du site, accès GSC si possible | Rapport de pré-décision (Phase 7) + dashboard HTML 8 onglets |
| 2 · Quoi produire | `workflow-mots-cles-complet.md` (14 étapes du vault) | Diagnostic du Bloc 1, thématique ou Money Page du client | Rapport de pré-décision mots-clés : une pré-décision URL par cluster (utiliser, renforcer l'existant, créer, bloqué…) avec score business /5 |
| 3 · Séquencement client | `seo-roadmap-pseo` | Clusters VALIDÉ du Bloc 2 | Calendrier 30/60/90 en 2 phases (transactionnel/décisionnel d'abord, informationnel bas de funnel ensuite), présentable en RDV commercial |

## Comment les blocs se nourrissent

- **Bloc 1 → Bloc 2** : ne pas relancer une extraction GSC neuve pour l'étape 2 du workflow mots-clés (« Search Console : quick wins, cannibalisation, content gaps ») si le Bloc 1 l'a déjà produite dans ses Phases 1-2 (indexation, quick wins) et sa Phase 4 (cannibalisations). Réutiliser ces exports.
- **Bloc 1 → Bloc 2**, sur la structure : le Bloc 5 de l'audit (`maillage-systeme` puis `maillage-interne-gsc`) donne l'architecture existante et les pages orphelines. Les réutiliser à l'étape 9 du workflow mots-clés (`seo-cluster-aeo`, cocon autour du pilier retenu) au lieu de repartir à vide.
- **Bloc 2 → Bloc 3** : la pré-décision URL de chaque cluster (format `.seokb/base/wiki/methodes/rapport-mots-cles-format.md`) prend une de huit valeurs, deux familles. Programmable : *utiliser*, *créer*, *conserver et enrichir* (calendrier `seo-roadmap-pseo`, ce sont des pages qui n'existent pas encore ou qui changent de statut). Suivi à part, pas dans le calendrier de production : *renforcer l'existant* (optimisation d'une page déjà en ligne, hors pipeline Money Page de `seo-roadmap-pseo`, listée dans la synthèse comme chantier parallèle). Non programmable : *analyser avant restauration*, *candidat avec validation SERP requise*, *bloqué*, *attendre*. Ces clusters restent « en attente » dans la synthèse, jamais sur une date.
- **Bloc 2 → Bloc 3**, sur la priorisation : le score business /5 de chaque cluster programmable oriente directement la Phase 1 (transactionnel/décisionnel) vs Phase 2 (informationnel bas de funnel qui maille vers la Phase 1) de `seo-roadmap-pseo`. Ne pas re-scorer les clusters une deuxième fois dans la roadmap.

## Gates (ne pas avancer sans)

- Ne pas démarrer le Bloc 2 sans le rapport de pré-décision du Bloc 1 (même partiel, avec ses zones « données insuffisantes » explicites).
- Ne pas démarrer le calendrier `seo-roadmap-pseo` du Bloc 3 sans au moins un cluster *utiliser*, *créer* ou *conserver et enrichir* en sortie du Bloc 2. Zéro cluster programmable, mais des clusters *renforcer l'existant* : pas de calendrier `seo-roadmap-pseo`, la synthèse séquence à la place les actions de renforcement et les leviers techniques du Bloc 1. Zéro cluster programmable et zéro renforcement : le dire dans la synthèse plutôt que de séquencer un cluster bloqué, candidat ou en attente.
- Si un bloc s'arrête sur un « décision stratégique requise » (positionnement, arbitrage business), la synthèse le remonte tel quel : jamais transformé en action programmée dans la roadmap.

## Sortie obligatoire

Les trois sorties natives, inchangées : dashboard HTML de l'audit, rapport de pré-décision mots-clés dans `wiki/keywords/`, calendrier 30/60/90 de `seo-roadmap-pseo`. Ce skill ajoute une seule pièce propre, une **synthèse d'assemblage** (pas une nouvelle doctrine, aucun contenu qui ne vienne pas des trois sorties) :

```markdown
## Stratégie SEO : [client], [date]

**Diagnostic.** [Une phrase, reprise telle quelle du diagnostic principal de l'audit.] → [lien dashboard]

**Ce qu'on produit.** [N clusters VALIDÉ, N BLOQUÉ, N HYPOTHÈSE.] → [lien rapport de pré-décision mots-clés]

| Cluster | Score business /5 | Phase roadmap | Pré-décision |
|---|---:|---|---|

**Calendrier.** [Phase 1 : dates. Phase 2 : dates.] → [lien roadmap]

**En attente, et pourquoi.** [Clusters non programmés, raison de non-décision.]
```

Sans les trois sorties natives et cette synthèse, le skill n'a pas terminé.
