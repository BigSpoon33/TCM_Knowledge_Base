---
# 🔹 Core Metadata (Universal Fields)
id: "herb-20251001123706"
name: "Wei Ling Xian"
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
  hanzi: "威灵仙"
  pinyin: "Wei Ling Xian"
  pharmaceutical: "Clematidis Radix"
  english: "Clematis root, Chinese clematis root"
  alternate_names: []

  # TCM Properties
  taste: [Acrid, Salty]
  temperature: "Warm"
  channels: [Bladder]

  # Clinical Information
  dosage: "6-9g"
  toxicity: "Because of its anemonin and protoanemonin content, this herb has a certain degree of toxicity, which is reduced by lengthy storage in a dry environment (polymerization of protoanemonin into anemonin). Within the normal range of dosage, no significant side effects are to be expected; however overdosage, long-term use, or even long-term topical application in high doses may cause toxic reactions.

Symptoms include burning sensation, swelling, and ulcerations of the oral cavity, vomiting, abdominal pain, severe diarrhea, dyspnea, bradycardia, agitation, a pale face, cold sweat, and dilated pupils. In severe cases, death has been reported about 10 hours after ingestion. The symptoms after topical application in high dosage include rash, blistering of the skin, and allergic dermatitis."
  functions: [Dispels wind-dampness, Unblocks the channels, Alleviates pain, Softens and transforms fish bones, Reduces phlegm and pathogenic water]
  dui_yao: []

  # Additional Information
  constituents: [Saponins: CP2, CP3, CP4, CP7, CP9 (sapogenin: oleanolic acid); CP1, CP3, CP5, CP6, CP8, CP10 (sapogenin: hederagenin), Lactones: protoanemonin (anemonol), anemonin, Other constituents: sterols, sugars, phenolic compounds, amino acids, Volatile oil: 3-hydroxy-4-methoxyl benzaldehyde, trans-anethole, 2-hydroxy-4-methyl acetophenone, 1,3,5-triisopropylbenzene, heptadecane, Lactones: anemonin, Organic acids: palmitic acid, caproic acid, myristic acid, γ-linoleic acid, δ-linoleic acid, oleic acid, pelargonic acid, Saponins: clematoside A, A', B, C]
  quality: "Good quality consists of large, thick roots with a black surface and powdery cross section, with no remaining stems."
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

*Clematidis Radix* (威灵仙 - wei ling xian) is acrid, and thus dispersing, with a strong mobilizing tendency, and a warm, unblocking, and facilitating nature that promotes flow in all the channels, although it tends to favor the lower limbs. Externally, it disperses pathogenic wind; internally, it transforms dampness, unblocks the channels, and extends its reach through the collaterals.

Guiding and disseminating, *Clematidis Radix* (威灵仙 - wei ling xian) is an important herb for pain due to wind. It is indicated for painful obstruction disorder due to wind, dampness, or cold leading to restricted movement of the joints, numbness of the muscles and flesh, and aches and pains in the sinews and bones. It is also used for phlegm-water in the vicinity of the diaphragm, as well as for gynecological pain due to qi and blood obstruction.

*Clematidis Radix* (威灵仙 - wei ling xian) is also salty; it softens areas of hardness and disperses clumps. It is therefore used for abdominal masses, breast lumps, and other clumping. Traditionally, it has even been used alone to soften bones lodged in the throat.

However, because of its very yang and mobilizing nature, it is also drying and tends to exhaust the normal qi. It must therefore not be used for extended periods of time, or in weaker patients.

*Transforming the Significance of Medicinal Substances* explains that this herb is violently urgent in nature, mobilizing without preserving, disseminating and unblocking all twelve channels and collaterals. It primarily treats wind, dampness, and phlegm accumulated in the midst of the channels and collaterals, leading to painful wind and painful joints that may be swollen or numb.

---
---

## 🔑 TCM Properties

**Taste:** `= join(this.herb_data.taste, ", ")`
**Temperature:** `= this.herb_data.temperature`
**Channels Entered:** `= join(this.herb_data.channels, ", ")`

---

## ⚡ Functions & Actions

*   **Dispels wind-dampness, unblocks the channels, and alleviates pain:** Especially useful for treating wind painful obstruction, as it both releases the exterior and promotes the movement of qi in the channels. It can be taken alone as a powder with warm wine for pain in the lower back and legs.
    *   With *Notopterygii Rhizoma seu Radix* (羌活 - qiang huo) for joint pain (especially in the upper extremities) due to wind damp painful obstruction.
    *   With *Achyranthis bidentatae Radix* (牛膝 - niu xi) for joint pain (especially in the lower extremities) due to wind dampness obstructing the channels.
*   **Softens and transforms fish bones:** For fish bones lodged in the throat. This herb is ineffective in the treatment of deeply lodged or relatively large bones.
    *   With vinegar and brown sugar for fish bones lodged in the throat.
*   **Also used for focal distention and accumulation in the middle burner** because it reduces phlegm and pathogenic water.
    *   With *Amomi Fructus* (砂仁 - sha ren) for epigastric pain. This combination is also used with vinegar for fish bones lodged in the throat.

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
Contraindications: Because this herb is very piercing and mobilizing, excessive use will readily injure the normal qi. It should be used with caution in those with qi and/or blood deficiency or in the debilitated. See TOXICITY below.

Traditional Contraindications:
"Its nature is rapid: excessive consumption dredges the true qi of the five organs." (*Extension of the Materia Medica*)

"Whenever blood deficiency generates wind, or qi deficiency generates phlegm, or Spleen deficiency fails to transport such that the qi lingers and generates dampness or generates phlegm or generates thin mucus-for all of these it is forbidden." (*Treasury of Words on the Materia Medica*)

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
Good quality consists of large, thick roots with a black surface and powdery cross section, with no remaining stems.

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
