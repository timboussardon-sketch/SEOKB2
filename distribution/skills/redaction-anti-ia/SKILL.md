---
name: redaction-anti-ia
description: "Relecture qui traque les structures d'écriture IA, pas seulement les mots. « /redaction-anti-ia », « tu écris comme une IA »."
---

# Rédaction anti-IA : traquer la mécanique

## Workflow obligatoire pour toute rédaction et correction (règle du 2026-11-06)

Toujours appliquer **brief → structure Hn → data dans les Hn → FAQ → rédaction**, avec validation explicite de chaque phase avant la suivante. Cela s'applique aussi à une réécriture, à une correction de wording et à une passe anti-IA sur un article ou une page de contenu. La longueur, l'urgence et le caractère mineur de la correction ne permettent pas de sortir du workflow.

Avant toute intervention sur le texte, lire `.claude/skills/seo-workflow-article/SKILL.md` et vérifier les cinq livrables, leurs versions et leurs validations. En reprise, conserver les validations dont le livrable et le périmètre sont inchangés ; rouvrir la phase touchée et faire valider la correction. Un changement de H1/H2/H3 rouvre la structure, une nouvelle donnée rouvre la data, une nouvelle réponse rouvre la FAQ. Une phase absente ou non validée doit être traitée avant les phases qui en dépendent.

`redaction-naturelle` et `redaction-anti-ia` interviennent dans la phase rédaction. Leurs scripts et leurs passes de correction ne remplacent jamais le workflow. Tracer dans le suivi les fichiers, accords explicites, changements et phase courante. Une correction ou un rappel du processus ne vaut pas validation d'un livrable.

## Quand utiliser ce skill

