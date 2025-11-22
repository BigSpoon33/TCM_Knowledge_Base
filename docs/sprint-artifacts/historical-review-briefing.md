# Briefing: Historical Pattern Review and Completeness Audit

**Objective:** To perform a data-driven analysis of Epics 0 through 4 to identify systemic patterns and uncover any incomplete work ("skeletons") before proceeding with new epics.

**Scope:** All story files associated with Epics 0, 1, 2, 3, and 4 located in `docs/sprint-artifacts/`.

## Process

This is a data analysis task, not a conversational retrospective. Follow these steps precisely:

1.  **Glob and Read:** Identify and read every story markdown file for Epics 0-4.
2.  **Execute Completeness Audit:**
    *   For each story, locate the `## Senior Developer Review (AI)` section.
    *   Identify any story where the `Outcome` is `BLOCKED`.
    *   Identify any story with un-checked action items of `[High]` or `[Medium]` priority.
    *   Compile a list of these stories, noting the specific incomplete items. This is your list of "skeletons."
3.  **Execute Pattern Review:**
    *   For each story, analyze the `## Dev Notes`, `## Learnings`, and review feedback sections.
    *   Identify recurring themes, challenges, or successes. Look for keywords that appear across multiple epics (e.g., "testing bottleneck," "unclear requirements," "dependency issues," "successful refactor").
    *   Tally the occurrences of these themes to find the most common patterns.
4.  **Synthesize and Report:**
    *   Create a final summary report that contains the following three sections:
        *   **Critical Unaddressed Issues:** The list of skeletons found in the Completeness Audit. Each item should be a clear, actionable task.
        *   **Top 3-5 Recurring Patterns:** The most frequent systemic issues or successes discovered. For each pattern, provide 2-3 examples from the story files.
        *   **Recommendations:** A prioritized list of suggestions to address the findings.

**Expected Output:** A single, comprehensive markdown report summarizing the findings of the audit and review.
