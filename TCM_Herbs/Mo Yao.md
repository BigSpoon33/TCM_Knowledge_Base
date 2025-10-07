---
# 🔹 Core Metadata (Universal Fields)
id: "herb-20251001123706"
name: "Myrrha / Mo Yao"
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
  hanzi: "沒藥"
  pinyin: "mò yào"
  pharmaceutical: "Myrrha"
  english: "myrrh"
  alternate_names: []

  # TCM Properties
  taste: [bitter, neutral]
  temperature: "Neutral"
  channels: [Heart, Liver, Spleen]

  # Clinical Information
  dosage: "3-9g"
  toxicity: "Ingestion of this substance can cause allergic reactions usually affecting the skin."
  functions: [Invigorates the blood, Dispels blood stasis, Reduces swelling, Alleviates pain, Promotes healing]
  dui_yao: []

  # Additional Information
  constituents: [Resins (25-35%): α-commiphoric acid, β-commiphoric acid, γ-commiphoric acid, commiphorinic acid, heerabomyrrhol, α-heerabomyrrholic acid, β-heerabomyrrholic acid, heeraboresene, commiferin, Volatile oil: eugenol, m-cresol, cuminaldehyde, pinene, limonene, cinnamic aldehyde, heerabolene, 8α-methoxyfuranodiene, 8α-acetylfuranodiene, isofuranogermacrene (curzerene), lindestrene, furanoeudesma-1,3-diene, furanodiene, Other constituents: balsams (57-65%) composed of arabinose, galactose, and xylose]
  quality: "Good quality consists of yellowish brown, broken, slightly translucent, oily pieces with an intense aroma and bitter taste, and without such foreign matter as sand and the like."
  text_first_appeared: "Materia Medica of Medicinal Properties"

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

All of the effects of *Myrrha* (*mò yào*) depend upon its ability to break up blood stagnation: it stops pain by removing obstruction to the flow of blood, which then suffuses affected tissues and stops pain; it reduces mobile and fixed abdominal masses by dispersing blood stasis; and it assists in the healing of injuries by eliminating obstruction from stasis that prevents nourishment and regeneration of the tissues.

Seeking Accuracy in the Materia Medica quotes Kou Zong-Shi as saying:

*Myrrha* (*mò yào*), in brief, unblocks stagnant blood. When blood stagnates, qi clogs statically, which makes the channels and collaterals full and tense. This fullness and tension causes pain and swelling. Strikes and blows, falls and injuries, all harm the channels and collaterals so that the qi and
blood are unable to flow; they clog and become static, causing swelling and pain.

This view is consistently expressed in the classic materia medica texts. Discussion of Medicinal Properties observes that it
governs injuries from strikes and blows [leaving] blood stasis in the Heart and abdomen; damage from falls, and breaks causing pain due to stagnation in the sinews and bones; injuries from metal blades causing intolerable pain.

Materia Medica of the Kaibao Era says that it "primarily breaks up blood [stasis] and stops pain", while the Grand Materia Medica says that it "disperses blood, reduces swelling, arrests pain, and generates flesh."

---
---

## 🔑 TCM Properties

**Taste:** `= join(this.herb_data.taste, ", ")`
**Temperature:** `= this.herb_data.temperature`
**Channels Entered:** `= join(this.herb_data.channels, ", ")`

---

## ⚡ Functions & Actions

* Invigorates the blood and dispels blood stasis, reduces swelling, and alleviates pain: for problems due to blood stasis, including pain from trauma, sores, carbuncles, swellings, fixed abdominal masses, painful obstruction, chest pain, abdominal pain, and amenorrhea.
    * With Corydalis Rhizoma (*yán hú suǒ*), Trogopterus Faeces (*wǔ líng zhī*), and Cyperi Rhizoma (*xiāng fù*) for epigastric and abdominal pain due to obstruction of qi and blood.
    * With Carthami Flos (*hóng huā*) for blood stasis-induced chest and abdominal pain, as well as amenorrhea and dysmenorrhea.
* Promotes healing: used topically to promote the healing of chronic nonhealing sores.

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
Contraindicated in the absence of stasis, or during pregnancy. Use with caution in those with weak stomachs. Should not be used long term.

"Cannot be consumed during pregnancy." (Essentials of Materia Medica Distinctions)

Should not be used when joint pain or chest, abdomen, hypochondrium, and flank pain are not due to retained blood stasis, but rather to blood deficiency. It should not be used for excessive loss of postpartum lochia with abdominal pain due to deficiency. It should not be used when sores have already perforated. (Commentary on the Divine Husbandman's Classic of Materia Medica)

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
Good quality consists of yellowish brown, broken, slightly translucent, oily pieces with an intense aroma and bitter taste, and without such foreign matter as sand and the like.

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
