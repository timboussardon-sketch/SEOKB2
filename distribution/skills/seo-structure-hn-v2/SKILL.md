---
name: seo-structure-hn-v2
description: "Structure Hn d'une page à créer : modèle réutilisable et progression. « structure Hn », « plan de page », « quels H2 mettre »."
---

# Skill — Structure Hn V2

## Quand utiliser ce skill

Structure de contenu à la création : 3 patterns. (1) modèle Hn réutilisable (H1 besoin, H2 question utile pour décider, H3 étape / critère / cas) et pattern interne à chaque section (réponse directe, preuve, détails utiles, limite). (3) progression mini-formation pour articles et newsletters de méthode (promesse, besoin, méthode, exemple, offre, répétition). Sert pour les pages outil / logiciel / solution / service, les articles et les newsletters. Chaque section n'existe que si la matière source permet de la démontrer : sinon elle est supprimée ou marquée [MATIÈRE MANQUANTE].

TOUJOURS utiliser ce skill quand l'utilisateur dit : "structure Hn v2", "plan de page", "quels H2 mettre", "structure de la page", "structure de la newsletter", "structure de l'article", ou avant tout brief / rédaction de page, article ou newsletter.

Remplace la logique de structure de seo-structure-hn (qui reste le skill d'AUDIT Hn d'un site existant) et s'insère dans seo-brief-contenu, seo-workflow-article. Ne dispense pas de ton-de-voix ni de redaction-anti-ia.

Version du 2026-10-07. Blocs à adapter, pas des cases à remplir.

## Règle de tête

Une section n'existe que si on peut la démontrer avec la matière source. Pas de matière : on supprime la section, ou on écrit `[MATIÈRE MANQUANTE]` dans le brief (jamais dans un livrable client). Test : « d'où vient cette phrase ? ».

Moins de sections génériques, plus de réponses précises démontrables.

## Rôles

- **H1** : identifie le besoin. `[Catégorie de solution] pour [besoin principal]`.
- **H2** : une question utile pour décider. Question de départ : « de quelle information le lecteur a-t-il besoin pour savoir si cette solution lui convient ? ».
- **H3** : précise une étape, un critère ou un cas.
- **Sous le titre** : réponse directe + preuve vérifiable + conditions.

Les Hn organisent la réponse. Ils ne remplacent pas son contenu.

## Pattern 1 : modèle Hn (pages outil / logiciel / solution / service)

```
H1 — [Catégorie de solution] pour [besoin principal]

INTRODUCTION
Problème concret du lecteur.
Réponse immédiate au besoin.
[Solution] est [catégorie] qui permet de [fonction précise].
Une preuve pertinente, si disponible.

H2 — Dans quels cas utiliser [solution] ?
  H3 — Pour [besoin concret / profil 1]
  H3 — Pour [besoin concret / profil 2]
  H3 — Quand une autre solution est plus adaptée

H2 — Comment [obtenir le résultat recherché] avec [solution] ?
  H3 — [Première étape concrète]
  H3 — [Deuxième étape concrète]
  H3 — [Résultat obtenu et utilisation]

H2 — [Question sur le principal critère de choix]
  H3 — [Ce qui est possible et dans quelles conditions]
  H3 — [Restrictions ou limites à connaître]

H2 — Quels résultats avons-nous observés sur [usage précis] ?
  H3 — [Méthode et conditions du test]
  H3 — [Résultats mesurés et limites observées]

H2 — [Solution] ou [alternatives] : quelles différences ?
  Tableau comparatif sur les mêmes critères.
  Sources, offres concernées et date de vérification.

H2 — Combien coûte [solution] et que comprend le prix ?
  Prix, unité de facturation, engagement et restrictions.

H2 — Questions pratiques sur [sujet]
  H3 — [Question importante non traitée dans la page]
  H3 — [Objection restante]
  H3 — [Cas particulier pertinent]
```

Adaptations :
- Sans test réel, remplacer « résultats » par une démonstration documentée.
- Sans question supplémentaire utile, supprimer la FAQ. Si elle reste : skill `seo-faq-query`.
- Page pédagogique : ajouter « Qu'est-ce que [sujet] ? » et remonter le fonctionnement.
- Recherche d'outil : donner d'abord les informations permettant de choisir.

## Pattern 2 : à l'intérieur de chaque section

```
H2 — Une question précise du lecteur

RÉPONSE DIRECTE
Quelques phrases. Nommer la solution ou le sujet.
Préciser les conditions importantes.

PREUVE
Résultat mesuré, exemple réel, démonstration ou source vérifiable.

DÉTAILS UTILES
Uniquement ce qui aide à comprendre ou décider.
H3 si plusieurs sous-questions le justifient.

LIMITE
Ce qui n'est pas couvert, ce qui dépend de l'offre,
ce qui nécessite une vérification humaine.
```

