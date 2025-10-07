---
# 🔹 Core Metadata (Universal Fields)
id: "technique-YYYYMMDDHHMMSS"
name: "Technique Name"
type: "technique"
aliases: ["Alternative Name", "Chinese Name", "Pinyin"]
tags: [TCM, Technique, Category, Method]

# 🔹 Cross-Link Fields (Universal Relationship Slots)
category: ["Technique Category"]  # "Acupuncture Techniques", "Moxibustion", "Cupping", "Needling Methods"
related: []  # Related techniques or methods
symptoms: []  # Symptoms/conditions this technique treats
patterns: []  # TCM patterns where this technique is applicable
western_conditions: []  # Modern conditions treated
formulas: []  # May be combined with these formulas
herbs: []
points: []  # Points where this technique is commonly applied
nutrition: []
tests: []

# 🔹 Technique-Specific Data
technique_data:
  chapter: "Chapter Number"
  chapter_name: "Chapter Name"
  section: "Section Name"

  technique_type: ""  # "needling", "moxibustion", "cupping", "manipulation", "supplementary"

  overview:
    description: "Brief description of the technique"
    traditional_name: "Classical Chinese name"
    pinyin: "Pinyin pronunciation"
    historical_origin: "Historical context or classical source"

  principles:
    therapeutic_mechanism: "How this technique works therapeutically"
    indications_general: "General conditions treated"
    contraindications: ["Contraindication 1", "Contraindication 2"]
    cautions: ["Caution 1", "Caution 2"]

  procedure:
    preparation:
      materials_needed: ["Material 1", "Material 2"]
      patient_position: "Patient positioning"
      practitioner_preparation: "What practitioner should prepare"

    execution:
      steps:
        - step_number: 1
          description: "Detailed step description"
          visual_cue: "What to observe"
        - step_number: 2
          description: "Next step"
          visual_cue: "Observable indicator"

      parameters:
        depth: "Needling depth or application intensity"
        duration: "How long to maintain"
        frequency: "How often to repeat"
        angle: "Angle of insertion (if applicable)"
        direction: "Direction of manipulation"

      sensation:
        practitioner: "What the practitioner should feel"
        patient: "Expected patient sensation (de qi, warmth, etc.)"

    completion:
      duration: "Total treatment time"
      post_procedure: "What to do after"
      needle_retention: "How long to retain (if applicable)"

  clinical_applications:
    primary_indications:
      - condition: "Condition name"
        pattern: "Specific pattern"
        points: ["Point 1", "Point 2"]
        notes: "Special considerations"

    specific_techniques:
      - variation_name: "Name of specific variation"
        description: "How this variation differs"
        when_used: "Specific indications"
        method: "Specific technique details"

  safety:
    contraindications:
      absolute: ["Absolute contraindication 1", "Absolute contraindication 2"]
      relative: ["Relative contraindication 1", "Relative contraindication 2"]

    precautions: ["Precaution 1", "Precaution 2"]
    adverse_effects_possible: ["Effect 1", "Effect 2"]
    management_of_complications: "How to handle adverse reactions"

  variations:
    - name: "Variation name"
      description: "Description of variation"
      indications: "When to use this variation"
      method: "How it differs from standard technique"

  combinations:
    compatible_techniques: ["Technique 1", "Technique 2"]
    incompatible_techniques: ["Technique to avoid", "Reason"]
    synergistic_effects: "How combining techniques enhances treatment"

  evidence:
    traditional_evidence: "Classical text references"
    clinical_observations: "Traditional clinical experience"
    modern_research: "Contemporary studies or findings"

created: YYYY-MM-DD
updated: YYYY-MM-DD
---

# 🔧 {{technique_name}}

**Traditional Name:** {{chinese_name}} ({{pinyin}})

## 📖 Overview

{{detailed_description}}

**Technique Type:** {{needling/moxibustion/cupping/etc.}}

**Historical Context:**
{{origin_and_classical_references}}

---

## ⚙️ Therapeutic Principles

### Mechanism of Action
{{how_this_technique_works}}

### General Indications
{{what_conditions_this_treats}}

**Primary Uses:**
- {{use_1}}
- {{use_2}}
- {{use_3}}

### Contraindications
**Absolute:**
- {{contraindication_1}}
- {{contraindication_2}}

**Relative:**
- {{relative_contraindication_1}}
- {{relative_contraindication_2}}

