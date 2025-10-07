---
# 🔹 Core Metadata (Universal Fields)
id: "herb-20251001123706"
name: "Bai Wei"
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
  hanzi: "白薇"
  pinyin: "Bai Wei"
  pharmaceutical: "Cynanchi Atrati Radix"
  english: "None"
  alternate_names: []

  # TCM Properties
  taste: [Bitter, Salty]
  temperature: "Cold"
  channels: [Lung, Stomach, Kidney]

  # Clinical Information
  dosage: "3-12g"
  toxicity: "This herb has relatively strong cardiotonic properties, and an overdose (30-45g) can provoke toxic reactions. Symptoms include palpitations, nausea, vomiting, dizziness, headache, diarrhea, and salivation."
  functions: [Clears heat and cools the blood, Cools the blood and promotes urination, Resolves toxicity and treats sores]
  dui_yao: []

  # Additional Information
  constituents: [cynanchol, volatile oil, cynatratoside A, cynatratoside B, cynatratoside C, cynatratoside D, cynatratoside E, cynatratoside F, glaucoside C, glaucoside H, glaucogenin A, atratoside A, atratoside B, atratoside C, atratoside D, cynanversicoside A, cynanversicoside B, cynanversicoside C, cynanversicoside D, cynanversicoside E, neocynanversicoside, glaucogenin D]
  quality: "Good quality consists of thick (1cm) and long roots with a compact center and a yellowish brown surface."
  text_first_appeared: "The Divine Husbandman's Classic of the Materia Medica"

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

Cynanchi Atrati Radix (Bai Wei) enters the Lung, Stomach, and Kidney channels. It is bitter, but not drying, so it directs it downward; it is salty, and can thus enter the blood, and also cold, enabling it to clear heat. These actions are performed without injuring the yin or blood. And because blood-level heat is cleared, the yin and blood are protected by this herb, which is equivalent to replenishing these substances. It cools both the heat of yin deficiency as well as that due to pathogenic excess, venting the pathogenic influence toward the surface where it is released. This is useful in such cases as prolonged low-grade fever due to a residual pathogenic influence in the later stages of a febrile disorder: heat in the blood is cooled directly and also by venting.

This herb cools the Lungs and facilitates the passage of urine, enabling it to treat painful urinary dribbling in which the urine is scanty and burning. Its functions in treating urinary disorders and sores are of secondary importance, however. Heat from deficiency following childbirth, painful urinary dribbling with blood in the urine, early periods due to heat in the blood-all of these conditions are appropriately treated with this herb. It also can be used for cough due to Lung heat, especially if associated with a low-grade fever.

Rectification of the Meaning of Materia Medica elaborates on the nature of this herb:

The Divine Husbandman's Classic of the Materia Medica states that the nature of Cynanchi Atrati Radix (Bai Wei) is neutral, but because it primarily treats warm and febrile pathogens, this 'neutral' should be 'cold'. Records of Famous Physicians does in fact call it 'greatly cold' - this should be its basic nature .... All bitter-cold herbs tend to be drying, except Cynanchi Atrati Radix (Bai Wei). Although cold, it does not harm the yin fluids, essence, or blood. Thus, its main indications all relate to heat at the blood level rather than to any damp-heat disorder. It can be regarded as possessing a mild, inherent yin enriching quality within its main heat-clearing actions. This is why ancient formulas used it so often for women.

---
---

## 🔑 TCM Properties

**Taste:** `= join(this.herb_data.taste, ", ")`
**Temperature:** `= this.herb_data.temperature`
**Channels Entered:** `= join(this.herb_data.channels, ", ")`

---

## ⚡ Functions & Actions

- Clears heat and cools the blood: for heat entering the nutritive or blood levels, yin-deficient fever, persistent summertime fever in children, postpartum fever, and lingering fever as the sequela of a warm-heat pathogen disease that injures the blood or yin. Most commonly used for postpartum fever and during the recovery stage from a febrile disease.

- With Lycii Cortex (Di Gu Pi) for steaming bone disorder due to blood deficiency with intermittent fever and chills, or afternoon fevers due to heat in the nutritive level.

- With Angelicae Sinensis Radix (Dang Gui) and Ginseng Radix (Ren Shen) for remnants of heat that cannot be eliminated, unremitting chronic fever, or postpartum fever and irritability due to blood deficiency.

- With Menthae Haplocalycis Herba (Bo He) and Polygonati Odorati Rhizoma (Yu Zhu) for externally-contracted wind-heat in one with underlying yin deficiency, as in Modified Solomon's Seal Decoction (Jia Jian Wei Rui Tang).

- With Peucedani Radix (Qian Hu) and Eriobotryae Folium (Pi Pa Ye) for cough from Lung heat.

- Cools the blood and promotes urination: for hot or painful bloody urinary dribbling, especially before or after giving birth.

- With Lophatheri Herba (Dan Zhu Ye) and Akebiae Caulis (Mu Tong) for urinary dysfunction due to yin deficiency and heat in the blood.

- With Paeoniae Radix Alba (Bai Shao), most commonly prepared in wine, for hot painful urinary dribbling or painful bloody urinary dribbling during pregnancy or postpartum.

- Resolves toxicity and treats sores: for toxic sores, swollen and painful throat, and snakebite. For these purposes, it can be taken internally or applied topically. This action is not particularly strong.

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
In Chen Shi-Duo's New Compilation of Materia Medica, cautions: "This is an important assistant or envoy herb, but is not suitable for chief or deputy status .... The dose should not exceed two Qian [6 g] to avoid injuring the Stomach with its intense cold." Dry-fried cynanchi can be used for patients with a weak Spleen and Stomach.

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
Good quality consists of thick (1cm) and long roots with a compact center and a yellowish brown surface.

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
