---
# 🔹 Core Metadata (Universal Fields)
id: "herb-20251001123706"
name: "Shui Niu Jiao"
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
  hanzi: "水牛角"
  pinyin: "Shui Niu Jiao"
  pharmaceutical: "Bubali Cornu"
  english: "Water Buffalo Horn"
  alternate_names: []

  # TCM Properties
  taste: [Salty, cold]
  temperature: "cold"
  channels: [Heart, Liver, Stomach]

  # Clinical Information
  dosage: "30-120g in decoction; 6-15g as a powder"
  toxicity: "After administration of a high dosage, side effects have been reported including gastric discomfort, nausea, vomiting, fullness in the abdomen, and reduced appetite."
  functions: [Clears heat, Resolves fire toxicity, Cools the blood, Arrests tremors]
  dui_yao: []

  # Additional Information
  constituents: [Amino acids: serine, glycine, alanine, lysine, histidine, aspartic acid, arginine, threonine, glutamic acid, proline, cystine, methionine, isoleucine, leucine, tyrosine, phenylalanine, Other constituents: cholesterol, cardiotonic constituent, peptides, keratin]
  quality: "This product can range in color from pale yellow to light brown."
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

Cold, bitter, and salty, Bubali Cornu (shui niu jiao) enters the nutritive and blood levels, primarily clearing intense heat from the Heart, Liver, Stomach, and Triple Burner while cooling the blood and resolving toxicity. Particularly effective for clearing pathogenic heat from the Heart channel, and resolving heat toxin from the blood, it is often used for high fever, clouded consciousness, convulsions, and spasms due to pathogenic heat entering the Heart and nutritive levels. It is also used for jaundice or rashes due to warm pathogen disease toxicity delving deeply into the blood, or heat forcing the blood to move chaotically, leading to epistaxis or the passage of blood in the stool or urine.

Water buffalo horn is not just a modern substitute for rhinoceros horn. The fifth-century Miscellaneous Records of Famous Physicians states that it "treats chills, fever, and headache due to seasonal disorders", while the Materia Medica of Hua-Zi confirms that "decocted, the liquid treats heat-toxin wind and high fever." The Grand Materia Medica also reports that it "treats painful urinary dribbling and breaks up blood stasis."

Like Rhinocerotis Cornu (xi jiao), water buffalo horn (shui niu jiao) is bitter, salty, and cold, and similarly cools the blood, clears heat, and resolves toxicity. However, its actions are weaker, and a larger amount of buffalo horn is necessary to be effective. Fortunately, there is as yet no shortage of this resource.

---
---

## 🔑 TCM Properties

**Taste:** `= join(this.herb_data.taste, ", ")`
**Temperature:** `= this.herb_data.temperature`
**Channels Entered:** `= join(this.herb_data.channels, ", ")`

---

## ⚡ Functions & Actions

- **Clears heat, resolves fire toxicity, and cools the blood:** For warm-heat pathogen diseases accompanied by extreme heat or heat signs, and for very high fever affecting the nutritive or blood levels with chaotic movement of hot blood. Manifestations include erythema, purpura, nose bleed, vomiting of blood, or convulsions and delirium.
    - With Saigae Tataricae Cornu (ling yang jiao) for high fever, delirium, and convulsions associated with warm heat pathogen diseases.
    - With Rehmanniae Radix (sheng di huang) for loss of consciousness and delirium together with vomiting of blood, nosebleed, or purpura due to heat in the blood level. Often Moutan Cortex (mu dan pi), Paeoniae Radix rubra (chi shao), Isatidis Folium (da qing ye), and Arnebiae/Lithospermi Radix (zi cao) are added to strengthen the blood-cooling action. See Rhinoceros Horn and Rehmannia Decoction (xi jiao di huang tang).
    - With Gypsum Fibrosum (shi gao) and Scrophulariae Radix (xuan shen) for high fever that worsens at night, dark-red maculae, thirst, and a rapid pulse due to fire in both the qi and blood levels, as in Transform Maculae Decoction (hua ban tang).
- **Clears heat and arrests tremors:** For warm-heat pathogen diseases when the heat enters the nutritive or blood levels with such symptoms as unremitting high fever, loss of consciousness, delirium, convulsions, or manic behavior, as in Greatest Treasure Special Pill (zhi bao dan).
    - With Coptidis Rhizoma (huang lian) and Scrophulariae Radix (xuan shen) for high fever, loss of consciousness and delirium, vomiting of blood, nosebleed, and purpura associated with warm-heat pathogen diseases.

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
Use with caution in those with cold from deficiency of the middle burner. See Toxicity below.

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
This product can range in color from pale yellow to light brown.

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
