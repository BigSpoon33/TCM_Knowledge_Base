#!/usr/bin/env python3
"""
Extract Diagnostic Sections from Maciocia Diagnosis Book

Focused extraction of:
1. Tongue Diagnosis (complete section)
2. Pulse Diagnosis (complete section)
3. Ten Questions / Questioning (complete section)

Creates comprehensive markdown files for each section.
"""

import re
import subprocess
from pathlib import Path

import fitz  # PyMuPDF


class DiagnosisExtractor:
    """Extract diagnostic sections from Maciocia book"""

    def __init__(self, pdf_path: Path, output_dir: Path):
        self.pdf_path = Path(pdf_path)
        self.output_dir = Path(output_dir)
        self.concepts_dir = output_dir / "TCM_Concepts"
        self.concepts_dir.mkdir(exist_ok=True, parents=True)

        self.images_dir = output_dir / "images" / "diagnosis"
        self.images_dir.mkdir(exist_ok=True, parents=True)

    def find_section_in_toc(self, section_keyword: str) -> tuple[int, int]:
        """Find section page range by searching TOC"""
        print(f"🔍 Searching for '{section_keyword}' in table of contents...")

        # Extract TOC (usually in first 30 pages)
        toc_text = self.extract_text(1, 30)

        # Look for section with page numbers
        # Common patterns:
        # "SECTION X: TONGUE DIAGNOSIS ... 259"
        # "Chapter XX: PULSE DIAGNOSIS ... 381"

        lines = toc_text.split("\n")
        start_page = None
        end_page = None

        for i, line in enumerate(lines):
            if section_keyword.upper() in line.upper():
                # Look for page number in this line or next few lines
                for j in range(i, min(i + 5, len(lines))):
                    numbers = re.findall(r"\b(\d{2,4})\b", lines[j])
                    if numbers:
                        start_page = int(numbers[0])
                        print(f"  ✓ Found start page: {start_page}")
                        break

                # Look for next section to find end page
                if start_page:
                    for j in range(i + 1, min(i + 20, len(lines))):
                        # Look for next major section or chapter
                        if re.match(r"(SECTION|Chapter|PART)", lines[j], re.IGNORECASE):
                            numbers = re.findall(r"\b(\d{2,4})\b", lines[j])
                            if numbers:
                                end_page = int(numbers[0]) - 1
                                print(f"  ✓ Found end page: {end_page}")
                                break
                    break

        if not start_page:
            print(f"  ⚠️  Could not find '{section_keyword}' in TOC")
            return 0, 0

        if not end_page:
            # Estimate end page (add 100 pages as default)
            end_page = start_page + 100
            print(f"  ⚠️  End page not found, estimating: {end_page}")

        return start_page, end_page

    def extract_text(self, start_page: int, end_page: int) -> str:
        """Extract text from page range"""
        try:
            result = subprocess.run(
                ["pdftotext", "-f", str(start_page), "-l", str(end_page), "-layout", str(self.pdf_path), "-"],
                capture_output=True,
                text=True,
                check=True,
            )
            return result.stdout
        except subprocess.CalledProcessError as e:
            print(f"❌ Error extracting text: {e}")
            return ""

    def extract_images(self, start_page: int, end_page: int, section_name: str) -> list[str]:
        """Extract images from page range"""
        images = []

        try:
            doc = fitz.open(self.pdf_path)
            safe_name = re.sub(r"[^\w\s-]", "", section_name).strip().replace(" ", "_")

            for page_num in range(start_page - 1, min(end_page, len(doc))):
                page = doc[page_num]
                image_list = page.get_images()

                for img_index, img in enumerate(image_list):
                    try:
                        xref = img[0]
                        base_image = doc.extract_image(xref)
                        image_bytes = base_image["image"]
                        image_ext = base_image["ext"]

                        # Create filename
                        image_filename = f"{safe_name}_p{page_num + 1}_img{img_index + 1}.{image_ext}"
                        image_path = self.images_dir / image_filename

                        # Save image
                        with open(image_path, "wb") as img_file:
                            img_file.write(image_bytes)

                        images.append(image_filename)

                    except Exception as e:
                        print(f"  ⚠️  Error extracting image {img_index} from page {page_num + 1}: {e}")

            doc.close()
            print(f"  📷 Extracted {len(images)} images")

        except Exception as e:
            print(f"❌ Error extracting images: {e}")

        return images

    def clean_text(self, text: str) -> str:
        """Clean extracted text"""
        # Remove excessive whitespace
        text = re.sub(r"\n{3,}", "\n\n", text)

        # Remove page numbers (standalone numbers on their own line)
        text = re.sub(r"\n\s*\d+\s*\n", "\n", text)

        # Remove headers/footers
        text = re.sub(r"Diagnosis in Chinese Medicine.*?\n", "", text)
        text = re.sub(r"CHAPTER \d+.*?\n", "", text)

        # Fix common OCR issues
        text = text.replace("ﬁ", "fi")
        text = text.replace("ﬂ", "fl")
        text = text.replace("–", "-")
        text = text.replace("\u2019", "'")  # Right single quotation mark
        text = text.replace("\u201c", '"')  # Left double quotation mark
        text = text.replace("\u201d", '"')  # Right double quotation mark

        return text.strip()

    def split_into_subsections(self, text: str) -> list[tuple[str, str]]:
        """Split text into subsections based on headings"""
        subsections = []

        # Look for major headings (ALL CAPS or Chapter headings)
        lines = text.split("\n")
        current_heading = "Introduction"
        current_content = []

        for line in lines:
            # Check if line is a heading
            if line.isupper() and len(line.strip()) > 3 and len(line.strip()) < 100:
                # Save previous section
                if current_content:
                    subsections.append((current_heading, "\n".join(current_content)))

                # Start new section
                current_heading = line.strip()
                current_content = []
            else:
                current_content.append(line)

        # Add last section
        if current_content:
            subsections.append((current_heading, "\n".join(current_content)))

        return subsections

    def create_markdown(self, section_name: str, text: str, images: list[str], start_page: int, end_page: int) -> str:
        """Create comprehensive markdown file"""
        md = f"# {section_name}\n\n"

        # Metadata
        md += "**Source**: Maciocia *Diagnosis in Chinese Medicine* 2nd ed.\n"
        md += f"**Pages**: {start_page}-{end_page}\n"
        md += "**Extracted**: 2025-11-04\n\n"
        md += "---\n\n"

        # Table of contents
        md += "## Table of Contents\n\n"
        subsections = self.split_into_subsections(text)
        for i, (heading, _) in enumerate(subsections, 1):
            safe_heading = heading.lower().replace(" ", "-").replace("/", "-")
            md += f"{i}. [{heading}](#{safe_heading})\n"
        md += "\n---\n\n"

        # Content by subsection
        for heading, content in subsections:
            md += f"## {heading}\n\n"
            md += self.clean_text(content)
            md += "\n\n"

        # Images section
        if images:
            md += "---\n\n"
            md += "## Images and Diagrams\n\n"
            for i, img in enumerate(images, 1):
                md += f"### Image {i}\n\n"
                md += f"![{img}](../../images/diagnosis/{img})\n\n"

        # Related concepts
        md += "---\n\n"
        md += "## Related Concepts\n\n"

        if "tongue" in section_name.lower():
            md += "- [[Inspection]]\n"
            md += "- [[Palpation]]\n"
            md += "- [[Tongue Coating]]\n"
            md += "- [[Tongue Body]]\n"
        elif "pulse" in section_name.lower():
            md += "- [[Palpation]]\n"
            md += "- [[Pulse Positions]]\n"
            md += "- [[Pulse Qualities]]\n"
        elif "question" in section_name.lower():
            md += "- [[Patient Interview]]\n"
            md += "- [[Medical History]]\n"
            md += "- [[Symptom Assessment]]\n"

        md += "\n---\n\n"
        md += "*This content is extracted from Maciocia's Diagnosis in Chinese Medicine for educational purposes.*\n"

        return md

    def extract_section(
        self, section_name: str, start_page: int = 0, end_page: int = 0, extract_images: bool = True
    ) -> Path:
        """Extract a complete section"""
        print(f"\n{'=' * 60}")
        print(f"EXTRACTING: {section_name}")
        print(f"{'=' * 60}")

        # Find pages if not provided
        if start_page == 0:
            start_page, end_page = self.find_section_in_toc(section_name)

        if start_page == 0:
            print(f"❌ Could not find section '{section_name}'")
            return None

        print(f"📄 Pages: {start_page}-{end_page}")

        # Extract text
        print("📝 Extracting text...")
        text = self.extract_text(start_page, end_page)

        if not text:
            print("❌ No text extracted")
            return None

        print(f"  ✓ Extracted {len(text)} characters")

        # Extract images
        images = []
        if extract_images:
            print("📷 Extracting images...")
            images = self.extract_images(start_page, end_page, section_name)

        # Create markdown
        print("📝 Creating markdown file...")
        markdown = self.create_markdown(section_name, text, images, start_page, end_page)

        # Save file
        safe_name = re.sub(r"[^\w\s-]", "", section_name).strip().replace(" ", "_")
        filename = f"{safe_name}_Comprehensive_Guide.md"
        output_path = self.concepts_dir / filename

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(markdown)

        print(f"✅ Created: {output_path}")
        print(f"   Size: {len(markdown)} characters")
        print(f"   Images: {len(images)}")

        return output_path


