---
# 🔹 Core Metadata (Universal Fields)
id: "herb-20251001123706"
name: "Bu Gu Zhi"
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
  hanzi: "补骨脂"
  pinyin: "bǔ gǔ zhī"
  pharmaceutical: "Psoraleae Fructus"
  english: "Malaytea Scurfpea Fruit"
  alternate_names: []

  # TCM Properties
  taste: [Acrid, bitter, very warm]
  temperature: "very warm"
  channels: [Kidney, Spleen]

  # Clinical Information
  dosage: "4.5-9g"
  toxicity: "Within the normal dosage range no side effects are to be expected. Overdosage may cause toxic symptoms such as general weakness, dizziness, and blurred vision followed by tachypnea, vomiting, and, in severe cases, hematemesis loss of consciousness, coma, and dyspnea. When taken orally, allergic reactions have been reported affecting both the skin and the upper digestive tract and mouth. Skin rashes and intense pruritis have also been reported following topical administration."
  functions: [Tonifies the Kidneys and fortifies the yang, Tonifies and warms the Spleen yang and stops diarrhea]
  dui_yao: []

  # Additional Information
  constituents: [Furanocoumarins: psoralen, isopsoralen, isopsoralidin, bakuchicin, angelicin, xanthotoxin (8-methoxypsoralen), psoralidin, psoralidin-2',3'-oxide, isopsoralidin, corylidin, bavacoumestan A, B, sophora coumestan A, Flavonoids, isoflavonoids: astragalin, bavachin (corylifolin), isobavachin, bavachinin; neobavaisoflavone, corylin, corylinal, psoralenol, Chalkons: bavachalcone, isobavachalcone (corylifolinin), isoneobavachalcone, neobavachalcone, bavachromene, bavachromanol, Other constituents: bakuchiol, triacontane, fixed oil, stigmasterol, β-sitosterol-D-glucoside]
  quality: "Good quality consists of dry, full, brownish black fruit without foreign matter."
  text_first_appeared: "Divine Husbandman's Classic of Materia Medica"

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

Acrid, bitter, and very warming, Psoraleae Fructus (bu gu zhi) tonifies the yang of both the Spleen and Kidneys, and has an astringent nature that acts on the Kidneys to secure the primal yang, and on the Spleen to stop diarrhea. It is often used to treat impotence, spermatorrhea, urinary frequency, and pain due to cold in the lower back and legs, as well as diarrhea associated with Spleen and Kidney yang deficiency. It also assists the Kidneys in grasping the qi, and can be used in the treatment of cough and wheezing due to cold from deficiency. Soaked in wine and applied topically, it is used to treat vitiligo.

Commentary on the Divine Husbandman's Classic of Materia Medica explains that Psoraleae Fructus (bu gu zhi):

is an important herb to warm the water organ, generate yang from within yin, reinforce fire and augment earth ... because it warms the water organ, it tonifies fire to generate earth, which means that the true fire within the Kidneys is tonified so that it can ascend to ripen and cook water and grains, steam the dregs, and transform the subtle essence. Spleen qi disperses essence to rise upward into the Lungs, and thus all of the five organs are nourished.

When applied topically for vitiligo, the affected area should be exposed to daylight (approximately 10 minutes) or ultraviolet light (2-5 minutes). It should then be washed to prevent local skin reactions. These can include a macular rash or blisters. If these do occur, administration of the herb should cease.

---
---

## 🔑 TCM Properties

**Taste:** `= join(this.herb_data.taste, ", ")`
**Temperature:** `= this.herb_data.temperature`
**Channels Entered:** `= join(this.herb_data.channels, ", ")`

---

## ⚡ Functions & Actions

*   Tonifies the Kidneys and fortifies the yang: for patterns of Kidney yang deficiency with such symptoms as impotence, premature ejaculation, enuresis, urinary frequency, cold and painful lower back, or weakness of the lower back and extremities. Also helps the Kidneys grasp the qi in the treatment of wheezing.

    *   With Juglandis Semen (he tao ren) and Aquilariae Lignum resinatum (chen xiang) for impotence.
    *   With Cuscutae Semen (tu si zi) and Alpiniae oxyphyllae Fructus (yi zhi ren) for urinary frequency, both daytime and nighttime, from Kidney yang deficiency.
    *   With Juglandis Semen (he tao ren) and Eucommiae Cortex (du zhong) for severe lower back pain or premature ejaculation, cough, and wheezing from Kidney yang deficiency, as in Young Maiden Pill (qing e wan).
*   Tonifies and warms the Spleen yang and stops diarrhea: for diarrhea due to cold from deficiency of the Spleen, borborygmus, and abdominal pain. Most appropriate in those with both Spleen and Kidney deficiency.

    *   With Myristicae Semen (rou dou kou), Schisandrae Fructus (wu wei zi), and Evodiae Fructus (wu zhu yu) for daybreak diarrhea, characterized by abdominal pain and borborygmus in the early morning hours that is alleviated upon evacuation, and is accompanied by a deep, thin pulse and a white tongue coating, as in Four-Miracle Pill (si shen wan).
*   Also used topically as a tincture for vitiligo.

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
Contraindicated in patterns of yin deficiency with heat signs or constipation. Although this herb can be hard on the Stomach, it is sometimes used, with caution, for cold from deficiency of the Stomach. See Toxicity below.

Traditional Contraindications

"Do not eat excessively [because they] disturb phlegm and thin mucus, making people nauseous so that they vomit water and food." (Important Formulas Worth a Thousand Gold Pieces)

"These are only appropriate for cold from deficiency, and should not be consumed by those with phlegm-fire or accumulated heat." (Detailed Materia Medica)

Its nature is drying and it assists fire; it is not to be taken when there is yin deficiency with fire blazing, excessive erections, spermatorrhea, blood in the urine, scanty, difficult urination, reddened eyes, bitter taste, dry tongue, and dry constipation, when internal heat causes thirst, or fire ascends causing indefinable epigastric discomfort, or damp-heat resulting in atrophy and weakness of the bones. (Harm and Benefit in the Materia Medica)

This book, and a number of other materia medica texts also state that Psoraleae Fructus (bu gu zhi) is contraindicated during pregnancy. However, in Readings in the Divine Husbandman's Classic of Materia Medica, Chen Nian-Zu observes that "The reference to 'abortion' in the Materia Medica of the Kaibao Era meant that this could be used to treat someone about to miscarry a pregnancy, not that it can cause miscarriage!" Chen goes on to explain that in fact, it "greatly stabilizes the fetus." Modern Chinese gynecology concurs with Chen and regards this as an herb that is used to prevent miscarriage due to instability of the Kidney yang.

According to some traditional sources, they should not be taken with strong tea.

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
Good quality consists of dry, full, brownish black fruit without foreign matter.

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
