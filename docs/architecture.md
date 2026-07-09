# NexusOps Architecture

NexusOps is built around five concepts.

## 1. Runtime

The runtime owns state, selected loop, selected skills, run reports, and future tool dispatch.

## 2. Loops

Loops define reusable automation patterns:

- trigger
- goal
- verifier
- max retries
- approval requirement
- terminal states

This is the project's loop engineering layer.

## 3. Skills

Skills are capability packages loaded from `skills/*/SKILL.md`.

They describe when to use a capability, what tools it can request, and what output it should produce.

## 4. Blueprints

Blueprints are Hermes-inspired workflow skeletons. They make specialist chains explicit and explainable.

## 5. Guardrails

The runtime starts conservative:

- planning is allowed
- risky actions require approval
- tool execution is added behind policies
- every run writes a report
