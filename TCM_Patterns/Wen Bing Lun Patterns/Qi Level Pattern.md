---
id: pattern-20251115-qi-level-pattern
name: Qi Level Pattern
type: pattern
aliases:
- Wei Qi Stage Heat
- Qi Stage Heat
tags:
- TCM
- Pattern
category:
- Four Levels
- Zang Fu
- Eight Principles
- Qi Blood
- Six Stages
- San Jiao
- Channel
- Five Elements
related:
- Lung Heat
- Damp-Heat in the Lungs
- Ying Level Pattern
- Blood Level Pattern
symptoms: []
patterns: []
western_conditions:
- [[Pneumonia]]
- [[Bronchitis]]
- [[Influenza]]
- [[Upper Respiratory Infection]]
formulas:
- [[Ma Xing Shi Gan Tang]]
- [[Xuan Bai Cheng Qi Tang]]
- [[Qing Wei San]]
herbs:
- [[Ma Huang]]
- [[Xing Ren]]
- [[Shi Gao]]
- [[Gan Cao]]
- [[Zhi Zi]]
- [[Huang Qin]]
- [[Lian Qiao]]
- [[Jin Yin Hua]]
points:
- [[LU5 (Chi Ze)]]
- [[LI11 (Qu Chi)]]
- [[DU14 (Da Zhui)]]
- [[ST40 (Feng Long)]]
- [[BL13 (Fei Shu)]]
nutrition: []
tests: []
created: 2024-10-27
updated: 2024-10-27

---
# `=this.name`

**Type:** `= this.pattern_data.pattern_type`
**Nature:** `= this.pattern_data.excess_deficiency` | `= this.pattern_data.hot_cold`
**Location:** `= this.pattern_data.interior_exterior`


## 🏷️ Pattern Classification

**System:** `= this.pattern_data.pattern_type`
**Subtype:** `= this.pattern_data.pattern_subtype`

**Eight Principles Analysis:**
- Excess/Deficiency: `= this.pattern_data.excess_deficiency`
- Hot/Cold: `= this.pattern_data.hot_cold`
- Interior/Exterior: `= this.pattern_data.interior_exterior`
- Yin/Yang: `= this.pattern_data.yin_yang`


## 🔍 Clinical Manifestations

### Cardinal Symptoms (CAM)
**Essential Symptoms:**
- High fever, often 102°F (39°C) or higher
- Aversion to heat, preferring cool environments
- Significant thirst, often desiring cold drinks
- Red tongue with thick-yellow coating, indicating intense Heat
- Rolling, rapid pulse, reflecting the excess Heat and its impact on the circulation

### Complete Symptom Picture

**Chief Symptoms:**
- High fever
- Aversion to heat
- Thirst

**Accompanying Symptoms:**
- Cough with expectoration of thin-yellow or thick-yellow sputum
- Asthma or wheezing
- Restlessness or irritability
- Dry mouth and throat
- Constipation (possible due to fluid depletion)
- Sweating (sometimes)

**Tongue:** `= this.pattern_data.tongue`

**Pulse:** `= this.pattern_data.pulse`


## 🔄 Differential Diagnosis

### Similar Patterns

| Feature | This Pattern | [[Lung Heat]] | [[Damp-Heat in the Lungs]] |
|---------|--------------|-------------------|-------------------|
| Chief symptom | High fever, thirst | Cough, thick yellow sputum | Cough, sticky yellow sputum, chest oppression |
| Tongue | Red, thick yellow coating | Red, yellow coating, possibly dry | Red, sticky yellow coating |
| Pulse | Rolling, rapid | Rapid, possibly slippery | Slippery, rapid |
| Key distinction | Systemic Heat signs (high fever, thirst) | Predominantly Lung symptoms | Dampness component (chest oppression, sticky sputum) |

**vs. [[Lung Heat]]:**
- Key difference: Qi Level Pattern presents with more systemic Heat signs like very high fever and strong thirst, whereas Lung Heat is more localized to the lungs.

**vs. [[Damp-Heat in the Lungs]]:**
- Key difference: Qi Level Pattern is primarily characterized by Heat, while Damp-Heat in the Lungs also includes significant Dampness signs like chest oppression, sticky sputum and a greasy tongue coating.


### Key Herbs

