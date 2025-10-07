---
# 🔹 Core Metadata (Universal Fields)
id: "herb-20251001123706"
name: "Wu Yao"
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
  hanzi: "乌药"
  pinyin: "Wu Yao"
  pharmaceutical: "Linderae Radix"
  english: "Lindera Root"
  alternate_names: []

  # TCM Properties
  taste: [Acrid]
  temperature: "Warm"
  channels: [Bladder, Kidney, Lung, Spleen]

  # Clinical Information
  dosage: "3-9g"
  toxicity: "Long-term administration and overdosage should both be avoided."
  functions: [Promotes the movement of qi and alleviates pain, Warms the Kidneys]
  dui_yao: []

  # Additional Information
  constituents: [Monoterpenes, sesquiterpenes: linderane, linderene, isolinderene, borneol (linderol), linderalactone, isolinderalactone, neolinderalactone, chamazulene (linderazulene), linderene acetate, lindenene, lindenenone, isofuranogermacren, lindestren, linder oxide, Alkaloids: laurolitsine, boldine, reticuline, Organic acids: decanoic acid, dodecanoic acid, tetradecanoic acid, cis-4-dodecenoic acid, cis-4-tetradecenoic acid, palmitic acid, octadecanoic acid, oleic acid, linoleic acid, eicosenoic acid]
  quality: "Good quality consists of tender roots with a yellowish-white, powdery cross section and an intense aroma."
  text_first_appeared: "Formulary of the Bureau of Medicines of the Taiping Era"

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

Acrid, warm, and aromatic, Linderae Radix (wu yao) disseminates and unblocks the qi, in the upper body mobilizing the Spleen and Lungs, in the lower body pervading the Liver, Kidneys, and Bladder. It smooths the flow of qi, directing it downward if rebellious, disperses cold, and alleviates pain, dredging and unblocking rebellious pathogenic qi in the chest and abdomen. It is often used in the treatment of distending pain in the chest or abdomen, rebellious qi with cough and wheezing, cold qi in the Bladder leading to urinary frequency, painful bulging disorder due to cold, and gynecological qi blockage and blood stasis-all cases of rebellious qi and pathogenic cold constraint.

Li Shi-Zhen observed that the herb is acrid, warm, aromatic and penetrating, with the ability to disperse all kinds of qi. This is why Formulary of the Bureau of Medicines of the Taiping Era [says that it] treats all patterns of wind-stroke or qi stroke by relying on the ability of Linderae Radix (wu yao) to smooth and disperse the qi: first dredging the patient's qi, for once the qi flows smoothly then wind naturally disperses.

Li also noted that "within its downward-directing is an ascending quality, and within its draining there is tonification."

*Transforming the Significance of Medicinal Substances* observes that Linderae Radix (wu yao) is powerful and warm, thus it eases the qi, disseminates and unblocks, dredging and dispersing congealed stagnation ... as it disperses cold qi, naturally residual coldness and cold pain will be expelled ... it quickly reduces constrained qi, nausea in the middle, abdominal pain, distention and fullness in the chest and diaphragm. It dredges channel qi, thus gradually unblocking paralysis due to qi stroke, or congealed qi and blood in the early stages of labor. All of this is the effect of its masculine qi.

---
---

## 🔑 TCM Properties

**Taste:** `= join(this.herb_data.taste, ", ")`
**Temperature:** `= this.herb_data.temperature`
**Channels Entered:** `= join(this.herb_data.channels, ", ")`

---

## ⚡ Functions & Actions

- Promotes the movement of qi and alleviates pain: for a stifling sensation in the chest, flank pain, and epigastric and abdominal pain and distention due to constraint from cold and qi stagnation. The herb warms and disperses, and is effective in spreading and unblocking the qi dynamic, thereby smooths the flow of qi, facilitates the middle. It disperses cold, and stops pain in many areas. It is also used when cold accumulation and qi stagnation manifest in lower abdominal pain, bulging disorders, or menstrual pain.
- With Allii macrostemi Bulbus (xie bai) and Curcumae Radix (yu jin) for a stifling sensation in the chest and flank pain.
- With Aucklandiae Radix (mu xiang) and Aurantii Fructus (zhi shi) for epigastric and abdominal pain and distention due to cold stagnation and qi obstruction.
- Add Cyperi Rhizoma (xiang fu) for dysmenorrhea due to stagnant qi.
- With Cinnamomi Cortex (rou gui) for abdominal pain, especially sensations of cold and pain in the lower abdomen.
- With Evodiae Fructus (wu zhu yu) for abdominal pain, vomiting, and diarrhea due to Spleen and Kidney cold from deficiency, as well as cold bulging disorders.
- With Foeniculi Fructus (xiao hui xiang) and Alpiniae officinarum Rhizoma (gao liang jiang) for cold bulging disorders with lower abdominal pain that radiates to the testicles, as in Top-Quality Lindera Powder (tian tai wu yao san).
- With Angelicae sinensis Radix (dang gui) and Cyperi Rhizoma (xiang fu) for menstrual pain.
- With Ephedrae Herba (ma huang) and Bombyx batryticatus (bai jiang can) for wind attacking the extremities characterized by joint pain, numbness, headache, and dizziness.
- Warms the Kidneys: for urinary frequency or incontinence due to insufficiency of Kidney yang and cold from deficiency of the Bladder.
- With Alpiniae oxyphyllae Fructus (yi zhi ren) and Dioscoreae Rhizoma (shan yao) for urinary frequency in adults and enuresis in children due to Kidney cold from deficiency, as in Shut the Sluice Pill (suo quan wan).

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
Because this herb is acrid, warm, and drying, it can disperse the qi and deplete the blood. It should not be used in those with significant qi and blood deficiency or internal heat. See Toxicity below.

"If discomfort in the chest and diaphragm occurs due to qi deficiency with internal heat, the disorder is not appropriate for this herb: Linderae Radix (wu yao) can only expel cold qi." (*Seeking Accuracy in the Materia Medica*)

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
Good quality consists of tender roots with a yellowish-white, powdery cross section and an intense aroma.

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
