---
# 🔹 Core Metadata (Universal Fields)
id: "herb-20251001123706"
name: "Kochia Fruit / Di Fu Zi"
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
  hanzi: "地肤子"
  pinyin: "Di Fu Zi"
  pharmaceutical: "Kochiae Fructus"
  english: "Kochia fruit, broom cypress"
  alternate_names: []

  # TCM Properties
  taste: [Sweet, bitter, cold]
  temperature: "cold"
  channels: [Bladder, Kidney]

  # Clinical Information
  dosage: "9-15g"
  toxicity: "Allergic reactions following oral application of the decoction have been reported in rare cases. The symptoms included urticaria, generalized pruritus, and vesicles on the mouth and lips."
  functions: [Clears damp-heat, promotes urination, Expels dampness, stops itching]
  dui_yao: []

  # Additional Information
  constituents: [Volatile oil: 2-propyl-toluene, 1-methyl-4-isopropenylcyclohexane, (E)-3,7-dimethyl-2,6-octadienal, 2-methyloctanoic acid methylester, 1-methoxy-4-(1-propenyl)benzene, methyl nonanate, ethylnonanate, 1-undecyne, 5-ethyl-2-nonanol, 4,8-dimethyl-1-nonanol, δ-farnesene, 2,6-di-tert-butyl-1,4-benzoquinone, β-ionone, ethyl dodecanate, methyl tetradecanate, hexadecane, ethyl hexadecanate, octadecane, 6,10,14-trimethyl-2-pentadecanone, eicosane, heneicosane, docosane, triacontanol, Triterpenes: Oleanolic acid, kochioside A, B, 3-O-[β-D-xylopyranosyl(1→3)-β-D-glucopyranosyl]oleanolic acid (momordin Ic), 3-O-[β-D-xylopyranosyl(1→3)-β-D-glucuronopyranosyl]oleanolic acid-28-O-β-D-glucopyranoside (momordin Ie), 3-O-[β-D-xylopyranosyl(1→3)-β-D-methylglucuronopyranosylate]oleanolic acid, 20-hydroxyecdysone, 25,20-dihydroxyecdysone, 20-hydroxy-24-methyleneecdysone, 20-hydroxy-24-methylecdysone, Alkaloids: Harman, harmine, Other constituents: Flavonoids, fixed oil, carotenoids]
  quality: "Good quality consists of well-dried, full, greyish green fruit without foreign matter."
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

*Di Fu Zi* (Kochiae Fructus) is acrid, bitter, and cold; it clears, facilitates, dredges, and disperses. It primarily enters the Bladder channel, which governs the exterior of the body, and also the lower outlet of the fluid pathways. Kochiae (*di fu zi*) Fructus mobilizes the exterior and thus alleviates itching by dispersing pathogenic wind in the muscle layer and skin. It also clears damp-heat internally and facilitates urination. Thus, it is often used, both internally and externally, for intense itching of the skin due to wind-dampness affecting the exterior in such disorders as eczema and scabies, or damp-heat in the genitals.

This herb is commonly used for urinary difficulty that is dark, scanty, burning, and painful due to accumulated damp-heat in the Bladder. Its ability to clear wind-heat enables it to treat swollen, painful eyes and head, or dizziness.

---
---

## 🔑 TCM Properties

**Taste:** `= join(this.herb_data.taste, ", ")`
**Temperature:** `= this.herb_data.temperature`
**Channels Entered:** `= join(this.herb_data.channels, ", ")`

---

## ⚡ Functions & Actions

*   **Clears damp-heat and promotes urination:** For painful urinary dribbling due to damp-heat accumulating in the Bladder with such symptoms as dark, burning, and scanty urine.
    *   With Polyporus (*zhu ling*), Tetrapanacis Medulla (*tong cao*), and Dianthi Herba (*qu mai*) for urinary discomfort due to damp-heat in the Bladder.
*   **Expels dampness and stops itching:** Used both internally and topically for damp skin disorders and other dermatological problems where itching is a major symptom, such as eczema and scabies. Also for damp-heat in the external genitals.
    *   With Sophorae Flavescentis Radix (*ku shen*) for itchiness and irritation of the skin due to damp-heat.
    *   With Cnidii Fructus (*she chuang zi*) as an external wash for itchy skin.
    *   With Rehmanniae Radix (*sheng di huang*) and Dictamni Cortex (*bai xian pi*) for eczema and itchy skin due to damp-heat or wind-heat.

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
See TOXICITY below.

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
Good quality consists of well-dried, full, greyish green fruit without foreign matter.

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
