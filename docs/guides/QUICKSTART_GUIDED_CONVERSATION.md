# Quick Start: Guided Conversation Learning

## 🎓 Interactive Learning Mode

Start a real-time conversation with AI assessment:

```bash
# Set API key
export GEMINI_API_KEY="AIzaSyCsTagD8ODpN2A_OMtcM0vtw0Nn8fByCKs"

# Navigate to project
cd /home/shuma/Documents/AI_Suite/TCM_Knowledge_Base

# Start conversation
python scripts/generate_guided_conversation.py "Lung Yin Deficiency"
```

### What Happens:
1. AI asks you about each section of the pattern
2. You answer in your own words
3. AI assesses your understanding (0-100 score)
4. If score < 71: AI explains missing concepts, asks follow-up
5. If score ≥ 71: Move to next section
6. Progress tracked throughout

### Commands:
- Type your answer normally
- `skip` - Skip current section
- `quit` - Exit and save progress

---

## 📝 Generate Study Guide (Script Mode)

Create a markdown conversation guide for self-study:

```bash
python scripts/generate_guided_conversation.py "Lung Yin Deficiency" --script-only
```

**Output:** `Materials/TCM_101/Lung_Yin_Deficiency_Guided_Conversation.md`

Use this for:
- Offline study
- Exam preparation
- Discussion prompts
- Self-assessment

---

## 📦 Generate All Materials (Including Conversation)

Create complete learning package:

```bash
python scripts/generate_all_materials.py "Lung Yin Deficiency" --class-id TCM_101
```

**Generates:**
- Flashcards
- Question Bank
- Slides
- **Guided Conversation** ⭐
- Study Material
- Tasks

---

## 🎯 Example Interaction

```
╔══════════════════════════════════════════════════════════╗
║  🎓 TCM GUIDED LEARNING CONVERSATION                     ║
╚══════════════════════════════════════════════════════════╝

📘 Topic: Lung Yin Deficiency
📊 Total Sections: 9

Progress: [████░░░░░░] 4/9 sections (44%)

📌 Clinical Manifestations

❓ What are the cardinal symptoms and diagnostic features 
   of Lung Yin Deficiency?

Your answer: Dry cough, night sweats, and dry mouth

🤔 Assessing your response...

🟡 Score: 65/100 (FAIR)

✅ What you got right:
   • Mentioned dry cough (cardinal symptom)
   • Identified night sweats (deficiency heat sign)
   • Noted dry mouth (dryness manifestation)

⚠️  Areas to review:
   • Tongue presentation (red, peeled coating)
   • Pulse characteristics (thin, rapid)
   • Complete triad: dryness, deficiency heat, impaired function

📝 Feedback: Good start! You've identified key symptoms. 
    Let's add the diagnostic features (tongue/pulse) to 
    complete the picture.

💡 Let me help clarify...

[AI explains tongue and pulse presentation]

❓ Can you now describe the tongue and pulse presentation?

Your answer: _
```

---

## 🔧 Customization

### Adjust Max Attempts

```bash
# Allow 5 attempts per section instead of default 3
python scripts/generate_guided_conversation.py "Lung Yin Deficiency" --max-attempts 5
```

### Custom Output Directory

```bash
python scripts/generate_guided_conversation.py "Lung Yin Deficiency" \
  --script-only \
  --output-dir /path/to/custom/dir
```

---

## 📊 View Progress

Conversation logs saved to:
```
Materials/TCM_101/conversation_logs/
└── {Pattern}_conversation_{timestamp}.json
```

Contains:
- All questions and answers
- Assessment scores
- Time spent per section
- Weak/strong areas identified

---

## 💡 Tips for Best Results

### For Interactive Mode:
1. **Answer in complete sentences** - AI assesses depth of understanding
2. **Use TCM terminology** - Shows mastery of concepts
3. **Provide examples** - Demonstrates application
4. **Don't rush** - Take time to think through answers
5. **Review feedback** - Learn from missing concepts

### For Script Mode:
1. **Answer before checking** - Test true recall
2. **Compare to key concepts** - Identify gaps
3. **Review reference content** - Fill knowledge holes
4. **Repeat weak sections** - Spaced repetition

---

## 🎯 Assessment Levels

| Score | What It Means | What Happens |
|-------|---------------|--------------|
| **71-100** 🟢 | Solid understanding | Advance to next section |
| **41-70** 🟡 | Partial understanding | Get explanation + follow-up |
| **0-40** 🔴 | Missing key concepts | Detailed explanation + retry |

---

## 🚨 Troubleshooting

**"GEMINI_API_KEY not set"**
```bash
export GEMINI_API_KEY="your-key-here"
```

**"Root note not found"**
- Check file exists in `Materials/TCM_101/`
- Verify frontmatter has `type: root_note`
- Try full filename: `Root_Note_Lung_Yin_Deficiency`

**Assessment seems off**
- AI is calibrated for TCM students
- Provide more detail in answers
- Use specific terminology
- Give clinical examples

---

## 📚 Next Steps

After completing guided conversation:

1. **Review weak areas** - Check conversation log
2. **Use flashcards** - Reinforce weak concepts
3. **Take quiz** - Test knowledge
4. **Review slides** - Visual reinforcement
5. **Repeat conversation** - Spaced repetition

---

**Ready to start learning? Run the command above!** 🚀
