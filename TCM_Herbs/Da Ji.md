---
# 🔹 Core Metadata (Universal Fields)
id: "herb-20251001123706"
name: "Da Ji"
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
  hanzi: "大蓟"
  pinyin: "dà jì"
  pharmaceutical: "Cirsii japonici Herba sive Radix"
  english: "Japanese Thistle"
  alternate_names: []

  # TCM Properties
  taste: [sweet, cool]
  temperature: "cool"
  channels: [Liver, Heart, Spleen]

  # Clinical Information
  dosage: "9-30g (Xiao Ji)"
  toxicity: "Note that if only the pinyin name without tone marks is written in a prescription, (da ji), it may be confused with the toxic drug Euphorbiae pekinensis Radix (da ji). Maximum daily dose is 9-15g."
  functions: [Cools the blood, stops bleeding, promotes urination (Xiao Ji), Reduces swelling, generates flesh at sores, Benefits the Gallbladder, reduces jaundice, Treats hypertension, Resolves toxicity, reduces abscesses (Xiao Ji)]
  dui_yao: []

  # Additional Information
  constituents: [aplotaxene, dihydroaplotaxene, tetrahydroaplotaxene, hexahydroaplotaxene, 1-pentadecene, cyperene, caryophyllene, thujopsene, a-himachalene, a-amyrin, B-amyrin, taraxasteryl acetate, B-sitosterol, stigmasterol, 5,7-dihydroxy-6,4'-dimethoxyflavone, inulin]
  quality: "Good quality has many greyish green leaves, and the roots should be free of fine hairy roots and root heads."
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

Sweet and cool, Cirsii japonici Herba sive Radix (da ji) enters the Liver, Heart, and Spleen channels. Because the Liver stores the blood and the Heart controls blood flow, its coolness reduces chaotically moving blood and thus stops bleeding. Its sweetness also helps tonify the blood, as noted in Essentials of the Materia Medica: "Its movement contains tonification." However, what this means is that it "removes the old in order to allow the new [blood] to be produced." Many materia medica texts record its beneficial effect on boils and furuncles, as it reduces swelling, cools heat, and removes stagnant blood. It also relieves jaundice and has recently been used to reduce high blood pressure.

Externally, this herb can be pounded into a paste and applied for bleeding from trauma. For swollen sores and boils, one can pound the fresh herb to extract the juice. The juice is drunk, and the paste is applied topically.

Commentary (Xiao Ji):
Sweet and cool, Cirsii Herba (xiao ji) enters the Heart and Liver channels to cool the blood and stop bleeding. Its actions are somewhat weaker than those of Cirsii japonici Herba sive Radix (da ji), and it has very little sore-reducing effect. However, because it is better able to promote urination, Cirsii Herba (xiao ji) is especially indicated for heat or damp-heat causing blood in the urine. Cirsii Herba (xiao ji), like Cirsii japonici Herba sive Radix (da ji), also promotes the function of the Gallbladder and reduces hypertension.

---
---

## 🔑 TCM Properties

**Taste:** `= join(this.herb_data.taste, ", ")`
**Temperature:** `= this.herb_data.temperature`
**Channels Entered:** `= join(this.herb_data.channels, ", ")`

---

## ⚡ Functions & Actions

- Cools the blood and stops bleeding: for chaotic movement of hot blood with such symptoms as nosebleed, vomiting blood, blood in the urine or stool, or uterine bleeding. It is especially effective in alleviating vomiting or coughing of blood.
    - With Rubiae Radix (qian cao) for nosebleed and spitting of blood due to heat in the blood.
    - Charred with Cirsii Herba (xiao ji) and Imperatae Rhizoma (bai mao gen) for heat-induced hemorrhage, as in Ten Partially-Charred Substances Powder (shi hui san).
- Reduces swelling and generates flesh at sores: used topically for carbuncles, sores, and swellings. For this purpose, the fresh herb is preferred.
    - With Achyranthis bidentatae Radix (niu xi), Sanguisorbae Radix (di yu), and Lonicerae Flos (jin yin hua) for internal abscesses such as Intestinal abscess.
- Benefits the Gallbladder and reduces jaundice: for jaundice, especially that due to damp-heat.
    - With Artemisiae scopariae Herba (yin chen) and Polygoni cuspidati Rhizoma (hu zhang) for damp-heat jaundice.
- Treats hypertension: recently used for hypertension, especially when accompanied by signs of Liver heat.
    - With Plantaginis Semen (che qian zi) as a daily beverage for hypertension.
    - With Prunellae Spica (xia ku cao) and Siegesbeckiae Herba (xi xian cao) for hypertension due to Liver heat.

Actions & Indications (Xiao Ji):
Cools the blood and stops bleeding: for any kind of bleeding due to heat in the blood leading to chaotic movement.

- With Imperatae Rhizoma (bai mao gen) for blood in the urine due to heat.
- With Rehmanniae Radix (sheng di huang), Talcum (hua shi), and Gardeniae Fructus (zhi zi) for hesitant, burning pain on urination or painful bloody urinary dribbling.
- The fresh root can be used with fresh Imperatae Rhizoma (xian bai mao gen) and fresh Nelumbinis Nodus rhizomatis (xian ou jie) for blood-streaked sputum with heat from deficiency. This is called Three Fresh Drink (san xian yin) by Zhang Xi-Chun (d. 1930).

Resolves toxicity and reduces abscesses: for sores and abscesses due to heat toxin. Used both internally and topically.

Recently used for damp-heat jaundice, hepatitis, and hypertension.

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
This herb is for hot patterns and should not be used for cold from deficiency of the Spleen and Stomach.

Traditional Contraindications

"It is not beneficial for disorders such as Stomach weakness leading to extreme blood deficiency, or Spleen and Stomach weakness with poor appetite." (Commentary on the Divine Husbandman's Classic of Materia Medica)

Use with caution in those with cold from deficiency of the Spleen and Stomach, loose stools, or diarrhea.(Xiao Ji)

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
Good quality has many greyish green leaves, and the roots should be free of fine hairy roots and root heads.

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
