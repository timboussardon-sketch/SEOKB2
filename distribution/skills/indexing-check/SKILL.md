---
name: indexing-check
description: "Indexing audit of a site, 9 checks per URL, no paid tool, read-only on the public web."
---

# Indexing audit

## Quand utiliser ce skill

Indexing audit of a site (B2B / editorial / pSEO) with no paid third-party tool. Runs 9 checks on every URL: HTTP status, technical blocks, noindex directives, sitemap (presence, lastmod, consistency), inbound internal links, content length, and observed Google indexing status. Output: a markdown report with a summary, the critical anomalies first, then the minor ones, then ranked recommendations. Keeps "not indexed" and "not testable" (Google rate limit) strictly apart. No forcing action, read-only on the public web.

## When this fires

- A point-in-time audit of a site (before a sales call, after a rebuild, after shipping a cluster)
- Recurring monthly monitoring on a retained client
- Diagnosing an unexplained traffic drop
- Pre-flight on a pSEO project, to check the technical base is sound before scaling

## Input required

| Source | Required |
|--------|----------|
| The list of URLs to monitor (a file in the repo: `urls.txt`, `src/data/wiki.ts`, `src/data/articles.ts`) OR the URL of the site's public sitemap.xml | Yes |
| The target domain (`client-site.com` for instance) | Yes |
| The link perimeter to crawl (hub pages: `/`, `/glossary`, `/wiki`, the footer, articles) | Recommended |
| A Search Console API service account (raises reliability) | Optional |

Minimum workable input: a list of URLs and the domain. The rest is inferred.

## The architecture, in three layers

```
1. Load the list of URLs (the human source of truth)
        ↓
2. LAYER A — Technical audit (the possible causes)
        ↓
3. LAYER B — Observed indexing status
        ↓
4. LAYER C — Markdown reporting
```

Splitting causes from status is deliberate. A check that only looks at status will report "OK 200"
on a page carrying an accidental `noindex`. These two are kept strictly apart.

## The 9 checks

### LAYER A — Technical audit, the causes

**1. HTTP check (404/500, redirects)**
For each URL:
```bash
curl -sIL -A "Mozilla/5.0" -o /dev/null -w "%{http_code}|%{url_effective}" {URL}
```
Note the final code AND the redirect chain. 200 is what you want. A systematic 301→200 is debt
worth reporting (trailing slash, http→https).

**2. robots.txt does not block**
```bash
curl -s https://{domain}/robots.txt
```
For each path, check that no `Disallow:` directive blocks it, for `User-agent: *` or for
`User-agent: Googlebot`.

**3. No noindex tag, in the HTML and in the HTTP header**
```bash
curl -sL -A "Mozilla/5.0" {URL} | grep -i 'name="robots"'
curl -sIL {URL} | grep -i 'x-robots-tag'
```
Report any `noindex` or `none`.

**4. Sitemap: presence and freshness**
```bash
curl -s https://{domain}/sitemap.xml
```
For each expected slug, check a `<loc>` exists and read its `<lastmod>`. Flag any `lastmod` older
than 6 months.

**5. Sitemap against the source of truth**
Diff the slugs in the source of truth (the human file) against the `<loc>` entries in the sitemap:
- In the source, missing from the sitemap → to add to the build
- In the sitemap, missing from the source → a sitemap orphan

**6. Inbound internal links**
Crawl the hub pages (`/`, `/glossary`, `/wiki`, the footer, a sample of articles) and count the
inbound internal links per target URL.
- 0 inbound links: orphan page, critical
- exactly 1 inbound link: under-linked, worth reporting

**7. Content length, as a proxy for thin content**
For each URL, pull the text out of `<main>` or `<article>` (failing that, `<body>` minus `<nav>`
and `<footer>`) and count the words.
- under 300 words: thin, dig into it
- 300-800: short, acceptable for an atomic entry
- over 800: fine

### LAYER B — Indexing status, the output

**8. Observed Google indexing, by scraping `site:`**
```bash
curl -sL -A "Mozilla/5.0 (Macintosh...)" "https://www.google.com/search?q=site:{URL}&hl=en"
```
**Guardrails, all of them mandatory:**
- Space the requests 3 to 5 seconds apart (`sleep 4`)
- Detect the block: `grep -E 'sorry/index|recaptcha|unusual traffic'`
- When blocked, mark it "not testable, rate limited", **not** "not indexed"
- Retry once on an empty response before concluding anything
- Mark it "indexed" if the URL appears in the response HTML

Reliability sits around 40 to 60% because of the rate limit. For full reliability, see the Search
Console API variant.

### LAYER C — Reporting

**9. Markdown report**
The structure is fixed:
- Summary at the top (X out of N per dimension, `✅` for clear, `⚠️` for an anomaly)
- CRITICAL anomalies, for immediate action: an accidental `noindex`, an orphan page, a 404 on a
  business page
