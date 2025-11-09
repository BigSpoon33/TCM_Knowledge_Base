# TCM Advanced Slides - Template Structure Design

This document defines the standardized slide structure for converting TCM notes into Advanced Slides presentations.

---

## General Principles

### Slide Organization Philosophy
1. **Progressive Disclosure**: Start with overview, drill down to details
2. **Visual Hierarchy**: Use vertical slides for related sub-topics
3. **Consistent Structure**: Same slide sequence for all items in a category
4. **Clinical Focus**: Emphasize practical application over theory
5. **Memory Aids**: Include mnemonics and key learning points

### Slide Separator Convention
- `---` = New main topic (horizontal slide)
- `----` = Sub-topic/detail slide (vertical slide, accessed by down arrow)

### Standard Frontmatter
```yaml
---
theme: black  # or: white, league, sky, beige, simple, serif, blood, night, moon, solarized
transition: slide  # or: none, fade, convex, concave, zoom
slideNumber: true
progress: true
controls: true
---
```

---

## 1. HERB SLIDE TEMPLATE STRUCTURE

### Deck Organization: One deck per herb category
**Example**: `Slides_Herbs_that_Stop_Bleeding.md`

### Slide Sequence Per Herb (7-10 slides)

#### Slide 1: Title Slide (Horizontal)
```markdown
---
# 🌿 [Pinyin Name]

**[Hanzi]** · *[English Name]*

**Category**: [Herb Category]

<!-- slide bg="[[herb_image.jpg]]" -->
---
```

**Purpose**: Introduction with visual impact
**Content**: Name in all forms, category, optional background image

---

#### Slide 2: Quick Reference (Horizontal)
```markdown
---
## Quick Reference

| Property | Value |
|----------|-------|
| **Taste** | [bitter, sweet, etc.] |
| **Temperature** | [warm, cool, etc.] |
| **Channels** | [Liver, Spleen, etc.] |
| **Dosage** | [3-9g] |

**Pharmaceutical**: [Latin name]

---
```

**Purpose**: At-a-glance properties for quick review
**Content**: Core TCM properties in table format

---

#### Slide 3: Functions Overview (Horizontal)
```markdown
---
## ⚡ Primary Functions

1. **[Function 1]**
2. **[Function 2]**
3. **[Function 3]**

> *Key Clinical Use*: [One-sentence summary]

---
```

**Purpose**: Memorize main therapeutic actions
**Content**: 3-5 primary functions, clinical summary

---

#### Slide 4-6: Detailed Functions (Vertical slides under Slide 3)
```markdown
----
### Function 1: [Name]

**Clinical Application**:
- [Specific pattern/condition]
- [Key symptoms]

**Important Combinations**:
- With **[Herb]** → for [condition]
- With **[Herb]** → for [condition]

**Example Formula**: [[Formula Name]]

----
```

**Purpose**: Deep dive into each major function
**Content**: One slide per major function with combinations
**Note**: Use vertical slides (----) so they're "under" the overview

---

#### Slide 7: Clinical Indications (Horizontal)
```markdown
---
## 🎯 Clinical Indications

### Symptoms Treated
- [Symptom 1]
- [Symptom 2]
- [Symptom 3]

### Modern Applications
- [Western condition 1]
- [Western condition 2]

---
```

**Purpose**: Bridge TCM and modern clinical use
**Content**: Traditional symptoms + Western conditions

---

#### Slide 8: Cautions & Contraindications (Horizontal)
```markdown
---
## ⚠️ Cautions

### Contraindications
- [Contraindication 1]
- [Contraindication 2]

### Toxicity Notes
[Brief toxicity information if applicable]

### Pregnancy Category
[Safe/Caution/Contraindicated]

<!-- slide class="alert" -->
---
```

**Purpose**: Safety information - critical for clinical practice
**Content**: All safety warnings, contraindications
**Note**: Use alert class for visual emphasis

---

