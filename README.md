# 🌿 TCM Knowledge Base

> **An open-source, community-driven Traditional Chinese Medicine knowledge base**
>
> Built for students, practitioners, researchers, and anyone interested in TCM.

[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)
[![Status: Active Development](https://img.shields.io/badge/Status-Active%20Development-green.svg)]()

---

## 📖 What is This?

The TCM Knowledge Base is a **collaborative, Wikipedia-style repository** of Traditional Chinese Medicine knowledge, designed to be:

- **📚 Comprehensive** - Covering herbs, acupuncture points, diseases, diagnostic concepts, and treatment techniques
- **🔗 Interconnected** - All entities are cross-linked, forming a rich knowledge graph
- **🤝 Community-Driven** - Open for contributions, corrections, and improvements from the TCM community
- **🔬 Research-Friendly** - Structured data format enables analysis, pattern discovery, and AI integration
- **💻 Practitioner-Focused** - Designed for clinical use, academic study, and reference

---

## 📊 Current Contents

| Category | Count | Description |
|----------|-------|-------------|
| 🌿 **Herbs** | 240 | Single herbs with properties, functions, indications |
| 📍 **Acupuncture Points** | 361 | All major points with locations, functions, indications |
| 🩺 **Diseases** | 29 | Disease patterns with etiology, treatment protocols |
| 📖 **Concepts** | 17 | Diagnostic methods, syndrome differentiation, pathogenic factors |
| ⚡ **Techniques** | 10 | Needling methods, moxibustion, treatment principles |

### 🔗 Knowledge Graph Statistics

- **133 total relationships** created through automated cross-linking
- **95 Concept→Disease** connections
- **38 Point→Disease** treatment relationships
- **Average 4.6 connections** per disease entity

---

## 🗂️ Repository Structure

```
TCM_Knowledge_Base/
├── TCM_Concepts/           # Diagnostic concepts & pathogenic factors
├── TCM_Diseases/           # Disease patterns with treatment protocols
├── TCM_Points/             # Acupuncture point database
├── TCM_Points_Images/      # Point location diagrams
├── TCM_Herbs/              # Single herb materia medica
├── TCM_Techniques/         # Treatment techniques & methods
├── scripts/                # Automation & analysis tools
│   ├── auto_linker.py                    # Concept-disease linker
│   ├── point_disease_linker.py           # Point-disease linker
│   ├── herb_disease_linker.py            # Herb-disease linker
│   └── generate_phase1_statistics.py     # Knowledge graph stats
├── README.md               # This file
├── CONTRIBUTING.md         # Contribution guidelines
└── LICENSE                 # CC BY-SA 4.0 License
```

---

## 🚀 Getting Started

### For Students & Practitioners

1. **Clone the repository:**
   ```bash
   git clone https://github.com/[your-username]/TCM_Knowledge_Base.git
   ```

2. **Open in Obsidian:**
   - Download [Obsidian](https://obsidian.md/)
   - Open the `TCM_Knowledge_Base` folder as a vault
   - Explore the interconnected knowledge graph!

3. **Browse & Search:**
   - Use graph view to visualize relationships
   - Search for symptoms, herbs, points, or diseases
   - Follow wikilinks to explore connections

### For Contributors

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines on:
- Adding new content
- Improving existing entries
- Submitting corrections
- Code contributions

### For Developers

**Run automated linking:**
```bash
cd scripts/
python3 auto_linker.py              # Link concepts to diseases
python3 point_disease_linker.py     # Link points to diseases
python3 herb_disease_linker.py      # Link herbs to diseases
```

**Generate statistics:**
```bash
python3 generate_phase1_statistics.py
```

---

## 🎯 Project Vision

### Phase 1: Automated Cross-Linking ✅ **COMPLETE**
- [x] Extract content from authoritative TCM textbooks
- [x] Build automated relationship detection
- [x] Create bidirectional wikilinks between entities
- [x] Generate knowledge graph statistics

### Phase 2: Semantic Analysis & Insights 🚧 **IN PROGRESS**
- [ ] Pattern clustering (similar diseases, herb combinations)
- [ ] Diagnostic decision trees
- [ ] Treatment protocol generator
- [ ] Contraindication checker

### Phase 3: Knowledge Graph & Visualization
- [ ] Interactive web-based knowledge graph
- [ ] Pathway analysis (symptom → diagnosis → treatment)
- [ ] Visual relationship explorer
- [ ] Export to standard graph formats (GraphML, Cytoscape)

### Phase 4: AI-Powered Clinical Assistant
- [ ] Natural language query interface
- [ ] Case study analyzer
- [ ] Differential diagnosis suggestions
- [ ] Formula customization recommendations

### Phase 5: Learning & Evolution System
- [ ] Community-contributed case database
- [ ] Pattern learning from clinical outcomes
- [ ] Automated content updates
- [ ] Peer review workflow

---

## 🤝 How to Contribute

We welcome contributions from:
- **TCM Students** - Add study notes, clarifications, examples
- **Practitioners** - Share clinical insights, case studies, practical tips
- **Researchers** - Contribute modern research, citations, correlations
- **Translators** - Improve translations, add multilingual support
- **Developers** - Build tools, improve automation, create visualizations

**Getting Started:**
1. Read [CONTRIBUTING.md](CONTRIBUTING.md)
2. Fork the repository
3. Make your changes in a new branch
4. Submit a pull request
5. Engage in peer review discussion

---

## 📜 License

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).

**You are free to:**
- ✅ **Share** - Copy and redistribute the material
- ✅ **Adapt** - Remix, transform, and build upon the material
- ✅ **Commercial Use** - Use for any purpose, even commercially

**Under the following terms:**
- **Attribution** - Give appropriate credit and indicate if changes were made
- **ShareAlike** - Distribute your contributions under the same license

---

## 🙏 Acknowledgments

### Source Texts
- **Chinese Acupuncture and Moxibustion** (Cheng Xinnong, 1987)
- **Chinese Herbal Medicine: Materia Medica** (Bensky & Gamble, 3rd Edition)
- Additional classical and modern TCM texts

### Inspiration
Built with the vision of creating a **"Wikipedia for TCM"** - a living, collaborative knowledge base that grows and improves through community contribution.

### Technology
- **Obsidian** - Knowledge management platform
- **Python** - Automation and analysis
- **Markdown** - Universal, portable format
- **Git** - Version control and collaboration
- **AI** - Content extraction and structuring (Google Gemini)

---

## 📞 Contact & Community

- **Issues & Bug Reports:** [GitHub Issues](https://github.com/[your-username]/TCM_Knowledge_Base/issues)
- **Discussions & Questions:** [GitHub Discussions](https://github.com/[your-username]/TCM_Knowledge_Base/discussions)
- **Feature Requests:** [GitHub Issues](https://github.com/[your-username]/TCM_Knowledge_Base/issues)

---

## 🌟 Star History

If you find this project useful, please consider starring it on GitHub! ⭐

---

**Built with ❤️ by the TCM community, for the TCM community**

*Last Updated: October 2025*
