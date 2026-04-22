# Awesome Agents

A curated collection of OpenClaw-ready agents organized by category and centered on reusable `SOUL.md` files.

This project takes structural cues from community agent collections while keeping the repository simple: one folder per agent, one `SOUL.md` as the primary prompt, and one short `README.md` that explains when to use it.

## Repository Layout

```text
agents/<category>/<agent>/
  README.md
  SOUL.md

templates/
  SOUL.template.md

agents.json
```

- `SOUL.md` is the main OpenClaw prompt.
- `README.md` summarizes scope, inputs, and ideal use cases.
- `templates/SOUL.template.md` is the authoring baseline for new agents.
- `agents.json` provides a machine-readable catalog of all agents.

## Current Coverage

This repository currently includes 45 agents across 15 categories.

## Browse By Category

- [Automation](agents/automation/README.md)
- [Browser](agents/browser/README.md)
- [Business](agents/business/README.md)
- [Content](agents/content/README.md)
- [Data](agents/data/README.md)
- [Developer](agents/developer/README.md)
- [Finance](agents/finance/README.md)
- [Marketing](agents/marketing/README.md)
- [Multi-Agent](agents/multi-agent/README.md)
- [Operations](agents/operations/README.md)
- [Product](agents/product/README.md)
- [Productivity](agents/productivity/README.md)
- [Research](agents/research/README.md)
- [Security](agents/security/README.md)
- [Support](agents/support/README.md)

## Featured Agents

- [agents/browser/browser-research-operator](agents/browser/browser-research-operator/): for tab-heavy browsing, source gathering, and structured online research
- [agents/automation/os-task-runner](agents/automation/os-task-runner/): for desktop-style task execution, file handling, and repeatable local workflows
- [agents/data/data-extraction-agent](agents/data/data-extraction-agent/): for turning raw pages, PDFs, tables, or notes into structured records
- [agents/multi-agent/multi-agent-coordinator](agents/multi-agent/multi-agent-coordinator/): for splitting larger objectives into specialist sub-agents and integrating their outputs
- [agents/product/product-spec-writer](agents/product/product-spec-writer/): for turning rough product ideas into buildable specs
- [agents/security/security-reviewer](agents/security/security-reviewer/): for early-stage risk spotting on features, workflows, and system changes

## Recommended Agent Combos

- `Research Stack`: `browser-research-operator` + `web-research-analyst` + `synthesis-editor`
- `Launch Stack`: `product-spec-writer` + `launch-planner` + `campaign-brief-writer` + `social-content-planner`
- `Support Stack`: `support-triage-agent` + `knowledge-base-editor` + `customer-onboarding-guide`
- `Incident Stack`: `incident-commander` + `security-reviewer` + `incident-postmortem-writer`
- `Automation Stack`: `workflow-orchestrator` + `os-task-runner` + `data-extraction-agent`
- `Executive Briefing Stack`: `browser-research-operator` + `meeting-briefing-agent` + `project-status-reporter`

## Catalog

### Automation
See [agents/automation/README.md](agents/automation/README.md).

- [os-task-runner](agents/automation/os-task-runner/): Handles repeatable local file and desktop-style task flows.
- [recurring-task-automator](agents/automation/recurring-task-automator/): Turns repeated routines into scheduled automation plans.
- [workflow-orchestrator](agents/automation/workflow-orchestrator/): Designs multi-step automations across tools and services.

### Browser
See [agents/browser/README.md](agents/browser/README.md).

- [browser-research-operator](agents/browser/browser-research-operator/): Navigates sources and tabs to build structured research packets.
- [site-qa-navigator](agents/browser/site-qa-navigator/): Explores sites like a tester to find broken flows and regressions.
- [web-form-automation-agent](agents/browser/web-form-automation-agent/): Handles repetitive browser form flows and data-entry tasks.

### Business
See [agents/business/README.md](agents/business/README.md).

- [customer-voice-analyst](agents/business/customer-voice-analyst/): Extracts themes and action items from customer feedback.
- [market-mapper](agents/business/market-mapper/): Maps market structure, segments, and key competitors.
- [sales-prospect-researcher](agents/business/sales-prospect-researcher/): Prepares prospect briefs for outreach and discovery.

### Content
See [agents/content/README.md](agents/content/README.md).

- [newsletter-writer](agents/content/newsletter-writer/): Drafts concise newsletters from source notes and links.
- [social-content-planner](agents/content/social-content-planner/): Builds channel-aware social publishing plans.
- [youtube-digest-curator](agents/content/youtube-digest-curator/): Creates high-signal digests from creator and topic watchlists.

### Data
See [agents/data/README.md](agents/data/README.md).

- [data-extraction-agent](agents/data/data-extraction-agent/): Pulls structured fields and records out of messy source material.
- [dataset-cleanup-agent](agents/data/dataset-cleanup-agent/): Finds inconsistencies, duplicates, and cleanup priorities in datasets.
- [spreadsheet-analyst](agents/data/spreadsheet-analyst/): Answers business questions from spreadsheet-style tables.

