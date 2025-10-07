---
# 🔹 Core Metadata (Universal Fields)
id: "herb-20251001123706"
name: "Ce Bai Ye"
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
  hanzi: "侧柏叶"
  pinyin: "Ce Bai Ye"
  pharmaceutical: "Platycladi Cacumen"
  english: "Oriental arborvitae leafy twig, arborvitae, Chinese arborvitae biota"
  alternate_names: []

  # TCM Properties
  taste: [Bitter, astringent]
  temperature: "slightly cold"
  channels: [Lung, Liver, Large Intestine]

  # Clinical Information
  dosage: "6-15g"
  toxicity: "Toxic overdosage or long-term use may cause gastric discomfort and other gastrointestinal symptoms such as reduced appetite. In severe cases, vomiting of blood may occur. The toxic ingredient is thujone, found in the volatile oil. Processing reduces its content, and thus the toxicity of this herb. Allergic reactions have also been reported in individual cases, with such symptoms as allergic rashes, edema of the eyelids, face, or lower extremities. These reactions normally disappear spontaneously once use of the herb is discontinued."
  functions: [Cools the blood and stops bleeding, Stops cough and expels phlegm, Promotes healing of burns]
  dui_yao: []

  # Additional Information
  constituents: [Volatile oil: thujene, α-thujone, fenchone, pinene, caryophyllene, Flavonoids: cupressuflavone, aromadendrine, apigenin, quercitrin, kaempferol-7-O-glucoside, quercetin-7-O-rhamnoside, myricetin, myricetin-3-O-α-L-rhamnoside, hinokiflavone, amentoflavone, Organic acids: palmitic acid, stearic acid, lauric acid, myristic acid, oleic acid, linoleic acid, capric acid, Other constituents: 10-nonacosanol, deoxypodophyllotoxin, isopimaric acid, β-sitosterol, tannins]
  quality: "Good quality consists of tender, dark green twigs."
  text_first_appeared: "Miscellaneous Records of Famous Physicians"

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

Bitter, astringent, slightly cold, Platycladi Cacumen (ce bai ye) enters the Liver, Lung, and Large Intestine channels. Bitterness dries dampness, astringency inhibits and restrains, and its slight coldness cools what is hot; thus, this herb cools the blood and inhibits bleeding. It also promotes hair growth and dries dampness to stop vaginal discharge. It can be used when heat in the blood leads to the coughing or expectoration of blood, blood in the stool or urine, and for irregular uterine bleeding. It cools the Lungs and expels phlegm, and applied topically can assist in the healing of burns, and promote the regrowth of hair in cases of balding, for which it is also taken internally.

Miscellaneous Records of Famous Physicians states that this herb "governs the vomiting of blood, nosebleed, bleeding dysenteric disorder, continuous vaginal bleeding and vaginal discharge; expels damp painful obstruction and generates flesh."

---
---

## 🔑 TCM Properties

**Taste:** `= join(this.herb_data.taste, ", ")`
**Temperature:** `= this.herb_data.temperature`
**Channels Entered:** `= join(this.herb_data.channels, ", ")`

---

## ⚡ Functions & Actions

Cools the blood and stops bleeding: Widely used for various bleeding disorders including vomiting blood, bleeding gums, coughing of blood, blood in the stool or urine, bloody dysenteric disorder, and uterine bleeding. Owing to its slightly cold nature, this herb is effectively used in treating patterns of hot blood, but it may also be used with warming herbs for bleeding associated with cold patterns.
    - With Rehmanniae Radix (sheng di huang) for many forms of hemorrhage resulting from the chaotic movement of hot blood.
    - With Cirsii Herba (xiao ji) and Cirsii japonici Herba sive Radix (da ji) for nosebleed with bright red blood due to heat forcing the blood upward. Can also be used for blood in the urine.
    - With Artemisiae argyi Folium (ai ye) and Zingiberis Rhizoma (gan jiang) for bleeding associated with cold from deficiency, as in Oriental Arborvitae Leafy Twig Decoction (bai ye tang).
    - With Typhae Pollen (pu huang) for excessive uterine bleeding due to heat.
    - With Codonopsis Radix (dang shen) and Angelicae sinensis Radix (dang gui) for excessive uterine bleeding with manifestations of both qi and blood deficiency.
- Stops cough and expels phlegm: For Lung heat patterns with cough and accumulation of phlegm. Especially important in cases of viscous, difficult-to-expectorate sputum streaked with blood.
    - With Jujubae Fructus (da zao) for chronic hot cough, especially of the dry, nonproductive variety.
- Promotes healing of burns: Used topically in powdered form for the early stages of burns over a small to moderate surface area. Also used for hair loss.

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
Must be combined with appropriate herbs for bleeding with deficiency.
Cold and drying by nature, [Platycladi Cacumen (ce bai ye)] greatly cuts down Stomach [qi]; although it can stop bleeding, it has no power to generate yang, therefore deficient patients who have lost blood should not take it without prescription.

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
Good quality consists of tender, dark green twigs.

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
