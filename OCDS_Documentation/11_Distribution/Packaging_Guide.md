# Packaging Guide

**Purpose:** Guide to packaging OCDS classes for distribution

**Last Updated:** 2025-11-06  
**OCDS Version:** 1.0.0

---

## 📋 Overview

Packaging creates a distributable .zip file containing all class materials and configuration.

---

## 📦 Package Structure

```
TCM_101_v1.0.0.zip
├── class_manifest.yaml
├── timeline.yaml
├── grading_config.yaml
├── question_bank.yaml
├── Materials/
│   ├── Week_01/
│   ├── Week_02/
│   └── ...
├── Images/
├── Resources/
└── README.md
```

---

## 🔧 Packaging Command

```bash
python package_class.py \
  --class-id TCM_101 \
  --output TCM_101_v1.0.0.zip \
  --include-images \
  --include-resources
```

---

## ✅ Pre-Package Checklist

- [ ] All materials tested
- [ ] Configuration files validated
- [ ] Images optimized
- [ ] README.md included
- [ ] Version number updated
- [ ] Changelog documented

---

## 📚 Related Documentation

- [[Class_Builder_Guide.md]] - Building classes
- [[Import_Instructions.md]] - Student import guide

---

*Last updated: 2025-11-06*  
*OCDS Version: 1.0.0*
