---
# 🔹 Core Metadata (Universal Fields)
id: "herb-20251001123706"
name: "Shan Dou Gen"
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
  hanzi: "山豆根"
  pinyin: "Shān dòu gēn"
  pharmaceutical: "Sophorae Tonkinensis Radix"
  english: "Tonkin Sophora Root"
  alternate_names: []

  # TCM Properties
  taste: [Bitter]
  temperature: "Cold"
  channels: [Lung, Large Intestine]

  # Clinical Information
  dosage: "3-9g"
  toxicity: "While Sophorae tonkinensis Radix (shan dou gen) is potentially toxic, the primary reason for this is overdosage. In traditional preparations, doses higher than 9g can cause toxicity. The main symptoms appear 30 minutes after ingestion: dizziness, blurred vision, chills, vomiting, and palpitations. In severe cases the following symptoms may appear: numbness of the limbs, severe headache, tachypnea, epigastric and abdominal fullness, generalized muscle tremors, tachycardia or bradycardia, unconsciousness, cyanosis, dilated pupils, and possible death due to respiratory failure. A lethal case of toxicity was reported after ingestion of a decoction of 60g of the herb. It should therefore be used with caution, and doses over 9g must be avoided."
  functions: [Clears heat, Resolves fire toxicity, Improves the condition of the throat, Disperses swellings]
  dui_yao: []

  # Additional Information
  constituents: [Alkaloids: matrine, oxymatrine, anagyrine, (-)-cytisine, methylcytisine, (+)-sophocarpine N-oxide, sophoramine, sophoranol, sophocarpine, dauricine, Flavonoids: sophoranone, sophoradin, sophoranone, sophoradochromene, sophoranochromene, genistein, 2',4',7-trihydroxy-6,8-bis(3-methyl-2-butenyl)flavonone, sophoraflavone A, B, Triterpene saponines: subproside I, II, soyasaponin II, dehydro soyasaponin I, soyasaponin I methylester, soyasaponin II methylester, soyasaponin A methylester, kudzusaponin A, kudzusapogenol A methylester, abrisaponin I, kalikasaponin I methylester, Other constituents: pterocarpine, maackiaintrifolirhizin, lupeol]
  quality: "Good quality consists of thick, solid roots with a bitter taste."
  text_first_appeared: "Illustrated Classic of the Materia Medica"

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

Very cold and bitter, with a nature that excels in draining and directing downward, Sophorae tonkinensis Radix (shan dou gen) clears and drains Lung and Stomach fire. It is best for resolving toxicity, benefiting the throat, and reducing swelling, and is most appropriate for the treatment of swollen, sore throat due to overwhelming accumulation of heat toxin, and swelling and pain of the gums and teeth.

The Illustrated Classic of the Materia Medica says about Sophorae tonkinensis Radix (shan dou gen): "holding [it] in the mouth and swallowing the juice resolves toxic swelling of the throat in a way that is truly remarkable."

Essentials of the Materia Medica confirms that Sophorae tonkinensis Radix (shan dou gen) "drains heat, resolves toxicity, and expels wind-heat from the Lung and Large Intestine. Holding the herb in the mouth and swallowing the juice stops throat pain, swollen gums, and toothache."

Rectification of the Meaning of Materia Medica provides clear guidelines for its use:

Nowadays it is used specifically for swelling and pain of the throat, based on the Illustrated Classic of the Materia Medica which says that it is really marvelous if held in the mouth to relieve swelling and pain of the throat. In Encountering the Sources of the Classic of Materia Medica, Zhang Lu says that one can either soak it in water then gargle, or decoct it and sip it gradually.

However, Zhang Shan-Lei warns:

Whenever roots are used in medicine, one is generally utilizing their ability to descend and direct downward. This herb is also very cold and very bitter, which directly cuts off the upward-blazing of toxic fire-but it is solely appropriate for fire from excess. A sore throat due to external binding of pathogenic wind must be opened and drained with acrid coolness, thus this herb must not be used too early or it will suppress the dispersal [of the pathogenic wind] and greatly increase its encumbrance .... If a pathogen is still present in the exterior, and one first uses coldness and directs it downward, then the external pathogen will not disperse, but rather be made to attack internally. If the heat is blazing, and light, rising herbs are mistakenly prescribed, then it will be like a fierce fire blown by the wind-the immediate result is scorched earth. In the clinic, these disorders must be differentiated beforehand without fail.

While this herb was included in ancient formulas for damp-heat jaundice, it is not commonly used for that purpose today.

---
---

## 🔑 TCM Properties

**Taste:** `= join(this.herb_data.taste, ", ")`
**Temperature:** `= this.herb_data.temperature`
**Channels Entered:** `= join(this.herb_data.channels, ", ")`

---

## ⚡ Functions & Actions

- Clears heat, resolves fire toxicity, and improves the condition of the throat: for swollen, painful throat. Can be used alone, both internally and as a gargle.
    - With Isatidis Radix (bei ban lan gen) for pain and swelling of a very red throat, painful teeth, and swollen and painful gums, sometimes accompanied by sores of the mouth and tongue.
    - With Belamcandae Rhizoma (she gan) for phlegm-heat in the throat with a swollen, sore throat and phlegm that is difficult to expectorate.
- Clear heat, resolves fire toxicity, and disperses swellings: for abscesses and other toxic sores. Also used for cancers, especially of the throat and lungs.
    - With Lonicerae Flos (jin yin hua), Forsythiae Fructus (lian qiao), and Coptidis Rhizoma (huang lian) for abscesses and toxic sores.

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
Inappropriate for those with cold from deficiency of the Spleen and Stomach, poor appetite, or loose stools. See Toxicity below.

"Very cold and very bitter, to which the Spleen and Stomach are most averse. Those who get full easily and have diarrhea should never allow it to pass their lips. It is also prohibited in those who are deficient." (Harm and Benefit in the Materia Medica)

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
Good quality consists of thick, solid roots with a bitter taste.

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
