# 📋 Sample Flashcard - Complete Example

This file shows what a complete flashcard looks like in the system.

---

## Example: ST-36 Location Flashcard

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

---

## How It Appears in Obsidian

### Front of Card (Question)
```
**ST-36** · ZÚSĀNLǏ (足三里) · *Leg Three Miles*

What is the location and special properties of this point?

[Click to reveal answer]
```

### Back of Card (Answer)
```
Location: Below the knee, 3 cun inferior to Dúbí ST-35, 
one finger-breadth lateral to the anterior crest of the tibia.

Notes: i. First locate Yánglíngquán GB-34...

Special Properties:
- He-Sea and Earth point of the Stomach channel
- Gao Wu Command point
- Ma Dan-yang Heavenly Star point
- Point of the Sea of Water and Grain

[Image of ST-36 location shown]

Rate: [Hard] [Good] [Easy]
```

---

## Card Components Explained

### Frontmatter (Metadata)
```yaml
material_type: flashcard          # Identifies as flashcard
topic: Acupuncture Points         # Main topic
subtopic: Location & Properties   # Specific category
point_code: ST-36                 # Point identifier
tags:                             # For filtering/searching
  - flashcard
  - acupoint
  - location
  - stomach-channel
```

### Header (Always Visible)
```markdown
# **ST-36** · ZÚSĀNLǏ (足三里) · *Leg Three Miles*
  ^^^^^^     ^^^^^^^^  ^^^^      ^^^^^^^^^^^^^^^^
  Code       Pinyin    Hanzi     English Name
```

### Question
```markdown
## What is the location and special properties of this point?
```

### Separator
```markdown
?
```
This tells Obsidian SR where the question ends and answer begins.

### Answer
```markdown
**Location:** [description]
**Notes:** [additional details]
**Special Properties:** [list]
![[image.jpg]]
```

### SR Metadata
```markdown
<!--SR:!2025-11-10,3,250-->
        ^^^^^^^^^^^  ^  ^^^
        Next review  |  Ease factor
                     Interval (days)
```

---

## All 6 Card Types for ST-36

### 1. Location Card
**Question:** What is the location and special properties?
**Answer:** Location description + special properties + image

### 2. Needling Card
**Question:** What is the needling technique and cautions?
**Answer:** Method + depth + cautions

### 3. Functions Card
**Question:** What are the functions and actions?
**Answer:** List of functions

### 4. Indications Card
**Question:** What are the clinical indications?
**Answer:** Categorized indications (respiratory, digestive, etc.)

### 5. Combinations Card
**Question:** What are classical point combinations?
**Answer:** Condition + points + source (first 5 combinations)

### 6. Theory Card
**Question:** What is the TCM theoretical understanding?
**Answer:** Summary of classical commentary

---

## Study Workflow

1. **Open flashcard file** in Obsidian
2. **Trigger SR review** (Ctrl/Cmd+P → "Review flashcards")
3. **Read question** (front of card)
4. **Try to recall** answer
5. **Click to reveal** answer
6. **Rate your recall:**
   - **Hard** (didn't remember) → Review in 1 day
   - **Good** (remembered with effort) → Review in 3 days
   - **Easy** (instant recall) → Review in 7 days
7. **Repeat** for all due cards

---

## Tips for Effective Study

### Visual Learners
- Focus on location cards first
- Study the embedded images
- Draw point locations

### Auditory Learners
- Read cards aloud
- Create verbal mnemonics
- Discuss with study partners

### Kinesthetic Learners
- Practice point location on body
- Use needling technique cards
- Apply in clinical practice

### All Learners
- Review daily (consistency is key)
- Be honest with ratings
- Trust the spaced repetition algorithm
- Apply knowledge clinically

---

*This is just ONE card out of 2,062 in the system!*
*Each point has 6 cards covering all aspects of study.*
