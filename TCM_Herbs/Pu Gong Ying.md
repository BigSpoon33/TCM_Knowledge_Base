---
# 🔹 Core Metadata (Universal Fields)
id: "herb-20251001123706"
name: "Pu Gong Ying"
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
  hanzi: "蒲公英"
  pinyin: "Pu Gong Ying"
  pharmaceutical: "Taraxaci Herba"
  english: "dandelion, taraxacum"
  alternate_names: []

  # TCM Properties
  taste: [Bitter, sweet]
  temperature: "cold"
  channels: [Liver, Stomach]

  # Clinical Information
  dosage: "9-30g"
  toxicity: "Administration of a large dosage may cause mild diarrhea. Allergic reactions have also been reported with pruritus, sensations of heat, urticaria, nausea, vomiting, abdominal discomfort, and mild diarrhea."
  functions: [Reduces abscesses and dissipates nodules, Clears the Liver and clears the eyes, Clears heat, resolves dampness, and unblocks painful urinary dribbling]
  dui_yao: []

  # Additional Information
  constituents: [taraxasterol, choline, inulin, pectin, volatile oil]
  quality: "Good quality consists of plants with many greyish green leaves and thick roots."
  text_first_appeared: "Tang Materia Medica"

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

Sweet, bitter, and cold, Taraxaci Herba (pu gong ying) cools heat, resolves toxicity, and excels at draining and directing downward, dispersing qi stagnation and clumping. Its traditional sphere of activity is in the treatment of breast abscess and other sores; it can be used both internally and externally in such cases. Regarding its use, the Tang Materia Medica says that "for women's breast abscess and edema, boil into juice to both drink and apply: immediate results."

The scope of the herb's activities has been expanding over the past few centuries, and is no longer limited to external disorders. It has been noted that Taraxaci Herba (pu gong ying) is effective for painful urinary dribbling, for moderating diarrhea, and for reducing clumping. Essentials of the Materia Medica says that this herb is "specific for breast abscess, deep-rooted sore toxin, and is also marvelous for unblocking painful urinary dribbling."

Zhu Dan-Xi noted that Taraxaci Herba (pu gong ying) "resolves toxicity due to stagnant food, disperses qi stasis, transforms heat toxin, reduces toxic swellings, clumping, nodes, and deep-set boils." Zhang Xi-Chun was enthusiastic about the herb's properties: "People have no idea that Taraxaci Herba (pu gong ying) treats eye diseases so marvelously - if they did, there would be no blind people in the world!"

Rectification of the Meaning of Materia Medica elaborates:

Its nature is clearing and cooling, and it treats all red and swollen heat toxin sores such as boils, furuncles, and carbuncles. It can be taken internally or applied externally, and lives up to [its description in the classics]. It is especially and particularly effective for breast abscess and sores on the breast when they are hard, red swellings. If fresh, grind into juice and drink warm; if dried, decoct to drink. Taraxaci Herba (pu gong ying) can be used alone to treat this condition, but if a larger prescription is selected, this must be one of the included herbs.

---
---

## 🔑 TCM Properties

**Taste:** `= join(this.herb_data.taste, ", ")`
**Temperature:** `= this.herb_data.temperature`
**Channels Entered:** `= join(this.herb_data.channels, ", ")`

---

## ⚡ Functions & Actions

- **Reduces abscesses and dissipates nodules:** For internal abscesses and external sores, particularly if they are firm and hard. Especially useful for breast and intestinal abscesses. Can be used both internally and topically.
    - With Trichosanthis Fructus (gua lou), Citri Reticulatae Pericarpium (qing pi), and Lonicerae Caulis (jin yin teng) for the early stages of breast abscess with redness, swelling, and pain. This is an important herb for this problem.
    - With Lonicerae Flos (jin yin hua) and Violae Herba (zi hua di ding) for all hot, painful, hard, and deep-rooted boils.
    - Add Forsythiae Fructus (lian qiao) and Chrysanthemi Indici Flos (ye ju hua) to strengthen the effect, as in Five-Ingredient Decoction to Eliminate Toxin (wu wei xiao du yin).
    - With Rhei Radix et Rhizoma (da huang), Patriniae Herba (bai jiang cao), and Moutan Cortex (mu dan pi) for intestinal abscess.
    - With Houttuyniae Herba (yu xing cao) and Benincasae Semen (dong gua zi) for Lung abscess with purulent sputum.
    - With Prunellae Spica (xia ku cao) for subcutaneous phlegm nodules. Often Fritillariae Thunbergii Bulbus (zhe bei mu) is added.
- **Clears the Liver and clears the eyes:** For redness and swelling of the eyes. Can be used alone as a steam for this purpose.
    - With Chrysanthemi Flos (ju hua), Scutellariae Radix (huang qin), and Prunellae Spica (xia ku cao) for redness and swelling of the eyes due to upward-blazing of Liver fire.
- **Clears heat, resolves dampness, and unblocks painful urinary dribbling:** For damp-heat jaundice and painful urinary dribbling.
    - With Artemisiae Scopariae Herba (yin chen) for jaundice.
    - With Lysimachiae Herba (jin qian cao) and Imperatae Rhizoma (bai mao gen) for painful urinary dribbling.

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
-
-

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
Good quality consists of plants with many greyish green leaves and thick roots.

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
