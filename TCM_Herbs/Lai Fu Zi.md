---
# 🔹 Core Metadata (Universal Fields)
id: "herb-20251001123706"
name: "Lai Fu Zi"
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
  hanzi: "莱菔子"
  pinyin: "lái fú zǐ"
  pharmaceutical: "Raphani Semen"
  english: "Radish Seed, Raphanus"
  alternate_names: []

  # TCM Properties
  taste: [Acrid, sweet, neutral]
  temperature: "neutral"
  channels: [Lung, Spleen, Stomach]

  # Clinical Information
  dosage: "4.5-9g; should be crushed prior to use"
  toxicity: "There is one report of significant side effects from the combination of this herb with *Rehmanniae Radix Preparata* and *Polygoni Multiflori Radix*, including dry mouth, vertigo, hoarseness, diminished consciousness, and spasms of the limbs."
  functions: [Reduces food stagnation, Eliminates distention, Causes qi to descend, Reduces phlegm]
  dui_yao: []

  # Additional Information
  constituents: [Fixed oil (30%): erucic acid, linoleic acid, linolenic acid, sinapine, raphanin, brassicasterol, 22-dehydrocampesterol, β-sitosterol, γ-sitosterol]
  quality: "Good quality consists of full, oily, reddish brown seeds without foreign matter."
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

Acrid, sweet, and neutral, *Raphani Semen* (莱菔子 lái fú zǐ) is best at facilitating the flow of qi. In its unprepared (raw) form, it raises the qi, but when dry-fried, it directs the qi downward.

It extends through the Lung channel to direct the qi downward and transform phlegm, and mobilizes the Spleen channel to promote the flow of Spleen qi and reduce food stagnation. Thus it is often used in the treatment of cough and wheezing with profuse phlegm, or abdominal distention, belching, loss of appetite, and diarrhea with tenesmus due to food and qi stagnation.

In its unprepared form, its raising action is strong, driving out wind-phlegm and relieving the upper burner stifling sensation in the chest. However, it often causes vomiting, a feature which is exploited in cases of wind stroke with phlegm welling upward and food stagnating in the middle burner. Often a single regurgitation of the obstructing pathogenic influence will provide great relief.

*Rectification of the Meaning of Materia Medica* provides a helpful discussion of this herb:

When unprepared [it] is slightly acrid and neutral in nature; when dry-fried it is aromatic and warm in nature. Its power both raises and directs downward; when unprepared its raising is greater than its downward-directing; when dry-fried it directs downward more than it raises. Use it unprepared for unbinding the qi and transforming phlegm; use it dry-fried when directing qi downward and reducing food stagnation. On investigation, regardless of whether unprepared or dry-fried, it can smooth [the flow of] qi and unbind constraint, reduce distention and eliminate fullness: it is a herb that transforms qi, not one that breaks up qi.

Most physicians believe that it as able to break up qi, and therefore [something that] should not be taken in high doses or for long periods of time, but this is quite incorrect. All herbs that regulate the qi injure the qi if [the herb is] taken alone or for a long time, but *Raphani Semen* (莱菔子 lái fú zǐ), if dry-fried and powdered, can be taken after every meal in doses just over one *qian* [approximately 4g] in order to reduce food stagnation and smooth the qi. It does not injure the qi at all, because it assists the intake of food and drink so that the qi aspect obtains nourishment. If used to expel fullness and unbind constraint, it can be assisted by such herbs as *Codonopsis Radix* (党参 dǎng shēn), *Astragali Radix* (黄芪 huáng qí), and *Atractylodis Macrocephalae Rhizoma* (白术 bái zhú); then, even if taken in higher doses or for a long time, how could it injure the qi aspect?

---
---

## 🔑 TCM Properties

**Taste:** `= join(this.herb_data.taste, ", ")`
**Temperature:** `= this.herb_data.temperature`
**Channels Entered:** `= join(this.herb_data.channels, ", ")`

---

## ⚡ Functions & Actions

*   **Reduces food stagnation and eliminates distention:** For food stagnation accumulating in the middle burner with fullness and distention, belching with a rotten smell, acid regurgitation, or abdominal pain with diarrhea.
    *   With *Crataegi Fructus* (山楂 shān zhā), *Massa Medicata Fermentata* (神曲 shén qū), and *Citri Reticulatae Pericarpium* (陈皮 chén pí) for abdominal distention, borborygmus, belching, acid regurgitation, and diarrhea due to stagnation in the Stomach and Intestines, as in Preserve Harmony Pill (保和丸 bǎo hé wán).
    *   Add *Atractylodis Macrocephalae Rhizoma* (白术 bái zhú) for accompanying Spleen deficiency.
    *   With *Aurantii Fructus* (枳壳 zhǐ ké) for focal distention, belching, and loss of appetite due to food stagnation.
*   **Causes qi to descend and reduces phlegm:** For chronic productive cough or wheezing. Most effective in cases due to excess.
    *   With *Pinelliae Rhizoma Preparatum* (制半夏 zhì bàn xià) for phlegm-dampness induced cough and wheezing. This combination is also used for distention and vomiting due to food stagnation.
    *   With *Armeniacae Semen* (杏仁 xìng rén) for chronic productive cough.
    *   With *Perillae Fructus* (紫苏子 zǐ sū zǐ) and *Sinapis Semen* (白芥子 bái jiè zi) for chronic cough and wheezing, especially that due to excessive phlegm disorders.
*   **Recently used for hypertension,** as in Three-Seed Decoction to Nourish One's Parents (三子养亲汤 sān zǐ yǎng qīn tāng).

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
Inappropriate in the absence of food stagnation, phlegm, or other form of accumulation. Because it consumes the qi, it should not be taken long term.  Should not be used together with *Ginseng Radix* (人参 rén shēn), *Rehmanniae Radix Preparata* (熟地黄 shú dì huáng), or *Polygoni Multiflori Radix Preparata* (制何首乌 zhì hé shǒu wū).

*Harm and Benefit in the Materia Medica* cautions that it is "even more rapid in reducing phlegm and driving qi downward [than radish itself]. When deficient or weak patients consume it, qi becomes difficult to distribute, affecting breathing." The *Materia Medica of Combinations* states that it is contraindicated when taking tonics.

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
Good quality consists of full, oily, reddish brown seeds without foreign matter.

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
