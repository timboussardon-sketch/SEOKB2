# Skill : audit-complet

Skill routeur qui déclenche l'audit SEO complet d'un site selon le workflow canonique du vault : `raw/bootcamp4/workflow-audit-bootcamp4.md` (8 phases, dérivé du Workflow V3 d'avril 2026). Le skill ne contient pas la méthode : il oblige à ouvrir le fichier du vault et à suivre ses 8 phases dans l'ordre, chacune branchée sur le skill dédié (indexation-check, seo-core-web-vitals, seo-quick-win, seo-cannibalisation, maillage-systeme, maillage-interne-gsc).

## Installation

```bash
mkdir -p ~/.claude/skills/audit-complet
cp SKILL.md ~/.claude/skills/audit-complet/SKILL.md
```

Prérequis : le vault seo-kb cloné dans `~/Code/seo-kb/` (le skill lit `raw/bootcamp4/workflow-audit-bootcamp4.md`). Sur une autre installation, adapter ce chemin dans SKILL.md. Les skills des 8 phases doivent aussi être installés.

## Utilisation

Déclencher dans Claude avec : « audit de mon site », « audit du site [X] », « audit complet », « audite [URL] », « lance l'audit », « workflow audit complet ».

Pour une dimension seule, le skill s'efface devant le skill dédié : audit indexation → indexation-check, audit GEO → seo-geo-audit, pré-audit commercial → seo-pre-audit.

Règles dures intégrées : 100 % données Google (GSC + crawl + Lighthouse), aucun chiffre estimé, le cadre de l'audit n'est jamais improvisé, constats critiques contre-vérifiés avant publication.

## Origine

Créé le 2026-09-16, après un audit d'organikk.co construit ad hoc au lieu de suivre le workflow du vault. Le skill est le verrou mécanique qui relie les mots « audit de mon site » au fichier de méthode.
