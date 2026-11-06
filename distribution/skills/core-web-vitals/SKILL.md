---
name: core-web-vitals
description: "Core Web Vitals audit (LCP, CLS, TBT) via local Lighthouse, mobile. \"CWV audit\", \"page speed\", \"why is my site slow\"."
---

# Core Web Vitals audit, with local Lighthouse

## Quand utiliser ce skill

Core Web Vitals audit (LCP, CLS, TBT) of a site, through local Lighthouse on a sample of URLs pulled from sitemap.xml. Mobile only. Produces a score table per URL, the problems that repeat site-wide, and a ranked fix plan for the five worst pages.

ALWAYS use this skill when the user says: "Core Web Vitals audit", "CWV audit", "SEO performance", "LCP CLS TBT", "Lighthouse audit", "page speed", "site performance audit", "why is my site slow", "PageSpeed score", "mobile performance audit", "Lighthouse score", "Web Vitals audit".

Part of the technical SEO set. Works alongside `indexing-check`, `structured-data`, `cannibalization-audit` and `internal-linking`.

## When this fires

Diagnosing the performance of a whole site, or getting the picture before a technical job (rebuild,
performance work, migration). Always mobile, since Google indexes mobile-first.

## Prerequisites, checked at the start

```bash
which lighthouse || echo "MISSING — install with: npm install -g lighthouse"
which jq || echo "MISSING — install with: brew install jq"
```

If Lighthouse is missing, offer `npm install -g lighthouse` to the user and stop. Do not install it
silently.

Without a global install: replace `lighthouse` with `npx lighthouse` in every command. The first
run is slower.

## Input required

| Source | Required | Default |
|--------|----------|---------|
| The sitemap.xml URL (`https://site.com/sitemap.xml`) | Yes | — |
| Sample size | No | 50 URLs |
| `all` mode, auditing every URL in the sitemap | No | off |

## The five steps

### Step 1 — Pull the sitemap

```bash
SITEMAP_URL="<url>"
curl -sL "$SITEMAP_URL" | grep -oE '<loc>[^<]+</loc>' | sed -E 's|</?loc>||g' > /tmp/cwv-urls.txt
wc -l /tmp/cwv-urls.txt
```

**Matters on BSD and macOS**: use `sed -E 's|</?loc>||g'` and **not** `sed 's|</\?loc>||g'`. The
`\?` does nothing in BSD sed and leaves the tags in place without saying a word.

**If the sitemap is an index** (it holds `<sitemapindex>` rather than `<urlset>`), take the first
child sitemap and work from that:

```bash
FIRST_CHILD=$(curl -sL "$SITEMAP_URL" | grep -oE '<loc>[^<]+</loc>' | sed -E 's|</?loc>||g' | head -1)
curl -sL "$FIRST_CHILD" | grep -oE '<loc>[^<]+</loc>' | sed -E 's|</?loc>||g' > /tmp/cwv-urls.txt
```

### Step 2 — Sample

```bash
TOTAL=$(wc -l < /tmp/cwv-urls.txt | tr -d ' ')
if [ "$TOTAL" -gt 50 ] && [ "$MODE" != "all" ]; then
  head -50 /tmp/cwv-urls.txt > /tmp/cwv-sample.txt
else
  cp /tmp/cwv-urls.txt /tmp/cwv-sample.txt
fi
wc -l /tmp/cwv-sample.txt
```

The first 50 URLs of a sitemap are usually the ones that matter most: homepage, hubs, top articles.
If the user asks for `all`, audit everything.

### Step 3 — Run Lighthouse on mobile, 3 workers in parallel

```bash
rm -rf /tmp/cwv-results /tmp/cwv-errors.log
mkdir -p /tmp/cwv-results
cat /tmp/cwv-sample.txt | xargs -I {} -P 3 sh -c '
  url="$1"
  hash=$(echo -n "$url" | md5)
  lighthouse "$url" \
    --output=json \
    --output-path="/tmp/cwv-results/${hash}.json" \
    --only-categories=performance \
    --form-factor=mobile \
    --screenEmulation.mobile=true \
    --chrome-flags="--headless=new --no-sandbox" \
    --quiet 2>/dev/null || echo "FAIL: $url" >> /tmp/cwv-errors.log
' _ {}
echo "Results: $(ls /tmp/cwv-results/ 2>/dev/null | wc -l | tr -d ' ')"
[ -f /tmp/cwv-errors.log ] && echo "Errors:" && cat /tmp/cwv-errors.log
```

