# Contributing

## Add A New Agent

Create a new folder under `agents/<category>/<agent-name>/` and include:

- `README.md` with purpose, best-fit tasks, and sample inputs
- `SOUL.md` with the actual OpenClaw agent instructions

Use `kebab-case` for folder names such as `sales-prospect-researcher`.

Base new `SOUL.md` files on [templates/SOUL.template.md](templates/SOUL.template.md).

Update `agents.json` with the new agent metadata, then run:

```bash
python3 scripts/generate_catalog.py --rewrite-json --write
```

## Quality Bar

- Keep the agent focused on one job
- Prefer concrete steps and output formats
- Avoid tool assumptions that are not stated
- Write prompts that can be reused without project-specific secrets
- Keep the standard sections in the same order across agents

## Updating Existing Agents

- Improve instructions without making the agent bloated
- Keep behavior predictable
- Document meaningful scope changes in the agent `README.md`
- Update `agents.json` when you add, remove, or rename an agent
- Re-run `python3 scripts/generate_catalog.py --rewrite-json --write` after metadata changes

## Pull Requests

Open a focused pull request that explains:

- what agent was added or changed
- why the change is useful
- how you verified the prompt is coherent
