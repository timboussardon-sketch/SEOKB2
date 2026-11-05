---
type: methode
title: "AI Search Growth System — stratégie GEO et acquisition"
aliases: [strategie-geo, ai-search-growth-system]
tags: [seo, geo, ia, acquisition, strategie]
created: 2026-10-25
updated: 2026-11-05
sources: 1
confidence: high
status: stable
---

# AI Search Growth System

Framework fourni par Tim dans la conversation du 25 octobre 2026 pour créer le skill `strategie-geo`. Le statut stable porte sur la méthode demandée ; aucun résultat d’acquisition n’est encore établi par cette création.

## Déclencheur prioritaire

Toute demande « stratégie SEO », « strat SEO », « stratégie GEO », « strat IA » ou « stratégie complète pour X » lance `strategie-geo`. Depuis la version canonique de Tim du 29 octobre, le pilote suit dix étapes et treize parties ; il ne déclenche plus automatiquement une mission `strategie-mot-cle` par terme. Ce spécialiste garde les demandes isolées. Audit, relevé, brief et article isolés gardent leur skill dédié.

Le cycle est **Comprendre → Observer → Diagnostiquer → Optimiser → Distribuer → Convertir**. Il relie les offres et les questions des acheteurs aux réponses réellement observées dans les moteurs, aux actions sur les pages et sources externes, puis aux demandes commerciales et clients documentés.

## Skill et template

Point d’entrée Codex : `.agents/skills/strategie-geo/SKILL.md`, qui charge la version canonique `~/.claude/skills/strategie-geo/SKILL.md`. Template en treize parties : `.agents/skills/strategie-geo/references/template.md`. Le contrat [[methodes/opportunites-business]] est partagé avec Audit V2 ; son branchement est décrit dans [[methodes/opportunites-business-integration]].

Après cadrage et collecte, qualifier la demande explorée. Après les observations, valider les opportunités avant architecture, production et roadmap. Scénarios et moyens peuvent rester non estimables. Les conditions commerciales peuvent conduire à traiter l’offre, la conversion ou le suivi avant l’acquisition.

## Phases à valider

| Phase | Proposition |
|---|---|
| Comprendre | Cadrage et groupes par offre |
| Questions | Mots-clés, intentions et panel sourcé |
| Observer | Protocole et coût éventuel, puis bilan des relevés réels |
| Diagnostiquer | Opportunités, preuves et priorités |
| Planifier et produire | Roadmap commune, puis livrables de contenu et distribution |
| Mesurer et apprendre | Bilan documenté et proposition du cycle suivant |

Chaque proposition attend la validation explicite de Tim. Les corrections reprennent la même phase. L’accord sur un plan ne pré-valide ni sa rédaction ni sa publication. Les articles conservent leurs validations brief, Hn, données puis rédaction. [[moc/doctrine-seo-reference]]

## Articulation du système

Les missions isolées par mot-clé réutilisent [[methodes/strategie-mot-cle-par-etapes]]. Leur consolidation passe par [[methodes/roadmap-seo-portefeuille-mots-cles]]. La mesure distingue mentions, recommandations, citations, acquisition et business ; aucune citation ne prouve une vente. L’apprentissage utilise [[methodes/apprentissage-continu]].

La création livre des instructions et un template ; elle n’installe ni agents exécutants, ni collecteur IA, ni dashboard client, ni automatisation. À l’ouverture d’une mission, les livrables alimentent le dashboard du coffre selon [[methodes/tableau-de-bord-par-projet-seo]].
