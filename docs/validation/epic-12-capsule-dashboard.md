---
type: capsule_dashboard
capsule_id: "test_capsule_123"
version: "1.0.0"
created: "2025-11-01"
updated: "2025-11-22"
cssclass: ocds-dashboard ocds-theme-neon

# Dashboard Metadata
dashboard_metadata:
  class: "TCM 101"
  topic: "Foundations"
  category: "Theory"
  active: true

source_capsules: ["test_capsule_123"]
---

<div class="ocds-dashboard ocds-theme-neon">

<div class="ocds-header">
  <h1 class="ocds-header__title">Test Capsule</h1>
  <div class="ocds-header__meta">
    <span>v1.0.0</span>
    <span>TCM</span>
  </div>
</div>

<div class="ocds-capsule-grid">

<div class="ocds-capsule-nav">
  <div class="ocds-card">
    <div class="ocds-card__header">
      <h3 class="ocds-card__title">Overview</h3>
    </div>
    <p><strong>ID:</strong> `test_capsule_123`</p>
    <p><strong>Mode:</strong> sequenced</p>
    <br>
    
    <!-- Navigation Buttons -->
    <div style="display: flex; flex-direction: column; gap: 0.5rem;">
      ```meta-bind-button
      label: ← Back to Master
      style: default
      class: ocds-btn
      action:
        type: open
        link: "[[Master-Dashboard]]"
      ```

      ```meta-bind-button
      label: Start Learning
      style: primary
      class: ocds-btn ocds-btn-primary
      action:
        type: command
        command: obsidian-dataview:dataview-force-refresh-views
      ```
    </div>
  </div>

  <div class="ocds-stat-card">
    <div class="ocds-stat-value">`$= dv.pages().where(p => p.source_capsules && p.source_capsules.includes("test_capsule_123") && p.type != "dashboard" && p.type != "capsule_dashboard").length`</div>
    <div class="ocds-stat-label">Root Notes</div>
  </div>

  <div class="ocds-stat-card">
    <div class="ocds-stat-value">`$= dv.pages().where(p => p.source_capsules && p.source_capsules.includes("test_capsule_123") && ["flashcard", "quiz", "slide", "conversation"].includes(p.type)).length`</div>
    <div class="ocds-stat-label">Study Mats</div>
  </div>
</div>

<div class="ocds-capsule-content">

<div class="ocds-section">
  <h2>📚 Root Notes</h2>
  <div class="ocds-table-container">
  ```dataview
  TABLE type, tags, updated
  FROM ""
  WHERE contains(source_capsules, "test_capsule_123")
    AND type != "dashboard"
    AND type != "capsule_dashboard"
    AND type != "quiz"
    AND type != "flashcard"
    AND type != "slide"
    AND type != "conversation"
  SORT name ASC
  LIMIT 20
  ```
  </div>
</div>

<div class="ocds-section">
  <h2>📝 Study Materials</h2>
  
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;">
    <div class="ocds-card">
      <div class="ocds-card__header">
        <h3 class="ocds-card__title">Flashcards</h3>
      </div>
      <div class="ocds-table-container">
      ```dataview
      LIST
      FROM ""
      WHERE contains(source_capsules, "test_capsule_123")
        AND type = "flashcard"
      SORT file.name ASC
      LIMIT 10
      ```
      </div>
      <div style="margin-top: 1rem;">
        ```meta-bind-button
        label: View All Flashcards
        style: default
        class: ocds-btn
        action:
          type: command
          command: obsidian-dataview:dataview-force-refresh-views
        ```
      </div>
    </div>

    <div class="ocds-card">
      <div class="ocds-card__header">
        <h3 class="ocds-card__title">Quizzes</h3>
      </div>
      <div class="ocds-table-container">
      ```dataview
      TABLE quiz_data.difficulty as "Difficulty"
      FROM ""
      WHERE contains(source_capsules, "test_capsule_123")
        AND type = "quiz"
      SORT file.name ASC
      LIMIT 10
      ```
      </div>
      <div style="margin-top: 1rem;">
        ```meta-bind-button
        label: View All Quizzes
        style: default
        class: ocds-btn
        action:
          type: command
          command: obsidian-dataview:dataview-force-refresh-views
        ```
      </div>
    </div>
  </div>
</div>

<div class="ocds-section">
  <h2>📊 Progress Tracking</h2>
  
  <div class="ocds-card">
    ```dataviewjs
    const capsuleId = "test_capsule_123";
    const pages = dv.pages().where(p => p.source_capsules && p.source_capsules.includes(capsuleId));
    let totalTasks = 0;
    let completedTasks = 0;

    for (let page of pages) {
        if (page.file.tasks) {
            totalTasks += page.file.tasks.length;
            completedTasks += page.file.tasks.where(t => t.completed).length;
        }
    }

    if (totalTasks > 0) {
        const percentage = Math.round((completedTasks / totalTasks) * 100);
        dv.paragraph(`
          <div class="ocds-header__meta" style="justify-content: space-between; margin-bottom: 0.5rem;">
            <span>Completion</span>
            <span>${percentage}%</span>
          </div>
          <div class="ocds-progress-container">
            <div class="ocds-progress-bar" style="width: ${percentage}%"></div>
          </div>
          <p class="ocds-text-sm ocds-text-muted" style="margin-top: 0.5rem;">${completedTasks}/${totalTasks} tasks completed</p>
        `);
    } else {
        dv.paragraph("No tasks found in this capsule.");
    }
    ```
  </div>

  <h3>Active Timeline</h3>
  <div class="ocds-table-container">
  ```dataview
  TASK
  WHERE contains(source_capsules, "test_capsule_123")
    AND !completed
  SORT due ASC
  LIMIT 10
  ```
  </div>
</div>

<div class="ocds-section">
  <h2>Recent Activity</h2>
  <div class="ocds-table-container">
  ```dataview
  TABLE type, updated
  FROM ""
  WHERE contains(source_capsules, "test_capsule_123")
    AND type != "dashboard"
    AND type != "capsule_dashboard"
  SORT updated DESC
  LIMIT 10
  ```
  </div>
</div>

<div class="ocds-section">
  ### Domain Specific Content

This is a placeholder for domain sections.
</div>

</div> <!-- End Content -->

</div> <!-- End Grid -->

</div> <!-- End Dashboard -->
