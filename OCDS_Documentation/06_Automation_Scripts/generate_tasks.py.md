# generate_tasks.py - Task Generation Script

**Purpose:** Auto-generate task checklists from timeline and materials

**Last Updated:** 2025-11-06  
**OCDS Version:** 1.0.0

---

## 📋 Overview

The `generate_tasks.py` script creates weekly task checklists that guide students through course materials. It reads the timeline and generated materials, then creates comprehensive to-do lists with proper linking and point values.

---

## 🚀 Quick Start

```bash
# Generate tasks for all weeks
python generate_tasks.py --class-id TCM_101 --weeks 1-12

# Generate tasks for single week
python generate_tasks.py --class-id TCM_101 --week 5
```

---

## 📖 Command Line Arguments

| Argument | Description | Example |
|----------|-------------|---------|
| `--class-id` | Class identifier (required) | `--class-id TCM_101` |
| `--weeks` | Week range | `--weeks 1-12` |
| `--week` | Single week | `--week 5` |
| `--force` | Overwrite existing | `--force` |

---

## 🏗️ How It Works

```python
def generate_week_tasks(class_id: str, week: int):
    """Generate task checklist for a week."""
    
    timeline = load_timeline(class_id)
    week_data = timeline['weeks'][week - 1]
    
    tasks = []
    
    # Study materials
    for material in week_data.get('study_materials', []):
        tasks.append({
            'description': f'Read {material["title"]}',
            'required': True,
            'points': 1,
            'linked_material': material['material_id']
        })
    
    # Quizzes
    for quiz in week_data.get('quizzes', []):
        tasks.append({
            'description': f'Complete {quiz["title"]} (70% minimum)',
            'required': True,
            'points': 2,
            'linked_material': quiz['material_id']
        })
    
    # Homework
    for hw in week_data.get('homework', []):
        tasks.append({
            'description': f'Submit {hw["title"]}',
            'required': True,
            'points': 2,
            'linked_material': hw['material_id']
        })
    
    create_task_file(class_id, week, tasks)
```

---

## 📊 Example Output

```
📋 OCDS Task Generator
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Class: TCM_101
Weeks: 1-12

Generating Tasks...

Week 1: 8 tasks created
  - 3 study tasks
  - 1 quiz task
  - 1 homework task
  - 3 bonus tasks

Week 2: 9 tasks created
  - 3 study tasks
  - 1 quiz task
  - 1 homework task
  - 4 bonus tasks

[... weeks 3-12 ...]

✅ Complete! 96 total tasks created
```

---

## 📚 Related Documentation

- [[Script_Overview.md]] - All automation scripts
- [[Task_Template.md]] - Task file format
- [[Timeline_Schema.md]] - Timeline configuration

---

*Last updated: 2025-11-06*  
*OCDS Version: 1.0.0*
