# Epic 12 Story Breakdown: Dashboard Polish & Interactivity

**Date:** 2025-11-22  
**Author:** Alice (Product Owner)  
**Status:** DRAFT  
**Epic ID:** 12  
**Prerequisites:** Epic 11 completion, Action Items #7-10 from Epic 11 Retrospective

---

## Executive Summary

Epic 12 transforms the functional dashboards delivered in Epic 11 into polished, production-ready navigation hubs that delight users and showcase the full potential of the Obsidian Capsule Delivery System. This epic focuses exclusively on visual design, user experience, and interactive features—the "presentation layer" that makes dashboards beautiful, intuitive, and engaging.

**Epic Vision:** Create dashboards so visually appealing and interactive that users want to spend time in them, making OCDS dashboards a competitive differentiator and reference implementation for the Obsidian community.

**Quality Bar:** Dashboards must be:
- **Visually Stunning:** Professional design with cohesive theming, visual hierarchy, and attention to detail
- **Highly Interactive:** Meta-Bind widgets for filtering, navigation, and progress visualization
- **Performant:** No degradation from Epic 11's performance benchmarks despite added features
- **Accessible:** Works across themes (light/dark), responsive layouts, graceful degradation
- **Self-Demonstrating:** New users immediately understand capabilities through visual examples

---

## Epic Overview and Goals

### Background

Epic 11 delivered the functional foundation:
- ✅ Master dashboard aggregates all capsules
- ✅ Capsule dashboards display metadata, navigation, file counts
- ✅ Dataview/DataviewJS queries work correctly
- ✅ Dashboard generation integrated into import workflow
- ✅ Performance validated with realistic data sets

**What's Missing:** The dashboards are utilitarian—functional but not polished. They lack:
- Visual design (colors, typography, spacing, separators)
- Interactive elements (buttons, filters, widgets)
- Advanced plugin integrations (Meta-Bind, Templater, Spaced Repetition)
- Responsive layouts optimized for different screen sizes
- Visual hierarchy that guides the eye
- Aesthetic improvements that make dashboards delightful to use

### Goals

**Primary Goals:**
1. **Visual Excellence:** Apply CSS theming, custom separators, neon accents, and visual hierarchy to all dashboard templates
2. **Interactive Widgets:** Integrate Meta-Bind for dynamic filtering, buttons, progress bars, and form controls
3. **Advanced Features:** Add Templater dynamic content, Spaced Repetition integration, and plugin-powered enhancements
4. **Responsive Design:** Ensure dashboards look great on laptop, desktop, and tablet screens
5. **Documentation:** Create visual examples and user guides showing polished dashboard capabilities

**Secondary Goals:**
- Establish CSS theming patterns for future dashboard customization
- Create reusable widget library for domain-specific dashboards
- Build inspiration gallery showcasing different dashboard styles
- Enable user customization through documented CSS snippets

### Success Criteria

**User Acceptance:**
- BMad confirms dashboards are "production-ready" and "visually competitive with best Obsidian dashboards"
- New users understand dashboard capabilities within 30 seconds of opening
- Tutorial capsule (post-Epic 12) uses polished dashboards as self-demonstrating examples

**Technical Acceptance:**
- All Epic 11 functionality preserved (no regressions)
- Performance remains within Epic 11 benchmarks
- Dashboards work in both light and dark themes
- Interactive widgets function correctly with Meta-Bind v0.9.0+
- CSS theming doesn't break with Obsidian updates (tested across 3+ themes)

---

## User Personas and Use Cases

### Primary Personas

**1. TCM Student (Emily)**
- **Context:** Studying for CALE/NCCAOM board exams
- **Needs:** Quick access to formulas, herbs, patterns; visual progress tracking; study material organization
- **Pain Points:** Overwhelmed by hundreds of notes, loses track of study progress
- **Dashboard Use:** Opens master dashboard daily to see active study capsules, uses capsule dashboard to navigate formula sets and track flashcard completion
- **Epic 12 Value:** Progress bars show completion %, interactive filters narrow formulas by category, visual separators group related content

**2. TCM Instructor (Dr. Chen)**
- **Context:** Creating educational capsules for students
- **Needs:** Professional-looking dashboards that students immediately understand; showcase system capabilities
- **Pain Points:** Current dashboards look "bare bones," don't inspire student confidence
- **Dashboard Use:** Distributes capsules with dashboards as student navigation hubs
- **Epic 12 Value:** Polished dashboards make capsules look professional, Meta-Bind buttons guide students to "Start Week 1" materials, visual design matches educational context

