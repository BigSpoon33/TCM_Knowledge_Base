# Advanced Slides - Visual Syntax Cheat Sheet

Quick reference for creating TCM presentations with Advanced Slides.

---

## 🎬 SLIDE NAVIGATION

### Horizontal Slides (Main Topics)

---
# Slide 1

---
# Slide 2

---
# Slide 3

**Navigation**: Left/Right arrows
**Use for**: Different herbs, formulas, or points

---

### Vertical Slides (Sub-Topics)

---
# Main Topic

----
## Detail 1

----
## Detail 2

----
## Detail 3

---
# Next Main Topic

**Navigation**: Up/Down arrows
**Use for**: Details about current herb/formula/point

---

## ✨ FRAGMENTS (Progressive Reveal)

### Basic Fade In

- Item 1 <!-- element class="fragment" -->
- Item 2 <!-- element class="fragment" -->
- Item 3 <!-- element class="fragment" -->

**Effect**: Items appear one at a time

---

### Directional Animations

- Fade up <!-- element class="fragment fade-up" -->
- Fade down <!-- element class="fragment fade-down" -->
- Fade left <!-- element class="fragment fade-left" -->
- Fade right <!-- element class="fragment fade-right" -->


---

### Highlighting

- Red highlight <!-- element class="fragment highlight-red" -->
- Green highlight <!-- element class="fragment highlight-green" -->
- Blue highlight <!-- element class="fragment highlight-blue" -->


---

### Size Changes

- Grow <!-- element class="fragment grow" -->
- Shrink <!-- element class="fragment shrink" -->


---

### Controlled Order

- Fourth <!-- element class="fragment" data-fragment-index="4" -->
- Third <!-- element class="fragment" data-fragment-index="3" -->
- Second <!-- element class="fragment" data-fragment-index="2" -->
- First <!-- element class="fragment" data-fragment-index="1" -->

**Effect**: Appear in specified order (1, 2, 3, 4)

---

## 🎭 AUTO-ANIMATIONS

### Morphing Elements

---
<!-- .slide: data-auto-animate -->
# Title

---
<!-- .slide: data-auto-animate -->
# Title
## Subtitle
### Details

**Effect**: Smooth transition between slides

---

### Growing Tables

---
<!-- .slide: data-auto-animate -->
| Herb | Role |
|------|------|
| Ren Shen | Chief |

---
<!-- .slide: data-auto-animate -->
| Herb | Role |
|------|------|
| Ren Shen | Chief |
| Bai Zhu | Deputy |

**Effect**: New rows smoothly appear

---

## 📐 GRID LAYOUTS

### Basic Grid

<grid drag="width height" drop="x y">
Content
</grid>


**Sizes**: Percentages (50 80) or pixels (400px 600px)
**Positions**: Numbers or names

---

### Named Positions

<grid drag="40 30" drop="topleft">
Top Left
</grid>

<grid drag="40 30" drop="center">
Center
</grid>

<grid drag="40 30" drop="bottomright">
Bottom Right
</grid>


**Available**: topleft, top, topright, left, center, right, bottomleft, bottom, bottomright

---

### Side-by-Side Layout

<grid drag="48 80" drop="left" bg="#4A90E2">
Left content
</grid>

<grid drag="48 80" drop="right" bg="#E24A4A">
Right content
</grid>


---

### Overlapping Elements

<grid drag="60 60" drop="center">
![[image.jpg]]
</grid>

<grid drag="30 20" drop="-5 10" bg="white" pad="10px">
Annotation box
</grid>


---

## 🎨 STYLING

### Background Colors

<grid drag="50 50" drop="center" bg="#2d5016">
Green background
</grid>

<grid drag="50 50" drop="center" bg="rgb(45, 80, 22)">
RGB color
</grid>

<grid drag="50 50" drop="center" bg="rgba(45, 80, 22, 0.8)">
Semi-transparent
</grid>


---

### Borders

<grid drag="50 50" drop="center" border="2px solid white">
White border
</grid>

