# TCM Symptom Standardization Plan

**Generated:** 2025-10-24
**Total Symptom Files:** 359
**Issues Found:** 387+ duplicate/variation cases

---

## 📊 Summary of Issues

### 1. **Case Variations** (33 groups)
Same symptom name, different capitalization

### 2. **Exact Duplicates** (15+ cases)
Files with " 1" suffix or very minor spelling differences

### 3. **Spelling Variations** (20+ cases)
Different spellings of same symptom (e.g., "Distension" vs "Distention")

### 4. **Similar Symptoms** (114 pairs)
Symptoms with 75%+ similarity that may need merging

### 5. **Subset/Superset** (240 pairs)
General terms vs specific variations (e.g., "Cough" vs "Dry Cough")

---

## 🎯 Standardization Strategy

### Naming Convention Rules:

1. **Capitalization**: Title Case for all symptom names
   - Standard: "Abdominal Distension"
   - NOT: "abdominal distension"

2. **Spelling**: Use most common TCM convention
   - "Distension" preferred over "Distention"
   - "Borborygmus" preferred over "Borborygmi"

3. **Specificity**: Keep specific variations separate, merge exact duplicates
   - Keep separate: "Cough", "Dry Cough", "Chronic Cough"
   - Merge: "Acid Reflux" and "Acid Reflux 1"

4. **Synonyms**: Merge very similar terms into most clinically accurate
   - Merge: "Acid Reflux" + "Acid Regurgitation" → "Acid Reflux"
   - Merge: "Night Sweating" + "Night Sweats" → "Night Sweats"

---

## 📋 Priority 1: Exact Duplicates (Immediate Merge)

These are identical symptoms with copy suffixes or exact duplicates:

| Files to Merge | Standard Name | Patterns | Formulas | Action |
|----------------|---------------|----------|----------|--------|
| Acid Reflux / Acid Reflux 1 | **Acid Reflux** | 4 / 4 | 14 / 14 | Merge both into "Acid Reflux", delete "Acid Reflux 1" |
| Acid Regurgitation / Acid Regurgitation 1 | **Acid Regurgitation** | 2 / 2 | 9 / 9 | Merge both into "Acid Regurgitation", delete "Acid Regurgitation 1" |
| Nocturnal Emission / Nocturnal Emissions | **Nocturnal Emissions** | 1 / 2 | 2 / 6 | Merge into "Nocturnal Emissions" |
| Manic Behavior / Manic behaviour | **Manic Behavior** | 1 / 1 | 4 / 4 | Merge into "Manic Behavior" (US spelling) |
| Hiccup / Hiccups | **Hiccups** | 2 / 2 | 9 / 8 | Merge into "Hiccups" (plural) |
| Tremor / Tremors | **Tremors** | 5 / 6 | 11 / 11 | Merge into "Tremors" (plural) |
| Opisthotonos / Opisthotonus | **Opisthotonos** | 2 / 3 | 4 / 4 | Merge into "Opisthotonos" (standard spelling) |
| Five Palm Heat / Five-Palm Heat | **Five-Palm Heat** | 5 / 1 | 13 / 3 | Merge into "Five-Palm Heat" (hyphenated) |
| Low Grade Fever / Low-Grade Fever / Low-grade Fever | **Low-Grade Fever** | 1/1/1 | varies | Merge all into "Low-Grade Fever" |

**Total Impact:** ~20 files to delete, ~50+ patterns to update

---

## 📋 Priority 2: Case Variations (Auto-Fix)

These differ only in capitalization. Always use Title Case:

