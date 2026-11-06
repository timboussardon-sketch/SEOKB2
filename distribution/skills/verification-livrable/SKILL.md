---
name: verification-livrable
description: "Vérificateur indépendant d'une tâche profonde, avant de la dire terminée. « vérifie le livrable », « contrôle qualité »."
---

# Vérification d'un livrable

## Quand utiliser ce skill

Contrôle qualité indépendant d'une tâche profonde (recherche de mots-clés, audit SEO, brief, stratégie, roadmap, clustering, modèles de pages, rédaction de page). Lance un sous-agent vérificateur qui relit le livrable point par point contre la demande, les skills utilisés et les règles du projet, et rend un tableau de verdict avec une ligne de compte. La réponse finale recopie ce tableau ET donne le lien du dashboard de suivi du projet : les deux vont toujours ensemble. TOUJOURS utiliser ce skill avant d'annoncer qu'une tâche profonde est terminée, et quand l'utilisateur dit « vérifie le livrable », « lance le vérificateur », « contrôle qualité », « c'est vraiment fini ? ».

## La règle

Une tâche profonde n'est finie que lorsque deux choses sont dans la réponse finale, ensemble :

1. le dernier tableau du vérificateur, recopié tel quel, avec sa ligne `✅ X | ❌ 0 | ⚠️ X` ;
2. le lien cliquable du dashboard de suivi du projet (skill `tableau-de-bord-projet`), vérifié juste avant.

L'un ne va jamais sans l'autre. Avant ça, ne pas écrire « terminé », « fait », « livrable prêt ».

Tâche profonde : tout travail produit avec un de ces skills ou un équivalent : recherche de mots-clés, clustering, mots-clés décisionnels, audit SEO, pré-audit, cannibalisation, maillage, stratégie SEO ou GEO, roadmap, modèles de pages, brief de contenu, rédaction d'une page. Une question rapide ou une petite correction n'en est pas une.

## La boucle

1. Faire le travail.
2. Lancer le vérificateur : un sous-agent (outil Agent, type `general-purpose`) dont le prompt commence par le contenu complet de `verificateur.md` (dans ce dossier), puis les six sections du gabarit ci-dessous, remplies en entier.
3. Corriger chaque ❌, et chaque ⚠️ qui peut l'être.
4. Relancer le vérificateur sur la nouvelle version. Un tableau ne vaut que pour la version qu'il a vérifiée : dès qu'un livrable change, il faut un nouveau passage.
5. Recommencer jusqu'à 0 ❌. Chaque ⚠️ restant doit être une vraie limite, expliquée.
6. Vérifier que le dashboard du projet répond (`curl -s -o /dev/null -w "%{http_code}" http://localhost:<port>/`), le relancer s'il est arrêté.
7. Réponse finale : le dernier tableau recopié tel quel, sa ligne de compte, puis le lien du dashboard.

Pour rendre la main en cours de route (question bloquante, accès manquant), écrire `⏸ TÂCHE PROFONDE EN COURS`, sans formule de fin.

## Gabarit du prompt du vérificateur

Le sous-agent démarre sans l'historique de la conversation : tout ce qu'il doit savoir est dans son prompt.

```
### DEMANDE UTILISATEUR
<la demande exacte, recopiée, et les précisions données ensuite>

### TYPE DE TÂCHE
<recherche de mots-clés | audit SEO | brief | stratégie | roadmap | clustering | modèles de pages | rédaction>

### SKILLS UTILISÉS
- <chemin absolu de chaque SKILL.md utilisé pendant la tâche>

### LIVRABLES À VÉRIFIER
- <chemin absolu de chaque fichier produit ou modifié>

### SOURCES ET DONNÉES UTILISÉES
- <exports, Search Console, transcripts, fichiers clients, SERP lue, avec chemins ou dates>
- <fichiers intermédiaires, marqués « intermédiaire »>

### CONTRAINTES PARTICULIÈRES
- <chaque consigne de l'utilisateur absente des skills ; « aucune » si aucune>
```

## Format de la réponse finale

```
**Dernier passage du vérificateur**

| # | Point vérifié | Exigence/source | Statut | Preuve |
|---|---|---|---|---|
| … | … | … | ✅ | … |

✅ X | ❌ 0 | ⚠️ X

**Dashboard de suivi du projet : http://localhost:<port>**
```

Sous le tableau, une ligne par ⚠️ restant : ce qu'il veut dire et qui doit trancher.
