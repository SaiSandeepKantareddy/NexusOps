from __future__ import annotations

from pathlib import Path
from typing import Optional

import yaml

from nexusops.models import LoopSpec


def load_loop(path: Path) -> LoopSpec:
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    if "id" not in data:
        data["id"] = path.stem
    return LoopSpec(**data)


def load_loops(loops_dir: Path) -> list[LoopSpec]:
    if not loops_dir.exists():
        return []
    return [load_loop(path) for path in sorted(loops_dir.glob("*.yaml"))]


def choose_loop(goal: str, loops: list[LoopSpec]) -> Optional[LoopSpec]:
    if not loops:
        return None
    goal_lower = goal.lower()
    for loop in loops:
        if loop.id.replace("_", " ") in goal_lower or loop.name.lower() in goal_lower:
            return loop
    return loops[0]
