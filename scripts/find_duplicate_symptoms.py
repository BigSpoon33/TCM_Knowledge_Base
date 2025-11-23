import argparse
import os
from difflib import SequenceMatcher
from pathlib import Path


def normalize_symptom_name(name):
    """Normalize symptom name for comparison."""
    name = name.lower().strip()
    if name.endswith("ing"):
        name = name[:-3]
    if name.endswith("s"):
        name = name[:-1]
    return name.replace(" ", "").replace("_", "")


def suggest_canonical_name(name1, name2):
    """Suggest the canonical name."""
    name1_orig = name1
    name2_orig = name2

    # Prefer non-gerund form
    if name1_orig.endswith("ing") and not name2_orig.endswith("ing"):
        return name2_orig.title()
    if name2_orig.endswith("ing") and not name1_orig.endswith("ing"):
        return name1_orig.title()

    # Prefer singular form
    if name1_orig.endswith("s") and not name2_orig.endswith("s"):
        return name2_orig.title()
    if name2_orig.endswith("s") and not name1_orig.endswith("s"):
        return name1_orig.title()

    # Prefer shorter name as a fallback
    return name1_orig.title() if len(name1_orig) <= len(name2_orig) else name2_orig.title()


def find_duplicate_symptoms(symptoms_dir, similarity_threshold=0.85):
    """Find potential duplicate symptom files."""
    files = [p for p in Path(symptoms_dir).glob("*.md") if p.is_file() and not p.name.startswith("00 -")]

    duplicates = []
    analyzed_pairs = set()

    for i, file1 in enumerate(files):
        for file2 in files[i + 1 :]:
            pair = tuple(sorted((file1.stem, file2.stem)))
            if pair in analyzed_pairs:
                continue

            analyzed_pairs.add(pair)

            name1_norm = normalize_symptom_name(file1.stem)
            name2_norm = normalize_symptom_name(file2.stem)

            similarity = SequenceMatcher(None, name1_norm, name2_norm).ratio()

            if similarity >= similarity_threshold:
                duplicates.append(
                    {
                        "file1": str(file1),
                        "file2": str(file2),
                        "similarity": f"{similarity:.2f}",
                        "suggestion": suggest_canonical_name(file1.stem, file2.stem),
                    }
                )

    return sorted(duplicates, key=lambda x: x["similarity"], reverse=True)


def main():
    parser = argparse.ArgumentParser(description="Find duplicate symptom files in the TCM knowledge base.")
    parser.add_argument("symptoms_dir", type=str, help="Path to the directory containing TCM symptom markdown files.")
    parser.add_argument(
        "--threshold", type=float, default=0.85, help="Similarity threshold for detecting duplicates (0.0 to 1.0)."
    )
    args = parser.parse_args()

    if not os.path.isdir(args.symptoms_dir):
        print(f"Error: Directory not found at '{args.symptoms_dir}'")
        return

    duplicate_symptoms = find_duplicate_symptoms(args.symptoms_dir, args.threshold)

    if not duplicate_symptoms:
        print("No potential duplicates found.")
        return

    print("Potential Duplicate Symptoms Found:")
    print("=" * 40)
    for item in duplicate_symptoms:
        print(f"  File 1: {os.path.basename(item['file1'])}")
        print(f"  File 2: {os.path.basename(item['file2'])}")
        print(f"  Similarity: {item['similarity']}")
        print(f"  Suggested Canonical Name: {item['suggestion']}")
        print("-" * 20)


if __name__ == "__main__":
    main()
