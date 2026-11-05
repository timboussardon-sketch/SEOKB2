---
type: methode
title: Pré-propale PDF après cold email (rapport neutre, titres et tableaux seulement)
aliases: [rapport pdf neutre, pdf tableaux organikk, pré-propale, pre-propale apres cold email]
tags: [da, pdf, rapport, organikk]
created: 2026-10-29
updated: 2026-10-29
sources: 1
confidence: high
status: stable
---

# Pré-propale PDF après cold email

Format des prochaines pré-propales envoyées à un prospect qui répond « ok » à un cold email (Tim, 2026-10-29 : « commit le format pour les prochains comme une pré propal après cold email »). Premier cas : Maître Pajaud Mendes. Format demandé par Tim le 2026-10-29 pour le rapport de citations GEO de Maître Pajaud Mendes : « document PDF neutre, juste les tableaux et les titres, organikk like ». Gabarit : `gabarit-rapport-pdf-neutre/gabarit.html`, exemple rendu : `~/Code/geo-citations/reports/pajaud/rapport-citations-geo-pajaud-2026-10-29.pdf`.

## Structure
0. **Page 1** (pleine page, sans marge) : fond bleu outremer grainé (dégradé `#1d44d4` → `#3d5af3` + bruit fractal en `overlay`), logo de 34 mm en SVG inline (tracés de `organikk-next/public/da/icons/logo-mark-white.svg`), dégradé blanc → bleu pâle avec grain outremer (filtre `feTurbulence` limité au logo), « organikk.co » dessous en 12 pt espacé. Un `mask` CSS ne passe pas à l'impression Chrome : il rend un carré. **Dernière page**, même fond : « Pourquoi travailler avec nous ? » et trois lignes numérotées (Tim, 2026-10-30 : « tu donnes le nombre de clients, notre approche, plus de dossiers qualifiés, présence sur les IA ») : plus de 100 entreprises accompagnées depuis 2020 (source : page consultant-geo d'organikk.co, `organikk-next/src/content/da/consultant-geo.html`), plus de dossiers qualifiés, présence dans les réponses de ChatGPT, Gemini et Google. Pas de slide « Travaillons ensemble » (retirée par Tim le 2026-10-30). **Page 2** : titre, sous-titre (cabinet · site · date du relevé) et deux paragraphes d'intro donnés par Tim pour le cas Pajaud : ce que le document réunit, puis ce que la stratégie couvre et son objectif commercial. Le contenu commence page 3.
1. **Rapport de citations GEO** : Résultat par question (les questions de l'email envoyé, pas d'autres), Limites du relevé. Pas de tableau Protocole ni de tableau des domaines cités (retirés par Tim le 2026-10-29).
2. **Stratégie GEO complète** : 2.1 familles d'offres, 2.2 mots-clés principaux, 2.3 bibliothèque de questions (un tableau par famille), 2.4 architecture et destinations, 2.5 leviers de contenu (seuls ceux qui ont un tableau : A, B), 2.6 carte des preuves, Mesure des résultats.
3. Une section sans tableau n'a pas de titre vide. Une cellule sans matière reste vide : pas de tiret cadratin, pas de `[MATIÈRE MANQUANTE]` dans le PDF.
4. Chaîne : cold email → réponse → relevé geo-citations sur les questions de l'email (coût annoncé, go de Tim) → matière stratégie fournie par Tim → PDF → Tim voit avant tout envoi. Rien ne part sans lui.

## Format
- A4, marges 16 mm × 14 mm, aucune prose : un titre, un sous-titre d'une ligne, puis des blocs titre H3 + tableau.
- Un bloc titre + tableau ne se coupe pas entre deux pages (`break-inside: avoid`), un titre ne reste jamais seul en bas de page.
- Titres H1/H2/H3 en outremer uni `#1d44d4`. Le dégradé en `background-clip: text` laisse un contour parasite dans le PDF Chrome : ne pas le réutiliser.
- Pas d'eyebrow, pas de barre colorée à gauche.

## DA des tableaux
- Police Geist (`geist.woff2`).
- Fond dégradé blanc vers bleu pâle (`#fff` → `#e9eefc`), bordure `#d3dcf5`, coins arrondis 10 px.
- En-tête `#dfe7fb` → `#eaf0fd`, texte outremer 8,5 pt ; cellules en texte foncé `#10163a` ; valeurs numériques en outremer, chiffres tabulaires.

## Génération
```
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --no-pdf-header-footer --print-to-pdf=rapport.pdf gabarit.html
```
Avant le PDF : `node ~/.claude/skills/redaction-anti-ia/slop.mjs gabarit.html` (règle 3). Lien : [[methodes/modele-contenu-qui-convertit]] pour la ligne éditoriale générale.
