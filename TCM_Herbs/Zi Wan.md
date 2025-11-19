---
# 🔹 Core Metadata (Universal Fields)
id: "herb-20251001123706"
name: "Zi Wan"
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
  hanzi: "紫菀"
  pinyin: "zi wan"
  pharmaceutical: "Asteris Radix"
  english: "Aster root, purple aster"
  alternate_names: []

  # TCM Properties
  taste: [Acrid, bitter, slightly warm]
  temperature: "slightly warm"
  channels: [Lung]

  # Clinical Information
  dosage: "5-9g"
  toxicity: "None"
  functions: [Relieves coughs and expels phlegm, Facilitates urination]
  dui_yao: []

  # Additional Information
  constituents: [astersaponin A, astersaponin B, astersaponin C, astersaponin D, astersaponin E, astersaponin F, astersaponin G, astersaponin H, astersaponin Hb, astersaponin He, astersaponin Hd, asterprosaponin, hederasaponin, kirengeshomasaponin, shionoside A, shionoside B, asterin (=astin) A, asterin (=astin) B, asterin (=astin) C, quercetin, epifriedelinol, friedelin, shionone, L-(-)-endo-camphanol, lachnophyllol, lachnophyllol acetate, anethol, fixed oil, aromatic acids, succinic acid, cyclochlorotine]
  quality: "Good quality consists of long, purplish red, pliable, and tough roots."
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

Asteris Radix (*zi wan*) disperses because it is acrid, and drains because it is bitter. It is warming and moistening without being drying, unlike most acrid and bitter herbs. It enters the qi aspect of the Lung channel, but also its blood aspect, and thus moves qi and blood by facilitating the flow of Lung qi, while also moistening the Lungs and directing rebellious Lung qi downward, transforming phlegm, and alleviating cough.

With other appropriate herbs, Asteris Radix (*zi wan*) can be used whether the cough is exogenous or endogenous, hot or cold. It is, however, most appropriate for Lung qi obstruction following externally-contracted wind-cold, which binds up the Lung qi, leading to cough and wheezing with profuse sputum.

*Seeking Accuracy in the Materia Medica* elaborates on the characteristics of this herb:

Acrid, bitter, and warm. It is red in color, and although it enters the highest organ, it also descends and directs downward. Thus, texts record that it enters the Lung metal blood aspect—acridity enters the Lungs, red enters the blood. It is able to treat deficiency consumptive cough, childhood convulsions, nosebleed, and all other bleeding disorders. It can likewise unblock and regulate fluid metabolism—since bitterness directs downward—and thereby treat bound urination and blood in the stool. In this way, both above and below benefit. Furthermore, this herb is acrid but not drying, moistening but not obstructing—it truly benefits the Lungs. Yet its dispersing nature is strong, while its nourishing, enriching power is weak.

*Required Readings from the Medical Ancestors* adds:

Although it enters the highest [organ], its descending tendency is superb in that it makes qi transformation reach down to the Bladder, so that urination is freely facilitated. This is something that people do not know.

---
---

## 🔑 TCM Properties

**Taste:** `= join(this.herb_data.taste, ", ")`
**Temperature:** `= this.herb_data.temperature`
**Channels Entered:** `= join(this.herb_data.channels, ", ")`

---

## ⚡ Functions & Actions

- Relieves coughs and expels phlegm: an important herb in stopping coughs of various etiologies including wind-cold, wind-heat, Lung deficiency, and consumption.
  - With Farfarae Flos (*kuan dong hua*) for cough and wheezing with copious sputum and rebellious qi. This is a very common combination.
  - With Platycodi Radix (*jie geng*) and Schizonepetae Herba (*jing jie*) for clogged Lung qi with a productive cough in the aftermath of an externally-contracted disease, usually wind-cold, as in Stop Coughing Powder (*zhi sou san*).
  - With Scutellariae Radix (*huang qin*) and Fritillariae Bulbus (*bei mu*) for coughing of viscous, yellow phlegm from Lung heat.
  - With Stemonae Radix (*bai bu*) for either acute or chronic cough with blood in the sputum.
  - With Schisandrae Fructus (*wu wei zi*) for productive cough, wheezing, and spontaneous sweating.
  - With Asparagi Radix (*tian men dong*), Scutellariae Radix (*huang qin*), and Mori Cortex (*sang bai pi*) for chronic cough, especially that due to debilitating heat, which often results in coughing up blood and pus.
  - With Anemarrhenae Rhizoma (*zhi mu*) and Fritillariae Cirrhosae Bulbus (*chuan bei mu*) for chronic cough due to Lung deficiency with blood-streaked sputum.

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
- [A]n acrid, warm herb to be used only temporarily.
- If the patient is yin deficient or has heat in the Lungs, it cannot be used alone or in large amounts, and Rehmanniae Radix (*sheng di huang*) or Ophiopogonis Radix (*mai men dong*) should support it. (Required Readings from the Medical Ancestors)

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
Good quality consists of long, purplish red, pliable, and tough roots.

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