**Matters on zsh**: use `rm -rf /tmp/cwv-results && mkdir -p /tmp/cwv-results` and **not**
`rm -f /tmp/cwv-results/*`. An empty glob makes zsh error out with `no matches found`, and the
exit code 1 can stop everything after it.

**`--headless=new`**, not the legacy `--headless`. It has been the stable one since Chrome 109 and
Lighthouse 13 needs it.

**Timing**: 15 to 30 seconds per URL with 3 workers. 50 URLs runs 5 to 10 minutes.

### Step 4 — Parse the results

For each JSON in `/tmp/cwv-results/`, pull the values with jq, using the Lighthouse 13 paths:

```bash
for f in /tmp/cwv-results/*.json; do
  jq '{
    url: .finalDisplayedUrl,
    lcp_ms: (.audits."largest-contentful-paint".numericValue // 0),
    cls: (.audits."cumulative-layout-shift".numericValue // 0),
    tbt_ms: (.audits."total-blocking-time".numericValue // 0),
    score: ((.categories.performance.score // 0) * 100),
    lcp_element: [.audits."lcp-breakdown-insight".details.items[]? | select(.type == "node") | {selector, snippet, nodeLabel}] | .[0],
    lcp_breakdown: [.audits."lcp-breakdown-insight".details.items[]? | select(.type == "table") | .items[]? | {subpart, label, duration_ms: .duration}],
    opportunities: [.audits | to_entries[] | select(.value.details.type == "opportunity" and (.value.details.overallSavingsMs // 0) > 100) | {id: .key, title: .value.title, savings_ms: .value.details.overallSavingsMs}] | sort_by(-.savings_ms) | .[0:5]
  }' "$f"
done | jq -s '.' > /tmp/cwv-parsed.json
echo "Parsed: $(jq 'length' /tmp/cwv-parsed.json) URLs"
```

**The Lighthouse 13 paths that trip people up**:
- Final URL: `.finalDisplayedUrl`, **not** `.finalUrl`, which can come back null
- LCP element: `.audits."lcp-breakdown-insight".details.items[] | select(.type == "node")`, **not**
  `.audits."largest-contentful-paint-element"`, which has been null since LH 13
- LCP breakdown (TTFB / render delay / load delay):
  `.audits."lcp-breakdown-insight".details.items[] | select(.type == "table") | .items[]`. This is
  what tells you **where** the LCP time goes

**Google's thresholds, which set the verdict**:

| Metric | Good | Needs improvement | Poor |
|--------|------|-------------------|------|
| LCP | under 2500 ms | 2500-4000 ms | over 4000 ms |
| CLS | under 0.1 | 0.1-0.25 | over 0.25 |
| TBT (proxy for INP) | under 200 ms | 200-600 ms | over 600 ms |
| Performance score | 90 or more | 50-89 | under 50 |

### Step 4b — Catch the "sitemap redirect" pattern automatically

If the `redirects` opportunity shows on **more than half the pages audited** with an average saving
over 300 ms, it is almost certainly a trailing slash mismatch between the sitemap and the server.

```bash
REDIRECT_COUNT=$(jq -r '.[] | .opportunities[] | select(.id == "redirects") | .id' /tmp/cwv-parsed.json | wc -l | tr -d ' ')
TOTAL=$(jq 'length' /tmp/cwv-parsed.json)
if [ "$REDIRECT_COUNT" -gt $((TOTAL / 2)) ]; then
  echo "⚠️ ALERT: $REDIRECT_COUNT/$TOTAL pages redirect. Check the sitemap trailing slash against the server."
fi
```

When this shows up it goes at the TOP of the report. It is the most profitable fix on the list.

### Step 5 — Write the markdown report

See the output section below.

## Pre-decision output (required)

This module's table is not the end. Its output also carries a decision: a one-sentence diagnosis (the structural cause), 3 to 5 figures, a state (critical / to improve / no major issue detected, with the real data coverage), problems (3 max) and opportunities kept apart, actions P1 to P3 (3 P1 max) with why, evidence, expected signal, effort low / medium / high, confidence, risk, "Validation required" for any deletion, 301 or merge. What the data cannot support. Full format: `../audit-report/FORMAT.md`; the `audit-report` module assembles every module's decision into the final report.

