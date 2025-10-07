---
# 🔹 Core Metadata (Universal Fields)
id: "herb-20251001123706"
name: "Winter Melon Seed / Dong Gua Zi"
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
  hanzi: "冬瓜子"
  pinyin: "dōng guā zǐ"
  pharmaceutical: "Benincasae Semen"
  english: "winter melon seed, wax gourd seed, benincasa"
  alternate_names: []

  # TCM Properties
  taste: [sweet, cold]
  temperature: "cold"
  channels: [Lung, Stomach, Large Intestine, Small Intestine]

  # Clinical Information
  dosage: "9-15g"
  toxicity: "None noted."
  functions: [Clears heat, Expels phlegm, Promotes the discharge of pus, Drains dampness]
  dui_yao: []

  # Additional Information
  constituents: [Saponins, urea, urease, citrulline, fats]
  quality: "Good quality consists of full, yellowish white seeds."
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

Sweet and cold, Benincasae Semen (冬瓜子 dōng guā zǐ) enters the Lung, Stomach, Large Intestine, and Small Intestine channels. Cold and slippery by nature, it cools Lung heat accumulating in the upper burner, while guiding out accumulated filth from the Large Intestine below. It also loosens phlegm and promotes the discharge of pus, and so can be used for Lung heat with thick yellow phlegm, and for damp-heat in the upper or lower burner, as in Lung or Intestinal abscess, or vaginal discharge.

Essentials of the Materia Medica observes that the herb also tonifies the Liver and benefits the vision, while the Divine Husbandman's Classic of the Materia Medica notes that the seeds make the skin glossy and moist, and improve the complexion; for this purpose, they can be taken internally or applied as a paste.

Li Shi-Zhen has an interesting observation regarding the flesh of the winter melon, the matrix from which the seeds are extracted:

The fruit's flesh is best taken by those who are hot; if taken by those who are cold, it will make them thin. Taken boiled, it blanches the five yin organs, as it drives qi downward. Those desiring a thin, light, healthy body should take it over the long term; if you need to put on weight, do not take it.

---
---

## 🔑 TCM Properties

**Taste:** `= join(this.herb_data.taste, ", ")`
**Temperature:** `= this.herb_data.temperature`
**Channels Entered:** `= join(this.herb_data.channels, ", ")`

---

## ⚡ Functions & Actions

- Clears heat, expels phlegm, and promotes the discharge of pus: for heat that has collected in the Lungs or Intestines, as in Lung heat, with expectoration of thick, yellow sputum. Also for damp-heat with phlegm obstruction in the upper or lower burner, as in Lung or Intestinal abscess.
  - With Platycodi Radix (桔梗 jie geng), Houttuyniae Herba (蕺菜 yú xing cao), and Lonicerae Flos (金银花 jin yin hua) for Lung abscess caused by hot phlegm.
  - With Coicis Semen (薏苡仁 yì yì rén) and Phragmitis Rhizoma (芦根 lú gēn) for Lung abscess due to heat toxin obstructing the Lungs, as in Reed Decoction (wei jing tang).
  - With Rhei Radix et Rhizoma (大黄 da huang) and Moutan Cortex (牡丹皮 mǔ dān pí) for Intestinal abscess as in Rhubarb and Moutan Decoction (da huang mu dan tang).
- Clears heat and drains dampness: especially useful in the treatment of damp-heat vaginal discharge.
  - With Phellodendri Cortex (黄柏 huáng bǎi) and Dioscoreae hypoglaucae Rhizoma (萆薢 bì xiè) for damp-heat vaginal discharge.

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
Zhu Dan-Xi observes:

Winter melon has a nature which urgently mobilizes. When Miscellaneous Records of Famous Physicians [sixth-century text] says that it separates and disperses toxic qi, this is utilizing its urgent, mobilizing nature. It should not be taken by those with chronic illness or yin deficiency.

In Essentials of the Materia Medica, however, Wang Ang disagrees:

Winter melon is something consumed almost daily as a food, and of all the melons, it particularly feels beneficial to people. Furthermore, its flavor is sweet and not acrid; how can its nature be seen as urgently mobilizing?!

In Seeking Accuracy in the Materia Medica, Huang Gong Xiu weighs in on the argument:

Since Wang Ang had previously stated that it alleviates thirst and reduces swelling, and then says that its nature is not mobilizing and its consumption is greatly beneficial-is he not contradicting himself?

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
Good quality consists of full, yellowish white seeds.

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
