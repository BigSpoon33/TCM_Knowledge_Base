---
# 🔹 Core Metadata (Universal Fields)
id: "herb-20251001123706"
name: "Lu Gen"
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
  hanzi: "芦根"
  pinyin: "Lu Gen"
  pharmaceutical: "Phragmitis Rhizoma"
  english: "Reed Rhizome"
  alternate_names: []

  # TCM Properties
  taste: [Sweet, Cold]
  temperature: "Cold"
  channels: [Lung, Stomach]

  # Clinical Information
  dosage: "15-30g"
  toxicity: "None"
  functions: [Clears heat, Generates fluids, Alleviates nausea, Promotes urination, Cools the Lungs and Stomach, Encourages rashes to surface]
  dui_yao: []

  # Additional Information
  constituents: [Phenolic compounds: caffeic acid, tocopherol, p-hydroxybenzaldehyde, syringaaldehyde, vanillic acid, p-coumaric acid, dioxanelignin, tricin, coixol, Triterpenes: β-amyrin, taraxerol, taraxerone, Other constituents: carbohydrates (51%), proteins (5%), fats (1%), asparamide, proline, betaine, 2,5-dimethoxy-p-benzoquinone, vitamine B1, B2, C]
  quality: "Good quality consists of thick, uniform, yellow, and glossy pieces."
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

Its primary functions are to cool Lung heat, eliminate phlegm, and expel pus, but it also cools the Stomach, generates fluids, and alleviates nausea. It is not greasy in nature, and does not have the effect of retaining pathogens within the body.

The *Grand Materia Medica* recites its major indications:

Wasting and thirsting with visitant heat (消渴热, *xiao ke re*), alleviates frequent urination, treats upset Stomach causing nausea and rebelliousness that prevents food intake, heat in the Stomach, and internal heat due to cold damage. It also resolves high fever, opens the Stomach, treats dysphagia and continuous dry retching, stifling irritability due to cold or hot seasonal disorders, thirst due to diarrhea or dysenteric disorder, and Heart heat during pregnancy.

*Seeking Accuracy in the Materia Medica* has an interesting discussion of the role of this herb in the treatment of urinary frequency due to compelling fire preventing the descent of Lung qi:

There is nothing unusual about its functions, which are simply to clear the Lungs and direct fire downward.

Whenever there is heat in the chest, fire ascends, causing vomiting; when rebellious qi refuses to descend, Spleen and Lung heat arise, causing wasting and thirsting with urinary frequency, which can even be unendurable.

Wang Ang elaborates on this mechanism:

The Lungs are the upper source of water. The Spleen distributes essence, which ascends and enters the Lungs. Only then can the Lungs unblock and regulate the fluid metabolism and transport to the Bladder. Kidneys are the water organ and control the two excretions. When the three channels have heat, urination will be frequent, and even a small amount cannot be withheld. This is because urgency is fire's nature. Phragmitis Rhizoma (*lu gen*) is hollow inside, thus it enters the Heart and Lungs to cool upper burner heat. When this heat is released, then the Lungs can transform and promote movement so that urination returns to normal.

---
---

## 🔑 TCM Properties

**Taste:** `= join(this.herb_data.taste, ", ")`
**Temperature:** `= this.herb_data.temperature`
**Channels Entered:** `= join(this.herb_data.channels, ", ")`

---

## ⚡ Functions & Actions

-   **Clears heat and generates fluids:** For heat patterns with such symptoms as high fever, irritability, and thirst. Especially useful when the heat is accompanied by upward-surging of rebellious qi.
    -   With Trichosanthis Radix (*tian hua fen*) and Ophiopogonis Radix (*mai men dong*) for injury to the fluids from febrile disease marked by irritability and thirst.
    -   With Chrysanthemi Flos (*ju hua*), Lonicerae Flos (*jin yin hua*), and Menthae Haplocalycis Herba (*bo he*) for externally-contracted wind-heat attacking the Lungs marked by cough and thirst, as in Mulberry Leaf and Chrysanthemum Drink (*sang ju yin*).
    -   With Bambusae Caulis in Taeniam (*zhu ru*) and Eriobotryae Folium (*pi pa ye*) for irritability, thirst, and vomiting due to Stomach heat.
    -   With Coicis Semen (*yi yi ren*) and Benincasae Semen (*dong gua zi*) for Lung abscess with purulent sputum streaked with fetid blood, as in Reed Decoction (*wei jing tang*).
    -   With Gypsum Fibrosum (*shi gao*) for dry mouth, severe bad breath, and toothache due to Stomach fire.
-   **Clears heat and promotes urination:** For dark, scanty urine or blood in the urine, especially when accompanied by irritability and thirst.
-   **Encourages rashes to surface:** For febrile diseases with rashes that are incompletely expressed.

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
Use with caution in those with cold from deficiency of the Spleen and Stomach.

"Its nature is cold and cooling; do not consume if there is distention due to cold sudden turmoil disorder, or nausea and vomiting due to cold upset Stomach." (*Harm and Benefit in the Materia Medica*)

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
Good quality consists of thick, uniform, yellow, and glossy pieces.

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