**3. Knowledge Worker (Alex)**
- **Context:** Building personal reference library across multiple domains (cooking, gardening, TCM)
- **Needs:** Aesthetic workspace that sparks joy, easy navigation across 20+ capsules
- **Pain Points:** Current dashboards feel "technical" rather than inviting
- **Dashboard Use:** Master dashboard as daily "home base" for accessing knowledge across domains
- **Epic 12 Value:** Neon theme option, custom separators, visual filtering make dashboards a pleasure to use; CSS snippets allow personalization

### Use Cases by Dashboard Type

**Master Dashboard Use Cases:**
1. **UC-1:** Filter capsules by active status to see only currently studying topics
2. **UC-2:** Search capsules by class/category for board exam preparation
3. **UC-3:** Visual progress overview showing completion % across all capsules
4. **UC-4:** Quick navigation buttons to "Resume Last Capsule" or "Start New Study Session"
5. **UC-5:** Visual dashboard gallery showing available capsule styles (neon, minimal, academic)

**Capsule Dashboard Use Cases:**
1. **UC-6:** Click "Start Learning" button to open first root note in sequence
2. **UC-7:** Progress bar shows "15/50 flashcards completed" with visual indicator
3. **UC-8:** Interactive filter toggles between formulas by category (Tonify Qi, Dispel Cold, etc.)
4. **UC-9:** Spaced Repetition widget shows "5 cards due for review today"
5. **UC-10:** Collapsible sections (expand/collapse) for domain-specific content

**Domain-Specific Dashboard Use Cases (TCM):**
1. **UC-11:** Formula dashboard with interactive ingredient extraction (click formula → see all herbs)
2. **UC-12:** Herb dashboard with category filters (Warm Interior, Tonify Qi, etc.)
3. **UC-13:** Pattern dashboard with differential diagnosis quick links
4. **UC-14:** Point dashboard with meridian filtering (LU, LI, ST, SP, etc.)
5. **UC-15:** Visual anatomy diagrams linked to point locations

---

## Story Organization

### Tracks and Themes

Epic 12 stories are organized into **5 thematic tracks** that can be worked in parallel or sequenced based on dependencies:

**Track 1: Foundation (CSS Theming & Visual Design)**
- Core CSS infrastructure, theming system, visual hierarchy
- **Stories:** 12-1, 12-2, 12-3
- **Priority:** Must-have (foundational work)
- **Dependencies:** None (can start immediately after Epic 11)

**Track 2: Interactive Widgets (Meta-Bind Integration)**
- Meta-Bind buttons, filters, progress bars, form controls
- **Stories:** 12-4, 12-5, 12-6
- **Priority:** Must-have (core interactivity)
- **Dependencies:** Track 1 (CSS theming defines widget styles)

**Track 3: Advanced Plugin Integration**
- Templater dynamic content, Spaced Repetition, advanced features
- **Stories:** 12-7, 12-8
- **Priority:** Should-have (enhances functionality)
- **Dependencies:** Track 2 (widgets provide foundation for advanced features)

**Track 4: Responsive Design & Accessibility**
- Layout optimization, theme compatibility, graceful degradation
- **Stories:** 12-9, 12-10
- **Priority:** Must-have (production readiness)
- **Dependencies:** Tracks 1-3 (optimize after features implemented)

**Track 5: Documentation & Examples**
- Visual examples, user guides, customization documentation
- **Stories:** 12-11, 12-12
- **Priority:** Must-have (user onboarding)
- **Dependencies:** Tracks 1-4 (document after implementation)

### Phases

**Phase 1: Visual Foundation (Weeks 1-2)**
- Stories: 12-1, 12-2, 12-3, 12-4
- **Goal:** CSS theming system in place, basic widgets functional
- **Deliverable:** Master and capsule dashboards visually polished with basic interactivity

**Phase 2: Advanced Interactivity (Weeks 2-3)**
- Stories: 12-5, 12-6, 12-7, 12-8
- **Goal:** Full Meta-Bind integration, advanced plugin features
- **Deliverable:** Dashboards with interactive filtering, progress tracking, and plugin enhancements

**Phase 3: Production Readiness (Week 4)**
- Stories: 12-9, 12-10, 12-11, 12-12
- **Goal:** Responsive design, accessibility, comprehensive documentation
- **Deliverable:** Production-ready dashboards with user guides and customization docs

---

## User Stories with Acceptance Criteria

### Track 1: Foundation (CSS Theming & Visual Design)

#### Story 12-1: CSS Theming System & Infrastructure

**As a** dashboard developer  
**I want** a CSS theming system for dashboard styling  
**So that** I can apply consistent visual design across all dashboards without inline styles

**Description:**
Research Obsidian CSS customization capabilities (CSS snippets, theme variables, selectors). Create infrastructure for dashboard CSS theming including:
- CSS snippet file structure
- Theme variable system (colors, spacing, typography)
- Dashboard-specific CSS classes
- Documentation for CSS customization

