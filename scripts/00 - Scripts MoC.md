# Scripts Map of Content

This document provides an overview of all scripts in the TCM Knowledge Base automation system.

---

## Data Extraction Scripts

### extract_herb_bensky.py
**Purpose:** Extracts herb information from Bensky's Materia Medica PDF and creates markdown files for each herb.

**How to Use:**
```bash
python scripts/extract_herb_bensky.py --pdf "Books/Bensky - Materia Medica.pdf" --herb "Huang Qi" --start-page 100 --end-page 105
```

**What it does:**
- Opens Bensky Materia Medica PDF
- Extracts text from specified page ranges
- Parses herb properties (temperature, flavor, channels, actions)
- Creates formatted markdown files in TCM_Herbs/

---

### extract_herbs_bensky.py
**Purpose:** Batch extraction of multiple herbs from Bensky's Materia Medica.

**How to Use:**
```bash
python scripts/extract_herbs_bensky.py --pdf "Books/Bensky - Materia Medica.pdf" --herbs-json "all_bensky_herbs.json"
```

**What it does:**
- Processes multiple herbs from a JSON configuration file
- Automates the extraction process for entire herb categories
- Creates markdown files for all specified herbs

---

### extract_formulas_bensky_ocr.py
**Purpose:** Extracts formula information from scanned Bensky Formulas & Strategies PDF using OCR.

**How to Use:**
```bash
python scripts/extract_formulas_bensky_ocr.py --pdf "Books/Bensky - Formulas and Strategies.pdf" --formula "Si Jun Zi Tang" --start-page 50 --end-page 55
```

**What it does:**
- Uses OCR (Tesseract) to read scanned PDF pages
- Extracts formula composition, indications, actions
- Handles pinyin tone marks and special characters
- Creates markdown files in TCM_Formulas/

---

### extract_missing_herbs.py
**Purpose:** Identifies herbs that are missing from the knowledge base and extracts them.

**How to Use:**
```bash
python scripts/extract_missing_herbs.py --reference "priority_herbs_pages.json"
```

**What it does:**
- Compares existing herb files against a master list
- Generates a list of missing herbs
- Can trigger extraction for missing herbs

---

### extract_maciocia_diagnosis.py
**Purpose:** Extracts diagnostic information from Maciocia's "Diagnosis in Chinese Medicine" PDF.

**How to Use:**
```bash
python scripts/extract_maciocia_diagnosis.py --pdf "Books/Diagnosis in Chinese Medicine.pdf" --topic "Tongue Diagnosis"
```

**What it does:**
- Extracts diagnostic criteria and patterns
- Creates structured notes for tongue, pulse, and other diagnostic methods
- Includes images and tables from the source material

---

### extract_foundations_patterns.py
**Purpose:** Extracts pattern information from Maciocia's "Foundations of Chinese Medicine."

**How to Use:**
```bash
python scripts/extract_foundations_patterns.py --pdf "Books/Maciocia - The foundation of Chinese medicine.pdf"
```

**What it does:**
- Extracts TCM pattern descriptions
- Parses clinical manifestations, etiology, treatment principles
- Creates pattern files in TCM_Patterns/

---

### extract_chinese_flashcards.py
**Purpose:** Extracts Chinese characters and pinyin from herb/formula files for language flashcards.

**How to Use:**
```bash
python scripts/extract_chinese_flashcards.py --output "anki_exports/tcm_chinese_flashcards.csv"
```

**What it does:**
- Scans all TCM_Herbs and TCM_Formulas files
- Extracts Chinese names and pinyin
- Generates flashcard CSV for Anki import
- Creates character study lists

---

### extract_diagnosis_auto.py
**Purpose:** Automatically extracts diagnostic patterns from clinical text using AI.

**How to Use:**
```bash
python scripts/extract_diagnosis_auto.py --input "case 1.md"
```

**What it does:**
- Uses pattern matching to identify diagnostic information
- Automatically structures clinical cases
- Links to existing patterns in the knowledge base

---

## AI-Powered Content Generation Scripts

### deep_research_pipeline.py
**Purpose:** Main orchestrator for creating complete OCDS materials from research to final notes.

**How to Use:**
```bash
python scripts/deep_research_pipeline.py \
  --topic "Spleen Qi Deficiency" \
  --project "Traditional Chinese Medicine" \
  --template "OCDS_Documentation/05_Material_Templates/Root_Note_Template.md" \
  --class-id "TCM_101"
```

**What it does:**
1. Generates AI research prompts for the topic
2. Conducts deep research using Gemini API
3. Parses template structure
4. Generates content for each section
5. Fills template with generated content
6. Creates all associated materials (flashcards, quizzes, slides)
7. Validates frontmatter and OCDS compliance

**Required:** GEMINI_API_KEY environment variable

