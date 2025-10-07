---
# 🔹 Core Metadata (Universal Fields)
id: "herb-20251001123706"
name: "Bai Jie Zi"
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
  hanzi: "白芥子"
  pinyin: "Bai Jie Zi"
  pharmaceutical: "Sinapis Semen"
  english: "White Mustard Seed"
  alternate_names: []

  # TCM Properties
  taste: [Acrid, warm]
  temperature: "Warm"
  channels: [Lung]

  # Clinical Information
  dosage: "3-9g"
  toxicity: "This herb may irritate the skin and the mucosa of the gastrointestinal tract. For that reason, it should be used very cautiously in patients suffering from peptic ulcer or gastric hemorrhage or allergies. High dosage can cause enteritis, abdominal pain, and diarrhea. Allergic reactions following internal and external application have been reported, with symptoms including pruritus, papular rashes, urticaria, and vesicles. Topical application of this herb as a plaster has led to tachypnea, sweating, dizziness, agitation, low blood pressure, and anaphylactic shock, with the symptoms appearing 40 minutes after topical application."
  functions: [Warms the Lungs, regulates the qi, and expels phlegm, Promotes movement of the qi, disperses clumps, unblocks the collaterals, and stops pain]
  dui_yao: []

  # Additional Information
  constituents: ["Sinapis alba"
  Glucosinolates: sinalbin, myrosin
  Enzymes: "myrosinase"
Organic acids: "sinapic acid, benzoic acid"
Amino acids: "lysine, arginine, histidine"
Other constituents: "fixed oil, sinapine, sinapine thiocyanate, 4-hydroxybenzoylcholine, 4-hydroxybenzoylamine, 4-hydroxybenzylcyanide, *Brassica juncea*:"

- Glucosinolates:" sinigrin (allyl glucosinolate), gluconapin, 4-hydroxy-indolylmethyll glucosinolate, glucobrassicin, neoglucobrassicin, progoitrin"
- Enzymes: "myrosinase"
- Organic acids: "sinapic acid"
- Other constituents: fixed oil (glycerides of erucic acid, arachidic acid, linolenic acid), sinapin]
  quality: "Good quality consists of big, round, yellowish white seeds with a strong acrid flavor. The seed of *Sinapis alba* (bai jie zi), the white variety, is said to be superior to that of *Brassica juncea* (huang jie zi), the yellow variety."
  text_first_appeared: "Harm and Benefit in the Materia Medica"

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

Sinapis Semen (bai jie zi) is intensely acrid and warm, with the distinctive ability to penetrate the yin and restore movement to the yang. Zhu Dan-Xi noted that "Phlegm in the subcostal region, and between the skin and the membranes, cannot be reached without using [it]." It enters the channels with the Lung qi and disperses clumps of cold-phlegm, causing pain in the joints, or yin flat abscesses, and can also reach the interior of the body to relieve pain in the epigastric and abdominal regions. The typical recommended dose is 3-9g, but doses of 15g are often more effective, with few deleterious effects. However, the higher dosage is best used for strong patients, as the strong qi-moving warmth of Sinapis Semen (bai jie zi) may injure the qi in a weak person. Still, this drawback may be less of a problem than one might think, judging from the experience recorded in various materia medica texts.

For example, Rectification of the Meaning of Materia Medica observes that "Because its flavor is strong but its aroma is light, while it has a rapid opening and guiding action, it does not overly exhaust the qi." A contrary view is expressed in the Convenient Reader of Materia Medica: "Yet it exhausts the yin and disperses qi, blurs the vision, and injures the spirit: it is forbidden for deficient patients."

Chen Shi-Duo was especially enthusiastic regarding the virtues of Sinapis Semen (bai jie zi):

In fact, it is more effective than Pinelliae Rhizoma preparata (zhi ban xia) or Arisaematis Rhizoma preparatum (zhi tian nan xing), as Pinelliae Rhizoma preparatum (zhi ban xia) is drying [in nature] and dries the yin, while the heavy flavor of Arisaematis Rhizoma preparatum (zhi tian nan xing) injures the Stomach. Only Sinapis Semen (bai jie zi) dissolves phlegm and sputum, and without exhausting or damaging the Lungs and Stomach. It is most appropriate for entering the qi level, but can also be used at the blood level.

Regarding its phlegm-dissolving properties, Chen continued:

You can verify this by considering malarial disorder phlegm, in which phlegm is hidden in the midst of the diaphragmatic membrane. When you use one liang [30g] of Sinapis Semen (bai jie zi), fried, powdered, and formed into pills with rice, the full amount taken in the space of one day, then even long-term malarial disorder suddenly stops-is this not clear proof of its ability to dissolve phlegm? The disorder ceases, yet the spirit is not lethargic-is this not clear proof that it does not exhaust the qi? Thus, the phlegm-dissolving capacity of Sinapis Semen (bai jie zi) truly surpasses that of Fritillariae Bulbus (bei mu), Pinelliae Rhizoma preparatum (zhi ban xia) ....

---
---

## 🔑 TCM Properties

**Taste:** `= join(this.herb_data.taste, ", ")`
**Temperature:** `= this.herb_data.temperature`
**Channels Entered:** `= join(this.herb_data.channels, ", ")`

---

## ⚡ Functions & Actions

Warms the Lungs, regulates the qi, and expels phlegm: for coughing of copious and thin sputum, chest distention, and pain due to the accumulation of cold-phlegm, especially in chronic disorders.
  - With Perillae Fructus (zi su zi) and Raphani Semen (lai fu zi) for cough with copious, clear, bubbly sputum, and pain, fullness, and distention in the chest due to cold-phlegm obstructing the chest and flanks, as in Three-Seed Decoction to Nourish One's Parents (san zi yang qin tang).
  - With Kansui Radix (gan sui) and Euphorbiae pekinensis Radix (da ji) for thin mucus and phlegm in the chest and diaphragm with sudden, excruciating pain in the thorax, neck, and lower back accompanied by cough, wheezing, greasy tongue coating, and a wiry, slippery pulse. See Control Mucus Special Pill (kong xian dan).
- Promotes movement of the qi, disperses clumps, unblocks the collaterals, and stops pain: for phlegm-dampness obstructing the channels and collaterals, yin flat abscesses and spreading sores, and phlegm nodules such as scrofula.
  - With Cinnamomi Cortex (rou gui) and Rehmannia Radix preparata (shu di huang) for joint pain and yin flat abscesses due to phlegm-dampness obstructing the channels.
  - With Momordicae Semen (mi bie zi), Myrrha (mo yao), and Cinnamomi Cortex (rou gui) for phlegm obstructing the channels and collaterals with numbness and pain in the shoulders and upper arms and/or back pain and stiffness.

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
- Contraindicated in patients with chronic cough from Lung deficiency or flaring of fire due to either yin deficiency or blazing Stomach fire.
- Overdosage readily causes diarrhea.
- See Toxicity below.

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
Good quality consists of big, round, yellowish white seeds with a strong acrid flavor. The seed of *Sinapis alba* (bai jie zi), the white variety, is said to be superior to that of *Brassica juncea* (huang jie zi), the yellow variety.

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