**Acceptance Criteria:**
1. Research Obsidian CSS snippet system and document capabilities/constraints
2. Create `capsule/templates/css/dashboard-theme.css` with base theme variables
3. Implement CSS class naming convention for dashboard elements (e.g., `.capsule-dashboard-header`, `.capsule-dashboard-section`)
4. Document how to install CSS snippets in Obsidian vault
5. Test CSS snippets work in both light and dark themes
6. Create example: "neon theme" and "minimal theme" variants

**Dependencies:** None  
**Priority:** Must-have  
**Effort:** M (5 points)  
**Risk:** Medium - CSS behavior may vary across Obsidian versions

---

#### Story 12-2: Visual Hierarchy & Typography

**As a** dashboard user  
**I want** clear visual hierarchy in dashboards  
**So that** I can quickly scan and find information

**Description:**
Apply typography, spacing, and visual hierarchy to dashboard templates using CSS from Story 12-1. Focus on:
- Heading styles (size, weight, color, spacing)
- Section separators (custom horizontal rules)
- Content grouping (cards, panels, borders)
- Typography scale (body text, metadata, labels)

**Acceptance Criteria:**
1. Update dashboard templates with CSS classes for headings (H1-H4)
2. Implement custom section separators (horizontal rules with visual flair)
3. Add CSS for content cards/panels with subtle borders and spacing
4. Define typography scale in CSS variables (base size, scale factor)
5. Test visual hierarchy with realistic dashboard content (10+ sections)
6. Document visual hierarchy guidelines for future dashboard development

**Dependencies:** 12-1 (CSS infrastructure)  
**Priority:** Must-have  
**Effort:** M (5 points)  
**Risk:** Low

---

#### Story 12-3: Color Theming & Accents

**As a** dashboard user  
**I want** visually appealing color schemes  
**So that** dashboards are pleasant to look at and use

**Description:**
Implement color theming for dashboards with multiple theme options:
- Neon theme (inspired by neon-homepage-vault)
- Minimal theme (clean, professional)
- Academic theme (traditional, formal)
Color applications include: section headers, separators, buttons, accents, links

**Acceptance Criteria:**
1. Define color palettes for 3 themes (neon, minimal, academic) in CSS variables
2. Apply colors to dashboard sections, headers, and accents
3. Implement hover states and interactive color feedback
4. Test color contrast for accessibility (WCAG AA minimum)
5. Create CSS snippet files for each theme (`dashboard-neon.css`, `dashboard-minimal.css`, `dashboard-academic.css`)
6. Document how users can switch between themes

**Dependencies:** 12-1 (CSS infrastructure), 12-2 (visual hierarchy)  
**Priority:** Should-have  
**Effort:** M (5 points)  
**Risk:** Low

---

### Track 2: Interactive Widgets (Meta-Bind Integration)

#### Story 12-4: Meta-Bind Integration Research & Setup

**As a** dashboard developer  
**I want** to understand Meta-Bind capabilities  
**So that** I can implement interactive widgets in dashboards

**Description:**
Research Meta-Bind plugin (v0.9.0+) capabilities including:
- Button syntax and actions
- Input fields (text, select, toggle)
- Progress bars
- View fields (dynamic data display)
- Limitations and performance considerations

**Acceptance Criteria:**
1. Document Meta-Bind button syntax with examples (open note, run command, templater)
2. Document Meta-Bind input field types (text, number, select, toggle, date)
3. Document Meta-Bind progress bar syntax and data binding
4. Create proof-of-concept dashboard with 5+ widget examples
5. Test Meta-Bind performance with complex dashboards (10+ widgets)
6. Document Meta-Bind version requirement and installation instructions

**Dependencies:** None (can run parallel with Track 1)  
**Priority:** Must-have  
**Effort:** S (3 points)  
**Risk:** Medium - Meta-Bind plugin behavior may change

---

#### Story 12-5: Interactive Navigation Buttons

**As a** dashboard user  
**I want** quick action buttons for common tasks  
**So that** I can navigate without manually clicking links

**Description:**
Implement Meta-Bind buttons for common navigation actions:
- "Start Learning" (open first root note)
- "Resume Last Session" (open recently updated note)
- "View Flashcards" (open flashcard deck)
- "Take Quiz" (open quiz)
- "Back to Master Dashboard" (navigate to master)

**Acceptance Criteria:**
1. Update capsule dashboard template with Meta-Bind navigation buttons
2. Implement "Start Learning" button (opens first root note in capsule)
3. Implement "Resume Last Session" button (opens most recently updated note)
4. Implement domain-specific buttons (e.g., "Browse Formulas," "View Herb Categories")
5. Style buttons using CSS from Track 1 (primary, secondary, tertiary styles)
6. Test buttons work correctly across different capsule types (freeform, sequenced)

