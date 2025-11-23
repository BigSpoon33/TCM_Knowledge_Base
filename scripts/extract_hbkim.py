#!/usr/bin/env python3
"""
HB Kim Handbook Interactive Extractor

Extracts pattern differentiation, symptoms, and diagnostic information
from HB Kim's Handbook of Oriental Medicine with human review at each step.

Features:
- Interactive page range selection
- Text extraction with structure preservation
- Vision model fallback for complex tables
- Manual review/editing of each extraction
- Output to symptom/disease templates
"""

import os
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path

import anthropic
import google.generativeai as genai


@dataclass
class Pattern:
    """Represents a TCM pattern extracted from the handbook"""

    name: str
    cam_symptoms: list[str]  # Chinese Acupuncture Medicine column
    fcm_symptoms: list[str]  # Foundations of Chinese Medicine column
    tongue: str
    pulse: str
    key_symptoms: str
    page_number: int
    raw_text: str


class HBKimExtractor:
    """Interactive extractor for HB Kim handbook"""

    def __init__(self, pdf_path: Path, base_dir: Path, vision_provider: str = "auto"):
        self.pdf_path = Path(pdf_path)
        self.base_dir = Path(base_dir)
        self.output_dir = self.base_dir / "extracted_data"
        self.output_dir.mkdir(exist_ok=True)

        # Initialize vision model clients
        self.vision_provider = vision_provider
        self.claude_client = None
        self.gemini_model = None

        # Try Claude
        claude_api_key = os.getenv("ANTHROPIC_API_KEY")
        if claude_api_key:
            self.claude_client = anthropic.Anthropic(api_key=claude_api_key)

        # Try Gemini
        gemini_api_key = os.getenv("GOOGLE_API_KEY")
        if gemini_api_key:
            genai.configure(api_key=gemini_api_key)
            self.gemini_model = genai.GenerativeModel("gemini-1.5-flash")

        # Auto-select provider
        if self.vision_provider == "auto":
            if self.gemini_model:
                self.vision_provider = "gemini"
                print("✅ Using Gemini vision model (faster, cheaper)")
            elif self.claude_client:
                self.vision_provider = "claude"
                print("✅ Using Claude vision model")
            else:
                self.vision_provider = None
                print("⚠️  No vision API keys found")
                print("    Set GOOGLE_API_KEY or ANTHROPIC_API_KEY to enable")

        # Report status
        if not self.gemini_model and not self.claude_client:
            print("⚠️  Vision model extraction disabled")

    def extract_page_range(self, start_page: int, end_page: int) -> str:
        """Extract text from PDF page range"""
        try:
            result = subprocess.run(
                [
                    "pdftotext",
                    "-f",
                    str(start_page),
                    "-l",
                    str(end_page),
                    "-layout",  # Preserve layout
                    str(self.pdf_path),
                    "-",
                ],
                capture_output=True,
                text=True,
                check=True,
            )
            return result.stdout
        except subprocess.CalledProcessError as e:
            print(f"❌ Error extracting pages: {e}")
            return ""

    def convert_page_to_image(self, page_number: int, output_path: Path) -> bool:
        """Convert a single PDF page to PNG image for vision model"""
        try:
            subprocess.run(
                [
                    "convert",
                    "-density",
                    "300",  # High resolution
                    f"{self.pdf_path}[{page_number - 1}]",  # 0-indexed
                    "-quality",
                    "100",
                    str(output_path),
                ],
                check=True,
                capture_output=True,
            )
            return True
        except subprocess.CalledProcessError as e:
            print(f"❌ Error converting page to image: {e}")
            return False

    def parse_pattern_section(self, text: str, page_num: int) -> list[Pattern]:
        """Parse pattern differentiation sections from extracted text"""
        patterns = []

        # Find all pattern headers - they're ALL CAPS lines with specific keywords
        # Match indented or not, with optional (FCM ONLY) or other suffixes
        pattern_regex = r"^\s*([A-Z][A-Z\s\-QLOI]+?(?:DEFICIENCY|STAGNATION|BLAZING|COLLAPSE|HEAT|COLD|WIND|DAMP|PHLEGM|YIN|YANG|QI|BLOOD))(?:\s*\([^)]+\))?\s*$"

        lines = text.split("\n")
        pattern_indices = []

        for i, line in enumerate(lines):
            match = re.match(pattern_regex, line)
            if match:
                pattern_name = match.group(1).strip()
                # Clean up OCR issues
                pattern_name = pattern_name.replace("Ql", "QI").replace("Sl", "SI")
                pattern_indices.append((i, pattern_name))

        # Extract content between pattern headers
        for idx, (line_num, pattern_name) in enumerate(pattern_indices):
            # Get content from this pattern to the next one (or end)
            start = line_num + 1
            if idx + 1 < len(pattern_indices):
                end = pattern_indices[idx + 1][0]
            else:
                end = len(lines)

            content = "\n".join(lines[start:end])

            # Must have either CAM/FCM markers OR tongue/pulse markers
            if not any(marker in content for marker in ["CAM", "FCM", "®", "①", "d)", "KEY SX", "Pale", "Thready"]):
                continue

            # Extract CAM and FCM columns
            cam_symptoms = []
            fcm_symptoms = []
            tongue = ""
            pulse = ""
            key_sx = ""

            # Split by CAM/FCM markers
            if "FCM" in content:
                parts = re.split(r"\bFCM\b", content)
                if len(parts) >= 2:
                    cam_section = parts[0]
                    fcm_section = parts[1]

                    # Extract bullet points from each section
                    cam_symptoms = self._extract_symptoms(cam_section)
                    fcm_symptoms = self._extract_symptoms(fcm_section)

                    # Extract tongue (marked with ① or "d)")
                    tongue_match = re.search(r"[①d]\)?\s*([^\n®]+)", fcm_section)
                    if tongue_match:
                        tongue = tongue_match.group(1).strip()

                    # Extract pulse (marked with ® or "®")
                    pulse_match = re.search(r"®\s*([^\n]+)", fcm_section)
                    if pulse_match:
                        pulse = pulse_match.group(1).strip()

                    # Extract KEY SX
                    key_match = re.search(r"KEY SX:\s*([^\n]+)", fcm_section)
                    if key_match:
                        key_sx = key_match.group(1).strip()

            if cam_symptoms or fcm_symptoms:
                patterns.append(
                    Pattern(
                        name=pattern_name,
                        cam_symptoms=cam_symptoms,
                        fcm_symptoms=fcm_symptoms,
                        tongue=tongue,
                        pulse=pulse,
                        key_symptoms=key_sx,
                        page_number=page_num,
                        raw_text=content[:500],  # First 500 chars for reference
                    )
                )

        return patterns

    def _extract_symptoms(self, text: str) -> list[str]:
        """Extract symptom bullet points from text section"""
        symptoms = []

        # Look for bullet points or line-starting symptoms
        lines = text.split("\n")
        for line in lines:
            line = line.strip()
            # Skip markers and empty lines
            if not line or line.startswith(("CAM", "FCM", "®", "①", "d)", "KEY SX")):
                continue
            # Clean up and add
            if len(line) > 3 and len(line) < 300:
                symptoms.append(line)

        return symptoms

    def extract_with_vision(self, page_number: int, extraction_prompt: str) -> str | None:
        """Use vision model (Gemini or Claude) to extract from page image"""
        if not self.vision_provider:
            print("❌ Vision model not available")
            print("   Set GOOGLE_API_KEY or ANTHROPIC_API_KEY")
            return None

        # Convert page to image
        image_path = self.output_dir / f"page_{page_number}.png"
        print(f"🖼️  Converting page {page_number} to image...")

        if not self.convert_page_to_image(page_number, image_path):
            return None

        try:
            if self.vision_provider == "gemini":
                return self._extract_with_gemini(image_path, extraction_prompt)
            elif self.vision_provider == "claude":
                return self._extract_with_claude(image_path, extraction_prompt)
            else:
                print(f"❌ Unknown vision provider: {self.vision_provider}")
                return None
        finally:
            # Clean up image
            if image_path.exists():
                image_path.unlink()

    def _extract_with_gemini(self, image_path: Path, prompt: str) -> str | None:
        """Extract using Google Gemini vision"""
        print("🤖 Sending to Gemini vision model...")

        try:
            from PIL import Image

            image = Image.open(image_path)

            response = self.gemini_model.generate_content([prompt, image])
            return response.text

        except Exception as e:
            print(f"❌ Gemini error: {e}")
            return None

    def _extract_with_claude(self, image_path: Path, prompt: str) -> str | None:
        """Extract using Claude vision"""
        print("🤖 Sending to Claude vision model...")

        try:
            import base64

            with open(image_path, "rb") as f:
                image_data = base64.standard_b64encode(f.read()).decode("utf-8")

            message = self.claude_client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=4000,
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "image",
                                "source": {
                                    "type": "base64",
                                    "media_type": "image/png",
                                    "data": image_data,
                                },
                            },
                            {"type": "text", "text": prompt},
                        ],
                    }
                ],
            )

            return message.content[0].text

        except Exception as e:
            print(f"❌ Claude error: {e}")
            return None

    def preview_pattern(self, pattern: Pattern) -> str:
        """Generate preview of extracted pattern"""
        preview = f"\n{'=' * 80}\n"
        preview += f"📋 {pattern.name} (Page {pattern.page_number})\n"
        preview += f"{'=' * 80}\n\n"

        preview += "**CAM Symptoms:**\n"
        for sx in pattern.cam_symptoms[:5]:  # Show first 5
            preview += f"  • {sx}\n"
        if len(pattern.cam_symptoms) > 5:
            preview += f"  ... and {len(pattern.cam_symptoms) - 5} more\n"

        preview += "\n**FCM Symptoms:**\n"
        for sx in pattern.fcm_symptoms[:5]:
            preview += f"  • {sx}\n"
        if len(pattern.fcm_symptoms) > 5:
            preview += f"  ... and {len(pattern.fcm_symptoms) - 5} more\n"

        if pattern.tongue:
            preview += f"\n**Tongue:** {pattern.tongue}\n"
        if pattern.pulse:
            preview += f"**Pulse:** {pattern.pulse}\n"
        if pattern.key_symptoms:
            preview += f"\n**KEY SX:** {pattern.key_symptoms}\n"

        return preview

    def pattern_to_markdown(self, pattern: Pattern, template_type: str = "symptom") -> str:
        """Convert pattern to markdown using template structure"""

        if template_type == "symptom":
            # Generate symptom-focused markdown
            md = f"# {pattern.name}\n\n"
            md += "## Pattern Information\n\n"

            md += "### Symptoms (CAM)\n"
            for sx in pattern.cam_symptoms:
                md += f"- {sx}\n"

            md += "\n### Symptoms (FCM - Maciocia)\n"
            for sx in pattern.fcm_symptoms:
                md += f"- {sx}\n"

            md += "\n## Diagnostic Signs\n\n"
            if pattern.tongue:
                md += f"**Tongue:** {pattern.tongue}\n\n"
            if pattern.pulse:
                md += f"**Pulse:** {pattern.pulse}\n\n"
            if pattern.key_symptoms:
                md += f"**Key Symptoms:** {pattern.key_symptoms}\n\n"

            md += f"\n---\n*Extracted from HB Kim Handbook, page {pattern.page_number}*\n"

        return md

    def interactive_session(self):
        """Run interactive extraction session"""
        print("\n" + "=" * 80)
        print("📖 HB KIM HANDBOOK INTERACTIVE EXTRACTOR")
        print("=" * 80)
        print("\nThis tool helps you extract pattern differentiation data")
        print("with human review at each step.\n")

        while True:
            print("\n" + "-" * 80)
            print("OPTIONS:")
            print("  1. Extract page range (text-based)")
            print("  2. Extract single page (vision model)")
            print("  3. View extraction history")
            print("  4. Exit")
            print("-" * 80)

            choice = input("\nChoice (1-4): ").strip()

            if choice == "1":
                self._extract_page_range_interactive()
            elif choice == "2":
                self._extract_page_vision_interactive()
            elif choice == "3":
                self._view_history()
            elif choice == "4":
                print("\n👋 Exiting extractor")
                break
            else:
                print("❌ Invalid choice")

    def _extract_page_range_interactive(self):
        """Interactive page range extraction"""
        print("\n📄 PAGE RANGE EXTRACTION")
        print("-" * 80)

        # Get page range
        start = input("Start page: ").strip()
        end = input("End page: ").strip()

        try:
            start_page = int(start)
            end_page = int(end)
        except ValueError:
            print("❌ Invalid page numbers")
            return

        print(f"\n🔍 Extracting pages {start_page}-{end_page}...")
        text = self.extract_page_range(start_page, end_page)

        if not text:
            print("❌ No text extracted")
            return

        # Parse patterns
        print("🔬 Parsing pattern sections...")
        patterns = self.parse_pattern_section(text, start_page)

        if not patterns:
            print("⚠️  No patterns found")
            print("\nRaw text preview (first 500 chars):")
            print("-" * 80)
            print(text[:500])
            print("-" * 80)

            use_vision = input("\nTry vision model instead? (y/n): ").strip().lower()
            if use_vision == "y":
                for page in range(start_page, end_page + 1):
                    self._extract_single_page_vision(page)
            return

        print(f"\n✅ Found {len(patterns)} patterns")

        # Preview each pattern
        for i, pattern in enumerate(patterns, 1):
            print(self.preview_pattern(pattern))

            action = (
                input(f"\nPattern {i}/{len(patterns)} - (s)ave / (e)dit / (sk)ip / (v)ision / (q)uit: ").strip().lower()
            )

            if action == "s":
                self._save_pattern(pattern)
            elif action == "e":
                self._edit_and_save_pattern(pattern)
            elif action == "v":
                self._extract_single_page_vision(pattern.page_number)
            elif action == "q":
                break
            # skip continues to next

    def _extract_page_vision_interactive(self):
        """Interactive single page vision extraction"""
        print("\n🖼️  VISION MODEL EXTRACTION")
        print("-" * 80)

        page_num = input("Page number: ").strip()
        try:
            page_number = int(page_num)
        except ValueError:
            print("❌ Invalid page number")
            return

        self._extract_single_page_vision(page_number)

    def _extract_single_page_vision(self, page_number: int):
        """Extract single page using vision model"""
        prompt = """Extract all TCM pattern differentiation information from this page.

For each pattern, provide:
1. Pattern name
2. Symptoms (CAM column if present)
3. Symptoms (FCM column if present)
4. Tongue diagnosis
5. Pulse diagnosis
6. Key symptoms

Format as markdown with clear sections. Be precise and include all details."""

        result = self.extract_with_vision(page_number, prompt)

        if result:
            print("\n" + "=" * 80)
            print(f"VISION MODEL EXTRACTION - Page {page_number}")
            print("=" * 80)
            print(result)
            print("=" * 80)

            save = input("\nSave this extraction? (y/n): ").strip().lower()
            if save == "y":
                filename = input("Filename (without .md): ").strip()
                output_path = self.output_dir / f"{filename}.md"
                with open(output_path, "w") as f:
                    f.write(result)
                    f.write(f"\n\n---\n*Extracted from page {page_number} using vision model*\n")
                print(f"✅ Saved to {output_path}")

    def _save_pattern(self, pattern: Pattern):
        """Save pattern to markdown file"""
        filename = pattern.name.lower().replace(" ", "_").replace("-", "_")
        output_path = self.output_dir / f"{filename}.md"

        md = self.pattern_to_markdown(pattern)

        with open(output_path, "w") as f:
            f.write(md)

        print(f"✅ Saved to {output_path}")

    def _edit_and_save_pattern(self, pattern: Pattern):
        """Allow user to edit pattern before saving"""
        print("\n📝 EDIT MODE")
        print("Leave blank to keep current value\n")

        pattern.name = input(f"Name [{pattern.name}]: ").strip() or pattern.name
        pattern.tongue = input(f"Tongue [{pattern.tongue}]: ").strip() or pattern.tongue
        pattern.pulse = input(f"Pulse [{pattern.pulse}]: ").strip() or pattern.pulse
        pattern.key_symptoms = input(f"Key SX [{pattern.key_symptoms}]: ").strip() or pattern.key_symptoms

        self._save_pattern(pattern)

    def _view_history(self):
        """View previously extracted files"""
        files = list(self.output_dir.glob("*.md"))

        if not files:
            print("\n📭 No extractions yet")
            return

        print(f"\n📚 EXTRACTION HISTORY ({len(files)} files)")
        print("-" * 80)
        for f in sorted(files):
            print(f"  • {f.name}")


def main():
    import sys

    base_dir = Path(__file__).parent.parent
    pdf_path = base_dir / "HOM 3rd Ed - HBKim.pdf"

    if not pdf_path.exists():
        print(f"❌ PDF not found: {pdf_path}")
        sys.exit(1)

    extractor = HBKimExtractor(pdf_path, base_dir)
    extractor.interactive_session()


if __name__ == "__main__":
    main()
