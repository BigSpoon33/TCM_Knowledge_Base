# Class Manifest Schema

**Complete specification for `class_manifest.yaml`**

---

## 📚 Overview

The class manifest is the main configuration file for an OCDS class. It defines:
- Class metadata (ID, name, version, author)
- Duration and structure
- Prerequisites
- Grading configuration
- Material references
- Distribution settings

**Location:** `Classes/{CLASS_NAME}/class_manifest.yaml`

---

## 📋 Complete Schema

```yaml
# ===========================================
# CLASS MANIFEST SCHEMA v1.0
# ===========================================

# ============ REQUIRED FIELDS ============

# Class Identification
class_id: string              # Unique identifier (alphanumeric, underscores)
class_name: string            # Display name
version: string               # Semantic versioning (e.g., "1.0.0")

# Authorship
author: string                # Creator name
created_date: YYYY-MM-DD      # Creation date
updated_date: YYYY-MM-DD      # Last update date

# Duration
duration_weeks: integer       # Total weeks in class
duration_days_per_week: integer  # Days per week (default: 7)

# ============ OPTIONAL FIELDS ============

# Prerequisites
prerequisites: array          # List of required class_ids
  - "CLASS_ID_1"
  - "CLASS_ID_2"

# Grading Configuration
passing_grade: integer        # Minimum % to pass (default: 70)
unlock_threshold: integer     # Score to unlock early (default: 75)
grading_weights:
  quizzes: float             # 0.0-1.0 (default: 0.4)
  flashcards: float          # 0.0-1.0 (default: 0.3)
  homework: float            # 0.0-1.0 (default: 0.2)
  pomodoros: float           # 0.0-1.0 (default: 0.1)

# Material References
materials_folder: string      # Relative path to materials
question_banks: array         # Paths to question bank files
  - "path/to/questions.yaml"
slide_decks: array           # Paths to slide decks
  - "path/to/slides.md"

# Metadata
description: string           # Course description
tags: array                   # Categorization tags
  - "tag1"
  - "tag2"
difficulty: string            # beginner | intermediate | advanced
estimated_hours: integer      # Total study time estimate
language: string              # en | es | fr | etc. (default: "en")

# Distribution
license: string               # License type (MIT, CC-BY, etc.)
price: float                  # Price in USD (0 = free)
marketplace_category: string  # Category for marketplace

# Advanced Settings
start_date_relative: boolean  # true = relative to import (default: true)
allow_retakes: boolean        # Allow quiz retakes (default: false)
show_answers: boolean         # Show quiz answers after submit (default: true)
require_sequential: boolean   # Must complete in order (default: true)
```
> This is really good. I can understand why each frontmatter i necessary and how it can be used. the license, price, and marketplace category is cool. 
---

## 🔍 Field Descriptions

### Class Identification

#### `class_id` (required)
- **Type:** string
- **Format:** Alphanumeric with underscores, no spaces
- **Example:** `"TCM_101"`, `"FOUNDATIONS_BASICS"`
- **Purpose:** Unique identifier for the class
- **Rules:**
  - Must be unique across all classes
  - Cannot contain spaces or special characters
  - Recommended format: `SUBJECT_LEVEL` or `SUBJECT_NUMBER`

#### `class_name` (required)
- **Type:** string
- **Example:** `"TCM Fundamentals: Patterns & Diagnosis"`
- **Purpose:** Human-readable display name
- **Rules:**
  - Can contain spaces and special characters
  - Should be descriptive and clear
  - Recommended length: 30-60 characters

#### `version` (required)
- **Type:** string
- **Format:** Semantic versioning (MAJOR.MINOR.PATCH)
- **Example:** `"1.0.0"`, `"2.1.3"`
- **Purpose:** Track class revisions
- **Rules:**
  - MAJOR: Breaking changes (incompatible updates)
  - MINOR: New features (backward compatible)
  - PATCH: Bug fixes
> really good explainations for how to write a class
---

### Authorship

#### `author` (required)
- **Type:** string
- **Example:** `"Dr. Jane Smith"`, `"TCM Academy"`
- **Purpose:** Credit creator

