# Construis ton propre agent SEO avec Claude

**De zéro à un système qui travaille avec tes méthodes, tes données et ton expérience.**

Par Timothée Boussardon — organikk.co

## Introduction

Ça fait des années que les consultants SEO utilisent les mêmes outils.

Les mêmes mots-clés, les mêmes scores, les mêmes recommandations.

Et à chaque nouveau client, on recommence presque de zéro.

Depuis plusieurs mois, j'ai complètement changé ma façon de travailler.

Aujourd'hui, Claude fait environ 80 % de mon travail SEO. Les 20 % restants, ce sont les décisions stratégiques, la connaissance du client et les arbitrages que je préfère garder.

Mais attention, je ne parle pas de demander à ChatGPT ou à Claude de faire un audit SEO avec un prompt.

Je parle de construire ton propre système.

Un système qui connaît tes méthodes, retrouve tes anciennes analyses, utilise tes données clients, exécute tes tâches et apprend de tes corrections.

Et surtout, un système que tu peux améliorer tous les jours.

C'est exactement ce que nous allons construire dans ce guide.

Je vais te montrer comment passer d'un simple chatbot à un véritable agent SEO, avec Claude Code et Obsidian.

On va avancer dans un ordre précis. Pas besoin de tout construire le premier jour.

**Le but, c'est qu'à chaque étape, tu repartes avec quelque chose qui fonctionne.**

---

# Avant de commencer

Quelques mots à comprendre.

- **Claude Code :** la version de Claude qui travaille directement dans ton terminal. Il peut lire des fichiers, en créer, lancer des commandes et utiliser tes méthodes.
- **Terminal :** une application de ton ordinateur qui permet d'exécuter des commandes.
- **Obsidian :** une application gratuite pour consulter et organiser tes notes. Elle est particulièrement pratique pour construire une base de connaissances.
- **Vault :** un dossier contenant tes notes. C'est le nom donné à un espace de travail Obsidian.
- **Skill :** une méthode que tu transformes en instructions réutilisables par Claude.
- **Workflow :** plusieurs tâches enchaînées dans un ordre précis.
- **Routine :** une tâche qui se déclenche automatiquement, par exemple tous les lundis.
- **Boucle :** un mécanisme qui récupère les résultats et les corrections pour améliorer ton système.

Je vais utiliser ces termes dans le guide, mais tu verras rapidement qu'ils sont assez simples à comprendre.

# Phase 0 — Comprendre ce que tu construis

Avant d'installer quoi que ce soit, il faut comprendre une différence importante.

Quand tu utilises Claude dans une conversation, tu lui demandes quelque chose et il te répond.

Tu peux lui donner du contexte, des documents ou des instructions.

Mais ce n'est pas encore un système SEO.

Pour construire ton agent, il te faut plusieurs éléments qui travaillent ensemble :

1. Une mémoire qui conserve tes connaissances.
2. Tes données, notamment celles de tes clients.
3. Tes propres méthodes SEO.
4. Tes règles de rédaction.
5. Des workflows qui enchaînent les tâches.
6. Des boucles qui récupèrent les résultats et les corrections.
7. Des routines qui lancent certaines missions automatiquement.

Pourquoi prendre le temps de construire tout ça ?

Parce que je pense que notre valeur de consultant ne sera plus dans notre capacité à utiliser un outil.

Tout le monde pourra utiliser les mêmes outils.

En revanche, tout le monde n'aura pas tes connaissances, ton expérience, les questions de tes clients, tes observations et tes méthodes.

**C'est justement ce qu'on va donner à ton agent.**

Une précision : si tu n'as pas de méthode SEO, Claude ne va pas l'inventer correctement à ta place.

Il pourra te faire des propositions. Mais il faudra toujours savoir les évaluer.

L'idée, ce n'est pas de remplacer ton expertise.

C'est de lui donner les moyens de travailler à plus grande échelle.

# Phase 1 — Construire le socle

On commence par le plus important : donner à Claude un endroit où travailler et des règles à respecter.

## Étape 1 — Installer Claude Code

Tu vas avoir besoin de :

- Un ordinateur avec un terminal.
- Un accès à Claude Code.
- Git, pour suivre les modifications de tes fichiers.
- Obsidian, pour consulter ta base de connaissances.

Installe Claude Code en suivant la documentation officielle d'Anthropic.

Une fois installé, ouvre ton terminal et lance :

`claude`

Connecte ton compte si nécessaire.

Tu peux maintenant discuter avec Claude directement depuis ton terminal.

La différence avec le chat classique, c'est qu'il peut travailler sur les fichiers de ton ordinateur, dans les limites des accès que tu lui donnes.

## Étape 2 — Créer ton vault

Crée un dossier sur ton ordinateur.

Appelle-le par exemple `mon-vault`.

C'est ici que tu vas conserver la mémoire de ton système.

Ouvre Claude Code depuis ce dossier et demande-lui :

> Crée une base de connaissances SEO dans ce dossier. Je veux deux espaces : raw pour conserver les documents d'origine et wiki pour les connaissances que tu vas produire à partir de ces documents. Organise les dossiers pour que je puisse ensuite utiliser Obsidian.

