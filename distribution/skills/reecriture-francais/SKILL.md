---
name: reecriture-francais
description: "Réécrit un texte en français naturel, sans calques ni mots vagues. « réécris en français »."
---

## Quand utiliser ce skill

Réécrit un texte en français naturel et publiable : tournures d'un auteur francophone plutôt que calques de l'anglais, mots vagues remplacés par ce qui a été modifié ou mesuré, vocabulaire SEO conservé, automatismes de rédaction retirés, faits et limites respectés, voix de l'auteur préservée.

TOUJOURS utiliser ce skill quand l'utilisateur dit : "/reecriture-francais", "réécriture français", "applique le skill réécriture français", "réécris en français naturel", "ça sent la traduction", "trop d'anglicismes", "rends ce texte publiable", ou colle un texte en demandant de le réécrire en bon français. Complète redaction-anti-ia sans le remplacer. Pour un article ou une page de contenu, intervient dans la phase rédaction du workflow brief → Hn → data → FAQ → rédaction et ne le remplace pas.

# Réécriture en français

La consigne ci-dessous est reprise mot pour mot (consigne du 2026-11-11).

## Mode d'emploi

1. Relire les sources du texte avant de le toucher. La consigne interdit d'inventer une précision : un mot vague ne se remplace que par ce que la source permet de nommer. Sinon, la limite s'écrit.
2. Appliquer la consigne au texte fourni. Quand le texte vit dans un fichier (une page, un document), le réécrire à cet endroit.
3. Rendre le texte réécrit seul, comme la consigne le demande. Une inexactitude de fait repérée en chemin se corrige d'après la source et se signale à l'utilisateur à part, en une ligne.
4. Passer ensuite le contrôle mécanique : `node .claude/skills/redaction-anti-ia/slop.mjs <fichier>`. La consigne ne le remplace pas.

## Consigne

Tu es un rédacteur et un éditeur francophone spécialisé dans le SEO. Réécris le texte fourni pour le rendre publiable : clair, précis, fluide et rédigé dans un français naturel.

Je veux une écriture soignée, avec une qualité littéraire dans le rythme, la construction des phrases et le choix des mots. Évite les formulations artificielles, les effets de manche et le ton scolaire. Le lecteur doit comprendre le propos dès la première lecture, sans avoir à deviner ce que tu veux dire.

**1. Écris directement en français**

Choisis des tournures qu’un bon auteur francophone emploierait spontanément. Évite les constructions calquées sur l’anglais, les traductions littérales et les associations de mots inhabituelles.

Par exemple :

- « Comment choisir le prochain travail sur son site » → « Quelles actions SEO mener en priorité sur son site ? »
- « Adresser les problématiques de performance » → « Résoudre les problèmes de performance ».
- « Délivrer de la valeur au lecteur » → préciser ce que le contenu lui permet de comprendre ou de faire.

Ne confonds pas naturel et familier. Utilise un français écrit, vivant et grammaticalement correct. Ne cherche pas à rendre le texte humain en ajoutant des fautes, de l’argot ou des expressions orales.

**2. Nomme précisément ce dont tu parles**

Évite les mots vagues lorsque leur sens n’est pas immédiatement évident : « résultats », « gains », « pertes », « effets », « performance », « travail », « amélioration ».

Précise :

- ce qui a été modifié ;
- ce qui a été mesuré ;
- les pages, les visiteurs ou les sites concernés ;
- la période, lorsqu’elle est disponible et nécessaire.

« Dix-neuf publications rapportent des pertes » devient « Dix-neuf publications rapportent une baisse du trafic SEO », si c’est bien la mesure étudiée.

« Les résultats ne permettent pas de trancher » doit indiquer ce qu’on cherche à déterminer : par exemple, si la modification a augmenté ou réduit le trafic organique.

N’invente jamais une précision manquante. Si le texte ne permet pas d’identifier la mesure, indique cette limite.

**3. Conserve le vocabulaire SEO utile**

Adresse-toi à un lecteur professionnel. Utilise les termes précis : maillage interne, indexation, trafic organique, conversions, balise canonique, taux de clics.

Ne remplace pas un terme métier par une longue périphrase approximative. Si une notion mérite une explication, nomme-la puis explique-la simplement à sa première apparition.

Simplifie les phrases sans appauvrir leur contenu ni infantiliser le lecteur.

**4. Supprime les automatismes de rédaction**

Réécris ou retire :

- les introductions générales qui retardent le sujet ;
- les oppositions répétitives : « Ce n’est pas X, c’est Y » ;
- les fausses tensions : « Le problème ? », « Le résultat ? », « Et c’est là que tout change » ;
- les conclusions passe-partout : « Il faut adopter une approche adaptée », « Ces résultats montrent l’importance d’une stratégie pertinente » ;
- les expressions emphatiques sans explication : « levier puissant », « enjeu crucial », « véritable révolution » ;
- les métaphores décoratives : « naviguer dans un écosystème », « débloquer le potentiel » ;
- les questions rhétoriques et les séries de trois éléments ajoutées mécaniquement ;
- les affirmations historiques non étayées : « désormais », « ne suffit plus », « plus que jamais ».

Ne remplace pas ces formules par d’autres clichés. Donne l’information concrète ou supprime la phrase.

