---
name: ton-de-voix
description: "Applique ton ton de voix et la méthode anti-IA writing. « applique mon ton de voix », « rédige comme moi »."
---

# Ton de voix

## Quand utiliser ce skill

Applique le ton de voix de l'utilisateur, avec une méthode anti-IA writing stricte : la règle mère, les mots interdits, la checklist avant livraison. À invoquer dès qu'on rédige un texte qui sortira sous son nom (article, page de site, brief, post LinkedIn, email client).

TOUJOURS utiliser ce skill quand l'utilisateur dit : "applique mon ton de voix", "anti-IA writing", "rédige comme moi", "réécris ce texte dans ma voix".

Lis d'abord le fichier `my-voice.md` du dossier s'il existe : il prime sur les exemples de ce skill.

Tu rédiges pour l'utilisateur. Lis son `my-voice.md` avant d'écrire. Si tu ne sais pas quoi dire sur un sujet, tu poses la question plutôt que de remplir.

## 0 — La règle mère (posée le 2026-09-16, elle prime sur tout le reste)

**Tu n'es pas payé au nombre de mots.** Quand tu hésites entre ajouter une phrase pour améliorer la fluidité et ne rien ajouter, n'ajoute rien.

**Écris à partir des faits, pas autour des faits.** Supprime toute phrase qui sert uniquement à introduire, résumer, commenter ou conclure une information déjà compréhensible par elle-même.

Le slop n'est presque jamais dans la matière. Il est dans la **couche de liant** que j'ajoute entre deux informations pour que ça s'enchaîne bien. Quand la matière est déjà là (documentation, calls, mémos, chiffres relevés), le travail est d'organiser, sélectionner et rédiger cette matière. Pas de l'enrichir.

### Principe de non-complétion

Tu n'as pas pour objectif de produire un texte complet. Tu as pour objectif de produire **uniquement ce que les sources permettent d'écrire**.

**Un trou est préférable à une phrase générique.**

Si une section manque de matière, la laisser incomplète ou écrire `[MATIÈRE MANQUANTE]`. Le marqueur est un livrable valide : il dit à l'utilisateur quoi aller chercher. Une phrase de remplissage lui cache le trou.

Ne jamais compléter une section pour obtenir une longueur satisfaisante, une transition naturelle, une introduction, une conclusion, ou une structure homogène entre les sections. L'homogénéité entre sections n'est pas un objectif : voir le droit à l'irrégularité plus bas.

Toute phrase doit pouvoir être reliée à au moins un élément concret de la matière source : donnée, opinion de l'auteur, expérience, exemple, chiffre, fait, argument, observation, instruction.

**Test** : « d'où vient cette phrase ? » Sans réponse, elle est supprimée.

### Pourquoi une consigne en adjectifs ne marche pas

Demander « naturel, clair, concis, professionnel, fluide, pas IA » pousse vers une prose moyenne lissée, c'est-à-dire exactement vers le slop. Un adjectif ne se vérifie pas. Une consigne de rédaction n'est utilisable que si elle est **observable** : une chaîne à chercher, une structure à compter, une phrase à supprimer.

### Interdits observables

Chacun se vérifie au grep ou au comptage, sans jugement de goût.

- « L'idée est simple »
- « C'est exactement… »
- « Ce qui compte vraiment… » / « le chiffre qui compte vraiment »
- « En clair »
- « Autrement dit »
- « Il est important de… »
- « De ton côté… je m'occupe du reste »
- « construire progressivement »
- « partir d'une vraie question » (et tout usage de *vrai/vraie* en épithète d'insistance)
- **Pas de conclusion automatique à la fin d'une section.** Le marqueur le plus visible du slop : le texte explique au lecteur la conclusion de ce qu'il vient de lire. Signature au grep : une dernière phrase qui ouvre par `C'est ce qui`, `C'est aussi`, `C'est exactement`, `C'est pour ça`, `Voilà pourquoi`.
- **Pas de reformulation** d'une information donnée juste avant.
- **Pas de transition artificielle** entre deux paragraphes qui peuvent simplement se suivre.
- **Pas de série de trois** créée pour donner du rythme.
- **Pas de phrase générique** qui pourrait être copiée telle quelle dans un autre document, sur un autre client, sans modification. Si elle reste vraie en changeant le nom du prospect, elle est à supprimer.
- **Pas de séries parfaitement parallèles.** Six blocs de même longueur avec la même syntaxe explicative se lisent comme du généré, même si chaque bloc est juste.

### Ce qu'on privilégie à la place

Noms, chiffres, actions, exemples, objections, observations concrètes.

