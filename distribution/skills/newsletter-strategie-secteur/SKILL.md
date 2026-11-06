---
name: newsletter-strategie-secteur
description: "Édition de newsletter courte (500 mots) tirée d'une stratégie SEO par secteur. « newsletter stratégie secteur »."
---

# Newsletter Stratégie SEO par secteur — `/newsletter-strategie-secteur`

## Quand utiliser ce skill

Transforme la « Stratégie SEO par secteur » (le modèle long publié sur organikk.co : serrurier Lyon, avocat Paris, hôtel Paris…) en une ÉDITION DE NEWSLETTER courte et accrocheuse : 1 secteur (+ 1 ville) par édition, MAX 500 mots, scannable, qui finit sur une action. Garde l'ADN du modèle (angle ultra-spécifique anti-générique, captation directe vs plateforme, outil Product-Led, roadmap 3 phases compressée) et SURTOUT la discipline anti-hallucination (aucun chiffre sans source, sinon placeholder). Voix Tim. Ne publie rien : produit un draft.

TOUJOURS utiliser ce skill quand l'utilisateur dit : "/newsletter-strategie-secteur", "newsletter stratégie secteur", "édition stratégie SEO pour [métier] [ville]", "fais la newsletter pour [secteur]", "version courte de la stratégie secteur", "stratégie secteur en 500 mots", ou quand il veut transformer une stratégie SEO sectorielle en newsletter courte.

Le modèle source (long, 10 sections) est `.seokb/base/wiki/methodes/modele-strategie.md`. Ce skill en garde **l'os stratégique** mais le sert en **édition de newsletter de 500 mots maximum**, conçue pour être ouverte (objet qui accroche) et lue d'un trait.

**Une édition = un secteur + une ville.** Ne jamais traiter deux secteurs dans une édition.

## Entrées
- `[SECTEUR]` (métier ou produit) — obligatoire.
- `[VILLE]` (zone) — obligatoire pour le SEO local ; optionnel si stratégie nationale/B2B.
- Optionnel : `[OUTIL-PRINCIPAL]` (simulateur, estimateur, calculateur, comparateur), `[DURÉE-ROADMAP]` (9 mois cycle court / 12 mois cycle long).

## Règles dures (non négociables)
1. **MAX 500 mots** pour le corps de l'édition (objet exclu). Si ça dépasse, on coupe, on ne dilue jamais.
2. **Anti-hallucination (héritée du modèle).** Aucun chiffre (prix, marché, %) sans source réelle datée. À défaut : placeholder explicite `[À SOURCER : …]`. Jamais « selon une étude » sans étude nommée. Pas de Semrush/Ahrefs, pas de scraping concurrent. La data terrain vient du client. Une stratégie chiffrée sans source ne sort pas.
3. **Angle ultra-spécifique, pas générique.** On n'attaque jamais le mot-clé `[SECTEUR] [VILLE]` brut. L'édition tient sur un angle en une phrase (un des 4 patterns du modèle : transparence ; micro-intentions + autorité niche ; média expert local ; captation directe vs plateforme).
4. **Voix Tim** : tutoiement, direct, anti-IA writing, positions tranchées, zéro tiret cadratin, zéro « ce n'est pas X c'est Y », zéro remplissage. Chaque ligne apporte une info (densité, facteur ranking n°2 du modèle).
5. **Conversion > trafic.** L'édition vise des leads, jamais « de la visibilité ».
6. **Marché atypique + réglementaire** (variables 4 et 5 du modèle) : vérifier en amont si `[SECTEUR] [VILLE]` crée un sous-marché atypique (ex. paysagiste Paris = terrasses/copro, pas jardins) et s'il y a une déontologie (avocat RIN, santé, finance AMF). Si oui, l'angle et le ton le reflètent.

