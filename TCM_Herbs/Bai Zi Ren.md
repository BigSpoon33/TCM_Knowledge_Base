---
# 🔹 Core Metadata (Universal Fields)
id: "herb-20251001123706"
name: "Bai Zi Ren"
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
  hanzi: "柏子仁"
  pinyin: "Bai Zi Ren"
  pharmaceutical: "Platycladi Semen"
  english: "Arborvitae seed, Oriental arborvitae, Chinese arborvitae, biota"
  alternate_names: []

  # TCM Properties
  taste: [Sweet]
  temperature: "Neutral"
  channels: [Heart, Kidney, Large Intestine]

  # Clinical Information
  dosage: "3-9g"
  toxicity: "As fat seeds, Platycladi Semen bear a high risk of being contaminated by carcinogenic aflatoxins. Good quality appropriate storage in a cool and dry place with good air circulation (not in a tightly sealed container or plastic bag) and regular turnover of stock is recommended for herbal dispensaries. Distributors need to regularly test their stock to be sure that aflatoxins are not present."
  functions: [Nourishes the Heart blood and yin to calm the spirit, Moistens the Kidneys and Large Intestine]
  dui_yao: []

  # Additional Information
  constituents: [Fixed oil: α-cedrol, platydiol, 5-hydroxypinusolidic acid, 5,11,14-eicosatrienoic acid, 5,11,14,17-eicosatetraenoic acid, Flavonoids: 5-hydroxy-7,4'-dimethoxyflavone, Phenolic compounds: (+)-catechin, (-)-epicatechin, procyanidin B-1, procyanidin B-3, Other constituents: vitamin A, β-sitosterol, volatile oil, proteins, saponins]
  quality: "Good quality consists of full, fresh, brownish yellow, oily seeds."
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

Sweet and neutral with a gentle, harmonious nature, the sweetness of Platycladi Semen (bai zi ren) enriches and tonifies, while its moisture eliminates dryness. Entering the Heart channel, it nourishes the Heart and calms the spirit; entering the Kidneys it tonifies the true yin and moistens Kidney dryness; entering the Large Intestine, it moistens the Intestines and unblocks stool. It is commonly used for anxiety, palpitations, and insomnia with dream-disturbed sleep due to Heart blood deficiency failing to nourish the spirit. It is also important for dry stools and constipation due to yin and blood deficiency. When the Kidney yin is exhausted, with sensations of heat, weakness in the knees and lower back, and amenorrhea due to yin and blood deficiency, Platycladi Semen (bai zi ren) can be used as an assistant herb.

The Grand Materia Medica states that it has a nature that is neither cold nor drying; its sweet flavor tonifies, its acrid flavor moistens, with a clear, fragrant aroma that penetrates the Heart and Kidneys, and augments the Spleen and Stomach - [for all of these reasons] it is considered in the top grade of herbs [in the Divine Husbandman's categories]. It should be used in prescriptions for enriching and nourishing.

Zhang Jie-Bin, however, points out that the herb's tonifying actions are limited. As an advocate of warm tonification, he describes Platycladi Semen (bai zi ren) as "sweet and neutral, with a slightly cooling nature." In Rectification of the Meaning of Materia Medica, Zhang notes:

In sum, it is cooling and aromatic with a moistening, slippery nature, and although it is excellent for enriching the yin and nourishing the blood, if one wishes to cultivate and tonify the fundamentals, this is not the strong point of a cooling herb.

Because the herb enters both the Heart and Kidney channels and moistens, it has been used as an aid to hair growth, particularly in those cases associated with blood deficiency and exhaustion of essence. One of its preparations involves combining it with Angelicae sinensis Radix (dang gui), grinding both herbs into a powder, and adding honey to make pills which are taken in doses of 6-9g, three times a day.

---
---

## 🔑 TCM Properties

**Taste:** `= join(this.herb_data.taste, ", ")`
**Temperature:** `= this.herb_data.temperature`
**Channels Entered:** `= join(this.herb_data.channels, ", ")`

---

## ⚡ Functions & Actions

- **Nourishes the Heart and calms the spirit:** For irritability, insomnia, forgetfulness, and palpitations with anxiety due to Heart yin deficiency and insufficient blood. Also used for night terrors in children, as a stand-alone herb in powder form.
  - With Ziziphi spinosae Semen (suan zao ren), Angelicae sinensis Radix (dang gui), and Poriae Sclerotium pararadicis (fu shen) for palpitations and insomnia due to Heart blood deficiency, as in Nourish the Heart Decoction (yang xin tang).
  - With Ophiopogonis Radix (mai men dong), Rehmanniae Radix preparata (shu di huang), and Acori tatarinowii Rhizoma (shi chang pu) for irritability, poor sleep, palpitations, and nocturnal emissions from lack of communication between the Heart and Kidneys, as in Arborvitae Seed Pill to Nourish the Heart (bai zi yang xin wan).
  - With Ginseng Radix (ren shen), Schisandrae Fructus (wu wei zi), and Atractylodis macrocephalae Rhizoma (bai zhu) for Heart blood deficiency leading to loss of nourishment for the Heart with severe palpitations, irritability from deficiency, vertigo, forgetfulness, and insomnia.
- **Moistens the Intestines and unblocks the bowels:** For constipation in the elderly, debilitated, and postpartum women due to blood or yin deficiency.
  - With Cannabis Semen (huo ma ren) and Juglandis Semen (he tao ren) for constipation in the elderly or in postpartum women due to blood deficiency. An alternative would be to combine with Persicae Semen (tao ren), Armeniacae Semen (xing ren), and Pruni Semen (yu li ren), as in Five-Seed Pills (wu ren wan).
- **Also used for nightsweats due to yin deficiency.**
  - With Ephedrae Radix (ma huang gen) and Ostreae Concha (mu li) for nightsweats due to yin deficiency.

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
Contraindicated in those with loose stools or phlegm disorders.
According to some traditional sources, this herb antagonizes Chrysanthemi Flos (ju hua).
Commentary on the Divine Husbandman's Classic Materia Medica observes that it is quite oily in form and nature, and should not be taken by those with Intestinal leakage causing diarrhea, or by those with excessive phlegm around the diaphragm. Its standard contraindications are [in those cases of] "repeated erections", "Kidney patients with heat", and summerheat dampness causing diarrhea.
Medicinal Combining adds: "Forbidden in four situations: those with excessive phlegm, Lung qi floating upward, loose stools, and Stomach deficiency with an urge to vomit."

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
Good quality consists of full, fresh, brownish yellow, oily seeds.

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
