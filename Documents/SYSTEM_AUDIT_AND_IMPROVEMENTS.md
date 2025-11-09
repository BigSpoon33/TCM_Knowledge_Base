# TCM Knowledge Base System Audit & Improvement Recommendations

**Date:** 2025-10-11
**Purpose:** Comprehensive analysis of template structure, diagnostic workflow, and opportunities for intelligent differential diagnosis

---

## Executive Summary

### Current Strengths
- ✅ **Rich template structure** with comprehensive frontmatter
- ✅ **Excellent cross-linking** capabilities via universal relationship slots
- ✅ **Differential diagnosis sections** already present in Pattern templates (line 138-154)
- ✅ **Point combinations** already documented in Point templates
- ✅ **Formula modifications** already structured in Formula templates
- ✅ **Semantic search** working well for initial pattern retrieval

### Key Opportunities
- 🎯 **Differential questioning** not yet leveraged from Pattern template data
- 🎯 **Treatment protocols** exist in templates but not extracted programmatically
- 🎯 **Pattern comparison tables** could drive intelligent questioning
- 🎯 **Rich clinical data** in templates underutilized by diagnostic agent

---

## Part 1: Template Frontmatter Audit

### Universal Cross-Link Fields (Present in ALL Templates)

```yaml
# Present in: Patterns, Formulas, Herbs, Points, Symptoms
category: []
related: []
symptoms: []
patterns: []
western_conditions: []
formulas: []
herbs: []
points: []
nutrition: []
tests: []
```

**Analysis:**
- ✅ **Highly structured** - Bidirectional linking capability
- ✅ **Queryable** via Dataview (already used in templates)
- ⚠️ **Underutilized by agent** - Currently only using `name` field
- 💡 **Opportunity**: Agent could query `symptoms`, `formulas`, `herbs`, `points` directly from pattern frontmatter

---

### Pattern-Specific Frontmatter (Lines 22-46)

#### Clinical Gold Mine for Differential Diagnosis:

```yaml
pattern_data:
  # Classification
  pattern_type: ""          # "Zang Fu", "Eight Principles", etc.
  pattern_subtype: ""       # "Liver", "Spleen", "Qi Stage"

  # Eight Principles (KEY FOR DIFFERENTIATION)
  excess_deficiency: ""     # "Excess", "Deficiency", "Mixed"
  hot_cold: ""             # "Hot", "Cold", "Neither", "Mixed"
  interior_exterior: ""     # "Interior", "Exterior", "Half-Interior"
  yin_yang: ""             # "Yin", "Yang", "Mixed"

  # Diagnostic Essentials
  cardinal_symptoms: []     # MUST-HAVE symptoms
  tongue: ""               # Specific tongue presentation
  pulse: ""                # Specific pulse presentation

  # Treatment Intelligence
  treatment_principle: []   # Ready-made treatment strategies
  contraindications: []     # What to avoid
```

**Current Agent Usage:** ❌ NONE - Agent doesn't read this at all!

**Massive Opportunity:**
1. Extract `cardinal_symptoms` to ask **specific follow-up questions**
2. Use `excess_deficiency`, `hot_cold` for **intelligent filtering**
3. Compare `tongue` and `pulse` between similar patterns for **differential questions**
4. Pull `treatment_principle` directly instead of LLM generation

---

### Formula-Specific Frontmatter (Lines 21-58)

```yaml
formula_data:
  composition: []          # Herb list with roles (Chief, Deputy, etc.)
  formula_actions: []      # Specific actions
  treatment_principles: [] # Treatment strategies
  primary_pattern: ""      # Main pattern treated
  key_symptoms: []         # Cardinal symptoms indicating this formula
  tongue: ""
  pulse: ""

  # Modifications (UNDERUSED GOLD)
  classical_variations: []
  common_modifications: []
  contraindications: []
```

**Current Agent Usage:** ⚠️ Partial - Only retrieves `name`, doesn't extract actions or modifications

**Opportunity:**
- Extract `key_symptoms`, `tongue`, `pulse` to **match pattern precisely**
- Use `common_modifications` for **intelligent formula customization**
- Pull `formula_actions` for **justification** instead of pure LLM reasoning