#### Slide 9: Formula Relationships (Horizontal)
```markdown
---
## 🔗 Key Formulas

### Chief Herb In:
- [[Formula 1]] - [Brief action]
- [[Formula 2]] - [Brief action]

### Deputy Herb In:
- [[Formula 3]] - [Brief action]

---
```

**Purpose**: Understand herb in formula context
**Content**: Major formulas containing this herb

---

#### Slide 10: Memory Aid (Horizontal)
```markdown
---
## 💡 Study Notes

### Mnemonic
[Memory device for functions/properties]

### Key Exam Points
1. [Point 1]
2. [Point 2]
3. [Point 3]

### Clinical Pearl
> [Practical clinical insight]

---
```

**Purpose**: Retention and exam preparation
**Content**: Mnemonics, exam tips, clinical pearls

---

## 2. FORMULA SLIDE TEMPLATE STRUCTURE

### Deck Organization: One deck per formula category
**Example**: `Slides_Qi_Tonic_Formulas.md`

### Slide Sequence Per Formula (10-12 slides)

#### Slide 1: Title Slide (Horizontal)
```markdown
---
# 💊 [Formula Name]

**[Pinyin]** · *[English Translation]*

**Category**: [Formula Category]
**Source**: [Classical text]

---
```

**Purpose**: Formula introduction
**Content**: Name, category, classical source

---

#### Slide 2: Formula Overview (Horizontal)
```markdown
---
## Overview

**Primary Action**: [Main therapeutic action]

**Key Pattern**: [Pattern treated]

**Tongue**: [Tongue presentation]
**Pulse**: [Pulse quality]

---
```

**Purpose**: Quick pattern recognition
**Content**: Action, pattern, tongue/pulse

---

#### Slide 3: Composition Table (Horizontal)
```markdown
---
## 🌿 Composition

| Herb | Dosage | Role |
|------|--------|------|
| [[Herb 1]] | 9-15g | Chief |
| [[Herb 2]] | 9-15g | Chief |
| [[Herb 3]] | 6-12g | Deputy |
| [[Herb 4]] | 3-6g | Envoy |

---
```

**Purpose**: Memorize formula composition
**Content**: All herbs with dosages and roles

---

#### Slide 4-7: Herb Roles Explained (Vertical slides under Slide 3)
```markdown
----
### Chief Herbs

**[[Herb 1]]** (9-15g)
- Function: [Primary action]
- Why chief: [Rationale]

**[[Herb 2]]** (9-15g)
- Function: [Primary action]
- Why chief: [Rationale]

----

### Deputy Herbs

**[[Herb 3]]** (6-12g)
- Function: [Supporting action]
- Synergy: [How it supports chiefs]

----
```

**Purpose**: Understand formula architecture
**Content**: One vertical slide per role category (Chief, Deputy, Assistant, Envoy)

---

#### Slide 8: Clinical Manifestations (Horizontal)
```markdown
---
## 🎯 Clinical Manifestations

### Key Symptoms
- [Symptom 1]
- [Symptom 2]
- [Symptom 3]
- [Symptom 4]

### Diagnostic Indicators
- **Tongue**: [Description]
- **Pulse**: [Description]

---
```

**Purpose**: Pattern recognition for diagnosis
**Content**: Complete symptom picture

---

#### Slide 9: Modern Applications (Horizontal)
```markdown
---
## 🏥 Modern Clinical Uses

### Western Conditions
- [Condition 1]
- [Condition 2]
- [Condition 3]

### Research Evidence
- [Key finding 1]
- [Key finding 2]

---
```

**Purpose**: Bridge to modern practice
**Content**: Western diagnoses, research support

---

#### Slide 10: Modifications (Horizontal)
```markdown
---
## 🔄 Common Modifications

| Condition | Add | Rationale |
|-----------|-----|-----------|
| [Condition 1] | [[Herb A]] + [[Herb B]] | [Reason] |
| [Condition 2] | [[Herb C]] | [Reason] |
| [Condition 3] | [[Herb D]] + [[Herb E]] | [Reason] |

---
```

