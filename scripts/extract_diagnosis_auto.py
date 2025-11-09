#!/usr/bin/env python3
"""
Automatic Diagnosis Section Extractor

Uses PDF metadata (bookmarks/outline) to automatically find and extract sections.
No manual page finding needed!
"""

import os
import re
import subprocess
from pathlib import Path
from typing import List, Tuple, Dict
import fitz  # PyMuPDF


class AutoDiagnosisExtractor:
    """Automatically extract diagnostic sections using PDF metadata"""
    
    def __init__(self, pdf_path: Path, output_dir: Path):
        self.pdf_path = Path(pdf_path)
        self.output_dir = Path(output_dir)
        self.concepts_dir = output_dir / "TCM_Concepts"
        self.concepts_dir.mkdir(exist_ok=True, parents=True)
        
        self.images_dir = output_dir / "images" / "diagnosis"
        self.images_dir.mkdir(exist_ok=True, parents=True)
        
        # Load PDF and TOC
        self.doc = fitz.open(self.pdf_path)
        self.toc = self.doc.get_toc()
        
        print(f"✅ Loaded PDF: {self.pdf_path.name}")
        print(f"   Total pages: {len(self.doc)}")
        print(f"   TOC entries: {len(self.toc)}")
    
    def find_section_pages(self, section_keyword: str) -> Tuple[int, int]:
        """Find section start and end pages from PDF metadata"""
        start_page = None
        end_page = None
        section_level = None
        
        for i, entry in enumerate(self.toc):
            level, title, page = entry
            
            # Check if this is our section
            if section_keyword.lower() in title.lower():
                start_page = page
                section_level = level
                print(f"  ✓ Found: '{title}' at page {page} (level {level})")
                
                # Find end page (next section at same or higher level)
                for j in range(i + 1, len(self.toc)):
                    next_level, next_title, next_page = self.toc[j]
                    if next_level <= section_level:
                        end_page = next_page - 1
                        print(f"  ✓ End page: {end_page} (before '{next_title}')")
                        break
                
                break
        
        if start_page and not end_page:
            # If no end found, go to end of document
            end_page = len(self.doc)
            print(f"  ✓ End page: {end_page} (end of document)")
        
        return start_page or 0, end_page or 0
    
    def get_subsections(self, start_page: int, end_page: int, 
                       parent_level: int) -> List[Tuple[str, int, int]]:
        """Get all subsections within a page range"""
        subsections = []
        
        in_range = False
        current_section = None
        
        for i, entry in enumerate(self.toc):
            level, title, page = entry
            
            # Check if we're in range
            if page == start_page:
                in_range = True
                parent_level = level
            
            if in_range and page <= end_page:
                # Only include subsections (higher level number = deeper)
                if level > parent_level:
                    if current_section:
                        # Close previous subsection
                        subsections.append(current_section + (page - 1,))
                    current_section = (title, page)
                elif level == parent_level and current_section:
                    # Same level, close previous
                    subsections.append(current_section + (page - 1,))
                    current_section = None
            
            if page > end_page:
                break
        
        # Close last subsection
        if current_section:
            subsections.append(current_section + (end_page,))
        
        return subsections
    
    def extract_text(self, start_page: int, end_page: int) -> str:
        """Extract text from page range"""
        try:
            result = subprocess.run(
                [
                    "pdftotext",
                    "-f", str(start_page),
                    "-l", str(end_page),
                    "-layout",
                    str(self.pdf_path),
                    "-"
                ],
                capture_output=True,
                text=True,
                check=True
            )
            return result.stdout
        except subprocess.CalledProcessError as e:
            print(f"❌ Error extracting text: {e}")
            return ""
    
    def extract_images(self, start_page: int, end_page: int, 
                      section_name: str) -> List[str]:
        """Extract images from page range"""
        images = []
        safe_name = re.sub(r'[^\w\s-]', '', section_name).strip().replace(' ', '_')
        
        for page_num in range(start_page - 1, min(end_page, len(self.doc))):
            page = self.doc[page_num]
            image_list = page.get_images()
            
            for img_index, img in enumerate(image_list):
                try:
                    xref = img[0]
                    base_image = self.doc.extract_image(xref)
                    image_bytes = base_image["image"]
                    image_ext = base_image["ext"]
                    
                    image_filename = f"{safe_name}_p{page_num+1}_img{img_index+1}.{image_ext}"
                    image_path = self.images_dir / image_filename
                    
                    with open(image_path, "wb") as img_file:
                        img_file.write(image_bytes)
                    
                    images.append(image_filename)
                    
                except Exception as e:
                    print(f"  ⚠️  Error extracting image: {e}")
        
        return images
    
    def clean_text(self, text: str) -> str:
        """Clean extracted text"""
        # Remove excessive whitespace
        text = re.sub(r'\n{3,}', '\n\n', text)
        
        # Remove page numbers
        text = re.sub(r'\n\s*\d+\s*\n', '\n', text)
        
        # Remove headers/footers
        text = re.sub(r'Diagnosis in Chinese Medicine.*?\n', '', text)
        text = re.sub(r'CHAPTER \d+.*?\n', '', text)
        
        # Fix OCR issues
        text = text.replace('ﬁ', 'fi')
        text = text.replace('ﬂ', 'fl')
        text = text.replace('–', '-')
        text = text.replace('\u2019', "'")
        text = text.replace('\u201c', '"')
        text = text.replace('\u201d', '"')
        
        return text.strip()
    
    def create_markdown(self, section_name: str, text: str, 
                       images: List[str], start_page: int, end_page: int,
                       subsections: List[Tuple[str, int, int]]) -> str:
        """Create comprehensive markdown file"""
        md = f"# {section_name}\n\n"
        
        # Metadata
        md += f"**Source**: Maciocia *Diagnosis in Chinese Medicine* 2nd ed.\n"
        md += f"**Pages**: {start_page}-{end_page}\n"
        md += f"**Extracted**: 2025-11-04\n\n"
        md += "---\n\n"
        
        # Table of contents from subsections
        if subsections:
            md += "## Table of Contents\n\n"
            for i, (title, s_start, s_end) in enumerate(subsections, 1):
                safe_title = re.sub(r'[^\w\s-]', '', title).strip().lower().replace(' ', '-')
                md += f"{i}. [{title}](#{safe_title}) (pp. {s_start}-{s_end})\n"
            md += "\n---\n\n"
        
        # Main content
        md += self.clean_text(text)
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
            md += "- [[Tongue Body Color]]\n"
            md += "- [[Tongue Coating]]\n"
            md += "- [[Tongue Shape]]\n"
        elif "pulse" in section_name.lower():
            md += "- [[Palpation]]\n"
            md += "- [[Pulse Positions]]\n"
            md += "- [[Pulse Qualities]]\n"
            md += "- [[28 Pulses]]\n"
        elif "question" in section_name.lower() or "interrogation" in section_name.lower():
            md += "- [[Patient Interview]]\n"
            md += "- [[Medical History]]\n"
            md += "- [[Ten Questions]]\n"
            md += "- [[Symptom Assessment]]\n"
        
        md += "\n---\n\n"
        md += "*Extracted from Maciocia's Diagnosis in Chinese Medicine for NCCAOM exam preparation.*\n"
        
        return md
    
    def extract_section(self, section_keyword: str, 
                       extract_images: bool = True) -> Path:
        """Extract a complete section automatically"""
        print(f"\n{'='*60}")
        print(f"EXTRACTING: {section_keyword}")
        print(f"{'='*60}")
        
        # Find pages from metadata
        start_page, end_page = self.find_section_pages(section_keyword)
        
        if start_page == 0:
            print(f"❌ Could not find section '{section_keyword}'")
            return None
        
        print(f"📄 Pages: {start_page}-{end_page} ({end_page - start_page + 1} pages)")
        
        # Get subsections
        subsections = self.get_subsections(start_page, end_page, 1)
        print(f"📑 Found {len(subsections)} subsections")
        
        # Extract text
        print(f"📝 Extracting text...")
        text = self.extract_text(start_page, end_page)
        
        if not text:
            print(f"❌ No text extracted")
            return None
        
        print(f"  ✓ Extracted {len(text):,} characters")
        
        # Extract images
        images = []
        if extract_images:
            print(f"📷 Extracting images...")
            images = self.extract_images(start_page, end_page, section_keyword)
            print(f"  ✓ Extracted {len(images)} images")
        
        # Create markdown
        print(f"📝 Creating markdown file...")
        markdown = self.create_markdown(section_keyword, text, images, 
                                       start_page, end_page, subsections)
        
        # Save file
        safe_name = re.sub(r'[^\w\s-]', '', section_keyword).strip().replace(' ', '_')
        filename = f"{safe_name}_Comprehensive_Guide.md"
        output_path = self.concepts_dir / filename
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(markdown)
        
        print(f"✅ Created: {output_path.name}")
        print(f"   Size: {len(markdown):,} characters")
        print(f"   Images: {len(images)}")
        
        return output_path
    
    def list_available_sections(self):
        """List all major sections in the PDF"""
        print("\n" + "="*60)
        print("AVAILABLE SECTIONS")
        print("="*60)
        
        for entry in self.toc:
            level, title, page = entry
            if level <= 2:  # Only show major sections
                indent = "  " * (level - 1)
                print(f"{indent}[Page {page:4d}] {title}")
    
    def close(self):
        """Close PDF document"""
        self.doc.close()


