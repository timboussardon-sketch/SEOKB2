---
name: internal-linking
description: "Internal linking architecture without Search Console: pillars, hubs, anchors, orphan pages. \"internal linking architecture\"."
---

# Internal linking: architecture, anchors and audit

## Quand utiliser ce skill

Strategic internal linking for a site (blog, catalogue, docs): pillar
architecture, hub and satellite classification, anchor selection with inbound
diversification, detection of orphan and dead-end pages, full audit of the
internal link graph.

Works alongside `internal-linking-gsc`, which reads Search Console data. This
one reasons on the editorial structure and the content, without depending on
Search Console. Usable from the scoping phase of a new site, before any
behavioural data exists.

ALWAYS use this skill when the user mentions: internal linking architecture,
blog pillars, hub and satellite, internal anchors, anchor text, choosing an
anchor, internal linking audit, orphan pages, dead-end pages, link equity,
structuring the linking of a new site, linking a blog before launch, silo
plan, or uploads a list of articles or URLs and wants a full linking plan.

## What this does

Builds and audits the internal link graph of a site from the content that exists or is planned,
without depending on Search Console. Three deliverables come out: a **pillar architecture**, a
**diversified anchor plan** per link, and an **audit report** of the structural holes.

The goal is not to generate links by the yard. It is to build a graph where every link is justified
by three signals: topic, intent and authority.

---

## The thinking behind it (Boussardon method)

- Internal linking is **a system, not a pass**. Three axes at once: topic, intent, authority.
- An anchor is not a keyword. It is **a promise of continuity** between two pages, read by Google,
  by LLMs as a vector, and by a human as a reason to click.
- **5 possible anchors to the same page means 5 different anchors.** One exact match only. The rest
  are partial, semantic, or long contextual.
- **The out-loud test**: if the sentence lands without the link, the anchor is properly embedded. If
  it limps, the anchor was bolted on.
- **Know→Do linking comes before Know→Know linking.** A page that explains a concept always points
  at the page that lets you execute it: a tool, an audit, a demo.
- **No "see also" block at the bottom of an article.** The link context is diluted. Contextual
  in-body links only.
- **A parent page is not a category title.** It is the most strategic article of the pillar, the one
  that defines the vocabulary and receives the most internal links.
- **Cross-pillar pollination counts as much as intra-cluster linking.** One outbound link in N
  points at another pillar, to avoid over-siloing.

---

## Data required

| Source | What it is | Required |
|--------|------------|----------|
| The list of URLs or articles | Title, slug, category, excerpt, target keywords | Yes |
| The full content (markdown or HTML) | To find the contextual opportunities | Recommended |
| The pillar keywords (3 to 5) | The client's business vocabulary | Recommended |
| The "Do" pages, identified | URLs of tools, audits, forms, calculators | Recommended |

**Minimum workable input**: the list of articles with title, excerpt and keywords. Without the full
content, this produces the architecture but not the precise anchors.

---

## Step 0 — Ingestion, for a site already online

**Context rule: the full content of the site NEVER enters the main context in one block.** An LLM's
reasoning degrades as the window fills; loading 50 or more HTML pages before reasoning produces a
mediocre plan. The main context works on the index only.

If the site is online with a sitemap, run the ingestion script BEFORE reading any page:

```bash
python3 .claude/skills/internal-linking/scripts/crawl_graph.py https://site.com/sitemap.xml -o ./linking-data
```

The script uses the Python standard library only, no dependency, and costs no tokens. It produces:

- **`index.json`** — one light line per page: URL, title, H1, meta description, editorial inbound
  and outbound counts, and the lists of orphan and dead-end pages. This is the ONLY file loaded
  into the main context.
- **`graph.json`** — every internal link with its exact anchor, flagged `in_body` (outside nav,
  header, footer and aside) and `sitewide` (the same target and anchor pair present on 80% or more
  of the pages is a template link, excluded from the editorial count even when the HTML is not
  semantic).

How the work splits after that:

1. **Steps 1-4 and 6-7** reason on `index.json` plus the counts in `graph.json`. No content reading.
2. **Step 5, the precise anchors**: delegate to sub-agents. Each sub-agent reads 2 or 3 source pages
   at most, proposes the passages and anchors, and only the result comes back to the main context.
3. The anchors already pointing at a target, for diversification, are read from `graph.json`, never
   by crawling again.

If the site is not online (planned content, local markdown), skip this step: the list the user
supplies acts as the index, and the mapping in step 4 comes from parsing the local files (grep the
links, do not read them whole into context).

---

## The agent's reasoning, steps that are not optional

The agent MUST follow these steps **in order** before answering.

### Step 1 — Classify every page by intent

For each article, settle its dominant intent:

| Intent | What it is | Signals |
|--------|------------|---------|
| **Know-Simple** | A short definition, a direct answer | title starts with "What is", "What does" |
| **Know** | An in-depth guide, a method, a comparison | title starts with "How", "Why", "Guide" |
| **Do** | A tool, a calculator, a form, a demo | URL holds `/tools/`, `/audit`, `/contact` |