Passe de relecture qui traque la MÉCANIQUE de l'écriture IA, pas seulement les
mots bannis. Un texte peut ne contenir aucun mot de la liste noire et rester
immédiatement reconnaissable comme généré, à cause de ses structures : gabarit
d'intertitres répété, phrases miroir, paragraphes qui se résument eux-mêmes,
« concrètement » en charnière, images plaquées à la place du fait, faux effet
de précision, déduction présentée comme établie par la source, moteur de
démonstration uniforme, schéma accumulation puis doctrine qui résout, écriture
auto-référentielle qui parle de la page au lieu du sujet, citation nue posée à
la place d'un titre. Ce skill donne la procédure de détection (grep +
comptage) et la règle de correction pour chacun. Il s'applique APRÈS
l'écriture, sur le texte produit, et il est cumulable avec ton-de-voix
(qui, lui, cadre l'écriture en amont).

TOUJOURS utiliser ce skill quand l'utilisateur dit : "/redaction-anti-ia", "ça sonne
IA", "c'est écrit comme une machine", "tu écris comme une IA", "relis ce hub",
"revois tous les articles de ce hub", "c'est du gabarit", "passe l'anti-IA
dessus", "ce titre ne veut rien dire", "ça ne veut rien dire", "il y a un
problème dans le ton de voix", "chaque phrase est fabriquée pour faire avancer
une démonstration", "il n'y a aucune phrase naturelle", "tu dois tout
réécrire", ou quand il pointe une phrase précise comme étant de l'écriture IA.
Dans ce dernier cas, ne jamais corriger uniquement la phrase pointée : elle
est presque toujours l'instance visible d'un pattern qui court dans tout le
fichier. On corrige le pattern.

## La règle qui gouverne tout : expliquer, ne pas imager

Une image remplace l'explication par une ressemblance. Le lecteur a la sensation
d'avoir compris, il n'a rien appris. **Quand tu es tenté par une image, c'est
presque toujours que tu n'as pas fini de comprendre le mécanisme.** L'image sert
à masquer ce trou, et c'est pour ça qu'elle sonne IA.

Ce qui est interdit : métaphore, analogie, comparaison, personnification,
vocabulaire emprunté à un autre domaine, idiome corporel.

Ce qui est demandé à la place : **dire ce qui se passe, dans quel ordre, et
pourquoi.** Direct, sans détour par une ressemblance.

| Imagé | Expliqué |
|---|---|
| « te battre au moment du geste, c'est arriver tout à la fin » | « te battre au moment du geste ne change rien aux pensées qui l'ont précédé » |
| « ça se paie » | « le but du combat, c'est de ne plus être tenu par cette habitude » |
| « le texte met le doigt dessus » | « c'est le point du texte » |
| « la première phrase annonce la couleur » | « la première phrase dit déjà l'inverse de ce qu'on en retient » |
| « c'est la certitude qui saute » | « ce qu'il enlève, c'est la certitude » |

**Test avant de valider une phrase** : est-ce qu'elle apprend un fait au
lecteur, ou est-ce qu'elle lui donne l'impression d'avoir compris ? Si c'est la
seconde, l'explication n'est pas écrite. Écris-la.

Deux corollaires :

- **Un verbe figuré est une micro-image.** Une habitude ne s'installe pas, elle
  vient de quelque chose. Une certitude ne saute pas, elle est enlevée. Une
  pensée ne se discute pas, on ne la raisonne pas.
- **Nommer plutôt que désigner.** « Ce qui l'amène » ne désigne rien. Nomme :
  « les pensées ». Voir le pattern 6.

## Règle d'entrée

L'utilisateur pointe une phrase. **La phrase n'est pas le bug, c'est le symptôme.**

Avant de corriger, compte combien de fois le même pattern apparaît dans le
fichier. Si c'est plus de deux, tu as un gabarit, et c'est le gabarit qu'on
corrige. Corriger la seule phrase pointée et rendre le travail est une faute :
L'utilisateur reviendra avec la suivante, et il aura raison.

Exemple vécu (hub éditorial, 2026-08-16) : L'utilisateur pointe
« Actes 5:3 montre une pensée déposée du dehors ». Le comptage donne 34
intertitres sur 55 bâtis sur `Référence + verbe abstrait`, et 16 titres de FAQ
sur 16 bâtis sur `nom, nom, nom`. Le bug était le moule, pas la phrase.

## La procédure

1. **Compter avant de corriger.** `grep -n` sur le champ concerné, lire la
   liste d'un coup. Un gabarit se voit à la colonne, jamais à la ligne.
2. **Mesurer le moteur, pas seulement la forme.** `node mesure.mjs` (dans le
   dossier de ce skill) sort l'histogramme des longueurs d'unité, la part de
   citations nues, les renvois au dispositif de la page, et surtout les deux
   colonnes à lire : toutes les ouvertures d'unité, puis toutes les fins.

   ```
   node .claude/skills/redaction-anti-ia/mesure.mjs <fichier>
   node .claude/skills/redaction-anti-ia/mesure.mjs lib/listes.ts \
     --champ label,note --de 'slug: "ma-page"' --a 'complementTitre'
   ```

   Le script ne détecte pas le pattern 11 et il le dit : aucune regex ne
   sépare « Il les laisse faire » qui conclut de « Il les laisse faire » qui
   constate. Il aligne la colonne, tu tranches. Un script qui répondrait
   « 0 violation » sur ce pattern serait un faux vert.
3. **Supprimer avant de corriger.** La passe destructive ci-dessous. Elle
   passe avant toute réécriture, et elle retire du texte sans le remplacer.
4. **Rouvrir la source** et remonter les faits concrets qui manquent. Voir
   « L'antidote est dans la source » plus bas. Cette étape passe avant toute
   réécriture, sinon la passe produit du style sur du vide.
5. **Corriger le pattern sur tout le fichier**, pas les occurrences signalées.
6. **Varier les formes.** Une correction appliquée à l'identique partout crée
   un nouveau gabarit. Si tu réécris 16 titres, ils doivent avoir des formes
   différentes : question, phrase pleine, énumération de groupes verbaux.
7. **Repasser le lint mécanique.** Le check global, sur n'importe quel
   `.md` / `.html` / `.txt` / `.ts` :

   ```
   node .claude/skills/redaction-anti-ia/slop.mjs <fichier...>
   node .claude/skills/redaction-anti-ia/slop.mjs --strict <fichier...>
   ```

   Il sort 1 sur un HARD (chaîne bannie de la règle mère) et liste les WARN
   (`X, jamais Y`, charnières, conclusions de fin de paragraphe, blocs trop
   réguliers). Plus le lint du repo s'il existe (`npm run check:anti-ai` si ton repo en a un). Ils attrapent tes propres rechutes, et ils en attrapent.

   **Un vert n'est pas un bon à livrer.** Le script cherche des chaînes ; une
   phrase générique sans chaîne bannie passe au vert et doit quand même sauter.
8. **Se relire soi-même.** Les corrections écrites dans l'urgence introduisent
   des images et des tournures fausses. Voir « Ce que tu vas casser en
   réparant » plus bas.
9. **Recompter, et coller le texte dans le chat** avec les trois chiffres
   d'avant et d'après.

---

## La passe destructive (obligatoire, posée le 2026-09-16)

Relis le texte comme un éditeur humain sévère. Pour **chaque phrase**, trois
questions :

1. Apporte-t-elle une information nouvelle ?
2. Est-elle spécifique à ce sujet, à ce client, à cette page ?
3. Un expert aurait-il une raison réelle de l'écrire ?
4. **D'où vient-elle ?** Nommer l'élément de matière source qui la porte : donnée,
   opinion de l'auteur, expérience, exemple, chiffre, fait, argument, observation,
   instruction. Sans réponse, elle est supprimée.

Un non, la phrase est supprimée. La question 4 est la plus coupante : elle attrape
les phrases qui passent les trois premières parce qu'elles sonnent juste.

**Principe de non-complétion.** La passe ne comble jamais le trou qu'elle vient
d'ouvrir. Un trou est préférable à une phrase générique. Si une section perd sa
matière, la laisser courte ou poser `[MATIÈRE MANQUANTE]`. Ne rien ajouter pour
rétablir une longueur, une transition, une introduction, une conclusion ou une
structure homogène entre les sections.

**Règle qui fait toute la valeur de cette passe : ne réécris pas les passages
supprimés.** Le but est de retirer du texte, pas de remplacer du slop par du
slop différent. C'est déjà ma rechute n°1 documentée plus bas (« créer un
nouveau gabarit en appliquant la même correction 16 fois ») : si je m'autorise à
remplacer, je reproduis le défaut sous une autre forme et le comptage reste bon.

