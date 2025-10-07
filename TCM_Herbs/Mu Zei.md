---
# 🔹 Core Metadata (Universal Fields)
id: "herb-20251001123706"
name: "Equisetum/Mu Zei"
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
  hanzi: "木賊"
  pinyin: "Mù Zéi"
  pharmaceutical: "Equiseti Hiemalis Herba"
  english: "equisetum, scouring rush, shave grass"
  alternate_names: []

  # TCM Properties
  taste: [Sweet, bitter, neutral]
  temperature: "neutral"
  channels: [Liver, Lung, Gallbladder]

  # Clinical Information
  dosage: "3-9g"
  toxicity: "None"
  functions: [Disperses wind-heat, clears the eyes, and reduces superficial visual obstruction, Clears heat and stops bleeding]
  dui_yao: []

  # Additional Information
  constituents: [Organic acids and esters: succinic acid, fumaric acid, ferulic acid, 4-hydroxybenzoic acid, 3-hydroxybenzoic acid, vanillic acid, caffeic acid, 3-methoxycinnamic acid, 4-methoxycinnamic acid, glutaric acid methylester, Flavonoids: kaempferol-3,7-diglucoside, kaempferol-3-diglucoside-7-glucoside, kaempferol-3-glucoside-7-diglucoside, gossypitrin, herbacetrin, Alkaloids: palustrin, nicotine, Other constituents: thymine, dimethyl sulfone, vanillin, 4-hydroxybenzaldehyde, sugars, tannins, saponins]
  quality: "Good quality has long, thick, green, and thick-walled stems which do not come apart at the nodes."
  text_first_appeared: "Materia Medica of the Jiayou Era"

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

This herb is good for treating red eyes, excessive tearing, and superficial visual obstruction resulting from wind-heat or Liver and Gallbladder channel fire. It does have a mild sweat-inducing action but is rarely used in exterior-releasing formulas unless there is an associated eye disorder.

In Rectification of the Meaning of Materia Medica, Zhang Shan-Lei observed:

*Equiseti hiemalis Herba* treats all diseases of the Liver and Gallbladder wood from turbulently rebellious pathogens. It can eliminate superficial visual obstruction and break up accumulated stagnation, both of which actions involve the grinding down of pathogenic excess. Thus, it is an important ophthalmological herb: not only can it be used to subdue wood and grind down superficial visual obstruction, it also has the ability to dredge wind, and drain and transform damp-heat, as well as to raise up in order to disperse constrained fire.

Seeking Accuracy in the Materia Medica emphasizes the herb's effect on wind-heat:

Similarly, other symptoms such as pain from bulging disorder, prolapsed rectum, bleeding hemorrhoids from Intestinal wind, blood in the stool and gynecological bleeding will all respond - as long as the cause is found to be wind-heat. The pain will stop, the rectum retract, the Intestines will be stabilized, and the bleeding will cease, without any symptom remaining - as long as the cause is wind-heat.

Li Shi-Zhen, however, notes in the Grand Materia Medica that it also releases the muscle layer and expels wind-dampness.

---
---

## 🔑 TCM Properties

**Taste:** `= join(this.herb_data.taste, ", ")`
**Temperature:** `= this.herb_data.temperature`
**Channels Entered:** `= join(this.herb_data.channels, ", ")`

---

## ⚡ Functions & Actions

- **Disperses wind-heat, clears the eyes, and reduces superficial visual obstruction:** for wind-heat affecting the eyes and causing redness, pain, swelling, cloudiness, blurred vision, pterygium, or excessive tearing.
    -   With Chrysanthemi Flos (*ju hua*) for swelling, pain, and redness of the eyes, and pterygium.
    -   With Atractylodis Rhizoma (*cang zhu*) for blurred vision and excessive tearing.
    -   With Tribuli Fructus (*ci ji li*) for hives and itching, pterygium, and excessive tearing.
-   With Chrysanthemi Flos (*ju hua*) for swelling, pain, and redness of the eyes, and pterygium.
-   With Eriocauli Flos (*gu jing cao*) and Haliotidis Concha (*shi jue ming*) for red eyes.
-   **Clears heat and stops bleeding:** as an auxiliary herb for blood in the stool or hemorrhoids.
    -   With Sophorae Fructus (*huai jiao*) and Sanguisorbae Radix (*di yu*) for bleeding hemorrhoids or blood in the stool due to heat in the blood.

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
Use with caution in cases of urinary frequency, depleted fluids, qi deficiency, and during pregnancy.

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
Good quality has long, thick, green, and thick-walled stems which do not come apart at the nodes.

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
