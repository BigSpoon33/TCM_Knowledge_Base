---
# 🔹 Core Metadata (Universal Fields)
id: "herb-20251001123706"
name: "Bai Bian Dou (Lablab Semen Album)"
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
  hanzi: "白扁豆"
  pinyin: "Bai Bian Dou"
  pharmaceutical: "Lablab Semen Album"
  english: "Lablab, hyacinth bean"
  alternate_names: []

  # TCM Properties
  taste: [Sweet, neutral]
  temperature: "neutral"
  channels: [Spleen, Stomach]

  # Clinical Information
  dosage: "9–30g"
  toxicity: "The raw form contains toxic proteins that are denatured by heat. Must be cooked (not just powdered) before use. Symptoms of toxicity include nausea, vomiting, abdominal pain, and diarrhea. Severe cases involve a burning sensation in the stomach, panic, fear of cold, vertigo, headache, and numbness of the extremities."
  functions: [Strengthens the Spleen, Nourishes the Stomach, Transforms Dampness, Harmonizes the Middle, Clears Summerheat Accompanied by Dampness, Treats Poisoning]
  dui_yao: []

  # Additional Information
  constituents: [Fixed oil: linoleic acid, elaidic acid, stearic acid, behenic acid, palmitic acid, oleic acid, arachidic acid, Alkaloids: trigonelline, Amino acids: methionine, leucine, threonine, Sugars: stachyose, raffinose, maltose, glucose, galactose, fructose, sucrose, Other constituents: L-2-pipecolic acid, phytin, hemagglutinin A, B, pantothenic acid, proteins, carotene, vitamin B1, steroids]
  quality: "Good quality beans are big, full, white, and heavy. The best quality comes from Zhejiang and Jiangsu provinces. Inferior quality is often flat and light (e.g., Yunnan lablab bean, yun nan bian dou)."
  text_first_appeared: "Miscellaneous Records"

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

Bai Bian Dou is classified as a tonifying herb because when dry-fried or baked, it is sweet and warm, strengthening the Spleen with little cloying nature. Its aroma transforms dampness without being overly drying. It serves as an excellent mild restorative for Spleen weakness, often used when patients cannot tolerate stronger tonics.

It can also clear summerheat, especially when the pathogen leads to nausea and vomiting. For clearing summerheat, the unprepared form (sheng bian dou) is best.

---
---

## 🔑 TCM Properties

**Taste:** `= join(this.herb_data.taste, ", ")`
**Temperature:** `= this.herb_data.temperature`
**Channels Entered:** `= join(this.herb_data.channels, ", ")`

---

## ⚡ Functions & Actions

1. Strengthens the Spleen, Nourishes the Stomach, Transforms Dampness, and Harmonizes the Middle:

- For: Chronic diarrhea with loud stomach growling and reduced appetite due to Spleen deficiency. Also for vaginal discharge due to Spleen deficiency.
- Combinations for Spleen Deficiency:
    - With Dioscoreae Rhizoma (shan yao) for Spleen tonification when other tonics are not tolerated (xu bu shou bu). Often Pseudostellariae Radix (tai zi shen) is also included.
    - With Codonopsis Radix (dang shen), Atractylodis Macrocephalae Rhizoma (bai zhu), and Poria (fu ling) for Spleen deficiency with significant dampness (refer to [[Shen Ling Bai Zhu San]]).
    - With Pseudostellariae Radix (tai zi shen) and Setariae Fructus Germinatus (gu ya) for loss of appetite after prolonged illness.
    - With Atractylodis Macrocephalae Rhizoma (bai zhu), Amomi Fructus (sha ren), and Gigeriae Galli Endothelium Corneum (ji nei jin) for lack of appetite in children from Spleen deficiency and stagnation due to dampness.
- Combinations for Vaginal Discharge:
    - With Atractylodis Rhizoma (cang zhu), Euryales Semen (qian shi), and Sepiae Endoconcha (hai piao xiao).

2. Clears Summerheat Accompanied by Dampness:

- For: Summerheat patterns, especially those with pronounced diarrhea or vomiting.
- Combinations:
    - With Moslae Herba (xiang ru) and Magnoliae Officinalis Cortex (hou po) for sudden turmoil disorder (refer to [[Xiang Ru San]]).
    - With Lophatheri Herba (dan zhu ye), Gypsum Fibrosum (shi gao), and Artemisiae Annuae Herba (qing hao) for unremitting summer feverishness in children.

3. Treats Poisoning:

- For: A variety of food-related poisoning, including that from spoiled food.
- Combinations:
    - With Phragmitis Rhizoma (lu gen) for puffer fish toxicity.
    - With Amomi Fructus Rotundus (bai dou kou) and Puerariae Flos (ge hua) for hangovers.

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
- Should only be used when the Spleen is oppressed by dampness, and there is no abdominal pain or stifling sensation due to constraint.
- Avoid if a malarial pathogen is not completely eliminated, or if a fever due to an externally contracted cold pathogen has just flared, as excessive consumption clogs the qi.
- Not contraindicated for chills and fever due to Spleen and Stomach deficiency from food injury or exhaustion.

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
Good quality beans are big, full, white, and heavy. The best quality comes from Zhejiang and Jiangsu provinces. Inferior quality is often flat and light (e.g., Yunnan lablab bean, yun nan bian dou).

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
