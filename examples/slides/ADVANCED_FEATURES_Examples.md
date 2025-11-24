# Advanced Slides Features - TCM Examples

This document demonstrates advanced animations, custom CSS, layouts, and visual effects for TCM presentations.

---

## Table of Contents

1. [Fragments & Progressive Reveal](#fragments)
2. [Auto-Animations](#auto-animations)
3. [Grid Layouts](#grid-layouts)
4. [Custom CSS Styling](#custom-css)
5. [Background Effects](#backgrounds)
6. [Complete Example Slides](#complete-examples)

---

## 1. FRAGMENTS & PROGRESSIVE REVEAL {#fragments}

### Basic Fragment Example - Herb Functions

---
## ⚡ Functions of Ai Ye

1. Warms the Womb and stops bleeding <!-- element class="fragment" -->
2. Disperses cold and alleviates pain <!-- element class="fragment" -->
3. Eliminates dampness and stops itching <!-- element class="fragment" -->

> Clinical Pearl: Best for cold-type gynecological disorders <!-- element class="fragment fade-in" -->

---

**Effect**: Each function appears one at a time when you advance

---

### Fragment Types for TCM Content

---
## Pattern Differentiation

### Cold vs Heat Bleeding

**Cold Type** <!-- element class="fragment fade-right" -->
- Pale blood <!-- element class="fragment" -->
- Cold abdomen <!-- element class="fragment" -->
- Pale tongue <!-- element class="fragment" -->

**Heat Type** <!-- element class="fragment fade-left" -->
- Bright red blood <!-- element class="fragment" -->
- Thirst <!-- element class="fragment" -->
- Red tongue <!-- element class="fragment" -->

---

**Available Fragment Types**:
- `fragment` - Basic fade in
- `fragment fade-out` - Fade out
- `fragment fade-up` - Slide up while fading
- `fragment fade-down` - Slide down while fading
- `fragment fade-left` - Slide from left
- `fragment fade-right` - Slide from right
- `fragment highlight-red` - Highlight in red
- `fragment highlight-green` - Highlight in green
- `fragment highlight-blue` - Highlight in blue
- `fragment grow` - Grow in size
- `fragment shrink` - Shrink in size

---

### Controlled Fragment Order

---
## Formula Composition - Si Jun Zi Tang

**Herbs appear in order of importance:**

- Gan Cao (Envoy) <!-- element class="fragment" data-fragment-index="4" -->
- Fu Ling (Deputy) <!-- element class="fragment" data-fragment-index="3" -->
- Bai Zhu (Deputy) <!-- element class="fragment" data-fragment-index="2" -->
- Ren Shen (Chief) <!-- element class="fragment" data-fragment-index="1" -->

---

**Effect**: Herbs appear in reverse order (Chief first, then Deputies, then Envoy)

---

### Fragment Lists (Auto-numbered)

---
## Treatment Principles

+ Tonify qi <!-- element class="fragment-list" -->
+ Strengthen Spleen
+ Resolve dampness
+ Harmonize middle jiao

---

**Effect**: Each item appears automatically in sequence

---

## 2. AUTO-ANIMATIONS {#auto-animations}

### Morphing Title Animation


---
<!-- .slide: data-auto-animate -->
# Ai Ye 


---
<!-- .slide: data-auto-animate -->

# Ai Ye
## 艾叶
### *Artemisia argyi*

---

**Effect**: Title smoothly morphs and additional text slides in

---

### Formula Building Animation

---
<!-- .slide: data-auto-animate -->
## Si Jun Zi Tang

| Herb | Role |
|------|------|
| Ren Shen | Chief |

---
<!-- .slide: data-auto-animate -->

## Si Jun Zi Tang

| Herb | Role |
|------|------|
| Ren Shen | Chief |
| Bai Zhu | Deputy |

---
<!-- .slide: data-auto-animate -->

## Si Jun Zi Tang

| Herb | Role |
|------|------|
| Ren Shen | Chief |
| Bai Zhu | Deputy |
| Fu Ling | Deputy |
| Gan Cao | Envoy |

---

**Effect**: Table rows smoothly animate in, showing formula building progressively

---

### Point Location Zoom

---
<!-- .slide: data-auto-animate -->

![[ST-36_diagram.jpg|400]]

---
<!-- .slide: data-auto-animate -->

![[ST-36_diagram.jpg|800]]

### ST-36 Location Detail

---

**Effect**: Image smoothly zooms from small to large

---

## 3. GRID LAYOUTS {#grid-layouts}

### Side-by-Side Comparison (FIXED)

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

**Effect**: Title anchored at top, two colored boxes side-by-side for easy comparison

**Key Changes:**
- Added title grid with `drop="top"` to anchor at top
- Changed left box from `drop="left"` to `drop="5 20"` (5% from left, 20% from top)
- Changed right box from `drop="right"` to `drop="-5 20"` (5% from right, 20% from top)

**Text Overflow Solution**: See `TEXT_OVERFLOW_SOLUTIONS.md` for handling long content

---

### Herb Properties Layout (FIXED)


---
<grid drag="100 18" drop="top" bg="linear-gradient(135deg, #2d5016 0%, #4a7c2c 100%)" align="center" pad="10px">
## 🌿 Ai Ye - Mugwort Leaf
</grid>

<grid drag="30 77" drop="5 23" border="2px solid white" pad="15px">

### Properties
- **Taste**: Bitter, Acrid
- **Temp**: Warm
- **Channels**: Sp, Liv, Kid

</grid>

<grid drag="65 77" drop="-5 23" pad="15px">

### Functions
1. Warms Womb, stops bleeding
2. Disperses cold, alleviates pain
3. Eliminates dampness, stops itching

### Key Formulas
- Jiao Ai Tang
- Ai Fu Nuan Gong Wan

</grid>

---


**Effect**: Styled title bar at top, properties box on left, main content on right

**Key Changes:**
- Title bar with gradient background (18% height)
- Content boxes start at 23% from top (below title)
- Boxes are 77% height to fit below title

---

### Point Location with Annotations (FIXED)


---
<grid drag="100 15" drop="top" align="center">
## 📍 ST-36 Location
</grid>

<grid drag="50 80" drop="2 20">
![[ST-36_diagram.jpg]]
</grid>

<grid drag="45 30" drop="-3 25" bg="rgba(255,255,255,0.9)" border="3px solid red" pad="15px">

### Location
3 cun below ST-35
1 finger lateral to tibia

</grid>

<grid drag="45 30" drop="-3 60" bg="rgba(255,255,255,0.9)" border="3px solid blue" pad="15px">

### Special Properties
- He-Sea point
- Command point
- Heavenly Star

</grid>

---


**Effect**: Title at top, image on left, floating annotation boxes on right

**Key Changes:**
- Added title grid at top
- Image positioned at 2% from left, 20% from top
- Annotation boxes positioned at specific vertical positions (25% and 60%)

---

### Formula Composition Grid (FIXED)


---
<grid drag="100 18" drop="top" bg="linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%)" align="center" pad="10px">
## Ba Zhen Tang Composition
</grid>

<grid drag="48 70" drop="2 23" bg="#5CB85C" pad="20px" flow="col">

### Si Jun Zi Tang (Qi)
- Ren Shen (Chief)
- Bai Zhu (Chief)
- Fu Ling (Deputy)
- Gan Cao (Deputy)

</grid>

<grid drag="48 70" drop="-2 23" bg="#D9534F" pad="20px" flow="col">

### Si Wu Tang (Blood)
- Dang Gui (Chief)
- Shu Di Huang (Chief)
- Bai Shao (Assistant)
- Chuan Xiong (Envoy)

</grid>

<grid drag="100 8" drop="bottom" bg="#F0AD4E" align="center" pad="5px">
**= Ba Zhen Tang (Qi + Blood)**
</grid>

---


**Effect**: Visual formula breakdown with color-coded sections and styled title/footer bars

**Key Changes:**
- Title bar with gradient background (18% height)
- Content boxes start at 23% from top
- Footer bar at bottom (8% height)
- Adjusted positioning for better fit

---

### Rotating Emphasis


---
<grid drag="40 40" drop="center" bg="#E74C3C" rotate="45" pad="30px" align="center">

## CAUTION

Contraindicated in
**Yin Deficiency Heat**

</grid>

---


**Effect**: Diamond-shaped warning box (rotated 45°)

---

## 4. CUSTOM CSS STYLING {#custom-css}

### Inline Style Block


---
<style>
.tcm-herb {
    background: linear-gradient(135deg, #2d5016 0%, #4a7c2c 100%);
    border-radius: 15px;
    padding: 20px;
    color: white;
    box-shadow: 0 4px 6px rgba(0,0,0,0.3);
}

.tcm-formula {
    background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);
    border-radius: 15px;
    padding: 20px;
    color: white;
    box-shadow: 0 4px 6px rgba(0,0,0,0.3);
}

.tcm-point {
    background: linear-gradient(135deg, #7f1d1d 0%, #dc2626 100%);
    border-radius: 15px;
    padding: 20px;
    color: white;
    box-shadow: 0 4px 6px rgba(0,0,0,0.3);
}

.highlight-box {
    border: 3px solid #fbbf24;
    background: rgba(251, 191, 36, 0.1);
    padding: 15px;
    border-radius: 10px;
}

.pulse-animation {
    animation: pulse 2s infinite;
}

@keyframes pulse {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.5; }
}
</style>

## Styled Content

<div class="tcm-herb">
🌿 This is an herb section with gradient background
</div>

<div class="tcm-formula">
💊 This is a formula section with blue gradient
</div>

<div class="tcm-point">
📍 This is a point section with red gradient
</div>

---


---

### External CSS File

**In frontmatter:**
```yaml
---
theme: black
css: [css/tcm-styles.css, css/animations.css]
---


**Create file: `css/tcm-styles.css`**
```css
/* TCM Category Colors */
.herb-category {
    background: #2d5016;
    color: #fff;
}

.formula-category {
    background: #1e3a8a;
    color: #fff;
}

.point-category {
    background: #7f1d1d;
    color: #fff;
}

/* Property Tables */
.property-table {
    border-collapse: collapse;
    width: 100%;
}

.property-table th {
    background: #374151;
    color: white;
    padding: 10px;
}

.property-table td {
    padding: 8px;
    border-bottom: 1px solid #4b5563;
}

/* Warning Boxes */
.warning-box {
    background: #7f1d1d;
    border-left: 5px solid #dc2626;
    padding: 15px;
    margin: 10px 0;
}

/* Clinical Pearl */
.clinical-pearl {
    background: #065f46;
    border-left: 5px solid #10b981;
    padding: 15px;
    margin: 10px 0;
    font-style: italic;
}


**Usage in slides:**

---
<div class="herb-category">
# Herbs that Stop Bleeding
</div>

<div class="clinical-pearl">
💡 Always differentiate between cold and heat patterns before selecting hemostatic herbs
</div>

<div class="warning-box">
⚠️ Contraindicated in yin deficiency with heat
</div>

---


---

### Animated Highlights


---
<style>
.glow {
    animation: glow 1.5s ease-in-out infinite alternate;
}

@keyframes glow {
    from { text-shadow: 0 0 5px #fff, 0 0 10px #fff, 0 0 15px #e60073; }
    to { text-shadow: 0 0 10px #fff, 0 0 20px #ff4da6, 0 0 30px #ff4da6; }
}

.slide-in {
    animation: slideIn 1s ease-out;
}

@keyframes slideIn {
    from { transform: translateX(-100%); opacity: 0; }
    to { transform: translateX(0); opacity: 1; }
}
</style>

<h2 class="glow">Most Important Point: ST-36</h2>

<div class="slide-in">
This content slides in from the left
</div>

---


---

## 5. BACKGROUND EFFECTS {#backgrounds}

### Image Backgrounds


---
<!-- slide bg="[[herb_field.jpg]]" -->

# 🌿 Herbs that Stop Bleeding

## Traditional Wisdom Meets Modern Practice

---


---

### Gradient Backgrounds


---
<!-- slide bg="linear-gradient(135deg, #667eea 0%, #764ba2 100%)" -->

# Pattern Differentiation

---


---

### Color Backgrounds with Opacity


---
<!-- slide bg="#2d5016" -->

# Herb Category Overview

---

<!-- slide bg="rgba(45, 80, 22, 0.8)" -->

# Semi-transparent background

---


---

### Video Background


---
<!-- slide bg="[[acupuncture_demo.mp4]]" -->

# Needling Techniques

---


---

## 6. COMPLETE EXAMPLE SLIDES {#complete-examples}

### Example 1: Animated Herb Introduction


---
theme: black
transition: slide
---

<style>
.herb-title {
    background: linear-gradient(135deg, #2d5016 0%, #4a7c2c 100%);
    padding: 30px;
    border-radius: 20px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.5);
}

.property-box {
    background: rgba(255,255,255,0.1);
    border: 2px solid #4a7c2c;
    border-radius: 10px;
    padding: 15px;
    margin: 10px 0;
}
</style>

---
<!-- .slide: data-auto-animate -->

<div class="herb-title">
# 🌿 Ai Ye
</div>

---
<!-- .slide: data-auto-animate -->

<div class="herb-title">
# 🌿 Ai Ye
## 艾叶
### *Artemisia argyi Folium*
</div>

---

## Quick Properties

<grid drag="48 70" drop="left" class="property-box">

### TCM Properties
- **Taste**: Bitter, Acrid <!-- element class="fragment" -->
- **Temperature**: Warm <!-- element class="fragment" -->
- **Channels**: Sp, Liv, Kid <!-- element class="fragment" -->
- **Dosage**: 3-9g <!-- element class="fragment" -->

</grid>

<grid drag="48 70" drop="right" class="property-box">

### Primary Functions
1. Warms Womb <!-- element class="fragment" data-fragment-index="1" -->
2. Stops bleeding <!-- element class="fragment" data-fragment-index="2" -->
3. Disperses cold <!-- element class="fragment" data-fragment-index="3" -->
4. Alleviates pain <!-- element class="fragment" data-fragment-index="4" -->

</grid>

---

<grid drag="100 100" drop="center" bg="rgba(127, 29, 29, 0.9)" pad="40px" align="center">

## ⚠️ CAUTION

### Contraindicated in:
- Yin deficiency with heat <!-- element class="fragment highlight-red" -->
- Blood heat patterns <!-- element class="fragment highlight-red" -->
- Dry blood conditions <!-- element class="fragment highlight-red" -->

### Toxicity Warning
Overdosage (20-30g) may cause serious side effects

</grid>

---


---

### Example 2: Formula Comparison with Grids


---
theme: sky
---

<style>
.formula-card {
    border-radius: 15px;
    padding: 20px;
    box-shadow: 0 5px 15px rgba(0,0,0,0.3);
    height: 100%;
}

.qi-tonic { background: linear-gradient(135deg, #10b981 0%, #059669 100%); }
.blood-tonic { background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%); }
.qi-blood-tonic { background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%); }
</style>

---

## Formula Progression: Building Tonification

<grid drag="30 70" drop="5 20" class="formula-card qi-tonic" flow="col">

### Si Jun Zi Tang
**Four Gentlemen**

**Tonifies**: Qi only

**Herbs**: 4
- Ren Shen
- Bai Zhu
- Fu Ling
- Gan Cao

</grid>

<grid drag="30 70" drop="35 20" class="formula-card blood-tonic" flow="col">

### Si Wu Tang
**Four Substances**

**Tonifies**: Blood only

**Herbs**: 4
- Dang Gui
- Shu Di Huang
- Bai Shao
- Chuan Xiong

</grid>

<grid drag="30 70" drop="-5 20" class="formula-card qi-blood-tonic" flow="col">

### Ba Zhen Tang
**Eight Treasures**

**Tonifies**: Qi + Blood

**Herbs**: 8
Si Jun Zi Tang
+
Si Wu Tang

</grid>

---

<grid drag="100 100" drop="center" bg="rgba(0,0,0,0.8)" pad="50px" align="center" animate="fadeIn">

## 💡 Clinical Pearl

> "When a patient is completely depleted from illness, surgery, or chronic stress, think Ba Zhen Tang. Results typically seen within 2-4 weeks."

### Key Exam Point
**Si Jun Zi Tang + Si Wu Tang = Ba Zhen Tang**

</grid>

---


---

### Example 3: Point Location with Interactive Elements


---
theme: blood
---

<style>
.point-header {
    background: linear-gradient(135deg, #7f1d1d 0%, #dc2626 100%);
    padding: 20px;
    border-radius: 15px;
    text-align: center;
}

.annotation-box {
    background: rgba(255,255,255,0.95);
    color: #1f2937;
    border-radius: 10px;
    padding: 15px;
    box-shadow: 0 5px 15px rgba(0,0,0,0.4);
}
</style>

---

<div class="point-header">
# 📍 ST-36 · ZÚSĀNLǏ
## 足三里 · *Leg Three Miles*
</div>

---

<grid drag="55 100" drop="left">
![[ST-36_diagram.jpg]]
</grid>

<grid drag="40 25" drop="-3 10" class="annotation-box" frag="1">

### 📍 Location
3 cun below ST-35
1 finger lateral to tibia

</grid>

<grid drag="40 25" drop="-3 40" class="annotation-box" frag="2">

### ⚡ Functions
- Tonifies qi & blood
- Harmonizes Stomach
- Fortifies Spleen

</grid>

<grid drag="40 25" drop="-3 70" class="annotation-box" frag="3">

### 🔧 Needling
**Method**: Perpendicular
**Depth**: 1-1.5 cun

</grid>

---

## Clinical Indications

<grid drag="100 80" drop="center" flow="row" align="stretch">

<div class="annotation-box">

### Digestive
- Epigastric pain <!-- element class="fragment" -->
- Nausea/vomiting <!-- element class="fragment" -->
- Diarrhea <!-- element class="fragment" -->
- Poor appetite <!-- element class="fragment" -->

</div>

<div class="annotation-box">

### Constitutional
- Fatigue <!-- element class="fragment" -->
- Weakness <!-- element class="fragment" -->
- Deficiency <!-- element class="fragment" -->
- Low immunity <!-- element class="fragment" -->

</div>

<div class="annotation-box">

### Mental-Emotional
- Anxiety <!-- element class="fragment" -->
- Depression <!-- element class="fragment" -->
- Mania <!-- element class="fragment" -->
- Palpitations <!-- element class="fragment" -->

</div>

</grid>

---

<grid drag="100 100" drop="center" bg="#7f1d1d" pad="50px" align="center" rotate="0">

<h1 style="font-size: 3em; text-shadow: 0 0 20px rgba(255,255,255,0.5);">
"All diseases can be treated"
</h1>

<p style="font-size: 1.5em; margin-top: 30px;">
— Qin Cheng-zu (Song Dynasty)
</p>

<p style="margin-top: 50px; font-size: 1.2em; opacity: 0.8;">
The most important point in the body
</p>

</grid>

---


---

### Example 4: Pattern Differentiation with Filters


---
theme: moon
---

<style>
.pattern-box {
    border-radius: 15px;
    padding: 25px;
    margin: 10px;
    box-shadow: 0 5px 20px rgba(0,0,0,0.3);
}
</style>

---

## Pattern Differentiation: Bleeding Disorders

---

<grid drag="48 80" drop="left" bg="#3b82f6" class="pattern-box" filter="brightness(0.9)">

### ❄️ Cold Pattern

**Characteristics:**
- Pale blood <!-- element class="fragment" -->
- Cold abdomen <!-- element class="fragment" -->
- Prefers warmth <!-- element class="fragment" -->

**Tongue:** Pale, wet <!-- element class="fragment" -->
**Pulse:** Slow, deep <!-- element class="fragment" -->

**Treatment:** Warm and stop bleeding <!-- element class="fragment" -->

**Key Herb:** Ai Ye (Mugwort) <!-- element class="fragment highlight-blue" -->

</grid>

<grid drag="48 80" drop="right" bg="#ef4444" class="pattern-box" filter="brightness(1.1)">

### 🔥 Heat Pattern

**Characteristics:**
- Bright red blood <!-- element class="fragment" -->
- Thirst <!-- element class="fragment" -->
- Restlessness <!-- element class="fragment" -->

**Tongue:** Red, dry <!-- element class="fragment" -->
**Pulse:** Rapid, full <!-- element class="fragment" -->

**Treatment:** Cool blood, stop bleeding <!-- element class="fragment" -->

**Key Herb:** Sheng Di Huang (Rehmannia) <!-- element class="fragment highlight-red" -->

</grid>

---

<grid drag="100 100" drop="center" bg="rgba(0,0,0,0.9)" pad="60px" align="center" animate="fadeIn slower">

## 🎯 Clinical Decision Point

<div style="font-size: 1.5em; margin: 40px 0;">

**ALWAYS differentiate pattern before treatment**

</div>

<grid drag="80 30" drop="center" bg="rgba(239, 68, 68, 0.3)" border="3px solid #ef4444" pad="20px" frag="1">

❌ **Wrong herb for pattern = Treatment failure**

</grid>

<grid drag="80 30" drop="center" bg="rgba(16, 185, 129, 0.3)" border="3px solid #10b981" pad="20px" frag="2">

✅ **Correct pattern identification = Treatment success**

</grid>

</grid>

---


---

## Summary of Advanced Features

### Fragments
- Progressive reveal of content
- Multiple animation types
- Controlled ordering
- Auto-numbered lists

### Auto-Animations
- Smooth morphing between slides
- Element position transitions
- Size and scale changes
- Perfect for showing progression

### Grid Layouts
- Precise positioning
- Side-by-side comparisons
- Overlapping elements
- Responsive design

### Custom CSS
- Inline styles
- External stylesheets
- Custom animations
- Brand consistency

### Visual Effects
- Backgrounds (image, video, gradient)
- Filters (blur, brightness, etc.)
- Rotation and transforms
- Opacity and transparency
- Borders and shadows

---

## Best Practices for TCM Slides

1. **Use fragments** for complex concepts that need step-by-step explanation
2. **Use grids** for comparing patterns, formulas, or properties
3. **Use auto-animate** for showing formula building or pattern progression
4. **Use custom CSS** to maintain consistent branding across all decks
5. **Use backgrounds** sparingly - don't distract from content
6. **Use colors** to reinforce categories (green=herbs, blue=formulas, red=points)
7. **Use animations** purposefully - not just for decoration

---

## Performance Tips

- Keep animations smooth by limiting simultaneous effects
- Optimize images before including (compress large diagrams)
- Use external CSS for reusable styles
- Test slides in presentation mode before teaching
- Consider audience - too many animations can be distracting

---

*These advanced features transform simple markdown into engaging, professional presentations perfect for TCM education.*
