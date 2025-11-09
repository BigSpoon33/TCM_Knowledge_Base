#!/usr/bin/env python3
"""
Enhanced extraction with better figure/image handling
Filters out decorative images and captures figure captions
"""

import os
import re
import fitz
from pathlib import Path
from datetime import datetime


class FigureExtractor:
    """Extract with improved figure handling"""
    
    def __init__(self, pdf_path: Path, output_dir: Path):
        self.pdf_path = Path(pdf_path)
        self.output_dir = Path(output_dir)
        self.concepts_dir = output_dir / "TCM_Concepts"
        self.concepts_dir.mkdir(exist_ok=True, parents=True)
        
        self.images_dir = output_dir / "images" / "patterns"
        self.images_dir.mkdir(exist_ok=True, parents=True)
        
        self.doc = fitz.open(self.pdf_path)
        self.toc = self.doc.get_toc()
        
        print(f"✅ Loaded PDF: {self.pdf_path.name}")
        print(f"   Total pages: {len(self.doc)}")
    
    def extract_section(self, start_page: int, end_page: int, section_title: str):
        """Extract section with improved figure handling"""
        print(f"\n{'='*60}")
        print(f"EXTRACTING: {section_title}")
        print(f"{'='*60}")
        print(f"📄 Pages: {start_page}-{end_page} ({end_page - start_page + 1} pages)")
        
        # Extract text and figures together
        print("📝 Extracting text and figures...")
        pages_data = []
        
        for page_num in range(start_page - 1, end_page):
            page = self.doc[page_num]
            page_data = self._extract_page_with_figures(page, page_num + 1, section_title)
            pages_data.append(page_data)
        
        # Get subsections
        subsections = self._get_subsections(start_page, end_page)
        print(f"📑 Found {len(subsections)} subsections")
        
        # Create markdown
        print("📝 Creating markdown file...")
        md_content = self._create_markdown(section_title, start_page, end_page,
                                          subsections, pages_data)
        
        # Save file
        filename = self._sanitize_filename(section_title) + "_Guide.md"
        filepath = self.concepts_dir / filename
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(md_content)
        
        # Count total figures
        total_figures = sum(len(p['figures']) for p in pages_data)
        total_chars = sum(len(p['text']) for p in pages_data)
        
        print(f"✅ Created: {filename}")
        print(f"   Size: {len(md_content):,} characters")
        print(f"   Figures: {total_figures} (filtered from decorative images)")
        print(f"\n{'='*60}")
        print("EXTRACTION COMPLETE")
        print(f"{'='*60}\n")
        
        return filepath
    
    def _extract_page_with_figures(self, page, page_num, section_title):
        """Extract text and figures from a page"""
        # Get text blocks
        blocks = page.get_text("blocks", sort=True)
        
        # Detect columns
        page_width = page.rect.width
        mid_point = page_width / 2
        
        left_blocks = []
        right_blocks = []
        full_width_blocks = []
        
        for block in blocks:
            x0, y0, x1, y1, text, block_no, block_type = block
            block_width = x1 - x0
            block_center = (x0 + x1) / 2
            
            if len(text.strip()) < 3:
                continue
            
            if block_width > page_width * 0.8:
                full_width_blocks.append((y0, text))
            elif block_center < mid_point:
                left_blocks.append((y0, text))
            else:
                right_blocks.append((y0, text))
        
        # Sort blocks
        left_blocks.sort(key=lambda x: x[0])
        right_blocks.sort(key=lambda x: x[0])
        full_width_blocks.sort(key=lambda x: x[0])
        
        # Combine text
        page_text = ""
        for _, text in full_width_blocks:
            page_text += text.strip() + "\n\n"
        
        if left_blocks and right_blocks:
            page_text += "### LEFT COLUMN\n\n"
            for _, text in left_blocks:
                page_text += text.strip() + "\n\n"
            page_text += "\n### RIGHT COLUMN\n\n"
            for _, text in right_blocks:
                page_text += text.strip() + "\n\n"
        else:
            all_blocks = left_blocks + right_blocks
            all_blocks.sort(key=lambda x: x[0])
            for _, text in all_blocks:
                page_text += text.strip() + "\n\n"
        
        # Extract figures (filter out small decorative images)
        figures = []
        image_list = page.get_images()
        
        for img_index, img in enumerate(image_list):
            try:
                xref = img[0]
                base_image = self.doc.extract_image(xref)
                
                # Filter: only keep images larger than 100x100 pixels
                width = base_image.get('width', 0)
                height = base_image.get('height', 0)
                
                if width > 100 and height > 100:
                    image_bytes = base_image["image"]
                    image_ext = base_image["ext"]
                    
                    section_slug = self._sanitize_filename(section_title)
                    image_filename = f"{section_slug}_p{page_num}_fig{img_index}.{image_ext}"
                    image_path = self.images_dir / image_filename
                    
                    with open(image_path, "wb") as img_file:
                        img_file.write(image_bytes)
                    
                    # Try to find figure caption in text
                    caption = self._find_figure_caption(page_text, img_index, page_num)
                    
                    figures.append({
                        'filename': image_filename,
                        'page': page_num,
                        'width': width,
                        'height': height,
                        'size': len(image_bytes),
                        'caption': caption,
                        'relative_path': f"../../images/patterns/{image_filename}"
                    })
            except Exception as e:
                print(f"  ⚠️  Could not extract image on page {page_num}: {e}")
        
        return {
            'page_num': page_num,
            'text': page_text,
            'figures': figures
        }
    
    def _find_figure_caption(self, text, img_index, page_num):
        """Try to extract figure caption from text"""
        # Look for patterns like "Figure 47.1", "Fig. 47.1", etc.
        patterns = [
            r'Figure\s+\d+\.\d+[^\n]*',
            r'Fig\.\s+\d+\.\d+[^\n]*',
            r'FIGURE\s+\d+\.\d+[^\n]*',
        ]
        
        for pattern in patterns:
            matches = re.findall(pattern, text)
            if matches and img_index < len(matches):
                return matches[img_index].strip()
        
        return f"Figure on page {page_num}"
    
    def _get_subsections(self, start_page: int, end_page: int):
        """Get subsections from TOC"""
        subsections = []
        for entry in self.toc:
            level, title, page = entry
            if start_page <= page <= end_page:
                subsections.append({
                    'level': level,
                    'title': title,
                    'page': page
                })
        return subsections
    
    def _create_markdown(self, title: str, start_page: int, end_page: int,
                        subsections: list, pages_data: list):
        """Create markdown content with embedded figures"""
        total_figures = sum(len(p['figures']) for p in pages_data)
        
        md = f"""# {title}

**Source**: Maciocia *The Foundations of Chinese Medicine* 3rd ed.
**Pages**: {start_page}-{end_page}
**Extracted**: {datetime.now().strftime("%Y-%m-%d")}
**Figures**: {total_figures} diagrams/images extracted

---

## Table of Contents

"""
        for sub in subsections:
            indent = "  " * (sub['level'] - 3)
            md += f"{indent}- [{sub['title']}](#{self._create_anchor(sub['title'])}) (p. {sub['page']})\n"
        
        md += f"""
---

## Content with Figures

**Note**: This PDF uses a two-column layout. Text is organized by page with LEFT/RIGHT COLUMN markers.
Figures are embedded inline where they appear in the text.

"""
        
        # Add pages with embedded figures
        for page_data in pages_data:
            md += f"\n{'='*60}\n"
            md += f"### Page {page_data['page_num']}\n"
            md += f"{'='*60}\n\n"
            
            # Add text
            md += page_data['text']
            
            # Add figures for this page
            if page_data['figures']:
                md += f"\n\n**Figures on this page:**\n\n"
                for fig in page_data['figures']:
                    md += f"**{fig['caption']}**\n\n"
                    md += f"![{fig['caption']}]({fig['relative_path']})\n\n"
                    md += f"*Size: {fig['width']}x{fig['height']} pixels, {fig['size']:,} bytes*\n\n"
                    md += "---\n\n"
        
        md += f"""

---

## All Figures Summary

"""
        if total_figures > 0:
            md += f"This section contains {total_figures} figures/diagrams:\n\n"
            for page_data in pages_data:
                for fig in page_data['figures']:
                    md += f"- **Page {fig['page']}**: {fig['caption']}\n"
                    md += f"  - File: `{fig['filename']}`\n"
                    md += f"  - Dimensions: {fig['width']}x{fig['height']} pixels\n\n"
        else:
            md += "*No figures extracted (only decorative images found)*\n"
        
        md += f"""
---

## Notes

- Improved extraction with column detection and figure filtering
- Only images larger than 100x100 pixels are extracted (filters out decorative elements)
- Figure captions extracted from text where possible
- Figures embedded inline in the text for easier reference
- Cross-reference with printed book for accuracy

---

*Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}*
"""
        return md
    
    def _sanitize_filename(self, title: str) -> str:
        """Convert title to safe filename"""
        safe = re.sub(r'[^\w\s-]', '', title)
        safe = re.sub(r'\s+', '_', safe)
        return safe
    
    def _create_anchor(self, title: str) -> str:
        """Create markdown anchor from title"""
        anchor = title.lower()
        anchor = re.sub(r'[^\w\s-]', '', anchor)
        anchor = re.sub(r'\s+', '-', anchor)
        return anchor


