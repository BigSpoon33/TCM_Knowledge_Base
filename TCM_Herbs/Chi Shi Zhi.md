---
# 🔹 Core Metadata (Universal Fields)
id: "herb-20251001123706"
name: "Chi Shi Zhi"
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
  hanzi: "赤石脂"
  pinyin: "Chi Shi Zhi"
  pharmaceutical: "Halloysitum Rubrum"
  english: "Halloysite, Kaolin"
  alternate_names: []

  # TCM Properties
  taste: [Sweet, Sour, Astringent, Warm]
  temperature: "Warm"
  channels: [Spleen, Stomach, Large Intestine]

  # Clinical Information
  dosage: "9-18g"
  toxicity: "Use with caution during pregnancy. Contraindicated for hot diarrhea or in the early stages of dysenteric disorders, and for accumulation of damp-heat from excess."
  functions: [Binds up the Intestines and stops diarrhea, Contains the blood and stops bleeding, Promotes healing of wounds]
  dui_yao: []

  # Additional Information
  constituents: [Inorganic material: silicate mineral Al4(Si4O10)(OH)8·4H2O, Fe, Mn, Mg, Ca]
  quality: "Good quality consists, inside and out, of homogenous flesh-colored pink, glossy, and soft pieces without any foreign mineral matter."
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

Chi Shi Zhi (Halloysitum Rubrum) is sweet and warm and thus augments the qi; heavy in weight, such that it enters the lower burner; reddish in color, such that it enters the blood level; and sour, such that it stabilizes and binds. These characteristics also enable it to generate flesh, and thus assist in the healing of chronic sores; it is also applied externally for this indication. Its main areas of application, however, are in the treatment of chronic diarrhea and uterine bleeding associated with deficiency disorders.

Although because of its crimson color the earlier materia medica texts associated this substance with the Heart and blood, in the Grand Materia Medica, Li Shi-Zhen says that:

All five stone resins are medicinals of the hand and foot yang brightness channels. They are sweet and warm, heavy in weight, with an astringent nature. Astringent and heavy, they therefore inhibit dampness, stop bleeding, and stabilize the lower [body]; sweet and warm, they augment the qi, generate flesh, and adjust the middle. The 'middle' here means the Intestines, Stomach, flesh, muscles, palpitations with anxiety, and jaundice; the 'lower [body]' means blood in the stool, dysenteric disorders, incessant uterine bleeding, vaginal discharge, and spermatorrhea.

Li goes on to say that the separation of attributes by color in Miscellaneous Records of Famous Physicians is rather forced, but "of the white and crimson colored, the white enters the qi level while the red enters the blood level."

Li Gao says that this medicinal expels retained placenta, but many commentators have disagreed, pointing out that this would require an ability to transform blood stagnation. Others suggest that Li was probably referring to women whose Spleen and Stomach qi is so exhausted following childbirth that they lack the strength to expel the placenta normally. For them, the warm sweetness of Halloysitum Rubrum can augment the qi, and thereby assist in the elimination of the placenta.

---
---

## 🔑 TCM Properties

**Taste:** `= join(this.herb_data.taste, ", ")`
**Temperature:** `= this.herb_data.temperature`
**Channels Entered:** `= join(this.herb_data.channels, ", ")`

---

## ⚡ Functions & Actions

Binds up the Intestines and stops diarrhea: for chronic diarrhea due to cold from deficiency, or chronic dysenteric disorders with mucus and blood in the stool. Usually the diarrhea is chronic and is often accompanied by undigested food in the stool.
    - With Limonitum (Yu Yu Liang) for chronic dysenteric diarrhea and incontinence.
    - With Zingiberis Rhizoma (Gan Jiang) and Paeoniae Radix Alba (Bai Shao) for purulent, bloody stools and abdominal pain associated with chronic dysenteric disorders and rectal prolapse due to cold from deficiency, as in Peach Blossom Decoction (Tao Hua Tang).
    - Add Codonopsis Radix (Dang Shen) and Atractylodis Macrocephalae Rhizoma (Bai Zhu) for concurrent qi deficiency.
    - With Coptidis Rhizoma (Huang Lian), Scutellariae Radix (Huang Qin), and Zingiberis Rhizoma (Gan Jiang) for chronic, recurrent dysenteric disorders accompanied by such symptoms as tenesmus and the presence of thick, mucoid stools.
- Contains the blood and stops bleeding: for uterine bleeding, excessive menstruation, blood in the stool, and bleeding prolapsed rectum due to cold from deficiency of the lower burner. Also used topically for bleeding due to trauma.
    - With Sepiae Endoconcha (Hai Piao Xiao) and Platycladi Cacumen (Ce Bai Ye) for excessive uterine bleeding associated with cold from deficiency.
    - With Sophorae Flos (Huai Hua) and Sanguisorbae Radix (Di Yu) for blood in the stool.
- Promotes healing of wounds: used in ground form and applied topically for chronic nonhealing ulcers. Also used topically for weeping damp sores as well as prolapsed rectum.
    - With Fossilia Ossis Mastodi (Long Gu), Daemonoropis Resina (Xue Jie), and Olibanum (Ru Xiang) as a topical powder for nonhealing skin ulcers.
    - With Terra Flava Usta (Zao Xin Tu) as a topical powder for prolapsed rectum.

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
According to some traditional sources, this herb antagonizes Cinnamomi Cortex (Rou Gui).

Commentary on the Divine Husbandman's Classic of Materia Medica warns that before using astringent substances, most of the pathogenic influences that are causing the problem should be eliminated. For example, "if a vaginal discharge is completely damp-heat, it should not be used"; and "the method for incessant uterine bleeding should be to tonify the yin and clear heat; one cannot totally depend upon binding and restraint." This book goes on to warn that, in cases where the pathogenic influence has not been removed, "herbs to arrest and bind are certainly inappropriate: take care, take care!"

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
Good quality consists, inside and out, of homogenous flesh-colored pink, glossy, and soft pieces without any foreign mineral matter.

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
