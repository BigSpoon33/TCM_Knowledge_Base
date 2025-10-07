---
# 🔹 Core Metadata (Universal Fields)
id: "herb-20251001123706"
name: "Ze Lan"
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
  hanzi: "泽兰"
  pinyin: "Ze Lan"
  pharmaceutical: "Lycopi Herba"
  english: "Lycopus Herb"
  alternate_names: []

  # TCM Properties
  taste: [Bitter, acrid]
  temperature: "Slightly warm"
  channels: [Liver, Spleen]

  # Clinical Information
  dosage: "9-15g"
  toxicity: "None"
  functions: [Invigorates the blood, Dispels stasis, Promotes urination]
  dui_yao: []

  # Additional Information
  constituents: [Volatile oil: hexanal, hexanol, cis-3-hexen-1-ol, trans-3-hexen-1-ol, α-thujene, α-pinene, β-pinene, myrcene, humulene, sabinene, camphene, α-phellandrene, β-phellandrene, linalool, limonene, benzaldehyde, p-cymene, γ-terpinene, terpinene-4-ol, trans-pinocarveol, methyl salicylate, myrtenol, geranyl acetate, bornyl acetate, γ-elemene, δ-elemene, bergaptene, α-cubebin, β-cubebin, δ-selinene, nerolidol, diethylphthalate, Triterpenes: oleanolic acid, betulinic acid, 3-epimaslinic acid, euscaphic acid, 2α-hydroxyursolic acid, tormentic acid, β-sitosterol]
  quality: "Good quality consists of unfragmented, yellowish-green plants with many leaves and flowers."
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

Lycopi Herba (ze lan) has three distinctive qualities: it invigorates the blood, facilitates urination, and accomplishes these actions in a gentle, harmonious manner. Materia Medica of Ri Hua-Zi says that it "nourishes the blood and qi, breaks up retained blood, reduces mobile and fixed abdominal masses, and all disorders surrounding the birth process ... reduces blood stasis due to traumatic injury." Many texts emphasize its importance in gynecology, particularly for abdominal masses and abdominal pain. This results from its qualities: acrid, such that it disperses; bitter, such that it drains; warm, such that it unblocks; and aromatic, such that it pierces congealed yin. Because it enters the blood aspect of the Liver channel, it is in this arena that its qualities will be expressed.

The ability of this herb to facilitate urination was recorded in the Divine Husbandman's Classic of the Materia Medica in the second century, where it is stated that it can be used for "distended abdominal edema, and floating edema of the trunk, face, and extremities." Commentary on the Divine Husbandman's Classic of Materia Medica elaborates:

If assisted by herbs that augment the Spleen earth, and enhanced [by combination] with Stephaniae/Cocculi/etc. Radix (fen fang ji), it governs distended abdominal edema and floating edema of the trunk, face, and extremities, as well as water qi within the bone joints.

### Mechanisms of Selected Combinations

- WITH STEPHANIAE TETRANDRAE RADIX (fen fang ji); see page 314
- WITH LEONURI HERBA (yi mu cao); see page 615

---
---

## 🔑 TCM Properties

**Taste:** `= join(this.herb_data.taste, ", ")`
**Temperature:** `= this.herb_data.temperature`
**Channels Entered:** `= join(this.herb_data.channels, ", ")`

---

## ⚡ Functions & Actions

- Invigorates the blood and dispels stasis: for pain due to blood stasis obstructing the menses, and for postpartum abdominal pain from blood stasis. Also used topically or internally for pain and swelling from traumatic injury or abscess.
    - With Chuanxiong Rhizoma (chuan xiong) for amenorrhea, dysmenorrhea, and trauma-induced pain.
    - With Salviae miltiorrhizae Radix (dan shen) for trauma-induced swelling and pain or pain in the chest and hypochondria.
    - With Curcumae longae Rhizoma (jiang huang) and Tinosporae sinensis Caulis (kuan jin teng) as an external wash for trauma-induced swelling and pain.
    - With Angelicae sinensis Radix (dang gui), Lonicerae Flos (jin yin hua), and Glycyrrhizae Radix (gan cao) for swelling and pain from abscess.
- Promotes urination: for postpartum edema, postpartum painful urinary dribbling, and systemic or facial edema. This effect is rather mild and is adjunctive in nature.
    - With Imperatae Rhizoma (bai mao gen) for edema with accompanying heat symptoms.
    - With Stephaniae tetrandrae Radix (fen fang ji) for postpartum edema.

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
- Use with caution in those with blood deficiency or in the absence of blood stasis.
- Use with caution during pregnancy.

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
Good quality consists of unfragmented, yellowish-green plants with many leaves and flowers.

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
