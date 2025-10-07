---
# 🔹 Core Metadata (Universal Fields)
id: "herb-20251001123706"
name: "Sang Zhi"
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
  hanzi: "桑枝"
  pinyin: "Sāng zhī"
  pharmaceutical: "Mori Ramulus"
  english: "Mulberry Twig"
  alternate_names: []

  # TCM Properties
  taste: [Bitter]
  temperature: "Neutral"
  channels: [Liver]

  # Clinical Information
  dosage: "9-15g (up to 30g in high doses)"
  toxicity: "None noted"
  functions: [Dispels wind, Unblocks the channels and collaterals, Benefits the joints]
  dui_yao: []

  # Additional Information
  constituents: [Flavonoids: mulberrin, mulberrochromene, cyclomulberrin, cyclomulberrochromene, dihydrokaempferol, Other constituents: morin, dihydromorin, cudranin, 2,4,4',6-tetrahydroxybenzophenone, 2,3',4,4',6-pentahydroxybenzophenone, 2',4,3',5'-tetrahydroxystilbene, alboctalol]
  quality: "Good quality consists of thin, tender twigs without leaves."
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

Bitter, neutral, yet slightly cooling, Mori Ramulus (sang zhi) enters the Liver channel. It expels wind-dampness, unblocks the channels and collaterals, and frees the movement of the joints. Mori Ramulus (sang zhi) is therefore used in the treatment of wind-damp painful obstruction disorder with numbness and spasms, as well as pain and itching in the limbs due to externally-contracted pathogenic wind.

Treasury of Words on the Materia Medica notes that "[Mori Ramulus (sang zhi)] dispels painful contraction [due to] wind qi." Essentials of the Materia Medica says that it "facilitates [movement of the] joints, nourishes the yin fluids and yang fluids, mobilizes water, and dispels wind." The Illustrated Classic of the Materia Medica has the most complete description of this medicinal's wide range of action:

[It] treats localized itching and dryness due to wind, leg qi, wind qi, contractions of the four limbs, rebellious qi, vertigo, and Lung qi cough; reduces food [stagnation], facilitates urination, and also treats dryness of the mouth.

---
---

## 🔑 TCM Properties

**Taste:** `= join(this.herb_data.taste, ", ")`
**Temperature:** `= this.herb_data.temperature`
**Channels Entered:** `= join(this.herb_data.channels, ", ")`

---

## ⚡ Functions & Actions

- Dispels wind, unblocks the channels and collaterals, and benefits the joints: for wind-damp painful obstruction with spasms. Most appropriate for the warm type that affects the upper extremities. Also used in formulas for numbness in the extremities or hemiplegia as sequelae to wind-stroke.
  - With Mori Folium (sang ye) to disperse externally-contracted wind-heat in the head, face, muscle layer, channels collaterals, and joints.
  - With Cinnamomi Ramulus (gui zhi) for pain in the upper extremities.
  - With Notopterygii Rhizoma seu Radix (qiang huo), Angelicae Pubescentis Radix (du huo), and Piperis Kadsurae Caulis (hai feng teng) for wind-damp painful obstruction, as in Remove Painful Obstruction Decoction from Medical Revelations (juan bi tang).
- Also used for edema, especially when accompanied by joint pain.

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
None noted

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
Good quality consists of thin, tender twigs without leaves.

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
