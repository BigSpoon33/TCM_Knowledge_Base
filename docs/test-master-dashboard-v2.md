---
type: master_dashboard
title: "My Knowledge System"
created: "2025-11-22"
updated: "2025-11-22"
cssclass: ocds-dashboard ocds-theme-neon
---

<div class="ocds-dashboard ocds-theme-neon">

<div class="ocds-header">
  <h1 class="ocds-header__title">My Knowledge System</h1>
  <div class="ocds-header__meta">
    <span>Updated: 2025-11-22</span>
  </div>
</div>

<div class="ocds-master-stats">
  <div class="ocds-stat-card">
    <div class="ocds-stat-value">12</div>
    <div class="ocds-stat-label">Capsules</div>
  </div>
  <div class="ocds-stat-card">
    <div class="ocds-stat-value">150</div>
    <div class="ocds-stat-label">Total Notes</div>
  </div>
  <div class="ocds-stat-card">
    <div class="ocds-stat-value">45</div>
    <div class="ocds-stat-label">Study Mats</div>
  </div>
  <div class="ocds-stat-card">
    <div class="ocds-stat-value">Active</div>
    <div class="ocds-stat-label">Status</div>
  </div>
</div>

<div class="ocds-master-grid">

<div class="ocds-master-main">

<div class="ocds-section">
  <h2>📚 Installed Capsules</h2>
  <div class="ocds-table-container">
  ```dataview
  TABLE 
    capsule_id as "ID",
    version as "Version",
    dashboard_metadata.topic as "Topic",
    dashboard_metadata.category as "Category"
  FROM ""
  WHERE type = "capsule_dashboard"
  SORT file.name ASC
  ```
  </div>
</div>

<div class="ocds-section">
  <h2>🔍 Interactive Filters</h2>
  <div class="ocds-card">
    <p>Type in the fields below to dynamically filter the capsule list.</p>
    
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-bottom: 1rem;">
      <div>
        <label class="ocds-text-sm ocds-text-muted">Class</label>
        <input type="text" id="classFilter" class="ocds-input" style="width: 100%" placeholder="e.g., TCM101">
      </div>
      <div>
        <label class="ocds-text-sm ocds-text-muted">Topic</label>
        <input type="text" id="topicFilter" class="ocds-input" style="width: 100%" placeholder="e.g., Herbal Medicine">
      </div>
    </div>
  </div>
</div>

</div> <!-- End Main -->

<div class="ocds-master-sidebar">

<div class="ocds-section">
  <h3>🗓️ Active Timelines</h3>
  <div class="ocds-table-container">
  ```dataview
  TASK
  WHERE source_capsules
    AND !completed
  SORT due ASC
  LIMIT 10
  ```
  </div>
</div>

</div> <!-- End Sidebar -->

</div> <!-- End Grid -->

</div> <!-- End Dashboard -->