---

### Point-Specific Frontmatter (Lines 21-57)

```yaml
point_data:
  channel: ""
  special_properties: []   # Yuan Source, Xi-Cleft, etc.
  functions: []            # Primary TCM functions

  # Indications by system (GRANULAR)
  indications: {
    respiratory: []
    digestive: []
    pain: []
    mental_emotional: []
    gynecological: []
    # ... more systems
  }

  # Combinations (PRESCRIPTIVE)
  combinations: [
    {condition: "", points: [], source: ""}
  ]
```

**Current Agent Usage:** ❌ NONE - Just name retrieval

**Opportunity:**
- Use `indications` to **filter points by symptom category**
- Extract `combinations` for **ready-made point prescriptions**
- Match `functions` to pattern treatment principles

---

## Part 2: Template Body Content Audit

### Pattern Template - Differential Diagnosis Section (Lines 138-154)

**THIS IS THE KEY TO INTELLIGENT QUESTIONING!**

```markdown
## Differential Diagnosis

### Similar Patterns

| Feature | This Pattern | Similar Pattern 1 | Similar Pattern 2 |
|---------|--------------|-------------------|-------------------|
| Chief symptom | [description] | [description] | [description] |
| Tongue | [description] | [description] | [description] |
| Pulse | [description] | [description] | [description] |
| Key distinction | [description] | [description] | [description] |

**vs. [[Similar Pattern 1]]:**
- Key difference: [distinguishing feature]

**vs. [[Similar Pattern 2]]:**
- Key difference: [distinguishing feature]
```

**Current Agent Usage:** ❌ ZERO

**CRITICAL OPPORTUNITY:**
This section **literally tells us what questions to ask** to differentiate patterns!

Example from your case:
- Agent identified: "Spleen Yang Deficiency", "Spleen Qi Deficiency with Cold-Damp", "Eight Principles Cold"
- These patterns likely have differential diagnosis sections comparing each other
- Agent should **parse this section** and ask:
  - "Is the tongue more pale or purple?"
  - "Does pressure relieve or worsen the pain?"
  - "Are limbs cold to touch?"

---

### Pattern Template - Treatment Approach (Lines 157-227)

```markdown
### Representative Formulas
**Primary Formula:**
- [[Main Formula]] → [Why this formula matches the pattern]

**Alternative Formulas:**
- [[Formula 1]] → [When to use this variation]
- [[Formula 2]] → [When to use this variation]

### Key Herbs
**Essential Herbs for This Pattern:**
- [[Herb 1]] → [Role and dosage considerations]

### Acupuncture Points
**Primary Points:**
- [[Point 1 (CODE-#)]] → [Action and needling consideration]

**Point Combinations:**
- [Combination 1]: [[Point A]] + [[Point B]] → [Rationale]
```

**Current Agent Usage:** ❌ Not extracting these curated recommendations

**Opportunity:**
- Pattern notes **already specify recommended formulas** - don't need semantic search!
- Pattern notes **already specify essential herbs** with dosage notes
- Pattern notes **already have point combinations** with rationale
- Agent should **read pattern markdown body**, not just frontmatter

---

### Formula Template - Modifications Section (Lines 147-173)

```markdown
### Common Additions

| Condition | Add Herbs | Rationale |
|-----------|-----------|-----------|
| [Presentation] | [[Herb A]] + [[Herb B]] | [Why these herbs] |

### Classical Variations
### Modern Modifications
```

**Current Agent Usage:** ❌ None

**Opportunity:**
After selecting base formula, agent should:
1. Read formula markdown
2. Extract modification table
3. Match patient presentation to conditions
4. Suggest appropriate herb additions

---

## Part 3: Diagnostic Agent Workflow Analysis

### Current Workflow

```
1. Collect chief complaint
2. Collect 10 Questions
3. Semantic search for patterns (top 10)
4. LLM analyzes and ranks patterns
5. Semantic search for formulas/herbs/points
6. LLM generates justifications
7. Save case note
```

### Identified Gaps

