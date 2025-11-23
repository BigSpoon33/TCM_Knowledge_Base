#!/usr/bin/env python3
"""
Deep Research Pipeline - Complete workflow from research to OCDS materials.

This is the main orchestrator that coordinates:
1. AI-powered research prompt generation
2. Deep research using Gemini
3. Template parsing
4. Content generation per heading
5. Template filling
6. Frontmatter validation
7. Materials generation (flashcards, quiz, etc.)
8. Packaging

Usage:
    python deep_research_pipeline.py \\
      --topic "Spleen Qi Deficiency" \\
      --project "Traditional Chinese Medicine" \\
      --template "Root_Note_Template.md" \\
      --class-id "TCM_101"
"""

import argparse
import os
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from content_generator import ContentGenerator
from gemini_research import GeminiDeepResearch
from generate_all_materials import MaterialsPackageGenerator
from research_prompt_generator import ResearchPromptGenerator
from template_filler import TemplateFiller
from template_parser import TemplateParser


class DeepResearchPipeline:
    """Complete pipeline from research to OCDS materials."""

    def __init__(self, api_key: str = None):
        """
        Initialize pipeline.

        Args:
            api_key: Gemini API key (uses GEMINI_API_KEY env var if None)
        """
        self.api_key = api_key or os.environ.get("GEMINI_API_KEY")

        if not self.api_key:
            raise ValueError(
                "Gemini API key required. Set GEMINI_API_KEY environment variable or pass api_key parameter."
            )

        # Initialize components
        self.prompt_generator = ResearchPromptGenerator(api_key=self.api_key)
        self.researcher = GeminiDeepResearch(api_key=self.api_key)
        self.content_generator = ContentGenerator(api_key=self.api_key)
        self.template_filler = TemplateFiller()
        self.template_parser = TemplateParser()

        # Results storage
        self.results = {
            "research_prompt": None,
            "research_context": None,
            "generated_sections": None,
            "root_note_path": None,
            "materials_paths": {},
        }

    def run(
        self,
        topic: str,
        project: str,
        template_path: Path,
        class_id: str = None,
        output_dir: Path = None,
        depth: str = "comprehensive",
        generate_prompt: bool = True,
        skip_materials: bool = False,
    ) -> dict:
        """
        Run complete pipeline.

        Args:
            topic: "Spleen Qi Deficiency"
            project: "Traditional Chinese Medicine"
            template_path: Path to template file
            class_id: Class ID for materials (e.g., "TCM_101")
            output_dir: Where to save outputs
            depth: Research depth ('quick', 'comprehensive', 'exhaustive')
            generate_prompt: Use AI to generate research prompt
            skip_materials: Skip material generation (only create root note)

        Returns:
            Results dict with paths to all generated files
        """
        print("\n" + "=" * 70)
        print("🔬 DEEP RESEARCH TO MATERIALS PIPELINE")
        print("=" * 70)
        print(f"\n📘 Topic: {topic}")
        print(f"📚 Project: {project}")
        print(f"📋 Template: {template_path.name}")
        print(f"🏫 Class ID: {class_id or 'Auto-generated'}")
        print(f"📊 Depth: {depth}")
        print("\n" + "=" * 70 + "\n")

        # Set up output directory
        if not output_dir:
            base_dir = Path(__file__).parent.parent / "Materials"
            if class_id:
                output_dir = base_dir / class_id
            else:
                output_dir = base_dir / f"{project.replace(' ', '_')}_{topic.replace(' ', '_')}"

        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

        # STEP 0: Generate research prompt (optional)
        if generate_prompt:
            research_prompt = self._step0_generate_prompt(topic, project, template_path)
        else:
            research_prompt = None

        # STEP 1: Deep research
        research_context = self._step1_deep_research(topic, project, depth, custom_prompt=research_prompt)

        # STEP 2: Parse template
        template_data = self._step2_parse_template(template_path)

        # STEP 3: Generate content per heading
        sections = self._step3_generate_content(template_data["headings"], topic, project, research_context)

        # STEP 4: Fill template
        root_note_content = self._step4_fill_template(template_path, sections, topic, project)

        # STEP 5: Save root note
        root_note_path = self._step5_save_root_note(root_note_content, topic, output_dir)

        # STEP 6: Generate materials (optional)
        if not skip_materials:
            materials_paths = self._step6_generate_materials(root_note_path, class_id, output_dir)
        else:
            materials_paths = {}

        # STEP 7: Summary
        self._step7_summary(root_note_path, materials_paths, output_dir)

        return self.results

    def _step0_generate_prompt(self, topic: str, project: str, template_path: Path) -> str:
        """Step 0: Generate optimal research prompt using AI."""
        print("🎯 STEP 0: Generating Research Prompt (AI)")
        print("-" * 70)

        research_prompt = self.prompt_generator.generate_prompt(
            topic=topic, project=project, template_path=template_path
        )

        self.results["research_prompt"] = research_prompt

        print("✅ Research prompt generated\n")
        return research_prompt

    def _step1_deep_research(self, topic: str, project: str, depth: str, custom_prompt: str = None) -> str:
        """Step 1: Conduct deep research."""
        print("🔬 STEP 1: Deep Research")
        print("-" * 70)

        if custom_prompt:
            # Use custom AI-generated prompt
            result = self.researcher.research(custom_prompt, use_search=True)
            research_context = result["content"]
        else:
            # Use standard deep research
            result = self.researcher.deep_research(topic, project, depth)
            research_context = result["content"]

        self.results["research_context"] = research_context

        print(f"✅ Research complete ({len(research_context)} characters)\n")
        return research_context

    def _step2_parse_template(self, template_path: Path) -> dict:
        """Step 2: Parse template structure."""
        print("📋 STEP 2: Parse Template")
        print("-" * 70)

        template_data = self.template_parser.parse(template_path)

        headings_count = len(self.template_parser._flatten_headings(template_data["headings"]))
        print(f"✅ Template parsed ({headings_count} headings)\n")

        return template_data

    def _step3_generate_content(self, headings: list, topic: str, project: str, context: str) -> dict:
        """Step 3: Generate content for each heading."""
        print("✍️  STEP 3: Generate Content (Per Heading)")
        print("-" * 70)

        sections = self.content_generator.generate_all_sections(
            headings=headings, topic=topic, project=project, context=context
        )

        self.results["generated_sections"] = sections

        print("\n✅ All sections generated\n")
        return sections

    def _step4_fill_template(self, template_path: Path, sections: dict, topic: str, project: str) -> str:
        """Step 4: Fill template with generated content."""
        print("🔧 STEP 4: Fill Template")
        print("-" * 70)

        content = self.template_filler.fill(
            template_path=template_path, sections=sections, topic=topic, project=project
        )

        # Validate
        validation = self.template_filler.validate()

        if not validation["valid"]:
            print("⚠️  Validation warnings:")
            for warning in validation["warnings"]:
                print(f"   - {warning}")

        print("✅ Template filled\n")
        return content

    def _step5_save_root_note(self, content: str, topic: str, output_dir: Path) -> Path:
        """Step 5: Save root note."""
        print("💾 STEP 5: Save Root Note")
        print("-" * 70)

        # Create filename
        filename = f"Root_Note_{topic.replace(' ', '_')}.md"
        root_note_path = output_dir / filename

        # Save
        with open(root_note_path, "w", encoding="utf-8") as f:
            f.write(content)

        self.results["root_note_path"] = root_note_path

        print(f"✅ Root note saved: {root_note_path}\n")
        return root_note_path

    def _step6_generate_materials(self, root_note_path: Path, class_id: str, output_dir: Path) -> dict:
        """Step 6: Generate OCDS materials."""
        print("📚 STEP 6: Generate Materials")
        print("-" * 70)

        # Use existing materials generator
        generator = MaterialsPackageGenerator(
            root_note_path=root_note_path, class_id=class_id, output_dir=output_dir, api_key=self.api_key
        )

        generator.generate_all()

        materials_paths = {
            "flashcards": output_dir / "Flashcards.md",
            "quiz": output_dir / "Quiz.md",
            "slides": output_dir / "Slides.md",
            "study_material": output_dir / "Study_Material.md",
            "tasks": output_dir / "Tasks.md",
        }

        self.results["materials_paths"] = materials_paths

        print("\n✅ Materials generated\n")
        return materials_paths

    def _step7_summary(self, root_note_path: Path, materials_paths: dict, output_dir: Path):
        """Step 7: Print summary."""
        print("=" * 70)
        print("📊 PIPELINE COMPLETE")
        print("=" * 70)

        print(f"\n📁 Output Directory: {output_dir}")
        print(f"\n📘 Root Note: {root_note_path.name}")

        if materials_paths:
            print("\n📚 Generated Materials:")
            for material_type, path in materials_paths.items():
                if path.exists():
                    print(f"   ✅ {material_type.replace('_', ' ').title()}: {path.name}")

        print(f"\n{'=' * 70}")
        print("✅ Complete OCDS class package ready!")
        print("=" * 70)

        print("\n💡 Next steps:")
        print(f"   1. Review root note: {root_note_path}")
        print(f"   2. Check generated materials in: {output_dir}")
        print("   3. Add to Student Dashboard")
        print("   4. Test with OCDS system\n")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Deep Research to OCDS Materials Pipeline",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Basic usage
  python deep_research_pipeline.py \\
    --topic "Spleen Qi Deficiency" \\
    --project "Traditional Chinese Medicine" \\
    --template "Root_Note_Template.md" \\
    --class-id "TCM_101"
  
  # With custom output directory
  python deep_research_pipeline.py \\
    --topic "Photosynthesis" \\
    --project "Biology" \\
    --template "Biology_Template.md" \\
    --class-id "BIO_101" \\
    --output-dir "Materials/BIO_101/Week_03"
  
  # Exhaustive research, skip materials
  python deep_research_pipeline.py \\
    --topic "Spleen Qi Deficiency" \\
    --project "Traditional Chinese Medicine" \\
    --template "Root_Note_Template.md" \\
    --depth exhaustive \\
    --skip-materials
        """,
    )

    parser.add_argument("--topic", required=True, help="Research topic")
    parser.add_argument("--project", required=True, help="Project/domain context")
    parser.add_argument("--template", required=True, help="Template file path")
    parser.add_argument("--class-id", help="Class ID (e.g., TCM_101)")
    parser.add_argument("--output-dir", help="Output directory")
    parser.add_argument(
        "--depth", default="comprehensive", choices=["quick", "comprehensive", "exhaustive"], help="Research depth"
    )
    parser.add_argument("--no-prompt-generation", action="store_true", help="Skip AI prompt generation")
    parser.add_argument(
        "--skip-materials", action="store_true", help="Skip material generation (only create root note)"
    )

    args = parser.parse_args()

    # Check for API key
    if not os.environ.get("GEMINI_API_KEY"):
        print("❌ Error: GEMINI_API_KEY environment variable not set")
        print("\nSet it with:")
        print("  export GEMINI_API_KEY='your-api-key-here'")
        sys.exit(1)

    # Initialize pipeline
    pipeline = DeepResearchPipeline()

    # Run pipeline
    try:
        results = pipeline.run(
            topic=args.topic,
            project=args.project,
            template_path=Path(args.template),
            class_id=args.class_id,
            output_dir=Path(args.output_dir) if args.output_dir else None,
            depth=args.depth,
            generate_prompt=not args.no_prompt_generation,
            skip_materials=args.skip_materials,
        )

        sys.exit(0)

    except Exception as e:
        print(f"\n❌ Pipeline error: {e}")
        import traceback

        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