Ce que cette passe cherche en priorité, dans l'ordre de visibilité :

- **La conclusion posée à la fin d'une section**, qui explique au lecteur ce
  qu'il vient de lire. Marqueur n°1. Relever toutes les dernières phrases de
  paragraphe et compter celles qui ouvrent par `C'est ce qui`, `C'est aussi`,
  `C'est exactement`, `C'est pour ça`, `Voilà pourquoi`.
- **Les transitions artificielles** entre deux paragraphes qui peuvent se
  suivre sans rien.
- **Les reformulations** d'une information donnée juste avant.
- **Les formules génériques** qui resteraient vraies dans un autre document.
- **Les constructions trop symétriques** : séries de blocs de même longueur et
  de même syntaxe, séries de trois créées pour le rythme. Une série artificielle
  ne se répare pas en variant les phrases, elle se répare en supprimant les
  éléments qui n'avaient rien à dire.

Après la passe, le texte doit être **plus court**. Un rapport de passe
destructive qui annonce un volume stable ou en hausse est un rapport de passe
ratée.

Le texte a le droit d'être irrégulier en sortie : une section de deux
paragraphes à côté d'une section de six, des phrases très courtes, deux
paragraphes qui s'enchaînent sans liant. L'irrégularité est le résultat attendu,
pas un défaut à rattraper.

---

## Les 14 patterns

Les patterns 1 à 10 portent sur la FORME des phrases. Les patterns 11 à 14
portent sur le MOTEUR du texte, et ce sont les plus coûteux : ils survivent à
une passe complète sur les dix premiers. Un texte peut sortir sans un seul
gabarit de forme et rester une machine.

### 1. Le gabarit d'intertitres

Le plus visible, et celui que l'utilisateur voit en premier.

Signature : tous les H2 d'un fichier suivent le même moule. Le cas le plus
fréquent est `Référence + verbe abstrait` :

- ❌ « Jacques 1:15 place la faute après le consentement »
- ❌ « Marc 7:21 vise les intentions, pas les pensées subies »
- ❌ « 2 Corinthiens 10:5 dit quoi faire de la pensée »

C'est un index de machine, pas un titre. Un lecteur qui raconte l'article à
quelqu'un ne dit jamais « Jacques 1:15 place la faute après ». Il dit « Jacques
dit à quel moment ça devient une faute ».

