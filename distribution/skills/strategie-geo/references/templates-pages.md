# Gabarits de pages par module

Règle commune aux cinq modules : la réponse à la question du titre apparaît dans les 40 à 80 premiers mots. Pas d'introduction, pas de rappel du sujet, pas de mise en contexte.

Deuxième règle commune : chaque section qui contient un fait porte sa source ou son marqueur (`[À VÉRIFIER]`, `[À PRODUIRE]`, `[NON VÉRIFIÉ]`).

---

## 1. Page Question / Réponse

```
H1 : [la question, écrite comme elle est posée]

Réponse directe
[40 à 80 mots. La réponse complète. Elle doit tenir seule, hors de la page.]

Les faits
- fait vérifiable, avec sa source
- fait vérifiable, avec sa source
- fait vérifiable, avec sa source

Comment ça fonctionne
[le mécanisme, pas le bénéfice]

Ce que ça couvre
[fonctionnalités ou périmètre concernés]

Exemples
[cas réels, nommés quand c'est autorisé]

Limites
[ce que ça ne fait pas, ou pas encore]

Alternatives
[les autres façons de résoudre le même problème, y compris sans l'outil]

FAQ
[5 à 7 questions, produites avec seo-faq-query, balisées FAQPage]

Sources
[liste datée]
```

Signaux à ne pas oublier : auteur, date de mise à jour, liens internes vers le pilier du cluster.

---

## 2. Page cas d'usage

```
H1 : [Produit] pour [persona ou secteur]

En bref
[40 à 80 mots : à qui, pour quoi, quel résultat]

Pour qui
[le persona précis, sa taille d'entreprise, son rôle dans la décision]

Le problème
[formulé avec les mots du persona, pas ceux du produit]

Comment ça se passe
1.
2.
3.
4.

Les fonctionnalités mobilisées
[celles qui servent vraiment ce cas, pas la liste complète]

Le résultat attendu
[mécanisme du gain, pas une promesse de chiffre non prouvée]

Exemple
[déroulé concret]

Preuve client
[étude de cas, verbatim, métrique, ou marqueur si absent]

Limites
[dans quels cas ce déroulé ne marche pas]

FAQ
```

Sans la section preuve, la page est une promesse. Une promesse ne se fait pas citer.

---

## 3. Page comparatif

```
H1 : [Produit A] vs [Produit B]

Réponse rapide
[40 à 80 mots : dans quel cas chacun est le bon choix]

[Produit A] est le meilleur choix quand
[Produit B] est le meilleur choix quand

Tableau de comparaison
Critère | A | B
Prix |
Langues |
Intégrations |
Sécurité et conformité |
Fonctions IA |
Support |
[autres critères propres au secteur]

Forces et limites
A : forces / limites
B : forces / limites

Qui devrait choisir A
Qui devrait choisir B

Verdict
```

Règles dures du module :

- chaque ligne du tableau est vérifiée sur la page officielle de l'éditeur concerné, à une date écrite dans la page ;
- si l'autre outil est meilleur sur un critère, c'est écrit noir sur blanc ;
- aucun avantage inventé pour la marque, aucune faiblesse exagérée chez l'autre ;
- ton posé, jamais accusateur, jamais de mise en scène de rivalité.

Déléguer la rédaction à `comparatif-neutre` quand le skill est disponible.

---

## 4. Page alternative

```
H1 : Les alternatives à [outil du marché]

Réponse rapide
[40 à 80 mots]

Pourquoi chercher une alternative
[les raisons réelles, tirées des verbatims, pas supposées]

Ce que les utilisateurs cherchent en général
[les critères de bascule, listés]

Les alternatives
1. Alternative A
2. Alternative B
3. [La marque]

Tableau comparatif

La meilleure alternative selon le besoin
[par critère : prix, conformité, langue, intégration]

Pourquoi choisir [la marque]

Dans quels cas [la marque] n'est pas le bon choix
[section obligatoire]

FAQ
```

La dernière section est ce qui rend la page reprenable. Une page qui ne dit jamais non se lit comme une page de vente et se cite moins.

---

## 5. Page intégration

```
H1 : [Produit] + [Outil intégré]

Réponse courte
[40 à 80 mots : ce que fait l'intégration]

Ce que l'intégration permet d'automatiser
- 
- 
- 

Comment ça marche
1.
2.
3.
4.

Cas d'usage
[deux ou trois situations concrètes]

Circulation des données
[quelle donnée part d'où, va où, dans quel sens, à quelle fréquence]

Sécurité
[droits demandés, périmètre d'accès, lieu de traitement]

Limites
[ce qui ne se synchronise pas, ce qui est à sens unique]

FAQ
Est-ce que ça supporte [X] ?
Est-ce que ça synchronise [Y] ?
Est-ce que ça automatise [Z] ?
```

Chaque intégration est une entité informationnelle autonome, avec sa propre URL, sa propre FAQ et ses propres liens. Jamais une ligne dans une page « intégrations » générique.

Une intégration ne se publie que si elle existe. Une intégration prévue se marque `[À PRODUIRE]` dans la roadmap, elle ne devient pas une page.
