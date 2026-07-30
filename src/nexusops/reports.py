from pathlib import Path

from nexusops.models import RunReport


def load_report(path: Path) -> RunReport:
    return RunReport.model_validate_json(path.read_text(encoding="utf-8"))


def list_report_paths(runs_dir: Path) -> list[Path]:
    if not runs_dir.exists():
        return []
    return sorted(runs_dir.glob("*.json"), key=lambda path: path.stat().st_mtime, reverse=True)
