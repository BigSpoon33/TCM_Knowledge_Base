---
# 🔹 Core Metadata (Universal Fields)
id: "herb-20251001123706"
name: "Yin Yang Huo"
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
  hanzi: "淫羊藿"
  pinyin: "yín yáng huò"
  pharmaceutical: "Epimedii Herba"
  english: "aerial parts of epimedium"
  alternate_names: []

  # TCM Properties
  taste: [Acrid, sweet]
  temperature: "warm"
  channels: [Kidney, Liver]

  # Clinical Information
  dosage: "3-9g"
  toxicity: "In rare cases, such side effects as dry mouth, nausea, vomiting, dizziness, nosebleed, and abdominal distention have been reported."
  functions: [Tonifies the Kidneys and fortifies the yang, Dispels wind-cold-dampness and warms and unblocks the flow of yang qi]
  dui_yao: []

  # Additional Information
  constituents: [icariin, des-0-methyl-icariin, icariside I, icariside II, ikarisoside C, baohuoside I, baohuoside II, sagittatoside B, magnoflorin, volatile oil, ceryl alcohol, bilobanol, hentriacontane, phytosterol, palmitic acid, stearic acid, oleic acid, epimedin A, epimedin B, epimedin C, epimedokoreanoside I, epimedokoreanoside II, epimedoside A, epimedoside C, ikarisoside A, liquiritigenin, isoliquiritigenin, tricin, quercetin, luteolin, hyperin, ikarisoside F (diphylloside A), 3-hydroxy-2-methylpyrane, salidroside, p-hydroxybenzoic acid, daucosterol, emodin, epimedoside C, baohuoside IV, baohuoside VI, hyperoside, rouhuoside, icaritin-3-0-a-rhamnoside, anhydroicaritin-3-0-a-rhamnoside, saggitatin A, saggitatin B, saggitatoside A, saggitatoside B, saggitatoside C, epimedin D, epimedin E, icariside A1, icariside B1, icariside B2, icariside B6, icariside B7, icariside B9, icariside E5, icariside E6, icariside H1, icariside H2, icarisidin B, isoquercetin, icariol A1, icariol A2, dilignol, β-sitosterol, β-sitosterolglucoside, wushanicariin, baohuoside VI, tannins, Fixed oil: triglycerides of palmitic acid, oleic acid and linoleic acid, 8-sitosteryl palmitate, daucosterol, campesterol, aliphatic hydrocarbons, Amino acids: 15 different amino acids, the main constituents being aspartic acid, proline, serine, alanine]
  quality: "Good quality has many leaves, and only a few stalks. The leaves should be yellowish green and unfragmented. Good quality consists of thick, heavy, and hard stems with an oily surface on cross section."
  text_first_appeared: "Divine Husbandman's Classic of the Materia Medica"

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

The sweet warmth of Epimedii Herba (*yin yang huo*) tonifies the fire at the gate of vitality and fortifies the Kidney yang, while its acrid warmth expels wind-dampness. Tonification of the Kidney yang enables it to treat impotence, spermatorrhea, and urinary frequency. Internally, reinforcement of the Kidney yang strengthens the bones, while externally, wind-dampness is dispersed so that painful obstruction is unblocked. Thus, not only are these pathogens expelled, but the injury done by them is repaired.

Materia Medica of Ri Hua-Zi says that it treats "every type of wind-cold consumptive qi, spasms and contractures of the sinews and bones, loss of feeling in the four extremities; and it tonifies the lower back and knees." Many materia medica texts record that it is good in wine, and that Dioscoreae Rhizoma (*shan yao*) enhances its functions.

Rectification of the Meaning of Materia Medica also says that it can be used as a wash for sores around the genitals: "Acrid-drying can expel damp-heat, in this it is like Cnidii Fructus (*she chuang zi*) as a wash for itchy sores."

