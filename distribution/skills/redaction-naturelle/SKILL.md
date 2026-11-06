---
name: redaction-naturelle
description: "Rythme d'écriture naturelle mesuré : paragraphes, modalisateurs, intertitres. « rédaction naturelle », « écris comme moi »."
---

## Quand utiliser ce skill

Le rythme d'écriture naturelle de Tim, mesuré et non deviné : ce qui sépare un
texte écrit par un agent d'un texte écrit à la main n'est pas la longueur des
phrases, c'est la longueur des PARAGRAPHES, l'absence de modalisateurs, les
déductions ajoutées à la source, les phrases sans verbe, les intertitres
étiquettes et l'accusation portée sur la personne au lieu de l'acte. Ce skill
donne les six règles, les paires avant/après relevées sur des réécritures
réelles de Tim, les cibles chiffrées et le script qui les mesure.

TOUJOURS invoquer ce skill quand Tim dit : "/redaction-naturelle", "écris
naturellement", "rédaction naturelle", "écris comme moi", "réécris cette
page", "réécris toutes les pages", "tue le pattern IA", "applique le registre",
ou quand il colle un texte réécrit à la main en exemple de ton de voix.

> **Règle mère (ton-de-voix § 0, posée le 2026-09-16).** Tu n'es pas payé au
> nombre de mots. Écris à partir des faits, pas autour des faits : supprime toute
> phrase qui sert uniquement à introduire, résumer, commenter ou conclure une
> information déjà compréhensible. Pas de conclusion en fin de section, pas de
> transition artificielle, pas de reformulation, pas de série de trois pour le
> rythme, pas de blocs de longueur égale, pas de phrase qui resterait vraie sur un
> autre client. Interdits au grep : « L'idée est simple », « C'est exactement »,
> « ce qui compte vraiment », « En clair », « Autrement dit », « Il est important
> de ». Après rédaction, **passe destructive obligatoire** (`redaction-anti-ia`) :
> le texte doit être plus court, et rien de supprimé n'est réécrit.
> **Non-complétion (règle absolue).** Produire uniquement ce que les sources
> permettent d'écrire. Un trou est préférable à une phrase générique : laisser la
> section courte ou poser `[MATIÈRE MANQUANTE]`. Ne jamais compléter pour une
> longueur, une transition, une introduction, une conclusion ou une structure
> homogène. Toute phrase doit être reliable à un élément de la matière source.
> Test : « d'où vient cette phrase ? » Sans réponse, elle est supprimée.
> Check : `node .claude/skills/redaction-anti-ia/slop.mjs <fichier>`


# Rédaction naturelle : mesurer avant de réécrire

## D'où viennent ces règles

Tim a réécrit à la main quatre textes de StopClope le 2026-08-18, puis a demandé la
comparaison éditoriale avec les versions qu'ils remplaçaient. Ce skill est le
résultat de ces comparaisons, mesurées, pas ressenties.

Ses quatre échantillons, mesurés :

| Texte de Tim | mots/phrase, médiane | mots/paragraphe, médiane |
|---|---|---|
| hypnose | 19 | 24 |
| cigarette et joints | 15 | 29 |
| marché du vapotage | 13,5 | 25 |
| **arrêt sans aide** (le plus récent, sa cible) | **11** | **23** |

**La cible est 11 à 13 mots par phrase, et 23 à 25 par paragraphe.**

Ce que produisait un agent avant correction : 17,5 mots par phrase, 36 par
paragraphe. Les 19 fiches de méthode du site sont passées de 14 à 10,5.

Et le point qui compte le plus, parce qu'il se rate même en visant juste :

**Raccourcir ne veut pas dire couper.** Sur le même contenu, Tim écrit
28 phrases là où l'agent en écrivait 20. Il en écrit *plus*, pas moins. Chaque
phrase porte une idée, et le mécanisme est déplié au lieu d'être comprimé.

