---
# 🔹 Core Metadata (Universal Fields)
id: "herb-20251001123706"
name: "Cao Dou Kou"
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
  hanzi: "草豆蔻"
  pinyin: "cǎo dòu kòu"
  pharmaceutical: "Alpiniae Katsumadai Semen"
  english: "Katsumada's Galangal Seed"
  alternate_names: []

  # TCM Properties
  taste: [Acrid, warm, aromatic]
  temperature: "warm"
  channels: [Spleen, Stomach]

  # Clinical Information
  dosage: "3-6g. Should be added near the end of the decocting process. For best results, crush before using."
  toxicity: "N/A"
  functions: [Dries dampness, Warms the middle, Mobilizes the qi]
  dui_yao: []

  # Additional Information
  constituents: [Volatile oil: trans-cinnamaldehyde, 1,8-cineole, α-humulene, camphor, terpinen-4-ol, carvotanacetone, borneol, bornyl acetate, geraniol, geranyl acetate, methyl cinnamate, linalool, nerolidol, trans,trans-farnesol, α-pinene, α-phellandrene, p-cymene, β-carene, camphene, limonene, α-pinene, β-pinene, myrcene, dehydrocalamenene, α-muurolene, γ-patchoulene, sabinyl acetate, α-elemene, α-bergamotene, δ-bisabolene, α-cadinene, α-cedrodrene, δ-selinene, 4.7-methylene-azulene, δ-cubebene, 4.7-dimethyl-7-isopropylbicyclo-[4,4,0]-decadiene-1,4, torreyol, δ-eudesmol, farnesol, trans-cinnamylaldehyde, trans,trans-1,7-diphenyl-4,6-heptadien-3-one, (3S,5R)-3,5-dihydroxy-1,7-diphenylheptane, trans-1,7-diphenyl-5-hydroxy-1-heptene, trans,trans-1,7-diphenyl-5-hydroxy-4,6-heptadien-3-one, (3S,5S)-trans-1,7-diphenyl-3,5-dihydroxy-1-heptene, (5R)-trans-1,7-diphenyl-5-hydroxy-6-hepten-3-one, Flavonoids: quercetin, kaempferol, rhamnocitrin, kumatakenin, alpinetin, cardamonin, pinocembrin]
  quality: "Good quality consists of subspherical, uniform and unfragmented, agglutinated full seeds, with a hard and heavy texture, and an intense aroma."
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

Acrid, dispersing, and warm, qualities which enable it to unblock, the clear aroma of Alpiniae katsumadai Semen (cao dou kou) is ideal for treating constrained clumping of cold-dampness in the middle burner, which disrupts the normal ascent and descent of qi. Symptoms include epigastric and abdominal cold pain and distention, nausea, epigastric discomfort, acid reflux, and a white, slippery tongue coating. This function also allows it to treat phlegm dampness constraining the Lungs and affecting breathing, causing fullness and a stifling sensation in the chest.

Supplement to the Extension of the Materia Medica observes that this herb is warm by nature, disperses stagnant qi, and reduces phlegm above the diaphragm. If it is obvious that the body has contracted pathogenic cold, [or the patient] consumes cold substances daily, with pain in the epigastric area, then one can warmly disperse, and the response will be as certain as the sound from a beaten drum; if a disorder results from will constraint and clumping of phlegm-dampness, it will also be effective.

---
---

## 🔑 TCM Properties

**Taste:** `= join(this.herb_data.taste, ", ")`
**Temperature:** `= this.herb_data.temperature`
**Channels Entered:** `= join(this.herb_data.channels, ", ")`

---

## ⚡ Functions & Actions

Dries dampness and warms the middle: for cold-dampness of the Spleen and Stomach with fullness, distention, and pain in the epigastrium and abdomen accompanied by vomiting and diarrhea.
- With Evodiae Fructus (wu zhu yu) for abdominal pain, vomiting, reduced appetite, pale lips and tongue, and the regurgitation of clear liquids due to Stomach cold.
- With Alpiniae officinarum Rhizoma (gao liang jiang) for reduced appetite, abdominal pain, and distention due to Spleen deficiency, and the resulting dampness-induced qi stagnation and obstruction.
- With Magnoliae officinalis Cortex (hou po) for cold dampness in the middle burner when dampness predominates, as in Magnolia Bark Decoction for Warming the Middle (hou po wen zhang tang).
- With Cinnamomi Cortex (rou gui) and Myristicae Semen (rou dou kou) for chronic diarrhea due to cold from deficiency.
- With Pinelliae Rhizoma preparatum (zhi ban xia) and Citri reticulatae Pericarpium (chen pi) for cold-phlegm affecting the chest and diaphragm with vomiting.

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
Contraindicated in cases with yin or blood deficiency.

Traditional Contraindications:
Its acrid-drying accosts the blood, and those with insufficiency of yin should keep their distance. Standard contraindications are malarial disorder not due to miasmic qi, pain in the epigastrium due to fire and not cold, and explosive diarrhea involving thirst which is due to summerheat and damp-heat. (Harm and Benefit in the Materia Medica)

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
Good quality consists of subspherical, uniform and unfragmented, agglutinated full seeds, with a hard and heavy texture, and an intense aroma.

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
