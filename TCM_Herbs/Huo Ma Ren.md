---
# 🔹 Core Metadata (Universal Fields)
id: "herb-20251001123706"
name: "Huo Ma Ren"
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
  hanzi: "火麻仁"
  pinyin: "Huo Ma Ren"
  pharmaceutical: "Cannabis Semen"
  english: "Hemp Seed"
  alternate_names: []

  # TCM Properties
  taste: [sweet, neutral]
  temperature: "neutral"
  channels: [Large Intestine, Spleen, Stomach]

  # Clinical Information
  dosage: "9-15g; crush before decocting"
  toxicity: "Ingestion of grossly excessive amounts of Semen Cannabis can be toxic. Symptoms include nausea, vomiting, diarrhea, numbness of the limbs, agitation and restlessness, confusion, loss of consciousness, and dilated pupils."
  functions: [Nourishes and moistens the Intestines, Nourishes the yin, Clears heat and promotes healing of sores]
  dui_yao: []

  # Additional Information
  constituents: [Fatty acid, esters: oleic acid, linoleic acid, palmitic acid, stearic acid, methyl palmitate, methyl oleate, methyl stearate, Lignanamides: cannabisin A, B, C, D, E, F, G, grossamide, N-trans-caffeoyltyramine, N-trans-feruloyltyramine, N-p-coumaroyltyramine, Phenolic compounds: cannabinol, cannabinolic acid, cannabidiol, cannabigerol, Alkenes: canniprene, dihydrostilbene derivates, Flavonoids: cannflavin A, B, Steroids: 5α-ergostane-3-one, 5α-stigmastane-3-one, stigmasterol, β-sitosterol, campesterol, Alkaloids: trigonelline, L(+)-isoleucin betaine, Other constituents: lipids (30%), phytin]
  quality: "Good quality consists of big, yellow, and full seeds."
  text_first_appeared: "None"

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

Sweet, neutral, slippery, and facilitating, Cannabis Semen (huo ma ren) enters the Spleen to enrich the yin fluids and transform dry clumps; it excels at moistening the Intestines and unblocking constipation. This herb is particularly appropriate for dry constipation in the elderly and deficient, or for dry constipation due to blood deficiency postpartum.

Transforming the Significance of Medicinal Substances notes that:

Cannabis Semen (huo ma ren) moistens the bowels and can be used for dryness of the blood in old age, poor qi and blood circulation in postpartum women, and for those whose primal qi has not recovered after an illness, or for weak people unable to walk far.

However, a number of materia medica texts stress that the slippery, downward-directing properties of Cannabis Semen (huo ma ren) make it unsuitable for use in those whose essence and primal qi tend to be insecure (see Traditional Contraindications below).

Records of Thoughtful Differentiation of Materia Medica provides this description: "Cannabis Semen (huo ma ren), sweet, neutral, slippery, and facilitating; within its softness it is hard, so that it can enter the Spleen and nourish its yin fluids while transforming its dryness." In Commentary on the Divine Husbandman's Classic of Materia Medica, Miao Xi-Yong explains that the herb:

is by nature extremely slippery and facilitating. Its sweetness tonifies the middle; when the middle is tonified, the qi is naturally augmented. Sweetness augments the blood; when the blood vessels are restored, then blood accumulation is broken up, and all the disorders of breastfeeding women after birth are expelled.

This view was mildly criticized by Miao's contemporary, Liu Ruo-Jin. In Description of the Materia Medica, Liu says that it:

is not a blood herb, but transforms the yin fluids of the blood; it does not augment the qi, but mobilizes the qi. Thus, it is most appropriate for wind-dryness in the Large Intestine.

---
---

## 🔑 TCM Properties

**Taste:** `= join(this.herb_data.taste, ", ")`
**Temperature:** `= this.herb_data.temperature`
**Channels Entered:** `= join(this.herb_data.channels, ", ")`

---

## ⚡ Functions & Actions

- Nourishes and moistens the Intestines: for constipation in the elderly, in the aftermath of a febrile disease, postpartum, and in cases of blood deficiency.
  - With Angelicae Sinensis Radix (dang gui) and Rehmanniae Radix Preparata (shu di huang) for constipation due to lack of fluids and blood deficiency, especially in the elderly and postpartum, as in Moisten the Intestines Pill from Master Shen's Book (run chang wan).
  - With Armeniacae Semen (xing ren), Paeoniae Radix Alba (bai shao), and Aurantii Fructus Immaturus (zhi shi) for constipation due to heat-induced dryness in the Stomach and Intestines, as in Hemp Seed Pills (ma zi ren wan).
  - With Perillae Fructus (zi su zi) for constipation in the elderly or debilitated, specifically if accompanied by coughing and wheezing.
- Nourishes the yin: mildly tonifies the yin and primarily used in cases of yin deficiency with constipation.
  - With Rehmanniae Radix (sheng di huang) and Ophiopogonis Radix (mai men dong) for yin deficiency with constipation.
- Clears heat and promotes healing of sores: as an auxiliary herb for sores and ulcerations, taken orally or applied topically.
  - With Lonicerae Flos (jin yin hua) and Glycyrrhizae Radix (gan cao) for redness, pain, and ulcerations of the oral cavity due to Stomach heat.

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
- Excessive consumption can lead to nausea, vomiting, and diarrhea. See Toxicity below.
- Overconsumption [of this herb] injures the blood vessels, [makes] essential qi slip out, and leads to impotence.
- Overconsumption by women brings on vaginal discharge due to its slippery, downward-draining, mobilizing-without-retaining properties.
- It is especially contraindicated for those with loose stools. (Harm and Benefit in the Materia Medica)
- In Rectification of the Meaning of Materia Medica, Zhang Jie-Bin agrees:
  - When disorders involve dryness and binding, draining downward is appropriate.
  - However, if there is instability of the lower [burner] primal qi accompanied by loose stools, impotence, spermatorrhea, or excessive vaginal discharge, it is forbidden in all of these cases.

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
Good quality consists of big, yellow, and full seeds.

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
