# Study Material Template

**Complete template for creating study materials**

---

## 📚 Overview

Study materials are the primary learning content in OCDS. They provide:
- Topic introduction and overview
- Detailed explanations
- Examples and applications
- Visual aids
- Practice questions
- Links to related materials

**Format:** Markdown with standardized frontmatter

---

## 📋 Complete Template

```markdown
---
# OCDS Metadata
type: study
class_id: "{{CLASS_ID}}"
week: {{WEEK_NUMBER}}
day: {{DAY_NUMBER}}
topic: "{{TOPIC_NAME}}"

# Learning Configuration
estimated_minutes: {{READING_TIME}}
difficulty: "{{beginner|intermediate|advanced}}"
prerequisites: []
learning_objectives: []

# Related Materials
related_flashcards: "[[Flashcards_{{TOPIC}}]]"
related_quiz: "[[Quiz_{{TOPIC}}]]"
related_slides: "[[Slides_{{TOPIC}}]]"

# Tags
tags:
  - study
  - {{CLASS_ID}}
  - week_{{WEEK_NUMBER}}
  - {{TOPIC_TAG}}

# Metadata
created: {{YYYY-MM-DD}}
updated: {{YYYY-MM-DD}}
---

# {{TOPIC_NAME}}

**{{CLASS_NAME}} - Week {{WEEK_NUMBER}}, Day {{DAY_NUMBER}}**

> [!info] Study Information
> - **Estimated Time:** {{READING_TIME}} minutes
> - **Difficulty:** {{DIFFICULTY}}
> - **Prerequisites:** {{PREREQUISITES or "None"}}

---

## 📋 Learning Objectives

By the end of this lesson, you will be able to:

- [ ] Objective 1
- [ ] Objective 2
- [ ] Objective 3
- [ ] Objective 4

---

## 📖 Overview

Brief introduction to the topic (2-3 paragraphs):
- What is this topic?
- Why is it important?
- How does it fit into the bigger picture?

---

## 🎯 Main Content

### Section 1: {{SECTION_TITLE}}

Detailed explanation of first major concept.

**Key Points:**
- Point 1
- Point 2
- Point 3

**Example:**
> Concrete example illustrating the concept

**Clinical Application:**
How this applies in practice

---

### Section 2: {{SECTION_TITLE}}

Detailed explanation of second major concept.

**Key Points:**
- Point 1
- Point 2
- Point 3

**Example:**
> Concrete example illustrating the concept

---

### Section 3: {{SECTION_TITLE}}

Detailed explanation of third major concept.

**Key Points:**
- Point 1
- Point 2
- Point 3

---

## 🔍 Detailed Analysis

### Subsection A: {{SUBTOPIC}}

In-depth exploration of specific aspect.

**Important Considerations:**
- Consideration 1
- Consideration 2

**Common Mistakes:**
- Mistake 1 to avoid
- Mistake 2 to avoid

---

### Subsection B: {{SUBTOPIC}}

In-depth exploration of another aspect.

**Clinical Pearls:**
- Pearl 1
- Pearl 2

---

## 📊 Comparison & Differentiation

### Comparison Table

| Feature | {{ITEM_A}} | {{ITEM_B}} | {{ITEM_C}} |
|---------|-----------|-----------|-----------|
| Feature 1 | Description | Description | Description |
| Feature 2 | Description | Description | Description |
| Feature 3 | Description | Description | Description |

### Key Differences

**{{ITEM_A}} vs {{ITEM_B}}:**
- Main difference 1
- Main difference 2

**{{ITEM_B}} vs {{ITEM_C}}:**
- Main difference 1
- Main difference 2

---

## 💡 Practical Application

### Clinical Scenarios

**Scenario 1:**
Description of clinical situation and how to apply this knowledge.

**Scenario 2:**
Another practical example.

### Case Study

**Patient Presentation:**
Brief case description

**Analysis:**
How to apply the concepts learned

**Outcome:**
Result and learning points

---

## 🧠 Memory Aids

### Mnemonic

[Memory device for key information]

### Visual Summary

```
[ASCII diagram or description of visual aid]
```

### Key Associations

- Association 1
- Association 2
- Association 3

---

## ✅ Self-Assessment

### Check Your Understanding

1. **Question 1**
   - Answer: [Brief answer]

2. **Question 2**
   - Answer: [Brief answer]

3. **Question 3**
   - Answer: [Brief answer]

### Reflection Questions

- How does this relate to what you already know?
- What aspects need more study?
- How will you apply this clinically?

---

## 📚 Related Materials

### Required Reading
- [[Related Topic 1]]
- [[Related Topic 2]]

### Recommended Reading
- [[Advanced Topic 1]]
- [[Advanced Topic 2]]

### Visual Learning
- [[Slides_{{TOPIC}}]] - Presentation slides
- [[Diagram_{{TOPIC}}]] - Visual diagrams

### Practice
- [[Flashcards_{{TOPIC}}]] - Review flashcards
- [[Quiz_{{TOPIC}}]] - Test your knowledge
- [[Homework_{{TOPIC}}]] - Practice assignment

---

## 🔗 Cross-References

### Related Patterns/Concepts
\```dataview
LIST
FROM ""
WHERE type = "study"
  AND contains(tags, "{{RELATED_TAG}}")
  AND file.name != this.file.name
LIMIT 5
\```

### Related Formulas/Treatments
- [[Formula 1]]
- [[Formula 2]]

---

## 📖 Classical References

### Source Texts

**Primary Source:**
- Text name, chapter/page reference
- Key quote or concept

**Secondary Sources:**
- Additional references

### Modern Interpretation

How contemporary TCM understands this concept.

---

## 🎓 Study Tips

### How to Study This Material

1. **First Pass (20 min):** Skim headings and key points
2. **Second Pass (30 min):** Read thoroughly, take notes
3. **Third Pass (10 min):** Review memory aids and self-assessment

### Note-Taking Suggestions

- Create concept maps
- Summarize each section
- List questions for further study

### Active Learning Strategies

- Teach concept to someone else
- Create your own examples
- Apply to clinical scenarios

---

## ⏭️ Next Steps

### Immediate Actions
1. [ ] Review flashcards: [[Flashcards_{{TOPIC}}]]
2. [ ] Complete quiz: [[Quiz_{{TOPIC}}]]
3. [ ] Review slides: [[Slides_{{TOPIC}}]]

### Follow-Up Study
- [[Next Topic in Sequence]]
- [[Related Advanced Topic]]

### Homework
- [[Homework_{{TOPIC}}]] - Due {{DUE_DATE}}

---

## 📝 Notes Section

*Use this space for your personal notes and observations*

---

---

## 🔄 Revision History

- **{{DATE}}:** Initial creation
- **{{DATE}}:** Updated with additional examples
- **{{DATE}}:** Added clinical scenarios

---

*Study material for {{CLASS_NAME}}*  
*Week {{WEEK_NUMBER}}, Day {{DAY_NUMBER}}*
```