**Dependencies:** 12-4 (Meta-Bind research), 12-1 (CSS theming)  
**Priority:** Must-have  
**Effort:** M (5 points)  
**Risk:** Low

---

#### Story 12-6: Interactive Filtering & Progress Widgets

**As a** dashboard user  
**I want** interactive filters and progress visualization  
**So that** I can dynamically explore content and track my progress

**Description:**
Implement Meta-Bind widgets for filtering and progress:
- Dropdown filters for capsule metadata (class, category, active status)
- Toggle filters for content types (root notes, flashcards, quizzes)
- Progress bars showing completion percentage
- Counter widgets showing file counts

**Acceptance Criteria:**
1. Update master dashboard with Meta-Bind dropdown filters (class, category, active)
2. Implement filter interaction with Dataview queries (filter results dynamically)
3. Add progress bars to capsule dashboards (study material completion %)
4. Implement counter widgets for file counts (X root notes, Y flashcards)
5. Style widgets using CSS from Track 1
6. Test filter performance with 20+ capsules

**Dependencies:** 12-4 (Meta-Bind research), 12-1 (CSS theming), 12-5 (widget patterns)  
**Priority:** Should-have  
**Effort:** L (8 points)  
**Risk:** Medium - Complex Dataview + Meta-Bind interaction

---

### Track 3: Advanced Plugin Integration

#### Story 12-7: Templater Dynamic Content Integration

**As a** dashboard user  
**I want** dynamic content that updates based on current date/time  
**So that** dashboards show relevant, timely information

**Description:**
Integrate Templater for dynamic dashboard content:
- "Today's Date" and "Current Week"
- "Last Updated" timestamps
- "Days Until Deadline" calculations (for sequenced capsules)
- Dynamic greetings ("Good morning," based on time of day)

**Acceptance Criteria:**
1. Research Templater syntax for date/time operations
2. Add Templater dynamic date to dashboard headers (`<% tp.date.now() %>`)
3. Implement "Last Updated" timestamp with relative time ("2 hours ago")
4. Add "Days Until Deadline" for sequenced capsule timelines
5. Implement dynamic greetings based on time of day
6. Document Templater version requirement (v1.16.0+)

**Dependencies:** 12-5 (dashboard templates updated with widgets)  
**Priority:** Nice-to-have  
**Effort:** S (3 points)  
**Risk:** Low

---

#### Story 12-8: Spaced Repetition Integration

**As a** student using flashcards  
**I want** Spaced Repetition reminders on dashboards  
**So that** I know when to review flashcards

**Description:**
Integrate Spaced Repetition plugin (if installed) to show:
- "Cards due for review today" count
- "Next review scheduled" timestamp
- "Review Now" button linking to flashcard deck
- Progress tracking for spaced repetition schedules

**Acceptance Criteria:**
1. Research Spaced Repetition plugin API/data structure
2. Implement DataviewJS query to count cards due for review
3. Add "Cards Due Today" widget to capsule dashboard
4. Implement "Review Now" button linking to flashcard deck
5. Handle graceful degradation if Spaced Repetition plugin not installed
6. Document Spaced Repetition plugin requirement (optional)

**Dependencies:** 12-5 (navigation buttons), 12-6 (widgets)  
**Priority:** Nice-to-have  
**Effort:** M (5 points)  
**Risk:** High - Plugin API may not be documented

---

### Track 4: Responsive Design & Accessibility

#### Story 12-9: Responsive Layout Optimization

**As a** dashboard user on different devices  
**I want** dashboards to look good on laptop, desktop, and tablet  
**So that** I can use OCDS on any screen size

**Description:**
Optimize dashboard layouts for different screen sizes:
- Mobile/tablet (768px-1024px width)
- Laptop (1024px-1440px width)
- Desktop (1440px+ width)
Adjustments include: column layouts, widget sizing, font scaling, image sizing

**Acceptance Criteria:**
1. Implement CSS media queries for 3 screen size breakpoints
2. Test dashboard layouts on 768px, 1024px, and 1440px+ widths
3. Adjust column layouts for narrow screens (single column on mobile)
4. Scale font sizes appropriately for screen size
5. Ensure interactive widgets remain usable on all screen sizes
6. Document responsive design guidelines

**Dependencies:** 12-1 (CSS infrastructure), 12-2 (visual hierarchy)  
**Priority:** Should-have  
**Effort:** M (5 points)  
**Risk:** Medium - Obsidian rendering may limit CSS control

---

#### Story 12-10: Theme Compatibility & Graceful Degradation

**As a** dashboard user with custom Obsidian themes  
**I want** dashboards to work with my theme  
**So that** visual consistency is maintained

**Description:**
Test and ensure dashboard CSS works across popular Obsidian themes:
- Default theme (light/dark)
- Minimal theme
- California Coast
- Things theme
- Custom themes
Implement graceful degradation for missing plugins (Meta-Bind, Templater, etc.)