**Règle** : un intertitre nomme ce que le lecteur va lire, dans ses mots à lui.
La référence reste dans la prose, où elle est déjà.

**Détection** : `grep -n 'h2:' fichier` puis regarder la colonne. Si plus de la
moitié commencent par un nom propre, un chiffre ou une référence, c'est un
gabarit.

Corollaire : le titre télégraphique en `nom, nom, nom`.

- ❌ « Pendant la prière, la culpabilité, en parler »

Celui-là ne veut littéralement rien dire : un complément, un nom et un
infinitif collés. Il faut soit une vraie question (« Pourquoi ça arrive surtout
quand tu pries »), soit une énumération grammaticalement homogène (« Porter une
arme, protéger sa famille, porter plainte »).

### 2. Les phrases miroir

Deux propositions bâties sur le même modèle pour produire une phrase qui sonne
forte. Une ou deux dans un texte long, ça passe. Cinq, c'est une signature.

- ❌ « Ananias ment, Judas livre. »
- ❌ « C'est là que se joue la réponse, et c'est là que se mène le combat. »
- ❌ « Le geste vient des pensées, le combat commence là. »
- ❌ « Le commerce reste, l'assurance tombe. »
- ❌ « L'attirance ouvre la séquence, le consentement la referme. »

**Règle** : casser le parallélisme. Écrire les deux faits en phrases de
longueurs différentes, ou n'en garder qu'un.

- ✅ « Ananias garde une partie de l'argent et ment devant toute l'assemblée.
  Judas va voir les chefs des sacrificateurs et fixe un prix. »

### 3. Le paragraphe qui se résume lui-même

L'IA reformule immédiatement ce qu'elle vient d'expliquer, comme pour vérifier
que le lecteur a suivi. C'est la phrase de trop, toujours en fin de paragraphe.

- ❌ « C'est cette obligation-là qu'Onan refuse. » (le paragraphe vient de le dire)
- ❌ « Le geste décrit sert ce refus. »
- ❌ « Le texte tient les deux. »
- ❌ « La conclusion est dans le verset, pas dans la déduction du lecteur. »
- ❌ « L'ordre des responsabilités est écrit dans le texte. »

**Règle** : supprimer. Un raisonnement peut se terminer sur le fait. Si la
conclusion n'est pas évidente sans la phrase de rappel, c'est le raisonnement
qu'il faut reprendre, pas le rappel qu'il faut garder.

### 4. Les charnières de transition