**Purpose**: Clinical flexibility and customization
**Content**: Common additions for specific presentations

---

#### Slide 11: Cautions & Contraindications (Horizontal)
```markdown
---
## ⚠️ Cautions

### Contraindications
- [Contraindication 1]
- [Contraindication 2]

### Special Populations
- **Pregnancy**: [Safe/Caution/Avoid]
- **Elderly**: [Considerations]

<!-- slide class="alert" -->
---
```

**Purpose**: Safety in clinical practice
**Content**: All contraindications and warnings

---

#### Slide 12: Related Formulas (Horizontal)
```markdown
---
## 🔗 Related Formulas

### Same Category
- [[Formula A]] - [Key difference]
- [[Formula B]] - [Key difference]

### Derived From
- [[Base Formula]] + [modifications]

### Variations
- [[Variation 1]] = This formula + [additions]

---
```

**Purpose**: Understand formula relationships
**Content**: Related formulas with key distinctions

---

#### Slide 13: Memory Aid (Horizontal)
```markdown
---
## 💡 Study Notes

### Formula Structure Mnemonic
[Memory device for composition]

### Key Exam Points
1. [Point 1]
2. [Point 2]
3. [Point 3]

### Clinical Pearl
> [Practical insight from experience]

---
```

**Purpose**: Retention and exam prep
**Content**: Mnemonics, exam focus, clinical wisdom

---

## 3. ACUPUNCTURE POINT SLIDE TEMPLATE STRUCTURE

### Deck Organization: One deck per channel
**Example**: `Slides_Stomach_Channel_Points.md`

### Slide Sequence Per Point (8-10 slides)

#### Slide 1: Title Slide (Horizontal)
```markdown
---
# 📍 [POINT-CODE]

**[PINYIN]** ([Hanzi]) · *[English Name]*

**Channel**: [Channel Name]

<!-- slide bg="[[point_diagram.jpg]]" -->
---
```

**Purpose**: Point introduction with visual
**Content**: Point code, names, channel, location image

---

#### Slide 2: Location (Horizontal)
```markdown
---
## 📍 Location

[Detailed location description]

### Location Notes
[Additional location tips]

### Special Properties
- [Property 1]
- [Property 2]

---
```

**Purpose**: Accurate point location
**Content**: Location description, special properties

---

#### Slide 3: Location Image Detail (Vertical under Slide 2)
```markdown
----
## Location Diagram

![[point_diagram.jpg]]

### Anatomical Landmarks
- [Landmark 1]
- [Landmark 2]

----
```

**Purpose**: Visual location reference
**Content**: Large diagram, anatomical landmarks

---

#### Slide 4: Needling Technique (Horizontal)
```markdown
---
## 🔧 Needling Technique

**Method**: [Perpendicular/Oblique/Transverse]
**Depth**: [X to Y cun]

### Cautions
- [Caution 1]
- [Caution 2]

---
```

**Purpose**: Safe and effective needling
**Content**: Technique, depth, safety notes

---

#### Slide 5: Functions Overview (Horizontal)
```markdown
---
## ⚡ Primary Functions

1. **[Function 1]**
2. **[Function 2]**
3. **[Function 3]**
4. **[Function 4]**

---
```

**Purpose**: Memorize main actions
**Content**: 3-6 primary functions

---

#### Slide 6: Clinical Indications by System (Horizontal)
```markdown
---
## 🎯 Clinical Indications

### Digestive
- [Indication 1]
- [Indication 2]

### Respiratory
- [Indication 1]
- [Indication 2]

### Other
- [Indication 1]
- [Indication 2]

---
```

**Purpose**: Organize indications by body system
**Content**: Categorized clinical uses

---

#### Slide 7-8: Point Combinations (Horizontal + Verticals)
```markdown
---
## 🔗 Classical Combinations

### Top 5 Combinations

1. **[Condition]**: [Points] - *[Source]*
2. **[Condition]**: [Points] - *[Source]*
3. **[Condition]**: [Points] - *[Source]*

---

----
### Combination Detail: [Condition 1]

**Points**: [Point 1], [Point 2], [Point 3]
**Source**: *[Classical text]*

**Rationale**:
[Why these points work together]

**Clinical Notes**:
[Practical application tips]

----
```

