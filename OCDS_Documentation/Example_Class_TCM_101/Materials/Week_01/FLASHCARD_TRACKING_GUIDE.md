# Flashcard Tracking Guide
**Complete Guide to Spaced Repetition Integration**

---

## 🎯 Overview

This system integrates with Obsidian's **Spaced Repetition plugin** to automatically track your flashcard progress. No manual updates needed!

---

## 📊 What Gets Tracked

### 1. Total Cards
- **Source:** Auto-counted from file
- **Method:** Counts lines with `?` separator
- **Updates:** Every time you open/refresh the file
- **Frontmatter:** `total_cards` and `card_count`

### 2. Cards Reviewed
- **Source:** Spaced Repetition plugin comments
- **Method:** Counts cards with `<!--SR:-->` comments
- **Updates:** After you review cards (must refresh page)
- **Frontmatter:** `cards_reviewed`

### 3. Cards Mastered
- **Source:** Ease factor in SR comments
- **Method:** Counts cards with ease ≥ 250
- **Criteria:** You've successfully reviewed the card
- **Frontmatter:** `cards_mastered`

### 4. Last Review Date
- **Source:** Current date when reviews detected
- **Method:** Set to today when `cards_reviewed` > 0
- **Format:** `YYYY-MM-DD`
- **Frontmatter:** `last_review_date`

---

## 🔧 How It Works

### Step 1: You Review Cards

Using Spaced Repetition plugin:
```
Ctrl/Cmd + P → "Review flashcards"
```

### Step 2: Plugin Adds Comments

After each review, plugin adds:
```markdown
What does a **pale tongue** indicate?
?
Qi Deficiency, Blood Deficiency, Yang Deficiency, or Cold
<!--SR:!2025-11-10,3,250-->
```

### Step 3: Our Script Reads Comments

When you open/refresh Flashcards.md:
```javascript
// Find SR comments
if (nextLine.includes('<!--SR:')) {
  reviewedCards++;
  
  // Extract ease factor
  const match = nextLine.match(/,(\d+)-->/);
  if (match && parseInt(match[1]) >= 250) {
    masteredCards++;
  }
}
```

### Step 4: Frontmatter Updates

```yaml
total_cards: 22          # Auto-counted
cards_reviewed: 21       # From SR comments
cards_mastered: 18       # Ease ≥ 250
last_review_date: 2025-11-07  # Today
```

### Step 5: Dashboard Reads Frontmatter

Dashboard queries read these fields:
```javascript
const reviewed = f.cards_reviewed || 0;
const total = f.total_cards || 0;
const percent = (reviewed / total) * 100;
```

---

## 📈 Progress Calculation

### Overall Completion
```
Completion % = (cards_reviewed / total_cards) × 100
```

**Example:**
- Total: 22 cards
- Reviewed: 21 cards
- Completion: 95.5%

### Mastery Rate
```
Mastery % = (cards_mastered / cards_reviewed) × 100
```

**Example:**
- Reviewed: 21 cards
- Mastered: 18 cards
- Mastery: 85.7%

### Dashboard Status
- **Not Started:** 0% reviewed
- **In Progress:** 1-79% reviewed
- **Complete:** ≥80% reviewed

---

## 🎓 Spaced Repetition Algorithm

### SM-2 Algorithm (Used by Plugin)

The plugin uses the SuperMemo SM-2 algorithm:

1. **First Review:** Interval = 1 day, Ease = 250
2. **Second Review:** Interval = 6 days (if marked "Good")
3. **Subsequent Reviews:** Interval increases based on ease

### How Ease Changes

**Mark "Easy":**
- Ease increases by 15
- Interval multiplied by ease factor
- Example: 250 → 265

**Mark "Good":**
- Ease stays same or increases slightly
- Interval increases normally

**Mark "Hard":**
- Ease decreases by 15
- Interval reduced
- Example: 250 → 235

**Mark "Again":**
- Ease decreases by 20
- Interval reset to 1 day
- Example: 250 → 230

---

## 📊 Tracking Examples

### Example 1: New Deck (Not Started)

**Frontmatter:**
```yaml
total_cards: 22
cards_reviewed: 0
cards_mastered: 0
last_review_date: null
```

**Display:**
```
Cards in Deck: 22
Cards Reviewed: 0 / 22 (0%)
Cards Mastered: 0
Last Review: Not yet
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ 0%
```

**Dashboard:**
- Status: Not Started
- Progress: 0/22 cards (0%)
- Action: Study

---

### Example 2: Partially Reviewed

**Frontmatter:**
```yaml
total_cards: 22
cards_reviewed: 10
cards_mastered: 8
last_review_date: 2025-11-07
```

