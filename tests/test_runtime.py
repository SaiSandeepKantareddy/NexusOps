from pathlib import Path

from nexusops.runtime import NexusRuntime
from nexusops.settings import Settings

ROOT = Path(__file__).resolve().parents[1]


def test_runtime_plan_selects_context() -> None:
    settings = Settings(
        NEXUSOPS_SKILLS_DIR=ROOT / "skills",
        NEXUSOPS_LOOPS_DIR=ROOT / "loops",
        NEXUSOPS_BLUEPRINTS_DIR=ROOT / "blueprints",
        NEXUSOPS_RUNS_DIR=ROOT / "runs",
    )
    report = NexusRuntime(settings).plan("Plan a repo change")
    assert report.goal == "Plan a repo change"
    assert report.selected_skills
    assert report.loop is not None
    assert report.blueprint is not None
    assert report.artifacts["loaded_counts"]["skills"] >= 1
    assert report.artifacts["selected_skill_ids"]


def test_runtime_save_and_load_report(tmp_path: Path) -> None:
    settings = Settings(
        NEXUSOPS_SKILLS_DIR=ROOT / "skills",
        NEXUSOPS_LOOPS_DIR=ROOT / "loops",
        NEXUSOPS_BLUEPRINTS_DIR=ROOT / "blueprints",
        NEXUSOPS_RUNS_DIR=tmp_path,
    )
    runtime = NexusRuntime(settings)
    report = runtime.plan("Plan a repo change")
    path = runtime.save_report(report)

    assert path.exists()
    assert path.parent == tmp_path
