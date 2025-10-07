---
# 🔹 Core Metadata (Universal Fields)
id: "herb-20251001123706"
name: "Qu Mai"
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
  hanzi: "瞿麦"
  pinyin: "Qu Mai"
  pharmaceutical: "Dianthi Herba"
  english: "dianthus, fringed pink (D. superbus), Chinese pink (D. chinensis)"
  alternate_names: []

  # TCM Properties
  taste: [Bitter, cold]
  temperature: "cold"
  channels: [Bladder, Heart, Small Intestine]

  # Clinical Information
  dosage: "9-15g"
  toxicity: "None noted"
  functions: [Clears damp-heat, Promotes urination, Unblocks painful urinary dribbling, Breaks up blood stasis]
  dui_yao: []

  # Additional Information
  constituents: [Triterpene saponins: dianoside A, B, C, D, E, F, G, H, azukisaponin IV, dianic acid, Flavonoids, anthocyanins: homoorientin, orientin, anthocyanin, Other constituents: pinitol, 2-methyl-3,4-dihydroxydihydropyran, 2-methyl-3,4-dihydroxydihydropyran-3-O-β-D-glucoside, proteins, vitamin A, alkaloids, Triterpene saponins: dianchinenoside A, B, dianthoside, Volatile oil: eugenol, phenylethyl alcohol, benzyl benzoate, methyl salicylate, benzyl salicylate, Other constituents: flavonoids, anthocyanins, pinitol]
  quality: "Good quality consists of tender, yellowish green twigs and leaves, without rootlets or foreign matter. The flower buds should still be closed. There is no difference in quality between the two species."
  text_first_appeared: "Divine Husbandman's Classic of the Materia Medica"

  # Source References
  bensky_pdf: "627"
  bensky_page: "290"

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

Bitter, cold, and downward-directing, Dianthi Herba (qu mai) is slippery by nature. It enters the blood level of the Heart channel to break up stasis and disperse clumps, and also enters the Small Intestine to guide heat downward and out through the urine. This dual action gives Dianthi Herba (qu mai) a special significance in the treatment of painful urinary dribbling; and because of its blood-invigorating quality, it can be used for other disorders due to blood stasis, such as amenorrhea. Because it leads heat in the lower burner downward and out of the body, it can also be used for gynecological toxic swellings and sores.

In Rectification of the Meaning of Materia Medica, Zhang Jie-Bin notes that this herb
is slippery and facilitating by nature, and can unblock urination, direct yin fire downward, eradicate the five types of painful urinary dribbling, and facilitate movement in the blood vessels. Together with cooling herbs, it can reduce swelling and pain in the eyes; together with blood [invigorating] herbs, it can promote menstruation, break up blood stasis, and abort a fetus. It can be used for all disorders involving lower burner damp-heat with aching pain.

---
---

## 🔑 TCM Properties

**Taste:** `= join(this.herb_data.taste, ", ")`
**Temperature:** `= this.herb_data.temperature`
**Channels Entered:** `= join(this.herb_data.channels, ", ")`

---

## ⚡ Functions & Actions

- **Clears damp-heat, promotes urination, and unblocks painful urinary dribbling:** for any type of painful urinary dribbling, especially painful bloody urinary dribbling.
    - With Polygoni avicularis Herba (bian xu) for damp-heat painful urinary dribbling. This is a common combination and is the foundation of such formulas as Eight-Herb Powder for Rectification (ba zheng san).
    - With Lygodii Spora (hai jin sha) for stones in the urinary tract.
    - With Gardeniae Fructus (zhi zi) for incomplete, dribbling, burning, and painful urination due to damp-heat in the lower burner.
    - Add Imperatae Rhizoma (bai mao gen) and Cirsii Herba (xiao ji) for heat-induced blood in the urine.
- **Breaks up blood stasis:** used as an auxiliary herb for amenorrhea due to blood stasis.
    - With Salviae miltiorrhizae Radix (dan shen), Paeoniae Radix rubra (chi shao), and Leonuri Herba (yi mu cao) for amenorrhea due to blood stasis.

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
Contraindicated during pregnancy.

Zhang Lu says that it is 'forbidden for use in urinary difficulty during pregnancy or after parturition, and also for edema due to Spleen deficiency,' but this also applies to older patients and deficient patients whose qi transformation is not smooth, leading to such symptoms as urinary blockage, when this is not from accumulation of clumped damp-heat. Their treatment should be to disseminate and transform the qi level. (Rectification of the Meaning of Materia Medica)

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
Good quality consists of tender, yellowish green twigs and leaves, without rootlets or foreign matter. The flower buds should still be closed. There is no difference in quality between the two species.

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
