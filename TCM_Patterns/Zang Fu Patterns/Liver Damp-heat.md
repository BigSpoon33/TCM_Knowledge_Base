---
id: pattern-20251115-liver-damp-heat
name: Liver Damp-heat
type: pattern
aliases:
- LV Damp-Heat (肝膽濕熱)
tags:
- TCM
- Pattern
category:
- Zang Fu
- Six Evils
- Eight Principles
- Qi Blood
- Six Stages
- Four Levels
- San Jiao
- Channel
- Five Elements
related:
- Liver Fire Blazing
- Spleen Qi Deficiency
- Gallbladder Damp-Heat
symptoms: []
patterns: []
western_conditions:
- [[Hepatitis]]
- [[Cholecystitis]]
- [[Pelvic Inflammatory Disease (PID)]]
- [[Orchitis]]
- [[Prostatitis]]
- [[Biliary Colic]]
formulas:
- [[Long Dan Xie Gan Tang]]
- [[Yin Chen Hao Tang]]
- [[Ba Zheng San]]
herbs:
- [[Long Dan Cao]]
- [[Huang Qin]]
- [[Zhi Zi]]
- [[Ze Xie]]
- [[Che Qian Zi]]
- [[Mu Tong]]
- [[Dang Gui]]
- [[Sheng Di Huang]]
- [[Chai Hu]]
- [[Yin Chen Hao]]
- [[Da Huang]]
- [[Hua Shi]]
- [[Bian Xu]]
- [[Qu Mai]]
- [[Shan Zhi Zi]]
- [[Gan Cao]]
points:
- [[LV 14]]
- [[GB 34]]
- [[UB 18]]
- [[RN 12]]
- [[SP 9]]
- [[SP 6]]
- [[LI 11]]
- [[LV 2]]
- [[GB 24]]
- [[SP 8]]
nutrition: []
tests:
- Liver function tests
- Urinalysis
- Stool culture
created: 2024-01-01
updated: 2024-01-01

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
- Bitter taste in mouth
- Yellowish discoloration (jaundice) of skin and sclera
- Dark yellow urine
- Hypochondriac pain or distention
- Irritability

### Complete Symptom Picture

**Chief Symptoms:**
- Bitter taste in the mouth, especially in the morning
- Jaundice, with yellowing of the skin and sclera
- Dark yellow urine, often concentrated
- Hypochondriac pain or distention, often worse with pressure
- Irritability, easily angered or frustrated

**Accompanying Symptoms:**
- Nausea or poor appetite
- Headache, often described as throbbing or distending
- Red eyes, possibly with itching or burning
- Thirst without a strong desire to drink
- Vaginal discharge (yellow and possibly foul-smelling) in women
- Scrotal dampness and itching in men
- Constipation or diarrhea, possibly with sticky stools

**Tongue:** `= this.pattern_data.tongue`

**Pulse:** `= this.pattern_data.pulse`


## 🔄 Differential Diagnosis

### Similar Patterns

| Feature | This Pattern | Similar Pattern 1 | Similar Pattern 2 |
|---------|--------------|-------------------|-------------------|
| Chief symptom | Bitter taste, jaundice, dark urine | Red eyes, headache, constipation | Fatigue, loose stools, abdominal distention |
| Tongue | Red, thick yellow greasy coat | Red, dry yellow coat | Pale, swollen, white coat |
| Pulse | Wiry, rapid, slippery | Wiry, rapid | Weak, soggy |
| Key distinction | Damp-Heat signs, esp. jaundice | Absence of Dampness, more heat-related | Absence of Heat, more deficiency-related |

**vs. [[Liver Fire Blazing]]:**
- Key difference: Liver Fire Blazing focuses more on intense heat signs such as severe headache, red face, and constipation, whereas Liver Damp-Heat presents with jaundice, greasy tongue coat, and dampness-related symptoms.

**vs. [[Spleen Qi Deficiency]]:**
- Key difference: Spleen Qi Deficiency is characterized by fatigue, loose stools, and abdominal distention, without the heat signs or jaundice seen in Liver Damp-Heat. The tongue is usually pale and swollen.


### Key Herbs

