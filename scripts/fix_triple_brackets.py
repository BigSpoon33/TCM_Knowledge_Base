#!/usr/bin/env python3
"""
Fix triple brackets and clean up frontmatter:
1. Fix [[[Item]]] -> [[Item]]
2. Remove # =9 comments from frontmatter
3. Clean up any remaining formatting issues
"""

import re
from pathlib import Path

def fix_frontmatter_final(content):
    """Final frontmatter cleanup"""
    if not content.startswith('---'):
        return content, False
    
    parts = content.split('\n---\n', 1)
    if len(parts) < 2:
        parts = content.split('---\n', 2)
        if len(parts) < 3:
            return content, False
        frontmatter_text = parts[1]
        body = '---\n' + parts[2]
    else:
        frontmatter_text = parts[0].replace('---\n', '', 1)
        body = '---\n' + parts[1]
    
    original_frontmatter = frontmatter_text
    
    # Remove # =9 comments from frontmatter
    lines = []
    for line in frontmatter_text.split('\n'):
        if line.strip().startswith('# =9'):
            continue
        if line.strip() == '#':
            continue
        lines.append(line)
    
    frontmatter_text = '\n'.join(lines)
    
    # Fix triple brackets: [[[Item]]] -> [[Item]]
    frontmatter_text = re.sub(r'\[\[\[([^\]]+)\]\]\]', r'[[\1]]', frontmatter_text)
    
    # Fix double brackets in arrays: [[["Item"]]] -> [["Item"]]
    frontmatter_text = re.sub(r'\[\[\["([^"]+)"\]\]\]', r'[["[\1]"]]', frontmatter_text)
    
    # Actually, for inline arrays with quotes, remove the extra brackets and quotes
    # Pattern: [[["Item"]]] or [["Item"]] -> [[Item]]
    frontmatter_text = re.sub(r'\[\["([^"]+)"\]\]', r'[[\1]]', frontmatter_text)
    
    changed = frontmatter_text != original_frontmatter
    
    # Reconstruct
    new_content = '---\n' + frontmatter_text + '\n' + body
    
    return new_content, changed

def fix_file(filepath):
    """Fix a file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content, changed = fix_frontmatter_final(content)
        
        if changed:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True
        
        return False
        
    except Exception as e:
        print(f"  ✗ Error: {e}")
        return False

def main():
    base_dir = Path(__file__).parent.parent / 'TCM_Patterns'
    
    print("="*70)
    print("FINAL FRONTMATTER CLEANUP")
    print("="*70)
    print("1. Fixing triple brackets [[[Item]]] -> [[Item]]")
    print("2. Removing # =9 comments from frontmatter")
    print()
    
    # Find all pattern files
    pattern_files = []
    for folder in base_dir.iterdir():
        if folder.is_dir():
            for file in folder.glob('*.md'):
                if (not file.name.startswith('00 ') and 
                    'TEMPLATE' not in file.name and
                    'EXAMPLE' not in file.name and
                    'MERGE' not in file.name and
                    'PHASE' not in file.name and
                    'STANDARDIZATION' not in file.name and
                    'QUICK_REFERENCE' not in file.name and
                    'Table' not in file.name and
                    'NEXT_STEPS' not in file.name and
                    'Comparison' not in file.name and
                    'Treatment' not in file.name and
                    'COMPLETE' not in file.name and
                    'SUMMARY' not in file.name and
                    'PROGRESS' not in file.name and
                    'Patterns.md' not in file.name):
                    pattern_files.append(file)
    
    print(f"Found {len(pattern_files)} pattern files to process\n")
    
    fixed_count = 0
    for i, filepath in enumerate(sorted(pattern_files), 1):
        rel_path = filepath.relative_to(base_dir)
        
        if fix_file(filepath):
            print(f"[{i}/{len(pattern_files)}] {rel_path} - ✓ Fixed")
            fixed_count += 1
    
    print()
    print("="*70)
    print(f"✅ COMPLETE: Fixed {fixed_count}/{len(pattern_files)} files")
    print("="*70)

if __name__ == '__main__':
    main()
