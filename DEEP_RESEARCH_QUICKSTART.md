# 🚀 Deep Research Pipeline - Quick Start Guide

**Status:** ✅ Complete and Ready to Use  
**Date:** 2025-11-07

---

## 📋 Overview

The Deep Research Pipeline automatically creates complete OCDS class packages from a single command. It uses AI to:
1. Generate an optimal research prompt
2. Conduct deep research
3. Generate content for each template section
4. Create a complete root note
5. Generate all materials (flashcards, quiz, slides, etc.)

**Time:** ~30 minutes (mostly AI processing)  
**Manual work:** Almost none  
**Output:** Complete OCDS class package

---

## ⚡ Quick Start

### **Prerequisites**

1. **Gemini API Key** (required)
   ```bash
   export GEMINI_API_KEY="your-api-key-here"
   ```
   
   Get your key from: https://makersuite.google.com/app/apikey

2. **Python packages** (should already be installed)
   ```bash
   pip install google-generativeai pyyaml
   ```

---

### **Basic Usage**

```bash
# Navigate to project directory
cd /home/shuma/Documents/AI_Suite/TCM_Knowledge_Base

# Run pipeline
python scripts/deep_research_pipeline.py \
  --topic "Spleen Qi Deficiency" \
  --project "Traditional Chinese Medicine" \
  --template "OCDS_Documentation/05_Material_Templates/Root_Note_Template.md" \
  --class-id "TCM_101"
```

**That's it!** The pipeline will:
- Generate research prompt (AI)
- Conduct deep research (Gemini with search)
- Parse template headings
- Generate content for each section (AI)
- Fill template
- Create root note
- Generate flashcards, quiz, slides, study guide, tasks
- Package everything in `Materials/TCM_101/`

---

## 📊 Output

After running, you'll have:

```
Materials/TCM_101/
├── Root_Note_Spleen_Qi_Deficiency.md  # Complete root note
├── Flashcards.md                       # ~20 flashcards
├── Quiz.md                             # ~6 questions
├── Slides.md                           # ~10 slides
├── Study_Material.md                   # Study guide
└── Tasks.md                            # Task checklist
```

---

## 🎯 Common Use Cases

### **1. TCM Pattern**

```bash
python scripts/deep_research_pipeline.py \
  --topic "Liver Qi Stagnation" \
  --project "Traditional Chinese Medicine" \
  --template "OCDS_Documentation/05_Material_Templates/Root_Note_Template.md" \
  --class-id "TCM_101"
```

### **2. Biology Topic**

```bash
python scripts/deep_research_pipeline.py \
  --topic "Photosynthesis" \
  --project "Biology" \
  --template "templates/Biology_Template.md" \
  --class-id "BIO_101"
```

### **3. Custom Output Directory**

```bash
python scripts/deep_research_pipeline.py \
  --topic "Spleen Qi Deficiency" \
  --project "Traditional Chinese Medicine" \
  --template "OCDS_Documentation/05_Material_Templates/Root_Note_Template.md" \
  --class-id "TCM_101" \
  --output-dir "Materials/TCM_101/Week_02"
```

### **4. Exhaustive Research (More Detailed)**

```bash
python scripts/deep_research_pipeline.py \
  --topic "Spleen Qi Deficiency" \
  --project "Traditional Chinese Medicine" \
  --template "OCDS_Documentation/05_Material_Templates/Root_Note_Template.md" \
  --class-id "TCM_101" \
  --depth exhaustive
```

### **5. Root Note Only (Skip Materials)**

```bash
python scripts/deep_research_pipeline.py \
  --topic "Spleen Qi Deficiency" \
  --project "Traditional Chinese Medicine" \
  --template "OCDS_Documentation/05_Material_Templates/Root_Note_Template.md" \
  --skip-materials
```

---

## 🔧 Advanced Options

### **All Command-Line Options**

```bash
python scripts/deep_research_pipeline.py \
  --topic "TOPIC_NAME" \              # Required: Research topic
  --project "PROJECT_NAME" \          # Required: Domain/project
  --template "TEMPLATE_PATH" \        # Required: Template file
  --class-id "CLASS_ID" \             # Optional: Class ID
  --output-dir "OUTPUT_PATH" \        # Optional: Output directory
  --depth [quick|comprehensive|exhaustive] \  # Optional: Research depth
  --no-prompt-generation \            # Optional: Skip AI prompt generation
  --skip-materials                    # Optional: Only create root note
```

### **Research Depth Levels**

- **quick** - Essential information only (~5 min)
- **comprehensive** - Detailed coverage (default, ~15 min)
- **exhaustive** - Maximum detail (~30 min)

---

## 🛠️ Individual Components

You can also use components separately:

### **1. Generate Research Prompt Only**

```bash
python scripts/research_prompt_generator.py \
  --topic "Spleen Qi Deficiency" \
  --project "Traditional Chinese Medicine" \
  --template "Root_Note_Template.md" \
  --output "prompts/spleen_prompt.txt"
```

### **2. Conduct Research Only**

```bash
python scripts/gemini_research.py \
  --topic "Spleen Qi Deficiency" \
  --project "Traditional Chinese Medicine" \
  --depth comprehensive \
  --output "research/spleen_research.md"
```

