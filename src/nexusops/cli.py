import typer
from rich.console import Console
from rich.table import Table

from nexusops.loops import load_loops
from nexusops.runtime import NexusRuntime
from nexusops.settings import get_settings
from nexusops.skills import load_skills

app = typer.Typer(help="NexusOps multi-agent runtime CLI.")
skills_app = typer.Typer(help="Inspect dynamic skills.")
loops_app = typer.Typer(help="Inspect loop engineering specs.")
app.add_typer(skills_app, name="skills")
app.add_typer(loops_app, name="loops")
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
def run(goal: str, save: bool = typer.Option(True, help="Write a JSON run report.")) -> None:
    """Plan a NexusOps run for a goal."""
    settings = get_settings()
    runtime = NexusRuntime(settings)
    report = runtime.plan(goal)

    console.print(f"[bold]Run:[/bold] {report.id}")
    console.print(f"[bold]Goal:[/bold] {report.goal}")
    if report.loop:
        console.print(f"[bold]Loop:[/bold] {report.loop.name} ({report.loop.id})")
    console.print("[bold]Selected skills:[/bold] " + ", ".join(skill.id for skill in report.selected_skills))
    for note in report.notes:
        console.print(f"- {note}")

    if save:
        path = runtime.save_report(report)
        console.print(f"[green]Saved run report:[/green] {path}")


if __name__ == "__main__":
    app()
