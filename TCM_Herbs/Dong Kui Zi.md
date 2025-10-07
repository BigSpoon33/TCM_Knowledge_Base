---
# 🔹 Core Metadata (Universal Fields)
id: "herb-20251001123706"
name: "Long Kui / Solani nigri Herba"
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
  hanzi: "龍葵"
  pinyin: "lóng kuí"
  pharmaceutical: "Solani nigri Herba"
  english: "Black Nightshade Herb"
  alternate_names: []

  # TCM Properties
  taste: [Bitter, slightly sweet]
  temperature: "Cold"
  channels: [Lung, Stomach, Bladder]

  # Clinical Information
  dosage: "15-30g"
  toxicity: "No side effects have been reported in patients taking a normal dosage of the crude preparation orally. Overdosage (45-60g), however, can cause problems that will occur anywhere from ten minutes to several hours after ingestion. These include itching throat, hot and burning sensation, epigastric pain, nausea, vomiting, diarrhea, dehydration, and electrolyte imbalance. In severe cases, shock, hypotension, dilated pupils, restlessness, delirium, spasms, dyspnea, and even respiratory and circulatory failure can occur."
  functions: [Clears heat, Resolves toxicity, Invigorates the blood, Reduces swellings, Promotes urination, Unblocks painful urinary dribbling, disperses clumps, facilitates urination, expels phlegm, stops cough, alleviates itching]
  dui_yao: []

  # Additional Information
  constituents: [Steroidal alkaloids: solasodamine, solasonine, solamargine, α-solanigrine, β-solanigrine, solavilline, solanigridine]
  quality: "Good quality consists of green, tender stems and leaves. The best quality has fruit."
  text_first_appeared: "Reference on Medicinal Properties"

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

Bitter, cold, and slightly toxic, Solani nigri Herba (long kui) enters the Lung, Stomach, and Bladder channels. It clears heat, resolves toxicity, invigorates the blood, disperses clumps, facilitates urination, reduces swelling, expels phlegm, stops cough, and alleviates itching. Traditionally, it was used primarily for toxic swellings, sores, carbuncles and furuncles; modern usage has extended its application to the treatment of many types of cancer, bronchitis, and urinary tract infections.

The external use of the leaves of Solani nigri Herba (long kui) for pemphigus and other toxic swellings was noted in the twelfth-century work Comprehensive Record of Sage-Like Benefit, which says that the young sprouting leaves should be crushed and applied externally to the blisters.

Encountering the Sources of the Classic of Materia Medica says that this herb is bitter, slightly sweet, slippery and cold, and non-toxic. When it is said that Solani nigri Herba (long kui) is slippery like other large-leaf plants [such as sunflower, hollyhock, or mallow], this is in reference to its sprouting leaves, which reduce heat and disperse blood; they suppress the toxicity of cinnabar-like minerals, and expel corrupted blood in women. The common name 'old duck eyes' refers to its fruit, which has an excellent ability to restore the sinews and reduce deep-rooted swellings [resolving toxicity] similar to the sprouted leaves. The root facilitates urination, particularly when decocted with Akebiae Caulis (mu tong). It should be noted that the unripe fruit is quite toxic.

Rectification of the Meaning of Materia Medica elaborates:

The nature of this herb is cold, cooling, slippery and facilitating, and is thus termed 'mallow' (kui). The stem is soft and tender, like a vine, but not a vine, spreading and extending widely, and is thus termed 'dragon,' referring to its endless meandering. ... The Tang Materia Medica says that [it] expels heat and reduces swelling; the Illustrated Classic of the Materia Medica says that it treats gynecological bad blood; Li Shi-Zhen states that it reduces heat and disperses blood, suppressing the ill effects of mineral and metal toxins, treating toxic swollen sores, and injury from trauma; and the Materia Medica of Diet Therapy notes that it can be crushed and applied to deep-rooted sores, swellings, and rashes. Thus, it can be taken internally, applied externally, used for clearing heat, unblocking and facilitating [urination], and therefore can also treat external injuries and bruising; but its special forte is reducing heat and swellings in external medicine.

---
---

## 🔑 TCM Properties

**Taste:** `= join(this.herb_data.taste, ", ")`
**Temperature:** `= this.herb_data.temperature`
**Channels Entered:** `= join(this.herb_data.channels, ", ")`

---

## ⚡ Functions & Actions

Clears heat, resolves toxicity, invigorates the blood, and reduces swellings: for sores and abscesses, pruritic sores and rashes, swollen and painful throat, and cancer.
    - With Isatidis Folium (da qing ye) and Belamcandae Rhizoma (she gan) for acute swollen and painful throat.
    - With Taraxaci Herba (pu gong ying) and Chrysanthemi indici Flos (ye ju hua) for abscesses. Can be taken internally and applied topically.
    - With Schizonepetae Herba (jing jie) and Cicadae Periostracum (chan tui) for pruritic sores and rashes.
    - With Scutellariae barbatae Herba (ban zhi lian) for a variety of cancers.
- Promotes urination and unblocks painful urinary dribbling: for hot painful urinary dribbling or edema with urinary dysfunction.
    - With Plantaginis Semen (che qian zi), Alismatis Rhizoma (ze xie), and Pyrrosiae Folium (shi wei) for hot painful urinary dribbling or edema with urinary dysfunction.

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
Contraindicated during pregnancy. See Toxicity below.

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
Good quality consists of green, tender stems and leaves. The best quality has fruit.

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
