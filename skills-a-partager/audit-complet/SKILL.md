---
name: audit-complet
description: |
  Audit SEO complet d'un site, exécuté selon le workflow canonique du vault : `~/Code/seo-kb/raw/bootcamp4/workflow-audit-bootcamp4.md` (8 phases, dérivé de la méthodologie « Workflow V3 » de Timothée, avril 2026). Ce skill est un routeur : il ne contient pas la méthode, il OBLIGE à ouvrir le fichier du vault et à suivre ses 8 phases dans l'ordre, chacune branchée sur le skill dédié (indexation-check, seo-core-web-vitals, seo-quick-win, seo-cannibalisation, maillage-systeme, maillage-interne-gsc). 100 % données Google (GSC + crawl + Lighthouse), aucun outil payant tiers, aucun chiffre estimé. Sortie : rapport avec synthèse en tête, plan d'action ordonné, une preuve par constat.

  TOUJOURS utiliser ce skill quand Tim dit : "audit de mon site", "audit du site [X]", "audit complet", "audite [site ou URL]", "fais l'audit de [site]", "lance l'audit", "lance le workflow audit", "workflow audit complet", "audit SEO de [site]", ou quand il donne une URL de site en demandant un état des lieux global.

  NE PAS utiliser ce skill (prendre le skill dédié à la place) quand la demande porte sur UNE seule dimension : audit indexation seul → indexation-check ; audit GEO / visibilité IA → seo-geo-audit ; pré-audit avant call commercial → seo-pre-audit ou audit-pre-call ; maillage seul → maillage-systeme / maillage-interne-gsc.
---

# Skill — Audit complet (routeur vers le workflow du vault)

## Règle unique, non négociable

La méthode vit dans le vault, pas ici : **ouvrir `~/Code/seo-kb/raw/bootcamp4/workflow-audit-bootcamp4.md` et suivre ses 8 phases dans l'ordre**. Ce skill ne duplique pas le contenu du fichier pour ne jamais diverger de lui (le vault décide, jamais l'IA). Si le fichier a bougé, le chercher dans seo-kb (`find ~/Code/seo-kb -iname "*workflow*audit*"`). Ne JAMAIS improviser le cadre, les critères ou la priorisation d'un audit.

## Carte des 8 phases (détail dans le fichier vault)

| Phase | Skill à invoquer | Source de données |
|-------|------------------|-------------------|
| 0 · Positionnement | aucun (prompt du fichier) | GSC + recherche web (qui est visible) |
| 1 · Indexation | `indexation-check` | sitemap + URLs |
| 1bis · Core Web Vitals | `seo-core-web-vitals` | Lighthouse local (échantillon 50) |
| 2 · Quick Wins | `seo-quick-win` | GSC + Chrome |
| 3 · Audit structurel Hn | aucun (prompt + scrap) | sitemap complet + crawl + GSC |
| 4 · Cannibalisations | `seo-cannibalisation` | GSC + Chrome |
| 5 · Maillage, deux passes | `maillage-systeme` PUIS `maillage-interne-gsc` | crawl liens + GSC |
| 6 · Synthèse + plan | synthèse | résultats des phases 0 à 5 |

Une phase nourrit la suivante : ne pas paralléliser ce qui dépend d'une phase amont.

## Données

- GSC en priorité par le MCP du site s'il existe (ex. `gsc-organikk`), sinon API ou export.
- Phase 1bis : Lighthouse en local au terminal. Sans terminal, sauter la phase et le documenter dans le rapport.
- Aucun chiffre estimé ou inventé. Distinguer strictement « non indexée » et « non testable ».

## Orchestration

Le multi-agents (outil Workflow) est autorisé pour la collecte à l'échelle, à une condition : les phases, critères et consignes de chaque agent viennent du fichier vault, pas de la tête de Claude. Contre-vérifier les constats critiques et hauts avant publication (un vérificateur qui reproduit chaque preuve).

## Sortie

Rapport dans l'ordre : synthèse et chiffres clés en tête, plan d'action ordonné (les dépendances d'abord), constats par phase avec une preuve chacun, méthode et limites en fin. Priorisation selon la doctrine du vault : élagage en 301 jamais en 410, meta tags en levier mineur, jamais d'achat de backlink. Écriture : ton factuel, mots bannis de Tim respectés, pas de tiret cadratin. Publier le rapport en artifact et redonner le lien.
