---
# 🔹 Core Metadata (Universal Fields)
id: "herb-20251001123706"
name: "Bai Hua She"
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
  hanzi: "None"
  pinyin: "None"
  pharmaceutical: "Agkistrodon/Bungarus"
  english: "None"
  alternate_names: []

  # TCM Properties
  taste: [Sweet, salty, warm, toxic]
  temperature: "None"
  channels: [Liver]

  # Clinical Information
  dosage: "3-9g in decoctions, 1-1.5g in pills or powders"
  toxicity: "None"
  functions: [Powerfully unblocks the channels and extinguishes wind, Dispels wind from the skin, Dispels wind from the sinews and settles jitteriness and convulsions]
  dui_yao: []

  # Additional Information
  constituents: []
  quality: "None"
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

Agkistrodon (qi she) Sweet and salty, enters the blood aspect of the Liver channel. It excels at venting wind from the bones, sinews, and skin, attacking toxins, and halting spasms. Internally, it reaches the organs, but its effects also extend out to the skin, giving it a very wide range of application. It is therefore an essential medicinal to powerfully extinguish and expel wind toxin that has accumulated in the blood level. It is effective for weakness and numbness of the limbs, skin rashes, dermatosis, tremors, spasms and seizures, such as muscular tetany.

The Grand Materia Medica notes that it can vent the bones and search out wind, calm jitteriness and settle spasms, and is thus an important substance in the treatment of wind painful obstruction, convulsions, scabies, and noxious sores. With its ability to reach the yin organs, and extend out to all areas of the skin, there is no place it does not influence.

Its best quality is the ability to track down and eliminate wind, as explained in Detailed Materia Medica: "This is because a snake's nature excels at rapid flight, so it guides medicinals to places where wind illnesses are present."

Zhang Jie-Bin notes that this snake is particularly quick in movement. Thus, it is an excellent choice for wind toxin in the exterior tissues, sinews, or bones, or for convulsions and spasms due to internal wind.

---
---

## 🔑 TCM Properties

**Taste:** `= join(this.herb_data.taste, ", ")`
**Temperature:** `= this.herb_data.temperature`
**Channels Entered:** `= join(this.herb_data.channels, ", ")`

---

## ⚡ Functions & Actions

- **Powerfully unblocks the channels and extinguishes wind:** for chronic wind-dampness with numbness and weakness of the limbs and cramping of the sinews. Generally used for stubborn cases.
    - With Notopterygii Rhizoma seu Radix (qiang huo), Saposhnikoviae Radix (fang feng), and Gentianae macrophylla Radix (qin jiao) for joint pain, weakness, and stiffness due to wind-dampness.
- **Dispels wind from the skin:** for dermatosis, numbness of the skin, or any kind of rash.
    - With Angelicae sinensis Radix (dang gui), Polygoni multiflori Radix preparata (zhi he shou wu), and Paeoniae Radix alba (bai shao) for chronic rashes.
- **Dispels wind from the sinews and settles jitteriness and convulsions:** for any kind of spasms, tremors, or seizures. Can be used for facial paralysis or hemiplegia due to wind stroke.
    - With Scorpio (quan xie), Schizonepetae Herba (jing jie), and Angelicae sinensis Radix (dang gui) as a medicinal liquor for facial paralysis, aphasia, and hemiplegia due to wind-stroke.
    - With Zaocys (wu shao she) and Scolopendra (wu gong) for muscular tetany.

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
Use with caution in those with yin deficiency and dry blood, or wind from blood deficiency. See Toxicity below.

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
-
-

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
