---
# 🔹 Core Metadata (Universal Fields)
id: "herb-20251001123706"
name: "Zi Su Ye"
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
  hanzi: "紫苏叶"
  pinyin: "Zi Su Ye"
  pharmaceutical: "Perillae Folium"
  english: "Perilla Leaf"
  alternate_names: []

  # TCM Properties
  taste: [Acrid, Aromatic]
  temperature: "Warm"
  channels: [Lung, Spleen]

  # Clinical Information
  dosage: "5-9g"
  toxicity: "A large dosage of this herb can raise blood sugar levels, and should not be used in those suffering from diabetes."
  functions: [Releases the exterior and disperses cold, Promotes the movement of qi and expands the chest, Use during pregnancy, Resolves seafood poisoning]
  dui_yao: []

  # Additional Information
  constituents: [Volatile oil: perilla aldehyde, l-limonene, α-pinene, β-pinene, perillanin, eugenol, isoegomaketone, isoamyl-3-furylketone, linalool, camphene, menthol, menthane, perilla alcohol, dihydroperilla alcohol, δ-dehydroelscholtzione, elemicin, perilla ketone, β-caryophyllene, γ-bergamotene, Other constituents: perilloside, perillyl-β-D-glucopyranoside, 1,2-methylenedioxy-4-methoxy-5-allyl-3-phenyl-β-D-glucopyranoside, cumic acid, tannins]
  quality: "Good quality consists of big, unfragmented, and stalkless leaves of purple color and an intensely aromatic fragrance."
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

"Its acrid flavor enters the qi level, while its purple color signals that it enters the blood level." These are the opening words from the discussion of Perillae Folium (*zi su ye*) in Essentials of the Materia Medica. Further description is found in Seeking Accuracy in the Materia Medica: "[I]ts aroma can vent wind outward, its warmth can warm the middle, facilitating the comfort of the whole body. Thus, it is named *su*." Materia Medica of Food Stuffs adds that it can "bring down floating qi in the chest and diaphragm."

Most classical texts warn, however, that continued consumption will drain away true qi (see CAUTIONS & CONTRAINDICATIONS above). The same caveat applies to all acrid, dispersing herbs.

---
---

## 🔑 TCM Properties

**Taste:** `= join(this.herb_data.taste, ", ")`
**Temperature:** `= this.herb_data.temperature`
**Channels Entered:** `= join(this.herb_data.channels, ", ")`

---

## ⚡ Functions & Actions

*   **Releases the exterior and disperses cold:** For externally contracted wind-cold with such symptoms as fever, chills, headache, nasal congestion, cough, or a stifling sensation in the chest, as in Apricot Kernel and Perilla Leaf Powder (*xing su san*) and Cyperus and Perilla Leaf Powder (*xiang su san*).
*   **With Cyperi Rhizoma** (*xiang fu*) to release the exterior in a patient with pre-existing qi constraint. Add Ephedrae Herba (*ma huang*) if the cold is severe.
*   **With Platycodi Radix** (*jie geng*) for common colds with such symptoms as nasal congestion and productive cough. The addition of Armeniacae Semen (*xing ren*) and Peucedani Radix (*qiang huo*) strengthens its effect in treating cough.
*   **With Codonopsis Radix** (*dang shen*) to benefit the qi and release the exterior in patients who are weak or debilitated.
*   **With Raphani Semen** (*lai fu zi*) and Armeniacae Semen (*xing ren*) to disperse phlegm and alleviate wheezing.
*   **With Chaenomelis Fructus** (*mu gua*) and Magnoliae officinalis Cortex (*hou po*) to disperse heat and relieve summerheat.
*   **Promotes the movement of qi and expands the chest:** For nausea, vomiting, or poor appetite, as in Patchouli/Agastache Powder to Rectify the Qi (*huo xiang zheng qi san*). Also used as an auxiliary herb to invigorate the blood.
*   **With Pogostemonis/Agastaches Herba** (*huo xiang*) to release the exterior, regulate the qi, warm the middle burner, and transform turbidity. Used in cases of influenza and the common cold caused by wind-cold-dampness. Especially effective for the associated symptoms of abdominal pain, vomiting, and diarrhea. Linderae Radix (*wu yao*) is often added.
*   **With Platycodi Radix** (*jie geng*) and Aurantii Fructus (*zhi ke*) to ease the diaphragm and Intestines.
*   **With Chuanxiong Rhizoma** (*chuan xiong*) and Angelicae sinensis Radix (*dang gui*) to harmonize the blood and disperse blood stasis.
*   **Use during pregnancy:** For calming a restless fetus, or for morning sickness.
*   **With Amomi Fructus** (*sha ren*) and Citri Reticulatae Pericarpium (*chen pi*) for restless fetus caused by stagnant qi. Also for a stifling sensation and fullness in the chest and abdomen.
*   **With Coptidis Rhizoma** (*huang lian*) for morning sickness and irritability during pregnancy, or whenever middle burner stagnation tends toward heat.
*   **Resolves seafood poisoning:** Used either alone or with other herbs.
*   **With Zingiberis Rhizoma Recens** (*sheng jiang*) for seafood poisoning or for exterior conditions.

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
Contraindicated in those with warm pathogen diseases, or with qi and exterior deficiency.

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
Good quality consists of big, unfragmented, and stalkless leaves of purple color and an intensely aromatic fragrance.

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
