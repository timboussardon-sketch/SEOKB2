---
name: structured-data
description: "Automatic JSON-LD structured data on Next.js. \"structured data\", \"schema.org\", \"JSON-LD\", \"rich results\"."
---

# Automatic JSON-LD structured data

## Quand utiliser ce skill

Sets up automatic JSON-LD structured data on a Next.js site (App Router):
one site-wide entity graph referenced by @id, and per-page schemas DERIVED
from the content (Article, FAQPage, HowTo, VideoObject, BreadcrumbList) with
nothing typed by hand. Generalised from a system running in production.

ALWAYS use this skill when the user says: "structured data", "schema.org",
"JSON-LD", "rich results", "rich snippets", "markup", "FAQPage",
"HowTo schema", "BreadcrumbList", "VideoObject", "Google entity",
"site knowledge graph", "@id graph", or asks to add, rebuild or audit the
structured markup of a site (Next.js App Router first).

## When this fires

Adding, rebuilding or auditing the structured markup of a site. The goal is eligibility for Google
rich results, and a single consolidated entity that answer engines can use. Not decorative schema.
Schema that serves grounding and citation.

## The principle, and it is not negotiable

Three rules, in this order. If one of them goes, the skill has failed.

1. **One source.** All the JSON-LD comes out of a single module (`lib/schema.ts`). No schema block
   written by hand inside a page.
2. **One entity, referenced by `@id`.** The site-wide graph (Organization, WebSite, Person) is
   emitted once, in the root layout. Every content page points at those nodes by `@id`
   (author / publisher / isPartOf); it never redeclares the author or the publisher. Google merges
   every block on a page and consolidates one entity. That is what builds the site's knowledge
   graph. Repetition does not.
3. **Schema is derived from the content, never typed by hand.** A schema field that is not computed
   from the page's own data is a debt: it falls out of sync at the first edit. If it has to be typed
   twice, it is broken.

## The reference architecture

Site-wide graph (`siteGraph()`, emitted in the root layout):

- `Organization` (plus `ProfessionalService` for a service business) with
  `@id = {SITE_URL}/#organization`
- `WebSite` with `@id = {SITE_URL}/#website`, `publisher` -> Organization ref
- `Person` (founder / author) with `@id = {SITE_URL}/#person-...`, `worksFor` -> Organization ref
- `ImageObject` logo with `@id = {SITE_URL}/#logo`, shared by `logo` and `image`
- `sameAs`: real social profiles (LinkedIn, YouTube, X, Substack). No invented URL.

Light refs, exported once and reused everywhere: `AUTHOR_REF = {'@id': PERSON_ID}`,
`PUBLISHER_REF = {'@id': ORG_ID}`, `WEBSITE_REF = {'@id': WEBSITE_ID}`.

## The derivation rule, which is the heart of this skill

Each schema type follows from a signal already present in the page's data. Apply this mapping:

| Signal in the content | Schema emitted | How it is derived |
|---|---|---|
| Any article or post page | `Article` or `BlogPosting` | title, excerpt, date, section; `wordCount` computed by `countWords()`; `keywords` from the highlights; author/publisher/isPartOf as refs |
| Every page, always | `BreadcrumbList` | `breadcrumb()` from the path (Home > section > title) |
| A `faq` block present in the sections | `FAQPage` | `mainEntity` = the q/a items mapped to Question/Answer. Nothing typed |
| A `video` section present | `VideoObject` | YouTube ID pulled from the URL by regex; thumbnail and embedUrl derived |
| An H2 whose title matches a predicate (contains "prompt", "steps", "tutorial") | `HowTo` | collects the numbered H3s that follow and their content (p / code / lists) as `HowToStep` |
| A product or offer page with a price | `Product` / `Offer` | from the price and availability fields in the data. Never an invented price |

The user is never asked which schema they want. Read the page structure and emit what the structure
proves. A schema with no proof in the content gets deleted.

## The procedure

1. **Read the ground.** Framework and version. If Next.js: App Router or Pages? Read the project's
   own bundled docs (`node_modules/next/dist/docs/`) and its internal conventions before writing a
   line. Never assume the metadata API.
2. **Map the data model.** Where the articles, pages, FAQs and videos live (`src/data/*.ts` for
   instance). Identify the shape of the sections, since the schema is derived from it.
3. **Create or rebuild `lib/schema.ts`**: identity config at the top (SITE_URL, Organization /
   Person identity, social profiles), then the nodes, `siteGraph()`, the `@id` refs, and the
   `breadcrumb()` and `countWords()` helpers. Start from `references/schema-reference.ts`.
4. **Wire the root layout**: a single `<script type="application/ld+json">` holding `siteGraph()`.
5. **Wire each content template**: build a `jsonLd[]` array (Article and breadcrumb always, then
   FAQ / Video / HowTo conditionally on the signals), serialised into ONE script at the top of the
   page.
6. **Deduplicate.** Remove every old Organization or Person block redeclared inside pages;
   everything goes through the `@id` refs.
7. **Validate** against the checklist below. Fix until there are no errors left.

## How it is emitted

- Site-wide: one `<script type="application/ld+json">` in the root layout, holding `siteGraph()`.
- Per page: one `<script type="application/ld+json">` at the top, holding `JSON.stringify(jsonLd)`
  where `jsonLd` is the array of that page's nodes.
- App Router: injected with `dangerouslySetInnerHTML` from a Server Component. No third-party
  library, these are plain JS objects.

## Validation checklist, zero errors tolerated

- [ ] Every site-wide `@id` is unique and stable, and reused by ref inside the pages
- [ ] No page redeclares a full Organization or Person node
- [ ] `Article`: headline not empty, `datePublished` valid, `wordCount` computed rather than
      hard-coded, author and publisher as refs
- [ ] `FAQPage` emitted only where a real FAQ block exists, and every answer is real text
- [ ] `HowTo` emitted only where ordered steps really exist
- [ ] `VideoObject`: `contentUrl` and `embedUrl` resolved, thumbnail valid
- [ ] `BreadcrumbList` matches the real URL
- [ ] The JSON-LD is valid and passes both Google's Rich Results test and the schema.org validator
- [ ] No invented field (price, rating, review, "first in X") without proof: a false signal drags
      the page's quality down

## Anti-patterns, never do these

- Redeclaring the author and publisher on every page instead of referencing them by `@id`
- Writing JSON-LD by hand inside a page's JSX
- Emitting a `FAQPage` or a `HowTo` "just in case", with no matching content visible on the page.
  That risks a penalty, and it lies to Google
- Adding `aggregateRating`, `Review` or prices that cannot be verified
- Stacking redundant `<script ld+json>` blocks instead of one array per page
- Hard-coding `wordCount`, dates or counters instead of deriving them from the data
- Assuming the Next.js API without reading the docs for the version the project runs

## Implementation reference

`references/schema-reference.ts` is a generalised module, ready to adapt: identity config at the
top, then the nodes, `siteGraph`, the `@id` refs, `breadcrumb`, `countWords`, and the
`articleSchema` / `faqSchema` / `videoSchema` / `howToFromSections` builders. It is the generalised
version of a system running in production. Adapt it to the target site's data model rather than
copying it as is.

## Related concepts

`aeo` · `grounding-score` · `vector-entities` · `passage-ranking` · `knowledge-graph` · `e-e-a-t`
