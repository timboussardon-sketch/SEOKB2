# Jev dans le système SEO

Jev (TypeSafe System One) répond à des questions typées : un choix parmi des critères, ou un score
à cinq niveaux, avec une confiance. Il ne génère pas de texte. Ici il sert à trier ce que le
système produit, avant relecture. Clé : `JEV_API_KEY` dans `.env.local`, jamais copiée.

Un appel : 0,8 s. Huit en parallèle : une page de 190 phrases en 30 s.

## Trois scripts, une boucle

| Script | Question posée | Entrée | Sortie |
|---|---|---|---|
| `jev/verifier.py DRAFT --corpus …` | chaque phrase est-elle appuyée par le corpus ? apporte-t-elle une information ? | draft md + dossiers de matière | phrases absentes, déduites, remplissage ; score |
| `jev/liens.py --site ID` ou `FICHIER` | la cible aide-t-elle le lecteur du passage ? l'ancre est-elle fidèle ? | base de l'audit JEV ou JSON de propositions | retenus / ancre à revoir / écartés |
| `jev/matiere.py "sujet" --corpus …` | ce passage porte-t-il une preuve ? de quelle nature ? | corpus brut | verbatims classés, compte de preuves par source |

Tout verdict va dans `loops/jev/ledgers/verdicts.jsonl` (append-only). Les rapports vont dans
`loops/jev/outputs/`.

## Calibration avant action

```
python3 jev/calibrer.py --noter verifier "la phrase exacte" ko    # verdict de Tim
python3 jev/calibrer.py                                          # accord Jev / Tim → derived/calibration.json
```

Un usage reste « tri pour relecture » tant que l'accord est sous 80 % sur moins de 30 cas.

La version du modèle est fixée dans `jev/client.py` (`jev-1.13.0`, surchargeable par `JEV_MODEL`) et écrite dans chaque verdict. Le client refuse une réponse servie par une autre version. La calibration ne compte que les verdicts de la version fixée : changer de version, c'est recalibrer.

## Où ça se branche

- Règle « d'où vient cette phrase ? » (CLAUDE.md § 2) : `verifier` la rend mécanique, comme `slop.mjs` pour l'écriture IA.
- Règle « scorer la page sur la matière » (§ 4) : `matiere` ajoute la qualité des preuves au comptage.
- Écran Liens de l'audit JEV (`~/Code/maillage`) : `liens --site ID` lit ses propositions ouvertes.
- Boucle correction → durcissement (AGENTS.md § 14) : les verdicts de Tim notés par `calibrer` sont la donnée.
