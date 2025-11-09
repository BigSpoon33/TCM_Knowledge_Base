# Example Timeline

**Purpose:** Sample timeline.yaml for reference

**Last Updated:** 2025-11-06  
**OCDS Version:** 1.0.0

---

```yaml
# Example timeline.yaml
class_id: TCM_101
title: "Traditional Chinese Medicine Fundamentals"
pacing_strategy: hybrid

weeks:
  - week: 1
    title: "Introduction to Tongue Diagnosis"
    unlock_date: 2025-01-01
    due_date: 2025-01-07
    
    topics:
      - "Tongue body characteristics"
      - "Tongue coating analysis"
    
    materials:
      - type: study
        title: "Tongue Diagnosis Fundamentals"
        estimated_time: 60
      
      - type: flashcards
        title: "Tongue Diagnosis Terms"
        card_count: 20
      
      - type: quiz
        title: "Week 1 Quiz"
        questions: 10
        points: 10
      
      - type: homework
        title: "Tongue Case Study"
        points: 20
    
    unlock_requirements: []  # Week 1 always unlocked
  
  - week: 2
    title: "Pulse Diagnosis Fundamentals"
    unlock_date: 2025-01-08
    due_date: 2025-01-14
    
    unlock_requirements:
      - material_id: quiz_week01
        min_score: 70
      - material_id: task_week01
        min_completion: 80
```

---

*Last updated: 2025-11-06*  
*OCDS Version: 1.0.0*
