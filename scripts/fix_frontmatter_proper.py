#!/usr/bin/env python3
"""
Properly fix frontmatter to match the Ai Ye herb format standard:
1. Empty arrays use [] syntax
2. Proper list item formatting (no broken multi-line)
3. Blank line before closing ---
4. Consistent formatting throughout
"""

import os
import re
from pathlib import Path
from datetime import datetime

def parse_yaml_frontmatter(frontmatter_text):
    """Parse YAML frontmatter into a structured dict"""
    lines = frontmatter_text.strip().split('\n')
    data = {}
    current_key = None
    current_parent = None
    indent_stack = []
    
    for line in lines:
        if line.strip() == '---' or not line.strip():
            continue
            
        # Calculate indentation level
        indent = len(line) - len(line.lstrip())
        
        # Check if it's a key-value pair
        if ':' in line and not line.strip().startswith('-'):
            parts = line.split(':', 1)
            key = parts[0].strip()
            value = parts[1].strip() if len(parts) > 1 else ''
            
            if indent == 0:
                # Top-level key
                current_key = key
                current_parent = None
                if value:
                    data[key] = value
                else:
                    data[key] = []
                indent_stack = [(0, key)]
            elif indent == 2:
                # Second-level (pattern_data subfields)
                if current_key not in data:
                    data[current_key] = {}
                if not isinstance(data[current_key], dict):
                    data[current_key] = {}
                current_parent = current_key
                if value:
                    data[current_key][key] = value
                else:
                    data[current_key][key] = []
                indent_stack = [(0, current_key), (2, key)]
        
        elif line.strip().startswith('-'):
            # List item
            item = line.strip()[1:].strip()
            
            # Determine which key this belongs to
            if indent == 0:
                # Top-level list
                if current_key and isinstance(data[current_key], list):
                    data[current_key].append(item)
            elif indent == 2:
                # Second-level list (pattern_data)
                if current_parent and len(indent_stack) > 1:
                    parent_key = indent_stack[0][1]
                    sub_key = indent_stack[1][1]
                    if parent_key in data and isinstance(data[parent_key], dict):
                        if sub_key not in data[parent_key]:
                            data[parent_key][sub_key] = []
                        if isinstance(data[parent_key][sub_key], list):
                            data[parent_key][sub_key].append(item)
    
    return data

def format_frontmatter(data, pattern_name):
    """Format data into clean YAML frontmatter"""
    lines = []
    lines.append('---')
    
    # Required fields in order
    if 'id' in data:
        lines.append(f"id: {data['id']}")
    else:
        date_str = datetime.now().strftime('%Y%m%d')
        slug = pattern_name.lower().replace(' ', '-').replace('(', '').replace(')', '').replace('→', '').strip('-')
        lines.append(f"id: pattern-{date_str}-{slug}")
    
    lines.append(f"name: {pattern_name}")
    lines.append('type: pattern')
    
    # Aliases
    if 'aliases' in data and data['aliases'] and isinstance(data['aliases'], list):
        lines.append('aliases:')
        for alias in data['aliases']:
            if alias and alias != '[]':
                lines.append(f"- {alias}")
    else:
        lines.append('aliases: []')
    
    # Tags
    if 'tags' in data and data['tags'] and isinstance(data['tags'], list):
        lines.append('tags:')
        for tag in data['tags']:
            if tag:
                lines.append(f"- {tag}")
    else:
        lines.append('tags:')
        lines.append('- TCM')
        lines.append('- Pattern')
    
    # Category
    if 'category' in data and data['category'] and isinstance(data['category'], list):
        lines.append('category:')
        for cat in data['category']:
            if cat:
                lines.append(f"- {cat}")
    else:
        lines.append('category: []')
    
    # Related
    if 'related' in data and data['related'] and isinstance(data['related'], list):
        lines.append('related:')
        for rel in data['related']:
            if rel:
                lines.append(f"- {rel}")
    else:
        lines.append('related: []')
    
    # Symptoms
    if 'symptoms' in data and data['symptoms'] and isinstance(data['symptoms'], list):
        lines.append('symptoms:')
        for sym in data['symptoms']:
            if sym:
                # Ensure wiki-link format
                if not sym.startswith("'[["):
                    if sym.startswith('[['):
                        sym = f"'{sym}'"
                    else:
                        sym = f"'[[{sym}]]'"
                lines.append(f"- {sym}")
    else:
        lines.append('symptoms: []')
    
    # Patterns
    lines.append('patterns: []')
    
    # Western conditions
    if 'western_conditions' in data and data['western_conditions'] and isinstance(data['western_conditions'], list):
        lines.append('western_conditions:')
        for wc in data['western_conditions']:
            if wc:
                lines.append(f"- {wc}")
    else:
        lines.append('western_conditions: []')
    
    # Formulas
    if 'formulas' in data and data['formulas'] and isinstance(data['formulas'], list):
        lines.append('formulas:')
        for formula in data['formulas']:
            if formula:
                lines.append(f"- {formula}")
    else:
        lines.append('formulas: []')
    
    # Herbs
    if 'herbs' in data and data['herbs'] and isinstance(data['herbs'], list):
        lines.append('herbs:')
        for herb in data['herbs']:
            if herb:
                lines.append(f"- {herb}")
    else:
        lines.append('herbs: []')
    
    # Points
    if 'points' in data and data['points'] and isinstance(data['points'], list):
        lines.append('points:')
        for pt in data['points']:
            if pt:
                lines.append(f"- {pt}")
    else:
        lines.append('points: []')
    
    # Nutrition
    if 'nutrition' in data and data['nutrition'] and isinstance(data['nutrition'], list):
        lines.append('nutrition:')
        for nut in data['nutrition']:
            if nut:
                lines.append(f"- {nut}")
    else:
        lines.append('nutrition: []')
    
    # Tests
    if 'tests' in data and data['tests'] and isinstance(data['tests'], list):
        lines.append('tests:')
        for test in data['tests']:
            if test:
                lines.append(f"- {test}")
    else:
        lines.append('tests: []')
    
    # Pattern data
    if 'pattern_data' in data and isinstance(data['pattern_data'], dict):
        lines.append('pattern_data:')
        pd = data['pattern_data']
        
        # Simple fields
        for key in ['pattern_type', 'pattern_subtype', 'excess_deficiency', 'hot_cold', 
                    'interior_exterior', 'yin_yang']:
            if key in pd:
                lines.append(f"  {key}: {pd[key]}")
        
        # List fields
        for key in ['etiology', 'pathomechanisms', 'cardinal_symptoms', 
                    'treatment_principle', 'contraindications']:
            if key in pd and pd[key]:
                if isinstance(pd[key], list):
                    lines.append(f"  {key}:")
                    for item in pd[key]:
                        if item:
                            lines.append(f"  - {item}")
        
        # String fields
        for key in ['disease_progression', 'tongue', 'pulse']:
            if key in pd and pd[key]:
                lines.append(f"  {key}: {pd[key]}")
    
    # Dates
    today = datetime.now().strftime('%Y-%m-%d')
    if 'created' in data:
        created = data['created']
        # Normalize date format
        if not re.match(r'\d{4}-\d{2}-\d{2}', str(created)):
            created = today
        lines.append(f"created: {created}")
    else:
        lines.append(f"created: {today}")
    
    if 'updated' in data:
        updated = data['updated']
        if not re.match(r'\d{4}-\d{2}-\d{2}', str(updated)):
            updated = today
        lines.append(f"updated: {updated}")
    else:
        lines.append(f"updated: {today}")
    
    # Blank line before closing
    lines.append('')
    lines.append('---')
    
    return '\n'.join(lines)

