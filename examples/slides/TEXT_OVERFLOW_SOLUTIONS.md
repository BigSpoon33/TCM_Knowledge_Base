# Text Overflow Solutions for Advanced Slides

Solutions for handling text that goes out of bounds in grid layouts.

---

## Problem: Text Overflowing Grid Boxes

When text content is too long for the grid box, it can overflow and look messy.

### Common Causes:
1. Too much content for box size
2. Long words or terms
3. Fixed grid heights
4. Small font sizes

---

## Solution 1: Auto-Scrolling (Best for Long Content)

Add `style="overflow-y: auto;"` to make boxes scrollable:


---
<grid drag="100 15" drop="top" align="center">
## Cold vs Heat Patterns
</grid>

<grid drag="45 80" drop="5 20" bg="#4A90E2" pad="20px" style="overflow-y: auto;">

### Cold Pattern

**Symptoms:**
- Pale complexion
- Cold limbs
- Clear urine
- Loose stools
- Aversion to cold
- Preference for warmth

**Tongue:** Pale, wet, swollen
**Pulse:** Slow, deep, weak

**Treatment:** Warm and tonify

</grid>

<grid drag="45 80" drop="-5 20" bg="#E24A4A" pad="20px" style="overflow-y: auto;">

### Heat Pattern

**Symptoms:**
- Red face
- Thirst
- Dark urine
- Constipation
- Restlessness
- Preference for cold

**Tongue:** Red, dry, yellow coating
**Pulse:** Rapid, full, strong

**Treatment:** Clear heat

</grid>

---


**Pros**: Handles any amount of content
**Cons**: Requires scrolling during presentation

---

## Solution 2: Smaller Font Size (Best for Slightly Too Much Content)

Use CSS to reduce font size within grids:


---
<style>
.compact-text {
    font-size: 0.8em;
    line-height: 1.3;
}

.compact-text h3 {
    font-size: 1.2em;
    margin-bottom: 10px;
}

.compact-text ul {
    margin: 5px 0;
}
</style>

<grid drag="100 15" drop="top" align="center">
## Cold vs Heat Patterns
</grid>

<grid drag="45 80" drop="5 20" bg="#4A90E2" pad="20px" class="compact-text">

### Cold Pattern

**Symptoms:**
- Pale complexion
- Cold limbs
- Clear urine
- Loose stools

**Tongue:** Pale, wet
**Pulse:** Slow, deep

</grid>

<grid drag="45 80" drop="-5 20" bg="#E24A4A" pad="20px" class="compact-text">

### Heat Pattern

**Symptoms:**
- Red face
- Thirst
- Dark urine
- Constipation

**Tongue:** Red, dry
**Pulse:** Rapid, full

</grid>

---


**Pros**: Clean look, no scrolling
**Cons**: Text may be too small for some audiences

---

## Solution 3: Taller Boxes (Best for Predictable Content)

Increase grid height to accommodate content:


---
<grid drag="100 15" drop="top" align="center">
## Cold vs Heat Patterns
</grid>

<grid drag="45 82" drop="5 18" bg="#4A90E2" pad="20px">

### Cold Pattern

**Symptoms:**
- Pale complexion
- Cold limbs
- Clear urine
- Loose stools

**Tongue:** Pale, wet
**Pulse:** Slow, deep

</grid>

<grid drag="45 82" drop="-5 18" bg="#E24A4A" pad="20px">

### Heat Pattern

**Symptoms:**
- Red face
- Thirst
- Dark urine
- Constipation

**Tongue:** Red, dry
**Pulse:** Rapid, full

</grid>

---


**Changes:**
- Height increased from 80% to 82%
- Start position moved from 20% to 18%
- Gives more vertical space

**Pros**: Simple, no special CSS
**Cons**: May not fit all screen sizes

---

## Solution 4: Reduce Content (Best for Presentations)

Keep only essential information on slide:


---
<grid drag="100 15" drop="top" align="center">
## Cold vs Heat Patterns
</grid>

<grid drag="45 80" drop="5 20" bg="#4A90E2" pad="20px">

### ❄️ Cold Pattern

- Pale complexion
- Cold limbs
- Clear urine
- Loose stools

**Tongue:** Pale, wet
**Pulse:** Slow, deep

</grid>

<grid drag="45 80" drop="-5 20" bg="#E24A4A" pad="20px">

### 🔥 Heat Pattern

- Red face
- Thirst
- Dark urine
- Constipation

