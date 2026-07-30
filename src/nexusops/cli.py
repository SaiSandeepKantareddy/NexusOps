from pathlib import Path

import typer
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from nexusops.loops import load_loops
from nexusops.reports import list_report_paths, load_report
from nexusops.runtime import NexusRuntime
from nexusops.settings import get_settings
from nexusops.skills import load_skills

app = typer.Typer(help="NexusOps multi-agent runtime CLI.")
skills_app = typer.Typer(help="Inspect dynamic skills.")
loops_app = typer.Typer(help="Inspect loop engineering specs.")
runs_app = typer.Typer(help="Inspect saved run reports.")
app.add_typer(skills_app, name="skills")
app.add_typer(loops_app, name="loops")
app.add_typer(runs_app, name="runs")
console = Console()


@app.command()
def doctor() -> None:
    """Show local configuration and readiness."""
    settings = get_settings()
    table = Table(title="NexusOps Doctor")
    table.add_column("Setting")
    table.add_column("Value")
    table.add_row("base_url", settings.openai_base_url)
    table.add_row("api_key", "set" if settings.openai_api_key else "missing")
    table.add_row("default_model", settings.default_model)
    table.add_row("router_model", settings.router_model)
    table.add_row("embedding_model", settings.embedding_model)
    table.add_row("skills_dir", str(settings.skills_dir))
    table.add_row("loops_dir", str(settings.loops_dir))
    table.add_row("runs_dir", str(settings.runs_dir))
    console.print(table)


@skills_app.command("list")
def list_skills() -> None:
    """List discovered SKILL.md capabilities."""
    settings = get_settings()
    skills = load_skills(settings.skills_dir)
    table = Table(title="Discovered Skills")
    table.add_column("ID")
    table.add_column("Name")
    table.add_column("Risk")
    table.add_column("Description")
    for skill in skills:
        table.add_row(skill.id, skill.name, skill.risk_level, skill.description)
    console.print(table)


@loops_app.command("list")
def list_loops() -> None:
    """List loop engineering specs."""
    settings = get_settings()
    loops = load_loops(settings.loops_dir)
    table = Table(title="Loop Specs")
    table.add_column("ID")
    table.add_column("Trigger")
    table.add_column("Verifier")
    table.add_column("Approval")
    for loop in loops:
        table.add_row(loop.id, loop.trigger, loop.verifier, str(loop.human_approval_required))
    console.print(table)


@app.command()
def demo() -> None:
    """Run an offline guided demo with no API key required."""
    goal = "Draft a plan to add GitHub issue triage automation"
    settings = get_settings()
    runtime = NexusRuntime(settings)
    report = runtime.plan(goal)
    path = runtime.save_report(report)

    console.print(
        Panel.fit(
            "This offline demo loads skills, loops, and blueprints, selects a workflow, "
            "and writes a traceable run report. No model call or API key is required.",
            title="NexusOps Demo",
        )
    )
    render_report_summary(report)
    console.print(f"[green]Saved run report:[/green] {path}")
    console.print("[bold]Next:[/bold] run `nexus runs show " + report.id + "`")


@app.command()
def run(goal: str, save: bool = typer.Option(True, help="Write a JSON run report.")) -> None:
    """Plan a NexusOps run for a goal."""
    settings = get_settings()
    runtime = NexusRuntime(settings)
    report = runtime.plan(goal)

    render_report_summary(report)

    if save:
        path = runtime.save_report(report)
        console.print(f"[green]Saved run report:[/green] {path}")


@runs_app.command("list")
def list_runs() -> None:
    """List saved run reports."""
    settings = get_settings()
    paths = list_report_paths(settings.runs_dir)
    table = Table(title="Run Reports")
    table.add_column("ID")
    table.add_column("Status")
    table.add_column("Goal")
    table.add_column("Path")
    for path in paths:
        report = load_report(path)
        table.add_row(report.id, report.status, report.goal, str(path))
    console.print(table)


@runs_app.command("show")
def show_run(run_id: str) -> None:
    """Show a saved run report by id or path."""
    settings = get_settings()
    path = settings.runs_dir / f"{run_id}.json"
    if not path.exists():
        candidate = Path(run_id)
        path = candidate if candidate.exists() else path
    if not path.exists():
        raise typer.BadParameter(f"Run report not found: {run_id}")

    report = load_report(path)
    render_report_summary(report)
    console.print_json(report.model_dump_json(indent=2))


def render_report_summary(report) -> None:
    console.print(f"[bold]Run:[/bold] {report.id}")
    console.print(f"[bold]Goal:[/bold] {report.goal}")
    if report.loop:
        console.print(f"[bold]Loop:[/bold] {report.loop.name} ({report.loop.id})")
    if report.blueprint:
        console.print(f"[bold]Blueprint:[/bold] {report.blueprint.name} ({report.blueprint.id})")
    console.print("[bold]Selected skills:[/bold] " + ", ".join(skill.id for skill in report.selected_skills))
    for note in report.notes:
        console.print(f"- {note}")


if __name__ == "__main__":
    app()
