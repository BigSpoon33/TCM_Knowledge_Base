---
# 🔹 Core Metadata (Universal Fields)
id: "herb-20251001123706"
name: "Olibanum / Ru Xiang"
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
  hanzi: "乳香"
  pinyin: "Ru Xiang"
  pharmaceutical: "Olibanum"
  english: "frankincense, gum olibanum, mastic"
  alternate_names: []

  # TCM Properties
  taste: [acrid, bitter, warm]
  temperature: "warm"
  channels: [Heart, Liver, Spleen]

  # Clinical Information
  dosage: "3-9g"
  toxicity: "Ingestion of this substance can cause allergic reactions."
  functions: [Invigorates the blood, Promotes the movement of qi, Stops pain, Generates flesh]
  dui_yao: []

  # Additional Information
  constituents: [Resins (60-70%): olibanoresene, α-boswellic acid, O-acetyl-α-boswellic acid, β-boswellic acid, O-acetyl-β-boswellic acid, dihydro roboric acid, epilupeol acetate, tirucallol, Balsams: magnesium and calcium salts of arabic acid, bassorin, Volatile oil: pinene, limonene, α-phellandrene, β-phellandrene, α-campholenaldehyde, cuminaldehyde, carvotanacetone, phellandral, o-methylacetophenone, carvone, perilla aldehyde, eucarvone, 1-acetyl-4-isopropenylcyclopentene, piperitone, nopinone, cryptone, verbenone, γ-campholenaldehyde, thujone, myrtenic acid, p-menth-4-en-3-one, 3,6,6-trimethylnorpinan-2-one, myrtenal, 2,4-dimethylacetophenone, pinocamphone, isopropylidenecyclohexane, α-amyrenone, 11-keto-α-amyrenone, 5-hydroxy-p-menth-6-en-2-one, 10-hydroxy-4-cadinen-3-one, Other constituents: bitter substances]
  quality: "Good quality consists of yellowish white, translucent drops with a glass-like cross section and an intense aroma."
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

Warm and aromatic, such that it unblocks the blood vessels, bitter, such that it drains stasis, Olibanum (ru xiang) is also acrid, enabling it to disperse the stagnation of qi. It acts therefore on both the qi and blood, treating qi and blood stasis causing pain in the Stomach and abdomen, and dysmenorrhea with clotted menstrual blood. It is a favored herb in external medicine due to its piercing aroma that internally disseminates and unblocks the organs, while thrusting out to vent the channels and collaterals on the exterior. Treasury of Words on the Materia Medica says that it is "a medicinal that invigorates the blood, expels wind, relaxes the sinews, and stops pain."

This herb has a strong ability to transform stasis, stop pain, and resolve the toxic swelling associated with early stage carbuncles and sores. Omissions from the Grand Materia Medica says that it "treats all sores by making them resolve internally." The Grand Materia Medica concurs: "eliminates the toxicity of sores and deep-seated toxic boils, supporting the interior and protecting the Heart." For these purposes the herb can be taken both internally and applied topically. Materia Medica of Ri Hua-Zi notes that it should be "decocted into a paste to stop pain and generate flesh."

---
---

## 🔑 TCM Properties

**Taste:** `= join(this.herb_data.taste, ", ")`
**Temperature:** `= this.herb_data.temperature`
**Channels Entered:** `= join(this.herb_data.channels, ", ")`

---

## ⚡ Functions & Actions

*   **Invigorates the blood and promotes the movement of qi:** for traumatic pain due to blood stasis, as well as the early stages of carbuncles, sores, swellings, and pain. Also for chest, epigastric, or abdominal pain due to blood stasis.
    *   With Myrrha (mo yao) for pain due to trauma or other forms of blood stasis obstructing the channels.
    *   With Moschus (she xiang) and Borneolum (bing pian) for pain from trauma, as in Seven-Thousandths of a Tael Powder (qi li san).
    *   With Toosendan Fructus (chuan lian zi) and Aucklandiae Radix (mu xiang) for epigastric pain due to qi stagnation and blood stasis.
    *   With Sargentodoxae Caulis (hong teng) and Violae Herba (zi hua di ding) for intestinal abscesses from heat and stagnant blood clogging the intestines.

*   **Relaxes the sinews, invigorates the channels, and alleviates pain:** for wind-damp painful obstruction, rigidity, and spasms.
    *   With Notopterygii Rhizoma seu Radix (qiang huo), and Gentianae Macrophyllae Radix (qin jiao) for joint pain due to wind-cold-damp painful obstruction, as in Remove Medical Revelations Painful Obstruction Decoction (juan bi tang).
    *   With Pheretima (di long) and Aconiti Radix Praeparata (zhi chuan wu) for spasms and rigidity associated with wind-stroke or cold-damp induced painful obstruction.
    *   With Achyranthis Bidentatae Radix (niu xi) for flank pain due to acute sprain.

*   **Reduces swelling and generates flesh:** applied topically as an ointment or powder to reduce swelling, generate flesh, alleviate pain, and promote healing of sores, carbuncles, and traumatic injury. Also for pain, redness, and swelling of the gums, mouth, and throat.
    *   With Myrrha (mo yao) as a paste for chronic, ulcerated, nonhealing sores.
    *   Add Realgar (xiong huang) and Moschus (she xiang) for abscesses which have not opened as well as ulcerations. Apply topically as a powder for chronic nonhealing ulcerations and wounds.

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
**Contraindications:** Contraindicated in the absence of stasis, and during pregnancy. Use with caution in those with weak stomachs. Should not be used long term. See Toxicity below.

## Traditional Contraindications

"Do not use if the Stomach is weak." (Encountering the Sources of the Classic of Materia Medica)

"Should not be consumed when sores have already perforated; when the pus is profuse, it should not be used too soon." (Commentary on the Divine Husbandman's Classic of Materia Medica) By this it is meant that, if used before the sores have perforated and the pus expelled, the ability of Olibanum (ru xiang) to generate flesh will tend to trap the pus internally rather than facilitating its expulsion from the body. The warning against use after sores have perforated may seem unusual for a substance that "assists the growth of flesh." The author of this text, Miao Xi-Yong, regards both Myrrha (mo yao) and Olibanum (ru xiang) to be primarily dispersing, and he repeats this warning in his entry for the latter substance. While he considers both substances valuable in the treatment of swollen sores due to obstruction, once the obstruction has been resolved and the sores have perforated, the growth of flesh will follow naturally and more dispersal is contraindicated.

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
Good quality consists of yellowish white, translucent drops with a glass-like cross section and an intense aroma.

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