**Display:**
```
Cards in Deck: 22
Cards Reviewed: 10 / 22 (45%)
Cards Mastered: 8
Last Review: 2025-11-07
█████████████░░░░░░░░░░░░░░░░░ 45%
```

**Dashboard:**
- Status: 🔄 In Progress
- Progress: 10/22 cards (45%)
- Action: Study

---

### Example 3: Mostly Complete

**Frontmatter:**
```yaml
total_cards: 22
cards_reviewed: 20
cards_mastered: 18
last_review_date: 2025-11-07
```

**Display:**
```
Cards in Deck: 22
Cards Reviewed: 20 / 22 (91%)
Cards Mastered: 18
Last Review: 2025-11-07
███████████████████████████░░░ 91%
```

**Dashboard:**
- Status: ✅ Complete (≥80%)
- Progress: 20/22 cards (91%)
- Action: Review

---

### Example 4: All Reviewed

**Frontmatter:**
```yaml
total_cards: 22
cards_reviewed: 22
cards_mastered: 20
last_review_date: 2025-11-07
```

**Display:**
```
Cards in Deck: 22
Cards Reviewed: 22 / 22 (100%)
Cards Mastered: 20
Last Review: 2025-11-07
██████████████████████████████ 100%
```

**Dashboard:**
- Status: ✅ Complete
- Progress: 22/22 cards (100%)
- Action: Review

---

## 🔄 Dynamic Updates

### When You Add Cards

**Before:**
```yaml
total_cards: 20
cards_reviewed: 20
```

**After adding 2 cards:**
```yaml
total_cards: 22  # ← Auto-updated!
cards_reviewed: 20  # ← Stays same (new cards not reviewed yet)
```

**Dashboard updates:**
- Completion: 100% → 91% (20/22)
- Status: Complete → In Progress

### When You Review New Cards

**After reviewing the 2 new cards:**
```yaml
total_cards: 22
cards_reviewed: 22  # ← Updated!
```

**Dashboard updates:**
- Completion: 91% → 100%
- Status: In Progress → Complete

---

## 🧪 Testing Scenarios

### Test 1: Review First Card
1. Review 1 card
2. Refresh Flashcards.md
3. Should show: `1 / 22 (5%)`

### Test 2: Review Half
1. Review 11 cards
2. Refresh Flashcards.md
3. Should show: `11 / 22 (50%)`

### Test 3: Complete Deck
1. Review all 22 cards
2. Refresh Flashcards.md
3. Should show: `22 / 22 (100%)`
4. Dashboard shows: ✅ Complete

### Test 4: Add New Cards
1. Add 3 new cards
2. Refresh Flashcards.md
3. Should show: `22 / 25 (88%)`
4. Status changes to: In Progress

### Test 5: Review New Cards
1. Review the 3 new cards
2. Refresh Flashcards.md
3. Should show: `25 / 25 (100%)`
4. Status: Complete again

---

## 💡 Pro Tips

### 1. Refresh After Reviewing
Always refresh Flashcards.md after a review session to see updated stats.

### 2. Check Dashboard
Dashboard shows aggregate progress across all flashcard decks.

### 3. Mastery Matters
Focus on getting cards to "Mastered" status (ease ≥ 250).

### 4. Review Regularly
Plugin schedules reviews optimally - follow the schedule!

### 5. Add Cards Anytime
System dynamically adjusts to new cards.

---

## 🐛 Troubleshooting

### Progress Not Updating

**Problem:** Reviewed cards but stats don't change

**Solutions:**
1. Refresh Flashcards.md (Ctrl/Cmd + R)
2. Check for SR comments in file
3. Verify Spaced Repetition plugin is active
4. Close and reopen file

### Dashboard Shows Old Data

**Problem:** Dashboard doesn't match Flashcards.md

**Solutions:**
1. Refresh Flashcards.md first (updates frontmatter)
2. Then refresh Dashboard (reads frontmatter)
3. Check frontmatter values (Ctrl/Cmd + E)

### Cards Not Counting as Mastered

**This is normal!**
- First review: ease = 250 (mastered)
- Mark "Hard": ease < 250 (not mastered)
- Review again with "Good" or "Easy" to increase ease

---

## 📝 Summary

**Automatic Tracking:**
- ✅ Total cards (auto-counted)
- ✅ Cards reviewed (from SR comments)
- ✅ Cards mastered (ease ≥ 250)
- ✅ Last review date (auto-set)

**Manual Steps:**
- Review cards using SR plugin
- Refresh Flashcards.md to update stats
- Refresh Dashboard to see progress

**Everything else is automatic!** 🎉

---

**Status:** Fully integrated with Spaced Repetition plugin
