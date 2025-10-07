---
# 🔹 Core Metadata (Universal Fields)
id: "herb-20251001123706"
name: "Tan Xiang"
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
  hanzi: "檀香"
  pinyin: "tan xiang"
  pharmaceutical: "Santali albi Lignum"
  english: "sandalwood, santalum"
  alternate_names: []

  # TCM Properties
  taste: [acrid, aromatic]
  temperature: "warm"
  channels: [Lung, Spleen, Stomach]

  # Clinical Information
  dosage: "2-5g"
  toxicity: "Contraindicated when there is fire or significant yin deficiency."
  functions: [Promotes the movement of qi and alleviates pain, Recently used in the treatment of coronary artery disease]
  dui_yao: []

  # Additional Information
  constituents: [Volatile oil: α-santalol, β-santalol (together >90%); santene, α-santalene, β-santalene, α-santalal, β-santalal, santenone, santenone alcohol, epi-β-santalene, epi-β-santalol, 12,13-dihydro-α-santalol, 12,13-dihydro-β-santalol, α-curcumene, β-curcumene, β-farnesene, santalic acid, ketosantalic acid, teresantalol, teresantalaldehyde, teresantalic acid, tricycloekasantalic acid, nortricycloekasantalic acid, dihydro-α-agrofuran, dihydro-β-agrofuran, 4,11-epoxy-cis-eudesmane, valencene, Amino acids: 4-hydroxyproline, sym-homospermidine, γ-L-glutamyl S-(prop-1-enyl)cysteine sulfoxide]
  quality: "Good quality consists of straight, solid, and heavy, cylindrical pieces with a glossy surface, dense annual rings, and an intense aroma."
  text_first_appeared: "Miscellaneous Records"

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

Acrid, aromatic, and warm, Santali albi Lignum (*tan xiang*) enters the Lung, Spleen, and Stomach channels. It warms and disperses qi stagnation in the chest and above the diaphragm, unblocking cold obstruction, stopping pain, settling nausea, and unbinding the Stomach. It is an important herb in the treatment of qi stagnation in the chest and abdomen causing pain, belching, nausea, and vomiting. Zhang Jie-Bin observed: "Taken in decoction, it can disperse cold qi, stop pain in the Heart and abdomen, arrest sudden turmoil disorder, harmonize the Stomach qi, unbind the diaphragm, stop nausea and vomiting, and promote food intake."

The Detailed Materia Medica makes an illuminating observation: "The aromatic qi of Santali albi Lignum (*tan xiang*) promotes upward movement; it will regulate qi above the diaphragm and chest, in the area of the throat." This indicates its area of action, and explains that the nauseous sensations best treated by this herb are felt in the chest and throat, not the epigastrium. This is why raising Stomach qi in these cases is beneficial. With this in mind, the following passage from Seeking Accuracy in the Materia Medica becomes comprehensible:

Whenever cold qi clumps in the upper body preventing the intake of food, and [pathogenic] qi rebels upward causing vomiting, despondency, and discomfort, consuming [Santali albi Lignum (*tan xiang*)] can guide the Stomach qi also upward-its power mobilizes upward. It can disperse wind painful obstruction, reducing the swelling and stopping the pain-its power primarily disperses outward. Its actions specifically enter the Spleen and Lungs, unlike the power of Aquilariae Lignum resinatum (*chen xiang*), which primarily directs downward and guides the qi downward.

---
---

## 🔑 TCM Properties

**Taste:** `= join(this.herb_data.taste, ", ")`
**Temperature:** `= this.herb_data.temperature`
**Channels Entered:** `= join(this.herb_data.channels, ", ")`

---

## ⚡ Functions & Actions

- Promotes the movement of qi and alleviates pain: for pain associated with stagnant qi in the chest and abdomen.
- Recently used in the treatment of coronary artery disease.
  - With Salviae miltiorrhizae Radix (*dan shen*) and Amomi Fructus (*sha ren*) for chest pain associated with obstructed Heart qi, as in Salvia Decoction (*dan shen yin*).
  - With Aucklandiae Radix (*mu xiang*) and Caryophylli Flos (*ding xiang*) for chest, epigastric, and abdominal pain due to stagnant qi and cold, as in Liquid Styrax Pill (*su he xiang wan*).
  - With Cyperi Rhizoma (*xiang fu*) for a stifling sensation in the chest and flanks from Liver-Spleen disorders.
  - Powdered, together with Poria (*fu ling*) and Citri reticulatae Exocarpium rubrum (*ju hong*), and chased with a decoction of Ginseng Radix (*ren shen*), for dysphagia occlusion when one suffers from a sense that food is stuck.

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
Contraindicated when there is fire or significant yin deficiency.

"If there is overabundance of fire due to yin deficiency, this can disturb the blood and cause cough: do not use it." (Treasury of Words on the Materia Medica)

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
Good quality consists of straight, solid, and heavy, cylindrical pieces with a glossy surface, dense annual rings, and an intense aroma.

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