**Acceptance Criteria:**
1. Test dashboards in 5+ popular Obsidian themes (light and dark modes)
2. Fix CSS conflicts and ensure readability across themes
3. Implement fallback styles for unsupported theme variables
4. Add plugin detection logic (show notice if Meta-Bind not installed)
5. Document theme compatibility testing process
6. Create "Known Issues" documentation for theme conflicts

**Dependencies:** 12-1 (CSS theming), 12-4 (Meta-Bind integration)  
**Priority:** Must-have  
**Effort:** M (5 points)  
**Risk:** Medium - Unpredictable theme interactions

---

### Track 5: Documentation & Examples

#### Story 12-11: Visual Dashboard Examples & Gallery

**As a** new OCDS user  
**I want** visual examples of polished dashboards  
**So that** I understand what's possible and how to use them

**Description:**
Create visual dashboard gallery showcasing:
- Master dashboard (3 theme variants: neon, minimal, academic)
- Capsule dashboard (TCM formulas, herbs, patterns)
- Domain-specific dashboards (education, reference, TCM)
Screenshots, GIFs, and example vaults demonstrating features

**Acceptance Criteria:**
1. Generate 3 master dashboard examples (neon, minimal, academic themes)
2. Generate 5 capsule dashboard examples (different domains)
3. Create screenshots showing: filtering, widgets, navigation, progress tracking
4. Record GIF demonstrations of interactive features (filtering, button clicks)
5. Create example vault with pre-populated dashboards for testing
6. Add visual examples to User Guide documentation

**Dependencies:** All Track 1-4 stories (showcase completed features)  
**Priority:** Must-have  
**Effort:** M (5 points)  
**Risk:** Low

---

#### Story 12-12: Dashboard Customization Documentation

**As a** power user  
**I want** documentation on customizing dashboards  
**So that** I can tailor them to my preferences

**Description:**
Create comprehensive documentation for dashboard customization:
- How to modify CSS themes
- How to add custom widgets
- How to create domain-specific dashboard sections
- How to integrate additional plugins
- Troubleshooting common issues

**Acceptance Criteria:**
1. Document CSS customization process with step-by-step guide
2. Document Meta-Bind widget customization with examples
3. Create tutorial: "Adding a Custom Dashboard Section"
4. Create tutorial: "Creating a New Theme Variant"
5. Document plugin integration patterns (Templater, Spaced Repetition)
6. Create FAQ section for common customization questions

**Dependencies:** 12-11 (examples), all Track 1-4 stories (complete features)  
**Priority:** Must-have  
**Effort:** L (8 points)  
**Risk:** Low

---

## Story Dependencies and Sequencing

### Dependency Graph

```
TRACK 1 (Foundation)
12-1 (CSS Infrastructure)
  ├─→ 12-2 (Visual Hierarchy)
  │     └─→ 12-3 (Color Theming)
  └─→ 12-9 (Responsive Design)

TRACK 2 (Widgets)
12-4 (Meta-Bind Research)
  ├─→ 12-5 (Navigation Buttons)
  │     └─→ 12-6 (Filtering & Progress)
  └─→ 12-10 (Theme Compatibility)

TRACK 3 (Advanced)
12-5 (Navigation Buttons)
  ├─→ 12-7 (Templater Integration)
  └─→ 12-8 (Spaced Repetition)

TRACK 4 (Production)
12-1, 12-2 → 12-9 (Responsive Design)
12-4 → 12-10 (Theme Compatibility)

TRACK 5 (Docs)
All Tracks 1-4 → 12-11 (Visual Examples)
12-11 → 12-12 (Customization Docs)
```

### Critical Path

**Longest dependency chain (determines minimum epic duration):**
1. 12-1 (CSS Infrastructure) - 5 pts
2. 12-2 (Visual Hierarchy) - 5 pts
3. 12-4 (Meta-Bind Research) - 3 pts *(parallel with 12-1)*
4. 12-5 (Navigation Buttons) - 5 pts
5. 12-6 (Filtering & Progress) - 8 pts
6. 12-11 (Visual Examples) - 5 pts
7. 12-12 (Customization Docs) - 8 pts

**Critical Path Total:** 39 points (~4 weeks at 10 pts/week velocity)

### Parallel Work Opportunities

**Week 1:**
- 12-1 (CSS Infrastructure) + 12-4 (Meta-Bind Research) *[parallel]*

**Week 2:**
- 12-2 (Visual Hierarchy) + 12-5 (Navigation Buttons) *[partial parallel after 12-1 complete]*
- 12-3 (Color Theming)

**Week 3:**
- 12-6 (Filtering & Progress)
- 12-7 (Templater) + 12-8 (Spaced Repetition) *[parallel, both optional]*
- 12-9 (Responsive Design) *[can start after 12-2]*

