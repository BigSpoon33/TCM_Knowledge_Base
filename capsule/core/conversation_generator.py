import re
from typing import List, Dict, Any
from ..core.researcher import ResearchProvider
from ..core.template_engine import TemplateEngine


class ConversationGenerator:
    """Generates guided conversation scripts from root note content."""

    def __init__(self, researcher: ResearchProvider):
        self.researcher = researcher
        self.template_engine = TemplateEngine()

    def generate_script(self, content: str, topic: str) -> str:
        """
        Generate a markdown conversation script.
        """
        # Parse content to get headings
        # We use a temporary file approach or modify TemplateEngine to accept string content
        # Since TemplateEngine currently takes a path, let's just extract headings manually here
        # or refactor TemplateEngine. For now, manual extraction is safer/faster.

        headings = self._extract_headings(content)

        script_content = f"""---
ocds_type: guided_conversation
material_id: conversation_{topic.lower().replace(" ", "_")}
title: "{topic} - Guided Learning Conversation"
topic: {topic}
total_headings: {len(headings)}
estimated_time: {len(headings) * 5}-{len(headings) * 8} minutes
---

# {topic} - Guided Learning Conversation

## How to Use This Guide

This guided conversation will help you master {topic} through active recall and discussion. Work through each section, testing your knowledge before reviewing the content.

**Instructions:**
1. Read each question carefully
2. Answer in your own words before looking at the reference content
3. Compare your answer to the key concepts
4. If you're missing concepts, review the explanation and try again

---

"""

        for i, heading in enumerate(headings):
            question = self._generate_initial_prompt(heading["title"], heading["content"])
            key_concepts = self._extract_key_concepts(heading["content"])

            script_content += f"""
## {i + 1}. {heading["title"]}

**Question:**
{question}

**Key Concepts to Cover:**
{key_concepts}

**Assessment Criteria:**
- Can you explain the main concepts clearly?
- Can you provide clinical examples?
- Can you relate this to other concepts?

**Reference Content:**
{heading["content"][:500]}...

---

"""
        return script_content

    def _extract_headings(self, content: str) -> List[Dict[str, str]]:
        """Extract headings and their content from markdown."""
        headings = []
        lines = content.split("\n")
        current_heading = None
        current_content = []

        for line in lines:
            match = re.match(r"^(#{1,3})\s+(.+)$", line)
            if match:
                if current_heading:
                    headings.append({"title": current_heading, "content": "\n".join(current_content).strip()})
                current_heading = match.group(2).strip()
                current_content = []
            else:
                if current_heading:
                    current_content.append(line)

        # Add last heading
        if current_heading:
            headings.append({"title": current_heading, "content": "\n".join(current_content).strip()})

        return headings

    def _generate_initial_prompt(self, heading_title: str, content: str) -> str:
        """Generate opening question for a heading."""
        # Use predefined templates for common headings
        templates = {
            "Overview": "What do you know about {topic}?",
            "Clinical Manifestations": "What are the cardinal symptoms and diagnostic features of {topic}?",
            "Etiology": "What causes {topic} and how does it develop?",
            "Differential Diagnosis": "How would you distinguish {topic} from similar patterns?",
            "Treatment Principles": "What are the main treatment principles for {topic}?",
            "Formulas": "What are the key herbal formulas used for {topic}?",
            "Acupuncture": "Which acupuncture points would you use for {topic}?",
            "Applications": "How would you apply your knowledge of {topic} in clinical practice?",
            "Study Tips": "What strategies would help you remember the key concepts of {topic}?",
        }

        for template_key, template in templates.items():
            if template_key.lower() in heading_title.lower():
                return template.format(topic=heading_title)

        # Generate custom prompt using AI
        prompt = f"""
        Generate a clear, open-ended question to test a TCM student's understanding of this topic.

        HEADING: {heading_title}

        CONTENT PREVIEW:
        {content[:500]}

        The question should:
        1. Be open-ended (not yes/no)
        2. Encourage the student to explain in their own words
        3. Cover the main concepts in this section
        4. Be appropriate for a TCM student
        5. Be concise (one sentence)

        Return ONLY the question, no other text.
        """
        return self.researcher.generate_content(prompt).strip()

    def _extract_key_concepts(self, content: str) -> str:
        """Extract key concepts from content."""
        lines = content.split("\n")
        concepts = []
        for line in lines[:15]:
            if line.strip().startswith("*") or line.strip().startswith("-"):
                concepts.append(line.strip())

        if concepts:
            return "\n".join(concepts[:5])
        else:
            return "- Review the main points in this section"
