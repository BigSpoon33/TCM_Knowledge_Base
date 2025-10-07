---
# 🔹 Core Metadata (Universal Fields)
id: "herb-20251001123706"
name: "Bian Xu"
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
  hanzi: "萹蓄"
  pinyin: "bian xu"
  pharmaceutical: "Polygoni avicularis Herba"
  english: "knotgrass, knotweed, polygonum"
  alternate_names: []

  # TCM Properties
  taste: [bitter, slightly cold]
  temperature: "cold"
  channels: [Bladder]

  # Clinical Information
  dosage: "9-15g"
  toxicity: "none noted"
  functions: [Clears damp-heat from the Bladder, promotes urination, unblocks painful urinary dribbling, Expels parasites, stops itching]
  dui_yao: []

  # Additional Information
  constituents: [Flavonoids: quercetin, avicularin, quercitrin, vitexin, isovitexin, luteolin, rhamnetin-3-galactoside, hyperin, Coumarins: umbelliferone, scopoletin, Phenolic acids: ferulic acid, sinapic acid, vanillic acid, syringic acid, melilotic acid, p-coumaric acid, p-hydroxybenzoic acid, salicylic acid, p-hydroxyphenylacetic acid, gentisic acid, caffeic acid, protocatechuic acid, gallic acid, ellagic acid, Other constituents: oxalic acid, silicic acid, amino acids, glucose, fructose, sucrose, polysaccharides, tannins, vitamin E]
  quality: "Good quality consists of young, green plants with many leaves and without foreign matter."
  text_first_appeared: "Divine Husbandman's Classic of the Materia Medica"

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

Bitter and cold, with downward-directing actions, Polygoni avicularis Herba (bian xu) is best for clearing heat and facilitating the removal of dampness. It can clear damp-heat from the Bladder, thereby promoting urination and unblocking painful urinary dribbling, while also clearing damp-heat so as to resolve the heat toxin. Thus, apart from treating painful urinary dribbling due to damp-heat, it is often used for damp-heat jaundice, dysenteric disorders due to damp-heat, and damp-heat sores and itchy rashes.

The Divine Husbandman's Classic of the Materia Medica notes that this herb "primarily treats pruritic weeping rashes, itchy sores, and hemorrhoids, and kills the three parasites." In Encountering the Sources of the Classic of Materia Medica, Zhang Lu observes that it "promotes urination and disperses damp-heat, treating jaundice, sudden turmoil disorder, and vaginal erosion." The Divine Husbandman [states that it] primarily treats pruritic weeping rashes, itchy sores, and hemorrhoids, all of which are damp-heat disorders. The three parasites, too, are transformed from damp-heat.

---
---

## 🔑 TCM Properties

**Taste:** `= join(this.herb_data.taste, ", ")`
**Temperature:** `= this.herb_data.temperature`
**Channels Entered:** `= join(this.herb_data.channels, ", ")`

---

## ⚡ Functions & Actions

*   **Clears damp-heat from the Bladder, promotes urination, and unblocks painful urinary dribbling:** for damp-heat painful urinary dribbling.
    *   With Dianthi Herba (qu mai) and Plantaginis Semen (che qian zi) for urinary discomfort due to damp-heat in the lower burner or urinary tract stones as in Eight-Herb Powder for Rectification (ba zheng san).
    *   With Cirsii Herba (xiao ji) and Imperatae Rhizoma (bai mao gen) for painful bloody urinary dribbling.
    *   With Jin Qian Cao (Lysimachiae/Desmodii/etc. Herba) and Lygodii Spora (hai jin sha) for stony painful urinary dribbling.
*   **Expels parasites and stops itching:** for damp skin lesions with itching, including tinea, or for intestinal parasites such as tapeworm, hookworm, and pinworm.
    *   With Kochiae Fructus (di fu zi) as an external wash for genital itching due to damp-heat in the lower burner.
    *   With Quisqualis Fructus (shi jun zi) and Mume Fructus (wu mei) for roundworm.
    *   With Torreyae Semen (fei zi), Stemonae Radix (bai bu), and Arecae Semen (bing lang) as an external wash for pinworm.

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
"This only treats the branch [of a disorder], it does not augment a person: do not use it for an extended period of time" (Seeking Accuracy in the Materia Medica).

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
Good quality consists of young, green plants with many leaves and without foreign matter.

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
