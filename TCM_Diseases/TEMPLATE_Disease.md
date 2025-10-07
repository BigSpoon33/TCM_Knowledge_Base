---
# 🔹 Core Metadata (Universal Fields)
id: "disease-YYYYMMDDHHMMSS"
name: "Disease Name"
type: "disease"
aliases: ["Alternative Name", "Pinyin Name", "Western Medical Term"]
tags: [TCM, Disease, System, Category]

# 🔹 Cross-Link Fields (Universal Relationship Slots)
category: ["Disease Category"]  # "Internal Diseases", "Gynecological Diseases", "External Diseases"
related: []  # Related diseases or conditions
symptoms: ["Symptom 1", "Symptom 2", "Symptom 3"]  # Main clinical manifestations
patterns: ["Pattern 1", "Pattern 2"]  # TCM pattern differentiations for this disease
western_conditions: ["Western Diagnosis 1", "Western Diagnosis 2"]  # Modern medical correlations
formulas: []  # Herbal formulas used to treat this
herbs: []  # Individual herbs commonly used
points: ["Point-1", "Point-2", "Point-3"]  # Acupuncture points in treatment protocols
nutrition: []  # Dietary recommendations
tests: []  # Diagnostic tests

# 🔹 Disease-Specific Data
disease_data:
  chapter: "Chapter Number"
  chapter_name: "Chapter Name"
  disease_category: ""  # "internal", "gynecological", "pediatric", "external", etc.

  overview:
    description: "Brief description of the disease"
    key_features: ["Feature 1", "Feature 2"]
    onset_characteristics: "Sudden/gradual, acute/chronic, etc."

  western_correlation:
    conditions: ["Modern diagnosis 1", "Modern diagnosis 2"]
    notes: "Additional notes on biomedical correlation"

  etiology:
    primary_causes: ["Cause 1", "Cause 2"]
    contributing_factors: ["Factor 1", "Factor 2"]
    pathogenesis: "Detailed explanation of how the disease develops"
    affected_organs: ["Organ 1", "Organ 2"]

  pattern_differentiation:
    - pattern_name: "Pattern Name 1"
      pattern_type: "excess/deficiency/mixed"
      subcategory: "tense/flaccid, heat/cold, etc."

      manifestations:
        main_symptoms: ["Symptom 1", "Symptom 2"]
        accompanying_symptoms: ["Symptom 3", "Symptom 4"]
        tongue: "Tongue appearance"
        pulse: "Pulse quality"

      analysis: "TCM pathological explanation of why these symptoms occur"

      treatment:
        principle: "Treatment principle for this pattern"
        method: "Primary treatment method"
        needle_technique: "reinforcing/reducing/even/moxibustion"

        primary_points:
          - code: "Point-Code"
            name: "Point Name"
            function: "Why this point is selected"
            technique: "Needle technique for this specific point"

        supplementary_points:
          - condition: "Specific symptom or complication"
            points:
              - code: "Point-Code"
                name: "Point Name"
                function: "Purpose"

        explanation: "Detailed rationale for point selection and combination"

        modifications:
          - condition: "If patient also has X"
            add_points: ["Point-1", "Point-2"]
            remove_points: ["Point-3"]

  differential_diagnosis:
    - disease: "Similar Disease Name"
      distinguishing_features: "How to differentiate from this disease"

  prognosis:
    general: "Overall prognosis information"
    favorable_signs: ["Sign 1", "Sign 2"]
    unfavorable_signs: ["Sign 1", "Sign 2"]

  prevention:
    lifestyle: ["Recommendation 1", "Recommendation 2"]
    prophylactic_treatment: "Preventive acupuncture or other measures"

  remarks: "Additional clinical notes, warnings, special considerations"

created: YYYY-MM-DD
updated: YYYY-MM-DD
---

# 🩺 {{disease_name}}

## 📖 Overview

{{detailed_description_of_disease}}

**Key Characteristics:**
- {{feature_1}}
- {{feature_2}}
- {{feature_3}}

**Onset:** {{onset_pattern}}

---

## 🏥 Western Medicine Correlation

**Modern Diagnosis:**
- {{western_condition_1}}
- {{western_condition_2}}

**Notes:**
{{additional_biomedical_context}}

---

## 🧬 Etiology & Pathogenesis

### Primary Causes
{{what_causes_this_disease}}

1. **{{Cause_1}}:** {{explanation}}
2. **{{Cause_2}}:** {{explanation}}

### Contributing Factors
- {{factor_1}}
- {{factor_2}}
- {{factor_3}}

