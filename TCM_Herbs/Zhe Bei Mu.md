---
# 🔹 Core Metadata (Universal Fields)
id: "herb-20251001123706"
name: "Zhe Bei Mu"
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
  hanzi: "浙贝母"
  pinyin: "zhè bèi mǔ"
  pharmaceutical: "Fritillariae Thunbergii Bulbus"
  english: "Zhejiang fritillaria bulb, Thunberg fritillaria bulb"
  alternate_names: []

  # TCM Properties
  taste: [Bitter, cold]
  temperature: "cold"
  channels: [Heart, Lung]

  # Clinical Information
  dosage: "4.5-9g"
  toxicity: "See Cremastrae; ENPleiones Pseudobulbus (shan gu) for Iphigenia indica (jiang shan ci gu, yi pi jian)."
  functions: [Clears and transforms phlegm-heat, Clears heat and dissipates nodules]
  dui_yao: []

  # Additional Information
  constituents: [Alkaloids: verticine, verticinone, peimine, peiminine, zhebeinine, zhebeirine, eduardine, zhebeinone, peimisine, isoverticine, verticine-N-oxide, verticinone-N-oxide, 11-deoxo-6-oxo-5α,6-dihydrojervine, 12,13-epoxy-11-deoxo-6-oxo-5α,6-dihydrojervine N,O-diacetate, 12, 13-epoxy-22β,25β,5α-veratramine-3β,17β,23α-triol-6-one N,O(3)diacetate, choline, Glycosides: peiminoside, zhebeininoside, Diterpenes: communic acid methylester, isopimaran-19-ol, isopimaran-19-oic acid methylester, ent-kauran16β,17-diol, ent-16α,17-epoxykaurane, ent-16α-methoxykauran-17β-ol, ent-kaur-15-en-17-ol, ent-kauran-16α,17-diol, Organic acids: coriolic acid, 13-hydroxy-9E,11E-octadecadienoic acid, α-dimorphecolic acid, δ-dimorphecolic acid, Other constituents: picropodophyllotoxin, β-sitosterol, carotene]
  quality: "Good quality consists of dry, white, powdery, solid bulbs without areas of loose texture."
  text_first_appeared: "Thoroughly Revised Materia Medica"

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

Fritillariae thunbergii Bulbus (zhe bei mu) cools heat and transforms phlegm, alleviates cough and disperses clumps and so is appropriate for externally-contracted pathogenic wind with phlegm-heat constraining the Lungs, leading to cough with thick yellow phlegm; chest pain resulting from phlegm clumping in the chest; scrofula; boils and other toxic swellings. Rectification of the Meaning of Materia Medica notes that it, "while bitter and cold, also has an implicit acrid, dispersing action; thus, while it can expel heat, drain and direct downward, it can also disperse clumps." Omissions from the Grand Materia Medica notes that Zhang Jing-Yue emphasized the herb's efficacy in treating toxic swellings, and extended this to other wounds as well: bleeding from wounds from metal implements, pain from fire sores, it can be applied as a powder or decocted and taken internally. Its flavor and nature are both strong, and compared to Fritillariae cirrhosae Bulbus (chuan bei mu), its ability to cool and direct downward is several times greater.

---
---

## 🔑 TCM Properties

**Taste:** `= join(this.herb_data.taste, ", ")`
**Temperature:** `= this.herb_data.temperature`
**Channels Entered:** `= join(this.herb_data.channels, ", ")`

---

## ⚡ Functions & Actions

*   Clears and transforms phlegm-heat: for acute Lung heat patterns with productive cough.
    *   With Forsythiae Fructus (lian qiao) and Arctii Fructus (niu bang zi) for cough, especially of an acute nature, due to externally-contracted wind-heat with dry mouth, scratchy throat, and thick yellow sputum.
*   Clears heat and dissipates nodules: for phlegm-fire which congeals and causes neck swellings. Also important for Lung and breast abscess and swellings.
    *   With Scrophulariae Radix (xuan shen), Ostreae Concha (mu li), and Prunellae Spica (xia ku cao) for scrofula.
    *   Especially due to phlegm-fire with pain and swelling at multiple sites, as in Reduce Scrofula Pill (xiao luo wan).
    *   With Sargassum (hai zao), Eckloniae Thallus (kun bu) and Pinelliae Rhizoma preparatum (zhi ban xia) for rock-like masses in the center of the neck, as in Sargassum Decoction for the Jade Flask (hai zao yu hu tang).
    *   With Prunellae Spica (xia ku cao), Sargassum (hai zao) and Curcumae Rhizoma (yu jin) for thyroid nodules.
    *   With Sepiae Endoconcha (hai piao xiao) for epigastric pain and acid regurgitation.
    *   With Lonicerae Flos (jin yin hua), Taraxaci Herba (pu gong ying), and Chrysanthemi Flos (ju hua) for abscess and other toxic swellings. This combination is most appropriate in the early stages where there is firm swelling, redness and pain.
    *   With Coicis Semen (yi yi ren), Benincasae Semen (gua lou zi), and Houttuyniae Herba (yu xing cao) for Lung abscess.

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
According to some traditional sources, this herb is incompatible with Aconiti Radix preparata (zhi chuan wu) and other aconite medicinals. It is ineffective for coughs due to phlegm secondary to cold-dampness.

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
Good quality consists of dry, white, powdery, solid bulbs without areas of loose texture.

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
