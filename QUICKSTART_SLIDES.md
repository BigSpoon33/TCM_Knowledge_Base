# Quick Start: Slides Generation

## Generate Slides for a Pattern

```bash
# 1. Set your API key
export GEMINI_API_KEY="AIzaSyCsTagD8ODpN2A_OMtcM0vtw0Nn8fByCKs"

# 2. Navigate to project
cd /home/shuma/Documents/AI_Suite/TCM_Knowledge_Base

# 3. Generate all materials (including slides)
python scripts/generate_all_materials.py "Spleen Qi Deficiency" --class-id TCM_101
```

## Generate Slides Only

```python
from pathlib import Path
from scripts.generate_slides_ai import SlidesGeneratorAI

# Read root note
root_note = Path('Materials/TCM_101/Root_Note_Spleen_Qi_Deficiency.md')
with open(root_note) as f:
    content = f.read()

# Generate slides
gen = SlidesGeneratorAI()
slides = gen.generate_pattern_slides(content, "Spleen Qi Deficiency")

# Save
output = Path('Materials/TCM_101/Spleen_Qi_Deficiency_Slides.md')
with open(output, 'w') as f:
    f.write(slides)
```

## View Slides in Obsidian

1. Open Obsidian vault: `/home/shuma/Documents/AI_Suite/TCM_Knowledge_Base`
2. Install **Advanced Slides** plugin (if not installed)
3. Open `Materials/TCM_101/{Pattern}_Slides.md`
4. Click **"Start Presentation"** button in toolbar
5. Navigate:
   - `→` / `Space` - Next slide
   - `←` - Previous slide
   - `Esc` - Overview mode
   - `S` - Speaker notes
   - `F` - Fullscreen

## Customize Slides

Edit `scripts/generate_slides_ai.py`:

```python
# Change theme
frontmatter = f"""---
theme: black  # Change to: white, league, beige, sky, night, serif, simple
transition: slide  # Change to: fade, convex, concave, zoom
---
"""

# Modify prompt for different structure
prompt = f"""
Create slides with:
- More clinical examples
- Fewer theoretical slides
- More images/diagrams
...
"""
```

## Slide Structure (TCM Patterns)

1. Title Slide (Pattern name + Chinese)
2. Overview (Category, characteristics)
3. Etiology & Pathology
4. Clinical Manifestations (with fragments)
5. Tongue & Pulse
6. Differential Diagnosis (comparison table)
7. Treatment Principles
8. Key Formulas
9. Acupuncture Points
10. Clinical Pearls
11. Case Example
12. Summary

## Tips

- **Fragments**: Use `<!-- .element: class="fragment" -->` for progressive reveal
- **Speaker Notes**: Add `Note: [your note]` for presenter insights
- **Emojis**: 🌿 herbs, 💊 formulas, 📍 points, ⚠️ cautions, 💡 pearls
- **Tables**: Great for differential diagnosis comparisons
- **Vertical Slides**: Use `----` for sub-topics (access with ↓ arrow)

## Troubleshooting

**"API key not set"**
```bash
export GEMINI_API_KEY="your-key-here"
```

**"Root note not found"**
- Check file exists in `Materials/TCM_101/`
- Verify frontmatter has `type: root_note`

**"Slides don't render in Obsidian"**
- Install Advanced Slides plugin
- Check frontmatter syntax (must start with `---`)
- Reload Obsidian

## Output Files

```
Materials/TCM_101/
├── Spleen_Qi_Deficiency_Flashcards.md    # 10 flashcards
├── Spleen_Qi_Deficiency_Bank.md          # 5 questions
├── Spleen_Qi_Deficiency_Slides.md        # ~13 slides ⭐
├── Spleen_Qi_Deficiency_Study_Material.md
└── Spleen_Qi_Deficiency_Tasks.md
```

---

**Ready to generate slides? Run the command above!** 🚀
