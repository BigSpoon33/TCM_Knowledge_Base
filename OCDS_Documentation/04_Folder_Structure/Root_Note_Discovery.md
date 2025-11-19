# Root Note Discovery System

**Version:** 1.0.0  
**Last Updated:** 2025-11-10  
**Purpose:** Technical guide to root note discovery and resolution

---

## Overview

The Root Note Discovery System is the core mechanism by which Capsule CLI and OCDS automation scripts locate and identify educational content across the vault. This document explains the technical implementation and design decisions.

---

## Discovery Problem

### The Challenge

Given a pattern name like `"Heart Blood Deficiency"`, the system must:

1. **Locate** the corresponding root note file
2. **Validate** it's a valid root note (not a random markdown file)
3. **Find** associated materials (flashcards, quizzes, etc.)
4. **Handle** multiple organization strategies (directories, tags, flat, hierarchical)
5. **Scale** to thousands of patterns

### Current Limitations

The existing system has these constraints:

- **Hard-coded paths**: Only searches `TCM_Patterns/` directory
- **Name-based only**: Matches filenames, not metadata
- **No cross-vault**: Can't discover patterns outside configured directory
- **Poor flexibility**: Students/instructors must follow strict folder structure

---

## Discovery Methods

### Method 1: Directory Scanning (Current Implementation)

**Location:** `capsule/utils/validation.py:9-48`

```python
def validate_pattern_exists(
    pattern: str,
    patterns_dir: Path
) -> Tuple[bool, Optional[str], List[str]]:
    """Validate that a pattern exists in the knowledge base."""
    
    if not patterns_dir.exists():
        return False, None, []
    
    # Get all pattern files from main dir and subdirectories
    pattern_files = list(patterns_dir.glob("*.md"))
    
    # Also check subdirectories
    for subdir in patterns_dir.iterdir():
        if subdir.is_dir() and not subdir.name.startswith('.'):
            pattern_files.extend(list(subdir.glob("*.md")))
    
    pattern_names = [f.stem.replace("_", " ") for f in pattern_files]
    
    # Exact match
    if pattern in pattern_names:
        return True, pattern, []
    
    # Case-insensitive match
    pattern_lower = pattern.lower()
    for name in pattern_names:
        if name.lower() == pattern_lower:
            return True, name, []
    
    # Fuzzy match for suggestions
    suggestions = get_close_matches(pattern, pattern_names, n=5, cutoff=0.6)
    
    return False, None, suggestions
```

**How it works:**

1. Scans `patterns_dir` for all `.md` files
2. Recursively checks immediate subdirectories
3. Extracts pattern names from filenames (converts `_` to space)
4. Matches user input against filenames
5. Provides fuzzy suggestions if no match

**Pros:**
- ✅ Simple and fast
- ✅ No metadata required
- ✅ Works with legacy content
- ✅ Predictable behavior

**Cons:**
- ❌ Limited to configured directory
- ❌ Doesn't discover research outputs
- ❌ No validation of content type
- ❌ Poor handling of name conflicts
- ❌ Can't handle complex categorization

---

### Method 2: Metadata-Based Discovery (Recommended)

**Status:** Not yet implemented  
**Priority:** HIGH

```python
def find_root_notes_by_metadata(
    kb_path: Path,
    search_paths: List[str] = None,
    filters: Dict[str, Any] = None
) -> List[Dict[str, Any]]:
    """
    Find root notes by scanning YAML frontmatter.
    
    Args:
        kb_path: Knowledge base root path
        search_paths: List of directories to search (relative to kb_path)
        filters: Dict of metadata filters (e.g., {"status": "published"})
    
    Returns:
        List of dicts with root note info:
        {
            "path": Path,
            "name": str,
            "material_id": str,
            "category": List[str],
            "status": str,
            ...
        }
    """
    
    if search_paths is None:
        search_paths = ["TCM_Patterns", "Materials", "."]
    
    root_notes = []
    
    for search_dir in search_paths:
        base_path = kb_path / search_dir
        if not base_path.exists():
            continue
        
        # Find all markdown files recursively
        for md_file in base_path.rglob("*.md"):
            try:
                frontmatter = parse_frontmatter(md_file)
                
                # Check if this is a root note
                if frontmatter.get("ocds_type") != "root_note":
                    continue
                
                # Apply filters
                if filters:
                    match = all(
                        frontmatter.get(key) == value 
                        for key, value in filters.items()
                    )
                    if not match:
                        continue
                
                # Extract key info
                root_notes.append({
                    "path": md_file,
                    "name": frontmatter.get("name", md_file.stem),
                    "material_id": frontmatter.get("material_id"),
                    "category": frontmatter.get("category", []),
                    "status": frontmatter.get("status", "unknown"),
                    "source": frontmatter.get("source", "unknown"),
                    "type": frontmatter.get("type"),
                })
                
            except Exception as e:
                # Skip files with invalid frontmatter
                continue
    
    return root_notes


def parse_frontmatter(file_path: Path) -> Dict[str, Any]:
    """
    Parse YAML frontmatter from markdown file.
    
    Args:
        file_path: Path to markdown file
    
    Returns:
        Dict of frontmatter data
    """
    import yaml
    
    content = file_path.read_text(encoding='utf-8')
    
    # Check for frontmatter
    if not content.startswith('---'):
        return {}
    
    # Extract frontmatter
    parts = content.split('---', 2)
    if len(parts) < 3:
        return {}
    
    try:
        frontmatter = yaml.safe_load(parts[1])
        return frontmatter if isinstance(frontmatter, dict) else {}
    except:
        return {}
```

