---
# 🔹 Core Metadata (Universal Fields)
id: "herb-20251001123706"
name: "Jiang Huang"
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
  hanzi: "姜黄"
  pinyin: "Jiāng Huáng"
  pharmaceutical: "Curcumae longae Rhizoma"
  english: "Turmeric rhizome"
  alternate_names: []

  # TCM Properties
  taste: [Acrid, bitter, warm]
  temperature: "warm"
  channels: [Spleen, Stomach, Liver]

  # Clinical Information
  dosage: "3-9g"
  toxicity: "No serious adverse effects have been reported. Individual patients have experienced mild gastric discomfort and frequent bowel movements."
  functions: [Invigorates the blood, Unblocks menstruation, Promotes the movement of qi, Alleviates pain, Expels wind, Promotes the movement of blood]
  dui_yao: []

  # Additional Information
  constituents: [Curcuminoids: curcumin, demethoxycurcumin, bisdemethoxycurcumin, dihydrocurcumin, Sesquiterpenes: curlone, turmeronol A, B, germacrone-13-al, 4-hydroxybisabola-2,10-diene-9-one, 4-methoxy-5-hydroxybisabola-2,10-diene-9-one, 2,5-dihydroxybisabola-3,10-diene, 4,5-dihydroxybisabola-2,10-diene, procurcumadiol, curcumenone, dehydrocurdione, (4S,5S)-germacrone-4,5-epoxide, α-turmerone, bisacumol, bisacurone, curcumenol, procurcumenol, isoprocurcumenol, epiprocurcumenol, zedoaronediol, Volatile oil: turmerone, ar-turmerone, germacrone, curcumene, ar-curcumene, terpinene, curdione, curcumol, turmerone, cineole, caryophyllene, limonene, linalool, α-pinene, β-pinene, camphene, isoborneol, Other constituents: polysaccharides utonan A, B, C, D, β-sitosterol, campesterol, stigmasterol, cholesterol]
  quality: "Good quality is golden yellow, solid, slightly powdery, and aromatic. Rhizomes with a greenish yellow cross section are of inferior quality."
  text_first_appeared: "Tang Materia Medica"

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

Curcumae longae Rhizoma (jiang huang) has a relatively strong effect in dispelling blood stasis, as it regulates the flow of qi by driving it downward, regulates menstruation and stops pain; but various materia medica texts also note that it moves qi and disperses qi stagnation. It also expels wind and treats painful obstruction. For example, the Grand Materia Medica states that it "treats wind painful obstruction causing aching arms." Materia Medica of Combinations concurs, noting that it "treats pain due to hand and arm wind painful obstruction."

The ability of this herb to treat qi and blood stagnation is equally well-referenced. The Illustrated Classic of the Materia Medica notes that it "treats qi distention and defeated blood attacking the Heart following parturition", while the Materia Medica of Combinations says that it "breaks up blood [stasis] and drives qi downward." Rectification of the Meaning of Materia Medica goes somewhat further, observing that it "eliminates clumped qi distention in the epigastrium and abdomen, and pain due to cold qi and food accumulation." In this way it not only enters the blood level to invigorate the blood and dispel stasis, but also enters the qi level to disperse stagnant qi and drive it downward. These actions make it a valuable herb for gynecological disorders, and also for painful swellings due to trauma.

### Mechanisms of Selected Combinations

- **WITH CINNAMOMI RAMULUS (gui zhi)**

These herbs complement each other very well. Cinnamomi Ramulus (gui zhi) warms and unblocks the channels and collaterals, soothes spasms and contractions in the sinews, and facilitates joint movement, while Curcumae longae Rhizoma (jiang huang) breaks up blood stasis and moves the qi to treat pain in the arms. The ability of Curcumae longae Rhizoma (jiang huang) to promote the movement of blood also benefits from the yang qi-enhancing action of Cinnamomi Ramulus (gui zhi). This combination is commonly used for congealed painful obstruction in either the upper or lower limbs, but excels in the treatment of shoulder disorders, for which it serves as an excellent foundation.

---
---

## 🔑 TCM Properties

**Taste:** `= join(this.herb_data.taste, ", ")`
**Temperature:** `= this.herb_data.temperature`
**Channels Entered:** `= join(this.herb_data.channels, ", ")`

---

## ⚡ Functions & Actions

- Invigorates the blood and unblocks menstruation: for chest or abdominal pain, amenorrhea, or dysmenorrhea due to blood stasis caused by cold from deficiency. Also used for pain and swelling due to trauma or the early stages of sores and abscesses.
    - With Angelicae sinensis Radix (dang gui) and Corydalis Rhizoma (yan hu suo) for amenorrhea and abdominal pain from Liver qi constraint and blood stasis.
    - With Cinnamomi Cortex (rou gui) for dysmenorrhea and postpartum abdominal pain due to blood stasis.
    - With Cinnamomi Ramulus (gui zhi) for pain from cold induced blood stasis or wind-cold painful obstruction. This combination is especially useful for shoulder pain.
    - With Rhei Radix et Rhizoma (da huang) and Angelicae dahuricae Radix (bai zhi) as a topical powder for swelling and pain during the early stages of sores.
- Promotes the movement of qi and alleviates pain: for epigastric and abdominal pain due to stagnant qi.
    - With Curcumae Radix (yu jin) for distention and pain in the chest and flank.
- Expels wind and promotes the movement of blood: for wind-damp painful obstruction with blood stasis, especially in the shoulders.
    - With Notopterygii Rhizoma seu Radix (qiang huo), Saposhnikoviae Radix (fang feng), and Angelicae sinensis Radix (dang gui) for wind-damp painful obstruction, especially of the shoulder.

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
Contraindicated during pregnancy.

Whenever the disorder is arm pain due to blood deficiency, or abdominal pain due to blood deficiency, and there is no stagnant blood congealing and blocking, or qi clogging and rebelling upward causing distention, it should definitely not be used. A mistake will further damage the blood aspect, making the disorder turn serious. (Encountering the Sources of the Classic of Materia Medica)

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
Good quality is golden yellow, solid, slightly powdery, and aromatic. Rhizomes with a greenish yellow cross section are of inferior quality.

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
