# Skill Spec

Skills describe reusable capabilities that the runtime can discover without changing orchestrator code.

Each skill lives in its own folder:

```text
skills/
  reader/
    SKILL.md
```

## Frontmatter

```yaml
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
```

## Body

The Markdown body should explain:

- when the skill should be used
- what it is responsible for
- what it should not do
- expected output shape
- safety notes

## Risk Levels

```text
low      summarize, classify, plan, draft
medium   propose file changes, inspect diffs, run checks
high     write files, install packages, push commits, open PRs, access secrets
```

High-risk skills should propose actions first and require human approval before activation or execution.
