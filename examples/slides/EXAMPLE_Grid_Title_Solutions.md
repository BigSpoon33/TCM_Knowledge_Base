---
theme: black
transition: slide
slideNumber: true
progress: true
---

# Grid Title Positioning Examples

Demonstrating different ways to position titles above grid content

---

## Solution 1: Simple Top Grid

Clean title at top, content boxes below

---

<grid drag="100 15" drop="top" align="center">
## Cold vs Heat Patterns
</grid>

<grid drag="45 80" drop="5 20" bg="#4A90E2" pad="20px">

### Cold Pattern

**Symptoms:**
- Pale complexion
- Cold limbs
- Clear urine
- Loose stools

**Tongue:** Pale, wet
**Pulse:** Slow, deep

</grid>

<grid drag="45 80" drop="-5 20" bg="#E24A4A" pad="20px">

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

## Solution 2: Styled Title Bar

Title bar with background and visual separation

---

<grid drag="100 20" drop="top" bg="rgba(255,255,255,0.1)" align="center" pad="10px" border="0 0 2px 0 solid rgba(255,255,255,0.3)">
## Cold vs Heat Patterns
</grid>

<grid drag="45 75" drop="5 25" bg="#4A90E2" pad="20px">

### Cold Pattern

**Symptoms:**
- Pale complexion
- Cold limbs
- Clear urine
- Loose stools

**Tongue:** Pale, wet
**Pulse:** Slow, deep

</grid>

<grid drag="45 75" drop="-5 25" bg="#E24A4A" pad="20px">

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

## Solution 2 Variation: Colored Title Bar

Using a gradient background for the title

---

<grid drag="100 20" drop="top" bg="linear-gradient(135deg, #667eea 0%, #764ba2 100%)" align="center" pad="10px">
## Cold vs Heat Patterns
</grid>

<grid drag="45 75" drop="5 25" bg="#4A90E2" pad="20px">

### Cold Pattern

**Symptoms:**
- Pale complexion
- Cold limbs
- Clear urine
- Loose stools

**Tongue:** Pale, wet
**Pulse:** Slow, deep

</grid>

<grid drag="45 75" drop="-5 25" bg="#E24A4A" pad="20px">

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

## Solution 2 Variation: TCM Category Bar

Title bar styled for TCM pattern category

---

