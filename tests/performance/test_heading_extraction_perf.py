import time
import re
import tempfile
import os
from pathlib import Path
from capsule.utils.dataview_queries import build_heading_extraction_query


def generate_notes(count: int, directory: Path):
    for i in range(count):
        content = f"""
# Note {i}

## Ingredients
Ingredient A, Ingredient B, Ingredient C

## Other Section
Some text.
"""
        (directory / f"note_{i}.md").write_text(content)


def extract_heading_python(content: str, heading: str):
    # Python equivalent of the JS regex
    escaped_heading = re.escape(heading)
    pattern = rf"^#+\s+{escaped_heading}\s*\n([\s\S]*?)(?=\n#+|$)"
    match = re.search(pattern, content, re.MULTILINE)
    return match.group(1).strip() if match else None


def benchmark_extraction(note_count: int):
    with tempfile.TemporaryDirectory() as tmpdir:
        path = Path(tmpdir)
        generate_notes(note_count, path)

        start_time = time.time()

        # Simulate reading and extracting
        files = list(path.glob("*.md"))
        for file_path in files:
            content = file_path.read_text()
            extract_heading_python(content, "Ingredients")

        end_time = time.time()
        duration = end_time - start_time

        print(f"Processed {note_count} notes in {duration:.4f} seconds ({duration / note_count:.4f} s/note)")
        return duration


def test_performance():
    print("\n--- Benchmarking Heading Extraction (Python Simulation) ---")

    # Benchmark query generation (trivial)
    start = time.time()
    build_heading_extraction_query("#formula", "Ingredients")
    print(f"Query generation time: {time.time() - start:.6f} seconds")

    # Benchmark extraction simulation
    t10 = benchmark_extraction(10)
    t50 = benchmark_extraction(50)
    t100 = benchmark_extraction(100)

    # Assertions (loose, just to ensure it's not catastrophically slow)
    # Target < 5 seconds for 100 notes (Obsidian might be slower due to overhead, but Python should be fast)
    assert t100 < 1.0, "Python simulation of 100 notes took too long"


if __name__ == "__main__":
    test_performance()