def main():
    """Main extraction workflow"""
    import argparse

    parser = argparse.ArgumentParser(description="Extract diagnostic sections from Maciocia book")
    parser.add_argument(
        "--pdf",
        default="/home/shuma/Documents/AI_Suite/TCM_Knowledge_Base/Books/Diagnosis in Chinese Medicine A Comprehensive Guide by Giovanni Maciocia [Giovanni Maciocia] (z-lib.org).pdf",
        help="Path to PDF file",
    )
    parser.add_argument(
        "--output", default="/home/shuma/Documents/AI_Suite/TCM_Knowledge_Base", help="Output directory"
    )
    parser.add_argument(
        "--section", choices=["tongue", "pulse", "questioning", "all"], default="all", help="Which section to extract"
    )
    parser.add_argument("--start-page", type=int, help="Override start page")
    parser.add_argument("--end-page", type=int, help="Override end page")
    parser.add_argument("--no-images", action="store_true", help="Skip image extraction")

    args = parser.parse_args()

    # Create extractor
    extractor = DiagnosisExtractor(pdf_path=Path(args.pdf), output_dir=Path(args.output))

    # Define sections to extract
    sections = {"tongue": "Tongue Diagnosis", "pulse": "Pulse Diagnosis", "questioning": "Diagnosis by Questioning"}

    # Extract requested sections
    if args.section == "all":
        for key, name in sections.items():
            extractor.extract_section(
                name, start_page=args.start_page or 0, end_page=args.end_page or 0, extract_images=not args.no_images
            )
    else:
        section_name = sections[args.section]
        extractor.extract_section(
            section_name,
            start_page=args.start_page or 0,
            end_page=args.end_page or 0,
            extract_images=not args.no_images,
        )

    print(f"\n{'=' * 60}")
    print("EXTRACTION COMPLETE")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()
