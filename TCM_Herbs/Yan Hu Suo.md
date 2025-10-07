---
# 🔹 Core Metadata (Universal Fields)
id: "herb-20251001123706"
name: "Yan Hu Suo"
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
  hanzi: "延胡索"
  pinyin: "yan hu suo"
  pharmaceutical: "Corydalis Rhizoma"
  english: "Corydalis rhizome"
  alternate_names: []

  # TCM Properties
  taste: [Acrid, bitter, warm]
  temperature: "warm"
  channels: [Heart, Liver, Stomach]

  # Clinical Information
  dosage: "3-9g"
  toxicity: "Within the normal dosage range no side effects are to be expected. In high doses (10-15g of the powdered substance), some patients develop drowsiness, dizziness, and abdominal distention. The toxic dose is between 60-120g, with symptoms of poisoning appearing 1-4 hours after ingestion. They include dizziness, facial pallor, drowsiness, weakness, dyspnea, spasms, low blood pressure, weak pulse, in severe cases shock, tetanic convulsion, and respiratory inhibition. Allergic reactions have also been reported, including drug fever, erythema, and pruritus, accompanied by nausea, dizziness, shortness of breath, and numbness of the lips and extremities."
  functions: [Invigorates the blood, promotes the movement of qi, alleviates pain]
  dui_yao: []

  # Additional Information
  constituents: [(-)-tetrahydrocolumbamine, (-)-tetrahydroberberine, (-)-tetrahydrocoptisine, (+)-corybulbine, dehydrocorydaline, dl-tetrahydropalmatine, palmatine, d-corydaline, protopine, dehydroglaucine, α-allocryptopine, N-methyllaurotetanine, yuanhunine, leonticine, dihydrosanguinarine, dehydronantenine, bicuculline, corydalmine, cryptopine, berberine, coptisine, mucilage, volatile oil]
  quality: "Good quality consists of large, full, hard, and brittle pieces with a light yellow, horny, wax-like, and glossy cross section. Small rhizomes with a loose texture and greyish yellow cross section are of inferior quality."
  text_first_appeared: "Omissions from the Materia Medica"

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

Due to its warmth and aroma, Corydalis Rhizoma (yan hu suo) disseminates the flow of qi, and because it is heavy and firm in texture, it sinks into the blood level of the Heart and Liver where its bitterness drains stasis and its acridity disperses stagnation. Its yellow color also signals an affinity to the Stomach. Its particular strength lies in its strong pain-relieving action.

In Convenient Reader of Materia Medica, Zhang Bing Cheng states that it:

"promotes the movement of qi within the blood; its quality is warm and aromatic so that it makes the qi flow smoothly to adjust the blood; its flavor is also acrid and bitter. It enters the Stomach to track down and eliminate stasis and cold pain; thrusting out to the Liver, it unblocks to treat women's menstruation."

Zhang goes on to say that because it is firm in texture, acrid, bitter, yellow, warm and aromatic, it is a herb of the Liver blood level, and can be used for any pain due to obstruction of the qi and blood. He warns, however, that "If the illness is not due to blocked obstruction of qi and blood, but involves deficiency, it is not appropriate."

Materia Medica of the Kaibao Era notes that it:

"breaks up blood stasis, and treats women's irregular menstruation, masses within the abdomen, continuous uterine bleeding, and all blood disorders in the postpartum stage [including] fainting due to blood stasis, sudden up-rushing of blood, or bleeding due to injury."

The Grand Materia Medica states that it:

"invigorates the blood, promotes the movement of qi, stops pain ... it promotes movement of qi stagnation within the blood, or blood stasis due to qi stagnation, and thus treats disorders throughout the body, whether in the upper body or the lower."

---
---

## 🔑 TCM Properties

**Taste:** `= join(this.herb_data.taste, ", ")`
**Temperature:** `= this.herb_data.temperature`
**Channels Entered:** `= join(this.herb_data.channels, ", ")`

---

## ⚡ Functions & Actions

- Invigorates the blood, promotes the movement of qi, and alleviates pain: for pain of almost any kind affecting the chest, abdomen, or limbs, including that due to blood stasis and trauma. Especially useful for epigastric pain and dysmenorrhea.
    - With Trogopterori Faeces (wu ling zhi) for pain in the chest and abdomen due to blood stasis.
    - With Cyperi Rhizoma (xiang fu) and Angelicae sinensis Radix (dang gui) for dysmenorrhea from stagnant qi and blood stasis.
    - With Curcumae Radix (yu jin) and Trichosanthis Fructus (gua lou) for chest and hypochondriacal pain from qi constraint and blood stagnation.
    - With Chuanxiong Rhizoma (chuan xiong) for blood stasis-induced body aches and headache.
    - With Foeniculi Fructus (xiao hui xiang) and Linderae Radix (wu yao) for abdominal pain and bulging disorders (疝 qi) from obstruction of the qi and blood due to cold.
    - With Cinnamomi Ramulus (gui zhi) and Angelicae sinensis Radix (dang gui) for dysmenorrhea due to cold in the blood or generalized pain that is more intense in the extremities from wind-cold entering the collaterals.
    - With Toosendan Fructus (chuan lian zi) for pain in the flank and upper right quadrant, as in Melia Toosendan Powder (jin ling zi san).
    - With Lonicerae Flos (jin yin hua) and Aucklandiae Radix (mu xiang) for abdominal pain from intestinal abscess.
    - With Olibanum (ru xiang) and Myrrha (mo yao) for pain due to trauma.
    - With Salviae miltiorrhizae Radix (dan shen), Carthami Flos (hong hua), and Chuanxiong Rhizoma (chuan xiong) for coronary artery disease.
    - With Salviae miltiorrhizae Radix (dan shen), Polygonati odorati Rhizoma (yu zhu), and Crataegi Fructus (shan zha) for irregular heartbeat.

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
Inappropriate during pregnancy unless warranted by exceptional circumstances.
"Acrid, warm, mobilizes without conserving; should be avoided in all cases of early menstruation, deficiency with continuous menstrual bleeding, and postpartum deficiency." (Harm and Benefit in the Materia Medica)

"Postpartum blood deficiency, or scanty dry menstrual blood that does not flow well, pain due to qi deficiency: in all of these it is very inappropriate." (Rectification of the Meaning of Materia Medica)

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
Good quality consists of large, full, hard, and brittle pieces with a light yellow, horny, wax-like, and glossy cross section. Small rhizomes with a loose texture and greyish yellow cross section are of inferior quality.

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