**Week 4:**
- 12-10 (Theme Compatibility)
- 12-11 (Visual Examples)
- 12-12 (Customization Docs)

---

## Effort Estimates and Prioritization

### Story Sizing (T-Shirt Sizes)

| Story | Title | Size | Points | Priority | Risk |
|-------|-------|------|--------|----------|------|
| 12-1 | CSS Theming System | M | 5 | Must-have | Medium |
| 12-2 | Visual Hierarchy & Typography | M | 5 | Must-have | Low |
| 12-3 | Color Theming & Accents | M | 5 | Should-have | Low |
| 12-4 | Meta-Bind Research & Setup | S | 3 | Must-have | Medium |
| 12-5 | Interactive Navigation Buttons | M | 5 | Must-have | Low |
| 12-6 | Interactive Filtering & Progress | L | 8 | Should-have | Medium |
| 12-7 | Templater Dynamic Content | S | 3 | Nice-to-have | Low |
| 12-8 | Spaced Repetition Integration | M | 5 | Nice-to-have | High |
| 12-9 | Responsive Layout Optimization | M | 5 | Should-have | Medium |
| 12-10 | Theme Compatibility & Degradation | M | 5 | Must-have | Medium |
| 12-11 | Visual Examples & Gallery | M | 5 | Must-have | Low |
| 12-12 | Customization Documentation | L | 8 | Must-have | Low |

**Total Effort:** 62 points

### MoSCoW Prioritization

**Must-Have (MVP for Epic 12):**
- 12-1: CSS Theming System (5 pts)
- 12-2: Visual Hierarchy & Typography (5 pts)
- 12-4: Meta-Bind Research & Setup (3 pts)
- 12-5: Interactive Navigation Buttons (5 pts)
- 12-10: Theme Compatibility & Degradation (5 pts)
- 12-11: Visual Examples & Gallery (5 pts)
- 12-12: Customization Documentation (8 pts)

**Must-Have Total:** 36 points (~3.5 weeks)

**Should-Have (High Value, Lower Risk):**
- 12-3: Color Theming & Accents (5 pts)
- 12-6: Interactive Filtering & Progress (8 pts)
- 12-9: Responsive Layout Optimization (5 pts)

**Should-Have Total:** 18 points (+ 2 weeks if included)

**Nice-to-Have (Enhancement, Higher Risk):**
- 12-7: Templater Dynamic Content (3 pts)
- 12-8: Spaced Repetition Integration (5 pts)

**Nice-to-Have Total:** 8 points (+ 1 week if included)

### Recommended Approach

**Phase 1 (Must-Have Only):** 36 points = ~4 weeks
- Delivers: Polished dashboards with CSS theming, Meta-Bind navigation, theme compatibility, documentation
- **Minimum Viable Epic 12**

**Phase 2 (Must-Have + Should-Have):** 54 points = ~5-6 weeks
- Adds: Color themes, interactive filtering, responsive design
- **Recommended Scope for v1.0**

**Phase 3 (Full Scope):** 62 points = ~6-7 weeks
- Adds: Templater integration, Spaced Repetition
- **Complete Epic 12** (defer to v1.1 if timeline constrained)

---

## Risks and Open Questions

### Risks

**RISK-1: CSS Behavior Across Obsidian Versions**
- **Impact:** High (dashboards may break with Obsidian updates)
- **Probability:** Medium
- **Mitigation:** 
  - Test CSS across multiple Obsidian versions (current, beta, previous)
  - Use conservative CSS (avoid experimental features)
  - Document tested Obsidian version
  - Monitor Obsidian release notes for CSS changes
- **Contingency:** Provide CSS fallbacks, maintain legacy CSS snippets

**RISK-2: Meta-Bind Plugin API Changes**
- **Impact:** High (widgets may break)
- **Probability:** Medium
- **Mitigation:**
  - Document tested Meta-Bind version (v0.9.0+)
  - Use stable Meta-Bind features (avoid experimental)
  - Test widget patterns thoroughly
  - Monitor Meta-Bind plugin updates
- **Contingency:** Graceful degradation (show static content if Meta-Bind unavailable)

**RISK-3: Theme Compatibility Issues**
- **Impact:** Medium (dashboards may look bad in some themes)
- **Probability:** High
- **Mitigation:**
  - Test across 5+ popular themes
  - Use theme-agnostic CSS variables where possible
  - Provide theme-specific CSS overrides
  - Document known theme conflicts
- **Contingency:** Recommend specific themes, provide custom theme variants

**RISK-4: Performance Degradation with Widgets**
- **Impact:** Medium (dashboards may slow down)
- **Probability:** Low
- **Mitigation:**
  - Benchmark widget performance (Story 12-4)
  - Limit widgets per dashboard (<10 recommended)
  - Test with large vaults (50+ capsules)
  - Document performance guidelines
