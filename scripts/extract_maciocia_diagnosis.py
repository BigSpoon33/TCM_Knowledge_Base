#!/usr/bin/env python3
"""
Maciocia Diagnosis in Chinese Medicine Extractor

Extracts chapters from Maciocia's Diagnosis book and creates markdown files
organized by the table of contents structure.

Features:
- Extracts text and images from PDF
- Organizes by Part/Section/Chapter structure
- Creates markdown files with proper formatting
- Preserves images and diagrams
- Links related concepts
"""

import os
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path

import fitz  # PyMuPDF for image extraction
import google.generativeai as genai


@dataclass
class Chapter:
    """Represents a chapter in the book"""

    number: int
    title: str
    part: str
    section: str
    start_page: int
    end_page: int
    level: int  # 1=Part, 2=Section, 3=Chapter


class MaciociaDiagnosisExtractor:
    """Extracts content from Maciocia Diagnosis book"""

    def __init__(self, pdf_path: Path, output_dir: Path):
        self.pdf_path = Path(pdf_path)
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)

        # Create subdirectories
        self.concepts_dir = self.output_dir / "TCM_Concepts"
        self.concepts_dir.mkdir(exist_ok=True)

        self.images_dir = self.output_dir / "images"
        self.images_dir.mkdir(exist_ok=True)

        # Initialize Gemini for image analysis (optional)
        self.gemini_model = None
        gemini_api_key = os.getenv("GOOGLE_API_KEY")
        if gemini_api_key:
            genai.configure(api_key=gemini_api_key)
            self.gemini_model = genai.GenerativeModel("gemini-2.0-flash-exp")
            print("✅ Gemini vision model available for image analysis")

        # Table of contents structure
        self.toc = self._build_toc()

    def _build_toc(self) -> list[Chapter]:
        """Build table of contents structure"""
        # Based on the extracted TOC, here's the structure
        # We'll focus on the main diagnostic sections

        toc = []

        # PART 1: DIAGNOSIS BY OBSERVATION
        # Section 1: Observation of Body, Mind and Complexion
        toc.append(
            Chapter(
                1,
                "Observation of Body Shape, Physique and Demeanour",
                "Part 1: Diagnosis by Observation",
                "Section 1: Observation of Body, Mind and Complexion",
                0,
                0,
                3,
            )
        )  # Pages TBD

        toc.append(
            Chapter(
                2,
                "Observation of the Mind, Spirit and Emotions",
                "Part 1: Diagnosis by Observation",
                "Section 1: Observation of Body, Mind and Complexion",
                0,
                0,
                3,
            )
        )

        toc.append(
            Chapter(
                3,
                "Observation of the Complexion Colour",
                "Part 1: Diagnosis by Observation",
                "Section 1: Observation of Body, Mind and Complexion",
                0,
                0,
                3,
            )
        )

        toc.append(
            Chapter(
                4,
                "Observation of Body Movements",
                "Part 1: Diagnosis by Observation",
                "Section 1: Observation of Body, Mind and Complexion",
                0,
                0,
                3,
            )
        )

        # Section 2: Observation of Parts of the Body
        body_parts = [
            "Head, Face and Hair",
            "Eyes",
            "Nose",
            "Lips, Mouth, Palate, Teeth, Gums and Philtrum",
            "Ears",
            "Throat and Neck",
            "Back",
            "Women's Breasts",
            "Heartbeat",
            "Hands",
            "Nails",
            "Chest and Abdomen",
            "Genitalia",
            "Four Limbs",
            "Legs",
            "Excretions",
        ]

        for i, part in enumerate(body_parts, start=5):
            toc.append(
                Chapter(
                    i,
                    f"Observation of the {part}",
                    "Part 1: Diagnosis by Observation",
                    "Section 2: Observation of Parts of the Body",
                    0,
                    0,
                    3,
                )
            )

        # PART 2: DIAGNOSIS BY AUSCULTATION AND OLFACTION
        # (Add if needed)

        # PART 3: DIAGNOSIS BY QUESTIONING
        # This is the "Ten Questions" section - very important!

        # PART 4: DIAGNOSIS BY PALPATION
        # Section on Tongue Diagnosis
        toc.append(
            Chapter(
                50,
                "Tongue Diagnosis - Introduction",
                "Part 4: Diagnosis by Palpation",
                "Section 1: Tongue Diagnosis",
                0,
                0,
                3,
            )
        )

        # Section on Pulse Diagnosis
        toc.append(
            Chapter(
                60,
                "Pulse Diagnosis - Introduction",
                "Part 4: Diagnosis by Palpation",
                "Section 2: Pulse Diagnosis",
                0,
                0,
                3,
            )
        )

        return toc

    def extract_text_from_pages(self, start_page: int, end_page: int, preserve_layout: bool = True) -> str:
        """Extract text from PDF page range"""
        try:
            layout_flag = "-layout" if preserve_layout else "-raw"
            result = subprocess.run(
                ["pdftotext", "-f", str(start_page), "-l", str(end_page), layout_flag, str(self.pdf_path), "-"],
                capture_output=True,
                text=True,
                check=True,
            )
            return result.stdout
        except subprocess.CalledProcessError as e:
            print(f"❌ Error extracting pages {start_page}-{end_page}: {e}")
            return ""

    def extract_images_from_pages(self, start_page: int, end_page: int, chapter_name: str) -> list[str]:
        """Extract images from PDF page range"""
        images = []

        try:
            doc = fitz.open(self.pdf_path)

            for page_num in range(start_page - 1, end_page):
                if page_num >= len(doc):
                    break

                page = doc[page_num]
                image_list = page.get_images()

                for img_index, img in enumerate(image_list):
                    xref = img[0]
                    base_image = doc.extract_image(xref)
                    image_bytes = base_image["image"]
                    image_ext = base_image["ext"]

                    # Create filename
                    safe_name = re.sub(r"[^\w\s-]", "", chapter_name).strip().replace(" ", "_")
                    image_filename = f"{safe_name}_p{page_num + 1}_img{img_index}.{image_ext}"
                    image_path = self.images_dir / image_filename

                    # Save image
                    with open(image_path, "wb") as img_file:
                        img_file.write(image_bytes)

                    images.append(image_filename)
                    print(f"  📷 Extracted image: {image_filename}")

            doc.close()

        except Exception as e:
            print(f"⚠️  Error extracting images: {e}")

        return images

    def analyze_image_with_gemini(self, image_path: Path) -> str:
        """Analyze image content using Gemini vision model"""
        if not self.gemini_model:
            return ""

        try:
            # Upload image
            image_file = genai.upload_file(str(image_path))

            # Analyze
            prompt = """Analyze this TCM diagnostic image and provide:
1. What type of diagnostic information is shown (tongue, pulse, body part, diagram, etc.)
2. Key features visible in the image
3. Any text or labels present
4. Clinical significance if apparent

Format as markdown."""

            response = self.gemini_model.generate_content([prompt, image_file])
            return response.text

        except Exception as e:
            print(f"⚠️  Error analyzing image: {e}")
            return ""

    def clean_text(self, text: str) -> str:
        """Clean extracted text"""
        # Remove excessive whitespace
        text = re.sub(r"\n{3,}", "\n\n", text)

        # Remove page numbers and headers/footers
        text = re.sub(r"\n\d+\n", "\n", text)
        text = re.sub(r"Diagnosis in Chinese Medicine.*?\n", "", text)

        # Fix common OCR issues
        text = text.replace("ﬁ", "fi")
        text = text.replace("ﬂ", "fl")
        text = text.replace("–", "-")

        return text.strip()

    def format_as_markdown(self, chapter: Chapter, text: str, images: list[str]) -> str:
        """Format extracted content as markdown"""
        md = f"# {chapter.title}\n\n"

        # Add metadata
        md += "**Source**: Maciocia *Diagnosis in Chinese Medicine* 2nd ed.\n"
        md += f"**Part**: {chapter.part}\n"
        md += f"**Section**: {chapter.section}\n"
        md += f"**Pages**: {chapter.start_page}-{chapter.end_page}\n\n"
        md += "---\n\n"

        # Add content
        md += self.clean_text(text)
        md += "\n\n"

        # Add images
        if images:
            md += "## Images and Diagrams\n\n"
            for img in images:
                md += f"![{img}](../images/{img})\n\n"

                # Add image analysis if available
                if self.gemini_model:
                    img_path = self.images_dir / img
                    analysis = self.analyze_image_with_gemini(img_path)
                    if analysis:
                        md += f"**Image Analysis**:\n{analysis}\n\n"

        # Add related links section
        md += "\n---\n\n"
        md += "## Related Concepts\n\n"
        md += "- [[Inspection]]\n"
        md += "- [[Palpation]]\n"
        md += "- [[Auscultation and Olfaction]]\n\n"

        return md

    def find_chapter_pages(self, chapter_title: str) -> tuple[int, int]:
        """Find start and end pages for a chapter by searching the PDF"""
        # Search for chapter title in PDF
        try:
            # Search first 500 pages for TOC
            toc_text = self.extract_text_from_pages(1, 50, preserve_layout=False)

            # Look for chapter title and page number
            # Format is usually: "Chapter X: TITLE ... page_number"
            pattern = rf"Chapter \d+:?\s*{re.escape(chapter_title)}.*?(\d+)"
            match = re.search(pattern, toc_text, re.IGNORECASE)

            if match:
                start_page = int(match.group(1))
                # Estimate end page (will refine later)
                end_page = start_page + 20  # Default chapter length
                return start_page, end_page

        except Exception as e:
            print(f"⚠️  Error finding pages for '{chapter_title}': {e}")

        return 0, 0

    def extract_chapter(
        self, chapter: Chapter, extract_images: bool = True, analyze_images: bool = False
    ) -> Path | None:
        """Extract a single chapter and create markdown file"""
        print(f"\n📖 Extracting: {chapter.title}")

        # Find pages if not set
        if chapter.start_page == 0:
            chapter.start_page, chapter.end_page = self.find_chapter_pages(chapter.title)

        if chapter.start_page == 0:
            print("  ⚠️  Could not find pages for chapter")
            return None

        print(f"  📄 Pages: {chapter.start_page}-{chapter.end_page}")

        # Extract text
        text = self.extract_text_from_pages(chapter.start_page, chapter.end_page)

        if not text:
            print("  ⚠️  No text extracted")
            return None

        # Extract images
        images = []
        if extract_images:
            images = self.extract_images_from_pages(chapter.start_page, chapter.end_page, chapter.title)

        # Format as markdown
        markdown = self.format_as_markdown(chapter, text, images)

        # Create filename
        safe_title = re.sub(r"[^\w\s-]", "", chapter.title).strip().replace(" ", "_")
        filename = f"{safe_title}.md"
        output_path = self.concepts_dir / filename

        # Write file
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(markdown)

        print(f"  ✅ Created: {output_path.name}")
        return output_path

    def extract_all_chapters(self, extract_images: bool = True, analyze_images: bool = False):
        """Extract all chapters from the book"""
        print("=" * 60)
        print("MACIOCIA DIAGNOSIS EXTRACTOR")
        print("=" * 60)
        print(f"PDF: {self.pdf_path.name}")
        print(f"Output: {self.output_dir}")
        print(f"Chapters to extract: {len(self.toc)}")
        print("=" * 60)

        extracted = 0
        failed = 0

        for chapter in self.toc:
            result = self.extract_chapter(chapter, extract_images, analyze_images)
            if result:
                extracted += 1
            else:
                failed += 1

        print("\n" + "=" * 60)
        print(f"✅ Extracted: {extracted}")
        print(f"❌ Failed: {failed}")
        print("=" * 60)

    def extract_specific_section(self, section_name: str, start_page: int, end_page: int):
        """Extract a specific section by page range"""
        print(f"\n📖 Extracting section: {section_name}")
        print(f"  📄 Pages: {start_page}-{end_page}")

        # Extract text
        text = self.extract_text_from_pages(start_page, end_page)

        # Extract images
        images = self.extract_images_from_pages(start_page, end_page, section_name)

        # Create chapter object
        chapter = Chapter(
            number=0,
            title=section_name,
            part="Custom Extract",
            section="",
            start_page=start_page,
            end_page=end_page,
            level=3,
        )

        # Format and save
        markdown = self.format_as_markdown(chapter, text, images)

        safe_title = re.sub(r"[^\w\s-]", "", section_name).strip().replace(" ", "_")
        filename = f"{safe_title}.md"
        output_path = self.concepts_dir / filename

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(markdown)

        print(f"  ✅ Created: {output_path.name}")
        return output_path