- Pas de cible de 50 mots : assez court pour être compris vite, assez complet pour ne pas tromper hors contexte.
- Jamais « Oui, cette fonctionnalité est disponible ». Écrire : `[Solution] permet de [fonction précise] sur [plateformes]. Incluse dans [offre], avec [restriction].`
- Les crochets sont des informations à vérifier, pas des formulations à publier.
- PREUVE ou LIMITE sans matière : la ligne saute, elle n'est pas inventée.

## Choisir les H2

| Titre vague | Titre à privilégier |
|---|---|
| Une précision exceptionnelle | Quelle est la précision de la transcription en français ? |
| Une solution flexible | Peut-on transcrire une réunion en présentiel ? |
| Des intégrations puissantes | Avec quels outils peut-on partager la transcription ? |
| La sécurité au cœur de notre solution | Où sont stockés les enregistrements et qui peut y accéder ? |
| Une offre adaptée à tous | Combien coûte la transcription et quelles sont les limites de l'offre ? |

Un H2 n'a pas à être une question : « Tarifs et limites des offres » vaut « Combien coûte la solution ? ». Prendre la formulation la plus naturelle, sans répéter le mot-clé artificiellement.

## Ce qui donne une raison de citer une section

Une définition générique explique le sujet. Un test, une donnée originale ou un exemple documenté apporte une information propre à la page.

Exemple de section à test (à publier uniquement avec des tests réellement réalisés) :

```
H2 — Quelle est la précision de la transcription en français ?
  Réponse fondée sur les observations disponibles.
  H3 — Comment nous avons testé la transcription
      Enregistrements, durée, langue, conditions, méthode.
  H3 — Quels types d'erreurs avons-nous observés ?
      Noms propres, vocabulaire métier, accents, prises de parole simultanées.
```

## Pattern 3 : articles et newsletters en méthode (mini-formation)

Pour tout contenu qui enseigne une méthode (article, newsletter longue, thread). Les patterns 1 et 2 règlent les pages ; celui-ci règle la progression.

Le contenu emmène le lecteur jusqu'à un premier résultat utilisable. Progression : une promesse forte → un besoin qui revient → une méthode concrète → un premier exemple → une offre → la répétition.

Chaque grande section répond à une question : pourquoi quelqu'un paierait, quoi préparer, comment produire, comment vérifier, comment vendre.

**Règle centrale : chaque section produit un résultat que le lecteur a entre les mains** (une bibliothèque, une fiche, un livrable, un message à envoyer). Section sans résultat à la clé = à retravailler ou à supprimer.

### Les 9 patterns à reprendre

| Pattern | À reprendre |
|---|---|
| Grande promesse, point de départ accessible | Résultat désirable, périmètre assez précis pour se lancer |
| Problème récurrent qui justifie l'offre | Pourquoi le problème revient, ce que le système prend en charge dans la durée |
| Fonctionnement résumé avant les détails | Toute la méthode en une phrase, avant les outils |
| Recherche qui produit du réutilisable | Ce qu'on collecte, ce qu'on observe, ce qu'on en tire. Séparer l'observation de l'interprétation |
| Base stable qui relie les étapes | Une mémoire, une procédure, une bibliothèque : ce que le lecteur garde après son premier essai |
| Règles pour juger le travail | Critères concrets pour accepter, corriger ou écarter un résultat |
| Erreurs expliquées au moment où elles arrivent | Par grande étape : l'erreur fréquente et le moyen de la repérer |
| Exemple concret relié à la vente | Premier livrable + comment le présenter au destinataire |
| Fin = ce qui devient réutilisable | Reproduire la méthode une fois le premier cas validé, avec les adaptations |

### Template (à adapter, crochets = matière à fournir)