Tu peux partir de cette structure :

```text
mon-vault/
├── CLAUDE.md
├── raw/
│   ├── articles/
│   ├── data/
│   ├── clients/
│   └── notes/
└── wiki/
    ├── index.md
    ├── log.md
    ├── hypotheses.md
    ├── sources/
    ├── concepts/
    ├── briefs/
    └── preuves/
```

Pas besoin de faire plus compliqué au départ.

`raw/` contient les fichiers d'origine.

`wiki/` contient les informations que ton agent a extraites, organisées et reliées entre elles.

Une règle importante : **Claude ne modifie jamais les documents de `raw/`.**

Il peut les lire, mais toutes ses productions doivent être enregistrées ailleurs.

Tu conserves ainsi tes sources intactes.

## Étape 3 — Connecter Obsidian

Ouvre Obsidian.

Choisis l'option permettant d'ouvrir un dossier existant comme coffre.

Sélectionne `mon-vault`.

Tu peux maintenant naviguer dans les fichiers que Claude crée.

C'est assez pratique : tu peux laisser Claude travailler dans le terminal et retrouver ses productions dans Obsidian.

Tu peux également modifier tes notes toi-même.

## Étape 4 — Écrire ta doctrine SEO

C'est probablement l'une des étapes les plus importantes.

Dans ton dossier principal, crée un fichier `CLAUDE.md`.

Ce fichier doit expliquer à Claude comment tu travailles.

Pas besoin d'écrire cinquante pages.

Commence par tes règles SEO non négociables.

Voici quelques exemples tirés de ma méthode :

- Je privilégie les conversions plutôt que le trafic.
- Je recherche d'abord des mots-clés liés aux offres du client.
- Je n'invente jamais de chiffres, de volumes ou de résultats.
- Je construis une page autour d'une intention principale et des questions qui l'accompagnent.
- J'utilise les questions des prospects et les données propriétaires pour enrichir les contenus.
- Je privilégie une structure de site cohérente plutôt que la multiplication des pages.
- Chaque recommandation doit être justifiée.
- Les décisions stratégiques importantes restent soumises à ma validation.

Tu peux ensuite demander à Claude :

> Pose-moi les questions nécessaires pour comprendre exactement ma méthode SEO. À partir de mes réponses, aide-moi à construire mon fichier CLAUDE.md. N'ajoute aucune règle que je n'ai pas validée.

Il va progressivement documenter ta façon de travailler.

C'est cette doctrine qui permettra à Claude d'appliquer tes méthodes plutôt que de produire systématiquement des recommandations génériques.

**À la fin de cette phase :** tu as Claude Code, ton vault Obsidian et tes premières règles SEO. Ton agent dispose d'un espace de travail et d'un cadre précis.

# Phase 2 — Donner tes connaissances à l'agent

Maintenant, il faut le nourrir.

Et c'est ici que je vois une énorme différence entre un consultant qui utilise simplement Claude et un consultant qui construit son système.

Le premier pose des questions.

Le deuxième donne à Claude tout ce qu'il a appris pendant des années.

## Étape 1 — Rassembler tes données

Commence par récupérer :

- Tes anciens audits SEO.
- Tes stratégies de mots-clés.
- Tes briefs de contenus.
- Tes rapports Search Console.
- Tes notes de rendez-vous.
- Les questions de tes prospects.
- Les transcriptions de tes appels commerciaux.
- Les objections que tu retrouves régulièrement.
- Les avis, témoignages et retours de tes clients.
- Tes observations et tes propres recherches.

Tu n'es pas obligé de tout intégrer dès le premier jour.

Commence avec un seul projet.

Par exemple, récupère trois anciens audits, une stratégie de mots-clés et quelques notes clients.

Dépose ces documents dans `raw/`.

Anonymise les informations personnelles et vérifie que tu es autorisé à traiter les données concernées.

## Étape 2 — Apprendre à Claude à traiter tes documents

Attention, déposer cent PDF dans un dossier ne suffit pas.

Claude doit pouvoir retrouver les informations importantes sans relire l'intégralité des documents à chaque mission.

On va donc lui apprendre à les traiter.

Demande-lui :

> Analyse les documents présents dans raw/. Pour chaque document, crée une fiche dans wiki/sources/ avec le contexte, les informations importantes, les chiffres utiles, les limites et les enseignements SEO. Relie ensuite ces informations aux concepts existants dans wiki/concepts/. Ne modifie jamais les sources d'origine.

Pour chaque document, ton agent doit :

1. Lire le contenu.
2. Identifier les informations intéressantes.
3. Créer une fiche.
4. Relier les informations aux connaissances déjà présentes.
5. Noter ce qu'il a fait dans `wiki/log.md`.

Fais-le d'abord sur un seul document.

Regarde le résultat dans Obsidian.

Corrige ce qui ne te plaît pas, puis recommence.

## Étape 3 — Organiser les connaissances

Imaginons que tu aies travaillé sur la cannibalisation SEO pour plusieurs clients.

