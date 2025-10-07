# 🤝 Contributing to TCM Knowledge Base

Thank you for your interest in contributing! This project thrives on community collaboration.

---

## 📋 Table of Contents

1. [Code of Conduct](#-code-of-conduct)
2. [How Can I Contribute?](#-how-can-i-contribute)
3. [Content Guidelines](#-content-guidelines)
4. [Technical Guidelines](#-technical-guidelines)
5. [Workflow](#-workflow)
6. [Review Process](#-review-process)

---

## 🌟 Code of Conduct

### Our Pledge

We are committed to providing a welcoming, inclusive, and harassment-free environment for everyone, regardless of:
- Background or experience level
- Educational background (formal TCM training or self-taught)
- Lineage or school of thought
- Geographic location or cultural background

### Expected Behavior

- **Be respectful** - Acknowledge different perspectives and schools of thought
- **Be constructive** - Provide helpful feedback, not just criticism
- **Be collaborative** - Work together to improve the knowledge base
- **Be accurate** - Cite sources and acknowledge uncertainty when appropriate
- **Be open-minded** - TCM has many valid interpretations and approaches

### Unacceptable Behavior

- Harassment, discrimination, or personal attacks
- Deliberate misinformation or plagiarism
- Promoting dangerous or unethical practices
- Spam or self-promotion without educational value

---

## 💡 How Can I Contribute?

### 1. 📝 Content Contributions

#### Add New Entities
- **Herbs** - Add missing herbs with properties, functions, combinations
- **Points** - Complete point descriptions, add clinical notes
- **Diseases** - Add disease patterns, treatment protocols
- **Formulas** - Classical and modern herbal formulas
- **Concepts** - Diagnostic methods, theoretical frameworks

#### Improve Existing Content
- **Clarifications** - Make complex concepts easier to understand
- **Examples** - Add clinical case examples
- **Citations** - Add references to classical texts or modern research
- **Corrections** - Fix errors, update outdated information
- **Translations** - Improve pinyin, hanzi, or English translations

#### Add Multimedia
- **Diagrams** - Point locations, meridian pathways
- **Images** - Herb identification photos
- **Tables** - Comparison charts, differential diagnosis

### 2. 🔗 Relationship Building
- Add cross-links between related entities
- Identify herb-disease relationships
- Document point-disease treatment protocols
- Connect symptoms to patterns

### 3. 🔧 Technical Contributions
- Improve automation scripts
- Build visualization tools
- Create data analysis utilities
- Develop export/import functions
- Write unit tests

### 4. 📚 Documentation
- Improve README or CONTRIBUTING guides
- Write tutorials or how-to guides
- Create study guides or learning paths
- Document workflows and processes

### 5. 🐛 Bug Reports & Feature Requests
- Report errors or inconsistencies
- Suggest new features or improvements
- Identify missing content areas

---

## 📖 Content Guidelines

### Universal Data Format

All content uses YAML frontmatter + Markdown body:

```markdown
---
# Core Metadata
id: "entity-YYYYMMDDHHMMSS"
name: "Entity Name"
type: "herb|point|disease|concept|technique|formula"
aliases: ["Alternative Name 1", "Alternative Name 2"]
tags: [TCM, Category, Subcategory]

# Cross-Link Fields
category: ["Primary Category"]
related: ["Related Entity 1", "Related Entity 2"]
symptoms: []
patterns: []
western_conditions: []
formulas: []
herbs: []
points: []
nutrition: []
tests: []

# Entity-Specific Data
[entity]_data:
  # Varies by entity type
---

# Markdown content below...
```

### Content Standards

#### ✅ DO:
- **Cite sources** - Reference textbooks, research papers, classical texts
- **Use standardized terminology** - Follow Wiseman/Ye conventions when possible
- **Be precise** - Distinguish between similar concepts
- **Acknowledge variations** - Different schools may have different interpretations
- **Include contraindications** - Safety information is critical
- **Use wikilinks** - Connect to related entities using `[[Entity Name]]`

#### ❌ DON'T:
- Copy copyrighted content verbatim without permission
- Make unsupported medical claims
- Promote specific products or services
- Include personally identifiable patient information
- Use inflammatory or divisive language about different TCM traditions

### Writing Style

- **Clear and concise** - Avoid unnecessary jargon
- **Educational tone** - Write for learners and practitioners
- **Neutral perspective** - Present information objectively
- **Active voice** - "This point treats headache" vs "Headache is treated by..."
- **Consistent formatting** - Follow existing examples

### Citation Format

Use inline citations:
```markdown
According to Maciocia (2015), Liver Blood deficiency commonly manifests with...

**Source:** Maciocia, G. (2015). *The Foundations of Chinese Medicine* (3rd ed.). Elsevier.
```

Or reference section:
```markdown
## References

1. Bensky, D., Clavey, S., & Stöger, E. (2004). *Chinese Herbal Medicine: Materia Medica* (3rd ed.).
2. Deadman, P., & Al-Khafaji, M. (2007). *A Manual of Acupuncture*.
```

---

## 🛠️ Technical Guidelines

### File Naming Conventions

- **Use underscores** for spaces: `Wind_Stroke.md` not `Wind Stroke.md`
- **Match the entity name**: File name should match the `name:` field
- **No special characters**: Avoid `/`, `\`, `:`, `*`, `?`, `"`, `<`, `>`, `|`

### YAML Frontmatter Rules

- **Always include required fields**: `id`, `name`, `type`, `tags`
- **Use consistent date format**: `YYYY-MM-DD`
- **Quote strings with special characters**: `name: "Boil and Red-Thread Boil"`
- **Use arrays for lists**: `aliases: ["Name1", "Name2"]`
- **Maintain cross-link fields** even if empty: `herbs: []`

### Markdown Body Standards

- **Use heading hierarchy**: `##` for sections, `###` for subsections
- **Include emoji headers** for visual navigation: `## 📖 Overview`
- **Create tables** for structured data (indications, dosages, etc.)
- **Use code blocks** for formulas or recipes

### Script Contributions

- **Follow PEP 8** for Python code
- **Add docstrings** for all functions
- **Include type hints** where applicable
- **Write unit tests** for new features
- **Update requirements.txt** if adding dependencies

---

## 🔄 Workflow

### Fork & Clone

```bash
# 1. Fork the repository on GitHub

# 2. Clone your fork
git clone https://github.com/YOUR_USERNAME/TCM_Knowledge_Base.git
cd TCM_Knowledge_Base

# 3. Add upstream remote
git remote add upstream https://github.com/ORIGINAL_OWNER/TCM_Knowledge_Base.git
```

### Create a Branch

```bash
# Create a descriptive branch name
git checkout -b add-herb-huang-qi
# or
git checkout -b fix-typo-wind-stroke
# or
git checkout -b improve-point-linker-script
```

### Make Changes

1. **Edit or create files** in your branch
2. **Test your changes** (run scripts if applicable)
3. **Preview in Obsidian** to ensure formatting is correct

### Commit Your Changes

```bash
# Stage your changes
git add TCM_Herbs/Huang_Qi.md

# Commit with a clear message
git commit -m "Add Huang Qi (Astragalus) herb entry

- Added full herb profile with properties
- Included clinical applications
- Added contraindications and dosage info
- Linked to related formulas"
```

**Commit Message Guidelines:**
- **First line**: Brief summary (50 chars or less)
- **Blank line**
- **Body**: Detailed description of what and why
- **Use bullet points** for multiple changes

### Push & Create Pull Request

```bash
# Push your branch
git push origin add-herb-huang-qi
```

Then on GitHub:
1. Click "Compare & pull request"
2. Fill out the PR template
3. Link any related issues
4. Request review from maintainers

---

## 🔍 Review Process

### What Reviewers Look For

1. **Accuracy** - Is the information correct?
2. **Completeness** - Are all required fields filled?
3. **Formatting** - Does it follow the template?
4. **Citations** - Are sources provided?
5. **Safety** - Are contraindications mentioned?
6. **Consistency** - Does it match existing style?

### Review Workflow

1. **Maintainer review** - Initial check for quality and accuracy
2. **Community feedback** - Other contributors may comment
3. **Revisions** - You may be asked to make changes
4. **Approval** - Once approved, PR will be merged
5. **Merge** - Your contribution is now part of the knowledge base!

### Response Times

- **First response**: Within 7 days
- **Full review**: Within 14 days
- **Urgent fixes** (safety issues): Within 24 hours

If you haven't heard back, feel free to ping the PR!

---

## 🎓 Learning Resources

### New to Git/GitHub?

- [GitHub Docs: Fork a Repo](https://docs.github.com/en/get-started/quickstart/fork-a-repo)
- [GitHub Docs: Creating a Pull Request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request)
- [Oh Shit, Git!?!](https://ohshitgit.com/) - Fixing common mistakes

### New to Obsidian?

- [Obsidian Help Docs](https://help.obsidian.md/)
- [Markdown Guide](https://www.markdownguide.org/)

### New to TCM?

Start by reading existing entries and contributing small improvements before adding major new content.

---

## 📞 Questions?

- **General questions**: Open a [Discussion](https://github.com/ORIGINAL_OWNER/TCM_Knowledge_Base/discussions)
- **Bug reports**: Open an [Issue](https://github.com/ORIGINAL_OWNER/TCM_Knowledge_Base/issues)
- **Unclear guidelines**: Ask in your PR or open an issue

---

## 🙏 Thank You!

Every contribution, no matter how small, helps build a better resource for the TCM community.

**Together, we're building the Wikipedia of Traditional Chinese Medicine!**

---

*Last Updated: October 2025*
