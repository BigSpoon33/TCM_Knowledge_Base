# Advanced Slides Plugin - OCDS Integration Guide

**Complete guide to using Advanced Slides for OCDS presentations**

---

## 📚 Overview

Advanced Slides transforms markdown files into professional presentations using reveal.js. OCDS uses it for:
- Lecture slide decks
- Study presentations
- Visual learning materials
- Teaching resources
- Review sessions

**Plugin:** https://github.com/MSzturc/obsidian-advanced-slides  
**Docs:** https://mszturc.github.io/obsidian-advanced-slides/

---

## 🎯 Why Advanced Slides for OCDS?

### Key Features
- **Markdown-based** - Easy to create and edit
- **Reveal.js powered** - Professional presentations
- **Fragments** - Progressive reveal
- **Grid layouts** - Precise positioning
- **Themes** - Customizable appearance
- **Export** - PDF, HTML
- **Presenter mode** - Speaker notes

### OCDS Use Cases
- **Lecture materials** - Weekly topic presentations
- **Study aids** - Visual review materials
- **Teaching tools** - Instructor presentations
- **Student resources** - Self-study slide decks

---

## 📝 Basic Syntax

### Slide Separators

```markdown
---
# Horizontal slide (new topic)

----
# Vertical slide (sub-topic, accessed with down arrow)
```

### Frontmatter Configuration

```yaml
---
theme: black
transition: slide
slideNumber: true
progress: true
controls: true
---
```

---

## 🎨 OCDS Slide Template

### Complete Template

```markdown
---
theme: black
transition: slide
slideNumber: true
progress: true
controls: true
css: [css/tcm-styles.css]
tags:
  - slides
  - {{CLASS_ID}}
  - {{TOPIC}}
---

<style>
/* OCDS Custom Styles */
.tcm-title {
    background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);
    padding: 40px;
    border-radius: 15px;
    color: white;
}

.tcm-content {
    background: rgba(255,255,255,0.1);
    padding: 20px;
    border-radius: 10px;
    border: 2px solid rgba(255,255,255,0.3);
}

.tcm-highlight {
    background: rgba(255, 255, 0, 0.3);
    padding: 5px 10px;
    border-radius: 5px;
}
</style>

---

# 🎓 {{TOPIC_NAME}}

**{{CLASS_NAME}}**  
Week {{WEEK_NUMBER}}

---

## 📋 Learning Objectives

By the end of this presentation, you will:

- Objective 1 <!-- element class="fragment" -->
- Objective 2 <!-- element class="fragment" -->
- Objective 3 <!-- element class="fragment" -->

---

## 📖 Overview

Brief introduction to the topic

---

# Main Content Sections

---

## Section 1: {{SECTION_TITLE}}

Content here

----

### Subsection 1.1

Detailed content (vertical slide)

----

### Subsection 1.2

More details (vertical slide)

---

## Section 2: {{SECTION_TITLE}}

Content here

---

## 💡 Key Takeaways

- Key point 1 <!-- element class="fragment" -->
- Key point 2 <!-- element class="fragment" -->
- Key point 3 <!-- element class="fragment" -->

---

## 📚 Next Steps

- Review flashcards: [[Flashcards_{{TOPIC}}]]
- Complete quiz: [[Quiz_{{TOPIC}}]]
- Read material: [[Study_{{TOPIC}}]]

---

# Questions?

**Thank you!**
```

---

## 🎭 Fragments (Progressive Reveal)

### Basic Fragment

```markdown
- Item 1 <!-- element class="fragment" -->
- Item 2 <!-- element class="fragment" -->
- Item 3 <!-- element class="fragment" -->
```

### Fragment Types

```markdown
<!-- element class="fragment fade-in" -->
<!-- element class="fragment fade-out" -->
<!-- element class="fragment fade-up" -->
<!-- element class="fragment fade-down" -->
<!-- element class="fragment fade-left" -->
<!-- element class="fragment fade-right" -->
<!-- element class="fragment grow" -->
<!-- element class="fragment shrink" -->
<!-- element class="fragment highlight-red" -->
<!-- element class="fragment highlight-green" -->
<!-- element class="fragment highlight-blue" -->
```

### Fragment Index (Control Order)

```markdown
- Item 3 <!-- element class="fragment" data-fragment-index="3" -->
- Item 1 <!-- element class="fragment" data-fragment-index="1" -->
- Item 2 <!-- element class="fragment" data-fragment-index="2" -->
```

---

## 📐 Grid Layouts

### Basic Grid

```markdown
<grid drag="50 80" drop="left" bg="#4A90E2" pad="20px">
Left content
</grid>

<grid drag="50 80" drop="right" bg="#E24A4A" pad="20px">
Right content
</grid>
```

