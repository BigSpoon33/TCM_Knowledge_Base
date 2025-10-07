---
# 🔹 Core Metadata (Universal Fields)
id: "herb-20251001123706"
name: "Hei Zhi Ma"
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
  hanzi: "黑芝麻"
  pinyin: "Hēi zhī má"
  pharmaceutical: "Sesami Semen Nigrum"
  english: "Black sesame seeds"
  alternate_names: []

  # TCM Properties
  taste: [Sweet]
  temperature: "Neutral"
  channels: [Kidney, Liver, Large Intestine]

  # Clinical Information
  dosage: "9-30g"
  toxicity: "Consumption may cause allergic reactions with such symptoms as asthma, pruritus, urticaria, edema, cough, sweating, nausea, vomiting, abdominal pain, sneezing, and an itchy throat."
  functions: [Nourishes and fortifies the Liver and Kidneys, Nourishes the blood and extinguishes wind, Moistens and lubricates the Intestines]
  dui_yao: []

  # Additional Information
  constituents: [Fatty oil: oleic acid, linoleic acid, palmitic acid, stearic acid, arachidic acid, behenic acid, lignoceric acid, lecithin, Lignans: sesamin, sesamolin, sesamol, Proteins: α-globulin, β-globulin, 13s-globulin, albumin, glutelin, sesame lectin, Phytosterols: sitosterol, campesterol, D-5-avenasterol, stigmasterol, Sugars: planteose, sesamose, D-glucose, D-galactose, D-fructose, raffinose, stachyose, sucrose, hemicellulose A, B, Other constituents: amino acids, pedaliin, folic acid, nicotinic acid, riboflavin, vitamin B, vitamin E, cytochrome C]
  quality: "Good quality consists of black, full seeds, uniform in size, with an intense aroma and lacking foreign matter."
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

Sweet, neutral, rather oily, and black, *Sesami Semen nigrum* (*hei zhi ma*) enters the Liver and Kidney channels to tonify the yin and blood, brighten the eyes, blacken the hair, moisten the skin, and lubricate the Intestines. Commentary on the Divine Husbandman's Classic of Materia Medica says that it is "harmonious in nature and flavor, neither hot nor cold; it is an excellent food that augments the Spleen and Stomach, and tonifies the Liver and Kidneys." For promoting lactation, the Grand Materia Medica recommends that the herb be dry-fried, mixed with a bit of salty water, and eaten.

The eighth-century book Ri Materia Medica of Hua-Z observes that it:

"Tonifies the middle, augments the qi, and nourishes the five yin organs so that it treats consumption, emaciation, and fatigue during the postpartum period, promotes resistance to extremes in temperature, and alleviates palpitations. It drives out wind-dampness, roving wind, and head wind."

Liu Wan-Su explains: "To treat wind, first treat the blood; when the blood is invigorated, then wind will be expelled. [This herb] enters the Liver and augments the blood, and thus cannot be omitted from herbs that treat wind."

---
---

## 🔑 TCM Properties

**Taste:** `= join(this.herb_data.taste, ", ")`
**Temperature:** `= this.herb_data.temperature`
**Channels Entered:** `= join(this.herb_data.channels, ", ")`

---

## ⚡ Functions & Actions

- **Nourishes and fortifies the Liver and Kidneys:** For yin deficiency of the Liver and Kidneys with such symptoms as blurred vision, tinnitus, and dizziness. Also used to help patients recover from severe illnesses and to increase the quantity of breast milk.
    - With Mori Folium (*sang ye*) for dizziness, blurred vision, tinnitus, and headache associated with Liver and Kidney yin deficiency with ascendant yang. Also for numbness, flank pain, and constipation due to blood or yin deficiency.
    - With Polygoni Multiflori Radix Preparata (*zhi he shou wu*), Cuscutae Semen (*tu si zi*), and Achyranthis Bidentata Radix (*niu xi*) for exhausted Kidneys and Liver with premature greying of the hair, dizziness, weak lower back and legs, and frequent nocturia.

- **Nourishes the blood and extinguishes wind:** For headaches, dizziness, and numbness due to blood or yin deficiency. Particularly useful for dizziness that worsens with activity.
    - With Atractylodis Macrocephalae Rhizoma (*bai zhu*) and Clematidis Radix (*wei ling xian*) for lower back and leg pain due to wind-dampness of mobile painful obstruction.
    - With Coicis Semen (*yi yi ren*) and Rehmanniae Radix (*sheng di huang*) as a tincture for mobile painful obstruction in the elderly or debilitated marked by generalized weakness and lower back and leg pain.

- **Moistens and lubricates the Intestines:** For constipation due to dry Intestines or blood deficiency.
    - With Angelicae Sinensis Radix (*dang gui*) and Platycladi Semen (*bai zi ren*) for constipation due to blood deficiency.
    - With chicken egg for constipation due to blood deficiency.

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
Contraindicated in those with diarrhea due to Spleen deficiency.

"It lubricates the Intestines—it should not be eaten by those with instability of the essential qi." (Thoroughly Revised Materia Medica)

"Forbidden when the lower base is unstable with loose stools, impotence, spermatorrhea, or vaginal discharge." (Seeking Accuracy in the Materia Medica)

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
Good quality consists of black, full seeds, uniform in size, with an intense aroma and lacking foreign matter.

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
