---
theme: black
transition: slide
slideNumber: true
progress: true
controls: true
css: [css/tcm-styles.css]
tags:
  - slides
  - tcm
  - template
---

<style>
/* TCM Category Colors */
.herb-style {
    background: linear-gradient(135deg, #2d5016 0%, #4a7c2c 100%);
    border-radius: 15px;
    padding: 20px;
    color: white;
    box-shadow: 0 4px 6px rgba(0,0,0,0.3);
}

.formula-style {
    background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);
    border-radius: 15px;
    padding: 20px;
    color: white;
    box-shadow: 0 4px 6px rgba(0,0,0,0.3);
}

.point-style {
    background: linear-gradient(135deg, #7f1d1d 0%, #dc2626 100%);
    border-radius: 15px;
    padding: 20px;
    color: white;
    box-shadow: 0 4px 6px rgba(0,0,0,0.3);
}

.warning-box {
    background: rgba(127, 29, 29, 0.9);
    border-left: 5px solid #dc2626;
    padding: 20px;
    border-radius: 10px;
}

.pearl-box {
    background: rgba(16, 185, 129, 0.2);
    border-left: 5px solid #10b981;
    padding: 20px;
    border-radius: 10px;
    font-style: italic;
}

.property-grid {
    background: rgba(255,255,255,0.1);
    border: 2px solid rgba(255,255,255,0.3);
    border-radius: 10px;
    padding: 15px;
}
</style>

---

# 🌿 [Category Name]

## [Subcategory or Topic]

**Presentation by**: [Your Name]
**Date**: [Date]

---

# 🌿 [Item Name]

**[Hanzi]** · *[English Translation]*

**Category**: [Category Name]

<!-- slide bg="[[optional_image.jpg]]" -->

---

## Quick Reference

<grid drag="100 80" drop="center" class="property-grid">

| Property | Value |
|----------|-------|
| **[Property 1]** | [Value] |
| **[Property 2]** | [Value] |
| **[Property 3]** | [Value] |
| **[Property 4]** | [Value] |

</grid>

---

## ⚡ Primary Functions

1. **[Function 1]** <!-- element class="fragment" -->
2. **[Function 2]** <!-- element class="fragment" -->
3. **[Function 3]** <!-- element class="fragment" -->

> *Key Clinical Use*: [One-sentence summary] <!-- element class="fragment fade-in" -->

---

----

### Function 1: [Name]

**Clinical Application**:
- [Specific pattern/condition]
- [Key symptoms]

**Important Combinations**:
- With **[Item]** → for [condition]
- With **[Item]** → for [condition]

**Example Formula/Protocol**: [[Reference]]

----

### Function 2: [Name]

**Clinical Application**:
- [Specific pattern/condition]
- [Key symptoms]

**Important Combinations**:
- With **[Item]** → for [condition]
- With **[Item]** → for [condition]

**Example Formula/Protocol**: [[Reference]]

----

---

## 🎯 Clinical Indications

<grid drag="48 70" drop="left" class="property-grid">

### Traditional Symptoms
- [Symptom 1] <!-- element class="fragment" -->
- [Symptom 2] <!-- element class="fragment" -->
- [Symptom 3] <!-- element class="fragment" -->
- [Symptom 4] <!-- element class="fragment" -->

</grid>

<grid drag="48 70" drop="right" class="property-grid">

### Modern Applications
- [Western condition 1] <!-- element class="fragment" -->
- [Western condition 2] <!-- element class="fragment" -->
- [Western condition 3] <!-- element class="fragment" -->

</grid>

---

## ⚠️ Cautions & Contraindications

<grid drag="100 80" drop="center" class="warning-box">

### Contraindications
- [Contraindication 1] <!-- element class="fragment highlight-red" -->
- [Contraindication 2] <!-- element class="fragment highlight-red" -->
- [Contraindication 3] <!-- element class="fragment highlight-red" -->

### Special Populations
- **Pregnancy**: [Safe/Caution/Contraindicated]
- **Elderly**: [Considerations]
- **Children**: [Considerations]

</grid>

---

## 🔗 Related Items

<grid drag="100 70" drop="center" class="property-grid" flow="col">

### Primary Relationships
- **[[Item 1]]** - [Relationship/Use]
- **[[Item 2]]** - [Relationship/Use]
- **[[Item 3]]** - [Relationship/Use]

### Secondary Relationships
- **[[Item 4]]** - [Relationship/Use]
- **[[Item 5]]** - [Relationship/Use]

</grid>

---

## 💡 Study Notes

<grid drag="100 80" drop="center" class="pearl-box">

### Mnemonic
[Memory device for key information]

### Key Exam Points
1. [Point 1] <!-- element class="fragment" -->
2. [Point 2] <!-- element class="fragment" -->
3. [Point 3] <!-- element class="fragment" -->

### Clinical Pearl
> [Practical clinical insight or wisdom]

</grid>

---

# [Next Item in Category]

**Continue to next item** →

---

# 📚 Category Summary

## Key Takeaways

1. [Takeaway 1] <!-- element class="fragment" -->
2. [Takeaway 2] <!-- element class="fragment" -->
3. [Takeaway 3] <!-- element class="fragment" -->

## Study Recommendations
- [Recommendation 1]
- [Recommendation 2]
- [Recommendation 3]

## Next Steps
Continue to: [[Next Category Deck]]

---

# Questions?

**Thank you for your attention**

---

<!-- 
QUICK REFERENCE GUIDE

SLIDE SEPARATORS:
--- = New horizontal slide (new topic)
---- = New vertical slide (sub-topic, accessed with down arrow)

FRAGMENTS (Progressive reveal):
<!-- element class="fragment" -->
<!-- element class="fragment fade-up" -->
<!-- element class="fragment highlight-red" -->
<!-- element class="fragment" data-fragment-index="1" -->

AUTO-ANIMATE (Smooth transitions):
<!-- .slide: data-auto-animate -->

GRIDS (Positioning):
<grid drag="width height" drop="x y" bg="color" pad="padding">
Content
</grid>

Common positions: topleft, top, topright, left, center, right, bottomleft, bottom, bottomright

BACKGROUNDS:
<!-- slide bg="[[image.jpg]]" -->
<!-- slide bg="#hexcolor" -->
<!-- slide bg="linear-gradient(135deg, #color1 0%, #color2 100%)" -->

STYLING:
Use the <style> block at the top or reference external CSS files

SPEAKER NOTES:
note: These notes appear in presenter mode only

CALLOUTS:
> [!warning] Title
> Content

> [!tip] Title
> Content

-->
