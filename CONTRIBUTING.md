# Contributing

Thanks for your interest in NexusOps.

NexusOps is early, so the best contributions are small, clear, and easy to review.

## Good First Contributions

- Improve documentation and examples.
- Add tests for skill, loop, or blueprint loading.
- Propose a new `SKILL.md` example.
- Improve CLI output.
- Add safety checks around future tool execution.

## Local Setup

```bash
conda env create -f environment.yml
conda activate nexusops
cp .env.example .env
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 pytest
ruff check .
```

## Contribution Guidelines

- Keep changes focused.
- Add or update tests when behavior changes.
- Keep risky automation behind explicit approval gates.
- Do not commit secrets, API keys, run reports, local envs, or generated caches.
- Prefer clear docs over hype.

## Pull Request Checklist

- [ ] Tests pass.
- [ ] `ruff check .` passes.
- [ ] Public docs are updated if behavior changed.
- [ ] New automation has an approval or safety story.
