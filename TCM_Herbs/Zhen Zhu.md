---
# 🔹 Core Metadata (Universal Fields)
id: "herb-20251001123706"
name: "Pearl / Zhen Zhu"
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
  hanzi: "真珠"
  pinyin: "Zhen Zhu"
  pharmaceutical: "Margarita"
  english: "Pearl"
  alternate_names: []

  # TCM Properties
  taste: [Sweet, salty, cold]
  temperature: "cold"
  channels: [Heart, Liver]

  # Clinical Information
  dosage: "0.3-1g"
  toxicity: "None"
  functions: [Sedates the Heart, settles tremors and palpitations, Clears the Liver, eliminates superficial visual obstructions, Promotes healing, generates flesh]
  dui_yao: []

  # Additional Information
  constituents: [Inorganic constituents (>87%): calcium carbonate (>80%), magnesium carbonate (>7%), calcium phosphate, silicium oxide, aluminum oxide, traces of Na, Mn, Fe, Zn, Ti, Organic constituents (6-13%): protein (amino acids: alanine, glycine, glutamic acid, aspartic acid, leucine, methionine, arginine, threonine, serine, cystine, tyrosine, phenylalanine), taurine, sugars, pigments (carotenoids, flavoxanthin)]
  quality: "Good quality consists of large, pure, round, fine, hard, lustrous pearls with distinct concentric layers in cross section."
  text_first_appeared: "Materia Medica of the Kaibao Era"

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

Sweet, salty, and cold, Margarita (zhen zhu) enters the Heart and Liver channels to clear heat from these two channels, and to calm the spirit, calm the Liver, and reduce superficial visual obstructions. It augments the yin and resolves toxicity and is used for palpitations, withdrawal-mania, childhood convulsions, and superficial visual obstructions with impaired vision, as well as for ulceration of the throat and gums. Applied topically, it restrains, inhibits, and generates flesh. The Materia Medica of the Kaibao Era says that it "sedates the Heart; applied as eyedrops it expels membranous superficial visual obstructions."

Seeking Accuracy in the Materia Medica explains that it enters the arm lesser yin Heart channel and leg terminal yin Liver channel. When the Heart has heat from deficiency, the spirit floats and strays; when the Liver has heat from deficiency, the eyes generate superficial visual obstructions. When the heat is expelled from theses two channels, the Heart is sedated and the vision is improved.

In Convenient Reader of Materia Medica, Zhang Bing Cheng observes:

It is generated endowed with the essential qi of the greater yin [i.e., the moon, so it] clears heat, augments the yin, and resolves toxicity. Because it is sweet, bland, salty, and cold in nature, it sedates the Heart, settles fright, and can remedy mania. It treats childhood convulsions with phlegm confusion, enters the Liver to brighten the eyes, generate flesh, reduce superficial visual obstructions, and enhance the complexion .... Augmenting the yin and resolving toxicity are its intrinsic actions.

Materia Medica from the [Southern} Seaboard Area and other texts note that it can eliminate darkish discolorations on the face, such as chloasma, and improve the complexion. For this reason, Margarita (zhen zhu) is included in a number of topically applied facial creams and beauty preparations.

**Mechanisms of Selected Combinations**

WITH Bovis Calculus (niu huang); see page 961

---
---

## 🔑 TCM Properties

**Taste:** `= join(this.herb_data.taste, ", ")`
**Temperature:** `= this.herb_data.temperature`
**Channels Entered:** `= join(this.herb_data.channels, ", ")`

---

## ⚡ Functions & Actions

*   **Sedates the Heart and settles tremors and palpitations:** For palpitations, childhood convulsions, and seizures. Also used for disharmony of the Heart and spirit wherein the patient is easily frightened or angered.
    *   With Ziziphi spinosae Semen (suan zao ren), Platycladi Semen (bai zi ren), and Schisandrae Fructus (wu wei zi) for irritability and insomnia from Heart deficiency with heat.
    *   With Angelicae sinensis Radix (dang gui), Rehmanniae Radix preparata (shu di huang), and Ginseng Radix (ren shen) for continuous palpitations and insomnia from Heart and Liver blood deficiency.
    *   With Succinum (hu po), Arisaematis Rhizoma preparata (zhi tian nan xing), and Cinnabaris (zhu sha) for palpitations with anxiety, seizures, or childhood convulsions.
    *   With Pinelliae Rhizoma preparatum (zhi ban xia), Uncariae Ramulus cum Uncis (gou teng), and Poria (fu ling) for continuous palpitations or palpitations with anxiety as well as disorientation.
    *   With Bovis Calculus (niu huang) and Coptidis Rhizoma (huang lian) for childhood convulsions, as in Calm the Palace Pill with Cattle Gallstone (an gong niu huang wan).
*   **Clears the Liver and eliminates superficial visual obstructions:** For blurred vision due to pterygium or other superficial disorders of the eyes. Often used topically as a powder.
    *   With Bovis Calculus (niu huang) and Borneolum (bing pian) for red eyes or superficial visual obstructions. This combination is also used for severe pain, swelling, and ulceration of the throat. It is generally applied topically as a powder and can be used for severe, chronic, nonhealing ulcerations anywhere on the body.
    *   With Chrysanthemi Flos (ju hua) and Haliotidis Concha (shi jue ming) for wind-heat affecting the Liver channel with red, dry, and painful eyes along with superficial visual obstructions.
*   **Promotes healing and generates flesh:** Used topically as a powder for chronic, nonhealing ulcers or macerated areas (usually throat or gums).
    *   With Borax (peng sha), Indigo naturalis (qing dai), and Borneolum (bing pian) as a powder applied topically for sores in the oral cavity and face, including those affecting the teeth, throat, and ears.

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
"Do not use if the disorder is not due to fire." (Commentary on the Divine Husbandman's Classic of Materia Medica)

"In toxic sores, if the interior toxin has not been completely [cleared], and one carelessly uses Margarita (zhen zhu) to generate flesh, the sores will subsequently have trouble healing over." (New Compilation of Materia Medica)
Use with caution during pregnancy.

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
Good quality consists of large, pure, round, fine, hard, lustrous pearls with distinct concentric layers in cross section.

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
