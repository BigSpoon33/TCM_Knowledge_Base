---
# 🔹 Core Metadata (Universal Fields)
id: "herb-20251001123706"
name: "Aloe / Lu Hui"
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
  hanzi: "芦荟"
  pinyin: "lu hui"
  pharmaceutical: "Aloe"
  english: "dried concentrate of the juice of the aloe leaf"
  alternate_names: []

  # TCM Properties
  taste: [bitter, cold]
  temperature: "cold"
  channels: [Large Intestine, Liver, Stomach]

  # Clinical Information
  dosage: "1.5-4.5g. Used in pills or capsules; do not decoct."
  toxicity: "The following adverse effects have been reported: nausea, vomiting, epistaxis, abdominal pain, diarrhea, bloody stool, hematuria, albuminuria, and after long-term administration, colitis. The risk of toxic effects from long-term use is similar to that of other anthraquinone-containing herbs, such as Sennae Folium (*fan xie ye*) and Rhei Radix et Rhizoma (*da huang*). Skin contact can cause allergic skin reactions."
  functions: [Drains fire and guides out accumulation, Clears heat and cools the Liver, Kills parasites and strengthens the Stomach]
  dui_yao: []

  # Additional Information
  constituents: [Anthraquinones: aloe emodin, aloin (barbaloin, aloin A), isobarbaloin (aloin B), 7-hydroxyaloin, homonataloin, chrysophanol, chrysophanol glucoside, anthranol, aloenin, aloesaponol 1·6-O-β-D-glucopyranoside, aloesaponol I, II, III, IV, aloesaponol II-6-O-D-glucopyranoside, aloesaponol III-8-O-D-glucopyranoside, aloesaponol IV-8-O-β-D-glucoside, isoeleutherol glucoside, isoxanthorin, Flavonoids: quercetin, campherenol, rutin, Sugars: glucose, mannose, arabinose, rhamnose, fructose, sucrose, xylose, glucuronic acid, Organic acids: capric acid, lauric acid, myristic acid, pentadecanoic acid, palmitic acid, margaric acid, stearic acid, palmitoleic acid, oleic acid, linoleic acid, succinic acid, malic acid, lactic acid, p-coumaric acid, Other constituents: amino acids (8 essential amino acids), cholesterol, campesterol, β-sitosterol]
  quality: "Good quality has an intense aroma and is water-soluble, without foreign matter or sand in the sediment."
  text_first_appeared: "Materia Medica of the Jiayou Era"

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

Very bitter and very cold, Aloe (*lu hui*) is yin by nature, moistening in texture, sinking and downward-directing. Entering the yang brightness channels, it drains fire and unblocks stool, dries dampness, and kills parasites. Here it is appropriate for habitual constipation, constipation due to clumped heat in the Intestine, vertigo, red eyes, restless insomnia, and abdominal pain due to bowel parasites. Entering the terminal yin channels, particularly the Liver, it cools the Liver, clears heat, and thus treats Liver channel heat from excess causing anger and irritability, fright, palpitations, and convulsions associated with constipation. Applied externally, it resolves toxicity and treats sores. Treasury of Words on the Materia Medica observes that it "is a herb to cool the Liver and kill parasites; whenever an illness involves the Liver and there is heat, it can be used without the slightest doubt!"

This substance works primarily by irritating the intestine, and its use may therefore be accompanied by colic. It is also excreted through the breast milk and can act as a purgative for the breastfeeding infant. It is usually used in pill form together with other herbs.

Among its three actions, cooling the Liver and relieving constipation are primary, while its ability to kill parasites is rather mild.

Mechanism of Selected Combinations

> WITH QUISQUALIS FRUCTUS (*shi jun zi*); see page 998

---
---

## 🔑 TCM Properties

**Taste:** `= join(this.herb_data.taste, ", ")`
**Temperature:** `= this.herb_data.temperature`
**Channels Entered:** `= join(this.herb_data.channels, ", ")`

---

## ⚡ Functions & Actions

*   **Drains fire and guides out accumulation:** For constipation, dizziness, red eyes, and irritability due to heat accumulation. Particularly indicated for hot constipation accompanied by exuberant Heart and Liver fire with irritability, restlessness, and insomnia. As a relatively mild herb, it is also used for chronic constipation.
    *   With Cinnabaris (*zhu sha*) for chronic constipation or that due to heat accumulation.
*   **Clears heat and cools the Liver:** For epigastric discomfort, dizziness, headache, tinnitus, irritability, constipation, and fever due to abundant heat in the Liver channel.
    *   With Gentianae Radix (*long dan cao*) and Gardeniae Fructus (*zhi zi*) for heat in the Liver channel with epigastric pain, dizziness, headache, and irritability, as in Tangkuei, Gentian, and Aloe Pill (*dang gui long hui wan*).
    *   With Arisaema cum Bile Bambusae (*dan nan xing*), Concretio Silicea (*tian zhu huang*), and Fritillariae Cirrhosae Bulbus (*chuan bei mu*) for childhood convulsions due to phlegm-heat.
*   **Kills parasites and strengthens the Stomach:** For childhood nutritional impairment, especially when due to roundworm. Also used for tinea.
    *   With Quisqualis Fructus (*shi jun zi*) for childhood nutritional impairment.
    *   With Borneolum (*bing pian*) as a topical application for hemorrhoids.

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
Contraindicated in those with cold from deficiency of the Spleen and Stomach, and during pregnancy. Use with caution during lactation. See TOXICITY below.

Traditional Contraindications

Bitterness and coldness by nature are contraindicated for Spleen and Stomach deficiency: taking them will cause continuous diarrhea. It is forbidden in children, those who are deficient in the Spleen and Stomach, those with no appetite, and those with diarrhea. (Harm and Benefit in the Materia Medica)

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
Good quality has an intense aroma and is water-soluble, without foreign matter or sand in the sediment.

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
