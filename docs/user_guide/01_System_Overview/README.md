# Obsidian Class Delivery System (OCDS)

**Version:** 1.0.0  
**Status:** In Development  
**Last Updated:** 2025-11-05

---

## 🎓 What is OCDS?

The **Obsidian Class Delivery System (OCDS)** is a comprehensive framework for creating, packaging, and distributing educational courses within Obsidian. It transforms your Obsidian vault into a complete learning management system with:

- **Automated content delivery** based on student progress
- **Performance-based progression** (not just time-based)
- **Auto-grading** for quizzes and assessments
- **Integrated study tools** (flashcards, slides, homework)
- **Progress tracking** with visual dashboards
- **Flexible pacing** that adapts to student performance

---

## 🌟 Key Features

### For Students
- ✅ **Self-paced learning** with flexible timelines
- ✅ **Spaced repetition** flashcards integrated into curriculum
- ✅ **Interactive quizzes** with instant feedback
- ✅ **Progress dashboards** showing grades and completion
- ✅ **Study materials** in multiple formats (text, slides, flashcards)
- ✅ **Time tracking** with Pomodoro integration
- ✅ **Review flags** highlighting areas needing attention

### For Instructors
- ✅ **Easy class creation** with templates and builders
- ✅ **Reusable materials** from content library
- ✅ **Automated grading** saves time
- ✅ **Question banks** for randomized quizzes
- ✅ **Performance analytics** track student progress
- ✅ **Flexible distribution** (free, paid, bundles)

### For Developers
- ✅ **Open architecture** using standard Obsidian plugins
- ✅ **Python automation** scripts for generation
- ✅ **YAML-based** configuration (human-readable)
- ✅ **Extensible design** for custom features
- ✅ **Well-documented** APIs and schemas

---

## 🏗️ System Architecture

### Core Components

```
OCDS Ecosystem
│
├── Materials Library
│   └── Source content (patterns, herbs, formulas, points, etc.)
│
├── Class Packages
│   ├── Manifest (metadata)
│   ├── Timeline (schedule)
│   ├── Grading Config (algorithm)
│   └── Weekly/Daily Materials
│
├── Automation Scripts
│   ├── Class Import
│   ├── Material Generation
│   ├── Task Generation
│   ├── Auto-Grading
│   └── Unlock Management
│
├── Student Progress
│   ├── Activity Tracking
│   ├── Grade Calculation
│   └── Progress Dashboards
│
└── Plugin Integration
    ├── Spaced Repetition (flashcards)
    ├── TaskNotes (scheduling)
    ├── Meta-bind (interactivity)
    ├── Dataview (queries)
    ├── Advanced Slides (presentations)
    └── Templater (automation)
```

### Data Flow

```
1. IMPORT CLASS
   ↓
2. GENERATE WEEK 1 TASKS & MATERIALS
   ↓
3. STUDENT COMPLETES ACTIVITIES
   ↓
4. AUTO-GRADER CALCULATES SCORE
   ↓
5. CHECK UNLOCK CONDITIONS
   ↓
6. IF MET → GENERATE NEXT WEEK
   ↓
7. UPDATE PROGRESS DASHBOARD
   ↓
8. REPEAT UNTIL CLASS COMPLETE
```

---

## 📦 What's Included

### Documentation (This Folder)
- **System Overview** - Architecture and concepts
- **Plugin Integration** - How to use each plugin
- **Data Standards** - YAML schemas and formats
- **Material Templates** - Ready-to-use templates
- **Automation Scripts** - Python tools
- **Best Practices** - Guidelines and tips
- **Examples** - Complete sample class

### Scripts (`/scripts/`)
- `import_class.py` - Import packaged classes
- `generate_materials.py` - Create study materials
- `generate_tasks.py` - Generate TaskNotes
- `auto_grader.py` - Grade quizzes automatically
- `unlock_manager.py` - Handle progression logic
- `build_class.py` - Package classes for distribution

### Templates (`/OCDS_Templates/`)
- Study material template
- Flashcard template
- Quiz template
- Homework template
- Slide deck template
- Task template
- Dashboard template

---

## 🚀 Quick Start

### For Students (Importing a Class)

1. **Download a class package** (`.zip` file)
2. **Run import script:**
   ```bash
   python scripts/import_class.py --class-path "TCM_101.zip" --start-date "2025-11-10"
   ```
3. **Open your vault** - new tasks and materials appear
4. **Start studying!** - follow the tasks in TaskNotes

### For Instructors (Creating a Class)

1. **Organize your materials** in `Materials/` folder
2. **Create question banks** for quizzes
3. **Design timeline** in `timeline.yaml`
4. **Configure grading** in `grading_config.yaml`
5. **Build class package:**
   ```bash
   python scripts/build_class.py --class-id "TCM_101"
   ```
6. **Distribute** the generated `.zip` file

---

## 📚 Documentation Structure

