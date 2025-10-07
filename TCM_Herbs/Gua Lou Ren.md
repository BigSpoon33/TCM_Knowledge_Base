---
# 🔹 Core Metadata (Universal Fields)
id: "herb-20251001123706"
name: "Gua Lou Ren"
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
  hanzi: "瓜蒌仁"
  pinyin: "gua lou ren"
  pharmaceutical: "Trichosanthis Semen"
  english: "Trichosanthes seed"
  alternate_names: []

  # TCM Properties
  taste: [Sweet, Slippery, moistens both the Lungs and Intestines, cools and transforms phlegm]
  temperature: "Cold"
  channels: [Lung, Stomach, Large Intestine]

  # Clinical Information
  dosage: "9-15g"
  toxicity: "None"
  functions: []
  dui_yao: []

  # Additional Information
  constituents: [Fixed oil: trichosanic acid is the main component, Sterols: campesterol, 7-campesterol, sitosterol, α-spinasterol, γ-stigmasterol, 5,25-stigmastadienol, 7,24-stigmastadienol, 7,25-stigmastadienol, stigmastanol, 7,22,25-stigmastatrienol, Triterpenes: karounidiol, karounidiol benzoate, Amino acids: glutamic acid, arginine, aspartic acid, leucine, Proteins: trichokirin, Other constituents: 11-methoxynoryangonin, vanillic acid, triticin]
  quality: "Good quality consists of large, full, oily seeds without a greasy surface."
  text_first_appeared: "Collection of Commentaries on the Classics of the Materia Medica"

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

In addition to moistening the Intestines, *Trichosanthis Semen* (*gua lou ren*) also moistens phlegm in the Lungs and thereby loosens it so that it can be coughed up. By cooling upper burner fire, it protects and generates the yang fluids and alleviates thirst. Zhu Dan-Xi described it as a "sage-like herb for wasting and thirsting disorder."

Transforming the Significance of Medicinal Substances notes that long-term, stubborn, constrained phlegm retained internally can obstruct the ascent and descent of qi, causing a stifling sensation in the chest, cough, insatiable thirst (due to impaired fluid transport), and the sound of phlegm in the throat, where the phlegm itself is difficult to expectorate. According to this source, *Trichosanthis Semen* (*gua lou ren*) is selected to utilize its slippery moistening power to scour foul grease from the diaphragmatic area. Phlegm will then be reduced and qi will descend, the chest will feel free and coughs will ease, thirst will be alleviated and fluids will be produced- all symptoms will be relieved. Its oil is exceedingly capable of moistening the Lungs and lubricating the Intestines. If pathogenic fire dries and clumps in the Large Intestine, use it to assist bitter, cold herbs, then the Intestine will naturally unblock and move freely.

Some also feel that the slippery nature of this herb can benefit other orifices, such as the urethra, and therefore advocate its use to promote urination. Similarly, Li Shi Zhen recorded a formula using the dry powder of dry-fried *Trichosanthis Semen* (*chao gua lou ren*) to promote lactation, 3g of which are to be taken internally with warm wine.

---
---

## 🔑 TCM Properties

**Taste:** `= join(this.herb_data.taste, ", ")`
**Temperature:** `= this.herb_data.temperature`
**Channels Entered:** `= join(this.herb_data.channels, ", ")`

---

## ⚡ Functions & Actions

Clears and transforms phlegm-heat: for phlegm-heat cough. Both cools and moistens. Especially useful for cough with chest pain and thick, difficult-to-expectorate sputum.
With *Pinelliae Rhizoma preparatum* (*zhi ban xia*) and *Coptidis Rhizoma* (*huang lian*) for cough accompanied by chest pain and sputum that is difficult to expectorate.
Add *Bupleuri Radix* (*chai hu*) and *Scutellariae Radix* (*huang qin*) if the pattern includes extreme heat.
Expands the chest: for accumulation of phlegm in the chest leading to a stifling sensation, pain, or diaphragmatic pressure.
With *Pinelliae Rhizoma preparatum* (*zhi ban xia*) and *Allii macrostemi Bulbus* (*xie bai*) for painful obstruction of the chest or Heart.
Moistens the Intestines: for dry constipation, especially when it appears in a pattern of Lung heat with dry mouth, thirst, and irritability.
With *Cannabis Semen* (*huo ma ren*), *Pruni Semen* (*yu li ren*), and *Aurantii Fructus* (*zhi ke*) for constipation, especially when due to internal obstruction of phlegm-heat with such symptoms as dry mouth and thirst. This combination can also be used for wasting and thirsting disease.
With *Angelicae sinensis Radix* (*dang gui*), *Platycladi Semen* (*bai zi ren*), *Polygoni multiflori Radix* (*he shou wu*), and *Armeniacae Semen* (*xing ren*) to moisten the bowels.
Promotes healing of sores: used adjunctively for breast abscess and swelling as well as sores that have not yet suppurated.
With *Houttuyniae Herba* (*yu xing cao*) and *Platycodi Radix* (*jie geng*) for Lung abscess.
With *Gleditsiae Spina* (*zao jiao ci*) and *Lonicerae Flos* (*jin yin hua*) for breast abscess.
With *Taraxaci Herba* (*pu gong ying*) for Intestinal abscess.

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
Contraindicated in those with a weak, deficient Spleen and either nausea or loose stools.
Essentials of the Materia Medica notes that it is "forbidden in those with diarrhea."

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
Good quality consists of large, full, oily seeds without a greasy surface.

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
