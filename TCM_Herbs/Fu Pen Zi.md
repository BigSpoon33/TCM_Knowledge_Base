---
# 🔹 Core Metadata (Universal Fields)
id: "herb-20251001123706"
name: "Fu Pen Zi"
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
  hanzi: "覆盆子"
  pinyin: "Fù Pén Zǐ"
  pharmaceutical: "Rubi Fructus"
  english: "Chinese raspberry, rubus"
  alternate_names: []

  # TCM Properties
  taste: [Sweet, astringent]
  temperature: "neutral"
  channels: [Kidney, Liver]

  # Clinical Information
  dosage: "6-12g"
  toxicity: "None"
  functions: [Augments the true yin of the Kidneys, contains the urine, secures the essence, Augments and stabilizes the Kidneys, binds the essence, contains the urine]
  dui_yao: []

  # Additional Information
  constituents: [Terpenes: goshonoside F1-F7, rubuscoside I, II, Ill, fupenzic acid, Sterols: β-sitosterol, Other constituents: sugars, organic acids, ellagic acid, amino acids, volatile oil, vitamins A, E]
  quality: "Good quality consists of unfragmented, full, yellowish green fruit with a sour taste."
  text_first_appeared: "Miscellaneous Records of Famous Physicians"

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

Rubi Fructus (*fu pen zi*) is sweet, slightly sour and astringent, and neutral; it tonifies Kidneys without causing dryness or heat, and secures the essence without causing inappropriate congealing. Both the Divine Husbandman and Miscellaneous Records of Famous Physicians state that it is neutral, while some later materia medica texts state that it is warming. Miscellaneous Records of Famous Physicians says "Primarily augments the qi, lightens the body, and keeps the hair from turning white."

The Materia Medica of the Kaibao Era elaborates:
Tonifies deficiency, restores what has been severed, strengthens the yin and constructs the yang, makes the skin glossy, quiets and harmonizes [both the] the yin and yang organs, warms the middle and augments the strength, remedies injury from consumption and wind deficiency, tonifies the Liver and brightens the eyes.

Discussion of Medicinal Properties says that it is indicated: "Primarily for spent deficiency of Kidney essence in the male; females consuming it bear children. Governs infertility." Extension of the Materia Medica captures its most essential qualities: "Augments the Kidney organ, contains the urine." Commentary on the Divine Husbandman's Classic of Materia Medica reiterates these observations, then adds: "All of these note [its ability to] augment the Kidneys and replenish the essence, and refer to the concept of 'sweet-sour binding restraint'."

Rectification of the Meaning of Materia Medica elaborates on its qualities and functions:
[It] is a herb that nourishes the true yin. Its flavor is slightly sour, it restrains and contains the yin qi that has been dispersed and depleted, and generates seminal fluids. This is the reason Kou Zong-Shi [in Extension of the Materia Medica] stated that it 'augments the Kidneys and contains the urine', and that those taking it can turn over their bed pan [as it will no longer be needed]. The Divine Husbandman [notes that it] 'primarily governs the five yin organs': all seeds are firm and full, and most [seeds] tonify the middle; with its sour capacity to restrain, it is naturally even more able to tonify the yin of the five yin organs and augment the essential qi. All seeds are heavy, and most augment the Kidneys, while this [herb] specifically enters the Kidney yin and fortifies the Kidney qi, hence the statement that it grows yin and creates fortitude. [The statement in the Divine Husbandman that it] 'strengthens resolve, doubles power, and enhances fertility': all are the effects of tonifying and augmenting the Kidney yin. That it 'lightens the body with long-term consumption and prevents aging' - this merely expresses the end result of these actions. [The statement in Miscellaneous Records of Famous Physicians that it] 'augments the qi, lightens the body, and keeps the hair from turning white' supports the Divine Husbandman's view.

Yet [it] only tonifies the yin, it does not reinforce the yang; neither the Divine Husbandman nor the Miscellaneous Records says that it is warm. Those statements calling it 'slightly warm' or 'slightly hot' are all later conjectures - as if all herbs that tonify the Kidneys must be warm! Don't they know that there are herbs that specifically govern Kidney yin and Kidney yang, and that those herbs that enrich and nourish the Kidney yin must not be warm!

The reading of materia medica texts must be based on the Divine Husbandman's Classic of the Materia Medica, supplemented by Miscellaneous Records of Famous Physicians. The various theories of later writers are often confused and jumbled: one must view them with discrimination.

---
---

## 🔑 TCM Properties

**Taste:** `= join(this.herb_data.taste, ", ")`
**Temperature:** `= this.herb_data.temperature`
**Channels Entered:** `= join(this.herb_data.channels, ", ")`

---

## ⚡ Functions & Actions

- Augments the true yin of the Kidneys, contains the urine, secures the essence.

- Augments and stabilizes the Kidneys, binds the essence, and contains the urine: for urinary frequency or enuresis, impotence, spermatorrhea, premature ejaculation, or wet dreams due to Kidney yang deficiency.

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
- Use with caution in cases of yin deficiency with heat signs.
- Contraindicated in cases of urinary difficulty.

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
Good quality consists of unfragmented, full, yellowish green fruit with a sour taste.

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
