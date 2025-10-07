---
# 🔹 Core Metadata (Universal Fields)
id: "herb-20251001123706"
name: "Mu Gua"
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
  hanzi: "木瓜"
  pinyin: "Mù Guā"
  pharmaceutical: "Chaenomelis Fructus"
  english: "Chinese Quince"
  alternate_names: []

  # TCM Properties
  taste: [Sour, Astringent]
  temperature: "Warm"
  channels: [Liver, Spleen]

  # Clinical Information
  dosage: "6-12g"
  toxicity: "Allergic reactions have been observed following skin contact with this herb, with localized pruritus and edema."
  functions: [Relaxes sinews, Unblocks channels, Harmonizes the Stomach, Transforms dampness, Reduces food stagnation]
  dui_yao: []

  # Additional Information
  constituents: [Organic acids: malic acid, citric acid, tartaric acid, ascorbic acid, fumaric acid, Triterpenes: oleanolic acid, Other constituents: flavonoids, tannins]
  quality: "Good quality consists of big, fleshy, purplish red fruit."
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

Aromatic, sour, and warm, Chaenomelis Fructus (*mu gua*) relaxes the sinews, opens the collaterals, harmonizes the Stomach, and transforms dampness. It is warm without being drying, and enters the Spleen and Liver channels. In the Spleen channel, it alleviates nausea, halts diarrhea, and thus treats sudden turmoil disorder with cramping. Entering the Liver channel, it expels dampness from the sinews and vessels, relaxes the sinews, and invigorates the collaterals, and thus treats damp-painful obstruction disorder and muscular cramps.

Li Gao noted that "Chaenomelis Fructus (*mu gua*) enters the blood level of the arm and leg greater yin channels. In abandonment of qi, [Chaenomelis Fructus (*mu gua*)] can restrain; in stagnation of qi, it can harmonize."

Chaenomelis Fructus (*mu gua*) is specifically indicated for the abdominal cramps associated with sudden turmoil disorder, or gastroenteritis, but is also very effective for muscular cramps of the leg, which can result from blood deficiency, or cold invasion leading to contraction. Regardless of the causative factor, the pathological mechanism which brings about cramping always involves the deprivation of nourishment to the muscles and sinews. Chaenomelis Fructus (*mu gua*) is sour and warm, regulates the Spleen and Stomach, alleviates vomiting and diarrhea, and thereby prevents further loss of qi and fluids. The sour flavor itself mobilizes the sinews and relaxes cramping spasms.

*Extension of the Materia Medica* offers the following explanation:

Chaenomelis Fructus (*mu gua*) obtains the normal qi of wood, thus it enters the sinews. This substance enters the Liver, thus it augments the sinews and blood. For disorders of the lower back and Kidneys, when the feet and knees have no strength, this herb cannot be omitted.

However, in his *Grand Materia Medica*, Li Shi-Zhen rejected this explanation:

Chaenomelis Fructus primarily treats sudden turmoil disorder with vomiting, diarrhea, cramps, and leg qi: All of these are disorders of the Spleen and Stomach, not the Liver. Although the Liver governs the sinews, cramps result from pathogenic damp-heat or cold-dampness harming the Spleen and Stomach, which is why cramps always start in the calves. The calves pertain to yang brightness, and the [mechanism of] treatment of cramps with Chaenomelis Fructus (*mu gua*) is not by augmenting the sinews, but by regulating the Spleen and hewing the Liver. Earth in disorder [causes] weakness of metal and preponderance of wood. Thus, the use of sour warmth restrains the depleted dispersal of the Spleen and Lungs, while it mobilizes the sinews, so that pathogenic wood is calmed. This is draining wood from within earth in order to assist metal. When wood is calmed, earth regains command and metal is shielded.

---
---

## 🔑 TCM Properties

**Taste:** `= join(this.herb_data.taste, ", ")`
**Temperature:** `= this.herb_data.temperature`
**Channels Entered:** `= join(this.herb_data.channels, ", ")`

---

## ⚡ Functions & Actions

- Relaxes the sinews and unblocks the channels: for damp-painful obstruction in the extremities, especially with severe cramping pain, and weakness in the lower back and lower extremities. This is one of the more effective herbs for relaxing the sinews.
  - With Angelicae Sinensis Radix (*dang gui*) and Paeoniae Radix Alba (*bai shao*) for muscular spasms due to blood deficiency.
  - With Tigris Os (*hu gu*) and Angelicae Pubescentis Radix (*du huo*) for weakness, atrophy, and joint pain in the lower extremities.
  - With Olibanum (*ru xiang*), Myrrha (*mo yao*), and Rehmanniae Radix (*sheng di huang*) for tight sinews and stiff neck that cannot be turned.
- Harmonizes the Stomach and transforms dampness: for abdominal pain, spasms, and cramping of the calves, and edema due to leg qi. Especially useful for disharmony between the Liver and Spleen leading to leg problems.
  - With Evodiae Fructus (*wu zhu yu*) and Arecae Semen (*bing lang*) for cold-damp abdominal pain and diarrhea, as in Powder to Take at Cock's Crow (*ji ming san*).
  - With Evodiae Fructus (*wu zhu yu*) and Foeniculi Fructus (*xiao hui xiang*) for simultaneous vomiting and diarrhea (as in sudden turmoil disorders) leading to cramping and spasms of the legs.
  - With Coicis Semen (*yi yi ren*) for painful heavy legs or injury from summerheat-damp injury.
  - With Pogostemonis/Agastaches Herba (*huo xiang*) and Amomi Fructus (*sha ren*) for sudden turmoil disorder often with spasms of the calf muscles, due to summerheat.
- Reduces food stagnation: for indigestion. While this effect is similar to that obtained from Crataegi Fructus (*shan zha*), it is not commonly used.

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
- Contraindicated in those with internal constrained heat and scanty dark urine. Also contraindicated in those with hyperchlorhydria. See TOXICITY below.
- *Harm and Benefit in the Materia Medica* cautions that Chaenomelis Fructus (*mu gua*) should not be used if weakness of the lower back and knees is due to insufficiency of essence, blood, or true yin.
- Its flavor is sour and astringent, and thus if the Spleen and Stomach are not deficient when food stagnates, and the accumulated blockage is excessive, then it should not be used.
- In my humble opinion, a warm nature must be drying, and because the Kidneys are averse to dryness, long-term consumption [of this herb] will injure the teeth and bones.
- This passage goes on to say that because of its propensity to obstruct the flow of urine, this herb should be combined with Plantaginis Semen (*che qian zi*).

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
Good quality consists of big, fleshy, purplish red fruit.

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
