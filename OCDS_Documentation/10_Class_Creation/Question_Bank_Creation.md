# Question Bank Creation

**Purpose:** Guide to writing effective quiz questions

**Last Updated:** 2025-11-06  
**OCDS Version:** 1.0.0

---

## 📋 Overview

Good quiz questions test understanding, not just memorization. This guide helps you write clear, effective questions.

---

## 🎯 Question Writing Principles

### 1. Clear and Concise

**Good:**
"Which tongue color indicates Heat?"

**Bad:**
"In Traditional Chinese Medicine diagnostic theory, when examining the tongue body, which of the following color presentations would typically be associated with a Heat pattern?"

---

### 2. One Correct Answer

**Good:**
```yaml
text: "A red tongue indicates:"
options:
  - "Heat"  # Correct
  - "Cold"
  - "Dampness"
  - "Dryness"
```

**Bad:**
```yaml
text: "Which indicates Heat?"
options:
  - "Red tongue"  # Correct
  - "Rapid pulse"  # Also correct!
  - "Yellow coating"  # Also correct!
```

---

### 3. Plausible Distractors

Wrong answers should be tempting:

**Good distractors:**
- Common misconceptions
- Related but incorrect concepts
- Partial truths

**Bad distractors:**
- Obviously wrong
- Unrelated to topic
- Joke answers

---

## 📚 Related Documentation

- [[Class_Builder_Guide.md]] - Complete building guide
- [[Quiz_Template.md]] - Quiz format

---

*Last updated: 2025-11-06*  
*OCDS Version: 1.0.0*
