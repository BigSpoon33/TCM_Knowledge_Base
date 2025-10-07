---
# 🔹 Core Metadata (Universal Fields)
id: "herb-20251001123706"
name: "Dan Zhu Ye"
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
  hanzi: "淡竹叶"
  pinyin: "Dan Zhu Ye"
  pharmaceutical: "Lophatheri Herba"
  english: "Lophatherum Herb"
  alternate_names: []

  # TCM Properties
  taste: [Sweet, bland]
  temperature: "Cold"
  channels: [Heart, Small Intestine, Stomach]

  # Clinical Information
  dosage: "6-9g"
  toxicity: "None noted"
  functions: [Clears heat and eliminates irritability, Promotes urination and clears damp-heat]
  dui_yao: []

  # Additional Information
  constituents: [Iridoid and flavonoid glycosides: gardenoside, geniposide, genipin-1-gentiobioside, shanzhiside, gardoside, scandoside methylester, geniposidic acid, deacetylasperulosidic acid, methyl deacetylasperulosidate, 10-O-acetylgeniposide, 6"-p-coumaroylgenipin gentiobioside, jasminoidin, rutin, Organic acids: chlorogenic acid, 3,4-di-O-caffeoylquinic acid, 3-O-caffeoyl-4-O-sinapoylquinic acid, 3,5-di-O-caffeoyl-4-O-(3-hydroxy-3-methylglutaroyl)quinic acid, 3,5-dicaffeoyl-5-(3-hydroxy-3-methylglutaroyl)quinic acid, picrocrocinic acid, crocetin, ursolic acid, Other constituents: crocin, choline, D-mannitol, β-sitosterol, nonacosane, xanthophyll]
  quality: "Good quality consists of big green leaves with few stalks, and without roots or spikes."
  text_first_appeared: "The Grand Materia Medica"

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

Lophatheri Herba (dan zhu ye) is bland, sweet, and cold. Its ability to leach out dampness and facilitate urination is very strong, while at the same time it cools the Heart and thus eliminates irritability. It is usually prescribed for febrile diseases, irritability, thirst, scanty dark urine, and painful urinary dribbling. Because it is lightweight with a thin qi, it is also used to treat upper burner qi-level heat. Harm and Benefit in the Materia Medica notes, however, that "Its therapeutic strength is rather weak. It cannot serve as the chief herb, but it can serve as an assistant." The Grand Materia Medica was the first book to identify Lophatheri Herba (dan zhu ye). It comments briefly that the herb "expels irritable heat, facilitates urination, and cools the Heart." Lophatheri Herba (dan zhu ye) has a greater diuretic action than actual bamboo leaves, which are better for heat in the upper burner causing cough, irritability, and thirst.

---
---

## 🔑 TCM Properties

**Taste:** `= join(this.herb_data.taste, ", ")`
**Temperature:** `= this.herb_data.temperature`
**Channels Entered:** `= join(this.herb_data.channels, ", ")`

---

## ⚡ Functions & Actions

• Clears heat and eliminates irritability: for heat patterns with irritability and thirst. Also used for mouth sores and swollen, painful gums due to heat in the Heart or Stomach channels.
  - With Gypsum fibrosum (shi gao) for late-stage febrile disease symptoms such as residual fever, sensation of heat and irritability in the chest, desire for cold beverages, and red tongue with thin coating.
  - With Ophiopogonis Radix (mai men dong), Phragmitis Rhizoma (lu gen), and Trichosanthis Radix (tian hua fen) for irritability in the chest with thirst from febrile disease.
• Promotes urination and clears damp-heat: for rough, scanty, painful urination. Especially useful for heat in the Small Intestine channel with the above symptoms plus irritability and a dark-red tip on the tongue.
  - With Akebiae Caulis (mu tong) and Rehmanniae Radix (sheng di huang) for sensation of heat and irritability in the chest, sores of the mouth and tongue, and dark, scanty urine due to heat in the Heart channel, as in Guide Out the Red Powder (dao chi san).

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
None noted

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
Good quality consists of big green leaves with few stalks, and without roots or spikes.

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
