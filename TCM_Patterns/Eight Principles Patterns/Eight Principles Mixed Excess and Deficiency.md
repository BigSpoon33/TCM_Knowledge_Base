---
id: pattern-20251115-eight-principles-mixed-excess-and-deficiency
name: Eight Principles Mixed Excess and Deficiency
type: pattern
aliases: []
tags:
- TCM
- Pattern
- Eight Principles
category:
- Eight Principles
- Zang Fu
- Qi Blood
- Six Stages
- Four Levels
- San Jiao
- Channel
- Five Elements
related: []
symptoms: []
patterns: []
western_conditions: []
formulas: []
herbs: []
points: []
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
- Signs of Deficiency (e.g., fatigue, weakness, dizziness)
- Signs of Excess (e.g., pain, distention, inflammation)
- Combination of deficiency and excess symptoms affecting the same or different areas of the body

### Complete Symptom Picture

**Chief Symptoms:**
- Fatigue
- Pain (localized or generalized)
- Dizziness or lightheadedness

**Accompanying Symptoms:**
- Weakness
- Distention or bloating
- Irritability
- Sleep disturbances
- Digestive issues
- Sweating (night sweats or spontaneous sweating)

**Tongue:** `= this.pattern_data.tongue`

**Pulse:** `= this.pattern_data.pulse`


## 🔄 Differential Diagnosis

### Similar Patterns

| Feature | This Pattern | Similar Pattern 1 | Similar Pattern 2 |
|---------|--------------|-------------------|-------------------|
| Chief symptom | Combination of Deficiency and Excess | Primarily Deficiency | Primarily Excess |
| Tongue | Mixed: normal/pale body with areas of red, purple, or thick coat | Pale, swollen, thin coat | Red, swollen, thick coat |
| Pulse | Wiry and thin, or weak and forceful | Weak, thready | Forceful, wiry, slippery |
| Key distinction | Coexistence of Deficiency and Excess | Predominance of Deficiency | Predominance of Excess |

**vs. [[Qi Deficiency]]:**
- Key difference: Qi Deficiency lacks the Excess component, such as pain or stagnation

**vs. [[Liver Qi Stagnation]]:**
- Key difference: Liver Qi Stagnation typically presents without significant underlying Deficiency.


### Key Herbs

**Essential Herbs for This Pattern:**
- [[Ren Shen]]  Tonifies Qi and strengthens the Spleen, but can be contraindicated if the excess is severe. Dosage considerations depend on the severity of deficiency.
- [[Dang Gui]]  Nourishes Blood and moves Blood, addressing both deficiency and stasis. Dosage should be carefully monitored to avoid aggravating stagnation.
- [[Fu Ling]]  Drains Dampness and strengthens the Spleen. Careful when there is a lot of yin defeciency.

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
- Aggressive purging or tonification without addressing the other aspect of the pattern
- Treating only the symptoms without addressing the root cause
- Using strong, drying herbs in cases of Yin deficiency

**Cautions:**
- Monitor the patient's response to treatment closely, adjusting the formula and acupuncture points as needed.
- Avoid over-tonifying or over-draining, which can exacerbate the imbalance.

**When to Avoid:**
- Avoid using strongly warming herbs in cases of Yin deficiency with Empty Heat.


## 🏷️ Western Medical Correlates

**Common Western Diagnoses:**
- Chronic Fatigue Syndrome
- Fibromyalgia
- Irritable Bowel Syndrome (IBS)
- Hypertension
- Menopause

**Biomedical Understanding:**
From a biomedical perspective, conditions like Chronic Fatigue Syndrome and Fibromyalgia often involve a combination of factors, including immune dysfunction, hormonal imbalances, and neurological abnormalities. IBS involves gut motility and sensitivity issues. Hypertension may be linked to kidney or cardiovascular issues. Menopause represents hormonal decline.

**Integration Notes:**
TCM pattern diagnosis can provide a more nuanced understanding of these conditions, identifying the specific imbalances that are contributing to the patient's symptoms. This allows for a more individualized treatment approach, addressing both the underlying causes and the presenting symptoms. For example, in a patient with Fibromyalgia, TCM may identify a combination of Liver Qi stagnation, Blood stasis, and Spleen Qi deficiency, leading to a treatment plan that addresses all three aspects.


## ✅ Clinical Pearls & Experience

### Clinical Tips
- Start with a gentle approach, gradually increasing the intensity of treatment as the patient's condition improves.
- Prioritize addressing the dominant aspect of the pattern, but always keep the other aspect in mind.
- Educate the patient about lifestyle modifications that can support their treatment, such as diet, exercise, and stress management.

### Common Mistakes
- Focusing solely on the excess symptoms without addressing the underlying deficiency.
- Using overly strong tonifying herbs in cases of Yin deficiency with Empty Heat.

### Treatment Modifications
- **If the patient is weak and frail:** Use a gentler approach, focusing on tonifying the deficiency first.
- **If the patient is experiencing severe pain:** Use acupuncture points and herbs that can quickly relieve pain.

### Success Indicators
- Reduction in both deficiency and excess symptoms
- Improved energy levels
- Improved sleep quality


## ✅ Pattern Comparison Table

| Feature | Mixed Excess and Deficiency | Qi Deficiency | Liver Qi Stagnation |
|---------|-----------------------------|-----------------|---------------------|
| Chief Symptoms | Fatigue, Pain, Dizziness | Fatigue, Weakness | Irritability, Distention |
| Tongue | Mixed: Normal/Pale with Red/Purple | Pale, Swollen | Normal/Red |
| Pulse | Wiry/Thin or Weak/Forceful | Weak, Thready | Wiry |
| Treatment | Tonify Deficiency, Reduce Excess | Tonify Qi | Move Qi |


## 📚 References & Resources

- Maciocia, Giovanni. *The Foundations of Chinese Medicine: A Comprehensive Text.* 3rd ed. Churchill Livingstone, 2015.
- Deadman, Peter, and Mazin Al-Khafaji. *A Manual of Acupuncture.* Journal of Chinese Medicine Publications, 2007.
