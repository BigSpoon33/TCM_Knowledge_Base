# Dashboard Metadata Schema - Test Plan

**Story:** 11-1-capsule-dashboard-metadata-schema  
**Date:** 2025-11-22  
**Purpose:** Validate the capsule dashboard frontmatter schema defined in Story 11-1

---

## Test Strategy

### Unit Tests

**Test Suite: Schema Validation**

Location: `tests/test_models/test_dashboard_schema.py`

**Test Case 1.1: Required Fields Validation**
- **Objective**: Verify schema requires `type`, `capsule_id`, and `version` fields
- **Method**: Create dashboard notes with missing required fields
- **Expected**: Validation error for each missing required field
- **Test Data**: 
  - Missing `type` → Error
  - Missing `capsule_id` → Error
  - Missing `version` → Error

**Test Case 1.2: Optional Metadata Fields**
- **Objective**: Verify optional metadata fields can be omitted
- **Method**: Create dashboard note with only required fields
- **Expected**: Validation succeeds, optional fields default to null
- **Test Data**: Dashboard with only `type`, `capsule_id`, `version`

**Test Case 1.3: Field Data Types**
- **Objective**: Verify correct data types for all fields
- **Method**: Create dashboard with various data types
- **Expected**: 
  - `type`: string
  - `capsule_id`: string
  - `version`: string (semver format)
  - `dashboard_metadata.class`: string or null
  - `dashboard_metadata.topic`: string or null
  - `dashboard_metadata.category`: string or null
  - `dashboard_metadata.active`: boolean or null

**Test Case 1.4: Nested Metadata Structure**
- **Objective**: Verify `dashboard_metadata` is properly nested object
- **Method**: Parse frontmatter and access nested fields
- **Expected**: Access via `dashboard_metadata.class`, `dashboard_metadata.topic`, etc.

### Integration Tests

**Test Suite: Dataview Query Compatibility**

Location: `tests/test_integration/test_dashboard_queries.py`

**Test Case 2.1: Filter by Active Status**
- **Objective**: Verify Dataview can filter by `active` field
- **Method**: 
  1. Create 3 dashboards: 2 active, 1 inactive
  2. Execute Dataview query filtering `active = true`
  3. Count results
- **Expected**: Returns 2 active dashboards
- **Query**:
  ```dataview
  TABLE capsule_id
  FROM ""
  WHERE type = "capsule_dashboard"
    AND dashboard_metadata.active = true
  ```

**Test Case 2.2: Filter by Class**
- **Objective**: Verify Dataview can filter by `class` field
- **Method**: 
  1. Create 3 dashboards: 2 with class="TCM101", 1 with class="Herbology"
  2. Execute Dataview query filtering `class = "TCM101"`
  3. Count results
- **Expected**: Returns 2 "TCM101" dashboards
- **Query**:
  ```dataview
  TABLE capsule_id, dashboard_metadata.class
  FROM ""
  WHERE type = "capsule_dashboard"
    AND dashboard_metadata.class = "TCM101"
  ```

**Test Case 2.3: Filter by Topic**
- **Objective**: Verify Dataview can filter by `topic` field
- **Method**: 
  1. Create dashboards with different topics
  2. Execute Dataview query filtering `topic = "Herbal Medicine"`
- **Expected**: Returns only dashboards with matching topic

**Test Case 2.4: Filter by Category**
- **Objective**: Verify Dataview can filter by `category` field
- **Method**: 
  1. Create dashboards with categories: "CALE", "NCCAOM", null
  2. Execute Dataview query filtering `category = "CALE"`
- **Expected**: Returns only "CALE" dashboards

**Test Case 2.5: Combined Filters**
- **Objective**: Verify multiple metadata filters work together
- **Method**: 
  1. Create diverse set of dashboards
  2. Execute query with multiple WHERE clauses
- **Expected**: Only dashboards matching all criteria returned
- **Query**:
  ```dataview
  TABLE capsule_id
  FROM ""
  WHERE type = "capsule_dashboard"
    AND dashboard_metadata.class = "TCM101"
    AND dashboard_metadata.active = true
    AND dashboard_metadata.category = "CALE"
  ```

**Test Case 2.6: DataviewJS Complex Filtering**
- **Objective**: Verify DataviewJS can perform advanced filtering
- **Method**: 
  1. Create dashboards with various metadata combinations
  2. Execute DataviewJS query with custom logic (AND/OR combinations)
- **Expected**: Custom filter logic works correctly
- **Query**: See sample in `tests/fixtures/sample_capsule_dashboard.md` (Test Query 4)

### End-to-End Tests

**Test Suite: Schema in Full Workflow**

Location: `tests/test_e2e/test_dashboard_import.py`

**Test Case 3.1: Dashboard Generation with Metadata**
- **Objective**: Verify dashboard generated during import includes metadata
- **Method**: 
  1. Create test capsule with `dashboard_metadata` in cypher
  2. Execute `capsule import`
  3. Read generated dashboard frontmatter
