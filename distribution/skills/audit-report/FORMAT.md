# Audit report format

The report is not a dump of the modules. It answers four questions: what is really happening on the site, what blocks progress the most, what to do first, and why. Little visible information, a lot of reasoning behind it.

## Before writing: six passes on structured objects

1. Normalisation: every URL gets a page type (homepage, money_page, service_page, pricing, case_study, category, guide, blog, tool, legal, contact, about, utility), a business weight from 0 to 1 (homepage, service, pricing 1; case study 0.8; guide 0.5; blog 0.3; legal 0.05), an age (under 30 days, 30 to 90, over 90) and a trend, last 28 days against the previous 28 and 90 against 90 (growing, stable, declining, new, insufficient data).
2. Atomic observations: one fact, one source, one URL, one confidence. Typed FACT, HYPOTHESIS or ACTION; never a hypothesis written as a fact. Search Console data strength: under 20 impressions insufficient, 20 to 100 weak, 100 to 500 usable, 500 and more solid.
3. Clustering and deduplication: four orphan pages make one problem, with the URLs as evidence. Many URLs disappearing or redirecting = probable migration, one global problem. Problem (degrades performance) and opportunity (could improve) are two distinct objects.
4. Root cause: symptom, possible cause, evidence, action. A recent page without impressions is not a failure. Correlation is not causation. False problems: low traffic is not a problem by itself, an orphan page is not critical by itself, short content alone is never a problem.
5. Prioritisation: internal score, never shown, impact × confidence × business weight × data strength ÷ effort, translated into P1, P2, P3. Three P1 maximum. Each action: why, evidence, expected signal (never a promised figure), effort low / medium / high (never in hours), confidence, risk low / medium / high. Every irreversible action (deletion, 301, merge, URL change) carries "Validation required" and its checklist.
6. Verification: URL indexed in the API but reported as not indexed = error; redirect analysed as a 200 page = error; few impressions and a strong conclusion = warning; 301 without a destination analysis = warning; merge without query overlap = warning.

Forbidden: a 301 because a URL is a 404; a merge because two pages look alike; a deletion because of low traffic; a rewrite because CTR = 0; a new page because a keyword has no page; folder-to-folder redirects. 404 rule, URL by URL: restore, redirect to a page that really is equivalent, keep the 404 or use a 410, or check by hand. Cannibalisation in three states: confirmed (same Search Console query on several URLs plus matching intent), potential overlap, close but distinguishable pages.

## The report: two tabs

### Summary, exactly 5 sections, readable in 60 seconds

1. **Diagnosis** (70 words max): one conclusion in bold, two lines of evidence, one priority in bold. Never more categorical than the data coverage ("the available data mostly points to…", "no major issue detected on the inspected URLs", never "healthy" on a partially covered area).
2. **Key figures** (4 max): number, label, optional trend. Precise wording: "404 URLs that still had impressions", not "served by Google".
3. **Priorities** (3 cards, 40 words each): title, one sentence in bold, the URLs as evidence, "To do" in one line, badges Impact · Effort · Confidence, "Validation required" if irreversible, "See details". No technical identifiers, no jargon.
4. **Next 30 days**: a table Priority / Action / Effort, 5 to 6 rows, nothing else, no repetition of the priorities.
5. **Opportunities** (3 max, 35 words each): figures, one sentence, "Next step". Unknown intent = "potential to confirm"; unknown queries = "to check", no action proposed.

Then one line "Reliability of the analysis" with one sentence of limits, and "See the technical analysis".

### Technical analysis

State by area (critical / to improve / no major issue detected, with the real coverage). Then each priority in detail, in this structure: one framing sentence; "What we observe" (measured facts as a list, pages in code); "Why it comes first" (two sentences); "Action" (short numbered list); "Expected impact" and "Risk" in bold. The 30-day plan in three tiers (Immediate, Second step, Secondary), one action per paragraph in bold followed by one sentence. "Watch before acting" for the page whose cause is not isolated. "Other pages to watch": figures separated by "·", one sentence, verdict in bold ("No action recommended", "Check before any change"). Full limits. Then Indexing, Architecture, Content (headings: one sentence plus strategic pages only), Performance ("Lighthouse mobile performance", never "Core Web Vitals" without field data; INP "not measured"; one sentence plus a table Page / LCP / Importance), Internal linking, Cannibalisation, and each module's report as an exportable appendix.

Tables: 5 columns maximum. Short sentences. No diagnosis without a data point. Google is never anthropomorphised ("Search Console data shows"). Forbidden phrases: "it is important to", "it is worth noting", "this may potentially", "in the context of".

## Quality gate: the report does not ship if

No main diagnosis; more than 3 P1; a 301 without destination; a merge without justification; a figure without a source; a contradiction; the same problem repeated; an action without evidence; a score out of 10; an estimate in hours; a promised figure; a technical identifier in the summary; "healthy" on a partially covered area; an action on a page whose queries are unknown; a word count presented alone as a problem.

Critical pass before showing: "You are an SEO reviewer. Look only for reasoning errors: abusive causality, over-interpretation, risky recommendation, contradiction, insufficient data, repetition, inconsistent priority." Fix, then deliver.