| Lowercase Version | Standard (Title Case) | Pattern Count | Formula Count |
|-------------------|----------------------|---------------|---------------|
| abdominal distension | **Abdominal Distension** | 1 → 9 | 6 → 17 |
| abdominal distention | **Abdominal Distention** | 1 → 5 | 3 → 12 |
| abdominal fullness | **Abdominal Fullness** | 1 → 2 | 4 → 6 |
| aversion to cold | **Aversion to Cold** | 3 → 12 | 7 → 20 |
| blurred vision | **Blurred Vision** | 2 → 9 | 9 → 20 |
| chest oppression | **Chest Oppression** | 1 → 13 | 3 → 24 |
| cold limbs | **Cold Limbs** | 2 → 16 | 6 → 35 |
| epigastric fullness | **Epigastric Fullness** | 2 → 6 | 5 → 13 |
| epigastric pain | **Epigastric Pain** | 1 → 11 | 5 → 33 |
| epigastric stuffiness | **Epigastric Stuffiness** | 1 → 1 | 4 → 2 |
| feeling of cold | **Feeling of Cold** | 1 → 1 | 3 → 3 |
| heaviness of the body | **Heaviness of the Body** | 3 → 1 | 8 → 3 |
| high fever | **High Fever** | 2 → 8 | 7 → 11 |
| incoherent speech | **Incoherent Speech** | 1 → 3 | 3 → 5 |
| loose stools | **Loose Stools** | 7 → 19 | 21 → 24 |
| mental confusion | **Mental Confusion** | 1 → 2 | 4 → 4 |
| night sweating | **Night Sweating** | 1 → 10 | 1 → 18 |
| no appetite | **No Appetite** | 1 → 1 | 4 → 3 |
| pale complexion | **Pale Complexion** | 3 → 6 | 6 → 15 |
| pale face | **Pale Face** | 1 → 1 | 4 → 2 |
| poor appetite | **Poor Appetite** | 5 → 15 | 14 → 24 |
| poor memory | **Poor Memory** | 2 → 7 | 4 → 17 |
| profuse sweating | **Profuse Sweating** | 1 → 5 | 4 → 9 |
| sallow complexion | **Sallow Complexion** | 1 → 4 | 4 → 7 |
| scanty menstruation | **Scanty Menstruation** | 1 → 1 | 4 → 5 |
| shortness of breath | **Shortness of Breath** | 3 → 21 | 6 → 33 |
| sore throat | **Sore Throat** | 2 → 9 | 8 → 15 |
| spontaneous sweating | **Spontaneous Sweating** | 2 → 14 | 7 → 19 |
| sticky taste | **Sticky Taste** | 1 → 1 | 5 → 3 |
| stiff neck | **Stiff Neck** | 1 → 1 | 1 → 1 |
| watery nasal discharge | **Watery Nasal Discharge** | 1 → 1 | 5 → 4 |
| weak voice | **Weak Voice** | 2 → 3 | 6 → 5 |

**Total Impact:** 33 files to delete, content merged, ~200+ pattern references to update

---

## 📋 Priority 3: Spelling Variations

Choose standard TCM spelling:

### Distension vs Distention

**Decision:** Use "Distension" (more common in TCM texts)

| Current | Standard | Patterns | Formulas |
|---------|----------|----------|----------|
| Abdominal Distention | **Abdominal Distension** | 5 | 12 |
| Abdominal distention | **Abdominal Distension** | 1 | 3 |
| Distention | **Distension** | 1 | 4 |

**Impact:** Merge 4 files into "Distension" versions

### Borborygmi vs Borborygmus

**Decision:** Use "Borborygmus" (singular form)

| Current | Standard | Patterns | Formulas |
|---------|----------|----------|----------|
| Borborygmi | **Borborygmus** | 2 | 2 |
| Borborygmus | **Borborygmus** | 7 | 15 |

**Impact:** Merge into "Borborygmus"

### Vision Variations

**Decision:** Use "Blurred Vision" (most common)

| Current | Standard | Patterns | Formulas |
|---------|----------|----------|----------|
| Blurred Vision | **Blurred Vision** | 9 | 20 |
| Blurred vision | **Blurred Vision** | 2 | 9 |
| Blurring of Vision | **Blurred Vision** | 1 | 3 |
| Blurry Vision | **Blurred Vision** | 2 | 6 |

**Impact:** Merge 4 files into "Blurred Vision"

---

## 📋 Priority 4: Similar Symptoms (Needs Review)

These are SIMILAR but may represent different clinical presentations. **USER DECISION REQUIRED:**

### Digestive Symptoms

#### Acid-Related
| Symptom 1 | Symptom 2 | Similarity | Recommendation |
|-----------|-----------|------------|----------------|
| Acid Reflux (4p, 14f) | Acid Regurgitation (2p, 9f) | Different patterns | **MERGE** - User requested |
| Acid Regurgitation | Sour Regurgitation | 77.78% | Keep separate - different quality |

**Proposed Merge:** Combine "Acid Reflux" and "Acid Regurgitation"
- Standard name: **"Acid Reflux"**
- Preserve all patterns from both files (6 unique patterns total)
- Combine all formulas, herbs, points
- Merge note body content

