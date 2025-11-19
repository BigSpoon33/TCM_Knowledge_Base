---
id: pattern-20251115-stomach-damp-heat
name: Stomach Damp-heat
type: pattern
aliases:
- ST Damp-Heat
- Stomach Phlegm-Heat
- Damp Heat in the Stomach
tags:
- TCM
- Pattern
category:
- Zang Fu Treatment Pattern
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
- Food Stagnation
- Liver Overacting on the Stomach
- Phlegm-Heat in the Lungs
symptoms: []
patterns: []
western_conditions:
- [[Gastritis]]
- [[Peptic ulcer disease]]
- [[GERD (Gastroesophageal Reflux Disease)]]
- [[H. pylori infection]]
- [[Dyspepsia]]
- [[Functional dyspepsia]]
formulas:
- [[Lian Po Yin]]
- [[Qing Wei San]]
- [[Ban Xia Xie Xin Tang]]
herbs:
- [[Huang Lian]]
- [[Ban Xia]]
- [[Zhu Ru]]
- [[Fu Ling]]
- [[Chen Pi]]
- [[Hou Po]]
points:
- [[ST44]]
- [[ST34]]
- [[ST21]]
- [[RN12]]
- [[RN13]]
- [[LI11]]
- [[LI4]]
- [[RN11]]
- [[ST25]]
- [[ST40]]
- [[SP9]]
- [[RN9]]
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
- Epigastric fullness and distention
- Nausea and vomiting
- Thick, greasy yellow tongue coating
- Rapid, slippery pulse
- Loss of appetite or desire to eat only small amounts

### Complete Symptom Picture

**Chief Symptoms:**
- Epigastric fullness and distention, often worse after eating
- Nausea and vomiting, possibly with sour or bitter taste
- Loss of appetite or early satiety

**Accompanying Symptoms:**
- Burning sensation in the epigastrium
- Acid reflux or regurgitation
- Bitter taste in the mouth
- Thirst, but no desire to drink large amounts
- Feeling of heaviness in the body
- Fatigue or lethargy
- Irritability or restlessness
- Sticky or loose stools

**Tongue:** `= this.pattern_data.tongue`

**Pulse:** `= this.pattern_data.pulse`


## 🔄 Differential Diagnosis

### Similar Patterns

| Feature | This Pattern | Similar Pattern 1 | Similar Pattern 2 |
|---------|--------------|-------------------|-------------------|
| Chief symptom | Epigastric fullness, nausea, thick yellow tongue coat | Epigastric pain, sour regurgitation, belching | Epigastric pain, distention, reduced appetite, diarrhea |
| Tongue | Red, thick, greasy yellow coat | Normal or red, thin, white or yellow coat | Pale, swollen, tooth-marked, white coat |
| Pulse | Rapid, slippery | Wiry | Weak, thin |
| Key distinction | Damp-Heat signs | Liver Qi Stagnation signs | Spleen Qi Deficiency signs |

**vs. [[Liver Overacting on the Stomach]]:**
- Key difference: Liver Overacting on the Stomach presents primarily with epigastric pain and distention that is related to emotional stress, while Stomach Damp-Heat has more pronounced Damp-Heat signs like a thick, greasy tongue coat and nausea.

**vs. [[Spleen Qi Deficiency]]:**
- Key difference: Spleen Qi Deficiency presents with fatigue, poor appetite, and loose stools, while Stomach Damp-Heat shows more pronounced Heat signs like a burning sensation and a thick, yellow tongue coat.


### Key Herbs

**Essential Herbs for This Pattern:**
- [[Huang Lian]]  Bitter and cold, clears Heat, dries Dampness, and drains Fire. Dosage considerations: use with caution in patients with Spleen Qi Deficiency.
- [[Ban Xia]]  Dries Dampness, transforms Phlegm, and regulates Qi in the Stomach. Dosage considerations: processed Ban Xia is preferred to reduce toxicity.
- [[Zhu Ru]]  Clears Heat, transforms Phlegm, and stops vomiting. Dosage considerations: often used in combination with Ban Xia to enhance its effect.

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
- Avoid greasy, spicy, and sweet foods during treatment.
- Use caution in patients with Spleen Qi Deficiency, as strong draining methods may further weaken the Spleen.
- Monitor for any signs of Stomach Qi Deficiency during treatment.
- Avoid overuse of cold and bitter herbs, as they may damage the Stomach Qi.
- Pregnancy (certain herbs are contraindicated).

