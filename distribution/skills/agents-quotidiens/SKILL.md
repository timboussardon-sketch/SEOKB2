---
name: agents-quotidiens
description: "Alertes Search Console chaque matin (pertes de trafic, de positions) et récap simple de la journée le soir, par Gmail ou WhatsApp. « alertes SEO », « récap du jour »."
---

# Agents quotidiens : alertes SEO et récap du jour

## Quand utiliser ce skill

« /agents-quotidiens », « alertes SEO », « alertes Search Console », « perte de trafic », « perte de positions », « récap du jour », « récap de la journée », « mets en place les alertes », « envoie-moi les alertes sur WhatsApp ».

Deux agents :

- **Alertes**, une fois par jour, à partir de 9 h. L'agent compare les 7 derniers jours disponibles dans la Search Console aux 7 jours d'avant. Il ne fait aucun appel à une IA, ce qui le rend gratuit. Il envoie un message seulement s'il y a une nouvelle alerte.
- **Récap**, une fois par jour, à partir de 20 h. Il tient en 5 à 10 lignes et liste les actions de la journée. Sa matière : les commits du coffre, les notes de `wiki/` et `raw/` modifiées, et la première demande de chaque session Claude Code ouverte sur le coffre.

## Ce que déclenche une alerte

| Alerte | Condition |
|---|---|
| Trafic | clics du site −25 % (au moins 20 clics la semaine d'avant), ou impressions −30 % (au moins 300) si le site a peu de clics |
| Page | une page perd 30 % de ses clics ou n'en a plus aucun (au moins 20 clics la semaine d'avant) |
| Top 10 | une page du top 10 en sort : elle disparaît des résultats, ou passe au-delà de la 10e place en perdant au moins 2 places (au moins 100 impressions) |
| Position | une requête du top 20 perd plus de 3 positions (au moins 50 impressions la semaine d'avant) |
| Donnée | aucune donnée Search Console depuis 5 jours sur un site qui en avait |

Sous ces seuils, l'agent ne conclut rien : sur de petits volumes, le bruit l'emporterait. Une même alerte n'est pas renvoyée pendant 6 jours. Le message liste au plus trois alertes par type et par site. La Search Console a 2 à 3 jours de retard : une alerte décrit donc la semaine qui finit deux ou trois jours avant le message.

## Mise en place

Faire les étapes dans l'ordre et poser les questions en QCM. Ne demander de saisie libre que pour les informations propres à l'élève : adresse, mot de passe, numéro, clé.

1. **Canal** : demander « Gmail », « WhatsApp » ou « les deux ».
2. **Réglages** : les écrire dans `.env.local`, à la racine du coffre. Ne jamais les écrire dans une note, dans un commit ou dans la conversation.

```
# Agents quotidiens SEOKB2
CANAL=gmail                          # gmail, whatsapp, ou gmail,whatsapp
GSC_CREDENTIALS=/chemin/vers/identifiants-gsc.json
ALERTES_SITES=                       # vide = toutes les propriétés visibles ; sinon exemple.fr,autre.fr
ALERTES_HEURE=9
RECAP_HEURE=20
FUSEAU=Europe/Paris
AGENTS_QUOTIDIENS=alertes,recap      # retirer l'un des deux pour ne garder que l'autre

GMAIL_ADRESSE=
GMAIL_MOT_DE_PASSE_APPLICATION=
ALERTES_DESTINATAIRE=                # vide = GMAIL_ADRESSE

WHATSAPP_NUMERO=                     # format international : +336…
CALLMEBOT_APIKEY=
```

   - **Search Console** : `GSC_CREDENTIALS` pointe vers le fichier d'identifiants OAuth en lecture seule déjà utilisé par `reporting-client` (`client_id`, `client_secret`, `refresh_token`, `quota_project_id`). Sans ce fichier, seul le récap peut tourner : mettre `AGENTS_QUOTIDIENS=recap`.
   - **Gmail** : activer la validation en deux étapes du compte Google, puis créer un mot de passe d'application sur https://myaccount.google.com/apppasswords. Ce mot de passe de 16 caractères sert seulement à cet envoi : ce n'est pas le mot de passe du compte. Le message part de l'adresse Gmail de l'élève vers elle-même.
   - **WhatsApp** : l'envoi passe par CallMeBot, un service tiers gratuit pour un usage personnel. Ce n'est pas l'API officielle de WhatsApp. La procédure à suivre est sur https://www.callmebot.com/blog/free-api-whatsapp-messages/ : ajouter le numéro du robot à ses contacts, lui envoyer le message d'autorisation, puis recopier la clé reçue dans `CALLMEBOT_APIKEY`. Dire à l'élève que le texte des alertes transite par ce service. Un message WhatsApp est coupé vers 1 500 caractères ; le rapport complet reste dans le coffre.
3. **Test** : lancer la vérification. Elle signale les réglages manquants, ajoute `.env*` au `.gitignore` si le coffre est un dépôt git, puis envoie un message de test.

```
python -X utf8 .seokb/runtime/agents_quotidiens.py verifier
```

4. **Passage à blanc** : lancer un calcul seul, sans envoi, pour montrer à l'élève ce que les agents lui enverraient.

```
python -X utf8 .seokb/runtime/agents_quotidiens.py alertes --sec
python -X utf8 .seokb/runtime/agents_quotidiens.py recap --sec
```

5. **Planification, après accord explicite de l'élève** : demander « Je pose la tâche qui lance les deux agents chaque jour ? » (Oui / Non, je les lance moi-même). Seulement sur un oui :

```
python -X utf8 .seokb/runtime/agents_quotidiens.py planifier
```

   La tâche se réveille toutes les heures, à la cinquième minute : LaunchAgent sur Mac, Planificateur de tâches sur Windows, cron sur Linux. À chaque réveil, chaque agent vérifie s'il a déjà tourné dans la journée et si son heure est passée. Un ordinateur éteint à 9 h envoie donc les alertes au premier réveil qui suit. Si l'ordinateur était éteint à 20 h, le récap de la veille part le lendemain matin, avant midi. Il ne tourne rien quand l'ordinateur dort.

   Sur Mac, si le coffre est dans Documents, sur le Bureau ou dans iCloud Drive, macOS peut bloquer la tâche. Après le premier passage, vérifier `.seokb/agents-quotidiens/logs/`. Si rien n'y est écrit, déplacer le coffre hors de ces dossiers ou lancer les agents à la main.

   Pour arrêter : `python -X utf8 .seokb/runtime/agents_quotidiens.py retirer`.

Sous Windows, remplacer `python` par `py -3` si la commande `python` n'existe pas.

## Lancer à la main

« alertes du jour » : `agents_quotidiens.py alertes`. « récap du jour » : `agents_quotidiens.py recap`. Chaque commande écrit son rapport dans `wiki/pilotage/alertes/AAAA-MM-JJ.md` ou `wiki/pilotage/recap/AAAA-MM-JJ.md`, puis l'envoie sur le canal choisi.

## Récap : d'où viennent les lignes

Si la commande `claude` est disponible, le récap est condensé par Claude Code avec le modèle le moins cher (haiku), à partir des seuls commits, notes et demandes du jour. Sinon, ou si Claude ne répond pas, le message part avec la liste brute : les premiers commits, le nombre de notes modifiées et le nombre de sessions. Les commits automatiques (`auto: WIP`, `(auto)`) sont écartés.

## Garde-fous

- L'agent n'écrit jamais dans la Search Console : l'accès est en lecture seule.
- Les messages ne partent que vers l'adresse ou le numéro de l'élève.
- Les secrets restent dans `.env.local`. La sauvegarde du coffre exclut ce fichier.
- Un seuil se change dans `SEUILS`, en tête de `.seokb/runtime/alertes_gsc.py`, uniquement à la demande de l'élève. Une mise à jour de SEOKB2 remet les valeurs d'origine.
- État et traces : `.seokb/agents-quotidiens/` (`etat.json`, `logs/`).