Au lieu de conserver trois rapports indépendants, Claude peut créer une note `cannibalisation-seo.md`.

Elle rassemble tes observations, les situations rencontrées, les solutions testées et les résultats mesurés.

Chaque information doit rester reliée au document qui la justifie.

La prochaine fois que tu lui demandes un audit de cannibalisation, il peut retrouver ce que tu sais déjà.

Et si un nouveau projet apporte un résultat différent, il pourra te le signaler.

C'est exactement le but.

## Étape 4 — Vérifier qu'il retrouve les bonnes informations

Teste ton système avec une question précise.

Par exemple :

> Retrouve tout ce que nous avons déjà appris sur les pages orphelines. Distingue mes observations, mes règles et les hypothèses qui restent à confirmer. Donne-moi les sources.

Regarde s'il retrouve correctement tes anciennes analyses.

Si la réponse est incomplète, améliore l'organisation des fiches.

Au départ, une simple recherche dans les fichiers peut suffire.

Quand ton vault devient beaucoup plus gros, tu peux ajouter un moteur de recherche sémantique local pour retrouver des informations même lorsque les mots utilisés sont différents.

## Étape 5 — Protéger les données de tes clients

Ton vault est stocké sur ton ordinateur, mais cela ne veut pas dire que les informations restent toutes sur ton ordinateur lorsque Claude les traite.

Claude Code transmet les données nécessaires au modèle selon son fonctionnement et les paramètres de ton compte.

Avant d'importer des données clients, vérifie les paramètres de confidentialité de ton compte Anthropic et les conditions de traitement applicables.

Pour un usage professionnel, privilégie un cadre contractuel adapté au traitement des données.

Et garde trois habitudes :

1. Informe les personnes concernées lorsqu'un appel est enregistré.
2. Évite de conserver des données personnelles inutiles.
3. Anonymise les documents dès que possible.

Ne confonds pas la désactivation de l'entraînement des modèles avec la conformité au RGPD. Ce sont deux sujets différents.

**À la fin de cette phase :** ton agent commence à retrouver tes connaissances, tes expériences et les informations de tes clients. Il ne travaille plus uniquement avec les connaissances générales de Claude.

# Phase 3 — Transformer tes méthodes en skills

On arrive à la partie que je préfère.

Tu vas maintenant transformer tes méthodes SEO en compétences exécutables.

Prenons un exemple.

Tu sais faire une recherche de mots-clés. Tu as probablement une méthode, même si tu ne l'as jamais formalisée.

Tu commences par comprendre l'offre du client. Tu identifies les problèmes de ses prospects. Tu recherches des formulations. Tu regroupes les intentions. Puis tu décides quelles pages créer.

Tout ça, c'est déjà un processus.

L'objectif est de le transformer en skill.

## Étape 1 — Choisir une tâche que tu maîtrises

Ne commence pas par un audit SEO de 50 étapes.

Choisis quelque chose de plus simple.

Par exemple : trouver les mots-clés business d'une entreprise.

Prends une méthode que tu utilises déjà et que tu sais évaluer.

## Étape 2 — Décomposer ta méthode

Écris les étapes dans l'ordre.

Pour une recherche de mots-clés, ça pourrait donner :

1. Comprendre l'offre.
2. Identifier les clients que l'entreprise veut attirer.
3. Récupérer les questions réelles de ses prospects.
4. Proposer des mots-clés liés à une intention commerciale.
5. Regrouper les formulations qui correspondent au même besoin.
6. Vérifier les données disponibles.
7. Préparer une liste de pages à travailler.
8. Soumettre la sélection pour validation.

L'ordre compte.

Tu ne veux pas que Claude commence à proposer trente pages avant d'avoir compris ce que vend l'entreprise.

## Étape 3 — Créer ton premier skill

Un skill Claude contient notamment un fichier `SKILL.md`.

Tu peux demander à Claude Code de créer cette compétence avec la structure attendue.

Voici un exemple simplifié :

```markdown
---
name: recherche-mots-cles
description: Recherche de mots-clés business à partir
  des offres, des clients et des données disponibles.
---

# Objectif

Identifier les mots-clés susceptibles d'attirer
des prospects qualifiés.

# Étapes

1. Lire la fiche du projet.
2. Identifier les offres.
3. Récupérer les questions des prospects.
4. Proposer les mots-clés business.
5. Regrouper les variantes par intention.
6. Vérifier les données disponibles.
7. Préparer une sélection argumentée.
8. Demander validation.

# Règles

- Ne jamais inventer de volume.
- Ne jamais inventer de données.
- Ne pas confondre mots-clés et pages.
- Privilégier les intentions commerciales.
- Signaler les informations manquantes.
- Ne pas créer de page sans validation.

# Livrable

Enregistrer le résultat dans wiki/briefs/.
```

Tu peux ensuite donner une mission réelle à Claude pour voir s'il applique bien le skill.

## Étape 4 — Tester le skill sur un vrai projet

Prends un client que tu connais.

Lance la recherche.

Regarde si Claude suit les étapes, utilise les bonnes données et respecte tes règles.

