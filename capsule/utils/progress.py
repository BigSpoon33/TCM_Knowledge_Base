"""Progress indicator utilities for the Capsule CLI.

This module provides standardized progress indicators using the Rich library.
All progress bars use consistent styling and configuration across commands.
"""

from typing import Optional

from rich.progress import (
    BarColumn,
    MofNCompleteColumn,
    Progress,
    SpinnerColumn,
    TaskProgressColumn,
    TextColumn,
    TimeElapsedColumn,
)


def create_spinner(message: str = "Processing...") -> Progress:
    """Create a spinner progress indicator for indeterminate operations.

    Args:
        message: Description text to show next to spinner

    Returns:
        Progress instance configured with spinner column

    Example:
        with create_spinner("Deep research...") as progress:
            task = progress.add_task(message, total=None)
            # Perform work...
            progress.update(task, description="Deep research... (5/10 sources)")

    Notes:
        - Use transient=False to keep completion status visible
        - Use total=None for indeterminate progress
        - Update description dynamically to show progress info
    """
    return Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        TimeElapsedColumn(),
        transient=False,  # Keep visible after completion
    )


def create_progress_bar(message: str = "Processing...", total: Optional[int] = None) -> Progress:
    """Create a progress bar with percentage and bar visualization.

    Args:
        message: Description text to show above progress bar
        total: Total number of items to process (None for indeterminate)

    Returns:
        Progress instance configured with bar and percentage columns

    Example:
        with create_progress_bar("Generating content...", total=100) as progress:
            task = progress.add_task(message, total=total)
            for i in range(total):
                # Do work...
                progress.update(task, advance=1)

    Notes:
        - Shows percentage completion and visual bar
        - Use MofNCompleteColumn for file counts (X/Y files)
        - transient=False ensures user sees final "100% complete" status
    """
    return Progress(
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TaskProgressColumn(),  # Shows percentage
        MofNCompleteColumn(),  # Shows "X/Y" count
        TimeElapsedColumn(),
        transient=False,  # Keep visible after completion
    )


def create_multi_task_progress() -> Progress:
    """Create a progress tracker for multiple simultaneous tasks.

    Returns:
        Progress instance that can track multiple tasks at once

    Example:
        with create_multi_task_progress() as progress:
            research_task = progress.add_task("Research phase", total=None)
            generation_task = progress.add_task("Generation phase", total=100)

            # Update tasks independently
            progress.update(research_task, description="Research... (3/10 sources)")
            progress.update(generation_task, advance=10)

    Notes:
        - Each task has its own row in the console
        - Useful for showing pipeline stages (research → generation → validation)
        - Tasks can have different total values (some indeterminate, some with counts)
    """
    return Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TaskProgressColumn(),
        MofNCompleteColumn(),
        TimeElapsedColumn(),
        transient=False,  # Keep visible after completion
    )
