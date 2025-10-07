---
# 🔹 Core Metadata (Universal Fields)
id: "herb-20251001123706"
name: "Deng Xin Cao"
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
  hanzi: "燈心草"
  pinyin: "Dēng Xīn Cǎo"
  pharmaceutical: "Juncus effusus"
  english: "Juncus Pith, Rush Pith"
  alternate_names: []

  # TCM Properties
  taste: [Sweet, Bland, Slightly cold]
  temperature: "Slightly cold"
  channels: [Heart, Lung, Small Intestine]

  # Clinical Information
  dosage: "1.5-4.5g"
  toxicity: "None noted"
  functions: [Promotes urination and unblocks painful urinary dribbling, Clears the Heart and directs fire downward]
  dui_yao: []

  # Additional Information
  constituents: [Volatile oil: α-ionone, β-ionone, β-phenylethyl alcohol, p-cresol, n-tridecan-2-one, 6,10,14-trimethylpentadecan-2-one, eugenol, dihydroactinolide, α-cyperone, δ-bisabolene, vanillin, Phenanthrene derivates: effusol, dehydroeffusol, dehydroeffusal, juncusol, juncunone, dihydrojuncunone, dihydrojuncunone methylether, isodihydrojuncunone, 2,6-dihydroxy-1,7-dimethyl-5-vinyl-9,10-dihydrophenanthrene, 2,3-dihydroxy-1,7-dimethyl-5-vinyl-9,10-dihydrophenanthrene, 2,7-dihydroxy-1,8-dimethyl-5-vinyl-9,10-dihydrophenanthrene, 2,8-dihydroxy-1,6-dimethyl-5-vinyl-9,10-dihydrophenanthrene, 8-hydroxy-2-methoxy-1,6-dimethyl-5-vinyl-9,10-dihydrophenanthrene, 2-hydroxy-7-methoxy-1,8-dimethyl-5-vinyl-9,10-dihydrophenanthrene, 8-carboxy-2-hydroxy-1-methyl-5-vinyl-9,10-dihydrophenanthrene, 5-formyl-2-hydroxy-1,8-dimethyl-7-methoxy-9,10-dihydrophenanthrene, 5-formyl-2,6-dihydroxy-1,7-dimethyl-9,10-dihydrophenanthrene, Flavonoids: luteolin, luteolin-7-glucoside, Organic acids: capric acid, lauric acid, myristic acid, stearic acid, oleic acid, linoleic acid, Amino acids: phenylalanine, norvaline, valine, methionine, tryptophan, β-alanine, glutamic acid, Other constituents: mono-p-coumaroylglyceride, α-tocopherol]
  quality: "Good quality consists of long, white, and elastic pieces of uniform thickness."
  text_first_appeared: "Materia Medica of Kaibao Era"

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

Sweet, bland, and slightly cold, Junci Medulla (deng xin cao) mobilizes the Heart and Lungs in the upper body, and the Small Intestine in the lower body. It thereby directs constrained heat in the Heart and Lungs smoothly downward through the fluid pathways of the Small Intestine to the Bladder, where it is expelled through the urine. Thus, it is often used clinically for infants or children with a restless sensation of heat in the chest, nightmares, night terrors, and dark, burning urine due to heat. It is also used for sore throat due to Lung heat.

*Transforming the Significance of Medicinal Substances* notes that the herb is mild in both flavor and aroma; lightness raises and floats, so that it especially enters the Lungs and Heart. Its nature and flavor are both bland; blandness benefits the orifices, causing constrained heat in the upper part [of the body] to travel downward and exit through the urine.

This herb can also be dipped in oil and used for cauterization.

Mechanisms of Selected Combinations
\>WITH AKEBIAE CAULIS (mu tong); see page 284

---
---

## 🔑 TCM Properties

**Taste:** `= join(this.herb_data.taste, ", ")`
**Temperature:** `= this.herb_data.temperature`
**Channels Entered:** `= join(this.herb_data.channels, ", ")`

---

## ⚡ Functions & Actions

- Promotes urination and unblocks painful urinary dribbling: for hot painful urinary dribbling or other heat disorders with dark, scanty urine.
    - With Lophatheri Herba (dan zhu ye) and Plantaginis Herba (che qian cao) for hot painful urinary dribbling.
    - With Talcum (hua shi) for irritability and incomplete, painful urination due to damp-heat in the Heart, Bladder, and Lung channels.
    - At present, used with Plantaginis Herba (che qian cao) and Imperatae Rhizoma (bai mao gen) for edema due to nephritis.
- Clears the Heart and directs fire downward: moves heat from the Heart channel downward into the Small Intestine channel where it is expelled through the urine. Commonly used in childhood sleep disorders accompanied by dark, scanty urine and irritability, especially at night. Can be used alone for this purpose. Also used in adults for insomnia or restless sleep due to lack of communication between the Heart and the Kidneys (i.e., excessive Heart fire with Kidney yin deficiency).
    - With Ziziphi spinosae Semen (suan zao ren), Poria (fu ling), and Cinnabaris (zhu sha) for irritability, insomnia, and dark, painful urination due to fire in the Heart channel.

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
"Its nature specifically unblocks and facilitates-it is not appropriate for extremely deficient people, and should not be consumed by those with cold in the middle or urinary incontinence." (*Harm and Benefit in the Materia Medica*)

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
Good quality consists of long, white, and elastic pieces of uniform thickness.

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
