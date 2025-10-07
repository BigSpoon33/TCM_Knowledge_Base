---
# 🔹 Core Metadata (Universal Fields)
id: "herb-20251001123706"
name: "Ye Jiao Teng"
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
  hanzi: "夜交藤"
  pinyin: "ye jiao teng"
  pharmaceutical: "Polygoni Multiflori Caulis"
  english: "Fleeceflower caulis"
  alternate_names: []

  # TCM Properties
  taste: [Sweet, Neutral]
  temperature: "Neutral"
  channels: [Heart, Liver]

  # Clinical Information
  dosage: "15-30g"
  toxicity: "Allergic reactions have been reported with such symptoms as skin eruptions, pruritus, tingling pain of the skin, and alternating hot and cold sensations."
  functions: [Nourishes the Heart, Calms the spirit, Unblocks the collaterals, Expels wind]
  dui_yao: []

  # Additional Information
  constituents: [Anthraglycosides: emodin, physcion, anthraglycoside B (emodin-8-O-β-D-glucopyranoside), Other constituents: polygoacetophenoside (2,3,4,6-tetrahydroxyacetophenone-3-O-β-D-glucopyranoside), luteolin-5-O-xyloside, β-sitosterol]
  quality: "Good quality consists of thick and uniform stems with a purplish brown outer bark."
  text_first_appeared: "Grand Materia Medica"

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

Sweet and neutral, Polygoni multiflori Caulis (ye jiao teng) enters the blood level of the Heart and Liver channels. The Heart governs the blood and stores the spirit, and the Liver stores the blood and governs wind. Hence this herb nourishes the blood and calms the spirit, while expelling wind and unblocking the collaterals to stop itching. It is used whenever blood deficiency leads to insomnia, restlessness, palpitations, and disturbing dreams; or aching soreness of the limbs; or itching skin disorders when blood deficiency has allowed encroachment of pathogenic wind.

Its now common use for calming the spirit is a rather late historical development. In the Grand Materia Medica, Li Shi-Zhen has only: "Wind sores and itching scabies decoct and use as a wash." Later, Ye Gui, in his nineteenth century work Renewed Materia Medica, says: "Tonifies the middle qi, promotes movement in the channels and collaterals, unblocks the blood vessels, quiets the spirit, and expedites sleep."

Rectification of the Meaning of Materia Medica notes that Li Shi-Zhen only mentions the use of the vine and leaves for the treatment of wind [patterns] causing sores, and scabies, and that it is particularly effective when the decoction is used as a wash. The present use, to treat lack of good sleep at night, relies on its ability to guide the yang into yin.

The phrase 'guide the yang into yin' refers to the ability of Polygoni multiflori Caulis (ye jiao teng) to nourish the blood, and thereby provide a balance to excessive yang activity.

Zhang Shan-Lei, the author of this text, goes on to say that the root enters deeply into the earth, the vine grows and extends over a great distance in great profusion, during the night it intertwines, and encompasses the qi of the utmost yin. It also has the power to congeal and secure, and thus enters the Liver and Kidneys, tonifying and nourishing the true yin.

While the latter part of this statement refers to the rhizome Polygoni multiflori Radix (he shou wu), the vine Polygoni multiflori Caulis (ye jiao teng) shares certain aspects of this tonification. New Reference of Prepared Medicines indicates that Polygoni multiflori Caulis (ye jiao teng) "nourishes the Liver and Kidneys, stops deficient sweating, quiets the spirit, and expedites sleep." When used to calm the spirit sufficient dosage is required: 15-30g.

---
---

## 🔑 TCM Properties

**Taste:** `= join(this.herb_data.taste, ", ")`
**Temperature:** `= this.herb_data.temperature`
**Channels Entered:** `= join(this.herb_data.channels, ", ")`

---

## ⚡ Functions & Actions

- Nourishes the Heart and blood and calms the spirit: for patterns of yin or blood deficiency with insomnia and irritability. Especially useful for dream-disturbed sleep.
  - With Albiziae Cortex (he huan pi), Ziziphi spinosae Semen (suan zao ren), and Platycladi Semen (bai zi ren) for insomnia due to Heart blood deficiency. Especially appropriate for patients who have many nightmares.
  - With Poriae Sclerotium Pararadicis (fu shen) to calm the spirit, as in Gastrodia and Uncaria Decoction (tian ma gou teng yin).
- Nourishes the blood and unblocks the channels: for generalized weakness, soreness, pain, and numbness due to blood deficiency. Used as an auxiliary herb for painful obstruction.
  - With Angelicae sinensis Radix (dang gui), Spatholobi Caulis (ji xue teng), and Salviae miltiorrhizae Radix (dan shen) for generalized muscular weakness, soreness, and numbness due to blood deficiency.
  - With Notopterygii Rhizoma seu Radix (qiang huo), Taxilli Herba (sang ji sheng), and Gentianae macrophyllae Radix (qin jiao) for wind-damp painful obstruction.
- Alleviates itching: used as an external wash for itching and skin rashes.
  - With Cicadae Periostracum (chan tui), Spirodelae Herba (fu ping), and Kochiae Fructus (di fu zi) as an external wash for wind-related itching.

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
None noted. See Toxicity below.

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
Good quality consists of thick and uniform stems with a purplish brown outer bark.

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
