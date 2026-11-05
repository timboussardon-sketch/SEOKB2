---
type: methode
title: Audit GSC ponctuel depuis un chat Codex Cloud
aliases: [audit-gsc-mobile, gsc-cloud-ponctuel]
tags: [gsc, audit, automatisation, cloud]
created: 2026-10-24
updated: 2026-10-24
sources: 2
confidence: high
status: draft
---

# Audit GSC ponctuel depuis un chat Codex Cloud

Dans l'application ChatGPT du téléphone, ouvrir **Codex**, choisir **Cloud**, puis l'environnement publié `seo-kb`. L'environnement est lié une fois au dépôt GitHub `timboussardon-sketch/seo-kb` : les nouvelles tâches lancées dedans retrouvent le dépôt et son `AGENTS.md`. Le message peut alors être « Audite la GSC d'Organikk sur 28 jours ». Le Mac n'a pas besoin d'être allumé. Un chat ChatGPT ordinaire hors de cet environnement n'a pas automatiquement accès au dépôt.

Le skill `gsc-cloud-audit` du dépôt oriente cette demande vers une lecture GSC en accès restreint. Son script compare deux périodes consécutives de même longueur : par défaut, les 28 derniers jours disponibles avec les 28 jours précédents. Il produit les totaux du site et les pages à examiner. Ces filtres servent au tri ; ils ne prouvent aucune cause et ne déclenchent aucune modification de page. Voir [[moc/doctrine-seo-reference]] et [[methodes/rapport-audit-seo-format]].

## Configuration unique sur le web ou dans l'application de bureau

1. Ouvrir **Settings → Codex Cloud → Environments → Create environment**. Choisir le dépôt privé `timboussardon-sketch/seo-kb`, puis laisser Codex préparer l'environnement. L'installation doit inclure `google-auth[requests]` pour le script du skill.
2. Réutiliser le compte `organikk-gsc-reader@organikk-gsc.iam.gserviceaccount.com` du projet Google Cloud `organikk-gsc`. Sa clé locale existe dans `~/.config/organikk-gsc/service-account.json` et l'API Search Console est activée. Le test du 24 octobre 2026 renvoie 403 sur `sc-domain:organikk.co` : dans Search Console, un propriétaire doit l'ajouter comme utilisateur **Restreint** de cette propriété. Voir [[preuves/SETUP-GSC]]. N'envoyer sa clé ni dans le chat ni dans le dépôt.
3. Dans la configuration de l'environnement, ajouter `GSC_SERVICE_ACCOUNT_JSON` comme **variable personnelle** contenant le JSON du compte de service. Ce format doit être une variable lue par le script pour signer la requête Google. Garder l'environnement privé (« Only me »).
4. Autoriser l'accès réseau aux domaines `oauth2.googleapis.com` et `searchconsole.googleapis.com`, tester une requête en lecture, puis publier l'environnement.

## Utilisation sur téléphone

Ouvrir **Codex → Cloud → seo-kb** dans l'app ChatGPT et écrire « Audite la GSC d'Organikk sur 28 jours. Sauve la source et la synthèse dans le wiki. » Le skill du dépôt donne au chat le script et les règles de sourcing. Codex montre le rapport et les fichiers créés avant validation.

Les notes sont d'abord dans l'espace de travail cloud. Elles apparaissent dans l'Obsidian du Mac **après** validation des changements sur GitHub et synchronisation du dépôt local. Le Mac éteint ne reçoit pas les fichiers en direct.

## État au 24 octobre 2026

Le script et le skill sont publiés sur GitHub. L'appel réel à GSC a confirmé que le compte de service est valide mais n'a pas accès à la propriété Organikk (403). Aucun environnement Codex Cloud n'est encore créé ou publié. Le canal mobile reste donc à activer et à vérifier de bout en bout. Le projet `gsc-simcity` dispose déjà de données GSC via l'edge Fusionn, mais ce parcours cloud utilise un accès GSC propre, limité aux propriétés autorisées. Voir [[preuves/index]].
