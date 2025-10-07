---
# 🔹 Core Metadata (Universal Fields)
id: "herb-20251001123706"
name: "alpinia fruit / Yi Zhi Ren"
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
  hanzi: "益智仁"
  pinyin: "yi zhi ren"
  pharmaceutical: "Alpiniae Oxyphyllae Fructus"
  english: "alpinia fruit, black cardamon, bitter-seeded cardamon"
  alternate_names: []

  # TCM Properties
  taste: [acrid]
  temperature: "warm"
  channels: [Kidney, Spleen]

  # Clinical Information
  dosage: "3-9g"
  toxicity: "None"
  functions: [Warms the Kidneys, retains the essence, and secures the urine, Warms the Spleen, stops diarrhea, and controls salivation]
  dui_yao: []

  # Additional Information
  constituents: [Volatile oil: α-cyperone, 1,8-cineole, α-pinene, β-pinene, 4-terpineol, α-terpineol, β-elemene, 1-methyl-3-isopropoxycyclohexane, α-muurolene, myrcene, geranyl acetate, zingiberene, guaiol, zingiberol, α-eudesmol, aromadendrene, acetone, 3-buten-3-one, 2-pentanol, 2-pentanone, isooctanol, furylaldehyde, zingiberene, zingiberol, patchoulene, gingerol, spiro[4,4]nonane-2-one, α-cyperone, nootkatol, nootkatone, Diphenylheptanes: yakuchinone A, B, Flavonoids: letochrysin, izalpinin, chrysin, 3,5-dihydroxy-7,4'-dimethoxyflavone, Other constituents: amino acids, fatty acids, sugars, proteins]
  quality: "Good quality consists of large, full fruit with an intense aroma."
  text_first_appeared: "Omissions from the [Classic of the] Materia Medica"

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

*Alpiniae oxyphyllae* Fructus (*yi zhi ren*) is acrid, warm, and aromatic, but also astringent, so that it warms the Spleen and Stomach to harmonize the middle, treat diarrhea, and contain excessive saliva; it also warms the Kidney yang and secures the lower burner. Thus it is often used in the treatment of Spleen and Stomach exposure to cold causing vomiting, diarrhea, abdominal pain, loss of appetite, and excessive salivation; and for cold from deficiency of the Kidneys leading to spermatorrhea, urinary incontinence, and continuous uterine bleeding.

Essentials of the Materia Medica says that it binds the essence, stabilizes the *qi*, warms the middle to improve food intake, contains thick saliva and sputum, secures the urine, and treats nausea, vomiting, diarrhea, lodged cold accosting the Stomach, cold *qi* abdominal pain, continuous uterine bleeding, vaginal discharge, and draining of the essence.

Encountering the Sources of the Classic of Materia Medica adds that it "augments the Spleen and Stomach, regulates the primal *qi*, tonifies Kidney deficiency [which allows] slippage of essence, Stomach deficiency with excessive salivation, and continuous uterine bleeding in women."

Summarization of Rectification of the Meaning of Materia Medica summarizes: "Everything the commentators have said is nothing but the effect of warm binding ... it warmly tonifies the Spleen and Kidneys, but particularly governs securing and binding."

---
---

## 🔑 TCM Properties

**Taste:** `= join(this.herb_data.taste, ", ")`
**Temperature:** `= this.herb_data.temperature`
**Channels Entered:** `= join(this.herb_data.channels, ", ")`

---

## ⚡ Functions & Actions

- Warms the Kidneys, retains the essence, and secures the urine: for such symptoms as frequent and copious urination, incontinence of urine, spermatorrhea, or dribbling of urine from Kidney yang deficiency. Also used for irregular uterine bleeding.
    - With Linderae Radix (*wu yao*) and Dioscoreae Rhizoma (*shan yao*) for urinary incontinence or frequency from cold deficient Spleen and Kidney cold from deficiency, as in Shut the Sluice Pill (*suo quan wan*).
    - With Amomi Fructus (*sha ren*) for uterine bleeding during pregnancy.
- Warms the Spleen, stops diarrhea, and controls salivation: used in patterns of Spleen or Stomach cold from deficiency with such symptoms as diarrhea, cold abdominal pain, excessive salivation, and a thick, unpleasant taste in the mouth. Also used for abdominal pain, vomiting, and diarrhea from cold entering the Spleen and Kidneys.
    - With Codonopsis Radix (*dang shen*), Pinelliae Rhizoma preparatum (*zhi ban xia*), and Poria (*fu ling*) for vomiting, diarrhea, cold and pain in the abdomen, reduced appetite, and excessive salivation associated with cold from deficiency of the Spleen and Stomach.
    - With Atractylodis macrocephalae Rhizoma (*bai zhu*) and Zingiberis Rhizoma (*gan jiang*) for abdominal pain, vomiting, and diarrhea from cold entering the Spleen and Kidneys.
    - With Dioscoreae Rhizoma (*shan yao*) to prevent the development of heat from deficiency as a side effect.

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
Contraindicated in those with lower burner problems due to heat.

Traditional Contraindications

"Do not mistakenly use if the blood is dry from fire." (Encountering the Sources of the Classic of Materia Medica)

"Its nature is more to travel than to tonify. It should be used in tonifying prescriptions; if used by itself it disperses the *qi*." (Arranged Mirror of Medicine)

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
Good quality consists of large, full fruit with an intense aroma.

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