- **Contingency:** Provide "lightweight" dashboard variant without widgets

**RISK-5: Spaced Repetition Plugin Unavailable/Incompatible**
- **Impact:** Low (nice-to-have feature)
- **Probability:** High
- **Mitigation:**
  - Mark as optional feature
  - Test multiple spaced repetition plugins
  - Implement graceful degradation
  - Document plugin requirements
- **Contingency:** Skip Story 12-8 if plugin integration infeasible

### Open Questions

**QUESTION-1: Should dashboards support user-editable themes?**
- **Context:** Users may want to customize colors, fonts, spacing
- **Options:**
  - A) Provide CSS snippets users can modify (self-service)
  - B) Provide UI for theme customization (future epic)
  - C) Offer 3-5 pre-built themes only
- **Recommendation:** Option A for v1.0 (documented CSS customization), Option B for v1.5

**QUESTION-2: How many theme variants should be included?**
- **Context:** More themes = more maintenance, but more user choice
- **Options:**
  - A) 1 theme (neon only)
  - B) 2 themes (neon + minimal)
  - C) 3 themes (neon + minimal + academic)
  - D) 5+ themes
- **Recommendation:** Option C (3 themes) for v1.0, community themes for v1.5

**QUESTION-3: Should interactive widgets be required or optional?**
- **Context:** Meta-Bind dependency adds complexity
- **Options:**
  - A) Required (dashboards assume Meta-Bind installed)
  - B) Optional (dashboards work without Meta-Bind, degraded experience)
- **Recommendation:** Option B (graceful degradation) for broader compatibility

**QUESTION-4: Should Epic 12 include mobile optimization?**
- **Context:** Obsidian mobile app has different rendering constraints
- **Options:**
  - A) Yes, optimize for mobile (1-2 additional stories)
  - B) No, defer to future epic
- **Recommendation:** Option B (defer to Epic 15: Mobile Optimization)

**QUESTION-5: Should visual examples be static or interactive?**
- **Context:** Screenshots vs. live demo vault
- **Options:**
  - A) Screenshots/GIFs only
  - B) Live demo vault (downloadable)
  - C) Both
- **Recommendation:** Option C (screenshots for docs, demo vault for hands-on testing)

**QUESTION-6: How to handle dashboard updates when Epic 12 completes?**
- **Context:** Existing users with Epic 11 dashboards need migration path
- **Options:**
  - A) Auto-update dashboards on next capsule import
  - B) Provide "upgrade dashboard" command
  - C) Manual update (user re-imports capsule)
- **Recommendation:** Option A (auto-update) with option to preserve custom changes

---

## Acceptance Testing Strategy

### Epic-Level Acceptance Criteria

**AC-1: Visual Polish**
- Dashboard screenshots pass "10-second test" (BMad approves within 10 seconds of viewing)
- Visual hierarchy clear: users can identify key sections without reading
- Color scheme cohesive and professional
- CSS theming works in light and dark modes

**AC-2: Interactivity**
- Meta-Bind buttons work for all defined actions (navigate, filter, etc.)
- Interactive filters update Dataview query results correctly
- Progress bars reflect accurate completion percentages
- Widgets degrade gracefully if Meta-Bind not installed

**AC-3: Performance**
- Dashboard load time ≤ Epic 11 benchmarks (no regression)
- Widget interaction response time < 500ms
- CSS rendering does not cause visual lag

**AC-4: Compatibility**
- Dashboards work in 5+ Obsidian themes (light/dark)
- Responsive layouts function on 3 screen sizes (laptop, desktop, tablet)
- Graceful degradation if optional plugins missing

**AC-5: Documentation**
- Visual examples clearly demonstrate features
- Customization guide enables users to modify themes
- FAQ addresses common issues

### Story-Level Testing

**Manual Testing (required for all stories):**
- Visual inspection in Obsidian
- Cross-theme testing (light/dark, 3+ themes)
- Widget interaction testing
- Screenshot/GIF capture for documentation

**Automated Testing (where applicable):**
- CSS validation (valid CSS syntax)
- Template rendering (generate dashboards without errors)
- Performance benchmarks (load time, query execution)

**User Acceptance Testing:**
- BMad review: "Does this look production-ready?"
- New user test: "Can you navigate this dashboard without instructions?"
- Power user test: "Can you customize this dashboard using docs?"

---

## Success Metrics

### Quantitative Metrics

1. **Visual Quality:** 90%+ approval in team review (4/5 team members approve aesthetics)
2. **Performance:** Dashboard load time ≤ Epic 11 baseline (no regression)
3. **Widget Adoption:** 80%+ of generated dashboards include Meta-Bind widgets
4. **Theme Compatibility:** 0 critical bugs in 5 tested themes
5. **Documentation Completeness:** 100% of features have visual examples + written docs