### **3. Parse Template**

```bash
python scripts/template_parser.py "Root_Note_Template.md"
```

---

## 📝 Custom Templates

You can create custom templates for any subject:

1. **Copy the base template:**
   ```bash
   cp OCDS_Documentation/05_Material_Templates/Root_Note_Template.md \
      templates/My_Custom_Template.md
   ```

2. **Edit headings** to match your subject
   - Keep the frontmatter structure
   - Modify body headings as needed
   - Add domain-specific sections

3. **Use your template:**
   ```bash
   python scripts/deep_research_pipeline.py \
     --topic "Your Topic" \
     --project "Your Domain" \
     --template "templates/My_Custom_Template.md" \
     --class-id "YOUR_CLASS"
   ```

---

## 🎯 Workflow Integration

### **Complete Content Creation Workflow**

```
1. Set API Key
   export GEMINI_API_KEY="your-key"

2. Run Pipeline
   python scripts/deep_research_pipeline.py \
     --topic "Topic" \
     --project "Domain" \
     --template "Template.md" \
     --class-id "CLASS_101"

3. Review Output
   - Check root note
   - Review flashcards
   - Test quiz

4. Add to Dashboard
   - Link from Student Dashboard
   - Test tracking

5. Deploy to Students
   - Materials ready!
```

---

## ⚠️ Troubleshooting

### **"GEMINI_API_KEY not set"**

```bash
# Set API key
export GEMINI_API_KEY="your-api-key-here"

# Or add to ~/.bashrc for persistence
echo 'export GEMINI_API_KEY="your-key"' >> ~/.bashrc
source ~/.bashrc
```

### **"Template not found"**

Use absolute or relative path from project root:
```bash
--template "OCDS_Documentation/05_Material_Templates/Root_Note_Template.md"
```

### **"Import errors"**

Make sure you're in the project directory:
```bash
cd /home/shuma/Documents/AI_Suite/TCM_Knowledge_Base
python scripts/deep_research_pipeline.py ...
```

### **API Rate Limits**

If you hit rate limits:
- Use `--depth quick` for faster processing
- Wait a few minutes between runs
- Consider upgrading API tier

---

## 💡 Tips & Best Practices

### **1. Topic Naming**
- Be specific: "Spleen Qi Deficiency" not just "Spleen"
- Use standard terminology
- Match your domain conventions

### **2. Template Selection**
- Use domain-specific templates when available
- TCM topics → Root_Note_Template.md
- Other subjects → Create custom template

### **3. Research Depth**
- Start with `comprehensive` (default)
- Use `exhaustive` for complex topics
- Use `quick` for simple overviews

### **4. Output Organization**
- Use `--class-id` to organize by class
- Use `--output-dir` for custom organization
- Keep related topics in same directory

### **5. Review Before Deploying**
- Always review generated root note
- Check flashcards for accuracy
- Test quiz questions
- Verify all materials generated

---

## 📊 Expected Results

### **Processing Time**

| Depth | Research | Content Gen | Total |
|-------|----------|-------------|-------|
| Quick | ~2 min | ~3 min | ~5 min |
| Comprehensive | ~5 min | ~10 min | ~15 min |
| Exhaustive | ~10 min | ~20 min | ~30 min |

### **Generated Content**

| Material | Typical Count |
|----------|---------------|
| Root Note | 1 complete file |
| Flashcards | 15-25 cards |
| Quiz Questions | 5-10 questions |
| Slides | 8-12 slides |
| Study Guide | 1 comprehensive |
| Tasks | 4-6 tasks |

---

## 🚀 Next Steps

After generating your first package:

1. **Review Quality**
   - Read through root note
   - Check accuracy of information
   - Verify all sections filled

2. **Test Materials**
   - Review flashcards in Obsidian
   - Test quiz auto-grading
   - Preview slides

3. **Integrate with OCDS**
   - Add to Student Dashboard
   - Link from class page
   - Test progress tracking

4. **Generate More Content**
   - Create additional topics
   - Build complete curriculum
   - Organize by weeks/modules

---

## 📞 Support

### **Common Issues**

See Troubleshooting section above.

### **Documentation**

- **Full System Docs:** `DEEP_RESEARCH_PIPELINE_STATUS.md`
- **Content Generation:** `CONTENT_GENERATION_SYSTEM_COMPLETE.md`
- **OCDS System:** `OCDS_Documentation/`

### **Component Docs**

- Template Parser: `scripts/template_parser.py --help`
- Gemini Research: `scripts/gemini_research.py --help`
- Prompt Generator: `scripts/research_prompt_generator.py --help`
- Main Pipeline: `scripts/deep_research_pipeline.py --help`

---

## ✅ Success Checklist

- [ ] API key set (`echo $GEMINI_API_KEY`)
- [ ] In project directory
- [ ] Template file exists
- [ ] Run pipeline command
- [ ] Check output directory
- [ ] Review root note
- [ ] Test materials
- [ ] Add to dashboard

---

**Ready to generate your first complete class package!** 🎉

Run the basic command and watch the AI create comprehensive educational materials in ~15 minutes.

---

*Last updated: 2025-11-07*  
*Pipeline Version: 1.0.0*