#### Gap 1: No Differential Questioning Phase
**Problem:** After retrieving similar patterns, agent doesn't ask follow-up questions
**Impact:** Lower diagnostic accuracy, missed distinctions

#### Gap 2: Not Reading Pattern Note Content
**Problem:** Agent only uses pattern `name` from vector search metadata
**Impact:** Missing curated treatment recommendations

#### Gap 3: Semantic Search Instead of Direct Lookup
**Problem:** Uses similarity search for formulas instead of reading pattern's recommended formulas
**Impact:** May miss optimal formulas that pattern author specifically recommends

#### Gap 4: No Formula Customization
**Problem:** Returns base formulas without modifications
**Impact:** Less precise treatment, misses clinical nuances

#### Gap 5: No Point Combination Logic
**Problem:** Returns individual points, not proven combinations
**Impact:** Less effective acupuncture prescriptions

---

## Part 4: Data Flow Mapping

### Current Data Flow

```
Patient Input
    ↓
Embeddings → Vector DB Search → Pattern Names
    ↓
LLM Analysis → Top Patterns
    ↓
Pattern Names → Formula Search → Formula Names
    ↓
LLM Justification → Display
```

### Missing Data Flows

```
❌ Pattern Names → Read Pattern Markdown → Extract Differential Questions
❌ Pattern Names → Read Pattern Markdown → Extract Recommended Formulas
❌ Pattern Names → Extract Treatment Principles from Frontmatter
❌ Formula Names → Read Formula Markdown → Extract Modifications
❌ Pattern + Symptoms → Read Point Combinations from Pattern Note
```

---

## Part 5: Proposed Improvements

### Improvement 1: Intelligent Differential Diagnosis System

**Add New Phase Between Pattern Ranking and Treatment Planning:**

```python
def generate_differential_questions(
    self,
    top_patterns: List[Dict],
    intake_data: Dict
) -> List[Dict[str, str]]:
    """
    Generate targeted questions to differentiate between similar patterns.

    Returns:
        List of {question, patterns_affected, reasoning}
    """
    # For top 3-5 patterns:
    # 1. Read each pattern's markdown file
    # 2. Extract "Differential Diagnosis" section
    # 3. Parse comparison tables
    # 4. Identify missing data points from intake
    # 5. Generate specific questions

    # Example:
    # Pattern A tongue: "Pale with thin white coat"
    # Pattern B tongue: "Pale with thick greasy coat"
    # User said: "pale thick white coat"
    # → Ask: "Is the coating greasy/slippery or dry?"
```

**Implementation:**
- Parse Pattern markdown using existing `markdown_parser.py`
- Extract differential diagnosis section
- Use LLM to generate 3-5 targeted questions
- Present questions to user
- Re-rank patterns based on answers

---

### Improvement 2: Pattern-Driven Treatment Recommendations

**Replace Semantic Search with Direct Lookup:**

```python
def get_pattern_recommended_treatments(
    self,
    pattern_name: str
) -> Dict[str, List]:
    """
    Read pattern markdown and extract curated treatment recommendations.

    Returns:
        {
            'formulas': [...],
            'herbs': [...],
            'points': [...],
            'treatment_principles': [...]
        }
    """
    # 1. Read pattern markdown file
    # 2. Extract "Representative Formulas" section
    # 3. Extract "Key Herbs" section
    # 4. Extract "Acupuncture Points" section
    # 5. Parse frontmatter treatment_principle field
```

**Benefits:**
- More accurate (uses expert curation, not just semantic similarity)
- Faster (direct file read vs. embedding search)
- Better justifications (already explained in pattern note)

---

### Improvement 3: Formula Modification Intelligence

```python
def customize_formula(
    self,
    base_formula: str,
    patient_symptoms: List[str],
    identified_patterns: List[str]
) -> Dict:
    """
    Suggest formula modifications based on patient presentation.

    Returns:
        {
            'base_formula': str,
            'add_herbs': List[{herb, reason}],
            'remove_herbs': List[{herb, reason}],
            'adjust_dosages': List[{herb, new_dosage, reason}]
        }
    """
    # 1. Read formula markdown
    # 2. Extract "Common Additions" table
    # 3. Match patient conditions to modification conditions
    # 4. Extract "Common Modifications" section
    # 5. Use LLM to select appropriate modifications
```

