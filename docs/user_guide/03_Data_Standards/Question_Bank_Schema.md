# Question Bank Schema

**Complete specification for quiz question banks**

---

## 📚 Overview

Question banks store pools of quiz questions organized by topic. They enable:
- Random quiz generation
- Question reuse across classes
- Difficulty balancing
- Topic-based filtering
- Version control

**Location:** `Materials/Question_Banks/{CATEGORY}/{TOPIC}.yaml`

---

## 📋 Complete Schema

```yaml
# ===========================================
# QUESTION BANK SCHEMA v1.0
# ===========================================

# ============ METADATA ============

topic: string                 # Topic name
category: string              # Category (patterns, herbs, formulas, points)
difficulty: string            # easy | medium | hard | mixed
version: string               # Version number
author: string                # Creator
created_date: YYYY-MM-DD
updated_date: YYYY-MM-DD
tags: array                   # Categorization tags

# ============ QUESTIONS ============

questions:
  - id: string                # Unique question ID
    type: string              # multiple_choice (only type for now)
    difficulty: string        # easy | medium | hard
    question: string          # Question text
    options: array            # Answer choices (4-5 options)
      - string
      - string
      - string
      - string
    correct: integer          # Index of correct answer (0-based)
    explanation: string       # Why answer is correct
    tags: array               # For filtering/grouping
    related_material: string  # Link to study material
    points: integer           # Point value (default: 1)
```

---

## 📝 Complete Example

