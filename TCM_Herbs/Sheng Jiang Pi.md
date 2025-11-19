---
# 🔹 Core Metadata (Universal Fields)
id: "herb-20251001123706"
name: "Sheng Jiang Pi"
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
  hanzi: "生姜皮"
  pinyin: "Shēng Jiāng Pí"
  pharmaceutical: "Zingiberis Rhizomatis Cortex"
  english: "Ginger Peel"
  alternate_names: []

  # TCM Properties
  taste: [Acrid, Cooling]
  temperature: "Cooling"
  channels: [Lung, Spleen, Stomach]

  # Clinical Information
  dosage: "N/A"
  toxicity: "N/A"
  functions: [Harmonizes the middle, Promotes urination, Reduces edema, Mobilizes the exterior]
  dui_yao: []

  # Additional Information
  constituents: []
  quality: "N/A"
  text_first_appeared: "N/A"

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

N/A

---
---

## 🔑 TCM Properties

**Taste:** `= join(this.herb_data.taste, ", ")`
**Temperature:** `= this.herb_data.temperature`
**Channels Entered:** `= join(this.herb_data.channels, ", ")`

---

## ⚡ Functions & Actions

- Releases the exterior and disperses cold: for exterior cold patterns.
    - With Jujubae Fructus (da zao) for externally-contracted wind-cold.
    - Also for alleviating epigastric pain, nausea, and vomiting by strengthening the Spleen qi. This combination protects the Stomach qi and reduces the irritation of the gastrointestinal tract caused by other herbs.
    - Also adjusts the nutritive and protective qi for patients suffering from exterior deficiency who sweat without an improvement in their condition, as in Cinnamon Twig Decoction (gui zhi tang).
- Warms the middle burner and alleviates vomiting: for cold in the Stomach, especially when there is vomiting.
    - With Pinelliae Rhizoma preparatum (zhi ban xia) for vomiting due to many causes, and for productive cough due to phlegm-dampness.
    - With Bambusae Caulis in taeniam (zhu ru) for vomiting due to heat in patients with Stomach qi deficiency.
- Warms the Lungs and stops cough: for cough due to both acute wind-cold cough patterns and chronic Lung disorders with phlegm.
    - With Perillae Folium (zi su ye), Armeniacae Semen (xing ren), and Asteris Radix (zi wan) for cough due to wind-cold affecting the Lung with profuse sputum.
    - With Bambusae Succus (zhu li) for cough and headache due to heat-induced phlegm, or aphasia and numbness from wind-stroke due to phlegm obstruction.
- Resolves toxicity: for resolving toxicity or treating the effects of overdose of other herbs, such as Aconiti Radix lateralis (fu zi) or Pinelliae Rhizoma (ban xia), or for seafood poisoning.
    - With Perillae Folium (zi su ye) for vomiting and diarrhea from seafood poisoning.

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
N/A

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
N/A

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
