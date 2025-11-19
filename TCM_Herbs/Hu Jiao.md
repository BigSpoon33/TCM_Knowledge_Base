---
# 🔹 Core Metadata (Universal Fields)
id: "herb-20251001123706"
name: "Hu Jiao / Black Pepper"
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
  hanzi: "胡椒"
  pinyin: "hú jiāo"
  pharmaceutical: "Piperis Fructus"
  english: "Pepper"
  alternate_names: []

  # TCM Properties
  taste: [Acrid, Hot]
  temperature: "Hot"
  channels: [Large Intestine, Stomach]

  # Clinical Information
  dosage: "1.5-3g in decoctions (crush before using), 0.5-1g in pills and powders"
  toxicity: "None"
  functions: [Warms the middle, Disperses cold]
  dui_yao: []

  # Additional Information
  constituents: [Volatile oil: n-tridecane, n-tridecene, n-tridecan-2-one, tridecanol, n-tridecene, n-pentadecane, n-pentadecene, β-bisabolene, α-caryophyllene, n-heptadecane, n-heptadecene, n-nonadecane, n-nonadecene, Alkaloids, amides: piperine, pipernonaline, piperundecalidine, dehydropipernonaline, N-isobutyldeca-trans-2-trans-4-dienamide, piperlonguminine, dropiperlonguminine, pipercide, guineensine, longamide, Other constituents: 3,4-dihydroxyphenylethanol glucoside, polysaccharides, fatty acids, Lignans: sesamin, asarinin, pluviatilol, fargesin, (+)-diaeudesmin, Other constituents: piperidine, tetrahydropiperic acid, piperolactam, palmitic acid, β-sitosterol, Volatile oil: piperonal, dihydrocarveol, δ-caryophyllene, caryophyllene oxide, α-pinene, β-pinene, β-pinone, sabinene, sesquisabinene, myrcene, limonene, p-cymene, cryptone, cis-p-menthenol, cis-p-2,8-menthadien-1-ol, trans-pinocarveol, 1-terpinen-5-ol, p-cymen-8-ol methylether, safrole, 1,1,4-trimethylcyclohepta-2,4-dien-6-one, Alkaloids, amides: piperine, piperanine, chavicine, pipercide, dihydropipercide, piperylin, piperettine, piperolein A, B. C, pellitorine, N-trans-feruloyltyramine, N-trans-feruloylpiperidine, feruperine, dihydroferuperine, coumaperine, N-isobutyl-2E,4E-octadecadienamide, N-isobutyl eicosa-trans-2-trans-4-dienamide]
  quality: "Good quality consists of large, full, solid and heavy, brownish black fruit spikes with an intense aroma.
- Good quality white pepper consists of large, white fruit with a strong aroma and taste. Good quality black pepper consists of large, full, black fruit with a wrinkled surface and a strong aroma and taste."
  text_first_appeared: "Tang Materia Medica"

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

*Piperis Fructus (hu jiao)* is primarily a digestive herb, as it enters the Stomach and Large Intestine channels, and is strictly focused on the elimination of pathogenic cold and disharmonies that occur as a consequence. It warms the middle, drives qi downward when cold causes vomiting of clear fluid, reduces food stagnation or phlegm that has accumulated due to cold or consumption of cold raw foods, and alleviates diarrhea due to cold in the Large Intestine. The Tang Materia Medica states that it "primarily drives qi downward, warms the middle, expels phlegm, and expels wind-cold in the midst of the organs."

Materia Medica of Diet Therapy says: "To treat wind cold in the five yin organs with cold qi [causing] epigastric and abdominal pain and vomiting of clear fluid, *Piperis Fructus (hu jiao)* wine can be taken; it can also be taken in soup."

On a cautionary note, however, Seeking Accuracy in the Materia Medica warns that it "has only the power to expel pathogenic cold, unlike the marvelous ability of *Cinnamomi Cortex (rou gui)* and *Aconiti Radix lateralis preparata (zhi fu zi)* to tonify fire and augment the primal qi. Furthermore, it mobilizes the qi and disturbs fire, so that those with yin deficiency or flimsy qi should avoid it."

---
---

## 🔑 TCM Properties

**Taste:** `= join(this.herb_data.taste, ", ")`
**Temperature:** `= this.herb_data.temperature`
**Channels Entered:** `= join(this.herb_data.channels, ", ")`

---

## ⚡ Functions & Actions

Warms the middle and disperses cold: for Stomach cold with such symptoms as vomiting, diarrhea, and abdominal pain.
    - With *Alpiniae officinarum* Rhizoma (*gao liang jiang*) for vomiting, diarrhea, and abdominal pain due to Stomach cold.
    - With *Zingiberis Rhizoma recens* (*sheng jiang*) and *Pinelliae Rhizoma preparatum* (*zhi ban xia*) for severe vomiting due to Stomach cold.

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
Contraindicated during pregnancy.
- "Acrid, warm, and depleting through dispersal, it can disturb fire in the Spleen and Lungs; excessive use makes people's eyes blurry: it should particularly not be used in food." (Grand Materia Medica)
- "Excessive consumption overly mobilizes and thus drains the true qi, causing Intestinal deficiency and tenesmus." (Extension of the Materia Medica)
Excessive consumption disturbs the fire, dries the yin fluids, depletes the qi, and injures the yin. It breaks up blood and aborts fetuses during pregnancy, brings out sores, and injures the eyes. Thus, pregnant women and those suffering from yin deficiency with internal heat, bleeding disorders, or hemorrhoid sufferers, and anyone who happens to have throat, mouth, teeth, or eye problems [at the time it might be consumed]-for all of these it is contraindicated. (Food and Drink Recipes from the Lay Buddhist Sui-Xi)

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
Good quality consists of large, full, solid and heavy, brownish black fruit spikes with an intense aroma.
- Good quality white pepper consists of large, white fruit with a strong aroma and taste. Good quality black pepper consists of large, full, black fruit with a wrinkled surface and a strong aroma and taste.

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
