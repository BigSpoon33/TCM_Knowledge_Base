---
# 🔹 Core Metadata (Universal Fields)
id: "herb-20251001123706"
name: "Gou Ji"
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
  hanzi: "狗脊"
  pinyin: "gǒu jí"
  pharmaceutical: "Cibotii Rhizoma"
  english: "Cibotium rhizome, chain fern"
  alternate_names: []

  # TCM Properties
  taste: [Bitter, sweet]
  temperature: "Warm"
  channels: [Kidney, Liver]

  # Clinical Information
  dosage: "9-15g"
  toxicity: "no specific toxicity mentioned"
  functions: [Tonifies the Liver and Kidneys, Strengthens the sinews and bones, Expels pathogenic wind, dampness, and cold, Warms and stabilizes the Kidneys]
  dui_yao: []

  # Additional Information
  constituents: [pterosin R, pterosin Z, onitin, onitin-2--0-B-D-glucoside, onitin-2'-0-B-D-alloside, ptaquiloside, vanillin, syringic aldehyde, p-hydroxybenzaldehyde, acetovanillone]
  quality: "For whole dried rhizomes, good quality consists of long, hard, and solid rhizomes, densely covered with golden yellow hairs. In its unprepared form, good quality is light brown, thin, and brittle with a powdery texture. Good quality cooked slices are hard and solid, and very dark brown."
  text_first_appeared: "The Divine Husbandman's Classic of Materia Medica"

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

Bitter, sweet, and slightly warm, Cibotii Rhizoma (gou ji) enters the Liver and Kidney channels. Being sweet, it tonifies and augments these organs; being bitter, it dries dampness, while its warmth unblocks and promotes movement. It is an herb that both tonifies and encourages movement at the level of the sinews and bones. It tonifies the Liver and Kidneys, fortifies the lower back and knees, strengthens the sinews and bones, and treats painful obstruction disorders by expelling cold, wind, and dampness.

The Divine Husbandman's Classic of Materia Medica describes its characteristics:

Its flavor is bitter and neutral, without being toxic; it governs stiffness in the upper and lower back, the degree of tension in the articulations, generalized painful obstruction disorder with cold-damp pain in the knees; and greatly benefits the elderly.

Encountering the Sources of the Classic of Materia Medica explains: "'Greatly benefits the elderly' [means that it] tonifies and augments the Kidney qi to fortify the sinews and strengthen the bones."

One Hundred Annotations to the Divine Husbandman's Classic of Materia Medica contains some interesting remarks on the relationship between the appearance of the herb and its therapeutic nature:

[This herb] grows [what looks like] body hair over, and all has many backbone[-like ridges]. It very much resembles the spine of a dog. Of the animals, the dog is the most cunning and agile, and this herb resembles it. Thus it can enter deep into the sinews, bones, and articulations, expel their congealed and stagnant cold-damp qi, and restore their health and strength, ease of movement, and agility. The shape [of the herb] is the same [as a dog's spine] and the nature is quite close as well.

---
---

## 🔑 TCM Properties

**Taste:** `= join(this.herb_data.taste, ", ")`
**Temperature:** `= this.herb_data.temperature`
**Channels Entered:** `= join(this.herb_data.channels, ", ")`

---

## ⚡ Functions & Actions

- **Tonifies the Liver and Kidneys and strengthens the sinews and bones:** for Liver and Kidney deficiency with such symptoms as stiffness, soreness, or weakness in the lower back, spine, and lower extremities.
    - With Eucommiae Cortex (杜仲 dù zhòng) and Achyranthis bidentatae Radix (牛膝 niú xī) for pain, stiffness, and motor impairment of the lower back, as well as weakness of the legs from Liver and Kidney deficiency.
    - With Angelicae sinensis Radix (当归 dāng guī) for swelling in the lower extremities as an aftermath of a long-term disease.
    - With Cuscutae Semen (菟丝子 tù sī zi) for lower back pain associated with Kidney disorders.
- **Expels wind and dampness:** for wind-damp painful obstruction with pain, soreness, or numbness. Especially useful in patients with wind-cold-dampness who have an underlying deficiency of the Liver and Kidneys.
    - With Cinnamomi Ramulus (桂枝 guì zhī) and Gentianae macrophyllae Radix (秦艽 qín jiāo) for painful obstruction in the lower back from wind and dampness.
- **Warms and stabilizes the Kidneys:** for incontinence of urine and vaginal discharge due to Kidney yang deficiency.
    - With Chaenomelis Fructus (木瓜 mù guā) and Eleutherococci gracilistyli Cortex (五加皮 wǔ jiā pí) for lower back pain and urinary frequency.
    - With Cervi Cornu pantotrichum (鹿茸 lù róng) and Artemisiae argyi Folium (艾叶 ài yè) for vaginal discharge associated with cold from deficiency of the Conception and Penetrating channels.

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
- Contraindicated in those with urinary difficulty or heat from yin deficiency.
- According to some traditional sources, this herb antagonizes Patriniae Herba (败酱草 bài jiàng cǎo).
- Its nature is warm and drying, so it is contraindicated for Kidney deficiency with heat and urinary difficulty that may be dark reddish yellow, scanty, and uncomfortable to pass, with a bitter taste in the mouth and a dry tongue. (Harm and Benefit in the Materia Medica)
- "Avoid its use in Liver deficiency with fire from constraint." (Treasury of Words on the Materia Medica)

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
For whole dried rhizomes, good quality consists of long, hard, and solid rhizomes, densely covered with golden yellow hairs. In its unprepared form, good quality is light brown, thin, and brittle with a powdery texture. Good quality cooked slices are hard and solid, and very dark brown.

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
