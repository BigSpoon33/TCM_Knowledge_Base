# Formula Extraction Summary

**Date**: 2025-11-05  
**Source**: Bensky - Formulas and Strategies, 2nd Edition (Scanned PDF)  
**Method**: OCR using Tesseract + PyMuPDF

## Results

- **Starting Count**: 95 formulas
- **Ending Count**: 137 formulas  
- **Newly Extracted**: 44 formulas
- **Progress**: 137/162 = **84.6% complete**

## Extraction Method

Since the PDF is a scanned document (no text layer), we used:
1. PyMuPDF to render pages as high-resolution images (300 DPI)
2. Tesseract OCR to extract text from images
3. Python script to clean and format the extracted text

## Newly Extracted Formulas

### Release Exterior (6)
- Bai Hu Jia Gui Zhi Tang
- Bai Hu Jia Ren Shen Tang  
- Chai Ge Jie Ji Tang
- Ge Gen Tang
- Ge Gen Huang Lian Huang Qin Tang
- Gui Zhi Jia Ge Gen Tang
- Ma Xing Shi Gan Tang
- Sang Xing Tang
- Xin Yi San

### Clear Heat (7)
- Huang Lian E Jiao Tang
- Huang Qin Tang
- Pu Ji Xiao Du Yin
- Qing Hao Bie Jia Tang
- Qing Ying Tang
- Xi Jiao Di Huang Tang

### Harmonize (1)
- Hao Qin Qing Dan Tang

### Drain Downward (3)
- Run Chang Wan
- Tiao Wei Cheng Qi Tang
- Wen Pi Tang

### Tonify (4)
- Bu Fei Tang
- Ding Chuan Tang
- E Jiao Ji Zi Huang Tang
- Zhi Bai Di Huang Wan

### Treat Phlegm (4)
- Bei Mu Gua Lou San
- Ling Gan Wu Wei Jiang Xin Tang
- San Zi Yang Qin Tang
- Xiao Xian Xiong Tang

### Regulate Qi (2)
- Ju Pi Zhu Ru Tang
- Tian Tai Wu Yao San

### Invigorate Blood (2)
- Dan Shen Yin
- Huo Luo Xiao Ling Dan

### Expel Dampness (4)
- San Ren Tang
- Yin Chen Hao Tang
- Zhen Wu Tang
- Zhu Ling Tang

### Treat Dryness (2)
- Yang Yin Qing Fei Tang
- Zeng Ye Tang

### Warm Interior (5)
- Da Jian Zhong Tang
- Li Zhong Wan
- Si Ni Tang
- Wu Zhu Yu Tang
- Xiao Jian Zhong Tang

## Status of Extracted Formulas

All newly extracted formulas have:
- ✅ Frontmatter with metadata
- ✅ Category classification
- ✅ Raw OCR'd text preserved
- ⚠️ **Status: needs_review** - OCR text requires manual formatting
- ⚠️ Some formulas may have captured TOC pages instead of content

## Next Steps

### Immediate (Manual Review Required)
1. **Review each extracted formula** - Check if OCR captured the correct pages
2. **Reformat content** - Structure into proper sections:
   - Pinyin name and translation
   - Actions/Indications
   - Ingredients with dosages
   - Tongue and pulse
   - Contraindications
   - Modifications
3. **Fix OCR errors** - Correct any character recognition mistakes
4. **Add wikilinks** - Link to related herbs, patterns, symptoms

### Remaining Formulas (25 still needed)

Based on Gap_Filling_Checklist.md, we still need approximately 25 more formulas to reach the NCCAOM requirement of 162 formulas.

## Technical Notes

### OCR Quality
- **Good**: Most text extracted successfully
- **Issues**: 
  - Some formulas captured TOC pages due to incorrect page numbers
  - Two-column layout sometimes causes text flow issues
  - Chinese characters not captured (expected - English OCR only)
  - Some special characters misread

### Performance
- **Time**: ~30-40 minutes for 44 formulas
- **Speed**: ~1 minute per formula (3-4 pages each)
- **File sizes**: 5,000-27,000 characters per formula

### Script Location
- `scripts/extract_formulas_bensky_ocr.py` - Main extraction script
- Test extraction code in session history

## Recommendations

1. **Priority**: Manually review and format the 44 newly extracted formulas
2. **Verify page numbers**: Some formulas may need re-extraction with corrected page ranges
3. **Consider alternative sources**: For remaining 25 formulas, check if they exist in:
   - Maciocia *Practice of Chinese Medicine*
   - Maclean *Clinical Handbook of Internal Medicine*
   - Online TCM databases

## Files Modified

- `TCM_Formulas/` - 44 new .md files created
- All new files have `extraction_method: "OCR"` and `status: "needs_review"` in frontmatter

---

*Generated: 2025-11-05*
