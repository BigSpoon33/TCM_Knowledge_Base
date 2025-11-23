# Epic 12 CSS Quick Start Guide

**Status:** Ready for Development  
**Last Updated:** 2025-11-22

---

## 🎯 Quick Links

- **Main Guide:** [CSS Theming Guide](guides/CSS_THEMING_GUIDE.md)
- **Research Report:** [Action Item #8 Report](sprint-artifacts/12-ACTION-8-CSS-THEMING-RESEARCH.md)
- **Epic 12 Planning:** [epics.md](epics.md#epic-12-dashboard-polish--interactivity-presentation-layer)

---

## 🚀 Getting Started (5 Minutes)

### 1. Create Your First CSS Snippet

```bash
# Navigate to snippets directory
cd .obsidian/snippets/

# Create a new snippet file
touch ocds-test.css
```

### 2. Add Basic Styling

```css
/* ocds-test.css */

/* Test card styling */
.markdown-preview-view h2 {
    color: var(--color-purple);
    padding-bottom: 0.5rem;
    border-bottom: 2px solid var(--color-purple);
}

/* Test table styling */
.dataview.table-view-table {
    border: 1px solid var(--background-modifier-border);
    border-radius: 8px;
    overflow: hidden;
}
```

### 3. Enable the Snippet

1. Open Obsidian Settings
2. Go to **Appearance** → **CSS snippets**
3. Click refresh icon (if needed)
4. Toggle on `ocds-test`
5. Changes apply immediately!

### 4. Test in a Dashboard

Create a test note with:

```markdown
## 📊 Test Dashboard

This heading should be purple with an underline.

```dataview
TABLE file.name as "Name"
FROM ""
LIMIT 5
```
```

---

## 📚 Essential CSS Variables

### Colors (Always Use These!)

```css
/* Backgrounds */
--background-primary          /* Main background */
--background-secondary        /* Sidebar background */
--background-modifier-border  /* Border color */
--background-modifier-hover   /* Hover state */

/* Text */
--text-normal                 /* Primary text */
--text-muted                  /* Secondary text */
--text-accent                 /* Links and highlights */

/* Extended Palette (Minimal Theme) */
--color-red                   /* #d04255 */
--color-orange               /* #d5763f */
--color-yellow               /* #e5b567 */
--color-green                /* #a8c373 */
--color-cyan                 /* #73bbb2 */
--color-blue                 /* #6c99bb */
--color-purple               /* #9e86c8 */
--color-pink                 /* #b05279 */
```

### Example Usage

```css
/* ✅ GOOD: Theme-compatible */
.dashboard-card {
    background: var(--background-secondary);
    color: var(--text-normal);
    border: 1px solid var(--background-modifier-border);
}

/* ❌ BAD: Breaks in dark mode */
.dashboard-card {
    background: #ffffff;
    color: #000000;
    border: 1px solid #cccccc;
}
```

---

## 🎨 Copy-Paste Components

### Stat Card

```css
/* Stats display card */
.stat-card {
    background: var(--background-secondary);
    border: 1px solid var(--background-modifier-border);
    border-radius: 8px;
    padding: 1rem;
    text-align: center;
}

.stat-value {
    font-size: 2rem;
    font-weight: 600;
    color: var(--text-accent);
}

.stat-label {
    font-size: 0.875rem;
    color: var(--text-muted);
    text-transform: uppercase;
}
```

**Usage in Markdown:**
```html
<div class="stat-card">
    <div class="stat-value">42</div>
    <div class="stat-label">Total Notes</div>
</div>
```

### Progress Bar

```css
/* Progress indicator */
.progress-bar {
    width: 100%;
    height: 24px;
    background: var(--background-modifier-border);
    border-radius: 8px;
    overflow: hidden;
}

.progress-fill {
    height: 100%;
    background: linear-gradient(90deg, 
        var(--color-cyan) 0%, 
        var(--color-blue) 100%);
    transition: width 0.3s ease;
}
```

**Usage in DataviewJS:**
```javascript
dv.paragraph(`
<div class="progress-bar">
    <div class="progress-fill" style="width: 75%;"></div>
</div>
`);
```

### Enhanced Table

```css
/* Better Dataview tables */
.dataview.table-view-table {
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 2px 4px var(--shadow-color);
}

.dataview.table-view-table th {
    background: var(--background-secondary);
    padding: 1rem;
    font-weight: 600;
    text-transform: uppercase;
    font-size: 0.875rem;
    color: var(--text-muted);
}

.dataview.table-view-table td {
    padding: 0.75rem 1rem;
}

.dataview.table-view-table tbody tr:hover {
    background: var(--background-modifier-hover);
}
```

---

## 🔧 Common Selectors

```css
/* Target specific dashboard types */
.markdown-preview-view[data-note-type="capsule_dashboard"] {
    /* Styles for capsule dashboards only */
}

.markdown-preview-view[data-note-type="master_dashboard"] {
    /* Styles for master dashboard only */
}

/* Target Dataview elements */
.block-language-dataview { /* Dataview block container */ }
.dataview.table-view-table { /* Dataview tables */ }
.dataview.list-view-ul { /* Dataview lists */ }

/* Target callouts */
.callout { /* All callouts */ }
.callout[data-callout="info"] { /* Info callouts */ }
.callout[data-callout="warning"] { /* Warning callouts */ }

/* Target headings */
.markdown-preview-view h1 { /* H1 in reading mode */ }
.markdown-preview-view h2 { /* H2 in reading mode */ }

/* Light/Dark mode specific */
.theme-light .my-element { /* Light mode only */ }
.theme-dark .my-element { /* Dark mode only */ }

/* Mobile specific */
.is-mobile .my-element { /* Mobile only */ }
```

---

## ⚡ Pro Tips

### 1. Use Browser DevTools

1. Open dashboard in Obsidian
2. Press `Ctrl+Shift+I` (or `Cmd+Option+I` on Mac)
3. Use element inspector to find selectors
4. Test CSS live in the console

### 2. Hot Reload Development

CSS snippets reload automatically when saved. Edit → Save → See changes instantly!

### 3. Start Small

Don't try to style everything at once:
1. Start with one component (e.g., tables)
2. Test thoroughly
3. Move to next component
4. Combine when patterns emerge

### 4. Test Light AND Dark

Always check both modes:
```css
/* Example: Different shadows for each mode */
.theme-light .card {
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.theme-dark .card {
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.5);
}
```

### 5. Mobile First

Start with mobile styles, then enhance for desktop:
```css
/* Mobile first (default) */
.grid {
    grid-template-columns: 1fr;
}

/* Desktop enhancement */
@media (min-width: 768px) {
    .grid {
        grid-template-columns: repeat(3, 1fr);
    }
}
```

---

## 🐛 Troubleshooting

### Styles Not Applying?

1. **Check snippet is enabled**
   - Settings → Appearance → CSS snippets → Toggle on

2. **Refresh snippet list**
   - Click refresh icon in CSS snippets section

3. **Check selector specificity**
   - Use browser DevTools to see which styles are applied
   - Increase specificity if needed

4. **Clear cache**
   - Close and reopen Obsidian
   - Or disable/re-enable snippet

### Colors Look Wrong?

1. **Use CSS variables** instead of hard-coded colors
2. **Test in both light and dark mode**
3. **Check theme compatibility** with different base themes

### Layout Issues?

1. **Avoid fixed widths** - use percentage or `fr` units
2. **Test on different screen sizes**
3. **Use flexbox/grid** for responsive layouts
4. **Check for conflicting styles** from theme or other snippets

---

## 📋 Recommended Reading Order

1. **This Quick Start** (you are here!) - 5 min
2. **[CSS Theming Guide](guides/CSS_THEMING_GUIDE.md)** - 30 min
3. **[Research Report](sprint-artifacts/12-ACTION-8-CSS-THEMING-RESEARCH.md)** - 15 min
4. **Browser DevTools** - Hands-on practice

---

## 🎯 Next Steps

### For Epic 12 Story Development

1. **Story 12-1:** Create `ocds-dashboard-core.css`
   - Start with grid layouts
   - Add card base styles
   - Define typography system

2. **Story 12-2:** Create `ocds-dataview-tables.css`
   - Copy enhanced table example
   - Add hover effects
   - Create variants

3. **Story 12-3:** Create `ocds-progress-indicators.css`
   - Copy progress bar example
   - Add stat cards
   - Create circular variant

### For Quick Wins

1. **Improve existing dashboards** with basic table styling
2. **Add stat cards** to master dashboard
3. **Create callout variant** for dashboard sections
4. **Add hover effects** to interactive elements

---

## 💡 Resources

- **Main Documentation:** [guides/CSS_THEMING_GUIDE.md](guides/CSS_THEMING_GUIDE.md)
- **Minimal Theme Docs:** https://minimal.guide/
- **Obsidian CSS Help:** https://help.obsidian.md/Extending+Obsidian/CSS+snippets
- **Community Forum:** https://forum.obsidian.md/t/meta-post-common-css-hacks/1978

---

**Ready to start?** Create your first snippet and begin styling! 🚀
