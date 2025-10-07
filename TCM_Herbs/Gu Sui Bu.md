---
# 🔹 Core Metadata (Universal Fields)
id: "herb-20251001123706"
name: "Gu Sui Bu"
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
  hanzi: "骨碎补"
  pinyin: "Gu Sui Bu"
  pharmaceutical: "Drynariae Rhizoma"
  english: "Drynaria rhizome"
  alternate_names: []

  # TCM Properties
  taste: [Bitter]
  temperature: "Warm"
  channels: [Kidney, Liver]

  # Clinical Information
  dosage: "9-21g"
  toxicity: "No toxic effects have been reported within the normal dosage range. High doses may lead to toxic side effects, however, as in the following case, after ingestion of 100g of the herb in a decoction: dry mouth, loquaciousness, fear, palpitations, a sense of oppression in the chest, muddled consciousness, and a manic-depressive type psychosis."
  functions: [Tonifies the Kidneys and strengthens bones, Promotes mending of the sinews and bones, Stimulates the growth of hair]
  dui_yao: []

  # Additional Information
  constituents: [hop-21-ene, fern-3-ene, filic-3-ene, 25-en-cycloartenol, 25-en-cycloartenone, 24-en-cycloartenol, 24-en-cycloartenone, 5-stigmasten-3-ol, stigmasten-3-one, cyclolaudenol, cyclolaudenyl acetate, cyclolaudenone, diploptene, diplopterol, cyclomargenyl acetate, β-sitosterol, stigmasterol, campesterol, naringin, glucose, L-rhamnose]
  quality: "Good quality consists of large, brown rhizomes with few hairs."
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

Drynariae Rhizoma (gu sui bu) tonifies the Kidneys and Liver, and is primarily used for repairing shattered bones, an effect that is assisted by its ability to invigorate the blood. However, it also directs floating yang downward, and is thus very effective for toothache, migrating teeth, and tinnitus.

In *Rectification of the Meaning of Materia Medica*, Zhang Shan-Lei pursues an interesting and cogent line of thought as he quotes various authorities and makes his own comments about this herb:

It is in the same category as Taxilli Herba (sang ji sheng). Its nature is warm and unblocking, thus it enters the blood and harmonizes the blood, unblocking and adjusting the vessels and collaterals. The *Materia Medica of the Kaibao Era* says that it is bitter and warm, and primarily breaks up blood stasis to stop bleeding, tonifies what has been broken, and also, because the root is used, it warmly harmonizes and reaches downward into the Liver and Kidneys. For this reason, Zhen Quan stated that it governs toxic qi within the bones, pain due to wind or blood stasis, heat in the upper body with cold in the lower-all of this is the result of warmth nourishing the lower primal qi, so that the herb can guide ascending floating heat downward to be stored in the residence of the lower burner. Li Shi-Zhen said that if it is powdered and baked in a pig's kidney, it can treat tinnitus and chronic diarrhea due to Kidney deficiency, as well as toothache. All of this is the same concept, but it cannot be indiscriminately used for toothache due to excess fire in the Stomach!

The ancients all said that this herb enters the Kidneys to treat the bones, and it treats bones that are injured and shattered, so it has this name. But we must acknowledge [the limits of] this concept: as long as it is not yin deficiency with heat leading to bone pain or bone atrophy, it can-as stated-always be used as a general primary treatment.

*Records of Thoughtful Differentiation of Materia Medica* provides the following explanation for the statement in *Materia Medica of the Kaibao Era* that "Drynariae Rhizoma (gu sui bu) breaks up blood stasis and stops bleeding" as follows:

The blood that it breaks up is the stagnant blood in fractured bones, and the bleeding that it stops is the loss of good blood from the fracture. It is not saying that it can break up blood or stop bleeding in other areas.

---
---

## 🔑 TCM Properties

**Taste:** `= join(this.herb_data.taste, ", ")`
**Temperature:** `= this.herb_data.temperature`
**Channels Entered:** `= join(this.herb_data.channels, ", ")`

---

## ⚡ Functions & Actions

- **Tonifies the Kidneys and strengthens bones:** For such symptoms as weak low back and knees, diarrhea, tinnitus, diminished hearing, and loose, painful teeth and bleeding gums associated with Kidney deficiency.
  - With Psoraleae Fructus (bu gu zhi) and Achyranthis bidentatae Radix (niu xi) for unremitting lower back and lower extremity pain from Kidney deficiency.
  - With Dioscoreae Rhizoma (shan yao) for tinnitus and chronic diarrhea.
  - Powder and roast in a pig's kidney for chronic Kidney type diarrhea.
  - With Asari Radix et Rhizoma (xi xin) and Rehmanniae Radix preparata (shu di huang) for toothache and loose teeth from Kidney yin deficiency and subsequent floating yang.
  - With Gypsum Fibrosum (shi gao) and Cimicifugae Rhizoma (sheng ma) for loose teeth and swollen, painful gums.
- **Promotes mending of the sinews and bones:** For traumatic injuries such as falls, fractures, contusions, and sprains. Especially useful for ligamentous injuries and simple fractures.
  - Also used to help regain strength during the convalescent phase of the above injuries.
  - With Dipsaci Radix (xu duan) for trauma-induced injury to the muscles, sinews, and bones.
  - Add Olibanum (ru xiang), Myrrha (mo yao), and Pyritum (zi ran tong) to strengthen this effect.
- **Stimulates the growth of hair:** Used topically as a tincture for alopecia.

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
Use with caution in those with yin deficiency or in the absence of blood stasis.
Contraindicated in all cases of blood deficiency wind dryness, blood deficiency fire, or blood deficiency cramping and painful obstruction.
It should not be used together with wind [-expelling] drying herbs because, while the bitterness of Drynariae Rhizoma (gu sui bu) fortifies the Kidneys, the Kidney organ is averse to dryness, and the additional warmth and dryness of wind herbs will be excessive, resulting in injury to the blood's fluid.

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
Good quality consists of large, brown rhizomes with few hairs.

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
