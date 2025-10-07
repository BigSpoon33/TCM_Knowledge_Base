---
# 🔹 Core Metadata (Universal Fields)
id: "herb-20251001123706"
name: "Zhu Ling"
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
  hanzi: "猪苓"
  pinyin: "Zhū Líng"
  pharmaceutical: "Polyporus"
  english: "Polyporus"
  alternate_names: []

  # TCM Properties
  taste: [Sweet, bland]
  temperature: "Slightly cool"
  channels: [Kidney, Bladder]

  # Clinical Information
  dosage: "6-12g"
  toxicity: "None"
  functions: [Promotes urination and leaches out dampness]
  dui_yao: []

  # Additional Information
  constituents: [steroid compounds: polyporussterone A, B, C, D, E, F, G, ergosta-4,6,8(14),22-tetraen-3-one, 25-deoxymakisterone A, 25-deoxy-24(28)-dehydromakisterone A, ergosta-7,22-dien-3-one, ergosta-7,22-dien-3-ol, ergosta-5,7,22-trien-3-ol, 5α,8α-epidioxyergosta-6,22-dien-3-ol, triterpenes: pachymic acid, pachymic acid methyl ester, 7,9(11)-dehydropachymic acid, 7,9(11)-dehydropachymic acid methyl ester, tumulosic acid, tumulosic acid methylester, 3β-hydroxyalanosta-7,9(11),24-trien-21-oic acid, 3β,16α-dihydroxalanosta-7,9(11),24(31)-trien-21-oic acid methylester, 3β-hydroxy-16α-acetoxyalanosta-7,9(11),24-trien-21-oic acid, polyporenic acid C methyl ester, eburicoic acid, dehydroeburicoic acid, trametenolic acid, poricoic acid A, B, C, D, DM, AM, polysaccharides: β-pachyman, pachymaran, pachymose, glucan H, polysaccharides Gu-1, Gu-2, Gu-3, Gu-4, Ap-1, Ap-2, Ap-3, Ap-4, Ap-5, Ap-6, Ap-7, Ap-8, Ap-9, Ap-10, organic acids: caprylic acid, lauric acid, palmitic acid, undecanoic acid, dodecenoic acid, other constituents: α-hydroxytetracosanoic acid, biotin, proteins, fats, choline, adenine, histidine, ergosterol]
  quality: "Good quality consists of heavy and solid pieces. Its surface should be black, smooth, and with few wrinkles. Its cross section should be white, without a black or hollow center."
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

Sweet, bland, and neutral, Polyporus (zhu ling) enters the Kidney and Bladder. It opens the interstices, facilitates the function of the lower orifices, leaches out dampness, and strongly promotes urination. It is used in the treatment of turbid painful urinary dribbling, anuria, and the distention and fullness of edema, damp-heat jaundice, leg qi edema, and chronic diarrhea. According to Transforming the Significance of Medicinal Substances, Polyporus (zhu ling) is bland in flavor: blandness primarily leaches. It enters the Spleen to unblock the water pathways and is the single fastest treatment for watery diarrhea and damp diarrhea, unblocking painful urinary dribbling and expelling dampness, reducing edema, and treating jaundice.

The Grand Materia Medica notes that it "is bland and leaching; its qi raises but also directs downward; thus, it can open the interstices and pores while facilitating urination."

In Hidden Aspects of Materia Medica, Chen Jia-Mo elaborates: When using it, the black cutis must be removed; it enters the Bladder and Kidney channels to unblock painful urinary dribbling, reduces edematous fullness, expels dampness, and facilitates urination. This is because its bitterness [sic] drains stagnation, while its blandness facilitates the orifices.

---
---

## 🔑 TCM Properties

**Taste:** `= join(this.herb_data.taste, ", ")`
**Temperature:** `= this.herb_data.temperature`
**Channels Entered:** `= join(this.herb_data.channels, ", ")`

---

## ⚡ Functions & Actions

- Promotes urination and leaches out dampness: for problems caused by stagnation of dampness such as edema, scanty urine, vaginal discharge, turbid painful urinary dribbling, as well as jaundice and diarrhea.
- Can be used alone for painful urinary dribbling during pregnancy.
- With Poria (fu ling) for diarrhea, edema, scanty urine, and painful urinary dribbling.
- With Arecae Pericarpium (da fu pi) for edema, abdominal distention, and urinary difficulty.
- With Akebiae Caulis (mu tong) and Talcum (hua shi) for painful urinary dribbling, bloody urine, and abdominal distention, usually with heat signs, as in Polyporus Decoction (zhu ling tang).

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
Do not use in the absence of dampness.

The Grand Materia Medica quotes from Kou Zong-Shi's Extension of the Materia Medica, which notes that this herb "powerfully mobilizes water; long-term use will certainly injure the Kidney qi and blur the eyes. Those consuming it over an extended period should be particularly cautious." It then proceeds to quote Zhang Yuan-Su, who also warned that this medicinal is "bland and leaching, very drying and exhausts the body fluids; it should not be taken by those without damp disorders."

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
Good quality consists of heavy and solid pieces. Its surface should be black, smooth, and with few wrinkles. Its cross section should be white, without a black or hollow center.

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
