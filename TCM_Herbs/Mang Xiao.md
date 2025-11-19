---
# 🔹 Core Metadata (Universal Fields)
id: "herb-20251001123706"
name: "Mang Xiao"
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
  hanzi: "芒硝"
  pinyin: "máng xiāo"
  pharmaceutical: "Natrii Sulfas"
  english: "Mirabilitum"
  alternate_names: []

  # TCM Properties
  taste: [Acrid, bitter, salty]
  temperature: "very cold"
  channels: [Stomach, Large Intestine]

  # Clinical Information
  dosage: "6-18g"
  toxicity: "None"
  functions: [Purges accumulation and guides out stagnation, Clears heat and drains fire, Clears heat and reduces swelling]
  dui_yao: []

  # Additional Information
  constituents: [Na2SO4 ·10H2O (>97%), K, Ca, Mg, Fe, Cl]
  quality: "Good quality is colorless, transparent, and crystalline."
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

Natrii Sulfas (mang xiao) acts by attracting water from the body into the intestines, thereby increasing the volume of feces. It is salty, and thus softens hardness and moistens dryness; bitter, and thus drains downward; and cold, and thus cools heat. Once it enters the Stomach and Large Intestine (yang brightness), these qualities enable it to wash away the hard, impacted stool which has combined with heat excess to cause constipation.

*Transforming the Significance of Medicinal Substances* elaborates:

The salty flavor softens areas of hardness, thus it can unblock dried clumps; its cold nature directs downward, thus it can expel fire. It primarily treats seasonal heat mania, pathogenic heat in the six yang organs, possibly with heat in the upper burner or diaphragm, or possibly with hardened stool in the lower burner. The classic states that 'Internal pernicious heat must be treated with salty coldness.' Using this as the chief herb is to overcome fire with water; it should be combined in treatment with the bitter and acrid Rhei Radix et Rhizoma (da huang).

"Overcoming fire with water" is a traditional adage that quite closely matches the modern biomedical understanding of this medicinal's effects on the body.

Cheng Wu-Ji describes its use in particular formulas:

Hardened qi requires the salty flavor to soften it; over abundant heat requires coldness to reduce it. Thus, Zhang Zhong-Jing's formulas Major Sinking Into the Chest Decoction (da xian xiong tang), Major Order the Qi Decoction (da cheng qi tang), and Regulate the Stomach Qi Decoction (tiao wei cheng qi tang) all use it to soften hardness and expel heat from excess. If the clumping is not hardened, Natrii Sulfas (mang xiao) cannot be used.

---
---

## 🔑 TCM Properties

**Taste:** `= join(this.herb_data.taste, ", ")`
**Temperature:** `= this.herb_data.temperature`
**Channels Entered:** `= join(this.herb_data.channels, ", ")`

---

## ⚡ Functions & Actions

- Purges accumulation and guides out stagnation: for heat in the Stomach and Intestines with constipation; this substance moistens dryness and softens hardness.
    - With Rhei Radix et Rhizoma (da huang) for constipation due to heat accumulation in the Stomach and Intestines, as in Major Order the Qi Decoction (da cheng qi tang).
- Clears heat and drains fire: for a wide variety of problems associated with heat in the Lungs and/or Stomach. Especially useful for accumulation such as phlegm or clumping in the Intestines.
    - With Scutellariae Radix (huang qin) and Trichosanthis Semen (gua lou ren) for phlegm-heat leading to cough.
    - With Pinelliae Rhizoma preparatum (ban xia) and Aurantii Fructus (zhi shi) for pain in both shoulders or swelling of the extremities due to phlegm-heat obstructing the collaterals.
- Clears heat and reduces swelling: for red, swollen, painful eyes; painful, swollen, ulcerated mouth or throat; and red, swollen skin lesions including breast problems. For external use. Can be used alone for the early stages of breast abscess before it has suppurated. Also helps promote lactation.
    - With Borax (peng sha) and Borneolum (bing pian) as a topical application for redness and swelling of the throat and ulcerations of the oral cavity.

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
- Contraindicated in cases of cold from deficiency of the Spleen and Stomach, and during pregnancy.
- When used externally to promote lactation, its use should cease as soon as an effect is seen, as overuse can lead to a reduction in lactation.
- If there is no pathogenic clumping in the lower burner, with no hard firmness to palpate, do not use it, for fear that it will exhaust the true yin of the lower burner.
- If an illness does not originate from pathogenic heat deeply bound, with closed clumping that is difficult to pass, definitely do not lightly use it. (Harm and Benefit in the Materia Medica)

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
Good quality is colorless, transparent, and crystalline.

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
