# TCM Flashcards - Spaced Repetition Study System

This directory contains automatically generated flashcards from the TCM Knowledge Base, formatted for use with Obsidian's Spaced Repetition plugin.

## 📚 Available Flashcard Collections

### Acupuncture Points
Located in `Acupuncture_Points/`

**Total Cards: 2,062** across 6 categories:

1. **Location & Properties** (361 cards)
   - Point location descriptions
   - Special properties
   - Location images
   
2. **Needling Technique** (361 cards)
   - Needling method
   - Needling depth
   - Cautions and contraindications

3. **Functions & Actions** (346 cards)
   - Primary functions
   - Therapeutic actions

4. **Clinical Indications** (346 cards)
   - Categorized by system (respiratory, digestive, etc.)
   - Traditional indications

5. **Point Combinations** (335 cards)
   - Classical point combinations
   - Condition-specific protocols
   - Source citations

6. **TCM Theory** (313 cards)
   - Theoretical understanding
   - Classical commentary
   - Channel theory

## 🎴 Flashcard Format

Each flashcard includes:

### Front of Card
```
**POINT-CODE** · PINYIN (汉字) · *English Name*

## Question about specific aspect
```

### Back of Card
```
Detailed answer with:
- Structured information
- Images (for location cards)
- Source references (for combinations)
```

### Example Card

```markdown
---
material_type: flashcard
topic: Acupuncture Points
subtopic: Location & Properties
point_code: ST-36
tags:
  - flashcard
  - acupoint
  - location
  - stomach-channel
---

# **ST-36** · ZÚSĀNLǏ (足三里) · *Leg Three Miles*

## What is the location and special properties of this point?
?
**Location:** Below the knee, 3 cun inferior to Dúbí ST-35, one finger-breadth lateral to the anterior crest of the tibia.

**Notes:** i. First locate Yánglíngquán GB-34. Zúsānlǐ ST-36 lies one cun inferior to Yánglíngquán GB-34 and one finger-breadth lateral to the anterior crest of the tibia; ii. Locate one handbreadth below Dúbí ST-35.

**Special Properties:**
- He-Sea and Earth point of the Stomach channel
- Gao Wu Command point
- Ma Dan-yang Heavenly Star point
- Point of the Sea of Water and Grain

![[ST-36_diagram.jpg]]
<!--SR:!2025-11-10,3,250-->
```

## 🔧 How to Use

### Setup
1. **Install Obsidian Spaced Repetition Plugin**
   - Open Obsidian Settings
   - Go to Community Plugins
   - Search for "Spaced Repetition"
   - Install and enable

2. **Configure Plugin**
   - Set review frequency
   - Adjust difficulty settings
   - Configure card format (default works with these cards)

### Study Workflow

1. **Open a flashcard file** (e.g., `Flashcards_Points_Location.md`)

2. **Start review session**
   - Use plugin command: "Spaced Repetition: Review flashcards"
   - Or click the SR icon in the ribbon

3. **Review cards**
   - Read the question
   - Try to recall the answer
   - Click to reveal
   - Rate your recall (Hard/Good/Easy)

4. **Track progress**
   - Plugin automatically schedules reviews
   - Cards appear based on spaced repetition algorithm
   - Mastered cards appear less frequently

### Study Strategies

**By Category** (Recommended for beginners)
- Start with Location cards
- Master locations before moving to functions
- Progress: Location → Functions → Indications → Needling → Combinations → Theory

**By Channel** (For systematic study)
- Study all aspects of one channel at a time
- Example: All Stomach channel cards together

**Mixed Review** (For advanced students)
- Combine multiple categories
- Reinforces connections between concepts

## 📊 Card Statistics

| Category | Cards | Avg. Difficulty |
|----------|-------|-----------------|
| Location | 361 | ⭐⭐ Basic |
| Needling | 361 | ⭐⭐⭐ Intermediate |
| Functions | 346 | ⭐⭐ Basic |
| Indications | 346 | ⭐⭐⭐ Intermediate |
| Combinations | 335 | ⭐⭐⭐⭐ Advanced |
| Theory | 313 | ⭐⭐⭐⭐⭐ Expert |

## 🔄 Regenerating Flashcards

If the source point files are updated, regenerate flashcards:

```bash
cd /home/shuma/Documents/AI_Suite/TCM_Knowledge_Base
python3 scripts/generate_point_flashcards.py
```

This will:
- Scan all point files in `TCM_Points/`
- Extract updated information
- Regenerate all flashcard files
- Preserve your review progress (SR metadata)

## 📝 Customization

### Modify Card Generation
Edit `scripts/generate_point_flashcards.py` to:
- Change card format
- Add/remove categories
- Adjust difficulty levels
- Customize grouping

### Create Custom Collections
Combine cards from multiple files:
```markdown
# My Custom Study Set

![[Flashcards_Points_Location.md#ST-36]]
![[Flashcards_Points_Functions.md#ST-36]]
![[Flashcards_Points_Indications.md#ST-36]]
```

## 🎯 Study Goals

### Beginner (0-3 months)
- [ ] Master all point locations (361 cards)
- [ ] Learn basic functions (346 cards)
- Target: 20 new cards/day, 100 reviews/day

### Intermediate (3-6 months)
- [ ] Master needling techniques (361 cards)
- [ ] Learn clinical indications (346 cards)
- Target: 15 new cards/day, 150 reviews/day

### Advanced (6-12 months)
- [ ] Master point combinations (335 cards)
- [ ] Understand TCM theory (313 cards)
- Target: 10 new cards/day, 200 reviews/day

## 🔗 Related Resources

- **Source Notes**: `../TCM_Points/` - Original point documentation
- **Images**: `../TCM_Points_Images/` - Point diagrams and Chinese characters
- **Scripts**: `../scripts/generate_point_flashcards.py` - Generation script

## 📅 Maintenance

**Last Generated:** 2025-11-03
**Source Files:** 361 point files
**Total Cards:** 2,062

To update:
1. Edit source point files in `TCM_Points/`
2. Run generation script
3. Review new/modified cards
4. Continue spaced repetition schedule

---

*Generated automatically from TCM Knowledge Base*
*For questions or issues, see `../scripts/generate_point_flashcards.py`*
