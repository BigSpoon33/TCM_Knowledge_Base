from ..core.researcher import ResearchProvider
from ..core.validator import Validator
from ..core.template_engine import TemplateEngine
from ..core.slides_generator import SlidesGenerator
from ..core.conversation_generator import ConversationGenerator
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
        self.slides_generator = SlidesGenerator(researcher)
        self.conversation_generator = ConversationGenerator(researcher)

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
            materials = ["flashcards", "quiz", "slides", "conversation", "study_material", "tasks", "root_note"]

        # Create a temporary directory for validation, but we will return content to be saved by the CLI
        # Actually, the CLI expects us to return a dict of content, but now we want to manage folders.
        # The CLI's generate command handles saving, but it saves flatly.
        # We need to change the CLI to respect the folder structure or handle saving here.
        # Given the current architecture, the CLI iterates over the returned dict and saves files.
        # We can return keys with paths like "Topic/File.md" to hint structure,
        # OR we can update the CLI to create the folder.

        # Let's stick to returning content and let the CLI handle saving,
        # BUT we will update the CLI to create the topic folder.

        # Wait, the user wants a specific folder structure: Materials/Topic_Name/
        # The CLI currently takes an --output dir.
        # If we return keys like "Topic_Name/Flashcards_Topic.md", the CLI might fail if it just joins paths.

        # Let's generate the content first.

        # 1. Root Note
        root_note_content = ""
        if "root_note" in materials:
            if template_name.endswith(".md"):
                root_note_content = self._generate_root_note_from_markdown(
                    topic, template_name, research_result.content
                )
            else:
                # Default Jinja2 handling for root note
                try:
                    template = self._load_template(f"root_note.md.j2")
                    context = asdict(research_result)
                    if research_result.metadata:
                        context.update(research_result.metadata)
                    context["topic"] = topic
                    context["created"] = datetime.now().strftime("%Y-%m-%d")
                    root_note_content = template.render(context)
                except jinja2.TemplateNotFound:
                    print("Warning: root_note template not found.")

            generated_content["root_note"] = root_note_content

        # Use root note content for other materials if available, otherwise research content
        base_content = root_note_content if root_note_content else research_result.content

        # 2. Slides
        if "slides" in materials:
            # Check if it's a pattern to use specialized generator
            is_pattern = "pattern" in topic.lower() or "deficiency" in topic.lower()
            if is_pattern:
                generated_content["slides"] = self.slides_generator.generate_pattern_slides(base_content, topic)
            else:
                generated_content["slides"] = self.slides_generator.generate_from_content(base_content, topic)

        # 3. Conversation
        if "conversation" in materials:
            generated_content["conversation"] = self.conversation_generator.generate_script(base_content, topic)

        # 4. Flashcards
        if "flashcards" in materials:
            try:
                template = self._load_template("flashcards.md.j2")
                context = asdict(research_result)
                context["topic"] = topic
                context["created"] = datetime.now().strftime("%Y-%m-%d")
                context["tags"] = ["capsule", "flashcards"] + [
                    t.strip().lower().replace(" ", "_") for t in topic.split(" ")
                ]

                if "flashcards" not in context:
                    context["flashcards"] = self._generate_flashcards_data(base_content)

                context["total_cards"] = len(context.get("flashcards", []))
                generated_content["flashcards"] = template.render(context)
            except Exception as e:
                print(f"Error generating flashcards: {e}")

        # 5. Quiz
        if "quiz" in materials:
            try:
                template = self._load_template("quiz.md.j2")
                context = asdict(research_result)
                context["topic"] = topic
                context["created"] = datetime.now().strftime("%Y-%m-%d")
                context["tags"] = ["capsule", "quiz"] + [t.strip().lower().replace(" ", "_") for t in topic.split(" ")]

                if "questions" not in context:
                    context["questions"] = self._generate_quiz_data(base_content)

                context["total_questions"] = len(context.get("questions", []))
                generated_content["quiz"] = template.render(context)
            except Exception as e:
                print(f"Error generating quiz: {e}")

        # 6. Study Material
        if "study_material" in materials:
            generated_content["study_material"] = (
                f"# Study Guide for {topic}\n\n*This is an auto-generated study guide based on the root note.*\n\n[[Root_Note_{topic.replace(' ', '_')}]]"
            )

        # 7. Tasks
        if "tasks" in materials:
            generated_content["tasks"] = (
                f"# Tasks for {topic}\n\n- [ ] Review [[{topic}_Flashcards]]\n- [ ] Take [[{topic}_Quiz]]\n- [ ] Review [[{topic}_Slides]]\n- [ ] Complete [[{topic}_Guided_Conversation]]"
            )

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
