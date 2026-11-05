---
type: query
title: "Simulateur de marge issue des leads SEO pour la page Consultant SEO Lyon"
aliases: [simulateur-leads-seo-lyon]
tags: [organikk, lyon, product-led-seo, simulateur, leads, marge]
created: 2026-10-10
updated: 2026-10-10
sources: 5
confidence: high
status: draft
statut_decision: PROPOSITION
skill: seo-product-led-seo
---

# Simulateur de marge issue des leads SEO

Outil à intégrer dans la page `/consultant-seo-geo-lyon/` sous le H2 « Simulateur : combien de marge peuvent générer vos leads SEO ? ». Tim a fixé le calcul : **trafic qualifié × taux de conversion × taux de transformation commerciale × marge**. Le résultat est une simulation à partir des hypothèses du visiteur, jamais une prévision de résultats Organikk. [[briefs/2026-10-10-consultant-seo-lyon-structure-hn]] · [[moc/doctrine-seo-reference]]

## Intention et choix du format

Le visiteur veut chiffrer la valeur d'une demande qualifiée avant d'appeler un consultant. La méthode de Tim demande de définir la qualification du lead et de relier les pages aux opportunités commerciales lorsque les données existent. Le simulateur rend cette chaîne visible : visites qualifiées, demandes qualifiées, clients signés, marge estimée. Il prolonge les questions de cadrage « combien de leads ? » et « quel objectif chiffré ? ». [[raw/organikk/_MODELE-discours-commercial]] · [[raw/notes/process-seo-b2b-2026]]

| Concept examiné | Réponse à l'intention | Données nécessaires | Décision de brief |
|---|---|---|---|
| Calculateur de marge des leads | Traduire quatre hypothèses commerciales en demandes, ventes et marge | Chiffres fournis par le visiteur | Retenu ; calcul déterministe réalisable dans la page |
| Estimation de trafic Google par mot-clé | Annoncer un trafic futur | SERP et projections fiables absentes | Écarté ; donnerait une précision fictive |
| Calculateur de CAC SEO | Comparer coût et clients signés | Coût complet et durée d'acquisition | Extension possible après le devis |
| Prévision de chiffre d'affaires à 90 jours | Projeter des ventes | Saisonnalité, capacité commerciale, historique | Écarté ; formule trop pauvre pour prédire les ventes |
| Générateur de roadmap personnalisée | Transformer les entrées en plan d'action | Audit réel du site et de l'offre | À réserver au diagnostic, distinct de la roadmap publique |

Le content gap observé dans le brief est la différence entre « nous générons des leads » et un raisonnement économique que le lecteur peut contester ou modifier. Le Surprise Gap tient à la sensibilité du résultat : améliorer le taux de signature peut avoir autant de poids que gagner du trafic. C'est une propriété arithmétique de la formule, pas une preuve qu'Organikk obtiendra ces gains. [[briefs/2026-10-10-consultant-seo-lyon-structure-hn]] · [[concepts/surprise-gap]]

## Entrées, calcul et résultats

| Entrée modifiable | Définition visible sous le champ | Contrôle |
|---|---|---|
| Visites qualifiées sur 90 jours | Visites arrivant sur des pages liées à l'offre et à une intention d'achat ; estimation saisie par le visiteur, non l'ensemble des clics du site | Entier ≥ 0 ; laisser vide au départ |
| Taux de conversion en demande qualifiée | Pourcentage de ces visites qui deviennent une demande répondant aux critères commerciaux du visiteur | 0 à 100 % ; laisser vide au départ |
| Taux de transformation commerciale | Pourcentage de ces demandes qui signent effectivement | 0 à 100 % ; laisser vide au départ |
| Marge moyenne par client | Contribution en euros d'un client signé sur la période choisie, après coûts variables ; ce n'est ni le panier moyen ni un taux de marge | Montant en € ≥ 0 ; laisser vide au départ |

Calcul à afficher en clair sous les champs :

```text
Demandes qualifiées = visites qualifiées × (taux de conversion / 100)
Clients signés = demandes qualifiées × (taux de transformation / 100)
Marge estimée = clients signés × marge moyenne par client en €
```

Le résultat affiche les trois valeurs. Conserver les décimales internes et arrondir seulement à l'affichage ; indiquer « moyenne attendue » pour un nombre de clients non entier. Mettre à jour les résultats à chaque modification, sans compte ni adresse e-mail. Une option « exemple fictif » peut remplir 300 visites, 4 %, 25 % et 2 000 € : 12 demandes, 3 clients, 6 000 € de marge. L'exemple est un contrôle du calcul, sans ancrage dans un cas client ni promesse de performance. Un bouton rétablit les champs vides. [[moc/doctrine-seo-reference]]

La période des quatre entrées doit être identique : ici **90 jours**. Si le client ne connaît que ses valeurs mensuelles, lui proposer d'entrer trois mois de trafic cumulé, sans supposer que chaque mois sera stable. Si « marge » veut dire pour lui taux de marge en %, ajouter en amont un panier moyen modifiable et calculer la marge par client ; ne jamais multiplier directement par un pourcentage sans montant de vente.

**Sortie complémentaire optionnelle.** Un coût de mission modifiable peut afficher `marge estimée − coût saisi`. Ce résultat s'intitule « différence illustrative », pas ROI : il manque le temps interne, les coûts techniques, le délai de conversion et la part réellement attribuable au SEO. La FAQ budget de 1 500 à 3 500 € reste sans unité confirmée ; ne pas préremplir ce coût avec cette fourchette. [[briefs/2026-10-10-consultant-seo-lyon-structure-hn]]

## Garde-fous et conversion

Les champs n'utilisent aucune donnée réelle automatiquement. L'outil ne sait pas si les visites futures arriveront, si les demandes seront qualifiées, ni quelle part de la vente revient au SEO. Un libellé permanent dit « Simulation fondée sur vos hypothèses ; aucun résultat garanti ». La page doit expliquer où récupérer les chiffres réels : GSC pour les requêtes et pages, analytics pour les visites et demandes, CRM pour qualification et ventes. GSC ne donne pas à elle seule le nombre de visites qualifiées ou de clients signés. [[prestation/roadmap]] · [[moc/doctrine-seo-reference]]

Le résultat complet reste visible. Le CTA suivant propose un diagnostic pour remplacer les hypothèses par les données du site et une roadmap adaptée. L'envoi du scénario par e-mail peut être proposé, avec consentement explicite, mais ne bloque pas le calcul. Aucun chiffre de résultat n'est présenté comme un cas client. [[concepts/anti-ai-writing]]

## Faisabilité et vérification

Calcul côté navigateur : quatre champs numériques, fonctions pures, zéro API ou donnée personnelle requise. Vérifier les cas `0`, champ vide, pourcentage > 100, valeur négative, forte marge et affichage mobile. Le format de nombres suit le français (`300`, `4 %`, `2 000 €`). Tester que l'exemple fictif retourne 12 demandes, 3 clients et 6 000 € ; tester qu'une conversion à 0 % retourne zéro sur les trois sorties. L'outil ne doit pas transformer les projections en données structurées ou en témoignage client.

Pages liées : [[briefs/2026-10-10-consultant-seo-lyon-structure-hn]] · [[briefs/annexes/2026-10-10-consultant-seo-lyon-matiere-par-hn]] · [[concepts/product-led-seo]] · [[moc/doctrine-seo-reference]]
