---
# 🔹 Core Metadata (Universal Fields)
id: "herb-20251001123706"
name: "Niu Xi"
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
  hanzi: "牛膝"
  pinyin: "niu xi"
  pharmaceutical: "Achyranthis Bidentatae Radix"
  english: "Achyranthes Root"
  alternate_names: []

  # TCM Properties
  taste: [Sweet, Bitter]
  temperature: "Neutral"
  channels: [Liver, Kidney]

  # Clinical Information
  dosage: "6-15g"
  toxicity: "Ingestion of this substance can cause allergic reactions usually affecting the skin."
  functions: [Invigorates the blood, Dispels blood stasis, Tonifies the Liver and Kidneys, Strengthens the sinews and bones, Benefits the joints, Induces the downward movement of blood and fire, Clears damp-heat in the lower burner]
  dui_yao: []

  # Additional Information
  constituents: [Triterpene saponines: sapogenin: oleanolic acid, Steroles: ecdysterone, inokosterone, rubrosterone, polysachharides, amino acids, coumarine derivates, alkaloids, betaine, saccharose]
  quality: "Good quality consists of dry, fleshy, long roots with thin cork, a yellowish grey surface, and sweet taste. The crown should be cut off."
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

Depending on its method of preparation, Achyranthis bidentatae Radix (niu xi) has very different properties. In its unprepared form, it breaks up blood, unblocks menstruation, and guides the blood downward, treating such symptoms as amenorrhea due to blood stasis, mobile and fixed abdominal masses, postpartum abdominal pain due to blood stagnation, difficult labor, retained placenta, swelling and pain from external injury, and pain in the joints from painful obstruction. It leads blood downward, which also has the effect of directing downward fire that is blazing upward and causing nosebleed, sore throat, and swollen, bleeding gums. However, the unprepared form also has a downward-slipping tendency that can aggravate spermatorrhea, vaginal discharge, and diarrhea; for patients with these problems, the herb should either be used in its prepared form, or not at all.

In its prepared form, the herb tonifies the Liver and Kidneys, strengthens the sinews and bones, and is used for aching weakness of the lower back and knees, and lack of strength in the sinews and bones. The Grand Materia states that it "is an herb of the leg terminal yin and leg lesser yin channels. When prepared with wine, it primarily tonifies the Liver and Kidneys; when used unprepared, it expels noxious blood."

---
---

## 🔑 TCM Properties

**Taste:** `= join(this.herb_data.taste, ", ")`
**Temperature:** `= this.herb_data.temperature`
**Channels Entered:** `= join(this.herb_data.channels, ", ")`

---

## ⚡ Functions & Actions

- Invigorates the blood and dispels blood stasis: for blood stasis patterns with such symptoms as dysmenorrhea, amenorrhea, and retained lochia. Also used for post-traumatic pain.
    - With Carthami Flos (hong hua), Angelicae sinensis Radix (dang gui), and Cinnamomi Cortex (rou gui) for amenorrhea, dysmenorrhea, and delayed menstruation due to blood stasis.
    - With Olibanum (ru xiang) and Myrrha (mo yao) for pain from trauma.
- Tonifies the Liver and Kidneys, strengthens the sinews and bones, and benefits the joints: for pain and soreness affecting the lower back and knees due to deficiency.
    - With Eucommiae Cortex (du zhong) for pain and weakness of the lower back and extremities due to Kidney deficiency and/or painful obstruction.
    - With Rehmanniae Radix preparata (shu di huang) and Testudinis Plastrum (gui ban) for weak lower back and extremities from Liver and Kidney insufficiency, as in Hidden Tiger Pill (hu qian wan).
    - With Chaenomelis Fructus (mu gua) and Dioscoreae hypoglaucae Rhizoma (bi xie) for lower extremity pain due to invasion of wind-dampness.
- Induces the downward movement of blood and fire: for chaotic movement of hot blood in the upper burner or yin deficiency with ascending fire. Manifestations include nosebleed, vomiting blood, toothaches, bleeding gums. Also for dizziness, headache, and blurred vision due to ascendent Liver yang.
    - With Gypsum fibrosum (shi gao) and Rehmanniae Radix preparata (shu di huang) for pain, swelling, and ulceration of the teeth, gums, and tongue from Stomach heat and yin deficiency, as in Jade Woman Decoction (yu nü jian).
    - With Haematitum (dai zhe shi) and Ostreae Concha (mu li) for dizziness and vertigo from ascendant Liver yang secondary to Liver and Kidney yin deficiency, as in Sedate the Liver and Extinguish Wind Decoction (zhen gan xi feng tang).
    - With Uncariae Ramulus cum Uncis (gou teng) and Taxilli Herba (sang ji sheng) for headache, dizziness, and blurred vision associated with ascendant Liver yang.
    - With Angelicae sinensis Radix (dang gui) and Testudinis Plastrum (gui ban) as an aid to difficult deliveries.
- Clears damp-heat in the lower burner: for cases of damp-heat pouring downward manifesting as knee pain or lower back damp painful obstruction. It is also an auxiliary herb for painful urinary dribbling or vaginal discharge. Especially useful for painful urinary dribbling with stones accompanied by lower back pain and bloody urine.
    - With Jin Qian Cao (Lysimachiae/Desmodii/etc. Herba) for painful urinary dribbling, especially when associated with kidney stones accompanied by bloody urine and lower back pain.
    - With Angelicae sinensis Radix (dang gui) and Scutellariae Radix (huang qin) for hot painful urinary dribbling.
    - With Phellodendri Cortex (huang bai) and Atractylodis Rhizoma (cang zhu) for red, swollen, and painful joints of the lower extremities from downward-pouring of damp-heat, as in Three-Marvel Pill (san miao wan).

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
- "Cannot be consumed during pregnancy." (Essentials of Materia Medica Distinctions)
- Should not be used when joint pain or chest, abdomen, hypochondrium, and flank pain are not due to retained blood stasis, but rather to blood deficiency.
- It should not be used for excessive loss of postpartum lochia with abdominal pain due to deficiency.
- It should not be used when sores have already perforated. (Commentary on the Divine Husbandman's Classic of Materia Medica)
- This warning may seem unusual for a substance that "assists the growth of flesh."
- "If amenorrhea is only short term, and pregnancy is suspected, do not use it. Do not add it to upper burner herbs. It is forbidden where there is continuous bleeding." (Commentary on the Divine Husbandman's Classic of Materia Medica)

- "If there is diarrhea, dysenteric disorder, or Spleen deficiency, with soreness and pain in the legs and knees, it should not be used." (Transforming the Significance of Medicinal Substances) This is because it directs downward thus opposing the ascent of Spleen qi, so even if knee pain would seem to indicate its use, it is forbidden. Materia Medica of Combinations concurs: "It is forbidden for both insufficiency of middle burner qi and incontinence of urine."

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
Good quality consists of dry, fleshy, long roots with thin cork, a yellowish grey surface, and sweet taste. The crown should be cut off.

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
