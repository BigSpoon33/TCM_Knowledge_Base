---
# 🔹 Core Metadata (Universal Fields)
id: "herb-20251001123706"
name: "Tu Fu Ling"
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
  hanzi: "土茯苓"
  pinyin: "Tǔ Fú Líng"
  pharmaceutical: "Smilacis Glabrae Rhizoma"
  english: "Smooth greenbrier rhizome, smilax"
  alternate_names: []

  # TCM Properties
  taste: [Sweet, bland, neutral]
  temperature: "neutral"
  channels: [Liver, Stomach]

  # Clinical Information
  dosage: "15-60g"
  toxicity: "There has been one report of an allergic reaction with pruritus, papular rash, and agitation."
  functions: [Resolves toxicity, eliminates dampness, Clears damp-heat from the skin]
  dui_yao: []

  # Additional Information
  constituents: [Flavonoid glycosides: astilbin, isoengeletin, Organic acids: 3-O-caffeoylshikimic acid, succinic acid, palmitic acid, shikimic acid, ferulic acid, Other constituents: resveratrol, (-)-epicatechin, β-sitosterol, daucosterol, glucose, tannins, resins]
  quality: "Good quality consists of rhizomes with a light brown outer bark, powdery texture, and a low proportion of vessels."
  text_first_appeared: "Grand Materia Medica"

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

Sweet, bland, and entering the Stomach and Liver channels, Smilacis Glabrae Rhizoma (tu fu ling) clears dampness, guides out heat through the urine, and resolves toxicity. While it can remove damp-heat and ease movement of the joints, it is best at treating noxious sores and swellings, and has long been used for the skin lesions and late-stage muscle spasms associated with syphilis, as well as those due to mercury toxicity, which was used in the past to treat syphilis. This herb also treats painful urinary dribbling and vaginal discharge due to toxic dampness.

The *Grand Materia Medica* says that Smilacis Glabrae Rhizoma (tu fu ling) can "expel wind-dampness, ease the joints, treat spasms and bone pain, noxious sores and swellings, and resolve the toxins from mercury and vermilion." The early twentieth-century text *Rectification of the Meaning of Materia Medica* elaborates:

This herb is derived from a vine, the root of which is jointed; by nature, it facilitates the removal of dampness and expels heat, thus it can enter the collaterals to search out and scour away the accumulated toxicity of damp-heat. Regarding its ability to resolve mercury poisoning, while other agents raise to draw the toxins upward, Smilacis Glabrae Rhizoma (tu fu ling) leaches and facilitates, guiding it downward and out [of the body]. This is why it is specific for syphilitic sores, it deeply enters the hundred collaterals, treating all of the noxious symptoms such as joint pain and even necrosis, as well as fire toxin moving upward leading to soreness and ulceration of the throat. Even Western trained doctors recognize this is the only effective medicine for syphilis.

---
---

## 🔑 TCM Properties

**Taste:** `= join(this.herb_data.taste, ", ")`
**Temperature:** `= this.herb_data.temperature`
**Channels Entered:** `= join(this.herb_data.channels, ", ")`

---

## ⚡ Functions & Actions

- **Resolves toxicity and eliminates dampness:** for joint pain, turbid and painful urination, or damp-heat jaundice.
    - With Coicis Semen (yi yi ren) for pain in the joints due to accumulated damp-heat toxin.
    - With Dioscoreae Hypoglaucae Rhizoma (bi xie) for pain in the joints and turbid urine due to damp-heat toxin.
    - With Taraxaci Herba (pu gong ying) for jaundice due to damp-heat in the Liver and Gallbladder.
    - With Imperatae Rhizoma (bai mao gen) and Akebiae Caulis (mu tong) for hot painful urinary dribbling with scanty, dark, and painful urination.
    - With Chuanxiong Rhizoma (chuan xiong) for headache from constrained damp-heat in the Liver channel.
- **Clears damp-heat from the skin:** for recurrent ulcers or other hot skin lesions.
    - With Dictamni Cortex (bai xian pi) for skin lesions associated with damp-heat.
    - With Lonicerae Flos (jin yin hua) and Chrysanthemi Indici Flos (ye ju hua) for abscesses and boils.
    - With Kochiae Fructus (di fu zi), Sophorae Flavescentis Radix (ku shen), and Atractylodis Rhizoma (cang zhu) for eczema or damp sores. Also used for psoriasis.

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
Contraindicated for either yin-type flat abscesses or yin-type jaundice.

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
Good quality consists of rhizomes with a light brown outer bark, powdery texture, and a low proportion of vessels.

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
