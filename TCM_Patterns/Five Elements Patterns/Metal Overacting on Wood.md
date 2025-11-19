---
id: pattern-20251115-metal-overacting-on-wood
name: Metal Overacting on Wood
type: pattern
aliases: []
tags:
- TCM
- Pattern
- Five Elements
category:
- Five Elements
- Zang Fu
- Eight Principles
- Qi Blood
- Six Stages
- Four Levels
- San Jiao
- Channel
related:
- Liver Qi Stagnation
- Lung Qi Deficiency
- Spleen Qi Deficiency
symptoms: []
patterns: []
western_conditions:
- [[Irritable Bowel Syndrome (IBS)]]
- [[Anxiety]]
- [[Depression]]
- [[Chronic Fatigue Syndrome]]
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
- Tiredness
- Irritability
- Feeling of distension
- White facial complexion
- Hypochondriac pain
- Tight chest
- Sighing
- Poor appetite

### Complete Symptom Picture

**Chief Symptoms:**
- Fatigue, especially in the mornings
- Irritability and frustration, often easily angered
- Distension in the chest and abdomen
- Pale or white facial complexion

**Accompanying Symptoms:**
- Hypochondriac pain or discomfort
- Frequent sighing
- Poor appetite and/or indigestion
- Possible loose stools
- Headaches (especially temporal)
- Premenstrual tension (in women)

**Tongue:** `= this.pattern_data.tongue`

**Pulse:** `= this.pattern_data.pulse`


## 🔄 Differential Diagnosis

### Similar Patterns

| Feature | This Pattern | Similar Pattern 1 | Similar Pattern 2 |
|---------|--------------|-------------------|-------------------|
| Chief symptom | Fatigue & Irritability | Primarily Irritability | Primarily Fatigue |
| Tongue | Pale, thin coating | Red, yellow coating | Pale, swollen |
| Pulse | Wiry, weak | Wiry, rapid | Weak, soggy |
| Key distinction | Lung Qi deficiency + Liver Stagnation | Liver Qi Stagnation alone | Spleen Qi Deficiency alone |

**vs. [[Liver Qi Stagnation]]:**
- Key difference: Presence of Lung Qi deficiency symptoms (fatigue, pale face) in Metal Overacting on Wood. Liver Qi Stagnation is more focused on emotional and digestive symptoms, without significant fatigue.

**vs. [[Spleen Qi Deficiency]]:**
- Key difference: Irritability and hypochondriac pain point to Liver involvement, not solely Spleen deficiency. Spleen Qi Deficiency presents primarily with digestive symptoms and fatigue.


### Key Herbs

**Essential Herbs for This Pattern:**
- [[Huang Qi (Astragalus)]]  Tonifies Lung and Spleen Qi, strengthens Wei Qi. Dosage: 9-30g
- [[Chai Hu (Bupleurum)]] 疏肝解郁,升阳举陷 – Spreads Liver Qi, raises the Yang. Dosage: 3-12g
- [[Dang Gui (Angelica sinensis)]]  Nourishes Blood, especially Liver Blood, and regulates menstruation. Dosage: 6-15g

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
`= join(this.pattern_data.contraindications, "\n- ")`

**Cautions:**
- Avoid strong purgative herbs that could further weaken Spleen Qi.
- Be cautious with strongly descending herbs if there is significant Spleen Qi sinking.

**When to Avoid:**
- Avoid using warming or drying herbs if the patient has Lung Yin deficiency.


## 🏷️ Western Medical Correlates

**Common Western Diagnoses:**
`= join(this.western_conditions, "\n- ")`

**Biomedical Understanding:**
Irritable Bowel Syndrome is often linked to stress and anxiety, which can influence the autonomic nervous system and affect digestive function. Chronic Fatigue Syndrome is characterized by persistent fatigue that is not relieved by rest and may be associated with immune dysfunction.

**Integration Notes:**
TCM pattern diagnosis can help refine the understanding of these conditions by identifying the underlying imbalances in Qi, Blood, and the Five Elements. This allows for a more individualized treatment approach that addresses the root cause of the symptoms.


## ✅ Clinical Pearls & Experience

### Clinical Tips
- Always consider the patient's emotional state when diagnosing this pattern.
- Palpate the abdomen for signs of Liver Qi stagnation (tenderness in the hypochondriac region).
- Assess Lung function by observing breathing patterns and asking about respiratory symptoms.

### Common Mistakes
- Focusing solely on the Liver Qi stagnation without addressing the underlying Lung Qi deficiency.
- Using overly aggressive Liver-soothing herbs that could further weaken Spleen Qi.

### Treatment Modifications
- **If Lung Yin Deficiency is present:** Add herbs like Mai Men Dong (Ophiopogonis Radix) to nourish Lung Yin.
- **If Dampness is present:** Add herbs like Cang Zhu (Atractylodis Rhizoma) to dry Dampness.

### Success Indicators
- Improved energy levels and reduced fatigue.
- Decreased irritability and improved mood.
- Improved digestion and appetite.


## ✅ Pattern Comparison Table

| Feature | Metal Overacting on Wood | Liver Qi Stagnation | Lung Qi Deficiency | Spleen Qi Deficiency |
|---|---|---|---|---|
| **Primary Imbalance** | Lung Qi Deficient + Liver Qi Stagnant | Liver Qi Stagnant | Lung Qi Deficient | Spleen Qi Deficient |
| **Key Symptoms** | Fatigue, Irritability, Hypochondriac Pain | Irritability, Chest Distension, Sighing | Fatigue, Shortness of Breath, Weak Voice | Fatigue, Poor Appetite, Loose Stools |
| **Tongue** | Pale, Possibly Tense | Normal or Slightly Red | Pale | Pale, Swollen |
| **Pulse** | Wiry, Weak | Wiry | Weak | Weak, Soggy |


## 📚 References & Resources

- Deadman, Peter, Al-Khafaji, Mazin, & Baker, Kevin. A Manual of Acupuncture. Journal of Chinese Medicine Publications, 2007.
- Maciocia, Giovanni. The Foundations of Chinese Medicine: A Comprehensive Text for Acupuncturists and Herbalists. 3rd ed., Elsevier Churchill Livingstone, 2015.
- Dharmananda, Subhuti. Acupuncture Points: Names, Functions, and Combinations. Institute for Traditional Medicine, 2002.
