---
# 🔹 Core Metadata (Universal Fields)
id: "herb-20251001123706"
name: "Ku Shen"
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
  hanzi: "苦参"
  pinyin: "Kǔ Shēn"
  pharmaceutical: "Sophorae Flavescentis Radix"
  english: "Sophora Root"
  alternate_names: []

  # TCM Properties
  taste: [extremely bitter]
  temperature: "cold"
  channels: [Bladder, Heart, Liver, Large Intestine, Stomach, Small Intestine]

  # Clinical Information
  dosage: "3-9g"
  toxicity: "The following side effects may occasionally occur: mild dizziness, nausea, vomiting, and constipation. These symptoms usually disappear spontaneously. In severe cases of overdosage the following symptoms have been reported: spasms, disturbance of speech, irregular breathing, respiratory failure and death. Allergic reactions have also been reported, primarily of maculopapular rashes."
  functions: [Clears heat and dries dampness, Disperses wind, kills parasites, and stops itching, Clears heat and promotes urination]
  dui_yao: []

  # Additional Information
  constituents: [Alkaloids: matrine, sophoridine, isomatrine, 7,11-dehydromatrine, sophocarpine, isosophocarpine, sophoramine, 6-dehydrosophoramine, sophoranol, 9a-hydroxysophoramine, 5a,9a-dihydroxymatrine, oxymatrine, N-methylcytisine, anagyrine, baptifoline, lupanine, mamanine, kuraramine, isokuraramine, Flavonoids: kushenol A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, methylkushenol C, isokurarinone, kurarinol, neokurarinol, norkurarinol, formononetin, kuraridinol, kushenin, 1-maackiain, trifolirhizin, xanthohumol, isoxanthohumol, luteolin-7-glucoside, Triterpenesaponines: sophoraflavoside I, II, III, IV, soyasaponin I, Other constituents: kushequinone A]
  quality: "Good quality consists of a uniform root with a yellowish white cross section and an extremely bitter taste."
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

Very bitter and very cold, with a descending nature, Sophorae Flavescentis Radix (ku shen) expels wind, stops itching, and promotes urination. It is particularly indicated for lower burner damp-heat, and damp-heat itching of the skin, but it also treats hot dysenteric disorder, for which it is a major constituent in several traditional formulas. Its ability to promote urination is used primarily when accumulated damp-heat clumps and disrupts the qi separation function of the Bladder; in such cases it leads the damp heat pathogen downward and out of the body through the urine. This is also a very effective strategy for clearing local dampness in cases of vaginal discharge.

Treasury of Words on the Materia Medica elaborates:

"Sophorae Flavescentis Radix (ku shen) expels wind and drains fire, dries dampness, and expels parasites. Earlier writers claimed that it tonifies the Kidneys and tonifies the yin, but this theory is grossly mistaken."

Zhang Shan-Lei, however, explained the basis for attributing tonifying qualities to Sophorae Flavescentis Radix (ku shen):

When they said that it 'tonifies the middle, nourishes the Liver and Gallbladder qi, calms the five yin organs, settles the mind, augments essence, facilitates the nine orifices, expels lurking heat, pacifies the Stomach qi, makes people desire food' and similar actions, all are due to damp-heat, which, once cleared, allows the normal qi to flourish!

---
---

## 🔑 TCM Properties

**Taste:** `= join(this.herb_data.taste, ", ")`
**Temperature:** `= this.herb_data.temperature`
**Channels Entered:** `= join(this.herb_data.channels, ", ")`

---

## ⚡ Functions & Actions

-   **Clears heat and dries dampness:** primarily for damp-heat in the lower burner leading to jaundice, dysenteric disorder, vaginal discharge, and sores.
    -   With Aucklandiae Radix (mu xiang) for damp-heat dysenteric disorder or jaundice.
    -   With Phellodendri Cortex (huang bai), Angelicae Dahuricae Radix (bai zhi), and Cnidii Fructus (she chuang zi) for thick yellow vaginal discharge with itching.
    -   With Cnidii Fructus (she chuang zi) and Salviae Miltiorrhizae Radix (dan shen) for damp skin lesions such as eczema.
    -   With Sophorae Flos (huai hua) and Sanguisorbae Radix (di yu) for blood in the stool from Intestinal heat, bleeding hemorrhoids, or vomiting of blood from Stomach heat.
-   **Disperses wind, kills parasites, and stops itching:** for damp toxin skin lesions or infestations with chronic itching, seepage, and bleeding. Also for genital itching and vaginal discharge. Used both internally and topically.
    -   With Cicadae Periostracum (chan tui) and Schizonepetae Herba (jing jie) for generalized itching, as in Eliminate Wind Powder (xiao feng san).
-   **Clears heat and promotes urination:** for such disorders as damp-heat in the Small Intestine, painful urinary dribbling, and hot edema.
    -   With Pyrrosiae Folium (shi wei) and Plantaginis Semen (che qian zi) for urinary dysfunction with burning, rough, and painful urination due to damp-heat.
    -   With Angelicae Sinensis Radix (dang gui) and Fritillariae Bulbus (bei mu) for urinary dysfunction during pregnancy.

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
Contraindicated in cases of cold from deficiency of the Spleen or Stomach. It should not be combined with Veratri nigri Radix et Rhizoma (li lu). See Toxicity below.

cautions: Rectification of the Meaning of Materia Medica

"All herbs which are very bitter and very cold are inevitably very drying in nature, and excessive use cannot but injure the Spleen or deplete the Kidneys." It notes that Shen Cun-Zhong recorded that he had used Sophorae Flavescentis Radix for many years as a toothpaste (ku shen) for his dental problems, but soon suffered from disabling lower backache. His friend also used Sophorae Flavescentis Radix (ku shen) in the same way, and likewise suffered from backache. Both gave up this practice, and their backaches thereupon ceased. "This, then, is a clear sign that Sophorae Flavescentis Radix (ku shen) damages the Kidneys!" Zhu Dan-Xi, however, rejected this conclusion: "If the lower back feels heavy when using Sophorae Flavescentis Radix (ku shen), this is because its qi directs downward and does not raise, not because it injures the Kidneys!"

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
Good quality consists of a uniform root with a yellowish white cross section and an extremely bitter taste.

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
