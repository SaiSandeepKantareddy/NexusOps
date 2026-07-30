# NexusOps

NexusOps is an early-stage learning project for building a GitHub-native agent runtime.

The goal is to make modern AI engineering patterns visible and approachable: skill-based agents, loop engineering, MCP-ready tool access, human approval, evaluation gates, and traceable runs.

It is intentionally small right now. The first version focuses on the runtime skeleton before adding real tool execution.

## Current Status

**Works today**

- Loads dynamic `SKILL.md` files from `skills/`
- Loads loop specs from `loops/*.yaml`
- Loads workflow blueprints from `blueprints/*.yaml`
- Selects relevant skills for a goal
- Produces a JSON run report
- Provides a small CLI for exploring the runtime
- Includes tests and linting

**Planned next**

- Model-backed routing and planning
- MCP filesystem and GitHub tools
- Human approval queue
- Evaluator checks
- GitHub issue-to-draft-PR workflow
- Phoenix/OpenTelemetry run traces
- Optional dashboard

## Why This Exists

Most AI coding starts like this:

```text
prompt -> response
```

Useful agent systems need more structure:

```text
goal -> context -> skills -> tools -> loop -> verification -> approval -> artifact
```

NexusOps is a reference project for learning that second pattern.

## Architecture Sketch

```text
CLI Goal / GitHub Issue
        |
        v
Nexus Runtime
        |
        +--> Skill Registry       skills/*/SKILL.md
        +--> Loop Registry        loops/*.yaml
        +--> Blueprint Registry   blueprints/*.yaml
        +--> Model Provider       OpenAI-compatible APIs
        +--> Tool Layer           MCP / GitHub / filesystem
        +--> Evaluator Gates      tests / schemas / review
        |
        v
Run Report / Draft Plan / Future PR
```

## Quick Start

NexusOps targets Python 3.12+.

Start with the lightweight learning environment. It installs the core CLI, tests,
and linting tools only.

```bash
conda env create -f environment-lite.yml
conda activate nexusops-lite
cp .env.example .env
nexus doctor
nexus demo
nexus skills list
nexus loops list
nexus run "Draft a plan to add GitHub issue triage automation"
nexus runs list
```

If you already have Python 3.12 active, the equivalent pip install is:

```bash
python -m pip install -e ".[dev]"
```

For the full experimental stack with model clients, MCP, GitHub, observability,
server, and storage dependencies:

```bash
conda env create -f environment.yml
conda activate nexusops
```

Or install the full extras into an existing environment:

```bash
python -m pip install -e ".[dev,agents,github,mcp,observability,server,storage]"
```

When running tests with the full observability stack, disable third-party pytest
plugin autoload so optional services do not start during unit tests:

```bash
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 pytest
```

Phoenix should store state inside the project:

```bash
export PHOENIX_WORKING_DIR=runs/phoenix
```

## Example Output

```text
NexusOps Demo
This offline demo loads skills, loops, and blueprints, selects a workflow, and writes a traceable run report. No model call or API key is required.

Run: 0404bed7-9e59-4567-8c37-edd432a77e60
Goal: Draft a plan to add GitHub issue triage automation
Loop: GitHub Issue Triage Loop (github_issue_triage)
Blueprint: Hermes-Inspired Repo Operations Blueprint (hermes_repo_ops)
Selected skills: planner, reader, writer
- Loaded dynamic skills from SKILL.md files.
- Selected loop specification with verifier and terminal states.
- Preferred skills from loop 'github_issue_triage' were used.
- Selected workflow blueprint.
- V1 is planning-only: tool execution and PR creation require later approval gates.
Saved run report: runs/0404bed7-9e59-4567-8c37-edd432a77e60.json
```

## Project Layout

```text
src/nexusops/        Python package and CLI
skills/              Dynamic agent capabilities
loops/               Loop engineering specs
blueprints/          Workflow blueprints
docs/                Architecture and spec notes
examples/            Guided examples
tests/               Unit tests for loaders and runtime basics
environment-lite.yml Lightweight first-run environment
environment.yml      Full experimental development environment
```

## Documentation

- [Architecture](docs/architecture.md)
- [Package Map](docs/package-map.md)
- [Skill Spec](docs/skill-spec.md)
- [Loop Spec](docs/loop-spec.md)
- [Public Roadmap](docs/public-roadmap.md)
- [First Run Example](examples/first-run.md)
- [Skill Authoring Example](examples/skill-authoring.md)

## Roadmap

```text
M0: Runtime skeleton
M1: Model-backed router
M2: MCP filesystem tool
M3: GitHub issue reader
M4: Human approval queue
M5: Issue-to-draft-PR demo
```

## Safety

NexusOps is designed around governed autonomy. The project should prefer proposing, reviewing, and approving work before taking risky actions such as writing files, installing packages, pushing commits, opening pull requests, or using secrets.

See [SECURITY.md](SECURITY.md).

## License

MIT. See [LICENSE](LICENSE).