**How it works:**

1. Recursively scans multiple directories
2. Opens each `.md` file
3. Parses YAML frontmatter
4. Checks for `ocds_type: root_note`
5. Applies optional filters (status, category, etc.)
6. Returns rich metadata for each root note

**Pros:**
- ✅ Discovers notes anywhere in vault
- ✅ Rich metadata for filtering/sorting
- ✅ Validates content type
- ✅ Supports complex queries
- ✅ Handles multi-dimensional categorization

**Cons:**
- ❌ Slower (must open every file)
- ❌ Requires metadata discipline
- ❌ More complex implementation
- ❌ Legacy content needs migration

---

### Method 3: Hybrid Approach (Best of Both Worlds)

**Recommended implementation:**

```python
def discover_root_notes(
    kb_path: Path,
    pattern: Optional[str] = None,
    method: str = "hybrid"
) -> List[Dict[str, Any]]:
    """
    Unified root note discovery with multiple methods.
    
    Args:
        kb_path: Knowledge base root path
        pattern: Optional pattern name to search for
        method: "directory" | "metadata" | "hybrid"
    
    Returns:
        List of root note information dicts
    """
    
    if method == "directory":
        return _discover_by_directory(kb_path, pattern)
    elif method == "metadata":
        return _discover_by_metadata(kb_path, pattern)
    else:  # hybrid
        # Try directory first (fast)
        results = _discover_by_directory(kb_path, pattern)
        
        # If found, return immediately
        if results:
            return results
        
        # Fall back to metadata search (thorough)
        return _discover_by_metadata(kb_path, pattern)


def _discover_by_directory(kb_path: Path, pattern: Optional[str]) -> List[Dict]:
    """Fast directory-based search."""
    patterns_dir = kb_path / "TCM_Patterns"
    
    if not patterns_dir.exists():
        return []
    
    # Get all .md files
    pattern_files = list(patterns_dir.rglob("*.md"))
    
    results = []
    for file_path in pattern_files:
        name = file_path.stem.replace("_", " ")
        
        # If pattern specified, filter
        if pattern and pattern.lower() != name.lower():
            continue
        
        results.append({
            "path": file_path,
            "name": name,
            "source": "directory_scan",
            "method": "filename"
        })
    
    return results


def _discover_by_metadata(kb_path: Path, pattern: Optional[str]) -> List[Dict]:
    """Thorough metadata-based search."""
    search_paths = ["TCM_Patterns", "Materials"]
    
    results = []
    for search_dir in search_paths:
        base_path = kb_path / search_dir
        if not base_path.exists():
            continue
        
        for md_file in base_path.rglob("*.md"):
            try:
                frontmatter = parse_frontmatter(md_file)
                
                if frontmatter.get("ocds_type") != "root_note":
                    continue
                
                name = frontmatter.get("name", md_file.stem)
                
                # If pattern specified, filter
                if pattern and pattern.lower() != name.lower():
                    continue
                
                results.append({
                    "path": md_file,
                    "name": name,
                    "material_id": frontmatter.get("material_id"),
                    "category": frontmatter.get("category", []),
                    "source": "metadata_scan",
                    "method": "frontmatter"
                })
            except:
                continue
    
    return results
```

**Benefits:**
- ✅ Fast for common cases (directory)
- ✅ Comprehensive for edge cases (metadata)
- ✅ Configurable via `method` parameter
- ✅ Backward compatible
- ✅ Future-proof

---

## Material Discovery

