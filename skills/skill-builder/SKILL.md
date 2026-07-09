---
id: skill-builder
name: Skill Builder
description: Proposes new SKILL.md capabilities when the runtime lacks a needed skill.
version: 0.1.0
category: self-improvement
allowed_tools:
  - filesystem.write_proposal
risk_level: high
---

# Skill Builder

Use this skill when NexusOps needs a new reusable capability.

Important safety rule:

- This skill may only propose new skills.
- A human must approve before a proposed skill is activated.

Output:

- proposed SKILL.md
- reason the skill is needed
- tools requested
- safety and abuse considerations
