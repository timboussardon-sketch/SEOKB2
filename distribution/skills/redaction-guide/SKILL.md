---
name: redaction-guide
description: "Rédige guides, playbooks et routines en « ligne claire ». « rédige un guide », « un playbook », « une routine »."
---

## Quand utiliser ce skill

Rédige les guides, playbooks et routines de Tim en « ligne claire » : une idée par ligne,
phrases courtes avec sujet et verbe, la donnée d'abord, saut de ligne entre chaque idée.
Rythme validé par Tim le 2026-07-03 sur le playbook Reddit. Cumule le ton-de-voix
(anti-IA writing, tutoiement) avec la mise en page type thread.

TOUJOURS utiliser ce skill quand Tim demande : "rédige un guide", "un playbook",
"une routine", "un plan d'action", "réécris ce doc en ligne claire", "mise en page
thread", "/redaction-guide", ou quand un livrable long (doctrine, méthode, programme)
doit sortir sous son nom.

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


# Rédaction guide : la ligne claire

Tu rédiges les guides de Tim dans un rythme précis. Il se décrit en une phrase : **une idée par ligne, la donnée d'abord, zéro tissu conjonctif.**

La voix de fond est dans le skill `ton-de-voix`.

## Le rythme, en 7 règles

**1. Une idée par ligne.**
Chaque phrase est un paragraphe. Saut de ligne entre chaque.
Une phrase = un fait, une action ou une conséquence. Jamais deux.

**2. Phrases courtes, mais complètes.**
Sujet + verbe, toujours. 15 mots maximum en moyenne, 25 en plafond.
Une phrase longue se découpe en deux ou trois.
Les fragments nominaux sont interdits (« Compte complété, vieillissement. » = non).
Exception : la ligne d'emphase après un fait (« Et c'est verrouillé par contrat. »), et les listes à deux points qui portent des données.

**3. La donnée ouvre, la source ferme.**
Le chiffre arrive dans les premiers mots, la source entre parenthèses en fin de ligne.
« L'indice Sistrix est monté de 95,1 à 1 370 points. Soit +1 328 % (Sistrix via Amsive, 2024). »
Jamais de chiffre sans source. Jamais d'étiquette avant le fait (« La donnée de cadrage : » = non).

**4. Le contraste en deux lignes.**
Avant / après, hier / aujourd'hui, problème / solution : deux lignes courtes qui se répondent.
« Juillet 2023 : reddit.com est le 68e domaine le plus visible sur Google US. »
« Juillet 2024 : top 5. »

**5. Les listes portent les données, la prose porte le raisonnement.**
Une liste = des faits atomiques ou des actions à l'impératif. Jamais de bullets décoratifs.
Le raisonnement (pourquoi, donc, mais) reste en lignes de prose.

**6. La ligne de chute.**
Chaque bloc se ferme sur la conséquence pratique, pas sur un résumé.
« C'est le levier GEO le plus rentable documenté à ce jour. »
« La machine ne publie jamais. Le clic reste manuel. »

**7. L'impératif pour l'action, l'indicatif pour le fait.**
Les étapes se donnent à l'impératif direct : « Crée le compte. », « Espace tes actions. »
Les faits se constatent à l'indicatif : « Reddit filtre les comptes neufs automatiquement. »
Tutoiement partout.

## La structure d'un guide

1. **Frontmatter YAML** si le doc vit dans le vault (type, tags, created, sources, confidence, status).
2. **Blockquote d'ouverture** : l'objectif en une phrase, la date, le niveau de vérification.
3. **« En résumé (à lire en premier) »** : le guide entier en 10-15 lignes claires.
4. **Sections numérotées**, titres descriptifs et secs (« 10. Shadowban : définition et déclencheurs », pas de punchline).
5. **Tableaux à 2 colonnes maximum** pour les quotas et paramètres (Action | Quota). Pas de colonne justification : la preuve vit dans le texte.
6. **Programmes en phases** avec critère de passage explicite : « Critère de passage : 50 à 100 points. » On ne passe pas à la phase suivante sans le remplir.
7. **Prompts et commandes en blockquote**, prêts à copier.
8. **Les sources à la toute fin**, en dernière section, groupées par thème.

## Les interdits (hérités de ton-de-voix, non négociables)

- Aucune tournure de compilateur : « la mécanique : », « le cadre de risque est », « la conséquence opérationnelle », « les tactiques documentées sont au nombre de », « une donnée de contexte », « la découverte passe par ». Le fait d'abord, directement.
- Aucun passif de compilation : « la détection se fait en » devient « Pour le détecter, ouvre... ».
- Pas de métaphores, pas de personnification, pas de « — », pas d'emojis.
- Pas de mots bannis : karma (dire réputation), marque, territoire, flinguer, visibilité seule (dire citations IA / positions / leads), backlink acheté, concurrent (contexte Fusionn).
- Pas de méta-intro (« Dans ce guide, nous allons voir ») ni de conclusion-résumé.
- Pas de règle de 3 systématique, pas de bold en début de chaque paragraphe.
- Zéro chiffre inventé : [À SOURCER] si la donnée manque.

## Auto-check avant livraison

1. Relis chaque phrase : un expert la dirait-il à voix haute à un autre expert ?
2. Compte les mots des 10 premières phrases : la moyenne dépasse 15 ? Découpe.
3. Cherche les « : » en début de phrase-étiquette : il en reste ? Supprime l'étiquette, garde le fait.
4. Chaque bloc finit-il sur une conséquence pratique ? Sinon, ajoute la ligne de chute ou coupe.
5. Chaque chiffre a-t-il sa source datée ?
6. Le doc passe-t-il les interdits ci-dessus ? Un seul écart = corrige avant de livrer.

## Exemple de transformation

Avant (slope IA) :
« La conséquence opérationnelle est que la contribution précède la promotion, le ratio de référence étant d'environ 90 % de contribution pour 10 % d'autopromo maximum. »

Après (ligne claire) :
« En pratique, tu contribues d'abord. La promotion vient ensuite.
Le ratio de référence : ~90 % de contribution pour 10 % d'autopromo maximum. »
