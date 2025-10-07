---
# 🔹 Core Metadata (Universal Fields)
id: "herb-20251001123706"
name: "Long Yan Rou"
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
  hanzi: "龍眼肉"
  pinyin: "lóng yǎn ròu"
  pharmaceutical: "Longan Arillus"
  english: "Longan Arillus"
  alternate_names: []

  # TCM Properties
  taste: [Sweet, Warm]
  temperature: "Warm"
  channels: [Heart, Spleen]

  # Clinical Information
  dosage: "9-15g"
  toxicity: "Taking high doses of this fruit can cause hemorrhagic colitis in children, which can be terminal. Note, however, that only two cases have been reported in the literature; in one, a three-year-old boy ate three handfuls of the fruit.

Allergic skin reactions have also been reported. Symptom appeared 30 minutes after ingestion and included intense pruritus and erythema, starting at the lower extremities and spreading over the entire body, including the face.

A single case of allergic drug rash has been reported with a scarlet, itching eruption expanding over the entire body, along with vertigo and an elevated temperature."
  functions: [Tonifies and augments the Heart and Spleen, Nourishes the blood, Calms the spirit]
  dui_yao: []

  # Additional Information
  constituents: [Organic acids: tartaric acid, 2-amino-4-methylhex-5-ynoic acid, 2-amino-4-hydroxymethylhex-5-ynoic acid, α-amino-4-hydroxyhept-6-ynoic acid, Sugars: glucose, sucrose, Flavonoids: quercetin, quercitrin, Other constituents: fats, proteins, vitamine B1, B2, C, D, pentacyclic triterpenes]
  quality: "Good quality consists of large, thick, soft, yellowish, translucent pieces with an intensely sweet taste."
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

As early as the Divine Husbandman's Classic of the Materia Medica, the gentle spirit-nourishing action of Longan Arillus (long yan rou) was noted: "primarily quiets the emotions and [treats] aversion to food; long-term consumption strengthens the corporeal and the ethereal souls, sharpens the intelligence, lightens the body, prevents aging, and facilitates enlightenment of the spirit."

Seeking Accuracy in the Materia Medica elaborates:
In general, the blood relies on the Heart for its generation, but also depends on the Spleen for control. [Excessive] thinking and deliberation can deplete the qi, which, without sweetness, cannot be tonified. [Excessive] thinking and deliberation also injure the spirit, which cannot be aided without moistening. Longan Arillus (long yan rou) has both sweetness and moisture, enabling it to tonify the Spleen and stabilize the qi; it also protects the blood from depletion. Then the spirit and qi naturally grow and are nourished, so that there can be no disorders such as palpitations with anxiety or forgetfulness.

---
---

## 🔑 TCM Properties

**Taste:** `= join(this.herb_data.taste, ", ")`
**Temperature:** `= this.herb_data.temperature`
**Channels Entered:** `= join(this.herb_data.channels, ", ")`

---

## ⚡ Functions & Actions

Tonifies and augments the Heart and Spleen, nourishes the blood, and calms the spirit: for insomnia, heart palpitations, forgetfulness, or dizziness due to Heart and Spleen deficiency. Commonly used for problems associated with excessive pensiveness or overwork. Can be taken alone as a tea.
    - With Angelicae sinensis Radix (dang gui), Ginseng Radix (ren shen), and Ziziphi spinosae Semen (suan zao ren) for palpitations and insomnia resulting from Heart blood deficiency, especially in those with accompanying Spleen qi deficiency, as in Restore the Spleen Decoction (gui pi tang).
    - With Lilii Bulbus (bai he) for mild cases of insomnia and excitability.
    - With Acori tatarinowii Rhizoma (shi chang pu) for forgetfulness, dizziness, and fatigue due to Heart qi and blood deficiency.
    - Cooked with white sugar for insufficiency of qi and blood.
    - With Zingiberis Rhizoma recens (sheng jiang) and Jujubae Fructus (da zao) for postpartum exhaustion of the qi and blood with floating edema.

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
Contraindicated in those with fire from constraint, phlegm with qi stagnation, or obstruction due to dampness.

"Sweet, warm, and moistening: the concern is that it will cause the qi to stagnate. It is inappropriate for those with Stomach heat with phlegm or fire; or in cases of wind heat in the Lungs causing cough with phlegm or blood." (Treasury of Words on the Materia Medica)

"Sweetness assists fire, and can also bring on pain; it should not be used with overabundant fire in the Heart or Lungs, fullness in the middle with nausea and vomiting, or constrained clumped qi in the diaphragm." (Treasury of Words on the Materia Medica)

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
Good quality consists of large, thick, soft, yellowish, translucent pieces with an intensely sweet taste.

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