---

## 📝 Filled Example

```markdown
---
# OCDS Metadata
type: study
class_id: "TCM_101"
week: 1
day: 1
topic: "Qi Deficiency Pattern"

# Learning Configuration
estimated_minutes: 60
difficulty: "beginner"
prerequisites: []
learning_objectives:
  - "Identify cardinal symptoms of Qi Deficiency"
  - "Understand etiology and pathogenesis"
  - "Recognize tongue and pulse presentations"
  - "Select appropriate treatment principles"

# Related Materials
related_flashcards: "[[Flashcards_Qi_Deficiency]]"
related_quiz: "[[Quiz_Qi_Deficiency]]"
related_slides: "[[Slides_Qi_Deficiency]]"

# Tags
tags:
  - study
  - tcm_101
  - week_1
  - patterns
  - qi_deficiency

# Metadata
created: 2025-11-01
updated: 2025-11-05
---

# Qi Deficiency Pattern

**TCM 101 - Fundamentals - Week 1, Day 1**

> [!info] Study Information
> - **Estimated Time:** 60 minutes
> - **Difficulty:** Beginner
> - **Prerequisites:** None

---

## 📋 Learning Objectives

By the end of this lesson, you will be able to:

- [ ] Identify the cardinal symptoms of Qi Deficiency
- [ ] Understand the etiology and pathogenesis
- [ ] Recognize tongue and pulse presentations
- [ ] Select appropriate treatment principles
- [ ] Differentiate from similar patterns

---

## 📖 Overview

Qi Deficiency is one of the most fundamental patterns in Traditional Chinese Medicine. It represents a state where the body's vital energy (Qi) is insufficient to perform normal physiological functions. This pattern forms the foundation for understanding many other deficiency patterns and is commonly seen in clinical practice.

Understanding Qi Deficiency is essential because:
- It's one of the most common patterns in modern practice
- It serves as a foundation for more complex patterns
- Many chronic conditions involve some degree of Qi Deficiency
- Treatment principles for Qi Deficiency apply broadly

Qi Deficiency can affect any organ system, but most commonly involves the Spleen, Lung, Heart, and Kidney. This lesson focuses on the general pattern, with specific organ manifestations covered in later lessons.

---

## 🎯 Main Content

### Section 1: Definition and Concept

**What is Qi Deficiency?**

Qi Deficiency (气虚, Qì Xū) is a pattern characterized by insufficient Qi to perform normal physiological functions. The body lacks the vital energy needed for:
- Movement and activity
- Transformation and transportation
- Protection from external pathogens
- Holding organs and fluids in place
- Warming the body

**Key Points:**
- Qi is the vital energy that powers all bodily functions
- Deficiency means insufficient quantity or strength
- Results in hypofunction rather than dysfunction
- Can be constitutional or acquired

**Example:**
> Think of Qi like electricity in a house. When there's insufficient power (Qi Deficiency), lights are dim (pale complexion), appliances work slowly (fatigue), and the heating doesn't work well (cold limbs).

**Clinical Application:**
Qi Deficiency patterns require tonification rather than sedation. Treatment focuses on strengthening and building, not clearing or draining.

---

### Section 2: Etiology (Causes)

**Primary Causes of Qi Deficiency:**

1. **Constitutional Weakness**
   - Inherited weak constitution
   - Prenatal Qi deficiency
   - Congenital factors

2. **Dietary Irregularities**
   - Insufficient food intake
   - Poor quality nutrition
   - Irregular eating habits
   - Excessive consumption of cold/raw foods

3. **Chronic Illness**
   - Long-term disease depleting Qi
   - Repeated acute illnesses
   - Incomplete recovery

4. **Overwork and Stress**
   - Physical overexertion
   - Mental/emotional strain
   - Insufficient rest
   - Chronic stress

**Key Points:**
- Multiple factors often combine
- Lifestyle plays a major role
- Prevention is easier than treatment
- Early intervention is important

---

### Section 3: Pathogenesis (How It Develops)

**Development of Qi Deficiency:**

1. **Initial Stage:**
   - Mild fatigue after exertion
   - Quick recovery with rest
   - Subtle signs

2. **Progressive Stage:**
   - Persistent fatigue
   - Slower recovery
   - More obvious symptoms

3. **Advanced Stage:**
   - Severe weakness
   - Multiple organ involvement
   - Difficult to recover

**Transformation Patterns:**

Qi Deficiency can progress to:
- **Blood Deficiency** - Qi fails to produce Blood
- **Yang Deficiency** - Qi Deficiency with cold signs
- **Qi Sinking** - Qi too weak to hold organs up
- **Qi Stagnation** - Paradoxically, weak Qi can stagnate

---

## 🔍 Detailed Analysis

### Cardinal Symptoms

**Primary Manifestations:**

1. **Fatigue and Weakness**
   - Constant tiredness
   - Worse with exertion
   - Improved with rest
   - Lack of strength

2. **Shortness of Breath**
   - Especially on exertion
   - Shallow breathing
   - Reluctance to speak
   - Weak voice

3. **Spontaneous Sweating**
   - Sweating during the day
   - Worse with slight exertion
   - Not from heat
   - Indicates Qi failing to secure

4. **Pale Complexion**
   - Lack of luster
   - Pale or white face
   - May be slightly puffy
   - Indicates Qi failing to nourish

**Important Considerations:**
- Not all symptoms need to be present
- Severity varies by individual
- Organ-specific symptoms may predominate
- Pattern combinations are common

**Common Mistakes:**
- Confusing with Yang Deficiency (no cold signs in pure Qi Deficiency)
- Missing subtle early signs
- Not considering constitutional factors

---

### Tongue and Pulse Diagnosis

**Tongue Presentation:**
- **Body Color:** Pale
- **Shape:** Swollen, may have tooth marks
- **Coating:** Thin white
- **Moisture:** Normal to slightly moist

**Pulse Presentation:**
- **Quality:** Weak (无力, Wú Lì)
- **Depth:** May be deep or superficial
- **Rate:** Normal or slightly slow
- **Strength:** Lacks force, easily compressed
- **Location:** Especially weak in Guan (middle) position

**Clinical Pearls:**
- Pale, swollen tongue with tooth marks is classic
- Weak pulse is the most reliable indicator
- Pulse may be normal in mild cases
- Tongue coating remains thin (not thick)

---

## 📊 Comparison & Differentiation

### Comparison Table

| Feature | Qi Deficiency | Yang Deficiency | Blood Deficiency |
|---------|---------------|-----------------|------------------|
| Fatigue | Yes | Yes | Yes |
| Cold signs | No | Yes | Mild |
| Sweating | Spontaneous (day) | None or night | None |
| Tongue | Pale, swollen | Pale, wet | Pale, thin |
| Pulse | Weak | Weak, slow | Weak, thin |
| Voice | Weak | Weak | Normal |

### Key Differences

**Qi Deficiency vs Yang Deficiency:**
- Qi Def: No cold signs, normal temperature
- Yang Def: Cold limbs, aversion to cold, prefers warmth
- Yang Def is more severe (Qi + warmth deficiency)

**Qi Deficiency vs Blood Deficiency:**
- Qi Def: Fatigue, shortness of breath, spontaneous sweating
- Blood Def: Dizziness, palpitations, insomnia, dry skin
- Blood Def has more "dryness" symptoms

---

## 💡 Practical Application

### Clinical Scenarios

**Scenario 1: Office Worker**
35-year-old presents with constant fatigue, especially in afternoon. Works long hours, skips meals, pale face, weak voice. Tongue: pale and swollen. Pulse: weak.

**Analysis:** Classic Spleen Qi Deficiency from irregular diet and overwork.

**Treatment:** Tonify Spleen Qi with Si Jun Zi Tang, recommend regular meals, adequate rest.

**Scenario 2: Post-Illness**
50-year-old recovering from flu. Still tired 2 weeks later, shortness of breath on exertion, spontaneous sweating. Tongue: pale. Pulse: weak.

**Analysis:** Qi Deficiency from illness depleting Qi.

**Treatment:** Tonify Qi with Bu Zhong Yi Qi Tang, gradual return to activity.

### Case Study

**Patient Presentation:**
42-year-old female, chronic fatigue for 6 months, poor appetite, loose stools, pale complexion, weak voice, spontaneous sweating. Tongue: pale, swollen with tooth marks. Pulse: weak, especially in Guan position.

**Analysis:**
- Cardinal symptoms present: fatigue, shortness of breath, spontaneous sweating
- Digestive symptoms indicate Spleen involvement
- Tongue and pulse confirm Qi Deficiency
- No cold signs (not Yang Deficiency)
- Pattern: Spleen Qi Deficiency

**Treatment:**
- Formula: Si Jun Zi Tang (Four Gentlemen Decoction)
- Acupuncture: ST-36, SP-6, CV-12, CV-6
- Lifestyle: Regular meals, adequate rest, gentle exercise
- Diet: Warm, cooked foods; avoid cold/raw

**Outcome:**
After 4 weeks: Energy improved 60%, appetite better, stools formed. Continued treatment for 8 more weeks with full recovery.

---

## 🧠 Memory Aids

### Mnemonic for Cardinal Symptoms

**"FAST"**
- **F**atigue and weakness
- **A**ppetite poor (if Spleen involved)
- **S**weating spontaneously
- **T**ongue pale and swollen

### Visual Summary

```
QI DEFICIENCY PATTERN

