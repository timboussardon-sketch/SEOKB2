# Preuves, entités, autorité tierce, actifs de données

## 1. Proof Map

Une ligne par affirmation importante. Une affirmation est importante si elle intervient dans une décision d'achat ou si elle est reprise dans plusieurs pages.

| Affirmation | Source | Type | Confiance |
|---|---|---|---|
| Intégration avec [outil] | documentation produit | première main | haute |
| [X] % de précision de transcription | étude interne | première main | moyenne |
| Utilisé par [client] | étude de cas signée | première main | haute |
| Meilleur que [outil] sur [critère] | test indépendant | tierce partie | haute |

**Première main** : documentation, données internes, études propriétaires, études de cas, statistiques maison.

**Tierce partie** : presse, G2, Capterra, Reddit, blogs, analystes, tests indépendants.

Trois niveaux de confiance :

- **Haute** : la source est publique, datée, vérifiable par un lecteur.
- **Moyenne** : la source existe mais elle est interne, non publiée, ou non reproductible.
- **Basse** : la source est déclarative, ancienne, ou impossible à retrouver.

Une affirmation à confiance basse ne se publie pas telle quelle.

## 2. Proof Gap Analysis

```
Affirmation :
Preuve actuelle :
Risque :
Recommandation :
```

Deux exemples de lecture :

```
Affirmation : « le produit est le plus précis du marché »
Preuve actuelle : aucune source indépendante
Risque : élevé
Recommandation : retirer l'affirmation, ou produire un benchmark reproductible avec méthode publiée
```

```
Affirmation : « conforme au RGPD »
Preuve actuelle : une page légale
Risque : moyen
Recommandation : publier l'hébergement, le DPA, les mesures de sécurité, les durées de conservation et la liste des sous-traitants
```

Le niveau de risque commande l'action :

- **élevé** : l'affirmation sort de la page tant que la preuve n'existe pas ;
- **moyen** : l'affirmation reste mais elle est complétée par les éléments vérifiables qui la soutiennent ;
- **faible** : l'affirmation reste, la preuve est planifiée.

## 3. Graphe d'entités

```
MARQUE
 ├── PRODUIT
 ├── CATÉGORIE
 ├── FONCTIONNALITÉS
 ├── CAS D'USAGE
 ├── SECTEURS
 ├── PERSONAS
 ├── INTÉGRATIONS
 ├── ACTEURS DU MARCHÉ
 ├── ALTERNATIVES
 ├── CLIENTS
 └── PREUVES
```

Une page utile renforce plusieurs relations d'un coup. Exemple de chaîne : marque, catégorie, cas d'usage commercial, CRM, intégration nommée, transcription, compte rendu.

### Contrôle de cohérence externe, à faire avant toute production

1. Relever ce que disent déjà les sources tierces sur les faits d'entité : statut juridique, pays, hébergement, certifications, langues, tarifs.
2. Comparer avec ce que dit le site.
3. Lister les contradictions.

Une contradiction sur un fait qui décide l'achat est le premier chantier, avant toute nouvelle page. Tant qu'elle tient, une réponse générée qui recoupe les sources n'a pas de fait stable à restituer, et elle écarte l'entité ou reste évasive.

Ordre de correction : le site d'abord, puis les fiches détenues par la marque, puis les pages tierces par demande de correction factuelle avec pièce à l'appui.

Formulation : un fait, une seule formulation, répétée à l'identique partout. Deux faits voisins qui se disent ensemble ne se fusionnent jamais en un seul raccourci.

## 4. Plan d'autorité tierce

```
CIBLE
Pourquoi elle est pertinente :
Sujet :
Preuve à fournir :
Angle de contenu :
Prise de contact :
```

Familles de cibles à balayer : médias du secteur, comparateurs et annuaires, communautés, podcasts, newsletters, experts reconnus, associations professionnelles, partenaires technologiques, clients, analystes.

Priorité de départ : les fiches déjà détenues par la marque et qui portent un fait faux ou incomplet. Les corriger coûte une demande et rapporte une source cohérente de plus.

Interdits : faux avis, avis sollicités contre contrepartie non déclarée, achat de liens, contenu placé sans mention de son origine, citations fabriquées.

## 5. Actifs de données

```
ACTIF DE DONNÉES
Nom :
Question à laquelle il répond :
Jeu de données :
Méthodologie :
Échantillon :
Fréquence de mise à jour :
Graphiques :
Téléchargement :
Commentaire d'expert :
Angle presse :
Citations potentielles :
```

Formes possibles : benchmark, étude annuelle, jeu de données, index, rapport, statistiques anonymisées, enquête, calculateur, observatoire.

Trois conditions pour qu'un actif se fasse citer :

- il répond à une question que personne d'autre ne chiffre ;
- sa méthode est publiée et reproductible ;
- son échantillon est décrit, avec ses limites.

Un actif sans méthode publiée n'est pas une étude, c'est une affirmation avec un graphique.

Sur une donnée client, vérifier l'autorisation et l'anonymisation avant toute publication.
