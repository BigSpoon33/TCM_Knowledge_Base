---
# 🔹 Core Metadata (Universal Fields)
id: "herb-20251001123706"
name: "Xian Mao"
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
  hanzi: "仙茅"
  pinyin: "xiān máo"
  pharmaceutical: "Curculiginis Rhizoma"
  english: "Curculigo, golden eye-grass rhizome"
  alternate_names: []

  # TCM Properties
  taste: [Acrid, hot, toxic]
  temperature: "hot"
  channels: [Kidney]

  # Clinical Information
  dosage: "3-9g"
  toxicity: "Administration of high doses can cause such side effects as cold sweating, numbness of the limbs, swollen tongue, agitation, and loss of consciousness. For this reason, overdosage must be strictly avoided, and a daily dose of 12g (in a decoction) should in no case be exceeded."
  functions: [Tonifies the Kidneys and fortifies the yang, Expels cold and eliminates dampness]
  dui_yao: []

  # Additional Information
  constituents: [cuculigosaponin A-M, curculigenin A, B, C, curculigol, yuccagenin, 31-methyl-3-oxoursen-28-oic acid, cycloartenol, β-sitosterol, stigmasterol, curculigoside, orcinol glucoside, curculigine A, lycorine, N-acetyl-N-hydroxy-2-carbamic acid methylester, N,N,N',N'-tetramethyl succinamide, hentriacontanol, 23-hydroxytriacontan-6-one]
  quality: "Good quality consists of dry, thick and long, solid roots with a greyish black surface."
  text_first_appeared: "Materia Medica from the [Southern] Seaboard Area"

  # Source References
  bensky_pdf: "627"
  bensky_page: "777"

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

*Xian Mao* (Curculiginis Rhizoma) has a harsh nature that strongly tonifies the Kidney yang, stimulates the fire at the gate of vitality, and expels cold-dampness to warm the lower back and knees. It is slightly toxic, and should only be used for short periods until the desired effect is achieved. Because it warms the Kidney yang, it indirectly warms the Spleen yang and assists digestion. The Materia Medica of the Kaibao Era says that it

governs cold *qi* in the epigastrium and abdomen with inability to eat, wind-cold causing cramps and spasms in the lower back and knees making one unable to walk, damp consumption in men, incontinence in the elderly, and assists sexual function in males.

Encountering the Sources of the Classic of Materia Medica adds that it

is hot in nature, and is an herb to tonify the Triple Burner and gate of vitality. It is only appropriate for those with impotence, cold essence, atrophy and weakness of the lower base, incontinence in the elderly, infertility, and males with deficient natural endowment.

---
---

## 🔑 TCM Properties

**Taste:** `= join(this.herb_data.taste, ", ")`
**Temperature:** `= this.herb_data.temperature`
**Channels Entered:** `= join(this.herb_data.channels, ", ")`

---

## ⚡ Functions & Actions

- **Tonifies the Kidneys and fortifies the yang:** For impotence, urinary incontinence, nocturnal emissions, and irregular menstruation from Kidney yang deficiency. This herb is used for infertility from either a cold Womb (in women) or cold essence (in men).
    - With Eucommiae Cortex (*du zhong*) for impotence, spermatorrhea, and weakness and pain in the lower back and legs.
    - Often combined with Epimedii Herba (*yin yang huo*) to strengthen its effects. This pair of herbs is also the core of the formula Two-Immortal Decoction (*er xian tang*).
- **Expels cold and eliminates dampness:** For obstinate cold-damp painful obstruction with generalized pain, a sense of weakness in the bones and sinews, and lower back and knee pain. Especially useful for cold abdominal or lower back pain.
    - With Asari Radix et Rhizoma (*xi xin*) and Eleutherococci Gracilistyli Cortex (*wu jia pi*) for cold-damp induced pain and coldness in the lower back and legs.

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
Contraindicated in patterns of yin deficiency with heat signs. Long-term use is not recommended.

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
Good quality consists of dry, thick and long, solid roots with a greyish black surface.

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