Il va probablement faire des erreurs.

C'est normal.

Mais au lieu de simplement corriger la réponse dans la conversation, demande-lui d'identifier ce qu'il faut améliorer dans le skill.

Tu valides ensuite la modification.

La prochaine fois, il utilisera la version corrigée.

C'est tout l'intérêt.

## Étape 5 — Construire les autres skills

Voici les neuf compétences SEO que je construirais en priorité :

1. **Recherche de mots-clés :** identifier les requêtes intéressantes à partir des offres et des données.
2. **Clustering :** regrouper les requêtes qui correspondent à une même intention.
3. **Mots-clés décisionnels :** identifier les recherches qui peuvent conduire à une demande commerciale.
4. **Brief de contenu :** préparer la structure d'une page et les questions auxquelles elle doit répondre.
5. **Entités sémantiques :** identifier les concepts nécessaires pour traiter correctement un sujet.
6. **Pages programmatiques :** créer une méthode de production adaptée à plusieurs pages construites sur un même modèle, lorsque chacune répond à un besoin réel.
7. **Maillage interne :** analyser les liens entre les pages et proposer des améliorations.
8. **Cannibalisation :** identifier les pages qui ciblent la même intention et recommander une action.
9. **Audit GEO :** étudier la présence d'une entreprise dans les réponses des moteurs IA et les possibilités d'amélioration.

Je ne te conseille pas de construire les neuf immédiatement.

Commence par trois : recherche de mots-clés, clustering et sélection des mots-clés business.

Fais-les fonctionner ensemble.

Ensuite seulement, ajoute les autres.

Mon système a évolué de cette façon. J'ai ajouté des compétences au fur et à mesure que je rencontrais des besoins.

Tu peux faire exactement pareil.

**À la fin de cette phase :** tu disposes de tes premiers skills SEO. Claude peut appliquer une méthode précise et conserver les améliorations que tu valides.

# Phase 4 — Apprendre à Claude à écrire comme toi

Tu as déjà remarqué que les textes écrits par les IA finissent souvent par se ressembler ?

Les mêmes expressions, les mêmes introductions, les mêmes conclusions.

Pour un consultant qui produit du contenu, c'est un vrai problème.

Il faut donc apprendre à ton agent comment tu écris.

## Étape 1 — Rassembler tes meilleurs textes

Crée un dossier consacré à ton style de rédaction.

Ajoute :

- Tes meilleurs posts LinkedIn ou X.
- Quelques newsletters.
- Des mails commerciaux que tu as réellement écrits.
- Des articles de ton site.
- Des passages que tu trouves particulièrement réussis.

Privilégie les textes qui représentent vraiment ta façon de parler.

Pas ceux que tu as fait entièrement rédiger par une IA.

## Étape 2 — Lui faire analyser ta voix

Demande à Claude :

> Analyse mes textes pour comprendre comment j'écris. Observe mes phrases, mon vocabulaire, mon rythme, mes introductions, mes transitions et mes conclusions. Identifie les expressions que j'utilise et celles que j'évite. Construis un guide de rédaction à partir de mes textes réels, sans inventer de préférences.

Tu obtiens une première version de ton guide de voix.

Relis-le et corrige ce qui ne te ressemble pas.

## Étape 3 — Ajouter tes règles anti-IA

Voici celles que j'utiliserais.

**Évite :**

- Les expressions artificielles comme « il est crucial de », « dans un monde en constante évolution » ou « véritable révolution ».
- Les superlatifs qui ne veulent rien dire.
- Les introductions qui prennent trois paragraphes pour arriver au sujet.
- Les listes de trois arguments systématiques.
- Les phrases qui reformulent plusieurs fois la même idée.
- Les conclusions qui résument simplement ce qui vient d'être expliqué.
- Les métaphores inutiles.
- Les transitions forcées entre chaque paragraphe.
- Le gras sur une phrase sur deux.
- Les tournures qui donnent l'impression de vendre quelque chose en permanence.

**Privilégie :**

- Des phrases naturelles.
- Des exemples concrets.
- Des observations personnelles.
- Des explications qui vont droit au but.
- Des variations de rythme.
- Le vocabulaire que tu utilises réellement.
- Des arguments qui reposent sur ton expérience et tes données.

Et surtout, il ne faut pas chercher à rendre tous tes textes parfaitement uniformes.

Les humains n'écrivent pas comme ça.

## Étape 4 — Tester sur un vrai contenu

Donne-lui une de tes anciennes newsletters.

Demande une nouvelle version basée sur le guide de voix.

Compare avec ton style.

Quand une phrase ne te ressemble pas, explique pourquoi.

Tu peux ensuite ajouter cette correction à ton guide, si c'est une préférence que tu souhaites conserver.

Le but n'est pas que Claude imite quelques mots que tu utilises.

**Le but, c'est qu'il comprenne comment tu construis une idée et comment tu l'expliques.**

Et garde toujours une relecture humaine.

Chez moi, l'agent fait une grosse partie du travail, mais je garde la rédaction finale et les derniers arbitrages.