### Developer
See [agents/developer/README.md](agents/developer/README.md).

- [api-integration-builder](agents/developer/api-integration-builder/): Plans API integrations and endpoint flows.
- [bug-triage-agent](agents/developer/bug-triage-agent/): Turns bug reports into reproducible engineering work.
- [code-reviewer](agents/developer/code-reviewer/): Reviews code changes for bugs, risks, and test gaps.

### Finance
See [agents/finance/README.md](agents/finance/README.md).

- [expense-auditor](agents/finance/expense-auditor/): Finds anomalies and cleanup opportunities in spend data.
- [kpi-analyst](agents/finance/kpi-analyst/): Summarizes business metrics and reporting deltas.
- [pricing-strategist](agents/finance/pricing-strategist/): Evaluates pricing models and packaging trade-offs.

### Marketing
See [agents/marketing/README.md](agents/marketing/README.md).

- [campaign-brief-writer](agents/marketing/campaign-brief-writer/): Turns rough marketing ideas into cross-channel briefs.
- [community-manager](agents/marketing/community-manager/): Plans community updates, moderation responses, and engagement loops.
- [seo-content-strategist](agents/marketing/seo-content-strategist/): Builds topic clusters and search-oriented content strategy.

### Multi-Agent
See [agents/multi-agent/README.md](agents/multi-agent/README.md).

- [multi-agent-coordinator](agents/multi-agent/multi-agent-coordinator/): Breaks larger goals into specialist workstreams and integrates the results.
- [specialist-router](agents/multi-agent/specialist-router/): Chooses the best agent or role for each subtask in a mixed workflow.
- [synthesis-editor](agents/multi-agent/synthesis-editor/): Combines multiple outputs into one coherent final deliverable.

### Operations
See [agents/operations/README.md](agents/operations/README.md).

- [incident-commander](agents/operations/incident-commander/): Coordinates response during outages and incidents.
- [project-status-reporter](agents/operations/project-status-reporter/): Creates short, honest stakeholder status updates.
- [sop-writer](agents/operations/sop-writer/): Converts repeated work into clear SOPs.

### Product
See [agents/product/README.md](agents/product/README.md).

- [feedback-prioritizer](agents/product/feedback-prioritizer/): Ranks feedback themes and product opportunities.
- [launch-planner](agents/product/launch-planner/): Builds cross-functional launch plans and readiness checklists.
- [product-spec-writer](agents/product/product-spec-writer/): Turns ideas and requirements into implementation-friendly specs.

### Productivity
See [agents/productivity/README.md](agents/productivity/README.md).

- [habit-coach](agents/productivity/habit-coach/): Supports accountability, reflection, and habit iteration.
- [inbox-triage-assistant](agents/productivity/inbox-triage-assistant/): Sorts inbox items into clear next actions.
- [meeting-briefing-agent](agents/productivity/meeting-briefing-agent/): Prepares concise, decision-ready meeting briefs.

### Research
See [agents/research/README.md](agents/research/README.md).

- [arxiv-paper-reader](agents/research/arxiv-paper-reader/): Explains technical papers and practical implications.
- [earnings-tracker](agents/research/earnings-tracker/): Summarizes earnings materials and management signal.
- [web-research-analyst](agents/research/web-research-analyst/): Turns broad research questions into source-backed findings.

### Security
See [agents/security/README.md](agents/security/README.md).

- [access-audit-analyst](agents/security/access-audit-analyst/): Reviews permissions for overbroad or stale access.
- [incident-postmortem-writer](agents/security/incident-postmortem-writer/): Writes postmortems from incident timelines and analysis.
- [security-reviewer](agents/security/security-reviewer/): Looks for obvious security risks and missing controls.

### Support
See [agents/support/README.md](agents/support/README.md).

- [customer-onboarding-guide](agents/support/customer-onboarding-guide/): Designs onboarding plans and activation guidance.
- [knowledge-base-editor](agents/support/knowledge-base-editor/): Turns rough support knowledge into help-center content.
- [support-triage-agent](agents/support/support-triage-agent/): Routes support requests by urgency and owner.

## How To Use

1. Pick a category and agent folder that fits the task.
2. Read the local `README.md` for scope, inputs, and output expectations.
3. Use the folder `SOUL.md` as the core prompt in OpenClaw.
4. Adjust voice, tools, and constraints for your environment.

## SOUL File Standard

Every agent in this repository follows the same core structure:

- `Role`
- `Mission`
- `Best For`
- `Expected Inputs`
- `Operating Principles`
- `Workflow`
- `Output Format`
- `Success Criteria`
- `Guardrails`

This makes agents easier to compare, reuse, and extend.

## Design Principles

- One agent, one clear responsibility
- Strong defaults, minimal fluff
- Real work categories over abstract personas
- Easy to combine into multi-agent workflows

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for authoring rules and [AGENTS.md](AGENTS.md) for repository-wide contributor guidance.
