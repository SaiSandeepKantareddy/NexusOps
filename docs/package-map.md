# Package Map

NexusOps keeps the base install small and moves heavier integrations into optional extras.

## Core

- `pydantic`: strict schemas for skills, loops, blueprints, and run reports.
- `pydantic-settings`: `.env` and configuration loading.
- `typer`: CLI commands.
- `rich`: readable terminal output.
- `pyyaml`: loop and blueprint YAML.
- `python-dotenv`: local `.env` support through settings.
- local frontmatter parser: `SKILL.md` metadata.

Install:

```bash
pip install -e ".[dev]"
```

## Agents Extra

- `openai`: OpenAI-compatible hosted model endpoint.
- `openai-agents`: agents, handoffs, guardrails, MCP integration, sessions, tracing.

Install:

```bash
pip install -e ".[agents]"
```

## MCP Extra

- `mcp`: Model Context Protocol client/server primitives.
- `fastmcp`: faster MCP server development.

Install:

```bash
pip install -e ".[mcp]"
```

## GitHub Extra

- `PyGithub`: GitHub API.
- `GitPython`: local repository inspection.

Install:

```bash
pip install -e ".[github]"
```

## Storage Extra

- `sqlalchemy`: future run database.

Install:

```bash
pip install -e ".[storage]"
```

## Observability Extra

- `opentelemetry-sdk`: trace foundation.
- `opentelemetry-exporter-otlp`: trace export.
- `arize-phoenix`: local AI tracing and eval UI.
- `openinference-instrumentation-openai`: OpenAI tracing instrumentation.

Install:

```bash
pip install -e ".[observability]"
```

## Server Extra

- `fastapi`: future API.
- `uvicorn`: API server.
- `sse-starlette`: streaming run events.

Install:

```bash
pip install -e ".[server]"
```

## Quality

- `pytest`: tests.
- `ruff`: linting and formatting.
