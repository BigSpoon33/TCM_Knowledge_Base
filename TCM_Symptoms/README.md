# TCM Symptoms Database

This directory contains standardized symptom files that serve as a crucial linking layer in the TCM Knowledge Base.

## Purpose

Symptoms connect diseases to treatments:
```
Diseases → Symptoms → Points/Herbs/Formulas
```

By creating symptom files, we can:
- Link multiple diseases that share symptoms
- Map symptoms to specific treatment strategies
- Differentiate patterns based on symptom combinations
- Auto-link related entities across the knowledge base

## Structure

Each symptom file follows the `TEMPLATE_Symptom.md` template with:

### Core Sections
- **Overview**: What the symptom is from TCM perspective
- **Pattern Differentiation**: Different TCM patterns that cause this symptom
- **Organs Involved**: Which Zang-Fu organs relate to the symptom
- **Treatment Approaches**: Points, herbs, formulas organized by pattern
- **Differential Diagnosis**: How to distinguish between similar presentations

### Frontmatter Fields
```yaml
name: "Symptom Name"
category: symptom
type: "" # physical, mental, energetic, digestive, pain, etc.
related_patterns: []
related_organs: []
related_meridians: []
associated_diseases: []
treatment_points: []
treatment_herbs: []
treatment_formulas: []
```

## Symptom Types

Organize symptoms by type for easier navigation:

- **Physical**: Headache, Dizziness, Sweating, etc.
- **Pain**: Chest pain, Abdominal pain, Joint pain, etc.
- **Mental**: Anxiety, Insomnia, Restlessness, etc.
- **Energetic**: Fatigue, Weakness, Heaviness, etc.
- **Digestive**: Nausea, Diarrhea, Constipation, etc.
- **Respiratory**: Cough, Wheezing, Shortness of breath, etc.
- **Circulatory**: Palpitations, Edema, Cold extremities, etc.

## Creating New Symptoms

1. Copy `TEMPLATE_Symptom.md`
2. Name file as `Symptom_Name.md` (e.g., `Headache.md`, `Syncope.md`)
3. Fill in pattern differentiation (most important!)
4. Add treatment approaches for each pattern
5. Include diagnostic significance
6. Auto-sync will extract wikilinks to build relationships

## Auto-Linking

When you use `[[Symptom Name]]` in disease files, the auto-sync system will:
- Detect the symptom wikilink
- Add it to the disease's frontmatter
- Build bidirectional relationships
- Enable queries like "which diseases cause headache?"

## Example Workflow

**Creating a disease file:**
```markdown
# Wind Stroke

## Main Manifestations
- [[Headache]] (sudden, severe)
- [[Syncope]] or loss of consciousness
- [[Hemiplegia]]
- Deviation of eye and mouth
```

**Auto-sync extracts:**
- Symptoms: Headache, Syncope, Hemiplegia
- Links these to treatment approaches in each symptom file

## Current Symptoms

- **Headache** - Complete with 8 pattern differentiations
- **Syncope** - Complete with 6 patterns + emergency protocols

## Next Steps

Build out common symptoms:
- Fatigue
- Dizziness
- Insomnia
- Palpitations
- Shortness of breath
- Cough
- Abdominal pain
- Diarrhea
- Constipation
- Anxiety
- etc.

---

**Note**: The symptom database is designed to grow organically. Add symptoms as you encounter them in clinical practice or textbooks. Quality over quantity - each symptom should have thorough pattern differentiation.
