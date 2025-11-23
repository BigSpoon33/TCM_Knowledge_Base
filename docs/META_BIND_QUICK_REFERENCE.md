# Meta-Bind Quick Reference for Epic 12

**Quick access guide for dashboard developers**

---

## ✅ Proven Patterns (Ready to Use)

### Navigation Button
```markdown
```meta-bind-button
label: 📚 Continue Learning
style: primary
action:
  type: open
  link: "[[Study_Material]]"
\```
```

### Quiz Question
```markdown
`INPUT[select(option(A), option(B), option(C), option(D)):q1_answer]`
```

### Display Value
```markdown
**Score:** `VIEW[{score}][text]` / 10
```

---

## ⚠️ Needs Testing

### Progress Bar
```markdown
```meta-bind
INPUT[progressBar(minValue(0), maxValue(100), value(grade))]
\```
```
**Action:** Test before using in Epic 12

### Task Toggle
```markdown
`INPUT[toggle(onValue(true), offValue(false)):completed]`
```
**Action:** Test TaskNotes integration

---

## 🚀 Epic 12 New Patterns

### Filter Control (Proposed)
```markdown
`INPUT[select(option(All), option(Week 1)):filter]`
```
**Action:** Research DataviewJS integration

---

## Common Pitfalls

1. **Syntax Errors:** Watch nested parentheses in options
2. **Reading Mode:** Some elements need Reading Mode
3. **Frontmatter:** Field must exist in frontmatter first
4. **Escaping:** Use `\```  in code blocks to show meta-bind syntax

---

## Resources

- **Full Evaluation:** `docs/META_BIND_EVALUATION_EPIC_12.md`
- **Vault Guide:** `OCDS_Documentation/02_Plugin_Integration/Meta_Bind_Syntax.md`
- **Official Docs:** https://www.moritzjung.dev/obsidian-meta-bind-plugin-docs/
- **Working Example:** `Quiz Example.md`

---

**Status:** ✅ Ready for Epic 12