Once a root note is found, the system must locate associated materials.

### Current Implementation: Naming Convention

```python
# capsule/commands/generate.py:88-96
materials_output_dir = kb_path / output_dir / class_id
pattern_safe = pattern.replace(" ", "_")

potential_files = [
    f"Flashcards_{pattern_safe}.md",
    f"Quiz_{pattern_safe}.md", 
    f"Slides_{pattern_safe}.md",
    f"Conversation_{pattern_safe}.md",
    f"Study_Material_{pattern_safe}.md",
    f"Root_Note_{pattern_safe}.md"
]

for filename in potential_files:
    file_path = materials_output_dir / filename
    if file_path.exists():
        existing_materials.append(filename)
```

**Pros:**
- ✅ Simple
- ✅ Fast
- ✅ Predictable

**Cons:**
- ❌ Fragile (rename breaks links)
- ❌ Limited to single location
- ❌ No material reuse across classes

---

### Recommended: Metadata Linking

```python
def find_materials_for_root_note(
    root_note_path: Path,
    kb_path: Path,
    material_types: List[str] = None
) -> Dict[str, Path]:
    """
    Find all materials associated with a root note.
    
    Args:
        root_note_path: Path to root note
        kb_path: Knowledge base root
        material_types: List of types to find (flashcards, quiz, etc.)
    
    Returns:
        Dict mapping material type to file path
    """
    
    if material_types is None:
        material_types = ["flashcards", "quiz", "slides", "study_material", "conversation"]
    
    # Get root note metadata
    root_frontmatter = parse_frontmatter(root_note_path)
    material_id = root_frontmatter.get("material_id")
    
    if not material_id:
        # Fall back to filename-based search
        return _find_materials_by_filename(root_note_path)
    
    # Search for materials with matching material_id
    materials = {}
    
    # Check same directory first (fast path)
    same_dir = root_note_path.parent
    for mat_type in material_types:
        for md_file in same_dir.glob("*.md"):
            frontmatter = parse_frontmatter(md_file)
            
            if (frontmatter.get("ocds_type") == mat_type and
                frontmatter.get("material_id") == material_id):
                materials[mat_type] = md_file
                break
    
    # Search broader if needed
    if len(materials) < len(material_types):
        materials_dir = kb_path / "Materials"
        for md_file in materials_dir.rglob("*.md"):
            frontmatter = parse_frontmatter(md_file)
            
            mat_type = frontmatter.get("ocds_type")
            if (mat_type in material_types and
                mat_type not in materials and
                frontmatter.get("material_id") == material_id):
                materials[mat_type] = md_file
    
    return materials
```

**Benefits:**
- ✅ Location-independent
- ✅ Survives renames
- ✅ Enables material reuse
- ✅ Supports versioning

---

## Configuration

### User-Facing Config

```yaml
# ~/.config/capsule/config.yaml

search:
  method: "hybrid"                    # directory | metadata | hybrid
  
  directories:
    - "TCM_Patterns"                 # Primary curated content
    - "Materials"                    # Generated content
    - "Research"                     # Research outputs
  
  recursive: true                    # Search subdirectories
  
  filters:
    status: ["published", "draft"]   # Only show these statuses
    source: null                     # null = all sources
  
  cache:
    enabled: true                    # Cache discovery results
    ttl: 300                         # Cache for 5 minutes
```

### CLI Usage

```bash
# Use default (hybrid) method
cap list

# Force directory-only search (fast)
cap list --method directory

# Force metadata search (comprehensive)
cap list --method metadata

# Filter by status
cap list --status published

# Filter by category
cap list --category "Zang Fu"

# Show all info
cap list --verbose
```

---

## Performance Considerations

### Directory Scan Performance

```
Small vault (100 patterns):    ~10ms
Medium vault (1,000 patterns): ~50ms
Large vault (10,000 patterns): ~500ms
```

**Optimization:**
- Use `glob()` instead of `os.walk()`
- Limit recursion depth
- Skip hidden directories

---

### Metadata Scan Performance

```
Small vault (100 patterns):    ~200ms
Medium vault (1,000 patterns): ~2s
Large vault (10,000 patterns): ~20s
```

**Optimization:**
- Cache results with TTL
- Index on startup (background)
- Only scan modified files
- Use SQLite for large vaults

---

### Caching Strategy