**Tongue:** Red, dry
**Pulse:** Rapid, full

</grid>

---


**Changes:**
- Removed "Symptoms:" header
- Simplified bullet points
- Added emoji for visual interest

**Pros**: Clean, readable, professional
**Cons**: Less detailed information

---

## Solution 5: Vertical Slides for Details

Use main slide for overview, vertical slides for details:


---
<grid drag="100 15" drop="top" align="center">
## Cold vs Heat Patterns
</grid>

<grid drag="45 80" drop="5 20" bg="#4A90E2" pad="20px" align="center">

### ❄️ Cold Pattern

**Key Features:**
- Pale, cold
- Slow, deep pulse

↓ *Details below*

</grid>

<grid drag="45 80" drop="-5 20" bg="#E24A4A" pad="20px" align="center">

### 🔥 Heat Pattern

**Key Features:**
- Red, hot
- Rapid, full pulse

↓ *Details below*

</grid>

---

----

### Cold Pattern - Full Details

**All Symptoms:**
- Pale complexion
- Cold limbs
- Clear urine
- Loose stools
- Aversion to cold
- Preference for warmth
- Fatigue

**Tongue:** Pale, wet, swollen
**Pulse:** Slow, deep, weak

**Treatment Principle:** Warm and tonify yang

----

### Heat Pattern - Full Details

**All Symptoms:**
- Red face
- Thirst
- Dark urine
- Constipation
- Restlessness
- Preference for cold
- Irritability

**Tongue:** Red, dry, yellow coating
**Pulse:** Rapid, full, strong

**Treatment Principle:** Clear heat and nourish yin

----

---


**Pros**: Best of both worlds - clean overview + full details
**Cons**: Requires navigation (down arrow)

---

## Solution 6: Dynamic Font Sizing with CSS

Make text automatically adjust to container:


---
<style>
.auto-fit {
    font-size: clamp(0.7em, 1.5vw, 1em);
    line-height: 1.4;
}

.auto-fit h3 {
    font-size: clamp(1em, 2vw, 1.5em);
}

.auto-fit ul {
    margin: 8px 0;
}

.auto-fit li {
    margin: 3px 0;
}
</style>

<grid drag="100 15" drop="top" align="center">
## Cold vs Heat Patterns
</grid>

<grid drag="45 80" drop="5 20" bg="#4A90E2" pad="20px" class="auto-fit">

### Cold Pattern

**Symptoms:**
- Pale complexion
- Cold limbs
- Clear urine
- Loose stools

**Tongue:** Pale, wet
**Pulse:** Slow, deep

</grid>

<grid drag="45 80" drop="-5 20" bg="#E24A4A" pad="20px" class="auto-fit">

### Heat Pattern

**Symptoms:**
- Red face
- Thirst
- Dark urine
- Constipation

**Tongue:** Red, dry
**Pulse:** Rapid, full

</grid>

---


**How it works:**
- `clamp(min, preferred, max)` adjusts font size based on viewport
- `0.7em` = minimum size
- `1.5vw` = preferred size (1.5% of viewport width)
- `1em` = maximum size

**Pros**: Responsive, adapts to screen size
**Cons**: Requires CSS knowledge

---

## Solution 7: Ellipsis for Long Text

Truncate text with "..." when it overflows:


---
<style>
.truncate {
    overflow: hidden;
    text-overflow: ellipsis;
}

.truncate li {
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}
</style>

<grid drag="100 15" drop="top" align="center">
## Cold vs Heat Patterns
</grid>

<grid drag="45 80" drop="5 20" bg="#4A90E2" pad="20px" class="truncate">

### Cold Pattern

**Symptoms:**
- Pale complexion
- Cold limbs
- Clear urine
- Loose stools

**Tongue:** Pale, wet
**Pulse:** Slow, deep

</grid>

<grid drag="45 80" drop="-5 20" bg="#E24A4A" pad="20px" class="truncate">

### Heat Pattern

**Symptoms:**
- Red face
- Thirst
- Dark urine
- Constipation

**Tongue:** Red, dry
**Pulse:** Rapid, full

</grid>

---


**Pros**: Prevents overflow completely
**Cons**: Hides content (not ideal for presentations)

---

## Recommended Approach by Use Case

### For Teaching/Classroom
**Use Solution 5** (Vertical slides for details)
- Overview on main slide
- Full details on vertical slides
- Students can review details later

### For Quick Reference
**Use Solution 4** (Reduce content)
- Only essential information
- Clean and readable
- Professional appearance

