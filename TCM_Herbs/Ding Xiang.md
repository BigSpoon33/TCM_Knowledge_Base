---
# 🔹 Core Metadata (Universal Fields)
id: "herb-20251001123706"
name: "Ding Xiang"
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
  hanzi: "丁香"
  pinyin: "Dīng Xiāng"
  pharmaceutical: "Caryophylli Flos"
  english: "Clove"
  alternate_names: []

  # TCM Properties
  taste: [Acrid, warm]
  temperature: "warm"
  channels: [Kidney, Spleen, Stomach]

  # Clinical Information
  dosage: "1-3g"
  toxicity: "There are no reports of toxic reactions within the normal dosage range. Overdosage can cause toxic reactions including nausea, vomiting, diarrhea, and upper gastrointestinal hemorrhage. Severe cases can lead to changes in liver function, dyspnea, loss of consciousness, and even death."
  functions: [Warms the middle burner and directs rebellious qi downward, Warms the Kidneys and aids the yang]
  dui_yao: []

  # Additional Information
  constituents: [Volatile oil: eugenol, acetyl eugenol, β-caryophyllene, β-caryophyllene epoxide, methyl-n-pentylketone, methyl-n-heptylketone, methyl salicylate, humulene, α-humulene epoxide, methyl benzoate, benzaldehyde, m-methoxybenzaldehyde, benzyl alcohol, furfural, vanillin, α-ylangene, chavicol, 1,8-cineol, carvacrol, Flavonoids: eugenin, eugenoside I, II, rhamnetin, kaempferol, eugenitin, isoeugenitin, isoeugenitol, Triterpenoids: oleanolic acid, 2α-hydroxyoleanolic acid methylester, sitosterol, stigmasterol, campesterol, Other constituents: isooleuropein, neooleuropein, oleoside, oleoside-7-methylester, tannins (eugeniin)]
  quality: "Good quality consists of full, oily, brownish red flower buds which sink down when placed in water."
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

Pure yang, acrid, warm, and aromatic, Caryophylli Flos (ding xiang) enters the Spleen and Stomach channels to warm the middle burner and direct Stomach qi downward, and is thus often used in the treatment of vomiting and hiccough due to Stomach cold. It also enters the Kidney channel and warms the lower burner in the treatment of impotence and cold sensations in the vagina.

Rectification of the Meaning of Materia Medica describes its effects: "warms the middle and eases the qi. Treats upper burner rebellion [causing] hiccough, eliminates Stomach cold diarrhea, [and any of] the five constraints affecting the seven emotions." In Convenient Reader of Materia Medica, Zhang Bing-Cheng concurs, but goes further:

Below, it reaches the Kidneys and Liver, guides the qi, expels cold. Whenever the lower burner has disorders such as running piglet, painful abdominal masses due to cold, mobile abdominal masses, and bulging disorders, as long as the Kidney yang is insufficient and there is coldness, this can be used for all.

---
---

## 🔑 TCM Properties

**Taste:** `= join(this.herb_data.taste, ", ")`
**Temperature:** `= this.herb_data.temperature`
**Channels Entered:** `= join(this.herb_data.channels, ", ")`

---

## ⚡ Functions & Actions

- **Warms the middle burner and directs rebellious qi downward:** for Stomach cold with vomiting, hiccough, abdominal pain, and diarrhea, and for Spleen or Stomach cold from deficiency with lack of appetite, vomiting, and diarrhea.
    - With Pinelliae Rhizoma preparatum (zhi ban xia) for abdominal pain and vomiting due to Stomach cold.
    - With Kaki Calyx (shi di) and Ginseng Radix (ren shen) for hiccough due to cold from deficiency, as in Clove and Persimmon Calyx Decoction (ding xiang shi di tang).
    - With Ginseng Radix (ren shen) and Pogostemonis Herba (huo xiang) for morning sickness.
    - With Amomi Fructus (sha ren) and Atractylodis macrocephalae Rhizoma (bai zhu) for vomiting, diarrhea, and reduced appetite due to Spleen and Stomach cold from deficiency.
- **Warms the Kidneys and aids the yang:** for impotence or clear vaginal discharge due to yang deficiency of the Kidneys. This type of vaginal discharge is regarded as a manifestation of Womb cold from deficiency and is usually accompanied by weakness in the legs.
    - With Cinnamomi Cortex (rou gui) and Morindae officinalis Radix (ba ji tian) for male impotence and female vaginal discharge due to Kidney deficiency.
    - With Rehmanniae Radix preparata (shu di huang), Asini Corii Colla (e jiao), and Artemisiae argyi Folium (ai ye) for persistent uterine bleeding with an ice-cold sensation in the lower abdomen, as in Clove, Ass-Hide Gelatin, and Ai Mugwort Decoction (ding xiang e jiao ai ye tang).

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
- Contraindicated in those with internal heat. Considered by a few traditional writers to be counteracted by Curcumae Radix (yu jin). See Toxicity below.
- "If nausea is due to Stomach fire, sudden turmoil disorder is due to summerheat, infestatious diarrhea (zhu xie), or pain is due to Heart deficiency - in all these cases it should be avoided." (Harm and Benefit in the Materia Medica)

"Acrid, hot, and drying, forbidden in any person with symptoms of fire. It should not be used for anything except cold from deficiency." (Harm and Benefit in the Materia Medica)

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
Good quality consists of full, oily, brownish red flower buds which sink down when placed in water.

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
