---
type: query
title: Extension « Cité par les IA » : plan technique pour le dev
tags: [geo, extension, chrome, citations-ia, produit]
created: 2026-10-22
updated: 2026-10-22
sources: 0
confidence: medium
status: draft
---

> Objectif : une extension Chrome qui dit, sur la page ouverte, si son URL est citée par ChatGPT, Perplexity et l'AI Overview Google sur ses requêtes principales. Plan à juger par le dev. Rédigé le 2026-10-22, non testé.

## En résumé (à lire en premier)

L'extension ne demande jamais à un modèle s'il cite la page. Elle pose de vraies requêtes et lit les citations renvoyées.

Trois moteurs, trois lecteurs de citations : API Perplexity, API OpenAI avec recherche web, SERP Google parsée.

Un backend fait tout le travail. L'extension n'envoie que l'URL et affiche le résultat.

Chaque URL est vérifiée une fois, puis mise en cache. La première personne paie la mesure, les suivantes lisent.

Chaque résultat est daté et compté : « citée sur 3 des 10 requêtes, 2 tirages sur 3, le 22/10 ».

Le cache par URL devient la base de données propriétaire du produit.

## 1. Architecture

Extension Chrome Manifest V3. Un service worker, un popup, aucun content script au départ.

Le popup envoie l'URL de l'onglet actif au backend et affiche la réponse.

Backend Node ou Python, une seule API publique : `POST /check { url }`.

Base Postgres. Tables : `pages`, `queries`, `runs`, `citations`.

File de jobs pour les mesures (BullMQ, ou une table `jobs` au début).

Aucune clé API dans l'extension. Toutes les clés vivent côté serveur.

## 2. Flux d'une vérification

1. Le popup envoie `POST /check { url }`.
2. Le backend normalise l'URL : https, sans paramètres de tracking, sans fragment, trailing slash unifié.
3. Si un résultat existe en cache et date de moins de 7 jours, il est renvoyé tout de suite.
4. Sinon, le backend crée un job et renvoie `{ status: "pending", job_id }`.
5. Le popup interroge `GET /check/:job_id` toutes les 2 secondes.
6. Le job termine en 20 à 60 secondes selon le nombre de requêtes et de tirages.

Critère de passage pour le MVP : une URL passe de « pending » à un résultat affiché sans intervention manuelle.

## 3. Trouver les requêtes principales de la page

Le backend télécharge la page et extrait title, H1, H2, meta description.

Sans GSC, il fabrique 5 à 10 requêtes à partir de ces éléments. Le title nettoyé devient la requête 1. Chaque H2 formulé en question devient une requête.

Un appel LLM peut reformuler les H2 en questions. Il ne doit jamais ajouter de requête absente de la page.

Avec GSC, l'utilisateur connecte son compte via OAuth Google. Le backend prend les 10 requêtes avec le plus d'impressions sur l'URL, 28 derniers jours.

Le popup affiche d'où viennent les requêtes : « déduites de la page » ou « GSC ».

Sans GSC, le résultat porte un avertissement visible. Les requêtes sont supposées, pas mesurées.

## 4. Les trois lecteurs de citations

### 4.1 Perplexity

API Perplexity, modèle Sonar. La réponse contient un tableau `citations` avec les URL sources.

Un appel par requête. Pas de parsing HTML.

### 4.2 ChatGPT

API OpenAI, Responses API, outil `web_search` activé.

La réponse contient des annotations `url_citation` avec l'URL de chaque source.

Un appel par requête. Le résultat reflète la recherche web d'OpenAI, pas l'interface ChatGPT grand public. Le popup le dit en toutes lettres.

### 4.3 AI Overview Google

Aucune API. Il faut ouvrir la SERP Google FR et parser le bloc AI Overview et ses liens sources.

Réutilise la machine Fly Paris de serp-vitrine. Chromium complet, profil persistant, c'est la seule configuration qui passe le captcha chez nous ([[project_serp_vitrine]]).

