---
# 🔹 Core Metadata (Universal Fields)
id: "herb-20251001123706"
name: "Bai Dou Kou (Amomi Fructus rotundus)"
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
  hanzi: "白豆蔻"
  pinyin: "Bái Dòu Kòu"
  pharmaceutical: "Amomi Fructus rotundus"
  english: "round cardamon, cardamon cluster"
  alternate_names: []

  # TCM Properties
  taste: [acrid, aromatic]
  temperature: "warm"
  channels: [Lung, Spleen, Stomach]

  # Clinical Information
  dosage: "3-6g"
  toxicity: "Contraindicated in those with yin or blood deficiency."
  functions: [Promotes the movement of qi, transforms dampness, and strengthens the Stomach, Warms the middle burner and causes rebellious qi to descend]
  dui_yao: []

  # Additional Information
  constituents: [Volatile oil: primarily 1,8-cineole, β-pinene; α-pinene, caryophyllene, bornyl acetate, α-terpineol, linalool, terpinene-4-ol, aromadendrene, γ-patchoulene, α-elemene, γ-cubebene, sabinene hydrate, nerolidol, bisabolene, camphene, carvone, Volatile oil: primarily 1,8-cineole, carvone, α-terpineol; β-pinene, γ-pinene, farnesol, linalool, p-cymene, sabinene, myrcene, myrcenol, 1,4-cineole, limonene, 3-carene, β-terpineol, camphor, borneol]
  quality: "Good quality consists of large, unfragmented, full fruit with an intense aroma."
  text_first_appeared: "Omissions from the Materia Medica"

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

Acrid, warm, and aromatic, **Amomi Fructus rotundus** (_bái dòu kòu_) enters the Lung, Spleen, and Stomach channels. It warms, disseminates, and pierces through turbidity by virtue of its aroma, and can mobilize stagnant qi within the Triple Burner, while opening the middle and easing the Stomach. It is particularly effective for dredging and dispersing Lung qi blockage. It can warm the middle, transform dampness, awaken the Spleen, and restore the appetite. In this way it treats phlegm-dampness obstructing the Lungs and qi stasis which causes a stifling sensation in the chest; it does this by its warming transformation of phlegm-dampness and its ability to disseminate the Lung qi. It also treats cold-dampness obstructing the middle with nausea, vomiting, hiccough or reflux, and Stomach and Intestinal qi constraint with epigastric and abdominal distention and pain.

---
---

## 🔑 TCM Properties

**Taste:** `= join(this.herb_data.taste, ", ")`
**Temperature:** `= this.herb_data.temperature`
**Channels Entered:** `= join(this.herb_data.channels, ", ")`

---

## ⚡ Functions & Actions

#### Promotes the movement of qi, transforms dampness, and strengthens the Stomach:

For dampness obstructing the middle burner as well as damp-warmth. Symptoms include a stifling sensation in the chest, fullness in the epigastrium, lack of appetite, and a very greasy tongue coating.

- With **Amomi Fructus** (_shā rén_) for fullness and a stifling sensation in the chest, vomiting, diarrhea, and a thick tongue coating from cold-dampness encumbering the Spleen and obstructing the movement of qi.

- With **Citri Reticulatae Pericarpium** (_chén pí_) for fullness and discomfort in the chest and abdomen, belching, nausea, vomiting, and diarrhea due to Spleen and Stomach deficiency with a subsequent accumulation of turbid dampness.

- With **Armeniacae Semen** (_xìng rén_) and **Coicis Semen** (_yì yì rén_) for headache, stifling sensation in the chest, fatigue, dark urine with reduced output, diarrhea, and usually accompanied by a white, greasy tongue coating, as in the early stages of damp-warmth. See **Three-Nut Decoction** (_Sān Rén Tāng_).

- With **Scutellariae Radix** (_huáng qín_), **Talcum** (_huá shí_), and **Polyporus** (_zhū líng_) for damp-warmth in the middle burner, with more heat than dampness, marked by recurring fevers, body aches, dark urine, and a yellow tongue coating, as in **Scutellaria and Talcum Decoction** (_Huáng Qín Huá Shí Tāng_).

- With **Magnoliae Officinalis Cortex** (_hòu pò_) and **Atractylodis Rhizoma** (_cāng zhú_) for distention due to qi obstruction or cold-dampness in the Spleen and Stomach.

#### Warms the middle burner and causes rebellious qi to descend:

For vomiting due to cold from deficiency of the Spleen and Stomach, Stomach cold, cold-dampness, or food stagnation.

- With **Pogostemonis/Agastaches Herba** (_huò xiāng_) and **Pinelliae Rhizoma preparatum** (_zhì bàn xià_) for nausea and vomiting, epigastric discomfort, and reduced appetite due to either cold-dampness or food stagnation. This combination can also be used for morning sickness.

- With **Caryophylli Flos** (_dīng xiāng_) for belching due to Stomach cold.

- Powdered together with **Amomi Fructus** (_shā rén_) and **Glycyrrhizae Radix** (_gān căo_) and placed inside an infant's mouth for spitting up of milk.

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
"Acrid, hot, and intensely drying, it promotes movement in the Triple Burner; it should not be included [in a prescription] whenever nausea and vomiting are not due to cold or yang deficiency." (_Harm and Benefit in the Materia Medica_)

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
Good quality consists of large, unfragmented, full fruit with an intense aroma.

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
