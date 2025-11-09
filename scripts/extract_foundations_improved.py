#!/usr/bin/env python3
"""
Improved extraction for two-column PDF layouts
Uses block-based extraction with column detection
"""

import os
import re
import fitz
from pathlib import Path
from datetime import datetime


class ImprovedFoundationsExtractor:
    """Extract with better column handling"""
    
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
        """Extract section with improved column handling"""
        print(f"\n{'='*60}")
        print(f"EXTRACTING: {section_title}")
        print(f"{'='*60}")
        print(f"📄 Pages: {start_page}-{end_page} ({end_page - start_page + 1} pages)")
        
        # Extract text with column awareness
        print("📝 Extracting text with column detection...")
        full_text = ""
        
        for page_num in range(start_page - 1, end_page):
            page = self.doc[page_num]
            page_text = self._extract_page_columns(page, page_num + 1)
            full_text += page_text + "\n\n" + "="*60 + f"\n[Page {page_num + 1}]\n" + "="*60 + "\n\n"
        
        print(f"  ✓ Extracted {len(full_text)} characters")
        
        # Extract images
        print("📷 Extracting images...")
        images = self._extract_images(start_page, end_page, section_title)
        print(f"  ✓ Extracted {len(images)} images")
        
        # Get subsections
        subsections = self._get_subsections(start_page, end_page)
        print(f"📑 Found {len(subsections)} subsections")
        
        # Create markdown
        print("📝 Creating markdown file...")
        md_content = self._create_markdown(section_title, start_page, end_page,
                                          subsections, full_text, images)
        
        # Save file
        filename = self._sanitize_filename(section_title) + "_Guide_v2.md"
        filepath = self.concepts_dir / filename
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(md_content)
        
        print(f"✅ Created: {filename}")
        print(f"   Size: {len(md_content):,} characters")
        print(f"\n{'='*60}")
        print("EXTRACTION COMPLETE")
        print(f"{'='*60}\n")
        
        return filepath
    
    def _extract_page_columns(self, page, page_num):
        """Extract text respecting column layout"""
        # Get text blocks with coordinates
        blocks = page.get_text("blocks", sort=True)
        
        if not blocks:
            return ""
        
        # Detect if page has two columns by analyzing x-coordinates
        page_width = page.rect.width
        mid_point = page_width / 2
        
        left_blocks = []
        right_blocks = []
        full_width_blocks = []
        
        for block in blocks:
            x0, y0, x1, y1, text, block_no, block_type = block
            block_width = x1 - x0
            block_center = (x0 + x1) / 2
            
            # Skip very small blocks (likely artifacts)
            if len(text.strip()) < 3:
                continue
            
            # If block spans most of page width, it's full-width (header/footer)
            if block_width > page_width * 0.8:
                full_width_blocks.append((y0, text))
            # Otherwise, assign to left or right column
            elif block_center < mid_point:
                left_blocks.append((y0, text))
            else:
                right_blocks.append((y0, text))
        
        # Sort blocks by y-coordinate (top to bottom)
        left_blocks.sort(key=lambda x: x[0])
        right_blocks.sort(key=lambda x: x[0])
        full_width_blocks.sort(key=lambda x: x[0])
        
        # Combine text: full-width first, then left column, then right column
        page_text = ""
        
        for _, text in full_width_blocks:
            page_text += text.strip() + "\n\n"
        
        # If we have two columns, process them separately
        if left_blocks and right_blocks:
            page_text += "### LEFT COLUMN\n\n"
            for _, text in left_blocks:
                page_text += text.strip() + "\n\n"
            
            page_text += "\n### RIGHT COLUMN\n\n"
            for _, text in right_blocks:
                page_text += text.strip() + "\n\n"
        else:
            # Single column or no clear division
            all_blocks = left_blocks + right_blocks
            all_blocks.sort(key=lambda x: x[0])
            for _, text in all_blocks:
                page_text += text.strip() + "\n\n"
        
        return page_text
    
    def _extract_images(self, start_page: int, end_page: int, section_title: str):
        """Extract images from pages"""
        images = []
        section_slug = self._sanitize_filename(section_title)
        
        for page_num in range(start_page - 1, end_page):
            page = self.doc[page_num]
            image_list = page.get_images()
            
            for img_index, img in enumerate(image_list):
                try:
                    xref = img[0]
                    base_image = self.doc.extract_image(xref)
                    image_bytes = base_image["image"]
                    image_ext = base_image["ext"]
                    
                    image_filename = f"{section_slug}_p{page_num + 1}_{img_index}.{image_ext}"
                    image_path = self.images_dir / image_filename
                    
                    with open(image_path, "wb") as img_file:
                        img_file.write(image_bytes)
                    
                    images.append({
                        'filename': image_filename,
                        'page': page_num + 1,
                        'relative_path': f"../../images/patterns/{image_filename}"
                    })
                except Exception as e:
                    print(f"  ⚠️  Could not extract image on page {page_num + 1}: {e}")
        
        return images
    
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
                        subsections: list, text: str, images: list):
        """Create markdown content"""
        md = f"""# {title}

**Source**: Maciocia *The Foundations of Chinese Medicine* 3rd ed.
**Pages**: {start_page}-{end_page}
**Extracted**: {datetime.now().strftime("%Y-%m-%d")}
**Note**: Improved extraction with column detection

---

## Table of Contents

"""
        for sub in subsections:
            indent = "  " * (sub['level'] - 3)
            md += f"{indent}- [{sub['title']}](#{self._create_anchor(sub['title'])}) (p. {sub['page']})\n"
        
        md += f"""
---

## Extracted Content

**Note**: This PDF uses a two-column layout. Text is organized by page, with LEFT COLUMN and RIGHT COLUMN markers where applicable.

{text}

---

## Images

"""
        if images:
            md += f"This section contains {len(images)} images:\n\n"
            for img in images:
                md += f"- Page {img['page']}: ![{img['filename']}]({img['relative_path']})\n"
        else:
            md += "*No images extracted*\n"
        
        md += f"""
---

## Notes

- Improved extraction with column detection
- LEFT COLUMN / RIGHT COLUMN markers show text flow
- Tables may still need manual review
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
    
    extractor = ImprovedFoundationsExtractor(pdf_path, base_dir)
    
    sections = [
        (754, 779, "Ch43_Pathogenic_Factors"),
        (780, 793, "Ch44_Six_Stages_Theory"),
        (794, 815, "Ch45_Four_Levels_Theory"),
        (816, 821, "Ch46_Three_Burners_Theory"),
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
