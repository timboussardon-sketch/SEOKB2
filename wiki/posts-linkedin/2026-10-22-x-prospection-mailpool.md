---
type: post
title: "Post X : prospection passée de Resend à Mailpool"
aliases: [tweet-mailpool]
tags: [x, prospection, email, mailpool]
created: 2026-10-22
updated: 2026-10-22
sources: 2
confidence: high
status: draft
---

J'envoyais ma prospection par Resend, depuis organikk.co.

529 emails.

Sauf que les conditions de Resend interdisent la prospection non sollicitée.

Ce que j'ai changé ce soir :

- domaine secondaire organikk-seo.co
- 1 boîte Mailpool, envoi en SMTP
- organikk.co intact (l'importer chez Mailpool effaçait tout son DNS)
- même template, rendu par la même fonction que sous Resend
- 30 emails par jour, un toutes les 12 minutes (domaine neuf)
- test Gmail : DKIM, SPF et DMARC en pass, arrivé en boîte de réception

Ce que j'ai trouvé en vérifiant :

- 0 réponse relevée sur 529 envois
- le suivi Gmail n'avait jamais été branché
- les relances ne partaient donc pas

Je n'ai aucune donnée pour dire quel relais convertit le mieux.

Prochaine étape : brancher le suivi des réponses avant de relancer les envois.

Sources : [[projets/courrier/dossier-envoi-prospection]], [[projets/courrier/verification-mailpool]].