```yaml
# ===========================================
# Qi Deficiency Pattern Questions
# ===========================================

# Metadata
topic: "Qi Deficiency Pattern"
category: "patterns"
difficulty: "mixed"
version: "1.0.0"
author: "Dr. Jane Smith"
created_date: 2025-11-01
updated_date: 2025-11-05
tags:
  - patterns
  - qi
  - deficiency
  - fundamentals

# Questions
questions:
  # ============ EASY QUESTIONS ============
  
  - id: "qd_001"
    type: "multiple_choice"
    difficulty: "easy"
    question: "What is the primary tongue presentation for Qi Deficiency?"
    options:
      - "Pale, swollen with tooth marks"
      - "Red with yellow coating"
      - "Purple with dark spots"
      - "Normal pink"
    correct: 0
    explanation: "Qi Deficiency typically shows a pale, swollen tongue with tooth marks due to Spleen Qi Deficiency affecting fluid metabolism."
    tags: ["tongue_diagnosis", "qi_deficiency", "spleen"]
    related_material: "[[Qi Deficiency Pattern]]"
    points: 1
  
  - id: "qd_002"
    type: "multiple_choice"
    difficulty: "easy"
    question: "Which of the following is a cardinal symptom of Qi Deficiency?"
    options:
      - "Thirst with desire for cold drinks"
      - "Fatigue and weakness"
      - "Night sweats"
      - "Dry stools"
    correct: 1
    explanation: "Fatigue and weakness are cardinal symptoms of Qi Deficiency, reflecting insufficient Qi to support normal activities."
    tags: ["symptoms", "qi_deficiency", "cardinal"]
    related_material: "[[Qi Deficiency Pattern]]"
    points: 1
  
  - id: "qd_003"
    type: "multiple_choice"
    difficulty: "easy"
    question: "What is the pulse presentation typically seen in Qi Deficiency?"
    options:
      - "Wiry and rapid"
      - "Slippery and full"
      - "Weak and empty"
      - "Choppy and irregular"
    correct: 2
    explanation: "Weak and empty pulse indicates Qi Deficiency, showing insufficient Qi to fill the vessels."
    tags: ["pulse_diagnosis", "qi_deficiency"]
    related_material: "[[Qi Deficiency Pattern]]"
    points: 1
  
  # ============ MEDIUM QUESTIONS ============
  
  - id: "qd_004"
    type: "multiple_choice"
    difficulty: "medium"
    question: "Which formula is the foundational treatment for Spleen Qi Deficiency?"
    options:
      - "Liu Jun Zi Tang"
      - "Si Jun Zi Tang"
      - "Bu Zhong Yi Qi Tang"
      - "Gui Pi Tang"
    correct: 1
    explanation: "Si Jun Zi Tang (Four Gentlemen Decoction) is the foundational formula for Spleen Qi Deficiency. Liu Jun Zi Tang adds Chen Pi and Ban Xia for phlegm."
    tags: ["formulas", "qi_deficiency", "spleen", "treatment"]
    related_material: "[[Si Jun Zi Tang]]"
    points: 1
  
  - id: "qd_005"
    type: "multiple_choice"
    difficulty: "medium"
    question: "What is the primary etiology of Qi Deficiency?"
    options:
      - "External pathogenic factors"
      - "Emotional stress and overwork"
      - "Dietary irregularities and constitutional weakness"
      - "Trauma and injury"
    correct: 2
    explanation: "Dietary irregularities and constitutional weakness are primary causes of Qi Deficiency. Overwork and chronic illness can also contribute."
    tags: ["etiology", "qi_deficiency", "causes"]
    related_material: "[[Qi Deficiency Pattern]]"
    points: 1
  
  - id: "qd_006"
    type: "multiple_choice"
    difficulty: "medium"
    question: "Which organ is most commonly affected in Qi Deficiency patterns?"
    options:
      - "Liver"
      - "Heart"
      - "Spleen"
      - "Kidney"
    correct: 2
    explanation: "The Spleen is the primary organ affected in Qi Deficiency patterns, as it governs transformation and transportation of Qi."
    tags: ["organs", "qi_deficiency", "spleen"]
    related_material: "[[Spleen Qi Deficiency]]"
    points: 1
  
  # ============ HARD QUESTIONS ============
  
  - id: "qd_007"
    type: "multiple_choice"
    difficulty: "hard"
    question: "A patient presents with fatigue, poor appetite, loose stools, and a pale swollen tongue. They also have prolapse of organs. Which formula is most appropriate?"
    options:
      - "Si Jun Zi Tang"
      - "Liu Jun Zi Tang"
      - "Bu Zhong Yi Qi Tang"
      - "Gui Pi Tang"
    correct: 2
    explanation: "Bu Zhong Yi Qi Tang is indicated for Spleen Qi Deficiency with sinking Qi, manifesting as prolapse. Si Jun Zi Tang treats basic Spleen Qi Deficiency without sinking."
    tags: ["formulas", "differential_diagnosis", "sinking_qi", "clinical_application"]
    related_material: "[[Bu Zhong Yi Qi Tang]]"
    points: 2
  
  - id: "qd_008"
    type: "multiple_choice"
    difficulty: "hard"
    question: "How does Spleen Qi Deficiency differ from Lung Qi Deficiency in terms of sweating?"
    options:
      - "Spleen: spontaneous sweating; Lung: spontaneous sweating"
      - "Spleen: night sweats; Lung: spontaneous sweating"
      - "Spleen: no sweating; Lung: spontaneous sweating"
      - "Spleen: spontaneous sweating; Lung: no sweating"
    correct: 0
    explanation: "Both Spleen and Lung Qi Deficiency can present with spontaneous sweating. The key difference is that Lung Qi Deficiency includes shortness of breath and weak voice, while Spleen includes digestive symptoms."
    tags: ["differential_diagnosis", "spleen", "lung", "symptoms"]
    related_material: "[[Spleen Qi Deficiency]], [[Lung Qi Deficiency]]"
    points: 2
  
  - id: "qd_009"
    type: "multiple_choice"
    difficulty: "hard"
    question: "A patient with Qi Deficiency also presents with Blood Deficiency symptoms. Which herb pair would address both patterns?"
    options:
      - "Ren Shen + Huang Qi"
      - "Ren Shen + Dang Gui"
      - "Huang Qi + Bai Zhu"
      - "Dang Gui + Bai Shao"
    correct: 1
    explanation: "Ren Shen tonifies Qi while Dang Gui nourishes Blood, addressing both deficiencies. This combination is found in Ba Zhen Tang (Eight Treasure Decoction)."
    tags: ["herbs", "qi_deficiency", "blood_deficiency", "herb_pairs"]
    related_material: "[[Ba Zhen Tang]]"
    points: 2
  
  - id: "qd_010"
    type: "multiple_choice"
    difficulty: "hard"
    question: "In the progression of Qi Deficiency, which pattern is most likely to develop next if untreated?"
    options:
      - "Qi Stagnation"
      - "Blood Deficiency"
      - "Yin Deficiency"
      - "Phlegm accumulation"
    correct: 1
    explanation: "Qi Deficiency often progresses to Blood Deficiency because Qi is needed to produce Blood. The saying 'Qi is the commander of Blood' reflects this relationship."
    tags: ["pattern_progression", "qi_deficiency", "blood_deficiency", "theory"]
    related_material: "[[Qi and Blood Relationship]]"
    points: 2
```
> would be nice to have the answers or options be dynamic somehow? or maybe setting all of the options staticly is better, maybe not idk. random answers with the one correct is kind of cooler in a way
---

