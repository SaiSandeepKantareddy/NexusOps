# First Run

After setup, run:

```bash
nexus doctor
nexus skills list
nexus loops list
nexus run "Draft a plan to add GitHub issue triage automation"
```

Expected shape:

```text
Run: <uuid>
Goal: Draft a plan to add GitHub issue triage automation
Loop: GitHub Issue Triage Loop (github_issue_triage)
Selected skills: planner, reader, writer
- Loaded dynamic skills from SKILL.md files.
- Selected loop specification with verifier and terminal states.
- Selected Hermes-inspired blueprint.
- V1 is planning-only: tool execution and PR creation require later approval gates.
Saved run report: runs/<uuid>.json
```

The run report is ignored by git because it is local execution state.
