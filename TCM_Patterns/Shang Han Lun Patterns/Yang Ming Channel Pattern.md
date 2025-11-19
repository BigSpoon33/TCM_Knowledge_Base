---
id: pattern-20251115-yang-ming-channel-pattern
name: Yang Ming Channel Pattern
type: pattern
aliases:
- Yangming Channel Stage
tags:
- TCM
- Pattern
category:
- Channel
- Six Stages
- Zang Fu
- Eight Principles
- Qi Blood
- Four Levels
- San Jiao
- Five Elements
related:
- Yang Ming Fu Organ Pattern
- Qi Level Heat
- Stomach Heat
symptoms: []
patterns: []
western_conditions:
- [[Fever]]
- [[Hyperthermia]]
- [[Dehydration]]
- [[Heatstroke]]
- [[Sepsis]]
formulas:
- [[Bai Hu Tang]]
- [[Zhu Ye Shi Gao Tang]]
- [[Tiao Wei Cheng Qi Tang]]
herbs:
- [[Shi Gao]]
- [[Zhi Mu]]
- [[Gan Cao]]
- [[Geng Mi]]
points:
- [[LI11]]
- [[DU14]]
- [[PC3]]
- [[ST44]]
- [[ST43]]
- [[ST25]]
- [[ST36]]
- [[LI4]]
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
`= join(this.pattern_data.cardinal_symptoms, "\n- ")`

### Complete Symptom Picture

**Chief Symptoms:**
- High fever, often spiking and unremitting
- Profuse sweating, especially on the head and face
- Intense thirst with a strong desire for cold drinks

**Accompanying Symptoms:**
- Red face and eyes, indicating heat in the upper body
- Headache, often throbbing due to the rising heat
- Restlessness and irritability, from the heat disturbing the Shen
- Dry mouth and throat, a result of the consumed body fluids
- Fullness in the chest and abdomen, suggesting stagnation
- Constipation, due to the dryness affecting the Large Intestine
- Delirium or confusion in severe cases, when the Shen is severely affected

**Tongue:** `= this.pattern_data.tongue`

**Pulse:** `= this.pattern_data.pulse`


## 🔄 Differential Diagnosis

### Similar Patterns

| Feature | This Pattern | Similar Pattern 1 | Similar Pattern 2 |
|---------|--------------|-------------------|-------------------|
| Chief symptom | High fever, aversion to heat | High fever, but less aversion to heat | Constipation and abdominal distension |
| Tongue | Red with yellow coating | Red with little coating | Dry, cracked with yellow-brown coating |
| Pulse | Surging, rapid | Rapid, but less forceful | Deep, forceful |
| Key distinction | Channel heat, body fluids are still somewhat present | Heat primarily affecting the Qi level | Focus is on dryness and obstruction in the Fu organs |

**vs. [[Qi Level Heat]]:**
- Key difference: Qi Level Heat may have a less pronounced aversion to heat and less profuse sweating. The pulse may also be less forceful. The Yang Ming Channel Pattern has specific channel involvement.

**vs. [[Yang Ming Fu Organ Pattern]]:**
- Key difference: The Yang Ming Fu Organ Pattern is characterized by severe constipation, abdominal distension and pain, and a deep, forceful pulse. The tongue will be very dry. This pattern shows organ level involvement with excess. The Yang Ming Channel Pattern is a step before this occurs.


### Key Herbs

**Essential Herbs for This Pattern:**
- [[Shi Gao]]  Clears heat, drains fire, and generates fluids. Dosage: 15-60g, depending on the severity.
- [[Zhi Mu]]  Clears heat, moistens dryness, and nourishes Yin. Dosage: 9-15g.
- [[Gan Cao]]  Harmonizes the formula, clears heat, and generates fluids. Dosage: 3-6g.
- [[Geng Mi]]  Protects the Stomach Qi and supports the generation of fluids. Dosage: 15-30g.

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
- Avoid prolonged use of strong cooling herbs in patients with underlying Spleen Qi deficiency, as this can further weaken the digestive system.
- Monitor patients closely for signs of Yin deficiency, such as night sweats or dry mouth, and adjust the treatment accordingly.

**When to Avoid:**
- Avoid strong purgative formulas in pregnant women without careful consideration.


## 🏷️ Western Medical Correlates

**Common Western Diagnoses:**
`= join(this.western_conditions, "\n- ")`

**Biomedical Understanding:**
From a biomedical perspective, this pattern often correlates with conditions involving significant inflammation and hyperthermia, such as infections (sepsis), heatstroke, or severe dehydration. These conditions involve an imbalance in the body's temperature regulation mechanisms and can lead to cellular damage and organ dysfunction.

**Integration Notes:**
TCM pattern diagnosis adds to Western diagnosis by providing a framework for understanding the underlying imbalances contributing to the symptoms. While Western medicine focuses on identifying and treating the specific cause of the inflammation or fever, TCM addresses the broader energetic disharmony within the body, aiming to restore balance and promote overall healing. TCM recognizes the functional aspects and responses of the body, and how it attempts to return to homeostasis.


## ✅ Clinical Pearls & Experience

### Clinical Tips
- Palpate the abdomen to assess for fullness or distension, which can indicate stagnation and the need for herbs that move Qi.
- Check the color and consistency of the urine, as this can provide valuable information about the degree of dehydration.
- Consider the patient's overall constitution when selecting herbs and acupuncture points, as a weaker constitution may require a more gentle approach.

### Common Mistakes
- Overcooling the body too quickly, which can lead to Spleen Qi deficiency and other complications.
- Neglecting to address the underlying cause of the heat, such as dietary excesses or emotional imbalances.
- Focusing solely on clearing heat without also protecting the Yin, which can further deplete the body's resources.

### Treatment Modifications
- **If the patient is elderly or debilitated:** Use lower dosages of cooling herbs and focus on nourishing Yin and Spleen Qi.
- **If the patient is pregnant:** Avoid strong purgative herbs and use acupuncture points with caution.

### Success Indicators
- Reduction in fever and sweating.
- Improvement in thirst and mental clarity.
- Softening of stools and restoration of normal bowel movements.


## ✅ Pattern Comparison Table

| Feature | Yang Ming Channel Pattern | Qi Level Heat | Yang Ming Fu Organ Pattern |
|---|---|---|---|
| **Fever** | High, Aversion to heat | High, Less Aversion to Heat | Very High, No Aversion to Heat |
| **Sweating** | Profuse | Moderate | Minimal or Absent |
| **Thirst** | Intense for Cold Drinks | Present | Extreme, but may not be able to drink |
| **Constipation** | Possible | Absent | Severe, Abdominal Distention |
| **Tongue** | Red with Yellow Coating | Red with Little Coating | Dry, Cracked with Yellow-Brown Coating |
| **Pulse** | Surging, Rapid | Rapid | Deep, Forceful |
| **Treatment** | Clear Heat, Generate Fluids | Clear Heat, Resolve Toxicity | Purge Heat, Moisten Intestines |


## 📚 References & Resources

- *Shang Han Lun* (Treatise on Cold Damage)
- *Practical Diagnosis in Traditional Chinese Medicine* by Giovanni Maciocia
- *Chinese Herbal Medicine: Formulas & Strategies* by Dan Bensky and Steven Clavey
