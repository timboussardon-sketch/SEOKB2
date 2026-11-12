# Mesure business et panel — contrat commun

Pour les nouvelles missions, `wiki/methodes/opportunites-business.md` et son calculateur fixent les définitions opérationnelles. Les barèmes de contenu ci-dessous ne sont jamais des scores de priorité business. Une citation indique une URL présente dans la réponse, pas la lecture complète de la page ni une vente.

Taux de mention/citation/recommandation : réponses positives divisées par réponses valides évaluées pour ce critère, par question et moteur. Inconnues, erreurs et runs manquants restent visibles. Part de voix : paires marque-réponse / paires acteur-réponse pour les acteurs suivis, sur les réponses où tous ont été évalués. Toujours indiquer période, panel, moteur, mode, répétitions, source et dénominateur ; jamais « part de marché ». Les formules sont celles du résultat commun, pas un compte de lignes CSV agrégées.

La demande Google, les questions clients et les observations IA restent séparées. Trente relevés est une règle de collecte existante, pas une preuve statistique de représentativité. Sous ce protocole, afficher la limite. Aucun passage visibilité → trafic → revenu sans données documentées. Les commandes payantes gardent leur validation de coût.

# Barèmes et mesure

## 1. Content Engineering Score, sur 100

Une page se note avant publication. Sous 70, elle ne se publie pas.

| Critère | Points | Ce qu'on note |
|---|---|---|
| Intent Match | 20 | la page répond-elle vraiment à la requête visée, et à elle seule |
| Information Quality | 15 | les informations sont-elles exactes, précises, à jour |
| Extraction Clarity | 15 | un moteur peut-il isoler la réponse sans lire la page entière |
| Evidence | 15 | les affirmations importantes sont-elles sourcées |
| Entity Coverage | 10 | la page renforce-t-elle des relations du graphe d'entités |
| Differentiation | 10 | apporte-t-elle une information que les autres pages du sujet n'ont pas |
| Internal Connectivity | 5 | est-elle reliée au pilier et aux pages voisines du cluster |
| Freshness | 5 | porte-t-elle une date de mise à jour, et est-elle tenue |
| Third-party potential | 5 | une autre source aurait-elle une raison de la citer |

Lecture des notes basses :

- Intent Match sous 12 : la page traite un sujet, pas une question. À reprendre au plan.
- Extraction Clarity sous 9 : la réponse est noyée. Remonter la réponse directe en tête.
- Evidence sous 9 : la page affirme. Passer par la Proof Gap Analysis avant publication.
- Differentiation sous 5 : n'importe quel moteur aurait pu écrire cette page. Elle n'a pas de raison d'exister.

Pour une notation fine sur les signaux de citation, passer la page à `seo-geo-audit`.

## 2. Contrôle de cannibalisation

Quatre signaux de recouvrement à croiser : intention identique, entités identiques, formulation proche, requêtes qui se chevauchent.

| Décision | Quand |
|---|---|
| GARDER | les intentions sont distinctes, le recouvrement est de surface |
| FUSIONNER | deux pages répondent à la même question, aucune n'est complète |
| REDIRIGER | une page est redondante et l'autre est meilleure sur tous les plans |
| REPOSITIONNER | la page a une valeur propre mais vise la mauvaise requête |
| SUPPRIMER | la page n'a ni requête, ni preuve, ni lien entrant |

Une suppression se fait par redirection 301 vers la page la plus proche. Jamais de 410.

Analyse détaillée : `seo-cannibalisation`.

## 3. AI Visibility, les sept mesures

Jamais présentées sous forme d'un score unique. Chacune répond à une question différente.

| Mesure | Définition | Ce qu'elle dit |
|---|---|---|
| Taux de mention | part des réponses où le nom apparaît | est-ce que l'entité existe pour le moteur |
| Taux de citation | part des réponses où le domaine est cité en source | est-ce que les pages sont lues et reprises |
| Taux de recommandation | part des réponses où l'entité est proposée comme solution | est-ce que le moteur la conseille, pas seulement la nomme |
| Position moyenne | rang du nom dans la liste proposée | est-ce qu'elle est premier choix ou mention de fin |
| Part de voix | part des noms cités qui est la marque, sur l'ensemble des noms | quelle place elle occupe dans la catégorie |
| Diversité des sources | nombre de domaines distincts cités par réponse | est-ce que la réponse s'appuie sur un écosystème ou sur une seule page |
| Taux de citation tierce | part des citations qui viennent d'un autre domaine que le site | est-ce que l'autorité est gagnée ou seulement déclarée |

## 4. Le relevé par requête

C'est la forme que le client lit. Un bloc par requête, par moteur, par date.

```
Requête : "meilleur outil de [catégorie] en [pays]"
Moteur : 
Date : 
Marque mentionnée : oui / non
Recommandée : oui / non
Citée en source : oui / non
Position dans la réponse : #
Sources citées : 
Noms cités à la place : 
```

Deux règles de mesure :

- **Minimum 30 relevés par requête et par moteur.** La variance d'une réponse générée à l'autre est forte. En dessous de 30, l'écrire explicitement : ce n'est pas un échantillon crédible.
- **Aucun chiffre de visibilité sans relevé réel.** Sans relevé, le livrable décrit le protocole et laisse les cases vides. Il n'estime pas.

L'outil de relevé est `geo-citations`. Chaque relevé coûte des appels payants : annoncer le calcul (requêtes × moteurs × runs) et attendre la validation avant de lancer.

## 5. Citation Engineering, la boucle d'action

La sortie la plus utile d'un relevé n'est pas le score, c'est la colonne « noms cités à la place » et « sources citées ».

```
Requête
 ↓ réponse actuelle
 ↓ noms cités
 ↓ sources citées
 ↓ pourquoi ces sources ont été citées (format, fraîcheur, preuve, autorité)
 ↓ manque de contenu ou manque de preuve
 ↓ action : page, preuve, ou prise de contact tierce
```

La liste des domaines cités à la place de la marque devient directement la liste de cibles du plan d'autorité tierce.

## 6. Cadence

| Moment | Ce qu'on fait |
|---|---|
| Avant production | ligne de base sur les requêtes P1 et un échantillon P2 |
| Jour 30 | premier relevé de contrôle, uniquement sur ce qui a été publié |
| Jour 90 | relevé complet, comparaison à la ligne de base, arbitrage |
| Ensuite | trimestriel, plus un relevé ponctuel après chaque publication majeure |

Sans ligne de base, aucun relevé ultérieur n'est interprétable. C'est la première dépense à engager, avant la première page.
