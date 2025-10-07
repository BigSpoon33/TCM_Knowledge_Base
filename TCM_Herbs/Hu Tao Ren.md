---
# 🔹 Core Metadata (Universal Fields)
id: "herb-20251001123706"
name: "Hu Tao Ren"
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
  hanzi: "胡桃仁"
  pinyin: "Hu Tao Ren"
  pharmaceutical: "Juglandis Semen"
  english: "Walnut Seed"
  alternate_names: []

  # TCM Properties
  taste: [Sweet, warm]
  temperature: "warm"
  channels: [Kidney, Large Intestine, Lung]

  # Clinical Information
  dosage: "9-15g in decoctions; 9-30g eaten by themselves"
  toxicity: "not specified"
  functions: [Tonifies the Kidneys and strengthens the back and knees, Warms the Lungs and helps the Kidneys grasp the qi, Moistens the Intestines and unblocks the bowels]
  dui_yao: []

  # Additional Information
  constituents: [Protein: 22%, Amino acids: glutamic acid, arginine, aspartic acid; isoleucine, leucine, tryptophan, phenylalanine, valine, threonine, lysine, Fats: triglycerides of linoleic acid, oleic acid, linolenic acid; β-sitosterol, campesterol, stigmasterol, δ-avenasterol, δ-stigmasterol]
  quality: "Good quality is large, full, oily, and yellowish brown without a rancid taste."
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

Sweet, warm, and moistening, Juglandis Semen (*he tao ren*) enters the Lung and Kidney channels where it has two principal actions: it warms the Kidney yang to strengthen the lower back and knees, and while tonifying the Kidneys it augments the Lungs and promotes the grasping of qi to settle wheezing. These effects, however, are gentle and gradual, and it generally serves as an assistant herb or in food therapy. Because it is rather oily and moist, it can moisten dryness and lubricate the Intestines.

The Detailed Materia Medica explains how it can affect both the Kidneys and the Lungs:

Once the gate of vitality is unblocked, the Triple Burner is naturally facilitated, and thus [the herb's actions] ascend to reach the Lungs and it is suitable for wheezing or cough due to cold from deficiency. It descends to reach the Kidneys, and it is thus appropriate for pain from deficiency in the lower back and legs ... [it] is only appropriate for cold from deficiency, and should not be consumed by those with phlegm-fire or accumulated heat.

The Grand Materia Medica says that walnuts can tonify the qi, nourish the blood, moisten dryness, transform phlegm, augment the gate of vitality, facilitate the Triple Burner, warm the Lungs, and moisten the Intestines. They treat coughs due to cold from deficiency, and heavy pain in the lower back and feet.

Essays on Medicine Esteeming the Chinese and Respecting the Western says that walnuts are an important herb for enriching and tonifying the Liver and Kidneys, and strengthening the sinews and bones. Hence they excel in the treatment of pain in the lower back and legs, and all types of pain in the sinews and bones. Because they tonify the Kidneys, they can stabilize the teeth, blacken the hair, and treat disorders such as coughs or wheezing due to deficiency consumption, the failure of qi to return to its base, lower burner cold from deficiency, urinary frequency, and uterine bleeding and vaginal discharge in women.

Essentials of the Materia Medica includes an interesting anecdote:

(Hong recorded:) My youngest son was ill with phlegmy wheezing. I had a dream of [the goddess] Guanyin, who directed me to administer Ginseng and Walnut Decoction (*ren shen hu tao tang*); he took it and was better. The next day [in preparing the decoction] I removed the pericarp from the walnut-the wheezing returned. When the pericarp was used, within several nights the illness was cured. Probably the pericarp can preserve the Lungs.

---
---

## 🔑 TCM Properties

**Taste:** `= join(this.herb_data.taste, ", ")`
**Temperature:** `= this.herb_data.temperature`
**Channels Entered:** `= join(this.herb_data.channels, ", ")`

---

## ⚡ Functions & Actions

- Tonifies the Kidneys and strengthens the back and knees: for patterns of Kidney deficiency with such symptoms as cold and painful back and knees and urinary frequency.
  - With Eucommiae Cortex (*du zhong*) and Psoraleae Fructus (*bu gu zhi*) for pain in the lower back and weakness in the legs from Kidney deficiency.
  - Add *jin qian cao* (Lysimachiae/Desmodii/etc. Herba) and Lygodii Spora (*hai jin sha*) for back pain associated with kidney stones.
- Warms the Lungs and helps the Kidneys grasp the qi: for deficient Lung chronic cough and wheezing that worsens with any exertion due to Lung and Kidney deficiency.
  - With Ginseng Radix (*ren shen*) for wheezing from Lung and Kidney deficiency, as in Ginseng and Walnut Decoction (*ren shen hu tao tang*).
  - Cooked with honey and taken with warm water for chronic cough due to cold from deficiency.
  - Add Epimedii Herba (*yin yang huo*) for concurrent lower back pain and weak legs from wind-damp painful obstruction.
- Moistens the Intestines and unblocks the bowels: for constipation in the elderly or that associated with injured fluids following a febrile disorder.
  - With Angelicae Sinensis Radix (*dang gui*) and Cistanches Herba (*rou cong rong*) for constipation due to insufficient fluids in the Intestines.

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
Contraindicated in patterns of phlegm-fire or hot coughs, yin deficiency with heat signs, and in those with watery stools.

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
Good quality is large, full, oily, and yellowish brown without a rancid taste.

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