---

### gemini_research.py
**Purpose:** Core module for AI-powered research using Google's Gemini API.

**How to Use:**
```python
from gemini_research import GeminiDeepResearch

researcher = GeminiDeepResearch(api_key="your_key")
result = researcher.research("What is Spleen Qi Deficiency in TCM?")
print(result['content'])
```

**What it does:**
- Interfaces with Gemini 2.0 Flash API
- Conducts deep research with search grounding
- Returns structured research results with sources
- Used by all other AI-powered scripts

---

### research_prompt_generator.py
**Purpose:** Generates optimized research prompts for AI research based on topic and template.

**How to Use:**
```bash
python scripts/research_prompt_generator.py --topic "Liver Blood Deficiency" --template "Root_Note_Template.md"
```

**What it does:**
- Analyzes template structure
- Creates comprehensive research prompts
- Tailors prompts to OCDS requirements
- Ensures all template sections will be covered

---

### content_generator.py
**Purpose:** Generates content for individual template sections using AI and research context.

**How to Use:**
```bash
python scripts/content_generator.py \
  --topic "Kidney Yang Deficiency" \
  --heading "Clinical Manifestations" \
  --context-file "research_output.txt"
```

**What it does:**
- Takes research context and heading name
- Generates appropriate content for that section
- Adapts writing style based on section type (overview, clinical manifestations, treatment, etc.)
- Tracks progress across all sections

---

### template_parser.py
**Purpose:** Parses markdown templates and extracts structure for content generation.

**How to Use:**
```python
from template_parser import TemplateParser

parser = TemplateParser()
structure = parser.parse(Path("Root_Note_Template.md"))
print(structure['headings'])
```

**What it does:**
- Extracts YAML frontmatter
- Identifies heading hierarchy (H1, H2, H3, H4)
- Creates structured representation of template
- Used by content generator to fill templates systematically

---

### template_filler.py
**Purpose:** Fills template with generated content and validates structure.

**How to Use:**
```python
from template_filler import TemplateFiller

filler = TemplateFiller()
filled_content = filler.fill_template(template_path, generated_sections)
```

**What it does:**
- Takes parsed template and generated content
- Merges content into template structure
- Maintains heading hierarchy
- Validates frontmatter completeness

---

## Materials Generation Scripts

### generate_all_materials.py
**Purpose:** Master script that generates ALL OCDS materials from a root note.

**How to Use:**
```bash
python scripts/generate_all_materials.py \
  --root-note "Materials/TCM_101/Root_Note_Spleen_Qi_Deficiency.md" \
  --class-id "TCM_101" \
  --week 3
```

**What it does:**
- Reads root note
- Generates flashcards using AI
- Generates quiz with clinical scenarios
- Generates presentation slides
- Creates guided conversation
- Creates study material summary
- Packages all materials together

---

### generate_flashcards_ai.py
**Purpose:** Generates flashcards from root note content using AI.

**How to Use:**
```bash
python scripts/generate_flashcards_ai.py \
  --root-note "Root_Note_Lung_Yin_Deficiency.md" \
  --num-cards 20
```

**What it does:**
- Analyzes root note content
- Uses AI to create high-quality Q&A flashcards
- Formats flashcards for Obsidian
- Exports to CSV for Anki if needed

---

### generate_flashcards_from_root.py
**Purpose:** Alternative flashcard generator that extracts from specific root note sections.

**How to Use:**
```bash
python scripts/generate_flashcards_from_root.py --pattern "Spleen Qi Deficiency"
```

**What it does:**
- Looks for "Flashcard Seeds" section in root note
- Parses Q&A pairs
- Creates flashcard markdown files
- Supports manual and AI-generated flashcards

---

### generate_formula_flashcards.py
**Purpose:** Generates specialized flashcards for formula memorization.

**How to Use:**
```bash
python scripts/generate_formula_flashcards.py --formula "Si Jun Zi Tang"
```

**What it does:**
- Creates composition flashcards (herbs in formula)
- Creates action/indication flashcards
- Creates dosage and modification flashcards
- Formats for spaced repetition

---

### generate_herb_flashcards.py
**Purpose:** Generates specialized flashcards for herb memorization.

**How to Use:**
```bash
python scripts/generate_herb_flashcards.py --herb "Huang Qi"
```

**What it does:**
- Creates property flashcards (temperature, flavor, channels)
- Creates action flashcards
- Creates combination flashcards
- Includes Chinese characters and pinyin

---

### generate_point_flashcards.py
**Purpose:** Generates specialized flashcards for acupuncture point memorization.

**How to Use:**
```bash
python scripts/generate_point_flashcards.py --point "ST-36"
```

**What it does:**
- Creates location flashcards
- Creates action/indication flashcards
- Creates combination flashcards
- Includes traditional and modern indications

