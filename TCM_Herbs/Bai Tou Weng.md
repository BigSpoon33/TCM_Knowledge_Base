---
# 🔹 Core Metadata (Universal Fields)
id: "herb-20251001123706"
name: "Bai Tou Weng"
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
  hanzi: "白头翁"
  pinyin: "bái tóu wēng"
  pharmaceutical: "Pulsatillae Radix"
  english: "Chinese anemone root, anemone"
  alternate_names: []

  # TCM Properties
  taste: [Bitter, cold]
  temperature: "cold"
  channels: [Large Intestine, Stomach]

  # Clinical Information
  dosage: "6-15g"
  toxicity: "The fresh herb contains protoanemonin, which irritates the skin and mucous membranes. Ingestion of the fresh herb causes salivation, gastrointestinal inflammation, vomiting, abdominal pain, hematuria, heart failure, and death as a consequence of respiratory failure. During the process of drying and storage, protoanemonin is polymerized to anemonin, which renders the herb less irritating. Only the dried herb should therefore be used. Decoctions of the dried herb in normal doses are very unlikely to cause significant side effects."
  functions: [Clears heat, Resolves fire toxicity, Cools the blood, Resolves toxicity]
  dui_yao: []

  # Additional Information
  constituents: [Triterpene saponins: pulchinenoside A (=anemoside A), pulchinenoside B, pulchinenoside C, pulchinenoside D, betulinic acid-3-O-α-L-arabinopyranoside, Organic acids: betulinic acid, 3-oxobetulinic acid, 23-hydroxybetulinic acid, pulsatillic acid, Other constituents: anemonin, protoanemonin, okinalin, okinalein, daucosterol, arabinose]
  quality: "Good quality consists of thick and long roots, with a solid texture."
  text_first_appeared: "Divine Husbandman's Classic of the Materia Medica"

  # Source References
  bensky_pdf: "627"
  bensky_page: "187"

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

Bitter and cold, Pulsatillae Radix (Bai Tou Weng) drains and directs downward, clears heat, cools the blood, and resolves toxicity. It enters the Stomach and Large Intestine channels, where it expels heat toxin accumulating into clumps in the Stomach and Intestine. It is thus commonly used in the treatment of hot dysenteric disorders accompanied by a bearing-down sensation, especially where bleeding is involved. It is also used as an enema for dysenteric disorders.
Essentials of the Materia Medica says of this herb: "Bitterness firms the Kidneys, coldness cools the blood, and it enters the blood level of the yang brightness channel. Treats heat toxin dysenteric disorder with bleeding." This is a good summary of the present understanding and use of Pulsatillae Radix (Bai Tou Weng). Earlier, however, the Grand Materia Medica records an interesting historical progression of indications for Pulsatillae Radix (Bai Tou Weng), from the Divine Husbandman's Classic of the Materia Medica up to the Materia Medica of Ri Hua-Zi:
[For] warm malarial disorder with frequent thrashing delirium, chills and fever, abdominal masses, accumulation and goiter; drives out blood, stops pain, treats metal sores (Divine Husbandman's Classic). Nosebleeds, alleviates toxic dysenteric disorders. (Miscellaneous Records). Red dysenteric disorder, abdominal pain, toothache, pain in all joints, scrofula on the lower neck (Arcane Essentials from the Imperial Library). All types of wind qi, warms the lower

---
---

## 🔑 TCM Properties

**Taste:** `= join(this.herb_data.taste, ", ")`
**Temperature:** `= this.herb_data.temperature`
**Channels Entered:** `= join(this.herb_data.channels, ", ")`

---

## ⚡ Functions & Actions

• Clears heat and resolves fire toxicity: primarily for dysenteric disorders, especially those due to damp-heat in the Stomach or Intestines.
- With Phellodendri Cortex (huang bai), Coptidis Rhizoma (huang lian), Fraxini Cortex (qin pi) for dysenteric disorders due to damp-heat or epidemic toxins, as in Bai Tou Weng Tang (Pulsatilla Decoction)
- With Portulacae Herba (ma chi xian) for dysenteric disorders due to heat toxin.
- With Bupleuri Radix (chai hu), Scutellariae Radix (huang qin), and Arecae Semen (bing lang) for warm malarial disorders.
- With Sophorae Flavescentis Radix (ku shen) as an external wash for itchy vaginal discharge.

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
Pulsatillae Radix (Bai Tou Weng) is bitter and cold, and is contraindicated for any vaginal discharge due to deficiency of the Stomach, or diarrhea due to cold from deficiency. Because the cold and bitterness drain and direct downward, it should not be used for dysenteric disorders that exhibit pale watery blood. (Rectification of the Meaning of Materia Medica)

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
Good quality consists of thick and long roots, with a solid texture.

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
