---
# 🔹 Core Metadata (Universal Fields)
id: "herb-20251001123706"
name: "Nu Zhen Zi"
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
  hanzi: "女贞子"
  pinyin: "Nu Zhen Zi"
  pharmaceutical: "Ligustri Lucidi Fructus"
  english: "Ligustrum, privet fruit"
  alternate_names: []

  # TCM Properties
  taste: [Bitter, sweet]
  temperature: "Cool"
  channels: [Kidney, Liver]

  # Clinical Information
  dosage: "9-18g"
  toxicity: "None"
  functions: [Nourishes Liver and Kidney yin, Clears heat, Brightens eyes, Blackens hair]
  dui_yao: []

  # Additional Information
  constituents: [Organic acids: oleanolic acid, acetyl oleanolic acid, 2α-hydroxyoleanolic acid, nuezhenidic acid, ursolic acid, 19α-hydroxy-3-acetylursolic acid, ligustrosidic acid, Flavonoids, glycosides: cosmosiin (apigenin-7-O-β-D-glucoside), luteolin-7-glucoside, cyanidine-3-glucoside, cyanidine-3-rutinoside, malvidin-3-rutinoside-5-glucoside, nuezhenide, neonuezhenide, acteoside, oleuropein, Volatile oil: acetaldehyde, hydrazine methyloxalate, thiopropanone, 2-ethoxypropane, 1-methyl-1-propylhydrazine, 4-acetoxy-2-butanone, 1-ethoxybutane, 2-ethoxybutane, 2,2-dimethylpentane, 3-methylhexane, ethylacetate, 2-acetyloxy-1-phenylethanone, 1-phenyl-1,2-butanediol, 1,2-diphenyl-1,2-ethanediol, Other constituents: hydroxyphenylethanol, fatty acids, phospholipides, polysaccharides, amino acids]
  quality: "Good quality consists of large, full, solid, greyish black fruit."
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

Sweet, bitter, and cooling, *Ligustri lucidi* Fructus (nu zhen zi) is a clearing and tonifying herb that is best for enriching and nourishing the Liver and Kidney yin. It does this without any cloying effect on the digestion. It is often used in the treatment of dizziness, tinnitus, blurred vision, weakness of the lower back and legs, and premature greying of the hair, as well as steaming bones and nightsweats. The Grand Materia Medica says that it "strengthens the yin, fortifies the lower back and knees, turns white hair [black], and brightens the eyes." Essentials of the Materia Medica confirms that it "augments the Liver and Kidneys, quiets the five organs, strengthens the lower back and knees, improves the hearing and vision, and blackens the hair." Thus, it tonifies as well as clears heat, with a gentle, harmonious action that makes it suitable for long-term use.

---
---

## 🔑 TCM Properties

**Taste:** `= join(this.herb_data.taste, ", ")`
**Temperature:** `= this.herb_data.temperature`
**Channels Entered:** `= join(this.herb_data.channels, ", ")`

---

## ⚡ Functions & Actions

- **Nourishes and tonifies the Liver and Kidneys:** For yin deficiency of the Liver and Kidneys with such symptoms as dizziness, spots before the eyes, soreness of the lower back, premature greying of the hair, and tinnitus.
  - With *Polygoni multiflori* Radix preparata (zhi he shou wu) and *Sesami Semen nigrum* (hei zhi ma) for premature greying of the hair.
  - With *Astragali complanati* Semen (sha yuan zi) for dizziness, tinnitus, and blurred vision due to Liver and Kidney yin deficiency.
- **Augments the Liver and Kidneys and clears heat from deficiency:** For internally-generated heat from yin deficiency.
  - With *Lycii Cortex* (di gu pi) and *Moutan Cortex* (mu dan pi) for heat from yin deficiency.
  - With *Artemisiae annuae* Herba (qing hao), *Prunellae Spica* (xia ku cao), and *Lycii Cortex* (di gu pi) for tidal fevers associated with tuberculosis.
- **Augments the Liver and Kidneys and improves the vision:** For diminished visual acuity in patients with Liver and Kidney deficiency.
  - With *Psoraleae Fructus* (bu gu zhi) and *Cuscutae Semen* (tu si zi) for dizziness, and weakness and soreness of the lower back and extremities, due to Kidney yin deficiency.
  - With *Rehmanniae Radix preparata* (shu di huang) and *Lycii Fructus* (gou qi zi) for diminished visual acuity due to Liver and Kidney deficiency.
  - With *Celosiae Semen* (qing xiang zi) and *Cassiae Semen* (jue ming zi) for red eyes from wind-heat.

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
- Contraindicated in those with diarrhea from Spleen and Stomach cold from deficiency.

Traditional Contraindications

It should be used in the midst of herbs that protect the Spleen and Stomach, and combined with warming herbs such as ginger and dates; otherwise there is a concern that it may cause abdominal pain and diarrhea. (Commentary on the Divine Husbandman's Classic of Materia Medica)

The reason for this warning is the herb's pure yin quality.

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
Good quality consists of large, full, solid, greyish black fruit.

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
