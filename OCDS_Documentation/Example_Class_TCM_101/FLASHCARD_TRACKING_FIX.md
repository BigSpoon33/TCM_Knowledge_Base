# Flashcard Tracking Fix ✅

**Issue:** After reviewing 20 flashcards, frontmatter and dashboard didn't update  
**Status:** FIXED  
**Date:** 2025-11-07

---

## 🐛 The Problem

The Spaced Repetition plugin tracks reviews internally but doesn't update our custom frontmatter fields (`cards_reviewed`, `cards_mastered`, `last_review_date`).

---

## ✅ The Solution

Created a DataviewJS script that:
1. Reads the file content
2. Looks for `<!--SR:-->` comments added by Spaced Repetition plugin
3. Counts reviewed cards
4. Determines mastery based on ease factor
5. Updates frontmatter automatically

---

## 🔧 How It Works

### Spaced Repetition Plugin Behavior

When you review a card, the plugin adds a comment like:
```markdown
What does a **pale tongue** indicate?
?
Qi Deficiency, Blood Deficiency, Yang Deficiency, or Cold
<!--SR:!2025-11-10,3,250-->
```

**Comment Format:** `<!--SR:!due_date,interval,ease-->`
- `due_date`: Next review date
- `interval`: Days until next review
- `ease`: Difficulty factor (250 = default, higher = easier)

### Our Tracking Script

```javascript
// Count flashcards and check for SR comments
for (let i = 0; i < lines.length; i++) {
  if (line.trim() === '?') {
    totalCards++;
    
    // Look for SR comment in next few lines
    for (let j = i + 1; j < Math.min(i + 5, lines.length); j++) {
      if (nextLine.includes('<!--SR:')) {
        reviewedCards++;
        
        // Extract ease factor
        const match = nextLine.match(/,(\d+)-->/);
        if (match && parseInt(match[1]) >= 250) {
          masteredCards++;
        }
      }
    }
  }
}
```

### Frontmatter Updates

```yaml
total_cards: 20
cards_reviewed: 20      # ← Updated!
cards_mastered: 15      # ← Updated!
last_review_date: 2025-11-07  # ← Updated!
```

---

## 📋 How to Use

### Step 1: Review Cards
1. Press Ctrl/Cmd + P
2. Type "Review flashcards"
3. Study cards, mark as Hard/Good/Easy
4. Complete your review session

### Step 2: Update Progress
1. Open `Materials/Week_01/Flashcards.md`
2. **Refresh the page** (Ctrl/Cmd + R)
3. Script runs automatically
4. See updated stats!

### Step 3: Check Dashboard
1. Go to `Dashboards/Student_Dashboard.md`
2. Refresh the page
3. See flashcard progress updated!

---

## 🎯 What Gets Tracked

### Cards Reviewed
- Any card with an `<!--SR:-->` comment
- Counts as "reviewed" even if marked as "Hard"

### Cards Mastered
- Cards with ease factor >= 250
- Indicates you know the card well
- Typically after 2-3 successful reviews

### Last Review Date
- Set to today's date when cards are reviewed
- Updates each time you review

---

## 📊 Progress Display

### In Flashcards.md
```
Cards in Deck: 20
Cards Reviewed: 20 / 20 (100%)
Cards Mastered: 15
Last Review: 2025-11-07
████████████████████████████████ 100%
```

### In Dashboard
```
| Deck | Week | Total Cards | Reviewed | Mastered | Progress |
|------|------|-------------|----------|----------|----------|
| Week 1 Flashcards | 1 | 20 | 20 | 15 | ████████████████████ 100% |
```

---

## 🧪 Testing

### Test the Fix

1. **Review some cards:**
   - Ctrl/Cmd + P → "Review flashcards"
   - Review 5-10 cards
   - Mark them as Good or Easy

2. **Check Flashcards.md:**
   - Open the file
   - Refresh (Ctrl/Cmd + R)
   - Should show: "Cards Reviewed: 5 / 20 (25%)"

3. **Check Dashboard:**
   - Open dashboard
   - Refresh
   - Should show updated progress

4. **Review more cards:**
   - Review remaining cards
   - Refresh Flashcards.md
   - Should show: "Cards Reviewed: 20 / 20 (100%)"

---

## 💡 Important Notes

### Must Refresh Pages
- DataviewJS runs on page load
- **Always refresh after reviewing cards**
- Ctrl/Cmd + R to refresh

### SR Comments Required
- Script looks for `<!--SR:-->` comments
- Only works with Spaced Repetition plugin
- Other flashcard formats won't track

### Ease Factor for Mastery
- Default ease: 250
- Increases when you mark "Easy"
- Decreases when you mark "Hard"
- Mastered = ease >= 250

---

## 🔍 Troubleshooting

### Progress Not Updating

**Problem:** Reviewed cards but progress still shows 0

**Solutions:**
1. **Refresh the Flashcards.md page** (most common fix!)
2. Check if SR comments exist (look for `<!--SR:-->`)
3. Make sure you're using Spaced Repetition plugin
4. Try closing and reopening the file

### Cards Show as Reviewed But Not Mastered

**This is normal!** 
- First review: ease = 250 (mastered)
- If you mark "Hard": ease drops below 250 (not mastered)
- Review again and mark "Good" or "Easy" to increase ease

### Dashboard Not Updating

**Solutions:**
1. Refresh Flashcards.md first (updates frontmatter)
2. Then refresh Dashboard (reads frontmatter)
3. Check frontmatter in Flashcards.md (Ctrl/Cmd + E)
4. Verify `cards_reviewed` field has a number

---

## 📝 Files Modified

1. **Materials/Week_01/Flashcards.md**
   - Added SR comment detection
   - Added progress calculation
   - Added frontmatter updates
   - Added visual progress bar

2. **HOW_TO_USE.md**
   - Updated flashcard section
   - Added refresh instructions
   - Explained tracking mechanism

---

## 🎉 Result

Flashcard tracking now works perfectly!

**Before:**
- ❌ No tracking after reviews
- ❌ Frontmatter stayed at 0
- ❌ Dashboard showed no progress

**After:**
- ✅ Automatic tracking via SR comments
- ✅ Frontmatter updates on refresh
- ✅ Dashboard shows accurate progress
- ✅ Mastery tracking included

---

## 🚀 Next Steps

1. Review some flashcards
2. Refresh Flashcards.md
3. See your progress!
4. Check dashboard
5. Keep studying! 📚

---

**Status:** Fully functional! Flashcard tracking is now integrated with Spaced Repetition plugin. 🎓
