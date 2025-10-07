---
# 🔹 Core Metadata (Universal Fields)
id: "herb-20251001123706"
name: "Fu Xiao Mai"
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
  hanzi: "浮小麦"
  pinyin: "Fú Xiǎo Mài"
  pharmaceutical: "Tritici Fructus Levis"
  english: "Floating Wheat Grain"
  alternate_names: []

  # TCM Properties
  taste: [Sweet, Slightly salty]
  temperature: "Cool"
  channels: [Heart]

  # Clinical Information
  dosage: "15-30g"
  toxicity: "Not toxic"
  functions: [Augments the Heart qi, Inhibits Heart fluids, Clears heat from the pores and interstices, Stops spontaneous sweating and nightsweats]
  dui_yao: []

  # Additional Information
  constituents: [Starch (53-70%), Protein (11%), Sugars: sucrose, maltose, fructose, glucose, raffinose, melibiose, dextrin, Amino acids: arginine, histidine, glycine, Fixed oil: glycerides of oleic acid, linoleic acid, palmitic acid, stearic acid, Other constituents: lecithin, allantoin, β-sitosterol, α-tocotrienol, gramisterol]
  quality: "Good quality wheat grains are uniform in size, lightweight, glossy, and are able to float."
  text_first_appeared: "Treasury of Words on the Materia Medica"

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

Sweet, such that it augments the qi, and slightly salty, such that it cools, Tritici Fructus levis (*fu xiao mai*) is light in weight so that it reaches outward to the exterior, yet enters the Heart channel where it conserves the yang fluids of the Heart. Because it reaches the exterior with a gentle cooling and restraining action and nourishes the Heart qi, it is most appropriate for stopping both spontaneous sweating and nightsweats. The Grand Materia Medica says that Tritici Fructus levis (*fu xiao mai*) is "sweet, salty, cold, and not toxic. It benefits the qi, eliminates heat, stops spontaneous sweating, nightsweats, steaming bones, and heat from deficiency, and consumptive heat in women." In Convenient Reader of Materia Medica, Zhang Bing-Cheng says that it is "Sweet, salty, eliminates heat from deficiency, cools and inhibits the Heart yang fluids."
- However, Treasury of Words on the Materia Medica suggests a somewhat different view of its actions: Tritici Fructus levis (*fu xiao mai*) is the husk of wheat, dried and floating, without [containing the] flesh [of the grain]. Light in weight and drying by nature, it excels at eliminating wind-dampness within the Spleen and Stomach. If dampness predominates with excessive sweating, dry-fry and decoct one or two decaliters (*ge*) to drink. If the spontaneous sweating or nightsweats are due solely to deficiency of yin and yang, this is inappropriate.
- While this view may seem contradictory, in the clinic it is not uncommon for dampness within the exterior - or just below the exterior, at the level of the flesh (part and parcel of the Spleen and Stomach) - to prevent the normal outward dissipation of heat, so that the heat increases locally and forces sweating by extruding the dampness outward. Greater accumulation of dampness at these levels may result in forcing heat upward toward the head, where there is less flesh, so that the patient sweats only on the face and head.
- This mechanism of action - dispersal of the pathogenic influence rather than inhibition of the sweating itself - seems to be supported by a passage in Encountering the Sources of the Classic of Materia Medica: "the ability of Tritici Fructus levis (*fu xiao mai*) to inhibit nightsweats is through its dispersal of heat from the skin and interstices." This understanding is reflected in certain modern texts as well. For example, Practical Differentiation of Chinese Materia Medica quotes the statement in Encountering the Source, then comments: "In summary, the effects of Tritici Fructus levis (*fu xiao mai*) are chiefly those of augmenting the qi and eliminating heat; its ability to stop sweating is not caused by restraining and inhibiting." Yet this has not prevented those authors (or ourselves) from placing this herb in the chapter on herbs that restrain and bind.

---
---

## 🔑 TCM Properties

**Taste:** `= join(this.herb_data.taste, ", ")`
**Temperature:** `= this.herb_data.temperature`
**Channels Entered:** `= join(this.herb_data.channels, ", ")`

---

## ⚡ Functions & Actions

**Stabilize and Bind**
- **English:** Light wheat grain
- **Japanese:** Fushobaku
- **Korean:** Pusomaek
- Augments the Heart qi, inhibits the Heart fluids, clears heat from the pores and interstices, and thus stops spontaneous sweating and nightsweats.
- **Inhibits sweating:** for many kinds of sweating from deficiency including spontaneous sweating from qi deficiency, and nightsweats from yin deficiency.
    - With Astragali Radix (*huang qi*) and calcined Ostreae Concha (*duan mu li*) for spontaneous sweating associated with deficiency, as in Oyster Shell Powder (*mu li san*).
    - With Lycii Cortex (*di gu pi*), Schisandrae Fructus (*wu wei zi*), and Ophiopogonis Radix (*mai men dong*) for nightsweats due to heat from yin deficiency.
    - With Rehmanniae Radix (*sheng di huang*), Scrophulariae Radix (*xuan shen*), and Lycii Cortex (*di gu pi*) for steaming bone disorder.

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
Contraindicated when sweating is caused by a pathogen in the exterior.
- Inappropriate for spontaneous sweating or nightsweats due only to deficiency of both yin and yang.

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
Good quality wheat grains are uniform in size, lightweight, glossy, and are able to float.

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
