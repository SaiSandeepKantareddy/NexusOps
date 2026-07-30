from pathlib import Path

from nexusops.loops import load_loops
from nexusops.reports import list_report_paths, load_report
from nexusops.skills import load_skills, select_skills

ROOT = Path(__file__).resolve().parents[1]


def test_load_skills() -> None:
    skills = load_skills(ROOT / "skills")
    ids = {skill.id for skill in skills}
    assert {"reader", "writer", "planner", "reviewer", "skill-builder"} <= ids


def test_select_skills() -> None:
    skills = load_skills(ROOT / "skills")
    selected = select_skills("read repo context and write a plan", skills, limit=2)
    assert selected
    assert len(selected) <= 2


def test_load_loops() -> None:
    loops = load_loops(ROOT / "loops")
    assert {loop.id for loop in loops} >= {"github_issue_triage", "repo_change_plan"}


def test_report_listing(tmp_path: Path) -> None:
    source = ROOT / "runs"
    assert list_report_paths(tmp_path) == []
    if source.exists():
        for path in list_report_paths(source):
            report = load_report(path)
            assert report.id
            break
