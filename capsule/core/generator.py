from ..core.researcher import ResearchProvider
from ..core.validator import Validator
from ..core.template_engine import TemplateEngine
from ..models.research import ResearchResult
import jinja2
import json
from dataclasses import asdict
from typing import List, Dict
import tempfile
import yaml
from pathlib import Path
from datetime import datetime
from ..constants import TEMPLATES_DIR
from ..models.capsule import Capsule


class ContentGenerator:
    def __init__(self, researcher: ResearchProvider, validator: Validator):
        self.researcher = researcher
        self.validator = validator
        self.template_env = jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATES_DIR))
        self.template_engine = TemplateEngine()

    def _load_template(self, template_name: str) -> jinja2.Template:
        return self.template_env.get_template(template_name)

    def generate(
        self, topic: str, template_name: str, materials: List[str], source_path: Path = None
    ) -> Dict[str, str]:
        if source_path and source_path.exists():
            # Read content from source file
            with open(source_path, "r", encoding="utf-8") as f:
                content = f.read()

            # Create a pseudo-research result from the file content
            research_result = ResearchResult(content=content, citations=[], metadata={"source_file": str(source_path)})
        else:
            research_result = self.researcher.research(topic)

        generated_content = {}

        if "all" in materials:
            materials = ["flashcards", "quiz", "slides", "conversation", "root_note"]

        with tempfile.TemporaryDirectory() as temp_dir:
            capsule_path = Path(temp_dir)

            # Create capsule-cypher.yaml
            cypher_data = {
                "capsule_id": "temp-capsule",
                "name": topic,
                "version": "1.0.0",
                "domain_type": "education",
                "folder_structure": {"root_notes": "root_notes"},
                "contents": {"root_notes": []},
            }

            for material in materials:
                try:
                    # Special handling for root_note if a custom markdown template is provided
                    # For now, we assume template_name passed to generate() is for the root note
                    # if it ends in .md (not .j2) and we are processing 'root_note'
                    if material == "root_note" and template_name.endswith(".md"):
                        # If source_path is provided, we probably shouldn't regenerate the root note
                        # unless explicitly requested. For now, let's assume if they asked for it, they want it.
                        # But if source_path IS the root note, regenerating it from itself is weird unless it's "enhancement".
                        rendered_content = self._generate_root_note_from_markdown(
                            topic, template_name, research_result.content
                        )
                    else:
                        # Default Jinja2 handling
                        template = self._load_template(f"{material}.md.j2")
                        context = asdict(research_result)
                        # Unpack metadata into context so templates can access fields like 'question', 'answer', etc.
                        if research_result.metadata:
                            context.update(research_result.metadata)

                        context["topic"] = topic
                        context["created"] = datetime.now().strftime("%Y-%m-%d")
                        # Generate simple tags
                        context["tags"] = ["capsule", material] + [
                            t.strip().lower().replace(" ", "_") for t in topic.split(" ")
                        ]

                        # Generate structured data if missing (e.g. when using source_path or standard research)
                        if material == "flashcards" and "flashcards" not in context:
                            context["flashcards"] = self._generate_flashcards_data(research_result.content)

                        if material == "quiz" and "questions" not in context:
                            context["questions"] = self._generate_quiz_data(research_result.content)

                        if "flashcards" in context:
                            context["total_cards"] = len(context["flashcards"])

                        if "questions" in context:
                            context["total_questions"] = len(context["questions"])

                        rendered_content = template.render(context)

                    # Save the rendered content to a file
                    material_path = capsule_path / "root_notes"
                    material_path.mkdir(exist_ok=True)
                    file_path = material_path / f"{material}.md"
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(rendered_content)

                    cypher_data["contents"]["root_notes"].append(
                        {"file": f"root_notes/{material}.md", "id": f"{material}-1"}
                    )
                    generated_content[material] = rendered_content
                except jinja2.TemplateNotFound:
                    print(f"Warning: Template for material '{material}' not found. Skipping.")
                except FileNotFoundError:
                    print(f"Warning: Markdown template '{template_name}' not found. Skipping root_note.")

            with open(capsule_path / "capsule-cypher.yaml", "w") as f:
                yaml.dump(cypher_data, f)

            validator = Validator(capsule_path)
            validator.validate_capsule()

        return generated_content

    def _generate_flashcards_data(self, content: str) -> List[Dict]:
        """Generates flashcard data from content using LLM."""
        prompt = f"""
        Create 5 flashcards based on the following text.
        Return ONLY valid JSON in the format:
        [
            {{"front": "Question", "back": "Answer"}}
        ]
        
        Text:
        {content[:4000]}
        """
        try:
            response = self.researcher.generate_content(prompt)
            # Clean up response if it contains markdown code blocks
            response = response.replace("```json", "").replace("```", "").strip()
            return json.loads(response)
        except Exception as e:
            print(f"Error generating flashcards: {e}")
            return []

    def _generate_quiz_data(self, content: str) -> List[Dict]:
        """Generates quiz data from content using LLM."""
        prompt = f"""
        Create 5 multiple choice questions based on the following text.
        Return ONLY valid JSON in the format:
        [
            {{
                "text": "Question text",
                "options": ["Option A", "Option B", "Option C", "Option D"],
                "correct_answer": "Option A",
                "explanation": "Explanation here"
            }}
        ]
        
        Text:
        {content[:4000]}
        """
        try:
            response = self.researcher.generate_content(prompt)
            # Clean up response if it contains markdown code blocks
            response = response.replace("```json", "").replace("```", "").strip()
            return json.loads(response)
        except Exception as e:
            print(f"Error generating quiz: {e}")
            return []

    def _generate_root_note_from_markdown(self, topic: str, template_path_str: str, context_text: str) -> str:
        """
        Generates a root note by parsing a markdown template and filling sections using AI.
        """
        template_path = Path(template_path_str)
        if not template_path.exists():
            # Try looking in TEMPLATES_DIR if absolute path fails
            template_path = Path(TEMPLATES_DIR) / template_path_str

        parsed_template = self.template_engine.parse(template_path)
        headings = parsed_template["headings"]

        sections = {}

        # Flatten headings to process them linearly
        flat_headings = []

        def flatten(node_list):
            for node in node_list:
                flat_headings.append(node)
                flatten(node["children"])

        flatten(headings)

        for heading in flat_headings:
            heading_text = heading["clean_text"]
            # Skip if it's just a container heading with no content expected?
            # For now, generate for all.

            prompt = f"""
            Write comprehensive content for the section "{heading_text}" about "{topic}".
            
            Use this research context:
            {context_text[:4000]}
            
            Requirements:
            - Write in clear, educational language
            - Use markdown formatting
            - Do NOT include the heading itself
            """

            content = self.researcher.generate_content(prompt)
            sections[heading_text] = content.strip()

        return self.template_engine.fill(sections, topic, {"domain": "Education"})
