---
id: pattern-20251115-next-steps
name: NEXT STEPS
type: pattern
aliases: []
tags:
- TCM
- Pattern
category: []
related: []
symptoms: []
patterns: []
western_conditions: []
formulas: []
herbs: []
points: []
nutrition: []
tests: []
created: 2025-11-15
updated: 2025-11-15

---


### Option 2: Work on Symptom Files (High Priority)
**What:** Apply the same standardization process to TCM_Symptoms folder
**Why:** Symptoms likely have similar issues (duplicates, incomplete files)
**Process:**
1. Check for duplicate symptom files
2. Merge backups with existing files
3. Standardize naming conventions
4. Ensure comprehensive content

---

### Option 3: Enhance Stub Patterns (Medium Priority)
**What:** Use deep_research_pipeline.py to enhance patterns that are still stubs
**Why:** Many patterns only have basic info (formulas/acu points) but lack:
- Clinical manifestations
- Etiology & pathomechanisms
- Diagnostic criteria
- Treatment principles
- Differential diagnosis

**How:** (Need API key)
```bash
export GEMINI_API_KEY='your-key'

# `=this.name`
python scripts/deep_research_pipeline.py \
  --topic "Pattern Name" \
  --project "Traditional Chinese Medicine" \
  --template "TCM_Patterns/TEMPLATE_Pattern.md" \
  --skip-materials
```

---

### Option 4: Review Pattern Naming Consistency
**What:** Quick review to ensure all pattern names are standardized
**Check for:**
- Inconsistent capitalization
- Duplicates we might have missed
- Files that should be renamed
- Patterns in wrong folders

**Examples to check:**
- "Liver And Kidney Yin Deficiency" vs "Liver-Kidney Yin Deficiency"
- Files with "&" vs "And" vs "-"
- Files with ".." in the name

---

### Option 5: Handle Other Pattern Folders
**What:** Apply same process to other pattern folders:
- Qi, Blood, and Body Fluids Patterns/
- Eight Principles Patterns/
- Channel Patterns/
- Five Elements Patterns/
- Shang Han Lun Patterns/
- San Jiao Patterns/

**Why:** These folders likely have similar issues

---

## 📝 My Recommendation: Priority Order

**1. Run Auto-Linking (30 min)**
- Quick win
- Immediately improves vault navigation
- No API key needed

**2. Standardize Symptom Files (2-3 hours)**
- Similar process to what we just did
- High impact on vault usability
- Should be done before comprehensive pattern enhancement

**3. Review & Fix Pattern Naming (1 hour)**
- Clean up any remaining inconsistencies
- Merge any missed duplicates
- Standardize "&" vs "And" vs "-"

**4. Enhance Stub Patterns (ongoing, needs API)**
- Long-term project
- Use deep_research_pipeline.py
- Create comprehensive versions like "Bladder Damp Turbidity"

**5. Other Pattern Folders (as needed)**
- Apply lessons learned
- Systematic cleanup

---

## 🤔 What Should We Do Next?

I recommend we:
1. **First:** Run auto_link_symptoms.py to link everything
2. **Then:** Work on standardizing the TCM_Symptoms folder (same process)
3. **After that:** You provide the API key and we enhance stub patterns

What would you like to do next?

