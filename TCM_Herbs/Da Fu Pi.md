---
# 🔹 Core Metadata (Universal Fields)
id: "herb-20251001123706"
name: "Da Fu Pi"
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
  hanzi: "大腹皮"
  pinyin: "Da Fu Pi"
  pharmaceutical: "Arecae Pericarpium"
  english: "Areca Peel/Areca Husk"
  alternate_names: []

  # TCM Properties
  taste: [Acrid, Slightly warm]
  temperature: "Slightly warm"
  channels: [Large Intestine, Small Intestine, Spleen, Stomach]

  # Clinical Information
  dosage: "4.5-9g"
  toxicity: "Allergic reactions have been reported including urticaria, severe abdominal pain, and diarrhea."
  functions: [Drives qi downward and eases the middle, Promotes urination and reduces edema]
  dui_yao: []

  # Additional Information
  constituents: [Catechin, Arecoline, Pararecoline]
  quality: "Good quality consists of yellowish white, soft pieces without foreign matter."
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

Arecae Pericarpium (da fu pi), acrid and warm, enters the Large Intestine, Small Intestine, Spleen, and Stomach channels. Unblocking because of its warm nature, and dispersing because of its acrid flavor, it transforms dampness which has clumped and obstructed the flow of qi, thus restoring normal qi and fluid circulation. It eases the middle, drives qi downward, promotes fluid metabolism and flow, and reduces edema. When the fluids flow in a regular fashion, urination is natural and easy. By this means it treats abdominal distention and fullness, incomplete bowel movements, urinary difficulty, edema and leg qi due to pathogenic dampness obstructing the qi dynamic.

This herb is particularly noted for its ability to treat pathogenic influences with or without form: it can disperse formless qi stagnation, but also drain dampness and edema, which do have form. *Materia Medica of Ri Hua-Zi* notes that it "drives all qi downward, stops sudden turmoil disorder, unblocks the Large and Small Intestines, strengthens the Spleen, unbinds the Stomach, and regulates the middle." *The Grand Materia Medica* lists the following actions:

directs rebellious qi downward, reduces water qi, floating edema in the muscles and skin, accumulated rebellious leg qi, focal distention and fullness, fetal qi [disturbance], morning sickness, and stifling sensations in the chest [during pregnancy].

---
---

## 🔑 TCM Properties

**Taste:** `= join(this.herb_data.taste, ", ")`
**Temperature:** `= this.herb_data.temperature`
**Channels Entered:** `= join(this.herb_data.channels, ", ")`

---

## ⚡ Functions & Actions

- Drives qi downward and eases the middle: for patterns of dampness or other processes obstructing the middle and leading to qi stagnation with such signs as epigastric and abdominal distention, focal distention and a stifling sensation, and belching with acid regurgitation. Especially useful when these disorders are accompanied by incomplete and irregular bowel movements.
  - With Magnoliae Officinalis Cortex (hou po) and Citri Reticulatae Pericarpium (chen pi) for epigastric and abdominal distention and discomfort with difficult bowel movements associated with stagnant qi and dampness, as in Separate and Reduce Decoction (fen xiao tang).
  - With Atractylodis Macrocephalae Rhizoma (bai zhu) for loss of appetite, epigastric and abdominal distention and fullness with edema from accumulation of dampness and water secondary to Spleen qi deficiency.
- Promotes urination and reduces edema: for abdominal distention accompanied by edema, especially superficial edema, or the symptoms of food stagnation. Also used for damp leg qi.
  - With Poriae Cutis (fu ling pi) and Zingiberis Rhizomatis Cortex (sheng jiang pi) for mild edema or superficial facial edema, as in Five-Peel Decoction (wu pi yin).

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
Use with caution during pregnancy. Forbidden in those with distention due to deficiency, because it can drain true qi.

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
Good quality consists of yellowish white, soft pieces without foreign matter.

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
