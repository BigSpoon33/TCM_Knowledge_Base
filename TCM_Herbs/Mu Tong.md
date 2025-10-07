---
# 🔹 Core Metadata (Universal Fields)
id: "herb-20251001123706"
name: "Mu Tong"
type: "herb"
aliases: []
tags: [TCM, Herb]

# 🔹 Cross-Link Fields (Universal Relationship Slots)
category: []
related: []
symptoms: []
patterns: []
western_conditions: []
formulas: []
points: []
nutrition: []
tests: []

# 🔹 Herb-Specific Data
herb_data:
  hanzi: "木通"
  pinyin: "Mù Tōng"
  pharmaceutical: "Akebiae Caulis"
  english: "Akebia Caulis"
  alternate_names: []

  # TCM Properties
  taste: [Bitter, Slightly cold]
  temperature: "Slightly cold"
  channels: [Bladder, Heart, Small Intestine]

  # Clinical Information
  dosage: "3-6g"
  toxicity: "Very low toxicity if taken orally. Toxicity of preparations for injection is reportedly higher. Contains nephrotoxin, aristolochic acid."
  functions: [Promotes urination, Directs fire and damp-heat downward and out through the urine, Facilitates lactation, Unblocks blood stasis]
  dui_yao: []

  # Additional Information
  constituents: [Triterpene saponins: sapogenin oleanolic acid (Akebia trifoliata), Triterpene saponins: akeboside Sta, Stb, Stc, Std, Ste, Stf, Stg, Stg1, DStg, Str Stk; the sapogenins are hederagenin and oleanolic acid (Akebia quinata), stigmasterol, β-sitosterol, β-sitosterol-β-D-glucoside, betulin, myoinositol (Akebia quinata)]
  quality: "Two different products can be distinguished. The first is *hua shi*, which primarily consists of magnesium silicate. *Yang hua shi*, This is the main product and the only one listed in the Chinese Pharmacopoeia. The second is *ruan hua shi*, which mainly consists of aluminum silicate, and is dispensed in a few locales (see above). The best quality is Guangxi talcum (*Guangxi hua shi*)."
  text_first_appeared: "Divine Husbandman's Classic of the Materia Medica"

  # Source References
  bensky_pdf: "627"
  bensky_page: "None"

created: 2025-10-01
updated: 2025-10-01
---

# 🌿 Ai Ye

**Pharmaceutical Name:** `= this.herb_data.pharmaceutical`
**English Name:** `= this.herb_data.english`
**Chinese Name (Hanzi):** `= this.herb_data.hanzi`
**Category:** `= this.category`

---

## 📖 Source Reference

*Bensky page reference not yet added*

**Classical Sources:**
- Text first appeared: `= this.herb_data.text_first_appeared`

**Additional Resources:**
- Add URLs or other references here

---

## 📖 Overview

Bitter and cold, the nature of Akebiae Caulis (*mu tong*) is to unblock, facilitate the removal of pathogenic water, clear, and direct downward. It clears fire from the Heart and Lungs in the upper body, guides out dampness from the Small Intestine and Bladder in the lower body, and drives damp-heat and pathogenic fire downward to drain out through the urine. Thus, it directs fire downward and promotes urination. It can be used in the treatment of rough painful urination, painful bloody urinary dribbling, ulcers of the mouth and tongue, irritability, red eyes, edema, and yellowish vaginal discharge and swelling due to internal congestion of damp-heat. Furthermore, it can promote the flow of qi and blood, unblocking lactation in the upper body, and treating amenorrhea due to blood stasis in the lower body. It also alleviates swelling and pain in the joints from obstruction of the collaterals throughout the body.
- *Rectification of the Meaning of Materia Medica* observes that this substance is light in weight, with tiny perforations passing through it, very bitter in flavor, and thus excels in draining and directing downward to dispel dampness; it is specific for treating collected clumping of damp-heat that is unable to move.

---
---

## 🔑 TCM Properties

**Taste:** `= join(this.herb_data.taste, ", ")`
**Temperature:** `= this.herb_data.temperature`
**Channels Entered:** `= join(this.herb_data.channels, ", ")`

---

## ⚡ Functions & Actions

Promotes urination and unblocks painful urinary dribbling: for painful urinary dribbling from damp-heat in the Bladder with dribbling, rough, and painful urination. Also used for edema and ascites.
  - With Plantaginis Semen (*che qian zi*), Gardeniae Fructus (*zhi zi*), and Talcum (*hua shi*) for damp-heat in the Bladder leading to painful urinary dribbling, as in Eight-Herb Powder for Rectification (*ba zheng san*).
  - With Nelumbinis Nodus rhizomatis (*ou jie*) and Typhae Pollen (*pu huang*) for painful bloody urinary dribbling.
  - With *jin qian cao* (Lysimachiae/Desmodii/etc. Herba) and Lygodii Spora (*hai jin sha*) for stony painful urinary dribbling.
  - With Poria (*fu ling*) and Polyporus (*zhu ling*) for edema.
- Promotes urination and drains heat from the Heart via the Small Intestine: for such symptoms as irritability accompanied by sores of the mouth or tongue, and scanty urine.
  - With Junci Medulla (*deng xin cao*) for Heart channel heat shifting into the Small Intestine.
  - With Lophatheri Herba (*dan zhu ye*) and Rehmanniae Radix (*sheng di huang*) for ulcerations of the oral cavity, burning pain in the throat, irritability, and insomnia due to excess Heart fire, as in Guide Out the Red Powder (*dao chi san*).