#### `created_date` (required)
- **Type:** date
- **Format:** YYYY-MM-DD
- **Example:** `2025-11-05`
- **Purpose:** Track when class was created

#### `updated_date` (required)
- **Type:** date
- **Format:** YYYY-MM-DD
- **Example:** `2025-11-05`
- **Purpose:** Track last modification
- **Rules:** Update whenever class content changes
>Give your class an author!
---

### Duration

#### `duration_weeks` (required)
- **Type:** integer
- **Range:** 1-52
- **Example:** `12`
- **Purpose:** Total length of class in weeks

#### `duration_days_per_week` (optional)
- **Type:** integer
- **Range:** 1-7
- **Default:** `7`
- **Example:** `5` (weekdays only)
- **Purpose:** How many days per week have content
>More for coordinating a program of classes. not as important for random class pickups but if you want to follow a sequence and stay on track with a timeline this can help with both
---

### Prerequisites

#### `prerequisites` (optional)
- **Type:** array of strings
- **Default:** `[]` (no prerequisites)
- **Example:**
  ```yaml
  prerequisites:
    - "TCM_100"
    - "FOUNDATIONS_101"
  ```
- **Purpose:** Required classes before enrollment
- **Rules:**
  - Must reference valid class_ids
  - Import script checks prerequisites
  - Students warned if not met
>could be used for shared materials like if a class is using the flashcards from another prereq class then  you need to have those materials from the required class in order to complete the material. also good for ensuing sequence of classes like 101 > 102 > 103 etc
---

### Grading Configuration

#### `passing_grade` (optional)
- **Type:** integer
- **Range:** 0-100
- **Default:** `70`
- **Example:** `75`
- **Purpose:** Minimum percentage to pass class

#### `unlock_threshold` (optional)
- **Type:** integer
- **Range:** 0-100
- **Default:** `75`
- **Example:** `80`
- **Purpose:** Score needed to unlock next week early
- **Rules:** Should be >= passing_grade

#### `grading_weights` (optional)
- **Type:** object with float values
- **Default:**
  ```yaml
  grading_weights:
    quizzes: 0.4
    flashcards: 0.3
    homework: 0.2
    pomodoros: 0.1
  ```
- **Purpose:** How much each component contributes to grade
- **Rules:**
  - All values must sum to 1.0
  - Each value between 0.0 and 1.0
  - Can omit components (will be 0)
> should be automated based on the class key. a key can be private or come with the class. The key would be something that can be used to automatically grade the class. like all the answers or the back of the book
---

### Material References

#### `materials_folder` (optional)
- **Type:** string
- **Example:** `"Materials/TCM_Patterns"`
- **Purpose:** Path to source materials
- **Rules:**
  - Relative to vault root
  - Must exist before building class

#### `question_banks` (optional)
- **Type:** array of strings
- **Example:**
  ```yaml
  question_banks:
    - "Materials/Question_Banks/Patterns/qi_patterns.yaml"
    - "Materials/Question_Banks/Patterns/blood_patterns.yaml"
  ```
- **Purpose:** Quiz question sources
- **Rules:**
  - Paths relative to vault root
  - Must be valid YAML files
  - Follow question bank schema

#### `slide_decks` (optional)
- **Type:** array of strings
- **Example:**
  ```yaml
  slide_decks:
    - "Materials/Slides/Qi_Deficiency_Slides.md"
  ```
- **Purpose:** Presentation materials

---

### Metadata

#### `description` (optional)
- **Type:** string
- **Example:** `"Introduction to TCM pattern differentiation and diagnosis"`
- **Purpose:** Course description for students
- **Recommended length:** 100-300 characters

#### `tags` (optional)
- **Type:** array of strings
- **Example:**
  ```yaml
  tags:
    - "tcm"
    - "patterns"
    - "diagnosis"
    - "fundamentals"
  ```
- **Purpose:** Categorization and search

#### `difficulty` (optional)
- **Type:** string
- **Values:** `beginner`, `intermediate`, `advanced`
- **Default:** `beginner`
- **Purpose:** Help students choose appropriate level

