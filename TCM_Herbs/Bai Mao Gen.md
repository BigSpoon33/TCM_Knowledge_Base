---
# 🔹 Core Metadata (Universal Fields)
id: "herb-20251001123706"
name: "Imperata Rhizome / Bai Mao Gen"
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
  hanzi: "白茅根"
  pinyin: "bái máo"
  pharmaceutical: "Imperatae Rhizoma"
  english: "imperata rhizome, woolly grass, white grass"
  alternate_names: []

  # TCM Properties
  taste: [Sweet, cold]
  temperature: "cold"
  channels: [Lung, Stomach, Small Intestine, Bladder]

  # Clinical Information
  dosage: "9-30g"
  toxicity: "Use with caution in those with cold from deficiency of the Spleen and Stomach."
  functions: [Cools the blood and stops bleeding, Clears heat and promotes urination, Clears heat from the Stomach and Lungs]
  dui_yao: []

  # Additional Information
  constituents: [Triterpenes: arundoin, cylindrin, fernenol, isoarborinol methylether, arborinol methylether, simiarenol, Organic acids: oxalic acid, malic acid, citric acid, Sugars: sucrose, glucose, fructose, xylose, Other constituents: anemonin, carotinoids]
  quality: "Good quality consists of thick, white rhizomes with a sweet taste."
  text_first_appeared: "Collection of Commentaries on the Materia Medica"

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

Sweet and cold, Imperatae Rhizoma (bái máo gēn) enters the Lung, Stomach, Small Intestine, and Bladder channels to clear latent lurking heat, cool the blood, and stop bleeding. It also benefits the Stomach and alleviates thirst, cools heat, and promotes urination. Its sweetness is not cloying, its coldness is not harmful to the Stomach, and when it promotes urination, this does not injure the yin, but rather leads heat downward and out of the body through the urine. For all of these reasons it is an excellent herb for treating bleeding in the upper or lower body due to heat, cough due to Lung heat, and damp-heat leading to painful urinary dribbling.

The primary types of bleeding for which it is used include vomiting blood, nosebleed, and blood in the urine, for which it is especially effective.

Imperatae Rhizoma is cold, cooling, and very sweet in flavor, able to clear heat in the blood aspect without injuring with dryness, and is also neither cloying nor sticky. It cools the blood without any worry that it will cause accumulation or stagnation—it can also unblock blocked urination due to painful urinary dribbling and treat blood in the urine. (Rectification of the Meaning of Materia Medica)

[Imperatae Rhizoma sweet in flavor, cool] is light by nature, hollow in the center with nodes; and the most excellent thing for venting and bringing out heat constrained within the Organs, drawing out the toxicity of pox and rashes to the exterior. It is also excellent for facilitating urine that is painful and difficult to pass, and scanty due to heat, with abdominal distention and generalized edema. Moreover, it enters the Lungs and clears heat to alleviate cough and calm wheezing. Because its flavor is sweet, and when the fresh root is chewed it is full of juice, it is able to enter the Stomach and enrich the yin in order to generate fluids and alleviate thirst. It treats heat in both the Lungs and Stomach, coughing of blood, spitting up of blood, nosebleed, and blood in the urine, but for marked therapeutic effect, the fresh root must be used.

---
---

## 🔑 TCM Properties

**Taste:** `= join(this.herb_data.taste, ", ")`
**Temperature:** `= this.herb_data.temperature`
**Channels Entered:** `= join(this.herb_data.channels, ", ")`

---

## ⚡ Functions & Actions

- Cools the blood and stops bleeding: for the chaotic movement of hot blood with such symptoms as nosebleed, vomiting blood, coughing of blood, and blood in the urine.
    - With Nelumbinis Nodus Rhizomatis (ǒu jié) and Cirsii Herba (xiǎo jì) for heat-induced nosebleed, bloody urine, or coughing of blood. Most effective if the fresh juice of these herbs is used.
    - With Rehmanniae Radix (shēng dì huáng) and Poria (fú líng) for blood in the urine due to heat, even with significant underlying deficiency.
- Clears heat and promotes urination: for hot painful urinary dribbling and other heat patterns with edema and urinary difficulty.
    - With Pyrrosiae Folium (shí wěi) for hesitating urination.
    - With Artemisiae Scopariae Herba (yīn chén) and Gardeniae Fructus (zhī zi) for jaundice due to damp-heat.
    - With Phaseoli Semen (chì xiǎo dòu) for edema from either deficiency or damp-heat, especially where there is also jaundice.
    - With Astragali Radix (huáng qí) for qi deficiency-induced edema.
- Clears heat from the Stomach and Lungs: for nausea and thirst due to Stomach heat, or wheezing due to Lung heat.
    - With Phragmitis Rhizoma (lú gēn) for the thirst and irritability associated with warm pathogen diseases.
    - With Puerariae Radix (gé gēn) for the nausea and vomiting associated with warm pathogen diseases.
    - With Gypsum Fibrosum (shí gāo) for remnants of fever along with thirst and dark urine in the later stages of warm pathogen diseases.

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
This is inappropriate if the bleeding results from cold from deficiency. The same applies if there is diarrhea due to cold, or vomiting of phlegm-dampness due to cold in the center, or fever from stasis of thin mucus. (Harm and Benefit in the Materia Medica)

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
Good quality consists of thick, white rhizomes with a sweet taste.

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
