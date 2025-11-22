# Security Checklist for File Operations

This checklist is intended to be used during the design and code review phases for any feature involving file operations (read, write, delete, extract, etc.).

## 1. Path Validation

- [ ] **Path Traversal Prevention:**
    - [ ] Are all file paths validated to ensure they are within the intended directory (e.g., using `pathlib.Path.resolve().relative_to()`)?
    - [ ] Are ".." components in paths explicitly checked or handled by the resolution process?
    - [ ] When extracting archives (zip, tar), is every member path validated *before* extraction?

- [ ] **Input Sanitization:**
    - [ ] Are filenames sanitized to remove potentially dangerous characters (e.g., null bytes, shell metacharacters)?
    - [ ] Are filenames checked for reserved names on target platforms (e.g., `CON`, `PRN` on Windows)?

## 2. File Permissions & Access Control

- [ ] **Least Privilege:**
    - [ ] Does the application run with the minimum necessary permissions?
    - [ ] Are file permissions set correctly on created files (e.g., not world-writable unless necessary)?

- [ ] **Overwrite Protection:**
    - [ ] Does the operation check if the destination file already exists?
    - [ ] Is there a mechanism to prevent accidental overwrites (e.g., user confirmation, unique filenames)?
    - [ ] Are backups created before destructive operations (overwrites, deletes)?

## 3. Temporary Files

- [ ] **Secure Creation:**
    - [ ] Are temporary directories created using secure methods (e.g., `tempfile.mkdtemp`)?
    - [ ] Are temporary files created with appropriate permissions?

- [ ] **Cleanup:**
    - [ ] Is there a robust mechanism to clean up temporary files and directories, even in case of errors (e.g., `try...finally` blocks)?

## 4. Resource Management

- [ ] **Size Limits:**
    - [ ] Are there limits on the size of files that can be read or extracted to prevent DoS?
    - [ ] Is there a limit on the number of files that can be processed?

- [ ] **Zip Bombs:**
    - [ ] When processing archives, is there a check for compression ratios or total extracted size to prevent zip bomb attacks?

## 5. Content Validation

- [ ] **File Type Verification:**
    - [ ] Is the file type verified (e.g., by magic numbers/headers) and not just by extension?
    - [ ] Is the content parsed safely (e.g., using `safe_load` for YAML)?

## 6. Error Handling & Logging

- [ ] **Information Leakage:**
    - [ ] Do error messages avoid revealing sensitive system paths or configuration details?
    - [ ] Are exceptions caught and handled gracefully?

- [ ] **Audit Trails:**
    - [ ] Are critical file operations logged (e.g., "File X extracted to Y")?

## 7. Review Sign-off

- [ ] **Design Review:** Security implications discussed during design phase.
- [ ] **Code Review:** Code verified against this checklist.