**Essential Herbs for This Pattern:**
- [[Long Dan Cao]] – Drains Liver Fire and clears Damp-Heat from the Liver and Gallbladder channels. Dosage: 3-9g
- [[Huang Qin]] – Clears heat, dries dampness, and detoxifies. Effective for addressing heat in the upper jiao and resolving damp-heat in the lower jiao. Dosage: 6-12g
- [[Zhi Zi]] – Clears heat, drains dampness, and resolves irritability. Especially effective for clearing heat from the Liver and Gallbladder. Dosage: 6-12g

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
- Pregnancy (use caution with strong draining herbs)
- Severe Deficiency syndromes
- Prolonged use in patients with weak Spleen Qi
- Patients on immunosuppressants (due to potential interactions with herbs)

**Cautions:**
- Avoid overly aggressive draining methods that could damage Zheng Qi.
- Monitor the patient's energy levels and digestive function throughout treatment.

**When to Avoid:**
- Avoid strong draining herbs if the patient is weak or elderly.


## 🏷️ Western Medical Correlates

**Common Western Diagnoses:**
- Hepatitis
- Cholecystitis
- Pelvic Inflammatory Disease (PID)
- Orchitis
- Prostatitis
- Biliary Colic

**Biomedical Understanding:**
Liver Damp-Heat shares similarities with inflammatory conditions of the liver, gallbladder, and urinary system. These conditions often involve infections or imbalances that lead to inflammation and dysfunction.

**Integration Notes:**
TCM pattern diagnosis helps to differentiate the underlying causes and individualize treatment. While Western medicine may focus on treating the infection or inflammation, TCM addresses the root imbalances that contribute to the development of the condition.


## ✅ Clinical Pearls & Experience

### Clinical Tips
- Pay close attention to the tongue coating to assess the degree of Dampness.
- Inquire about dietary habits and emotional stressors.
- Use pulse diagnosis to confirm the pattern and evaluate the patient's overall condition.

### Common Mistakes
- Overlooking the importance of dietary and lifestyle modifications.
- Using overly aggressive draining methods that could damage Zheng Qi.

### Treatment Modifications
- **If Spleen Qi Deficiency is present:** Add herbs that tonify Spleen Qi, such as [[Ren Shen]] and [[Bai Zhu]].
- **If Liver Qi Stagnation is prominent:** Add herbs that soothe Liver Qi, such as [[Chai Hu]] and [[Xiang Fu]].

### Success Indicators
- Reduction in jaundice.
- Improvement in the color of urine.
- Relief of hypochondriac pain.
- Decreased irritability.
- Cleared tongue coating


## ✅ Pattern Comparison Table

| Feature | Liver Damp-Heat | Liver Fire Blazing | Damp-Heat in the Lower Jiao |
|-------------------|-------------------------------------------------------|-----------------------------------------------------|---------------------------------------------------|
| Primary Location | Liver and Gallbladder | Liver Channel | Lower Jiao (Bladder, Intestines) |
| Key Symptoms | Jaundice, bitter taste, dark urine, hypochondriac pain | Red face, headache, irritability, constipation | Frequent, urgent urination, burning sensation |
| Tongue | Red, thick yellow greasy coat | Red, dry yellow coat | Red, yellow greasy coat, especially at the root |
| Pulse | Wiry, rapid, slippery | Wiry, rapid, forceful | Slippery, rapid |
| Treatment | Clear Heat, resolve Dampness, soothe Liver Qi | Clear Liver Fire, subdue Liver Yang | Clear Damp-Heat, promote urination |
| Representative Formula | [[Long Dan Xie Gan Tang]] | [[Xie Qing Wan]] | [[Ba Zheng San]] |


## 📚 References & Resources

- Maciocia, G. (2015). *The Foundations of Chinese Medicine: A Comprehensive Text*. Churchill Livingstone.
- Bensky, D., Gamble, A., & Kaptchuk, T. J. (1993). *Chinese Herbal Medicine: Materia Medica*. Eastland Press.
- Deadman, P., Al-Khafaji, M., & Baker, K. (2007). *A Manual of Acupuncture*. Journal of Chinese Medicine Publications.
