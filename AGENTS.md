# Repository Guidelines

## Project Structure & Module Organization
This repository is an OpenClaw agent catalog. Keep the root focused on repository docs and indexes, and place reusable agent content under `agents/`:

- `agents/<category>/<agent>/SOUL.md` for the core prompt
- `agents/<category>/<agent>/README.md` for scope, inputs, and usage notes
- `agents/<category>/README.md` for category-level navigation
- `templates/SOUL.template.md` for new agent authoring
- `agents.json` for the machine-readable catalog

Use `kebab-case` for category and agent folder names, for example `agents/security/access-audit-analyst/`. Current top-level categories include `automation`, `browser`, `business`, `content`, `data`, `developer`, `finance`, `marketing`, `multi-agent`, `operations`, `product`, `productivity`, `research`, `security`, and `support`.

## Build, Test, and Development Commands
There is no build system in this repository. Use simple shell checks to validate structure and consistency:

- `git status` checks the current workspace before making changes.
- `rg --files agents` lists all agent files.
- `find agents -name 'SOUL.md' | wc -l` verifies the total number of agents.
- `sed -n '1,120p' agents/<category>/<agent>/SOUL.md` reviews prompt structure quickly.

## Coding Style & Naming Conventions
Use short, direct Markdown. Keep headings consistent across agents. Every `SOUL.md` should follow the shared section order: `Role`, `Mission`, `Best For`, `Expected Inputs`, `Operating Principles`, `Workflow`, `Output Format`, `Success Criteria`, `Guardrails`. Use 2-space indentation in JSON and keep file and directory names in `kebab-case`.

## Testing Guidelines
There is no automated test framework yet. Validate contributions by checking that each new agent folder contains both `README.md` and `SOUL.md`, that each category keeps a current `agents/<category>/README.md`, that `agents.json` is updated, and that the prompt reads coherently end to end. When changing multiple agents, spot-check category listings in the root [README.md](README.md).

## Commit & Pull Request Guidelines
Use focused, imperative commits such as `feat: add finance agent set` or `docs: standardize soul template`. Pull requests should state which categories or agents changed, why the addition is useful, and what structural checks you ran. If you changed the template or repository conventions, mention the migration impact clearly.
