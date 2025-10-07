---
# 🔹 Core Metadata (Universal Fields)
id: "herb-20251001123706"
name: "Gao Liang Jiang"
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
  hanzi: "高良姜"
  pinyin: "Gāo Liáng Jiāng"
  pharmaceutical: "Alpiniae Officinarum Rhizoma"
  english: "Lesser Galangal Rhizome"
  alternate_names: []

  # TCM Properties
  taste: [Acrid]
  temperature: "Warm"
  channels: [Spleen, Stomach]

  # Clinical Information
  dosage: "3-9g"
  toxicity: "None mentioned"
  functions: [Warms the middle, Alleviates pain, Disperses pathogenic cold in the Spleen and Stomach, Direct rebellious qi downward, Alleviates nausea]
  dui_yao: []

  # Additional Information
  constituents: [Volatile oil: 1,8-cineol, 4-phenylisobutanone, 3-phenylpropanal, α-pinene, δ-guaiene, α-terpineol, γ-elemene, methylcinnamate, eugenol, cadinene, Diphenylheptane derivates: curcumin, dihydrocurcumin, hexahydrocurcumin, epihexahydrocurcumin, octahydrocurcumin, 1,7-diphenylhept-4-en-3-one, 7-(4''-hydroxy-3''-methoxyphenyl)-1-phenylhept-4-en-3-one, 1,7-diphenyl-5-hydroxy-3-heptanone, dihydroyashabushi ketone, 1,7-(4''-hydroxyphenyl)-1-phenyl-4-hepten-3-one, 5-methoxy-7-(4''-hydroxyphenyl)-1-phenyl-3-heptanone, 5-methoxy-1,7-diphenyl-3-heptanone, Flavonoids: galangin, galangin-3-methylester, kaempferide, kaempferol, quercetin, isorhamnetin, quercetin-5-methylether, rhamnocitrin, 7-hydroxy-3,5-dimethoxyflavone., Triterpenes: β-sitosterol-β-D-glucoside, stigmasterol-β-D-glucoside, campesterol-β-D-glucoside, Other constituents: (6)-zingerol, benzylacetone, eualpinol]
  quality: "Good quality consists of full, reddish brown rhizomes with only a few branches and an intense aroma and acrid taste. The cultivated product is considered better quality than the wild-crafted."
  text_first_appeared: "None mentioned"

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

Acrid and very warming, Alpiniae officinarum Rhizoma (gao liang jiang) specifically disperses pathogenic cold in the Spleen and Stomach to warm the middle, stop pain, direct rebellious qi downward, and alleviate nausea. It is often used in the treatment of cold pain in the epigastrium, as well as hiccough, belching, nausea, and vomiting of clear fluids due to Stomach cold causing rebellious qi to ascend.

*The Miscellaneous Records of Famous Physicians* says that it "governs sudden cold, cold rebellion in the Stomach, and abdominal pain in sudden turmoil disorder."

*Treasury of Words on the Materia Medica* states that it "dispels cold dampness, and warms the Spleen and Stomach."

---
---

## 🔑 TCM Properties

**Taste:** `= join(this.herb_data.taste, ", ")`
**Temperature:** `= this.herb_data.temperature`
**Channels Entered:** `= join(this.herb_data.channels, ", ")`

---

## ⚡ Functions & Actions

- Warms the middle and alleviates pain: for epigastric and abdominal pain, vomiting, hiccough, or diarrhea due to cold in the middle burner.
  - With Litseae Fructus (bi cheng qie) and Zingiberis Rhizoma Preparatum (pao jiang) for Stomach cold-induced pain and vomiting.
  - Add Cinnamomi Cortex (rou gui) for cold-induced sudden turmoil disorder.
  - With Cyperi Rhizoma (xiang fu) for cold-induced epigastric pain, as in Galangal and Cyperus Pill (liang fu wan).
  - With Pinelliae Rhizoma Preparatum (zhi ban xia) and Zingiberis Rhizoma Recens (sheng jiang) for rebellious qi with vomiting of clear fluid due to Stomach cold.
  - With Codonopsis Radix (dang shen) and Poria (fu ling) for hiccough due to Stomach deficiency.
  - With Trogopterori Faeces (wu ling zhi) for epigastric pain due to cold causing stagnation of qi and blood.

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
Contraindicated in those with heat from yin deficiency.

"If nausea is due to Stomach fire, sudden turmoil disorder is due to summerheat, infestatious diarrhea (zhu xie), or pain is due to Heart deficiency - in all these cases it should be avoided." (Harm and Benefit in the Materia Medica)

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
Good quality consists of full, reddish brown rhizomes with only a few branches and an intense aroma and acrid taste. The cultivated product is considered better quality than the wild-crafted.

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