A page can carry a dominant intent and a secondary one. Note both.

### Step 2 — Identify the pillars

Group the articles by meaning, not by technical category. Aim for **3 to 5 pillars, no more**. And
no fewer than 3.

What makes a cluster a real pillar:
- At least 3 articles in it
- One central business keyword that comes back in every title or excerpt
- A natural hub page: the most complete or most strategic article of the cluster

A cluster with fewer than 3 articles becomes a **sub-cluster** of an existing pillar, not a pillar
of its own.

### Step 3 — Name the hub of each pillar

For each pillar, identify the hub page:
- The most complete article, or the one meant to be
- It covers the secondary concepts of the other articles in the pillar
- Ideally it targets the exact pillar keyword

The hub receives inbound links from every satellite. The hub redistributes to the satellites through
contextual links, not through a list.

### Step 4 — Map the existing links

If step 0 ran, this mapping is ALREADY in `index.json` (the counts) and `graph.json` (the anchor
detail). Read it, do not redo it. Otherwise, for each article, list:
- **Inbound links**: how many articles point at it?
- **Outbound links**: how many articles does it point at?

(Click depth is NOT a criterion here. It is not measured and not corrected.)

Find the anomalies:
- **Orphan pages**: 0 inbound links
- **Dead-end pages**: 0 outbound links
- **Under-linked hub**: fewer than 5 inbound links from its satellites

### Step 5 — Pick the anchors for each proposed link

For each `source → target` link to create, produce **3 anchor options**, ranked:

1. **Exact match** (1 per target at most, on the first mention): reproduces the target's exact
   pillar keyword
2. **Partial match** (60 to 70% of the inbound links to a target): a variation on the pillar keyword
3. **Extended semantic**: restates the target's promise without using the keyword

For each anchor, run the 5 checks:

| Check | The question |
|-------|--------------|
| The target's promise | Does the anchor reflect what the reader will find, rather than the H1? |
| The carrying sentence | Does the sentence still read well out loud without the link? |
| Diversification | Is this anchor already used towards the same target from another page? |
| Position | Does the anchor carry the action verb or the central noun, rather than a connecting word? |
| Link context | Do the 5 words before and after talk about the target's subject? |

An anchor that fails one check gets rejected.

### Step 6 — Rank the links to create

Urgency score per proposed link:
**score = (target impressions × intent_weight) + (authority_gain × 0.4)**

Where:
- `intent_weight`: Do = 1.0, decisional Know = 0.8, Know = 0.5, Know-Simple = 0.3
- `authority_gain`: 1 if the source is a hub, 0.5 if the source is a linked satellite, 0.2 otherwise

Then rank in this order:
1. **Missing hub → satellite links** inside a pillar, to switch the silo on
2. **Know → Do links**, to steer the funnel
3. **Cross-pillar links**, at least one per pillar towards another pillar
4. **Links to the orphan pages** found in step 4

### Step 7 — Check the conservation rules

Before finalising the plan, confirm:
- No orphan page left: every page receives at least 1 inbound link
- No dead-end page: every page holds at least 2 outbound links
- Every hub receives at least 5 inbound links from its satellites
- No target receives the same anchor twice
- Sane density: 2 to 5 internal links per 1,000 words, never more

**DO NOT answer before every step is done.**

---

## Pre-decision output (required)

This module's table is not the end. Its output also carries a decision: a one-sentence diagnosis (the structural cause), 3 to 5 figures, a state (critical / to improve / no major issue detected, with the real data coverage), problems (3 max) and opportunities kept apart, actions P1 to P3 (3 P1 max) with why, evidence, expected signal, effort low / medium / high, confidence, risk, "Validation required" for any deletion, 301 or merge. What the data cannot support. Full format: `../audit-report/FORMAT.md`; the `audit-report` module assembles every module's decision into the final report.

Rules: every statement is a FACT, a HYPOTHESIS or an ACTION; a problem exists once; an anomaly is not a priority by default; business pages and Search Console trends before secondary technical anomalies; never a merge, 301, deletion, rewrite or new page recommended automatically; never a score out of 10, an estimate in hours or a promised figure; short content alone is never a problem; the certainty shown never exceeds the data coverage; no action on a page whose queries are unknown.

## Output format, mandatory

### Block 1 — The architecture found

```
PILLAR 1 — [topic name] (pillar keyword: "...")
├── HUB: [article title + slug]
├── Satellite: [title + slug] (intent: Know)
├── Satellite: [title + slug] (intent: Know)
└── Satellite: [title + slug] (intent: Do)

PILLAR 2 — [name]
...
```

### Block 2 — Audit of the existing graph

| Article | Inbound | Outbound | Status |
|---------|---------|----------|--------|
| ... | 3 | 4 | OK |
| ... | 0 | 2 | **ORPHAN** |
| ... | 5 | 0 | **DEAD END** |