**Purpose**: Learn classical point protocols
**Content**: Overview + detailed vertical slides for top combinations

---

#### Slide 9: TCM Theory (Horizontal)
```markdown
---
## 🧬 TCM Theory

### Point Significance
[Classical understanding and importance]

### Channel Theory
[How point relates to channel function]

### Historical Commentary
> [Classical quote or commentary]

---
```

**Purpose**: Theoretical understanding
**Content**: Classical theory, historical context

---

#### Slide 10: Memory Aid (Horizontal)
```markdown
---
## 💡 Study Notes

### Location Mnemonic
[Memory device for location]

### Function Mnemonic
[Memory device for functions]

### Key Exam Points
1. [Point 1]
2. [Point 2]

### Clinical Pearl
> [Practical clinical insight]

---
```

**Purpose**: Retention and exam prep
**Content**: Mnemonics, exam focus, clinical tips

---

## 4. PATTERN SLIDE TEMPLATE STRUCTURE

### Deck Organization: One deck per pattern category
**Example**: `Slides_Qi_Blood_Fluids_Patterns.md`

### Slide Sequence Per Pattern (6-8 slides)

#### Slide 1: Title Slide (Horizontal)
```markdown
---
# 🔍 [Pattern Name]

**Category**: [Pattern Category]
**Pathomechanism**: [Brief mechanism]

---
```

#### Slide 2: Etiology & Pathogenesis (Horizontal)
```markdown
---
## 🌊 Etiology

### Common Causes
- [Cause 1]
- [Cause 2]
- [Cause 3]

### Pathomechanism
[How the pattern develops]

---
```

#### Slide 3: Clinical Manifestations (Horizontal)
```markdown
---
## 🎯 Clinical Manifestations

### Key Symptoms
- [Symptom 1]
- [Symptom 2]
- [Symptom 3]

### Tongue & Pulse
- **Tongue**: [Description]
- **Pulse**: [Description]

---
```

#### Slide 4: Differential Diagnosis (Horizontal)
```markdown
---
## 🔄 Differential Diagnosis

| Pattern | Key Difference |
|---------|----------------|
| [[Similar Pattern 1]] | [Distinguishing feature] |
| [[Similar Pattern 2]] | [Distinguishing feature] |

---
```

#### Slide 5: Treatment Principle (Horizontal)
```markdown
---
## 💊 Treatment Principle

**Primary Principle**: [Main treatment strategy]

### Treatment Methods
1. [Method 1]
2. [Method 2]
3. [Method 3]

---
```

#### Slide 6: Representative Formulas (Horizontal)
```markdown
---
## 🌿 Key Formulas

### Primary Formula
**[[Formula 1]]** - [Brief description]

### Alternative Formulas
- [[Formula 2]] - [When to use]
- [[Formula 3]] - [When to use]

---
```

#### Slide 7: Acupuncture Treatment (Horizontal)
```markdown
---
## 📍 Acupuncture Points

### Primary Points
- [[Point 1]] - [Function]
- [[Point 2]] - [Function]
- [[Point 3]] - [Function]

### Supporting Points
- [[Point 4]] - [Function]
- [[Point 5]] - [Function]

---
```

#### Slide 8: Clinical Notes (Horizontal)
```markdown
---
## 💡 Clinical Pearls

### Diagnostic Keys
- [Key 1]
- [Key 2]

### Treatment Tips
- [Tip 1]
- [Tip 2]

### Prognosis
[Expected outcomes and timeline]

---
```

---

## 5. CATEGORY OVERVIEW SLIDES

### First Slide of Each Deck: Category Introduction

```markdown
---
# [Category Name]

## Overview
[Brief description of category]

## Topics Covered
1. [Item 1]
2. [Item 2]
3. [Item 3]
...

**Total Items**: [Number]

---
```

