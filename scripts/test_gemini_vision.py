#!/usr/bin/env python3
"""
Quick test script to verify Gemini vision extraction works
"""

import os
from pathlib import Path

from extract_hbkim import HBKimExtractor


def test_gemini():
    """Test Gemini vision on a single page"""

    # Check for API key
    if not os.getenv("GOOGLE_API_KEY"):
        print("❌ GOOGLE_API_KEY not set")
        print("   Get your key from: https://aistudio.google.com/app/apikey")
        print("   Then run: export GOOGLE_API_KEY='your-key'")
        return

    base_dir = Path(__file__).parent.parent
    pdf_path = base_dir / "HOM 3rd Ed - HBKim.pdf"

    if not pdf_path.exists():
        print(f"❌ PDF not found: {pdf_path}")
        return

    print("=" * 80)
    print("GEMINI VISION TEST")
    print("=" * 80)
    print("\nTesting extraction on page 100 (Heart QI Deficiency section)")
    print("\nThis will:")
    print("  1. Convert PDF page to image")
    print("  2. Send to Gemini vision model")
    print("  3. Extract pattern differentiation data")
    print("=" * 80)

    extractor = HBKimExtractor(pdf_path, base_dir, vision_provider="gemini")

    if not extractor.gemini_model:
        print("\n❌ Gemini model not initialized")
        return

    prompt = """Extract all TCM pattern differentiation information from this page.

For each pattern, provide:
1. Pattern name (e.g., HEART QI DEFICIENCY)
2. Symptoms from CAM column (if present)
3. Symptoms from FCM column (if present)
4. Tongue diagnosis (marked with ① or d))
5. Pulse diagnosis (marked with ®)
6. Key symptoms (marked with KEY SX)

Format as clear markdown with sections for each pattern.
Be precise and include all symptom details."""

    print("\n🚀 Starting extraction...")
    result = extractor.extract_with_vision(100, prompt)

    if result:
        print("\n" + "=" * 80)
        print("✅ EXTRACTION SUCCESSFUL")
        print("=" * 80)
        print(result)
        print("=" * 80)
        print("\n✅ Test complete! Gemini vision is working.")
        print("   You can now use the full extractor with vision mode.")
    else:
        print("\n❌ Extraction failed")


if __name__ == "__main__":
    test_gemini()
