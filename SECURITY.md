# Security Policy

NexusOps is an early-stage agent runtime. Treat it as experimental software.

## Supported Versions

Only the latest `main` branch is currently supported.

## Reporting a Vulnerability

Please open a GitHub issue with a clear description if the report is safe to discuss publicly.

If the issue involves secrets, credential exposure, or a dangerous execution path, do not include sensitive data in the issue. Instead, provide a minimal description and request a private disclosure path.

## Safety Principles

NexusOps should default to governed autonomy:

- Read-only actions are lower risk.
- File writes should be scoped and reviewable.
- Shell commands should be allowlisted or approval-gated.
- Package installation should require approval.
- Git pushes and pull request creation should require approval.
- Secrets should never be written to logs, traces, run reports, or examples.
- Future tool execution should prefer sandboxed workspaces.

## Current Limitations

The current version is planning-only. It loads skills, loops, and blueprints, then writes run reports. Real MCP tool execution, GitHub mutation, and sandboxed coding are planned milestones and should be added with tests and approval gates.
