---
id: pattern-20251115-pattern-standardization-plan
name: PATTERN STANDARDIZATION PLAN
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


## 🎯 Standardization Rules

### Naming Conventions
1. **Use Standard TCM Names** - Follow Maciocia/Bensky conventions
2. **Capitalization** - Title Case (e.g., "Spleen Qi Deficiency")
3. **Separators** - Use hyphens for compound patterns (e.g., "Damp-Heat")
4. **Arrows** - Use for transformations (e.g., "Liver Fire → Liver Wind")
5. **No Generic Labels** - Avoid "Empty:", "Full:", "Pattern:", etc. in final names

### Pattern Categories
- **Primary Patterns** - Single organ deficiency/excess (e.g., "Spleen Qi Deficiency")
- **Combination Patterns** - Two organs (e.g., "Spleen and Liver Blood Deficiency")
- **Transformation Patterns** - One leading to another (e.g., "Liver Fire → Liver Wind")
- **Pathogenic Patterns** - Specific pathogen (e.g., "Damp-Heat in Liver and Gallbladder")

---

## 📋 PART 1: Glob Files to Break Apart

These files contain multiple patterns that should be separate files:

### Bladder Patterns
**File:** `Bladder Full Patterns.md`  
**Action:** Break into separate files:
- → `Bladder Damp-Heat.md` (may already exist - merge)
- → `Bladder Damp-Cold.md` (may already exist - merge)
- → `Bladder Damp Turbidity.md` (already exists - good)
- → `Bladder Qi Stagnation.md` (if present in glob)

**File:** `Bladder Empty Patterns.md`  
**Action:** Break into:
- → `Bladder Qi Deficiency.md`
- → `Bladder Yang Deficiency.md`

---

### Gallbladder Patterns
**File:** `Gall Bladder Empty Patterns.md`  
**Action:** Break into:
- → `Gallbladder Qi Deficiency.md`
- → `Gallbladder Yin Deficiency.md` (if present)