### For Comprehensive Content
**Use Solution 1** (Auto-scrolling)
- All information visible
- Scrollable if needed
- Good for reference slides

### For Variable Screen Sizes
**Use Solution 6** (Dynamic font sizing)
- Adapts to projector/screen
- Consistent appearance
- Professional look

---

## Complete Example: All Solutions Combined


---
theme: black
---

<style>
/* Solution 2: Compact text */
.compact {
    font-size: 0.85em;
    line-height: 1.3;
}

/* Solution 6: Dynamic sizing */
.auto-fit {
    font-size: clamp(0.7em, 1.5vw, 1em);
    line-height: 1.4;
}

/* Custom styling */
.pattern-box {
    border-radius: 10px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.3);
}
</style>

---

<!-- Solution 4: Reduced content -->
<grid drag="100 15" drop="top" align="center">
## Cold vs Heat Patterns
</grid>

<grid drag="45 80" drop="5 20" bg="#4A90E2" pad="20px" class="pattern-box compact">

### ❄️ Cold

- Pale, cold
- Clear urine
- Loose stools

**T:** Pale, wet
**P:** Slow, deep

</grid>

<grid drag="45 80" drop="-5 20" bg="#E24A4A" pad="20px" class="pattern-box compact">

### 🔥 Heat

- Red, hot
- Dark urine
- Constipation

**T:** Red, dry
**P:** Rapid, full

</grid>

---

<!-- Solution 5: Vertical slides for full details -->

----

<grid drag="100 15" drop="top" align="center" bg="#4A90E2">
### ❄️ Cold Pattern - Complete Details
</grid>

<grid drag="90 80" drop="center" pad="30px" style="overflow-y: auto;" class="auto-fit">

**All Symptoms:**
- Pale complexion
- Cold limbs
- Clear, copious urine
- Loose stools
- Aversion to cold
- Preference for warmth
- Fatigue and weakness
- Lack of thirst

**Tongue:** Pale body, wet coating, may be swollen
**Pulse:** Slow, deep, weak

**Pathomechanism:** Yang deficiency leading to cold

**Treatment Principle:** Warm and tonify yang qi

**Key Formulas:**
- Si Ni Tang
- Fu Zi Li Zhong Wan

</grid>

----

<grid drag="100 15" drop="top" align="center" bg="#E24A4A">
### 🔥 Heat Pattern - Complete Details
</grid>

<grid drag="90 80" drop="center" pad="30px" style="overflow-y: auto;" class="auto-fit">

**All Symptoms:**
- Red face
- Thirst with desire for cold drinks
- Dark, scanty urine
- Constipation with dry stools
- Restlessness and irritability
- Preference for cold
- Feeling of heat in body
- Possible fever

**Tongue:** Red body, dry with yellow coating
**Pulse:** Rapid, full, strong

**Pathomechanism:** Excess heat or yin deficiency

**Treatment Principle:** Clear heat and nourish yin

**Key Formulas:**
- Bai Hu Tang
- Zhi Zi Chi Tang

</grid>

----

---


---

## Quick Decision Guide

| Situation | Best Solution | Why |
|-----------|---------------|-----|
| Teaching class | #5 (Vertical slides) | Overview + details |
| Quick reference | #4 (Reduce content) | Clean and simple |
| Lots of content | #1 (Scrolling) | Everything visible |
| Unknown screen size | #6 (Dynamic sizing) | Adapts automatically |
| Slightly too much | #2 (Smaller font) | Easy fix |
| Fixed content | #3 (Taller boxes) | Simple adjustment |

---

## Pro Tips

1. **Test on actual projector** - What looks good on laptop may overflow on projector
2. **Use speaker notes** - Put extra details in notes instead of on slide
3. **Break into multiple slides** - Better than cramming everything on one
4. **Prioritize information** - Most important points first
5. **Use abbreviations** - "T:" for Tongue, "P:" for Pulse
6. **Consider your audience** - Students need more detail than quick reference

---

## Common Mistakes to Avoid

❌ **Don't**: Cram too much text on one slide
✅ **Do**: Use vertical slides for additional details

❌ **Don't**: Use tiny fonts to fit everything
✅ **Do**: Reduce content or use multiple slides

❌ **Don't**: Let text overflow without handling it
✅ **Do**: Choose appropriate solution for your use case

❌ **Don't**: Forget to test in presentation mode
✅ **Do**: Always preview before presenting

---

*Use these solutions to create professional, readable TCM presentations!*
