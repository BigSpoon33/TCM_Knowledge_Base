# Flashcard Template

**Complete template for creating Spaced Repetition flashcards**

---

## 📚 Overview

Flashcards in OCDS use the Obsidian Spaced Repetition plugin format. They enable:
- Active recall practice
- Spaced repetition scheduling
- Progress tracking
- Topic-based review

**Format:** Multi-line flashcard format with context headers

---

## 📋 Complete Template

```markdown
---
# OCDS Metadata
type: flashcards
class_id: "{{CLASS_ID}}"
topic: "{{TOPIC_NAME}}"
category: "{{CATEGORY}}"
total_cards: {{CARD_COUNT}}
difficulty: "{{easy|medium|hard|mixed}}"

# Tags
tags:
  - flashcards
  - {{CLASS_ID}}
  - {{TOPIC_TAG}}

# Metadata
created: {{YYYY-MM-DD}}
updated: {{YYYY-MM-DD}}
---

# {{TOPIC_NAME}} Flashcards

**{{CLASS_NAME}}**  
**Total Cards:** {{CARD_COUNT}}

---

# {{CONTEXT_HEADER}}
## {{QUESTION}}
?
{{ANSWER}}
<!--SR:!2025-11-10,3,250-->

---

# {{CONTEXT_HEADER}}
## {{QUESTION}}
?
{{ANSWER}}
<!--SR:!2025-11-10,3,250-->

<!-- Repeat for all flashcards -->
```
>Might have to keep everything int he frontmatter that isn't a flashcard or spaced repetition may think the topicname classname totalcards part is a flashcard.
---

## 📝 Filled Example