<grid drag="50 50" drop="center" border="thick dashed red">
Thick dashed red
</grid>


---

### Padding

<grid drag="50 50" drop="center" pad="20px">
Equal padding all sides
</grid>

<grid drag="50 50" drop="center" pad="10px 20px">
10px top/bottom, 20px left/right
</grid>

<grid drag="50 50" drop="center" pad="10px 15px 20px 25px">
Top, Right, Bottom, Left
</grid>


---

### Rotation

<grid drag="40 40" drop="center" rotate="45">
Rotated 45 degrees
</grid>

<grid drag="40 40" drop="center" rotate="-15">
Rotated -15 degrees
</grid>


---

### Opacity

<grid drag="50 50" drop="center" opacity="1.0">
Fully opaque
</grid>

<grid drag="50 50" drop="center" opacity="0.5">
50% transparent
</grid>

<grid drag="50 50" drop="center" opacity="0.1">
90% transparent
</grid>


---

### Filters

<grid drag="50 50" drop="center" filter="blur(5px)">
Blurred
</grid>

<grid drag="50 50" drop="center" filter="grayscale()">
Grayscale
</grid>

<grid drag="50 50" drop="center" filter="brightness(1.5)">
Brighter
</grid>


**Available**: blur, bright, contrast, grayscale, hue, invert, saturate, sepia

---

### Alignment

<grid drag="50 50" drop="center" align="left">
Left aligned
</grid>

<grid drag="50 50" drop="center" align="center">
Center aligned
</grid>

<grid drag="50 50" drop="center" align="right">
Right aligned
</grid>


**Available**: left, center, right, justify, top, bottom, topleft, topright, bottomleft, bottomright, stretch

---

### Flow Direction

<grid drag="50 80" drop="center" flow="col">
Item 1
Item 2
Item 3
</grid>

**col** = Vertical layout (default)


<grid drag="80 50" drop="center" flow="row">
Item 1
Item 2
Item 3
</grid>

**row** = Horizontal layout

---

## 🖼️ BACKGROUNDS

### Slide Backgrounds

<!-- slide bg="[[image.jpg]]" -->



<!-- slide bg="#2d5016" -->



<!-- slide bg="linear-gradient(135deg, #667eea 0%, #764ba2 100%)" -->



<!-- slide bg="[[video.mp4]]" -->


---

## 🎨 CUSTOM CSS

### Inline Styles

<style>
.custom-class {
    background: #2d5016;
    color: white;
    padding: 20px;
    border-radius: 10px;
}
</style>

<div class="custom-class">
Styled content
</div>


---

### External CSS
**In frontmatter:**
```yaml
---
css: [css/tcm-styles.css, css/animations.css]
---


---

### Inline Element Styling

<div style="background: red; padding: 20px;">
Direct inline styles
</div>


---

## 📝 FRONTMATTER OPTIONS

```yaml
---
theme: black
# Options: black, white, league, sky, beige, simple, serif, 
#          blood, night, moon, solarized

transition: slide
# Options: none, fade, slide, convex, concave, zoom

slideNumber: true
progress: true
controls: true
autoSlide: 0
loop: false

css: [css/custom.css]
---


---

## 💬 SPEAKER NOTES


---
## Slide Content

note: These are speaker notes that only appear in presenter mode.
Include teaching tips, reminders, or additional context here.

---


**Access**: Press 'S' during presentation

---

## 📋 CALLOUTS


> [!warning] Caution
> This herb is contraindicated in pregnancy

> [!tip] Clinical Pearl
> Best results when combined with dietary therapy

> [!info] Note
> Also known as Artemisia argyi

> [!success] Key Point
> Most important point on the channel


---

## 🎯 COMMON PATTERNS

### TCM Herb Slide

