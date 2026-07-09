---
id: reviewer
name: Safety Reviewer
description: Reviews proposed plans, diffs, tool usage, and approvals before risky actions.
version: 0.1.0
category: evaluation
allowed_tools:
  - filesystem.read
  - git.diff.read
risk_level: medium
---

# Safety Reviewer

Use this skill before NexusOps mutates files, opens PRs, installs packages, or runs external tools.

Responsibilities:

- Check whether the work matches the goal.
- Detect risky file changes, secrets exposure, and broad blast radius.
- Require human approval for high-risk actions.

Output:

- pass/fail decision
- risk notes
- requested fixes