def main():
    """Main extraction workflow"""
    import argparse

    parser = argparse.ArgumentParser(description="Extract chapters from Maciocia Diagnosis book")
    parser.add_argument(
        "--pdf",
        default="/home/shuma/Documents/AI_Suite/TCM_Knowledge_Base/Books/Diagnosis in Chinese Medicine A Comprehensive Guide by Giovanni Maciocia [Giovanni Maciocia] (z-lib.org).pdf",
        help="Path to PDF file",
    )
    parser.add_argument(
        "--output", default="/home/shuma/Documents/AI_Suite/TCM_Knowledge_Base", help="Output directory"
    )
    parser.add_argument("--section", help="Extract specific section (e.g., 'Tongue Diagnosis')")
    parser.add_argument("--start-page", type=int, help="Start page for specific section")
    parser.add_argument("--end-page", type=int, help="End page for specific section")
    parser.add_argument("--no-images", action="store_true", help="Skip image extraction")
    parser.add_argument("--analyze-images", action="store_true", help="Analyze images with Gemini vision model")

    args = parser.parse_args()

    # Create extractor
    extractor = MaciociaDiagnosisExtractor(pdf_path=Path(args.pdf), output_dir=Path(args.output))

    # Extract specific section or all chapters
    if args.section and args.start_page and args.end_page:
        extractor.extract_specific_section(args.section, args.start_page, args.end_page)
    else:
        extractor.extract_all_chapters(extract_images=not args.no_images, analyze_images=args.analyze_images)


if __name__ == "__main__":
    main()