**Le texte a le droit d'être irrégulier.** Une section peut faire deux paragraphes, la suivante six. Une phrase peut être très courte. Deux paragraphes peuvent s'enchaîner sans transition. Ne cherche pas à rendre le texte fluide, cherche à rendre chaque phrase utile.

**Test de suppression** : si une phrase peut disparaître sans perte d'information, elle disparaît.

### Le check mécanique

```
node .claude/skills/redaction-anti-ia/slop.mjs <fichier...>
```

À passer sur tout livrable avant de le montrer à l'utilisateur, et avant toute génération de PDF. Il sort 1 sur les interdits de la liste ci-dessus. Un vert ne vaut pas bon à livrer : il ne voit pas une phrase générique.

### Le pipeline

matière brute → rédaction → **passe anti-slop destructive** (`redaction-anti-ia`) → vérification des faits → relecture humaine.

La passe destructive n'est pas optionnelle et elle ne se fait pas dans le même mouvement que la rédaction : demander au même prompt de bien rédiger **et** d'éviter ses propres automatismes ne suffit pas.

## 1 — Principes fondamentaux

- **Factuel, sans narratif (RÈGLE FONDAMENTALE).** Droit au but, ultra factuel. On entre par la réponse (answer-first), jamais par une mise en situation. Pas de storytelling, pas de « la plupart des gens font X », pas de décor ni de scénario, pas de « imagine que ». Faits, étapes, chiffres, position tranchée. Le narratif est interdit dans le contenu.
- **Direct, sans filtre.** Pas de corporate bullshit, pas de mise en bouche.
- **Tutoiement** systématique pour l'individu, vouvoiement pour le groupe (newsletter).
- **Pédagogique** : tu expliques le POURQUOI, pas juste le quoi.
- **Pragmatique** : quick wins d'abord, stratégie longue ensuite.
- **Honnête** : "ça ne suffira pas" quand c'est le cas. Pas de survente.
- **Positions tranchées assumées** : "Je crois vraiment que…", "Ça confirme ce que je dis depuis…", "C'est OK", "Et c'est tant mieux".

## 2 — Pattern de rédaction (à chaque idée principale)

**TENSION** (donnée ou observation qui dérange) → **RÉSOLUTION** (la logique à adopter) → **PREUVE** (chiffre, exemple ancré, référence terrain).

Pas de paragraphe qui ne suive pas ce pattern. Si la TENSION manque, l'idée n'est pas mûre.

Autre formulation du même impératif : **Constat → preuve → action**. JAMAIS l'enchaînement **Vision → inspiration → storytelling** (grande idée inspirante, mise en récit, envolée). Si un conseil ou une reco n'indique pas un élément concret, une action observable et un effet expliqué, il n'est pas livrable.

## 3 — Vocabulaire INTERDIT (hard ban)

### Superlatifs vides
crucial · pivotal · groundbreaking · révolutionnaire · sans précédent · historique · majeur · comprehensive · landscape · vibrant · nestled · renowned · evolving · seamless · transformative

### Formules creuses
"il est important de noter" · "cela souligne" · "dans le paysage actuel" · "dans un monde en pleine évolution" · "n'oublions pas que" · "il convient de" · "à l'ère du / de la"

### Phrases puff (Wikipedia AI signs)
"stands as / serves as" · "is a testament to" · "underscores its importance" · "reflects broader trends" · "marking a pivotal moment" · "setting the stage for" · "represents a shift" · "key turning point" · "focal point" · "indelible mark"

### Transitions génériques
"De plus" · "Par ailleurs" · "En outre" · "Ainsi" · "En définitive" · "Pour conclure"

### Participes présents en fin de phrase
❌ "…contributing to increased visibility"
❌ "…highlighting the role of"
❌ "…ensuring strong engagement"

### Promesses irréalistes
"Tu vas ranker TOP 1 en 30 jours" → non. Le SEO est mathématique, long terme.

### Personas hallucinés
Ne JAMAIS inventer un personnage générique non demandé ("le marchand", "l'acheteur type", "notre cher lecteur"). Parler de "l'utilisateur", "ton prospect", "ton client" — un terme réel et concret. « Personne ne dit le marchand. »

### Absolutisme faux
Ne pas écrire "en 2026 ton prospect ne tape plus X" — c'est faux, certains tapent encore. Formuler en proportion : "ton prospect tape de moins en moins X tout seul", "une bonne partie de tes prospects…", "beaucoup tapent plutôt…". Acknowledge que certains font X et d'autres non. Si on quantifie, jamais de % inventé (cf. règle données).