def main():
    import sys
    
    base_dir = Path(__file__).parent.parent
    pdf_path = base_dir / "Books" / "Maciocia, Giovanni - The foundation of Chinese medicine_ a comprehensive text (2015, Elsevier) - libgen.lc.pdf"
    
    if not pdf_path.exists():
        print(f"❌ PDF not found: {pdf_path}")
        return 1
    
    extractor = FigureExtractor(pdf_path, base_dir)
    
    sections = [
        (754, 779, "Ch43_Pathogenic_Factors"),
        (780, 793, "Ch44_Six_Stages_Theory"),
        (794, 815, "Ch45_Four_Levels_Theory"),
        (816, 821, "Ch46_Three_Burners_Theory"),
        (824, 835, "Ch47_12_Channels"),
        (836, 849, "Ch48_Eight_Extraordinary_Vessels"),
        (850, 853, "Ch49_Five_Elements"),
    ]
    
    if len(sys.argv) > 1:
        section_num = int(sys.argv[1]) - 1
        if 0 <= section_num < len(sections):
            start, end, title = sections[section_num]
            extractor.extract_section(start, end, title)
        else:
            print(f"❌ Invalid section number. Choose 1-{len(sections)}")
            return 1
    else:
        for start, end, title in sections:
            extractor.extract_section(start, end, title)
    
    return 0


if __name__ == "__main__":
    exit(main())
