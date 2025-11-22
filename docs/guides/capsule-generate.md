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
2.  Generate content based on the default "education" template.
3.  Create files in the current directory.

---

## 4. Options & Flags

The command supports several options to customize the generation process:

| Option | Short | Description | Default |
| :--- | :--- | :--- | :--- |
| `--template` | `-t` | Specify the template to use. | `education` |
| `--output` | `-o` | Specify the output directory. | `.` (Current Dir) |
| `--materials` | `-m` | Comma-separated list of materials to generate. | `all` |
| `--hybrid` | | Path to an existing note for AI enhancement. | `None` |
| `--no-research` | | Skip the research phase and use the template only. | `False` |
| `--dry-run` | | Preview the operation without creating files. | `False` |

---

## 5. Examples

### 5.1 Generating Specific Materials

If you only want specific types of content, use the `--materials` flag. Available types include: `flashcards`, `quizzes`, `slides`, `conversations`.

```bash
# Generate only flashcards and a quiz
capsule generate "Photosynthesis" --materials "flashcards,quizzes"
```

### 5.2 Specifying an Output Directory

Keep your vault organized by directing output to a specific folder.

```bash
# Generate content in the 'Biology' folder
capsule generate "Cell Structure" --output "./Biology"
```

### 5.3 Using a Different Template

If you have custom templates (e.g., for medical or technical topics), you can specify them.

```bash
capsule generate "Python Decorators" --template "technical_guide"
```

### 5.4 Hybrid Mode (Enhancing Existing Notes)

Use the `--hybrid` flag to enhance an existing note with AI-generated content. This is useful for expanding on your own rough notes.

```bash
capsule generate "My Rough Notes" --hybrid "./notes/draft.md"
```

### 5.5 Dry Run

Use `--dry-run` to see what the command would do without actually creating any files or making API calls.

```bash
capsule generate "Quantum Physics" --dry-run
```

**Output:**
```text
[DRY RUN] Would generate capsule about: Quantum Physics
Template: education
Output: .
```

---

## 6. Troubleshooting

### "ConfigError: Gemini API key is not set"
**Cause:** The `research.api_key` is missing from your configuration.
**Solution:** Check your `config.yaml` file and ensure the key is present under the `research` section as shown in the Prerequisites.

### "NetworkError: An error occurred while calling the Gemini API"
**Cause:** Issues with internet connection or the API service.
**Solution:** Check your internet connection. If the problem persists, verify your API key is valid and has quota remaining.

### "Template not found"
**Cause:** The specified template (e.g., `my_template.md.j2`) does not exist in the templates directory.
**Solution:** Verify the template name and ensure it exists in your templates folder.
