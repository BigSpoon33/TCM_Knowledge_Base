# Grading Weights

**Purpose:** Configuration and calculation of weighted grade components

**Last Updated:** 2025-11-06  
**OCDS Version:** 1.0.0

---

## 📋 Overview

Grading weights determine how much each assessment component contributes to the final grade. OCDS uses a flexible weighting system that instructors can customize per class.

---

## ⚖️ Default Weights

### Standard Configuration

| Component | Weight | Rationale |
|-----------|--------|-----------|
| **Quizzes** | 40% | Primary knowledge assessment |
| **Flashcards** | 30% | Retention and review |
| **Homework** | 20% | Application and analysis |
| **Tasks** | 10% | Engagement and completion |
| **TOTAL** | **100%** | |

---

## 🔧 Configuring Weights

### grading_config.yaml

```yaml
# Component Weights (must sum to 1.0)
weights:
  quizzes: 0.40      # 40%
  flashcards: 0.30   # 30%
  homework: 0.20     # 20%
  tasks: 0.10        # 10%

# Validation
validate_weights: true  # Ensure weights sum to 1.0
allow_bonus: true       # Allow components to exceed 100%
cap_final_grade: true   # Cap final grade at 100%
```

---

## 📊 Weight Calculation

### Final Grade Formula

```python
def calculate_final_grade(scores: Dict[str, float], 
                         weights: Dict[str, float]) -> float:
    """Calculate weighted final grade."""
    
    # Validate weights sum to 1.0
    if abs(sum(weights.values()) - 1.0) > 0.01:
        raise ValueError("Weights must sum to 1.0")
    
    # Calculate weighted components
    weighted_scores = {}
    for component, score in scores.items():
        weight = weights.get(component, 0)
        weighted_scores[component] = score * weight
    
    # Sum to final grade
    final_grade = sum(weighted_scores.values())
    
    # Cap at 100% if configured
    if cap_final_grade:
        final_grade = min(final_grade, 100)
    
    return final_grade
```

---

## 🎯 Alternative Weight Schemes

### Scheme 1: Quiz-Heavy (Assessment Focus)

```yaml
weights:
  quizzes: 0.50      # 50%
  flashcards: 0.20   # 20%
  homework: 0.25     # 25%
  tasks: 0.05        # 5%
```

**Best for:** Classes emphasizing knowledge recall

---

### Scheme 2: Homework-Heavy (Application Focus)

```yaml
weights:
  quizzes: 0.30      # 30%
  flashcards: 0.20   # 20%
  homework: 0.40     # 40%
  tasks: 0.10        # 10%
```

**Best for:** Classes emphasizing practical application

---

### Scheme 3: Balanced (Equal Distribution)

```yaml
weights:
  quizzes: 0.33      # 33%
  flashcards: 0.33   # 33%
  homework: 0.34     # 34%
  tasks: 0.00        # 0% (not graded)
```

**Best for:** Classes valuing all assessment types equally

---

### Scheme 4: Engagement-Heavy (Process Focus)

```yaml
weights:
  quizzes: 0.25      # 25%
  flashcards: 0.35   # 35%
  homework: 0.20     # 20%
  tasks: 0.20        # 20%
```

**Best for:** Classes emphasizing consistent effort

---

## 📈 Weight Impact Analysis

### Example Student Scores

```
Quizzes: 85%
Flashcards: 90%
Homework: 75%
Tasks: 95%
```

### Impact of Different Weights

| Scheme | Quiz | Flash | HW | Tasks | **Final** |
|--------|------|-------|----|----|-----------|
| **Default** | 34.0 | 27.0 | 15.0 | 9.5 | **85.5%** |
| **Quiz-Heavy** | 42.5 | 18.0 | 18.75 | 4.75 | **84.0%** |
| **HW-Heavy** | 25.5 | 18.0 | 30.0 | 9.5 | **83.0%** |
| **Balanced** | 28.05 | 29.7 | 25.5 | 0 | **83.25%** |
| **Engagement** | 21.25 | 31.5 | 15.0 | 19.0 | **86.75%** |

