import unittest
from unittest.mock import Mock
from capsule.core.generator import ContentGenerator
from capsule.core.researcher import ResearchProvider, ResearchResult
from capsule.utils.validation import Validator
import os
import shutil

class TestContentGenerator(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory for templates
        self.temp_dir = "temp_templates"
        os.makedirs(self.temp_dir, exist_ok=True)

    def tearDown(self):
        # Remove the temporary directory and its contents
        shutil.rmtree(self.temp_dir)

    def test_constructor(self):
        researcher = Mock(spec=ResearchProvider)
        validator = Mock(spec=Validator)
        generator = ContentGenerator(researcher, validator)
        self.assertIs(generator.researcher, researcher)
        self.assertIs(generator.validator, validator)

    def test_generate(self):
        researcher = Mock(spec=ResearchProvider)
        validator = Mock(spec=Validator)
        
        research_result = ResearchResult(content="Test content", citations=[], metadata={})
        researcher.research.return_value = research_result
        validator = Mock(spec=Validator)
        validator.validate_capsule = Mock(return_value=True)
        
        generator = ContentGenerator(researcher, validator)
        generator.template_env.loader.searchpath = [self.temp_dir]
        
        # Create dummy template files in the temporary directory
        with open(os.path.join(self.temp_dir, "flashcards.md.j2"), "w") as f:
            f.write("flashcard content")
        with open(os.path.join(self.temp_dir, "quiz.md.j2"), "w") as f:
            f.write("quiz content")

        content = generator.generate("test topic", "test_template.md.j2", ["flashcards", "quiz"])
        
        self.assertEqual(content, {"flashcards": "flashcard content", "quiz": "quiz content"})
        researcher.research.assert_called_once_with("test topic")
        # self.assertEqual(validator.validate.call_count, 2)

if __name__ == '__main__':
    unittest.main()