```markdown
---
# OCDS Metadata
type: flashcards
class_id: "TCM_101"
topic: "Qi Deficiency Pattern"
category: "patterns"
total_cards: 20
difficulty: "mixed"

# Tags
tags:
  - flashcards
  - tcm_101
  - patterns
  - qi_deficiency

# Metadata
created: 2025-11-01
updated: 2025-11-05
---

# Qi Deficiency Pattern Flashcards

**TCM 101 - Fundamentals**  
**Total Cards:** 20

---

# Qi Deficiency Pattern
## What is the primary tongue presentation?
?
**Pale, swollen with tooth marks**

**Explanation:**
- Pale indicates Qi/Blood Deficiency
- Swollen indicates Spleen Qi Deficiency
- Tooth marks from fluid retention
<!--SR:!2025-11-10,3,250-->

---

# Qi Deficiency Pattern
## What are the four cardinal symptoms?
?
1. **Fatigue and weakness**
2. **Shortness of breath**
3. **Spontaneous sweating**
4. **Pale complexion**

**Mnemonic:** FAST (Fatigue, Appetite, Sweating, Tongue)
<!--SR:!2025-11-10,3,250-->

---

# Qi Deficiency Pattern
## What is the pulse presentation?
?
**Weak (无力, Wú Lì)**

**Characteristics:**
- Lacks force
- Easily compressed
- May be deep or superficial
- Especially weak in Guan position
<!--SR:!2025-11-10,3,250-->

---

# Qi Deficiency Pattern - Etiology
## What are the primary causes?
?
1. **Constitutional weakness** - Inherited
2. **Dietary irregularities** - Poor nutrition
3. **Chronic illness** - Depletes Qi
4. **Overwork and stress** - Exhausts Qi

**Key:** Multiple factors often combine
<!--SR:!2025-11-10,3,250-->

---

# Qi Deficiency vs Yang Deficiency
## What is the key difference?
?
**Yang Deficiency has COLD signs**

**Qi Deficiency:**
- Fatigue, weak voice
- NO cold signs

**Yang Deficiency:**
- Fatigue, weak voice
- PLUS cold limbs, aversion to cold

**Remember:** Yang Def = Qi Def + Cold
<!--SR:!2025-11-10,3,250-->

---

# Si Jun Zi Tang (Four Gentlemen)
## What is the composition?
?
**Chief (君):**
- Ren Shen 9g - Tonify Qi

**Deputy (臣):**
- Bai Zhu 9g - Strengthen Spleen

**Assistant (佐):**
- Fu Ling 9g - Drain Dampness

**Envoy (使):**
- Zhi Gan Cao 6g - Harmonize

**Action:** Tonify Spleen Qi
<!--SR:!2025-11-10,3,250-->

---

# Qi Deficiency Pattern
## What type of sweating is characteristic?
?
**Spontaneous sweating during the day**

**Why:**
- Qi fails to secure the exterior
- Pores not properly closed
- Worse with slight exertion

**Differentiate from:**
- Night sweats (Yin Deficiency)
- No sweating (Yang Deficiency)
<!--SR:!2025-11-10,3,250-->

---

# Qi Deficiency Pattern
## What is the treatment principle?
?
**Tonify Qi and Strengthen the Spleen**

**Methods:**
- Use Qi-tonifying herbs
- Strengthen digestive function
- Support transformation/transportation
- Avoid draining/clearing methods

**Foundation formula:** Si Jun Zi Tang
<!--SR:!2025-11-10,3,250-->

---

# Qi Deficiency Pattern
## Can it progress to other patterns?
?
**Yes, commonly progresses to:**

1. **Blood Deficiency** - Qi fails to produce Blood
2. **Yang Deficiency** - Qi Def + Cold
3. **Qi Sinking** - Qi too weak to hold up
4. **Qi Stagnation** - Weak Qi can stagnate

**Key:** Early treatment prevents progression
<!--SR:!2025-11-10,3,250-->

---

# Qi Deficiency Pattern
## Which organ is most commonly affected?
?
**Spleen**

**Why:**
- Spleen governs transformation/transportation
- Source of Post-Heaven Qi
- Produces Qi and Blood
- Most affected by diet/lifestyle

**Also common:** Lung, Heart, Kidney
<!--SR:!2025-11-10,3,250-->

---

# Qi Deficiency Pattern - Clinical
## A patient has fatigue, poor appetite, loose stools, pale swollen tongue. Which formula?
?
**Si Jun Zi Tang (Four Gentlemen Decoction)**

**Reasoning:**
- Fatigue = Qi Deficiency
- Poor appetite + loose stools = Spleen
- Pale swollen tongue = Spleen Qi Def
- Si Jun Zi Tang is foundation for Spleen Qi Def

**If also phlegm:** Add Chen Pi + Ban Xia (= Liu Jun Zi Tang)
<!--SR:!2025-11-10,3,250-->

---

# Qi Deficiency Pattern - Diagnosis
## What is the most reliable diagnostic indicator?
?
**Weak pulse**

**Why:**
- Pulse directly reflects Qi strength
- Most objective finding
- Present in all Qi Deficiency cases
- Tongue may be normal in mild cases

**Location:** Especially weak in Guan (Spleen)
<!--SR:!2025-11-10,3,250-->

---

# Qi Deficiency Pattern
## What dietary recommendations?
?
**Warm, cooked, easily digestible foods**

**Recommended:**
- Cooked grains (rice, oats)
- Root vegetables
- Soups and stews
- Small frequent meals

**Avoid:**
- Cold/raw foods
- Excessive sweets
- Irregular eating
- Overeating

**Why:** Support Spleen transformation
<!--SR:!2025-11-10,3,250-->

---

# Qi Deficiency Pattern
## What lifestyle modifications?
?
**Rest, regular routine, gentle exercise**

**Recommendations:**
1. **Adequate sleep** - 7-8 hours
2. **Regular meals** - Same time daily
3. **Gentle exercise** - Tai Chi, walking
4. **Stress management** - Meditation, rest
5. **Avoid overwork** - Balance activity/rest

**Key:** Build Qi gradually, don't deplete further
<!--SR:!2025-11-10,3,250-->

---

# Qi Deficiency - Advanced
## How does Spleen Qi Deficiency differ from Lung Qi Deficiency?
?
**Spleen Qi Deficiency:**
- Poor appetite
- Loose stools
- Abdominal distension
- Weak limbs

**Lung Qi Deficiency:**
- Shortness of breath (prominent)
- Weak voice
- Cough with thin sputum
- Susceptible to colds

**Both have:** Fatigue, spontaneous sweating, pale tongue, weak pulse
<!--SR:!2025-11-10,3,250-->

---

# Qi Deficiency - Theory
## What does "Qi is the commander of Blood" mean?
?
**Qi has four relationships with Blood:**

1. **Generates Blood** - Qi produces Blood
2. **Moves Blood** - Qi circulates Blood
3. **Holds Blood** - Qi keeps Blood in vessels
4. **Warms Blood** - Qi provides warmth

**Clinical significance:**
- Qi Def → Blood Def (fails to generate)
- Qi Def → Bleeding (fails to hold)
- Qi Def → Blood Stasis (fails to move)
<!--SR:!2025-11-10,3,250-->

---

# Qi Deficiency - Clinical Pearl
## What is a common modern presentation?
?
**Chronic Fatigue Syndrome**

**Typical presentation:**
- Persistent fatigue >6 months
- Post-exertional malaise
- Unrefreshing sleep
- Cognitive difficulties
- Often Spleen + Kidney Qi Deficiency

**Treatment approach:**
- Tonify Spleen and Kidney Qi
- Bu Zhong Yi Qi Tang or modifications
- Lifestyle modifications essential
- Gradual improvement over months
<!--SR:!2025-11-10,3,250-->

---

# Qi Deficiency - Mnemonic
## What does the FAST mnemonic stand for?
?
**F** - Fatigue and weakness  
**A** - Appetite poor (Spleen)  
**S** - Sweating spontaneously  
**T** - Tongue pale and swollen

**Use:** Quick recall of cardinal symptoms

**Additional memory aid:**
- Pale = Deficiency
- Weak = Qi Deficiency
- Spontaneous sweating = Day (vs night sweats = Yin Def)
<!--SR:!2025-11-10,3,250-->

---

# Qi Deficiency - Exam Question
## A patient presents with fatigue, prolapse of organs, and bearing-down sensation. Which formula?
?
**Bu Zhong Yi Qi Tang (Tonify the Middle and Augment the Qi Decoction)**

**Reasoning:**
- Fatigue = Qi Deficiency
- Prolapse = Qi Sinking
- Bearing-down = Qi fails to hold up
- Bu Zhong Yi Qi Tang treats Spleen Qi Def with sinking

**Differentiate from:**
- Si Jun Zi Tang (no sinking)
- Liu Jun Zi Tang (with phlegm, no sinking)
<!--SR:!2025-11-10,3,250-->

---

# Qi Deficiency - Integration
## How does Qi Deficiency relate to modern medicine?
?
**Possible correlations:**

**Conditions:**
- Chronic Fatigue Syndrome
- Anemia (with Blood Def)
- Hypothyroidism (with Yang Def)
- Adrenal fatigue
- Post-viral syndrome

**Lab findings may show:**
- Low hemoglobin (if Blood Def)
- Low thyroid (if Yang Def)
- Normal labs (functional issue)

**Key:** TCM treats pattern, not just disease
<!--SR:!2025-11-10,3,250-->
```

---

## 💡 Best Practices

### Card Design
- **One concept per card** - Keep focused
- **Context header** - Identify topic
- **Clear question** - No ambiguity
- **Complete answer** - Include explanation
- **Memory aids** - Mnemonics, associations

### Difficulty Levels
- **Easy cards:** Basic recall (30%)
- **Medium cards:** Application (50%)
- **Hard cards:** Clinical reasoning (20%)

### Answer Format
- **Bold key points** - Highlight important info
- **Bullet lists** - Organize information
- **Explanations** - Why, not just what
- **Differentiations** - Compare/contrast

### Review Strategy
- **Daily review** - 20-30 cards
- **Topic-based** - Focus on current week
- **Mixed review** - Combine topics weekly
- **Honest ratings** - Accurate scheduling

---

## 📚 Related Documentation

- **Spaced Repetition Guide:** `../02_Plugin_Integration/Spaced_Repetition_Guide.md`
- **Study Material Template:** `Study_Material_Template.md`
- **Quiz Template:** `Quiz_Template.md`

---

**Create effective flashcards for active recall! 🎴**

---

*Last updated: 2025-11-05*  
*OCDS Version: 1.0.0*