> **Agent** (comprimé) : « Ce chiffre mesure ce qui se passe **par tentative**,
> dans un essai, avec un suivi. »
>
> **Tim** (déplié) : « Mais attention à ce que mesure ce chiffre. Il parle d'une
> **tentative d'arrêt** : une personne essaie d'arrêter, avec ou sans traitement,
> puis les chercheurs regardent si elle tient dans le temps. »

Un texte dense n'est pas un texte naturel. C'est un texte que le lecteur doit
déplier lui-même.

## Règle d'entrée

Avant de réécrire quoi que ce soit : **mesurer**.

```bash
node .claude/skills/redaction-naturelle/mesure.mjs <fichier|dossier> [...]
```

Le script sort, par fichier : mots, médiane de paragraphe, phrase la plus longue,
modalisateurs pour 1000 mots, chiffres collés à `%`/`€`, tutoiement. Il ne juge
pas à ta place et il ne casse aucun build : il dit où regarder.

Ne jamais annoncer « j'ai appliqué le registre » sans avoir relancé le script
après.

---

## Les huit règles

### 1. Une phrase, une idée

**Cible : 11 à 13 mots de médiane.**

Une phrase qui contient « et », « mais », « ce qui » ou un deux-points porte
presque toujours deux idées. Coupe à la charnière, garde les deux.

| Agent | Tim |
|---|---|
| « Les substituts nicotiniques doublent les chances de réussite, et 133 essais cliniques le montrent. » | « Les substituts nicotiniques doublent environ les chances de réussir. C'est ce que montrent 133 essais cliniques. » |
| « Une tentative sans aide réussit moins souvent qu'une tentative encadrée, mais les tentatives sans aide sont bien plus nombreuses, et on peut recommencer. » | « Une tentative sans aide a moins de chances de fonctionner qu'une tentative avec un traitement. Mais les tentatives sans aide sont beaucoup plus nombreuses. Et quand ça ne marche pas, on peut toujours réessayer. » |
| « C'est le taux par tentative, et il est bas. » | « Le chiffre est faible. » (seul, sur sa ligne) |

Les charnières restent, et elles restent naturelles : « Mais attention à ce que
mesure ce chiffre », « La raison est simple : », « Et pourtant ». Un agent qui
supprime tous les connecteurs produit un texte clinique, pas un texte naturel.

**Le pivot d'un raisonnement tient sur sa propre ligne.** « Ce n'est pas la même
chose. » Quatre mots, un paragraphe.

### 2. Le paragraphe, pas seulement la phrase

**Cible : 23 à 25 mots de médiane, 29 en plafond.** Une idée, une ligne blanche,
l'idée suivante.

> **Agent** : « La mesure est faite par une machine qui tire des bouffées
> calibrées. Un fumeur ne fume pas comme une machine : la profondeur des
> bouffées, leur fréquence et la position des doigts sur les perforations du
> filtre changent la quantité réellement inhalée. »
>
> **Tim** : « La mesure est faite par une machine qui tire des bouffées
> calibrées.
>
> Un fumeur ne fume pas de cette façon. La profondeur des bouffées, leur
> fréquence et la position des doigts sur les perforations du filtre changent la
> quantité réellement inhalée. »

### 3. Modaliser ce que la source modalise

**Cible : environ 19 modalisateurs pour 1000 mots** quand la source est une
observation, une association, une moyenne. Zéro quand la source constate une
absence totale d'étude : là il n'y a rien à nuancer, et coller des « peut-être »
abîme le texte.

Les mots : généralement, souvent, notamment, semble, peut, selon, environ,
toutefois, plutôt, parfois, nécessairement.

Un agent affirme tout au même niveau. C'est le tic le plus visible.

> **Agent** : « Six mois, c'est la durée minimale de suivi qu'exigent les études
> sérieuses. »
>
> **Tim** : « C'est aussi à cette échéance que les études sur le sevrage
> tabagique évaluent **généralement** la réussite à long terme. »

Note ce que Tim a retiré en même temps : le jugement (« sérieuses »). Il modalise
le fait et supprime l'adjectif qui distribue les bons points.

### 4. La position dans le verdict, le corps reste descriptif

Le haut de page tranche. Le reste décrit et laisse le lecteur conclure.

