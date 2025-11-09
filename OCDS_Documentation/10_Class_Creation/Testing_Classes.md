# Testing Classes

**Purpose:** QA process for OCDS classes before distribution

**Last Updated:** 2025-11-06  
**OCDS Version:** 1.0.0

---

## 📋 Overview

Thorough testing ensures students have a smooth learning experience. This guide covers the complete QA process.

---

## ✅ Testing Checklist

### Configuration Files

- [ ] class_manifest.yaml validates
- [ ] timeline.yaml has all required fields
- [ ] grading_config.yaml weights sum to 1.0
- [ ] question_bank.yaml has correct answers

---

### Materials

- [ ] All study materials render correctly
- [ ] Flashcards import to SR plugin
- [ ] Quizzes have correct answers
- [ ] Homework rubrics are clear
- [ ] All links work
- [ ] Images display properly

---

### Functionality

- [ ] Week 1 unlocks on import
- [ ] Quizzes auto-grade correctly
- [ ] Task completion tracks
- [ ] Homework submission works
- [ ] Dashboard displays grades
- [ ] Unlock logic works

---

### User Experience

- [ ] Instructions are clear
- [ ] Workload is reasonable
- [ ] Difficulty progression is smooth
- [ ] No broken links
- [ ] Consistent formatting

---

## 🧪 Test Process

### 1. Import Test

```bash
python import_class.py \
  --package TCM_101.zip \
  --student-id test_user \
  --vault-path test_vault/
```

---

### 2. Complete Week 1

- Read study material
- Review flashcards
- Take quiz
- Submit homework
- Check all tasks

---

### 3. Verify Grading

- Check quiz auto-grades
- Verify grade calculations
- Test dashboard display

---

### 4. Test Unlocking

- Complete Week 1 requirements
- Verify Week 2 unlocks
- Test early unlock (if enabled)

---

## 📚 Related Documentation

- [[Class_Builder_Guide.md]] - Complete building guide
- [[import_class.py.md]] - Import script

---

*Last updated: 2025-11-06*  
*OCDS Version: 1.0.0*
