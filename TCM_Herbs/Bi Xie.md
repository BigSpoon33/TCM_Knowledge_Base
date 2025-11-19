---
# 🔹 Core Metadata (Universal Fields)
id: "herb-20251001123706"
name: "Bi Xie"
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
  hanzi: "萆薢"
  pinyin: "bì xiè"
  pharmaceutical: "Dioscoreae Hypoglaucae Rhizoma"
  english: "Tokoro, fish-poison yam rhizome"
  alternate_names: []

  # TCM Properties
  taste: [Bitter, neutral]
  temperature: "neutral"
  channels: [Bladder, Liver, Stomach]

  # Clinical Information
  dosage: "9-15g"
  toxicity: "None noted"
  functions: [Separates the pure from the turbid, Expels wind-dampness, relaxes the sinews, and unblocks the collaterals, Clears damp-heat from the skin]
  dui_yao: []

  # Additional Information
  constituents: [Saponins: diosgenin, yamogenin, hypoglaucin A, protohypoglaucine A, gracilin, protogracilin]
  quality: "Good quality consists of large, thin, yellowish white, elastic, unfragmented slices."
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

Bitter and neutral, *Dioscoreae Hypoglaucae Rhizoma* (*bi xie*) enters the Bladder, Liver, and Stomach channels. Through the Liver channel it acts upon the sinews and expels wind; through the Stomach channel it acts upon the flesh, expelling dampness, which is eliminated through the Bladder. Dampness can block the sinews, bones, flesh and skin, leading to pain, softening the sinews and causing atrophy and loss of function, or seeping into the flesh and skin to form toxic sores. Turbid dampness can flow downward causing turbid painful urinary dribbling or vaginal discharge.

This herb excels at expelling dampness by encouraging the separation of the pure from the turbid, which it then directs downward. An ancient adage points out that "It is best at treating dampness, next best at treating wind, and finally, it also treats cold." Its most appropriate indication is for turbid painful urinary dribbling and vaginal discharge due to lower burner turbid dampness. However, it is also effective for painful muscles due to damp-heat or wind-dampness, for eczema and damp sores due to seeping damp-heat, and atrophy of the limbs due to dampness obstructing the sinews and bones.

Chen Shi-Duo observed that it is more appropriate for chronic painful obstruction than for acute painful obstruction, because its action is gradual, the effect only becoming apparent after several weeks.

Thoroughly Revised Materia Medica describes an interesting pathological mechanism which throws light on one aspect of this herb:

When a person has urinary frequency with unbearable pain while voiding, this condition is necessarily due to blocked hot constipation. Water and fluids can only enter the Small Intestine, and the Large Intestine becomes ever more dry and parched. When serious, the patient is feverish and desires cold drinks. The disorder stems from greed for wine and sex, or the overconsumption of acrid, heating, meaty or fermented things which accumulate into heat toxin. They rot and stagnate the blood; then, taking advantage of deficiency, enter the Small Intestine, thus causing pain on urination. This type of urinary frequency and pain on voiding is different from the grating pain of painful urinary dribbling. One should use 60g of *Dioscoreae Hypoglaucae Rhizoma* (*bi xie*) dry-fried with salt water and powdered, taken in doses of 6-9g. This will make the water turn and flow into the Large Intestine. At the same time, one should use scallion soup to frequently rub the anus in order to unblock the qi, then the urinary frequency and pain will be reduced as a matter of course.

---
---

## 🔑 TCM Properties

**Taste:** `= join(this.herb_data.taste, ", ")`
**Temperature:** `= this.herb_data.temperature`
**Channels Entered:** `= join(this.herb_data.channels, ", ")`

---

## ⚡ Functions & Actions

*   Separates the pure from the turbid: for resolving turbid dampness in the lower burner manifested in cloudy urine (like rice porridge) or vaginal discharge. Can be used for problems due to either deficiency or damp-heat. For urine like rice porridge without pain or signs of heat, as in Tokoro Decoction to Separate the Clear (*bi xie fen qing yin*).

*   With *Plantaginis Semen* (che qian zi), *Talcum* (hua shi), and *Phellodendri Cortex* (huang bai) for damp-heat pouring downward with urinary frequency, cloudy urine, and vaginal discharge with a red tongue body and a yellow, greasy coating.

*   With *Alpiniae Oxyphyllae Fructus* (yi zhi ren), *Acori Tatarinowii Rhizoma* (shi chang pu), and *Linderae Radix*.

*   Expels wind-dampness, relaxes the sinews, and unblocks the collaterals: for wind-dampness or damp-heat painful obstruction with lower back pain, numbness or stiffness of the lower extremities, or muscle aches. The effect is mild.

    *   With *Clematidis Radix* (wei ling xian) for painful obstruction due to wind-dampness.
    *   Add *Cinnamomi Ramulus* and *Aconiti Radix Lateralis Preparata* (zhi fu zi) if due to cold-dampness.
    *   Add *Gentianae Macrophyllae Radix* (qin jiao) and *Coicis Semen* (yi yi ren) if due to damp-heat.

*   With *Achyranthis Bidentatae Radix* (niu xi) and *Eucommiae Cortex* (du zhong) for pain in the lower back with weakness due to Kidney deficiency and wind-dampness.

*   Clears damp-heat from the skin: for damp-heat skin lesions such as eczema and pustular sores.

    *   With *Phellodendri Cortex* (huang bai) and *Coicis Semen* (yi yi ren) for damp-heat skin lesions.

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
"Contraindicated for yin deficiency with blazing fire, terminal dribbling of urine with no dampness present, and low back pain due to Kidney deficiency." (Thoroughly Revised Materia Medica)

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
Good quality consists of large, thin, yellowish white, elastic, unfragmented slices.

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
