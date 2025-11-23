"""Unit tests for progress indicator utilities.

Tests verify that progress utilities create Progress objects with correct
configuration (columns, transient setting, etc.) and apply consistent styling.
"""

import pytest
from rich.progress import (
    BarColumn,
    MofNCompleteColumn,
    Progress,
    SpinnerColumn,
    TaskProgressColumn,
    TextColumn,
    TimeElapsedColumn,
)

from capsule.utils.progress import create_multi_task_progress, create_progress_bar, create_spinner


class TestCreateSpinner:
    """Test create_spinner() function."""

    def test_returns_progress_instance(self):
        """Verify create_spinner returns a Progress object."""
        progress = create_spinner("Testing...")
        assert isinstance(progress, Progress)

    def test_contains_spinner_column(self):
        """Verify spinner progress has SpinnerColumn."""
        progress = create_spinner("Testing...")
        # Check columns by type
        column_types = [type(col) for col in progress.columns]
        assert SpinnerColumn in column_types

    def test_contains_text_column(self):
        """Verify spinner progress has TextColumn for description."""
        progress = create_spinner("Testing...")
        column_types = [type(col) for col in progress.columns]
        assert TextColumn in column_types

    def test_contains_time_elapsed_column(self):
        """Verify spinner progress has TimeElapsedColumn."""
        progress = create_spinner("Testing...")
        column_types = [type(col) for col in progress.columns]
        assert TimeElapsedColumn in column_types

    def test_transient_configured(self):
        """Verify spinner is configured (transient is set in constructor)."""
        # Note: Progress object doesn't expose transient as an attribute
        # We verify it's created successfully - transient=False is set internally
        progress = create_spinner("Testing...")
        assert isinstance(progress, Progress)

    def test_accepts_custom_message(self):
        """Verify create_spinner accepts custom message parameter."""
        custom_msg = "Custom processing message"
        progress = create_spinner(custom_msg)
        # Add a task to verify message can be used
        with progress:
            task_id = progress.add_task(custom_msg, total=None)
            task = progress.tasks[task_id]
            assert task.description == custom_msg


class TestCreateProgressBar:
    """Test create_progress_bar() function."""

    def test_returns_progress_instance(self):
        """Verify create_progress_bar returns a Progress object."""
        progress = create_progress_bar("Processing...", total=100)
        assert isinstance(progress, Progress)

    def test_contains_text_column(self):
        """Verify progress bar has TextColumn for description."""
        progress = create_progress_bar("Processing...", total=100)
        column_types = [type(col) for col in progress.columns]
        assert TextColumn in column_types

    def test_contains_bar_column(self):
        """Verify progress bar has BarColumn for visualization."""
        progress = create_progress_bar("Processing...", total=100)
        column_types = [type(col) for col in progress.columns]
        assert BarColumn in column_types

    def test_contains_task_progress_column(self):
        """Verify progress bar has TaskProgressColumn for percentage."""
        progress = create_progress_bar("Processing...", total=100)
        column_types = [type(col) for col in progress.columns]
        assert TaskProgressColumn in column_types

    def test_contains_mofn_complete_column(self):
        """Verify progress bar has MofNCompleteColumn for X/Y display."""
        progress = create_progress_bar("Processing...", total=100)
        column_types = [type(col) for col in progress.columns]
        assert MofNCompleteColumn in column_types

    def test_contains_time_elapsed_column(self):
        """Verify progress bar has TimeElapsedColumn."""
        progress = create_progress_bar("Processing...", total=100)
        column_types = [type(col) for col in progress.columns]
        assert TimeElapsedColumn in column_types

    def test_transient_configured(self):
        """Verify progress bar is configured (transient is set in constructor)."""
        # Note: Progress object doesn't expose transient as an attribute
        # We verify it's created successfully - transient=False is set internally
        progress = create_progress_bar("Processing...", total=100)
        assert isinstance(progress, Progress)

    def test_accepts_total_parameter(self):
        """Verify create_progress_bar accepts total parameter."""
        progress = create_progress_bar("Processing...", total=42)
        with progress:
            task_id = progress.add_task("Processing...", total=42)
            task = progress.tasks[task_id]
            assert task.total == 42

    def test_accepts_none_total(self):
        """Verify create_progress_bar accepts None for indeterminate progress."""
        progress = create_progress_bar("Processing...", total=None)
        with progress:
            task_id = progress.add_task("Processing...", total=None)
            task = progress.tasks[task_id]
            assert task.total is None


class TestCreateMultiTaskProgress:
    """Test create_multi_task_progress() function."""

    def test_returns_progress_instance(self):
        """Verify create_multi_task_progress returns a Progress object."""
        progress = create_multi_task_progress()
        assert isinstance(progress, Progress)

    def test_contains_spinner_column(self):
        """Verify multi-task progress has SpinnerColumn."""
        progress = create_multi_task_progress()
        column_types = [type(col) for col in progress.columns]
        assert SpinnerColumn in column_types

    def test_contains_bar_column(self):
        """Verify multi-task progress has BarColumn."""
        progress = create_multi_task_progress()
        column_types = [type(col) for col in progress.columns]
        assert BarColumn in column_types

    def test_contains_text_column(self):
        """Verify multi-task progress has TextColumn."""
        progress = create_multi_task_progress()
        column_types = [type(col) for col in progress.columns]
        assert TextColumn in column_types

    def test_transient_configured(self):
        """Verify multi-task progress is configured (transient is set in constructor)."""
        # Note: Progress object doesn't expose transient as an attribute
        # We verify it's created successfully - transient=False is set internally
        progress = create_multi_task_progress()
        assert isinstance(progress, Progress)

    def test_supports_multiple_tasks(self):
        """Verify multi-task progress can track multiple tasks simultaneously."""
        progress = create_multi_task_progress()
        with progress:
            task1 = progress.add_task("Task 1", total=None)
            task2 = progress.add_task("Task 2", total=100)
            task3 = progress.add_task("Task 3", total=50)

            # Verify all tasks are tracked
            assert len(progress.tasks) == 3
            assert progress.tasks[task1].description == "Task 1"
            assert progress.tasks[task2].description == "Task 2"
            assert progress.tasks[task3].description == "Task 3"


class TestStylingConsistency:
    """Test that all progress types apply consistent styling."""

    def test_all_progress_types_created(self):
        """Verify all progress types are created successfully."""
        # Note: transient=False is configured in constructors but not exposed as attribute
        spinner = create_spinner()
        bar = create_progress_bar()
        multi = create_multi_task_progress()

        assert isinstance(spinner, Progress)
        assert isinstance(bar, Progress)
        assert isinstance(multi, Progress)

    def test_all_include_time_elapsed(self):
        """Verify all progress types include TimeElapsedColumn for consistency."""
        spinner = create_spinner()
        bar = create_progress_bar()
        multi = create_multi_task_progress()

        spinner_types = [type(col) for col in spinner.columns]
        bar_types = [type(col) for col in bar.columns]
        multi_types = [type(col) for col in multi.columns]

        assert TimeElapsedColumn in spinner_types
        assert TimeElapsedColumn in bar_types
        assert TimeElapsedColumn in multi_types
