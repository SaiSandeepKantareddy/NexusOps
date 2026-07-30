from __future__ import annotations

from datetime import UTC, datetime
from pathlib import Path
from typing import Any, Literal

from pydantic import BaseModel, Field


class Skill(BaseModel):
    id: str
    name: str
    description: str
    version: str = "0.1.0"
    category: str = "general"
    allowed_tools: list[str] = Field(default_factory=list)
    risk_level: Literal["low", "medium", "high"] = "low"
    source_path: Path
    instructions: str


class LoopSpec(BaseModel):
    id: str
    name: str
    trigger: str
    goal: str
    verifier: str
    max_retries: int = 3
    human_approval_required: bool = True
    preferred_skills: list[str] = Field(default_factory=list)
    terminal_states: list[str] = Field(default_factory=lambda: ["completed", "blocked", "needs_approval"])


class BlueprintStep(BaseModel):
    id: str
    agent: str
    purpose: str
    expected_output: str


class Blueprint(BaseModel):
    id: str
    name: str
    description: str
    steps: list[BlueprintStep]


class RunReport(BaseModel):
    id: str
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
    goal: str
    loop: LoopSpec | None = None
    selected_skills: list[Skill] = Field(default_factory=list)
    blueprint: Blueprint | None = None
    status: Literal["planned", "completed", "blocked", "needs_approval"] = "planned"
    notes: list[str] = Field(default_factory=list)
    artifacts: dict[str, Any] = Field(default_factory=dict)