- Promotes lactation and unblocks the blood vessels: for insufficient lactation; less commonly for amenorrhea, and for pain and stiffness of the joints.
  - With Astragali Radix (*huang qi*) and Angelicae sinensis Radix (*dang gui*) for insufficient lactation due to qi deficiency.
  - With Stephaniae tetrandrae Radix (*han fang ji*) and Atractylodis Rhizoma (*cang zhu*) for joint pain and obstruction due to wind-dampness.
  - With Achyranthis bidentatae Radix (*niu xi*) and Carthami Flos (*hong hua*) for amenorrhea due to blood stasis.
  - With pig's feet (ham hocks) and Vaccariae Semen (*wang bu liu xing*), as a thick stew, for insufficient lactation.

## 🎯 Patterns & Symptoms

**TCM Patterns Treated:**
```dataview
LIST
FROM [[]]
WHERE contains(patterns, this.file.link)
```

**Common Symptoms:**
`= join(this.symptoms, ", ")`

**Western Conditions:**
`= join(this.western_conditions, ", ")`

---

## ⚗️ Dui Yao (Herb Pairs)

**Common Pairings:**
```dataview
TABLE
    herb_data.dui_yao as "Paired With",
    "Rationale" as "Clinical Rationale"
WHERE type = "herb" AND file.name = this.file.name
```

- With **[[]]** → for
- With **[[]]** → for

---

## 🔗 Formula Combinations

**Formulas Containing This Herb:**
```dataview
TABLE
    Category as "Formula Category",
    Formula_Actions as "Primary Actions"
FROM ""
WHERE type = "formula" AND contains(herbs, this.file.link)
SORT Category, file.name
```

**Common Combinations:**
- In **[[]]** → serves as [Chief/Deputy/Assistant/Envoy]
- In **[[]]** → serves as [Chief/Deputy/Assistant/Envoy]

---

## 💊 Dosage & Administration

**Standard Dosage:** `= this.herb_data.dosage`

**Preparation Methods:**
- Decoction:
- Powder:
- Other:

**Special Cooking Instructions:**
- [ ] Decoct first
- [ ] Add near end
- [ ] Decoct in gauze
- [ ] Dissolve in strained decoction
- [ ] Crush before cooking
- [ ] Separately simmer

---

## ⚠️ Cautions & Contraindications

**Toxicity:** `= this.herb_data.toxicity`

**Contraindications:**
Use cautiously during pregnancy. It is contraindicated for any patient with insecure, slipping essence, spermatorrhea, yang deficiency and weakness of qi, or anywhere internal damp-heat is absent. It is particularly forbidden in pregnant women. (Harm and Benefit in the Materia Medica)

**Drug Interactions:**
-

**Pregnancy/Lactation:**
-

**Food Incompatibilities:**
-

---

## 🧪 Constituents & Pharmacology

**Chemical Constituents:**
```dataview
LIST herb_data.constituents
WHERE file.name = this.file.name
```

-
-

**Modern Pharmacological Research:**
-
-

---

## 🌱 Quality Criteria & Authentication

**Quality Indicators:**
Two different products can be distinguished. The first is *hua shi*, which primarily consists of magnesium silicate. *Yang hua shi*, This is the main product and the only one listed in the Chinese Pharmacopoeia. The second is *ruan hua shi*, which mainly consists of aluminum silicate, and is dispensed in a few locales (see above). The best quality is Guangxi talcum (*Guangxi hua shi*).

**Common Adulterants:**
-

**Processing Methods:**
- Raw (Sheng):
- Processed (Zhi):

---

## 🧾 Classical Sources & Commentary

**Historical References:**
- *Text in which first appeared:* `= this.herb_data.text_first_appeared`
- Key quotes:
  >

**Traditional Understanding:**
-

**Classical Commentary:**
-

---

## 💡 Clinical Notes & Modern Research

**Clinical Pearls:**
-
-

**Modern Clinical Applications:**
-
-

**Research Highlights:**
-
-

**Case Studies:**
-

---

## 📊 Related Herbs (Same Category)

```dataview
TABLE
    herb_data.taste as "Taste",
    herb_data.temperature as "Temp",
    herb_data.channels as "Channels"
FROM ""
WHERE type = "herb"
    AND category = this.category
    AND file.name != this.file.name
SORT file.name
LIMIT 10
```

---

## 📂 Related Notes & Cross-References

**Related Patterns:**
- [[]]

**Related Points:**
- [[]]

**Related Formulas:**
- [[Formulas including Ai Ye]]

**Related Western Conditions:**
- [[]]

**Nutritional Therapy:**
- [[]]

---

## 📝 Study Notes & Memory Aids

**Key Learning Points:**
1.
2.
3.

**Memory Device/Mnemonic:**
-

**Common Exam Points:**
-
-

**Clinical Decision Points:**
- When to use vs. similar herbs:
- Dosage modifications:
- Combination strategies:

---

*Last updated: 2025-10-01*
*Category: `= join(this.category, ", ")` | Type: [[TCM Herbs]]*