**Cautions:**
- Modify treatment according to the patient's overall condition and constitution.
- Educate the patient about dietary modifications and lifestyle changes to prevent recurrence.

**When to Avoid:**
- Avoid strong purgatives if there is underlying Spleen Qi Deficiency.


## 🏷️ Western Medical Correlates

**Common Western Diagnoses:**
- Gastritis
- Peptic ulcer disease
- GERD (Gastroesophageal Reflux Disease)
- H. pylori infection
- Dyspepsia
- Functional dyspepsia

**Biomedical Understanding:**
Western medicine attributes these conditions to factors such as bacterial infections (H. pylori), excessive stomach acid production, and inflammation of the gastric lining. Medications like proton pump inhibitors and antibiotics are commonly used.

**Integration Notes:**
TCM pattern diagnosis provides a more nuanced understanding of the underlying imbalances contributing to these conditions. TCM treatment can address the root cause of the problem by clearing Heat, drying Dampness, and strengthening the digestive system, potentially reducing reliance on long-term medication.


## ✅ Clinical Pearls & Experience

### Clinical Tips
- Always assess the patient's overall constitution and address any underlying deficiencies, such as Spleen Qi Deficiency.
- Dietary advice is crucial for managing Stomach Damp-Heat. Advise patients to avoid greasy, spicy, and sweet foods.
- Consider the emotional component of the pattern, especially if the patient experiences chronic stress or anxiety.

### Common Mistakes
- Focusing solely on clearing Heat without addressing the underlying Dampness.
- Using overly harsh draining methods that damage the Stomach Qi.

### Treatment Modifications
- **If Spleen Qi Deficiency is present:** Add herbs that tonify the Spleen, such as [[Bai Zhu]] and [[Fu Ling]].
- **If Liver Qi Stagnation is present:** Add herbs that soothe the Liver and regulate Qi, such as [[Chai Hu]] and [[Xiang Fu]].

### Success Indicators
- Reduction in epigastric fullness and distention.
- Improvement in appetite.
- Clearing of the tongue coating.


## ✅ Pattern Comparison Table

| Feature | Stomach Damp-Heat | Liver Overacting on the Stomach | Spleen Qi Deficiency | Food Stagnation |
|--------------------------|---------------------------|------------------------------------|--------------------------|--------------------|
| **Chief Complaint** | Epigastric Fullness, Nausea | Epigastric Pain (stress related) | Fatigue, Poor Appetite | Epigastric Distention |
| **Tongue**  | Red, Thick, Greasy Yellow Coat | Normal or Red, Thin White/Yellow Coat | Pale, Swollen, Tooth-Marked, White Coat | Thick, Greasy Coat  |
| **Pulse**   | Rapid, Slippery   | Wiry      | Weak, Thin    | Slippery   |
| **Key Signs** | Damp-Heat Signs   | Emotional Factors  | Spleen Deficiency Signs   | Undigested Food   |
| **Etiology** | Diet, Weak Spleen Qi | Stress, Emotional Constraint  | Chronic Illness, Overwork  | Overeating |
| **Treatment Focus** | Clear Heat, Dry Damp, Harmonize Stomach | Soothe Liver, Regulate Qi  | Tonify Spleen, Boost Qi  | Promote Digestion, Resolve Stagnation |


## 📚 References & Resources

- Maciocia, Giovanni. *The Foundations of Chinese Medicine: A Comprehensive Text for Acupuncturists and Herbalists.* 3rd ed. Edinburgh: Churchill Livingstone, 2015.
- Bensky, Dan, Steven Clavey, and Erich Stöger. *Chinese Herbal Medicine: Materia Medica.* 3rd ed. Seattle, WA: Eastland Press, 2004.
- Deadman, Peter, Alon Marcus, and Mazin Al-Khafaji. *A Manual of Acupuncture.* 2nd ed. East Sussex, England: Journal of Chinese Medicine Publications, 2000.
