from pathlib import Path

# Base directory of the project
BASE_DIR = Path.cwd()

# Path to the templates directory
TEMPLATES_DIR = BASE_DIR / "capsule" / "templates"

# Centralized configuration for generated materials
MATERIAL_CONFIG = {
    "root_note": {
        "template": "root_note.md.j2",
        "filename": "Root_Note_{topic}.md",
        "description": "The main content note for the topic.",
    },
    "flashcards": {
        "template": "flashcards.md.j2",
        "filename": "{topic}_Flashcards.md",
        "description": "A deck of flashcards for spaced repetition.",
    },
    "quiz": {
        "template": "quiz.md.j2",
        "filename": "{topic}_Quiz.md",
        "description": "A multiple-choice quiz to test knowledge.",
    },
    "slides": {
        "template": "slides.md.j2",
        "filename": "{topic}_Slides.md",
        "description": "A presentation/slideshow for the topic.",
    },
    "conversation": {
        "template": "conversation.md.j2",
        "filename": "{topic}_Guided_Conversation.md",
        "description": "A guided conversation script for interactive learning.",
    },
    "study_material": {
        "template": None,  # This is a special case, generated from a string
        "filename": "{topic}_Study_Material.md",
        "description": "A study guide linking to other materials.",
    },
    "tasks": {
        "template": None,  # Also a special case
        "filename": "{topic}_Tasks.md",
        "description": "A task list for tracking study progress.",
    },
}
