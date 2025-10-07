---
# 🔹 Core Metadata (Universal Fields)
id: "herb-20251001123706"
name: "Tian Men Dong"
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
  hanzi: "天門冬"
  pinyin: "tiān mén dōng"
  pharmaceutical: "Asparagi Radix"
  english: "Asparagus Root"
  alternate_names: []

  # TCM Properties
  taste: [Sweet, bitter]
  temperature: "very cold"
  channels: [Kidney, Lung]

  # Clinical Information
  dosage: "6-12g"
  toxicity: "Contraindicated in those with diarrhea from deficiency or cold."
  functions: [Nourishes the Kidney yin and clears Lung heat, Moistens the Lungs, nourishes the Kidneys, and generates fluids]
  dui_yao: []

  # Additional Information
  constituents: [Amino acids: asparagine, serine, citrullin, threonine, proline, glycine, alanine, valine, methionine, leucine, isoleucine, phenylalanine, tyrosine, aspartic acid, glutamic acid, arginine, histidine, lysine, Saponins: Asp-IV, V, VI, VII (sapogenins: yamogenin, diosgenin, sarsapogenin, smilagenin), methylprotodioscin, pseudoprotodioscin, Polysaccharides: asparagus polysaccharide A, B, C, D, Other constituents: 5-methoxymethylfurfural, β-sitosterol]
  quality: "Good quality consists of thick, full, compact, yellowish white, and translucent roots."
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

Sweet, cold, clearing, and moistening, Asparagi Radix (tian men dong) enters the Lung and Kidney channels. It is best at enriching the Lung and Kidney yin, but also clears heat due to yin deficiency. It is most often used in the treatment of disorders such as cough due to Lung heat injuring the yin, wasting and thirsting disorder due to internal heat from yin deficiency injuring the yang fluids, and constipation due to Intestinal dryness.

Essays on Medicine Esteeming the Chinese and Respecting the Western observes that it is sweet, slightly acrid, and cooling, full of fluids, and rich, slippery, and moistening. Its color is yellow with whiteness; it enters the Lungs to cool dry heat, thus it excels at facilitating [the removal of] phlegm and calming coughs. It enters the Stomach to reduce excess heat, and thus generates fluids and alleviates thirst. With a nature that is rich in yang fluids, slippery with yin fluids, it unblocks and facilitates the movement of both stool and urine, reaches throughout the channels and collaterals, and although it is a yin-enriching herb, in fact, it also can tonify and augment the qi level.

---
---

## 🔑 TCM Properties

**Taste:** `= join(this.herb_data.taste, ", ")`
**Temperature:** `= this.herb_data.temperature`
**Channels Entered:** `= join(this.herb_data.channels, ", ")`

---

## ⚡ Functions & Actions

- Nourishes the Kidney yin and clears Lung heat: for yin deficiency with heat signs in the upper burner, typically dryness of the mouth.
- Also for dry Lung patterns with such signs as dry mouth and a cough that is either nonproductive or productive of scanty, viscous sputum that may be streaked with blood.
- With Ophiopogonis Radix (mai men dong) for cough, thirst, and other symptoms associated with yin deficiency and injured fluids.
- Add Rehmanniae Radix (sheng di huang), Fritillariae cirrhosae Bulbus (chuan bei mu), and Lilii Bulbus (bai he) for chronic, dry cough due to heat with difficult-to-expectorate sputum associated with Lung yin deficiency, as in Moonlight Pill (yue hua wan).
- Add Panacis quinquefolii Radix (xi yang shen) and Rehmanniae Radix preparata (shu di huang) for qi and yin deficiency with dry throat, thirst, low-grade fever, and debility, as in the aftermath of a severe illness.
- With Mori Folium (sang ye), Adenophorae Radix (nan sha shen), and Armeniacae Semen (xing ren) for warm-dryness with fever, slight aversion to wind, cough with blood-streaked sputum, and chest pain.
- With Mori Cortex (sang bai pi), Lycii Cortex (di gu pi), and Fritillariae thunbergii Bulbus (zhe bei mu) for cough and wheezing with thick, yellow, viscous sputum due to blazing Lung fire.
- Moistens the Lungs, nourishes the Kidneys, and generates fluids: for Lung and Kidney yin deficiency, especially wasting and thirsting disorder and consumption, with low-grade afternoon fever. Because it enters the Lungs and Kidneys it can be used for upper, middle, and lower burner types of wasting and thirsting disorders. Also for constipation due to dry Intestines.
- With Asini Corii Colla (e jiao) for dryness affecting the Lungs and Kidneys with such symptoms as emaciation, tidal fevers, parched throat, and a dry cough with blood-streaked phlegm.
- With Ophiopogonis Radix (mai men dong), Trichosanthis Radix (tian hua fen), and Anemarrhenae Rhizoma (zhi mu) for upper burner wasting and thirsting disorder.
- With Gypsum fibrosum (shi gao), Rehmanniae Radix (sheng di huang), and Coptidis Rhizoma (huang lian) for middle burner wasting and thirsting disorder.
- With Anemarrhenae Rhizoma (zhi mu), Phellodendri Cortex (huang bai), and Corni Fructus (shan zhu yu) for lower burner wasting and thirsting disorder.
- With Scrophulariae Radix (xuan shen), Ophiopogonis Radix (mai men dong), and Rehmanniae Radix (sheng di huang) for constipation due to yin deficiency.
- With Angelicae sinensis Radix (dang gui), Polygoni multiflori Radix preparata (zhi he shou wu), and a large dosage of Paeoniae Radix alba (bai shao) for constipation due to blood deficiency.

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
Extension of the Materia Medica notes that it "has its best effect in the treatment of Lung heat. Its flavor is bitter, but it only drains, it does not attack; those who are mainly cold should avoid it."

The Changsha Explanation of Medicines warns that:

Its nature is cold, slippery, damp, and moistening; it greatly subdues the Spleen and Stomach and drains the Large Intestine. It should definitely be avoided by those with yang exhaustion and flourishing yin, or earth dampness and loose stools.

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
Good quality consists of thick, full, compact, yellowish white, and translucent roots.

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