Etiology → Pathogenesis → Manifestations
    ↓            ↓              ↓
 Diet/Work → Qi Depleted → Fatigue
 Illness  → Hypofunction → Weak Voice
 Stress   → Weak Pulse   → Pale Face
```

### Key Associations

- Pale = Deficiency
- Swollen tongue = Spleen Qi Deficiency
- Spontaneous sweating = Qi failing to secure
- Weak pulse = Qi Deficiency (most reliable)

---

## ✅ Self-Assessment

### Check Your Understanding

1. **What are the four cardinal symptoms of Qi Deficiency?**
   - Answer: Fatigue, shortness of breath, spontaneous sweating, pale complexion

2. **How does the pulse feel in Qi Deficiency?**
   - Answer: Weak, lacking force, easily compressed

3. **What is the primary difference between Qi and Yang Deficiency?**
   - Answer: Yang Deficiency has cold signs; Qi Deficiency does not

4. **What is the foundational formula for Spleen Qi Deficiency?**
   - Answer: Si Jun Zi Tang (Four Gentlemen Decoction)

5. **Can Qi Deficiency progress to other patterns?**
   - Answer: Yes, commonly to Blood Deficiency or Yang Deficiency

### Reflection Questions

- How does this pattern relate to modern lifestyle factors?
- What preventive measures would you recommend?
- How would you explain this to a patient?

---

## 📚 Related Materials

### Required Reading
- [[Spleen Qi Deficiency]]
- [[Lung Qi Deficiency]]
- [[Si Jun Zi Tang]]

### Recommended Reading
- [[Qi and Blood Relationship]]
- [[Eight Principles - Deficiency]]
- [[Constitutional Patterns]]

### Visual Learning
- [[Slides_Qi_Deficiency]] - Presentation slides
- [[Tongue_Diagnosis_Atlas]] - Visual reference

### Practice
- [[Flashcards_Qi_Deficiency]] - 20 review cards
- [[Quiz_Qi_Deficiency]] - 10 question quiz
- [[Homework_Week_1]] - Pattern differentiation practice

---

## 🔗 Cross-References

### Related Patterns
- [[Blood Deficiency Pattern]]
- [[Yang Deficiency Pattern]]
- [[Spleen Qi Deficiency]]
- [[Lung Qi Deficiency]]

### Related Formulas
- [[Si Jun Zi Tang]] - Foundation formula
- [[Bu Zhong Yi Qi Tang]] - For sinking Qi
- [[Liu Jun Zi Tang]] - With phlegm

---

## 📖 Classical References

### Source Texts

**Primary Source:**
- *Huangdi Neijing* (Yellow Emperor's Classic)
- "When Qi is deficient, there is weakness and fatigue"

**Secondary Sources:**
- *Zhongyi Zhenduan Xue* (TCM Diagnostics)
- *Zhongyi Neike Xue* (TCM Internal Medicine)

### Modern Interpretation

Contemporary TCM recognizes Qi Deficiency as increasingly common due to modern lifestyle factors: poor diet, stress, overwork, and insufficient rest. Treatment emphasizes both herbal medicine and lifestyle modification.

---

## 🎓 Study Tips

### How to Study This Material

1. **First Pass (20 min):** Read overview and cardinal symptoms
2. **Second Pass (30 min):** Study etiology, pathogenesis, and differentiation
3. **Third Pass (10 min):** Review memory aids and self-assessment

### Note-Taking Suggestions

- Create a concept map linking causes → symptoms → treatment
- Make comparison charts for similar patterns
- List clinical pearls in your own words

### Active Learning Strategies

- Explain the pattern to a study partner
- Create your own clinical scenarios
- Practice tongue and pulse diagnosis
- Apply to real or hypothetical cases

---

## ⏭️ Next Steps

### Immediate Actions
1. [ ] Review flashcards: [[Flashcards_Qi_Deficiency]]
2. [ ] Complete quiz: [[Quiz_Qi_Deficiency]]
3. [ ] Watch slides: [[Slides_Qi_Deficiency]]

### Follow-Up Study
- [[Spleen Qi Deficiency]] - Tomorrow's topic
- [[Blood Deficiency Pattern]] - Week 2

### Homework
- [[Homework_Week_1]] - Pattern differentiation practice
- Due: End of Week 1

---

## 📝 Notes Section

*Use this space for your personal notes and observations*

---

---

## 🔄 Revision History

- **2025-11-01:** Initial creation
- **2025-11-03:** Added clinical scenarios
- **2025-11-05:** Updated with additional examples

---

*Study material for TCM 101 - Fundamentals*  
*Week 1, Day 1*
```

