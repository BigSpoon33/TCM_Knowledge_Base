---
# This is a comment at the top
id: complex-note-001
name: Complex Note Test
type: test_note
tags:
  - test
  - complex
  - yaml

# Section with block scalar
description: |
  This is a multi-line description.
  It preserves newlines.

  And blank lines.

# Section with nested data
metadata:
  created: 2025-11-21
  updated: 2025-11-21
  author: BMad # Inline comment

  # Nested list
  contributors:
    - name: Alice
      role: Developer
    - name: Bob
      role: Reviewer

# Domain specific data
herb_data:
  hanzi: "生姜"
  pinyin: "Shēng Jiāng"
  temperature: warm
  # List of functions
  functions:
    - releases the exterior
    - warms the middle jiao
---
# Body Content
This is the body of the note.

It has multiple lines.
And some markdown *formatting*.
