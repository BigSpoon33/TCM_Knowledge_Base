---
# 🔹 Core Metadata (Universal Fields)
id: "herb-20251001123706"
name: "Gua Lou Pi"
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
  hanzi: "瓜蒌皮"
  pinyin: "Gua Lou Pi"
  pharmaceutical: "Trichosanthis Pericarpium"
  english: "Trichosanthes Peel"
  alternate_names: []

  # TCM Properties
  taste: [sweet, cold]
  temperature: "cold"
  channels: [Lungs, Stomach, Large Intestine]

  # Clinical Information
  dosage: "6-12g; see COMMENTARY below for exceptions"
  toxicity: "See Trichosanthis Fructus (gua lou)."
  functions: [Clears the Lungs and transforms phlegm, Regulates the qi and expands the chest]
  dui_yao: []

  # Additional Information
  constituents: [esters of nonanoic acid, capric acid, lauric acid, myristic acid, pentadecanoic acid, palmitoleic acid, palmitic acid, linoleic acid, linolenic acid, stearic acid, acetoin, 3-methyl-1-butanol, 2,3-butanediol, 1-hexanol, benzaldehyde, 1-phenylethanone, cis-linalool oxide, trans-linalool oxide, 2,4-dimethylphenol, 1-nonanol, naphthalene, 2-methylnaphthalene, 1,5-dimethylnaphthalene, 1,1'-biphenyl, δ-elemene, geranylacetone, acenaphthylene, δ-selinene, dibenzofuran, 9H-fluorene, anthracene, phenanthrene, trichosanatine, lignoceric acid, cerotic acid, montanic acid, melissic acid, L-(-)-α-monopalmitin, 5,7-stigmastanone-3, 5,7-stigmastenol-3-D-glucopyranoside, heptacosane, nonacosane, hentriacontane, 5,7-stigmastenol, 5,7-stigmastenol-3-D-glucopyranoside, spinasterol, docosanol, tetracosanol, docosanoic acid]
  quality: "Good quality consists of dry, thick pieces of the skin with an orange outer surface and a clean white inner surface."
  text_first_appeared: "Miscellaneous Records of Famous Physicians"

  # Source References
  bensky_pdf: "627"
  bensky_page: "386"

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

Trichosanthis Pericarpium (gua lou pi) specifically mobilizes qi in order to unbind the diaphragm and ease chest discomfort, transform phlegm, and disperse clumps. Light in weight and mild in action, it is often used for cough and a stifling sensation in the chest as well as breast lumps, breast abscess, and pain. Because it cools and transforms phlegm, it also directs the turbid results of this transformation downward to be eliminated from the body. This allows the normal qi to resume its unobstructed circulation throughout the upper body, providing a rejuvenating sensation akin to the replenishment of qi in a deficient patient by the use of tonifying herbs. Despite this downward-directing action, the peel is not as effective for moistening the Intestines as the seeds, Trichosanthis Semen (gua lou ren); however, the peel can be beneficial when a patient with phlegm-heat in the chest also has loose stools.

Zhang Xi-Chun observed that "Although the power of Trichosanthis Fructus (gua lou) is slightly weak, when used in larger doses this weakness is turned to strength." A dosage of 15g is typical for Trichosanthis Pericarpium (gua lou pi), and 30g is not uncommon; when dispersing clumps, up to 60g or more can be used for a limited period of time. It should be noted that Zhang routinely used a higher than normal dosage of this herb.

Mechanisms of Selected Combinations:
>WITH TARAXACI HERBA (pu gong ying)
Trichosanthis Pericarpium (gua lou pi) can transform stagnant glue-like phlegm and release constrained heat. Taraxaci Herba (pu gong ying) is bitter, sweet, and cold, and has a relatively strong cooling and toxicity-resolving action. Because it enters the leg yang brightness and leg terminal yin channels, it is especially effective in the treatment of breast abscess. This effect is considerably enhanced when combined with Trichosanthis Pericarpium (gua lou pi), which regulates the flow of qi in the chest and disperses constrained clumps. In the early stage of breast abscess, this pair of herbs can both be taken internally and applied externally, providing an excellent cooling, releasing, reducing, and dispersing action. If the breast abscess has already formed pus, other herbs should be added which cool and expel pus, such as Platycodi Radix (jie geng), Trichosanthis Radix (tian hua fen), or Gleditsiae Spina (zao jiao ci).

>WITH TRICHOSANTHIS RADIX (tian hua fen); see page

---
---

## 🔑 TCM Properties

**Taste:** `= join(this.herb_data.taste, ", ")`
**Temperature:** `= this.herb_data.temperature`
**Channels Entered:** `= join(this.herb_data.channels, ", ")`

---

## ⚡ Functions & Actions

• Clears the Lungs and transforms phlegm: for phlegm-heat in the chest or dry cough with difficult-to-expectorate sputum and dry throat due to wind-heat.
- With Fritillariae Bulbus (bei mu), Platycodi Radix (jie geng), and Armeniacae Semen (xing ren) for phlegm-heat cough due to clogging and hindering of the Lung qi.
- With Trichosanthis Radix (tian hua fen) for a nonproductive or slightly productive cough due to injury of the Lung fluids in the aftermath of a febrile disease.
• Regulates the qi and expands the chest: for chest painful obstruction, clumping in the chest, and the early stages of breast abscess.
- With Taraxaci Herba (pu gong ying) for the early stages of breast abscess due to phlegm-heat.

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
See Trichosanthis Fructus (gua lou).

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
Good quality consists of dry, thick pieces of the skin with an orange outer surface and a clean white inner surface.

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
