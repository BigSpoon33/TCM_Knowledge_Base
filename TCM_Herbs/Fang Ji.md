---
# 🔹 Core Metadata (Universal Fields)
id: "herb-20251001123706"
name: "Fang Ji / Mu Fang Ji"
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
  hanzi: "防己"
  pinyin: "Fáng Jǐ / Mù Fáng Jǐ"
  pharmaceutical: "Cocculi Radix"
  english: "Cocculus root"
  alternate_names: []

  # TCM Properties
  taste: [Bitter, Acrid]
  temperature: "Cold"
  channels: [Bladder, Kidney, Spleen]

  # Clinical Information
  dosage: "6-12g"
  toxicity: "Aristolochic acid in some species (e.g., *Aristolochia fangchi*). Use with caution."
  functions: [Dispels wind and eliminates dampness, Promotes urination and reduces swellings]
  dui_yao: []

  # Additional Information
  constituents: [Alkaloids: tetrandrine (hanfangchin A), fangchinoline (demethyltetrandrine, hanfangchin B), hanfangchin C, menisine, menisidine, cyclanoline, berbamine, oxofangchinine, stephanthrine, (+)-2-methylfangchinoline, (+)-2-methyltetrandrine, 2,2'-N,N-dichloromethyltetrandrine, fenfangjine A, B, C, D, magnoflorine, oblongine, Alkaloids: trilobine, isotrilobine, trilobamine, magnoflorine, menisarine, normenisarine, epistephanine, coclobine, flavonoids, phenolic compounds, organic acids, volatile oils]
  quality: "Good quality consists of heavy, uniform, and powdery roots. Good quality consists of uniform, solid, and heavy roots."
  text_first_appeared: "Discussion of Medicinal Properties"

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

Several commentators on the materia medica tradition have described the differences in usage of these two herbs. In *Omissions from the [Classic of the] Materia Medica*, Chen Cang-Qi states that "Stephaniae tetrandrae Radix (*han fang ji*) governs water *qi* while Cocculi Radix (*mu fang ji*) governs wind *qi* as it disseminates and unblocks." Similarly, Huang Yuan-Yu notes in *Changsha Explanation of Medicines* that Stephaniae tetrandrae Radix (*han fang ji*) drains damp excess from the channels and collaterals while Cocculi Radix (*mu fang ji*) drains water pathogen from the organs. This clear differentiation was somewhat disputed by Zhang Shan-Lei in *Rectification of the Meaning of Materia Medica*, where he says that these two herbs are actually rather close in their usage.

---
---

## 🔑 TCM Properties

**Taste:** `= join(this.herb_data.taste, ", ")`
**Temperature:** `= this.herb_data.temperature`
**Channels Entered:** `= join(this.herb_data.channels, ", ")`

---

## ⚡ Functions & Actions

*   Dispels wind and eliminates dampness: for painful obstruction, especially where there is also heat. However, as it is effective in treating pain, it can also be used for other types of painful obstruction.
    *   With *Achyranthis bidentatae* Radix (*niu xi*), *Chaenomelis* Fructus (*mu gua*), and *Phellodendri* Cortex (*huang bai*) for damp-heat painful obstruction.
    *   With *Notopterygii Rhizoma seu Radix* (*qiang huo*) and *Angelicae pubescentis* Radix (*du huo*) for wind-cold-damp painful obstruction.
*   Promotes urination and reduces swellings: for edema with urinary dysfunction.
    *   With *Malvae* Fructus (*dong kui guo*), *Saposhnikoviae* Radix (*fang feng*), and *Plantaginis Semen* (*che qian zi*) for edema with urinary dysfunction.
    *   With *Cinnamomi Ramulus* (*gui zhi*) and *Poria* (*fu ling*) for edema.

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
Use with caution during pregnancy.

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
Good quality consists of heavy, uniform, and powdery roots. Good quality consists of uniform, solid, and heavy roots.

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
