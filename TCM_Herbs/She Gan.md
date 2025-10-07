---
# 🔹 Core Metadata (Universal Fields)
id: "herb-20251001123706"
name: "She Gan / Belamcandae Rhizoma"
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
  hanzi: "射干"
  pinyin: "Shè Gàn"
  pharmaceutical: "Belamcandae Rhizoma"
  english: "Leopard Lily Rhizome"
  alternate_names: []

  # TCM Properties
  taste: [Bitter, Cold]
  temperature: "Cold"
  channels: [Lung]

  # Clinical Information
  dosage: "3-9g"
  toxicity: "None listed"
  functions: [Clears heat, resolves toxicity, and improves the condition of the throat, Transforms phlegm and clears the Lungs]
  dui_yao: []

  # Additional Information
  constituents: [Isoflavones: iridin, irigenin, tectoridin, tectorigenin, irisflorentin, noririsflorentin, belamcanidin, methylirisolidone, isotectorin A, B, isotectorigenin A, B, demethyltectorigenin, muningin, 5,3'-dihydroxy-4',5'-dimethoxy-6,7-methylenedioxyisoflavone, 5,7,3'-trihydroxy-8,4'-dimethoxyisoflavone, rhamnocitrin, Bicyclic triterpenes: belamcandal, deacetylbelamcandal, acylbelamcandal, isoiridogermanal, isoiridogermanal monoacetate, acylisoiridogermanal, acylisoiridogermanal monoacetate, Phenylpropanones: apocynin, sheganone, androsin, tecturoside, Phenoles, quinones: belamcandol A, B, belamcandaquinone A, B, (2-methoxy-6-pentadeca-10'-en)-1,4-benzoquinone]
  quality: "Good quality consists of dry, full rhizomes with a hard texture and without fibrous roots or soil on the surface. The cross section is yellow."
  text_first_appeared: "Divine Husbandman's Classic of Materia Medica"

  # Source References
  bensky_pdf: "627"
  bensky_page: "N/A"

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

Bitter and cold, Belamcandae Rhizoma (she gan) clears heat toxin, resolves swelling and pain of the throat, transforms phlegm in the throat, and is thus effective for cough, wheezing, and audible breathing due to clumping of phlegm and pathological water.

The Grand Materia Medica notes that "Belamcandae Rhizoma (she gan) directs downward, which explains its importance in ancient formulas for treating sore throat and painful obstruction in the throat." Rectification of the Meaning of Materia Medica observes: "The main therapeutic effects of Belamcandae Rhizoma (she gan) may seem to be many, but they can be subsumed under these two: 'directs downward to unbind phlegm' and 'breaks up clumps to drain heat'." Thus, Belamcandae Rhizoma (she gan) is used for swelling and pain of the throat from either wind-heat or phlegm-heat obstruction, and for phlegm leading to coughing and wheezing. By cooling the heat in the Lungs, the yang fluids of the Lungs no longer thicken, thereby reducing the accumulation of phlegm, and facilitating its expulsion.

Encountering the Sources of the Classic of Materia Medica suggests that Belamcandae Rhizoma (she gan) also possesses an acrid flavor, and explains its functions:

The primary indications in the Divine Husbandman are cough and upward rebellion of qi, and painful obstruction of the throat that does not let up. It disperses clumped qi, rebellious qi within the abdomen, and over-consumption of very hot food or drink. To clarify: bitterness can drive downward and drain, acridity can disperse upward, so all of the indications in the Divine Husbandman involve its clump-dispersing effect-and it is indeed an important medicinal for painful obstruction of the throat.

---
---

## 🔑 TCM Properties

**Taste:** `= join(this.herb_data.taste, ", ")`
**Temperature:** `= this.herb_data.temperature`
**Channels Entered:** `= join(this.herb_data.channels, ", ")`

---

## ⚡ Functions & Actions

- Clears heat, resolves toxicity, and improves the condition of the throat: for swelling and pain of the throat due to fire excess, fire toxin, or phlegm-heat obstruction. Sometimes used alone for sore throat.
    - With Scutellariae Radix (huang qin) for sore throat and cough due to heat in the Lungs.
    - Add Platycodi Radix (jie geng) for pain and swelling of the throat with hoarseness of varying severity due to fire excess.
    - With Sophorae tonkinensis Radix (shan dou gen) for severe sore throat and phlegm that is difficult to expectorate.
    - With Lonicerae Flos (jin yin hua) and Lasiosphaera/Calvatia (ma bo) for throat painful obstruction, as in Honeysuckle, Forsythia, and Puffball Powder (yin qiao ma bo san).
    - With Lasiosphaera/Calvatia (ma bo), Cimicifugae Rhizoma (sheng ma), and Scrophulariae Radix (xuan shen) for fire toxin affecting the throat.
- Transforms phlegm and clears the Lungs: for cough and wheezing with phlegm obstruction. Its effect on phlegm is so strong that it is combined with warming herbs in treating obstruction and clogging due to cold-phlegm.
    - With Armeniacae Semen (xing ren) and Platycodi Radix (jie geng) for such Lung heat symptoms as cough, and pain and swelling of the throat with difficulty in expectorating.
    - With Ephedrae Herba (ma huang), Asari Radix et Rhizoma (xi xin), and Zingiberis Rhizoma recens (sheng jiang) for wind-cold asthma with constriction of the chest secondary to phlegm, as in Belamcanda and Ephedra Decoction (she gan ma huang tang).

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
Contradindicated in those with loose stools, as ingestion can lead to watery diarrhea.
Relatively contraindicated during pregnancy.

When using this herb to treat wind-fire or damp-heat, it can be used as the chief constituent, but only for a short time; it cannot be used for any extended period of time.
It enters the Lungs and disperses clumping at the qi level, thus dispersing wind-phlegm. However, if clumping is present, it will disperse the clumps, but if there is no actual clumping, it will disperse the qi. This will inevitably lead to wheezing from deficiency. (New Compilation of Materia Medica)

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
Good quality consists of dry, full rhizomes with a hard texture and without fibrous roots or soil on the surface. The cross section is yellow.

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