**Observation:** Weight scheme can change final grade by 3-4 percentage points!

---

## 🔍 Choosing the Right Weights

### Considerations

**Learning Objectives:**
- What skills are most important?
- Knowledge recall vs. application?
- Individual work vs. collaboration?

**Student Workload:**
- How much time does each component require?
- Balance effort with grade impact

**Assessment Reliability:**
- Auto-graded (quizzes) vs. manual (homework)
- Objective vs. subjective measures

**Pedagogical Philosophy:**
- Mastery-based vs. effort-based?
- Summative vs. formative assessment?

---

## 🎯 Best Practices

### For Instructors

**Setting Weights:**
- ✅ **Align with goals** - Weight what matters most
- ✅ **Test with examples** - Calculate sample grades
- ✅ **Consider workload** - Don't overweight low-effort items
- ✅ **Be transparent** - Explain weights to students
- ✅ **Review mid-course** - Adjust if needed (with notice)

**Communicating Weights:**
- ✅ **In syllabus** - Document clearly
- ✅ **In dashboard** - Show breakdown
- ✅ **With examples** - Demonstrate calculations
- ✅ **Early in course** - Set expectations upfront

---

### For Students

**Understanding Weights:**
- ✅ **Know the breakdown** - Where to focus effort
- ✅ **Calculate your grade** - Verify accuracy
- ✅ **Prioritize wisely** - Focus on high-weight components
- ✅ **Don't ignore low-weight** - Every point counts

**Strategic Studying:**
```
If quizzes = 40% and homework = 20%:
- Improving quiz score 10% = +4% final grade
- Improving homework 10% = +2% final grade
- Focus on quizzes for maximum impact!
```

---

## 📊 Weight Visualization

### Component Breakdown (Pie Chart)

```dataviewjs
const weights = {
  'Quizzes': 40,
  'Flashcards': 30,
  'Homework': 20,
  'Tasks': 10
};

// Create simple text visualization
let output = "**Grade Component Weights:**\n\n";
for (const [component, weight] of Object.entries(weights)) {
  const bar = '█'.repeat(weight / 2);
  output += `${component}: ${bar} ${weight}%\n`;
}

dv.paragraph(output);
```

---

## 🔄 Dynamic Weighting (Advanced)

### Adaptive Weights Based on Performance

```python
def calculate_adaptive_weights(student_scores: Dict[str, float]) -> Dict[str, float]:
    """Adjust weights to favor student's strengths (optional)."""
    
    base_weights = {
        'quizzes': 0.40,
        'flashcards': 0.30,
        'homework': 0.20,
        'tasks': 0.10
    }
    
    # Find student's strongest component
    strongest = max(student_scores, key=student_scores.get)
    
    # Boost strongest component by 5%, reduce others proportionally
    adjusted_weights = base_weights.copy()
    adjusted_weights[strongest] += 0.05
    
    # Reduce other components proportionally
    reduction_per_component = 0.05 / 3
    for component in adjusted_weights:
        if component != strongest:
            adjusted_weights[component] -= reduction_per_component
    
    return adjusted_weights
```

**Note:** This is an advanced feature. Use with caution and clear communication.

---

## ✅ Weight Configuration Checklist

### Before Finalizing Weights

- [ ] Weights sum to exactly 1.0 (100%)
- [ ] Weights align with learning objectives
- [ ] Weights reflect component difficulty/effort
- [ ] Tested with sample student data
- [ ] Documented in class manifest
- [ ] Communicated to students
- [ ] Compared to similar courses
- [ ] Approved by department (if required)

---

## 📚 Related Documentation

- [[Auto_Grading_Overview.md]] - Overall grading system
- [[Grading_Config_Schema.md]] - Configuration format
- [[Grade_Reports.md]] - Grade display and reports
- [[auto_grader.py.md]] - Grading calculations

---

*Last updated: 2025-11-06*  
*OCDS Version: 1.0.0*
