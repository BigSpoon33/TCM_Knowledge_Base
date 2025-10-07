---
# 🔹 Core Metadata (Universal Fields)
id: "herb-20251001123706"
name: "He Ye"
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
  hanzi: "荷叶"
  pinyin: "hé yè"
  pharmaceutical: "Nelumbinis Folium"
  english: "Lotus Leaf"
  alternate_names: []

  # TCM Properties
  taste: [Bitter, slightly sweet, neutral]
  temperature: "neutral"
  channels: [Heart, Liver, Spleen]

  # Clinical Information
  dosage: "3-9g"
  toxicity: "none noted"
  functions: [Clears heat, Resolves summerheat, Raises clear yang, Stops bleeding]
  dui_yao: []

  # Additional Information
  constituents: [Alkaloids: nuciferine, N-nornuciferine, O-nornuciferine, anonaine, roemerine, dehydroroemerine, armepavine, N-methylcoclaurine, pronuciferine, liriodenine, Glycosides: nelumboside, isoquercitrin, Organic acids: citric acid, tartaric acid, malic acid, oxalic acid, succinic acid, Other constituents: quercetin, tannin, alanine, proline, arginine, γ-aminobutyric acid, betanidin, betanidine, isobetanin, isobetanidin, betanidin-5-O-β-cellobioside, isobetanidin-5-O-β-cellobioside, thiamine, riboflavine, vitamine A, lutein, β-carotene, α-tocopherol, proteins, fixed oil]
  quality: "Good quality consists of big, unfragmented, green leaves without moldy spots."
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

Nelumbinis Folium (he ye) is bitter, sweet, and neutral. It is aromatic and blue-green in color, entering the Liver, Heart, and Spleen channels. It is best for clearing heat, resolving summerheat, raising and discharging clear yang, and also stops bleeding. It is often used for excessive summerheat leading to splitting headache, stifling sensation of the chest, nausea, vomiting, and diarrhea. It can also be used for any type of bleeding.

The Renewed Materia Medica says that it can "cool, clear, and resolve summerheat, alleviate thirst, generate yang fluids, treat diarrhea and dysenteric disorders, while also resolving fire and heat."

Penetrating the Mysteries of the Materia Medica notes that it can "open the Stomach, reduce food [stagnation], stop bleeding, and secure the essence."

In the Zhang Convenient Reader of Materia Medica, Bing-Cheng explains its properties:

Nelumbinis Folium (he ye) is bitter, neutral, aromatic, blue-green in color, the leaves are shaped like the trigram ☳ (zhen) [symbolizing wood and the east] so that it enters the Liver channel. Liver stores the blood, thus this herb disperses blood and has the ability to raise yang.

---
---

## 🔑 TCM Properties

**Taste:** `= join(this.herb_data.taste, ", ")`
**Temperature:** `= this.herb_data.temperature`
**Channels Entered:** `= join(this.herb_data.channels, ", ")`

---

## ⚡ Functions & Actions

- Treats summerheat patterns: for fever, irritability, excessive sweating, scanty urine, and especially diarrhea due to summerheat.
  - With Lablab Flos (bian dou hua) and Lonicerae Flos (jin yin hua) for summerheat disorder, as in Clear the Collaterals Drink (qing luo yin). Note that this formula calls for all fresh ingredients.
- Raises and clears the yang of the Spleen: for diarrhea due to Spleen deficiency, especially in the aftermath of summerheat.
- Stops bleeding: primarily for bleeding in the lower burner due to heat or stagnation, but also for vomiting blood. Generally used as an adjunctive herb.
  - With Cirsii Herba (xiao ji), Rubiae Radix (qian cao gen), and Imperatae Rhizoma (bai mao gen)-all charred-for sudden onset of bleeding, as in Ten Partially-Charred Substances Powder (shi hui san).

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
none noted

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
Good quality consists of big, unfragmented, green leaves without moldy spots.

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