- **Expected**: Dashboard contains all metadata fields from cypher

**Test Case 3.2: Dashboard Without Metadata**
- **Objective**: Verify dashboard generation works without optional metadata
- **Method**: 
  1. Create test capsule with no `dashboard_metadata` in cypher
  2. Execute `capsule import`
  3. Read generated dashboard frontmatter
- **Expected**: Dashboard has required fields, no `dashboard_metadata` section

**Test Case 3.3: Master Dashboard Filtering**
- **Objective**: Verify master dashboard can filter installed capsules by metadata
- **Method**: 
  1. Import 3 capsules with different metadata
  2. Open master dashboard in test Obsidian vault
  3. Execute filter queries
- **Expected**: Filters return correct capsule subsets

### Manual Tests

**Test Suite: PoC Validation**

**Manual Test 1: PoC Query Compatibility**
- **Objective**: Verify schema supports all queries from 11-0-dataview-spike-poc.md
- **Method**: 
  1. Review PoC queries in lines 583-651
  2. For each query, verify schema provides required fields
  3. Execute queries in test vault
- **Expected**: All PoC queries work without modification

**Manual Test 2: Obsidian Dataview Rendering**
- **Objective**: Verify queries render correctly in Obsidian
- **Method**: 
  1. Open sample dashboard in Obsidian
  2. Enable Dataview plugin
  3. Verify all queries execute without errors
- **Expected**: All queries display results, no syntax errors

**Manual Test 3: Graceful Degradation**
- **Objective**: Verify dashboard readable without Dataview
- **Method**: 
  1. Open sample dashboard in Obsidian
  2. Disable Dataview plugin
  3. Verify content is still readable
- **Expected**: Frontmatter visible, queries shown as code blocks

---

## Test Data

### Sample Dashboards

**Dashboard 1: Active TCM101 Capsule**
```yaml
---
type: capsule_dashboard
capsule_id: "TCM_Herbs_v1"
version: "1.0.0"
dashboard_metadata:
  class: "TCM101"
  topic: "Herbal Medicine"
  category: "CALE"
  active: true
source_capsules: ["TCM_Herbs_v1"]
---
```

**Dashboard 2: Inactive Herbology Capsule**
```yaml
---
type: capsule_dashboard
capsule_id: "Culinary_Herbs_v1"
version: "2.0.0"
dashboard_metadata:
  class: "Herbology"
  topic: "Culinary Applications"
  category: "General"
  active: false
source_capsules: ["Culinary_Herbs_v1"]
---
```

**Dashboard 3: Minimal Metadata Capsule**
```yaml
---
type: capsule_dashboard
capsule_id: "TCM_Points_v1"
version: "1.0.0"
dashboard_metadata:
  topic: "Acupuncture Points"
  active: true
source_capsules: ["TCM_Points_v1"]
---
```

**Dashboard 4: No Metadata Capsule**
```yaml
---
type: capsule_dashboard
capsule_id: "Test_Capsule_v1"
version: "1.0.0"
source_capsules: ["Test_Capsule_v1"]
---
```

---

## Test Coverage Matrix

| Acceptance Criterion | Test Cases | Coverage Level |
|---------------------|------------|----------------|
| AC1: Clear, consistent schema | 1.1, 1.2, 1.3, 1.4 | Unit |
| AC2: capsule_id and version fields | 1.1, 3.1, 3.2 | Unit + E2E |
| AC3: Filterable metadata fields | 2.1, 2.2, 2.3, 2.4, 2.5 | Integration |
| AC4: Schema documented | Manual review | Manual |

---

## Validation Checklist

- [ ] All required fields validated (type, capsule_id, version)
- [ ] All optional metadata fields validated (class, topic, category, active)
- [ ] Data types correct for each field
- [ ] Nested dashboard_metadata structure works
- [ ] Dataview queries filter by active status
- [ ] Dataview queries filter by class
- [ ] Dataview queries filter by topic
- [ ] Dataview queries filter by category
- [ ] Combined filters work (multiple WHERE clauses)
- [ ] DataviewJS complex filtering works
- [ ] Dashboard generation includes metadata
- [ ] Dashboard generation works without metadata
- [ ] All PoC queries compatible with schema
- [ ] Queries render correctly in Obsidian
- [ ] Graceful degradation without Dataview plugin

---

## Performance Expectations

Based on Story 11-0 technical spike findings:

- **Simple metadata queries**: < 10ms (Dataview indexed)
- **Complex combined filters**: 20-50ms
- **DataviewJS filtering**: 30-70ms

All query performance within acceptable range for <500 note vaults.

---

## References

- Schema definition: `docs/architecture.md` → "Capsule Dashboard Metadata Schema" section
- PoC validation: `docs/sprint-artifacts/11-0-dataview-spike-poc.md` (lines 583-651)
- Technical specification: `docs/sprint-artifacts/tech-spec-epic-11.md`
- Sample dashboard: `tests/fixtures/sample_capsule_dashboard.md`
