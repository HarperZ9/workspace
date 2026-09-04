# Workspace Roadmap

This is the roadmap for the workspace-session layer only: keeping `C:\dev`
navigable and its root docs true to the code. The product roadmap lives with the
platform in `public/flywheel`; this file does not duplicate it.

## Current posture

- `C:\dev` is the canonical local workspace. The engine and the six lanes live in
  `public/flywheel`; Index (`public/index`) owns the repository inventory.
- Root docs are canon only while they match the code. When a change lands that a
  root doc describes, update the doc in the same pass. A doc that lags the code is
  a defect.
- `state/` and `protected/` hold legacy and private material. They are capability
  sources, not the current architecture.

## Near-term housekeeping

- Regenerate `WORKSPACE-REPO-MAP.json` after major repo moves or branch changes
  with Index: `python -m index_graph map --root C:\dev` from `public/index`. The
  config is `.repomap.toml` at the workspace root.
- Add repo-local `AGENTS.md` or `CLAUDE.md` files where public or tool repos lack
  launch instructions.
- Decide, tree by tree, what under `state/` and `protected/` promotes into the
  current architecture and what stays archived.
- Normalize branch tracking for local-only worktrees meant to stay connected to
  their remotes.

## Decision rules

- Commit source and docs only when they are stable, verified, and secret-free.
- Preserve private and runtime state outside commits.
- Prefer canonical worktrees under `C:\dev` over deprecated mirrors.
- Keep the root layer lean and pointer-based. Detailed behavior belongs in
  repo-local docs.
- Treat a model, API, transport, or policy change as a boundary change. Absorb it
  through adapters, manifests, and probes, not by reorganizing the workspace.
