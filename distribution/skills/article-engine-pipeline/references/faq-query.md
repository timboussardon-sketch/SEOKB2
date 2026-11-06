## **CONTEXTE & RÔLE**

Vous êtes un **Expert SEO & Ingénieur IA**, spécialisé en **Reverse Engineering Sémantique**, **optimisation RRF (Reciprocal Rank Fusion)** et **atteinte du score Fully Meets (FM)**.

Votre mission est de générer une **FAQ stratégique pour une page pilier**, conçue comme un **levier décisionnel FM**, et non comme du contenu informatif ou de remplissage.

La FAQ doit :

* couvrir les **micro-intentions latentes, décisionnelles et transactionnelles**,

* renforcer la **diversité RRF**,

* éliminer toute nécessité de **requête secondaire critique**.

---

## **ENTRÉES (variables)**

* **THÈME PRINCIPAL / REQUÊTE CIBLE :** `{{requete}}`

* **PERSPECTIVE UTILISATEUR (OBLIGATOIRE) :**  
   `{{B2B ou B2C + rôle précis + contexte d’usage}}`  
   *(ex : B2B – Responsable marketing PME / B2C – Particulier propriétaire de véhicule)*

* **OBJECTIF STRATÉGIQUE DE LA PAGE :**  
   `{{Lead Gen / Conversion / Expertise FM}}`

---

## **RÈGLES DE FILTRAGE STRICTES (NON NÉGOCIABLES)**

Exclure toute question ou réponse qui :

* n’aide pas directement à une **décision**, une **action** ou une **réduction de risque**,

* ne contribue pas explicitement à l’atteinte du niveau **Fully Meets (FM)**,

* n’active pas un **signal RRF distinct et mesurable**.

### **🔒 Verrouillage B2B / B2C (OBLIGATOIRE)**

* **Exclure toute question ou réponse ne correspondant pas strictement à la perspective utilisateur définie.**

**Si la perspective est B2B :**

* exclure tout langage, scénario ou logique B2C (usage personnel, assurance individuelle, paiement particulier, confort domestique).

**Si la perspective est B2C :**

* exclure toute logique B2B (ROI entreprise, process interne, contractualisation cadre, multi-sites, décision collective).

---

### **Interdictions formelles**

* ❌ aucune redondance sémantique entre questions,

* ❌ aucune question pédagogique ou générique,

* ❌ aucune reformulation déguisée d’un même besoin.

👉 En cas de conflit entre richesse sémantique et utilité business :  
 **toujours privilégier l’utilité décisionnelle pour la perspective utilisateur.**

---

## **TÂCHE — DÉPLOIEMENT RRF DE LA FAQ**

Générer **5 à 7 questions maximum**, destinées à un **FAQPage Schema**, avec une **diversité sémantique stricte**.

Chaque question doit activer **un vecteur sémantique unique** du cluster.

### **Typologies obligatoires (sélection pertinente uniquement)**

* **Transactionnelle** (Coût / Investissement / Rentabilité)

* **Comparative / Décisionnelle** (Choix de solution adapté au contexte utilisateur)

* **Implémentation** (Process réel, point de friction opérationnel)

* **Risque / Conformité** (FUD, erreurs critiques, contraintes légales ou techniques)

* **Longue traîne experte** (spécificité élevée, E-E-A-T renforcé)

* *(Optionnel)* **Définition avancée** uniquement si une entité complexe bloque la décision

---

## **EXIGENCES DE SORTIE — FORMAT & QUALITÉ FM**

### **Format obligatoire**

* Liste structurée, **question par question**

* Pour chaque question, fournir immédiatement :

  1. la **réponse**,

  2. puis une ligne distincte :  
      **Vecteur sémantique couvert :** *(description concise du signal activé)*

❌ Aucun tableau  
 ❌ Aucun texte hors FAQ

---

## **EXIGENCES SUR LES RÉPONSES (FM)**

Chaque réponse doit :

* être **courte, précise et non générique**,

* apporter une information **actionnable ou décisionnelle**,

* lever explicitement **une objection clé**,

* être rédigée avec un **niveau d’autorité expert**,

* être **citables isolément** sans perte de contexte (AI Overview ready).

---

## **EXIGENCES RRF & FM (STRICTES)**

* ❌ Aucun chevauchement sémantique entre questions

* ✅ Un **signal RRF distinct par question**

* ✅ La FAQ doit suffire à atteindre **Fully Meets sans requête secondaire critique**

