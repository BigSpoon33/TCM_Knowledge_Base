---
# 🔹 Core Metadata (Universal Fields)
id: "herb-20251001123706"
name: "Sang Shen Zi"
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
  hanzi: "桑椹子"
  pinyin: "Sang Shen Zi"
  pharmaceutical: "Mori Fructus"
  english: "Mulberry, morus fruit"
  alternate_names: []

  # TCM Properties
  taste: [Sweet, Cold]
  temperature: "Cold"
  channels: [Heart, Liver, Kidney]

  # Clinical Information
  dosage: "9-15g"
  toxicity: "Taking high doses of this fruit can cause hemorrhagic colitis in children, which can be terminal. Note, however, that only two cases have been reported in the literature; in one, a three-year-old boy ate three handfuls of the fruit. Allergic skin reactions have also been reported. Symptoms appeared 30 minutes after ingestion and included intense pruritus and erythema, starting at the lower extremities and spreading over the entire body, including the face."
  functions: [Tonifies the blood and enriches the yin, Moistens the Intestines]
  dui_yao: []

  # Additional Information
  constituents: [Volatile oil: cineol, geraniol, linalool, linalyl acetate, camphor, α-pinene, limonene, Phospholipides: phosphatidyl choline, lysophosphatidyl choline, phosphatidyl ethanolamine, phosphatidic acid, phosphatidyl inositol, diphosphatidyl glycerol, Organic and fatty acids: malic acid; linoleic acid, oleic acid, palmitic acid, stearic acid, caprylic acid, pelargonic acid, capric acid, myristic acid, linolenic acid, Other constituents: sugars, tannic acid, cyanidin, chrysanthemin, carotene, vitamin B1, B2]
  quality: "Good quality consists of large, unfragmented, purplish red sweet fruit with thick flesh and without foreign matter."
  text_first_appeared: "Tang Materia Medica"

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

Sweet and cold, *Mori Fructus* enters the Heart, Liver, and Kidney channels with a nature that is harmonious and gentle, tonifying the blood and yin without being cloying or upsetting the digestion. It is often used for yin and blood deficiency patterns involving dryness of the mouth and thirst, as well as headache, dizziness, and insomnia associated with Liver yin deficiency, which allows the Liver yang to ascend. This medicinal is moistening and lubricates the Intestines.

---
---

## 🔑 TCM Properties

**Taste:** `= join(this.herb_data.taste, ", ")`
**Temperature:** `= this.herb_data.temperature`
**Channels Entered:** `= join(this.herb_data.channels, ", ")`

---

## ⚡ Functions & Actions

- Tonifies the blood and enriches the yin: for dizziness, tinnitus, insomnia, and premature greying of the hair. Also suitable for wasting and thirsting disorder due to yin deficiency.
- With Spatholobi Caulis (鸡血藤 - ji xue teng): for dizziness, tinnitus, and wasting and thirsting disorder due to yin deficiency.
- With Polygoni multiflori Radix preparata (制何首乌 - zhi he shou wu), Ecliptae Herba (墨旱莲 - mo han lian), and Ligustri lucidi Fructus (女贞子 - nü zhen zi): for premature greying of the hair due to Liver and Kidney deficiency. This combination is also used for constipation in the elderly and postpartum.
- With Rehmanniae Radix (生地黄 - sheng di huang) and Dendrobii Herba (石斛 - shi hu): for dizziness, blurred vision, and insomnia due to yin and blood deficiency.
  - Add Trichosanthis Radix (天花粉 - tian hua fen) and Anemarrhenae Rhizoma (知母 - zhi mu) for more heat signs.
  - Add Panacis quinquefolii Radix (西洋参 - xi yang shen) and Astragali Radix (黄芪 - huang qi) for concurrent qi deficiency.
- With Ophiopogonis Radix (麦门冬 - mai men dong) and Trichosanthis Radix (天花粉 - tian hua fen): for symptoms such as dryness of the mouth and throat and irritability resulting from deficiency of the blood and fluids.
- Moistens the Intestines: for constipation due to blood deficiency or insufficient fluids.
- With Sesami Semen nigrum (黑芝麻 - hei zhi ma) and Cannabis Semen (火麻仁 - huo ma ren): for constipation due to yin and blood deficiency.
  - Add a small amount of Aurantii Fructus (枳壳 - zhi ke) for accompanying qi stagnation.

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
Should not be consumed by those with diarrhea due to Spleen and Stomach deficiency and weakness.

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
Good quality consists of large, unfragmented, purplish red sweet fruit with thick flesh and without foreign matter.

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
