---
id: pattern-20251115-phlegm-fluids
name: Phlegm-Fluids
type: pattern
aliases:
- Tan Yin
- Watery Phlegm
tags:
- TCM
- Pattern
category:
- Qi Blood Body Fluids
- Zang Fu
- Eight Principles
- Qi Blood
- Six Stages
- Four Levels
- San Jiao
- Channel
- Five Elements
related:
- Spleen Qi Deficiency
- Kidney Yang Deficiency
- Phlegm-Damp
- Phlegm-Heat
- Lung Qi Deficiency
symptoms: []
patterns: []
western_conditions:
- [[Bronchitis]]
- [[Asthma]]
- [[COPD]]
- [[Pneumonia]]
- [[Edema]]
- [[Meniere's Disease]]
- [[Vertigo]]
formulas:
- [[Ling Gui Zhu Gan Tang]]
- [[Er Chen Tang]]
- [[Wu Ling San]]
- [[Bei Mu Gua Lou San]]
herbs:
- [[Fu Ling]]
- [[Gui Zhi]]
- [[Bai Zhu]]
- [[Gan Cao]]
- [[Ban Xia]]
- [[Chen Pi]]
- [[Zhi Shi]]
- [[Zhi Gan Cao]]
- [[Ze Xie]]
- [[Zhu Ling]]
- [[Bai Shu]]
- [[Gua Lou]]
- [[Bei Mu]]
points:
- [[SP-9]]
- [[LU-1]]
- [[ST-40]]
- [[REN-12]]
- [[BL-20]]
- [[BL-22]]
- [[KI-3]]
- [[LI-4]]
- [[PC-6]]
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
- Watery sputum
- Rattling sounds in the throat
- Dizziness

### Complete Symptom Picture

**Chief Symptoms:**
- Cough with copious, watery sputum
- Dizziness, often described as a feeling of being lightheaded or unsteady
- Rattling or gurgling sounds in the throat and chest

**Accompanying Symptoms:**
- Nausea, sometimes leading to vomiting of clear, watery fluids
- Edema, particularly in the lower limbs
- Pale complexion
- Fatigue and lethargy
- Cold limbs
- Loose stools
- Poor appetite

**Tongue:** `= this.pattern_data.tongue`

**Pulse:** `= this.pattern_data.pulse`


## 🔄 Differential Diagnosis

### Similar Patterns

| Feature | This Pattern | Similar Pattern 1 | Similar Pattern 2 |
|---------|--------------|-------------------|-------------------|
| Chief symptom | Watery sputum | Sticky, profuse sputum | Scanty, difficult to expectorate sputum |
| Tongue | Pale, swollen, white greasy coat | Red, yellow greasy coat | Dry, red, little coat |
| Pulse | Slippery, weak | Slippery, rapid | Wiry, thin |
| Key distinction | Thin, watery sputum; dizziness | Thick, sticky sputum; heat signs | Dryness, Yin deficiency signs |

**vs. [[Phlegm-Damp]]:**
- Key difference: Phlegm-Damp presents with thicker, stickier sputum and a feeling of heaviness, while Phlegm-Fluids is characterized by watery sputum and dizziness.

**vs. [[Phlegm-Heat]]:**
- Key difference: Phlegm-Heat involves yellow, thick sputum and heat signs such as fever, thirst, and a red tongue, whereas Phlegm-Fluids does not present with heat signs and the sputum is clear and watery.


### Key Herbs

**Essential Herbs for This Pattern:**
- [[Fu Ling]] – Drains Dampness, strengthens the Spleen, and harmonizes the Middle Jiao. Dosage: 9-15g
- [[Gui Zhi]] – Warms the Yang, transforms fluids, and promotes Qi circulation. Dosage: 3-9g. Use with caution in cases of Yin deficiency.
- [[Bai Zhu]] – Strengthens the Spleen, dries Dampness, and regulates Qi. Dosage: 6-12g.
- [[Gan Cao]] – Harmonizes the formula and tonifies the Spleen. Dosage: 3-6g.
- [[Ban Xia]] - Dries dampness, transforms phlegm, and descends rebellious Qi. Dosage: 6-9g
- [[Ze Xie]] - Promotes urination and drains dampness. Dosage: 9-15g

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
- Overly drying or warming herbs in cases of Yin deficiency
- Strong purgatives in patients with weak constitution
- Astringent herbs that may trap the fluids further

**Cautions:**
- Use warming herbs cautiously in patients with underlying Heat conditions.
- Monitor the patient for signs of dehydration if using diuretics.
- Adjust the formula based on the individual's constitution and presenting symptoms.

**When to Avoid:**
- Avoid strong diuretics in patients with severe Qi deficiency.


## 🏷️ Western Medical Correlates

**Common Western Diagnoses:**
- Bronchitis
- Asthma
- COPD
- Pneumonia
- Edema
- Meniere's Disease
- Vertigo

**Biomedical Understanding:**
From a biomedical perspective, these conditions are often associated with inflammation, fluid accumulation in the lungs or other tissues, and impaired respiratory function. For example, bronchitis involves inflammation of the bronchial tubes, leading to increased mucus production. Asthma is characterized by airway inflammation and constriction, causing wheezing and difficulty breathing. Meniere's Disease involves fluid imbalances in the inner ear, leading to vertigo and tinnitus.

**Integration Notes:**
TCM pattern diagnosis can add valuable information to Western diagnoses by identifying the underlying imbalances contributing to the symptoms. For instance, while a Western diagnosis of bronchitis focuses on the inflammation of the bronchial tubes, a TCM diagnosis of Phlegm-Fluids identifies the Spleen Qi Deficiency as the root cause, leading to a more holistic treatment approach.


## ✅ Clinical Pearls & Experience

### Clinical Tips
- Always assess the patient's Spleen Qi and Kidney Yang status when diagnosing Phlegm-Fluids.
- Consider dietary modifications, such as reducing damp-producing foods, to support treatment.
- Use acupuncture points to regulate Qi and promote fluid metabolism.

### Common Mistakes
- Overlooking the underlying Spleen Qi Deficiency and focusing solely on resolving the Phlegm-Fluids.
- Using overly drying herbs in patients with underlying Yin deficiency.
- Ignoring the patient's overall constitution and tailoring the treatment accordingly.

### Treatment Modifications
- **If the patient presents with significant edema:** Add herbs that strongly promote urination, such as Ze Xie (Alisma).
- **If the patient presents with cold limbs:** Increase the dosage of warming herbs, such as Gui Zhi (Cinnamomi Ramulus).

### Success Indicators
- Reduction in the amount of watery sputum.
- Improvement in dizziness and nausea.
- Increased energy levels.


## ✅ Pattern Comparison Table

| Feature | Phlegm-Fluids | Phlegm-Damp | Phlegm-Heat |
|---|---|---|---|
| Sputum | Watery, thin, copious | Thick, sticky, profuse | Yellow, thick, difficult to expectorate |
| Tongue | Pale, swollen, white greasy coat | Swollen, white greasy coat | Red, yellow greasy coat |
| Pulse | Slippery, weak | Slippery | Slippery, rapid |
| Key Symptoms | Dizziness, rattling in throat | Heaviness, fatigue | Fever, thirst, irritability |
| Etiology | Spleen/Kidney Qi Deficiency | Spleen Qi Deficiency, dietary factors | Heat, exterior invasion |


## 📚 References & Resources

- Maciocia, Giovanni. *The Foundations of Chinese Medicine*. 3rd ed. Churchill Livingstone, 2015.
- Bensky, Dan, et al. *Chinese Herbal Medicine: Materia Medica*. 3rd ed. Eastland Press, 2004.
- Deadman, Peter, et al. *A Manual of Acupuncture*. 2nd ed. Journal of Chinese Medicine Publications, 2001.
