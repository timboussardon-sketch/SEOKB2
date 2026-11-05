---
name: indexation-check
description: Audite l'indexation d'un site en lecture seule. 9 contrôles, "non indexée" et "non testée" toujours séparés. Déclencheurs : "audit indexation", "mes pages sont-elles indexées", "vérifier l'indexation".
---

# Audit d'indexation

## Ce que tu donnes à Claude

- Le domaine et le sitemap (ou un `urls.txt`).
- Tes pages d'offre prioritaires : elles passent en tête du rapport.
- Un accès Search Console, si tu l'as. C'est la seule source fiable du statut.

## Consigne

> Audit indexation de mon-site.fr, la liste des URLs est dans sitemap.xml.

## Les 9 contrôles

Causes :
1. Statut HTTP et chaîne de redirections.
2. robots.txt : aucun `Disallow` sur la page.
3. `noindex` dans le HTML ou l'en-tête `X-Robots-Tag`.
4. Présence dans le sitemap et `lastmod`.
5. Écart entre ta liste et le sitemap.
6. Liens internes entrants.
7. Longueur du contenu principal.

Statut :
8. Avec Search Console : l'API URL Inspection, 2 000 inspections par jour et par propriété. Sans elle : `site:`, 4 secondes entre deux requêtes.

Rapport :
9. Synthèse, anomalies critiques en tête, limites.

## Ce que `site:` prouve

Une présence prouve l'indexation à la date du test.

Une absence ne prouve rien.

Page bloquée par Google : écris « non testable », jamais « non indexée ».

## Conclusions interdites

- HTTP 200 = indexée.
- Hors sitemap = problème.
- URL inconnue = manque de maillage.
- `lastmod` ancien = sitemap mauvais.
- Moins de 300 mots = problème d'indexation.
- Quelques URL testées = tout le lot dans le même état.
- Non testée = non indexée.

## Règles

- « Rien de confirmé » est une réponse autorisée.
- 404 traitées URL par URL : 301 seulement vers une page équivalente, sinon 404 ou 410. Jamais de 301 de dossier à dossier.
- Un `noindex` accidentel sur une page d'offre remonte en tête du rapport.
- Lecture seule : aucune soumission, aucune modification du site.

## Sortie

- Diagnostic en une phrase.
- 3 à 5 chiffres, avec leur source.
- 3 problèmes maximum : état constaté, preuve, action.
- 3 actions P1 maximum.
- Ce que les données ne permettent pas de conclure.

Enregistre la sortie dans `AAAA-MM-JJ-<site>-indexation.md`.

## Récurrence

Valide un premier rapport à la main. Vérifie deux ou trois constats toi-même.

Ensuite seulement, programme un contrôle mensuel avec `/schedule`.