The Divine Husbandman's Classic of Materia Medica states that the herb is "acrid, cold, governs impotence, infertility, pain in the penis, facilitates urination, augments the power of qi, strengthens resolve." Most materia medica texts since that time have objected to its characterization as a cold herb. For example, Commentary on the Divine Husbandman's Classic of Materia Medica says that its "temperature is warm and it is non-toxic. The Divine Husbandman's statement that it is cold is incorrect." Li Shi Zhen, in the Grand Materia Medica, agrees:

Epimedii Herba (*yin yang huo*) is sweet in flavor and aromatic; its nature is warm, not cold [as the Divine Husbandman's Classic of Materia Medica states]. It augments the essential qi, and is an herb of the arm and leg yang brightness, Triple Burner, and gate of vitality. It is appropriate for those with insufficiency of true yang.

The ability of this herb to assist the memory and resolve is recorded in many materia medica texts, including the Classic of Materia Medica, as well as the Materia Medica of Ri Hua-Zi, which says that it treats "old-age confusion and middle-age forgetfulness."

---
---

## 🔑 TCM Properties

**Taste:** `= join(this.herb_data.taste, ", ")`
**Temperature:** `= this.herb_data.temperature`
**Channels Entered:** `= join(this.herb_data.channels, ", ")`

---

## ⚡ Functions & Actions

Tonifies the Kidneys and fortifies the yang: for patterns of Kidney yang deficiency with such symptoms as impotence, infertility, urinary frequency, forgetfulness, withdrawal, and painful cold lower back and knees.
    *   With Rehmanniae Radix preparata (*shu di huang*), Testudinis Plastri Colla (*gui ban jiao*), and Hominis Placenta (*zi he che*) for impotence accompanied by coldness of the lower back and legs. This is both an example of using other substances to ameliorate the dry, yin-consuming nature of this herb, which can injure the yin and essence, and of 'seeking yang in the yin' (阴中求阳 yīn zhōng qiú yáng), as in most cases of severe yang deficiency there is also exhaustion of the essence.
    *   With Curculiginis Rhizoma (*xian mao*), Phellodendri Cortex (*huang bai*), and Anemarrhenae Rhizoma (*zhi mu*) for menopausal symptoms such as facial pallor, lower back pain, nocturia, menstrual irregularity, and dizziness from Liver and Kidney yin deficiency, as in Two-Immortal Decoction (*er xian tang*).
    *   With Schisandrae Fructus (*wu wei zi*), Lycii Fructus (*gou qi zi*), and Astragali complanati Semen (*sha yuan zi*) for impotence and infertility associated with Kidney deficiency.
*   Dispels wind-cold-dampness and warms and unblocks the flow of yang qi: for wind-cold-damp painful obstruction with such symptoms as spasms or cramps in the hands and feet, joint pain, and numbness in the extremities. Also used for the contractures, numbness, or hemiplegia following wind-stroke.
    *   With Taxilli Herba (*sang ji sheng*) for painful obstruction, especially paralysis and pain of the lower extremities, or muscular contracture and numbness of the extremities.
    *   With Notopterygii Rhizoma seu Radix (*qiang huo*), Saposhnikoviae Radix (*fang feng*), and Aconiti Radix lateralis preparata (*zhi fu zi*) for wind-cold-damp painful obstruction with joint pain and difficulty in movement.

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
Contraindicated in those with loose stools, unstable essence, and overabundant fire causing constipation, excessive erections, and deficiency distention of the Heart qi.
*   Contraindicated in those with fire from yin deficiency. This herb should not be taken as a decoction over a long period of time, as it can injure the yin. See toxicity below.

Encountering the Sources of the Classic of Materia Medica observes that wine made from this herb is an important remedy for hemiplegia, and can be taken by itself, "but if there is yin deficiency with spermatorrhea or persistent erections, it is forbidden to take it."

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
Good quality has many leaves, and only a few stalks. The leaves should be yellowish green and unfragmented. Good quality consists of thick, heavy, and hard stems with an oily surface on cross section.

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
