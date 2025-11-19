#!/usr/bin/env python3
"""
Remove duplicate original content sections and fix heading issues
Many enhanced patterns have the old format preserved at the end.
This script removes those sections while preserving the enhanced content.
"""

import re
from pathlib import Path

def clean_file(filepath):
    """Remove duplicate/original content sections"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        changed = False
        
        # Find and remove "Original Note Content" section
        markers = [
            r'\n## 📦 Original Note Content.*?```markdown.*?```\n---\n',
            r'\n## 📦 Original Note Content.*?```\n---\n',
            r'\n## 📦 Original Note Content.*$',
        ]
        
        for marker in markers:
            new_content = re.sub(marker, '', content, flags=re.DOTALL)
            if new_content != content:
                content = new_content
                changed = True
        
        # Remove duplicate # =9 headings and content after them
        # Look for pattern where we have valid content, then # =9 appears
        lines = content.split('\n')
        clean_lines = []
        found_valid_heading = False
        skip_rest = False
        
        for i, line in enumerate(lines):
            if skip_rest:
                continue
            
            # Track if we've found the proper heading
            if '`=this.name`' in line and line.startswith('# '):
                found_valid_heading = True
                clean_lines.append(line)
                continue
            
            # If we find # =9 AFTER the valid heading, skip everything after
            if found_valid_heading and line.startswith('# =9'):
                skip_rest = True
                changed = True
                continue
            
            # If we find # CAM heading, skip it and everything after
            if line.strip() == '# CAM':
                skip_rest = True
                changed = True
                continue
            
            clean_lines.append(line)
        
        if changed:
            content = '\n'.join(clean_lines)
            
            # Clean up trailing newlines
            content = content.rstrip() + '\n'
            
            # Write back
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            return True
        
        return False
        
    except Exception as e:
        print(f"  ✗ Error: {e}")
        return False

def main():
    base_dir = Path(__file__).parent.parent / 'TCM_Patterns'
    
    print("="*70)
    print("REMOVING DUPLICATE CONTENT SECTIONS")
    print("="*70)
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
                    'PROGRESS' not in file.name):
                    pattern_files.append(file)
    
    print(f"Found {len(pattern_files)} pattern files to check\n")
    
    cleaned_count = 0
    for i, filepath in enumerate(sorted(pattern_files), 1):
        rel_path = filepath.relative_to(base_dir)
        
        if clean_file(filepath):
            print(f"[{i}/{len(pattern_files)}] {rel_path} - ✓ Cleaned")
            cleaned_count += 1
    
    print()
    print("="*70)
    print(f"✅ COMPLETE: Cleaned {cleaned_count} files")
    print("="*70)

if __name__ == '__main__':
    main()
