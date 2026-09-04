# C:\dev Workspace

The canonical local workspace. A session rooted here inherits this layer. Global
engineering standards sit above it in `~/.claude/CLAUDE.md`, and each project
under here is its own standalone repo with its own instructions. Start with the
canon, then the map.

## Read in this order

1. `AGENTS.md` (or `CLAUDE.md`): the workspace canon. What this is, the
   verification discipline, the engine, safety and hygiene, launch order.
2. `ECOSYSTEM.md`: the public tools and how they compose. The platform is Flywheel.
3. `MISSION.md`: what Zentropy Labs is building and why.
4. `CREDO.md`: the belief the tools instantiate.
5. `WORKSPACE-INDEX.md`: the local map. Directory classes, what is private or
   generated, repo-selection rules, and how to regenerate the repo inventory.
6. `public/flywheel/GETTING-STARTED.md`: your first thirty minutes with the engine.

## What this is

`C:\dev` is a local workspace for vendor portability, schema stability, and
operator-owned provenance across nested repos, CLIs, model routes, and research
lanes. Tools and models are replaceable materials, and the user chooses them. The
epistemic verification engine and its lane layer live in `public/flywheel`.

## Operating shape

State here is file-backed, local, and explicit. Do not assume a model has hidden
awareness of prior sessions or roadmap. Load this root layer, then the target
repo's own instructions, and run `git status` before editing. Never commit
`.env`, keys, tokens, browser profiles, local databases, or credential files.
`protected/`, `secrets/`, and warden-ops material stay local.
