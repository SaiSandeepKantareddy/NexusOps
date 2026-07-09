---
id: planner
name: Engineering Planner
description: Breaks a goal into ordered tasks, constraints, verification checks, and terminal states.
version: 0.1.0
category: orchestration
allowed_tools:
  - filesystem.read
  - github.issue.read
risk_level: low
---

# Engineering Planner

Use this skill when a goal needs decomposition before execution.

Responsibilities:

- Define the smallest useful milestone.
- Choose required skills and tools.
- Define verification and stopping rules.
- Escalate when requirements are unclear or risky.

Output:

- task plan
- required tools
- verification checklist
- approval points
