---
name: quick-wins
description: "Fast SEO wins from Search Console: pages in position 3-12 with low CTR. \"quick wins\", \"low CTR pages\"."
---

# Quick wins

## Quand utiliser ce skill

Finds the fast SEO opportunities in Search Console data: pages sitting in position 3-12 with high impressions and an underperforming CTR. Optimising what exists comes before writing anything new. Six steps: filter (positions 3-15, drop branded queries and the homepage) → sort by impressions → compute the CTR gap → cross with search intent → rank → list the levers (title, meta description, H1, FAQ at the top of the page, atomic densification).

ALWAYS use this skill when the user says: "quick wins", "pages close to the top 3", "low CTR pages", "pages in position 3-12", "what can I fix fast", "low hanging fruit", or uploads a Search Console export.

## When this fires

Pages in position 3-12, high impressions, CTR below what the position should bring. Optimise what
exists before creating content.

## Input required

| Source | Required |
|--------|----------|
| Search Console Pages export — URL, Clicks, Impressions, CTR, Position (90 days) | Yes |
| Sector context | Recommended |

Minimum workable input: a 30-day export, positions 4-15, sorted by impressions descending.

## The six steps

1. **Filter** — positions 3.0 to 15.0, drop branded queries and the homepage
2. **Sort** — top 10 by impressions, descending
3. **Compute the CTR gap** — expected CTR (position 4 = 7%, 5 = 5%, 6-10 = 2-3%) against actual CTR
4. **Cross with intent** — decisional P1 > transactional P2 > informational P3
5. **Rank** — decisional + more than 500 impressions a month + CTR under 3% + gap over 1.5%
6. **List the levers** — title, meta description, H1, FAQ at the top of the page, atomic densification

## Pre-decision output (required)

This module's table is not the end. Its output also carries a decision: a one-sentence diagnosis (the structural cause), 3 to 5 figures, a state (critical / to improve / no major issue detected, with the real data coverage), problems (3 max) and opportunities kept apart, actions P1 to P3 (3 P1 max) with why, evidence, expected signal, effort low / medium / high, confidence, risk, "Validation required" for any deletion, 301 or merge. What the data cannot support. Full format: `../audit-report/FORMAT.md`; the `audit-report` module assembles every module's decision into the final report.

Rules: every statement is a FACT, a HYPOTHESIS or an ACTION; a problem exists once; an anomaly is not a priority by default; business pages and Search Console trends before secondary technical anomalies; never a merge, 301, deletion, rewrite or new page recommended automatically; never a score out of 10, an estimate in hours or a promised figure; short content alone is never a problem; the certainty shown never exceeds the data coverage; no action on a page whose queries are unknown.

## Output required

A table of 5 to 10 pages, plus an action sheet per page with at least 2 actions, one of which is an
atomic proof.

```
QUICK WINS — Top N opportunities from Search Console
| # | URL | Position | Impressions | Actual CTR | Expected CTR | Gap | Intent |

→ Page /url
Action 1: [type] — [what to change, concretely]
Action 2: Atomic densification — [before / after]
```

## Hard rules

- Do not propose new content before the existing quick wins are exhausted
- No generic advice without the URL it applies to
- Do not confuse search volume with Search Console impressions
- Always include at least one before/after example of atomic densification

## Saving the output

Write the output to `wiki/quick-wins/YYYY-MM-DD-slug.md` in your notes folder.

## Related concepts

`atomic-proof` · `grounding-score` · `search-intent` · `gsc-export`
