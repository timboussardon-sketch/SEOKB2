---
type: source
source_type: article
title: "LeadFactory OS, cockpit open source d'une agence lead gen"
aliases: [leadfactory-os]
tags: [dashboard, agence, outils, meta-ads]
created: 2026-10-21
updated: 2026-10-21
sources: 1
confidence: medium
status: stable
---

# LeadFactory OS

Dépôt `https://github.com/gquthier/leadfactory-os`, MIT, lu le 2026-10-21 (v0.5.2). Cockpit local d'une agence de lead generation Meta Ads : app Next.js complète (`full-app/`, stockage JSON local, dashboard, pipeline, clients, campagnes, leads, CRM, finances, journal d'activité) et 23 skills Claude Code / Codex (adaptés de `tarsluna/my-custom-skills`).

## Ce qui a été retenu

Trois mécanismes, transposés dans [[methodes/tableau-de-bord-par-projet-seo]] : statuts canoniques fermés avec jalon de lancement et santé du pipeline (`full-app/src/types/index.ts`, `src/lib/pipeline-timeline.ts`), note de santé par client triée du pire au meilleur (`src/app/admin/results/`), rapport hebdo client généré depuis l'API (`src/lib/weekly-report-email.ts`).

## Limites

Le README est une page de vente ; ses chiffres (6 M€, 7 908 leads) ne sont pas vérifiables. Le dashboard lui-même est quatre compteurs. Tout le reste est Meta Ads, VSL, créas IA, cold call : hors périmètre SEO.
