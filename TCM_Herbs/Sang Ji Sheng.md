---
# 🔹 Core Metadata (Universal Fields)
id: "herb-20251001123706"
name: "Sang Ji Sheng"
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
  hanzi: "桑寄生"
  pinyin: "Sāng Jì Shēng"
  pharmaceutical: "Taxilli Herba"
  english: "Taxillus, Mulberry Mistletoe Stems, Mistletoe"
  alternate_names: []

  # TCM Properties
  taste: [Bitter, Sweet, Neutral]
  temperature: "Neutral"
  channels: [Kidney, Liver]

  # Clinical Information
  dosage: "9-15g"
  toxicity: "No toxic effects should be expected within the normal dosage range. Allergic reactions have been reported, however, including papular rashes and pruritus."
  functions: [Tonifies the Liver and Kidneys, Strengthens the sinews and bones, Expels wind-dampness, Nourishes the blood, Calms the Womb, Benefits the skin]
  dui_yao: []

  # Additional Information
  constituents: [Flavonoids: avicularin, quercetin, quercitrin, hyperin, Phenolic compounds: catechol]
  quality: "Good quality consists of thin and young, reddish brown twigs with many leaves."
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

Sweet, bitter, and harmonious in that it is neither hot nor cold in nature, and rather moistening, tonifies the Liver and Kidney yin and blood, expels wind-dampness, unblocks the blood vessels, and quiets the fetus during pregnancy.
Encountering the Sources of the Classic of Materia Medica notes that Taxilli Herba (sang ji sheng) "has a nature that specifically expels wind, drives out dampness, unblocks and adjusts the blood vessels."
It is used particularly for chronic painful obstruction disorder, which over the long term has deprived the local joints, sinews, and bones of the nourishment from blood and essence, causing atrophy, weakness, and pain. This same ability to harmoniously nourish the essence and the blood of the Liver and Kidneys, along with the plant's quality of tenacity as a parasite, allows it to calm a disturbed fetus, manifesting as bleeding or pain in the lower back and abdomen.
The Divine Husbandman's Classic of the Materia Medica also notes that it firms the teeth and prevents hair loss, while Miscellaneous Records of Famous Physicians says that it "governs wounds from metal, expels painful obstruction, [and treats] continuous bleeding in women, internal injury and insufficiency, illnesses following parturition, and promotes lactation."
Seeking Accuracy in the Materia Medica explains that it specifically enters the Liver and Kidneys, and grows from the essential qi of the mulberry tree. Its flavor is bitter and sweet, with a neutral and harmonious nature that is neither hot nor cold. It is well known as an important medicinal for tonifying Kidneys and the blood. The reason is that the Kidneys govern the bones and hair, and govern the blood. Bitterness enters the Kidneys. When the Kidneys are tonified, the sinews and bones have strength and do not atrophy or ache. Sweetness tonifies the blood. When the blood is tonified, the hair receives its sustaining irrigation and does not become parched and fall out. Thus, whenever the lower back aches, the sinews and bones are disordered, or the fetus [threatens to] miscarry, or externally there are muscle and skin wounds from metal, or wind-dampness, in all such cases this is the main treatment.
This passage goes on to repeat Li Shi-Zhen's warning, in the Grand Materia Medica, that only the parasite from the mulberry tree is the true herb, and that to be sure, one must collect it oneself, although "if it is still attached to mulberry leaves, it can be used."

---
---

## 🔑 TCM Properties

**Taste:** `= join(this.herb_data.taste, ", ")`
**Temperature:** `= this.herb_data.temperature`
**Channels Entered:** `= join(this.herb_data.channels, ", ")`

---

## ⚡ Functions & Actions

*   **Tonifies the Liver and Kidneys, strengthens the sinews and bones, and expels wind-dampness:** for insufficiency of Liver and Kidney yin with soreness and pain in the lower back and legs, joint problems, numbness, and weakness and atrophy of the sinews and bones. Can be used for these problems whether or not wind-dampness is present.

    *   With Angelicae Pubescentis Radix (du huo) and Achyranthis Bidentatae Radix (niu xi) for pain, stiffness, and soreness of the lower back and lower extremities due to wind dampness and Liver and Kidney deficiency, as in Pubescent Angelica and Taxillus Decoction (du huo ji sheng tang).
    *   With Cervi Cornu Pantotrichum (lu rong) and Eucommiae Cortex (du zhong) for lower back and leg pain from Kidney qi deficiency.
    *   With Rehmanniae Radix (sheng di huang), Paeoniae Radix Rubra (chi shao), and Spatholobi Caulis (ji xue teng) for headache, dizziness, tinnitus, and palpitations due to Liver and Kidney yin deficiency with ascendant yang.
*   **Nourishes the blood and calms the Womb:** for restless fetus or uterine bleeding during pregnancy. Also promotes lactation.

    *   With Dipsaci Radix (xu duan), Cuscutae Semen (tu si zi), and Asini Corii Colla (e jiao) for restless fetus and threatened miscarriage due to Liver and Kidney deficiency, as in Fetus Longevity Pill (shou tai wan).
    *   With Asini Corii Colla (e jiao) and Artemisiae Argyi Folium (ai ye) for restless fetus accompanied by stabbing abdominal pain.
    *   With Mori Cortex (sang bai pi), Perillae Caulis (zi su geng), and Arecae Pericarpium (da fu pi) for edema that develops during pregnancy.
*   **Nourishes the blood and benefits the skin:** for dry, scaly skin due to blood deficiency.

    *   With chicken eggs and brown sugar for dry and scaly skin due to blood deficiency.

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
None noted. See TOXICITY below.

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
Good quality consists of thin and young, reddish brown twigs with many leaves.

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