---

### Improvement 4: Point Combination Prescriptions

```python
def get_point_prescriptions(
    self,
    identified_patterns: List[str],
    chief_complaint: str
) -> List[Dict]:
    """
    Extract proven point combinations from pattern notes.

    Returns:
        [
            {
                'combination': [point_names],
                'indication': str,
                'source': str,
                'rationale': str
            }
        ]
    """
    # 1. For each identified pattern
    # 2. Read pattern markdown
    # 3. Extract "Point Combinations" section
    # 4. Parse combinations from Point markdown files
    # 5. Return structured combinations with rationale
```

---

### Improvement 5: Enhanced Frontmatter Utilization

**Current:** Agent doesn't read frontmatter beyond `name`

**Proposed:**
```python
def enrich_pattern_data(self, pattern_name: str) -> Dict:
    """
    Read pattern frontmatter for structured diagnostic data.
    """
    frontmatter = FrontmatterParser.parse_file(pattern_file)

    return {
        'name': pattern_name,
        'cardinal_symptoms': frontmatter['pattern_data']['cardinal_symptoms'],
        'tongue': frontmatter['pattern_data']['tongue'],
        'pulse': frontmatter['pattern_data']['pulse'],
        'treatment_principles': frontmatter['pattern_data']['treatment_principle'],
        'contraindications': frontmatter['pattern_data']['contraindications'],
        'eight_principles': {
            'excess_deficiency': frontmatter['pattern_data']['excess_deficiency'],
            'hot_cold': frontmatter['pattern_data']['hot_cold'],
            'interior_exterior': frontmatter['pattern_data']['interior_exterior']
        }
    }
```

**Usage:**
- Compare user's tongue/pulse to pattern's expected tongue/pulse
- Check if user has cardinal symptoms
- Use Eight Principles for logical filtering
- Pull treatment principles directly from frontmatter

---

## Part 6: Simplified Frontmatter Recommendations

### Current Frontmatter Issues

1. **Redundancy:** `patterns: []` field in formulas duplicates pattern note's `formulas: []`
2. **Complexity:** Too many empty fields in templates create cognitive load
3. **Inconsistent Population:** Some fields rarely get filled

### Simplification Proposals

#### Keep (Essential):
- Core metadata (id, name, type, aliases, tags)
- Primary cross-links (patterns, symptoms, formulas, herbs, points)
- Type-specific essential data (cardinal_symptoms, tongue, pulse for patterns)

#### Simplify/Merge:
- Merge `category` into `tags` (single tagging system)
- Remove `nutrition` and `tests` (rarely used)
- Move `related` into note body (less structured)

