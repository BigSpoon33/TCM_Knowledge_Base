---
id: pattern-20251115-eight-principles-excess-cold-full-cold
name: Eight Principles Excess-Cold (Full-Cold)
type: pattern
aliases:
- Full-Cold
- Excess Cold
- Interior Full Cold
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
related:
- Spleen Yang Deficiency
- Liver Qi Stagnation
- Stomach Cold
- Intestinal Cold
symptoms: []
patterns: []
western_conditions:
- [[Constipation]]
- [[Intestinal obstruction]]
- [[IBS (Irritable Bowel Syndrome)]]
- [[Dysmenorrhea]]
formulas:
- [[Da Cheng Qi Tang (Major Order the Qi Decoction)]]
- [[Li Zhong Wan (Regulate the Middle Pill)]]
herbs:
- [[Fu Zi (Radix Aconiti Lateralis Preparata)]]
- [[Gan Jiang (Rhizoma Zingiberis)]]
- [[Rou Gui (Cortex Cinnamomi)]]
- [[Da Huang (Radix et Rhizoma Rhei)]]
points:
- [[ST-25 (Tianshu)]]
- [[CV-12 (Zhongwan)]]
- [[CV-6 (Qihai)]]
- [[SP-9 (Yinlingquan)]]
- [[ST-36 (Zusanli)]]
nutrition: []
tests: []
created: 2024-01-22
updated: 2024-01-22

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
- Sharp abdominal pain aggravated by pressure
- Aversion to cold
- Thick-white tongue coating
- Excess-tight-deep pulse

### Complete Symptom Picture

**Chief Symptoms:**
- Sharp, localized pain, often in the abdomen
- Aversion to cold, seeking warmth
- Absence of thirst or preference for warm drinks

**Accompanying Symptoms:**
- Cold limbs, especially hands and feet
- Abdominal distension and fullness
- Constipation, or diarrhea with undigested food
- Bright-white complexion

**Tongue:** `= this.pattern_data.tongue`

**Pulse:** `= this.pattern_data.pulse`


## 🔄 Differential Diagnosis

### Similar Patterns

| Feature | This Pattern | Similar Pattern 1 | Similar Pattern 2 |
|---------|--------------|-------------------|-------------------|
| Chief symptom | Sharp, fixed pain | Dull, aching pain | Intermittent, distending pain |
| Tongue | Thick-white coating | Pale, swollen tongue | Thin-white coating |
| Pulse | Excess-tight-deep | Weak, slow | Wiry |
| Key distinction | Excess nature, pain worse with pressure | Deficiency of Yang Qi | Qi stagnation as primary issue |

**vs. [[Spleen Yang Deficiency]]:**
- Key difference: Spleen Yang Deficiency presents with chronic, dull pain, fatigue, and loose stools due to impaired Spleen function, whereas Excess-Cold features acute, sharp pain and an aversion to cold.

**vs. [[Liver Qi Stagnation]]:**
- Key difference: Liver Qi Stagnation manifests with fluctuating, distending pain that is often related to emotional stress, while Excess-Cold has a more consistent, sharp pain pattern aggravated by pressure and cold exposure.


### Key Herbs

**Essential Herbs for This Pattern:**
- [[Fu Zi (Radix Aconiti Lateralis Preparata)]] – This herb strongly warms the Kidneys and fortifies Yang, expelling deep Cold and alleviating pain. Dosage considerations include careful preparation to reduce toxicity and monitoring for adverse reactions.
- [[Gan Jiang (Rhizoma Zingiberis)]] – Warms the middle Jiao, strengthens the Spleen, and expels Cold. It's milder than Fu Zi and can be used for milder cases or in combination with stronger herbs.
- [[Rou Gui (Cortex Cinnamomi)]] - Enters the Kidney channel to strongly warm and tonify Kidney Yang, while also guiding fire downwards. This helps to dispel Cold and alleviate pain, particularly in the lower abdomen.
- [[Da Huang (Radix et Rhizoma Rhei)]] - While seemingly contradictory, Da Huang is used in Da Cheng Qi Tang to strongly purge stagnant Heat and fluids that have accumulated from the stagnation of Cold, particularly in cases of severe constipation.

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
- Use caution in patients with underlying Yin Deficiency.
- Avoid strong warming herbs in patients with signs of Heat.
- Contraindicated in patients with true Heat patterns.

**Cautions:**
- Avoid using strong warming herbs for extended periods, as this can deplete Yin.
- Closely monitor patients for signs of adverse reactions to warming herbs, such as dryness or irritability.

**When to Avoid:**
- Avoid strongly warming treatments during febrile illnesses or when signs of Heat are present.


## 🏷️ Western Medical Correlates

**Common Western Diagnoses:**
- Constipation
- Intestinal obstruction
- IBS (Irritable Bowel Syndrome)
- Dysmenorrhea

**Biomedical Understanding:**
From a biomedical perspective, conditions such as constipation, intestinal obstruction, and IBS can involve impaired bowel motility, inflammation, or structural abnormalities. Dysmenorrhea may involve hormonal imbalances, uterine contractions, or inflammation.

**Integration Notes:**
TCM pattern diagnosis adds to Western diagnosis by identifying the underlying imbalance of Qi, Blood, and Yin/Yang, allowing for a more holistic and individualized treatment approach. For example, TCM can differentiate between different types of constipation based on the underlying pattern, guiding the selection of appropriate herbs and acupuncture points.


## ✅ Clinical Pearls & Experience

### Clinical Tips
- Always palpate the abdomen to assess the location and severity of the pain.
- Check for aversion to cold and preference for warm drinks to confirm the diagnosis.
- Consider underlying Yang Deficiency, especially in chronic cases.

### Common Mistakes
- Over-treating with warming herbs without addressing underlying Yin Deficiency.
- Misdiagnosing Excess-Cold as Heat, leading to inappropriate treatment.

### Treatment Modifications
- **If the patient has significant Qi Stagnation:** Add herbs that move Qi, such as Chen Pi (Citri Reticulatae Pericarpium) and Xiang Fu (Cyperi Rhizoma).
- **If the patient has significant Phlegm:** Add herbs that resolve Phlegm, such as Ban Xia (Pinelliae Rhizoma) and Chen Pi (Citri Reticulatae Pericarpium).

### Success Indicators
- Relief of pain and abdominal distension.
- Improvement in tongue coating and pulse quality.


## ✅ Pattern Comparison Table

[Optional: Include a table comparing this pattern with related patterns]


## 📚 References & Resources

- *Shanghan Lun (Treatise on Cold Damage)*
- *Practical Diagnosis in Traditional Chinese Medicine* by Giovanni Maciocia
- *Chinese Herbal Medicine: Formulas & Strategies* by Bensky, Clavey, & Stöger
