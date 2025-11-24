#!/usr/bin/env python3
"""
Quality check for enhanced pattern files
Checks for:
1. Proper frontmatter structure
2. Correct heading syntax
3. Presence of key sections
4. Content completeness
5. Link integrity
"""

import random
import re
from collections import defaultdict
from pathlib import Path


class PatternQualityChecker:
    def __init__(self):
        self.issues = defaultdict(list)
        self.checks_passed = 0
        self.checks_failed = 0

    def check_frontmatter(self, content, filename):
        """Check frontmatter structure and completeness"""
        # Check for frontmatter delimiters
        if not content.startswith("---\n"):
            self.issues[filename].append("Missing opening frontmatter delimiter")
            self.checks_failed += 1
            return False

        # Find closing delimiter
        end_idx = content.find("\n---\n", 4)
        if end_idx == -1:
            self.issues[filename].append("Missing closing frontmatter delimiter")
            self.checks_failed += 1
            return False

        frontmatter = content[4:end_idx]

        # Check required fields
        required_fields = ["id:", "name:", "type: pattern", "tags:", "category:"]
        missing = []
        for field in required_fields:
            if field not in frontmatter:
                missing.append(field)

        if missing:
            self.issues[filename].append(f"Missing required fields: {', '.join(missing)}")
            self.checks_failed += 1
            return False

        self.checks_passed += 1
        return True

    def check_heading_syntax(self, content, filename):
        """Check first heading uses correct Obsidian syntax"""
        lines = content.split("\n")

        # Find first heading after frontmatter
        in_frontmatter = False
        found_heading = False

        for line in lines:
            if line.strip() == "---":
                in_frontmatter = not in_frontmatter
                continue

            if in_frontmatter:
                continue

            if line.startswith("# "):
                if "`=this.name`" in line:
                    self.checks_passed += 1
                    return True
                else:
                    self.issues[filename].append(f"Incorrect heading syntax: {line.strip()}")
                    self.checks_failed += 1
                    return False

        self.issues[filename].append("No heading found after frontmatter")
        self.checks_failed += 1
        return False

    def check_emoji_sections(self, content, filename):
        """Check for presence of emoji-enhanced section headings"""
        required_sections = {
            "📋 Overview": False,
            "🌱 Etiology": False,
            "🔍 Clinical Manifestations": False,
        }

        for section in required_sections:
            if section in content:
                required_sections[section] = True

        missing = [s for s, found in required_sections.items() if not found]

        if missing:
            self.issues[filename].append(f"Missing key sections: {', '.join(missing)}")
            self.checks_failed += 1
            return False

        self.checks_passed += 1
        return True

    def check_content_length(self, content, filename):
        """Check if pattern has substantial content (not a stub)"""
        # Remove frontmatter
        end_idx = content.find("\n---\n", 4)
        if end_idx != -1:
            body = content[end_idx + 5 :]
        else:
            body = content

        # Remove code blocks and dataview queries
        body = re.sub(r"```.*?```", "", body, flags=re.DOTALL)
        body = re.sub(r"`.*?`", "", body)

        # Count meaningful content
        words = len(body.split())

        if words < 100:
            self.issues[filename].append(f"Very short content ({words} words) - likely a stub")
            self.checks_failed += 1
            return False
        elif words < 500:
            self.issues[filename].append(f"Short content ({words} words) - may need expansion")
            # This is a warning, not a failure
            self.checks_passed += 1
            return True
        else:
            self.checks_passed += 1
            return True

    def check_broken_links(self, content, filename):
        """Check for potentially broken wikilinks"""
        # Find all [[links]]
        links = re.findall(r"\[\[([^\]]+)\]\]", content)

        suspicious = []
        for link in links:
            # Check for common issues
            if "  " in link:  # Double spaces
                suspicious.append(f"Double space in link: [[{link}]]")
            if link.strip() != link:  # Leading/trailing spaces
                suspicious.append(f"Whitespace in link: [[{link}]]")
            if "|" in link and link.split("|")[0].strip() == "":
                suspicious.append(f"Empty link target: [[{link}]]")

        if suspicious:
            self.issues[filename].append("Potential link issues: " + "; ".join(suspicious[:3]))
            self.checks_failed += 1
            return False

        self.checks_passed += 1
        return True

    def check_file(self, filepath):
        """Run all checks on a file"""
        filename = filepath.name

        try:
            with open(filepath, encoding="utf-8") as f:
                content = f.read()
        except Exception as e:
            self.issues[filename].append(f"Error reading file: {e}")
            self.checks_failed += 5  # Count as multiple failures
            return False

        # Run all checks
        self.check_frontmatter(content, filename)
        self.check_heading_syntax(content, filename)
        self.check_emoji_sections(content, filename)
        self.check_content_length(content, filename)
        self.check_broken_links(content, filename)

        return len(self.issues[filename]) == 0