---

## 💡 Best Practices

### Content Structure
- **Clear hierarchy** - Use headings effectively
- **Logical flow** - Build from simple to complex
- **Consistent format** - Same structure across materials
- **Visual breaks** - Don't overwhelm with text

### Writing Style
- **Clear and concise** - Avoid unnecessary jargon
- **Active voice** - More engaging
- **Examples** - Concrete illustrations
- **Clinical focus** - Practical application

### Learning Design
- **Objectives first** - Set expectations
- **Multiple formats** - Text, tables, examples
- **Self-assessment** - Check understanding
- **Next steps** - Guide continued learning

### Integration
- **Link related materials** - Flashcards, quizzes, slides
- **Cross-reference** - Related topics
- **Build on previous** - Connect to prior knowledge
- **Preview next** - Prepare for upcoming content
> Just had a cool idea that the lecture could have a template for the note that basically guides the student with 5 questions they should try to answer during class. that way they're engaged and looking for the key words that would come from the speaker notes in the slides or something.
---

## 📚 Related Documentation

- **Quiz Template:** `Quiz_Template.md`
- **Flashcard Template:** `Flashcard_Template.md`
- **Slide Deck Template:** `Slide_Deck_Template.md`
- **Timeline Schema:** `../03_Data_Standards/Timeline_Schema.md`

---

**Create effective study materials! 📖**

---

*Last updated: 2025-11-05*  
*OCDS Version: 1.0.0*
