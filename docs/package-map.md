# Package Map

## Core

- `pydantic`: strict schemas for skills, loops, blueprints, run reports.
- `pydantic-settings`: `.env` and configuration loading.
- `typer`: CLI commands.
- `rich`: readable terminal output.
- `pyyaml`: loop and blueprint YAML.
- local frontmatter parser: `SKILL.md` metadata.

## Agents

- `openai`: OpenAI-compatible hosted model endpoint.
- `openai-agents`: agents, handoffs, guardrails, MCP integration, sessions, tracing.

## Tooling

- `mcp` and `fastmcp`: MCP client/server integration.
- `PyGithub`: GitHub API.
- `GitPython`: local repo inspection.

## Storage and Tracing

- `sqlalchemy`: future run database.
- `opentelemetry-sdk`: trace foundation.
- `opentelemetry-exporter-otlp`: trace export.

## Quality

- `pytest`: tests.
- `ruff`: linting and formatting.
