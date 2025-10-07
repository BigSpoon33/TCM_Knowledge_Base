---
# 🔹 Core Metadata (Universal Fields)
id: "herb-20251001123706"
name: "Zhu Ru"
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
  hanzi: "竹茹"
  pinyin: "zhu ru"
  pharmaceutical: "Bambusae Caulis in Taeniam"
  english: "Bamboo Shavings"
  alternate_names: []

  # TCM Properties
  taste: [Sweet, slightly cold]
  temperature: "Slightly cold"
  channels: [Lung, Stomach, Gallbladder]

  # Clinical Information
  dosage: "4.5-9g"
  toxicity: "None"
  functions: [Clears and transforms phlegm-heat, Clears heat and stops vomiting]
  dui_yao: []

  # Additional Information
  constituents: [Phenolic compounds: *p*-hydroxybenzaldehyde, syringaaldehyde, coniferylaldehyde, phenol, cresol, guaiacol, 2,5-dimethoxy-*p*-benzoquinone, Organic acids: formic acid, acetic acid, benzoic acid, salicylic acid, Other constituents: 1,4-benzenedicarboxylic acid, 2'-hydroxyethylmethylester, amino acids, tannins, saponins, alkaloids, sugars, triterpenes]
  quality: "Good quality consists of yellowish green, soft, and pliable pieces, without wooden parts."
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

Circulating in the Lungs, *Bambusae Caulis in Taeniam* (zhu ru) scours hot-phlegm; entering the Stomach, it expels heat and stops nausea and reflux; entering the Gallbladder, it calms the spirit, releases constraint, and alleviates irritability. Thus the adage that *Bambusae Caulis in Taeniam* (zhu ru) is specifically indicated for cooling Lung heat, but is also valuable for calming the spirit and releasing constraint.

Transforming the Significance of Medicinal Substances provides the following description of this herb: "Its lightness can expel excess, its coolness can expel heat, and its bitterness can direct downward—an admirable herb for calming the spirit and relieving constraint!"

In Essays on Medicine Esteeming the Chinese and Respecting the Western, Zhang Xi-Chun describes some of the less commonly recognized applications of *Bambusae Caulis in Taeniam* (zhu ru):

As the bark of the bamboo, it is both cooling and directs downward; thus, while cooling the Lungs and facilitating [the removal of] phlegm, it disseminates and unblocks the fluid passageways of the Triple Burner, and below unblocks the Bladder. Therefore, it is an important herb for unblocking and facilitating the flow of urine, similar to bamboo leaves, but superior to the leaves in its power. It also excels at cooling heat in the Intestines and eliminates tenesmus and abdominal pain from dysenteric disorders. Because of its cooling and unblocking dissemination, those with swelling and pain due to trauma and blood stasis will find the swelling and pain reduced and the blood stasis transformed by taking it. Boiling in vinegar and rinsing the mouth [with the resulting liquid] can stop bleeding gums. The greenish outer bark of the tender bamboo must be used; the inner bark is less powerful.

---
---

## 🔑 TCM Properties

**Taste:** `= join(this.herb_data.taste, ", ")`
**Temperature:** `= this.herb_data.temperature`
**Channels Entered:** `= join(this.herb_data.channels, ", ")`

---

## ⚡ Functions & Actions

- Clears and transforms phlegm-heat: for heat in the Lungs with viscous sputum, stifling sensation in the chest, or coughing up blood. Also for Gallbladder fire harboring phlegm and phlegm-heat.
  - With *Trichosanthis Fructus* (gua lou) and *Scutellariae Radix* (huang qin) for cough due to heat in the Lungs.
  - With *Aurantii Fructus Immaturus* (zhi shi) and *Pinelliae Rhizoma Preparatum* (zhi ban xia) for insomnia, palpitations, and irritability due to intermixed phlegm and heat leading to disharmony between the Gallbladder and Stomach, with a stifling sensation in the chest, irritability, restlessness, and insomnia. See Warm the Gallbladder Decoction (wen dan tang).
- Clears heat and stops vomiting: for vomiting of bitter or sour matter due to heat in the Stomach with bad breath, aversion to heat, and a yellow, greasy tongue. The Stomach heat can be due to either excess or deficiency. This herb is very effective at stopping vomiting and can be used, with other appropriate herbs, in treating other types of vomiting including that associated with morning sickness.
  - With *Coptidis Rhizoma* (huang lian) and *Citri Reticulatae Pericarpium* (chen pi) for phlegm-heat in the Stomach with a stifling sensation in the epigastrium and vomiting.
  - With *Dendrobii Herba* (shi hu) for hunger with an inability to eat very much, recurring nausea and vomiting or dry retching, thirst, and dry mouth due to Stomach yin insufficiency.
  - With *Phragmitis Rhizoma* (lu gen) for irritability, thirst, and vomiting due to the depletion of fluids caused by a heat disorder.
  - With *Citri Reticulatae Pericarpium* (chen pi), *Zingiberis Rhizoma Recens* (sheng jiang), and *Ginseng Radix* (ren shen) for vomiting or hiccough due to Stomach deficiency with heat.
  - With *Zingiberis Rhizomatis Succus* (jiang zhi), both to mitigate its cold properties and enhance its ability to stop vomiting. This is especially useful in treating morning sickness, often with the addition of *Atractylodis Macrocephalae Rhizoma* (bai zhu) and *Perillae Caulis* (zi su geng).

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
"Bamboo is cold by nature, and [its use] is prohibited where there is nausea and vomiting from Stomach cold, or vomiting due to externally-contracted cold with excessive consumption of food." (Harm and Benefit in the Materia Medica)

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
Good quality consists of yellowish green, soft, and pliable pieces, without wooden parts.

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