- Minor anomalies: `lastmod` older than 6 months, under-linking, thin content
- Ranked recommendations, 2 to 5 actions, ordered by estimated impact
- A "limits of this report" section: what could not be tested, and why

## Pre-decision output (required)

This module's table is not the end. Its output also carries a decision: a one-sentence diagnosis (the structural cause), 3 to 5 figures, a state (critical / to improve / no major issue detected, with the real data coverage), problems (3 max) and opportunities kept apart, actions P1 to P3 (3 P1 max) with why, evidence, expected signal, effort low / medium / high, confidence, risk, "Validation required" for any deletion, 301 or merge. What the data cannot support. Full format: `../audit-report/FORMAT.md`; the `audit-report` module assembles every module's decision into the final report.

Rules: every statement is a FACT, a HYPOTHESIS or an ACTION; a problem exists once; an anomaly is not a priority by default; business pages and Search Console trends before secondary technical anomalies; never a merge, 301, deletion, rewrite or new page recommended automatically; never a score out of 10, an estimate in hours or a promised figure; short content alone is never a problem; the certainty shown never exceeds the data coverage; no action on a page whose queries are unknown.

## Output required

```markdown
# Indexing check — {domain} — {date}

## Summary

Checks that came back clear:
✅ {check}: X / N
✅ ...

Checks with anomalies:
⚠️ {check}: X / N ({Y details})
⚠️ ...

## CRITICAL anomalies, immediate action

⚠️ {URL} — {what was found}
   {context: since when, estimated impact in impressions or clicks}
   → {the action to take}

## Minor anomalies

- {the secondary points, compacted}

## Ranked recommendations

1. {action 1} — {effort}, {estimated impact}
2. {action 2} — ...
3. {action 3} — ...

## Limits of this report

- {what could not be tested, and why: Google rate limit, client-side rendered JS, and so on}
```

## Guardrails, not negotiable

- **Read-only** on the public web. No authenticated request that was not explicitly allowed.
- **No action that forces indexing.** No Search Console submission, no force-crawl.
- **No change to the site.** No pull request on the source files. Output goes to `reports/` or
  straight into the conversation.
- **Keep "not indexed" and "not testable" strictly apart** in the report.
- **Reporting comes first**: an accidental `noindex` on a business page belongs at the top of the
  report, not on line 47 of a table.
- If a check fails, run the others and say so under "limits".

> The discipline: the agent observes, the human decides. An agent that can repair things can also
> break everything at 3am on a Sunday.

## High-reliability variant — the Search Console URL Inspection API

If the user has a Google Cloud service account and owns the Search Console property:
1. Read the JSON key from a secret stored on the project side
2. Sign a JWT, exchange it for an access token
3. POST to `https://searchconsole.googleapis.com/v1/urlInspection/index:inspect`
4. Official statuses available: `INDEXED`, `DISCOVERED_NOT_INDEXED`, `CRAWLED_NOT_INDEXED`,
   `URL_IS_UNKNOWN_TO_GOOGLE`

This takes check 8 from around 50% to full reliability. Setup runs about 30 minutes. It removes the
Google rate limit, the official ceiling being 2,000 inspections per day per property.

## Variant for a client-side rendered site (SPA)

If the main content is rendered client-side, `curl` sees an almost empty HTML shell. Wire in
headless Playwright:
1. Start a headless browser
2. Load the URL, wait for `networkidle`
3. Compare the rendered HTML against the HTML the server sent
4. Report anything that only exists after the JS runs, since it is invisible to crawlers that do
   not execute JS

Keep this for SPA sites or critical clusters, it costs around 30 seconds per URL.

## Running it monthly with `/schedule`

To turn the one-shot audit into continuous monitoring:
```
/schedule
```
The choices that matter:
- **Recurrence**: `cron_expression: "0 1 1 * *"` (the 1st of each month, 01:00 UTC)
- **One-shot alternative**: `run_once_at` set 14 days after shipping a cluster
- **Model**: `claude-sonnet-5` is enough for this job
- **Tools**: `Bash, Read, Write, Edit, Glob, Grep`

Each run takes 5 to 10 minutes in the background, and posts its report into the conversation, or
opens a pull request if the repo is set up for it.

## Reusing this on a client

To apply this to a client you work with:
1. Create a `urls-prio.txt` in their repo (their top 30 business pages), or point at the public
   sitemap
2. Adapt the link perimeter to their hub pages
3. Schedule it monthly
4. Include the monthly report in the follow-up note

Marginal cost per client: around 15 minutes of setup, nothing recurring. Bill it inside the monthly
retainer, or use it as a differentiator when you pitch.

## Related concepts

`grounding-score` · `passage-ranking`
