#!/usr/bin/env python3
"""
Frontmatter Auditor
Analyzes all markdown files to check frontmatter quality and completeness
"""

import os
import re
import yaml
from pathlib import Path
from typing import Dict, List, Set
from collections import defaultdict


class FrontmatterAuditor:
    """Audits frontmatter across all entity types"""

    def __init__(self, base_dir: Path):
        self.base_dir = Path(base_dir)

        # Define expected fields for each entity type
        self.expected_fields = {
            'herb': ['id', 'name', 'type', 'category', 'related', 'symptoms', 'patterns',
                    'western_conditions', 'formulas', 'points', 'herb_data'],
            'point': ['id', 'name', 'type', 'category', 'related', 'symptoms', 'patterns',
                     'western_conditions', 'formulas', 'herbs', 'points', 'treats_diseases', 'point_data'],
            'disease': ['id', 'name', 'type', 'category', 'related', 'symptoms', 'patterns',
                       'western_conditions', 'formulas', 'herbs', 'points'],
            'concept': ['id', 'name', 'type', 'category', 'related', 'symptoms', 'patterns',
                       'western_conditions', 'formulas', 'herbs', 'points'],
            'technique': ['id', 'name', 'type', 'category', 'related', 'technique_data']
        }

        # Results storage
        self.results = {
            'herbs': [],
            'points': [],
            'diseases': [],
            'concepts': [],
            'techniques': []
        }

        self.issues = defaultdict(list)

    def audit_file(self, file_path: Path, entity_type: str) -> Dict:
        """Audit a single file's frontmatter"""
        result = {
            'file': file_path.name,
            'path': str(file_path),
            'has_frontmatter': False,
            'frontmatter_valid': False,
            'missing_fields': [],
            'empty_fields': [],
            'has_wikilinks': False,
            'error': None
        }

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Check for frontmatter
            match = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)

            if not match:
                result['error'] = "No frontmatter found"
                self.issues['no_frontmatter'].append(str(file_path))
                return result

            result['has_frontmatter'] = True
            frontmatter_text = match.group(1).strip()

            # Check if frontmatter is empty or just dashes
            if not frontmatter_text or frontmatter_text == '----':
                result['error'] = "Empty frontmatter"
                result['frontmatter_valid'] = False
                self.issues['empty_frontmatter'].append(str(file_path))
                return result

            # Try to parse YAML
            try:
                frontmatter = yaml.safe_load(frontmatter_text)
                result['frontmatter_valid'] = True
            except yaml.YAMLError as e:
                result['error'] = f"YAML parse error: {str(e)}"
                result['frontmatter_valid'] = False
                self.issues['yaml_parse_error'].append(str(file_path))
                return result

            # Check for expected fields
            expected = self.expected_fields.get(entity_type, [])
            for field in expected:
                if field not in frontmatter:
                    result['missing_fields'].append(field)
                elif not frontmatter[field] or frontmatter[field] == [] or frontmatter[field] == '':
                    result['empty_fields'].append(field)

            # Check for wikilinks in content
            result['has_wikilinks'] = bool(re.search(r'\[\[.+?\]\]', content))

            # Record issues
            if result['missing_fields']:
                self.issues['missing_fields'].append(f"{file_path.name}: {', '.join(result['missing_fields'])}")
            if result['empty_fields']:
                self.issues['empty_fields'].append(f"{file_path.name}: {', '.join(result['empty_fields'])}")

        except Exception as e:
            result['error'] = f"File read error: {str(e)}"
            self.issues['file_read_error'].append(str(file_path))

        return result

    def audit_directory(self, directory: Path, entity_type: str) -> List[Dict]:
        """Audit all files in a directory"""
        if not directory.exists():
            return []

        results = []
        for file_path in directory.glob("*.md"):
            # Skip templates and examples
            if file_path.stem.startswith("TEMPLATE_") or file_path.stem.startswith("EXAMPLE_"):
                continue

            result = self.audit_file(file_path, entity_type)
            results.append(result)

        return results

    def run_audit(self):
        """Run audit on all entity types"""
        print("=" * 80)
        print("🔍 FRONTMATTER AUDIT")
        print("=" * 80)

        # Audit each entity type
        print("\n📖 Auditing Concepts...")
        self.results['concepts'] = self.audit_directory(
            self.base_dir / "TCM_Concepts", 'concept'
        )

        print("🩺 Auditing Diseases...")
        self.results['diseases'] = self.audit_directory(
            self.base_dir / "TCM_Diseases", 'disease'
        )

        print("📍 Auditing Points...")
        self.results['points'] = self.audit_directory(
            self.base_dir / "TCM_Points", 'point'
        )

        print("🌿 Auditing Herbs...")
        self.results['herbs'] = self.audit_directory(
            self.base_dir / "TCM_Herbs", 'herb'
        )

        print("⚡ Auditing Techniques...")
        self.results['techniques'] = self.audit_directory(
            self.base_dir / "TCM_Techniques", 'technique'
        )

    def generate_report(self, output_file: Path = None):
        """Generate comprehensive audit report"""
        if output_file is None:
            output_file = self.base_dir / "FRONTMATTER_AUDIT_REPORT.md"

        report = []
        report.append("# 🔍 Frontmatter Audit Report\n")
        report.append(f"**Generated:** {Path(__file__).stem}\n")
        report.append("---\n")

        # Summary statistics
        report.append("## 📊 Summary\n")

        for entity_type, results in self.results.items():
            total = len(results)
            with_frontmatter = sum(1 for r in results if r['has_frontmatter'])
            valid_frontmatter = sum(1 for r in results if r['frontmatter_valid'])
            with_errors = sum(1 for r in results if r['error'])

            report.append(f"### {entity_type.title()}")
            report.append(f"- **Total files:** {total}")
            report.append(f"- **Has frontmatter:** {with_frontmatter}/{total} ({with_frontmatter/total*100 if total else 0:.1f}%)")
            report.append(f"- **Valid YAML:** {valid_frontmatter}/{total} ({valid_frontmatter/total*100 if total else 0:.1f}%)")
            report.append(f"- **Files with errors:** {with_errors}\n")

        # Issues breakdown
        report.append("\n---\n")
        report.append("## ⚠️ Issues Found\n")

        if self.issues['no_frontmatter']:
            report.append(f"### Missing Frontmatter ({len(self.issues['no_frontmatter'])} files)\n")
            for file in self.issues['no_frontmatter'][:20]:
                report.append(f"- `{Path(file).name}`")
            if len(self.issues['no_frontmatter']) > 20:
                report.append(f"\n_...and {len(self.issues['no_frontmatter']) - 20} more_\n")
            report.append("\n")

        if self.issues['empty_frontmatter']:
            report.append(f"### Empty Frontmatter ({len(self.issues['empty_frontmatter'])} files)\n")
            for file in self.issues['empty_frontmatter'][:20]:
                report.append(f"- `{Path(file).name}`")
            if len(self.issues['empty_frontmatter']) > 20:
                report.append(f"\n_...and {len(self.issues['empty_frontmatter']) - 20} more_\n")
            report.append("\n")

        if self.issues['yaml_parse_error']:
            report.append(f"### YAML Parse Errors ({len(self.issues['yaml_parse_error'])} files)\n")
            for file in self.issues['yaml_parse_error']:
                report.append(f"- `{Path(file).name}`")
            report.append("\n")

        # Missing fields summary
        if self.issues['missing_fields']:
            report.append(f"### Missing Required Fields ({len(self.issues['missing_fields'])} files)\n")
            for issue in self.issues['missing_fields'][:30]:
                report.append(f"- {issue}")
            if len(self.issues['missing_fields']) > 30:
                report.append(f"\n_...and {len(self.issues['missing_fields']) - 30} more_\n")
            report.append("\n")

        # Detailed results by category
        report.append("\n---\n")
        report.append("## 📋 Detailed Results\n")

        for entity_type, results in self.results.items():
            report.append(f"### {entity_type.title()}\n")

            # Files with issues
            problem_files = [r for r in results if r['error'] or r['missing_fields'] or not r['frontmatter_valid']]

            if problem_files:
                report.append(f"**Files needing attention: {len(problem_files)}**\n")
                for result in problem_files[:15]:
                    report.append(f"#### {result['file']}")
                    if result['error']:
                        report.append(f"- ❌ Error: {result['error']}")
                    if result['missing_fields']:
                        report.append(f"- Missing fields: {', '.join(result['missing_fields'])}")
                    if result['empty_fields']:
                        report.append(f"- Empty fields: {', '.join(result['empty_fields'])}")
                    report.append("")

                if len(problem_files) > 15:
                    report.append(f"_...and {len(problem_files) - 15} more files with issues_\n")
            else:
                report.append("✅ All files have valid frontmatter!\n")

            report.append("\n")

        # Write report
        report_text = "\n".join(report)
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(report_text)

        print(f"\n✅ Audit report generated: {output_file}")
        return output_file

    def print_summary(self):
        """Print summary to console"""
        print("\n" + "=" * 80)
        print("📊 AUDIT SUMMARY")
        print("=" * 80)

        for entity_type, results in self.results.items():
            total = len(results)
            valid = sum(1 for r in results if r['frontmatter_valid'])
            print(f"\n{entity_type.title()}: {valid}/{total} valid ({valid/total*100 if total else 0:.1f}%)")

            # Count issues
            no_fm = sum(1 for r in results if not r['has_frontmatter'])
            errors = sum(1 for r in results if r['error'])
            missing = sum(1 for r in results if r['missing_fields'])

            if no_fm:
                print(f"  ⚠️  {no_fm} files without frontmatter")
            if errors:
                print(f"  ❌ {errors} files with errors")
            if missing:
                print(f"  📝 {missing} files missing required fields")

        print("\n" + "=" * 80)

    def run(self):
        """Run complete audit"""
        self.run_audit()
        self.print_summary()
        self.generate_report()


def main():
    base_dir = Path(__file__).parent.parent
    auditor = FrontmatterAuditor(base_dir)
    auditor.run()


if __name__ == "__main__":
    main()
