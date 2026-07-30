# Loop Spec

Loops define repeatable work patterns around an agent runtime.

Each loop is a YAML file:

```text
loops/
  github_issue_triage.yaml
```

## Example

```yaml
id: github_issue_triage
name: GitHub Issue Triage Loop
trigger: github_issue_label:nexusops:triage
goal: Read a GitHub issue, classify it, identify needed skills, and draft a response or plan.
verifier: issue_summary_has_sources_and_next_action
max_retries: 2
human_approval_required: true
preferred_skills:
  - reader
  - planner
  - writer
terminal_states:
  - completed
  - needs_approval
  - blocked
```

## Fields

- `id`: stable machine-readable loop id
- `name`: human-readable name
- `trigger`: event or command that starts the loop
- `goal`: target outcome
- `verifier`: check that decides whether the loop succeeded
- `max_retries`: retry budget before escalation
- `human_approval_required`: whether risky output needs approval
- `preferred_skills`: skills the runtime should prefer
- `terminal_states`: allowed end states

## Design Notes

Good loops are narrow. They should define a clear goal, a clear stopping rule, and a clear escalation path.