`Concrètement` est le marqueur le plus reconnaissable : principe → «
concrètement » → liste d'actions. Même famille : `En pratique`, `Autrement
dit`, `C'est là que`, `La question est`, `Le point important est`, `Cela
signifie que`, `Il faut noter que`.

**Règle** : maximum une par document, et seulement si elle porte une vraie
rupture. Sinon, attaquer directement sur l'action.

- ❌ « Concrètement, cela veut dire couper ce qui alimente : les contenus… »
- ✅ « Couper les contenus qui montrent des scènes sexuelles, la musique qui en
  parle sans arrêt, les conversations qui y ramènent. »

### 5. L'image plaquée à la place du fait

**Le piège numéro un quand on corrige de l'abstraction.** On remplace une
formule creuse par une image, et on aggrave. Interdiction totale : métaphore,
analogie, personnification, vocabulaire emprunté à un autre univers.

Cas réels produits en corrigeant, tous refusés par l'utilisateur :

| Écrit | Pourquoi c'est refusé | Correction |
|---|---|---|
| « Te battre sur le geste seul, c'est arriver tout à la fin. » | image temporelle à la place du fait | « Si tu ne te bats qu'au moment du geste, tu ne touches pas à ce qui l'amène. » |
| « Ne plus être tenu par une habitude, ça se paie. » | vocabulaire du commerce | « Le but du combat, c'est de ne plus être tenu par cette habitude. » |
| « C'est là que le texte met le doigt. » | idiome corporel | « C'est le point du texte. » |
| « La première phrase annonce la couleur. » | image de jeu de cartes | « La première phrase dit déjà l'inverse de ce qu'on en retient. » |
| « Tu ne restes pas devant elle à la regarder. » | personnification de la pensée | « Tu passes à autre chose, tu ne t'arrêtes pas dessus. » |
| « Il ne demande pas de rester dans la pièce et de serrer les dents. » | idiome | « Il ne demande à personne de rester sur place et de résister. » |
| « C'est la certitude qui saute. » | verbe figuré | « Ce qu'il enlève, c'est la certitude. » |

**Exception** : une image qui appartient à la source citée reste (le chameau et
l'aiguille, le joug), parce qu'on rapporte le texte. On ne l'invente pas.

### 6. Le vocabulaire abstrait posé à la place du concret

Une formule qui « fait sens » à la lecture rapide mais que personne ne dirait,
et qui ne désigne rien de précis.

- ❌ « une pensée déposée du dehors »
- ❌ « deux hommes reçoivent une idée qu'ils n'ont pas cherchée »
- ❌ « décide à l'avance ce qui entre chez toi »
- ❌ « traiter la sortie du processus »

**Test** : est-ce que quelqu'un dirait ça à voix haute à un ami ? Si non, écris
le fait. « Ce qui entre chez toi » devient « regarde le premier épisode avant
eux ». « Deux hommes reçoivent une idée » devient « chez Ananias comme chez
Judas, c'est le passage à l'acte qui est reproché ».

**Sous-cas le plus tenace : le désignateur vague.** Un groupe pronominal qui
occupe la place du sujet réel sans jamais le nommer. Il survit aux relectures
parce qu'il a l'air d'une phrase normale.

- ❌ « te battre au moment du geste ne touche pas à **ce qui l'amène** »
- ❌ « couper **ce qui alimente** »
- ❌ « les conversations qui **y ramènent** »
- ❌ « c'est là que **ça se règle** »
- ❌ « l'habitude **s'installe dans** ce que tu écoutes »

**Règle** : nommer la chose. Si tu ne peux pas la nommer, c'est que tu ne sais
pas de quoi tu parles, et la phrase saute.

- ✅ « te battre au moment du geste **ne change rien à ces pensées** »
- ✅ « l'habitude **vient de** ce que tu écoutes, de ce que tu regardes en série »

### 7. La déduction présentée comme établie par la source

**Le plus grave, parce que ce n'est plus du style.** On prend une interprétation
raisonnable et on l'écrit comme si la source la disait.

- ❌ « La masturbation arrive presque toujours après des pensées sexuelles
  qu'on a laissées tourner. » → « presque toujours » est une affirmation
  psychologique forte, qu'aucun verset cité ne démontre.
- ❌ « Deux choses qui l'accompagnent presque toujours sont nommées »
- ❌ « Si le mariage n'est pas possible maintenant, le combat se mène sur ce que
  tu regardes et sur le temps que tu passes seul » → prescription pastorale
  écrite comme une prescription biblique.

**Règle** : séparer explicitement ce que la source dit de ce qu'on en déduit.
Deux formulations qui marchent : « Regarde d'abord si ton cas ressemble à ça,
parce que le texte ne dit rien de la mécanique » et « Ce qui suit n'est pas dans
les versets, c'est ce qui marche en pratique ».

Chercher : `presque toujours`, `toujours`, `systématiquement`, `dans tous les
cas`, `on sait que`, `il est clair que`, `évidemment`.

### 8. Le faux effet de précision

Des chiffres exacts posés pour donner de l'autorité, sans rapport avec ce
qu'on démontre.

Exemple : une page sur la masturbation qui annonce « esclave apparaît dans 108
versets (77 dans l'Ancien Testament, 31 dans le Nouveau), sur 31 livres ». Le
chiffre est vrai et sourcé. Il ne prouve rien du tout sur la question posée.

**Règle** : un chiffre ne se publie que s'il sert l'argument de la page. Sinon
il donne l'impression d'une recherche exhaustive qui n'a pas eu lieu, et c'est
exactement le reproche qu'on fait à l'IA.

Variante du même défaut : la fausse précision linguistique.

- ❌ « « esclave », le mot que Paul emploie » → Paul écrit en grec. « esclave »
  est le mot français qui le traduit.
- ✅ « le mot français qui traduit le terme employé par Paul »

### 9. Le français approximatif produit en corrigeant

Sous pression, on écrit des tournures qui ne sont pas du français.

- ❌ « tu n'en es nulle part là » → ✅ « tu n'as rien fait de tout ça »

**Règle** : relire à voix haute chaque phrase réécrite. Une phrase qu'on ne
peut pas prononcer n'est pas une phrase.

### 10. Le CTA plaqué en fin d'article

Un article de fond qui se termine par une bascule vers une fonctionnalité du
produit se lit comme du contenu SEO généré.

**Règle** : le CTA reprend le sujet exact de la page et l'état dans lequel le
lecteur finit sa lecture. Il ne recycle jamais la même phrase d'une page à
l'autre. S'il n'y a rien de spécifique à dire, il vaut mieux ne pas en mettre.

- ❌ « Si tu veux arrêter et que tu ne sais pas par où commencer, demande au
  chatbot. » (interchangeable avec n'importe quelle autre page)
- ✅ un CTA qui nomme la situation traitée par cette page-là, et rien d'autre.

### 11. Le moteur de démonstration

Le plus difficile à voir, parce qu'aucune phrase n'est fautive. Chaque unité du
texte est bâtie sur le même moteur : on pose un élément, puis on dit ce qu'il
prouve. Répété vingt fois, ça donne la sensation décrite ainsi : « chaque
phrase a été fabriquée pour faire avancer une démonstration, il n'y a presque
aucune phrase naturelle, aucun moment où l'auteur s'arrête simplement sur le
texte ».

Cas vécu (liste de citations commentées, 2026-08-16) : 28
notes sur 28 suivaient `citation + ce qu'elle établit`. Zéro mot banni, zéro
image, et le texte restait une machine.