## 🎯 Question Writing Guidelines

### Question Structure

**Clear and concise:**
```yaml
question: "What is the primary tongue presentation for Qi Deficiency?"
```

**Not ambiguous:**
```yaml
# ❌ Bad
question: "What might you see in Qi Deficiency?"

# ✅ Good
question: "What is the primary tongue presentation for Qi Deficiency?"
```

---

### Answer Options

**4 options (standard):**
```yaml
options:
  - "Option A"
  - "Option B"
  - "Option C"
  - "Option D"
```

**5 options (harder):**
```yaml
options:
  - "Option A"
  - "Option B"
  - "Option C"
  - "Option D"
  - "Option E"
```

**Rules:**
- One clearly correct answer
- Plausible distractors (wrong but reasonable)
- Similar length and format
- No "all of the above" or "none of the above"

---

### Difficulty Levels

**Easy (30% of questions):**
- Recall facts
- Basic definitions
- Simple identification
- Memorization

**Example:**
```yaml
difficulty: "easy"
question: "What is the primary tongue presentation for Qi Deficiency?"
```

**Medium (50% of questions):**
- Apply knowledge
- Compare/contrast
- Analyze relationships
- Understand concepts

**Example:**
```yaml
difficulty: "medium"
question: "Which formula is the foundational treatment for Spleen Qi Deficiency?"
```

**Hard (20% of questions):**
- Clinical application
- Differential diagnosis
- Complex reasoning
- Integration of concepts

**Example:**
```yaml
difficulty: "hard"
question: "A patient presents with fatigue, poor appetite, loose stools, and prolapse. Which formula is most appropriate?"
```

---

### Explanations

**Good explanation:**
```yaml
explanation: "Si Jun Zi Tang (Four Gentlemen Decoction) is the foundational formula for Spleen Qi Deficiency. Liu Jun Zi Tang adds Chen Pi and Ban Xia for phlegm."
```

**Include:**
- Why answer is correct
- Why others are wrong (if helpful)
- Additional context
- Related concepts

---

## 🔄 Quiz Generation

### Random Selection

```python
def generate_quiz(question_bank, count=10, difficulty_mix=None):
    """Generate quiz from question bank."""
    
    if difficulty_mix is None:
        # Default mix: 30% easy, 50% medium, 20% hard
        difficulty_mix = {
            'easy': 0.3,
            'medium': 0.5,
            'hard': 0.2
        }
    
    questions = []
    
    # Calculate counts per difficulty
    easy_count = int(count * difficulty_mix['easy'])
    medium_count = int(count * difficulty_mix['medium'])
    hard_count = count - easy_count - medium_count
    
    # Get questions by difficulty
    easy_q = [q for q in question_bank['questions'] if q['difficulty'] == 'easy']
    medium_q = [q for q in question_bank['questions'] if q['difficulty'] == 'medium']
    hard_q = [q for q in question_bank['questions'] if q['difficulty'] == 'hard']
    
    # Random selection
    questions.extend(random.sample(easy_q, min(easy_count, len(easy_q))))
    questions.extend(random.sample(medium_q, min(medium_count, len(medium_q))))
    questions.extend(random.sample(hard_q, min(hard_count, len(hard_q))))
    
    # Shuffle
    random.shuffle(questions)
    
    return questions
```

---

### Topic-Based Selection

```python
def generate_quiz_by_topic(question_banks, topics, count=10):
    """Generate quiz from multiple topics."""
    
    questions = []
    per_topic = count // len(topics)
    
    for topic in topics:
        bank = question_banks[topic]
        topic_questions = random.sample(bank['questions'], per_topic)
        questions.extend(topic_questions)
    
    # Fill remaining with random
    remaining = count - len(questions)
    if remaining > 0:
        all_questions = [q for bank in question_banks.values() for q in bank['questions']]
        questions.extend(random.sample(all_questions, remaining))
    
    random.shuffle(questions)
    return questions
```

