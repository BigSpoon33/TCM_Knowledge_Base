---
# 🔹 Core Metadata (Universal Fields)
id: "herb-20251001123706"
name: "Wang Bu Liu Xing"
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
  hanzi: "王不留行"
  pinyin: "wáng bù liú xíng"
  pharmaceutical: "Vaccariae Semen"
  english: "Cowherb Seed"
  alternate_names: []

  # TCM Properties
  taste: [Bitter]
  temperature: "Neutral"
  channels: [Liver, Stomach]

  # Clinical Information
  dosage: "4.5-9g"
  toxicity: "None"
  functions: [Promotes the movement of blood and invigorates the channels, Reduces swellings]
  dui_yao: []

  # Additional Information
  constituents: [Triterpene saponines: vacsegoside A, B, C, D (sapogenine: gypsogenin-3-B-D-glucuronoside), isosaponarin (sapogenine: saponaretin), Flavonoids: sapxanthone, 1,8-dihydroxy-3,5-dimethoxy-9H-xanthone, vaccarin, Other constituents: phospholipides, phytin, stigmasterol, proteins, fats, alkaloids, coumarins]
  quality: "Good quality consists of full, black seeds."
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

Promoting movement without restraint, Vaccariae Semen (wang bu liu xing) enters the blood aspect and excels at facilitating movement in the blood vessels, transforming stasis, and dispersing swelling and distention. Its bitterness adds a downward-draining action that is quite strong, and many of its notable clinical effects derive from this, such as unblocking menstruation, inducing labor, and promoting the flow of breast milk. It is often used in the treatment of amenorrhea or dysmenorrhea due to stagnation of qi and blood, delayed initiation of labor, and postpartum obstruction of the collaterals of the breast, causing breast distention and preventing sufficient milk flow.

Rectification of the Meaning of Materia Medica states that it unblocks and facilitates [blood flow] in a rapid accelerated (~ ji) manner, hence the name 'the king cannot stay its movement' (wang bu liu xing). This actually means that, even should the king command it to stop, its movement cannot halt: its dredging-facilitating nature is so violent. Its flavor is also bitter, so it drains and directs downward: it is only appropriate for hot clumping. ... It also treats difficult labor, and unblocks breast milk. Zhen Quan says it treats wind toxicity and unblocks the blood vessels. Ri Hua-Zi says it governs roving wind (you feng), wind rash, and irregular menstruation in women. Li Shi-Zhen says it promotes urination. Zhang Jie-Bin says that it facilitates the yang brightness channel, the Penetrating and Conception vessels, and the sea of blood, so that it unblocks menstrual stagnation and irregularity. Zhang Lu says it travels without restraint, and is best at facilitating the orifices. All of the above are the effects of breaking up clumping, disseminating, and guiding. If a person is deficient [however] it must be applied cautiously in a light dosage; it is strictly forbidden during pregnancy!

---
---

## 🔑 TCM Properties

**Taste:** `= join(this.herb_data.taste, ", ")`
**Temperature:** `= this.herb_data.temperature`
**Channels Entered:** `= join(this.herb_data.channels, ", ")`

---

## ⚡ Functions & Actions

- Promotes the movement of blood and invigorates the channels: in the upper part of the body this herb promotes lactation, and in the lower part it unblocks menstruation.
  - For insufficient lactation or amenorrhea due to blood stasis.
  - With Angelicae sinensis Radix (dang gui) and Cyperi Rhizoma (xiang fu) for blood stasis leading to menstrual irregularities or amenorrhea.
  - With Manitis Squama (chuan shan jia) for insufficient lactation and breast abscess.
  - With Liquidambaris Fructus (lu lu tong), Tetrapanacis Medulla (tong cao), and Astragali Radix (huang qi) for insufficient lactation.
  - With Astragali Radix (huang qi) and Angelicae sinensis Radix (dang gui) for insufficient lactation due to postpartum qi and blood deficiency.
- Reduces swellings: for painful swellings, especially of the breast or testicles.
  - With Taraxaci Herba (pu gong ying) and Trichosanthis Fructus (gua lou) for breast abscess.
  - With Toosendan Fructus (chuan lian zi) and Isatidis/Baphicacanthis Radix (ban lan gen) for orchitis from mumps.

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
Contraindicated during pregnancy.

"Those with blood loss disorders and those with continuous menstrual bleeding must both avoid it." (Treasury of Words on the Materia Medica)

Zhang Shan-Lei cautions: "If a person is deficient it must be used with caution in a small dosage; it is strictly forbidden during pregnancy!"

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
Good quality consists of full, black seeds.

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