**Détection** : prendre les unités du fichier (notes, puces, paragraphes) et
regarder si la dernière phrase de chacune est une conclusion. Si plus de la
moitié concluent, le moteur tourne.

**Règle** : une partie des unités ne doit rien démontrer. Elles racontent ce qui
se passe, elles citent, elles s'arrêtent. Une autre partie a le droit d'être
d'une seule ligne, sans commentaire.

- ❌ « Thomas parle huit jours après la résurrection, devant Jésus. Jésus ne
  reprend pas la formule, ce qui vaut acceptation. »
- ✅ « Thomas avait annoncé qu'il ne croirait pas sans mettre son doigt dans la
  marque des clous. Huit jours passent. Jésus entre, les portes fermées, et lui
  dit d'avancer sa main. »

**Mesure à donner dans le rapport** : l'histogramme du nombre de phrases par
unité. Un texte de machine est plat (`{2: 19, 3: 9}`), un texte écrit respire
(`{1: 3, 2: 7, 3: 7, 4: 6, 5: 4, 6: 2, 8: 1}`).

### 12. L'accumulation qui se dénoue en doctrine

Pattern nommé mot pour mot : « Voici A. Voici B. Voici C. Voici D. Ces
éléments semblent contradictoires. La doctrine X permet de les tenir ensemble. »

On empile des faits, on pose une tension, on sort le concept qui range tout. La
fin est trop propre pour être vraie, et le lecteur sent la mise en scène.

**Règle** : couper le mouvement de résolution. Poser les faits, nommer le
désaccord, et laisser ouvert ce qui est ouvert. Une position peut se donner
comme position, jamais comme dénouement.

- ❌ « Les deux séries de versets sont dans le même Nouveau Testament. Le
  christianisme historique les tient ensemble sous le nom de Trinité. »
- ✅ « Le désaccord porte sur la manière de lire l'ensemble. Les versets, eux,
  sont les mêmes pour tout le monde. »

### 13. L'écriture auto-référentielle

On écrit sur la page au lieu d'écrire sur le sujet. Le rédacteur a la structure
sous les yeux, le lecteur non : il arrive de Google et ne sait pas ce que « la
liste » désigne, ni qui est ce « on ».

Le tell le plus net est un titre ou une phrase d'ouverture qui suppose un cadre
jamais posé.

- ❌ « Les versets qu'on cite en face » (en face de quoi ? qui est « on » ?)
- ❌ « Ces versets-là sont cités contre la liste, et ils sont dans le texte. »
- ❌ « c'est la formulation affichée sur ce site »
- ❌ « expliqué plus haut sur cette page »
- ✅ « Jésus dit aussi « le Père est plus grand que moi » »
- ✅ « La phrase est de lui, à ses disciples, le soir de son arrestation. »

