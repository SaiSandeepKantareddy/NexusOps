from __future__ import annotations

from pathlib import Path

import yaml

from nexusops.models import Blueprint


def load_blueprint(path: Path) -> Blueprint:
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    if "id" not in data:
        data["id"] = path.stem
    return Blueprint(**data)


def load_blueprints(blueprints_dir: Path) -> list[Blueprint]:
    if not blueprints_dir.exists():
        return []
    return [load_blueprint(path) for path in sorted(blueprints_dir.glob("*.yaml"))]
