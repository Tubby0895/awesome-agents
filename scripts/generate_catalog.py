#!/usr/bin/env python3
import argparse
import json
import pathlib
from copy import deepcopy


ROOT = pathlib.Path(__file__).resolve().parents[1]
CATALOG_PATH = ROOT / "agents.json"


CATEGORY_DESCRIPTIONS = {
    "automation": "Agents for repeatable local tasks, orchestrated workflows, and recurring automation opportunities.",
    "browser": "Agents for browsing-heavy work such as research, form automation, and web flow validation.",
    "business": "Agents for market mapping, sales research, and customer insight synthesis.",
    "content": "Agents for drafting newsletters, planning social content, and digesting creator material.",
    "data": "Agents for extracting, cleaning, and interpreting structured and semi-structured data.",
    "developer": "Agents for engineering review, debugging intake, and integration planning.",
    "finance": "Agents for KPI interpretation, pricing strategy, and spend review.",
    "marketing": "Agents for campaign planning, SEO content strategy, and community operations.",
    "multi-agent": "Agents for routing work across specialists, coordinating larger workflows, and synthesizing outputs.",
    "operations": "Agents for incident response, SOP writing, and project status reporting.",
    "product": "Agents for specification writing, prioritization, validation, and launch planning.",
    "productivity": "Agents for inbox cleanup, planning, relationship management, and personal operations.",
    "research": "Agents for web research, paper reading, and analytical briefings.",
    "security": "Agents for security review, access audits, and incident postmortems.",
    "support": "Agents for support queue triage, help-center writing, and onboarding guidance.",
}

FULL_TITLE_OVERRIDES = {
    "multi-agent": "Multi-Agent",
}

PART_TITLE_OVERRIDES = {
    "api": "API",
    "arxiv": "arXiv",
    "crm": "CRM",
    "kpi": "KPI",
    "n8n": "n8n",
    "os": "OS",
    "qa": "QA",
    "seo": "SEO",
    "sop": "SOP",
    "youtube": "YouTube",
}

CATEGORY_TAGS = {
    "automation": ["automation", "workflows"],
    "browser": ["browser", "web"],
    "business": ["business", "analysis"],
    "content": ["content", "publishing"],
    "data": ["data", "structured-data"],
    "developer": ["developer", "engineering"],
    "finance": ["finance", "metrics"],
    "marketing": ["marketing", "growth"],
    "multi-agent": ["multi-agent", "coordination"],
    "operations": ["operations", "execution"],
    "product": ["product", "planning"],
    "productivity": ["productivity", "personal-ops"],
    "research": ["research", "analysis"],
    "security": ["security", "risk"],
    "support": ["support", "customer-ops"],
}

CATEGORY_BEST_FOR = {
    "automation": ["repeatable tasks", "workflow planning", "operations with dependencies"],
    "browser": ["web navigation", "browser-driven research", "UI and form workflows"],
    "business": ["market analysis", "sales research", "customer insight synthesis"],
    "content": ["digest creation", "editorial planning", "content production"],
    "data": ["data extraction", "table review", "dataset cleanup"],
    "developer": ["engineering workflows", "bug and code review", "integration planning"],
    "finance": ["metric review", "pricing analysis", "spend monitoring"],
    "marketing": ["campaign planning", "audience messaging", "growth content"],
    "multi-agent": ["task routing", "coordination", "cross-output synthesis"],
    "operations": ["status reporting", "incident response", "execution tracking"],
    "product": ["idea evaluation", "spec writing", "launch planning"],
    "productivity": ["daily planning", "personal organization", "follow-up management"],
    "research": ["source-backed analysis", "technical reading", "topic briefings"],
    "security": ["risk review", "audit preparation", "post-incident learning"],
    "support": ["customer support", "knowledge management", "onboarding workflows"],
}