**Détection** : `grep -c` sur `cette liste`, `de la liste`, `ci-dessus`, `plus
haut sur cette page`, `sur ce site`, `affiché ici`, `en face`, `comme on l'a
vu`, `nous allons voir`. Chaque occurrence se réécrit en parlant du sujet.

**Attention** : une référence interne au TEXTE SOURCE reste légitime (« trois
versets plus haut », « le verset d'après »). Ce qui saute, c'est la référence au
DISPOSITIF de la page.

### 14. La citation nue posée à la place d'un titre

Recopier la source au lieu de dire ce qu'elle fait. Le lecteur doit lire la
suite pour comprendre pourquoi l'élément est là.

Cas vécu, même fichier : 25 libellés sur 28 étaient un verset entre guillemets.

**Règle** : le libellé dit ce que la citation fait. La citation descend dans le
corps, où elle est déjà sourcée. On garde le format citation seulement quand les
mots exacts portent toute la charge.

- ❌ « Ton trône, ô Dieu, est éternel » → ✅ Le Père s'adresse au Fils et
  l'appelle Dieu
- ❌ « Je sais qui tu es : le Saint de Dieu » → ✅ Un esprit impur le nomme « le
  Saint de Dieu »

---

## L'antidote est dans la source, pas dans le style

Quand un texte n'a « aucune aspérité », la réponse n'est pas d'écrire mieux.
C'est de retourner lire la source et d'en rapporter le détail concret qu'on
n'avait pas lu.

Sur la liste des versets, les seuls passages qui ont cessé de sonner IA sont
ceux où j'étais allé lire les versets d'à côté : le toit découvert au-dessus du
paralytique (Marc 2:4), l'hiver et le portique de Salomon (Jean 10:22-23), « Tu
n'as pas encore cinquante ans » (Jean 8:57), le vent qui cesse quand ils
remontent dans la barque (Matthieu 14:32).

Aucun de ces détails n'était accessible en réécrivant. Il fallait relire.

**Règle** : avant toute passe de style sur un texte jugé fabriqué, rouvrir la
source et remonter cinq faits concrets qui n'y sont pas encore. S'il n'y en a
aucun, c'est le travail de documentation qui n'a pas été fait, et aucune
réécriture ne le remplacera.

---

## Ce que tu vas casser en réparant

Les trois rechutes observées, dans cet ordre de fréquence :

1. **Remplacer une abstraction par une image** (pattern 5). C'est pire que le
   défaut initial. Le fait se décrit littéralement.
2. **Créer un nouveau gabarit** en appliquant la même correction 16 fois.
   Varier les formes est une obligation, pas un raffinement.
3. **Écrire du français approximatif** (pattern 9), parce qu'on écrit vite pour
   réparer vite.
4. **Corriger le pattern signalé et laisser tourner le moteur** (pattern 11).
   Sur la liste des versets, la première passe a fait tomber le gabarit de
   libellés de 25 à 6 et a cassé le rythme des notes. Le texte sonnait toujours
   IA, parce que chaque note continuait de démontrer quelque chose. Un gabarit
   de forme peut disparaître pendant que le gabarit d'argument reste.
5. **Remplacer une auto-référence par une autre** (pattern 13). « contre la
   liste » devient « en face », qui ne veut rien dire non plus. La sortie n'est
   pas une reformulation, c'est de parler du sujet.
6. **Déplacer le gabarit d'un cran au lieu de le supprimer.** Sur la liste des
   versets, les citations nues sont passées de 25 libellés sur 28 à 6 sur 30.
   Mesure faite après coup sur le champ voisin : les notes ouvrant sur une
   citation étaient montées de 1 sur 28 à 11 sur 30. Le moule avait changé de
   champ. Toujours mesurer le champ d'à côté après avoir corrigé un champ.

Relire ses propres corrections fait partie de la passe. Ce n'est pas fini quand
les occurrences signalées sont traitées.

## Quand l'utilisateur dit « tu dois tout réécrire »

Il ne demande pas une passe de plus. Il demande de repartir du contenu, pas du
texte existant : rouvrir la source, refaire le plan, réécrire chaque unité sans
regarder l'ancienne. Retoucher les phrases pointées puis rendre un rapport de
deux corrections est une faute, et il le dira.

---

## Checklist de sortie

- [ ] Compté les occurrences du pattern avant de corriger, pas seulement traité
      la phrase signalée ?
- [ ] **Passe destructive faite avant toute réécriture, et le texte est plus
      court en sortie ?** (donner le nombre de signes avant / après)
- [ ] Aucun passage supprimé n'a été remplacé par une reformulation ?
- [ ] Zéro conclusion de section qui explique ce qu'on vient de lire
      (`C'est ce qui`, `C'est aussi`, `C'est exactement`, `C'est pour ça`) ?
- [ ] Zéro phrase générique qui resterait vraie sur un autre client ou un autre
      sujet ?
- [ ] Les séries de blocs ont des longueurs inégales ?
- [ ] Aucun gabarit d'intertitre : les H2 du fichier ont des formes variées ?
- [ ] Aucun titre télégraphique `nom, nom, nom` ?
- [ ] Moins de deux phrases miroir sur tout le document ?
- [ ] Aucun paragraphe qui se résume lui-même en dernière phrase ?
- [ ] Une seule charnière (`concrètement`, `en pratique`, `autrement dit`) au
      maximum, ou zéro ?
- [ ] Aucune métaphore, analogie ou personnification introduite par la
      correction ?
- [ ] Chaque formule abstraite passe le test « quelqu'un dirait ça à voix
      haute » ?
- [ ] Chaque `presque toujours` / `systématiquement` est démontré par la source
      citée, ou explicitement donné comme une observation hors source ?
- [ ] Chaque chiffre sert l'argument de la page ?
- [ ] Aucune confusion entre le mot français et le terme de la langue d'origine ?
- [ ] Chaque phrase réécrite se prononce à voix haute sans buter ?
- [ ] Le CTA est spécifique à cette page ?
- [ ] Moins de la moitié des unités finissent sur une conclusion, et
      l'histogramme des longueurs est dispersé ?
- [ ] Au moins trois unités ne démontrent rien et s'arrêtent sur le fait ?
- [ ] Aucune accumulation qui se dénoue en doctrine ou en concept qui range
      tout ?
- [ ] Zéro renvoi au dispositif de la page (`cette liste`, `ci-dessus`, `sur ce
      site`, `en face`) ?
- [ ] Les titres et libellés disent ce que la source fait, sans se contenter de
      la recopier entre guillemets ?
- [ ] Cinq faits concrets remontés de la source relue, absents de la version
      précédente ?
- [ ] Le lint mécanique du repo repasse au vert (`npm run check:anti-ai` si ton repo en a un) ?

## Rapport à rendre

Donner le comptage, pas l'adjectif. « 34 intertitres sur 55 suivaient
`Référence + verbe abstrait`, 16 titres de FAQ sur 16 suivaient `nom, nom,
nom` » se vérifie. « J'ai amélioré le ton » ne se vérifie pas.

**Coller le texte réécrit dans le chat.** L'utilisateur juge de l'écriture, pas du code :
il doit lire les avant/après sans ouvrir un fichier ni un serveur. Donner un
lien local à la place lui fait perdre le tour.

**Ne jamais lancer un build pendant qu'un serveur de dev tourne.** Sur un site Next.js,
`npm run build` et `next dev` écrivent dans le même `.next`, et le serveur se
met à servir une version périmée sans rien signaler. Une version que j'avais déjà remplacée. Si un serveur doit servir de preuve, le
redémarrer et vérifier le HTML servi avec un `curl | grep` sur une phrase de la
nouvelle version.

## Voisinage

- `ton-de-voix` : cadre l'écriture **avant**. Liste des mots bannis,
  positions, tutoiement. Ce skill-ci nettoie **après**, sur la mécanique.
- `redaction-guide` : mise en page « ligne claire » des guides et playbooks.
- Si ton repo a un `AGENTS.md` et un script de lint anti-IA, ils portent les
  interdits durs et en vérifient mécaniquement une partie au build. Un check mécanique vaut mieux qu'une consigne répétée : quand un
  pattern est automatisable, l'ajouter au script plutôt qu'à une doctrine.
