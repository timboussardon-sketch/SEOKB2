# Query Universe : les 9 familles, les amorces, le filtre

## Principe

On génère **par intention, puis on classe**. Jamais l'inverse. Partir des catégories produit des étiquettes de stratégie, pas des requêtes : des libellés que personne ne tape et que personne ne pose.

Chaque requête est écrite deux fois quand les deux formes diffèrent :

- **forme tapée** : ce qu'un humain écrit dans Google, courte, sans verbe ;
- **forme posée** : ce qu'un humain écrit à une IA, une phrase complète avec sa contrainte.

Exemple : `outil prise de notes ia france` et « Quel outil de prise de notes IA est hébergé en France ? ». La seconde peut valoir zéro au Keyword Planner et beaucoup en réponse générée.

## Les 9 familles et leurs amorces

### A. Générique
La catégorie seule, sans contrainte.
```
meilleur [catégorie]
[catégorie] IA
logiciel [problème]
outil [problème]
solution [problème]
top [catégorie]
```
Chemin de citation : mémoire du modèle. Ne se gagne pas par une page.

### B. Problème
Le problème avant la solution. L'acheteur ne connaît pas encore la catégorie.
```
comment [résoudre problème]
outil pour [problème]
automatiser [processus]
réduire [coût / temps / erreur]
remplacer [processus manuel]
arrêter de [tâche pénible]
```

### C. Cas d'usage
Le persona, le secteur, la taille.
```
[catégorie] pour commerciaux
[catégorie] pour RH
[catégorie] pour agences
[catégorie] pour PME
[catégorie] pour grands comptes
[catégorie] pour [secteur régulé]
```

### D. Fonctionnalité
La capacité précise recherchée.
```
outil avec [fonctionnalité]
logiciel permettant [fonctionnalité]
[fonctionnalité] automatique
meilleur outil pour [fonctionnalité]
```

### E. Intégration
L'outil déjà en place dans la pile de l'acheteur.
```
[catégorie] + [CRM]
intégration [outil] [catégorie]
[catégorie] compatible [outil]
connecter [catégorie] à [outil]
```
Chemin de citation : page de l'éditeur. C'est la famille où une page bien faite se fait citer le plus vite, parce que peu de monde documente l'intégration en détail.

### F. Géographique et réglementaire
La contrainte de territoire ou de droit. Souvent sans volume Google, souvent très posée aux IA.
```
meilleur [catégorie] en [pays]
[catégorie] français / européen
[catégorie] conforme [réglementation]
[catégorie] hébergé en [pays]
[catégorie] certifié [norme]
```

### G. Comparatif
Deux noms dans la même requête.
```
[A] vs [B]
[A] ou [B]
différence entre [A] et [B]
```

### H. Alternative
Le remplacement d'un outil en place.
```
alternative à [outil]
meilleure alternative à [outil]
remplacer [outil]
équivalent [outil] en [pays]
```

### I. Transactionnel
Le prix et l'achat.
```
prix [catégorie]
[produit] tarifs
combien coûte [catégorie]
[catégorie] gratuit
[catégorie] pour entreprise
```

### J. Éducatif
Le concept, en amont de tout achat.
```
qu'est-ce qu'un [concept]
comment fonctionne [concept]
avantages [concept]
[concept] vs [concept]
```
Chemin de citation : autorité. Sert l'entité et le maillage, pas la conversion.

## Le filtre de requêtabilité humaine, bloquant

Une requête ne passe que si elle coche les trois :

1. **Un humain la taperait ou la poserait telle quelle.** Test : la lire à voix haute. Si elle sonne comme un intitulé de rubrique, elle est rejetée.
2. **Elle porte une intention identifiable.** On sait ce que la personne veut obtenir en la posant.
3. **Elle n'a pas été fabriquée pour remplir une famille.** Une famille qui n'a que trois requêtes réelles reste à trois.

Rejets typiques : « solution innovante de [catégorie] », « [catégorie] nouvelle génération », « optimiser sa [catégorie] », « [catégorie] pour professionnels exigeants ». Ce sont des étiquettes, pas des requêtes.

## Où trouver les requêtes réelles avant d'en inventer

Par ordre de fiabilité :

1. **Search Console du client** : ce qui génère déjà des impressions, y compris sans clic.
2. **Sources internes** : tickets de support, transcripts de démonstration, questions des rendez-vous commerciaux. C'est là qu'on trouve les mots exacts des acheteurs et leurs objections.
3. **People Also Ask et suggestions** de la catégorie.
4. **Reddit et forums** du secteur : les verbatims donnent la formulation naturelle.
5. **Pages déjà positionnées** sur la catégorie : les questions qu'elles traitent.
6. **Keyword Planner** pour confirmer ou infirmer un volume, jamais pour générer la liste.

Une requête qui ne vient d'aucune de ces six sources est signalée comme inférée dans le livrable.

## Colonnes du fichier `data/queries.csv`

Contrat officiel, celui que lit le dashboard :

```
query,intention,priorite,brand_fit,chemin_citation,type_page,cluster,justification
```

Deux colonnes facultatives que le dashboard ignore mais qui servent à la relecture : `forme_posee` (la phrase complète telle qu'on la pose à une IA) et `source` (d'où vient la requête, parmi les six sources ci-dessus).

`chemin_citation` prend trois valeurs : `recherche_directe`, `memoire_modele`, `page_editeur`. C'est cette colonne qui commande l'action, pas la priorité seule. Une requête en `memoire_modele` ne se traite pas par une page, et il faut le dire au client plutôt que de lui vendre un article.

## Réserve à écrire dans tout livrable

Le Keyword Planner regroupe les requêtes et coupe la longue traîne sous son seuil de report. « Aucune donnée » ne veut pas dire zéro recherche. Seule la Search Console du site tranche. Quand l'accès n'est pas ouvert, l'écrire, avec la date de la demande.
