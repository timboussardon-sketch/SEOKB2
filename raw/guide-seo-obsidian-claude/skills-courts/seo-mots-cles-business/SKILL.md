---
name: seo-mots-cles-business
description: Trie les mots-clés d'un site par intention business, avec ou sans Search Console. Trois portes, cinq décisions, aucun volume inventé. Déclencheurs : "mots-clés business", "quels mots-clés cibler", "sur quoi mon site doit se battre".
---

# Mots-clés business

## Ce que tu donnes à Claude

- L'offre et le point de conversion (devis, rendez-vous, achat).
- La cible, le marché, la langue.
- Les URL des pages d'offre.
- L'export Search Console Requêtes + Pages, 3 à 6 mois, si tu l'as.
- Des verbatims clients, si tu en as.

## Consigne

> Lance seo-mots-cles-business sur [URL]. Offre : [...], cible : [...], conversion : [...], marché : [...].

## Étapes

1. Liste les requêtes hors marque. Regroupe les variantes d'un même besoin en une intention. Signale chaque fusion.
2. Sans Search Console, collecte Google Suggest, recherche web et verbatims. Deux requêtes qui partagent le même top 10 vont sur une seule page.
3. Écarte ce qu'une IA répond sans clic : définition, « comment », fait unique. Garde achat, prix, comparatif, avis, local.
4. Passe chaque intention aux trois portes :
   - Correspond à l'offre ? Oui / Non.
   - Intention business ? Forte / Moyenne / Faible, lue aux modificateurs, jamais au volume.
   - Opportunité démontrée ? Déjà captée / Nouvelle / Non démontrée.
5. Décide : POUSSER, CRÉER, CONSOLIDER, ÉCARTER ou À VALIDER.

## Demande observée (sans Search Console)

Écris Faible / Moyenne / Forte, avec les signaux nommés à côté.

Forte : 5 variantes Suggest ou plus, 7 mentions en calls ou plus.

Seules 20 impressions Search Console ou plus confirment la demande.

## Sortie

- Diagnostic en une phrase.
- 3 à 5 chiffres, avec source et période.
- Quatre tableaux : intentions captées, opportunités sans page, pages qui sous-performent, requêtes écartées avec leur raison.
- 3 actions maximum, chacune justifiée par sa porte.
- Ce que les données ne permettent pas de conclure.

## Règles

- Aucun volume, position ou CPC inventé.
- Aucun score sur 10.
- Une requête à fort volume hors offre finit ÉCARTÉE, raison écrite.
- La Search Console ne montre pas tout le marché. Une intention absente de l'export n'est pas écartée pour ça.
- Aucune page créée par automatisme. Cherche d'abord une URL ou un contenu existant.

Enregistre la sortie dans `AAAA-MM-JJ-<site>-mots-cles-business.md`.
