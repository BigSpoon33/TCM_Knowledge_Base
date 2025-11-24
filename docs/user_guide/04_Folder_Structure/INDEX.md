# 04 - Folder Structure Documentation

**Version:** 1.0.0  
**Last Updated:** 2025-11-10  
**Status:** Complete ✅

---

## Overview

This section documents the folder structure, organization strategies, and content discovery systems for OCDS. It provides guidance for organizing educational content at any scale, from individual practitioners to large institutions.

---

## Documents in This Section

### 1. [README.md](README.md) - Comprehensive Folder Structure Guide
**Purpose:** Complete overview of OCDS folder architecture

**Key Topics:**
- Complete vault structure breakdown
- Core folder purposes and conventions
- Root note discovery system
- Material linking mechanisms
- Capsule CLI integration
- Configuration reference
- Best practices by role (creator/student/developer)
- Migration guides

**Audience:** Everyone (start here!)

**Read Time:** 30 minutes

---

### 2. [Root_Note_Discovery.md](Root_Note_Discovery.md) - Technical Discovery System
**Purpose:** Deep dive into how Capsule finds and validates root notes

**Key Topics:**
- Discovery algorithms (directory vs metadata vs hybrid)
- Performance optimization
- Caching strategies
- Material linking implementation
- Testing strategies
- Future enhancements (semantic search, GraphQL queries)

**Audience:** Developers, advanced users

**Read Time:** 25 minutes

---

### 3. [Organization_Strategies.md](Organization_Strategies.md) - Practical Organization Patterns
**Purpose:** Real-world organizational patterns for different use cases

**Key Topics:**
- Course creator workflow (hierarchical source library)
- Student workflow (class-centric organization)
- Institution workflow (multi-instructor repository)
- Research/AI workflow (flat with rich metadata)
- Migration strategies
- Real-world examples

**Audience:** Course creators, instructors, students

**Read Time:** 30 minutes

---

## Quick Reference

### For Course Creators