#### `estimated_hours` (optional)
- **Type:** integer
- **Example:** `120`
- **Purpose:** Total study time estimate
- **Calculation:** Sum of all task estimated_minutes / 60

#### `language` (optional)
- **Type:** string
- **Format:** ISO 639-1 code
- **Default:** `"en"`
- **Example:** `"en"`, `"es"`, `"fr"`, `"zh"`
- **Purpose:** Content language
>can be helpful for organizing market by language or knowing if a language class is good for you. like a learn spanish deck might be for english or spanish speakers? idk doesn't really make sense I'm high.
---

### Distribution

#### `license` (optional)
- **Type:** string
- **Example:** `"MIT"`, `"CC-BY-4.0"`, `"All Rights Reserved"`
- **Purpose:** Usage rights

#### `price` (optional)
- **Type:** float
- **Default:** `0` (free)
- **Example:** `29.99`
- **Purpose:** Marketplace pricing

#### `marketplace_category` (optional)
- **Type:** string
- **Example:** `"Health & Medicine"`, `"TCM"`, `"Acupuncture"`
- **Purpose:** Marketplace organization
> v cool idea. could be a cash shop or a community hub kind of thing. can also have a way to send classes in the class capsule thing I was thinking about in chatgpt and gemini. so you can send a class to your friend or even play a tcg game or a dnd game with friends through it.
---

### Advanced Settings

#### `start_date_relative` (optional)
- **Type:** boolean
- **Default:** `true`
- **Purpose:** If true, dates calculated from import date
- **Example:**
  - `true`: Week 1 starts on import date
  - `false`: Use absolute dates from timeline

#### `allow_retakes` (optional)
- **Type:** boolean
- **Default:** `false`
- **Purpose:** Allow students to retake quizzes
- **Rules:**
  - If true, best score counts
  - If false, first attempt only

#### `show_answers` (optional)
- **Type:** boolean
- **Default:** `true`
- **Purpose:** Show correct answers after quiz submission

#### `require_sequential` (optional)
- **Type:** boolean
- **Default:** `true`
- **Purpose:** Must complete weeks in order
- **Rules:**
  - If true, Week 2 blocked until Week 1 complete
  - If false, all weeks available immediately
>I like this for keeping track of when you took your classes and everything. keeping the schedule relative to when you start the class and not when the class was made by the author
---

## 📝 Complete Example

```yaml
# ===========================================
# TCM 101: Fundamentals
# ===========================================

# Class Identification
class_id: "TCM_101"
class_name: "TCM Fundamentals: Patterns & Diagnosis"
version: "1.0.0"

# Authorship
author: "Dr. Jane Smith"
created_date: 2025-11-05
updated_date: 2025-11-05

# Duration
duration_weeks: 12
duration_days_per_week: 7

# Prerequisites
prerequisites: []

# Grading Configuration
passing_grade: 70
unlock_threshold: 75
grading_weights:
  quizzes: 0.4
  flashcards: 0.3
  homework: 0.2
  pomodoros: 0.1

# Material References
materials_folder: "Materials/TCM_Patterns"
question_banks:
  - "Materials/Question_Banks/Patterns/qi_patterns.yaml"
  - "Materials/Question_Banks/Patterns/blood_patterns.yaml"
  - "Materials/Question_Banks/Patterns/yin_yang_patterns.yaml"
slide_decks:
  - "Materials/Slides/Qi_Deficiency_Slides.md"
  - "Materials/Slides/Blood_Deficiency_Slides.md"

# Metadata
description: "Introduction to TCM pattern differentiation and diagnosis. Learn to identify patterns, analyze tongue and pulse, and select appropriate treatments."
tags:
  - "tcm"
  - "patterns"
  - "diagnosis"
  - "fundamentals"
  - "beginner"
difficulty: "beginner"
estimated_hours: 120
language: "en"

# Distribution
license: "CC-BY-4.0"
price: 0
marketplace_category: "TCM Education"

# Advanced Settings
start_date_relative: true
allow_retakes: false
show_answers: true
require_sequential: true
```
>oooh this kind of clicked something for me. it's like each note that is used in the material needs to have it's own flashcards, quizbank, slides, what else? that way you can have classes use the material dynamically instead of glob with each herbal category. for example if all the single herbs have their own materials then you can break classes apart to study all single herbs in the formulas of a category.  but it's kind of a pain to have to specify every single herb. maybe a tag system along with the specific one by one approach. so you could do tag yang tonics for single herbs and then specify other things or yeah. something
---

