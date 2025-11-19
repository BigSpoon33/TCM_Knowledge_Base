---
# 🔹 Core Metadata (Universal Fields)
id: "herb-20251001123706"
name: "Yi Mu Cao"
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
  hanzi: "益母草"
  pinyin: "yì mǔ cǎo"
  pharmaceutical: "Leonuri Herba"
  english: "Motherwort Herb"
  alternate_names: []

  # TCM Properties
  taste: [Acrid, bitter]
  temperature: "Slightly cold"
  channels: [Heart, Liver, Bladder]

  # Clinical Information
  dosage: "9-15g (large doses up to 30g)"
  toxicity: "Due to its alkaloid content, overdosage of this herb is slightly toxic, with side effects appearing 4-6 hours after ingestion. Symptoms include sudden general weakness, stiffness and paralysis, general body pains, an oppressive sensation in the chest, excessive sweating, low blood pressure, cold extremities, and, in severe cases, shock, cyanosis, and respiratory paralysis. Overdosage can also cause miscarriage. After ingestion of 20-30g, toxic reactions may appear in 4-10 hours. Symptoms include generalized weakness, paralysis of the lower limbs, numb, painful sensation of the whole body, an oppressive sensation in the chest, and sweating, along with normal consciousness and clear speech. For this reason, the maximum dose of 15g per day should not be exceeded."
  functions: [Invigorates the blood and dispels stasis, Promotes urination and reduces swelling, Clears heat and resolves toxicity]
  dui_yao: []

  # Additional Information
  constituents: [Alkaloids: leonurine, stachydrine, leonuridine, leonurinine, Flavonoids: rutin, kaempferol, quercetin, apigenin, genkwanin, Diterpenes: prehispanolone, hispanolone, geleopsin, preleoheterin, leoheterin, Volatile oil: 1-octen-3-ol, 3-octanol, β-ocimene, linalool, nonanol, copaene, caryophyllene, caryophyllene oxide, humulene, γ-elemene, cadinene, hexahydrofarnesylacetone, methyl palmitate, dibutylphthalate, nonadecane, Organic acids: palmitic acid, fumaric acid, lauric acid, palmitic acid, oleic acid, linoleic acid, linolenic acid, arachidic acid, stearic acid, Other constituents: iridoids, phytol, leonuramide]
  quality: "Good quality consists of tender plants with many greyish green leaves. Old plants that mostly consist of thick stems should not be used."
  text_first_appeared: "Divine Husbandman's Classic of Materia Medica"

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

Acrid, such that it disperses blockage, Leonuri Herba (yi mu cao) enters the blood level of the Heart and Liver channels to invigorate the flow of blood, remove blood stasis, and regulate menstruation. It is thus appropriate for all disorders involving blood stasis, especially irregular menstruation, dysmenorrhea, postpartum abdominal pain, and heavy periods and continual menstrual bleeding when clotting is evident. It also facilitates urination and resolves toxicity, and is thus especially indicated when edema and blood stagnation co-exist, or blood stagnation is involved with toxic sores and swellings.

---
---

## 🔑 TCM Properties

**Taste:** `= join(this.herb_data.taste, ", ")`
**Temperature:** `= this.herb_data.temperature`
**Channels Entered:** `= join(this.herb_data.channels, ", ")`

---

## ⚡ Functions & Actions

Invigorates the blood and dispels stasis: commonly used for gynecological disorders such as irregular menstruation, premenstrual abdominal pain, heavy menstruation with clots, fixed abdominal masses, infertility, and postpartum abdominal pain with retained lochia. Also used for traumatic pain.
    -   With Angelicae sinensis Radix (dang gui) for irregular menstruation, scanty menstruation, lower abdominal distention and pain, and infertility due to blood stasis.
    -   Add Chuanxiong Rhizoma (chuan xiong) and Cyperi Rhizoma (xiang fu) for dysmenorrhea or lower abdominal pain due to postpartum blood stasis.
    -   With Typhae Pollen (pu huang) for retained lochia.
-   Promotes urination and reduces swelling: for acute systemic edema. Especially useful when accompanied by blood in the urine.
    -   With Imperatae Rhizoma (bai mao gen) for edema accompanied by blood stasis. Recently this combination has been used in treating edema associated with nephritis.
    -   With Lycopi Herba (ze lan) for disorders involving both blood stasis and pathogenic fluids.
    -   With Polygonati Rhizoma (huang jing), Pyrrosiae Folium (shi wei), and Malvae Fructus (dong kui guo) for kidney stones and bloody urine.
-   Clears heat and resolves toxicity: for sores, abscesses, and toxic swellings. Also for itchy rashes from damp-heat collecting and steaming the muscles and subcutaneous tissues. Used either internally or topically.

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
Contraindicated in those with yin deficiency or insufficient blood, and during pregnancy. Leonuri Herba (yi mu cao) is appropriate for blood heat, blood stasis, and delayed or difficult labor. It is not appropriate for constitutional blood and qi deficiency associated with cold, or for any disorder involving unstable slipping downward.

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
Good quality consists of tender plants with many greyish green leaves. Old plants that mostly consist of thick stems should not be used.

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
