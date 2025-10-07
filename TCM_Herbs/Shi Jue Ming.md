---
# 🔹 Core Metadata (Universal Fields)
id: "herb-20251001123706"
name: "Shi Jue Ming"
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
  hanzi: "石决明"
  pinyin: "Shí Jué Míng"
  pharmaceutical: "Haliotidis Concha"
  english: "Abalone Shell"
  alternate_names: []

  # TCM Properties
  taste: [Salty, cold]
  temperature: "cold"
  channels: [Kidney, Liver]

  # Clinical Information
  dosage: "15-30g"
  toxicity: "None"
  functions: [Drains Liver fire and anchors and sedates the Liver yang, Improves the vision and causes superficial visual obstructions to recede]
  dui_yao: []

  # Additional Information
  constituents: [Inorganic constituents: carbonates (>90%), phosphates and silicates of Ca (>90%), Na, Al, Ti, Mn, Fe, Cr, Mg, Sr, Ba, Zn, Cu, Ni, Cl, I, S, Other constituents: conchiolin, amino acids]
  quality: "Good quality has a thick shell (0.6-0.9cm), the outer surface is clean and free of concrements, the inner surface has a pearl-like luster, and is multicolored."
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

(Shi jue ming) Salty, cold, and heavy, Haliotidis Concha enters the Liver channel to cool the Liver and calm ascendant Liver yang. The Liver governs wind, and the orifice of the Liver is the eyes; if blood is deficient and the Liver is hot, wind-fire blazes upward and the Liver yang follows it causing dizziness, vertigo, and headaches. In severe cases it will lead to insidous onset of loss of vision without visible physical changes to the eye. Not only does Haliotidis Concha (shi jue ming) cool the Liver and anchor the Liver yang, it also enriches and nourishes the Liver yin, and thus addresses both the branch manifestation and the basic root of the condition.

Commentary on the Divine Husbandman's Classic of Materia Medica states that it is a medicinal of the leg terminal yin channel, the orifice of which is the eyes: 'when the eyes obtain blood, vision is possible.' If blood is deficient, and there is heat, insidous onset of loss of vision without visible physical changes to the eye, and superficial visual obstructions, are generated. Salty coldness enters the blood to eliminate heat, and therefore this governs eye diseases.

Master Shen's Book for Revering Life says that "Haliotidis Concha (shi jue ming) greatly tonifies the Liver yin: when the Liver channel is deficient, one definitely cannot do without it."

---
---

## 🔑 TCM Properties

**Taste:** `= join(this.herb_data.taste, ", ")`
**Temperature:** `= this.herb_data.temperature`
**Channels Entered:** `= join(this.herb_data.channels, ", ")`

---

## ⚡ Functions & Actions

- Drains Liver fire and anchors and sedates the Liver yang: for Liver fire and ascendant Liver yang patterns with such symptoms as headache, dizziness, and red eyes. Commonly used for hypertension with ascendant Liver yang.
    - With Paeoniae Radix alba (bai shao), Rehmanniae Radix (sheng di huang), and Ostreae Concha (mu li) for Liver yin deficiency with ascendant yang, as in Ass-Hide Gelatin and Egg Yolk Decoction (e jiao ji zi huang tang).
    - With Prunellae Spica (xia ku cao), Astragali Radix (huang qi), and Chrysanthemi Flos (ju hua) for Liver fire or ascendant Liver yang with heat signs, dizziness, headache, irritability, and insomnia.
- Improves the vision and causes superficial visual obstructions to recede: for Liver heat patterns that affect the eyes causing photophobia, pterygium or other superficial visual obstructions, red eyes, and blurred vision.
    - With Chrysanthemi Flos (ju hua), Cassiae Semen (jue ming zi), and Prunellae Spica (xia ku cao) for eye redness, swelling, and pain due to the upward-blazing of Liver fire.
    - With Rehmanniae Radix preparata (shu di huang) and Corni Fructus (shan zhu yu) for impaired vision due to Liver and Kidney yin deficiency.
    - With Cicadae Periostracum (chan tui) for chronic progressive loss of vision and night blindness.
    - With Buddlejae Flos (mi meng hua) and Eriocauli Flos (gu jing cao) for pterygium due to wind-heat.
- Recently also used for increased gastric acidity, and, topically, for bleeding due to trauma.

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
Use with caution in those with cold from deficiency of the Spleen and Stomach with reduced appetite and loose stools.

"Overconsumption makes people cold in the middle." (Harm and Benefit in the Materia Medica)

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
Good quality has a thick shell (0.6-0.9cm), the outer surface is clean and free of concrements, the inner surface has a pearl-like luster, and is multicolored.

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