Rules: every statement is a FACT, a HYPOTHESIS or an ACTION; a problem exists once; an anomaly is not a priority by default; business pages and Search Console trends before secondary technical anomalies; never a merge, 301, deletion, rewrite or new page recommended automatically; never a score out of 10, an estimate in hours or a promised figure; short content alone is never a problem; the certainty shown never exceeds the data coverage; no action on a page whose queries are unknown.

## Output required

```markdown
# Core Web Vitals audit — [domain] — [date]

**Sample**: X URLs audited out of Y in the sitemap. **Form factor**: mobile.
**Worth knowing**: INP cannot be measured locally by Lighthouse, it is a field metric. TBT stands
in as the proxy.

## Scores per URL

| URL | LCP | CLS | TBT | Score | Verdict |
|-----|-----|-----|-----|-------|---------|
| / | 1.8s ✅ | 0.05 ✅ | 150ms ✅ | 92 | Good |
| /blog/article-x | 4.2s ❌ | 0.18 ⚠️ | 720ms ❌ | 38 | Poor |
| /category/y | — | — | — | — | ERROR (timeout) |

Key: ✅ good — ⚠️ needs improvement — ❌ poor

## Summary

- **X of Y pages** are poor, scoring under 50
- **X of Y pages** have an LCP over 4s, which is critical for ranking
- **X of Y pages** have a CLS over 0.25, which degrades the experience
- Median performance score: X. Mean: Y

## Problems that repeat site-wide

Lighthouse opportunities showing on more than 30% of the pages audited:

1. **Unused JavaScript** — X pages — average saving: Xs
   - Likely cause: [bundle not tree-shaken / third-party scripts: analytics, chat, ads]
2. **Render-blocking resources** — X pages — average saving: Xs
3. **Properly size images** — X pages — average saving: Xs
4. **Largest Contentful Paint image** — X pages — average saving: Xs
5. **Reduce JavaScript execution time** — X pages — average saving: Xs

## The five pages to fix first

(sorted by performance score, ascending)

### 1. /blog/article-x (score: 38)
- **LCP**: 4.2s ❌ — element: `<img class="hero" src="...">` (selector: `main > article > img.hero`)
  - Breakdown: TTFB 800ms / load delay 1200ms / load duration 1500ms / render delay 700ms
  - → Most of the time goes into **load delay**, the image is discovered late
- **CLS**: 0.18 ⚠️ — likely shifts: ad slots, images without dimensions
- **TBT**: 720ms ❌ — blocking JS: [the scripts found]

**Fix plan**:
1. Preload the hero LCP image and add `fetchpriority="high"`
2. Set explicit width and height on every content image
3. Defer the non-critical scripts (analytics, chat), and set iframes to `loading="lazy"`

**Reading the LCP breakdown**:
- TTFB over 600ms → server, CDN or cache
- Load delay over 200ms → the LCP image is not in the initial HTML (lazy, CSS background, injected
  by JS)
- Load duration over 500ms → the image is too heavy, or not served in a modern format (avif, webp)
- Render delay over 300ms → render-blocking CSS or JS, or slow hydration

### 2. ...

(repeat for the five worst)

## Limits of this audit

- INP is not measured. Lighthouse is a lab tool, TBT stands in as the proxy
- No variation across real devices, this emulates a Moto G Power
- No measurement on a real connection, the 4G throttling is simulated
- For real field data, cross this with the PageSpeed Insights API or CrUX
```

## Hard rules

- **Mobile only.** Google indexes mobile-first. Desktop is never the default here.
- **INP is not measured.** Always say in the report that TBT stands in as the proxy.
- **No invented score.** If a URL fails (timeout, 404, JS error), mark it `ERROR` in the table, not
  `0` and not a placeholder.
- **No recommendation without a matching Lighthouse opportunity.** Do not write "X should be
  optimised" if Lighthouse did not raise it for that page.
- **No silent install.** If Lighthouse is missing, ask the user to install it.
- **An honest sample.** If the sample is 50 URLs out of 2,000, say so plainly. Do not extrapolate
  to the whole site from 2.5% of it.

## Edge cases

- **A sitemap index** (sitemapindex rather than urlset) → take the first child and use it, and tell
  the user they can name a specific child sitemap to target.
- **A protected sitemap** (auth, 403) → ask the user for a local export of the URLs.
- **More than 500 URLs in `all` mode** → confirm with the user, it will be slow: 500 URLs at around
  10s across 3 workers runs about 30 minutes.
- **An SPA, or a site behind auth** → some pages will time out, that is expected, mark them ERROR.
- **A multi-language sitemap** → leave it as is, the report will show the gaps per locale.
