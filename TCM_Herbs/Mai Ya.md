---
# 🔹 Core Metadata (Universal Fields)
id: "herb-20251001123706"
name: "Mai Ya"
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
  hanzi: "麥芽"
  pinyin: "mài yá"
  pharmaceutical: "Hordei Fructus Germinatus"
  english: "Barley Sprouts"
  alternate_names: []

  # TCM Properties
  taste: [Sweet]
  temperature: "Neutral"
  channels: [Liver, Spleen, Stomach]

  # Clinical Information
  dosage: "9-15g. For restraining lactation, use 30-60g."
  toxicity: "See Contraindications"
  functions: [Reduces food stagnation, softens areas of hardness, improves the appetite., Facilitates the smooth flow of Liver qi, Restrains lactation, Strengthens the Stomach]
  dui_yao: []

  # Additional Information
  constituents: [Enzymes: α-amylase, β-amylase, catalyticase, peroxidisomerase, Alkaloids: hordenine, hordatine A, B, betaine, Other constituents: cadenine, choline, cytochrome C, α-tocopheryl quinone, α-tocotrineol, saponarin, lutonarin, amino acids, proteins, phospholipids, dextrin, maltose, vitamins B, D, E]
  quality: "Good quality consists of full, pale yellow fruit with bud lets."
  text_first_appeared: "None"

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

Sweet and neutral, Hordei Fructus Germinatus (麥芽, mài yá) raises and stimulates the Stomach qi in order to digest food stagnation, particularly that associated with starches and all types of fruit. Thus it is often used in the treatment of epigastric focal distention, abdominal fullness and distention, and loss of appetite due to Spleen and Stomach deficiency with stagnation of undigested food. It is also used to soften areas of hardness, and thus treats breast distention and pain.

The Grand Materia Medica records various descriptions of the actions of Hordei Fructus Germinatus (麥芽, mài yá) found in earlier materia medica texts, after which Li Shi-Zhen adds his own observations:

[It] is salty, warm, and without toxicity; it digests food, harmonizes the Stomach (Miscellaneous Records); breaks up cold qi, expels epigastric and abdominal fullness (Materia Medica of Medicinal Properties); unbinds the Stomach, stops sudden turmoil disorder, eliminates irritable stifling sensations, reduces phlegm and thin mucus, breaks up mobile abdominal masses and clumps, promotes labor and drops the fetus (Materia Medica of Ri Hua-Zi); tonifies Spleen and Stomach deficiency, eases the Intestines and drives qi downward, used for borborygmus (Pouch of Pearls); can reduce and guide out accumulated food stagnation from rice, flour, and all fruits.

Seeking Accuracy in the Materia Medica adds that barley is sweet and warm, specifically entering the Stomach to digest food; it also has a slightly salty flavor, enabling it to soften areas of hardness. Its warmth primarily unblocks and mobilizes, and its generative emerging qi [i.e., due to its sprouting] raises the Stomach qi to assist in healthy transport. Thus, it can digest food stagnation, and treat all types of residual food stagnation and cold qi.

The use of barley sprouts as a supplemental herb to dredge Liver qi is relatively new and can be attributed to the influential early twentieth-century physician Zhang Xi-Chun, who wrote:

Its nature is good for reducing and transforming and simultaneously unblocking the two excretions [stool and urine]. While it is regarded as a herb of the Spleen and Stomach, it is actually good for dredging the Liver qi.

---
---

## 🔑 TCM Properties

**Taste:** `= join(this.herb_data.taste, ", ")`
**Temperature:** `= this.herb_data.temperature`
**Channels Entered:** `= join(this.herb_data.channels, ", ")`

---

## ⚡ Functions & Actions

- **Reduces food stagnation and strengthens the Stomach:** For poor digestion due to stagnation and accumulation of undigested starchy foods, as well as poorly digested milk in infants. Also for weak digestion and loss of appetite in cases of Spleen deficiency. This strengthening function is rather weak.
  - With Zingiberis Rhizoma (乾薑, gān jiāng) for indigestion due to Spleen and Stomach deficiency.
  - With torrifying herbs to prevent undesirable side effects such as gas and distention.
- **Restrains lactation:** For women who are discontinuing nursing, or for distended and painful breasts.
  - With Massa Medicata Fermentata (神麯, shén qū) for indigestion due to food stagnation. Also for breast tenderness and swelling associated with the discontinuation of nursing. For these disorders the herb is usually prescribed in its dry-fried form with a large dosage.
- **Facilitates the smooth flow of Liver qi:** For constrained Liver qi manifesting as a stifling sensation and distention in the epigastrium or ribs, belching, and loss of appetite. It is a supplementary herb for these functions.
  - With Artemisiae Scopariae Herba (茵陳, yīn chén) and Toosendan Fructus (川楝子, chuān liàn zǐ) for eliminating the erratic movement of constrained Liver qi, as in Sedate the Liver and Extinguish Wind Decoction (鎮肝熄風湯, zhèn gān xī fēng tāng).

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
- **Contraindications:** Contraindicated in women during lactation, except in a very low dosage (up to 9g).
- Li Shi-Zhen cautioned:
  - It will only help the digestion in those with accumulation.
  - In those without accumulation, if it is taken over a long period of time, it will reduce their primal qi: one must not be ignorant of this fact.
  - If it is to be taken over a long period of time, it must be combined with such herbs as Atractylodis Macrocephalae Rhizoma (bai zhu)-then will be no harm.
- The comments of Zhang Jie-Bin are in a similar vein:
  - In chronic illness with reduced food intake, its grain qi can be utilized to unbind the Stomach.
  - Those with primal qi deficiency should not overuse it, as it reduces Kidney [qi].
  - It also excels at promoting labor and dropping the fetus.
  - Only [with a dosage of] 60g can it reduce breast swelling.
  - When it exhausts and disperses qi and blood in this fashion, why is it used so much in every prescription for weak Spleen and Stomach with undigested food and drink?
  - Pregnant women should not overuse it.

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
Good quality consists of full, pale yellow fruit with bud lets.

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