---
<style>
.herb-box {
    background: linear-gradient(135deg, #2d5016 0%, #4a7c2c 100%);
    border-radius: 15px;
    padding: 20px;
    color: white;
}
</style>

<div class="herb-box">
# 🌿 Ai Ye
## 艾叶 · *Mugwort*
</div>

---

## Properties

| Property | Value |
|----------|-------|
| Taste | Bitter, Acrid |
| Temp | Warm |
| Channels | Sp, Liv, Kid |

---

## Functions

1. Warms Womb <!-- element class="fragment" -->
2. Stops bleeding <!-- element class="fragment" -->
3. Disperses cold <!-- element class="fragment" -->

---


---

### Comparison Slide

---
## Cold vs Heat

<grid drag="45 70" drop="left" bg="#4A90E2" pad="20px">

### Cold
- Pale
- Slow pulse
- Cold limbs

</grid>

<grid drag="45 70" drop="right" bg="#E24A4A" pad="20px">

### Heat
- Red
- Rapid pulse
- Thirst

</grid>

---


---

### Point Location Slide

---
<grid drag="50 100" drop="left">
![[ST-36_diagram.jpg]]
</grid>

<grid drag="45 30" drop="-3 10" bg="white" border="2px solid red" pad="10px">

### Location
3 cun below ST-35

</grid>

<grid drag="45 30" drop="-3 -10" bg="white" border="2px solid blue" pad="10px">

### Functions
- Tonifies qi
- Harmonizes Stomach

</grid>

---


---

## ⌨️ KEYBOARD SHORTCUTS

| Key | Action |
|-----|--------|
| **→** | Next horizontal slide |
| **←** | Previous horizontal slide |
| **↓** | Next vertical slide |
| **↑** | Previous vertical slide |
| **Space** | Next slide (any direction) |
| **Esc** | Slide overview |
| **S** | Speaker notes |
| **F** | Fullscreen |
| **B** | Pause (black screen) |
| **?** | Help |

---

## 🎨 COLOR PALETTE SUGGESTIONS

### TCM Categories
```css
/* Herbs */
--herb-primary: #2d5016;
--herb-secondary: #4a7c2c;

/* Formulas */
--formula-primary: #1e3a8a;
--formula-secondary: #3b82f6;

/* Points */
--point-primary: #7f1d1d;
--point-secondary: #dc2626;

/* Patterns */
--pattern-primary: #581c87;
--pattern-secondary: #a855f7;


### Yin/Yang
```css
--yin-color: #3b82f6;  /* Blue */
--yang-color: #ef4444; /* Red */


### Five Elements
```css
--wood: #10b981;  /* Green */
--fire: #ef4444;  /* Red */
--earth: #f59e0b; /* Yellow/Orange */
--metal: #e5e7eb; /* White/Gray */
--water: #3b82f6; /* Blue */


---

## 📊 QUICK DECISION GUIDE

### When to use Fragments?
✅ Complex concepts needing step-by-step reveal
✅ Building up to a conclusion
✅ Comparing multiple items
❌ Simple lists that don't need emphasis

### When to use Auto-Animate?
✅ Showing progression or transformation
✅ Formula building
✅ Zooming into details
❌ Unrelated slides

### When to use Grids?
✅ Side-by-side comparisons
✅ Precise positioning needed
✅ Overlapping elements
❌ Simple single-column content

### When to use Custom CSS?
✅ Consistent branding across decks
✅ Special visual effects
✅ Reusable components
❌ One-off styling (use inline)

---

## 🚀 PERFORMANCE TIPS

1. **Optimize images** - Compress before adding
2. **Limit animations** - Don't overuse on single slide
3. **Test early** - View in presentation mode often
4. **Keep it simple** - Clarity over complexity
5. **Use fragments wisely** - Too many = distracting

---

## 📚 QUICK LINKS

- **Advanced Slides Docs**: https://mszturc.github.io/obsidian-advanced-slides/
- **Reveal.js Docs**: https://revealjs.com/
- **CSS Gradients**: https://cssgradient.io/
- **Color Picker**: https://htmlcolorcodes.com/

---

*Print this cheat sheet for quick reference while creating slides!*