### Grid Parameters

- `drag="width height"` - Size (percentage)
- `drop="position"` - Location
- `bg="color"` - Background color
- `pad="padding"` - Internal padding
- `flow="col"` - Column layout

### Common Positions

```
topleft    top    topright
left      center     right
bottomleft bottom bottomright
```

### OCDS Pattern Comparison

```markdown
<grid drag="45 70" drop="left" class="tcm-content">

### Pattern A
- Symptom 1
- Symptom 2
- Symptom 3

</grid>

<grid drag="45 70" drop="right" class="tcm-content">

### Pattern B
- Symptom 1
- Symptom 2
- Symptom 3

</grid>
```

---

## 🎨 Styling

### Inline Styles

```markdown
<div style="background: #1e3a8a; padding: 20px; border-radius: 10px;">
Styled content
</div>
```

### CSS Classes

```markdown
<div class="tcm-title">
Title content
</div>
```

### Custom CSS in Frontmatter

```markdown
---
theme: black
---

<style>
.custom-class {
    /* Your styles */
}
</style>
```

---

## 🖼️ Images

### Basic Image

```markdown
![[image.png]]
```

### Sized Image

```markdown
![[image.png|400]]
```

### Background Image

```markdown
<!-- slide bg="[[image.jpg]]" -->
```

### Grid with Image

```markdown
<grid drag="50 80" drop="left">
![[diagram.png]]
</grid>

<grid drag="50 80" drop="right">
Explanation text
</grid>
```

---

## 🎬 Animations

### Auto-Animate

```markdown
<!-- .slide: data-auto-animate -->
# Title

---

<!-- .slide: data-auto-animate -->
# Title
## Subtitle appears smoothly
```

### Auto-Animate Example

```markdown
<!-- .slide: data-auto-animate -->
## Formula Components

---

<!-- .slide: data-auto-animate -->
## Formula Components

**Chief Herbs:**
- Ren Shen

---

<!-- .slide: data-auto-animate -->
## Formula Components

**Chief Herbs:**
- Ren Shen

**Deputy Herbs:**
- Bai Zhu
```

---

## 📊 OCDS Slide Deck Examples

### 1. Pattern Presentation

```markdown
---
theme: black
transition: slide
slideNumber: true
tags: [slides, tcm_101, patterns]
---

<style>
.pattern-title {
    background: linear-gradient(135deg, #581c87 0%, #9333ea 100%);
    padding: 30px;
    border-radius: 15px;
    color: white;
}
</style>

---

# 🔍 Qi Deficiency Pattern

**TCM 101 - Week 1**

---

## 📋 Learning Objectives

- Identify cardinal symptoms <!-- element class="fragment" -->
- Understand etiology <!-- element class="fragment" -->
- Recognize tongue/pulse <!-- element class="fragment" -->
- Select treatment principles <!-- element class="fragment" -->

---

## 📖 Definition

<div class="pattern-title">
Qi Deficiency is a pattern characterized by insufficient Qi to perform normal physiological functions
</div>

---

## 🎯 Cardinal Symptoms

<grid drag="100 70" drop="center" class="tcm-content">

- Fatigue and weakness <!-- element class="fragment" -->
- Shortness of breath <!-- element class="fragment" -->
- Spontaneous sweating <!-- element class="fragment" -->
- Pale complexion <!-- element class="fragment" -->
- Weak voice <!-- element class="fragment" -->

</grid>

---

## 👅 Tongue & Pulse

<grid drag="45 70" drop="left">

### Tongue
- Pale body
- Swollen
- Tooth marks
- Thin white coating

</grid>

<grid drag="45 70" drop="right">

### Pulse
- Weak
- Empty
- Especially in Guan

</grid>

---

## 🌱 Etiology

1. Constitutional weakness <!-- element class="fragment" -->
2. Chronic illness <!-- element class="fragment" -->
3. Dietary irregularities <!-- element class="fragment" -->
4. Overwork and stress <!-- element class="fragment" -->

---

## 🏥 Treatment Principle

<div class="tcm-highlight">
Tonify Qi and Strengthen the Spleen
</div>

---

## 💊 Primary Formula

**Si Jun Zi Tang**  
(Four Gentlemen Decoction)

- Ren Shen (Chief)
- Bai Zhu (Deputy)
- Fu Ling (Assistant)
- Zhi Gan Cao (Envoy)

---

## 💡 Key Takeaways

- Qi Deficiency = Insufficient Qi <!-- element class="fragment" -->
- Fatigue is cardinal symptom <!-- element class="fragment" -->
- Pale, swollen tongue <!-- element class="fragment" -->
- Si Jun Zi Tang is foundation <!-- element class="fragment" -->

---

## 📚 Next Steps

- Review: [[Flashcards_Qi_Deficiency]]
- Quiz: [[Quiz_Qi_Deficiency]]
- Study: [[Qi_Deficiency_Pattern]]

---

# Questions?
```

