# Maciocia Diagnosis Extraction Guide

## Overview

This guide helps you extract diagnostic sections from Maciocia's "Diagnosis in Chinese Medicine" book and create comprehensive markdown notes.

## Scripts Available

1. **extract_diagnosis_sections.py** - Main extraction script
2. **extract_maciocia_diagnosis.py** - Full book extractor (more complex)

## Quick Start

### Step 1: Find Page Numbers

Open the PDF and manually find the page numbers for each section:

**Method 1: Use PDF viewer**
- Open the PDF in your PDF viewer
- Use the table of contents/bookmarks to navigate
- Note the actual page numbers (not PDF page numbers)

**Method 2: Search in PDF**
- Search for "Chapter 23: TONGUE DIAGNOSIS"
- Search for "Chapter X: PULSE DIAGNOSIS"  
- Search for "DIAGNOSIS BY QUESTIONING"

### Step 2: Extract Sections

Once you have page numbers, run the extraction:

```bash
# Extract tongue diagnosis (example: pages 300-400)
python3 scripts/extract_diagnosis_sections.py \
  --section tongue \
  --start-page 300 \
  --end-page 400

# Extract pulse diagnosis (example: pages 450-550)
python3 scripts/extract_diagnosis_sections.py \
  --section pulse \
  --start-page 450 \
  --end-page 550

# Extract questioning section (example: pages 150-250)
python3 scripts/extract_diagnosis_sections.py \
  --section questioning \
  --start-page 150 \
  --end-page 250

# Extract all sections (if you know all page ranges)
python3 scripts/extract_diagnosis_sections.py --section all
```

### Step 3: Include Images (Optional)

To extract images along with text:

```bash
python3 scripts/extract_diagnosis_sections.py \
  --section tongue \
  --start-page 300 \
  --end-page 400
  # (images are extracted by default)
```

To skip images (faster):

```bash
python3 scripts/extract_diagnosis_sections.py \
  --section tongue \
  --start-page 300 \
  --end-page 400 \
  --no-images
```

## Manual Page Finding Instructions

### For Tongue Diagnosis:

1. Open PDF: `Books/Diagnosis in Chinese Medicine...pdf`
2. Look for **"SECTION 3: TONGUE DIAGNOSIS"** or **"Chapter 23"**
3. This section typically includes:
   - Chapter 23: Tongue Diagnosis (Introduction)
   - Chapter 24: Tongue-Body Colour
   - Chapter 25: Tongue-Body Shape
   - Chapter 26: Tongue Coating
   - Chapter 27: Tongue-Body Texture
   - Chapter 28: Tongue-Body Movement
   - Chapter 29: Sublingual Veins
4. Note start page of Chapter 23 and end page of Chapter 29

### For Pulse Diagnosis:

1. Look for **"SECTION X: PULSE DIAGNOSIS"** or relevant chapter
2. This section typically includes:
   - Introduction to Pulse Diagnosis
   - Pulse Positions
   - Pulse Qualities (28 pulses)
   - Clinical Applications
3. Note start and end pages

### For Questioning (Ten Questions):

1. Look for **"DIAGNOSIS BY QUESTIONING"** or **"PART 3"**
2. This section covers:
   - The Ten Questions (Shi Wen)
   - Pain assessment
   - Appetite and thirst
   - Sleep and sweating
   - Urination and bowels
   - Menstruation
   - Emotional factors
3. Note start and end pages

## Output

The script creates:

1. **Markdown files** in `TCM_Concepts/`:
   - `Tongue_Diagnosis_Comprehensive_Guide.md`
   - `Pulse_Diagnosis_Comprehensive_Guide.md`
   - `Diagnosis_by_Questioning_Comprehensive_Guide.md`

2. **Images** in `images/diagnosis/`:
   - All extracted diagrams and photos
   - Named by section and page number

## File Structure

Each generated markdown file includes:

- **Metadata**: Source, page numbers, extraction date
- **Table of Contents**: Auto-generated from subsections
- **Content**: Organized by subsections with headings
- **Images**: Embedded with proper paths
- **Related Concepts**: Wikilinks to related notes

