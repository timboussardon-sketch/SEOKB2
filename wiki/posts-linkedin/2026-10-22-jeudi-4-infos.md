---
type: post
title: "Post LinkedIn : 4 infos SEO du jeudi (2026-10-22)"
aliases: [post-jeudi-4-infos-2026-10-22, jeudi-4-infos-22-octobre]
tags: [post-linkedin, doctrine-tim, agentic-search, query-fan-out, data-proprietaire, boucle-sortie-mesure, tabou-visibilite]
created: 2026-10-22
updated: 2026-10-22
status: draft
sources: 4
confidence: medium
---

# Post LinkedIn : 4 infos SEO du jeudi (2026-10-22)

> **Draft.** Tim relit avant de poster. Format validé : hook 🍿, titres en phrase, chiffres isolés sur leur ligne, une prise de position par info, question finale. Voix Tim, pas de tiret cadratin.
>
> **Source, à lire avant de poster.** `agent-synthetic/revuedepressIA/breves-IA/` ne contient toujours aucune édition de brèves dans la fenêtre 2026-10-15 → 2026-10-22 (dernière : `2026-10-02-breves.md`, 20 jours de silence, déjà signalé dans [[posts-linkedin/2026-10-15-jeudi-4-infos]] sans réponse). Le dossier contient en revanche `breves-IA/scan-arxiv/2026-10-19-scan-arxiv.md`, sous-doc des brèves : l'info 2 en vient. Les infos 1, 3 et 4 viennent des éditions Algorithme `2026-10-15` à `2026-10-21` du même dossier parent, option (b) de la semaine dernière, appliquée ici faute de réponse plutôt que de livrer un second draft vide. Si Tim refuse ce fallback, le post se réduit à l'info 2.

---

Cette semaine, 4 infos où quelqu'un d'autre décide à ta place : Google finalise la vente, ChatGPT réécrit la question, OpenAI réécrit l'annonce, et un blog a laissé l'IA écrire. 🍿

**Depuis le 15 octobre, Google encaisse la commande dans Search et Gemini aux États-Unis, et l'Europe est écartée**

Universal Cart est en production aux États-Unis dans Google Search et l'application Gemini. Un seul panier multi-marchands, suivi des baisses de prix et des retours en stock, paiement dans Google Pay ou transfert vers le site du marchand.

Marchands au lancement : Nike, Sephora, Target, Ulta Beauty, Walmart, Wayfair, et des boutiques Shopify comme Fenty et Steve Madden.

Environ 60 milliards de listings produits dans la Shopping Graph derrière.

Le même jour, Shopify avait ouvert Shop MCP, un serveur qui donne à n'importe quel agent 17 outils pour chercher, remplir un panier et payer en Shop Pay, sur plus d'un milliard de produits, sans ouvrir de navigateur.

Google ne publie ni le nombre de marchands actifs ni le volume de sessions. Mais le fait structurel est là : une part des sessions Search ne s'oriente plus, elle achète, et c'est Google qui tient la caisse. [[concepts/agentic-search]] cesse d'être une hypothèse de conférence le jour où Walmart et Target branchent leur checkout dessus. L'Europe est écartée au lancement, et je ne lis pas ça comme une protection. C'est juste plus de temps pour vérifier ton flux Merchant Center avant que la question se pose chez toi.

(Sources : TheNextWeb, PPC Land, Shopifreaks, 15 octobre 2026 ; changelog développeur Shopify, 13 octobre 2026)

**ChatGPT cite ce que sa propre recherche a retrouvé, et ça explique 32 % de la variation des citations, contre 2,8 % pour ce qu'il y a sur ta page**

Un paper arXiv publié cette semaine (2610.15033) a rejoué pendant 90 jours des questions commerciales sur ChatGPT, Gemini et Perplexity, dans deux marchés.

158 099 réponses.

468 037 citations.

Chaque page citée par ChatGPT avait été remontée par sa recherche interne, sur des sous-requêtes réécrites à chaque réponse, qui coïncident rarement avec les résultats de Google ou Bing. À l'intérieur d'un même site, un seul facteur de contenu compte : les pages dont le titre et les paragraphes correspondent aux questions posées. FAQ, données structurées, encadrés de synthèse et vitesse ne pèsent qu'en comparant des sites différents.

Et ChatGPT injecte dans ses recherches les marques qu'il connaît déjà, et en nomme certaines sans aucune page à l'appui.

Ça confirme ce que je dis sur [[concepts/query-fan-out]] depuis le début : le levier n'est pas le balisage, c'est d'être retrouvé sur les sous-questions que le moteur se pose à ta place. Un audit GEO qui te vend du schema FAQ comme levier principal se trompe de 32 % contre 2,8 %. La réserve que je garde : un seul paper, pas encore relu dans le PDF, et un second (2610.15382) arrive au même mécanisme par une autre équipe, ce qui me suffit pour en parler, pas encore pour le mettre dans une propale.

(Source : arXiv 2610.15033, données et code publiés, scan arXiv du 19 octobre 2026)

**Un blog de 500 billets écrits à la main a publié 31 billets assistés IA : les clics du blog ont chuté de 67,8 %**

