---
# 🔹 Core Metadata (Universal Fields)
id: "herb-20251001123706"
name: "Mori Cortex / Sang Bai Pi"
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
  hanzi: "桑白皮"
  pinyin: "Sang Bai Pi"
  pharmaceutical: "Mori Cortex"
  english: "Mulberry Root Bark"
  alternate_names: []

  # TCM Properties
  taste: [Sweet, Cold]
  temperature: "Cold"
  channels: [Lung]

  # Clinical Information
  dosage: "6-15g"
  toxicity: "Its nature is not entirely beneficial, so it should not be overused. It is forbidden in those with Lung deficiency and excessive urination, and also for cough from externally-contracted wind-cold."
  functions: [Drains heat from the Lungs, stops coughs, and calms wheezing, Promotes urination and reduces edema]
  dui_yao: []

  # Additional Information
  constituents: [Flavonoids: morusin, cyclomorusin, oxydihydromorusin, morusinol, kuwanon A-V, mulberrin, mulberrochromene, cyclomulberrochromene, cyclomulberrin, mulberranol, moranoline, moracenin A-D, morachalcone A, morusenin A, B, sanggenon A-N, 5,7-dihydrochromone, Aromatic furane derivates: mulberrofuran A-I, Anthocyanosides: pelargonidin-3-glucoside, petunidin-3-rutinoside, Other constituents: volatile oil]
  quality: "Good quality consists of thick, white, pliable pieces of bark without any orange outer bark."
  text_first_appeared: "None"

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

Sang Bai Pi (桑白皮) - *Mori Cortex* is downward-directing in nature, primarily settles cough and wheezing due to heat, and facilitates urination. There is a saying that 'Draining Lung excess will not be successful without Mori Cortex (Sang Bai Pi).' It is most commonly used in two areas: cough and wheezing with yellow sputum (or blood in the sputum) due to heat from excess in the Lungs, and for edema with urinary difficulty due to heat from excess. While effective for general edema, it is particularly helpful for swelling around the eyes.

*The Grand Materia Medica* notes that "Its strong point is facilitating urination, as 'excess requires draining of the child'; therefore, it is appropriate when there is water qi in the Lungs, and when Lung fire is excessive."

*Transforming the Significance of Medicinal Substances* explains that it disperses heat and mainly treats wheezing, fullness, and cough, hot phlegm, and spitting of blood. All of these symptoms result from excess pathogenic constraint holding back the Lung qi so that the Lung cavity fails to maintain free and unobstructed activity. Using this herb to permeate and then disperse the constraint in order to facilitate the Lung qi will naturally rectify all symptoms.

---
---

## 🔑 TCM Properties

**Taste:** `= join(this.herb_data.taste, ", ")`
**Temperature:** `= this.herb_data.temperature`
**Channels Entered:** `= join(this.herb_data.channels, ", ")`

---

## ⚡ Functions & Actions

- **Drains heat from the Lungs, stops coughs, and calms wheezing:** For cough and wheezing due to Lung heat. With Di Gu Pi (地骨皮) - *Lycii Cortex* and Gan Cao (甘草) - *Glycyrrhizae Radix* for cough with viscous sputum, fever, irritability, and thirst due to phlegm-heat obstructing the Lungs, as in Xie Bai San (瀉白散) - *Drain the White Powder*. With Zhi Fu Zi (制附子) - *Aconiti Radix Lateralis Preparata* for cough and wheezing with edema due to Kidney yang deficiency.
- **Promotes urination and reduces edema:** Used in disorders where Lung heat obstructs the downward movement of Lung qi, preventing water from moving and cutting off perspiration. This manifests as floating edema, facial edema, swelling of the extremities, fever and thirst, urinary difficulty, and a floating pulse. With Da Fu Pi (大腹皮) - *Arecae Pericarpium* and Fu Ling Pi (茯苓皮) - *Poriae Cutis* for superficial edema with urinary difficulty, as in Wu Pi Yin (五皮飲) - *Five-Peel Decoction*. With Ting Li Zi (葶藶子) - *Lepidii/Descurainiae Semen* for swelling of the face and eyes with urinary difficulty.
- **Also recently used for hypertension:** With Huang Qin (黃芩) - *Scutellariae Radix*, Jue Ming Zi (決明子) - *Cassiae Semen*, and Xia Ku Cao (夏枯草) - *Prunellae Spica* for hypertension due to ascendant Liver yang.

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
Contraindicated for cough or wheezing from Lung cold.

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
Good quality consists of thick, white, pliable pieces of bark without any orange outer bark.

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