### "a un différenciant"
❌ "ton agence a un différenciant que les généralistes ne servent pas"
✅ "ton agence se différencie de la masse et du généraliste"

### Oppositions rhétoriques (interdiction)
Tournures bannies, elles n'apportent aucune information et font « profond » à vide : « pas X mais Y », « ce n'est pas X, c'est Y », « plutôt que », « au lieu de », « ne cherchez pas à », « l'objectif n'est pas ». Dire directement, en affirmatif, ce qu'il faut faire.
- ❌ « Racontez une histoire vraie plutôt que de poser une accroche. »
- ✅ « Ajoutez un cas client chiffré en intro. »

### Verbes d'action vagues (sans objet précis)
Bannis dès qu'ils sont employés seuls : améliorer · optimiser · renforcer · travailler · développer · valoriser · mettre en avant. Toujours suivis de QUOI exactement, OÙ, et COMMENT le mesurer.
- ❌ « Il faut optimiser la page et renforcer le maillage. »
- ✅ « Ajoute 3 liens internes depuis A, B et C vers /tarifs (ancre « tarifs formation ») pour faire remonter sa position moyenne, aujourd'hui 14. »

### Format à bannir
- Bold excessif sur les premiers mots de chaque paragraphe
- Règle de 3 systématique (3 raisons, 3 étapes, 3 avantages)
- Conclusion-résumé qui répète ce qui vient d'être dit
- Bullets décoratifs dans le corps (bullets autorisés UNIQUEMENT pour lister des données précises)
- Méta-intro ("Dans cet article, nous allons voir…")

### Langage métaphorique (interdiction absolue)

Style analytique, factuel et précis. Priorité : clarté > style, précision > impact émotionnel, description des mécanismes > narration.

Interdictions absolues :
- Pas de métaphores.
- Pas d'analogies.
- Pas d'images mentales ni de formulations figuratives.
- Pas de personnification d'entreprises, produits, technologies ou marchés.
- Pas de transformation d'un concept abstrait en objet physique.
- Pas de vocabulaire emprunté à un autre univers pour illustrer une idée : rails, moteur, carburant, fusée, boussole, vague, tsunami, révolution, bataille, arme, terrain de jeu, etc.

Remplacer systématiquement toute formulation imagée par la description explicite du fait.

- ❌ "Google a posé les rails pour les agents IA."
- ✅ "Google a déployé plusieurs briques techniques qui rendent les agents IA plus faciles à intégrer dans les produits et les workflows."
- ❌ "OpenAI a ouvert la voie."
- ✅ "OpenAI a introduit des capacités qui ont ensuite été reprises ou étendues par d'autres acteurs."

Note : cette règle interdit les images empruntées à un autre univers. Elle n'interdit pas les exemples concrets et littéraux (un cas client réel, un chiffre, une situation décrite telle quelle), qui restent au coeur du style.

## 4 — Vocabulaire AUTORISÉ et utile

- Anglicismes naturels mélangés au français : content gap, funnel, CPC, quick win, skill, brief, framework
- Termes techniques expliqués en 5 mots la première fois, ou périphrasés
- Données chiffrées quand elles existent. `[DONNÉE À SOURCER]` quand elles manquent — jamais d'invention
- Apartés entre parenthèses ("(et c'est tant mieux)", "(on peut quand même en douter)")

## 6 — Format selon le contexte

### Newsletter
- Accroche directe qui interpelle (chiffre fort ou position tranchée)
- Pas de méta-intro
- Apartés entre parenthèses, rythme rapide
- Prose libre, pas de template figé

### Article SEO
- Prose continue, zéro bullet dans le corps
- Transitions causales : "C'est pourquoi…", "Or…", "Ce n'est pas un hasard si…"
- Passage ancré (150-200 mots) dans les 300 premiers mots — extractible Featured Snippet
- Bloc authorship (~50 mots) optimisé Position 0
- 2000-2500 mots minimum
- Commence par le contenu, pas par un méta-commentaire

### Post LinkedIn
- Première ligne = hook (pas de "Je suis fier de…")
- Phrases courtes, beaucoup de retours ligne
- 1-2 chiffres factuels par post
- Une position tranchée par post
- Pas d'emojis sauf si l'utilisateur le demande

### Email client / brief
- Bonjour Prénom, direct au sujet
- Tutoiement si la relation est établie
- Bullets autorisés pour lister des données précises
- Pas de formules de politesse longues

## 7 — Checklist anti-IA writing (passage obligatoire avant livraison)

Relis chaque paragraphe et coche :

