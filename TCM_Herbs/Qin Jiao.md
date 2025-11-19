---
# 🔹 Core Metadata (Universal Fields)
id: "herb-20251001123706"
name: "Qin Jiao"
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
  hanzi: "秦艽"
  pinyin: "qín jiāo"
  pharmaceutical: "Gentianae Macrophyllae Radix"
  english: "Large Gentian Root"
  alternate_names: []

  # TCM Properties
  taste: [Bitter, Acrid]
  temperature: "Slightly Cold"
  channels: [Gallbladder, Liver, Stomach]

  # Clinical Information
  dosage: "3-9g"
  toxicity: "N/A"
  functions: [Dispels wind-dampness and soothes the sinews and collaterals, Clears heat from deficiency, Resolves dampness and reduces jaundice, Moistens the Intestines and unblocks the bowels]
  dui_yao: []

  # Additional Information
  constituents: [*Gentiana macrophylla*:
    - Alkaloids: gentianine, gentianidine, gentianal
    - Iridoid glycosides: qinjiaoside, gentiopicroside, harpagoside, swertiamarin
    - Other constituents: montanic acid, methyl montanate, roburic acid, α-amyrin, γ-amyrin, β-sitosterol, β-sitosterol-β-D-glucoside, *Gentiana straminea*:
    - Alkaloids: gentianine, gentianal
    - Iridoid glycosides: gentiopicroside, sweroside, swertiamarin, *Gentiana crassicaulis*:
    - Alkaloids: gentianine, gentianal
    - Iridoid glycosides: gentiopicroside, sweroside, swertiamarin, *Gentiana dahurica*:
    - Alkaloids: gentianine, gentianal
    - Iridoid glycosides: gentiopicroside, swertiamarin]
  quality: "Good quality consists of large, solid, and heavy roots that are aromatic."
  text_first_appeared: "Harm and Benefit in the Materia Medica"

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

Acrid, bitter, and slightly cold (rated 'neutral' in some sources), Gentianae Macrophyllae Radix (qin jiao) enters the Spleen and Liver channels. Acridity disperses and bitterness drains; Gentianae Macrophyllae Radix (qin jiao) therefore dispels wind and drains dampness from these channels, unblocking the flow of nutrients to the sinews and muscles, and thereby eliminating painful obstruction disorder. It also treats damp-heat jaundice. By eliminating yang brightness dampness, the pathogenic heat has no material impediment to its dispersal. In this way, it halts the process that leads to steaming bones and tidal fevers.
- Although it is a wind-expelling herb—which are usually drying—its bitterness does not dry excessively, and its nature is relatively harmonious. This has given rise to the adage, "All wind herbs are drying, but only Gentianae Macrophyllae Radix (qin jiao) tends to be moistening." In this context, "moistening" really means less drying, such that when it dispels wind and dampness, it does not severely damage the yin or fluids. It can therefore be used in the treatment of steaming bones, heat from consumption, heat during pregnancy, and the constrained heat involved in childhood nutritional impairment.

---
---

## 🔑 TCM Properties

**Taste:** `= join(this.herb_data.taste, ", ")`
**Temperature:** `= this.herb_data.temperature`
**Channels Entered:** `= join(this.herb_data.channels, ", ")`

---

## ⚡ Functions & Actions

Dispels wind-dampness and soothes the sinews and collaterals: for wind-damp painful obstruction and cramping, especially in the extremities. Can be used for acute or chronic, cold or hot disorders. Because this substance is slightly cold and most other herbs for wind-dampness are warm, it is particularly suitable for hot painful obstruction.
    - With Anemarrhenae Rhizoma (zhi mu) and Lonicerae Caulis (ren dong teng) for hot painful obstruction.
    - With Saposhnikoviae Radix (fang feng), Angelicae pubescentis Radix (du huo), and Notopterygii Rhizoma seu Radix (qiang huo) for wind-cold-damp painful obstruction.
    - With Angelicae sinensis Radix (dang gui), Gastrodiae Rhizoma (tian ma), Chuanxiong Rhizoma (chuan xiong), and Paeoniae Radix alba (bai shao) for hemiplegia, especially with hypertonicity of the upper extremities, presenting with symptoms of blood deficiency, as in Major Large Gentianae Decoction (da qin jiao tang).
- Clears heat from deficiency: for yin deficiency patterns that manifest with fever, including steaming bone disorder.
    - With Trionycis Carapax (bie jia), Artemisiae annuae Herba (qing hao), and Lycii Cortex (di gu pi) for fever of steaming bone disorder, afternoon fever, and other low-grade fevers due to yin deficiency associated with the aftermath of a long-term illness, as in Large Gentianae and Soft-Shelled Turtle Shell Powder (qin jiao bie jia san).
- Resolves dampness and reduces jaundice: for jaundice due to damp-heat, especially in acute cases and in infants.
    - With Scutellariae Radix (huang qin) and Atractylodis Rhizoma (cang zhu) for damp-heat induced jaundice, especially in children.
- Moistens the Intestines and unblocks the bowels: for dry constipation. This herb is commonly used to counteract the drying qualities of other herbs that dispel wind-dampness.
    - With Cannabis Semen (huo ma ren) and Pruni Semen (yu li ren) for constipation due to dry Intestines.

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
"Use with caution in those with internal heat due to yin deficiency." (New Reference of Prepared Medicines)
- Inappropriate for those with loose stools due to Spleen deficiency.
- "Herbs that drain, disperse, dredge, and facilitate should not be taken when there is cold from deficiency in the lower part [of the body], incontinence of urine, or loose stools." (Harm and Benefit in the Materia Medica)

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
Good quality consists of large, solid, and heavy roots that are aromatic.

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
