# generate_materials.py - Material Generation Script

**Purpose:** Auto-generate course materials from templates and timeline configuration

**Last Updated:** 2025-11-06  
**OCDS Version:** 1.0.0

---

## 📋 Overview

The `generate_materials.py` script is the **class builder** for instructors. It reads your timeline and question bank, then automatically generates all course materials (study materials, quizzes, homework, slides, flashcards) with proper frontmatter and structure.

### What This Script Does

1. ✅ **Reads timeline.yaml** - Gets week/day structure
2. ✅ **Reads question_bank.yaml** - Gets quiz questions
3. ✅ **Generates study materials** - From templates
4. ✅ **Creates quizzes** - Pulls questions from bank
5. ✅ **Builds homework** - From assignment templates
6. ✅ **Makes slide decks** - From presentation templates
7. ✅ **Creates flashcards** - From flashcard definitions
8. ✅ **Applies frontmatter** - Correct metadata for all files

---

## 🚀 Quick Start

### Basic Usage

```bash
python generate_materials.py --class-id TCM_101 --weeks 1-12
```

### Generate Single Week

```bash
python generate_materials.py --class-id TCM_101 --week 5
```

### With Custom Templates

```bash
python generate_materials.py \
  --class-id TCM_101 \
  --weeks 1-12 \
  --templates-dir custom_templates/
```

---

## 📖 Command Line Arguments

| Argument | Description | Example |
|----------|-------------|---------|
| `--class-id` | Class identifier (required) | `--class-id TCM_101` |
| `--weeks` | Week range to generate | `--weeks 1-12` |
| `--week` | Single week | `--week 5` |
| `--materials-dir` | Output directory | `--materials-dir Materials/` |
| `--templates-dir` | Templates location | `--templates-dir templates/` |
| `--force` | Overwrite existing files | `--force` |
| `--dry-run` | Preview without creating | `--dry-run` |
| `--verbose` | Detailed output | `--verbose` |

---

## 🏗️ How It Works

### Generation Process

```python
def generate_materials(class_id: str, weeks: List[int]):
    """Generate all materials for specified weeks."""
    
    # Load configurations
    manifest = load_yaml(f'Classes/{class_id}/class_manifest.yaml')
    timeline = load_yaml(f'Classes/{class_id}/timeline.yaml')
    question_bank = load_yaml(f'Classes/{class_id}/question_bank.yaml')
    
    for week_num in weeks:
        week_data = get_week_data(timeline, week_num)
        
        # Generate each material type
        generate_study_material(class_id, week_num, week_data)
        generate_flashcards(class_id, week_num, week_data)
        generate_quiz(class_id, week_num, week_data, question_bank)
        generate_homework(class_id, week_num, week_data)
        generate_slides(class_id, week_num, week_data)
        
        print(f"✅ Week {week_num} complete")
```

---

## 📝 Template System

### Jinja2 Templates

Materials are generated from Jinja2 templates with variables:

**Study Material Template** (`study_material.md.j2`):
```markdown
---
ocds_type: study
material_id: study_week{{ week_num }}_{{ topic_slug }}
class_id: {{ class_id }}
week: {{ week_num }}
title: "{{ title }}"
---

# {{ title }}

{{ content }}

## Learning Objectives

{% for objective in learning_objectives %}
- {{ objective }}
{% endfor %}

## Key Concepts

{% for concept in key_concepts %}
### {{ concept.name }}

{{ concept.description }}
{% endfor %}
```

**Quiz Template** (`quiz.md.j2`):
```markdown
---
ocds_type: quiz
material_id: quiz_week{{ week_num }}
class_id: {{ class_id }}
week: {{ week_num }}
title: "{{ title }}"
questions: {{ questions|length }}
---

# {{ title }}

{% for question in questions %}
## Question {{ loop.index }}

{{ question.text }}

{% for option in question.options %}
- [ ] {{ option.text }}
{% endfor %}

**Correct Answer:** {{ question.correct_answer }}
{% endfor %}
```

---

## 📊 Example Output

```
🎓 OCDS Material Generator
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Class: TCM_101 - Traditional Chinese Medicine Fundamentals
Weeks: 1-12

📚 Generating Materials...

Week 1: Introduction to Tongue Diagnosis
  ✅ Study Material: Week_1_Study_Material.md (1,200 lines)
  ✅ Flashcards: Week_1_Flashcards.md (20 cards)
  ✅ Quiz: Week_1_Quiz.md (10 questions)
  ✅ Homework: Week_1_Homework.md
  ✅ Slides: Week_1_Slides.md (25 slides)

Week 2: Pulse Diagnosis Fundamentals
  ✅ Study Material: Week_2_Study_Material.md (1,500 lines)
  ✅ Flashcards: Week_2_Flashcards.md (25 cards)
  ✅ Quiz: Week_2_Quiz.md (10 questions)
  ✅ Homework: Week_2_Homework.md
  ✅ Slides: Week_2_Slides.md (30 slides)

[... weeks 3-12 ...]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ Complete!

Summary:
  📄 Files created: 60
  📝 Total lines: 45,000
  ⏱️  Time: 12.3 seconds

Next steps:
  1. Run: python generate_tasks.py --class-id TCM_101 --weeks 1-12
  2. Review generated materials in: Classes/TCM_101/Materials/
  3. Customize as needed
```

---

## 🎯 Best Practices

### For Instructors

- ✅ **Complete timeline first** - Define all weeks before generating
- ✅ **Build question bank** - Write all quiz questions upfront
- ✅ **Use templates** - Customize templates for your teaching style
- ✅ **Review output** - Always check generated files
- ✅ **Version control** - Git track your materials
- ✅ **Test before distributing** - Import and test the class

---

## 📚 Related Documentation

- [[Script_Overview.md]] - All automation scripts
- [[Timeline_Schema.md]] - Timeline configuration
- [[Question_Bank_Schema.md]] - Question bank format
- [[Study_Material_Template.md]] - Study material format

---

*Last updated: 2025-11-06*  
*OCDS Version: 1.0.0*
