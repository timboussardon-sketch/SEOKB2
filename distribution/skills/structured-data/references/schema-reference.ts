/**
 * REFERENCE — Automatic JSON-LD structured data (Next.js App Router)
 *
 * The generalised version of a system running in production. ADAPT it to the
 * target site's data model,
 * do not copy it as is.
 *
 * The principle: one source, one entity referenced by @id, schema derived from
 * the content. These functions return plain JS objects only. The consumer
 * (layout or page, a Server Component) is what serialises them into a
 * <script type="application/ld+json">.
 *
 * Typical wiring:
 *
 *   // app/layout.tsx (Server Component)
 *   import { siteGraph } from '@/lib/schema'
 *   <script type="application/ld+json"
 *     dangerouslySetInnerHTML={{ __html: JSON.stringify(siteGraph()) }} />
 *
 *   // app/blog/[slug]/page.tsx
 *   const jsonLd = [
 *     articleSchema(article, url),
 *     breadcrumb([...]),
 *     ...(faqBlock ? [faqSchema(faqBlock.items)] : []),
 *     ...(video ? [videoSchema(video, article)] : []),
 *     ...howToFromSections(article.sections),
 *   ]
 *   <script type="application/ld+json"
 *     dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLd) }} />
 */

// ─────────────────────────────────────────────────────────────────────────
// 1. IDENTITY CONFIG — the only block to edit per site
// ─────────────────────────────────────────────────────────────────────────

export const SITE_URL = 'https://example.com'

const IDENTITY = {
  orgName: 'YourCompany',
  orgDescription: 'A clear positioning sentence, with no unverifiable superlative.',
  orgSlogan: 'A short tagline',
  foundingYear: '2020',
  isProfessionalService: true, // adds the ProfessionalService @type
  logoPath: '/logo.png',
  knowsAbout: ['SEO', 'GEO', 'AEO'],
  serviceType: ['SEO', 'SEO audit'],
  areaServedCountry: 'CountryName',
  locality: 'CityName',
  region: 'RegionName',
  countryCode: 'XX',
  email: 'contact@example.com',
  language: 'en-US',
  orgSameAs: [
    'https://www.linkedin.com/company/...',
    'https://www.youtube.com/@...',
  ],
  person: {
    slug: 'first-last',
    name: 'First Last',
    givenName: 'First',
    familyName: 'Last',
    jobTitle: 'SEO & GEO consultant',
    aboutPath: '/about',
    portraitPath: '/portrait.png',
    sameAs: [
      'https://www.linkedin.com/in/...',
      'https://x.com/...',
    ],
  },
} as const

// ─────────────────────────────────────────────────────────────────────────
// 2. IDs STABLES + REFS LÉGÈRES
// ─────────────────────────────────────────────────────────────────────────

export const ORG_ID = `${SITE_URL}/#organization`
export const WEBSITE_ID = `${SITE_URL}/#website`
export const PERSON_ID = `${SITE_URL}/#${IDENTITY.person.slug}`
const LOGO_ID = `${SITE_URL}/#logo`

export const AUTHOR_REF = { '@id': PERSON_ID } as const
export const PUBLISHER_REF = { '@id': ORG_ID } as const
export const WEBSITE_REF = { '@id': WEBSITE_ID } as const

// ─────────────────────────────────────────────────────────────────────────
// 3. NŒUDS SITE-WIDE
// ─────────────────────────────────────────────────────────────────────────

