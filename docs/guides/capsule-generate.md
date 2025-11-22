# Capsule Generate Command Guide

**Purpose: A comprehensive guide to using the `capsule generate` command for AI-assisted content creation.**

---

## 1. Overview

The `capsule generate` command is a powerful tool that leverages AI to research topics and generate structured educational content for your Obsidian vault. It uses the Gemini API to perform deep research and then synthesizes that information into various formats like flashcards, quizzes, slides, and conversation scripts.

## 2. Prerequisites

Before using the generate command, you must ensure your environment is configured correctly:

1.  **Gemini API Key**: You need a valid Google Gemini API key.
2.  **Configuration**: The API key must be set in your capsule configuration file.

### Setting up the API Key

Add your API key to your configuration file (usually located at `~/.config/capsule/config.yaml` or `.capsule/config.yaml` in your project root):

```yaml
research:
  api_key: "YOUR_GEMINI_API_KEY"
```

---

## 3. Basic Usage

The simplest way to generate content is to provide a topic. By default, this will generate all available material types using the "education" template.

```bash
capsule generate "Topic Name"
```

**Example:**
```bash
capsule generate "Introduction to TCM Herbs"
```

This command will:
1.  Research "Introduction to TCM Herbs".
2.  Create a folder named `Introduction_to_TCM_Herbs`.
3.  Generate a comprehensive Root Note and supporting materials (Flashcards, Quiz, Slides, etc.) inside that folder.

---

## 4. Options & Flags

The command supports several options to customize the generation process:

| Option | Short | Description | Default |
| :--- | :--- | :--- | :--- |
| `--template` | `-t` | Specify the template to use (Jinja2 or Markdown). | `education` |
| `--output` | `-o` | Specify the parent output directory. | `.` (Current Dir) |
| `--materials` | `-m` | Comma-separated list of materials to generate. | `all` |
| `--hybrid` | | Path to an existing source file (Root Note) to generate materials from. | `None` |
| `--no-research` | | Skip the research phase and use dummy content (for testing). | `False` |
| `--dry-run` | | Preview the operation without creating files. | `False` |

---

## 5. Advanced Features

### 5.1 Deep Research Mode (Custom Markdown Templates)

For highly detailed and structured notes, you can provide a custom Markdown template. The system will parse the template's headings and generate content for each section individually using the AI.

**How to use:**
1.  Create a markdown template (e.g., `my_template.md`) with the desired structure:
    ```markdown
    ---
    type: root_note
    ---
    # {{ topic }}
    
    ## Overview
    [Content will be generated here]
    
    ## Key Concepts
    [Content will be generated here]
    ```
2.  Run the command pointing to your template:
    ```bash
    capsule generate "Deep Learning" --template path/to/my_template.md
    ```

This mode produces richer, more comprehensive content compared to the standard generation.

### 5.2 Hybrid Mode (Generate from Source)

If you already have a detailed note and want to generate study materials (Flashcards, Quiz, Slides) from it without re-researching, use the `--hybrid` flag.

**How to use:**
```bash
capsule generate "Machine Learning" --hybrid "path/to/Root_Note_Machine_Learning.md"
```

The system will read your existing note and use it as the context to generate:
*   Flashcards (JSON structured)
*   Quiz Questions (JSON structured)
*   Presentation Slides
*   Guided Conversation Script

### 5.3 Output Structure

The command automatically organizes generated content into a dedicated folder for the topic.

**Example Structure:**
```text
Output_Dir/
└── Topic_Name/
    ├── Root_Note_Topic_Name.md
    ├── Topic_Name_Flashcards.md
    ├── Topic_Name_Quiz.md
    ├── Topic_Name_Slides.md
    ├── Topic_Name_Guided_Conversation.md
    ├── Topic_Name_Study_Material.md
    └── Topic_Name_Tasks.md
```

---

## 6. Examples

### 6.1 Generating Specific Materials

If you only want specific types of content, use the `--materials` flag. Available types include: `flashcards`, `quiz`, `slides`, `conversation`, `study_material`, `tasks`, `root_note`.

```bash
# Generate only flashcards and a quiz
capsule generate "Photosynthesis" --materials "flashcards,quiz"
```

### 6.2 Specifying an Output Directory

Keep your vault organized by directing output to a specific folder. The topic folder will be created inside this directory.

```bash
# Generate content in the 'Biology' folder
# Result: ./Biology/Cell_Structure/
capsule generate "Cell Structure" --output "./Biology"
```

### 6.3 Dry Run

Use `--dry-run` to see what the command would do without actually creating any files or making API calls.

```bash
capsule generate "Quantum Physics" --dry-run
```

---

## 7. Troubleshooting

### "ConfigError: Gemini API key is not set"
**Cause:** The `research.api_key` is missing from your configuration.
**Solution:** Check your `config.yaml` file and ensure the key is present under the `research` section as shown in the Prerequisites.

### "NetworkError: An error occurred while calling the Gemini API"
**Cause:** Issues with internet connection or the API service.
**Solution:** Check your internet connection. If the problem persists, verify your API key is valid and has quota remaining.

### "Template not found"
**Cause:** The specified template (e.g., `my_template.md.j2` or `my_template.md`) does not exist.
**Solution:** Verify the template name and ensure it exists in your templates folder or provide the full path to a custom markdown template.