**File:** Review and potentially merge:
- `Gallbladder Damp.md` - KEEP (if it's distinct from Damp-Heat)
- `Gallbladder Deficiency.md` - RENAME → `Gallbladder Qi Deficiency.md`
- `Depressed Gallbladder + Phlegm.md` - RENAME → `Gallbladder Deficiency with Phlegm.md`

---

### Kidney Patterns
**File:** `Kidney Empty Patterns.md`  
**Action:** Break into:
- → `Kidney Qi Deficiency.md`
- → `Kidney Yang Deficiency.md` (if not separate)
- → `Kidney Yin Deficiency.md` (if not separate)
- → `Kidney Essence Deficiency.md`

**File:** `Kidney Empty + Full Patterns.md`  
**Action:** Break into combination patterns:
- → `Kidney Yin Deficiency with Empty Fire.md`
- → Review what other combinations exist

**File:** `Kidney Combi Patterns.md`  
**Action:** Break into specific combinations:
- → `Kidney and Heart Not Harmonized.md`
- → `Kidney and Liver Yin Deficiency.md`
- → etc.

---

### Large Intestine Patterns
**File:** `Large Intestine Empty.md`  
**Action:** Break into:
- → `Large Intestine Qi Deficiency.md`
- → `Large Intestine Fluid Deficiency.md`

**File:** `Large Intestine Full.md`  
**Action:** Break into:
- → `Large Intestine Damp-Heat.md`
- → `Large Intestine Dry Heat.md`
- → `Large Intestine Qi Stagnation.md`
- → `Large Intestine Heat Obstruction.md` (Yang Ming Fu)

**File:** `Large Intestines Patterns.md` (note plural)  
**Action:** Review and merge with above or delete

---

### Small Intestine Patterns
**File:** `Small Intestine Empty.md`  
**Action:** Break into:
- → `Small Intestine Qi Deficiency.md`
- → `Small Intestine Deficiency and Cold.md` (already exists - merge)

**File:** `Small Intestine Full.md`  
**Action:** Break into:
- → `Small Intestine Qi Pain.md`
- → `Small Intestine Qi Tied.md`
- → `Small Intestine Heat.md`

**File:** `Small Intestine Patterns.md`  
**Action:** Review and merge or delete

---

### Heart Patterns
**File:** `Heart Empty.md`  
**Action:** Break into:
- → `Heart Qi Deficiency.md` (already exists - merge)
- → `Heart Yang Deficiency.md`
- → `Heart Blood Deficiency.md`
- → `Heart Yin Deficiency.md`

**File:** `Heart Full.md`  
**Action:** Break into:
- → `Heart Fire Blazing.md` (already exists - merge)
- → `Phlegm-Fire Harassing the Heart.md`
- → `Heart Blood Stasis.md` (already exists - merge)

**File:** `Heart E+f.md`  
**Action:** Unclear - review content, likely delete after breaking apart above

**File:** `Heart Patterns.md`  
**Action:** Review and delete if just a container

---

### Liver Patterns
**File:** `Liver Empty Patterns.md`  
**Action:** Break into:
- → `Liver Blood Deficiency.md` (already exists - merge)
- → `Liver Yin Deficiency.md` (already exists - merge)

**File:** `Liver Full Patterns.md`  
**Action:** Break into:
- → `Liver Fire Blazing.md` (already exists - merge)
- → `Liver Qi Stagnation.md` (already exists - merge)
- → `Liver Blood Stasis.md` (already exists - merge)
- → `Liver Damp-Heat.md` (already exists - merge)

**File:** `Liver Patterns.md`  
**Action:** Review and delete if just a container

---

### Lung Patterns
**File:** `Lung Empty.md`  
**Action:** Break into:
- → `Lung Qi Deficiency.md` (already exists - merge)
- → `Lung Yin Deficiency.md` (already exists - merge)

**File:** `Lung Full.md`  
**Action:** Break into:
- → `Lung Heat.md`
- → `Lung Dryness.md`
- → `Phlegm-Heat in the Lungs.md`
- → `Wind-Cold Invading Lungs.md`
- → `Wind-Heat Invading Lungs.md`

**File:** `Lung Combi.md`  
**Action:** Break into:
- → `Lung and Spleen Qi Deficiency.md` (may already exist)
- → `Lung and Kidney Yin Deficiency.md`

**File:** `Lung Patterns.md`  
**Action:** Review and delete if container

**File:** `Lung & Large Intestines.md`  
**Action:** Review - may be about relationship, not a pattern

---

### Pericardium Patterns
**File:** `Pericardium Empty.md`  
**Action:** Break into:
- → `Pericardium Blood Deficiency.md` (already exists - merge)
- → `Pericardium Qi Deficiency.md`

**File:** `Pericardium Full.md`  
**Action:** Break into:
- → `Pericardium Blood Stasis.md` (already exists - merge)
- → `Phlegm-Fire Harassing Pericardium.md`

---

### Spleen Patterns
**File:** `Spleen Patterns.md`  
**Action:** Review and delete if container

**File:** `Spleen & Stomach.md`  
**Action:** Review - may be about relationship or:
- → RENAME → `Spleen and Stomach Disharmony.md` (if pattern)

---

### Generic "Empty/Full" Files
**File:** `Empty: Control Blood.md`  
**Action:** RENAME → `Spleen Not Controlling Blood.md`

**File:** `Empty: Qi.md`  
**Action:** Review - likely delete (too generic)

**File:** `Empty: Qi Sinking.md`  
**Action:** RENAME → `Spleen Qi Sinking.md` (already exists - merge)

**File:** `Empty: Yang.md`  
**Action:** Review context:
- If Spleen: RENAME → `Spleen Yang Deficiency.md` (already exists - merge)
- If generic: delete

**File:** `Empty: Yin.md`  
**Action:** Review context:
- If Stomach: RENAME → `Stomach Yin Deficiency.md` (already exists - merge)
- If generic: delete

**File:** `Full: Blood Stasis.md`  
**Action:** Review context:
- If Stomach: RENAME → `Stomach Blood Stasis.md` (already exists - merge)
- If generic: Move to Qi/Blood/Body Fluids patterns

**File:** `Full: Cold Damp.md`  
**Action:** RENAME → `Cold-Damp Invading the Spleen.md` (already exists - merge)

**File:** `Full: Cold Fluid.md`  
**Action:** RENAME → `Cold Fluids Obstructing the Stomach.md`

**File:** `Full: Damp Heat.md`  
**Action:** Review context - likely:
- RENAME → `Spleen Damp-Heat.md` (already exists - merge)

**File:** `Full: Fire.md`  
**Action:** RENAME → `Stomach Fire.md` (already exists - merge)

**File:** `Full: Phlegm-fire.md`  
**Action:** RENAME → `Stomach Phlegm-Fire.md`

---

### Other Glob/Container Files
**File:** `Combined Patterns.md`  
**Action:** Review and break into specific combinations

**File:** `Differentiation - 3. Zang Fu.md`  
**Action:** Educational/reference - move to different folder or delete

**File:** `Qi, Blood, Body Fluids vs Zang Fu.md`  
**Action:** Educational/reference - review purpose

**File:** `Table of Contents.md`  
**Action:** Delete (outdated)

**File:** `Treatments for Zang Fu Patterns.md`  
**Action:** Educational/reference - move or keep as reference

**File:** `Zang Fu Pattern Comparison.md`  
**Action:** Educational/reference - keep as reference

---

## 📋 PART 2: Duplicates to Merge

### Spleen Qi Deficiency Group
**Standard Name:** `Spleen Qi Deficiency.md`  
**Files to Merge:**
- ✓ `Spleen Qi Deficiency.md` - KEEP as base
- ✗ `spleen qi deficiency1.md` - DELETE (case + duplicate)
- Review: `Stomach-spleen Qi Deficiency.md` - May be distinct pattern or merge

**Keep Separate:**
- `Spleen Qi Sinking.md` - Distinct pattern (complication of Qi Def)
- `Spleen Qi Deficiency with Damp Retention.md` - Distinct combination
- `Liver Qi Stagnation with Spleen Qi Deficiency.md` - Combination pattern

---

### Spleen Not Controlling Blood Group
**Standard Name:** `Spleen Not Controlling Blood.md`  
**Files to Merge:**
- ✓ `Spleen Not Controlling Blood.md` - KEEP
- ✗ `Spleen Not Controlling Blood1.md` - DELETE (duplicate)
- ✗ `Spleen unable to control blood.md` - DELETE (duplicate, different wording)
- ✗ `Empty: Control Blood.md` - DELETE (merged above)

---

### Heart Fire Group
**Standard Name:** `Heart Fire Blazing.md`  
**Files to Merge:**
- ✓ `Heart Fire Blazing.md` - KEEP as base
- Review context from glob files:
  - `Fire.md` - If about Heart Fire, merge
  - `Heart Fire.md` - If exists, merge
  - `Full: Fire.md` - Review context (might be Stomach Fire)

---

### Phlegm-Fire Harassing Heart Group
**Standard Name:** `Phlegm-Fire Harassing the Heart.md`  
**Files to Merge:**
- Choose ONE as base (suggest the longer one)
- ✗ `Phlegm Fire Harassing the Heart1.md` - DELETE
- ✗ `Phlegm-fire Harassing The Heart.md` - DELETE
- ✗ `Phlegm Fire.md` - DELETE (if same pattern)
- ✗ `Phlegm in the Heart.md` - DELETE (if same pattern)
- ✗ `Phlegm Misting the Mind.md` - KEEP SEPARATE (different focus - mental)
- ✗ `Phlegm Misting The Heart.md` - Review if same as above
- ✗ `phlegm misting the heart.md` - DELETE (case duplicate)
- ✗ `phlegm obstructing the heart orifices.md` - DELETE (same pattern)

---

### Liver Fire Group
**Standard Name:** `Liver Fire Blazing.md`  
**Files to Merge:**
- ✓ `Liver Fire Blazing.md` - KEEP as base
- ✗ `Liver Fire Flare-up.md` - MERGE (same pattern, different name)
- ✗ `Liver Pattern: Fire.md` - MERGE
- Review: `Liver Fire Insulting Lung.md` - KEEP SEPARATE (complication pattern)

**Keep Separate (Transformations):**
- `Liver Fire → Liver Wind.md` - Distinct transformation pattern
- `Liver-fire → Wind.md` - Review if duplicate of above

---

### Liver Wind Group
**Standard Name:** `Internal Liver Wind.md` OR `Liver Wind.md`  
**Files to Review:**
- `Internal Liver wind?` (from ToDo) - Find and standardize
- `Extreme heat -> Liver Wind.md` - RENAME → `Extreme Heat → Liver Wind.md`
- `Extreme-Heat → Wind.md` - MERGE with above
- `Liver Fire → Liver Wind.md` - KEEP (different etiology)
- `Liver-fire → Wind.md` - MERGE with above
- `Liver Blood Def. → Wind.md` - KEEP (different etiology)

---

### Liver Yang Rising Group
**Standard Name:** `Liver Yang Rising.md`  
**Files to Review:**
- ✓ `Liver Yang Rising.md` - KEEP
- ✗ `Liver Pattern: Yang Rising.md` - MERGE

**Keep Separate (Transformations):**
- `Liver Blood Deficiency → Liver Yang Rising.md`
- `Liver Yin Deficiency → Liver Yang Rising.md`
- `Liver Kidney Yin Deficiency → Liver Yang Rising.md`

---

### Liver Damp-Heat Group
**Standard Name:** `Liver Damp-Heat.md`  
**Files to Merge:**
- ✓ Choose one as base
- ✗ `Liver Damp Heat.md` - MERGE (no hyphen)
- ✗ `Liver Damp-heat.md` - MERGE (lowercase)
- ✗ `Liver-gallbladder Damp-heat.md` - Review: may be distinct or merge
- ✗ `Damp-heat In Liver And Gallbladder.md` - Review: may be distinct

---

### Gallbladder Damp-Heat Group
**Standard Name:** `Gallbladder Damp-Heat.md`  
**Files to Merge:**
- ✓ `Gallbladder Damp-Heat.md` - KEEP
- ✗ `Gallbladder Heat Congesting.md` - Review if same or distinct

---

### Food Retention Group
**Standard Name:** `Food Retention in the Stomach.md`  
**Files to Merge:**
- ✓ Choose one as base (use "the")
- ✗ `Food Retention in Stomach.md` - MERGE
- ✗ `Food Retention In The Stomach.md` - MERGE
- ✗ `Full: Food Retention.md` - MERGE

---

### Large Intestine Heat Obstruction Group
**Standard Name:** `Large Intestine Heat Obstruction.md`  
**Files to Merge:**
- ✓ Base file (may need to create)
- ✗ `Heat.md` - Review context, likely merge if LI
- ✗ `Heat Obstructing the Large Intestine.md` - MERGE
- ✗ `Yang Ming Fu Syndrome.md` - MERGE or ALIAS
- ✗ `Large Intestine Heat.md` - Review if distinct or merge

---

### Heart Qi Deficiency Group
**Standard Name:** `Heart Qi Deficiency.md`  
**Files to Merge:**
- ✓ `Heart Qi Deficiency.md` - KEEP (if comprehensive)
- ✗ `Heart Qi Deficiency1.md` - MERGE
- ✗ `Qi.md` - Review context (too generic)

---

### Heart & Spleen Deficiency Group
**Standard Name:** `Heart Blood and Spleen Qi Deficiency.md`  
**Files to Merge:**
- Choose ONE as standard
- ✗ `Heart Blood And Spleen Qi Deficiency.md`
- ✗ `Heart Blood & Spleen Qi Def..md`
- ✗ `Spleen Qi And Heart Blood Def..md`

---

### Lung & Spleen Qi Deficiency Group
**Standard Name:** `Lung and Spleen Qi Deficiency.md`  
**Files to Merge:**
- ✓ Choose one
- ✗ `Lung And Spleen Qi Deficiency.md`
- ✗ `Lung & Spleen Qi Deficiency.md`

---

### Spleen & Liver Blood Deficiency Group
**Standard Name:** `Spleen and Liver Blood Deficiency.md`  
**Files to Merge:**
- ✓ Choose one
- ✗ `Spleen & Liver Blood Xu.md`
- ✗ `Spleen and Liver Blood Def..md`
- ✗ `Spleen And Liver Blood Def..md`

---

### Kidney & Bladder Group
**Standard Name:** `Kidney Deficiency with Damp-Heat in the Bladder.md`  
**Files to Review:**
- `Kidney & Bladder.md` - Review if same pattern

---

### Pericardium Blood Deficiency
**Standard Name:** `Pericardium Blood Deficiency.md`  
**Files to Merge:**
- ✓ `Pericardium Blood Deficiency.md` - KEEP
- ✗ Any from glob files

---

### Lung Yin Deficiency Group
**Standard Name:** `Lung Yin Deficiency.md`  
**Files to Merge:**
- ✓ `Lung Yin Deficiency.md` - KEEP
- ✗ `Dryness (empty).md` - Review: may be distinct or merge
- ✗ `Lung Dryness.md` - Review: may be distinct pathogen pattern

---

### Exterior/Interior Files
**Files to Review:**
- `Exterior.md` - TOO GENERIC - review and likely delete or move
- `Interior.md` - TOO GENERIC - review and likely delete or move

---

### Special Cases
**File:** `Turbid Phlegm Disturbing the Head.md`  
**Action:** KEEP - distinct pattern

**File:** `Phlegm Fluids.md`  
**Action:** Review - may be educational reference

**File:** `Rebellious Liver Qi.md`  
**Action:** KEEP - distinct from Qi Stagnation

**File:** `Vacuity Vexation Of Liver-gallbladder.md`  
**Action:** Review - keep if distinct TCM term

---

## 📋 PART 3: Final Standardized Pattern List

After all merges and separations, we should have approximately 120 patterns:

### BLADDER (4)
- Bladder Damp-Heat
- Bladder Damp-Cold  
- Bladder Damp Turbidity
- Bladder Qi Deficiency
- Bladder Yang Deficiency

### GALLBLADDER (4)
- Gallbladder Damp-Heat
- Gallbladder Qi Deficiency
- Gallbladder Deficiency with Phlegm
- Liver-Gallbladder Damp-Heat (if distinct)

### HEART (10)
- Heart Qi Deficiency
- Heart Yang Deficiency
- Heart Blood Deficiency
- Heart Yin Deficiency
- Heart Fire Blazing
- Heart Blood Stasis
- Phlegm-Fire Harassing the Heart
- Phlegm Misting the Mind
- Heart and Kidney Not Harmonized
- Heart Blood and Spleen Qi Deficiency

### KIDNEY (12+)
- Kidney Qi Deficiency
- Kidney Qi Not Firm
- Kidney Yang Deficiency
- Kidney Yin Deficiency
- Kidney Essence Deficiency
- Kidney Yin Deficiency → Empty Fire Blazing
- Kidney Deficiency with Damp-Heat in the Bladder
- Kidney and Liver Yin Deficiency
- Kidney and Heart Not Harmonized
- (+ other combinations from Combi file)

### LARGE INTESTINE (6)
- Large Intestine Qi Deficiency
- Large Intestine Fluid Deficiency
- Large Intestine Qi Stagnation
- Large Intestine Damp-Heat
- Large Intestine Dry Heat
- Large Intestine Heat Obstruction (Yang Ming Fu)

### LIVER (15+)
- Liver Qi Stagnation
- Liver Qi Stagnation → Heat
- Liver Fire Blazing
- Liver Fire Insulting Lung
- Liver Fire → Liver Wind
- Liver Blood Deficiency
- Liver Blood Deficiency → Wind
- Liver Blood Deficiency → Liver Yang Rising
- Liver Yin Deficiency
- Liver Yin Deficiency → Liver Yang Rising
- Liver Yang Rising
- Liver Yang Deficiency
- Liver Blood Stasis
- Liver Damp-Heat
- Liver Kidney Yin Deficiency → Liver Yang Rising
- Liver Qi Invading Spleen
- Liver Qi Invading Stomach
- Liver Overacting on Spleen
- Internal Liver Wind
- Extreme Heat → Liver Wind

### LUNG (10+)
- Lung Qi Deficiency
- Lung Yin Deficiency
- Lung Dryness
- Phlegm-Heat in the Lungs
- Lung Wind-Cold
- Lung Wind-Heat
- Lung Wind Water
- Lung and Spleen Qi Deficiency
- Lung and Kidney Yin Deficiency

### PERICARDIUM (4)
- Pericardium Qi Deficiency
- Pericardium Blood Deficiency
- Pericardium Blood Stasis
- Phlegm-Fire Harassing Pericardium

### SMALL INTESTINE (6)
- Small Intestine Qi Deficiency
- Small Intestine Deficiency and Cold
- Small Intestine Qi Pain
- Small Intestine Qi Tied
- Small Intestine Heat
- Worms in the Small Intestine

### SPLEEN (12+)
- Spleen Qi Deficiency
- Spleen Qi Deficiency with Damp Retention
- Spleen Qi Sinking
- Spleen Yang Deficiency
- Spleen Yin Deficiency
- Spleen Blood Deficiency
- Spleen Not Controlling Blood
- Spleen Damp-Heat
- Cold-Damp Invading the Spleen
- Spleen Damp + Liver Qi Stagnation
- Spleen and Stomach Disharmony
- Spleen and Liver Blood Deficiency
- Liver Qi Stagnation with Spleen Qi Deficiency

### STOMACH (12)
- Stomach Qi Deficiency
- Stomach Qi Stagnation
- Stomach Qi Rebelling Upwards
- Stomach Yin Deficiency
- Stomach Fire
- Stomach Phlegm-Fire
- Stomach Blood Stasis
- Stomach Damp-Heat
- Stomach Deficiency and Cold
- Cold Fluids Obstructing the Stomach
- Food Retention in the Stomach
- Cold Invading Stomach

### OTHER/SPECIAL (5)
- Rebellious Liver Qi
- Turbid Phlegm Disturbing the Head
- Vacuity Vexation of Liver-Gallbladder
- Depressed Gallbladder + Phlegm

---

## 🔄 Implementation Workflow

### Phase 1: Analysis & Backup
```bash
# `=this.name`
cd TCM_Patterns/Zang\ Fu\ Patterns
tar -czf ~/pattern_backup_$(date +%Y%m%d).tar.gz *.md

# 2. Analyze all glob files manually
# Read each file and document what patterns it contains
```

### Phase 2: Break Apart Glob Files
For each glob file:
1. Read the content
2. Identify distinct patterns within
3. Create new individual files using TEMPLATE_Pattern.md
4. Copy relevant content to each
5. Delete original glob file

### Phase 3: Merge Duplicates
For each duplicate group:
1. Identify the most complete version
2. Review all duplicates for unique content
3. Merge unique content into primary file
4. Update frontmatter with all aliases
5. Delete duplicate files

### Phase 4: Rename Non-Standard Files
1. Rename all "Empty:", "Full:", "Pattern:" files to standard names
2. Update any wikilinks that reference old names

### Phase 5: Comprehensive Enhancement
Once standardized names are set:
1. Use deep_research_pipeline.py with API key to create comprehensive versions
2. OR manually enhance using TEMPLATE_Pattern.md structure

### Phase 6: Auto-Link
```bash
python scripts/auto_link_symptoms.py --dirs "TCM_Patterns/Zang Fu Patterns"
```

---

## 📝 Decision Points Needing Clarification

1. **Liver-Gallbladder Damp-Heat** vs **Liver Damp-Heat** + **Gallbladder Damp-Heat**
   - Are these the same or distinct patterns?
   - Recommend: Keep Liver-Gallbladder as combination pattern

2. **Phlegm Misting the Mind** vs **Phlegm Misting the Heart**
   - Same pattern or different focus?
   - Recommend: Keep as one pattern, Heart focus with mental symptoms

3. **Lung Dryness** vs **Lung Yin Deficiency**
   - Distinct patterns or same?
   - Recommend: Keep separate (Dryness is pathogen, Yin Def is organ deficiency)

4. **Yang Ming Fu Syndrome** naming
   - Use this classical name or "Large Intestine Heat Obstruction"?
   - Recommend: Use "Large Intestine Heat Obstruction" with Yang Ming Fu as alias

5. **Stomach-Spleen Qi Deficiency** vs separate patterns
   - Is this a distinct combination or just referring to both?
   - Recommend: Merge with Spleen Qi Deficiency unless content shows it's distinct

---

## 🎯 Priority Order

### HIGH PRIORITY (Do First)
1. Merge simple duplicates (same name, different case)
2. Rename "Empty:", "Full:" files to proper names
3. Break apart Heart, Liver, Kidney glob files (most clinically important)

### MEDIUM PRIORITY
4. Break apart Lung, Spleen glob files
5. Merge Liver Fire group
6. Merge Phlegm-Fire Heart group

### LOW PRIORITY (Can wait)
7. Break apart Small Intestine, Large Intestine globs
8. Review educational/reference files
9. Handle edge cases and special patterns

---

## ✅ Success Criteria

- [ ] No files with "Empty:", "Full:", "Pattern:" prefixes
- [ ] No duplicate pattern files (1.md, etc.)
- [ ] All glob files separated into individual patterns
- [ ] All patterns follow naming conventions
- [ ] All patterns have comprehensive structure (post API enhancement)
- [ ] All symptoms auto-linked
- [ ] No broken wikilinks

---

**Ready for review and API key to proceed with comprehensive enhancement!**
