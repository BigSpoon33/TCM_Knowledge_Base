---
type: widget_gallery
cssclass: ocds-dashboard ocds-theme-neon
progress_value: 45
filter_class: "TCM101"
filter_active: true
---

<div class="ocds-dashboard ocds-theme-neon">

<div class="ocds-header">
  <h1 class="ocds-header__title">Meta-Bind Widget Gallery</h1>
  <div class="ocds-header__meta">
    <span>Test Suite</span>
    <span>v1.0</span>
  </div>
</div>

<div class="ocds-section">
  <h2>1. Navigation Buttons</h2>
  <p>Standard buttons for dashboard navigation.</p>
  
  <div class="ocds-card">
    <div style="display: flex; gap: 1rem; flex-wrap: wrap;">
      <!-- Primary Button -->
      ```meta-bind-button
      label: Start Learning
      style: primary
      class: ocds-btn ocds-btn-primary
      action:
        type: command
        command: app:open-settings
      ```

      <!-- Secondary Button (using default style) -->
      ```meta-bind-button
      label: View Flashcards
      style: default
      class: ocds-btn
      action:
        type: command
        command: app:open-settings
      ```
    </div>
  </div>
</div>

<div class="ocds-section">
  <h2>2. Input Fields</h2>
  <p>Inputs bound to frontmatter for filtering.</p>
  
  <div class="ocds-card">
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;">
      
      <!-- Text Input -->
      <div>
        <label class="ocds-text-sm ocds-text-muted">Class Filter</label>
        ```meta-bind
        INPUT[text:filter_class]
        ```
      </div>

      <!-- Toggle -->
      <div>
        <label class="ocds-text-sm ocds-text-muted">Active Only</label>
        ```meta-bind
        INPUT[toggle:filter_active]
        ```
      </div>

      <!-- Select -->
      <div>
        <label class="ocds-text-sm ocds-text-muted">Category</label>
        ```meta-bind
        INPUT[inlineSelect(option(All), option(TCM), option(Coding)):filter_class]
        ```
      </div>

    </div>
    
    <div style="margin-top: 1rem; padding: 0.5rem; background: var(--ocds-bg-dashboard); border-radius: 4px;">
      <strong>Current State:</strong><br>
      Class: `VIEW[{filter_class}]`<br>
      Active: `VIEW[{filter_active}]`
    </div>
  </div>
</div>

<div class="ocds-section">
  <h2>3. Progress Bars</h2>
  <p>Visualizing completion status.</p>
  
  <div class="ocds-card">
    <div class="ocds-header__meta" style="justify-content: space-between; margin-bottom: 0.5rem;">
      <span>Course Progress</span>
      <span>`VIEW[{progress_value}]`%</span>
    </div>
    
    <!-- Meta-Bind Progress Bar -->
    ```meta-bind
    INPUT[progressBar(minValue(0), maxValue(100), value(progress_value))]
    ```
    
    <div style="margin-top: 1rem;">
      <label class="ocds-text-sm ocds-text-muted">Adjust Progress:</label>
      ```meta-bind
      INPUT[slider(minValue(0), maxValue(100)):progress_value]
      ```
    </div>
  </div>
</div>

<div class="ocds-section">
  <h2>4. View Fields</h2>
  <p>Dynamic data display.</p>
  
  <div class="ocds-stat-card">
    <div class="ocds-stat-value">`VIEW[{progress_value}]`</div>
    <div class="ocds-stat-label">Dynamic Score</div>
  </div>
</div>

</div>
