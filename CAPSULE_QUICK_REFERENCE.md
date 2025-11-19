# Capsule CLI - Quick Reference

## ✅ Successfully Recovered!

All functionality has been restored from the git history loss.

## 🚀 Quick Start

### List Available Patterns
```bash
capsule list                    # List all 359+ patterns
cap list | grep -i kidney       # Filter patterns
```

### Configuration
```bash
capsule config set api.gemini_key "your-key"
capsule config list
capsule config path
```

### Generate Materials
```bash
# Generate all materials for a pattern
capsule generate "Kidney Yang Deficiency"
cap gen "Heart Blood Deficiency" --class-id TCM_201

# Skip specific materials
cap gen "Lung Yin Deficiency" --skip-slides --skip-conversation
```

### Guided Conversations
```bash
# Interactive conversation
capsule conversation "Kidney Yang Deficiency"

# Generate script only
cap chat "Spleen Qi Deficiency" --script
```

### Research
```bash
# Standard research
capsule research "Liver Qi Stagnation"

# Deep research
cap study "Wind-Heat" --deep
```

## 📋 All Commands

| Command | Aliases | Description |
|---------|---------|-------------|
| `capsule` | `cap` | Main command |
| `generate` | `gen` | Generate learning materials |
| `conversation` | `chat` | Start guided conversation |
| `research` | `study` | Research topics |
| `list` | - | List available patterns |
| `config` | - | Manage configuration |

## 🔧 Configuration

Config file: `~/.config/capsule/config.yaml`

```yaml
api:
  gemini_key: your-key-here

paths:
  knowledge_base: /path/to/TCM_Knowledge_Base
  output_dir: Materials

defaults:
  class_id: TCM_101
  max_attempts: 3
  template: TCM_Pattern_Template_Simple.md
```

## ✨ Features

- ✅ 359+ TCM patterns supported
- ✅ Beautiful terminal output with colors and tables
- ✅ Smart pattern matching with suggestions
- ✅ YAML configuration management
- ✅ Short command aliases (gen, chat, study)
- ✅ Integration with existing scripts
- ✅ Fuzzy pattern matching
- ✅ Nested directory support

## 📦 Files Recovered

```
capsule/
├── __init__.py
├── cli.py
├── commands/
│   ├── __init__.py
│   ├── config.py
│   ├── list.py
│   ├── generate.py
│   ├── conversation.py
│   └── research.py
└── utils/
    ├── __init__.py
    ├── config.py
    ├── output.py
    └── validation.py

setup.py
.gitignore
```

## 🎯 Examples

### Complete Workflow
```bash
# 1. Configure
capsule config set api.gemini_key "AIza..."

# 2. List patterns
capsule list | grep -i lung

# 3. Generate materials
cap gen "Lung Yin Deficiency"

# 4. Study with conversation
cap chat "Lung Yin Deficiency"

# 5. Research related topics
cap study "Lung Patterns" --deep
```

---

**Status**: ✅ Fully Operational  
**Date Recovered**: 2025-11-08  
**Patterns Available**: 359+

---

## ⚠️ Important: File Overwriting Behavior

### What Happens to Existing Files?

**BY DEFAULT, THE CLI WILL ASK BEFORE OVERWRITING:**

#### Research Command
If a root note already exists for a topic:
```bash
$ capsule research "Kidney Yang Deficiency"

⚠️  Warning: Root note already exists: Materials/TCM_101/Root_Note_Kidney_Yang_Deficiency.md
? Overwrite existing root note? (y/N)
```

- **Answer 'n' (No)**: Research cancelled, existing file preserved
- **Answer 'y' (Yes)**: Old file is **completely overwritten** with new research

#### Generate Command
If materials already exist for a pattern:
```bash
$ capsule generate "Kidney Yang Deficiency"

⚠️  Warning: Found 1 existing material(s) for 'Kidney Yang Deficiency':
   - Root_Note_Kidney_Yang_Deficiency.md
? Overwrite existing materials? (y/N)
```

- **Answer 'n' (No)**: Generation cancelled, existing files preserved
- **Answer 'y' (Yes)**: Old files are **completely overwritten** with new materials

### Best Practices

1. **Check what exists first**:
   ```bash
   ls Materials/TCM_101/*Kidney_Yang*.md
   ```

2. **Use custom output paths** to avoid overwriting:
   ```bash
   capsule research "Kidney Yang Deficiency" --output "Research_v2.md"
   ```

3. **Back up important files** before regenerating:
   ```bash
   cp Materials/TCM_101/Root_Note_*.md ~/backups/
   ```

4. **Use version control** (git) to track changes and revert if needed

### The CLI Does NOT:

- ❌ Create backups automatically
- ❌ Merge with existing content
- ❌ Append to existing files
- ❌ Use existing files as input

### The CLI DOES:

- ✅ Warn you before overwriting
- ✅ Ask for confirmation
- ✅ Show which files will be affected
- ✅ Allow you to cancel safely

---

**Last Updated**: 2025-11-08  
**Safety Features Added**: File overwrite protection
