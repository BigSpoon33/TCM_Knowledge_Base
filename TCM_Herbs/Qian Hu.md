---
# 🔹 Core Metadata (Universal Fields)
id: "herb-20251001123706"
name: "Qian Hu"
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
  hanzi: "前胡"
  pinyin: "Qián Hú"
  pharmaceutical: "Peucedani Radix"
  english: "Peucedanum Root"
  alternate_names: []

  # TCM Properties
  taste: [Bitter, Acrid]
  temperature: "Slightly cold"
  channels: [Lung]

  # Clinical Information
  dosage: "3-9g"
  toxicity: "N/A"
  functions: [Directs qi downward, Dispels phlegm, Disperses and scatters wind-heat]
  dui_yao: []

  # Additional Information
  constituents: [7,8-Pyranocoumarins: (±)-praeruptorin A (Pd-Ia), (±)-praeruptorin B (Pd II), (+)-praeruptorin C, D, E, Pd-Ib, praeroside II, III, IV, V, peucedanocoumarin I, II, III, qianhucoumarin A, B, C, D, E, pteryxin, 6,7-Furanocoumarins: praeroside I, isorutarin, rutarin, marmesinin, nodakenin, nodaketenin, psoralen, 5-methoxypsoralen, 8-methoxypsoralen, Simple coumarins: (-)-peucedanol, scopolin, scopoletin, skimmin, apiosylskimmin, umbelliferone, Triterpenes: Pd-saponin V (3-O-α-L-arabinopyranosyl-hederagenin-28-O-β-gentiobioside, β-sitosterol, daucosterol, Volatile oil: 1,3,3-trimethyltricyclo[2.2.1.0.2,6]heptane, 4(10)-thujene, 1-(1,5-bimethyl-4-hexenyl)-4-methylbenzene, aromadendrene, β-elemene, 6,7-Pyranocoumarins: Pd-C-I (3'(S)-senecioyloxy-4'-(R)-hydroxy-3',4'-dihydroxanthyletin), Pd-C-II, Pd-C-III, Pd-C-IV, Pd-C-V, AD-I, decursin, decursidin, 6,7-Furanocoumarins: nodakenin, nodaketenin, decuroside I, II, III, IV, V, bergapten, Simple coumarins: umbelliprenin, Triterpenes: Pd-saponin I, II, III, IV, V (sapogenin: hederagenin), Volatile oil: estragole, limonene, m-cymene, 4(10)-thujene, p-tert-butylanethole]
  quality: "Good quality consists of thick, soft roots with a yellowish-white cross section and an intense aroma. If the roots are sliced, the center looks like a drawing of a chrysanthemum flower. Poor quality has a dark, withered, hollow center."
  text_first_appeared: "N/A"

  # Source References
  bensky_pdf: "627"
  bensky_page: "N/A"

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

The bitter nature of Peucedani Radix (qian hu) facilitates the downward direction of qi, while its acrid flavor helps it spread and disseminate. Thus, while it drains Lung heat by eliminating phlegm and directing qi downward, it also expels externally-contracted pathogens by assisting in the spreading of the Lung qi. It is therefore most appropriate in treating the cough, headache, and constrained Lung heat that results from externally-contracted pathogenic wind-heat, or the cough and wheezing with thick sputum that results from Lung qi failing to properly descend. When these two co-exist—thick phlegm and externally contracted heat—Peucedani Radix (qian hu) is especially indicated. Many texts warn, however, that it should not be used for externally-contracted disorders in the absence of phlegm accumulation.

The *Grand Materia Medica* observes: "The merit of Peucedani Radix (qian hu) lies primarily in directing qi downward, for when qi descends then fire will descend, and phlegm will also descend. Peucedani Radix (qian hu) can be credited with driving out the old to bring forth the new, and is a valued herb for the treatment of qi and phlegm."

The expression "driving out the old to bring forth the new" in descriptions of this herb appears in many textbooks of materia medica. It refers to the restoration of normal qi that results when obstructing phlegm is eliminated. There is also a somewhat greater emphasis in the ancient literature, compared to more recent textbooks, on its ability to disperse epigastric clumped qi and enhance digestive function, for example, in the treatment of childhood nutritional impairment. Several works also mention that it enters the Liver and Gall Bladder; *Essentials of the Materia Medica* goes so far as to say that "Wind-phlegm in the Liver and Gall Bladder channels cannot be expelled without [the use of] Peucedani Radix (qian hu)."

---
---

## 🔑 TCM Properties

**Taste:** `= join(this.herb_data.taste, ", ")`
**Temperature:** `= this.herb_data.temperature`
**Channels Entered:** `= join(this.herb_data.channels, ", ")`

---

## ⚡ Functions & Actions

- Directs qi downward and dispels phlegm: for cough or wheezing with thick sputum due to turbid clogging of the Lungs.
    - With Mori Cortex (sang bai pi), Armeniacae Semen (xing ren), and Fritillariae Bulbus (bei mu) for Lung heat with coughing of thick sputum, stifling sensation in the chest, and irritability.
    - With Cynanchi stauntonii Rhizoma (bai qian) for cough due to a disturbance in the normal functioning of the Lungs from an externally-contracted disease.
- Disperses and scatters wind-heat: for the exterior patterns of externally-contracted wind-heat with headache and cough. Most suitable when wind-heat constrains the Lungs.
    - With Bupleuri Radix (chai hu) for wind-heat constraining the Lungs leading to a stifling sensation in the chest and cough with profuse sputum.
    - With Platycodi Radix (jie geng), Arctii Fructus (niu bang zi), and Menthae haplocalycis Herba (bo he) for headache, fever, nasal congestion, runny nose, and cough associated with externally-contracted wind-heat.

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
As a bitter, draining, and dispersing herb, it should not be used for cough due to fire from yin deficiency, or cough and wheezing associated with cold, thin mucus.

According to some traditional sources, this herb counteracts Veratri nigri Radix et Rhizoma (li lu).

*Encountering the Sources of the Classic of Materia Medica* notes that the herb is indicated for "wind-phlegm with excess qi; it is forbidden for phlegm which is disturbed by fire from yin deficiency, or for patients with audible phlegm that does not result from an externally-contracted disorder."

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
Good quality consists of thick, soft roots with a yellowish-white cross section and an intense aroma. If the roots are sliced, the center looks like a drawing of a chrysanthemum flower. Poor quality has a dark, withered, hollow center.

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