def main():
    base_dir = Path(__file__).parent.parent / "TCM_Patterns"

    print("=" * 70)
    print("PATTERN QUALITY CHECK")
    print("=" * 70)
    print()

    # Collect all pattern files
    pattern_files = []
    for folder in base_dir.iterdir():
        if folder.is_dir():
            for file in folder.glob("*.md"):
                if (
                    not file.name.startswith("00 ")
                    and "TEMPLATE" not in file.name
                    and "EXAMPLE" not in file.name
                    and "MERGE" not in file.name
                    and "PHASE" not in file.name
                    and "STANDARDIZATION" not in file.name
                    and "QUICK_REFERENCE" not in file.name
                    and "Table" not in file.name
                    and "NEXT_STEPS" not in file.name
                    and "Comparison" not in file.name
                    and "Treatment" not in file.name
                    and "COMPLETE" not in file.name
                    and "SUMMARY" not in file.name
                    and "PROGRESS" not in file.name
                ):
                    pattern_files.append(file)

    print(f"Found {len(pattern_files)} pattern files")

    # Sample files for detailed check (all from each category + random sample)
    sample_size = min(30, len(pattern_files))

    # Get representative samples from each folder
    samples_by_folder = defaultdict(list)
    for file in pattern_files:
        folder = file.parent.name
        samples_by_folder[folder].append(file)

    sample_files = []
    for folder, files in samples_by_folder.items():
        # Take 2-3 random files from each category
        num_samples = min(3, len(files))
        sample_files.extend(random.sample(files, num_samples))

    # If we need more, add random files
    if len(sample_files) < sample_size:
        remaining = [f for f in pattern_files if f not in sample_files]
        additional = min(sample_size - len(sample_files), len(remaining))
        sample_files.extend(random.sample(remaining, additional))

    sample_files = sample_files[:sample_size]

    print(f"Checking {len(sample_files)} sample files across all categories")
    print()

    checker = PatternQualityChecker()
    perfect_files = []
    files_with_issues = []

    for i, filepath in enumerate(sorted(sample_files), 1):
        rel_path = filepath.relative_to(base_dir)
        print(f"[{i}/{len(sample_files)}] {rel_path}")

        if checker.check_file(filepath):
            print("  ✓ All checks passed")
            perfect_files.append(filepath.name)
        else:
            print("  ⚠ Issues found:")
            for issue in checker.issues[filepath.name]:
                print(f"    - {issue}")
            files_with_issues.append((filepath.name, checker.issues[filepath.name]))

    # Summary
    print()
    print("=" * 70)
    print("QUALITY CHECK SUMMARY")
    print("=" * 70)
    print(f"Files checked: {len(sample_files)}")
    print(f"Perfect files: {len(perfect_files)} ({len(perfect_files) / len(sample_files) * 100:.1f}%)")
    print(f"Files with issues: {len(files_with_issues)} ({len(files_with_issues) / len(sample_files) * 100:.1f}%)")
    print()
    print(f"Total checks passed: {checker.checks_passed}")
    print(f"Total checks failed: {checker.checks_failed}")
    print(f"Success rate: {checker.checks_passed / (checker.checks_passed + checker.checks_failed) * 100:.1f}%")

    if files_with_issues:
        print()
        print("ISSUES SUMMARY:")
        print("-" * 70)

        # Group issues by type
        issue_types = defaultdict(int)
        for filename, issues in files_with_issues:
            for issue in issues:
                # Extract issue type
                if ":" in issue:
                    issue_type = issue.split(":")[0]
                else:
                    issue_type = issue
                issue_types[issue_type] += 1

        for issue_type, count in sorted(issue_types.items(), key=lambda x: x[1], reverse=True):
            print(f"  {issue_type}: {count} occurrences")

    print()
    print("=" * 70)

    # Return exit code
    if checker.checks_failed > 0:
        print("⚠ Some quality issues detected - review recommended")
        return 1
    else:
        print("✅ All quality checks passed!")
        return 0


if __name__ == "__main__":
    exit(main())
