---
# 🔹 Core Metadata (Universal Fields)
id: "herb-20251001123706"
name: "Shen Qu / Massa medicata fermentata"
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
  hanzi: "神曲"
  pinyin: "Shén Qū"
  pharmaceutical: "Massa medicata fermentata"
  english: "medicated leaven"
  alternate_names: []

  # TCM Properties
  taste: [sweet, acrid, warm]
  temperature: "warm"
  channels: [Spleen, Stomach]

  # Clinical Information
  dosage: "6-15g"
  toxicity: "none noted"
  functions: [Reduces food stagnation, Harmonizes the Stomach, Promotes the flow of qi, Alleviates diarrhea]
  dui_yao: []

  # Additional Information
  constituents: [Fermented mass of the following ingredients: flour (100 parts), Armeniacae Semen amarum (4 parts), Phaseoli Semen (4 parts), Artemisiae annuae Herba recens (7 parts), Xanthii Herba recens (7 parts), Polygoni hydropiperis Herba recens (7 parts), Volatile oil, glycosides, fixed oil, vitamin B, yeast]
  quality: "Good quality consists of dry, aged pieces without insect holes or an unpleasant moldy smell."
  text_first_appeared: "Materia Medica of Medicinal Properties"

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

Massa medicata fermentata (shén qū) is acrid, sweet, and warm, but its acrid flavor does not overly disperse, its sweetness does not accumulate or obstruct, and its warmth does not dry. It is highly valued for its ability to promote the flow of qi, regulate the middle, reduce food stagnation, and unbind the Stomach. It is most appropriate for food stagnation due to overconsumption of starch and grains, leading to qi stasis with abdominal distention and diarrhea.

This substance directs qi downward and transforms phlegm, warms the Stomach, and transforms thin mucus. Seeking Accuracy in the Materia Medica explains that it is acrid, sweet, and warm; disperses qi, regulates the middle, warms the Stomach, transforms phlegm, drives out water, and reduces stagnation. In children it tonifies the Spleen.

Physicians use it for regulating treatments; however, for best results it should be combined with herbs that tonify the Spleen.

As a substance that strengthens the Spleen, it alleviates diarrhea and distention: "[It treats] all disorders of diarrhea, dysentery, distention, and fullness." (Grand Materia Medica) Less well-known, however, is its ability to reduce lactation and facilitate weaning: "For postpartum women who wish to cease lactating, dry-fry and grind [it], then take 6g with wine twice a day until the milk stops: very effective." (Grand Materia Medica)

---
---

## 🔑 TCM Properties

**Taste:** `= join(this.herb_data.taste, ", ")`
**Temperature:** `= this.herb_data.temperature`
**Channels Entered:** `= join(this.herb_data.channels, ", ")`

---

## ⚡ Functions & Actions

- Reduces food stagnation and harmonizes the Stomach: for Stomach cold with food stagnation or accumulation, with such symptoms as epigastric and abdominal fullness or distention, lack of appetite, borborygmus, and diarrhea.
    - With Atractylodis macrocephalae Rhizoma (bái zhú) for food stagnation and diarrhea due to Spleen deficiency.
    - With Aurantii Fructus (zhǐ ké) for reduced appetite and fullness and distention of the epigastrium and abdomen due to cold stagnation, as in Unripe Bitter Orange Pill to Guide out Stagnation (zhǐ shí dǎo zhì wán).
    - With Arecae Semen (bīng láng) for childhood nutritional impairment or focal distention of the abdomen due to food stagnation.
    - With Aucklandiae Radix (mù xiāng) and Amomi Fructus (shā rén) for abdominal pain associated with food stagnation.
    - With exterior-releasing herbs for diarrhea accompanying externally-contracted disorders.
- Also added to pills that contain minerals to aid in their digestion and absorption, as in Magnetite and Cinnabar Pill (cí zhū wán).

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
"An acrid, warm, extremely drying medicinal. It should not be used when the Spleen yin is deficient, nor when Stomach fire blazes." (Harm and Benefit in the Materia Medica)

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
Good quality consists of dry, aged pieces without insect holes or an unpleasant moldy smell.

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
