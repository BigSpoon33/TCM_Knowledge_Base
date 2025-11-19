---
# 🔹 Core Metadata (Universal Fields)
id: "herb-20251001123706"
name: "Ji Nei Jin"
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
  hanzi: "雞內金"
  pinyin: "ji nei jin"
  pharmaceutical: "Gigeriae Galli Endothelium Corneum"
  english: "Gizzard Lining"
  alternate_names: []

  # TCM Properties
  taste: [Sweet, neutral]
  temperature: "neutral"
  channels: [Bladder, Small Intestine, Spleen, Stomach]

  # Clinical Information
  dosage: "3-9g"
  toxicity: "There is one report of significant side effects from the combination of this herb with Rehmanniae Radix Preparata and Polygoni Multiflori Radix, including dry mouth, vertigo, hoarseness, diminished consciousness, and spasms of the limbs. There has been one report of epistaxis following ingestion of this substance."
  functions: [Reduces all types of food stagnation, Stops enuresis, Dissolves stones]
  dui_yao: []

  # Additional Information
  constituents: [Proteins: ventriculin, amylase, pepsin, diastase, keratin, Amino acids: lysine, histidine, arginine, glutamic acid, aspartic acid, leucine, threonine, serine, glycine, alanine, cysteine, valine, methionine, isoleucine, tyrosine, phenylalanine, proline, tryptophan, Other constituents: vitamin B1, B2, nicotinic acid, Fixed oil (30%): erucic acid, linoleic acid, linolenic acid, Other constituents: sinapine, raphanin, brassicasterol, 22-dehydrocampesterol, β-sitosterol, γ-sitosterol]
  quality: "-   Good quality consists of large, unfragmented, yellow, and clean pieces.
-   Good quality consists of full, oily, reddish brown seeds without foreign matter."
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

Sweet and harmonious in nature, Gigeriae Galli Endothelium Corneum (*ji nei jin*) augments the Spleen earth and tonifies the Stomach qi while reducing food stagnation and transforming stones. It enters the Bladder channel and inhibits urination. Because it reduces food stagnation, it is used for nausea, vomiting, diarrhea, and childhood nutritional impairment from accumulated undigested food. Because it transforms stones, it is used for stones in either the biliary or urinary tracts. And because it secures the Kidney essence and halts enuresis, it can be used for spermatorrhea, urinary incontinence, and childhood bed-wetting.

This herb was a favorite of the early twentieth-century physician Zhang Xi-Chun. In Essays on Medicine Esteeming the Chinese and Respecting the Western, Zhang observes:

"Not only can it reduce accumulation in the Spleen and Stomach, regardless of which organ is affected by accumulation, Gigeriae Galli Endothelium Corneum (*ji nei jin*) can reduce them all. Thus, for abdominal masses in men, and both mobile and fixed abdominal masses in women, if taken over the long term it can cure them all."

---
---

## 🔑 TCM Properties

**Taste:** `= join(this.herb_data.taste, ", ")`
**Temperature:** `= this.herb_data.temperature`
**Channels Entered:** `= join(this.herb_data.channels, ", ")`

---

## ⚡ Functions & Actions

- **Strongly reduces food stagnation and improves the Spleen's transportive function:** for various types of food stagnation. Used alone for mild cases, usually dry-fried and powdered. Also important in the treatment of childhood nutritional impairment.
    - With Hordei Fructus Germinatus (*mai ya*) and Crataegi Fructus (*shan zha*) for indigestion, fullness, and distention of the epigastrium and abdomen, and childhood nutritional impairment. For concurrent deficiency of the Spleen and Stomach with reduced appetite and diarrhea, add Atractylodis Macrocephalae Rhizoma (*bai zhu*) along with Codonopsis Radix (*dang shen*) and Dioscoreae Rhizoma (*shan yao*).
    - With Salviae Miltiorrhizae Radix (*dan shen*) for epigastric pain, especially when associated with chronic hepatitis.
    - With Trionycis Carapax (*bie jia*) for childhood nutritional impairment, abdominal distention, and subcostal focal distention.
- **Secures the essence and stops enuresis:** for bed-wetting, urinary frequency, and urination at night.
    - With Mantidis Ootheca (*sang piao xiao*), Fossilia Ossis (*long gu*), and Ostreae Concha (*mu li*) for bed-wetting in children or urinary frequency in adults. When the diagnosis is a deficient and cold Bladder, Cervi Cornu Pantotrichum (*lu rong*) is often added.
    - With Cuscutae Semen (*tu si zi*) and Schisandrae Fructus (*wu wei zi*) for spontaneous emissions, as in Cuscuta Seed Pill (*tu si zi wan*).
- **Transforms hardness and dissolves stones:** for stones in either the urinary or biliary tract.
    - With *jin qian cao* (Lysimachiae/Desmodii/etc. Herba) for stones in the urinary or biliary tract.

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
Use with caution in those with Spleen deficiency where food stagnation is absent.
-   Should not be used together with Ginseng Radix (*ren shen*), Rehmanniae Radix Preparata (*shu di huang*), or Polygoni Multiflori Radix Preparata (*zhi he shou wu*).
-   Harm and Benefit in the Materia Medica cautions that it is "even more rapid in reducing phlegm and driving qi downward [than radish itself]. When deficient or weak patients consume it, qi becomes difficult to distribute affecting breathing."
-   The Materia Medica of Combination states that it is contraindicated when taking tonics.

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
-   Good quality consists of large, unfragmented, yellow, and clean pieces.
-   Good quality consists of full, oily, reddish brown seeds without foreign matter.

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