JumpFly a publié le 20 octobre une étude de cas sous nom de client, EarthMed, avec les chiffres Search Console du client.

Avant : plus de 500 billets rédigés à la main, environ 35 000 pages indexées, le blog pesait 45,4 % des 65 000 clics du site en octobre 2025.

Entre mi-juillet 2025 et mi-2026 : 31 billets assistés IA, chacun retravaillé environ 90 minutes par un expert du secteur.

Décembre 2025, Core Update : clics du blog en recul de 30,7 % sur 28 jours.

Mai 2026 : aucun des 8 derniers billets publiés n'est indexé.

Août 2026 : clics du blog en recul de 67,8 %, part du site tombée à 24 %.

Cas unique, pas de groupe de contrôle, et le Core Update de décembre brouille l'attribution. Je le cite quand même, parce que c'est le premier cas chiffré et nommé que je vois, et que 31 billets sur 500 ont suffi. 90 minutes de relecture par un expert n'ont pas sauvé le site. Ce qui manque dans ce cas, ce n'est pas la relecture, c'est la matière : un billet assisté IA relu reste un billet sans donnée propriétaire, et Google l'a traité comme tel. EarthMed a tout retiré et en a pour 6 à 18 mois de récupération estimée. [[concepts/data-proprietaire]], encore.

(Source : JumpFly, A Cautionary Tale: One Site's AI-Assisted SEO Crash, 20 octobre 2026, chiffres Search Console du client)

**Le 30 octobre, OpenAI active par défaut la réécriture de tes annonces ChatGPT, URL de destination comprise**

OpenAI a écrit le 20 octobre aux annonceurs ChatGPT Ads : à partir du 30 octobre, Creative Enhancements est activé par défaut sur les campagnes existantes.

Ce que la fonction peut réécrire seule : titres, descriptions, visuels redimensionnés, texte traduit, et l'URL de destination.

Formule du courrier : ces annonces « can run automatically without requiring you to review or approve each version ».

10 jours pour poser l'opt-out.

Le pattern est celui de Google depuis des années : activé par défaut, désactivation manuelle. Ce qui est nouveau, c'est la ligne URL de destination. Si l'URL cliquée diffère de celle que tu as soumise, ton attribution GA4 et tes UTM divergent, et tu ne le verras pas dans ChatGPT. Je l'ajoute à la boucle d'attribution ChatGPT déjà cassée côté trafic direct ([[concepts/boucle-sortie-mesure]]). Si tu as une campagne ChatGPT Ads, l'opt-out se décide avant le 30, pas après avoir constaté le trou dans le reporting.

(Source : Search Engine Roundtable, Barry Schwartz, 20 octobre 2026, d'après le courrier OpenAI aux annonceurs)

Toi, sur ces 4 décisions prises à ta place, laquelle apparaît déjà dans ton reporting ?

---

## Notes de production

- **Source** : voir le bandeau en tête. Une info sur quatre vient du périmètre strict (`breves-IA/scan-arxiv/`), trois viennent des éditions Algorithme du 15 au 21 octobre. Fallback explicite, à valider par Tim.
- **Infos écartées** : audit WashU des AI Overviews (29,8 % de domaines cités hors top 10), même mécanisme que l'info 2, aurait fait doublon ; Meta qui retire « train » de ses conditions commerciales au 30 octobre mais garde le droit de crawl, business mais juridique, moins actionnable ; DeepSeek à 0,75 USD les 1 000 requêtes de recherche web, intéressant pour la couche économique, pas une décision pour un client cette semaine ; DataDome Q3 (29,1 millions de requêtes Muse en 12 jours), chiffre fort mais sans action côté site.
- Fil conducteur : quatre décisions prises hors de la main du propriétaire du site, Google qui encaisse, ChatGPT qui réécrit la requête, OpenAI qui réécrit l'annonce, et le cas inverse, un site qui a laissé l'IA décider du contenu.
- Une prise de position par info, adossée à un concept du vault : [[concepts/agentic-search]] (Universal Cart), [[concepts/query-fan-out]] (paper 2610.15033), [[concepts/data-proprietaire]] (EarthMed), [[concepts/boucle-sortie-mesure]] (ChatGPT Ads).
- Réserves à garder si un commentaire les soulève : Universal Cart sans chiffre de marchands actifs ni de sessions ; paper arXiv lu sur abstract et résumé du scan, pas sur le PDF ; cas EarthMed unique, attribution par élimination, Core Update confondant ; ChatGPT Ads rapporté par Schwartz d'après le courrier, documentation OpenAI à confirmer.
- Non-répétition vérifiée : [[posts-linkedin/2026-10-08-jeudi-4-infos]] couvrait G2, Search Console IA et Prime Day ; [[posts-linkedin/2026-09-24-jeudi-4-infos]] l'écart citation/visite ; [[posts-linkedin/2026-09-17-jeudi-4-infos]] Ads et feed marchand. Aucun ne couvrait Universal Cart, le paper fan-out, EarthMed ni Creative Enhancements.
- Auto-check anti-IA (§11) : pas de tiret cadratin, pas de mot banni, « visibilité » absent du corps.