## Tips for Best Results

### 1. Accurate Page Numbers
- Use the **actual book page numbers**, not PDF page numbers
- PDF page numbers may be offset by 10-20 pages
- Check the page header/footer in the PDF for actual page numbers

### 2. Section Boundaries
- Include complete sections (don't cut off mid-chapter)
- Better to include a few extra pages than miss content
- You can always edit the markdown file afterward

### 3. Image Quality
- Images are extracted at original resolution
- Large sections may have many images (100+)
- Use `--no-images` flag for faster text-only extraction

### 4. Text Cleanup
- The script automatically cleans common OCR issues
- You may need to manually fix some formatting
- Tables may need manual adjustment

## Troubleshooting

### "Error extracting text"
- Check that page numbers are valid (start < end)
- Verify PDF path is correct
- Ensure `pdftotext` is installed: `which pdftotext`

### "No text extracted"
- Page range may be incorrect
- Try a smaller page range first
- Check if pages are image-only (scanned pages)

### "Could not find section"
- Use manual page numbers with `--start-page` and `--end-page`
- Don't rely on automatic TOC detection

### Images not extracting
- Ensure PyMuPDF is installed: `pip install PyMuPDF`
- Some PDFs have protected images
- Try `--no-images` and add images manually later

## Example Workflow

```bash
# 1. Open PDF and find page numbers
# Tongue: pages 300-400
# Pulse: pages 450-550  
# Questioning: pages 150-250

# 2. Extract each section
cd /home/shuma/Documents/AI_Suite/TCM_Knowledge_Base

python3 scripts/extract_diagnosis_sections.py \
  --section tongue \
  --start-page 300 \
  --end-page 400

python3 scripts/extract_diagnosis_sections.py \
  --section pulse \
  --start-page 450 \
  --end-page 550

python3 scripts/extract_diagnosis_sections.py \
  --section questioning \
  --start-page 150 \
  --end-page 250

# 3. Check output
ls -lh TCM_Concepts/*Comprehensive_Guide.md
ls -lh images/diagnosis/

# 4. Open in Obsidian and review
# Make any necessary edits
# Add wikilinks to related concepts
```

## Next Steps After Extraction

1. **Review the generated markdown files**
   - Check formatting
   - Verify images are embedded correctly
   - Fix any OCR errors

2. **Add wikilinks**
   - Link to existing pattern notes
   - Link to symptom notes
   - Link to related diagnostic concepts

3. **Enhance with examples**
   - Add clinical examples from your experience
   - Add case studies
   - Add practice questions

4. **Create flashcards**
   - Extract key points for flashcards
   - Use for exam preparation

5. **Update Gap_Filling_Checklist**
   - Check off completed items
   - Update progress tracking

## Advanced Usage

### Extract Custom Page Range

```bash
# Extract any custom section
python3 scripts/extract_diagnosis_sections.py \
  --section tongue \
  --start-page 123 \
  --end-page 456
```

### Batch Extract Multiple Sections

```bash
# Create a shell script
cat > extract_all.sh << 'EOF'
#!/bin/bash
python3 scripts/extract_diagnosis_sections.py --section tongue --start-page 300 --end-page 400
python3 scripts/extract_diagnosis_sections.py --section pulse --start-page 450 --end-page 550
python3 scripts/extract_diagnosis_sections.py --section questioning --start-page 150 --end-page 250
EOF

chmod +x extract_all.sh
./extract_all.sh
```

## Dependencies

Required:
- Python 3.7+
- `pdftotext` (from poppler-utils)
- `PyMuPDF` (fitz) for image extraction

Install:
```bash
# Ubuntu/Debian
sudo apt-get install poppler-utils
pip install PyMuPDF

# macOS
brew install poppler
pip install PyMuPDF
```

## Support

If you encounter issues:
1. Check this guide first
2. Verify all dependencies are installed
3. Try with a small page range first (10-20 pages)
4. Check the PDF is not corrupted or password-protected

---

*Last Updated: 2025-11-04*
