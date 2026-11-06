---
name: audit-pre-call
description: "Document d'audit pré-call d'un prospect en HTML/PDF, données publiques seules. « fais l'audit pré-call », « /audit-pre-call »."
---

# Audit SEO pré-call, le document livrable

## Quand utiliser ce skill

Produit le document d'audit SEO pré-call d'un prospect Organikk, à partir de
sa seule URL et de données 100 % publiques (aucun outil payant, aucune GSC
requise). Sort un document HTML autoportant dans la charte Organikk (Geist,
dégradé bleu), imprimable en PDF A4, structuré en trois livrables : un audit
structuré (identité, état SEO réel, constat, angle), un tableau de MODÈLES DE
PAGES à produire (pas une liste de mots-clés) avec vérification de ce qui
existe déjà sur le site, et une roadmap 90 jours calée sur la méthode Organikk
en 4 phases. Règle absolue : aucun volume, position ou trafic inventé (les chiffres réels de Keyword Planner ou Search Console, eux, s'affichent avec leur source), et on ne
cible jamais une requête que le site couvre déjà.

TOUJOURS utiliser ce skill quand l'utilisateur dit : "/audit-pre-call", "fais l'audit
pré-call", "sors le doc d'audit avant le call", "audit HTML d'un prospect",
"prépare le document d'audit pour [site]", "l'audit + modèles de pages +
roadmap", ou fournit une URL de prospect en demandant le document d'audit
pré-call (le livrable HTML, pas la note markdown interne du skill seo-pre-audit).

Diffère de seo-pre-audit (qui sort une note markdown de préparation interne) :
ici on produit le DOCUMENT livrable, mis en page, prêt à montrer. seo-pre-audit
reste mobilisable pour la partie raisonnement en amont.

Ce skill transforme l'URL d'un prospect en un document d'audit mis en page, dans la charte Organikk, prêt à être montré ou envoyé. Il ne s'arrête pas à l'analyse : il sort le fichier HTML + PDF.

Référence canonique de rendu : `template.html` dans ce dossier, rempli avec l'exemple réel Harvestr. C'est le gabarit. On le duplique et on remplit le corps, on ne touche pas au `<style>`.

## Le document produit, trois livrables dans un seul fichier

1. **L'audit structuré** : identité et modèle, état SEO technique (chiffres réels relevés), le constat reformulé en coût, l'angle défendable.
2. **Les modèles de pages à produire** : un tableau de MODÈLES (pas de mots-clés bruts), chacun avec une colonne « déjà sur le site ? » vérifiée dans le sitemap.
3. **La roadmap 90 jours** : les 4 phases de la méthode Organikk, déclinées sur la data du prospect.

Plus un bloc « À récupérer au call » (GSC et questions), et un pied de prudence.

## Règles dures, non négociables

- **Zéro chiffre inventé.** Aucun volume de recherche, aucune position, aucun trafic estimés ; un chiffre issu de Keyword Planner ou de Search Console s'affiche avec sa source. La GSC n'est pas disponible avant le call : on la marque « à récupérer au call ». Tout chiffre avancé est un fait public relevé (nombre de pages au sitemap, date de dernier article, nombre de pages bloquées au robots.txt), daté dans le document.
- **On ne cible jamais une requête déjà couverte.** Avant de proposer un modèle, on vérifie dans le sitemap ce qui existe déjà. La colonne « déjà sur le site ? » porte cette vérification. Un prospect qui voit qu'on lui propose une page qu'il a déjà nous disqualifie.
- **Des modèles de pages, pas une liste de mots-clés.** Un modèle, une variable, des dizaines de pages, et on ne produit que les cases vides. Les requêtes exactes ne sont que des illustrations, figées au cadrage avec la Search Console.
- **Aucun volume inventé.** En pré-call il n'y a pas d'accès aux données du prospect, donc pas de colonne Volume par défaut ; si une donnée réelle existe, elle peut s'afficher avec sa source (décision du 2026-09-16).
- **Zéro tiret cadratin.** Deux-points, virgules, parenthèses.
- **Pas d'eyebrow mono-majuscule.** Aucun label du type `IDENTITÉ & MODÈLE`, `SECTION 01`, `DOCUMENT`. Les sous-titres sont en Geist casse normale (h3). Les en-têtes de tableau aussi. C'est un tell d'IA, il est banni. Cf. le design system Organikk.
- **Pas de trait latéral d'accent** (`border-left` coloré) : pattern IA également banni.
- **Anti-AI-writing sur toute la prose.** Pas de « visibilité » (dire positions, citations IA, demandes entrantes), pas de règle de 3 systématique, pas de rhétorique « ce n'est pas X, c'est Y », prose continue.
- **Le pain se formule en coût, pas en reproche.** « Chaque page non couverte est une demande de démo qui part ailleurs », pas « votre SEO est mauvais ».

## Phase A. Collecte (données publiques uniquement)

Relever, en notant la source et la date de chaque fait :

```bash
# Sitemaps : compter les pages utiles, repérer les patterns existants
curl -s -A "Mozilla/5.0" https://SITE/sitemap.xml | grep -oE '<loc>[^<]+</loc>' | sed 's/<[^>]*>//g'
curl -s -A "Mozilla/5.0" https://SITE/sitemap.xml | grep -c "<loc>"
# robots.txt : chercher les Disallow qui bloquent des pages business (intégrations, comparatifs, LP)
curl -s -A "Mozilla/5.0" https://SITE/robots.txt
```

Puis, via WebFetch :
- **Positionnement** : H1, promesse, cible, point de conversion (démo, devis, achat, inscription).
- **Le blog / ressources** : nombre d'articles, langue, fraîcheur (date du dernier post), et surtout leur nature (informationnel absorbé par l'IA, ou décisionnel).
- **La catégorie** : les outils auxquels le prospect est comparé, les patterns de requêtes décisionnelles (`[outil] alternative`, `[outil] with [intégration]`, `feedback for [équipe]`).
- **La data propriétaire** : cas clients, logos, méthodologie, chiffres internes. C'est le carburant des pages.