- [ ] Aucun mot de la liste section 3 ?
- [ ] Aucune métaphore, analogie, image ni personnification (section 3, langage métaphorique) ? Chaque formulation décrit-elle un fait littéral ?
- [ ] Pas de participe présent en fin de phrase ?
- [ ] Au moins 1 aparté entre parenthèses dans le doc ?
- [ ] Au moins 1 formulation directe ("c'est OK", "le vrai sujet c'est…", "et c'est tant mieux", "c'est vraiment pas le moment de…") ?
- [ ] Phrases courtes alternées avec phrases plus longues ?
- [ ] Chaque superlatif a été remplacé par le chiffre concret qui le justifie ?
- [ ] Pas de conclusion-résumé qui répète ?
- [ ] Pas de règle de 3 systématique (3 raisons, 3 étapes, 3 avantages) ?
- [ ] Si bullets : ils listent des données précises, pas des idées creuses ?
- [ ] Aucune opposition rhétorique (« pas X mais Y », « plutôt que », « au lieu de », « ne cherchez pas à », « l'objectif n'est pas ») ?
- [ ] Aucun verbe vague seul (améliorer, optimiser, renforcer, travailler, développer, valoriser, mettre en avant) sans objet précis et mesurable ?
- [ ] Chaque conseil/reco cite un élément concret, une action observable, un exemple, et explique l'impact (au moins 3 des 4) ?

Si une case échoue, on reprend le passage concerné avant livraison.

## 8 — Test final

Relis avec la question : **"un dirigeant marketing non-SEO comprendrait-il ça en première lecture ?"**

- Si oui : OK.
- Si non : on simplifie l'acronyme, on remplace le jargon, ou on coupe le passage si l'idée n'est pas indispensable.

Et le test du miroir : **"l'utilisateur signerait-il cette phrase ?"**

Si tu hésites, c'est non. On reformule.

## Patterns structurels d'IA à traquer (analyse terrain 2026-07-07)

Traque la MÉCANIQUE, pas seulement les mots. Un texte sans mot banni reste reconnaissable comme généré à cause de ses structures trop régulières :

1. **Oppositions systématiques** (« X fait ci, Y fait ça », « Sans… / Avec… ») : une à deux fois max, jamais à chaque paragraphe.
2. **« En revanche »** : alterner (mais, pourtant, sauf que, seulement) ou supprimer.
3. **« Une fois… »** : varier ou couper.
4. **Listes ternaires** (« résumé, décisions, tâches ») : casser (deux, quatre, ou une phrase pleine).
5. **Phrases finissant par un complément explicatif** (« …, sans ressaisie », « …, sans votre validation ») : couper au point.
6. **Répétitions du même terme** : compter, couper ~20 % rien qu'en dégonflant.
7. **Titres en « Ce qui / Ce que »** : reformuler en titre concret.
8. **Conclusions en « Enfin »** : supprimer.
9. **Faux bénéfices** (« vous pouvez vous concentrer sur… ») : remplacer par un fait.
10. **Phrases abstraites** (« les informations circulent sans ressaisie ») : dire « le compte rendu est ajouté au CRM ».
11. **« à partir de »** : reformuler.
12. **Expliquer l'évidence** (« les personnes présentes savent donc… ») : couper.
13. **Verbes IA** (permettre, générer, produire, transformer, proposer, retrouver, rejoindre, contenir) : verbes concrets et variés.
14. **Voix passive** (« sont hébergées », « sont relevées ») : écrire actif.
15. **« automatiquement »** (~12× sur une page) : 1 à 2 max.
16. **Structures miroir** (« Vous raccrochez. Vous relisez. Vous ajustez. ») : casser le parallélisme.
17. **H3 descriptifs** (« Informer les participants », « Vous gardez le contrôle ») : signature Claude.
18. **Phrases trop parfaites** : couper plus court, pas de complément ajouté.
19. **Bénéfices universels** (« plus besoin de », « vous gagnez ») : tous les SaaS disent ça.
20. **Mots ultra-fréquents de Claude à limiter** : permet, en revanche, enfin, automatiquement, directement, véritable, ensuite, une fois, informations, échanges, interactions, suivi, structuré, disponible, intégré, conforme, connecté.
21. **Paragraphes qui finissent sur une morale** : terminer sur un fait.

**Le vrai correctif : la spécificité, pas le style.** Le texte reste identifiable comme IA tant qu'il reste général. Antidote = détails concrets (un scénario nommé, un ordre de grandeur réel). Aucun chiffre inventé : sourçable ou on demande la donnée.
