---
# 🔹 Core Metadata (Universal Fields)
id: "herb-20251001123706"
name: "Shan Zha"
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
  hanzi: "山楂"
  pinyin: "Shān Zhā"
  pharmaceutical: "Crataegi Fructus"
  english: "crataegus fruit, hawthorn fruit"
  alternate_names: []

  # TCM Properties
  taste: [Sour, Sweet]
  temperature: "Slightly Warm"
  channels: [Liver, Spleen, Stomach]

  # Clinical Information
  dosage: "9-12g"
  toxicity: "None"
  functions: [Reduces food stagnation and transforms accumulation, Transforms blood stasis and dissipates clumps, Stops diarrhea, Used for hypertension, coronary artery disease, and elevated serum cholesterol]
  dui_yao: []

  # Additional Information
  constituents: [Flavonoids: hyperoside, quercetin, vitexin, rutin, epicatechin, eriodictyol-7,3-diglucoside, Organic acids: citric acid, oxalic acid, malic acid, chlorogenic acid, ursolic acid, oleanolic acid, oleic acid, linoleic acid, stearic acid, palmitic acid, succinic acid, Hydrocarbons: 3-methyl-hexane, heptane, 2-methylheptane, 2,3-dimethylheptane, 3-methyl-cyclohexane, 1,3-dimethyl-cis-cyclohexane, 1,4-dimethyl-cis-cyclohexane, 1,3,5-trimethyl cyclohexane, 1,2,3-trimethyl cyclohexane, ethyl cyclohexane, propyl cyclohexane, 1-propenyl cyclohexane, butyl cyclohexane, 4-methyl-nonane, toluene, xylene, 1,2,3-trimethyl benzene, (1s,3s)-(+)-m-menthane, Other constituents: tannin, sugar, proteins, vitamin C]
  quality: "Good quality of the northern variety consists of large fruit (or slices) with a red or reddish brown surface and fleshy pulp. Good quality of the southern variety consists of reddish brown fruit, uniform in size, with thick pulp. Because the northern variety is more sour, it is considered to be of superior quality."
  text_first_appeared: "Collection of Commentaries on the Classic of the Materia Medica"

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

Sour, sweet, and slightly warm, Crataegi Fructus (shan zha) awakens the Spleen, unbinds the Stomach, promotes food intake, and assists digestion. It is particularly useful for problems due to overindulgence in meat and greasy foods. For this purpose it can be used alone as a decoction. It stops diarrhea and dysenteric disorders. It also enters the Liver channel to disperse blood stasis and invigorate the blood.

---
---

## 🔑 TCM Properties

**Taste:** `= join(this.herb_data.taste, ", ")`
**Temperature:** `= this.herb_data.temperature`
**Channels Entered:** `= join(this.herb_data.channels, ", ")`

---

## ⚡ Functions & Actions

- Reduces food stagnation and transforms accumulation: for accumulation due to meat or greasy foods with abdominal distention, pain, or diarrhea.
    - With Massa Medicata Fermentata (shen qu) for abdominal distention, belching, and reduced appetite associated with food stagnation, as in Preserve Harmony Pill (Bao He Wan).
    - Hordei Fructus Germinatus (mai ya) is often added.
    - Also effective for childhood nutritional impairment due to improper breast feeding.
    - Add Aucklandiae Radix (mu xiang) and Aurantii Fructus (zhi ke) for more intense symptoms such as pain.
    - With Aucklandiae Radix (mu xiang), Myristicae Semen (dou kou), and Lablab Semen Album (bai bian dou) for abdominal distention and pain, diarrhea, and dysenteric disorders. The ingredients are usually dry-fried before decocting.
- Transforms blood stasis and dissipates clumps: for postpartum abdominal pain and clumps due to blood stasis.
    - Also for bulging disorders.
    - With Chuanxiong Rhizoma (chuan xiong), Leonuri Herba (yi mu cao), and Angelicae Sinensis Radix (dang gui) for menstrual pain and postpartum lower abdominal pain due to blood stasis.
    - With Salviae Miltiorrhizae Radix (dan shen) for painful obstruction of the chest due to blood stasis in the Heart channel.
    - With Foeniculi Fructus (xiao hui xiang) and Citri Reticulatae Semen (ju he) for bulging disorders with testicular pain and swelling associated with prolapse.
- Stops diarrhea: the partially charred herb is used for the diarrhea of chronic dysentery-like disorders.
- Also recently used for hypertension, coronary artery disease, and elevated serum cholesterol.

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
- Use with caution in those with weakness or deficiency of the Spleen and Stomach.
- Large doses are absolutely contraindicated during pregnancy, as this can lead to fetal death.

Its nature conquers and cuts down; if Stomach patients have no food accumulation, or if the Spleen is deficient and cannot transport and transform, or those with no appetite will consume it, it will conversely conquer and curtail the generative qi of the Spleen and Stomach, causing restless irritability and an increase in hunger. If the Spleen and Stomach are deficient, but there is also accumulated stagnation, it should be used together with herbs that tonify the qi, but should not be overly used. It can also injure the teeth. (Harm and Benefit in the Materia Medica)

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
Good quality of the northern variety consists of large fruit (or slices) with a red or reddish brown surface and fleshy pulp. Good quality of the southern variety consists of reddish brown fruit, uniform in size, with thick pulp. Because the northern variety is more sour, it is considered to be of superior quality.

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
