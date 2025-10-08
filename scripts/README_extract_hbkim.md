# HB Kim Handbook Extractor

Interactive tool for extracting TCM pattern differentiation data from HB Kim's *Handbook of Oriental Medicine* (3rd Edition).

## Features

✅ **Text-based extraction** - Fast parsing of pattern sections
✅ **Vision model fallback** - Use Claude vision for complex tables
✅ **Interactive review** - Review every extraction before saving
✅ **Edit mode** - Manually adjust extracted data
✅ **Markdown output** - Ready for symptom/disease templates

## Usage

### Basic Workflow

```bash
python3 scripts/extract_hbkim.py
```

### Menu Options

**1. Extract page range (text-based)**
- Enter start and end page numbers
- Tool extracts and parses pattern sections
- Review each pattern individually
- Save, edit, skip, or use vision model

**2. Extract single page (vision model)**
- Enter page number
- Sends page image to Claude vision API
- Gets structured markdown output
- Review and save

**3. View extraction history**
- See all previously extracted files

## Example Session

```
📖 HB KIM HANDBOOK INTERACTIVE EXTRACTOR
════════════════════════════════════════

OPTIONS:
  1. Extract page range (text-based)
  2. Extract single page (vision model)
  3. View extraction history
  4. Exit

Choice: 1

📄 PAGE RANGE EXTRACTION
────────────────────────────────────────
Start page: 100
End page: 105

🔍 Extracting pages 100-105...
🔬 Parsing pattern sections...

✅ Found 15 patterns

════════════════════════════════════════
📋 HEART QI DEFICIENCY (Page 100)
════════════════════════════════════════

**FCM Symptoms:**
  • Palpitations, shortness of breath on exertion
  • Sweating, pallor, tiredness, listlessness
  • Pale or normal tongue color

**Tongue:** Pale or normal
**Pulse:** Empty

**KEY SX:** Palpitations, tiredness, empty pulse

Pattern 1/15 - (s)ave / (e)dit / (sk)ip / (v)ision / (q)uit: s
✅ Saved to extracted_data/heart_qi_deficiency.md
```

## Page Number Tips

**PDF pages vs Book pages:**
- The PDF has ~7 pages of front matter
- PDF page 100 ≈ Book page 93
- Check the page numbers printed in the PDF to verify

**Finding sections:**
- Table of contents: PDF pages 1-20
- Diagnosis patterns: PDF pages ~85-120
- Point therapeutics: PDF pages ~200-400
- Herbs: PDF pages ~400-600

## Output Files

Extracted patterns are saved to `extracted_data/` with:
- Pattern name as filename (e.g., `heart_qi_deficiency.md`)
- Structured markdown format
- Symptoms organized by CAM/FCM
- Tongue/pulse diagnosis
- Key symptoms highlighted
- Source page reference

## Vision Model Setup

To enable vision model fallback:

```bash
export ANTHROPIC_API_KEY="your-api-key"
```

**When to use vision mode:**
- Complex tables with borders
- Multi-column layouts
- Charts and diagrams
- When text extraction fails

## Parsing Quality

### Works Well On:
✅ Pattern differentiation sections (CAM/FCM format)
✅ Symptom lists with bullet points
✅ Tongue/pulse markers (®, ①, d))
✅ Key symptom summaries

### May Need Vision Model:
⚠️ Dense tables with cell borders
⚠️ Multi-column comparison charts
⚠️ Diagrams with annotations
⚠️ Hand-drawn illustrations

## Workflow Tips

### Recommended Extraction Order:

1. **Start with major organ patterns** (Pages 93-120)
   - Heart, Liver, Spleen, Lung, Kidney patterns
   - These are the foundation

2. **Extract common symptoms** (Pages varies)
   - Headache, dizziness, pain, etc.
   - Map to symptom templates

3. **Point therapeutics** (Pages 200+)
   - Point combinations
   - Therapeutic properties

4. **Herbal formulas** (Pages 400+)
   - Formula compositions
   - Pattern indications

### Quality Control:

- **Always review before saving** - Text extraction isn't perfect
- **Use edit mode** to clean up OCR issues (Ql→QI, Sl→SI, etc.)
- **Try vision model** if text looks garbled
- **Manual transcription** for critical tables if needed

## Known Issues

### Text Extraction Quirks:
- OCR sometimes reads `QI` as `Ql`
- OCR sometimes reads `SI` as `Sl`
- CAM/FCM columns may blend together
- Indentation can be inconsistent

**Solution:** Use edit mode or vision model

### Vision Model Limitations:
- Requires ANTHROPIC_API_KEY
- Costs ~$0.01-0.05 per page
- Takes 5-10 seconds per page
- Very accurate but slower

## Advanced Usage

### Batch Extract a Section:

```python
from scripts.extract_hbkim import HBKimExtractor
from pathlib import Path

extractor = HBKimExtractor(
    Path("HOM 3rd Ed - HBKim.pdf"),
    Path(".")
)

# Extract Heart patterns (pages 100-105)
text = extractor.extract_page_range(100, 105)
patterns = extractor.parse_pattern_section(text, 100)

for pattern in patterns:
    print(pattern.name)
    # Process pattern...
```

### Custom Extraction Prompt:

When using vision model, you can customize the extraction prompt in the code to focus on specific data types (symptoms, points, herbs, etc.).

## Next Steps

After extracting:

1. **Review and clean** extracted markdown files
2. **Merge into symptom templates** using TCM_Symptoms/TEMPLATE_Symptom.md
3. **Add wikilinks** to related entities
4. **Run auto-sync** to build relationships
5. **Commit to Git**

---

**Happy extracting!** 📚✨

The goal is accuracy over speed - take your time reviewing each extraction.