```python
import time
import hashlib
from pathlib import Path
from typing import Dict, List

class RootNoteCache:
    """Cache for root note discovery results."""
    
    def __init__(self, cache_dir: Path, ttl: int = 300):
        self.cache_dir = cache_dir
        self.ttl = ttl
        self.cache_dir.mkdir(parents=True, exist_ok=True)
    
    def get(self, kb_path: Path, method: str) -> Optional[List[Dict]]:
        """Get cached results if valid."""
        cache_key = self._cache_key(kb_path, method)
        cache_file = self.cache_dir / f"{cache_key}.json"
        
        if not cache_file.exists():
            return None
        
        # Check age
        age = time.time() - cache_file.stat().st_mtime
        if age > self.ttl:
            cache_file.unlink()  # Delete stale cache
            return None
        
        # Load cache
        import json
        return json.loads(cache_file.read_text())
    
    def set(self, kb_path: Path, method: str, results: List[Dict]):
        """Store results in cache."""
        cache_key = self._cache_key(kb_path, method)
        cache_file = self.cache_dir / f"{cache_key}.json"
        
        import json
        cache_file.write_text(json.dumps(results, default=str))
    
    def _cache_key(self, kb_path: Path, method: str) -> str:
        """Generate cache key."""
        key_str = f"{kb_path}:{method}"
        return hashlib.md5(key_str.encode()).hexdigest()
```

---

## Migration Path

### Phase 1: Add Metadata (No Breaking Changes)

1. Add `ocds_type` to existing patterns
2. Keep directory-based discovery as default
3. Add `--method metadata` flag for testing

```bash
# Script to add metadata
python scripts/add_ocds_metadata.py
```

---

### Phase 2: Hybrid Default (Recommended)

1. Switch default to `hybrid` method
2. Directory scan for curated content (fast)
3. Metadata scan for research outputs (comprehensive)

```yaml
# New default config
search:
  method: "hybrid"
```

---

### Phase 3: Full Metadata (Future)

1. All content has proper metadata
2. Metadata scan becomes primary
3. Directory structure optional (organization only)

---

## Testing Strategy

### Unit Tests

```python
def test_directory_discovery():
    """Test directory-based discovery."""
    kb_path = Path("test_vault")
    results = _discover_by_directory(kb_path, "Heart Blood Deficiency")
    assert len(results) == 1
    assert results[0]["name"] == "Heart Blood Deficiency"


def test_metadata_discovery():
    """Test metadata-based discovery."""
    kb_path = Path("test_vault")
    results = _discover_by_metadata(kb_path, "Impotence")
    assert len(results) >= 1
    assert all(r["method"] == "frontmatter" for r in results)


def test_hybrid_discovery():
    """Test hybrid discovery."""
    kb_path = Path("test_vault")
    
    # Should find curated patterns (directory)
    results = discover_root_notes(kb_path, "Heart Blood Deficiency")
    assert len(results) >= 1
    
    # Should find research outputs (metadata)
    results = discover_root_notes(kb_path, "Impotence")
    assert len(results) >= 1
```

---

### Integration Tests

```bash
# Test full workflow
cap research "Test Pattern" --deep
cap list  # Should show "Test Pattern"
cap chat "Test Pattern"  # Should load successfully
```

---

## Future Enhancements

### 1. Full-Text Search

```python
def search_root_notes(query: str, kb_path: Path) -> List[Dict]:
    """Search root note content, not just names."""
    # Use ripgrep or similar for fast full-text search
```

### 2. Fuzzy Semantic Search

```python
def semantic_search(query: str, kb_path: Path) -> List[Dict]:
    """Find root notes by meaning, not exact match."""
    # Use embeddings for semantic similarity
```

### 3. GraphQL-style Queries

```python
results = query_root_notes("""
{
  rootNotes(
    category: "Zang Fu"
    status: "published"
    tags: ["deficiency", "heart"]
  ) {
    name
    path
    materials {
      flashcards
      quiz
    }
  }
}
""")
```

---

## Summary

### Current State
- ✅ Directory-based discovery works
- ✅ Simple and fast
- ❌ Limited flexibility
- ❌ Poor discoverability for generated content

### Recommended Path
1. Add metadata to existing patterns (non-breaking)
2. Implement hybrid discovery (backward compatible)
3. Gradually transition to metadata-first

### Key Benefits
- 🎯 Flexibility in organization
- 🎯 Discoverability across vault
- 🎯 Rich metadata for filtering
- 🎯 Future-proof architecture

---

**Related Documentation:**
- `README.md` - Folder structure overview
- `03_Data_Standards/Frontmatter_Schema.md` - Metadata specification
- `06_Automation_Scripts/Script_Overview.md` - Automation implementation

---

*Last updated: 2025-11-10*  
*Version: 1.0.0*