C'est la règle qui explique pourquoi Tim a gardé « L'hypnose ne fait pas mieux
qu'un arrêt sans aide » en ouverture, et supprimé dans le corps les deux phrases
qui rejouaient le verdict :

- « Sur ce volume d'essais, un effet réel aurait été détecté. »
- « Une méthode testée sur près de 2 000 participants sans jamais prendre
  l'avantage sur rien du tout n'est plus une méthode en attente de preuve. »

Aucune des deux n'est dans la source. **Tout ce qui n'est pas dans la source
part, même quand c'est vrai.**

### 5. L'accusation porte sur l'acte, jamais sur celui qui le commet

Même reproche, sujet grammatical différent. La version de Tim est plus longue et
beaucoup plus difficile à contester.

| Agent | Tim |
|---|---|
| titre « Une caution officielle **inventée** » | titre « Une caution officielle **qui n'existe pas** » |
| « L'affirmation est fausse. » | « **Présenter ce chiffre** comme une recommandation officielle de la Haute Autorité de santé est donc trompeur. » |
| « le secteur ne connaît même pas sa propre étude » | « Aucune boutique consultée ne cite le moindre essai clinique. » |

Cumulable avec `comparatif-neutre` sur les pages qui comparent.

### 6. Sujet et verbe, partout

Les ellipses économisent trois mots et obligent le lecteur à reconstruire le
sujet. Un agent les adore parce qu'elles sonnent « punchy ».

| Agent | Tim |
|---|---|
| « Trois sources indépendantes, le même résultat. » | « Trois sources indépendantes **arrivent donc à** une conclusion similaire : … » |
| « Il donne la quantité contenue dans le flacon, pas la quantité inhalée. » | « **Cela ne signifie pas que** 200 mg seront inhalés. **La quantité effectivement absorbée dépend** notamment de l'appareil utilisé… » |
| « Ce site évalue des méthodes, il ne prescrit pas. » | « Ce site compare des méthodes et des produits ; il ne prescrit pas **de traitement**. » |
| « Preuve très faible. Aucune revue dédiée : … » | « Le laser anti-tabac n'a jamais fait l'objet d'une revue scientifique qui lui soit consacrée. » |

Exception : `redaction-guide` autorise la ligne d'emphase après un fait, dans les
guides et playbooks en ligne claire. Sur une page publiée, non.

### 7. Le mot courant, pas le terme du domaine

Le lecteur est un fumeur, pas un lecteur de revue. Le terme technique se
remplace, ou s'explique dans la phrase.

| Terme du domaine | Écrit pour le lecteur |
|---|---|
| « l'arrêt assisté » | « l'arrêt avec une aide » |
| « les traitements d'aide à l'arrêt » | « les traitements pour arrêter de fumer » |
| « abstinence vérifiée au CO expiré » | « vérifié par une mesure du monoxyde de carbone dans le souffle » |
| « sans groupe placebo » | « personne n'y recevait de faux traitement » |
| « l'auriculothérapie » | « l'auriculothérapie, la variante qui pique l'oreille » |
| « un accompagnement » | « un coach » |
| « écart non significatif » | « un écart trop faible pour être fiable » |
| « la nature de l'écart » (terme du fichier ANSES) | « le problème relevé » |

La règle vaut aussi pour les termes hérités de la donnée source, pas seulement
pour le jargon médical (correction de Tim du 2026-08-22 sur les pages écarts).
Même passe : « simplement » sert de modalisateur d'atténuation quand une donnée
neutre risque une lecture alarmiste (« il décrit simplement le problème relevé »).

Corollaire : quand une notion est nécessaire, l'expliquer coûte deux phrases et
les vaut. C'est ce qui fait monter le nombre de phrases, et c'est voulu.

### 8. Le chiffre remplace l'image

Une image plaquée signale une explication non écrite. La règle complète est dans
`redaction-anti-ia`, avec ses 14 patterns. Le raccourci :