1. **Start:** [Organization_Strategies.md#for-course-creators](Organization_Strategies.md#for-course-creators)
2. **Understand:** [README.md#core-folder-architecture](README.md#core-folder-architecture)
3. **Implement:** Hierarchical source library in `TCM_Patterns/`
4. **Generate:** Materials to `Materials/{class_id}/`

---

### For Students

1. **Start:** [Organization_Strategies.md#for-students](Organization_Strategies.md#for-students)
2. **Understand:** [README.md#capsule-cli-integration](README.md#capsule-cli-integration)
3. **Import:** Class packages with `cap import`
4. **Study:** Keep personal notes separate from class materials

---

### For Developers

1. **Start:** [Root_Note_Discovery.md](Root_Note_Discovery.md)
2. **Understand:** Directory vs metadata discovery
3. **Implement:** Hybrid discovery for flexibility
4. **Optimize:** Caching and indexing strategies

---

### For Researchers

1. **Start:** [Organization_Strategies.md#for-research--ai-generation](Organization_Strategies.md#for-research--ai-generation)
2. **Understand:** Flat organization with rich metadata
3. **Generate:** Content with `cap research --deep`
4. **Validate:** Review workflow before publishing

---

## Key Concepts

### Folder Organization Philosophy

The OCDS system supports **multiple organizational strategies** simultaneously:

1. **Hierarchical** (directories) - Good for browsing, curriculum structure
2. **Tagged** (metadata) - Good for filtering, cross-categorization
3. **Hybrid** (both) - Best of both worlds (recommended!)

### Content Flow

```
Research/Generation → Validation → Curation → Packaging → Distribution
        ↓                ↓            ↓           ↓            ↓
    Materials/      Review Queue  TCM_Patterns/  Build     Student
    Project_X/                                   Class     Import
```

### Discovery Methods

| Method | Speed | Coverage | Flexibility | Use Case |
|--------|-------|----------|-------------|----------|
| **Directory** | Fast | Limited | Low | Curated content |
| **Metadata** | Slow | Complete | High | Generated content |
| **Hybrid** | Fast* | Complete | High | Production (recommended) |

*Fast for common cases (directory hit), comprehensive for edge cases (metadata fallback)

---

## Common Patterns

### Pattern 1: Source Library + Generated Materials

```
TCM_Patterns/          ← Curated, reviewed, version-controlled
    └── [Hierarchical organization]

Materials/             ← Generated, class-specific, ephemeral
    └── {class_id}/
        └── [Auto-generated from TCM_Patterns/]
```

**When:** Course creation, content distribution

---

### Pattern 2: Flat with Rich Metadata

```
Generated_Content/     ← Flat folder structure
    ├── Pattern_A.md   ← Rich frontmatter metadata
    ├── Pattern_B.md   ← Tags for categorization
    └── Pattern_C.md   ← Discovery via metadata
```

**When:** AI generation, research, exploratory

---

### Pattern 3: Multi-Layer with Shared Library

```
Content_Library/       ← Shared across institution
    └── [Canonical source]

Instructors/           ← Per-instructor customization
    └── {instructor}/
        └── {semester}/

Student_Deployments/   ← Packaged distributions
    └── {semester}/
```

**When:** Institutional deployment, multiple instructors

---

## Configuration

### Key Config Settings

```yaml
# ~/.config/capsule/config.yaml

paths:
  knowledge_base: "/path/to/vault"
  output_dir: "Materials"               # Where generated content goes
  pattern_dirs:                         # Where to find root notes
    - "TCM_Patterns"
    - "Materials"

search:
  method: "hybrid"                      # directory | metadata | hybrid
  recursive: true                       # Search subdirectories
  cache:
    enabled: true
    ttl: 300                           # 5 minute cache
```

### CLI Commands

```bash
# List all root notes
cap list

# Generate materials from root note
cap generate "Pattern Name" --class-id TCM_101

# Research new topic (generates root note + materials)
cap research "New Topic" --deep

# Start guided conversation
cap chat "Pattern Name"

# Configure paths
cap config set paths.knowledge_base "/path/to/vault"
cap config set paths.output_dir "Materials"
```

---

## Metadata Standards

### Essential Frontmatter

Every root note should have:

```yaml
---
ocds_type: "root_note"                 # Enables discovery
material_id: "unique-identifier"       # Links materials
name: "Display Name"                   # Human-readable name
type: "pattern"                        # Content type
category: ["Category 1", "Category 2"] # Hierarchical categories
tags: ['tag1', 'tag2']                # Flat tags
status: "published"                    # Lifecycle status
source: "curated"                      # Provenance
---
```

**See:** `03_Data_Standards/Frontmatter_Schema.md` for complete schema

---

## Migration Checklist

### Moving to OCDS Folder Structure

- [ ] Identify your use case (creator/student/institution/research)
- [ ] Choose organization strategy
- [ ] Create folder structure
- [ ] Add metadata to existing content
- [ ] Test discovery with `cap list`
- [ ] Configure Capsule CLI paths
- [ ] Generate sample materials
- [ ] Validate workflows

**See:** [README.md#migration-guide](README.md#migration-guide) for detailed steps

---

## Troubleshooting

### "Pattern not found"

1. Check `cap config get paths.knowledge_base`
2. Verify file exists: `ls TCM_Patterns/`
3. Try: `cap list` to see all discoverable patterns
4. Check filename matches pattern name
5. Try adding metadata: `ocds_type: root_note`

---

### "Materials generation failed"

1. Check root note has valid frontmatter
2. Verify output directory writable
3. Check `cap config get paths.output_dir`
4. Try: `cap config set paths.output_dir "Materials"`

---

### "Discovery is slow"

1. Enable caching: `cap config set search.cache.enabled true`
2. Use directory method for curated content
3. Limit search paths: `cap config set search.directories '["TCM_Patterns"]'`
4. Consider indexing for large vaults (1000+ patterns)

---

## Best Practices Summary

### Do's ✅

- ✅ Use consistent metadata across all root notes
- ✅ Separate source (`TCM_Patterns/`) from generated (`Materials/`)
- ✅ Version control your source library
- ✅ Use tags for flexible categorization
- ✅ Link to root notes, don't duplicate content
- ✅ Choose organization that fits your scale

### Don'ts ❌

- ❌ Don't mix curated and generated content
- ❌ Don't nest folders more than 3-4 levels deep
- ❌ Don't use spaces in folder names (use underscores)
- ❌ Don't modify generated materials manually (regenerate instead)
- ❌ Don't ignore metadata (limits discoverability)
- ❌ Don't premature optimize (start simple, scale later)

---

## Related Documentation

### Within This Section
- [README.md](README.md) - Main folder structure guide
- [Root_Note_Discovery.md](Root_Note_Discovery.md) - Discovery system
- [Organization_Strategies.md](Organization_Strategies.md) - Practical patterns

### Related Sections
- `01_System_Overview/README.md` - OCDS architecture
- `03_Data_Standards/Frontmatter_Schema.md` - Metadata specification
- `05_Material_Templates/Root_Note_Template.md` - Root note format
- `06_Automation_Scripts/Script_Overview.md` - Automation tools
- `12_Best_Practices/Content_Organization.md` - Organization best practices

---

## Feedback & Contributions

This documentation is a living resource. Contributions welcome:

- **Found an error?** Submit an issue
- **Have a use case not covered?** Share your organizational strategy
- **Improved a workflow?** Contribute documentation
- **Built tooling?** Share scripts and automation

---

## Document History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2025-11-10 | Initial comprehensive documentation |

---

## Summary

The OCDS folder structure supports **flexibility** while maintaining **discoverability**:

- 📁 **Directories** provide visual organization and fast scanning
- 🏷️ **Tags** enable flexible categorization and filtering
- 🔍 **Hybrid discovery** gives best of both worlds
- 🎯 **Multiple strategies** support different use cases
- 🚀 **Scales** from individual practitioners to large institutions

**Key insight:** Organization is about **purpose**, not just **structure**. The same content can live in different locations depending on its stage (research → validation → curation → distribution) and audience (creator → instructor → student).

---

*Last updated: 2025-11-10*  
*Version: 1.0.0*  
*Status: Complete ✅*
