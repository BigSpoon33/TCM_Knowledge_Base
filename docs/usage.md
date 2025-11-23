# User Guide

## Installation

```bash
pip install capsule-learn
```

## Configuration

Initialize the configuration:

```bash
capsule init
```

This will create a configuration file at `~/.config/capsule/config.yaml`. You need to set your Google Gemini API key:

```bash
capsule config --api-key YOUR_API_KEY
```

## Generating Capsules

To generate a new learning capsule:

```bash
capsule generate "Topic Name"
```

Options:
- `--output`, `-o`: Output directory (default: current directory)
- `--template`, `-t`: Template to use (default: root_note)
- `--materials`, `-m`: Materials to generate (flashcards, quiz, slides, conversation, or all)
- `--no-research`: Skip AI research and just use templates

Example:

```bash
capsule generate "Liver Qi Stagnation" -o MyVault/Capsules -m all
```

### Dashboards

Generated capsules now include a **Capsule Dashboard** (`Dashboard.md`) that provides an overview of the content, progress tracking, and quick links.

To view the dashboard properly in Obsidian, ensure you have the **Dataview** and **Meta Bind** plugins installed.

## CSS Theming

The system comes with a modular CSS framework. When you generate a capsule, CSS snippets are automatically deployed to your vault's `.obsidian/snippets` directory (if detected).

To enable the theme:
1. Go to Obsidian Settings > Appearance > CSS Snippets.
2. Enable `ocds-core`, `ocds-components`, `ocds-layouts`.
3. Enable a theme variant (e.g., `neon`, `minimal`, `academic`).

## Exporting Capsules

To share a capsule:

```bash
capsule export path/to/capsule
```

This creates a ZIP file containing the capsule and its metadata.

## Importing Capsules

To import a capsule:

```bash
capsule import capsule_package.zip
```

This will unzip the capsule and place it in your vault, handling version conflicts if necessary.
