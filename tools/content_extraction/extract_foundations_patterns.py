#!/usr/bin/env python3
"""
Extract Pattern Differentiation sections from Maciocia Foundations of Chinese Medicine
Handles complex two-column layouts, tables, and images
"""

import re
from datetime import datetime
from pathlib import Path

import fitz  # PyMuPDF


class FoundationsExtractor:
    """Extract pattern differentiation sections from Foundations PDF"""

    def __init__(self, pdf_path: Path, output_dir: Path):
        self.pdf_path = Path(pdf_path)
        self.output_dir = Path(output_dir)
        self.concepts_dir = output_dir / "TCM_Concepts"
        self.concepts_dir.mkdir(exist_ok=True, parents=True)

        self.images_dir = output_dir / "images" / "patterns"
        self.images_dir.mkdir(exist_ok=True, parents=True)

        # Load PDF and TOC
        self.doc = fitz.open(self.pdf_path)
        self.toc = self.doc.get_toc()

        print(f"✅ Loaded PDF: {self.pdf_path.name}")
        print(f"   Total pages: {len(self.doc)}")
        print(f"   TOC entries: {len(self.toc)}")

    def extract_section(self, start_page: int, end_page: int, section_title: str):
        """Extract a section from specified pages"""
        print(f"\n{'=' * 60}")
        print(f"EXTRACTING: {section_title}")
        print(f"{'=' * 60}")
        print(f"📄 Pages: {start_page}-{end_page} ({end_page - start_page + 1} pages)")

        # Get subsections from TOC
        subsections = self._get_subsections(start_page, end_page)
        print(f"📑 Found {len(subsections)} subsections")

        # Extract text
        print("📝 Extracting text...")
        full_text = ""
        for page_num in range(start_page - 1, end_page):
            page = self.doc[page_num]
            text = page.get_text("text", sort=True)  # sort=True helps with column layout
            full_text += text + "\n\n"

        print(f"  ✓ Extracted {len(full_text)} characters")

        # Extract images
        print("📷 Extracting images...")
        images = self._extract_images(start_page, end_page, section_title)
        print(f"  ✓ Extracted {len(images)} images")

        # Create markdown
        print("📝 Creating markdown file...")
        md_content = self._create_markdown(section_title, start_page, end_page, subsections, full_text, images)

        # Save file
        filename = self._sanitize_filename(section_title) + "_Guide.md"
        filepath = self.concepts_dir / filename

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(md_content)

        print(f"✅ Created: {filename}")
        print(f"   Size: {len(md_content):,} characters")
        print(f"   Images: {len(images)}")
        print(f"\n{'=' * 60}")
        print("EXTRACTION COMPLETE")
        print(f"{'=' * 60}\n")

        return filepath

    def _get_subsections(self, start_page: int, end_page: int):
        """Get subsections from TOC within page range"""
        subsections = []
        for entry in self.toc:
            level, title, page = entry
            if start_page <= page <= end_page:
                subsections.append({"level": level, "title": title, "page": page})
        return subsections

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

                    # Save image
                    image_filename = f"{section_slug}_p{page_num + 1}_{img_index}.{image_ext}"
                    image_path = self.images_dir / image_filename

                    with open(image_path, "wb") as img_file:
                        img_file.write(image_bytes)

                    images.append(
                        {
                            "filename": image_filename,
                            "page": page_num + 1,
                            "relative_path": f"../../images/patterns/{image_filename}",
                        }
                    )
                except Exception as e:
                    print(f"  ⚠️  Could not extract image on page {page_num + 1}: {e}")

        return images

    def _create_markdown(self, title: str, start_page: int, end_page: int, subsections: list, text: str, images: list):
        """Create markdown content"""
        md = f"""# {title}

**Source**: Maciocia *The Foundations of Chinese Medicine* 3rd ed.
**Pages**: {start_page}-{end_page}
**Extracted**: {datetime.now().strftime("%Y-%m-%d")}

---

## Table of Contents

"""
        # Add subsections to TOC
        for sub in subsections:
            indent = "  " * (sub["level"] - 3)  # Adjust indent based on level
            md += f"{indent}- [{sub['title']}](#{self._create_anchor(sub['title'])}) (p. {sub['page']})\n"

        md += f"""
---

## Extracted Content

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

- This file was auto-extracted from the PDF
- Two-column layout may cause some text flow issues
- Tables and complex formatting may need manual review
- Images are stored in `images/patterns/` directory
- Cross-reference with printed book for accuracy

---

*Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}*
"""
        return md

    def _sanitize_filename(self, title: str) -> str:
        """Convert title to safe filename"""
        # Remove special characters
        safe = re.sub(r"[^\w\s-]", "", title)
        # Replace spaces with underscores
        safe = re.sub(r"\s+", "_", safe)
        return safe

    def _create_anchor(self, title: str) -> str:
        """Create markdown anchor from title"""
        anchor = title.lower()
        anchor = re.sub(r"[^\w\s-]", "", anchor)
        anchor = re.sub(r"\s+", "-", anchor)
        return anchor


def main():
    import sys

    base_dir = Path(__file__).parent.parent
    pdf_path = (
        base_dir
        / "Books"
        / "Maciocia, Giovanni - The foundation of Chinese medicine_ a comprehensive text (2015, Elsevier) - libgen.lc.pdf"
    )

    if not pdf_path.exists():
        print(f"❌ PDF not found: {pdf_path}")
        return 1

    extractor = FoundationsExtractor(pdf_path, base_dir)

    # Define sections to extract
    sections = [
        (754, 779, "Ch43_Pathogenic_Factors"),
        (780, 793, "Ch44_Six_Stages_Theory"),
        (794, 815, "Ch45_Four_Levels_Theory"),
        (816, 821, "Ch46_Three_Burners_Theory"),
    ]

    # Extract specific section if provided as argument
    if len(sys.argv) > 1:
        section_num = int(sys.argv[1]) - 1
        if 0 <= section_num < len(sections):
            start, end, title = sections[section_num]
            extractor.extract_section(start, end, title)
        else:
            print(f"❌ Invalid section number. Choose 1-{len(sections)}")
            return 1
    else:
        # Extract all sections
        for start, end, title in sections:
            extractor.extract_section(start, end, title)

    return 0


if __name__ == "__main__":
    exit(main())