Quand tu construis un agent pour un client, tu refais cette phase avec ses propres textes.

**À la fin de cette phase :** ton agent possède un guide de rédaction personnalisé et des règles pour éviter les formulations typiques de l'IA.

# Phase 5 — Construire tes workflows SEO

Maintenant que Claude possède plusieurs compétences, on va lui apprendre à les utiliser ensemble.

Parce que dans une mission SEO, tu ne fais pas une recherche de mots-clés isolée.

Tu analyses le site, tu identifies des opportunités, tu prépares des pages, puis tu regardes les résultats.

Tout est lié.

J'organise ce travail autour de quatre workflows.

## Workflow 1 — L'audit SEO

**Objectif : comprendre ce qui bloque le site et identifier les premières actions.**

Étape par étape :

1. Claude récupère les informations du projet.
2. Il analyse les données Search Console disponibles.
3. Il examine la structure du site et les résultats d'un crawl.
4. Il identifie les problèmes d'indexation, de structure et de maillage.
5. Il analyse les pages liées aux offres commerciales.
6. Il regroupe les problèmes par priorité.
7. Il prépare un plan d'action.
8. Tu valides les actions importantes.

L'agent ne doit pas simplement te sortir une liste de 150 problèmes techniques.

Il doit t'aider à comprendre ce qu'il faut corriger en premier et pourquoi.

## Workflow 2 — La stratégie de mots-clés

**Objectif : décider quelles pages travailler ou créer.**

Étape par étape :

1. Lire les offres et les objectifs du client.
2. Rechercher les questions et les besoins de ses prospects.
3. Exécuter le skill de recherche de mots-clés.
4. Regrouper les requêtes par intention.
5. Sélectionner les opportunités commerciales.
6. Étudier les pages existantes.
7. Proposer les pages à améliorer ou à créer.
8. Préparer la stratégie pour validation.

C'est important : on ne crée pas automatiquement une nouvelle URL pour chaque question.

Plusieurs questions peuvent être traitées sur une même page lorsqu'elles participent à la même intention.

L'objectif est d'avoir un site cohérent, pas de multiplier les contenus sans raison.

## Workflow 3 — La rédaction

**Objectif : préparer une page qui répond aux besoins de tes prospects.**

Étape par étape :

1. Récupérer le mot-clé principal et les questions associées.
2. Lire les informations disponibles dans le vault.
3. Retrouver les preuves, les exemples et les objections clients.
4. Préparer la structure de la page.
5. Rédiger une première version en respectant ton style.
6. Vérifier les données et les affirmations.
7. Appliquer les règles anti-IA.
8. Te soumettre le contenu pour relecture.
9. Préparer la publication une fois la page validée.

C'est là que tes données propriétaires deviennent particulièrement utiles.

Au lieu de demander à Claude d'écrire une page à partir de connaissances génériques, tu lui donnes de vraies questions, de vrais exemples et des informations issues du terrain.

## Workflow 4 — Le suivi

**Objectif : comprendre ce que le travail SEO a réellement apporté.**

Étape par étape :

1. Récupérer les dernières données Search Console.
2. Comparer avec la période précédente.
3. Identifier les pages dont les performances progressent ou reculent.
4. Repérer les nouvelles opportunités de requêtes.
5. Vérifier les éventuels problèmes de cannibalisation.
6. Proposer les améliorations de maillage.
7. Mettre à jour les fiches de suivi des pages.
8. Préparer les prochaines actions.

La boucle est simple :

Audit → mots-clés → rédaction → suivi.

Puis le suivi alimente le prochain audit ou les prochaines décisions de contenu.

## Le contrôle qualité

Je te conseille d'ajouter un point de contrôle avant toute publication.

Il doit notamment vérifier que :

- Les chiffres et les affirmations sont justifiés.
- Le contenu répond bien à l'intention ciblée.
- Les informations du client sont correctement utilisées.
- Les règles de rédaction sont respectées.
- La page propose une action cohérente avec son objectif.
- Les éléments importants ont été validés.

Une page qui échoue à un contrôle bloquant ne doit pas être publiée automatiquement.

**À la fin de cette phase :** ton agent peut enchaîner plusieurs compétences dans une mission complète. Tu interviens aux moments où ton jugement est nécessaire, pas pour lui rappeler chaque étape.

# Phase 6 — Construire les boucles d'amélioration

C'est ici que ton système commence réellement à devenir intéressant.

Parce qu'un agent qui produit des audits et des contenus n'est pas forcément un bon agent.

Il peut simplement répéter les mêmes erreurs plus vite.

Pour progresser, il doit récupérer ce qu'il apprend de ses missions.

Je te propose quatre boucles.

## Boucle 1 — Transformer les documents en connaissances

Tu vas régulièrement ajouter de nouvelles données dans ton vault.

Le problème, c'est qu'elles risquent de rester dans tes dossiers sans être exploitées.

Il faut donc une routine de traitement.

Étape par étape :

