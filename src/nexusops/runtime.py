from pathlib import Path
from uuid import uuid4

from nexusops.blueprints import load_blueprints
from nexusops.loops import choose_loop, load_loops
from nexusops.models import RunReport
from nexusops.settings import Settings
from nexusops.skills import load_skills, select_skills


class NexusRuntime:
    def __init__(self, settings: Settings) -> None:
        self.settings = settings

    def plan(self, goal: str) -> RunReport:
        skills = load_skills(self.settings.skills_dir)
        loops = load_loops(self.settings.loops_dir)
        blueprints = load_blueprints(self.settings.blueprints_dir)

        loop = choose_loop(goal, loops)
        preferred = []
        if loop:
            preferred_ids = set(loop.preferred_skills)
            preferred = [skill for skill in skills if skill.id in preferred_ids]

        selected = preferred or select_skills(goal, skills)
        blueprint = blueprints[0] if blueprints else None

        selection_reason = (
            f"Preferred skills from loop '{loop.id}' were used."
            if preferred and loop
            else "Skills were selected with lightweight keyword matching."
        )
        notes = [
            "Loaded dynamic skills from SKILL.md files.",
            "Selected loop specification with verifier and terminal states."
            if loop
            else "No loop specification found; using direct planning mode.",
            selection_reason,
            "Selected workflow blueprint." if blueprint else "No blueprint found.",
            "V1 is planning-only: tool execution and PR creation require later approval gates.",
        ]

        return RunReport(
            id=str(uuid4()),
            goal=goal,
            loop=loop,
            selected_skills=selected,
            blueprint=blueprint,
            notes=notes,
            artifacts={
                "model_roles": {
                    "default": self.settings.default_model,
                    "fast": self.settings.fast_model,
                    "router": self.settings.router_model,
                    "embedding": self.settings.embedding_model,
                },
                "selected_skill_ids": [skill.id for skill in selected],
                "selection_reason": selection_reason,
                "loaded_counts": {
                    "skills": len(skills),
                    "loops": len(loops),
                    "blueprints": len(blueprints),
                },
            },
        )

    def save_report(self, report: RunReport) -> Path:
        self.settings.runs_dir.mkdir(parents=True, exist_ok=True)
        path = self.settings.runs_dir / f"{report.id}.json"
        path.write_text(report.model_dump_json(indent=2), encoding="utf-8")
        return path
