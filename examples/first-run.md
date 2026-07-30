# First Run

Create the lightweight learning environment first:

```bash
conda env create -f environment-lite.yml
conda activate nexusops-lite
cp .env.example .env
```

Then run:

```bash
nexus doctor
nexus demo
nexus skills list
nexus loops list
nexus run "Draft a plan to add GitHub issue triage automation"
nexus runs list
```

Expected shape:

```text
NexusOps Demo
This offline demo loads skills, loops, and blueprints, selects a workflow, and writes a traceable run report. No model call or API key is required.

Run: <uuid>
Goal: Draft a plan to add GitHub issue triage automation
Loop: GitHub Issue Triage Loop (github_issue_triage)
Blueprint: Hermes-Inspired Repo Operations Blueprint (hermes_repo_ops)
Selected skills: planner, reader, writer
- Loaded dynamic skills from SKILL.md files.
- Selected loop specification with verifier and terminal states.
- Preferred skills from loop 'github_issue_triage' were used.
- Selected workflow blueprint.
- V1 is planning-only: tool execution and PR creation require later approval gates.
Saved run report: runs/<uuid>.json
```

The run report is ignored by git because it is local execution state.

Inspect it with:

```bash
nexus runs show <uuid>
```
