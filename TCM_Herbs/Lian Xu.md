---
# 🔹 Core Metadata (Universal Fields)
id: "herb-20251001123706"
name: "Lotus Stamen / Lian Xu"
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
  hanzi: "莲须"
  pinyin: "lian xu"
  pharmaceutical: "Nelumbinis Stamen, Nelumbo nucifera (lian) GAERTN."
  english: "Lotus stamen"
  alternate_names: []

  # TCM Properties
  taste: [Sweet, astringent]
  temperature: "Neutral"
  channels: [Heart, Kidney, Liver]

  # Clinical Information
  dosage: "3-9g"
  toxicity: "None"
  functions: [Clears the Heart and stabilizes the Kidneys, while binding the essence and stopping its loss, Stops bleeding]
  dui_yao: []

  # Additional Information
  constituents: [luteolin, luteolinglucoside, isoquercitrin, quercetin]
  quality: "Good quality consists of long and thin, pale yellow, soft, and unfragmented stamina."
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

Sweet, astringent, and neutral, *Nelumbinis* Stamen (lian xu) is more binding than *Nelumbinis* Semen (lian zi). Like the seeds, it cools the Heart and secures the essential qi of the Kidneys, while more strongly stopping spermatorrhea, enuresis, vomiting of blood, and incessant uterine bleeding. It is often mentioned in connection with thin, watery semen, as in the following passage from *Encountering the Sources of the Classic of Materia Medica*: "[It] cools the Heart and unblocks the Kidneys. Because its nature is binding, it is an important herb to secure the essential qi... however, it is appropriate only for thin semen due to excessive [sexual] desire."

*Commentary on the Divine Husbandman's Classic of Materia Medica* states that it was not recorded in the *Divine Husbandman*, but was often used in ancient formulas [designed] to secure the true, augment, and tonify. Detailing its primary therapeutic indications, it is a herb of the leg lesser yin [Kidney] channel, and also unblocks the arm lesser yin [Heart] channel; it cools the Heart, enters the Kidneys to secure the essential qi, blacken the hair, stop vomiting of blood, and remedy leakage and drainage.

*Seeking Accuracy in the Materia Medica* observes: Its actions are similar to those of *Nelumbinis* Semen (lian zi), but it is more astringent in nature. Consumed, it can cool the Heart and unblock the Kidneys, augment the blood, secure the essence, blacken the hair and beard, and stop incessant uterine bleeding and vaginal discharge.

---
---

## 🔑 TCM Properties

**Taste:** `= join(this.herb_data.taste, ", ")`
**Temperature:** `= this.herb_data.temperature`
**Channels Entered:** `= join(this.herb_data.channels, ", ")`

---

## ⚡ Functions & Actions

*   **Clears the Heart and stabilizes the Kidneys, while binding the essence and stopping its loss:** For wet dreams, spermatorrhea, premature ejaculation, enuresis, and vaginal discharge.

    *   With *Astragali complanati* Semen (sha yuan zi) and *Ostreae* Concha (mu li) for loss of sperm and tinnitus, as in Metal Lock Pill to Stabilize the Essence (*jin suo gu jing wan*).
    *   With *Rosae laevigatae* Fructus (jin ying zi) and *Euryale* Semen (qian shi) for vaginal discharge from Kidney deficiency.
*   **Stops bleeding:** Has a mild effect and is usually accompanied by other herbs.

    *   With charred *Nelumbinis* Nodus rhizomatis (ou jie tan) for a variety of bleeding disorders.
    *   With *Agrimoniae* Herba (xian he cao) and *Bletilla* Rhizoma (bai ji) for incessant vomiting of blood.
    *   With *Angelicae sinensis* Radix (dang gui) and *Carthami* Flos (hong hua) for irregular uterine bleeding when one needs to both stop the bleeding and invigorate the blood.

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
Contraindicated in those with abdominal distention or constipation.

**Traditional Contraindications**

"Contraindicated in those with urinary difficulty." (*Thoroughly Revised Materia Medica*)

"It should not be used for loss of control due to ascendant yang, for fear that its binding confinement will lead to [further] afflictions." (*Encountering the Sources of the Classic of Materia Medica*)

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
Good quality consists of long and thin, pale yellow, soft, and unfragmented stamina.

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
