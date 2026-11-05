---
type: source
source_type: test-terrain
title: Questionnaire de pré-audit en fin de stratégie SEO B2B
tags: [organikk, conversion, site]
created: 2026-10-10
updated: 2026-10-10
sources: 2
confidence: high
status: stable
---

# Questionnaire de pré-audit

Demande de Tim : préciser une présentation en visio de 30 minutes et ajouter un questionnaire final inspiré de la candidature Bootcamp.

La page `/strategie-seo-b2b/` comporte désormais un questionnaire progressif : URL, problématique, budget et temporalité de démarrage, dans cet ordre demandé par Tim. Après correction de Tim, le fond outremer grainé, la feuille blanche arrondie et les boutons reprennent la DA Bootcamp. La progression, le retour et les choix radio reprennent le principe de `src/content/da/bootcamp.html`. L’envoi utilise le même endpoint Formspree, avec un objet de pré-audit distinct et la source de la page. La confirmation propose la réservation d’une visio de 30 minutes. Les coordonnées sont renseignées sur le calendrier ; aucune question de contact supplémentaire dans le questionnaire.

Fichiers modifiés dans `/Users/timothee/Code/organikk-next` : `src/content/da/strategie-seo-b2b.html`, `public/da/strategie-seo-b2b.css` et `public/da/strategie-seo-b2b.js`.

## Vérification locale

Compilation Next.js et TypeScript réussie dans `/private/tmp/strategy-questionnaire/build`. Test Chromium : champs obligatoires, rejet des adresses invalides, retour avec conservation des réponses, erreur d’envoi suivie d’une nouvelle tentative, contrôle du contenu transmis et confirmation. Aucun envoi réel : requêtes Formspree interceptées. La réception réelle par Formspree reste non testée.

Captures contrôlées à 1440, 390 et 375 pixels, sans débordement horizontal ni erreur JavaScript. Preuves : `/private/tmp/strategy-questionnaire/check.cjs`, `outremer-desktop.png`, `outremer-mobile-390.png` et `outremer-temporalite-375.png`. Aperçu : `http://localhost:5195/strategie-seo-b2b/#pre-audit`. Modification locale, sans publication.

Application des skills `organikk-site` et `ton-de-voix-tim`, avec le vouvoiement demandé par Tim. Références : [[concepts/anti-ai-writing]] et [[entities/organikk]].