```
H1 — Comment [obtenir un résultat concret] avec [un système précis] : la méthode complète

INTRO
Tu [problème vécu]. À chaque [moment où il revient], tu dois [travail à recommencer].
Je vais te montrer comment construire [système] pour [résultat], de [point de départ] à [livrable final].
Le besoin : [cible] doit régulièrement [tâche]. Aujourd'hui, [difficulté] lui coûte [conséquence réelle].
Plan en liste : comprendre le besoin, récupérer les informations, construire la base réutilisable,
produire et vérifier le premier résultat, le montrer au destinataire, réutiliser ce qui fonctionne.

H2 — La méthode en une phrase
  Tu [action 1], tu [action 2], puis tu [action 3]. Exemple : pour [cas], tu pars de [matière] et tu arrives à [livrable].
  Si prestation : le client reçoit [livrable], à [cadence], pour [décision visée]. Le besoin revient parce que [raison].

H2 — Commence par un cas précis
  Choisis [cible / site / offre]. Il te faut [donnée], [contexte], un moyen de vérifier [résultat].
  Fin d'étape : tu sais sur quoi tu travailles, pour qui, avec quel objectif.

H2 — Récupère la matière avant de produire
  Sources 1 puis 2. Par élément : source + date, contexte, ce que tu observes, ce que tu penses pouvoir en tirer.
  Séparer les deux dernières. Outil + opération. Erreur fréquente + contrôle.
  Fin d'étape : matière exploitable.

H2 — Construis ta base de référence
  Fiche / mémoire / procédure / bibliothèque : contexte, règles, exemples, critères de qualité.
  Règle simple : si [critère] manque, tu [correction]. Distinguer l'élément stable de l'élément variable.

H2 — Produis une première version
  Opération 1, 2, 3 avec entrée exacte, consigne, sortie attendue.
  Essai sur un petit périmètre d'abord ; vérifier la partie déterminante avant les variantes.

H2 — Vérifie ce que tu as obtenu
  3 critères observables. Si problème : corriger tel élément, refaire le contrôle.
  Test réel : « sur ce cas, j'ai observé [résultat] dans [conditions]. Reste à vérifier [limite] ».
  Pas de test : dire comment il sera mené et ce qui sera observé.

H2 — Prépare un premier exemple
  Appliquer la méthode à un cas : point de départ, travail effectué, résultat constaté.
  Ce que le destinataire peut en faire. Garder temps passé et corrections.

H2 — Présente ton offre
  Message type : « J'ai préparé [livrable] pour [cas]. Il vous permet de [usage]. Je peux prendre en charge [périmètre] à [cadence], avec [suivi]. »
  Ce que le client reçoit : livrable/volume, fréquence, contrôle, conditions. Prix seulement si l'offre et son périmètre sont définis.

H2 — Réutilise ce qui a été validé
  Conserver procédure, exemple validé, correction utile. Adapter données, contexte, contraintes.
  Avant d'augmenter le volume : temps total, coût, qualité. Garder la décision importante sous contrôle.

COMMENCE ICI
  Prends [cas], fais [première action] avec [matière]. Tu sais que tu peux passer à la suite quand [critère simple].
  Une seule invitation (ressource, offre ou question liée au sujet).
```

### Ton

- « je » pour raconter les choix, « tu » pour les actions.
- Chaque décision est expliquée, puis un détail pratique, puis l'erreur possible.
- Quelques phrases de synthèse, espacées, entre de nombreuses phrases normales.
- Sponsor ou offre : placé dans le mode opératoire (plusieurs usages pendant le tutoriel), mention finale.

### Prudence

- Promesses financières et chiffres de prix : jamais repris du texte de référence. Ils viennent de nos propres offres, de nos tests ou de sources vérifiées (le texte de référence ne démontrait pas les ventes).
- Détails techniques : à vérifier avant publication.
- Fil conducteur : un même cas qui avance du début à la fin, avec un résultat concret à chaque étape.

### Transposition SEO / IA

| Texte de référence | Nos contenus |
|---|---|
| Les marques renouvellent leurs publicités | Le client choisit, applique et suit les prochaines actions sur son site |
| Vidéos = matière de départ | Données GSC, pages existantes, questions clients, nos tests |
| Fiche de référence du personnage | Mémoire client, règles métier, exemples vérifiés |
| Les outils produisent des publicités | Le système produit audit, brief, sélection de mots-clés, proposition de maillage |
| Premières publicités = démonstration | Un cas réel, données de départ, décisions que le livrable permet |
| Formats validés réutilisés | Procédures et contrôles réutilisés, stratégie adaptée par client |

Angle type : « Comment construire ton système SEO avec Claude et Obsidian, du premier audit au suivi client », déroulé sur un seul site gardé du début à la fin.

### Articulation

- Newsletter : l'ordre des blocs obligatoires (`feedback_structure_newsletter_3blocs.md`, skill `newsletter-ia`) prime ; ce pattern règle l'intérieur d'un bloc long.
- Article d'étude, brève, page outil : patterns 1 et 2, pas celui-ci.
- Le principe de non-complétion s'applique : étape sans matière = supprimée ou `[MATIÈRE MANQUANTE]` dans le brief.

## Ce que la structure ne règle pas

- Contenu accessible : ne pas bloquer OAI-SearchBot (ChatGPT Search).
- Suivi : « la marque est mentionnée » ≠ « la page est citée comme source ».

## Contrôle avant de rendre

1. Chaque H2 répond à une question de décision ? Aucun titre vague du tableau ci-dessus ?
2. Chaque section a une réponse directe qui nomme le sujet et ses conditions (pas de « Oui » sec) ?
3. Preuve réelle ou ligne supprimée ? Test non réalisé = pas de section « résultats ».
4. Limite présente quand elle existe ?
5. Comparatif : mêmes critères, sources, date de vérification. Prix : unité, engagement, restrictions.
6. Passe `redaction-anti-ia`, puis `node .claude/skills/redaction-anti-ia/slop.mjs <fichier>`.