BEGINNER_PICKS = [
    "inbox-triage-assistant",
    "meeting-briefing-agent",
    "newsletter-digest-agent",
    "browser-research-operator",
    "project-status-reporter",
    "knowledge-base-editor",
]

FEATURED_STACKS = [
    {
        "name": "Research Stack",
        "description": "Go from browsing to synthesis without losing sources or follow-up ideas.",
        "agents": ["browser-research-operator", "web-research-analyst", "synthesis-editor"],
    },
    {
        "name": "Launch Stack",
        "description": "Move from early concept to launch planning and outward-facing messaging.",
        "agents": [
            "idea-validator-agent",
            "product-spec-writer",
            "launch-planner",
            "campaign-brief-writer",
        ],
    },
    {
        "name": "Daily Personal Ops Stack",
        "description": "Keep mornings, relationships, and newsletter-heavy inputs under control.",
        "agents": [
            "morning-briefing-agent",
            "newsletter-digest-agent",
            "personal-crm-agent",
        ],
    },
    {
        "name": "Automation Stack",
        "description": "Design and run automation workflows with practical recovery and data handoffs.",
        "agents": ["workflow-orchestrator", "n8n-integration-architect", "data-extraction-agent"],
    },
]

FEATURED_AGENTS = [
    "browser-research-operator",
    "os-task-runner",
    "data-extraction-agent",
    "multi-agent-coordinator",
    "product-spec-writer",
    "security-reviewer",
]


def titleize_slug(slug: str) -> str:
    if slug in FULL_TITLE_OVERRIDES:
        return FULL_TITLE_OVERRIDES[slug]
    parts = slug.split("-")
    titled = []
    for part in parts:
        if part in PART_TITLE_OVERRIDES:
            titled.append(PART_TITLE_OVERRIDES[part])
        else:
            titled.append(part.capitalize())
    return " ".join(titled)


def infer_tags(category_name: str, slug: str) -> list[str]:
    stopwords = {
        "agent",
        "assistant",
        "manager",
        "operator",
        "planner",
        "writer",
        "reviewer",
        "analyst",
        "curator",
        "producer",
        "tracker",
        "extractor",
        "validator",
        "architect",
        "commander",
        "reporter",
        "guide",
        "coordinator",
        "strategist",
        "coach",
        "builder",
        "editor",
    }
    tags = list(CATEGORY_TAGS[category_name])
    for part in slug.split("-"):
        if part not in stopwords and part not in tags:
            tags.append(part)
    return tags[:6]


def infer_requires(category_name: str, slug: str) -> dict:
    lowered = slug.lower()
    browser = category_name == "browser"
    filesystem = any(token in lowered for token in {"os", "file", "dataset", "server", "spreadsheet"})
    api = any(token in lowered for token in {"api", "integration", "n8n", "workflow", "tracker"})
    human_review = category_name in {"security", "finance"} or "health" in lowered or "incident" in lowered
    return {
        "browser": browser,
        "filesystem": filesystem,
        "api": api,
        "humanReview": human_review,
    }


def normalize_catalog(raw_catalog: dict) -> dict:
    catalog = deepcopy(raw_catalog)
    catalog["formatVersion"] = 2
    catalog["beginnerPicks"] = BEGINNER_PICKS
    catalog["featuredAgents"] = FEATURED_AGENTS
    catalog["featuredStacks"] = FEATURED_STACKS

    for category in catalog["categories"]:
        category_name = category["name"]
        category["title"] = titleize_slug(category_name)
        category["description"] = CATEGORY_DESCRIPTIONS[category_name]

        for agent in category["agents"]:
            agent["slug"] = agent["id"]
            agent["name"] = agent.get("name") or titleize_slug(agent["id"])
            agent["category"] = category_name
            agent["tags"] = agent.get("tags") or infer_tags(category_name, agent["id"])
            agent["bestFor"] = agent.get("bestFor") or CATEGORY_BEST_FOR[category_name]
            agent["maturity"] = agent.get("maturity") or "ready"
            agent["beginnerFriendly"] = agent.get("beginnerFriendly", agent["id"] in BEGINNER_PICKS)
            agent["requires"] = agent.get("requires") or infer_requires(category_name, agent["id"])

    return catalog


