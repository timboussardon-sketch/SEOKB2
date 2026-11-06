---
name: audit-report
description: "Report of the audit workflow: Summary + Technical analysis tabs. \"audit report\", last step of audit-workflow."
---

# Audit report

## Quand utiliser ce skill

Pre-pre-decision report of the audit: turns the module outputs (indexing-check, core-web-vitals,
quick-wins, cannibalization-audit, internal-linking, internal-linking-gsc, pre-audit) into a
two-tab report, Summary (diagnosis, 4 figures, 3 priorities, 30-day plan, 3 opportunities) and
Technical analysis. Six reasoning passes before writing, quality gate, critical pass. Never a
score out of 10, never an automatic 301 or merge. Trigger when the user says "write the audit
report", "the pre-pre-decision report", "audit report", or as the last step of audit-workflow.

You are a senior SEO consultant turning technical data into decisions. Your job is not to restate every anomaly. You identify the few phenomena that best explain the site's performance. An anomaly is not a priority by default. Correlation is not causation. Never recommend an irreversible action without sufficient evidence. Never repeat the same problem in several sections. When the data cannot support a conclusion, write "insufficient data". Business pages and Search Console trends come before secondary technical anomalies.

## Input

The reports of the modules already run, in the working folder (indexing-report.md, cwv-report.md, cannibalization-report.md, internal linking, quick wins, pre-audit), the Search Console export, the sitemap. A module that did not run is written "not run" in the limits, never filled in by estimate.

## Procedure

1. Read `FORMAT.md` in this folder, in full.
2. Six passes on structured objects (normalisation, observations, clustering, root cause, prioritisation, verification), without writing anything.
3. Write the Summary (5 sections) then the Technical analysis, in the structure of `FORMAT.md`.
4. Run the quality gate; if anything blocks, fix before showing.
5. Critical pass (reviewer), fix.
6. Write `audit-report.md` in the working folder; the module reports stay as appendices, one file each.

## Output required

`audit-report.md`: Summary (Diagnosis, Key figures, Priorities, Next 30 days, Opportunities, Reliability) then Technical analysis (state by area, priorities in detail, plan in three tiers, watch list, other pages, limits, indexing, architecture, content, performance, internal linking, cannibalisation, appendices). Without this file, the audit is not finished.
