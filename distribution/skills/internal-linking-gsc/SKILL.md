---
name: internal-linking-gsc
description: "Internal linking plan from Search Console data, parent/child pages. \"internal linking\", \"orphan pages\"."
---

# Internal linking from Search Console

## Quand utiliser ce skill

Internal linking read from Search Console data. Parent / child / grandchild hierarchy, following the Boussardon method. Five steps: pull the Search Console exports → diagnose the structure (candidate parent pages, under-linked pages, orphan pages) → build the linking plan with the Know→Do rules → rank by urgency score → write the recommendations (source page, target page, anchor, insertion context).

ALWAYS use this skill when the user says: "internal linking", "internal links", "link silo", "orphan pages", "which pages should link to which", "internal linking plan", "Search Console plus my site structure", or uploads a Search Console file.

## When this fires

Reading and improving internal linking from Search Console data. Parent / child / grandchild
hierarchy.

## The principle

> "Internal linking is where the power is. And it starts from your keywords."

- A parent page carries at least 5 citations from child or grandchild pages
- Internal linking starts from the keyword strategy; the silo is the consequence, not the plan
- Order of priority: transactional > decisional > informational
- Link by intent (Know → Do) on top of linking by meaning

## Input required

| Source | Required |
|--------|----------|
| Search Console Pages export — URL, Clicks, Impressions, CTR, Position | Yes |
| Search Console Queries export, per page | Recommended |
| A 3 to 6 month window | Recommended |

## The five steps

1. **Pull the Search Console data** — Pages export plus Queries per URL
2. **Diagnose the structure**:
   - Candidate parent pages (high impressions, position 4-15, transactional query)
   - Under-linked pages (good position, weak CTR)
   - Orphan pages (no secondary topic showing in Search Console)
3. **Build the linking plan** — parent / child / grandchild hierarchy plus the Know→Do rules
4. **Rank** — urgency score = (Impressions × 0.4) + (Position upside × 0.4) + (Business value × 0.2)
5. **Write the recommendations** — source page, target page, anchor, context, priority

## The hierarchy

```
Parent page (the main business keyword)
├── Child page 1 (secondary transactional query)
│   ├── Grandchild page A (long tail / micro-intent)
│   └── Grandchild page B
└── Child page 2
```

Know → Do rule: every Know page links to at least one Do page on a related topic.

## Pre-decision output (required)

This module's table is not the end. Its output also carries a decision: a one-sentence diagnosis (the structural cause), 3 to 5 figures, a state (critical / to improve / no major issue detected, with the real data coverage), problems (3 max) and opportunities kept apart, actions P1 to P3 (3 P1 max) with why, evidence, expected signal, effort low / medium / high, confidence, risk, "Validation required" for any deletion, 301 or merge. What the data cannot support. Full format: `../audit-report/FORMAT.md`; the `audit-report` module assembles every module's decision into the final report.

Rules: every statement is a FACT, a HYPOTHESIS or an ACTION; a problem exists once; an anomaly is not a priority by default; business pages and Search Console trends before secondary technical anomalies; never a merge, 301, deletion, rewrite or new page recommended automatically; never a score out of 10, an estimate in hours or a promised figure; short content alone is never a problem; the certainty shown never exceeds the data coverage; no action on a page whose queries are unknown.

## Output required

For each action:
- Source page (Know / Do / Know+Do intent)
- Target page, and its intent
- What kind of link it is (by meaning, or Know→Do by intent)
- The anchor to use, never "click here"
- Where to insert it
- Priority (High / Medium / Low)

## Hard rules

- Do not automate this end to end — linking starts from the strategy, not from a tool
- Do not link without weighing the intent; by meaning and by intent are not the same thing
- Do not repeat the same anchor across every child page
- 10 citations is the floor for a parent page to count as active

## Saving the output

Write the output to `wiki/internal-linking/YYYY-MM-DD-slug.md` in your notes folder.

## Related concepts

`semantic-silo` · `internal-pagerank` · `search-intent` · `cannibalization` · `gsc-export`