const organizationNode = {
  '@type': IDENTITY.isProfessionalService
    ? ['Organization', 'ProfessionalService']
    : 'Organization',
  '@id': ORG_ID,
  name: IDENTITY.orgName,
  legalName: IDENTITY.orgName,
  url: SITE_URL,
  description: IDENTITY.orgDescription,
  slogan: IDENTITY.orgSlogan,
  foundingDate: IDENTITY.foundingYear,
  logo: {
    '@type': 'ImageObject',
    '@id': LOGO_ID,
    url: `${SITE_URL}${IDENTITY.logoPath}`,
    contentUrl: `${SITE_URL}${IDENTITY.logoPath}`,
    caption: IDENTITY.orgName,
  },
  image: { '@id': LOGO_ID },
  founder: { '@id': PERSON_ID },
  knowsLanguage: IDENTITY.language,
  knowsAbout: IDENTITY.knowsAbout,
  serviceType: IDENTITY.serviceType,
  areaServed: { '@type': 'Country', name: IDENTITY.areaServedCountry },
  address: {
    '@type': 'PostalAddress',
    addressLocality: IDENTITY.locality,
    addressRegion: IDENTITY.region,
    addressCountry: IDENTITY.countryCode,
  },
  email: IDENTITY.email,
  contactPoint: {
    '@type': 'ContactPoint',
    email: IDENTITY.email,
    contactType: 'customer support',
    areaServed: IDENTITY.countryCode,
    availableLanguage: 'French',
  },
  sameAs: IDENTITY.orgSameAs,
}

const personNode = {
  '@type': 'Person',
  '@id': PERSON_ID,
  name: IDENTITY.person.name,
  givenName: IDENTITY.person.givenName,
  familyName: IDENTITY.person.familyName,
  url: `${SITE_URL}${IDENTITY.person.aboutPath}`,
  image: {
    '@type': 'ImageObject',
    url: `${SITE_URL}${IDENTITY.person.portraitPath}`,
  },
  jobTitle: IDENTITY.person.jobTitle,
  worksFor: { '@id': ORG_ID },
  knowsAbout: IDENTITY.knowsAbout,
  sameAs: IDENTITY.person.sameAs,
}

const websiteNode = {
  '@type': 'WebSite',
  '@id': WEBSITE_ID,
  url: SITE_URL,
  name: IDENTITY.orgName,
  description: IDENTITY.orgSlogan,
  inLanguage: IDENTITY.language,
  publisher: { '@id': ORG_ID },
}

/** The site-wide graph. Emit it ONCE, in the root layout. */
export function siteGraph() {
  return {
    '@context': 'https://schema.org',
    '@graph': [organizationNode, websiteNode, personNode],
  }
}

// ─────────────────────────────────────────────────────────────────────────
// 4. HELPERS DÉRIVÉS
// ─────────────────────────────────────────────────────────────────────────

/** Breadcrumb. Always emitted, derived from the page's real path. */
export function breadcrumb(items: { name: string; url: string }[]) {
  return {
    '@context': 'https://schema.org',
    '@type': 'BreadcrumbList',
    itemListElement: items.map((it, i) => ({
      '@type': 'ListItem',
      position: i + 1,
      name: it.name,
      item: it.url,
    })),
  }
}

/**
 * Counts the words in any section structure.
 * A defensive walk: it adds up every string value, whatever shape the content
 * takes. Use it to derive wordCount, never to hard-code it.
 */
export function countWords(value: unknown): number {
  if (typeof value === 'string') {
    return value.trim().split(/\s+/).filter(Boolean).length
  }
  if (Array.isArray(value)) {
    return value.reduce<number>((n, v) => n + countWords(v), 0)
  }
  if (value && typeof value === 'object') {
    return Object.values(value).reduce<number>((n, v) => n + countWords(v), 0)
  }
  return 0
}

// ─────────────────────────────────────────────────────────────────────────
// 5. BUILDERS PER TYPE — adapt the field names to the site's model
// ─────────────────────────────────────────────────────────────────────────

type ArticleLike = {
  title: string
  excerpt: string
  date: string
  category?: string
  highlights?: string[]
  sections: unknown
}