| Imagé | Chiffré |
|---|---|
| « deux fois plus bas que celui affiché **en vitrine** » | « **nettement plus bas : 35 à 40 %** » |
| « vos chances **explosent** » | « votre probabilité de continuer à fumer **chute de 67 %** » |
| « le vert **se mérite** » | « le vert marque les méthodes dont l'efficacité est établie par des essais indépendants » |
| « le marché **vit de** vos rechutes » | « les méthodes les plus chères sont rarement les mieux prouvées » |

---

## Deux réglages de forme qui se voient tout de suite

**Typographie.** `%` et `€` prennent une espace : « 40,1 % », « 350 € ». Un agent
les colle une fois sur deux, ce qui rend l'incohérence visible dans la même page.

**Personne.** Sur une page publiée :

- **vouvoiement** quand la page parle de ce que vit le lecteur (symptômes,
  situations, calculateurs) ;
- **tournure impersonnelle** quand elle évalue un objet (fiches de méthode,
  pages de données) ;
- **jamais de tutoiement**. Le tutoiement appartient aux contenus signés Tim,
  guides et posts, où `ton-de-voix` et `redaction-guide` prennent le relais.

**Intertitres.** Une étiquette ne dit rien. Écrire ce que la section dit, ou la
question que le lecteur se pose.

| Étiquette | Ce que la section dit |
|---|---|
| « À retenir » | « Ce que le même budget achète ailleurs » |
| « Ce que ça coûte » | « Combien coûte une séance de laser anti-tabac ? » |
| « Comment lire ça » | « Ce que l'accompagnement apporte, et à quelle condition » |
| « Le point qui fâche » | « Sa disponibilité en France reste à vérifier » |
| « Les limites honnêtes » | « Ses effets indésirables » |

Un même intertitre répété de fiche en fiche redevient un gabarit. Varier en
restant factuel.

---

## Ce qui n'appartient pas au texte

- **Les renvois de la page à elle-même.** « Ce que cette page donne », « le
  tableau ci-dessus », « c'est le cas d'école de ce site ». Le lecteur voit la
  page, il n'a pas besoin qu'on la lui commente.
- **Les fonctionnalités qui n'existent pas.** Vérifier avant d'écrire « ce site
  propose ». Une phrase de la fiche accompagnement annonçait un assistant
  documentaire qui n'était pas branché.
- **Le vocabulaire de classement interne.** « Preuve forte », « niveau de
  preuve », « statut », « cluster » : ce sont des champs de base, pas du
  français lisible.
- **Les mots bannis** de `ton-de-voix` §3, et le tiret cadratin, nulle part,
  jamais.

---

## Checklist de sortie

Avant de rendre, dans cet ordre :

1. `node mesure.mjs` sur les fichiers touchés. Phrase médiane ≤ 13, paragraphe
   médian ≤ 29, tutoiement à 0, chiffres collés à 0. Viser 11 et 23.
2. Relire chaque chiffre : est-il dans la source, ou déduit ? Un déduit part.
3. Relire chaque intertitre : étiquette ou phrase ?
4. Relire chaque verdict : porte-t-il sur l'acte ou sur la personne ?
5. Chercher `ci-dessus`, `ci-dessous`, `concrètement`, `autrement dit`, `ce site`.
6. Si le repo a un lint de rédaction, le lancer. Un motif qui a traversé la passe
   entre dans le lint, pas dans une consigne répétée.

## Rapport à rendre

Trois lignes, pas plus : la médiane de paragraphe avant et après, ce qui a été
retiré par catégorie, et ce qui n'a **pas** bougé (chiffres, sources, liens,
tableaux). Si un fait a été supprimé, le dire, toujours.

## Voisinage

- `ton-de-voix` — la voix, les positions, le vocabulaire banni. En amont.
- `redaction-guide` — la ligne claire des guides et playbooks, tutoiement, une
  idée par ligne. Pour les documents signés Tim, pas pour les pages publiées.
- `redaction-anti-ia` — la passe de réparation profonde, 14 patterns, quand un
  texte sonne encore faux après celle-ci.
- `comparatif-neutre` — dès qu'une page compare des offres ou des méthodes.
