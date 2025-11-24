---
ocds_type: flashcard
material_id: flashcards_week01_tongue
class_id: TCM_101
week: 1
title: "Week 1 Flashcards: Tongue Diagnosis"
description: Spaced repetition flashcards for tongue diagnosis fundamentals
topic: Tongue Diagnosis
total_cards: 22
cards_reviewed: 22
cards_mastered: 21
last_review_date: 2025-11-09
tags:
  - flashcards
  - week1
  - tongue-diagnosis
  - spaced-repetition
card_count: 22
---

# Week 1 Flashcards: Tongue Diagnosis

**Total Cards:** 20  
**Topic:** Tongue Diagnosis Fundamentals

```dataviewjs
// Track flashcard reviews using Spaced Repetition plugin data
const file = dv.current().file;
const content = await dv.io.load(file.path);
const lines = content.split('\n');

let totalCards = 0;
let reviewedCards = 0;
let masteredCards = 0;

// Count flashcards and check review status
for (let i = 0; i < lines.length; i++) {
  const line = lines[i];
  
  // Count cards (lines with "?" separator)
  if (line.trim() === '?') {
    totalCards++;
    
    // Check next few lines for SR comment (indicates reviewed)
    for (let j = i + 1; j < Math.min(i + 5, lines.length); j++) {
      const nextLine = lines[j];
      
      // Look for SR comment: <!--SR:!2025-11-10,3,250-->
      if (nextLine.includes('<!--SR:')) {
        reviewedCards++;
        
        // Extract ease factor (last number)
        const match = nextLine.match(/,(\d+)-->/);
        if (match) {
          const ease = parseInt(match[1]);
          // Consider mastered if ease >= 250 (default is 250)
          if (ease >= 250) {
            masteredCards++;
          }
        }
        break;
      }
    }
  }
}

// Calculate percentage
const reviewPercent = totalCards > 0 ? Math.round((reviewedCards / totalCards) * 100) : 0;

// Update frontmatter
const currentFile = app.workspace.getActiveFile();
if (currentFile) {
  await app.fileManager.processFrontMatter(currentFile, (fm) => {
    fm.total_cards = totalCards;
    fm.card_count = totalCards;
    fm.cards_reviewed = reviewedCards;
    fm.cards_mastered = masteredCards;
    if (reviewedCards > 0) {
      fm.last_review_date = new Date().toISOString().split('T')[0];
    }
  });
}

// Display progress
dv.paragraph(`**Cards in Deck:** ${totalCards}`);
dv.paragraph(`**Cards Reviewed:** ${reviewedCards} / ${totalCards} (${reviewPercent}%)`);
dv.paragraph(`**Cards Mastered:** ${masteredCards}`);
dv.paragraph(`**Last Review:** ${reviewedCards > 0 ? new Date().toISOString().split('T')[0] : 'Not yet'}`);

// Progress bar
const barWidth = 30;
const filled = Math.round((reviewPercent / 100) * barWidth);
const empty = barWidth - filled;
const bar = '█'.repeat(filled) + '░'.repeat(empty);
dv.paragraph(`\`${bar}\` ${reviewPercent}%`);
```

> [!info] Flashcard Tracking - How It Works
> **Spaced Repetition Plugin Integration:**
> - Plugin adds `<!--SR:!date,interval,ease-->` comments to reviewed cards
> - This script reads those comments to track your progress
> - **Refresh this page** after reviewing to see updated stats
> - Dashboard reads from frontmatter (updated by this script)
> 
> **Tracking Metrics:**
> - `total_cards`: Total flashcards in deck (auto-counted)
> - `cards_reviewed`: Cards with SR comments (you've seen them)
> - `cards_mastered`: Cards with ease ≥ 250 (you know them well)
> - `last_review_date`: Last time you studied

---

## 📊 Spaced Repetition Data Explained

### What the SR Comments Mean

When you review a card, the plugin adds:
```markdown
<!--SR:!2025-11-10,3,250-->
```

**Format:** `<!--SR:!due_date,interval,ease-->`
- **Due Date** (`2025-11-10`): When to review next
- **Interval** (`3`): Days until next review
- **Ease** (`250`): Difficulty factor (higher = easier)

### Ease Factor Guide

| Ease | Meaning | How to Get There |
|------|---------|------------------|
| < 130 | Very Hard | Marked "Again" multiple times |
| 130-200 | Hard | Marked "Hard" or "Again" |
| 250 | Normal | Default, or marked "Good" |
| 250+ | Easy | Marked "Easy" or "Good" multiple times |

**Our Mastery Threshold:** Ease ≥ 250 (you know it!)

### Review Intervals

| Interval | Meaning |
|----------|---------|
| 0-1 days | Just learned, review soon |
| 2-7 days | Learning phase |
| 8-30 days | Retention phase |
| 31+ days | Long-term memory |

---

## How to Use These Flashcards

### Method 1: Plugin Review Interface (Recommended)
1. Press **Ctrl/Cmd + P**
2. Type "**Review flashcards**"
3. Study cards in the review interface
4. Mark as: **Again** / **Hard** / **Good** / **Easy**
5. Plugin schedules next review automatically

### Method 2: In-File Review
1. Read the question
2. Think of the answer
3. Reveal the answer (below the `?`)
4. Right-click the card → "Review: Easy/Good/Hard/Again"

### After Reviewing
1. **Refresh this page** (Ctrl/Cmd + R)
2. See updated stats above
3. Go to dashboard and refresh
4. Progress appears!

---

## Flashcards

### Card 1
What does a **pale tongue** indicate?
?
Qi Deficiency, Blood Deficiency, Yang Deficiency, or Cold
<!--SR:!2025-11-10,3,250-->

---

### Card 2
What does a **red tongue** indicate?
?
Heat (Excess Heat if bright red, Deficiency Heat if dark red)
<!--SR:!2025-11-10,3,250-->

---

### Card 3
What does a **purple tongue** indicate?
?
Blood Stasis (purple-blue = Cold Stasis, purple-red = Heat with Stasis)
<!--SR:!2025-11-10,3,250-->

---

### Card 4
What does a **thick tongue coating** indicate?
?
Presence of excess pathogen (Dampness, Phlegm, or Food Stagnation)
<!--SR:!2025-11-10,3,250-->

---

### Card 5
What does a **thin tongue coating** indicate?
?
Normal Stomach Qi, no significant pathogen
<!--SR:!2025-11-10,3,250-->

---

### Card 6
What does a **white coating** indicate?
?
Cold, Exterior condition, or Dampness
<!--SR:!2025-11-10,3,250-->

---

### Card 7
What does a **yellow coating** indicate?
?
Heat (light yellow = mild Heat, deep yellow = severe Heat)
<!--SR:!2025-11-10,3,250-->

---

### Card 8
What do **tooth marks** on the tongue indicate?
?
Spleen Qi Deficiency (tongue swells and presses against teeth)
<!--SR:!2025-11-10,3,250-->

---

### Card 9
What does a **swollen tongue** indicate?
?
Dampness, Phlegm, or Qi Deficiency
<!--SR:!2025-11-10,3,250-->

---

### Card 10
What does a **thin tongue** indicate?
?
Blood Deficiency or Yin Deficiency
<!--SR:!2025-11-10,3,250-->

---

### Card 11
What do **cracks** on the tongue indicate?
?
Yin Deficiency or Heat consuming fluids (unless constitutional)
<!--SR:!2025-11-10,3,250-->

---

### Card 12
What does a **peeled coating** indicate?
?
Stomach or Kidney Yin Deficiency
<!--SR:!2025-11-10,3,250-->

---

### Card 13
Which organ(s) correspond to the **tip** of the tongue?
?
Heart and Lungs
<!--SR:!2025-11-10,3,250-->

---

### Card 14
Which organ(s) correspond to the **center** of the tongue?
?
Spleen and Stomach
<!--SR:!2025-11-10,3,250-->

---

### Card 15
Which organ(s) correspond to the **root** of the tongue?
?
Kidneys and Bladder
<!--SR:!2025-11-10,3,250-->

---

### Card 16
Which organ(s) correspond to the **sides** of the tongue?
?
Liver and Gallbladder
<!--SR:!2025-11-10,3,250-->

---

### Card 17
What are the characteristics of a **normal healthy tongue**?
?
Pale red color, thin white coating, slightly moist, flexible, not swollen
<!--SR:!2025-11-10,3,250-->

---

### Card 18
What does a **dry coating** indicate?
?
Yin Deficiency, Heat consuming fluids, or dehydration
<!--SR:!2025-11-10,3,250-->

---

### Card 19
What does a **wet/slippery coating** indicate?
?
Dampness, Yang Deficiency, or fluid accumulation
<!--SR:!2025-11-10,3,250-->

---

### Card 20
What does a **red tongue with no coating** indicate?
?
Yin Deficiency with Heat
<!--SR:!2025-11-10,3,250-->

---

### Card 21
What does a **red tongue with no coating** indicate? booty style
?
Yin Deficiency with Heat style of the boot
<!--SR:!2025-11-08,1,230-->


---

### Card 22
What does a **red tongue with no coating** indicate? booty stylesasasasas
?
Yin Deficiency with Heat style of the bootsaasasasssaa
<!--SR:!2025-11-10,3,250-->


---

**Review these cards daily using the Spaced Repetition plugin!**
