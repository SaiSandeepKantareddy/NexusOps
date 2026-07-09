# NexusOps

NexusOps is a GitHub-native multi-agent runtime for learning and demonstrating modern agent engineering.

It is not a chatbot. It is a small, inspectable agent operating system:

- **Loop engineering**: reusable loops with triggers, goals, verifiers, retry limits, and stopping rules.
- **Skill-based scaling**: OpenClaw-style `SKILL.md` capabilities loaded dynamically from `skills/`.
- **Hermes-inspired blueprints**: structured specialist workflows in `blueprints/`.
- **MCP-ready tools**: designed around standard tool/data access rather than one-off integrations.
- **Human-governed autonomy**: agents can propose and prepare; risky actions require approval.
- **Observable runs**: every run produces a traceable JSON report.

## Why Build This?

The shift in engineering is from:

```text
prompt -> response
```

to:

```text
runtime -> skills -> tools -> memory -> loops -> verification -> traces -> approval -> artifacts
```

NexusOps is a learning project for that second world.

## Model Setup

Create a `.env` file:

```env
OPENAI_BASE_URL=https://azure.agentslab.host/v1
OPENAI_API_KEY=your_key_here

NEXUSOPS_DEFAULT_MODEL=Kimi-K2.6
NEXUSOPS_FAST_MODEL=gpt-5.4-mini
NEXUSOPS_ROUTER_MODEL=grok-4-fast-non-reasoning
NEXUSOPS_EMBEDDING_MODEL=text-embedding-3-small
```

## First Commands

```bash
conda create -n nexusops python=3.12 -y
conda activate nexusops
conda install cryptography -y
pip install -e ".[dev,observability,server]"
nexus doctor
nexus skills list
nexus loops list
nexus run "Draft a plan to add GitHub issue triage automation"
```

NexusOps targets Python 3.12+. The MCP packages are part of the main install. Server/dashboard dependencies are optional:

```bash
pip install -e ".[server]"
```

For the full local development environment used by this repo:

```bash
conda env create -f environment.yml
conda activate nexusops
```

When running tests in the full environment, disable third-party pytest plugin autoload so optional observability packages do not start services during unit tests:

```bash
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 pytest
```

Phoenix should store state inside the repo:

```bash
export PHOENIX_WORKING_DIR=runs/phoenix
```

The first V1 runtime is intentionally conservative: it loads skills, selects relevant capabilities, records the loop context, and writes a run report. Tool execution, GitHub PR creation, MCP servers, and sandboxed coding arrive as explicit milestones.

## Project Layout

```text
src/nexusops/        Python package and CLI
skills/              Dynamic agent capabilities
loops/               Loop engineering specs
blueprints/          Hermes-inspired workflow blueprints
docs/                Architecture and learning notes
runs/                Local run reports, ignored by git
tests/               Unit tests for loaders and runtime basics
```

## Roadmap

1. CLI, config, skill registry, loop registry, run reports.
2. Hosted model calls through OpenAI-compatible endpoint.
3. Semantic skill routing using embeddings.
4. MCP filesystem and GitHub tools.
5. Planner, coder, tester, reviewer handoffs.
6. Human approval queue.
7. Phoenix/OpenTelemetry traces.
8. GitHub issue-to-draft-PR workflow.
9. Dashboard for runs, skills, traces, costs, and approvals.