---

### Tag-Based Selection

```python
def generate_quiz_by_tags(question_bank, tags, count=10):
    """Generate quiz filtered by tags."""
    
    # Filter questions by tags
    filtered = [
        q for q in question_bank['questions']
        if any(tag in q['tags'] for tag in tags)
    ]
    
    # Random selection
    if len(filtered) >= count:
        return random.sample(filtered, count)
    else:
        return filtered
```
>the quiz generation is going to be a really cool feature when there is a way to make a random quiz of x questions from x question banks. this is where we get to use material in more classes than one. so we can have all of the herb material distributed in a glob or piece by piece through classes.
---

## 📊 Question Bank Statistics

### Analyze Bank

```python
def analyze_question_bank(bank):
    """Analyze question bank statistics."""
    
    questions = bank['questions']
    total = len(questions)
    
    # Count by difficulty
    easy = sum(1 for q in questions if q['difficulty'] == 'easy')
    medium = sum(1 for q in questions if q['difficulty'] == 'medium')
    hard = sum(1 for q in questions if q['difficulty'] == 'hard')
    
    # Count by tags
    tag_counts = {}
    for q in questions:
        for tag in q['tags']:
            tag_counts[tag] = tag_counts.get(tag, 0) + 1
    
    return {
        'total_questions': total,
        'easy': easy,
        'medium': medium,
        'hard': hard,
        'easy_pct': (easy / total) * 100,
        'medium_pct': (medium / total) * 100,
        'hard_pct': (hard / total) * 100,
        'tag_counts': tag_counts
    }
```

---

## ✅ Validation Rules

```python
def validate_question_bank(bank):
    """Validate question bank structure."""
    
    # Check required metadata
    required_meta = ['topic', 'category', 'difficulty', 'version']
    for field in required_meta:
        if field not in bank:
            raise ValueError(f"Missing required field: {field}")
    
    # Check questions exist
    if 'questions' not in bank or not bank['questions']:
        raise ValueError("Question bank must have at least one question")
    
    # Validate each question
    for i, q in enumerate(bank['questions']):
        # Required fields
        required_q = ['id', 'type', 'difficulty', 'question', 'options', 'correct', 'explanation']
        for field in required_q:
            if field not in q:
                raise ValueError(f"Question {i}: Missing required field: {field}")
        
        # Check options count
        if len(q['options']) < 4:
            raise ValueError(f"Question {i}: Must have at least 4 options")
        
        # Check correct index
        if q['correct'] < 0 or q['correct'] >= len(q['options']):
            raise ValueError(f"Question {i}: Invalid correct index")
        
        # Check unique ID
        ids = [q['id'] for q in bank['questions']]
        if len(ids) != len(set(ids)):
            raise ValueError("Duplicate question IDs found")
    
    return True
```

---

## 💡 Best Practices

### Question Bank Size
- **Minimum:** 20 questions per topic
- **Recommended:** 50+ questions per topic
- **Ideal:** 100+ questions per topic

### Difficulty Distribution
- **Easy:** 30% (recall, basic facts)
- **Medium:** 50% (application, analysis)
- **Hard:** 20% (clinical, integration)

### Question Quality
- **Clear wording** - No ambiguity
- **One correct answer** - Definitively right
- **Plausible distractors** - Wrong but reasonable
- **Good explanations** - Learning opportunity
- **Relevant tags** - Easy filtering

### Maintenance
- **Review regularly** - Update outdated questions
- **Track performance** - Identify problematic questions
- **Add variety** - New questions regularly
- **Version control** - Track changes
> grading question difficulty would be a cool thing to have integrated so that quizzes can dynamically increase or decrease difficulty. could even work mid quiz to add or increase difficulty based on current score.
---

## 📚 Related Documentation

- **Quiz Template:** `../05_Material_Templates/Quiz_Template.md`
- **Auto-Grader:** `../07_Grading_System/Quiz_Grading.md`
- **Timeline Schema:** `Timeline_Schema.md`

---

**Build comprehensive question banks! 📝**

---

*Last updated: 2025-11-05*  
*OCDS Version: 1.0.0*
