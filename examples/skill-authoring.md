# Skill Authoring

To add a new capability, create a folder under `skills/` with a `SKILL.md` file.

Example:

```text
skills/docs-auditor/SKILL.md
```

```markdown
---
id: docs-auditor
name: Docs Auditor
description: Reviews documentation for missing setup steps, unclear commands, and outdated examples.
version: 0.1.0
category: documentation
allowed_tools:
  - filesystem.read
risk_level: low
---

# Docs Auditor

Use this skill when a goal involves improving project documentation.

Responsibilities:

- Read the relevant docs.
- Identify unclear or missing setup steps.
- Suggest concise improvements.
- Avoid changing files directly unless a human approves a write action.

Output:

- findings
- suggested edits
- confidence level
```

Then run:

```bash
nexus skills list
```

The runtime should discover the new skill without orchestrator code changes.
