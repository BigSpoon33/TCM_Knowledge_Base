import typer
from capsule.utils.validation import run_validation, generate_report
from capsule.utils.output import console

app = typer.Typer()


@app.command()
def validate(
    report: bool = typer.Option(
        False,
        "--report",
        "-r",
        help="Generate a markdown validation report.",
    ),
):
    """
    Run validation checks on the project.

    Performs the following integrity checks:
    1. File Inventory: Checks for missing or unexpected files in the capsule directory.
    2. Schema Validation: Validates capsule-cypher.yaml against the required schema.
    3. Encoding Check: Ensures all text files are UTF-8 or ASCII encoded.

    Returns a summary of errors if any are found.
    """
    console.print("Running validation checks...")
    results = run_validation()

    if report:
        report_path = generate_report(results)
        console.print(f"Validation report generated at: [bold green]{report_path}[/bold green]")
    else:
        # Print a summary to the console
        total_errors = sum(len(result.get("errors", [])) for result in results.values())
        if total_errors > 0:
            console.print(f"[bold red]Validation Failed! Found {total_errors} errors.[/bold red]")
            # Optionally, print more details here
        else:
            console.print("[bold green]Validation Passed![/bold green]")


if __name__ == "__main__":
    app()
