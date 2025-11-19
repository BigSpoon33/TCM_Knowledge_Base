#!/usr/bin/env python3
"""
Split Five Elements glob files into individual pattern files.
"""

import os
import re
from pathlib import Path
from datetime import datetime

def split_five_elements_file(filepath: Path, output_dir: Path):
    """Split a Five Elements glob file into individual patterns."""
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split by ## headers (pattern sections)
    sections = re.split(r'\n## (.*?)\n', content)
    
    # First section is frontmatter
    frontmatter = sections[0]
    
    # Process each pattern (every 2 items: header + content)
    patterns_created = []
    for i in range(1, len(sections), 2):
        if i + 1 < len(sections):
            header = sections[i].strip()
            pattern_content = sections[i + 1].strip()
            
            # Create pattern name from header
            # e.g., "FIRE ⇨ EARTH (Not Generating Son)" -> "Fire Not Generating Earth"
            pattern_name = create_pattern_name(header)
            
            # Create individual pattern file
            individual_content = create_individual_pattern(
                pattern_name, header, pattern_content, frontmatter
            )
            
            # Save
            output_file = output_dir / f"{pattern_name}.md"
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(individual_content)
            
            patterns_created.append(pattern_name)
            print(f"✅ Created: {pattern_name}")
    
    return patterns_created

def create_pattern_name(header: str) -> str:
    """Create a clean pattern name from header."""
    # Extract elements and relationship type
    # e.g., "FIRE ⇨ EARTH (Not Generating Son)" 
    
    match = re.match(r'(\w+)\s*⇨\s*(\w+)\s*\((.*?)\)', header)
    if match:
        source = match.group(1).capitalize()
        target = match.group(2).capitalize()
        relationship = match.group(3)
        
        # Create readable name
        if "Not Generating" in relationship:
            return f"{source} Not Generating {target}"
        elif "Overacting" in relationship:
            return f"{source} Overacting on {target}"
        elif "Insulting" in relationship:
            return f"{source} Insulting {target}"
    
    # Fallback
    return header.replace("⇨", "to").replace("(", "").replace(")", "")

def create_individual_pattern(name: str, header: str, content: str, original_frontmatter: str) -> str:
    """Create a complete individual pattern file."""
    
    # Extract symptoms from content
    symptoms = []
    symptom_section = re.search(r'\*\*Symptoms \(CAM\):\*\*(.*?)(?=\*\*Additional Notes|\Z)', content, re.DOTALL)
    if symptom_section:
        symptom_lines = symptom_section.group(1).strip().split('\n')
        symptoms = [line.strip('- ').strip() for line in symptom_lines if line.strip().startswith('-')]
    
    # Extract zangfu diagnosis
    zangfu = ""
    zangfu_match = re.search(r'Zangfu Diagnosis:\s*(.+)', content)
    if zangfu_match:
        zangfu = zangfu_match.group(1).strip()
    
    # Create new frontmatter
    now = datetime.now()
    new_frontmatter = f"""---
# =9 Core Metadata (Universal Fields)
id: "pattern-{now.strftime('%Y%m%d%H%M%S')}"
name: "{name}"
type: "pattern"
aliases: []
tags: [TCM, Pattern, Five_Elements]

# =9 Cross-Link Fields (Universal Relationship Slots)
category: [Five Elements]
related: []
symptoms: {symptoms}
patterns: []
western_conditions: []
formulas: []
herbs: []
points: []
nutrition: []
tests: []

# =9 Pattern-Specific Data
pattern_data:
  pattern_type: "Five Elements"
  pattern_subtype: "{name}"
  excess_deficiency: ""
  hot_cold: ""
  interior_exterior: "Interior"
  yin_yang: ""
  etiology: []
  pathomechanisms: []
  disease_progression: ""
  cardinal_symptoms: {symptoms}
  tongue: ""
  pulse: ""
  treatment_principle: []
  contraindications: []

created: {now.strftime('%Y-%m-%d')}
updated: {now.strftime('%Y-%m-%d')}
---

# {name}

## Pattern Relationship
{header}

## Clinical Manifestations

**Cardinal Symptoms:**
{chr(10).join('- ' + s for s in symptoms)}

**Zangfu Diagnosis:** {zangfu}

## Additional Information

{content}
"""
    
    return new_frontmatter

def main():
    """Main function."""
    base_dir = Path(__file__).parent.parent
    source_dir = base_dir / "TCM_Patterns" / "Five Elements Patterns"
    output_dir = source_dir
    
    print("🔧 Splitting Five Elements glob files...")
    print("="*70)
    
    glob_files = [
        "Five Elements Fire Patterns.md",
        "Five Elements Wood Patterns.md",
        "Five Elements Earth Patterns.md",
        "Five Elements Metal Patterns.md",
        "Five Elements Water Patterns.md"
    ]
    
    all_created = []
    for filename in glob_files:
        filepath = source_dir / filename
        if filepath.exists():
            print(f"\n📄 Processing: {filename}")
            created = split_five_elements_file(filepath, output_dir)
            all_created.extend(created)
    
    print("\n" + "="*70)
    print(f"✅ Split complete! Created {len(all_created)} individual patterns")
    print("="*70)
    
    return all_created

if __name__ == "__main__":
    created_patterns = main()
    print("\n💡 Next step: Enhance these patterns with:")
    print("   python scripts/enhance_pattern_single_call.py \"[Pattern Name]\" --pattern-dir \"TCM_Patterns/Five Elements Patterns\"")
