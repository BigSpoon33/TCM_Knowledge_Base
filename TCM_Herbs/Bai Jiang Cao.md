---
# 🔹 Core Metadata (Universal Fields)
id: "herb-20251001123706"
name: "Bai Jiang Cao"
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
  hanzi: "白 Jiang 草"
  pinyin: "bái jiàng cǎo"
  pharmaceutical: "Patriniae Herba"
  english: "Patrinia"
  alternate_names: []

  # TCM Properties
  taste: [Acrid, bitter]
  temperature: "slightly cold"
  channels: [Large Intestine, Liver, Stomach]

  # Clinical Information
  dosage: "6-15g"
  toxicity: "Use with caution during pregnancy, and then only when absolutely necessary."
  functions: [Clears heat, resolves toxicity, expels pus, Dispels blood stasis, stops pain]
  dui_yao: []

  # Additional Information
  constituents: [Volatile oil: patrinene, isopatrinene, Saponins, sapogenins: patrinoside A, B, C, D, E, F, G, H, J, K, L, scabioside A, B, C, D, E, F, G, 3-0-α-L-arabinopyranosyloleanolic acid, 3-0-α-L-arabinopyranosylhederagenin, 2'-0-acetyl-3-0-α-L-arabinopyranosylhederagenin; hederagenin, oleanolic acid, Other constituents: scopoletin, esculetin, patrinoside, daucosterol, β-sitosterol]
  quality: "Good quality consists of a yellowish-green, dry herb with long roots and a high percentage of unfragmented leaves, without foreign matter."
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

*Patriniae Herba* (bai jiang cao) is acrid, and thus disperses; bitter, and thus drains; and cold, and thus cools heat. It enters the Liver, Stomach, and Large Intestine channels, and is best for resolving toxicity, expelling pus, invigorating the blood, and reducing abscesses. In particular, it mobilizes areas of stasis and blockage in the Stomach and Intestines. For all of these reasons, it is valued in the treatment of intestinal abscess, whether or not pus has formed. It also treats abdominal pain in women due to blood stasis and is a widely used gynecological herb for blood stasis with toxic accumulation.

In Convenient Reader of Materia Medica, Zhang Bing Cheng observes: "In expelling pus and reducing swelling to treat intestinal abscess, it utilizes its acrid bitterness; in spreading out the Stomach and mobilizing the Liver to treat stagnant heat, it calls upon its salty, cold powers." While the herb is no longer considered salty, it was so described in Miscellaneous Records of Famous Physicians, the fourth-century work.

The Grand Materia Medica notes:

*Patriniae Herba* (bai jiang cao) is an herb of the yang brightness and terminal yin channels; it excels at expelling pus and breaking up blood stasis. This is the reason that [Zhang] Zhong-Jing used it to treat abscess, and it is used in many ancient gynecological formulas.

### Mechanisms of Selected Combinations

**With *Taraxaci Herba* (pu gong ying)**

Entering both the qi and blood levels of the Liver and Stomach channels, this pair of herbs strongly disperses stagnation due to heat toxin, which can lead to pain and distention of the abdomen, abdominal masses, and jaundice. It is also appropriate for gynecological disorders involving vaginal discharge, pain, and abdominal distention due to heat and stasis.

---
---

## 🔑 TCM Properties

**Taste:** `= join(this.herb_data.taste, ", ")`
**Temperature:** `= this.herb_data.temperature`
**Channels Entered:** `= join(this.herb_data.channels, ", ")`

---

## ⚡ Functions & Actions

Clears heat, resolves toxicity, and expels pus: For either internal fire toxin disorders, such as intestinal abscess, or fire toxin surface sores and swellings. May be taken internally or applied topically.
    With *Lonicerae Flos* (jin yin hua) for suppurative abscesses.
    Add *Rhei Radix et Rhizoma* (da huang) and *Moutan Cortex* (mu dan pi) for intestinal abscesses that have not completely suppurated.
    With *Taraxaci Herba* (pu gong ying) for swollen toxic sores and abscesses, as well as pain, redness, and swelling of the eyes.
    With *Coicis Semen* (yi yi ren) for suppurations due to smoldering damp-heat.
    Add *Aconiti Radix Lateralis Preparata* (zhi fu zi) for suppurative intestinal abscess presenting without heat symptoms, as in Coicis, Aconite Accessory Root, and Patrinia Powder (yi yi fu zi bai jiang san).
    With *Houttuyniae Herba* (yu xing cao) and *Scutellariae Radix* (huang qin) for Lung abscess.

Dispels blood stasis and stops pain: For pain and obstruction associated with heat-induced blood stasis, especially in the abdomen and chest. Also for postpartum pain, and more recently, for post-operative pain.
    With *Paeoniae Radix Rubra* (chi shao) for abdominal pain with fever due to postpartum blood stasis, and for unsuppurated intestinal abscess presenting with a fixed abdominal mass.
    With *Trogopterori Faeces* (wu ling zhi), *Cyperi Rhizoma* (xiang fu), and *Angelicae Sinensis Radix* (dang gui) for chest and abdominal pain.

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
Encountering the Sources of the Classic of Materia Medica observes that this herb "cannot be used if pus has formed and the heat toxin is forcing its way outward" because its bitter, descending nature opposes the natural outward moving tendency of the sore itself. This viewpoint is characteristic of one of the main schools of external medicine, which holds that the excessive use of bitter, cold medicines can trap the toxins internally.

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
Good quality consists of a yellowish-green, dry herb with long roots and a high percentage of unfragmented leaves, without foreign matter.

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