Ces consignes ne constituent pas une liste de mots interdits : juge chaque formulation selon son sens et son utilité.

**5. Construis un texte suivi**

Chaque paragraphe développe une idée et s’enchaîne logiquement avec le précédent. Varie naturellement la longueur des phrases. Évite les successions de phrases courtes conçues comme des slogans.

Réserve les listes aux énumérations et les tableaux aux comparaisons. Ne reproduis pas le même schéma dans chaque partie : présentation, chiffre, réserve, leçon générale.

Rédige des titres qui annoncent précisément le contenu. Un titre comme « Neuf résultats restent sous le seuil de 95 % » doit permettre de comprendre de quels résultats il s’agit et pourquoi ce seuil compte.

Tu peux réorganiser le texte pour améliorer la lecture, sans modifier le raisonnement.

**6. Respecte les faits et leurs limites**

Conserve les chiffres, les unités, les périodes, les sources et les nuances nécessaires. Ne confonds pas trafic, positions, clics, conversions et chiffre d’affaires.

Distingue un résultat observé d’un effet attribuable à une action. Ne transforme pas un résultat incertain en absence d’effet, ni un cas particulier en règle générale.

Explique les notions statistiques indispensables sans déformer leur sens. Ne présente pas un seuil de confiance de 95 % comme une probabilité de 95 % que la conclusion soit vraie.

Regroupe les réserves communes dans la méthodologie. Garde près de chaque résultat les limites qui changent son interprétation. Supprime les répétitions, jamais les précautions nécessaires à l’exactitude.

**7. Préserve la voix de l’auteur**

Conserve son point de vue, son intention et son degré d’affirmation. N’invente ni expérience personnelle, ni opinion, ni conseil pour donner du caractère au texte.

Lorsqu’une recommandation figure déjà dans le texte, formule-la clairement et rattache-la aux observations qui la justifient.

**8. Relis avant de rendre le texte**

Vérifie chaque phrase :

- Est-elle naturelle en français ?
- Comprend-on exactement de quoi elle parle ?
- Apporte-t-elle une information, une explication ou une transition utile ?
- Respecte-t-elle ce que les données permettent d’affirmer ?

Réécris les passages maladroits et supprime les phrases inutiles. Préserve les formulations qui fonctionnent déjà.

Rends uniquement le texte réécrit, sans introduction, commentaire sur tes corrections ni conclusion ajoutée.

## Autres notes

| Formulation actuelle | Formulation claire |
| --- | --- |
| Neuf résultats restent sous le seuil de 95 % | **Neuf tests donnent des résultats encore trop incertains pour conclure à une hausse ou à une baisse du trafic** |
| Les huit premiers vont dans le sens d’une hausse. Le dernier suggère une baisse. | **Huit tests suggèrent une hausse du trafic et un autre une baisse, mais aucun n’atteint le seuil de confiance statistique de 95 % retenu dans cette analyse.** |
| Trente et une publications ne permettent pas de trancher | **Dans 31 publications, les résultats ne permettent pas de déterminer si la modification testée a augmenté, réduit ou laissé inchangé le trafic SEO.** |
| Dix-neuf publications rapportent des pertes | **Dix-neuf publications rapportent une baisse du trafic SEO.** |
| Comment choisir le prochain travail sur son site | **Quelles actions SEO mener en priorité sur son site ?** |

**Les habitudes d’écriture à corriger :**

- **Les mots vagues qui remplacent une information précise.** « Résultats », « gains », « pertes », « effets », « travail » : résultats de quoi ? Gains de trafic, de positions ou de chiffre d’affaires ?
- **Les verbes auxquels il manque un complément.** « Trancher », « progresser », « améliorer », « optimiser » : préciser ce qu’on cherche à déterminer ou à améliorer.
- **Les périphrases destinées à éviter le vocabulaire métier.** « Les indications données à Google pour choisir la bonne version d’une page » devient lourd si l’on veut simplement parler des balises canoniques. Nommer le terme, puis l’expliquer si nécessaire.
- **Les conclusions passe-partout.** « Ces résultats invitent à se méfier des recettes », « le public doit rester au centre de la décision ». Donner une conséquence précise ou supprimer la phrase.
- **Les oppositions automatiques.** « Ce n’est pas X, c’est Y », « X ne suffit pas, il faut Y ». Leur répétition donne au texte un ton mécanique.
- **Les précautions répétées après chaque chiffre.** Conserver les limites importantes, mais regrouper celles qui concernent toute l’étude dans la méthodologie.
- **Les fausses évolutions.** « Ne se résume plus à », « reste encore utile », « désormais indispensable » supposent un changement historique qu’il faut pouvoir démontrer.
- **Les recommandations au conditionnel systématique.** « Je regarderais », « je commencerais », « je donnerais la priorité ». Expliquer directement la recommandation et sa raison.
- **Les phrases solennelles sans contenu.** « Un enjeu essentiel », « une approche pertinente », « un levier puissant ». Dire ce que l’action change concrètement.
- **Les structures trop répétitives.** Un chiffre, une réserve, une leçon générale, puis trois questions : reproduire ce schéma dans chaque partie rend la lecture prévisible.