---

### generate_quiz_ai.py
**Purpose:** Generates clinical scenario quizzes using AI.

**How to Use:**
```bash
python scripts/generate_quiz_ai.py \
  --root-note "Root_Note_Heart_Blood_Deficiency.md" \
  --num-questions 10
```

**What it does:**
- Creates realistic clinical scenarios
- Generates multiple-choice questions
- Provides detailed explanations
- Formats for OCDS quiz system

---

### generate_quiz_from_root.py
**Purpose:** Extracts quiz questions from root note "Quiz Seeds" section.

**How to Use:**
```bash
python scripts/generate_quiz_from_root.py --pattern "Kidney Yin Deficiency"
```

**What it does:**
- Parses "Quiz Seeds" section
- Formats questions for quiz system
- Adds scoring and feedback
- Creates quiz markdown file

---

### generate_slides_ai.py
**Purpose:** Generates presentation slides using Advanced Slides format.

**How to Use:**
```bash
python scripts/generate_slides_ai.py \
  --root-note "Root_Note_Liver_Qi_Stagnation.md" \
  --theme "black"
```

**What it does:**
- Creates visually structured presentation
- Uses progressive reveal (fragments)
- Includes speaker notes
- Formats for Obsidian Advanced Slides plugin
- Adds clinical pearls and mnemonics

---

### generate_guided_conversation.py
**Purpose:** Creates interactive guided learning conversation.

**How to Use:**
```bash
python scripts/generate_guided_conversation.py --pattern "Lung Qi Deficiency"
```

**What it does:**
- Generates conversational questions for each section
- Creates assessment criteria
- Provides scaffolded learning path
- Can run as interactive CLI or generate markdown script

---

## Conversation & Assessment Scripts

### conversation_engine.py
**Purpose:** Main orchestrator for guided learning conversations.

**How to Use:**
```bash
python scripts/conversation_engine.py "Spleen Qi Deficiency" --max-attempts 3
```

**What it does:**
- Runs interactive CLI conversation
- Asks questions about each root note section
- Assesses understanding using AI
- Provides reinforcement and feedback
- Tracks progress and saves conversation log

---

### conversation_state.py
**Purpose:** Manages conversation progress and state.

**How to Use:**
```python
from conversation_state import ConversationState

state = ConversationState(root_note_path)
heading = state.get_current_heading()
state.advance_heading()
```

**What it does:**
- Tracks current position in conversation
- Records student responses and scores
- Calculates progress percentage
- Saves/loads conversation state
- Generates summary statistics

---

### understanding_assessor.py
**Purpose:** AI-powered assessment of student understanding.

**How to Use:**
```python
from understanding_assessor import UnderstandingAssessor

assessor = UnderstandingAssessor()
result = assessor.assess_response(question, student_answer, reference_content)
print(result['score'])  # 0-100
print(result['feedback'])
```

**What it does:**
- Evaluates student responses using AI
- Identifies strengths and missing concepts
- Detects misconceptions
- Provides constructive feedback
- Determines if student should advance or review

---

### prompt_generator.py
**Purpose:** Generates prompts for guided conversations.

**How to Use:**
```python
from prompt_generator import PromptGenerator

gen = PromptGenerator()
question = gen.generate_initial_prompt("Clinical Manifestations", content)
```

**What it does:**
- Creates initial questions for each section
- Generates reinforcement prompts for unclear areas
- Creates encouragement messages
- Adapts difficulty based on student performance

---

## Data Processing & Linking Scripts

### auto_link_symptoms.py
**Purpose:** Automatically links symptoms in herb/formula/pattern files to TCM_Symptoms files.

**How to Use:**
```bash
# Preview changes
python scripts/auto_link_symptoms.py --dry-run

# Apply changes
python scripts/auto_link_symptoms.py

# Specific directories
python scripts/auto_link_symptoms.py --dirs TCM_Herbs TCM_Formulas
```

**What it does:**
- Scans all TCM_Symptoms/ files
- Searches through herb/formula/pattern files for symptom mentions
- Updates frontmatter 'symptoms' field with wikilinks
- Creates backups before modifying files
- Supports aliases for flexible matching

---

### enhance_symptoms.py
**Purpose:** Enhances symptom files with additional information and standardization.

**How to Use:**
```bash
python scripts/enhance_symptoms.py --symptom-dir "TCM_Symptoms/"
```

**What it does:**
- Standardizes symptom file formatting
- Adds missing frontmatter fields
- Links related symptoms
- Categorizes symptoms by system (digestive, respiratory, etc.)

---

### find_duplicate_symptoms.py
**Purpose:** Identifies duplicate or near-duplicate symptom files.

**How to Use:**
```bash
python scripts/find_duplicate_symptoms.py
```

