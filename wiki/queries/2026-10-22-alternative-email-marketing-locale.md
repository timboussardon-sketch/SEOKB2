---
type: query
title: "Cadrage d'une alternative locale à Mailchimp et Resend"
aliases: [email-marketing-local, newsletter-locale]
tags: [email, newsletter, produit, logiciel, deliverabilite]
created: 2026-10-22
updated: 2026-10-22
sources: 1
confidence: medium
status: draft
---

# Cadrage d'une alternative locale à Mailchimp et Resend

## Installation livrée le 22 octobre 2026

Le MVP « Courrier » est implémenté dans `wiki/projets/courrier/`. Application : http://127.0.0.1:8984/ ; suivi : http://127.0.0.1:8984/#project. Guide : [[projets/courrier/README]]. État et limites : [[projets/courrier/recap]].

Choix appliqués pour cette première version : newsletter marketing, une publication, un utilisateur local, SQLite et Python sans dépendance externe. Le mode local génère des fichiers email sans expédition. Le connecteur Resend est implémenté ; son activation nécessite les accès fournisseur, le domaine et une URL HTTPS publique. Les éléments ci-dessous restent le cadrage initial, pas une liste de fonctions toutes livrées.

## Intention

Construire un outil auto-hébergé pour gérer des newsletters marketing et transactionnelles. Les données, les brouillons et l'interface restent sur l'infrastructure de Tim. L'envoi passe par un fournisseur SMTP/API interchangeable : un ordinateur local ne maîtrise ni la réputation IP ni la réception chez Gmail, Outlook ou Yahoo.

La liste fournie décrit une plateforme de publication, CRM, automation, paiement, communauté, podcast et publicité. La reproduire intégralement serait un produit multi-années avec une charge permanente d'exploitation. Le premier produit doit résoudre un seul flux : collecter des contacts consentants, préparer une campagne, l'envoyer et comprendre ses résultats.

## Première version proposée

1. **Publications** : expéditeur, domaine, identité visuelle et pied de page par publication.
2. **Contacts** : import CSV, champs personnalisés, tags, source d'acquisition, statut de consentement et historique.
3. **Conformité** : double opt-in configurable, désinscription en un clic, suppression par publication et liste globale, journal d'événements.
4. **Campagnes** : éditeur blocs simple, aperçu texte/HTML, test email, planification et envoi à un segment.
5. **Segments** : règles sur tags, champs, date d'inscription et engagement disponible.
6. **Envoi** : adaptateur SMTP/API, file de tâches, reprises de déférés, classification des rebonds et suppressions.
7. **Mesure** : livraisons, rebonds, plaintes et désinscriptions. Ouverture/clic restent des mesures indicatives (pixels bloqués, protections anti-traçage et clics automatisés).
8. **Automatisation initiale** : une séquence de bienvenue avec délai et désinscription automatique si le contact se retire.

## Architecture de départ

- Application web et API : interface auto-hébergée.
- PostgreSQL : publications, contacts, consentements, campagnes, segments, événements et audit.
- Worker/queue : envois, reprises et webhooks entrants.
- Stockage local ou S3 compatible : images et pièces jointes.
- Connecteur d'envoi remplaçable (SMTP ou API d'un ESP). Ne pas envoyer depuis une IP résidentielle.
- Webhooks de l'ESP : livraison, bounce, plainte, désinscription et report de blocage.
- Secrets d'envoi hors base applicative, sauvegardes chiffrées, journal d'accès et politique de rétention.

## Découpage du backlog

### MVP — construire d'abord

Modèle multi-publications léger, contacts et consentement, import/export, désinscription, suppressions, éditeur campagne, aperçu, envoi test, planification, segmentation simple, file d'envoi, webhooks et tableaux de résultats.

### Après validation du flux

Automatisations avec branches, collaboration/commentaires, tests A/B, domaines multiples, formulaires intégrables, API publique, MCP, dynamic content, version web et personnalisation avancée.

### Hors périmètre initial

Réseau public de recommandations, ads marketplace, abonnements payants, paiements, communauté, podcast, webinars, site builder, AI writer et garanties de délivrabilité. Ces modules ajoutent des produits distincts et des responsabilités opérationnelles.

## Garde-fous de délivrabilité

Un taux de livraison revendiqué n'est pas une propriété qu'un logiciel local peut garantir. Il dépend du consentement, de la qualité des listes, du domaine, de la réputation d'envoi, du contenu et des fournisseurs destinataires. Première version : respecter SPF/DKIM/DMARC, gérer plaintes et rebonds dès leur réception, supprimer les contacts désinscrits, limiter la cadence, demander une validation avant les gros envois et montrer les volumes par fournisseur quand la donnée existe.

Ne pas implémenter le réchauffage d'IP ou les règles de retry à l'aveugle : les politiques doivent suivre le fournisseur choisi et les réponses observées. Ne pas promettre une détection universelle des clics bots.

## Décisions à prendre avant l'implémentation

- Fournisseur d'envoi initial : Amazon SES, Resend, Postmark ou autre. Le code doit garder un adaptateur remplaçable.
- Mode de déploiement : ordinateur/NAS privé ou serveur VPS auto-hébergé. Le poste fermé ne peut pas recevoir les webhooks Internet.
- Premier usage : newsletter éditoriale, emails marketing, ou transactionnel. Les règles de consentement et la mesure diffèrent.
- Un utilisateur ou plusieurs membres/roles dès le départ.
- Langage et stack selon la cible réelle de déploiement.

## Liens

- Source de la demande : liste de fonctionnalités Beehiiv fournie par Tim dans la conversation du 2026-10-22.
- [[methodes/tableau-de-bord-par-projet-seo]] (référence de pilotage local)
- [[concepts/anti-ai-writing]]
