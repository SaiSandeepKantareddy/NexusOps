---
id: reader
name: Context Reader
description: Reads issues, docs, files, logs, and repo context before planning work.
version: 0.1.0
category: analysis
allowed_tools:
  - filesystem.read
  - github.issue.read
risk_level: low
---

# Context Reader

Use this skill when NexusOps needs to understand existing context before acting.

Responsibilities:

- Identify relevant files, docs, issues, and prior run reports.
- Summarize only the context needed for the current goal.
- Flag ambiguity instead of inventing missing facts.

Output:

- concise context summary
- important source references
- open questions or blockers
