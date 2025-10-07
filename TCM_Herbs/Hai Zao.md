---
# 🔹 Core Metadata (Universal Fields)
id: "herb-20251001123706"
name: "Hai Zao / Sargassum"
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
  hanzi: "海藻"
  pinyin: "Hai Zao"
  pharmaceutical: "Sargassum"
  english: "Sargassum, seaweed"
  alternate_names: []

  # TCM Properties
  taste: [Bitter, Salty, Cold]
  temperature: "Cold"
  channels: [Kidney, Liver, Lung, Stomach]

  # Clinical Information
  dosage: "6-15g"
  toxicity: "None noted"
  functions: [Reduces phlegm and softens areas of hardness, Promotes urination and reduces edema]
  dui_yao: []

  # Additional Information
  constituents: [*Sargassum fusiforme*: alginic acid, mannitol, proteins, J, K, polysaccharides, laminarin, *Sargassum pallidum*: alginic acid, mannitol, proteins, J, K, polysaccharides, sargassan, cephalin]
  quality: "Good quality consists of clean, thick, and regular formed thallus, without foreign matter."
  text_first_appeared: "Divine Husbandman's Classic of the Materia Medica"

  # Source References
  bensky_pdf: "627"
  bensky_page: "400"

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

In the ancient work Divine Husbandman's Classic of the Materia Medica, Sargassum (hai zao) is said to govern goiter, clumped qi, disperse hard painful nodules on the lower neck, swollen sores, mobile and fixed abdominal masses and areas of hardened qi, thundering sounds in the upper, middle, and lower abdomen, and all types of edema. It is still used for all these problems, except for "thundering sounds."

Sargassum (hai zao) is a salty, bitter, cold, moistening herb that enters the Liver channel. Its major functions are reducing phlegm, softening areas of hardness, and mobilizing fluid metabolism. It is especially indicated for goiter and nodules of phlegm, both of which are frequently caused by Liver and Gallbladder fire drying and thickening the fluids until they form phlegm and obstruct the collaterals. Sargassum (hai zao) is both cooling and softening in nature, and thus addresses both the fire and the dry, hardened phlegm clumps.

Because it is cooling and clears the accumulation of fluids, it can also treat damp-heat, and is often used for swelling and pain of the testicles (a form of bulging disorder) or leg qi with fluid retention. As noted in Encountering the Sources of the Classic of Materia Medica, "The pathogen is expelled through the urine."

---
---

## 🔑 TCM Properties

**Taste:** `= join(this.herb_data.taste, ", ")`
**Temperature:** `= this.herb_data.temperature`
**Channels Entered:** `= join(this.herb_data.channels, ", ")`

---

## ⚡ Functions & Actions

- **Reduces phlegm and softens areas of hardness:** for neck nodules such as goiter and scrofula. Also used for bulging disorders, especially those involving the scrotum and testicles.
    - With *Eckloniae Thallus* (kun bu), *Fritillariae thunbergii Bulbus* (zhe bei mu), and *Citri reticulatae Pericarpium* (chen pi) for goiter, as in Sargassum Decoction for the Jade Flask (hai zao yu hu tang).
    - With *Prunellae Spica* (xia ku cao), *Forsythiae Fructus* (lian qiao), and *Scrophulariae Radix* (xuan shen) for scrofula.
- **Promotes urination and reduces edema:** an adjunctive herb for edema due to leg qi or floating edema.
    - With *Polyporus* (zhu ling), *Alismatis Rhizoma* (ze xie), and *Plantaginis Semen* (che qian zi) for edema with urinary difficulty.

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
None noted

Thoroughly Revised Materia Medica notes that "patients with Spleen cold and dampness should not take it." And Seeking Accuracy in the Materia Medica observes:

If the disorder is not due to excess pathogenic clumping, it is definitely contraindicated ... furthermore, [because] it drives qi downward very rapidly, long-term consumption makes people thin. As to those island peoples who eat it frequently [without ill effect], this is because their environment differs.

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
Good quality consists of clean, thick, and regular formed thallus, without foreign matter.

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
