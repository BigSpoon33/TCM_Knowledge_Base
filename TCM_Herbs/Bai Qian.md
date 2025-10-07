---
# 🔹 Core Metadata (Universal Fields)
id: "herb-20251001123706"
name: "Bai Qian"
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
  hanzi: "白前"
  pinyin: "Bai Qian"
  pharmaceutical: "Cynanchi Stauntonii Rhizoma"
  english: "cynanchum root and rhizome"
  alternate_names: []

  # TCM Properties
  taste: [Acrid, sweet]
  temperature: "Slightly warm"
  channels: [Lung]

  # Clinical Information
  dosage: "3-9g"
  toxicity: "This herb irritates the gastric mucosa and should not be given to those with gastric disorders or bleeding diathesis."
  functions: [Redirects the qi downward, dispels phlegm, and stops cough]
  dui_yao: []

  # Additional Information
  constituents: [Triterpene saponines: glaucoside A-K, glaucogenin A, B, C, D, glaucogenin C momo-D-thevetoside, neoglaucogenin, neoglaucoside A, Other constituents: glaucobiose, hancockinol, β-sitosterol, C24-C30 fatty acids]
  quality: "Good quality is yellowish white with large rhizomes and the cross section is whitish and powdery."
  text_first_appeared: "Miscellaneous Records of Famous Physicians"

  # Source References
  bensky_pdf: "627"
  bensky_page: "49"

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

*Cynanchi stauntonii* Rhizoma (*bai qian*) is acrid, bitter, sweet, slightly warming, and enters the Lung channel. A primary characteristic is its ability to direct qi downward. Its efficacy is related to the often quoted adage that "When qi descends, phlegm and thin mucus will disperse by themselves, and the cough will naturally cease." Because of this ability, *Cynanchi stauntonii* Rhizoma (*bai qian*) is known as an outstanding herb for Lung patients. Whenever profuse phlegm obstructs the Lungs leading to symptoms of cough, sensations of fullness in the chest, and wheezing, irrespective of whether the condition is hot or cold, it can be used, if properly combined with other herbs. This may be one reason that it is sometimes regarded as a neutral herb.

An interesting quality mentioned in various materia medica texts is the ability of this herb to address qi gathered in the throat with audible phlegm. For example, the New Edition of Mei's Collected Empiric Formulas recommends powdered *Cynanchi stauntonii* Rhizoma (*bai qian*), taken with wine, to treat chronic cough that prevents sleep, with the rattling sound of phlegm in the throat. The Tang Materia Medica notes that the herb "primarily treats ascending qi rushing up into the throat, threatening to stop breathing." And Zhang Shan-Lei observes that "The reason that *Cynanchi stauntonii* Rhizoma (*bai qian*) can alleviate coughing lies in its ability to calm rebellious qi and prevent turbid qi below the diaphragm from rising up and accosting the Lungs."

---
---

## 🔑 TCM Properties

**Taste:** `= join(this.herb_data.taste, ", ")`
**Temperature:** `= this.herb_data.temperature`
**Channels Entered:** `= join(this.herb_data.channels, ", ")`

---

## ⚡ Functions & Actions

- Redirects the qi downward, dispels phlegm, and stops cough: for cough with copious sputum and gurgling in the throat.
- This is a very important herb for Lung qi blockage and stagnation.
- Is used for disorders of excess with copious sputum that is difficult to expectorate, as well as wheezing.
- Although slightly warm, it is not drying.
    - With Asteris Radix (*zi wan*) and Pinelliae Rhizoma preparatum (*zhi ban xia*) for cough and wheezing accompanied by sputum that is difficult to expectorate, respiratory difficulty, and gurgling sounds in the throat due to phlegm dampness obstructing the Lungs.
    - With Mori Cortex (*sang bai pi*) and Lycii Cortex (*di gu pi*) for chronic productive cough due to Lung heat.
    - With Platycodi Radix (*jie geng*) and Schizonepetae Herba (*jing jie*) for cough associated with externally-contracted wind-cold-phlegm obstruction, as in Stop Coughing Powder (*zhi sou san*).
    - With Peucedani Radix (*qian hu*) for cough with profuse phlegm due to externally-contracted wind-heat.
    - With Atractylodis Rhizoma (*cang zhu*) for dampness induced edema.

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
In Convenient Reader of Materia Medica, Zhang Bing Cheng notes that it is "Specific for Lung patients, best at directing qi downward and causing phlegm to descend; if the Lungs do not have accumulated excess, it is inappropriate."

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
Good quality is yellowish white with large rhizomes and the cross section is whitish and powdery.

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
