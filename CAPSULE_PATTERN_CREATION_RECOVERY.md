# Pattern File Creation - Recovery Guide

## 🎯 What You Had

Looking at your pattern files (e.g., Bladder Damp Turbidity), you had a sophisticated system for creating TCM pattern documentation with:

1. **Rich Frontmatter** - Extensive YAML metadata
2. **Structured Content** - Consistent sections with emojis
3. **Cross-linking** - Wikilinks to symptoms, herbs, formulas, points
4. **Dataview Queries** - Dynamic content from linked notes
5. **Created Recently** - Most files from Nov 3-4, 2025

---

## 📋 Pattern File Structure

### Frontmatter Sections

```yaml
---
# Core Metadata
id: pattern-20251104-bladder-damp-turbidity
name: Bladder Damp Turbidity
type: pattern
aliases: [UB Damp Turbidity, ...]
tags: [TCM, Pattern, Zang-Fu, ...]

# Cross-Links (THE KEY TO YOUR SYSTEM!)
category: [Zang Fu, Bladder Patterns, ...]
related: [Bladder Damp-Heat, ...]
symptoms: ['[[Turbid Urine]]', '[[Cloudy Urine]]', ...]
formulas: [Bi Xie Fen Qing Yin, ...]
herbs: [Bi Xie, Shi Chang Pu, ...]
points: [SP-9, SP-6, RN-3, ...]

# Pattern Data (Structured Information)
pattern_data:
  pattern_type: Zang Fu
  pattern_subtype: Urinary Bladder
  excess_deficiency: Excess
  hot_cold: Neither
  etiology: [...]
  pathomechanisms: [...]
  cardinal_symptoms: [...]
  tongue: "Pale or normal tongue..."
  pulse: "Slippery, soggy, or weak"
  treatment_principle: [...]
  contraindications: [...]

created: 2025-11-04
updated: 2025-11-04
---
```

### Content Sections

```markdown
# 🔮 Pattern Name

## 📖 Overview
## 🎯 Pattern Classification  
## 🧬 Etiology & Pathogenesis
## 🔍 Clinical Manifestations
## 🎯 Diagnostic Criteria
## 🔬 Differential Diagnosis
## 💊 Treatment Approach
## ⚠️ Contraindications & Cautions
## 🔄 Pattern Variations
## 🏥 Western Medical Correlates
## 📚 Classical Sources
## 💡 Clinical Pearls
## 🔗 Related Notes (Dataview queries)
## 📊 Pattern Comparison Table
## 🎓 Study Notes
## 📖 References
```

---

## 🛠️ Available Scripts for Pattern Creation

### 1. PDF Extraction Scripts

```bash
scripts/extract_foundations_patterns.py
scripts/extract_diagnosis_auto.py
scripts/extract_diagnosis_sections.py
scripts/extract_maciocia_diagnosis.py
```

**What they do:**
- Extract text from TCM textbooks (Maciocia Foundations, Diagnosis)
- Handle complex layouts, tables, images
- Use PDF bookmarks/TOC for automatic section detection
- Save extracted content as markdown

**Example usage:**
```bash
# Extract pattern from Foundations book
python scripts/extract_foundations_patterns.py \
  --section "Bladder Patterns" \
  --start-page 450 \
  --end-page 470
```

### 2. Content Enhancement Scripts

```bash
scripts/enhance_symptoms.py
scripts/auto_link_symptoms.py
```

**What they do:**
- `enhance_symptoms.py`: Add pattern-specific info to symptom files
- `auto_link_symptoms.py`: Automatically create wikilinks for symptoms

**Example usage:**
```bash
# Auto-link symptoms in pattern files
python scripts/auto_link_symptoms.py

# Enhance symptom files with pattern data
python scripts/enhance_symptoms.py
```

### 3. Pattern Templates

```
TCM_Patterns/TEMPLATE_Pattern.md       # Full template
TCM_Patterns/EXAMPLE_Blood_Stasis_Heart.md  # Example
```

---

## 🔄 Likely Creation Workflow

Based on the files and scripts, here's what you probably did:

### Method 1: Manual Creation from Template

```bash
# 1. Copy template
cp TCM_Patterns/TEMPLATE_Pattern.md "TCM_Patterns/Zang Fu Patterns/New Pattern.md"

# 2. Fill in frontmatter manually
# - Set id, name, aliases
# - Add symptoms list
# - Add formulas, herbs, points
# - Fill pattern_data fields

# 3. Write content sections
# - Overview
# - Clinical manifestations
# - Treatment, etc.

# 4. Auto-link symptoms
python scripts/auto_link_symptoms.py
```

### Method 2: Extract from PDF + Enhance

```bash
# 1. Extract pattern from textbook
python scripts/extract_foundations_patterns.py \
  --section "Bladder Patterns" \
  --start-page 450 \
  --end-page 470

# 2. Copy extracted content to template
# 3. Add frontmatter manually
# 4. Format and enhance
# 5. Auto-link symptoms
python scripts/auto_link_symptoms.py
```

