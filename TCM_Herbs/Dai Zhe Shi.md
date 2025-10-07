---
# 🔹 Core Metadata (Universal Fields)
id: "herb-20251001123706"
name: "Hematite / Dai Zhe Shi"
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
  hanzi: "代赭石"
  pinyin: "Dai Zhe Shi"
  pharmaceutical: "Haematitum"
  english: "Hematite"
  alternate_names: []

  # TCM Properties
  taste: [Bitter, Cold]
  temperature: "Cold"
  channels: [Heart, Liver, Pericardium]

  # Clinical Information
  dosage: "9-30g in decoctions (crushed); 1-3g in pills and powders"
  toxicity: "Long-term administration (over 20 days) can cause such toxic side effects as bleeding of the gingiva and thrombocytopenic purpura."
  functions: [Sedates and anchors the Liver yang and clears Liver fire, Strongly directs rebellious qi downward, Cools the blood and stops bleeding]
  dui_yao: []

  # Additional Information
  constituents: [Fe₂O₃, Si, Al, Mg, Mn, Ca, Ti]
  quality: "Good quality is brownish black, exhibits many layers in cross section, and is free of foreign mineral matter."
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

Bitter, cold, and heavy in weight, Haematitum (dai zhe shi) cools heat and suppresses rebellion, relying on its heaviness to sedate the Liver fire, and to calm and direct the rebellious qi downward. Encountering the Sources of the Classic of Materia Medica observes: "The heaviness of Haematitum (dai zhe shi) is used to sedate rebellious qi."

It is thus used for dizziness, tinnitus, and deafness due to Liver yang ascendancy. When there is transverse rebellion of Liver fire affecting the Lungs and Stomach, leading to nausea, vomiting, belching, and acute wheezing from phlegm, Haematitum (dai zhe shi) can be used as a chief medicinal. Its heaviness sedates trepidation, jitteriness, and fright causing the qi to float upward, and it is used in the treatment of convulsions in both adults and children.

Because the Liver stores the blood, and Haematitum (dai zhe shi) excels at clearing Liver fire, it also cools the blood and stops bleeding associated with heat in the blood, whether it manifests as nosebleed, vomiting of blood, or continuous uterine bleeding.

As explained in Essays on Medicine Esteeming the Chinese and Respecting the Western: It can generate blood while cooling blood; its weighty mass excels at suppressing rebellious qi, directing phlegm downward, stopping nausea and vomiting, and unblocking dry clumps-when used adroitly it can achieve marvelous results.

---
---

## 🔑 TCM Properties

**Taste:** `= join(this.herb_data.taste, ", ")`
**Temperature:** `= this.herb_data.temperature`
**Channels Entered:** `= join(this.herb_data.channels, ", ")`

---

## ⚡ Functions & Actions

* Sedates and anchors the Liver yang and clears Liver fire: for ascendant Liver yang with such signs as dizziness, vertigo, headache, sensation of pressure around the eyes, or tinnitus.
    * With Achyranthis bidentatae Radix (niu xi), Fossilia Ossis Mastodi (long gu), and Ostreae Concha (mu li) for dizziness and tinnitus from ascendant Liver yang, as in Sedate the Liver and Extinguish Wind Decoction (zhi gan xi feng tang).
    * With Margaritiferae Concha usta (zhen zhu mu), Magnetitum (ci shi), and Pinelliae Rhizoma preparatum (zhi ban xia) for hypertension with either ascendant Liver yang or Liver fire.
    * With Saigae tataricae Cornu (ling yang jiao), Gentianae Radix (long dan cao), and Bombyx batryticatus (bai jiang can) for acute febrile convulsions in children.
* Strongly directs rebellious qi downward: for such symptoms as belching, vomiting, hiccough, and acute wheezing.
    * With Pinelliae Rhizoma preparatum (zhi ban xia) and Inulae Flos (xuan fu hua) for vomiting, hiccough, and belching due to rebellious qi, as in Inula and Hematite Decoction (xuan fu dai zhe tang).
    * Add Mori Cortex (sang bai pi) and Perillae Fructus (zi su zi) for cough and wheezing from Lung heat.
    * With Gentianae Radix (long dan cao), Indigo naturalis (qing dai), and Paeoniae Radix alba (bai shao) for vomiting due to Gallbladder fire assaulting the Stomach.
    * With Codonopsis Radix (dang shen), Juglandis Semen (he tao ren), and Carpesii Fructus (he shi) for wheezing from deficiency of both the yin and yang.
* Cools the blood and stops bleeding: for vomiting of blood and nosebleeds. While primarily used for bleeding due to hot blood, it can also be used for bleeding due to cold from deficiency when combined with other appropriate herbs.
    * Can be used by itself for this purpose.
    * With Paeoniae Radix alba (bai shao), Bambusae Caulis in taeniam (zhu ru), and Arctii Fructus (niu bang zi) for vomiting of blood or nosebleeds due to heat in the blood.
    * With Limonitum (yu yu liang), Fluoritum (zi shi ying), and Halloysitum rubrum (chi shi zhi) for continuous uterine bleeding of purple or dark blood due to cold from deficiency of the Conception and Penetrating vessels.
    * With Atractylodis macrocephalae Rhizoma (bai zhu) and Zingiberis Rhizoma preparatum (pao jiang) for nosebleeds due to cold from deficiency.
    * With Rehmanniae Radix (sheng di huang) and Moutan Cortex (mu dan pi) for coughing or vomiting blood due to hot blood in patterns of disharmony between the Liver and Stomach, with accompanying rebellious Stomach qi.

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
Use with caution during pregnancy. Do not take long term.

"Contraindicated if the qi is insufficient, or the yin fluids and yang fluids are dry." (Medicinal Combining)

According to some traditional sources, this substance counteracts Aconiti Radix lateralis preparata (zhi fu zi).

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
Good quality is brownish black, exhibits many layers in cross section, and is free of foreign mineral matter.

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
