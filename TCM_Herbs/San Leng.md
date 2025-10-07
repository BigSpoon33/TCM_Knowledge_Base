---
# 🔹 Core Metadata (Universal Fields)
id: "herb-20251001123706"
name: "San Leng"
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
  hanzi: "三棱"
  pinyin: "Sān Léng"
  pharmaceutical: "Sparganii Rhizoma"
  english: "Sparganium Rhizome"
  alternate_names: []

  # TCM Properties
  taste: [Bitter, Acrid]
  temperature: "Neutral"
  channels: [Liver, Spleen]

  # Clinical Information
  dosage: "3-9g"
  toxicity: "The following side effects may occur during treatment: dizziness, nausea, dyspnea, and, in rare cases, fever, cyanosis, anxiety, general weakness, and temporarily elevated levels of SGPT. Severe pain may occur if injected. Overdosage and long-term administration should be avoided."
  functions: [Forcefully breaks up blood stasis, promotes the movement of qi, and alleviates pain, Dissolves accumulations]
  dui_yao: []

  # Additional Information
  constituents: [Volatile oil: formic acid ethylester, octanol, phenylethanol, 1,4-benzenediol, hexadecanoic acid, dehydrocostuslactone, 3,4-dihydro-8-hydroxy-3-methyl-1H-2-benzopyran-4-one, 1-hydroxy-2-acetyl-4-methylbenzene, δ-elemene, 2-furanmethanol, 2-acetylpyrrole, Organic acid: succinic acid, sanleng acid, decanedioic acid, 9,11-octadecadienoic acid, 9,12-octadecadienoic acid, 9-octadecenoic acid, 9-hexadecenoic acid, 19-nonadecenoic acid, 11-eicosenoic acid, benzoic acid, azelaic acid, 3-phenyl-2-propenoic acid, Other constituents: formonetin, stigmasterol, β-sitosterol, daucosterol]
  quality: "Good quality consists of heavy, solid, yellowish white rhizomes with the outer bark removed."
  text_first_appeared: "Materia Medica of the Kaibao Era"

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

Bitter, acrid, and neutral, Sparganii Rhizoma (*sān léng*) enters the Liver and Spleen channels, and also both the blood level and the qi level. Its bitter flavor drains blood stagnation, while its acrid flavor disperses qi stagnation; the herb has a strong ability to reduce stagnation and stop pain. It is used for abdominal masses, amenorrhea, and postpartum stagnation, but also promotes the movement of qi to reduce stasis due to food stagnation, which has led to distending pain in the chest and abdomen.

Materia Medica of the Kaibao Era says that it "governs stubborn lumps, abdominal masses, and clumping." The Grand Materia Medica states that it "breaks up qi and disperses clumps."

---
---

## 🔑 TCM Properties

**Taste:** `= join(this.herb_data.taste, ", ")`
**Temperature:** `= this.herb_data.temperature`
**Channels Entered:** `= join(this.herb_data.channels, ", ")`

---

## ⚡ Functions & Actions

- Forcefully breaks up blood stasis, promotes the movement of qi, and alleviates pain: for blood stasis patterns with amenorrhea, dysmenorrhea, postpartum abdominal pain, and abdominal masses.
    - With Curcumae Rhizoma (*e zhu*), Angelicae sinensis Radix (*dāng guī*), Carthami Flos (*hóng huā*), and Persicae Semen (*táo rén*) for amenorrhea, postpartum abdominal pain, and fixed abdominal masses due to blood stasis.
    - With Corydalis Rhizoma (*yán hú suǒ*) for pain due to blood stasis.
- Dissolves accumulations: for severe abdominal pain and distention due to food stagnation and stagnant qi.
    - With Aucklandiae Radix (*mù xiāng*), Arecae Semen (*bīng láng*), Citri reticulatae viride Pericarpium (*qīng pí*), and Massa medicata fermentata (*shén qū*) for pain due to food stagnation.
    - Add Codonopsis Radix (*dǎng shēn*) and Atractylodis macrocephalae Rhizoma (*bái zhú*) for the above symptoms accompanied by Spleen deficiency.

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
- Contraindicated during pregnancy or in those with excessive menstruation.
- "In all cases of early menstruation, and all disorders due to blood heat, it is forbidden." (Harm and Benefit in the Materia Medica)
- "Its nature is hard and drastic - without firm stubborn accumulation, it should not be used." (Rectification of the Meaning of Materia Medica)
- Contraindicated in the absence of stasis, and during pregnancy. Use with caution in those with weak stomachs. Should not be used long term.
- "Its use is forbidden in those with constitutional bleeding disorders." (Materia Medica of Combinations)

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
Good quality consists of heavy, solid, yellowish white rhizomes with the outer bark removed.

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
