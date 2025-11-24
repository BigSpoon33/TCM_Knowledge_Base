# Root Note Template

**Universal template for creating comprehensive subject matter notes that can auto-generate OCDS materials**

---

## 📚 Purpose

Root notes are **comprehensive, structured knowledge files** that serve as the single source of truth for a topic. They contain enough detail to automatically generate:
- Flashcards (spaced repetition)
- Quizzes (auto-graded)
- Slides (presentations)
- Study materials
- Tasks

**Philosophy:** Write once, generate many.

---

## 🎯 Design Principles

1. **Domain-Agnostic** - Works for TCM, biology, history, programming, etc.
2. **Comprehensive** - Contains all essential information for learning
3. **Structured** - Parseable by scripts and AI
4. **Hierarchical** - Core concepts → Details → Applications
5. **Cross-Linked** - References related concepts
6. **Testable** - Contains facts, relationships, and applications suitable for assessment

---

## 📋 Complete Template

```markdown
---
# ═══════════════════════════════════════════════════════════
# CORE METADATA (Universal - All Root Notes)
# ═══════════════════════════════════════════════════════════
id: "root-{{YYYYMMDDHHMMSS}}"
name: "{{TOPIC_NAME}}"
type: "root_note"
domain: "{{DOMAIN}}" # e.g., "TCM", "Biology", "History", "Programming"
subject: "{{SUBJECT}}" # e.g., "Patterns", "Cell Biology", "World War II", "Python"
aliases: []
tags: [root_note, {{DOMAIN}}, {{SUBJECT}}]

# ═══════════════════════════════════════════════════════════
# CROSS-REFERENCE FIELDS (Relationship Mapping)
# ═══════════════════════════════════════════════════════════
category: [] # Hierarchical categories
related: [] # Related root notes
prerequisites: [] # What you need to know first
leads_to: [] # What comes after this topic

# ═══════════════════════════════════════════════════════════
# LEARNING METADATA (Educational Context)
# ═══════════════════════════════════════════════════════════
learning_data:
  # Difficulty & Scope
  difficulty: "{{beginner|intermediate|advanced}}"
  estimated_study_time: "{{X hours}}"
  bloom_levels: [] # e.g., ["Remember", "Understand", "Apply", "Analyze"]
  
  # Learning Objectives (SMART format)
  objectives:
    - "{{Specific, measurable learning objective 1}}"
    - "{{Specific, measurable learning objective 2}}"
  
  # Key Questions (What students should be able to answer)
  key_questions:
    - "{{Essential question 1}}"
    - "{{Essential question 2}}"
  
  # Common Misconceptions
  misconceptions:
    - misconception: "{{Common wrong belief}}"
      correction: "{{Accurate explanation}}"

# ═══════════════════════════════════════════════════════════
# CONTENT STRUCTURE (Topic-Specific Data)
# ═══════════════════════════════════════════════════════════
content_data:
  # Core Concepts (The "What")
  core_concepts:
    - name: "{{Concept Name}}"
      definition: "{{Clear, concise definition}}"
      importance: "{{Why this matters}}"
      keywords: []
  
  # Key Facts (The "Must Know")
  key_facts:
    - fact: "{{Factual statement}}"
      category: "{{Fact type}}"
      testable: true # Can this be tested?
  
  # Processes/Mechanisms (The "How")
  processes:
    - name: "{{Process Name}}"
      steps:
        - step: 1
          description: "{{What happens}}"
          key_point: "{{Why it matters}}"
      outcome: "{{End result}}"
  
  # Relationships (The "Connections")
  relationships:
    - type: "{{causes|leads_to|contrasts_with|similar_to}}"
      entity_a: "{{Concept A}}"
      entity_b: "{{Concept B}}"
      explanation: "{{How they relate}}"
  
  # Applications (The "When/Where")
  applications:
    - context: "{{Real-world scenario}}"
      application: "{{How concept is used}}"
      example: "{{Concrete example}}"
  
  # Comparisons (The "Versus")
  comparisons:
    - entities: ["{{Entity 1}}", "{{Entity 2}}"]
      dimensions:
        - dimension: "{{Comparison aspect}}"
          entity_1_value: "{{Value for entity 1}}"
          entity_2_value: "{{Value for entity 2}}"
      key_distinction: "{{Main difference}}"

# ═══════════════════════════════════════════════════════════
# ASSESSMENT DATA (For Quiz/Flashcard Generation)
# ═══════════════════════════════════════════════════════════
assessment_data:
  # Flashcard Seeds (Direct Q&A pairs)
  flashcard_seeds:
    - question: "{{Question}}"
      answer: "{{Answer}}"
      context: "{{Topic context}}"
      difficulty: "{{easy|medium|hard}}"
      card_type: "{{basic|cloze|comparison|application}}"
  
  # Quiz Seeds (Multiple choice, short answer, etc.)
  quiz_seeds:
    - question: "{{Question text}}"
      question_type: "{{multiple_choice|true_false|short_answer|matching}}"
      correct_answer: "{{Correct answer}}"
      distractors: ["{{Wrong answer 1}}", "{{Wrong answer 2}}"]
      explanation: "{{Why this is correct}}"
      difficulty: "{{easy|medium|hard}}"
      bloom_level: "{{Remember|Understand|Apply|Analyze}}"
  
  # Clinical/Applied Scenarios (Case-based questions)
  scenarios:
    - scenario: "{{Realistic situation description}}"
      question: "{{What should you do/identify?}}"
      correct_response: "{{Correct answer}}"
      reasoning: "{{Why this is correct}}"

# ═══════════════════════════════════════════════════════════
# PRESENTATION DATA (For Slide Generation)
# ═══════════════════════════════════════════════════════════
presentation_data:
  # Slide Outline
  slide_outline:
    - slide_number: 1
      slide_type: "{{title|content|comparison|process|summary}}"
      title: "{{Slide title}}"
      key_points: []
      visual_suggestion: "{{Diagram/chart type}}"
  
  # Key Visuals
  visuals:
    - type: "{{diagram|flowchart|table|image}}"
      description: "{{What to show}}"
      purpose: "{{Why include this}}"
  
  # Memory Aids
  memory_aids:
    - type: "{{mnemonic|acronym|analogy|story}}"
      content: "{{The memory device}}"
      applies_to: "{{What it helps remember}}"

# ═══════════════════════════════════════════════════════════
# METADATA
# ═══════════════════════════════════════════════════════════
created: {{YYYY-MM-DD}}
updated: {{YYYY-MM-DD}}
author: "{{Your Name}}"
sources: []
---

# 📘 {{TOPIC_NAME}}

**Domain:** `= this.domain` | **Subject:** `= this.subject`  
**Difficulty:** `= this.learning_data.difficulty` | **Study Time:** `= this.learning_data.estimated_study_time`

---

## 🎯 Learning Objectives

By the end of this topic, you should be able to:

`= join(this.learning_data.objectives, "\n- ")`

---

## 📖 Overview

{{Brief 2-3 paragraph introduction to the topic. What is it? Why does it matter? Where does it fit in the bigger picture?}}

**Key Context:**
- **Prerequisites:** `= join(this.prerequisites, ", ")`
- **Builds Toward:** `= join(this.leads_to, ", ")`
- **Related Topics:** `= join(this.related, ", ")`

---

## 🧠 Core Concepts

### {{Concept 1 Name}}

**Definition:** {{Clear, precise definition}}

**Importance:** {{Why this concept matters}}

**Key Characteristics:**
- {{Characteristic 1}}
- {{Characteristic 2}}
- {{Characteristic 3}}

**Common Misconception:**
> ❌ **Wrong:** {{Common misunderstanding}}  
> ✅ **Correct:** {{Accurate understanding}}

---

### {{Concept 2 Name}}

{{Repeat structure for each core concept}}

---

## 🔍 Detailed Explanation

### {{Section 1: Main Topic Area}}

{{Comprehensive explanation of the topic. Include:}}
- {{Detailed information}}
- {{Supporting details}}
- {{Examples}}
- {{Clarifications}}

**Key Points to Remember:**
1. {{Essential point 1}}
2. {{Essential point 2}}
3. {{Essential point 3}}

---

### {{Section 2: Mechanisms/Processes}}

**Process Name:** {{Name of the process}}

**Steps:**
1. **{{Step 1}}** - {{Description and significance}}
2. **{{Step 2}}** - {{Description and significance}}
3. **{{Step 3}}** - {{Description and significance}}

**Outcome:** {{What results from this process}}

**Clinical/Practical Significance:** {{Why this matters in practice}}

---

## 🔗 Relationships & Connections

### How {{Topic}} Relates to {{Related Concept A}}

{{Explanation of relationship}}

**Key Connection:** {{The main link between them}}

---

### {{Topic}} vs {{Similar/Contrasting Concept}}

| Feature | {{Topic}} | {{Other Concept}} |
|---------|-----------|-------------------|
| {{Dimension 1}} | {{Value}} | {{Value}} |
| {{Dimension 2}} | {{Value}} | {{Value}} |
| {{Dimension 3}} | {{Value}} | {{Value}} |

**Key Distinction:** {{The most important difference}}

---

## 💡 Applications & Examples

### Real-World Application 1

**Context:** {{When/where this applies}}

**Application:** {{How the concept is used}}

**Example:**
{{Concrete, detailed example showing the concept in action}}

**Outcome:** {{What happens/what's achieved}}

---

### Real-World Application 2

{{Repeat structure for additional applications}}

---

## 🎯 Clinical/Practical Scenarios

### Scenario 1: {{Scenario Title}}

**Situation:**
{{Realistic scenario description}}

**Question:** {{What would you do/identify/recommend?}}

**Correct Response:** {{The right answer}}

**Reasoning:**
{{Step-by-step explanation of why this is correct}}

**Common Mistakes:**
- ❌ {{Common wrong approach and why it's wrong}}
- ❌ {{Another common mistake}}

---

## 📊 Comparison Table

{{If applicable, include comprehensive comparison table}}

| Feature | Option A | Option B | Option C |
|---------|----------|----------|----------|
| {{Feature 1}} | {{Value}} | {{Value}} | {{Value}} |
| {{Feature 2}} | {{Value}} | {{Value}} | {{Value}} |
| **When to Use** | {{Context}} | {{Context}} | {{Context}} |

---

## 🧩 Differential Diagnosis / Decision Points

{{For clinical/applied topics - how to distinguish between similar options}}

### When You See {{Indicator A}}

**Think:** {{Likely option}}

**Confirm By:** {{Additional checks}}

**Rule Out:** {{What it's NOT}}

---

## 💊 Treatment/Solution Approach

{{For clinical/problem-solving topics}}

### Primary Approach

**Method:** {{Main strategy}}

**Rationale:** {{Why this works}}

**Steps:**
1. {{Action step 1}}
2. {{Action step 2}}
3. {{Action step 3}}

### Alternative Approaches

**When to Use Alternative:** {{Conditions for using different approach}}

---

## ⚠️ Important Warnings & Contraindications

{{Critical information about what NOT to do}}

**Do NOT:**
- {{Contraindication 1}}
- {{Contraindication 2}}

**Cautions:**
- {{Important consideration 1}}
- {{Important consideration 2}}

**Red Flags:**
- {{Warning sign 1}}
- {{Warning sign 2}}

---

## 🎓 Study Tips & Memory Aids

### Mnemonic Device

**{{ACRONYM}}** stands for:
- **{{Letter}}** - {{What it represents}}
- **{{Letter}}** - {{What it represents}}

**How to Use:** {{When/how to apply this mnemonic}}

---

### Analogy

**Think of {{Topic}} like {{Familiar Concept}}:**

{{Detailed analogy that makes the concept intuitive}}

**Key Similarity:** {{What makes this analogy work}}

**Limitation:** {{Where the analogy breaks down}}

---

### Visual Memory Aid

{{Description of a mental image or diagram to remember}}

---

## ✅ Self-Check Questions

Test your understanding:

1. **{{Question 1}}**
   - {{Answer}}

2. **{{Question 2}}**
   - {{Answer}}

3. **{{Question 3}}**
   - {{Answer}}

---

## 🔬 Advanced Topics

{{Optional: More complex aspects for advanced learners}}

### {{Advanced Topic 1}}

{{Explanation of more nuanced/complex aspect}}

---

## 📚 Summary

### Key Takeaways

1. **{{Main Point 1}}** - {{Brief explanation}}
2. **{{Main Point 2}}** - {{Brief explanation}}
3. **{{Main Point 3}}** - {{Brief explanation}}

### Essential Facts to Remember

- {{Fact 1}}
- {{Fact 2}}
- {{Fact 3}}

### Common Exam Questions

- {{Typical question 1}}
- {{Typical question 2}}

---

## 🔗 Related Notes

### Prerequisites
- [[{{Prerequisite Topic 1}}]]
- [[{{Prerequisite Topic 2}}]]

### Related Topics
- [[{{Related Topic 1}}]]
- [[{{Related Topic 2}}]]

### Next Steps
- [[{{Follow-up Topic 1}}]]
- [[{{Follow-up Topic 2}}]]

---

## 📖 References & Sources

1. {{Source 1}}
2. {{Source 2}}
3. {{Source 3}}

---

## 📝 Study Notes

{{Space for personal notes, insights, questions}}

---

*Last updated: `= this.updated`*  
*Domain: `= this.domain` | Subject: `= this.subject` | Difficulty: `= this.learning_data.difficulty`*
```