**What it does:**
- Scans all symptom files
- Identifies duplicates and similar symptoms
- Suggests merges or alias relationships
- Helps maintain clean symptom database

---

### body_parser.py
**Purpose:** Utility module that extracts structured data from root note markdown body.

**How to Use:**
```python
from body_parser import BodyParser

parser = BodyParser(markdown_content)
flashcard_seeds = parser.extract_flashcard_seeds()
quiz_seeds = parser.extract_quiz_seeds()
core_concepts = parser.extract_core_concepts()
```

**What it does:**
- Extracts flashcard Q&A pairs
- Extracts quiz questions
- Extracts core concepts
- Parses structured sections from markdown

---

## Documentation

### DIAGNOSIS_EXTRACTION_GUIDE.md
**Purpose:** Comprehensive guide for extracting diagnostic information from source materials.

**Contents:**
- Step-by-step extraction workflows
- Pattern identification guidelines
- Formatting standards
- Quality control checklist

---

## Environment Setup

To use these scripts, you need:

### Python Dependencies
```bash
pip install pyyaml google-generativeai pymupdf pytesseract pillow
```

### Environment Variables
```bash
export GEMINI_API_KEY="your_gemini_api_key"
```

### Directory Structure
Ensure your knowledge base follows the OCDS structure:
```
TCM_Knowledge_Base/
├── TCM_Herbs/
├── TCM_Formulas/
├── TCM_Points/
├── TCM_Patterns/
├── Materials/
│   └── TCM_101/
├── scripts/
└── OCDS_Documentation/
```

---

## Common Workflows

### Creating a New Pattern from Scratch
```bash
# 1. Generate all materials using deep research
python scripts/deep_research_pipeline.py \
  --topic "Heart Fire" \
  --project "Traditional Chinese Medicine" \
  --template "OCDS_Documentation/05_Material_Templates/Root_Note_Template.md" \
  --class-id "TCM_101"

# 2. Review and edit generated root note
# 3. Generate additional materials if needed
python scripts/generate_all_materials.py --root-note "Materials/TCM_101/Root_Note_Heart_Fire.md"
```

### Extracting from Books
```bash
# Extract a single herb
python scripts/extract_herb_bensky.py \
  --pdf "Books/Bensky - Materia Medica.pdf" \
  --herb "Ren Shen" \
  --start-page 120 \
  --end-page 125

# Extract a formula with OCR
python scripts/extract_formulas_bensky_ocr.py \
  --pdf "Books/Bensky - Formulas and Strategies.pdf" \
  --formula "Liu Wei Di Huang Wan" \
  --start-page 280 \
  --end-page 285
```

### Creating Study Materials
```bash
# Generate complete materials package
python scripts/generate_all_materials.py \
  --root-note "Materials/TCM_101/Root_Note_Spleen_Qi_Deficiency.md" \
  --class-id "TCM_101" \
  --week 3
```

### Linking Symptoms
```bash
# Preview symptom linking
python scripts/auto_link_symptoms.py --dry-run

# Apply symptom linking
python scripts/auto_link_symptoms.py
```

### Running Guided Conversation
```bash
# Interactive mode
python scripts/conversation_engine.py "Lung Yin Deficiency"

# Generate conversation script
python scripts/conversation_engine.py "Lung Yin Deficiency" --script --output "conversation.md"
```

---

## Troubleshooting

### API Key Issues
If you get API key errors:
```bash
# Check if key is set
echo $GEMINI_API_KEY

# Set temporarily
export GEMINI_API_KEY="your_key_here"

# Set permanently (add to ~/.bashrc or ~/.zshrc)
echo 'export GEMINI_API_KEY="your_key_here"' >> ~/.bashrc
```

### Module Import Errors
If you get import errors, ensure you're in the correct directory:
```bash
cd /home/shuma/Documents/AI_Suite/TCM_Knowledge_Base
python scripts/script_name.py
```

### PDF Extraction Issues
If OCR isn't working:
```bash
# Install Tesseract OCR
sudo apt-get install tesseract-ocr

# Check installation
tesseract --version
```

---

## Script Dependencies Map

```
deep_research_pipeline.py
├── research_prompt_generator.py
├── gemini_research.py
├── template_parser.py
├── content_generator.py
│   └── gemini_research.py
├── template_filler.py
└── generate_all_materials.py
    ├── generate_flashcards_ai.py
    │   └── gemini_research.py
    ├── generate_quiz_ai.py
    │   └── gemini_research.py
    ├── generate_slides_ai.py
    │   └── gemini_research.py
    └── conversation_engine.py
        ├── conversation_state.py
        ├── understanding_assessor.py
        │   └── gemini_research.py
        └── prompt_generator.py
            └── gemini_research.py
```

---

*Last Updated: November 14, 2025*