### Qualitative Metrics

1. **"Wow Factor":** New users express positive surprise when opening dashboards
2. **Professional Appearance:** Dashboards could be used in commercial products without embarrassment
3. **Ease of Use:** Users navigate without training or documentation
4. **Customization Success:** Power users successfully customize themes within 30 minutes
5. **Competitive Positioning:** Dashboards compare favorably to inspiration sources (neon-homepage-vault, DashboardPlusPlus)

---

## Epic 12 Completion Definition

Epic 12 is **complete** when:

✅ All Must-Have stories (12-1, 12-2, 12-4, 12-5, 12-10, 12-11, 12-12) delivered and tested  
✅ Master and capsule dashboard templates include CSS theming and Meta-Bind widgets  
✅ Visual examples and customization documentation published  
✅ BMad approves dashboards as "production-ready"  
✅ No performance regressions from Epic 11 baseline  
✅ All acceptance criteria met (AC-1 through AC-5)  
✅ Tutorial capsule ready to begin (post-Epic 12, uses polished dashboards)

---

## Appendix A: Inspiration Gallery

### Reference Implementations

**1. HOCA-1/neon-homepage-vault**
- **Strengths:** Stunning neon theme, visual hierarchy, custom CSS
- **Applicable Patterns:** Color scheme, section separators, accent colors
- **Story Impact:** 12-3 (Color Theming)

**2. rafaelveiga/obsidian-widgets**
- **Strengths:** Meta-Bind widget library, interactive elements
- **Applicable Patterns:** Button styles, progress bars, form controls
- **Story Impact:** 12-5 (Navigation Buttons), 12-6 (Filtering)

**3. TfTHacker/DashboardPlusPlus**
- **Strengths:** Professional layout, comprehensive examples
- **Applicable Patterns:** Dashboard structure, navigation patterns
- **Story Impact:** 12-2 (Visual Hierarchy)

**4. Obsidian Forum: Fancy Horizontal Rules**
- **Strengths:** Custom section separators, visual flair
- **Applicable Patterns:** Horizontal rule designs, dividers
- **Story Impact:** 12-2 (Visual Hierarchy)

---

## Appendix B: CSS Snippet Structure

### Proposed CSS File Organization

```
capsule/templates/css/
├── base/
│   ├── variables.css           # CSS custom properties (colors, spacing, fonts)
│   ├── reset.css              # Dashboard-specific resets
│   └── typography.css         # Font families, sizes, weights
│
├── themes/
│   ├── neon.css               # Neon theme variant
│   ├── minimal.css            # Minimal theme variant
│   └── academic.css           # Academic theme variant
│
├── components/
│   ├── headers.css            # Dashboard header styles
│   ├── sections.css           # Section containers and separators
│   ├── widgets.css            # Meta-Bind widget styles
│   └── buttons.css            # Button styles
│
└── layouts/
    ├── master-dashboard.css   # Master dashboard layout
    ├── capsule-dashboard.css  # Capsule dashboard layout
    └── responsive.css         # Responsive design media queries
```

---

## Appendix C: Meta-Bind Widget Patterns

### Widget Pattern Library (Story 12-4 Deliverable)

**Navigation Button:**
```markdown
```meta-bind-button
label: Start Learning
style: primary
action:
  type: open
  link: "[[First_Root_Note]]"
```​
```

**Dropdown Filter:**
```markdown
```meta-bind
INPUT[inlineSelect(option(All), option(TCM101), option(TCM201)):class_filter]
```​
```

**Progress Bar:**
```markdown
```meta-bind
INPUT[progressBar(
  minValue(0),
  maxValue(100),
  value(progress_percentage)
)]
```​
```

**Counter Widget:**
```markdown
```meta-bind
VIEW[{total_notes}][math]
```​
```

---

## Appendix D: User Testing Protocol

### New User Test (Story 12-11 Validation)

**Participant Profile:** Obsidian user, unfamiliar with OCDS

**Test Protocol:**
1. Open master dashboard (no prior instruction)
2. Observe for 30 seconds (no guidance)
3. Ask: "What do you think this dashboard does?"
4. Ask: "How would you navigate to a specific capsule?"
5. Ask: "How would you filter capsules by category?"
6. Observe button clicks and interactions
7. Collect feedback: "What's confusing? What's delightful?"

**Success Criteria:**
- User correctly identifies dashboard purpose within 10 seconds
- User navigates to capsule without help
- User successfully uses at least 1 interactive filter
- User expresses positive sentiment about visual design

---

**Epic 12 Story Breakdown — End of Document**

*Approved for development after Action Items #7-10 complete*