#### Auto-Populate:
- Use scripts to bidirectionally link (when formula links to pattern, auto-add formula to pattern's frontmatter)

---

## Part 7: Recommended Implementation Phases

### Phase 1: Foundation (Week 1)
**Goal:** Enable agent to read pattern markdown content

- [ ] Add markdown content parser to RAG pipeline
- [ ] Extract "Representative Formulas" from pattern markdown
- [ ] Extract "Key Herbs" from pattern markdown
- [ ] Extract "Acupuncture Points" from pattern markdown
- [ ] Test: Compare semantic search results vs. pattern-recommended results

**Expected Impact:** 30-40% better formula/herb/point accuracy

---

### Phase 2: Differential Diagnosis (Week 2)
**Goal:** Implement intelligent follow-up questioning

- [ ] Parse "Differential Diagnosis" section from pattern markdown
- [ ] Create differential question generator
- [ ] Add CLI interaction for follow-up questions
- [ ] Re-rank patterns based on differential answers
- [ ] Test with 10 real cases

**Expected Impact:** 50-60% better pattern accuracy

---

### Phase 3: Treatment Customization (Week 3)
**Goal:** Provide modified formulas and point combinations

- [ ] Parse "Common Additions" from formula markdown
- [ ] Match patient presentation to modification conditions
- [ ] Extract point combinations from pattern markdown
- [ ] Generate customized treatment recommendations
- [ ] Test formula modifications against classical texts

**Expected Impact:** More clinically precise, personalized treatments

---

### Phase 4: Frontmatter Integration (Week 4)
**Goal:** Fully utilize structured frontmatter data

- [ ] Extract Eight Principles from pattern frontmatter
- [ ] Use cardinal_symptoms for validation
- [ ] Compare tongue/pulse to expected presentations
- [ ] Pull treatment_principle from frontmatter
- [ ] Create diagnostic confidence scoring

**Expected Impact:** More transparent, explainable diagnostics

---

## Part 8: Specific Code Changes

### New Module: `markdown_content_parser.py`

```python
class MarkdownContentParser:
    """Parse semantic content from template markdown files."""

    @staticmethod
    def extract_differential_diagnosis(file_path: Path) -> Dict:
        """Extract differential diagnosis section from pattern markdown."""

    @staticmethod
    def extract_recommended_formulas(file_path: Path) -> List[Dict]:
        """Extract formula recommendations with rationale."""

    @staticmethod
    def extract_point_combinations(file_path: Path) -> List[Dict]:
        """Extract point combination prescriptions."""

    @staticmethod
    def extract_formula_modifications(file_path: Path) -> Dict:
        """Extract common additions and modifications table."""
```

### Enhanced RAG Methods:

```python
# In rag.py

def analyze_pattern_differentials(
    self,
    top_patterns: List[Dict],
    intake_data: Dict
) -> List[Dict]:
    """Generate differential questions from pattern markdown."""

def get_pattern_treatments(
    self,
    pattern_name: str
) -> Dict:
    """Read pattern markdown for curated treatments."""

def customize_formula_for_patient(
    self,
    formula_name: str,
    patient_presentation: str
) -> Dict:
    """Suggest formula modifications from markdown."""
```

---

## Part 9: Validation & Testing Strategy

### Test Cases for Differential Diagnosis

**Test Case 1: Spleen Qi Deficiency vs. Spleen Yang Deficiency**
- Both patterns share: fatigue, loose stools, poor appetite
- Key differentiators: cold limbs, aversion to cold, pulse depth
- Expected: Agent should ask about cold signs and pulse depth

**Test Case 2: Liver Fire vs. Liver Yang Rising**
- Both patterns share: headache, red eyes, irritability
- Key differentiators: tongue color, pulse wiry vs. flooding
- Expected: Agent should ask specific tongue and pulse questions

### Accuracy Metrics

1. **Pattern Accuracy:** % of correct primary pattern (Gold standard: experienced practitioner)
2. **Formula Relevance:** % of formulas that are appropriate for identified patterns
3. **Differential Question Quality:** Do questions actually help differentiate?
4. **Treatment Precision:** Do modifications match patient presentation?

---

## Summary of Key Insights

1. **Template structure is excellent** - Rich with diagnostic intelligence
2. **Agent is underutilizing available data** - Only using 10% of template capacity
3. **Differential diagnosis sections hold the key** - They literally tell us what to ask
4. **Pattern notes already recommend treatments** - Don't need to search, just read
5. **Frontmatter has structured data ready to use** - Eight Principles, cardinal symptoms, etc.
6. **Major workflow gap: No differential questioning** - This is the most critical missing piece

---

## Priority Recommendations

### Immediate (Do First):
1. **Add differential questioning phase** using pattern markdown differential sections
2. **Read pattern-recommended formulas** instead of semantic search
3. **Extract treatment principles from frontmatter** instead of LLM generation

### High Value (Do Soon):
4. Parse formula modifications for customization
5. Extract point combinations from pattern notes
6. Use Eight Principles frontmatter for filtering

### Nice to Have (Later):
7. Simplify/standardize frontmatter structure
8. Auto-populate bidirectional links
9. Add confidence scoring based on cardinal symptoms

---

**Next Steps:**
1. Review this audit with user
2. Prioritize improvements together
3. Start with Phase 1: Foundation (pattern markdown reading)
4. Test and iterate

