# End-to-End (E2E) Testing Guide for Obsidian Capsule Delivery

**For QA Lead & Testers**
**Purpose: Step-by-step instructions for manual E2E testing of the capsule system.**

---

## 1. Prerequisites

Before starting the test, ensure you have the following installed:

- **Python 3.10+**: Required to run the CLI.
- **Obsidian (Optional)**: Useful for visual verification of the vault, but file system checks are sufficient.
- **Project Source Code**: Clone the repository to your local machine.

### Install Dependencies

Navigate to the project root and install the package in editable mode (or use `uv` / `poetry` if configured):

```bash
pip install -e .
```

Verify the installation:

```bash
capsule --help
```

---

## 2. Setup

We will create a temporary environment to avoid modifying your actual Obsidian vaults.

### 2.1 Create a Dummy Vault

Create a directory structure that simulates an empty Obsidian vault.

```bash
# Create a directory for the test vault
mkdir -p ~/tmp/TestVault

# Create a .obsidian folder (simulates a real vault)
mkdir -p ~/tmp/TestVault/.obsidian
```

### 2.2 Configure the Project

You can either modify the global config or, preferably, use the `--target` flag during the import step to point to your dummy vault.

For this guide, we will use the `--target` flag to keep the global config clean.

If you wish to set it globally:
1. Locate `config.yaml` (usually in `~/.config/capsule/` or the project root).
2. Set `user.vault_path` to `~/tmp/TestVault`.

---

## 3. Test Scenario

This scenario covers the full lifecycle: Creating content -> Packaging (Export) -> Delivering (Import) -> Verifying.

### Step 1: Create a Source Capsule

Create a folder that represents the "Capsule" you want to distribute.

```bash
# Create a source directory for the capsule
mkdir -p ~/tmp/SourceCapsule

# Create the manifest file (capsule-cypher.yaml)
cat <<EOF > ~/tmp/SourceCapsule/capsule-cypher.yaml
capsule_id: "e2e_test_v1"
name: "E2E Test Capsule"
version: "1.0.0"
domain_type: "education"
folder_structure:
  content: "Content"
contents:
  content:
    - file: "Content/Hello_World.md"
data_schemas: {}
EOF

# Create a content file
mkdir -p ~/tmp/SourceCapsule/Content
cat <<EOF > ~/tmp/SourceCapsule/Content/Hello_World.md
---
title: Hello World
type: note
status: active
---

# Hello World

This is a test note from the E2E capsule.
EOF
```

### Step 2: Package/Export the Capsule

Use the CLI to export the source folder into a distributable `.capsule` file (which is a zip archive).

```bash
# Syntax: capsule export <source_folder> <output_file>
capsule export ~/tmp/SourceCapsule ~/tmp/e2e_test_v1.capsule
```

**Verification:**
- Check that `~/tmp/e2e_test_v1.capsule` exists.

### Step 3: Import the Capsule

Now, act as the end-user importing this capsule into their vault (`~/tmp/TestVault`).

```bash
# Syntax: capsule import <capsule_file> --target <vault_path>
capsule import ~/tmp/e2e_test_v1.capsule --target ~/tmp/TestVault
```

**Expected Behavior:**
1. The CLI should display a **Preview** of changes.
2. It should show that `Content/Hello_World.md` will be created.
3. It will ask for confirmation (unless `--force` is used).
4. Type `y` to proceed.

### Step 4: Verification

Check the "User's Vault" to ensure the content was delivered correctly.

**Check File Existence:**
```bash
ls -R ~/tmp/TestVault
```
*Expect to see `Content/Hello_World.md`.*

**Check Content Integrity:**
```bash
cat ~/tmp/TestVault/Content/Hello_World.md
```
*Verify that the frontmatter and body text match the source created in Step 1.*

---

## 4. Cleanup

After testing is complete, remove the temporary directories.

```bash
rm -rf ~/tmp/TestVault
rm -rf ~/tmp/SourceCapsule
rm ~/tmp/e2e_test_v1.capsule
```

---

## Troubleshooting

- **Command not found**: Ensure you are in the virtual environment where `capsule` is installed.
- **Permission denied**: Check read/write permissions for the `~/tmp` directory.
- **Import failed**: Run with `--debug` (if available) or check the console output for specific error messages.
