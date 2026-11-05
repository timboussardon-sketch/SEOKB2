---
type: source
source_type: test-terrain
title: Stock de 700 emails professionnels nominatifs d’avocats
aliases: [stock-700-avocats]
tags: [prospection, avocats, donnees, agents]
created: 2026-10-10
updated: 2026-10-10
sources: 700
confidence: medium
status: stable
---

# Stock de 700 emails professionnels nominatifs d’avocats

Tim demande de porter le stock à 700 emails. Le fichier livré contient les 100 contacts précédents et 600 adresses supplémentaires à ce lot. Chaque adresse est publiée dans un contexte professionnel et rattachée à un avocat nommé. Contexte : [[sources/2026-10-10-selection-emails-avocats-specialises]] et [[agents/agent-avocats]].

## Résultat vérifié

Le CSV contient 700 lignes, 700 adresses distinctes et 700 identités distinctes. Chaque ligne donne la source publique de l’adresse et celle de la pratique juridique. Le contrôle DNS trouve un MX pour chaque domaine retenu ; aucune boîte n’a été testée. Preuves : `~/Code/prospection/agent-avocats/prospection-avocats/stock-700-2026-10-10/700-emails-nominatifs.csv`, le JSON associé et `verification.json`. Empreinte SHA-256 du CSV : `8a35a8ba967ed1544dc1d1138ac234a19000008748161626e7455dfa4bae2d44`.

Les sources se répartissent entre 506 contacts issus de barreaux, 158 de sites de cabinets et 36 d’AvoSial. Les regroupements par cabinet identifient 559 groupes techniques et 141 contacts de réserve dans un groupe déjà représenté. Ils reposent sur le rattachement connu, le domaine professionnel ou l’identité pour les domaines mutualisés. Les structures juridiques n’ont pas toutes été vérifiées ; ce décompte ne constitue pas un dénombrement certifié de cabinets distincts. Les contacts de réserve sont signalés dans une colonne dédiée. Source des décomptes : `verification.json` du lot.

## Limites de qualification

Le lot couvre le droit du travail, le droit social et la sécurité sociale. Il conserve séparément la pratique déclarée et le certificat de spécialisation. La qualification employeur reste à confirmer pour 496 lignes. Les sources comprennent notamment des listes du CNB par compétence employeur, dont l’appartenance a été conservée dans les données locales, et des annuaires de spécialisation ou d’activité dominante. Les fiches CNB dont la lecture avait échoué ne deviennent pas des preuves de contenu relu. Les tailles de cabinets restent à contrôler.

Les annuaires de Lyon et de Marseille ont fourni des adresses professionnelles sur des domaines mutualisés, notamment avocat.fr et Gmail. Le domaine d’hébergement ne suffit pas à qualifier une adresse de privée ou de générique : l’attribution nominative et la publication professionnelle sont contrôlées. Les coordonnées privées non publiées pour l’activité ne sont pas recherchées. Sources publiques : https://www.barreaulyon.com/annuaire/activite/droit-du-travail/ ; https://www.barreaulyon.com/annuaire/specialite/droit-du-travail/ ; https://www.barreau-marseille.avocat.fr/wp-content/uploads/annuaire-cache/annuaire-avocats.pdf ; https://www.barreaudenice.com/fr/annuaire/specialisations-41-droit-du-travail.

## État opérationnel

Le rapprochement final avec l’historique local ne trouve aucun envoi pour les emails ou cabinets identifiés du lot. Il ne couvre pas les envois extérieurs à l’application ni les structures inconnues sous une autre dénomination. Aucun email n’a été envoyé et aucune campagne n’a été activée pendant cette recherche. La base PostgreSQL n’a pas été modifiée. Les compteurs restent à 250 lignes outreach, 480 brouillons et 251 approbations ; contrôle conservé dans `verification.json`.

Le tableau de bord http://127.0.0.1:3456/recap est mis à jour. Le rythme configuré reste de 100 emails par jour ouvré, décrit dans [[sources/2026-10-10-agent-prospect-enrichissement]]. Le filtre exclusivement nominatif de l’envoi reste à corriger avant utilisation automatique. Les 700 lignes forment un stock de recherche avec qualification visible.

## Contrôles et apprentissage

Le collecteur AvoSial s’est arrêté sur une réponse HTTP 429. Les autres recherches ont utilisé des sources indépendantes. Le collecteur de cabinets respecte les refus HTTP 403 et 429 et les restrictions de robots.txt.

L’extraction automatique de texte HTML peut coller un numéro de téléphone au début d’une adresse ou un mot à la fin de son domaine. Un domaine contenant une erreur peut malgré tout avoir un MX. Les candidats contenant ces anomalies ont été écartés ; le MX seul ne valide pas l’adresse. Les profils fiscaux ou de droit des sociétés détectés par simple présence du droit social dans le menu ont aussi été exclus. Observation cohérente avec [[methodes/apprentissage-continu]] et le précédent contrôle individuel.