## Le gabarit d'édition (≤ 500 mots, dans cet ordre)
1. **Objet** — 1 ligne, ≤ 55 caractères, curiosity gap. C'est ce qui fait ouvrir. (En proposer 3, garder le meilleur.)
2. **Accroche** — 1 phrase : le mot-clé générique est imprenable / là n'est pas l'argent. Pose l'angle.
3. **Le constat** — 2-3 lignes : le trou de marché concret, ce que les concurrents cachent ou ratent, et ce que tape le vrai client décisionnel.
4. **La thèse** — 1-2 lignes : l'angle différenciant en une phrase (le pattern retenu).
5. **Le plan en 3 temps** — 3 puces courtes = la roadmap compressée :
   - Mois 0-3 : bottom-funnel transactionnel + `[OUTIL-PRINCIPAL]`.
   - Mois 3-6 : transparence/prix datés + longue traîne décisionnelle.
   - Mois 6-`[DURÉE]` : ultra-niche + autorité + newsletter pour backlinks naturels.
6. **L'outil qui fait la différence** — 1 ligne : la mécanique `[OUTIL-PRINCIPAL]` (donne la valeur AVANT le contact = page « Do » Fully Meets).
7. **3 mots-clés décisionnels** — 1 ligne, séparés par ·, en exemples réels du secteur (intention d'achat, pas d'exploration).
8. **CTA unique** — 1 ligne, une seule action.
9. **PS** (optionnel) — 1 ligne, teaser de l'édition suivante (rétention).

## Boucle (mémoire, légère)
Mémoire dans `newsletter-strategie-secteur/` :
- `ledgers/editions.jsonl` (append-only) : `{date, secteur, ville, angle_pattern, objet, mots_cles, claims_sources}`.
- `memory/wording_rules.md` (voix), `memory/directives.md` (apprentissages).
- **Anti-redite** : avant d'écrire, lire `editions.jsonl` ; ne pas reprendre un angle/objet déjà servi pour le même secteur.
- **Fin de run (apprendre)** : logger l'édition, noter ce qui manque comme data terrain, poser les questions à Tim dans `memory/questions.md`. Plus tard : résoudre avec les vrais taux d'ouverture/clic.

## Sortie
Draft dans `newsletter-strategie-secteur/editions/{YYYY-MM-DD}-{secteur}-{ville}.md` (suffixer `-v2` si existe). Ne publie pas : produit le draft + l'objet retenu + 2 objets alternatifs.

## Exemple (serrurier · Lyon — pattern transparence tarifaire) ~230 mots
> **Objet :** Serrurier à Lyon : pourquoi tu n'apparais jamais en urgence
>
> « Serrurier Lyon » est imprenable, et tant mieux : ce n'est pas là que sont les appels.
>
> Tes concurrents cachent leurs prix et empilent des pages « serrurier [quartier] » vides. Pendant ce temps, le client en urgence tape « prix ouverture porte claquée Lyon 6 » à 23h, et personne ne lui répond clairement.
>
> Ton angle : la **transparence tarifaire publique**. Tu affiches la fourchette avant l'appel, tu captes en direct au lieu d'engraisser les annuaires sponsorisés.
>
> Le plan, en 3 temps :
> - **Mois 0-3** : 10 pages/mois sur les urgences + un simulateur de prix (type d'intervention → fourchette immédiate + bouton appel).
> - **Mois 3-6** : pages prix datées, longue traîne « combien coûte… », avis vérifiés sur la page.
> - **Mois 6-9** : ultra-niche (après-effraction, assurance) + une newsletter locale qui ramène des backlinks naturels.
>
> L'outil qui change tout : un simulateur « type de serrure + situation = fourchette + appel ». Il donne la valeur avant d'exiger un contact. Page « Do », notée Fully Meets.
>
> 3 requêtes qui ramènent des appels : prix ouverture porte claquée Lyon · serrurier urgence Lyon 6 · changement serrure après cambriolage.
>
> (Affiche tes vrais tarifs, jamais un prix inventé.)
>
> **Réponds « SIMULATEUR »** et je te donne la structure de la page qui rank.
>
> *PS : demain, l'agence immo qui traite Lyon comme un média.*

## Concepts et sources liés
Modèle long : `raw/articles/modele-production/modele-strategie.md` · variante B2B : `modele-strategie-b2b.md` · applications publiées : `raw/articles/organikk-blog/strategie-seo-*` · concepts : passage-ranking, fully-meets, product-led-seo, data-proprietaire, anti-ai-writing · voix : `ton-de-voix`.
