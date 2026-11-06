---
name: seo-donnees-structurees
description: "Données structurées JSON-LD automatiques sur Next.js. « données structurées », « schema.org », « JSON-LD »."
---

# Skill — Données structurées JSON-LD automatiques

## Quand utiliser ce skill

Mise en place de données structurées JSON-LD automatiques sur un site Next.js
(App Router) : graphe d'entité site-wide unique référencé par @id, et schémas
par page DÉRIVÉS du contenu (Article, FAQPage, HowTo, VideoObject,
BreadcrumbList) sans saisie manuelle. Généralisé à partir du système en
production sur organikk-next (src/lib/schema.ts).

TOUJOURS utiliser ce skill quand l'utilisateur dit : "données structurées",
"schema.org", "JSON-LD", "rich results", "rich snippets", "balisage",
"FAQPage", "HowTo schema", "BreadcrumbList", "VideoObject", "entité Google",
"knowledge graph du site", "@id graph", ou demande d'ajouter, refondre ou
auditer le balisage structuré d'un site (en priorité Next.js App Router).

## Quand déclencher

Ajouter, refondre ou auditer le balisage structuré d'un site. Objectif : éligibilité aux rich results Google ET consolidation d'une entité unique exploitable par les moteurs de réponse (AEO). Pas du schema décoratif, du schema qui sert le Grounding et la citation.

## Principe non-négociable

Trois règles, dans cet ordre. Si l'une saute, le skill a échoué.

1. **Source unique.** Tout le JSON-LD vient d'un seul module (`lib/schema.ts`). Aucun bloc schema écrit en dur dans une page.
2. **Une entité, référencée par `@id`.** Le graphe site-wide (Organization, WebSite, Person) est émis une seule fois dans le layout racine. Chaque page de contenu pointe vers ces nœuds par `@id` (author / publisher / isPartOf), elle ne redéclare jamais l'auteur ni l'éditeur. Google fusionne tous les blocs d'une page et consolide une seule entité. C'est ça qui construit le knowledge graph du site, pas la répétition.
3. **Le schema est dérivé du contenu, jamais saisi à la main.** Un champ schema qui n'est pas calculé depuis la donnée de la page est une dette : il se désynchronise au premier edit. Si on doit le taper deux fois, c'est cassé.

## Architecture de référence

Graphe site-wide (`siteGraph()`, émis dans le layout racine) :

- `Organization` (+ `ProfessionalService` si activité de service) avec `@id = {SITE_URL}/#organization`
- `WebSite` avec `@id = {SITE_URL}/#website`, `publisher` -> ref Organization
- `Person` (fondateur / auteur) avec `@id = {SITE_URL}/#person-...`, `worksFor` -> ref Organization
- `ImageObject` logo avec `@id = {SITE_URL}/#logo`, partagé par `logo` et `image`
- `sameAs` : profils sociaux réels (LinkedIn, YouTube, X, Substack). Pas d'URL inventée.

Refs légères exportées et réutilisées partout : `AUTHOR_REF = {'@id': PERSON_ID}`, `PUBLISHER_REF = {'@id': ORG_ID}`, `WEBSITE_REF = {'@id': WEBSITE_ID}`.

## Règle de dérivation automatique (le cœur du skill)

Chaque type de schema se déduit d'un signal présent dans la donnée de la page. Tableau de correspondance à appliquer :

| Signal dans le contenu | Schema émis | Dérivation |
|---|---|---|
| Toute page article / post | `Article` ou `BlogPosting` | titre, excerpt, date, section ; `wordCount` calculé par `countWords()` ; `keywords` depuis les highlights ; author/publisher/isPartOf = refs |
| Toute page (toujours) | `BreadcrumbList` | `breadcrumb()` à partir du chemin (Accueil > rubrique > titre) |
| Bloc `faq` présent dans les sections | `FAQPage` | `mainEntity` = map des items q/a en Question/Answer. Zéro saisie |
| Section `video` présente | `VideoObject` | ID YouTube extrait par regex de l'URL ; thumbnail + embedUrl déduits |
| H2 dont le titre matche un prédicat (ex. contient "prompt", "étapes", "tutoriel") | `HowTo` | collecte les H3 numérotés suivants + leur contenu (p / code / listes) en `HowToStep` |
| Page produit / offre avec prix | `Product` / `Offer` | depuis les champs prix/dispo de la donnée. Jamais de prix inventé |

