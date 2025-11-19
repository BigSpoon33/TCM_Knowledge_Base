---
id: pattern-20251115-wei-level-summer-heat
name: Wei Level Summer-Heat
type: pattern
aliases:
- Summerheat at the Wei Level
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
- Qi Level Summer-Heat
- Damp-Heat
- Wind-Heat
symptoms: []
patterns: []
western_conditions:
- [[Heatstroke]]
- [[Sunstroke]]
formulas:
- [[Qing Luo Yin]]
herbs:
- [[Jin Yin Hua]]
- [[Lian Qiao]]
- [[Xi Gua Pi]]
- [[Lu Dou Yi]]
- [[He Ye]]
- [[Xiang Ru]]
points:
- [[LI4]]
- [[LI11]]
- [[SJ5]]
- [[DU14]]
- [[DU26]]
- [[UB40]]
- [[PC9]]
nutrition: []
tests: []
created: 2024-01-20
updated: 2024-01-20

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
- Fever, aversion to cold
- No sweating
- Headache
- A feeling of heaviness
- An uncomfortable sensation in the epigastrium
- Irritability
- Thirst

### Complete Symptom Picture

**Chief Symptoms:**
- Fever
- Aversion to Cold
- Headache

**Accompanying Symptoms:**
- No sweating or scanty sweating
- Heaviness of the head and body
- Epigastric fullness or discomfort
- Thirst, but not wanting to drink much
- Irritability and restlessness
- Possible nausea or vomiting

**Tongue:** `= this.pattern_data.tongue`

**Pulse:** `= this.pattern_data.pulse`


## 🔄 Differential Diagnosis

### Similar Patterns

| Feature | This Pattern | Similar Pattern 1 | Similar Pattern 2 |
|---------|--------------|-------------------|-------------------|
| Chief symptom | Fever, aversion to cold, lack of sweat | High fever, profuse sweating | Fever, chills, body aches |
| Tongue | Red front/sides, sticky white coat | Red, yellow coat | Thin white coat |
| Pulse | Soggy, rapid | Rapid, forceful | Floating, tight |
| Key distinction | Lack of sweat, damp symptoms | Profuse sweating, Qi consumption | Wind-Cold invasion |

**vs. [[Qi Level Summer-Heat]]:**
- Key difference: Qi Level Summer-Heat will exhibit higher fever, more pronounced thirst, and a yellow tongue coating, indicating the heat has penetrated deeper. Sweating is also more likely.

**vs. [[Wind-Heat]]:**
- Key difference: Wind-Heat typically presents with a floating pulse, sore throat, and a thin tongue coating, reflecting an exterior invasion of wind. Wei Level Summer-Heat presents with heaviness and digestive symptoms due to the dampness.


### Key Herbs

**Essential Herbs for This Pattern:**
- [[Jin Yin Hua]]  Sweet, cold; clears heat, resolves toxicity, and clears damp-heat from the Wei level. (Dosage: 6-15g)
- [[Lian Qiao]]  Bitter, slightly cold; clears heat, resolves toxicity, disperses wind-heat, and gently releases the exterior. (Dosage: 6-15g)
- [[Xi Gua Pi]]  Sweet, cold; clears summer-heat, generates fluids, and promotes urination to drain dampness. (Dosage: 9-30g)
- [[Lu Dou Yi]]  Sweet, cold; clears heat, resolves toxicity, promotes urination, and alleviates summer-heat. (Dosage: 9-15g)
- [[He Ye]]  Bitter, neutral; clears summer-heat, transforms dampness, and raises the clear Yang of the Spleen. (Dosage: 6-15g)
- [[Xiang Ru]]  Acrid, slightly warm; releases the exterior, transforms dampness, and harmonizes the Stomach. (Dosage: 3-9g, use cautiously as it can be drying)

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
- Strong purgatives
- Excessive sweating with forced methods if body fluids are already depleted
- Strong tonics in the acute stage

**Cautions:**
- Avoid excessive sweating if the patient is already dehydrated.
- Use caution with warm or hot therapies as they may exacerbate the heat.

**When to Avoid:**
- Avoid strongly warming herbs unless there is underlying Cold.


## 🏷️ Western Medical Correlates

**Common Western Diagnoses:**
- Heatstroke
- Sunstroke

**Biomedical Understanding:**
Heatstroke and sunstroke are characterized by the body's inability to regulate its temperature, leading to a rapid rise in body temperature, central nervous system dysfunction, and potentially organ damage. Dehydration and electrolyte imbalances are common complications.

**Integration Notes:**
TCM pattern diagnosis can help differentiate between various presentations of heat-related illnesses. For example, Wei Level Summer-Heat emphasizes the presence of dampness, which can be addressed with specific herbal formulas that target damp-heat. While Western medicine focuses on immediate cooling and hydration, TCM offers a more nuanced approach to restoring balance and promoting long-term recovery.


## ✅ Clinical Pearls & Experience

### Clinical Tips
- Always check the tongue coating carefully to assess the degree of dampness.
- Ask about the patient's environment and activities leading up to the onset of symptoms.
- Consider the patient's constitution when choosing herbal formulas.

### Common Mistakes
- Mistaking this pattern for Wind-Cold due to the aversion to cold.
- Over-treating with cooling herbs and injuring the Spleen Qi.

### Treatment Modifications
- **If Dampness is very pronounced:** Increase the dosage of damp-transforming herbs like [[He Ye]] and [[Xiang Ru]].
- **If Fever is very high:** Add herbs that strongly clear heat, such as [[Shi Gao]] (use with caution).

### Success Indicators
- Reduction in fever and aversion to cold.
- Improvement in tongue coating and pulse.
- Increase in sweating and overall sense of well-being.


## ✅ Pattern Comparison Table

| Feature | Wei Level Summer-Heat | Qi Level Summer-Heat | Damp-Heat | Wind-Heat |
|---|---|---|---|---|
| **Chief Symptom** | Fever, aversion to cold, lack of sweat, heaviness | High fever, thirst, sweating | Fever, heaviness, yellow greasy coating | Fever, aversion to wind, sore throat |
| **Tongue** | Red front/sides, white sticky coat | Red, yellow coat | Red, yellow greasy coat | Red, thin white coat |
| **Pulse** | Soggy, rapid | Rapid, forceful | Soggy, rapid | Floating, rapid |
| **Key Herbs** | [[Jin Yin Hua]], [[Lian Qiao]], [[He Ye]], [[Xiang Ru]] | [[Shi Gao]], [[Zhi Mu]], [[Lu Gen]] | [[Huang Qin]], [[Huang Lian]], [[Yi Yi Ren]] | [[Jin Yin Hua]], [[Lian Qiao]], [[Bo He]] |


## 📚 References & Resources

- *Wen Bing Tiao Bian* (《温病条辨》)
- *Chinese Herbal Medicine: Formulas & Strategies* by Dan Bensky and Steven Clavey
- *A Manual of Acupuncture* by Peter Deadman