1. L'agent repère les nouveaux fichiers dans `raw/`.
2. Il vérifie lesquels ont déjà été traités.
3. Il prépare une liste des documents en attente.
4. Il classe les documents par importance.
5. Tu valides ceux à traiter.
6. Il crée les fiches correspondantes.
7. Il met à jour les concepts concernés.

Tu peux faire ce contrôle une fois par semaine.

Ainsi, ton système continue d'intégrer de nouvelles connaissances.

## Boucle 2 — Mettre tes convictions à l'épreuve

Nous avons tous des convictions SEO.

Mais certaines reposent sur des données solides, d'autres sur des observations limitées.

Je te conseille de créer un fichier :

`wiki/hypotheses.md`

Il contiendra les idées que tu souhaites suivre.

Pour chaque hypothèse, tu peux noter :

- Ce que tu penses.
- Pourquoi tu le penses.
- Les données disponibles.
- Ce qu'il faudrait observer pour la confirmer ou la remettre en question.
- Son statut actuel.

Par exemple, tu peux avoir une hypothèse sur la manière dont le maillage interne influence certaines pages.

L'agent va retrouver les observations pertinentes dans les projets et te signaler lorsqu'une nouvelle donnée apporte un éclairage.

Une hypothèse ne devient pas une règle validée simplement parce que Claude trouve l'idée convaincante.

Il faut des preuves.

## Boucle 3 — Apprendre des résultats

C'est celle que je trouve la plus importante.

Quand tu publies une page, ton système doit être capable de retrouver quelques mois plus tard ce qui a été décidé et ce qui s'est réellement passé.

Voici comment faire.

**À la publication :**

1. Créer une fiche pour la page.
2. Enregistrer son URL et sa date de publication.
3. Conserver le mot-clé et l'intention ciblés.
4. Noter les principales décisions SEO.
5. Définir les résultats attendus et les hypothèses à tester.

**À J+30 :**

1. Récupérer les données Search Console.
2. Comparer les résultats aux attentes.
3. Identifier les premiers signaux.
4. Noter les observations.

**À J+90 :**

1. Refaire l'analyse.
2. Regarder les impressions, les clics et les requêtes.
3. Ajouter les données de conversion lorsqu'elles sont disponibles.
4. Identifier ce qui semble avoir fonctionné ou non.
5. Proposer les ajustements nécessaires.

Attention, une progression SEO ne prouve pas à elle seule qu'une action précise en est la cause.

L'objectif est d'accumuler des observations exploitables, pas d'inventer des certitudes.

Au fil des missions, ton agent retrouve les choix précédents et les résultats observés.

Tes prochaines décisions peuvent donc s'appuyer sur davantage de données réelles.

## Boucle 4 — Transformer tes corrections en règles

Imaginons que Claude rédige un titre.

Tu le corriges.

Deux semaines plus tard, il refait exactement la même erreur.

Tu le corriges à nouveau.

Puis encore une fois le mois suivant.

C'est une perte de temps.

Il faut donc un endroit où enregistrer ces corrections.

Crée un fichier :

`wiki/corrections-recurrentes.md`

À chaque correction importante :

1. Claude note ce que tu as corrigé.
2. Il explique la raison de la correction.
3. Il retrouve les corrections similaires.
4. Si le même problème revient, il te propose une nouvelle règle.
5. Tu valides ou refuses.
6. La règle est intégrée à la doctrine ou au skill concerné.
7. Un contrôle automatique est ajouté lorsqu'il est possible de détecter l'erreur mécaniquement.

Il ne faut pas que Claude modifie librement toutes tes méthodes.

Il te propose une amélioration. Tu décides si elle doit devenir permanente.

C'est comme ça que ton système conserve les apprentissages de tes anciennes missions.

## Le rendez-vous du vendredi

Je te conseille de réserver quinze minutes par semaine pour faire le point.

Demande simplement à Claude :

> Prépare ma revue hebdomadaire. Montre-moi les nouvelles connaissances intégrées, les résultats SEO récupérés, les hypothèses qui ont évolué, les contradictions détectées et les corrections récurrentes. Termine par les décisions que je dois prendre.

Tu dois obtenir quelque chose de court et exploitable.

Pas un rapport de trente pages.

Si tu passes une heure à comprendre ce que ton agent a fait, c'est qu'il faut encore améliorer son organisation.

**À la fin de cette phase :** ton système ne se contente plus de produire. Il conserve des observations, confronte ses hypothèses aux résultats et te propose des améliorations fondées sur tes corrections.

# Phase 7 — Automatiser les routines

Tout ce que nous avons construit jusqu'ici peut fonctionner à la demande.

Tu ouvres ton terminal, tu demandes un audit et Claude exécute le workflow.

Maintenant, on va automatiser certaines tâches.

Pas besoin de tout automatiser.

Commence par celles que tu répètes régulièrement.

## Étape 1 — Choisir ta première routine

Prends une tâche simple.

Par exemple, chaque lundi matin, ton agent prépare la liste des documents qui n'ont pas encore été intégrés dans le vault.

Tu peux lui donner cette consigne :

