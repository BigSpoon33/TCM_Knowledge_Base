---
# 🔹 Core Metadata (Universal Fields)
id: "herb-20251001123706"
name: "Pi Pa Ye"
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
  hanzi: "枇杷葉"
  pinyin: "pi pa ye"
  pharmaceutical: "Eriobotryae Folium"
  english: "loquat leaf, eriobotrya"
  alternate_names: []

  # TCM Properties
  taste: [bitter, neutral]
  temperature: "Neutral"
  channels: [Lung, Stomach]

  # Clinical Information
  dosage: "6-15g"
  toxicity: "For internal use the fuzz should be removed from the leaves, as the unprocessed leaves are highly irritating to the mucosa and may aggravate a cough, causing edema and spasms of the larynx."
  functions: [Transforms phlegm, Clears Lung heat, Redirects Lung qi downward, Harmonizes the Stomach, Clears Stomach heat]
  dui_yao: []

  # Additional Information
  constituents: [Volatile oil: nerolidol, farnesol, α-pinene, β-pinene, myrcene, p-cymene, linalool, linalool oxide, α-ylangene, α-farnesene, β-farnesene, camphor, nerol, geraniol, α-cadinol, cis-β-hexenol, cis-γ-hexenol, Triterpenes: ursolic acid, 2α-hydroxyursolic acid, 6α,19α-dihydroxyursolic acid, maslinic acid, methyl maslinate, euscaphic acid, tormentic acid, 23-cis-/ 23-trans-p-coumaroyltormentic acid, 3-O-trans-caffeoyltormentic acid, 3-O-trans-p-coumaroyltormentic acid, 3-O-trans-p-coumaroylrotundic acid, Organic acids: citric acid, malic acid, tartaric acid, Glycosides: amygdalin, nerolidol-3-O-α-L-rhamnopyranosyl (1→2)-β-D-glucopyranoside, nerolidol-3-O-α-L-rhamnopyranosyl (1→4)-β-D-glucopyranoside, nerolidol-3-O-α-L-rhamnopyranosyl (1→4)-α-L-rhamnopyranosyl (1→6)-β-D-glucopyranoside, quercetin-3-glucoside, hyperoside, Other constituents: ceryl alcohol, ceryl palmitate, amino acids, saponins, proteins, tannins, cryptoxanthin, vitamin B1]
  quality: "Good quality consists of large, green or reddish brown (exposure to sunlight turns the green leaves brown) unfragmented leaves. Yellow leaves are of inferior quality."
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

Best at directing rebellious qi downward, Eriobotryae Folium (枇杷葉 pi pa ye) cools Lung heat to transform phlegm and alleviate cough; it also cools Stomach heat, alleviates nausea, and quenches restless thirst. Thus, by cooling Lung heat and directing Lung qi downward, Eriobotryae Folium (枇杷葉 pi pa ye) can be used for cough, coughing of blood, or nosebleed due to Lung disturbance from wind-warmth, warm-heat, pathogenic summerheat, or dry-heat. It can likewise be used to direct turbid pathogens downward and out of the Stomach in cases of continuous vomiting due to externally-contracted damp-warmth or other contagious toxins.
The Grand Materia Medica describes the main therapeutic action of this herb:
Eriobotryae Folium (枇杷葉 pi pa ye), in treating Lung and Stomach disorders, is generally used for its ability to direct rebellious qi downward. When qi is driven downward, fire will then descend and phlegm is smoothly [eliminated]. Thus, rebelliousness is curbed, nausea is quelled, thirst is quenched, and the cough is alleviated.

---
---

## 🔑 TCM Properties

**Taste:** `= join(this.herb_data.taste, ", ")`
**Temperature:** `= this.herb_data.temperature`
**Channels Entered:** `= join(this.herb_data.channels, ", ")`

---

## ⚡ Functions & Actions

• Transforms phlegm, clears Lung heat, and redirects Lung qi downward: for Lung heat or Lung dryness patterns with cough and wheezing.
- With Armeniacae Semen (杏仁 xing ren) for Lung heat induced nonproductive cough, or cough with viscous sputum that is difficult to expectorate, accompanied by chest pain and a dry throat. Often Coptidis Rhizoma (黃連 huang lian), Mori Cortex (桑白皮 sang bai pi), and Gardeniae Fructus (梔子 zhi zi) are added.
- With Mori Cortex (桑白皮 sang bai pi), Platycodi Radix (桔梗 jie geng), and Stemonae Radix (百部 bai bu) for cough and wheezing from dry heat marked by sputum that is difficult to expectorate, dry mouth, and a red tongue.
• Harmonizes the Stomach, clears Stomach heat, and redirects Stomach qi downward: for nausea, vomiting, hiccough, and belching due to Stomach heat.
- With Scutellariae Radix (黃芩 huang qin) and Cyperi Rhizoma (香附 xiang fu) for Stomach heat-induced vomiting and belching.
- With Imperatae Rhizoma (白茅根 bai mao gen) for vomiting or vomiting of blood due to a heat disorder.
- With Bletillae Rhizoma (白芨 bai ji) for coughing of blood streaked sputum.
- With Phragmitis Rhizoma (蘆根 lu gen) for irritability and vomiting due to injury of the fluids from a warm-heat pathogen disease.
- With Pinelliae Rhizoma preparatum (制半夏 zhi ban xia) to alleviate nausea and calm the Stomach.

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
Encountering the Sources of the Classic of Materia Medica notes that although Eriobotryae Folium (枇杷葉 pi pa ye) is commonly used for cough, nausea, and vomiting, "it is still contraindicated for nausea and vomiting from Stomach cold, or cough due to wind-cold." These conditions can still be treated with this herb, however, if the leaves are prepared with ginger, and other appropriate herbs are added.
Use with caution for cough or vomiting due to cold.

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
Good quality consists of large, green or reddish brown (exposure to sunlight turns the green leaves brown) unfragmented leaves. Yellow leaves are of inferior quality.

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