>oh man this is actually a great side example. there are a few things I thought about when going through it. speaker notes. basically every fragment should have a bit to talk about it like how it shows qi deficiency key symptoms. each symptom should have common pattern or simple explaination as a speaker note. that way the fragment element gets utilized for dramatic effect and to keep it speaking and conversational without just reading the slides
---

### 2. Formula Presentation

```markdown
---
theme: black
transition: slide
tags: [slides, tcm_101, formulas]
---

<style>
.formula-box {
    background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);
    padding: 25px;
    border-radius: 12px;
    color: white;
}
</style>

---

# 💊 Si Jun Zi Tang

**Four Gentlemen Decoction**

---

## 📋 Formula Overview

<div class="formula-box">
Foundation formula for Spleen Qi Deficiency
</div>

---

## 🌿 Composition

<!-- .slide: data-auto-animate -->

---

## 🌿 Composition

<!-- .slide: data-auto-animate -->

**Chief (君):**
- Ren Shen 9g - Tonify Qi

---

## 🌿 Composition

<!-- .slide: data-auto-animate -->

**Chief (君):**
- Ren Shen 9g - Tonify Qi

**Deputy (臣):**
- Bai Zhu 9g - Strengthen Spleen

---

## 🌿 Composition

<!-- .slide: data-auto-animate -->

**Chief (君):**
- Ren Shen 9g - Tonify Qi

**Deputy (臣):**
- Bai Zhu 9g - Strengthen Spleen

**Assistant (佐):**
- Fu Ling 9g - Drain Dampness

---

## 🌿 Composition

<!-- .slide: data-auto-animate -->

**Chief (君):**
- Ren Shen 9g - Tonify Qi

**Deputy (臣):**
- Bai Zhu 9g - Strengthen Spleen

**Assistant (佐):**
- Fu Ling 9g - Drain Dampness

**Envoy (使):**
- Zhi Gan Cao 6g - Harmonize

---

## 🎯 Actions

<grid drag="100 70" drop="center">

1. Tonify Qi <!-- element class="fragment" -->
2. Strengthen Spleen <!-- element class="fragment" -->
3. Harmonize Middle Jiao <!-- element class="fragment" -->

</grid>

---

## 🏥 Indications

- Spleen Qi Deficiency <!-- element class="fragment" -->
- Poor appetite <!-- element class="fragment" -->
- Loose stools <!-- element class="fragment" -->
- Fatigue <!-- element class="fragment" -->
- Pale tongue <!-- element class="fragment" -->

---

## 🔄 Modifications

<grid drag="45 70" drop="left">

### + Chen Pi + Ban Xia
= Liu Jun Zi Tang
(For phlegm)

</grid>

<grid drag="45 70" drop="right">

### + Huang Qi
= Bu Zhong Yi Qi Tang
(For sinking Qi)

</grid>

---

## 💡 Clinical Pearls

> "The foundation of all Qi-tonifying formulas"

---

# Questions?
```

---

## 🎓 OCDS Slide Deck Structure

### Standard Structure

```
1. Title Slide (class, week, topic)
2. Learning Objectives
3. Overview/Definition
4. Main Content (3-5 sections)
   - Each section can have vertical sub-slides
5. Key Takeaways
6. Next Steps (links to materials)
7. Questions
```

### Recommended Slide Counts

- **Short deck (15-20 min):** 10-15 slides
- **Medium deck (30-40 min):** 20-30 slides
- **Long deck (60 min):** 40-50 slides
> I like how short these are. It makes review a little easier but also allows to combine multiple slides for a class presentation kind of like a single herb vs a category with all the single herb slides vs a formula that adds the slides for each single herb. How can these types of slides be autogenerated from a more comprehensive note? like basically yeah this would be doable based on the headings or the syntax. you could specify the headings to pull and how to format the note body from the heading. 
---

## ⌨️ Keyboard Shortcuts

### Navigation
- `→` or `Space` - Next slide
- `←` - Previous slide
- `↓` - Down (vertical slides)
- `↑` - Up (vertical slides)
- `Home` - First slide
- `End` - Last slide

### Presentation
- `F` - Fullscreen
- `S` - Speaker notes
- `O` - Overview mode
- `B` or `.` - Pause (black screen)
- `Esc` - Exit presentation