### Method 3: AI-Assisted Creation (Most Likely!)

Given that files were created Nov 3-4 and look very consistent, you probably:

```bash
# 1. Used AI (Gemini) to generate initial content
# 2. Used template structure
# 3. AI filled in:
#    - Frontmatter fields
#    - All content sections
#    - Symptom lists with wikilinks
#    - Formula/herb/point recommendations
# 4. Ran auto_link_symptoms.py to finalize links
```

---

## 💡 How to Recreate Pattern Files

### Option A: Add to Capsule CLI

Create a new command:
```bash
capsule create-pattern "Pattern Name"
```

**What it would do:**
1. Use template: TCM_Patterns/TEMPLATE_Pattern.md
2. AI generates content for all sections
3. AI fills frontmatter (symptoms, formulas, herbs, points)
4. Saves to TCM_Patterns/[Category]/Pattern Name.md
5. Runs auto_link_symptoms.py

### Option B: Use Deep Research with Pattern Template

```bash
# Create new pattern template for deep research
cp TCM_Patterns/TEMPLATE_Pattern.md \
   OCDS_Documentation/05_Material_Templates/Pattern_Creation_Template.md

# Then use:
capsule research "New Pattern" --deep --template Pattern_Creation_Template.md
```

### Option C: Manual Script

Create a new script:
```bash
scripts/create_pattern.py
```

That:
1. Takes pattern name as input
2. Uses Gemini to research the pattern
3. Fills template with AI-generated content
4. Saves to appropriate category folder
5. Auto-links symptoms

---

## 🎯 Next Steps to Recover Functionality

### High Priority

1. **Create `capsule create-pattern` command**
   - Use TEMPLATE_Pattern.md
   - AI-generate all sections
   - Auto-fill frontmatter
   - Save to correct category

2. **Integrate with existing scripts**
   - Call auto_link_symptoms.py automatically
   - Use enhance_symptoms.py after creation

### Medium Priority

3. **Batch pattern creation**
   - Read list of patterns to create
   - Create multiple at once

4. **Pattern update command**
   - Update existing patterns
   - Preserve manual edits

### Documentation Needed

5. **Document the workflow**
   - How patterns were created
   - Best practices
   - Template guide

---

## 📊 Pattern File Statistics

```bash
# Count pattern files
find TCM_Patterns -name "*.md" ! -name "TEMPLATE*" ! -name "EXAMPLE*" | wc -l
# Result: ~359 patterns

# Recent patterns (Nov 3-4)
find TCM_Patterns -name "*.md" -mtime -7 | wc -l
# Result: ~15 recent patterns

# Categories
ls -d TCM_Patterns/*/
# Result: Multiple category folders
```

---

## 🔧 Template Key Features

### Frontmatter Powers Obsidian

- **Wikilinks** - `[[Symptom Name]]` creates bidirectional links
- **Dataview** - Dynamic queries pull related content
- **Metadata** - Rich structured data for queries
- **Tags** - Organize and filter patterns

### Content Follows TCM Structure

1. Overview - Brief intro
2. Classification - Eight Principles
3. Etiology - Causes
4. Pathogenesis - How it develops
5. Manifestations - Signs and symptoms
6. Diagnosis - How to identify
7. Differential - vs similar patterns
8. Treatment - Formulas, herbs, points
9. Clinical pearls - Practical tips

---

## 💾 What You Have Right Now

✅ **Template** - TCM_Patterns/TEMPLATE_Pattern.md
✅ **Example** - TCM_Patterns/EXAMPLE_Blood_Stasis_Heart.md
✅ **15+ Perfect Examples** - In Zang Fu Patterns folder
✅ **Extraction Scripts** - For textbook content
✅ **Enhancement Scripts** - For auto-linking
✅ **359 Pattern Files** - Various stages of completion

---

## 🚀 Recommended Action

**Create the pattern creation command NOW:**

```python
# capsule/commands/create_pattern.py

@click.command(name='create-pattern')
@click.argument('pattern_name')
@click.option('--category', help='Pattern category')
def create_pattern_cmd(pattern_name: str, category: str):
    """Create a new TCM pattern file from template.
    
    Uses AI to generate complete pattern documentation.
    """
    # 1. Load template
    # 2. Use Gemini to research pattern
    # 3. Fill all sections with AI
    # 4. Fill frontmatter (symptoms, formulas, etc.)
    # 5. Save to TCM_Patterns/{category}/{name}.md
    # 6. Run auto_link_symptoms.py
```

This would let you do:
```bash
capsule create-pattern "Liver Blood Deficiency" --category "Zang Fu Patterns"
```

And get a perfectly formatted pattern file in ~5 minutes! 🎉

---

**Status:** Pattern creation workflow identified  
**Next:** Implement `create-pattern` command in Capsule CLI
