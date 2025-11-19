"""Guided conversation commands."""
import typer
import os
import sys
import subprocess
from pathlib import Path

from ..utils.config import get_config
from ..utils.validation import (
    validate_pattern_exists,
    validate_api_key,
    find_script_path,
    get_all_patterns,
)
from ..utils.output import (
    print_header,
    print_success,
    print_error,
    print_warning,
    print_suggestions,
)

conversation_app = typer.Typer()

@conversation_app.command("start")
def conversation_start(
    pattern: str,
    script: bool = typer.Option(False, "--script", help='Generate script only (no interactive mode)'),
    max_attempts: int = typer.Option(None, "--max-attempts", help='Maximum attempts per question'),
    output: str = typer.Option(None, "--output", help='Output file path')
):
    """Start a guided learning conversation about a TCM pattern."""
    config = get_config()
    
    # Get configuration values
    kb_path = Path(config.get('paths.knowledge_base', Path.cwd()))
    max_attempts = max_attempts or config.get('defaults.max_attempts', 3)
    
    # Validate API key
    api_key = config.get('api.gemini_key')
    is_valid, error_msg = validate_api_key(api_key)
    if not is_valid:
        print_error(error_msg)
        raise typer.Abort()
    
    # Validate pattern
    patterns_dir = kb_path / "TCM_Patterns"
    exists, matched_pattern, suggestions = validate_pattern_exists(pattern, patterns_dir)
    
    if not exists:
        print_error(f"Pattern '{pattern}' not found")
        
        if suggestions:
            print_suggestions(suggestions, "Did you mean:")
        else:
            all_patterns = get_all_patterns(patterns_dir)
            if all_patterns:
                print_suggestions(all_patterns[:10], "Available patterns:")
        
        print_warning("Use 'capsule list' to see all patterns")
        raise typer.Abort()
    
    # Use matched pattern
    pattern = matched_pattern or pattern
    
    # Print header
    mode = "Script Generation" if script else "Interactive"
    print_header(
        "Guided Conversation",
        f"Pattern: {pattern}\nMode: {mode}\nMax Attempts: {max_attempts}"
    )
    
    # Find conversation script
    scripts_dir = kb_path / "scripts"
    
    if script:
        script_path = find_script_path("generate_guided_conversation", scripts_dir)
        script_name = "generate_guided_conversation.py"
    else:
        script_path = find_script_path("conversation_engine", scripts_dir)
        script_name = "conversation_engine.py"
    
    if not script_path:
        print_error(
            "Conversation script not found",
            f"Expected: scripts/{script_name}"
        )
        raise typer.Abort()
    
    # Build command arguments
    cmd_args = [
        sys.executable,
        str(script_path),
        pattern,
    ]
    
    if max_attempts:
        cmd_args.extend(["--max-attempts", str(max_attempts)])
    
    if output:
        cmd_args.extend(["--output", output])
    
    # Run conversation script
    try:
        result = subprocess.run(
            cmd_args,
            cwd=kb_path,
            env={'GEMINI_API_KEY': api_key, **os.environ}
        )
        
        if result.returncode == 0:
            if script:
                print_success("Conversation script generated!")
        else:
            print_error("Conversation failed")
            raise typer.Abort()
            
    except KeyboardInterrupt:
        print_warning("\nConversation interrupted by user")
        raise typer.Abort()
    except Exception as e:
        print_error(f"Failed to run conversation: {e}")
        raise typer.Abort()