Point décisif de cette phase : **cartographier ce qui existe déjà sur le site** (pages de comparaison présentes, pages d'intégration présentes ou bloquées, pages persona, pages piliers). C'est ce qui alimente la colonne « déjà sur le site ? » et empêche de proposer du doublon.

## Phase B. L'audit structuré

Quatre sous-parties, en Geist casse normale (h3), jamais en eyebrow majuscule :

- **Identité et modèle.** Qui ils sont, ce qu'ils vendent, à qui, le point de conversion. Lister la data propriétaire mobilisable.
- **État SEO technique.** Quatre chiffres réels en cartes (nombre de pages au sitemap, articles de blog + fraîcheur, pages décisionnelles existantes, anomalies techniques). Puis une liste des faits saillants : page de comparaison unique, pages bloquées au robots.txt, blog daté, preuve tierce.
- **Le constat, reformulé en coût.** Le vrai problème business, formulé comme une perte, pas comme un reproche.
- **L'angle défendable.** Le terrain où le prospect tient face à l'IA (décisionnel de la catégorie, data propriétaire).

## Phase C. Les modèles de pages (le cœur)

Un tableau de 4 à 6 modèles. Colonnes : **Modèle de page · Pattern d'URL · Intention · Déjà sur le site ? · Ce qui remplit la page**.

- Chaque modèle a une variable et un pattern d'URL réel (`/compare/[outil]-alternative`, `/product/integrations/[outil]`, `/solutions/[équipe]`).
- La colonne « déjà sur le site ? » est verte quand ça existe (à renforcer, ne pas recréer), rouge quand c'est vide ou bloqué (à créer ou débloquer). Elle est relevée dans le sitemap, datée.
- La colonne « ce qui remplit la page » ancre chaque modèle dans la data du prospect (cas clients, angle propriétaire), jamais dans du vide.
- Sous le tableau, une note rappelle que les requêtes exactes se figent au cadrage, Search Console en main, après vérification de ce que le site couvre déjà, et qu'aucun volume n'est estimé : un volume ne s'affiche que s'il vient d'une donnée réelle (Keyword Planner, Search Console), avec sa source.

Skills mobilisables pour muscler cette phase si besoin : `seo-modeles-pseo`, `seo-mots-cles-decisionnels`, `seo-programmatique-pseo`.

## Phase D. La roadmap 90 jours

Les 4 phases de la méthode Organikk, non réinventées, déclinées sur la data du prospect :

1. **Mois 1, Stratégie.** Audit, connexion GSC, relevé de ce sur quoi le site ressort déjà, sortie des requêtes décisionnelles de la data client, carte des pages, deux modèles de départ, corrections techniques.
2. **Mois 2, Mise en production et agent SEO.** Premières pages des modèles prioritaires, déblocage des pages bloquées, construction de l'agent SEO client.
3. **Mois 3, Mise en production et optimisation.** Suite des modèles, mesure GSC, optimisation de l'existant, décision autonomie ou prolongation.
4. **Mois 3 à 6, Optimisation, production et CRO.** Déclinaison du reste, optimisation, travail du taux de conversion.

Rythme figé par la doctrine : **10 à 15 pages par mois, 45 à 50 à trois mois.** Ne pas le retirer. Fermer par la ligne d'ancrage doctrine (4 piliers, data propriétaire, liens gagnés jamais achetés, mots-clés actionnels).

Les libellés de phase (« Mois 1 ») sont en Geist casse normale, pas en mono-majuscule.

## Phase E. À récupérer au call

Bloc liste, organisé en questions de découverte plutôt qu'en vrac :

- **Situation.** Comment gèrent-ils le SEO/contenu aujourd'hui ? Quel est leur processus actuel ? Qui décide, qui pilote le repo.
- **Accès et faisabilité.** GSC (impressions, position moyenne, requêtes qui ramènent déjà des demandes, **et ce sur quoi le site ressort déjà pour ne produire aucun doublon**), outils les plus comparés, faisabilité technique.
- **Problème et conséquences.** Ce qui frustre le plus dans la situation actuelle, depuis quand, l'impact business si rien ne change. Sert à confirmer ou affiner le constat de la Phase B, pas à le deviner.

Cette liste reste le bloc de questions du document. Le déroulé complet de call (connexion, solution idéale, présentation, objections, closing) est un outil interne de pas un contenu à faire figurer dans le document envoyé au prospect : voir `_MODELE-pre-call.md` section 6 dans le vault seo-kb.

## Phase F. Rendu et livraison

1. Dupliquer `template.html` en `audit-[prospect]-organikk.html` dans le dossier de travail (par défaut `wiki/propositions/`, ou le dossier du client s'il existe).
2. Remplacer **uniquement** le contenu entre `<body>` et `</body>`. Ne pas toucher au `<style>` ni au `<head>` (hors `<title>`).
3. Générer le PDF A4 :

```bash
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless --disable-gpu --no-pdf-header-footer \
  --virtual-time-budget=9000 --run-all-compositor-stages-before-draw \
  --print-to-pdf="Audit-SEO-[Prospect]-organikk.co.pdf" \
  "file:///chemin/absolu/audit-[prospect]-organikk.html"
```

4. Contrôler le rendu (rasteriser le PDF avec `pdftoppm -png -r 95` et regarder chaque page). Vérifier : tableau qui tient dans la largeur sans scroll ni troncature, zéro tiret cadratin, zéro eyebrow majuscule, colonne « déjà sur le site ? » remplie.
5. **Montrer en local avant tout envoi** : servir le dossier (`python3 -m http.server 8747 --bind 127.0.0.1` depuis le dossier) et donner l'URL `http://localhost:8747/audit-[prospect]-organikk.html`. Cf. la règle « montrer en local toujours ».

## Checklist qualité avant de livrer

- Les trois livrables sont là : audit, tableau de modèles, roadmap.
- Chaque modèle a une variable, un pattern d'URL réel, et un statut « déjà sur le site ? » vérifié dans le sitemap.
- Aucun modèle ne propose une page que le site a déjà (sinon : « à renforcer », pas « à créer »).
- Zéro chiffre de volume, position ou trafic inventé. Un chiffre issu d'une donnée réelle (Keyword Planner, Search Console) s'affiche avec sa source. GSC marquée à récupérer si absente.
- Zéro eyebrow mono-majuscule, zéro `border-left` d'accent, zéro tiret cadratin, zéro « visibilité ».
- Le `<style>` du gabarit est intact.
- Le rendu a été montré en local.

## Vérification finale (obligatoire)

Avant de présenter le livrable comme terminé : lancer `verificateur-livrable` avec les 6 sections de le skill `verification-livrable` (demande de tous les skills utilisés, livrables, sources, contraintes). Corriger les ❌, relancer le vérificateur sur la nouvelle version, recopier le dernier tableau dans la réponse. Un hook refuse la fin de la réponse tant que ce n'est pas fait.
