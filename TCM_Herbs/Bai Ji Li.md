---
# 🔹 Core Metadata (Universal Fields)
id: "herb-20251001123706"
name: "Bai Ji Li"
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
  hanzi: "白芨"
  pinyin: "Bái Jí"
  pharmaceutical: "Bletillae Rhizoma"
  english: "bletilla rhizome"
  alternate_names: []

  # TCM Properties
  taste: [bitter, sweet, cool]
  temperature: "cool"
  channels: [Lung, Stomach, Liver]

  # Clinical Information
  dosage: "None"
  toxicity: "Side effects have been reported in rare cases. The symptoms included nausea, vomiting, dizziness, and cold sweat. These symptoms resolved spontaneously after the herb was discontinued. Other side effects included an oppressive feeling in the chest, dyspnea, palpitations, cold sweat, and agitation. Allergic reactions such as as pruritus and urticaria, as well as one case of allergic asthma, have also been reported."
  functions: [restrains to stop bleeding, reduces swelling, generates flesh]
  dui_yao: []

  # Additional Information
  constituents: [Phenolic compounds: agrimol A, B, C, D, E, F, G, hyperoside, osthole, coumarin, Flavonoids, flavonoid glycosides: luteolin-7-glucoside, apigenin-7-glucoside, quercetin, cosmosiin, hyperoside, rutin, catechin, Organic acids: ellagic acid, gallic acid, caffeic acid, pinic acid,
ursolic acid, 1β,2α,3β,19α-tetrahydroxyurs-12-en-28-oic acid,
1β,2β,3β,19α-tetrahydroxyurs-12-en-28-oic acid]
  quality: "Good quality consists of dry, tender plants with reddish brown stems and many leaves."
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

WITH AGrIMONIAE HERBA (xian he cao 仙鹤草) AND ASINI CORII COLLA (e
jiao 阿胶)
Both herbs stop bleeding, but Agrimoniae Herba (xian
he cao) (see also regulates and tonifies the qi and blood
CoMMENTARY above), while Asini Corii Colla (e jiao) nour
ishes the blood and yin fluids. The combination therefore
has both a strong effect in stopping bleeding, and also a cer
tain supplementing effect. It is widely used for many types
of bleeding disorders such as coughing of blood, Intestinal
wind with blood in the stool, blood in the urine due to yin
deficiency, bleeding during pregnancy, and continuous
uterine bleeding. It is most appropriate when bleeding is
found with indications of yin and blood deficiency.

---
---

## 🔑 TCM Properties

**Taste:** `= join(this.herb_data.taste, ", ")`
**Temperature:** `= this.herb_data.temperature`
**Channels Entered:** `= join(this.herb_data.channels, ", ")`

---

## ⚡ Functions & Actions

regulate the Blood 585
Omissions abscesses, and killing parasites. For example,
from the Grand Materia Medica records that it
reduces food stagnation, eases fullness in the middle, drives
qi downward, treats all disorders involving vomiting of
blood, upset Stomach, belching, malarial disorders, pain
ful obstruction of the throat, Intestinal wind with blood in
the stool, accumulated food [stasis], jaundice, and treats
abscesses and deep-rooted toxic sores, Lung abscess, breast
abscess, and swollen hemorrhoids.
At present it is primarily used for bleeding disorders associ
ated with some of the ailments listed in this passage, such
as bleeding dysenteric disorders, but also for malarial dis
orders, swollen sores, hemorrhoids, and vaginal pruritus
due to trichomonas infection. For the latter condition the
young, fresh stems and leaves are often used as part of an
external wash or douche.
People south of the Yangtze river in China use this
herb as a qi tonic in cases of exhaustion-hence the name
shi li cao (失力草), loss-of-strength herb (shili cao 失力草). For this purpose,
30g of the herb are combined with ten red dates in a strong
decoction and sipped as a tea throughout the day. This has
also been effectively used for bleeding ulcers in the stom
ach or duodenum. It can also be included in the formula
Gui Pi Tang (归脾汤) Restore the Spleen Decoction when bleeding is
due to Spleen deficiency which renders it unable to contain
the blood.

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
Good quality consists of dry, tender plants with reddish brown stems and many leaves.

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
