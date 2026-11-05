---
type: methode
title: "Connecter Keyword Planner au système : le prompt pour les élèves"
aliases: [keyword-planner-api-eleves, prompt-keyword-planner]
tags: [methode, keyword-planner, google-ads, bootcamp, systeme]
created: 2026-10-22
updated: 2026-10-22
sources: 1
confidence: medium
status: draft
---

# Connecter Keyword Planner au système

Prompt à coller tel quel dans le terminal (Claude Code), à la racine du système SEO. Claude guide l'élève étape par étape et écrit le script. Calqué sur le connecteur Google Ads de Qadence (`supabase/functions/google-ads/index.ts`, API REST v22, `generateKeywordIdeas`, langue 1002 = français, zone 2250 = France).

Ce que l'élève doit avoir avant de commencer : un compte Google, un compte Google Ads (gratuit, sans campagne ni budget), un navigateur. Le token développeur en accès de base est validé par Google sous quelques heures à quelques jours : c'est la seule attente de la procédure.

## Le prompt

```
Je veux connecter Google Keyword Planner à mon système SEO par l'API Google Ads, pour que les skills de recherche de mots-clés et d'audit lisent les volumes et les CPC à la source, sans export CSV. Guide-moi étape par étape, une étape à la fois, et attends ma confirmation avant de passer à la suivante. Ne devine aucune valeur : si une étape échoue, montre-moi le message exact et dis-moi quoi vérifier.

Étape 1 : le compte Google Ads. Vérifie avec moi que j'ai un compte Google Ads sur ads.google.com (sans campagne ni budget, c'est suffisant). Demande-moi l'identifiant client à 10 chiffres affiché en haut à droite (format 123-456-7890). Si mon compte est un compte administrateur (MCC), demande-moi aussi l'identifiant du compte administrateur.

Étape 2 : le token développeur. Explique-moi où le demander : Google Ads, Outils, Configuration, Centre API, demande d'accès de base. Dis-moi que l'accès test ne permet pas d'appeler Keyword Planner sur des données réelles et qu'il faut attendre l'accès de base. Demande-moi de te coller le token quand je l'ai.

Étape 3 : le projet Google Cloud. Guide-moi pour créer un projet sur console.cloud.google.com, activer l'API « Google Ads API », configurer l'écran de consentement OAuth en mode externe avec mon adresse comme utilisateur test, puis créer un identifiant OAuth de type « application de bureau ». Demande-moi le client ID et le client secret.

Étape 4 : le refresh token. Écris un script Python local (fichier scripts/google-ads-auth.py) qui ouvre mon navigateur sur l'autorisation Google avec la portée https://www.googleapis.com/auth/adwords, récupère le code sur http://localhost:8085, l'échange contre un refresh token et me l'affiche. Utilise uniquement la bibliothèque standard et requests. Lance-le, puis attends que je te colle le refresh token.

Étape 5 : le fichier .env. Écris ces cinq variables dans .env à la racine du système, et ajoute .env au .gitignore s'il n'y est pas :
GOOGLE_ADS_DEVELOPER_TOKEN=
GOOGLE_ADS_CLIENT_ID=
GOOGLE_ADS_CLIENT_SECRET=
GOOGLE_ADS_REFRESH_TOKEN=
GOOGLE_ADS_CUSTOMER_ID=
et GOOGLE_ADS_LOGIN_CUSTOMER_ID= seulement si je passe par un compte administrateur. Ne les affiche jamais dans tes réponses.

Étape 6 : le script Keyword Planner. Écris scripts/keyword-planner.py qui :
- lit .env, obtient un access token depuis le refresh token (POST https://oauth2.googleapis.com/token) ;
- appelle POST https://googleads.googleapis.com/v22/customers/{CUSTOMER_ID}:generateKeywordIdeas avec les en-têtes developer-token, Authorization: Bearer, et login-customer-id si défini ; corps : language languageConstants/1002, geoTargetConstants geoTargetConstants/2250, keywordPlanNetwork GOOGLE_SEARCH, keywordSeed avec mes mots-clés (20 maximum par appel) ; option --url pour une graine URL ; options --langue et --pays pour changer les constantes ;
- écrit planner.json dans le dossier client passé en argument, au format que lit top20.py : {"quand": date ISO, "sources": ["google-ads-api"], "idees": {mot-clé: {"volume": entier, "cpc_low": euros, "cpc_high": euros, "competition": texte}}, "exacts": {}} ; les enchères arrivent en micros, divise par 1 000 000 ; une métrique absente reste null, jamais inventée ;
- ajoute une commande --exacts qui appelle generateKeywordHistoricalMetrics sur ma liste et remplit "exacts" ;
- affiche un tableau lisible en sortie : mot-clé, volume mensuel, CPC bas, CPC haut, concurrence.

Étape 7 : le test. Lance python3 scripts/keyword-planner.py . "consultant seo" "agence seo" et montre-moi le tableau. Si l'API répond DEVELOPER_TOKEN_NOT_APPROVED, dis-moi que l'accès de base n'est pas encore validé et arrête-toi là. Si elle répond ACCESS_TOKEN_SCOPE_INSUFFICIENT, refais l'étape 4. Si elle répond que la version v22 n'existe plus, cherche la version courante dans la documentation Google Ads API et remplace-la.

Étape 8 : brancher les skills. Mets à jour le fichier de contexte du système pour que les skills de recherche de mots-clés et l'audit (onglet mots-clés business) appellent scripts/keyword-planner.py quand .env contient GOOGLE_ADS_DEVELOPER_TOKEN, et reviennent à l'export CSV sinon. Résume-moi en cinq lignes ce qui a été installé et où.
```

## Ce que l'élève doit savoir

Le quota de l'accès de base est de 15 000 opérations par jour, largement suffisant pour un consultant. Les CPC sont dans la devise du compte Google Ads : un compte en euros évite toute conversion. Le refresh token d'une application en mode test expire au bout de sept jours tant que l'écran de consentement n'est pas publié ; publier l'application (sans validation Google, portée adwords acceptée) lève cette limite.

## Lié

[[methodes/demande-observee]] · skill `kw-research-workflow` (phase 1, export CSV) · `audit-complet-v2/planner_csv.py` (même format `planner.json`)