def main():
    """Main extraction workflow"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Automatically extract diagnostic sections from Maciocia book"
    )
    parser.add_argument(
        "--pdf",
        default="/home/shuma/Documents/AI_Suite/TCM_Knowledge_Base/Books/Diagnosis in Chinese Medicine A Comprehensive Guide by Giovanni Maciocia [Giovanni Maciocia] (z-lib.org).pdf",
        help="Path to PDF file"
    )
    parser.add_argument(
        "--output",
        default="/home/shuma/Documents/AI_Suite/TCM_Knowledge_Base",
        help="Output directory"
    )
    parser.add_argument(
        "--section",
        help="Section keyword to extract (e.g., 'Tongue Diagnosis', 'Pulse Diagnosis')"
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="List all available sections"
    )
    parser.add_argument(
        "--no-images",
        action="store_true",
        help="Skip image extraction"
    )
    parser.add_argument(
        "--all-diagnostic",
        action="store_true",
        help="Extract all main diagnostic sections (Tongue, Pulse, Questioning)"
    )
    
    args = parser.parse_args()
    
    # Create extractor
    extractor = AutoDiagnosisExtractor(
        pdf_path=Path(args.pdf),
        output_dir=Path(args.output)
    )
    
    try:
        # List sections if requested
        if args.list:
            extractor.list_available_sections()
            return
        
        # Extract all diagnostic sections
        if args.all_diagnostic:
            sections = [
                "TONGUE DIAGNOSIS",
                "PULSE DIAGNOSIS",
                "THE ART OF INTERROGATION"
            ]
            for section in sections:
                extractor.extract_section(section, extract_images=not args.no_images)
        
        # Extract specific section
        elif args.section:
            extractor.extract_section(args.section, extract_images=not args.no_images)
        
        else:
            print("Please specify --section, --all-diagnostic, or --list")
            parser.print_help()
    
    finally:
        extractor.close()
    
    print(f"\n{'='*60}")
    print("EXTRACTION COMPLETE")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