### Block 3 — The links to create, ranked

For each proposed link:

```
PRIORITY: HIGH | Score: 8.4
─────────────────────────────────
SOURCE  : [source article title] (Know)
TARGET  : [target article title] (Do)
PILLAR  : Cross-pillar (Pillar 1 → Pillar 3)
NATURE  : Know → Do (funnel steering)

PROPOSED PASSAGE:
"[the full sentence where the link goes, showing the words before and after]"

ANCHOR OPTIONS (pick 1):
  [exact]     "the exact pillar keyword"
  [partial]   "a natural variation of the keyword"
  [semantic]  "a restatement of the target's promise"

WHY: [one sentence on what this link is worth]
```

### Block 4 — Governance rules

A final checklist the client follows on every new publication:

- [ ] The new article receives at least 3 inbound links from 3 existing articles
- [ ] The new article holds at least 3 outbound links to existing articles
- [ ] At least 1 outbound link points at a Do page
- [ ] At least 1 outbound link points at another pillar (cross-pollination)
- [ ] No exact anchor is duplicated towards the same target
- [ ] Every link is in-body, none in a "see also" block

---

## What to watch

- **Do not automate all of it.** This proposes, the human decides. A forced anchor destroys the
  naturalness of a text.
- **Context is worth more than the anchor.** A perfect anchor inside a sentence about something
  else is a weak link. Rewrite the sentence.
- **The hub is not fixed.** If a new satellite becomes more complete than the historical hub, move
  the hub. The structure follows the content, not the reverse.
- **Cross-pillar is not off-topic.** The bridge between two pillars rests on a real conceptual
  connection, not on needing a link.
- **Never link to the homepage from the content.** The homepage already holds all the PageRank. Keep
  it for the business pages.
- **FAQs are an anchor mine.** Every FAQ answer that mentions a sub-topic already covered should
  link. High density, natural context.
- **Density has a ceiling.** Past 5 internal links per 1,000 words, dilution sets in. Google weights
  each anchor by 1/N, where N is the total number of links.

---

## Special case — a site with no Search Console data

If the site is new (under 3 months, or no Search Console access):
- Step 4, the inbound and outbound mapping, comes from step 0 if the site is online, otherwise from
  parsing the local content (markdown or HTML)
- Step 6, the scoring, uses a proxy: `business_position` (1 for Do, 0.7 for decisional Know, 0.5 for
  Know, 0.3 for Know-Simple) instead of Search Console impressions
- The plan still holds, and gets adjusted with Search Console as soon as the data arrives

---

## Special case — rebuilding an existing site

If the site exists and has 6 months or more of Search Console data:
- Chain this with **internal-linking-gsc**: this one sets the architecture, the other injects the
  behavioural data
- Find the pages already ranking on the pillar and promote them to hub where it makes sense
- Preserve the existing links that work. No blind rebuild

---

## Special case — pages generated in bulk from a data table

This skill reasons by reading and editorial judgement, steps 1 to 7. That reasoning assumes a number
of pages an agent can still compare with each other coherently. It stops holding beyond a few
hundred pages coming out of the same template.

**How to spot it**: if a batch of pages shares the same route and template and comes from a data
table (pSEO: one lexicon word, one product, one location, one entity per row), and that batch goes
past **300 to 500 instances**, DO NOT apply steps 1 to 7 to it. The pillar of those pages is already
given by the template itself. There is nothing to cluster.

**What replaces the agent's reasoning at that scale**: a real, verifiable data signal, computed once
for the whole batch, never an agent judging page by page. In order of preference:

1. **A relation already present in the data** (co-occurrence, a shared attribute, a cross reference,
   a foreign key). This is the most reliable signal, because it is verifiable rather than merely
   "semantically close". A worked case: on a site of 13,000 lexicon pages, one per word, the
   "related words" on each page come from counting co-occurrence across the corpus, not from an
   embedding and not from an agent.
2. **Embedding plus kNN**, only where no data relation exists to connect the instances.

In both cases the agent only works upstream, setting the rule: which signal, how many links, which
rendering format. Never page by page. The rendering is a templated block, a "related words" section
for instance, not an in-body link. The "no see also" rule above targets editorial content written by
hand; it does not apply to a template generated at scale, where no organic prose exists to slip a
contextual link into.

If the batch stays under the threshold, from a few dozen up to around 300 pages, steps 1 to 7 apply
normally. At that scale editorial judgement stays reliable, and it is cheaper to set up than a
dedicated data pipeline.

---

## The method, in short

> "Internal linking is a system, not a pass."
> "5 inbound links to the same page means 5 different anchors. One exact match only."
> "The out-loud test: if the sentence lands without the link, the anchor is good."
> "A Know page always points at a Do page."
> "No see also. In-body links only."
> "A hub is not a category. It is the most strategic article of the pillar."
> "The 5 words before and after the anchor are worth more than the anchor itself."