def agent_link(path: str) -> str:
    return f"{path}/"


def render_repository_layout() -> str:
    return """## Repository Layout

```text
agents/<category>/<agent>/
  README.md
  SOUL.md

templates/
  SOUL.template.md

agents.json
scripts/generate_catalog.py
```

- `SOUL.md` is the main OpenClaw prompt.
- `README.md` summarizes scope, inputs, and ideal use cases.
- `templates/SOUL.template.md` is the authoring baseline for new agents.
- `agents.json` is the source catalog used to generate repository indexes.
- `scripts/generate_catalog.py` regenerates the root and category README files.
"""


def render_quick_start() -> str:
    return """## Quick Start

1. Pick an agent from a category page or the beginner picks below.
2. Open that agent folder and read its `README.md` for scope and expected inputs.
3. Copy the folder `SOUL.md` into your OpenClaw setup or adapt it for your runtime.
4. If you customize the agent, keep the core responsibility narrow and preserve the output contract.
"""


def render_beginner_picks(catalog: dict) -> str:
    by_id = {
        agent["id"]: agent
        for category in catalog["categories"]
        for agent in category["agents"]
    }
    lines = ["## Beginner Picks", ""]
    for agent_id in catalog["beginnerPicks"]:
        agent = by_id[agent_id]
        lines.append(f"- [{agent['name']}]({agent_link(agent['path'])}): {agent['description']}")
    return "\n".join(lines)


def render_browse_by_category(catalog: dict) -> str:
    lines = ["## Browse By Category", ""]
    for category in catalog["categories"]:
        category_readme = category.get("path") or f"agents/{category['name']}/README.md"
        lines.append(f"- [{category['title']}]({category_readme})")
    return "\n".join(lines)


def render_featured_agents(catalog: dict) -> str:
    by_id = {
        agent["id"]: agent
        for category in catalog["categories"]
        for agent in category["agents"]
    }
    lines = ["## Featured Agents", ""]
    for agent_id in catalog["featuredAgents"]:
        agent = by_id[agent_id]
        lines.append(f"- [{agent['path']}]({agent_link(agent['path'])}): {agent['description']}")
    return "\n".join(lines)


def render_featured_stacks(catalog: dict) -> str:
    by_id = {
        agent["id"]: agent
        for category in catalog["categories"]
        for agent in category["agents"]
    }
    lines = ["## Recommended Agent Combos", ""]
    for stack in catalog["featuredStacks"]:
        names = [f"`{by_id[agent_id]['id']}`" for agent_id in stack["agents"]]
        lines.append(f"- `{stack['name']}`: {' + '.join(names)}")
        lines.append(f"  {stack['description']}")
    return "\n".join(lines)


def render_catalog(catalog: dict) -> str:
    lines = ["## Catalog", ""]
    for category in catalog["categories"]:
        lines.append(f"### {category['title']}")
        lines.append(f"{category['description']}")
        lines.append("")
        lines.append(f"See [agents/{category['name']}/README.md](agents/{category['name']}/README.md).")
        lines.append("")
        for agent in category["agents"]:
            lines.append(f"- [{agent['name']}]({agent_link(agent['path'])}): {agent['description']}")
        lines.append("")
    return "\n".join(lines).rstrip()


def render_submit_section() -> str:
    return """## Submit an Agent

1. Create a folder under `agents/<category>/<agent-name>/`.
2. Add a focused `README.md` and a reusable `SOUL.md`.
3. Update `agents.json` with the new agent metadata.
4. Run `python3 scripts/generate_catalog.py --write` to regenerate the repository indexes.
5. Open a PR with the agent purpose, target user, and a short verification note.

See [CONTRIBUTING.md](CONTRIBUTING.md) for the contribution rules and [templates/SOUL.template.md](templates/SOUL.template.md) for the prompt baseline.
"""


