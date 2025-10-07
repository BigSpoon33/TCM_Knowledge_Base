---
# 🔹 Core Metadata (Universal Fields)
id: "herb-20251001123706"
name: "Xian He Cao"
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
  hanzi: "仙鶴草"
  pinyin: "xian he cao"
  pharmaceutical: "Agrimoniae Herba"
  english: "Agrimony Herb"
  alternate_names: []

  # TCM Properties
  taste: [Bitter, Astringent]
  temperature: "Neutral"
  channels: [Lung, Liver, Spleen]

  # Clinical Information
  dosage: "6-12g"
  toxicity: "Side effects have been reported in rare cases. The symptoms included nausea, vomiting, dizziness, and cold sweat. These symptoms resolved spontaneously after the herb was discontinued. Other side effects included an oppressive feeling in the chest, dyspnea, palpitations, cold sweat, and agitation. Allergic reactions such as pruritus and urticaria, as well as one case of allergic asthma, have also been reported."
  functions: [Restrains leakage of blood and stops bleeding, Alleviates diarrhea and dysenteric disorders, Kills parasites]
  dui_yao: []

  # Additional Information
  constituents: [Phenolic compounds: agrimol A, B, C, D, E, F, G, hyperoside, osthole, coumarin, Flavonoids, flavonoid glycosides: luteolin-7-glucoside, apigenin-7-glucoside, quercetin, cosmosiin, hyperoside, rutin, catechin, Organic acids: ellagic acid, gallic acid, caffeic acid, pinic acid, ursolic acid, 1β,2α,3β,19α-tetrahydroxyurs-12-en-28-oic acid, 1β,2β,3β,19α-tetrahydroxyurs-12-en-28-oic acid]
  quality: "Good quality consists of dry, tender plants with reddish brown stems and many leaves."
  text_first_appeared: "Unknown"

  # Source References
  bensky_pdf: "627"
  bensky_page: "583"

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

Bitter, astringent, and neutral, Agrimoniae Herba (xian he cao) enters the blood aspect of the Lung, Liver, and Spleen channels. It is commonly used to bind up and inhibit bleeding. As its nature is neither hot nor cold, its use is not restricted to disorders due to either heat or cold, deficiency or excess; it can be used for all types of bleeding. Mirror of the Hundred Herbs states it is used for "external injuries, vomiting of blood, continuous uterine bleeding, dysenteric disorders, and Intestinal wind with passage of blood." It can be used by itself or combined with other herbs to stop bleeding due to various causes.

There are a number of other uses for this herb mentioned in the various materia medica texts, including checking malarial disorders, resolving toxicity, reducing abscesses, and killing parasites. For example, the Grand Materia Medica records that it reduces food stagnation, eases fullness in the middle, drives qi downward, treats all disorders involving vomiting of blood, upset Stomach, belching, malarial disorders, painful obstruction of the throat, Intestinal wind with blood in the stool, accumulated food stasis, jaundice, and treats abscesses and deep-rooted toxic sores, Lung abscess, breast abscess, and swollen hemorrhoids.

At present it is primarily used for bleeding disorders associated with some of the ailments listed in this passage, such as bleeding dysenteric disorders, but also for malarial disorders, swollen sores, hemorrhoids, and vaginal pruritus due to trichomonas infection. For the latter condition the young, fresh stems and leaves are often used as part of an external wash or douche.

People south of the Yangtze river in China use this herb as a qi tonic in cases of exhaustion - hence the name loss-of-strength herb (tuo li cao). For this purpose, 30g of the herb are combined with ten red dates in a strong decoction and sipped as a tea throughout the day. This has also been effectively used for bleeding ulcers in the stomach or duodenum. It can also be included in the formula Gui Pi Tang (Restore the Spleen Decoction) when bleeding is due to Spleen deficiency which renders it unable to contain the blood.

---
---

## 🔑 TCM Properties

**Taste:** `= join(this.herb_data.taste, ", ")`
**Temperature:** `= this.herb_data.temperature`
**Channels Entered:** `= join(this.herb_data.channels, ", ")`

---

## ⚡ Functions & Actions

Restrains leakage of blood and stops bleeding: Widely used for various types of bleeding such as vomiting blood, coughing blood, nosebleed, bleeding gums, blood in the urine, or uterine bleeding. Depending on its particular combination with other herbs, it can be used for bleeding due to heat, cold, excess, or deficiency.
- With Sepiae Endoconcha (hai piao xiao) for excessive uterine bleeding or dark bloody stools associated with pain in the middle burner.
- With Sophorae Flos Immaturus (huai mi) for bloody stools.
- With Imperatae Rhizoma (bai mao gen) for bloody urine.
- Add Nelumbinis Nodus Rhizomatis (ou jie) for nosebleed.
- With Platycladi Cacumen (ce bai ye) and Rehmanniae Radix Crudus (sheng di huang) for blood coming from the upper part of the body (nose or mouth) due to internal heat and exhausted yin.
- With Asini Corii Colla (e jiao) for bleeding with underlying yin and blood deficiency.
- With Platycladi Cacumen (ce bai ye) for vomiting of blood.

Alleviates diarrhea and dysenteric disorders: For chronic problems, as this herb has a restraining nature.
- With Sanguisorbae Radix (di yu) for bloody dysenteric disorders.

Kills parasites: For trichomonas vaginitis and tapeworm, as well as malarial disorders. Used topically for trichomonas vaginitis.

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
As an astringent, binding herb, it is appropriate for chronic forms of diarrhea, but not for those with active pathogens.

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
