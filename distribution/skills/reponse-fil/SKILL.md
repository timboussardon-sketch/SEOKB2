---
name: reponse-fil
description: "Prépare ta réponse à un fil d'emails : demande, engagements sourcés, manques, brouillon. N'envoie jamais. « prépare la réponse », « il m'a répondu »."
---

# Réponse à un fil

Prépare ta réponse à un fil d'emails ou de messages (prospect qui répond à une campagne, client, partenaire) à partir de ce que ton coffre sait de l'interlocuteur.

## Quand utiliser ce skill

« /reponse-fil », « prépare la réponse », « réponds à ce fil », « il m'a répondu », « qu'est-ce que je lui réponds », « traite les réponses de la campagne X », ou un échange collé avec la question de quoi répondre.

## Ce que le skill rend, dans cet ordre

1. **La demande** de l'interlocuteur, en une phrase.
2. **Engagements déjà pris**, chacun avec sa source (chemin de fichier, ID de message, date). Aucun engagement sans source.
3. **Ce qui manque** pour répondre. Une source inaccessible s'écrit telle quelle : « la note dit vendredi ; le dernier message n'a pas pu être ouvert ».
4. **À trancher**, hors du brouillon : toute date, tout prix, tout livrable ou tout rendez-vous qui n'est pas déjà un engagement sourcé. Formuler le choix exact.
5. **Le brouillon**, dans ta voix.

Les notes de travail restent séparées du texte du message.

## Étape 1 — Lire le fil

- Depuis Gmail si un connecteur est disponible et autorisé dans la session : relever ID, expéditeur, date, objet de chaque message.
- Ou le texte collé dans la conversation.

Vérifier d'abord que c'est une vraie réponse. Accusés de réception, réponses automatiques, « adresse inactive » et rebonds se classent à part, sans brouillon.

Conserver qui a dit quoi. Ne jamais t'attribuer une phrase de l'interlocuteur, ni l'inverse.

## Étape 2 — Retrouver le contexte

Chercher par nom de la personne, de l'entreprise et par domaine (`rg -il "<nom>" wiki raw`) :

- `wiki/` : fiche de la personne, notes de call, pré-audit, proposition, suivi du projet (`wiki/pilotage/`).
- `raw/` : emails et notes d'origine.
- Agent prospect, si tu l'utilises : le mail exact que le prospect a reçu (objet, accroche, chiffres cités).

La réponse ne contredit pas le mail envoyé. Elle ne cite aucun chiffre qui n'y est pas ou qui n'est pas dans une source du coffre.

Les faits qui changent (date de livraison, prix, disponibilité, paiement) se relisent dans leur source actuelle. Noter la source et l'heure du relevé.

## Étape 3 — Rédiger

- Appliquer le skill `ton-de-voix`. Le meilleur échantillon de voix est le mail que tu as déjà envoyé dans ce fil.
- Répondre à la demande réelle, pas à une version élargie.
- Pas de formule d'ouverture générique quand le fil est déjà engagé.
- Une proposition nouvelle (« je peux vous montrer la page jeudi ») reste au point 4 tant que tu ne l'as pas validée.
- Un trou se signale au point 3, jamais par une phrase de remplissage dans le brouillon.

Contrôle mécanique avant de montrer :

```
node .claude/skills/redaction-anti-ia/slop.mjs <fichier>
```

## Étape 4 — Enregistrer et montrer

Fichier : `wiki/reponses/AAAA-MM-JJ-<interlocuteur>.md`, frontmatter du coffre, avec les cinq blocs et un wikilink vers la fiche de l'interlocuteur.
Campagne traitée en lot : un fichier par interlocuteur, plus `wiki/reponses/AAAA-MM-JJ-<campagne>-tri.md` (vraies réponses, réponses automatiques, rebonds).

Montrer le brouillon dans la conversation.

## Limite

- N'envoie jamais. Un brouillon dans la messagerie seulement sur demande explicite.
- Fil incomplet : demander le contexte manquant avant de proposer un engagement.

## Contrôles avant de rendre la main

1. Qui a dit quoi est-il conservé ?
2. Le brouillon répond-il à la demande réelle ?
3. Les propositions nouvelles sont-elles séparées des engagements déjà pris ?
4. Chaque engagement a-t-il sa source ?
5. `slop.mjs` passe-t-il ?

Quand tu corriges un brouillon d'une façon qui doit valoir pour la suite, noter la règle dans `wiki/corrections-recurrentes.md` (date, thème, correction, `isolée` ou `récurrente`).
