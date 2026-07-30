from __future__ import annotations

from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    openai_base_url: str = Field(default="https://api.openai.com/v1", alias="OPENAI_BASE_URL")
    openai_api_key: str | None = Field(default=None, alias="OPENAI_API_KEY")

    default_model: str = Field(default="gpt-4.1", alias="NEXUSOPS_DEFAULT_MODEL")
    fast_model: str = Field(default="gpt-4.1-mini", alias="NEXUSOPS_FAST_MODEL")
    router_model: str = Field(default="gpt-4.1-mini", alias="NEXUSOPS_ROUTER_MODEL")
    embedding_model: str = Field(default="text-embedding-3-small", alias="NEXUSOPS_EMBEDDING_MODEL")

    skills_dir: Path = Field(default=Path("skills"), alias="NEXUSOPS_SKILLS_DIR")
    loops_dir: Path = Field(default=Path("loops"), alias="NEXUSOPS_LOOPS_DIR")
    blueprints_dir: Path = Field(default=Path("blueprints"), alias="NEXUSOPS_BLUEPRINTS_DIR")
    runs_dir: Path = Field(default=Path("runs"), alias="NEXUSOPS_RUNS_DIR")


def get_settings() -> Settings:
    return Settings()