---

## 🔧 Plugin Configuration

### Recommended Settings

```
Settings → Advanced Slides
├── Theme: black (or your preference)
├── Slide number: ON
├── Progress bar: ON
├── Controls: ON
├── Transition: slide
├── Transition speed: default
└── Export directory: Exports/Slides
```

---

## 📤 Exporting

### Export to PDF

1. Open presentation
2. Press `E` key
3. Select "Export to PDF"
4. Choose location
5. Save

### Export to HTML

1. Open presentation
2. Press `E` key
3. Select "Export to HTML"
4. Standalone HTML file created

---

## 💡 Best Practices

### Content
- **One concept per slide** - Don't overcrowd
- **Visual hierarchy** - Use headings effectively
- **Bullet points** - Keep concise
- **Images** - Use liberally
- **Fragments** - Reveal progressively

### Design
- **Consistent theme** - Use same theme throughout
- **Color coding** - Patterns=purple, Formulas=blue, etc.
- **White space** - Don't fill every inch
- **Readable fonts** - Large enough to see
- **High contrast** - Text vs background

### Presentation
- **Practice** - Run through before teaching
- **Speaker notes** - Add reminders
- **Timing** - 1-2 minutes per slide
- **Interaction** - Pause for questions
- **Backup** - Export PDF as backup

---

## 🎨 OCDS Color Scheme

```css
/* Patterns */
.pattern-style {
    background: linear-gradient(135deg, #581c87 0%, #9333ea 100%);
}

/* Formulas */
.formula-style {
    background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);
}

/* Herbs */
.herb-style {
    background: linear-gradient(135deg, #2d5016 0%, #4a7c2c 100%);
}

/* Points */
.point-style {
    background: linear-gradient(135deg, #7f1d1d 0%, #dc2626 100%);
}

/* Concepts */
.concept-style {
    background: linear-gradient(135deg, #0f766e 0%, #14b8a6 100%);
}
```

---

## 🔗 Integration with OCDS

### Link from Timeline

```yaml
materials:
  - type: "slides"
    source: "Materials/Slides/Qi_Deficiency_Slides.md"
    title: "Qi Deficiency Presentation"
    estimated_minutes: 30
```

### Link from Study Material

```markdown
## Visual Learning

View the slide presentation: [[Qi_Deficiency_Slides]]
```

### Link from Task

```markdown
## Study Materials

1. Read: [[Qi_Deficiency_Pattern]]
2. View slides: [[Qi_Deficiency_Slides]]
3. Review flashcards: [[Flashcards_Qi]]
```

---

## 🐛 Troubleshooting

### Slides Not Rendering

**Problem:** Presentation mode doesn't work

**Solutions:**
1. Ensure Advanced Slides plugin is enabled
2. Check frontmatter syntax
3. Verify slide separators (`---`)
4. Restart Obsidian

### Images Not Showing

**Problem:** Images don't appear in presentation

**Solutions:**
1. Check image paths are correct
2. Use `[[image.png]]` format
3. Ensure images are in vault
4. Try absolute paths

### Fragments Not Working

**Problem:** Progressive reveal doesn't work

**Solutions:**
1. Check comment syntax exactly: `<!-- element class="fragment" -->`
2. Ensure no extra spaces
3. Test in presentation mode (not edit mode)

### CSS Not Applying

**Problem:** Custom styles don't show

**Solutions:**
1. Check `<style>` block in frontmatter area
2. Verify CSS syntax
3. Use browser inspector (F12) to debug
4. Try inline styles as test

---

## ✅ Quick Reference

### Slide Separators
```markdown
---  (horizontal)
---- (vertical)
```

### Fragments
```markdown
<!-- element class="fragment" -->
<!-- element class="fragment fade-up" -->
```
> what if you had a fade or slide that randomized for each character.
### Grid
```markdown
<grid drag="50 80" drop="left">
Content
</grid>
```

### Background
```markdown
<!-- slide bg="[[image.jpg]]" -->
<!-- slide bg="#1e3a8a" -->
```

### Auto-Animate
```markdown
<!-- .slide: data-auto-animate -->
```

---

## 📚 Related Documentation

- **Slide Template Structure:** `../Documents/SLIDE_TEMPLATE_STRUCTURE.md`
- **Advanced Slides Examples:** `../Documents/Advanced_Slides_Examples/`
- **Material Templates:** `../05_Material_Templates/Slide_Deck_Template.md`

---

**Create engaging presentations with Advanced Slides! 🎬**

---

*Last updated: 2025-11-05*  
*OCDS Version: 1.0.0*
