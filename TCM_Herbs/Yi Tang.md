---
# 🔹 Core Metadata (Universal Fields)
id: "herb-20251001123706"
name: "Malt Sugar / Yi Tang"
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
  hanzi: "饴糖"
  pinyin: "Yí Táng"
  pharmaceutical: "Maltosum"
  english: "Malt sugar, maltose"
  alternate_names: []

  # TCM Properties
  taste: [Sweet]
  temperature: "Slightly warm"
  channels: [Lung, Spleen, Stomach]

  # Clinical Information
  dosage: "15-60g. Do not cook in decoctions, but take with the strained decoction."
  toxicity: "None"
  functions: [Tonifies the Spleen and augments the qi, Tonifies the middle burner qi and alleviates pain, Moistens the Lungs and stops coughs]
  dui_yao: []

  # Additional Information
  constituents: []
  quality: "Good quality consists of a yellowish brown, highly viscous, and very sticky mass with a sweet taste."
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

The Changsha Explanation of Medicines provides perhaps the best summary of the actions of Maltosum (*yi tang*): "Tonifies the Spleen and Stomach, transforms the Stomach qi, generates fluids, nourishes the blood, moderates interior urgency, alleviates abdominal pain." However, it is the Miscellaneous Records of Famous Physicians that sets forth the classical definition of its indications: "Primarily tonifies consumptive deficiency, alleviates thirst, and expels blood."

In Commentary on the Divine Husbandman's Classic of Materia Medica, Miao Xi-Yong elaborates:

"[It] is sweet to enter the Spleen, and because rice and wheat are both Spleen and Stomach nourishing substances, it primarily tonifies consumptive deficiency, precisely the reason it is used [Zhang] Zhong-Jing's Minor Construct the Middle Decoction (*xiao jian zhong tang*). Fire in the Lungs and Stomach causes thirst, and when fire blazes upward it forces the blood into chaotic movement, causing spitting up of blood. Sweetness can moderate the manifestation of fire, so that by directing fire downward, thirst is alleviated and bleeding is eliminated."

Records of Thoughtful Differentiation of Materia Medica observes:

"Sowing upon the earth produces sweetness, and Maltosum (*yi tang*) is the quintessence of the quintessence of the crop. Spleen earth resides in the middle. If there is consumptive deficiency, one should construct the middle, but in constructing the middle there should be no veering laterally: only Maltosum (*yi tang*) [of all the medicinals] has this focus. Thus, when the sage [Zhang] Zhong-Jing named Minor Construct the Middle Decoction (*xiao jian zhong tang*), the formula had to include Maltosum (*yi tang*), for without it, it would not have been given that name."

---
---

## 🔑 TCM Properties

**Taste:** `= join(this.herb_data.taste, ", ")`
**Temperature:** `= this.herb_data.temperature`
**Channels Entered:** `= join(this.herb_data.channels, ", ")`

---

## ⚡ Functions & Actions

- **Tonifies the Spleen and augments the qi:** for overexertion that injures the Spleen with shortness of breath and reduced appetite.
    - With *Codonopsis Radix* (dang shen) and *Glycyrrhizae Radix preparata* (zhi gan cao) for insufficiency of the middle qi with shortness of breath, fatigue, and reduced appetite.
- **Tonifies the middle burner qi and alleviates pain:** for abdominal pain due to cold from deficiency of the middle burner accompanied by excessive salivation, a pale tongue with a white coating, and a deep, slow pulse.
    - With *Cinnamomi Ramulus* (gui zhi), *Paeoniae Radix alba* (bai shao), and *Glycyrrhizae Radix* (gan cao) for abdominal pain due to cold from deficiency of the middle burner that responds favorably to pressure and is somewhat alleviated after eating. This combination is also used for externally-contracted wind-cold in weak patients suffering from chronic illness, as in Minor Construct the Middle Decoction (*xiao jian zhong tang*).
    - Add *Astragali Radix* (huang qi) for severe deficiency. This combination can also be used to speed postoperative recovery or treat allergies.
    - Add *Angelicae sinensis Radix* (dang gui) for concurrent blood deficiency.
    - With *Zingiberis Rhizoma* (gan jiang) and *Zanthoxyli Pericarpium* (hua jiao) for deficiency of the middle yang with ascendant yin marked by abdominal pain, cold limbs, and vomiting, as in Major Construct the Middle Decoction (*da jian zhong tang*).
- **Moistens the Lungs and stops coughs:** for dry, nonproductive coughs with labored, slow breathing, and a weak voice due to Lung deficiency.
    - With *Stemonae Radix* (bai bu) and *Armeniacae Semen* (xing ren) for dry, nonproductive coughs characterized by a weak voice and wheezing upon exertion due to severe Lung deficiency.
    - With *Zingiberis Rhizoma recens* (sheng jiang) for sudden onset of coughing.

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
- Contraindicated in those with damp-heat, phlegm-heat, or childhood nutritional impairment.
- It is particularly contraindicated for those with clumped constipation, dental caries, red eyes, and childhood nutritional impairment. (Grand Materia Medica)

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
Good quality consists of a yellowish brown, highly viscous, and very sticky mass with a sweet taste.

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
