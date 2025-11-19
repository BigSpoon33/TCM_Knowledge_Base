---
# 🔹 Core Metadata (Universal Fields)
id: "herb-20251001123706"
name: "Suo Yang"
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
  hanzi: "鎖陽"
  pinyin: "suǒ yáng"
  pharmaceutical: "Cynomorii Herba"
  english: "Fleshy stem of cynomorium"
  alternate_names: []

  # TCM Properties
  taste: [Sweet, Warm]
  temperature: "Warm"
  channels: [Large Intestine, Kidney, Liver]

  # Clinical Information
  dosage: "5-15g"
  toxicity: "N/A"
  functions: [Tonifies the Kidneys, assists the yang, and augments the Liver yin and blood, Moistens the Intestines, unblocks the bowels, augments the essence and nourishes the blood]
  dui_yao: []

  # Additional Information
  constituents: [cynoterpene, acetylursolic acid, ursolic acid, triglycerides of palmitic acid, oleic acid and linoleic acid, β-sitosteryl palmitate, daucosterol, campesterol, aliphatic hydrocarbons, 15 different amino acids, aspartic acid, proline, serine, alanine, tannins]
  quality: "Good quality consists of thick, heavy, and hard stems with an oily surface on cross section."
  text_first_appeared: "Supplement to the Extension of the Materia Medica"

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

Sweet and warm, but moist in texture, Cynomorii Herba (suo yang) augments the Liver and Kidney yin but excites the yang, and has a strong ability to nourish the sinews and treat male impotence. It is often used in the treatment of atrophy of the sinews and bones causing difficulty in walking, due to Liver and Kidney deficiency, and impotence due to Kidney yang deficiency. Because it is moist, it moistens the Intestines to promote movement of stool. The Grand Materia Medica says that it "moistens dryness, nourishes the sinews, treats atrophy and weakness." Thoroughly Revised Materia Medica states that it "treats atrophy and weakness, and lubricates the Intestines."

---
---

## 🔑 TCM Properties

**Taste:** `= join(this.herb_data.taste, ", ")`
**Temperature:** `= this.herb_data.temperature`
**Channels Entered:** `= join(this.herb_data.channels, ", ")`

---

## ⚡ Functions & Actions

- Tonifies the Kidneys, assists the yang, and augments the Liver yin and blood: for Kidney yang deficiency leading to impotence, infertility, urinary frequency, and spermatorrhea. Also for atrophy disorder from Liver and Kidney deficiency.
    - With Cistanches Herba (rou cong rong) for impotence or infertility due to insufficiency of the Liver and Kidneys along with exhausted essence and blood.
    - With Tigris Os (hu gu), Achyranthis bidentatae Radix (niu xi), and Rehmanniae Radix preparata (shu di huang) for weakness, paralysis, motor impairment, and atrophy of the musculature associated with atrophy disorders from severe Liver and Kidney deficiency, as in Hidden Tiger Pill (hu qian wan).
    - With Mantidis Ootheca (sang piao xiao) for premature ejaculation, urinary incontinence, and urinary frequency from Kidney yang deficiency.
- Moistens the Intestines, unblocks the bowels, augments the essence and nourishes the blood: for constipation from qi or blood deficiency.
    - With Mori Fructus (sang shen) and honey for constipation due to yang deficiency and insufficient blood in the elderly or debilitated.
- A large dosage is needed to be effective.

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
Contraindicated in those with Kidney yin deficiency with heat signs, as well as those with diarrhea from Spleen deficiency or constipation due to heat from excess.

Traditional Contraindications:
"Contraindicated in those with loose stools, unstable essence, and overabundant fire causing constipation, excessive erections, and deficiency distention of the Heart qi." (Materia Medica of Combinations)

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
Good quality consists of thick, heavy, and hard stems with an oily surface on cross section.

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