### Last Slide of Each Deck: Summary

```markdown
---
# 📚 Category Summary

## Key Takeaways
1. [Takeaway 1]
2. [Takeaway 2]
3. [Takeaway 3]

## Study Recommendations
- [Recommendation 1]
- [Recommendation 2]

## Next Steps
Continue to: [[Next Category Deck]]

---
```

---

## 6. ADVANCED FEATURES TO USE

### Split Layouts for Comparisons
```markdown
---
<split even>

## Pattern A
- Symptom 1
- Symptom 2

## Pattern B
- Symptom 1
- Symptom 2

</split>
---
```

### Fragments for Progressive Reveal
```markdown
---
## Functions

- Function 1 <!-- element class="fragment" -->
- Function 2 <!-- element class="fragment" -->
- Function 3 <!-- element class="fragment" -->

---
```

### Speaker Notes
```markdown
---
## Slide Content

note: These are speaker notes that won't appear on the slide but can be viewed in presenter mode. Include teaching tips, clinical stories, or additional context here.

---
```

### Callouts for Emphasis
```markdown
---
> [!warning] Important Safety Note
> This herb is contraindicated in pregnancy

> [!tip] Clinical Pearl
> Best results when combined with dietary therapy

---
```

---

## 7. NAMING CONVENTIONS

### File Naming Pattern
```
Slides_[Type]_[Category].md
```

**Examples**:
- `Slides_Herbs_Qi_Tonics.md`
- `Slides_Formulas_Exterior_Releasing.md`
- `Slides_Points_Stomach_Channel.md`
- `Slides_Patterns_Qi_Blood_Fluids.md`

### Frontmatter Tags
```yaml
---
theme: black
tags:
  - slides
  - tcm
  - [type]
  - [category]
material_type: presentation
created: 2025-11-04
---
```

---

## 8. GENERATION SCRIPT REQUIREMENTS

The slide generation script should:

1. **Read source files** from TCM_Herbs/, TCM_Formulas/, TCM_Points/, TCM_Patterns/
2. **Group by category** (herb category, formula category, channel, pattern type)
3. **Generate one deck per category** with all items in that category
4. **Follow template structure** exactly as defined above
5. **Include navigation** between items (horizontal) and details (vertical)
6. **Preserve wikilinks** to maintain Obsidian connectivity
7. **Include images** where available (point diagrams, herb photos)
8. **Add frontmatter** with appropriate theme and settings
9. **Create index file** listing all slide decks

---

## 9. PRESENTATION WORKFLOW

### For Teaching/Presenting
1. Open slide deck in Obsidian
2. Use Advanced Slides plugin to start presentation
3. Navigate horizontally through items
4. Navigate vertically for details on each item
5. Use speaker notes for teaching points

### For Self-Study
1. Review slides sequentially
2. Test recall before revealing details (vertical slides)
3. Use memory aid slides for retention
4. Link to source notes for deeper study

### For Exam Prep
1. Focus on "Key Exam Points" slides
2. Use mnemonics for memorization
3. Practice with "Quick Reference" slides
4. Review "Clinical Pearls" for practical application

---

## 10. VISUAL DESIGN RECOMMENDATIONS

### Color Coding by Type
- **Herbs**: Green theme (🌿)
- **Formulas**: Blue theme (💊)
- **Points**: Red theme (📍)
- **Patterns**: Purple theme (🔍)

### Icon Usage
- 🌿 Herbs
- 💊 Formulas
- 📍 Points
- 🔍 Patterns
- ⚡ Functions
- 🎯 Indications
- ⚠️ Cautions
- 🔗 Relationships
- 💡 Study notes
- 🧬 Theory

### Font Sizes (via CSS)
- Title: Large (H1)
- Section: Medium (H2)
- Content: Normal (body)
- Notes: Small (italics)

---

*This template structure provides a standardized, pedagogically sound approach to converting TCM knowledge base notes into presentation slides suitable for teaching, studying, and clinical reference.*
