---
name: brief-matin
description: "Brief du matin centré sur tes décisions : faits sourcés, inférences marquées, fait hier, à décider, questions. « brief du matin », « qu'est-ce que je décide »."
---

# Brief du matin

Lit ton coffre et écrit, en moins de 400 mots, ce que tu dois trancher aujourd'hui.

## Quand utiliser ce skill

« /brief-matin », « brief du matin », « qu'est-ce que je dois décider aujourd'hui », « décisions en attente ».
Aucune tâche planifiée n'est installée : lance-le en début de journée, ou planifie-le toi-même.

## Sources, dans cet ordre

Noter l'heure du relevé de chaque source.

1. `wiki/pilotage/` : suivi du projet, prochaine action, priorités que tu as **déclarées**.
2. `wiki/log.md` : entrées depuis le dernier brief.
3. `git log --since="24 hours ago" --oneline` si le coffre est un dépôt git : travail **fait**.
4. `wiki/corrections-recurrentes.md`, s'il existe : lignes passées `récurrente`.
5. `wiki/reponses/` : brouillons du skill `reponse-fil` pas encore validés.
6. Le dernier brief, pour ne pas répéter une décision sans dire depuis quand elle attend.

Messagerie et agenda : seulement si un connecteur est disponible et autorisé dans la session. Sinon, ne pas les citer comme vérifiés.

## Format

Fichier `wiki/pilotage/brief-matin/AAAA-MM-JJ.md`, frontmatter du coffre (`type: register`).
N'écrire une section que si elle a du contenu.

```
# Brief du AAAA-MM-JJ

## À décider
- <choix exact> — <fichier concerné> — <pourquoi aujourd'hui>

## Faits
- <changement> — source : <chemin> — relevé <HH:MM>

## Inférences
- (inférence) <implication possible>, à partir de <faits>

## Fait hier
- <fichier ou commit produit> — <chemin ou hash>

## Questions
- <information manquante qui bloque un travail utile>
```

## Règles

- **À décider** passe en premier. Une décision est un choix précis : « Valider le brouillon de réponse à X dans `wiki/reponses/…` », pas « Suivre la prospection ».
- Engagements confirmés et échéances datées d'abord.
- Séparer tes priorités déclarées de ce que l'activité laisse supposer. Le temps passé sur un projet est un fait d'activité, pas une priorité : le marquer en inférence.
- Une inférence porte le mot « (inférence) ». Jamais de fait sans source.
- Une source illisible s'écrit telle quelle dans Faits, avec les éléments touchés.
- Rien de neuf : « Rien de nouveau depuis le brief du <date>. Sources lues : … ».
- Aucune action externe : pas d'envoi, pas de publication, pas de modification en dehors du brief.

Contrôle avant de finir :

```
node .claude/skills/redaction-anti-ia/slop.mjs wiki/pilotage/brief-matin/AAAA-MM-JJ.md
```

Le dashboard du coffre affiche le dernier brief en tête de sa page d'accueil.