def render_contributing_footer() -> str:
    return """## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for authoring rules and [AGENTS.md](AGENTS.md) for repository-wide contributor guidance.
"""


def render_root_readme(catalog: dict) -> str:
    category_count = len(catalog["categories"])
    agent_count = sum(len(category["agents"]) for category in catalog["categories"])

    sections = [
        "# Awesome Agents",
        "",
        "A curated collection of OpenClaw-ready agents organized by category and centered on reusable `SOUL.md` files.",
        "",
        "This project takes structural cues from community agent collections while keeping the repository simple: one folder per agent, one `SOUL.md` as the primary prompt, and one short `README.md` that explains when to use it.",
        "",
        "<!-- Generated by scripts/generate_catalog.py -->",
        "",
        render_repository_layout().rstrip(),
        "",
        "## Current Coverage",
        "",
        f"This repository currently includes {agent_count} agents across {category_count} categories.",
        "",
        render_quick_start().rstrip(),
        "",
        render_beginner_picks(catalog).rstrip(),
        "",
        render_browse_by_category(catalog).rstrip(),
        "",
        render_featured_agents(catalog).rstrip(),
        "",
        render_featured_stacks(catalog).rstrip(),
        "",
        render_catalog(catalog).rstrip(),
        "",
        "## SOUL File Standard",
        "",
        "Every agent in this repository follows the same core structure:",
        "",
        "- `Role`",
        "- `Mission`",
        "- `Best For`",
        "- `Expected Inputs`",
        "- `Operating Principles`",
        "- `Workflow`",
        "- `Output Format`",
        "- `Success Criteria`",
        "- `Guardrails`",
        "",
        "This makes agents easier to compare, reuse, and extend.",
        "",
        "## Design Principles",
        "",
        "- One agent, one clear responsibility",
        "- Strong defaults, minimal fluff",
        "- Real work categories over abstract personas",
        "- Easy to combine into multi-agent workflows",
        "",
        render_submit_section().rstrip(),
        "",
        render_contributing_footer().rstrip(),
        "",
    ]
    return "\n".join(sections)


def render_category_readme(category: dict) -> str:
    lines = [
        f"# {category['title']}",
        "",
        category["description"],
        "",
        "<!-- Generated by scripts/generate_catalog.py -->",
        "",
        "## Agents",
        "",
    ]
    for agent in category["agents"]:
        tags = ", ".join(f"`{tag}`" for tag in agent["tags"][:4])
        lines.append(f"- [{agent['name']}](./{agent['id']}/): {agent['description']}")
        lines.append(f"  Best for: {', '.join(agent['bestFor'][:2])}. Tags: {tags}.")
    lines.append("")
    return "\n".join(lines)


def write_output(catalog: dict, output_dir: pathlib.Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "README.md").write_text(render_root_readme(catalog))
    agents_root = output_dir / "agents"
    for category in catalog["categories"]:
        category_dir = agents_root / category["name"]
        category_dir.mkdir(parents=True, exist_ok=True)
        (category_dir / "README.md").write_text(render_category_readme(category))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--catalog-path", default=str(CATALOG_PATH))
    parser.add_argument("--output-dir", default=str(ROOT))
    parser.add_argument("--rewrite-json", action="store_true")
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()

    catalog_path = pathlib.Path(args.catalog_path)
    output_dir = pathlib.Path(args.output_dir)
    raw_catalog = json.loads(catalog_path.read_text())
    catalog = normalize_catalog(raw_catalog)

    if args.rewrite_json:
        catalog_path.write_text(json.dumps(catalog, indent=2) + "\n")

    if args.write or output_dir != ROOT:
        write_output(catalog, output_dir)


if __name__ == "__main__":
    main()
