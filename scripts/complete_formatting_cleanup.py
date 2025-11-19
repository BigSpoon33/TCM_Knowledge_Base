#!/usr/bin/env python3
"""
Complete formatting cleanup: Fix headings and add missing emoji sections
This script:
1. Fixes first heading from "# 🔮 Pattern Name" to "# `=this.name`"
2. Adds emoji headings where missing
3. Ensures all patterns match the TEMPLATE_Pattern.md standard
"""

import re
from pathlib import Path

# Standard emoji headings from template
EMOJI_HEADINGS = {
    'Overview': '📋',
    'Pattern Classification': '🏷️',
    'Etiology & Pathogenesis': '🌱',
    'Clinical Manifestations': '🔍',
    'Diagnostic Criteria': '✅',
    'Differential Diagnosis': '🔄',
    'Treatment Principles': '🎯',
    'Herbal Formulas': '🌿',
    'Acupuncture Treatment': '📍',
    'Acupuncture Points': '📍',
    'Lifestyle & Prevention': '💡',
    'Modern Medicine Correlation': '🔬',
    'Clinical Notes': '📝',
    'References & Resources': '📚',
    'Case Studies': '📋',
    'Treatment Approach': '💊',
    'Study Notes & Memory Aids': '📝',
    'Western Medical Correlates': '🏥',
    'Pattern Variations & Combinations': '🔄',
    'Contraindications & Cautions': '⚠️',
    'Related Notes & Cross-References': '🔗',
    'Pattern Comparison Table': '📊',
}

def fix_first_heading(content):
    """Fix the first heading to use `=this.name` syntax"""
    lines = content.split('\n')
    fixed = False
    
    for i, line in enumerate(lines):
        # Skip frontmatter
        if line.strip() == '---':
            continue
        
        # Find first heading after frontmatter
        if line.startswith('# ') and not fixed:
            # Check if it's already in correct format
            if '`=this.name`' in line:
                return content  # Already correct
            
            # Replace with correct format
            lines[i] = '# `=this.name`'
            fixed = True
            
            # Remove any duplicate heading on the next line
            if i + 1 < len(lines) and lines[i + 1].startswith('## '):
                # Check if it's a duplicate of the pattern name
                if any(keyword in lines[i + 1].lower() for keyword in ['liver', 'heart', 'kidney', 'spleen', 'lung', 'qi', 'blood', 'yin', 'yang', 'damp', 'heat', 'cold']):
                    lines[i + 1] = ''  # Remove duplicate
            
            break
    
    return '\n'.join(lines)

def add_emoji_to_heading(line):
    """Add appropriate emoji to a heading if missing"""
    # Skip if already has emoji (contains non-ASCII in first 10 chars)
    if any(ord(c) > 127 for c in line[:15]):
        return line
    
    # Extract heading text
    match = re.match(r'^(##\s+)(.+)$', line)
    if not match:
        return line
    
    prefix = match.group(1)
    text = match.group(2).strip()
    
    # Check for known headings
    for heading_name, emoji in EMOJI_HEADINGS.items():
        if heading_name.lower() in text.lower() or text.lower() in heading_name.lower():
            return f"{prefix}{emoji} {heading_name}\n"
    
    # If no match, return original
    return line

def fix_emoji_headings(content):
    """Add emojis to headings that are missing them"""
    lines = content.split('\n')
    fixed_lines = []
    
    in_frontmatter = False
    for line in lines:
        # Track frontmatter
        if line.strip() == '---':
            in_frontmatter = not in_frontmatter
            fixed_lines.append(line)
            continue
        
        # Skip frontmatter
        if in_frontmatter:
            fixed_lines.append(line)
            continue
        
        # Fix ## headings
        if line.startswith('## ') and not line.startswith('### '):
            fixed_lines.append(add_emoji_to_heading(line))
        else:
            fixed_lines.append(line)
    
    return '\n'.join(fixed_lines)

def fix_file(filepath):
    """Apply all formatting fixes to a file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Apply fixes
        content = fix_first_heading(content)
        content = fix_emoji_headings(content)
        
        # Only write if changed
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        
        return False
        
    except Exception as e:
        print(f"  ✗ Error: {e}")
        return False

def main():
    # Read the list of files needing fixes
    files_list = Path('/tmp/files_needing_heading_fix.txt')
    
    if not files_list.exists():
        print("Error: files list not found at /tmp/files_needing_heading_fix.txt")
        return
    
    with open(files_list, 'r') as f:
        file_paths = [line.strip() for line in f if line.strip()]
    
    print("="*70)
    print("COMPLETE FORMATTING CLEANUP")
    print("="*70)
    print(f"Processing {len(file_paths)} files")
    print()
    
    fixed_count = 0
    for i, filepath_str in enumerate(file_paths, 1):
        filepath = Path(filepath_str)
        
        if not filepath.exists():
            print(f"[{i}/{len(file_paths)}] SKIP: {filepath.name} (not found)")
            continue
        
        print(f"[{i}/{len(file_paths)}] {filepath.name}")
        
        if fix_file(filepath):
            print(f"  ✓ Fixed")
            fixed_count += 1
        else:
            print(f"  - No changes needed")
    
    print()
    print("="*70)
    print(f"✅ COMPLETE: Fixed {fixed_count}/{len(file_paths)} files")
    print("="*70)

if __name__ == '__main__':
    main()
