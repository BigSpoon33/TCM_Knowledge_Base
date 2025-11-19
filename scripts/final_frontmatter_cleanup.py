#!/usr/bin/env python3
"""
Final cleanup of frontmatter issues:
1. Fix broken closing --- (like "- --")
2. Ensure blank line after closing ---
3. Remove duplicate categories
4. Ensure proper spacing
"""

import re
from pathlib import Path

def fix_file(filepath):
    """Fix final frontmatter issues"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Fix 1: Fix broken closing --- markers
        # Pattern: "- --" or similar malformed closing
        content = re.sub(r'\n- --\n', '\n\n---\n', content)
        content = re.sub(r'\n--\n', '\n---\n', content)
        
        # Fix 2: Ensure blank line after closing ---
        # Replace "---\n##" with "---\n\n##"
        content = re.sub(r'\n---\n(#)', r'\n---\n\n\1', content)
        
        # Fix 3: Remove duplicate "Zang Fu" in categories
        lines = content.split('\n')
        fixed_lines = []
        in_frontmatter = False
        in_category = False
        seen_categories = set()
        
        for i, line in enumerate(lines):
            if line.strip() == '---':
                if not in_frontmatter:
                    in_frontmatter = True
                    in_category = False
                    seen_categories = set()
                else:
                    in_frontmatter = False
                    in_category = False
                fixed_lines.append(line)
                continue
            
            if in_frontmatter:
                # Check if we're entering category section
                if line.strip().startswith('category:'):
                    in_category = True
                    seen_categories = set()
                    fixed_lines.append(line)
                    continue
                elif line.strip() and not line.strip().startswith('-') and ':' in line:
                    # New key, exit category section
                    in_category = False
                
                # If in category section, remove duplicates
                if in_category and line.strip().startswith('-'):
                    category = line.strip()[1:].strip()
                    if category not in seen_categories:
                        seen_categories.add(category)
                        fixed_lines.append(line)
                    continue
            
            fixed_lines.append(line)
        
        content = '\n'.join(fixed_lines)
        
        # Only write if changed
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  ✓ Fixed frontmatter issues")
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
    print()
    
    # Find all pattern markdown files
    pattern_files = []
    for folder in base_dir.iterdir():
        if folder.is_dir():
            for file in folder.glob('*.md'):
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
