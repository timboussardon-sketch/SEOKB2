---
name: seo-donnees-structurees
description: Met en place ou audite les données structurées JSON-LD d'un site, dérivées du contenu de chaque page. Déclencheurs : "données structurées", "JSON-LD", "schema.org", "rich results", "balisage".
---

# Données structurées JSON-LD

## Ce que tu donnes à Claude

- L'accès au code du site.
- L'URL des pages à contrôler.
- L'identité réelle : nom, logo, fondateur, profils sociaux.

## Consigne

> Mets en place les données structurées JSON-LD sur ce projet.

> Vérifie que le balisage de [URL] correspond à ce que la page affiche.

## Trois règles

1. **Une seule source.** Tout le JSON-LD vient d'un module (`lib/schema.ts`). Aucun bloc écrit en dur dans une page.
2. **Une entité, référencée par `@id`.** Organization, WebSite et Person sont émis une fois, dans le layout racine. Chaque page y renvoie par `@id`, sans les redéclarer.
3. **Dérivé du contenu.** Un champ tapé à la main se désynchronise au premier edit.

## Ce que chaque signal déclenche

| Signal dans la page | Schema |
|---|---|
| Article | `Article`, `wordCount` calculé |
| Toute page | `BreadcrumbList` depuis le chemin |
| Bloc FAQ réel | `FAQPage` |
| Vidéo YouTube | `VideoObject` |
| Étapes numérotées | `HowTo` |
| Prix affiché | `Product` / `Offer` |

Ne demande jamais « quel schema veux-tu ». Lis la page, émets ce qu'elle prouve.

## Procédure

1. Identifie le framework et sa version. Lis sa doc avant d'écrire.
2. Repère où vivent les données : articles, FAQ, vidéos.
3. Crée `lib/schema.ts` à partir de `references/schema-reference.ts`.
4. Émets le graphe du site dans le layout racine, un seul script.
5. Émets un tableau JSON-LD par page, un seul script.
6. Supprime les anciens blocs redéclarés.
7. Valide avec le test des résultats enrichis Google et le validateur schema.org.

## Audit : trois contrôles

- Le JSON est valide.
- Chaque valeur balisée existe telle quelle sur la page.
- Le balisage sert une fonctionnalité Google réelle.

Un balisage qui dit ce que la page ne montre pas est un défaut.

## Interdits

- `FAQPage` ou `HowTo` « au cas où ».
- `aggregateRating`, avis ou prix invérifiables.
- Auteur et éditeur redéclarés sur chaque page.
- `wordCount` ou dates codés en dur.

Google a retiré les résultats enrichis FAQ le 7 mai 2026. Un `FAQPage` n'apporte plus d'affichage enrichi.

Demande ton accord avant chaque écriture dans le code.