---

## 🎯 How to Use This Template

### Step 1: Fill in Frontmatter
- Set domain (TCM, Biology, etc.)
- Define learning objectives
- Add assessment seeds (flashcard/quiz questions)
- Include presentation outline

### Step 2: Write Comprehensive Content
- **Overview** - Context and importance
- **Core Concepts** - Definitions and key ideas
- **Detailed Explanation** - In-depth coverage
- **Applications** - Real-world examples
- **Comparisons** - Distinguish similar concepts

### Step 3: Add Learning Aids
- Mnemonics and memory devices
- Analogies and visual aids
- Self-check questions
- Common misconceptions

### Step 4: Generate Materials
Run generation scripts:
```bash
# Generate flashcards
python scripts/generate_flashcards_from_root.py "Root Note Name"

# Generate quiz
python scripts/generate_quiz_from_root.py "Root Note Name"

# Generate slides
python scripts/generate_slides_from_root.py "Root Note Name"
```

---

## 💡 Best Practices

### Content Quality
- **Comprehensive** - Cover all essential aspects
- **Clear** - Use precise language
- **Structured** - Logical flow from basic to advanced
- **Testable** - Include facts that can be assessed

### Assessment Seeds
- **Variety** - Mix easy/medium/hard questions
- **Bloom Levels** - Cover Remember → Analyze
- **Realistic** - Use clinical/applied scenarios
- **Distractors** - Make wrong answers plausible

### Memory Aids
- **Mnemonics** - For lists and sequences
- **Analogies** - For complex concepts
- **Visuals** - For spatial/relational info
- **Stories** - For processes and mechanisms

### Cross-Linking
- **Prerequisites** - What to study first
- **Related** - Parallel topics
- **Leads To** - What comes next
- **Comparisons** - Similar/contrasting concepts

---

## 🔄 Workflow Integration

```
Research/Source Material
         ↓
   Extract Key Info
         ↓
   Fill Root Note Template
         ↓
   Review & Enhance
         ↓
   ┌──────┴──────┬──────────┬──────────┐
   ↓             ↓          ↓          ↓
Flashcards    Quizzes   Slides    Study Guide
   ↓             ↓          ↓          ↓
   └──────┬──────┴──────────┴──────────┘
          ↓
    OCDS Class Package
```

---

## 📚 Related Documentation

- **Flashcard Template:** `Flashcard_Template.md`
- **Quiz Template:** `Quiz_Template.md`
- **Slides Template:** `Slides_Template.md`
- **Study Material Template:** `Study_Material_Template.md`

---

**Create comprehensive root notes for automated material generation! 📘**

---

*Last updated: 2025-11-07*  
*OCDS Version: 1.0.0*
