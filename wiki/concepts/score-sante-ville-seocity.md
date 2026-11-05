---
type: concept
title: "Score de santé d'une ville (méthode SEO City)"
aliases: [score-sante-seocity, score-sante-ville, note-sante-ville]
tags: [seo, gsc, seocity, mesure, score, data-proprietaire]
created: 2026-08-31
updated: 2026-08-31
sources: 1
confidence: high
status: draft
---

# Score de santé d'une ville (méthode SEO City)

Note la santé d'un site sur cinq dimensions, appliquées à l'identique à une page, un quartier ou au site entier. Code source : `~/Code/gsc-simcity/build.js`, fonctions `signal`, `depuisVar`, `volatilite`, `noteSante`.

À ne pas confondre avec [[concepts/score-sante-site]] (méthode Organikk, 4 dimensions Rendement/Concentration/Renouvellement/Tenue, percentile sur un corpus de 17 sites) : deux outils différents, deux formules différentes, malgré le nom proche.

## 1. La comparaison de base

Deux fenêtres de 28 jours adjacentes, jamais chevauchantes : la fenêtre actuelle contre les 28 jours qui la précèdent immédiatement.

Trois seuils minimaux d'impressions sur la fenêtre précédente, en dessous desquels la dimension concernée n'est pas notée (retour à 50, neutre) :

| Périmètre | Seuil |
|---|---|
| page | 12 impressions |
| quartier | 30 impressions |
| site | 80 impressions |

## 2. Le signal brut

```
signal(actuel, precedent, seuil):
  si precedent.impressions < seuil : renvoie { impr: null, clics: null, pos: null }
  impr  = (actuel.impressions - precedent.impressions) / precedent.impressions
  clics = (actuel.clics - precedent.clics) / precedent.clics, seulement si precedent.clics >= 3, sinon null
  pos   = precedent.position - actuel.position, seulement si les deux positions sont connues (positif = amélioration)
```

## 3. Les cinq dimensions

```
depuisVar(v) = si v est null : 50, sinon borne(0, 100, 50 + v * 50)

visibilite  = depuisVar(impr)
acquisition = depuisVar(clics)
performance = si pos est null : 50, sinon borne(0, 100, 50 + pos * 6)
stabilite   = si volatilite est null : 50, sinon borne(0, 100, 100 - volatilite * 55)
expansion   = borne(0, 100, 50 + nb_pages_apparues_28j * 15)
```

Deux choix documentés dans le code :
- **Performance** : le ×6 rend l'échelle volontairement large. Une position moyenne qui se dégrade parce que beaucoup de nouvelles pages démarrent bas ne doit pas coûter aussi cher qu'un vrai décrochage.
- **Expansion** : zéro page neuve donne 50, un score neutre. Ne pas publier n'est pas en soi un signal négatif.

## 4. La volatilité (sert à Stabilité)

```
volatilite(serie_quotidienne_impressions_28j):
  si moins de 4 points, ou moyenne <= 0 : renvoie null
  moyenne = moyenne de la série
  saut = somme des |valeur du jour - valeur de la veille| sur toute la série
  renvoie (saut / (n - 1)) / moyenne
```

Ce n'est pas un écart-type classique : un écart-type pénaliserait une croissance régulière, qui est l'inverse de l'instabilité. On mesure le saut moyen d'un jour à l'autre, rapporté au niveau moyen.

## 5. Le score global

```
base  = visibilite*0,35 + acquisition*0,30 + performance*0,15 + stabilite*0,10 + expansion*0,10
score = round(base * (1 - part_pages_en_declin * 0,45))
```

`part_pages_en_declin` = proportion des pages vivantes dont l'état du jour est déclin. Pénalité jusqu'à 45 % si toutes les pages sont en déclin, pour qu'un bon score d'Expansion ne masque pas un quartier qui s'éteint.

## 6. L'étiquette affichée

| Score | Étiquette |
|---|---|
| aucune page vivante | pas de note |
| >= 65 | croissance |
| >= 50 | stable |
| >= 35 | surveillance |
| < 35 | déclin |

## 7. Une seule formule, trois échelles

Le calcul est strictement identique pour une page, un quartier et le site. Seule la source des chiffres change : page et quartier agrègent les pages du périmètre ; le site utilise l'agrégat brut quotidien fourni par Search Console (`serieSite`/`fenSite` dans le code), pas une moyenne des quartiers. Le score du site n'est donc pas la moyenne des scores de ses quartiers.

## Le plafond, un effet du coefficient, recalibré le 2026-08-31

`depuisVar` a longtemps atteint 100 dès que `v = 0,5`, c'est-à-dire dès qu'une variation de clics ou d'impressions atteignait +50 % sur la fenêtre (`50 + 0,5 * 100 = 100`). Une conséquence mathématique directe du coefficient ×100, jamais un seuil métier documenté comme tel dans le code (contrairement au ×6 de Performance ou au 50 neutre d'Expansion, commentés explicitement).

Observé sur organikk.co le 2026-08-31 : 20 clics puis 30 clics sur deux fenêtres de 28 jours consécutives, soit +50 %, suffisaient à afficher Acquisition = 100/100, quel que soit le volume réel. Le plafond saturait aussi vite pour un site à faible trafic que pour un gros site.

**Recalibré le même jour** : le coefficient passe de ×100 à ×50. Il faut désormais un doublement complet (+100 %) pour saturer une dimension à 100, et symétriquement une perte totale des clics ou impressions (−100 %) pour tomber à 0. Effet mesuré sur organikk.co (mêmes données, jour du 2026-08-27) : Acquisition passe de 100 à 69, le score global du site de 50 (« stable ») à 41 (« surveillance »). Le changement rend les scores globalement plus conservateurs pour tous les sites, pas seulement ceux à faible volume : un ancien score de 50 stable peut désormais tomber en surveillance sur la même donnée.

Pages liées : [[concepts/score-sante-site]] (l'autre score de santé, méthode Organikk, percentile sur corpus) · [[entities/gsc]] · [[concepts/data-proprietaire]]