## ✅ Validation Rules

### Required Fields Check
```python
required_fields = [
    'class_id',
    'class_name',
    'version',
    'author',
    'created_date',
    'updated_date',
    'duration_weeks'
]
```

### Format Validation
```python
def validate_manifest(manifest):
    """Validate class manifest."""
    
    # Check required fields
    for field in required_fields:
        if field not in manifest:
            raise ValueError(f"Missing required field: {field}")
    
    # Validate class_id format
    if not re.match(r'^[A-Z0-9_]+$', manifest['class_id']):
        raise ValueError("class_id must be alphanumeric with underscores")
    
    # Validate version format
    if not re.match(r'^\d+\.\d+\.\d+$', manifest['version']):
        raise ValueError("version must be semantic (X.Y.Z)")
    
    # Validate dates
    try:
        datetime.strptime(manifest['created_date'], '%Y-%m-%d')
        datetime.strptime(manifest['updated_date'], '%Y-%m-%d')
    except ValueError:
        raise ValueError("Dates must be YYYY-MM-DD format")
    
    # Validate duration
    if manifest['duration_weeks'] < 1 or manifest['duration_weeks'] > 52:
        raise ValueError("duration_weeks must be 1-52")
    
    # Validate grading weights sum to 1.0
    if 'grading_weights' in manifest:
        total = sum(manifest['grading_weights'].values())
        if abs(total - 1.0) > 0.01:
            raise ValueError(f"grading_weights must sum to 1.0 (got {total})")
    
    return True
```

---

## 🔄 Version Migration

### Updating from v0.9 to v1.0

```yaml
# Old format (v0.9)
name: "TCM 101"
weeks: 12

# New format (v1.0)
class_id: "TCM_101"
class_name: "TCM 101"
duration_weeks: 12
version: "1.0.0"
```

---

## 💡 Best Practices

### Naming Conventions
- **class_id:** Use SUBJECT_LEVEL format (e.g., `TCM_101`, `HERBS_201`)
- **class_name:** Be descriptive and specific
- **version:** Start at 1.0.0, increment appropriately

### Grading Weights
- **Quizzes:** 40% (primary assessment)
- **Flashcards:** 30% (daily practice)
- **Homework:** 20% (application)
- **Pomodoros:** 10% (time investment)
- **Adjust** based on class type and goals

### Prerequisites
- **List all** required prior knowledge
- **Order matters** - list in sequence
- **Be specific** - reference exact class_ids

### Material Organization
- **Centralize** materials in Materials/ folder
- **Reuse** materials across classes
- **Version control** question banks separately

---

## 🐛 Common Errors

### Invalid YAML Syntax
```yaml
# ❌ Wrong - missing quotes
description: This is a description with: colons

# ✅ Correct - quoted
description: "This is a description with: colons"
```

### Grading Weights Don't Sum to 1.0
```yaml
# ❌ Wrong - sums to 0.9
grading_weights:
  quizzes: 0.4
  flashcards: 0.3
  homework: 0.2

# ✅ Correct - sums to 1.0
grading_weights:
  quizzes: 0.4
  flashcards: 0.3
  homework: 0.2
  pomodoros: 0.1
```

### Invalid Date Format
```yaml
# ❌ Wrong
created_date: 11/05/2025

# ✅ Correct
created_date: 2025-11-05
```

---

## 📚 Related Documentation

- **Timeline Schema:** `Timeline_Schema.md`
- **Grading Config:** `Grading_Config_Schema.md`
- **Question Banks:** `Question_Bank_Schema.md`
- **Class Creation:** `../10_Class_Creation/Class_Builder_Guide.md`

---

**Define your class with a solid manifest! 📋**

---

*Last updated: 2025-11-05*  
*OCDS Version: 1.0.0*
