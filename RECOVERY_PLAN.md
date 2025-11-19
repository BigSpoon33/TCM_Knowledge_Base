# Complete Recovery Plan

## 🎯 What We Have

### ✅ Still Intact (100%)
- ✅ All 35 Python scripts in `scripts/`
- ✅ All 81 documentation files in `OCDS_Documentation/`
- ✅ All 10 templates in `OCDS_Documentation/05_Material_Templates/`
- ✅ Pattern template: `TCM_Patterns/TEMPLATE_Pattern.md`
- ✅ Working Capsule CLI (just rebuilt!)
- ✅ Week-old backup of TCM files

### 📊 Current Status
- ✅ **347 Pattern files** (you've been creating these!)
- ✅ **77 Herb files** (partial)
- ✅ **42 Formula files** (partial)
- ✅ **19 Point files** (partial)

### 📦 What We Can Rebuild
- 🔄 Missing ~217 herbs
- 🔄 Missing ~325 points
- 🔄 Missing ~94 formulas
- 🔄 Any other missing TCM content

---

## 🛠️ Available Tools for Rebuilding

### 1. PDF Extraction Scripts (For Textbook Content)

```bash
# Extract herb information from Bensky
scripts/extract_herb_bensky.py
scripts/extract_herbs_bensky.py

# Extract formulas from Bensky
scripts/extract_formulas_bensky_ocr.py

# Extract patterns from Maciocia Foundations
scripts/extract_foundations_patterns.py
scripts/extract_foundations_improved.py

# Extract diagnosis content
scripts/extract_diagnosis_auto.py
scripts/extract_maciocia_diagnosis.py
```

### 2. AI Generation Scripts (For Creating Content)

```bash
# Generate flashcards for herbs/formulas/points
scripts/generate_herb_flashcards.py
scripts/generate_formula_flashcards.py
scripts/generate_point_flashcards.py

# Content generation
scripts/content_generator.py

# Deep research
scripts/deep_research_pipeline.py
scripts/gemini_research.py
```

### 3. Enhancement Scripts (For Polishing)

```bash
# Auto-link symptoms
scripts/auto_link_symptoms.py

# Enhance symptom files
scripts/enhance_symptoms.py
```

### 4. Capsule CLI (We Just Built!)

```bash
# Deep research to create new content
capsule research "topic" --deep

# Generate materials
capsule generate "pattern"

# Interactive learning
capsule conversation "pattern"
```

---

## 🗺️ Recovery Strategy

### Phase 1: Restore from Week-Old Backup (FASTEST)

```bash
# 1. Locate your week-old backup
# (wherever you have it stored)

# 2. Copy files back
cp -r /path/to/backup/TCM_Herbs/* TCM_Herbs/
cp -r /path/to/backup/TCM_Points/* TCM_Points/
cp -r /path/to/backup/TCM_Formulas/* TCM_Formulas/

# 3. Check what's restored
find TCM_Herbs -name "*.md" | wc -l
find TCM_Points -name "*.md" | wc -l
find TCM_Formulas -name "*.md" | wc -l
```

**Time:** 5 minutes  
**Cost:** $0  
**Result:** Most content restored

---

### Phase 2: Extract Missing Content from PDFs (MEDIUM)

For any files not in the backup:

```bash
# Extract herbs from Bensky
python scripts/extract_herbs_bensky.py \
  --pdf "Books/Bensky - Materia Medica.pdf" \
  --output TCM_Herbs/

# Extract formulas from Bensky
python scripts/extract_formulas_bensky_ocr.py \
  --pdf "Books/Bensky - Formulas and Strategies.pdf" \
  --output TCM_Formulas/

# Extract point info
# (if you have a points textbook PDF)
```

**Time:** 1-2 hours (mostly automated)  
**Cost:** $0 (no AI, just PDF extraction)  
**Result:** Textbook-based content restored

---

### Phase 3: AI-Generate Any Remaining Content (SLOWEST)

For files that aren't in backup or PDFs:

#### Option A: Use Capsule CLI

```bash
# Create a new command for this
capsule create-herb "Herb Name"
capsule create-formula "Formula Name"
capsule create-point "Point Name"
```

#### Option B: Batch AI Generation

```bash
# Create a list of missing items
cat > missing_herbs.txt << 'LIST'
Herb 1
Herb 2
Herb 3
LIST

# Generate with AI
while read herb; do
  capsule research "$herb" --deep
done < missing_herbs.txt
```

**Time:** Depends on count (5-10 min per item)  
**Cost:** AI tokens (~$0.01-0.05 per item with Gemini)  
**Result:** Complete, detailed content

---

## 💡 Recommended Workflow

### Step 1: Restore Backup (DO THIS FIRST)

```bash
# Find your backup
ls -la ~/backups/  # or wherever you backed up
ls -la /path/to/external/drive/

# Copy everything back
cp -r /backup/path/TCM_Knowledge_Base/TCM_Herbs/* TCM_Herbs/
cp -r /backup/path/TCM_Knowledge_Base/TCM_Points/* TCM_Points/
cp -r /backup/path/TCM_Knowledge_Base/TCM_Formulas/* TCM_Formulas/
```

### Step 2: Identify Gaps

```bash
# See what's still missing
cd TCM_Herbs && ls *.md | wc -l  # Should be ~294
cd TCM_Points && ls *.md | wc -l  # Should be ~344
cd TCM_Formulas && ls *.md | wc -l  # Should be ~136

# Find what changed in the last week
# (these might not be in backup)
find TCM_Herbs -name "*.md" -mtime -7
find TCM_Points -name "*.md" -mtime -7
find TCM_Formulas -name "*.md" -mtime -7
```

### Step 3: Fill Gaps Strategically

**For High-Priority Items:**
- Use AI generation (fastest, most complete)

**For Textbook-Based Content:**
- Use PDF extraction scripts (accurate, free)

**For Low-Priority Items:**
- Generate as needed when you study them

---

## 📋 Checklist

### Immediate Actions

- [ ] Locate week-old backup
- [ ] Restore TCM_Herbs/ from backup
- [ ] Restore TCM_Points/ from backup
- [ ] Restore TCM_Formulas/ from backup
- [ ] Count files to verify restoration
- [ ] Identify any gaps

### Optional Enhancements

- [ ] Extract additional content from PDFs
- [ ] AI-generate missing items
- [ ] Update auto-linking (run auto_link_symptoms.py)
- [ ] Enhance symptom files (run enhance_symptoms.py)

### Future Protection

- [ ] Set up automatic git commits (cron job?)
- [ ] Set up cloud backup (Dropbox, Google Drive, etc.)
- [ ] Create weekly backup script
- [ ] Document backup locations

---

## 🎯 Quick Recovery Commands

```bash
# === STEP 1: RESTORE FROM BACKUP ===
# (Replace /path/to/backup with your actual backup location)

cp -r /path/to/backup/TCM_Herbs/* TCM_Herbs/
cp -r /path/to/backup/TCM_Points/* TCM_Points/
cp -r /path/to/backup/TCM_Formulas/* TCM_Formulas/

# === STEP 2: VERIFY ===

echo "Herbs: $(find TCM_Herbs -name '*.md' | wc -l)"
echo "Points: $(find TCM_Points -name '*.md' | wc -l)"
echo "Formulas: $(find TCM_Formulas -name '*.md' | wc -l)"
echo "Patterns: $(find TCM_Patterns -name '*.md' ! -name 'TEMPLATE*' ! -name '00*' | wc -l)"

# === STEP 3: COMMIT ===

git add TCM_Herbs/ TCM_Points/ TCM_Formulas/ TCM_Patterns/
git commit -m "Restored from backup + current work"
git push

# === STEP 4: AUTO-ENHANCE ===

python scripts/auto_link_symptoms.py
python scripts/enhance_symptoms.py

# Done! 🎉
```

---

## 💰 Cost Estimate

If you need to AI-generate missing content:

| Item Type | Count to Generate | Time per Item | Cost per Item | Total |
|-----------|------------------|---------------|---------------|-------|
| Herbs | ~50 (if not in backup) | 5 min | $0.02 | $1 |
| Points | ~100 (if not in backup) | 3 min | $0.01 | $1 |
| Formulas | ~30 (if not in backup) | 7 min | $0.03 | $0.90 |
| **TOTAL** | ~180 items | ~12 hours | | **~$3** |

**With backup:** Most items restored for FREE!  
**Without backup:** ~$3 and 12 hours of mostly automated work

---

## 🚀 Next Steps

1. **Find your backup** - Check:
   - External drives
   - Cloud storage (Dropbox, Google Drive, OneDrive)
   - Time Machine / Windows Backup
   - Other computers
   - Email attachments
   - GitHub (if you pushed before the reset)

2. **Restore files** - Copy everything back

3. **Verify restoration** - Count files

4. **Commit immediately** - Save to git

5. **Set up better backups** - Prevent this in future

---

## 🎓 What We Learned

### Backup Strategy Going Forward

```bash
# Create a daily backup script
cat > backup.sh << 'SCRIPT'
#!/bin/bash
DATE=$(date +%Y%m%d)
BACKUP_DIR=~/TCM_Backups/$DATE

mkdir -p $BACKUP_DIR
cp -r TCM_Herbs/ $BACKUP_DIR/
cp -r TCM_Points/ $BACKUP_DIR/
cp -r TCM_Formulas/ $BACKUP_DIR/
cp -r TCM_Patterns/ $BACKUP_DIR/
cp -r capsule/ $BACKUP_DIR/
cp -r scripts/ $BACKUP_DIR/

echo "✅ Backup created: $BACKUP_DIR"
SCRIPT

chmod +x backup.sh

# Run daily
# Add to crontab: 0 22 * * * cd ~/TCM_Knowledge_Base && ./backup.sh
```

### Git Best Practices

```bash
# Commit frequently
git add .
git commit -m "Daily progress"
git push

# Create branches for risky operations
git checkout -b experimental
# do risky stuff
git checkout main  # go back if it fails
```

---

## 💪 You've Got This!

- ✅ All scripts intact
- ✅ Templates intact
- ✅ CLI working
- ✅ Backup exists (week old)
- ✅ Knowledge of how to rebuild

**This is recoverable!** It's just a matter of:
1. Restoring from backup (5 min)
2. Filling any gaps (optional)
3. Setting up better backups

You'll be back to 100% in no time! 🎉

---

**Status:** Recovery plan ready  
**Next Step:** Locate and restore from backup  
**Time to Recovery:** ~5 minutes to several hours (depending on backup status)
