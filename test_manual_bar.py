#!/usr/bin/env python3
"""Test manual progress bar with mutable table."""

import time
import threading
from collections import deque
from rich.console import Console
from rich.live import Live
from rich.panel import Panel
from rich.table import Table

def test_manual_progress_bar_simulation(capsys):
    console = Console(record=True, width=80)
    # Shared state
    recent_lines = deque(maxlen=5)
    progress_data = {'current': 0, 'total': 17, 'status': 'Starting...'}

    def make_panel() -> Panel:
        """Create a new panel with the current progress."""
        completed = progress_data['current']
        total = progress_data['total']
        percentage = int((completed / total) * 100) if total > 0 else 0
        
        bar_width = 40
        filled = int((completed / total) * bar_width) if total > 0 else 0
        bar = "━" * filled + "╺" + " " * (bar_width - filled - 1) if filled < bar_width else "━" * bar_width
        
        progress_line = f"[cyan]  {progress_data['status']} {bar} {percentage:>3}%"
        
        table = Table.grid(expand=True)
        table.add_column()
        table.add_row(progress_line)
        table.add_row("")
        
        for line in recent_lines:
            table.add_row(f"  [dim]{line}")
            
        return Panel(table, title="[cyan]Test Progress", border_style="cyan", padding=(1, 1))

    # Simulate the work
    for i in range(1, 18):
        progress_data['current'] = i
        progress_data['status'] = f"Step {i}/17"
        recent_lines.append(f"✅ Completed step {i}")
        console.print(make_panel())

    # Final state check
    progress_data['status'] = 'Complete!'
    console.print(make_panel())

    captured_output = console.export_text()
    assert "Test Progress" in captured_output
    assert "Step 1/17" in captured_output
    assert "Step 17/17" in captured_output
    assert "Complete!" in captured_output
    assert "✅ Completed step 17" in captured_output

