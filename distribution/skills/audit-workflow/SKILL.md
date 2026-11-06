---
name: audit-workflow
description: "Audit & alerting workflow: every technical check, then the report and alerting. \"run the audit workflow on [site]\"."
---

# Audit & alerting workflow

## Quand utiliser ce skill

Audit & alerting workflow: put a site through every check (technical,
indexing, cannibalization, internal linking, speed), deliver the pre-pre-decision report and set up
the recurring alerting. Trigger when the user says "run the audit workflow on [site]",
"full technical audit", "run the whole agent", "audit and alerting",
"set up alerting", "audit my site end to end", or uploads a sitemap or a
list of URLs to put through the checks.

See the problems before they hit the rankings. **Load the site context first** if there is one
(Search Console is the source of truth, never an invented figure, the user's own wording).
Announce each step in plain words.

## The modules this calls

`pre-audit` · `indexing-check` · `cannibalization-audit` · `internal-linking-gsc` +
`internal-linking` · `core-web-vitals` · `audit-report`

## The steps

1. **Scoping** — perimeter, the pages that matter, business goals (`pre-audit`).
2. **Technical & indexing** — what blocks crawling and indexing; list the pages that are not
   indexed, keeping "not indexed" and "not testable" apart (`indexing-check`).
3. **Cannibalization & internal linking** — pages competing with each other
   (`cannibalization-audit`), holes in the link graph: orphan pages, dead ends, links to add
   (`internal-linking-gsc`, `internal-linking`).
4. **Speed** — Core Web Vitals and what weighs on the experience (`core-web-vitals`).
5. **Pre-pre-decision report** — `audit-report`: six reasoning passes on the outputs of steps 1 to 4
   (normalisation, observations, clustering, root cause, prioritisation, verification), then the
   two-tab report. Summary: diagnosis (70 words), 4 figures, 3 priorities, next 30 days,
   3 opportunities, reliability. Technical analysis: state by area, each priority (what we
   observe, why, action, expected impact, risk), plan in three tiers, pages to watch, limits,
   then the module reports as appendices. Never a score out of 10, never an automatic 301 or
   merge, "Validation required" on every irreversible action. Without this report, the audit is
   not finished.
6. **Alerting** — recurring checks (indexing, 404s, post-migration, internal linking). Offer to
   schedule it as a recurring routine.

## A step without its input

A module whose input is missing (no Search Console export, Lighthouse not installed) is reported
as **not run**, with what is missing and how to get it. It is never filled in by estimate.

## What comes out

`audit-report.md` in two tabs (a Summary readable in 60 seconds, a Technical analysis), each module's report as an appendix, and recurring alerting.
