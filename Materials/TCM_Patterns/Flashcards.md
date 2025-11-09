---
ocds_type: flashcard
material_id: flashcards_tcm_patterns
class_id: TCM_Patterns
title: Blood Stasis Pattern Flashcards
description: Spaced repetition flashcards for Blood Stasis Pattern
topic: Blood Stasis Pattern
total_cards: 21
cards_reviewed: 21
cards_mastered: 21
last_review_date: 2025-11-09
tags:
  - flashcards
  - tcm_patterns
  - tcm
  - patterns
  - spaced-repetition
card_count: 21
difficulty: intermediate
created: 2025-11-07
updated: 2025-11-07
---

# Blood Stasis Pattern Flashcards

**Total Cards:** 21  
**Topic:** Blood Stasis Pattern

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

// Display stats
dv.paragraph(`
**📊 Review Progress**

- **Total Cards:** ${totalCards}
- **Reviewed:** ${reviewedCards} (${reviewPercent}%)
- **Mastered:** ${masteredCards}
- **Status:** ${reviewPercent >= 80 ? '✅ Complete' : '⏳ In Progress'}
`);
```

---

# Blood Stasis Pattern
## What are the four cardinal symptoms of Blood Stasis?
?
1) Fixed, stabbing pain, 2) Purple tongue or purple spots, 3) Dark complexion, 4) Choppy/hesitant/wiry pulse
<!--SR:!2025-11-10,3,250-->

---

# Blood Stasis Pattern
## What is Blood Stasis (Xue Yu)?
?
**Definition:** A pathological condition where blood flow slows, pools, or becomes obstructed in the vessels and channels

**Importance:** Blood Stasis is a major pathological product that causes pain, masses, and can lead to serious diseases
<!--SR:!2025-11-10,3,250-->

---

# Blood Stasis Pattern
## What is Fixed Stabbing Pain?
?
**Definition:** Pain that is sharp, piercing, boring in quality and fixed in one location

**Importance:** The hallmark symptom that distinguishes Blood Stasis from other patterns
<!--SR:!2025-11-10,3,250-->

---

# Blood Stasis Pattern
## What is Purple Manifestations?
?
**Definition:** Dark, dusky, or purplish discoloration of tongue, lips, nails, and complexion

**Importance:** Visual confirmation of blood flow obstruction
<!--SR:!2025-11-10,3,250-->

---

# Blood Stasis vs Qi Stagnation
## What is the key difference between Blood Stasis pain and Qi Stagnation pain?
?
Blood Stasis pain is FIXED in location and STABBING in quality. Qi Stagnation pain is MOVING and DISTENDING.
<!--SR:!2025-11-10,3,250-->

---

# Qi-Blood Theory
## What does 'Qi is the commander of Blood' mean?
?
Qi has four relationships with Blood: 1) Generates Blood, 2) Moves Blood, 3) Holds Blood in vessels, 4) Warms Blood
<!--SR:!2025-11-10,3,250-->

---

# Blood Stasis Treatment
## What is the primary formula for upper body Blood Stasis (chest area)?
?
Xue Fu Zhu Yu Tang (Drive Out Stasis from the Mansion of Blood Decoction)
<!--SR:!2025-11-10,3,250-->

---

# Blood Stasis Contraindications
## When should blood-invigorating herbs be used with caution?
?
During pregnancy, with bleeding disorders, or if Blood Stasis is not confirmed
<!--SR:!2025-11-10,3,250-->

---

# Blood Stasis Clinical Application
## A patient has fatigue, pale face, stabbing pain, and purple tongue. What is the pattern?
?
Blood Stasis arising from Qi or Blood Deficiency (Mixed Deficiency-Excess pattern)
<!--SR:!2025-11-10,3,250-->

---

# Blood Stasis Pattern - Clinical Manifestation
## What is Blood Stasis pain?
?
fixed in location and stabbing in quality
<!--SR:!2025-11-10,3,250-->

---

# Blood Stasis Pattern - Diagnosis
## What is The tongue in Blood Stasis?
?
purple or has purple spots (petechiae)
<!--SR:!2025-11-10,3,250-->

---

# Blood Stasis Pattern - Diagnosis
## What is The pulse in Blood Stasis?
?
choppy, hesitant, wiry, or firm
<!--SR:!2025-11-10,3,250-->

---

# Blood Stasis Pattern - Theory
## What is Qi?
?
the commander of Blood - Qi moves Blood
<!--SR:!2025-11-10,3,250-->

---

# Blood Stasis Pattern - Treatment Contraindication
## When is this contraindicated?
?
Blood-invigorating herbs are contraindicated in pregnancy
<!--SR:!2025-11-10,3,250-->

---

# Blood Stasis Pattern - Treatment
## What is Xue Fu Zhu Yu Tang?
?
the primary formula for upper body Blood Stasis
<!--SR:!2025-11-10,3,250-->

---

# Blood Stasis Pattern - Comparison
## What is the key difference between Blood Stasis and Qi Stagnation?
?
**Key Distinction:** Blood Stasis pain is FIXED and STABBING; Qi Stagnation pain is MOVING and DISTENDING
<!--SR:!2025-11-10,3,250-->

---

# Blood Stasis Pattern - Comparison
## Compare Blood Stasis and Qi Stagnation in terms of Pain Quality
?
**Blood Stasis:** Fixed, stabbing, boring, piercing

**Qi Stagnation:** Moving, distending, comes and goes
<!--SR:!2025-11-10,3,250-->

---

# Blood Stasis Pattern - Comparison
## Compare Blood Stasis and Qi Stagnation in terms of Pain Location
?
**Blood Stasis:** Fixed in one spot

**Qi Stagnation:** Moves around
<!--SR:!2025-11-10,3,250-->

---

# Blood Stasis Pattern - Comparison
## Compare Blood Stasis and Qi Stagnation in terms of Tongue
?
**Blood Stasis:** Purple body or purple spots

**Qi Stagnation:** Normal or slightly red sides
<!--SR:!2025-11-10,3,250-->

---

# Blood Stasis Pattern - Memory Aid
## What does the MNEMONIC help you remember?
?
**Mnemonic:** FAST - Fixed pain, Appearance purple, Stabbing quality, Tongue purple

**Applies to:** Cardinal symptoms of Blood Stasis
<!--SR:!2025-11-10,3,250-->

---

# Blood Stasis Pattern - Memory Aid
## What does the ACRONYM help you remember?
?
**Acronym:** PURPLE - Pain fixed, Ugly dark complexion, Rough choppy pulse, Purple tongue, Lesions/masses, Etiology from Qi/Cold/Trauma

**Applies to:** Complete Blood Stasis presentation
<!--SR:!2025-11-10,3,250-->

---

