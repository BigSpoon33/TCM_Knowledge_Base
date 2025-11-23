from pathlib import Path

import yaml


def get_pattern_info(pattern_file):
    """Extracts symptoms, tongue, and pulse from a pattern file."""
    with open(pattern_file, encoding="utf-8") as f:
        content = f.read()

    try:
        frontmatter = yaml.safe_load(content.split("---")[1])
        symptoms = frontmatter.get("symptoms", [])
        tongue = frontmatter.get("pattern_data", {}).get("tongue", "")
        pulse = frontmatter.get("pattern_data", {}).get("pulse", "")
        return {"symptoms": symptoms, "tongue": tongue, "pulse": pulse}
    except Exception as e:
        print(f"Error parsing {pattern_file}: {e}")
        return None


def enhance_symptom_files(symptoms_dir, patterns_dir):
    """Enhances symptom files with differential diagnosis info from patterns."""
    symptom_files = [
        p
        for p in Path(symptoms_dir).glob("*.md")
        if p.is_file() and not p.name.startswith("00 -") and p.name != "README.md"
    ]

    for symptom_file in symptom_files:
        with open(symptom_file, encoding="utf-8") as f:
            content = f.read()

        try:
            frontmatter = yaml.safe_load(content.split("---")[1])
            patterns = frontmatter.get("patterns", [])

            if not patterns:
                continue

            enhancement = "\n\n### Pattern-Specific Manifestations\n"

            for pattern_name in patterns:
                pattern_file = Path(patterns_dir) / f"{pattern_name}.md"
                if pattern_file.exists():
                    pattern_info = get_pattern_info(pattern_file)
                    if pattern_info:
                        enhancement += f"\n#### {pattern_name}\n\n"
                        enhancement += "**Symptoms:**\n"
                        for symptom in pattern_info["symptoms"]:
                            enhancement += f"- {symptom}\n"
                        enhancement += f"\n**Tongue:** {pattern_info['tongue']}\n"
                        enhancement += f"**Pulse:** {pattern_info['pulse']}\n---\n"

            with open(symptom_file, "a", encoding="utf-8") as f:
                f.write(enhancement)
            print(f"Enhanced {symptom_file.name}")

        except Exception as e:
            print(f"Error processing {symptom_file.name}: {e}")


if __name__ == "__main__":
    symptoms_directory = "TCM_Symptoms"
    patterns_directory = "TCM_Patterns"
    enhance_symptom_files(symptoms_directory, patterns_directory)