<style>
.pattern-title-bar {
    background: linear-gradient(135deg, #581c87 0%, #a855f7 100%);
    border-radius: 10px 10px 0 0;
    box-shadow: 0 4px 6px rgba(0,0,0,0.3);
}
</style>

<grid drag="100 18" drop="top" class="pattern-title-bar" align="center" pad="12px">
## 🔍 Cold vs Heat Patterns
</grid>

<grid drag="45 77" drop="5 23" bg="#4A90E2" pad="20px" border="2px solid rgba(255,255,255,0.2)">

### ❄️ Cold Pattern

**Symptoms:**
- Pale complexion
- Cold limbs
- Clear urine
- Loose stools

**Tongue:** Pale, wet
**Pulse:** Slow, deep

</grid>

<grid drag="45 77" drop="-5 23" bg="#E24A4A" pad="20px" border="2px solid rgba(255,255,255,0.2)">

### 🔥 Heat Pattern

**Symptoms:**
- Red face
- Thirst
- Dark urine
- Constipation

**Tongue:** Red, dry
**Pulse:** Rapid, full

</grid>

---

## Comparison Summary

**Solution 1 (Simple Top Grid)**
- ✅ Clean and minimal
- ✅ Easy to implement
- ✅ Consistent positioning
- ❌ Less visual impact

**Solution 2 (Styled Title Bar)**
- ✅ Professional appearance
- ✅ Visual hierarchy
- ✅ Category identification
- ✅ Customizable styling
- ❌ Slightly more complex

---

## When to Use Each

### Use Solution 1 When:
- You want simplicity
- Content is the focus
- Minimal styling needed
- Quick implementation

### Use Solution 2 When:
- Creating polished presentations
- Need visual hierarchy
- Branding/category colors important
- Teaching/professional context

---

## Pro Tips

1. **Consistent spacing**: Keep title height at 15-20% for balance
2. **Content positioning**: Start content boxes at 20-25% from top
3. **Box heights**: Adjust to 75-80% to fit below title
4. **Alignment**: Always use `align="center"` for titles
5. **Padding**: Add padding to title for breathing room

---

## More Examples

Different content types with proper title positioning

---

<grid drag="100 18" drop="top" bg="linear-gradient(135deg, #2d5016 0%, #4a7c2c 100%)" align="center" pad="10px">
## 🌿 Herb Properties Comparison
</grid>

<grid drag="30 77" drop="5 23" bg="rgba(255,255,255,0.1)" pad="15px" border="2px solid #4a7c2c">

### Ai Ye
**Taste:** Bitter, Acrid
**Temp:** Warm
**Channels:** Sp, Liv, Kid

**Function:**
Warms Womb, stops bleeding

</grid>

<grid drag="30 77" drop="35 23" bg="rgba(255,255,255,0.1)" pad="15px" border="2px solid #4a7c2c">

### Sheng Di Huang
**Taste:** Sweet, Bitter
**Temp:** Cold
**Channels:** Ht, Liv, Kid

**Function:**
Cools blood, stops bleeding

</grid>

<grid drag="30 77" drop="-5 23" bg="rgba(255,255,255,0.1)" pad="15px" border="2px solid #4a7c2c">

### Bai Ji
**Taste:** Bitter, Sweet, Astringent
**Temp:** Slightly Cold
**Channels:** Lu, Liv, St

**Function:**
Astringes, stops bleeding

</grid>

---

<grid drag="100 18" drop="top" bg="linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%)" align="center" pad="10px">
## 💊 Formula Building Progression
</grid>

<grid drag="28 75" drop="5 25" bg="rgba(16, 185, 129, 0.3)" border="3px solid #10b981" pad="15px" flow="col">

### Si Jun Zi Tang
**Four Gentlemen**

Tonifies Qi

**Herbs:** 4
- Ren Shen
- Bai Zhu
- Fu Ling
- Gan Cao

</grid>

<grid drag="8 75" drop="36 25" align="center" flow="col" pad="30px 0">

### +

</grid>

<grid drag="28 75" drop="46 25" bg="rgba(239, 68, 68, 0.3)" border="3px solid #ef4444" pad="15px" flow="col">

### Si Wu Tang
**Four Substances**

Nourishes Blood

**Herbs:** 4
- Dang Gui
- Shu Di Huang
- Bai Shao
- Chuan Xiong

</grid>

<grid drag="8 75" drop="77 25" align="center" flow="col" pad="30px 0">

### =

</grid>

<grid drag="12 75" drop="-3 25" bg="rgba(245, 158, 11, 0.3)" border="3px solid #f59e0b" pad="15px" align="center" flow="col">

### Ba Zhen Tang

**8 Herbs**

Qi + Blood

</grid>

---

<grid drag="100 18" drop="top" bg="linear-gradient(135deg, #7f1d1d 0%, #dc2626 100%)" align="center" pad="10px">
## 📍 Point Location Comparison
</grid>

<grid drag="48 77" drop="2 23" bg="rgba(255,255,255,0.05)" pad="15px">

### ST-36 (Zusanli)

**Location:**
3 cun below ST-35
1 finger lateral to tibia

**Special Properties:**
- He-Sea point
- Earth point
- Command point

**Primary Function:**
Tonifies qi and blood

</grid>

<grid drag="48 77" drop="-2 23" bg="rgba(255,255,255,0.05)" pad="15px">

### ST-40 (Fenglong)

**Location:**
8 cun above lateral malleolus
2 fingers lateral to tibia

**Special Properties:**
- Luo-connecting point

**Primary Function:**
Transforms phlegm and dampness

</grid>

---

## Copy-Paste Templates

Ready to use in your slides

---

### Template 1: Simple Top Grid


<grid drag="100 15" drop="top" align="center">
## Your Title Here
</grid>

<grid drag="45 80" drop="5 20" bg="#4A90E2" pad="20px">
Left content
</grid>

<grid drag="45 80" drop="-5 20" bg="#E24A4A" pad="20px">
Right content
</grid>


---

### Template 2: Styled Title Bar


<grid drag="100 20" drop="top" bg="linear-gradient(135deg, #667eea 0%, #764ba2 100%)" align="center" pad="10px">
## Your Title Here
</grid>

<grid drag="45 75" drop="5 25" bg="#4A90E2" pad="20px">
Left content
</grid>

<grid drag="45 75" drop="-5 25" bg="#E24A4A" pad="20px">
Right content
</grid>


---

### Template 3: Three Column with Title


<grid drag="100 18" drop="top" bg="linear-gradient(135deg, #2d5016 0%, #4a7c2c 100%)" align="center" pad="10px">
## Your Title Here
</grid>

<grid drag="30 77" drop="5 23" bg="rgba(255,255,255,0.1)" pad="15px">
Column 1
</grid>

<grid drag="30 77" drop="35 23" bg="rgba(255,255,255,0.1)" pad="15px">
Column 2
</grid>

<grid drag="30 77" drop="-5 23" bg="rgba(255,255,255,0.1)" pad="15px">
Column 3
</grid>


---

## Key Measurements Reference

### Title Grid
- **Height**: 15-20% of slide
- **Position**: `drop="top"`
- **Padding**: 10-12px

### Content Grids
- **Start Position**: 20-25% from top
- **Height**: 75-80% of slide
- **Spacing**: 5% from edges, 2-5% between boxes

### Two Column Layout
- **Width**: 45-48% each
- **Left**: `drop="5 20"` or `drop="2 20"`
- **Right**: `drop="-5 20"` or `drop="-2 20"`

### Three Column Layout
- **Width**: 30% each
- **Left**: `drop="5 23"`
- **Center**: `drop="35 23"`
- **Right**: `drop="-5 23"`

---

# End of Examples

Test these in presentation mode to see the difference!

---