| Section | Purpose | Start Here If... |
|---------|---------|------------------|
| **01_System_Overview** | High-level concepts | You're new to OCDS |
| **02_Plugin_Integration** | Plugin syntax & usage | Setting up your vault |
| **03_Data_Standards** | YAML schemas | Creating class configs |
| **04_Folder_Structure** | File organization | Organizing materials |
| **05_Material_Templates** | Content templates | Writing course content |
| **06_Automation_Scripts** | Python scripts | Automating workflows |
| **07_Grading_System** | Auto-grading | Setting up assessments |
| **08_Unlock_System** | Progression logic | Designing pacing |
| **09_Dashboard_Design** | Progress tracking | Building dashboards |
| **10_Class_Creation** | Building classes | Creating a course |
| **11_Distribution** | Packaging & sharing | Distributing courses |
| **12_Best_Practices** | Guidelines | Improving quality |
| **13_Examples** | Sample classes | Learning by example |

---

## 🎯 Use Cases

### Educational Institutions
- Distribute course materials to students
- Track student progress and grades
- Standardize curriculum across instructors
- Provide self-paced learning options

### Independent Educators
- Create and sell online courses
- Build course libraries
- Offer subscription-based learning
- Provide custom training programs

### Self-Learners
- Structure personal learning projects
- Track study progress
- Use spaced repetition effectively
- Stay motivated with gamification

### Corporate Training
- Onboard new employees
- Deliver compliance training
- Track completion and certification
- Customize content by role

---

## 🔧 Technical Requirements

### Required Software
- **Obsidian** (v1.4.0+)
- **Python** (3.8+) for automation scripts

### Required Plugins
- Spaced Repetition
- TaskNotes
- Meta-bind
- Dataview
- Advanced Slides
- Templater

### Optional Plugins
- Obsidian Pomodoro (time tracking)
- Charts (progress visualization)
- Kanban (task management)

### System Requirements
- **OS:** Windows, macOS, or Linux
- **Storage:** 500MB+ for typical class
- **RAM:** 4GB+ recommended

---

## 🎓 Philosophy

OCDS is built on these core principles:

1. **Mastery-Based Learning** - Progress when you've learned, not just when time passes
2. **Local-First** - Your data stays in your vault, no cloud dependency
3. **Open & Extensible** - Built with standard tools, easy to customize
4. **Reusable Content** - Write once, use in multiple contexts
5. **Student-Centered** - Flexible pacing adapts to individual needs
6. **Evidence-Based** - Uses proven techniques (spaced repetition, active recall)

---

## 📖 Learning Path

### Beginner (Getting Started)
1. Read this README
2. Review `Quick_Start_Guide.md`
3. Import the example class (`13_Examples/`)
4. Complete Week 1 as a student
5. Explore the generated files

### Intermediate (Creating Content)
1. Study `05_Material_Templates/`
2. Review `03_Data_Standards/`
3. Create a simple 1-week class
4. Test it yourself
5. Refine based on experience

### Advanced (Full System)
1. Study `06_Automation_Scripts/`
2. Review `07_Grading_System/`
3. Build a complete multi-week course
4. Implement custom grading logic
5. Create question banks
6. Package for distribution

---

## 🤝 Contributing

OCDS is designed to be extended and customized. Ways to contribute:

- **Create templates** for new material types
- **Write scripts** for additional automation
- **Build plugins** for enhanced features
- **Share classes** with the community
- **Improve documentation**
- **Report bugs** and suggest features

---

## 📞 Support & Resources

### Documentation
- Full documentation in `OCDS_Documentation/`
- Example class in `13_Examples/`
- Video tutorials (coming soon)

### Community
- GitHub repository (coming soon)
- Discord server (coming soon)
- Forum discussions (coming soon)

### Getting Help
1. Check the documentation
2. Review examples
3. Search existing issues
4. Ask in community forums
5. File a bug report

---

## 🗺️ Roadmap

### Version 1.0 (Current)
- ✅ Core architecture
- ✅ Plugin integration
- ✅ Material templates
- 🔄 Automation scripts (in progress)
- 🔄 Example class (in progress)
- 🔄 Documentation (in progress)

### Version 1.1 (Planned)
- [ ] GUI class builder
- [ ] Enhanced dashboards
- [ ] Mobile optimization
- [ ] Export to Anki
- [ ] Certificate generation

### Version 2.0 (Future)
- [ ] Multi-instructor support
- [ ] Peer review system
- [ ] Discussion forums
- [ ] Video integration
- [ ] AI tutor integration

---

## 📄 License

OCDS is released under the MIT License. You are free to:
- Use commercially
- Modify and distribute
- Use privately
- Sublicense

See `LICENSE` file for full details.

---

## 🙏 Acknowledgments

OCDS builds on the excellent work of:
- **Obsidian** team for the amazing platform
- **Plugin developers** for essential tools
- **TCM Knowledge Base** as the original use case
- **Community contributors** for feedback and ideas

---

## 📬 Contact

**Project Maintainer:** [Your Name]  
**Email:** [Your Email]  
**GitHub:** [Repository URL]

---

**Ready to transform your Obsidian vault into a learning powerhouse?**

👉 **Next Step:** Read `Quick_Start_Guide.md` to get started!

---

*Last updated: 2025-11-05*  
*Version: 1.0.0*  
*Status: In Development*