### Cautions
- {{caution_1}}
- {{caution_2}}

---

## 🛠️ Procedure

### Preparation

**Materials Needed:**
- {{material_1}}
- {{material_2}}
- {{material_3}}

**Patient Position:**
{{how_to_position_patient}}

**Practitioner Preparation:**
{{what_practitioner_needs_to_do}}

---

### Execution

#### Step-by-Step Instructions

**Step 1:**
{{detailed_description}}
- **Visual Cue:** {{what_to_observe}}

**Step 2:**
{{detailed_description}}
- **Visual Cue:** {{what_to_observe}}

**Step 3:**
{{detailed_description}}
- **Visual Cue:** {{what_to_observe}}

---

#### Technical Parameters

| Parameter | Specification |
|-----------|---------------|
| **Depth** | {{depth_specification}} |
| **Duration** | {{time_duration}} |
| **Frequency** | {{repetition_frequency}} |
| **Angle** | {{insertion_angle}} |
| **Direction** | {{manipulation_direction}} |

---

#### Expected Sensations

**Practitioner Should Feel:**
{{what_practitioner_senses}}

**Patient Should Feel:**
{{expected_patient_sensation}}

**De Qi Characteristics:**
{{description_of_qi_arrival}}

---

### Completion

**Treatment Duration:** {{total_time}}

**Needle Retention:** {{retention_time}}

**Post-Procedure:**
{{what_to_do_after_treatment}}

---

## 🎯 Clinical Applications

### Condition 1: {{Condition_Name}}

**Pattern:** {{Specific_TCM_pattern}}

**Recommended Points:**
- [[Point-1]] - {{function}}
- [[Point-2]] - {{function}}

**Technique Notes:**
{{specific_considerations_for_this_condition}}

---

### Condition 2: {{Condition_Name}}

**Pattern:** {{Specific_TCM_pattern}}

**Recommended Points:**
- [[Point-3]] - {{function}}
- [[Point-4]] - {{function}}

**Technique Notes:**
{{specific_considerations}}

---

## 🔄 Variations & Modifications

### Variation 1: {{Name}}

**Description:**
{{how_this_differs}}

**Indications:**
{{when_to_use_this_variation}}

**Method:**
{{specific_technique_details}}

---

### Variation 2: {{Name}}

**Description:**
{{how_this_differs}}

**Indications:**
{{when_to_use}}

**Method:**
{{technique_details}}

---

## 🔗 Combinations

### Compatible Techniques
Can be effectively combined with:
- [[Technique 1]] - {{synergistic_effect}}
- [[Technique 2]] - {{synergistic_effect}}

### Incompatible Techniques
Should NOT be combined with:
- [[Technique 3]] - {{reason}}

### Synergistic Effects
{{how_combinations_enhance_treatment}}

---

## ⚠️ Safety Considerations

### Precautions
1. {{precaution_1}}
2. {{precaution_2}}
3. {{precaution_3}}

### Possible Adverse Effects
- {{adverse_effect_1}}
- {{adverse_effect_2}}

### Managing Complications
{{how_to_handle_problems}}

**If {{complication}} occurs:**
{{specific_management_strategy}}

---

## 📊 Evidence & Clinical Experience

### Traditional Evidence
{{classical_text_references}}

> "{{Classical_quote}}"
> — *{{Source}}*, Chapter {{number}}

### Clinical Observations
{{traditional_clinical_experience}}

### Modern Research
{{contemporary_findings}}

---

## 💡 Clinical Pearls

{{expert_tips}}

{{common_mistakes_to_avoid}}

{{optimization_strategies}}

---

## 📚 Related Information

**Related Techniques:** [[Technique A]] | [[Technique B]]
**Commonly Used Points:** [[Point 1]] | [[Point 2]] | [[Point 3]]
**Related Patterns:** [[Pattern 1]] | [[Pattern 2]]
**Treated Conditions:** [[Disease 1]] | [[Disease 2]]

**Chapter Reference:** Chapter {{number}} - {{chapter_name}}

---

## 📝 Practice Notes

{{space_for_personal_observations}}

{{refinements_from_clinical_practice}}

{{patient_feedback_patterns}}

---

## 📹 Visual References

{{diagrams_or_image_links}}

{{video_demonstrations_if_available}}

---

*Source: Chinese Acupuncture and Moxibustion (Xinnong), Chapter {{number}}*
*Last updated: {{date}}*
