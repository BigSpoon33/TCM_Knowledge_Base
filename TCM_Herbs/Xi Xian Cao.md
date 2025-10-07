---
# 🔹 Core Metadata (Universal Fields)
id: "herb-20251001123706"
name: "Xi Xian Cao"
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
  hanzi: "豨莶草"
  pinyin: "xi xian cao"
  pharmaceutical: "Siegesbeckiae Herba"
  english: "siegesbeckia"
  alternate_names: []

  # TCM Properties
  taste: [Bitter, cold]
  temperature: "cold"
  channels: [Kidney, Liver]

  # Clinical Information
  dosage: "None"
  toxicity: "None"
  functions: [Dispels wind-dampness and unblocks the channels and collaterals, Clears heat and pacifies the Liver, Clears and transforms damp-heat]
  dui_yao: []

  # Additional Information
  constituents: [*Siegesbeckia orientalis*:
  - Terpenoids, terpenoid glycosides: darutoside, darutigenol, isodarutogenol B, C, (-)-16,17-dihydroxy-16β-kauran-19-oic acid
  - Lactones: orientin, orientalide, 9β-hydroxy-8β-isobutyryloxycostunolide, 9β-hydroxy-8β-methacryloyloxycostunolide, 14-hydroxy-8β-isobutyryloxycostunolide, 9β,14-dihydroxy-8β-isobutyryloxycostunolide, 8β-isobutyryl oxy-1β,10α-epoxycostunolide, 9β-hydroxy-8β-isobutyryl oxy-1β,10α-epoxycostunolide, 14-hydroxy-8β-isobutyryloxy-1β,10α-epoxycostunolide, 15-hydroxy-9α-acet-oxy-8β-isobutyryl oxy-14-oxomelampolide, 9α,15-dihydroxy-8β-isobutyryloxy-14-oxomelampolide, 15-dihydroxy-8β-isobutyryloxy-14-oxomelampolide, 1α-acetoxy-2α,3α-epoxyisoalantolactone
  - Other constituents: volatile oil, alkaloids, 3,7-demethoxyquercitrin, stigmasterol, KNO3, *Siegesbeckia pubescens*:
  - Terpenoids, terpenoid glycosides: siegesbeckioside, siegesbeckiol, siegesbeckic acid, (-)-16,17-dihydroxy-16β-kauran-19-oic acid, (-)-17-hydroxy-16β-kauran-19-oic acid, 16αH-16,19-kaurandioic acid, grandifloric acid
  - Volatile oil: germacene D, α-cadinene, sesquiterpene alcohols, acetylenic aldehydes
  - Other constituents: kirenol, sitosterol, daucosterol, *Siegesbeckia glabrescens*:
  - Terpenoids, terpenoid glycosides: darutigenol, darutoside, neodarutoside
  - Other constituents: 16-acetylkirenol, isopropylidenekirenol]
  quality: "Good quality is dark green and has many leaves and tender twigs."
  text_first_appeared: "None"

  # Source References
  bensky_pdf: "627"
  bensky_page: "360"

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

Acrid, bitter, and cold, Siegesbeckiae Herba (xi xian cao) enters the Liver and Kidney channels. It clears Liver channel heat, expels wind-dampness, transforms and cools damp-heat, expels wind, and alleviates itching, and thus can be used in the treatment of damp-heat sores, wind rash, and itching due to damp toxin. If prepared by steaming with wine, its bitter and cold qualities become sweet and warm, after which it is traditionally believed to be capable of tonifying the Kidneys and Liver and strengthening the bones and tendons, while still clearing dampness and expelling wind (see NOMENCLATURE & PREPARATION below). Thus, it can be used to treat numbness of the limbs, aching joints, and sore lower back and knees, whether due to pathogenic wind-dampness, or to Kidney and Liver deficiency. It can also be used for insomnia, irritability, tinnitus, and vertigo, but it is best for numbness of the limbs.

The decocted liquid is applied to sores and rashes due to damp-heat, and the juice obtained by crushing the fresh plant is used topically for spider and snake bites. However, the juice will cause vomiting if ingested, a warning that is mentioned repeatedly in various materia medica texts. Interestingly, Omissions from the Grand Materia Medica turns this problem to an advantage: "Fresh, pounded, and twisted, the juice causes vomiting to bring out phlegm."

---
---

## 🔑 TCM Properties

**Taste:** `= join(this.herb_data.taste, ", ")`
**Temperature:** `= this.herb_data.temperature`
**Channels Entered:** `= join(this.herb_data.channels, ", ")`

---

## ⚡ Functions & Actions

- Dispels wind-dampness and unblocks the channels and collaterals: for wind-damp painful obstruction with pain in the joints. Because it is good at unblocking the channels and invigorating the collaterals, it is also commonly used for spasms and cramps in the extremities, numbness in the extremities, and weak legs, including weakness as a sequelae of wind-stroke.
  - With Clematidis Radix (wei ling xian) for pain and soreness in the bones and sinews and numbness in the extremities due to wind-dampness.
- Clears heat and pacifies the Liver: for patterns of ascendant Liver yang with such symptoms as headache and dizziness.
  - With Prunellae Spica (xia ku cao) for headache, dizziness, and blurred vision due to ascending Liver fire.
- Clears and transforms damp-heat: for damp-heat sores and itching, wind-damp rash, or other forms of itching.
- Also used for hypertension.
  - With Clerodendri Folium (chou wu tong) for hypertension. Note that when used together, these herbs also have a synergistic effect on wind-dampness.

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
Commentary on the Divine Husbandman's Classic of Materia Medica cautions:

Whenever patients have numbness or painful obstruction of the limbs, aching within the bones, and weakness of the knees and lower back, [all of which are] due to Spleen and Kidney deficiency or deficiency of yin and blood, rather than as a result of attack by wind or dampness, this should not be consumed.

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
Good quality is dark green and has many leaves and tender twigs.

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
