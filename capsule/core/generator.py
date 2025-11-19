from ..core.researcher import ResearchProvider
from ..core.validator import Validator
import jinja2
from dataclasses import asdict
from typing import List, Dict
import tempfile
import yaml
from pathlib import Path

class ContentGenerator:
    def __init__(self, researcher: ResearchProvider, validator: Validator):
        self.researcher = researcher
        self.validator = validator
        self.template_env = jinja2.Environment(
            loader=jinja2.FileSystemLoader('capsule/templates')
        )

    def _load_template(self, template_name: str) -> jinja2.Template:
        return self.template_env.get_template(template_name)

    def generate(self, topic: str, template_name: str, materials: List[str]) -> Dict[str, str]:
        research_result = self.researcher.research(topic)
        
        generated_content = {}

        if "all" in materials:
            materials = ["flashcards", "quiz", "slides", "conversation", "root_note"]

        with tempfile.TemporaryDirectory() as temp_dir:
            capsule_path = Path(temp_dir)
            
            # Create a mock capsule object with a path attribute
            class MockCapsule:
                def __init__(self, path):
                    self.path = path
            
            mock_capsule = MockCapsule(capsule_path)

            # Create capsule-cypher.yaml
            cypher_data = {
                'capsule_id': 'temp-capsule',
                'name': topic,
                'version': '1.0.0',
                'domain_type': 'education',
                'folder_structure': {'root_notes': 'root_notes'},
                'contents': {'root_notes': []}
            }

            for material in materials:
                try:
                    template = self._load_template(f"{material}.md.j2")
                    rendered_content = template.render(asdict(research_result))
                    
                    # Save the rendered content to a file
                    material_path = capsule_path / 'root_notes'
                    material_path.mkdir(exist_ok=True)
                    file_path = material_path / f"{material}.md"
                    with open(file_path, 'w') as f:
                        f.write(rendered_content)
                    
                    cypher_data['contents']['root_notes'].append({'file': f"root_notes/{material}.md", 'id': f"{material}-1"})
                    generated_content[material] = rendered_content
                except jinja2.TemplateNotFound:
                    print(f"Warning: Template for material '{material}' not found. Skipping.")

            with open(capsule_path / 'capsule-cypher.yaml', 'w') as f:
                yaml.dump(cypher_data, f)

            self.validator.validate_capsule(mock_capsule)

        return generated_content