def fix_file(filepath):
    """Fix frontmatter in a single file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if '---' not in content:
            return False
        
        # Split frontmatter and body
        parts = content.split('---', 2)
        if len(parts) < 3:
            return False
        
        old_frontmatter = parts[1]
        body = parts[2]
        
        filename = os.path.basename(filepath)
        pattern_name = filename.replace('.md', '')
        
        # Parse frontmatter
        data = parse_yaml_frontmatter(old_frontmatter)
        
        # Check if already properly formatted
        if (old_frontmatter.strip().count('\naliases: []') > 0 or 
            (old_frontmatter.strip().count('\naliases:\n-') > 0)):
            # Check if has blank line before closing ---
            if body.startswith('\n\n'):
                print(f"  ✓ Already properly formatted")
                return False
        
        # Format new frontmatter
        new_frontmatter = format_frontmatter(data, pattern_name)
        
        # Ensure body starts cleanly
        body = body.lstrip('\n')
        
        # Write back
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(f"{new_frontmatter}\n\n{body}")
        
        print(f"  ✓ Fixed frontmatter")
        return True
        
    except Exception as e:
        print(f"  ✗ Error: {e}")
        return False

def main():
    base_dir = Path(__file__).parent.parent / 'TCM_Patterns'
    
    print("="*70)
    print("FIXING FRONTMATTER TO PROPER YAML FORMAT")
    print("="*70)
    print()
    
    # Find all pattern markdown files
    pattern_files = []
    for folder in base_dir.iterdir():
        if folder.is_dir():
            for file in folder.glob('*.md'):
                # Skip index files, templates, and documentation
                if (not file.name.startswith('00 ') and 
                    'TEMPLATE' not in file.name and
                    'MERGE' not in file.name and
                    'PHASE' not in file.name and
                    'STANDARDIZATION' not in file.name and
                    'QUICK_REFERENCE' not in file.name and
                    'Table' not in file.name and
                    'NEXT_STEPS' not in file.name):
                    pattern_files.append(file)
    
    print(f"Found {len(pattern_files)} pattern files to check\n")
    
    fixed_count = 0
    for i, filepath in enumerate(sorted(pattern_files), 1):
        rel_path = filepath.relative_to(base_dir)
        print(f"[{i}/{len(pattern_files)}] {rel_path}")
        
        if fix_file(filepath):
            fixed_count += 1
    
    print()
    print("="*70)
    print(f"✅ COMPLETE: Fixed {fixed_count} files")
    print("="*70)

if __name__ == '__main__':
    main()
