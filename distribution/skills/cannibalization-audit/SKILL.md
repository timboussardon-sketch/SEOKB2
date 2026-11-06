---
name: cannibalization-audit
description: "Keyword cannibalization audit from Search Console: conflict type, then 301, merge or differentiate. \"cannibalization\"."
---

# Keyword cannibalization

## Quand utiliser ce skill

Keyword cannibalization audit from Search Console data. Finds the pages competing with each other on the same keywords or the same intent, classifies the conflict type (exact keyword, same intent, semantic proximity, SERP triad), reads the metrics, and calls the action: 301, merge, differentiate, cross-link, or nothing at all when it is a SERP triad.

ALWAYS use this skill when the user says: "cannibalization", "keyword cannibalization", "two pages on the same keyword", "I used to rank better", "my pages are competing with each other", "cannibalization audit", "which page should I keep".

## When this fires

Two pages compete on the same keywords or the same intent. Unexplained position drops, a CTR that
stalls while the volume holds.

## Input required

| Source | Required |
|--------|----------|
| Search Console Queries export — filtered by URL, 90 days | Yes |
| The list of URLs (crawl or sitemap) | Recommended |
| Strategic context (pillar or satellite) | Recommended |

## The five steps

1. **Find the conflicts** — queries that fire 2 or more URLs in Search Console
2. **Classify the type**:
   - **(A) Exact keyword** — two pages on the same precise query
   - **(B) Same intent** — two pages answering the same intent
   - **(C) Semantic proximity** — neighbouring subjects, no direct conflict
   - **(SERP triad)** — an opportunity, not a conflict
3. **Read the metrics** — position, impressions, clicks, CTR for each page
4. **Weigh the architecture** — pillar or satellite, business goal
5. **Call the action**:

| Situation | Action |
|-----------|--------|
| Type A, one page clearly weaker | 301 redirect |
| Type A, both pages strong | Merge, then 301 |
| Type B, distinct micro-intents | Differentiate, then cross-link |
| Type C | More internal links towards the pillar |
| SERP triad | Nothing — optimise each angle separately |

## Pre-decision output (required)

This module's table is not the end. Its output also carries a decision: a one-sentence diagnosis (the structural cause), 3 to 5 figures, a state (critical / to improve / no major issue detected, with the real data coverage), problems (3 max) and opportunities kept apart, actions P1 to P3 (3 P1 max) with why, evidence, expected signal, effort low / medium / high, confidence, risk, "Validation required" for any deletion, 301 or merge. What the data cannot support. Full format: `../audit-report/FORMAT.md`; the `audit-report` module assembles every module's decision into the final report.

Rules: every statement is a FACT, a HYPOTHESIS or an ACTION; a problem exists once; an anomaly is not a priority by default; business pages and Search Console trends before secondary technical anomalies; never a merge, 301, deletion, rewrite or new page recommended automatically; never a score out of 10, an estimate in hours or a promised figure; short content alone is never a problem; the certainty shown never exceeds the data coverage; no action on a page whose queries are unknown.

## Output required

```
CANNIBALIZATION FOUND
Query: '[query]' — Type: (A/B/C/Triad)
| URL | Position | Impressions | Clicks | CTR | Status |

→ Diagnosis: [what is happening]
→ Action: [the exact action, plus its 3 implementation steps]
```

## Hard rules

- Never recommend a 301 without reading the metrics of both pages
- Do not treat every cannibalization the same way
- Do not confuse duplicate content with cannibalization
- Do not merge pages that answer distinct micro-intents
- Report SERP triads as opportunities, not as problems

## Saving the output

Write the output to `wiki/cannibalization/YYYY-MM-DD-slug.md` in your notes folder.

## Related concepts

`serp-triad` · `rrf` · `internal-linking` · `search-intent` · `gsc-export`