> Chaque lundi, vérifie les nouveaux documents présents dans raw/. Compare-les aux fiches existantes dans wiki/sources/. Prépare une liste des documents à traiter, classés par priorité. Ne modifie pas les fichiers sources et conserve un journal d'exécution.

## Étape 2 — Choisir comment la lancer

Tu as plusieurs possibilités.

**Option 1 — Sur ton ordinateur**

Tu peux utiliser un planificateur local, comme `launchd` sur Mac ou `cron` sur Linux.

Claude Code peut être lancé sans conversation interactive, par exemple avec :

`claude -p "Exécute la routine de revue du backlog"`

Il faut que ton ordinateur soit allumé et que les accès nécessaires fonctionnent.

**Option 2 — Avec GitHub Actions**

Tu peux versionner ton vault avec Git et déclencher certaines tâches depuis GitHub Actions.

L'exécution se fait alors dans le cloud.

Ton ordinateur n'a pas besoin de rester allumé, mais il faut prévoir l'accès aux fichiers, au modèle et aux secrets nécessaires.

**Option 3 — Avec les tâches planifiées Claude**

Tu peux aussi utiliser les fonctionnalités de planification proposées dans ton environnement Claude, selon celles disponibles avec ton compte.

Elles permettent de lancer certaines tâches à des horaires définis.

Le principe est le même : une mission précise, un déclencheur et un résultat enregistré.

## Étape 3 — Ajouter les premières routines SEO

Voici le planning que je te conseille pour commencer.

| Routine | Fréquence | Mission |
|---|---|---|
| Données Search Console | Chaque mois | Récupérer les données et mettre à jour les suivis |
| Audit d'indexation | Chaque mois | Identifier les URL présentant des problèmes |
| Documents non traités | Lundi | Préparer la liste des nouvelles sources |
| Revue des hypothèses | Début de mois | Examiner les nouvelles observations |
| Revue des corrections | Vendredi | Proposer les règles à améliorer |
| Revue hebdomadaire | Vendredi | Résumer ce qui nécessite ton attention |

Commence par une seule routine.

Fais-la fonctionner correctement, puis passe à la suivante.

## Étape 4 — Vérifier ce que les routines font réellement

C'est indispensable.

Une routine peut échouer sans que tu sois devant ton ordinateur.

Elle peut aussi récupérer des données incomplètes ou produire un résultat incorrect.

Je te conseille donc trois règles :

1. Chaque routine conserve la date, les actions réalisées et son résultat.
2. Si une donnée manque, l'agent le signale au lieu de l'inventer.
3. Les actions sensibles, comme une publication ou une modification importante, demandent une autorisation explicite.

Les logs doivent te permettre de comprendre ce qui s'est passé.

Ne donne pas les pleins pouvoirs à ton agent simplement parce que tu veux gagner du temps.

L'automatisation est utile uniquement si tu peux garder le contrôle.

**À la fin de cette phase :** certaines tâches répétitives peuvent se lancer automatiquement. Ton agent prépare ses résultats et te remonte les problèmes au lieu de te demander de tout exécuter toi-même.

# Phase 8 — Apprendre à manager ton agent

C'est la dernière étape.

Et probablement le changement le plus important dans ta façon de travailler.

Avant, tu faisais toi-même toutes les tâches.

Maintenant, tu dois apprendre à déléguer les bonnes choses.

Ton travail consiste davantage à définir les objectifs, améliorer les méthodes et prendre les décisions importantes.

## Étape 1 — Arrêter de tout refaire toi-même

Si tu demandes un audit à Claude, ne recommence pas l'audit intégralement à la main.

Vérifie plutôt :

- Les données utilisées.
- Les conclusions importantes.
- Les recommandations prioritaires.
- Les points sur lesquels l'agent manque d'informations.

Si tu repères une erreur, cherche aussi pourquoi elle s'est produite.

Est-ce que la doctrine manque d'une règle ?

Est-ce que le skill est incomplet ?

Est-ce que les données du client ne sont pas suffisantes ?

C'est en corrigeant la méthode que tu gagnes réellement du temps.

## Étape 2 — Définir ce que Claude peut décider

Toutes les décisions ne se valent pas.

Tu peux autoriser l'agent à organiser des fichiers, préparer des rapports ou exécuter des analyses.

En revanche, certaines actions doivent rester entre tes mains.

Par exemple :

- Valider la stratégie du client.
- Choisir les principales pages commerciales.
- Accepter une recommandation importante.
- Valider le contenu final.
- Autoriser une publication.
- Modifier une règle fondamentale de ta doctrine.

Tu peux définir ces limites directement dans `CLAUDE.md` et dans les skills.

## Étape 3 — Améliorer le système après chaque mission

Une mission ne doit pas simplement produire un livrable.

Elle peut aussi améliorer le système.

Après un projet, demande à Claude :

> Qu'avons-nous appris pendant cette mission ? Quelles erreurs ont été corrigées ? Quelles méthodes mériteraient d'être améliorées ? Prépare des propositions, sans modifier les règles existantes avant ma validation.

Tu vas progressivement construire un système de plus en plus adapté à ta manière de travailler.

## Étape 4 — Adapter les modèles aux tâches