#### Appetite
| Symptom 1 | Symptom 2 | Recommendation |
|-----------|-----------|----------------|
| No Appetite | Poor Appetite | Keep separate - different severity |
| Anorexia | No Appetite | **MERGE** - synonyms |

#### Fullness/Stuffiness
| Group | Recommendation |
|-------|----------------|
| Epigastric Fullness / Epigastric Stuffiness | **MERGE** into "Epigastric Fullness" |
| Abdominal Fullness / Abdominal Distension | Keep separate - different sensations |

### Respiratory Symptoms

| Symptom 1 | Symptom 2 | Recommendation |
|-----------|-----------|----------------|
| Night Sweating | Night Sweats | **MERGE** into "Night Sweats" |
| Spontaneous Sweating | Profuse Sweating | Keep separate - different etiologies |
| Breathlessness | Shortness of Breath | **MERGE** into "Shortness of Breath" |

### Pain Symptoms

**General Strategy:** Keep specific pain types separate from general "Pain"

| Specific | General | Recommendation |
|----------|---------|----------------|
| Hypochondriac Pain | Hypochondrial Pain | **MERGE** - spelling variation |
| Sore Low Back | Sore Lower Back | **MERGE** into "Lower Back Pain" |
| Soreness of Lower Back | Sore Lower Back | **MERGE** into "Lower Back Pain" |

### Bleeding Symptoms

| Symptom 1 | Symptom 2 | Recommendation |
|-----------|-----------|----------------|
| Blood in stools | Bloody stools | **MERGE** into "Blood in Stool" |
| Blood in Stool | Bloody stools | Merge duplicates |
| Vomiting Blood | Vomiting of blood | **MERGE** into "Vomiting Blood" |

### Stool Symptoms

| Symptom 1 | Symptom 2 | Recommendation |
|-----------|-----------|----------------|
| Dark Stools | Dry Stools | Keep separate - different meanings |
| Loose Stools | Loose stools | Case variation - merge |

---

## 📋 Priority 5: Subset/Superset Symptoms

**Strategy:** Keep specific variations separate, but ensure they link to general term

Examples:
- Keep both "Cough" AND "Dry Cough" - but "Dry Cough" should reference "Cough"
- Keep both "Pain" AND "Chest Pain" - but "Chest Pain" should reference "Pain"
- Keep both "Fever" AND "High Fever" - but "High Fever" should reference "Fever"

**Action:** Don't merge these, but add cross-references in note body

---

## 🔧 Implementation Plan

### Phase 1: Exact Duplicates (Safest)
1. Merge " 1" suffixed files
2. Update pattern frontmatter
3. Update all links
4. Delete merged files

### Phase 2: Case Variations (Auto-Fix)
1. For each lowercase variant:
   - Rename file to Title Case
   - Merge content if both exist
   - Update all pattern references
   - Update all links

### Phase 3: Spelling Variations
1. Standardize to preferred spelling
2. Merge files
3. Update references

### Phase 4: User-Approved Merges
1. Present final list to user
2. Get approval for each merge
3. Execute approved merges

---

## ⚠️ Risk Mitigation

1. **Backup First:** Create git commit or backup before any changes
2. **Test on Sample:** Start with 5 files to test the process
3. **Verify Links:** After each batch, verify no broken links
4. **Pattern Check:** Ensure all patterns still load correctly

---

## 📝 User Decisions Needed

### Question 1: Symptom Merges

Do you want to merge these similar symptoms?

- [ ] Acid Reflux + Acid Regurgitation → **Acid Reflux**
- [ ] Breathlessness → **Shortness of Breath**
- [ ] Night Sweating + Night Sweats → **Night Sweats**
- [ ] Epigastric Fullness + Epigastric Stuffiness → **Epigastric Fullness**
- [ ] No Appetite → Keep separate from "Poor Appetite"?
- [ ] Anorexia → Merge into "No Appetite" or keep separate?

### Question 2: Naming Preferences

- [ ] "Distension" or "Distention"? (Recommend: **Distension**)
- [ ] "Borborygmus" or "Borborygmi"? (Recommend: **Borborygmus**)
- [ ] "Night Sweats" or "Night Sweating"? (Recommend: **Night Sweats**)

### Question 3: Subset Strategy

Should specific symptoms reference the general term?
Example: "Dry Cough" note body includes link to [[Cough]]

- [ ] Yes, add cross-references
- [ ] No, keep them independent

---

**Next Step:** Review this plan and provide answers to the decisions above.
Then I'll create the automated tool to execute the standardization.
