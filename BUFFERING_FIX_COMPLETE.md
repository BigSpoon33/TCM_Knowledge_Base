# Deep Research Progress Display - Buffering Fix Complete

## Problem Identified

The progress display was not showing updates in real-time. All output was buffered and only appeared at the very end when the research completed.

### Root Cause
Python's default behavior is to buffer stdout when writing to pipes. The subprocess output was being captured but not flushed until the program finished.

## Solution Applied

Added **two layers of buffering fixes**:

### 1. Environment Variable in CLI (`capsule/commands/research.py`)
Set `PYTHONUNBUFFERED=1` environment variable when starting the subprocess:

```python
# Start the process with unbuffered output
env = {'GEMINI_API_KEY': api_key, 'PYTHONUNBUFFERED': '1', **os.environ}
process = subprocess.Popen(
    cmd_args,
    cwd=kb_path,
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    text=True,
    bufsize=1,
    env=env
)
```

This tells Python to not buffer output at all.

### 2. Explicit Flush Calls in Pipeline Scripts

Added `flush=True` to all `print()` statements in:

#### `scripts/deep_research_pipeline.py`
- Initial pipeline header prints
- All step announcement prints (STEP 0-7)
- All completion status prints

```python
print("🔬 STEP 1: Deep Research", flush=True)
print("-" * 70, flush=True)
# ... work happens ...
print(f"✅ Research complete ({len(research_context)} characters)\n", flush=True)
```

#### `scripts/content_generator.py`
- Section generation announcements
- Per-heading progress updates
- Completion messages

```python
print(f"   {'  ' * (level-1)}✍️  Generating: {heading_text}", flush=True)
# ... generation happens ...
print(f"   {'  ' * (level-1)}✅ Generated ({len(content)} chars)", flush=True)
```

## Files Modified

1. ✅ `capsule/commands/research.py` - Added PYTHONUNBUFFERED environment variable
2. ✅ `scripts/deep_research_pipeline.py` - Added flush=True to all print statements
3. ✅ `scripts/content_generator.py` - Added flush=True to all print statements

## Result

Now you'll see **real-time progress** like this:

```
╭─────────────────────────── Deep Research Progress ───────────────────────────╮
│ ⠼ Deep Research in progress...                                               │
│                                                                              │
│   🔬 STEP 1: Deep Research                                                   │
│   Starting Gemini research...                                                │
│   Analyzing TCM patterns...                                                  │
│   Gathering clinical information...                                          │
│   Synthesizing research findings...                                          │
╰──────────────────────────────────────────────────────────────────────────────╯
```

The display updates **immediately** as each line is printed, showing:
- ⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏ Animated spinner (confirms work is happening)
- Last 5 lines of output (shows what's currently being done)
- Real-time updates (no waiting until the end)

## Testing

Buffering fix was verified with a test script that:
1. Created a subprocess that prints with delays
2. Confirmed output appears line-by-line in real-time
3. Verified PYTHONUNBUFFERED + flush=True work together

## Why Both Fixes Are Needed

1. **PYTHONUNBUFFERED**: Disables Python's internal buffering at the process level
2. **flush=True**: Forces immediate write to stdout for each print statement

Using both together ensures:
- No line buffering delays
- Immediate output visibility
- Real-time progress tracking
- Works reliably across all systems

## Usage

Run deep research as normal - progress will now appear in real-time:

```bash
capsule research "yangming headache" --deep
capsule research "Spleen Qi Deficiency" --deep --class-id TCM_101
capsule research "Liver Blood Deficiency" --deep --depth exhaustive
```

## Technical Notes

### Why This Matters
- **User Feedback**: Users know the system is working, not frozen
- **Progress Tracking**: See which step takes the longest
- **Error Detection**: Spot issues immediately, not after waiting
- **Better UX**: Builds confidence that work is progressing

### Buffer Types Addressed
1. **Line buffering**: Disabled via PYTHONUNBUFFERED
2. **Block buffering**: Disabled via flush=True on each print
3. **Pipe buffering**: Minimized with bufsize=1 in Popen

### Alternative Approaches Considered
- Using `python -u` flag: Requires changing entry point
- Using `sys.stdout.flush()`: More verbose than flush=True
- Using `print(..., file=sys.stderr)`: Would break output capture

### Why Our Approach Is Best
✅ Works with existing CLI structure  
✅ Minimal code changes  
✅ No performance impact  
✅ Reliable across Python versions  
✅ Easy to maintain  

## Verification

To verify it's working:
1. Run: `capsule research "test topic" --deep --depth quick`
2. Watch for immediate output after each step starts
3. Spinner should animate continuously
4. Last 5 lines should update in real-time
5. No long silent periods

If you see output immediately (not all at the end), it's working! ✅
