from pathlib import Path
from typing import Any

import yaml

from nexusops.models import Skill


def _metadata_value(metadata: dict[str, Any], key: str, default: Any = None) -> Any:
    value = metadata.get(key, default)
    return default if value is None else value


def load_skill(path: Path) -> Skill:
    metadata, content = parse_skill_markdown(path.read_text(encoding="utf-8"))
    skill_id = _metadata_value(metadata, "id", path.parent.name)
    return Skill(
        id=skill_id,
        name=_metadata_value(metadata, "name", skill_id.replace("-", " ").title()),
        description=_metadata_value(metadata, "description", ""),
        version=_metadata_value(metadata, "version", "0.1.0"),
        category=_metadata_value(metadata, "category", "general"),
        allowed_tools=list(_metadata_value(metadata, "allowed_tools", [])),
        risk_level=_metadata_value(metadata, "risk_level", "low"),
        source_path=path,
        instructions=content.strip(),
    )


def parse_skill_markdown(markdown: str) -> tuple[dict[str, Any], str]:
    if not markdown.startswith("---"):
        return {}, markdown

    parts = markdown.split("---", 2)
    if len(parts) < 3:
        return {}, markdown

    metadata = yaml.safe_load(parts[1]) or {}
    return metadata, parts[2]


def load_skills(skills_dir: Path) -> list[Skill]:
    if not skills_dir.exists():
        return []
    skill_files = sorted(skills_dir.glob("*/SKILL.md"))
    return [load_skill(path) for path in skill_files]


def select_skills(goal: str, skills: list[Skill], limit: int = 3) -> list[Skill]:
    goal_terms = {term.strip(".,:;!?()[]{}").lower() for term in goal.split()}
    scored: list[tuple[int, Skill]] = []
    for skill in skills:
        haystack = " ".join([skill.id, skill.name, skill.description, skill.category]).lower()
        score = sum(1 for term in goal_terms if term and term in haystack)
        scored.append((score, skill))

    scored.sort(key=lambda item: (item[0], item[1].id), reverse=True)
    selected = [skill for score, skill in scored if score > 0][:limit]
    return selected or skills[:limit]