**Essential Herbs for This Pattern:**
- [[Shi Gao]] – Clears Heat, drains Fire, generates fluids. Dosage: 15-30g
- [[Ma Huang]] – Releases the exterior, disperses the Lungs, relieves asthma. Dosage: 3-9g (use with caution, especially in patients with underlying Yin Deficiency)
- [[Xing Ren]] – Descends Lung Qi, stops cough, transforms Phlegm. Dosage: 6-9g

```dataview
TABLE
    herb_data.taste as "Taste",
    herb_data.temperature as "Temp",
    herb_data.channels as "Channels",
    herb_data.functions as "Functions"
FROM ""
WHERE type = "herb" AND contains(patterns, this.file.link)
SORT file.name
LIMIT 15
```


##  Contraindications & Cautions

**Treatment Contraindications:**
- Exterior Deficiency: If there are signs of concurrent Exterior Deficiency (e.g., aversion to wind, spontaneous sweating), use caution with strong heat-clearing herbs that may further weaken the Wei Qi.
- Weak constitution: In patients with a weak constitution, use smaller doses of heat-clearing herbs and consider adding Qi-tonifying herbs to support the body's Qi.
- Yin Deficiency with Empty Heat: Avoid using drying heat-clearing herbs if there is underlying Yin Deficiency, as this can exacerbate the Yin Deficiency.

**Cautions:**
- Ma Huang should be used with caution in patients with hypertension or heart conditions due to its potential to raise blood pressure.
- Monitor the patient's condition closely for any signs of adverse reactions to the herbs.
- Adjust the herbal formula based on the patient's individual presentation and response to treatment.

**When to Avoid:**
- Avoid strong heat-clearing herbs during pregnancy unless absolutely necessary, and only under the guidance of an experienced practitioner.
- Avoid using cold, bitter herbs for prolonged periods, as this can damage the Spleen Qi.


## 🏷️ Western Medical Correlates

**Common Western Diagnoses:**
- Pneumonia
- Bronchitis
- Influenza
- Upper Respiratory Infection

**Biomedical Understanding:**
From a biomedical perspective, these conditions involve inflammation of the respiratory tract caused by viral or bacterial infections. This inflammation leads to symptoms such as fever, cough, sputum production, and difficulty breathing.

**Integration Notes:**
TCM pattern diagnosis can help differentiate between different types of respiratory infections based on the specific TCM pattern presentation. For example, the Qi Level Pattern would correspond to a severe infection with significant inflammation and systemic symptoms. Treatment can then be tailored to address the specific TCM pattern, potentially leading to more effective outcomes.


## ✅ Clinical Pearls & Experience

### Clinical Tips
- Always check the tongue and pulse to confirm the diagnosis.
- Use caution with strong heat-clearing herbs in patients with a weak constitution.
- Monitor the patient's condition closely for any signs of adverse reactions to the herbs.

### Common Mistakes
- Misdiagnosing a Wei Level Pattern as a Qi Level Pattern.
- Using overly strong heat-clearing herbs in patients with Yin Deficiency.
- Neglecting to address underlying deficiencies that may have contributed to the development of the pattern.

### Treatment Modifications
- **If there is concurrent Phlegm:** Add herbs like Ban Xia and Chen Pi to transform Phlegm.
- **If there is constipation:** Add herbs like Da Huang to promote bowel movements.

### Success Indicators
- Reduction in fever
- Improvement in cough and sputum production
- Relief of thirst
- Normalization of pulse


## ✅ Pattern Comparison Table

| Feature | Qi Level Pattern | Wei Level Pattern | Ying Level Pattern |
|---|---|---|---|
| Fever | High, often 102°F (39°C) or higher | Mild to moderate | May be high or low |
| Aversion to | Heat | Wind, cold | Variable |
| Thirst | Pronounced | Mild | May be present |
| Tongue | Red, thick yellow coating | Thin white or yellow coating | Red, peeled coating |
| Pulse | Rolling, rapid | Floating, rapid | Thready, rapid |
| Mental State | Generally clear | Clear | Restlessness, delirium |


## 📚 References & Resources

- Maciocia, Giovanni. *The Foundations of Chinese Medicine: A Comprehensive Text for Acupuncturists and Herbalists*. 3rd ed. Churchill Livingstone, 2015.
- Wiseman, Nigel, and Ye Feng. *A Practical Dictionary of Chinese Medicine*. 2nd ed. Paradigm Publications, 2002.