Principe : on ne demande jamais à l'utilisateur "quel schema veux-tu". On lit la structure de la page et on émet ce que la structure prouve. Un schema sans preuve dans le contenu = suppression.

## Procédure

1. **Détecter le terrain.** Framework et version. Si Next.js : App Router ou Pages ? Lire la doc du projet (sur organikk-next : `node_modules/next/dist/docs/`, conventions imposées par AGENTS.md) avant d'écrire une ligne. Ne jamais présumer l'API metadata.
2. **Cartographier le modèle de données.** Où vivent les articles, pages, FAQ, vidéos (ex. `src/data/*.ts`). Identifier la forme des sections (le schema se dérive de là).
3. **Créer / refondre `lib/schema.ts`** : config d'identité en tête (SITE_URL, identité Organization/Person/sociaux), les nœuds, `siteGraph()`, les refs `@id`, les helpers `breadcrumb()` et `countWords()`. Partir de `references/schema-reference.ts`.
4. **Câbler le layout racine** : un seul `<script type="application/ld+json">` avec `siteGraph()`.
5. **Câbler chaque template de contenu** : construire un tableau `jsonLd[]` (Article + breadcrumb toujours, puis FAQ / Video / HowTo conditionnels selon les signaux), sérialisé dans UN script en tête de page.
6. **Dédupliquer.** Supprimer tout ancien bloc Organization/Person redéclaré dans les pages : tout passe par les refs `@id`.
7. **Valider** (voir checklist). Corriger jusqu'à zéro erreur.

## Émission

- Site-wide : un `<script type="application/ld+json">` dans le layout racine, contenu = `siteGraph()`.
- Par page : un seul `<script type="application/ld+json">` en tête, contenu = `JSON.stringify(jsonLd)` où `jsonLd` est le tableau des nœuds de la page.
- App Router : injection via `dangerouslySetInnerHTML` dans un Server Component. Ne pas utiliser de lib tierce, ce sont des objets JS purs.

## Validation (checklist, zéro erreur tolérée)

- [ ] Chaque `@id` site-wide est unique et stable, réutilisé par ref dans les pages
- [ ] Aucune page ne redéclare un nœud Organization ou Person en entier
- [ ] `Article` : headline non vide, `datePublished` valide, `wordCount` calculé (pas codé en dur), author/publisher en ref
- [ ] `FAQPage` émis seulement si un vrai bloc FAQ existe, et chaque réponse est du texte réel
- [ ] `HowTo` émis seulement si des étapes ordonnées existent réellement
- [ ] `VideoObject` : `contentUrl`/`embedUrl` résolus, thumbnail valide
- [ ] `BreadcrumbList` cohérent avec l'URL réelle
- [ ] JSON-LD valide et passe le test Rich Results de Google + le validateur schema.org
- [ ] Aucun champ inventé (prix, note, avis, premier sur X) sans preuve : un faux signal dégrade la note Google de la page

## Anti-patterns (à ne jamais faire)

- Redéclarer l'auteur et l'éditeur sur chaque page au lieu de référencer par `@id`
- Écrire du JSON-LD en dur dans le JSX d'une page
- Émettre un `FAQPage` ou `HowTo` "au cas où" sans contenu correspondant visible sur la page (risque de pénalité, et c'est du mensonge à Google)
- Mettre `aggregateRating` / `Review` / prix non vérifiables
- Multiplier les `<script ld+json>` redondants au lieu d'un tableau unique par page
- Hardcoder `wordCount`, des dates ou des compteurs au lieu de les dériver de la donnée
- Présumer l'API Next.js sans lire la doc de la version du projet

## Référence d'implémentation

`references/schema-reference.ts` : module généralisé prêt à adapter (config d'identité en tête, nœuds, `siteGraph`, refs `@id`, `breadcrumb`, `countWords`, builders `articleSchema` / `faqSchema` / `videoSchema` / `howToFromSections`). C'est la version dé-Organikk-isée du système en production sur `organikk-next/src/lib/schema.ts`. L'adapter au modèle de données du site cible, ne pas le copier tel quel.

## Concepts liés

`aeo` · `grounding-score` · `entites-vectorielles` · `passage-ranking` · `knowledge-graph` · `e-e-a-t`
