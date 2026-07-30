# Public Roadmap

NexusOps is intentionally incremental. The goal is to keep each milestone useful and inspectable.

## M0: Runtime Skeleton

Status: current

- CLI
- config loading
- skill registry
- loop registry
- blueprint registry
- offline demo
- run listing and inspection
- JSON run reports
- tests and linting

## M1: Model-Backed Router

- OpenAI-compatible model provider
- structured routing output
- router evaluation fixtures
- fallback when no skill matches

## M2: MCP Filesystem Tool

- read-only filesystem MCP integration
- path allowlist
- file summaries
- source references in run reports

## M3: GitHub Issue Reader

- GitHub issue fetch
- issue classification
- repo context lookup
- draft triage response

## M4: Human Approval Queue

- approval objects
- CLI approval review
- policy checks for risky actions
- audit trail

## M5: Issue-to-Draft-PR Demo

- create isolated branch/workspace
- prepare a small docs/code change
- run tests
- review diff
- open draft PR after approval

## Later

- semantic skill routing
- local model support
- Phoenix/OpenTelemetry trace views
- dashboard
- plugin-like skill packages