Le bloc AI Overview ne s'affiche pas sur toutes les requêtes. Le résultat distingue « pas d'AI Overview » et « AI Overview sans citation de la page ».

Les sélecteurs CSS du bloc changent sans préavis. Prévois un test quotidien sur 3 requêtes témoins qui alerte quand le parseur rend zéro source.

## 5. Comparer

Une citation compte si l'URL source, normalisée comme en étape 2, est égale à l'URL de la page.

Une deuxième ligne de résultat compte les citations du domaine entier. Elle sert quand la page n'est pas citée mais qu'une autre page du site l'est.

Les redirections comptent. Si la source renvoie une URL qui redirige vers la page, c'est une citation.

## 6. Répéter les tirages

Une réponse IA change d'un appel à l'autre.

Chaque requête est posée 3 fois par moteur. Le résultat est une fréquence : « 2 tirages sur 3 ».

Les 3 tirages se font avec les mêmes paramètres, même pays, même langue.

Un tirage unique ne s'affiche jamais comme un verdict.

## 7. Format du résultat

```json
{
  "url": "https://exemple.fr/page",
  "checked_at": "2026-10-22T10:00:00Z",
  "queries_source": "page" | "gsc",
  "queries": [
    {
      "text": "comment choisir un consultant seo",
      "perplexity": { "cited": 2, "runs": 3 },
      "chatgpt": { "cited": 0, "runs": 3 },
      "aio": { "present": true, "cited": 1, "runs": 3 }
    }
  ],
  "domain_cited": { "perplexity": 5, "chatgpt": 1, "aio": 2 }
}
```

Le popup affiche trois lignes, une par moteur. Chaque ligne donne « cité sur X des N requêtes ». Le détail par requête s'ouvre au clic.

## 8. Cache et coût

Clé de cache : URL normalisée.

Durée de vie : 7 jours. Un bouton « revérifier » force une nouvelle mesure, limité à une par URL et par jour.

Coût par vérification sans cache : 10 requêtes × 3 moteurs × 3 tirages = 90 appels. Prix unitaire par moteur [À SOURCER sur les grilles API du jour].

Le MVP réduit à 5 requêtes et 2 tirages, soit 30 appels, le temps de mesurer le coût réel.

Limite par utilisateur anonyme : 10 vérifications par jour, identifiées par un ID d'installation généré par l'extension.

## 9. Ce qui fait la base propriétaire

Chaque run stocke la requête, le moteur, la date, toutes les URL citées, pas seulement celle vérifiée.

Après quelques milliers de vérifications, la table `citations` dit quels domaines les IA citent sur quelles requêtes en France.

C'est le futur produit payant. L'extension gratuite le remplit.

## 10. Risques à trancher avec le dev

Le parsing Google peut casser à tout moment. C'est le seul composant sans API. Prévois de pouvoir couper l'AI Overview du popup sans casser le reste.

Les conditions d'utilisation de Google interdisent le scraping automatisé. Risque à évaluer avant lancement.

Le résultat ChatGPT via API ne reproduit pas l'interface grand public. Si le dev veut l'interface, il faut un navigateur automatisé avec compte, bien plus fragile.

La page peut bloquer le téléchargement par le backend. Prévoir un fallback où l'extension envoie le title et les H2 lus dans l'onglet.

## 11. Ordre de construction

1. Backend `POST /check` avec Perplexity seul, requêtes déduites de la page, 1 tirage. Critère de passage : une URL connue renvoie un résultat correct vérifié à la main.
2. Popup Chrome qui affiche ce résultat.
3. Ajout OpenAI.
4. Cache et limites par utilisateur.
5. Ajout AI Overview via la machine Fly.
6. Tirages multiples et fréquences.
7. Connexion GSC.

Rien ne se publie sur le Chrome Web Store avant l'étape 4.

## Sources

Aucune source externe citée. Les comportements d'API décrits (`citations` Perplexity, `url_citation` OpenAI) sont à confirmer par le dev sur la documentation du jour avant de coder.