/** Article / BlogPosting derived from the data. Author and publisher as @id refs. */
export function articleSchema(a: ArticleLike, url: string, ogImage = `${SITE_URL}/og.png`) {
  return {
    '@context': 'https://schema.org',
    '@type': 'BlogPosting',
    headline: a.title,
    description: a.excerpt,
    url,
    datePublished: a.date,
    dateModified: a.date,
    articleSection: a.category,
    inLanguage: IDENTITY.language,
    isAccessibleForFree: true,
    wordCount: countWords(a.sections),
    keywords: a.highlights?.join(', '),
    image: ogImage,
    author: AUTHOR_REF,
    publisher: PUBLISHER_REF,
    isPartOf: WEBSITE_REF,
    mainEntityOfPage: { '@type': 'WebPage', '@id': url },
  }
}

/** FAQPage. Emitted ONLY where a real FAQ block exists on the page. */
export function faqSchema(items: { q: string; a: string }[]) {
  return {
    '@context': 'https://schema.org',
    '@type': 'FAQPage',
    mainEntity: items.map(({ q, a }) => ({
      '@type': 'Question',
      name: q,
      acceptedAnswer: { '@type': 'Answer', text: a },
    })),
  }
}

/** VideoObject. YouTube ID pulled by regex, thumbnail and embed derived. */
export function videoSchema(
  video: { url: string; caption?: string },
  ctx: { title: string; excerpt: string; date: string },
) {
  const ytId =
    video.url.match(/(?:youtu\.be\/|v=|shorts\/|embed\/)([\w-]{11})/)?.[1] ?? null
  return {
    '@context': 'https://schema.org',
    '@type': 'VideoObject',
    name: video.caption ?? ctx.title,
    description: ctx.excerpt,
    uploadDate: ctx.date,
    thumbnailUrl: ytId ? `https://i.ytimg.com/vi/${ytId}/maxresdefault.jpg` : undefined,
    contentUrl: video.url,
    embedUrl: ytId ? `https://www.youtube-nocookie.com/embed/${ytId}` : video.url,
  }
}

/**
 * HowTo derived from the sections: finds an H2 whose title matches `predicate`,
 * then collects the numbered H3s that follow and their content as HowToStep.
 * Returns [] when there is no real step, so never an empty HowTo.
 *
 * Adapt the section shape to the site's model. The default reproduces the
 * reference heuristic: an H2 containing "prompt".
 */
type Section =
  | { type: 'h2'; title: string }
  | { type: 'h3'; title: string; content?: string }
  | { type: 'p' | 'code'; content: string }
  | { type: 'ul' | 'ol'; content: string[] }
  | { type: string; [k: string]: unknown }

export function howToFromSections(
  sections: Section[],
  predicate: (h2Title: string) => boolean = (t) => /prompt/i.test(t),
) {
  const out: Record<string, unknown>[] = []
  for (let i = 0; i < sections.length; i++) {
    const s = sections[i]
    if (s.type !== 'h2' || !predicate((s as { title: string }).title)) continue
    const steps: { name: string; text: string }[] = []
    let j = i + 1
    while (j < sections.length) {
      const t = sections[j]
      if (t.type === 'h2') break
      if (t.type === 'h3' && /^\d+\.\s/.test((t as { title: string }).title)) {
        const stepName = (t as { title: string }).title.replace(/^\d+\.\s*/, '').trim()
        const parts: string[] = []
        const c = (t as { content?: string }).content
        if (c) parts.push(c)
        let k = j + 1
        while (k < sections.length) {
          const u = sections[k]
          if (u.type === 'p' || u.type === 'code') { parts.push((u as { content: string }).content); k++ }
          else if (u.type === 'ul' || u.type === 'ol') { parts.push((u as { content: string[] }).content.join('\n')); k++ }
          else break
        }
        if (parts.length) steps.push({ name: stepName, text: parts.join('\n\n') })
        j = k
      } else j++
    }
    if (steps.length) {
      out.push({
        '@context': 'https://schema.org',
        '@type': 'HowTo',
        name: (s as { title: string }).title,
        step: steps.map((st, idx) => ({
          '@type': 'HowToStep',
          position: idx + 1,
          name: st.name,
          text: st.text,
        })),
      })
      break // un seul HowTo par page
    }
  }
  return out
}