Tu n'as pas forcément besoin du modèle le plus puissant pour chaque opération.

Réserve les modèles les plus capables aux tâches qui demandent une analyse complexe ou beaucoup de jugement.

Pour certaines opérations répétitives et bien cadrées, des modèles plus économiques peuvent suffire.

Teste toujours la qualité des résultats avant de changer de modèle sur une tâche importante.

## Étape 5 — Garder ton rôle de consultant

Je veux insister sur un point.

Ce n'est pas parce que ton agent sait proposer une stratégie SEO qu'il doit prendre toutes les décisions à ta place.

C'est toi qui connais ton client.

C'est toi qui comprends ses objectifs commerciaux.

C'est toi qui peux décider qu'une opportunité semble intéressante sur le papier, mais ne vaut pas le temps nécessaire.

Claude peut analyser énormément d'informations et te faire gagner du temps.

Mais **il doit travailler avec ton expertise, pas à la place de ton expertise.**

C'est ce que j'entends par manager son agent.

# Les six erreurs à éviter

J'en ai fait certaines moi-même.

**1. Vouloir construire un système parfait avant de l'utiliser.**

Commence avec un vault, une doctrine et trois skills. Lance ensuite une vraie mission. Tu amélioreras le reste au fur et à mesure.

**2. Ne donner aucune donnée propriétaire.**

Si tu ne fournis ni expérience, ni données clients, ni méthode personnelle, tu risques simplement de construire une version plus compliquée d'un chatbot.

**3. Laisser Claude inventer des chiffres.**

Aucun volume, aucune statistique et aucun résultat ne doit être inventé. Cette règle doit être présente dans la doctrine et dans les skills concernés.

**4. Produire sans mesurer.**

Si tu ne récupères jamais les résultats de ce que tu publies, tu ne peux pas savoir si tes décisions étaient pertinentes.

**5. Laisser ton agent décider de tout.**

L'autonomie n'est pas un objectif en soi. Il faut toujours définir les actions autorisées et les décisions qui demandent une validation.

**6. Garder les bonnes méthodes dans les conversations.**

Si tu corriges une erreur importante ou améliores une méthode, conserve cette information dans ton système. Sinon, tu risques de devoir recommencer plus tard.

# Ton plan de construction, étape par étape

Tu as maintenant toutes les pièces.

Voici l'ordre que je suivrais si je devais repartir de zéro.

Ne passe pas à la phase suivante simplement pour aller plus vite. Vérifie d'abord que ce que tu viens de construire fonctionne.

| Ordre | Ce que tu construis | Comment savoir que c'est prêt |
|---|---|---|
| 1 | Claude Code et Obsidian | Claude travaille dans ton vault |
| 2 | Ta doctrine SEO | Il connaît et applique tes principales règles |
| 3 | Ta base de connaissances | Il retrouve correctement tes anciennes informations |
| 4 | Tes trois premiers skills | Ils fonctionnent sur un projet réel |
| 5 | Ton guide de rédaction | Les brouillons respectent ta voix |
| 6 | Tes workflows | Plusieurs skills s'enchaînent correctement |
| 7 | Tes boucles d'amélioration | Les résultats et les corrections sont conservés |
| 8 | Tes routines | Une première tâche fonctionne automatiquement |
| 9 | Ton management | Tu sais ce que tu délègues et ce que tu valides |

Et surtout, ne cherche pas à construire les neuf étapes avant de commencer à travailler pour tes clients.

Dès que tu as le socle et un premier skill, utilise-le.

Tu découvriras très vite ce qui manque.

# Le mot de la fin

Je pense sincèrement que le métier de consultant va énormément changer.

Aujourd'hui, presque tout le monde peut demander à Claude de faire une recherche de mots-clés ou de rédiger un article.

Mais ce qui fera la différence, ce ne sera pas le nombre de prompts que tu connais.

Ce sera ta capacité à construire un système qui utilise tes connaissances, tes méthodes et tes données.

Un système qui conserve ce que tu apprends.

Qui retrouve les problèmes déjà rencontrés.

Qui applique tes méthodes.

Et qui devient plus utile à chaque nouvelle mission.

C'est ce que je construis depuis plusieurs mois.

Et c'est aussi pour cette raison que j'ai progressivement arrêté de dépendre des outils SEO classiques.

Je préfère investir du temps dans un système qui m'appartient, que je peux personnaliser et améliorer.

Tu n'as pas besoin de tout construire cette semaine.

Commence par ton vault.

Ajoute ta méthode.

Construis ton premier skill.

Et fais-le travailler sur un vrai projet.

Le reste viendra avec la pratique.

---

## On regarde tes process ensemble ?

Je te propose trente minutes en visio.

Tu me montres comment tu travailles aujourd'hui, les tâches que tu répètes pour chaque client et les outils que tu utilises encore.

On regarde ce que tu pourrais automatiser avec Claude Code et Obsidian, quelles méthodes transformer en skills et par où commencer.

**Réserver un créneau :** https://cal.com/tim-boussardon-yzrrb1/30min

organikk.co
