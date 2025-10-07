---
# 🔹 Core Metadata (Universal Fields)
id: "herb-20251001123706"
name: "Notopterygium Root / Qiang Huo"
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
  hanzi: "羌活"
  pinyin: "Qiang Huo"
  pharmaceutical: "Notopterygii Rhizoma seu Radix"
  english: "Notopterygium Root"
  alternate_names: []

  # TCM Properties
  taste: [Acrid, Bitter, Aromatic]
  temperature: "Warm"
  channels: [Bladder, Kidney]

  # Clinical Information
  dosage: "3-9g"
  toxicity: "Allergic reactions have been reported affecting the skin and digestive system."
  functions: [Releases the exterior and disperses cold, Unblocks painful obstruction and alleviates pain, Guides qi to the greater yang channel and Governing vessel]
  dui_yao: []

  # Additional Information
  constituents: [*Notopterygium incisum*:
    - Volatile oil: α-thujene, α-pinene, δ-ocimene, γ-terpinene, limonene, α-terpinolene, terpinen-4-ol, bornyl acetate, α-copaene, trans-β-farnesene, apiol, guaiol, benzylbenzoate, methyltetradecanoate, 12-methyltetradecanoic acid methylester, methyloctadecanoate, methyl-9-octadecenoate
    - Furanocoumarines: isoimperatorin, cnidilin, notopterol, bergaptene, demethylfuropinnarin, phellopterin, bergaptoi-O-β-D-glucopyranoside, osthenol, nodakenetin, notoptol, anhydronotoptol, marmesin, columbiananin, columbianetin, 5-hydroxy-8-(1',1'-dimethylallyl)psoralen
    - Phenolic compounds: p-hydroxyphenethyl anisate, ferulic acid
    - Other constituents: 19 amino acids, phenethylferulate, rhamnose, glucose, fructose, sucrose, *Notopterygium forbesii*:
    - Volatile oil: hexanal, heptanal, sabinene, α-pinene, γ-pinene, camphene, β-pinene, myrcene, α-phellandrene, octanal, 2-carene, 3-carene, p-cymene, limonene, γ-terpinene, 4-terpinenol, terpinolene, carvol, α-terpineol, bornyl acetate, δ-selinene
    - Furanocoumarines: isoimperatorin, notopterol, cnidilin, nodakenin, nodakenetin, 6-O-(trans-feruloyl) nodakenin, bergaptoi-O-β-D-glucopyranoside
    - Phenolic compounds: p-hydroxyphenethyl anisate, ferulic acid]
  quality: "The best quality is Sichuan notopterygium (chuan qiang huo) with short internodes, forming dense annulations like a silkworm. It is also called silkworm notopterygium (can qiang). The surface should be coarse and dark brown, the roots aromatic, and a cross section will show many oily brown dots."
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

Acrid, bitter, and warm, the clear, strong aroma of Notopterygii Rhizoma seu Radix (qiang huo) has a powerful dispersing quality that can strongly raise and discharge wind, cold, or damp pathogens in the exterior.

Entering the qi level of the greater yang Bladder channel, it releases the superficial muscle layer from exterior wind-cold and cold-dampness with such symptoms as headache, stiff neck, and sore shoulders. As it enters the qi level of the Liver and Kidney channels, it vents and eases the joints and is excellent for alleviating deep pain by removing wind-dampness and wind-cold-dampness from between the sinews and bones. For these reasons it is a commonly used herb for painful obstruction, especially in the upper body.

Essentials of the Materia Medica observes that Notopterygii Rhizoma seu Radix (qiang huo) is most appropriate for Governing vessel disorders involving muscular tetany (jing). When there is damage from wind without sweating, it is called hard muscular tetany; with sweating it is called soft tetany. There is also blood deficiency tetany. In general, both Notopterygii Rhizoma seu Radix (qiang huo) and Angelicae pubescentis Radix (du huo) are appropriate for wind disorders, but are forbidden for blood deficiency tetany.

Treasury of Words on the Materia Medica explains the use of the acrid, dispersing property of Notopterygii Rhizoma seu Radix (qiang huo) for sores and boils as "using its ability to expel pus and draw out toxins, bring lesions to a head, and regenerate tissues."

---
---

## 🔑 TCM Properties

**Taste:** `= join(this.herb_data.taste, ", ")`
**Temperature:** `= this.herb_data.temperature`
**Channels Entered:** `= join(this.herb_data.channels, ", ")`

---

## ⚡ Functions & Actions

- Releases the exterior and disperses cold: for exterior cold patterns with such symptoms as chills, fever, headache, body aches and pains. Most commonly used when accompanied by dampness with joint pain, a general feeling of heaviness, sleepiness, or when there is pain in the occipital region, as in Nine-Herb Decoction with Notopterygium (jiu wei qiang huo tang).
    - With Chuanxiong Rhizoma (chuan xiong) for headache and generalized body aches associated with the common cold or painful obstruction.
    - With Saposhnikoviae Radix (fang feng) for pain due to externally-contracted wind-dampness.
- Unblocks painful obstruction and alleviates pain: for wind-cold-damp painful obstruction, especially in the upper limbs and back, as in Remove Painful Obstruction Decoction (juan bi tang).
    - With Angelicae pubescentis Radix (du huo) for wind-dampness at any level.
- Guides qi to the greater yang channel and Governing vessel: to direct other herbs in a prescription to the areas served by these two channels.

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
Contraindicated for blood-deficient painful obstruction.

Both Notopterygii Rhizoma seu Radix (qiang huo) and Angelicae pubescentis Radix (du huo) are wind herbs, important for expelling wind, dispersing cold, and eliminating dampness. Both, however, are forbidden for internal injury causing blood-deficient headache and generalized pain, resulting in chills and hot flushes, because these wind herbs can dry the blood. (Harm and Benefit in the Materia Medica)

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
The best quality is Sichuan notopterygium (chuan qiang huo) with short internodes, forming dense annulations like a silkworm. It is also called silkworm notopterygium (can qiang). The surface should be coarse and dark brown, the roots aromatic, and a cross section will show many oily brown dots.

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