### Pathological Mechanism
{{detailed_explanation_of_disease_development}}

**Affected Organs:**
- **{{Organ_1}}:** {{how_affected}}
- **{{Organ_2}}:** {{how_affected}}

**Qi & Blood Dynamics:**
{{description_of_qi_blood_disruption}}

---

## 🔬 Pattern Differentiation

### Pattern 1: {{Pattern Name}}

**Type:** {{Excess/Deficiency/Mixed}}
**Subcategory:** {{Tense/Flaccid, Heat/Cold, etc.}}

#### Main Manifestations
- {{symptom_1}}
- {{symptom_2}}
- {{symptom_3}}

**Tongue:** {{appearance}}
**Pulse:** {{quality}}

#### TCM Analysis
{{pathological_explanation_of_why_these_symptoms_occur}}

---

### Pattern 2: {{Pattern Name}}

**Type:** {{Excess/Deficiency/Mixed}}

#### Main Manifestations
- {{symptom_1}}
- {{symptom_2}}

**Tongue:** {{appearance}}
**Pulse:** {{quality}}

#### TCM Analysis
{{pathological_explanation}}

---

## 💉 Treatment Protocols

### Pattern: {{Pattern_1_Name}}

#### Treatment Principle
{{treatment_strategy}}

#### Method
{{primary_treatment_approach}}

**Needle Technique:** {{Reinforcing/Reducing/Even/Moxibustion}}

#### Primary Points

| Point | Name | Function | Technique |
|-------|------|----------|-----------|
| [[{{Code}}]] | {{Name}} | {{Purpose}} | {{Method}} |
| [[{{Code}}]] | {{Name}} | {{Purpose}} | {{Method}} |
| [[{{Code}}]] | {{Name}} | {{Purpose}} | {{Method}} |

#### Supplementary Points

**For {{Specific_Symptom}}:**
- [[Point-1]] - {{function}}
- [[Point-2]] - {{function}}

**For {{Another_Symptom}}:**
- [[Point-3]] - {{function}}

#### Explanation
{{detailed_rationale_for_point_selection}}

{{explanation_of_point_combinations}}

{{mechanism_of_therapeutic_effect}}

#### Modifications
- **If {{condition}}:** Add [[Point-X]], [[Point-Y]]
- **If {{condition}}:** Remove [[Point-Z]]

---

### Pattern: {{Pattern_2_Name}}

#### Treatment Principle
{{treatment_strategy}}

#### Method
{{primary_treatment_approach}}

**Needle Technique:** {{Reinforcing/Reducing/Even/Moxibustion}}

#### Primary Points

| Point | Name | Function |
|-------|------|----------|
| [[{{Code}}]] | {{Name}} | {{Purpose}} |
| [[{{Code}}]] | {{Name}} | {{Purpose}} |

#### Explanation
{{treatment_rationale}}

---

## 🔍 Differential Diagnosis

### vs. [[Similar Disease 1]]
{{distinguishing_features}}

**Key Differences:**
- {{difference_1}}
- {{difference_2}}

### vs. [[Similar Disease 2]]
{{distinguishing_features}}

---

## 📊 Prognosis

{{general_prognosis_information}}

**Favorable Signs:**
- {{sign_1}}
- {{sign_2}}

**Unfavorable Signs:**
- {{sign_1}}
- {{sign_2}}

---

## 🛡️ Prevention & Prophylaxis

### Lifestyle Recommendations
- {{recommendation_1}}
- {{recommendation_2}}
- {{recommendation_3}}

### Prophylactic Treatment
{{preventive_acupuncture_or_measures}}

**Recommended Points for Prevention:**
- [[Point-1]] - {{function}}
- [[Point-2]] - {{function}}

---

## ⚠️ Clinical Remarks

{{special_considerations}}

{{warnings_or_contraindications}}

{{additional_clinical_pearls}}

---

## 📚 Related Information

**Related Patterns:** [[Pattern A]] | [[Pattern B]]
**Related Diseases:** [[Disease A]] | [[Disease B]]
**Key Concepts:** [[Concept 1]] | [[Concept 2]]
**Common Formulas:** [[Formula 1]] | [[Formula 2]]

**Chapter Reference:** Chapter {{number}} - {{chapter_name}}

---

## 📖 Case Studies / Clinical Notes

{{space_for_clinical_observations}}

{{treatment_outcomes}}

{{personal_notes}}

---

*Source: Chinese Acupuncture and Moxibustion (Xinnong), Chapter {{number}}*
*Last updated: {{date}}*
