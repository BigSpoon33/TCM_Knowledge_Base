import json
from dataclasses import asdict
from datetime import datetime
from pathlib import Path

import jinja2

from ..constants import MATERIAL_CONFIG, TEMPLATES_DIR
from ..core.conversation_generator import ConversationGenerator
from ..core.researcher import ResearchProvider
from ..core.slides_generator import SlidesGenerator
from ..core.template_engine import TemplateEngine
from ..core.validator import Validator
from ..models.research import ResearchResult
from ..utils.file_ops import FileOps
from ..utils.logger import get_logger

logger = get_logger(__name__)


class ContentGenerator:
    def __init__(self, researcher: ResearchProvider, validator: Validator, dry_run: bool = False):
        self.researcher = researcher
        self.validator = validator
        self.dry_run = dry_run
        self.file_ops = FileOps(dry_run=dry_run)
        self.template_env = jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATES_DIR))
        self.template_engine = TemplateEngine()
        self.slides_generator = SlidesGenerator(researcher)
        self.conversation_generator = ConversationGenerator(researcher)

    def _load_template(self, template_name: str) -> jinja2.Template:
        return self.template_env.get_template(template_name)

    def generate(
        self, topic: str, template_name: str, materials: list[str], source_path: Path = None
    ) -> dict[str, str]:
        if source_path and source_path.exists():
            # Read content from source file
            content = self.file_ops.read_text(source_path)

            # Create a pseudo-research result from the file content
            research_result = ResearchResult(content=content, citations=[], metadata={"source_file": str(source_path)})
        else:
            research_result = self.researcher.research(topic)

        generated_content = {}

        if "all" in materials:
            materials = list(MATERIAL_CONFIG.keys())

        # 1. Generate Root Note first (if requested) as it serves as base content
        base_content = research_result.content
        if "root_note" in materials:
            root_note_content = self._generate_root_note(topic, template_name, research_result)
            generated_content["root_note"] = root_note_content
            if root_note_content:
                base_content = root_note_content

        # 2. Generate other materials
        for material in materials:
            if material == "root_note":
                continue  # Already handled

            if material not in MATERIAL_CONFIG:
                logger.warning(f"Unknown material type '{material}'")
                continue

            # Dynamic dispatch to _generate_{material}
            handler_name = f"_generate_{material}"
            if hasattr(self, handler_name):
                try:
                    content = getattr(self, handler_name)(topic, base_content, research_result)
                    if content:
                        generated_content[material] = content
                except Exception as e:
                    logger.error(f"Error generating {material}: {e}", exc_info=True)
            else:
                logger.warning(f"No handler found for material '{material}'")

        return generated_content

    def _generate_root_note(self, topic: str, template_name: str, research_result: ResearchResult) -> str:
        if template_name.endswith(".md"):
            return self._generate_root_note_from_markdown(topic, template_name, research_result.content)
        else:
            # Default Jinja2 handling for root note
            try:
                template = self._load_template(template_name)
                context = asdict(research_result)
                if research_result.metadata:
                    context.update(research_result.metadata)
                context["topic"] = topic
                context["created"] = datetime.now().strftime("%Y-%m-%d")
                return template.render(context)
            except jinja2.TemplateNotFound:
                logger.warning("root_note template not found")
                return ""

    def _generate_slides(self, topic: str, base_content: str, research_result: ResearchResult) -> str:
        # Check if it's a pattern to use specialized generator
        is_pattern = "pattern" in topic.lower() or "deficiency" in topic.lower()
        if is_pattern:
            return self.slides_generator.generate_pattern_slides(base_content, topic)
        else:
            return self.slides_generator.generate_from_content(base_content, topic)

    def _generate_conversation(self, topic: str, base_content: str, research_result: ResearchResult) -> str:
        return self.conversation_generator.generate_script(base_content, topic)

    def _generate_flashcards(self, topic: str, base_content: str, research_result: ResearchResult) -> str:
        template = self._load_template(MATERIAL_CONFIG["flashcards"]["template"])
        context = asdict(research_result)
        context["topic"] = topic
        context["created"] = datetime.now().strftime("%Y-%m-%d")
        context["tags"] = ["capsule", "flashcards"] + [t.strip().lower().replace(" ", "_") for t in topic.split(" ")]

        if "flashcards" not in context:
            context["flashcards"] = self._generate_flashcards_data(base_content)

        context["total_cards"] = len(context.get("flashcards", []))
        return template.render(context)

    def _generate_quiz(self, topic: str, base_content: str, research_result: ResearchResult) -> str:
        template = self._load_template(MATERIAL_CONFIG["quiz"]["template"])
        context = asdict(research_result)
        context["topic"] = topic
        context["created"] = datetime.now().strftime("%Y-%m-%d")
        context["tags"] = ["capsule", "quiz"] + [t.strip().lower().replace(" ", "_") for t in topic.split(" ")]

        if "questions" not in context:
            context["questions"] = self._generate_quiz_data(base_content)

        context["total_questions"] = len(context.get("questions", []))
        return template.render(context)

    def _generate_study_material(self, topic: str, base_content: str, research_result: ResearchResult) -> str:
        return f"# Study Guide for {topic}\n\n*This is an auto-generated study guide based on the root note.*\n\n[[Root_Note_{topic.replace(' ', '_')}]]"

    def _generate_tasks(self, topic: str, base_content: str, research_result: ResearchResult) -> str:
        return f"# Tasks for {topic}\n\n- [ ] Review [[{topic}_Flashcards]]\n- [ ] Take [[{topic}_Quiz]]\n- [ ] Review [[{topic}_Slides]]\n- [ ] Complete [[{topic}_Guided_Conversation]]"

    def _generate_flashcards_data(self, content: str) -> list[dict]:
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
            logger.error(f"Error generating flashcards: {e}", exc_info=True)
            return []

    def _generate_quiz_data(self, content: str) -> list[dict]:
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
            logger.error(f"Error generating quiz: {e}", exc_info=True)
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
