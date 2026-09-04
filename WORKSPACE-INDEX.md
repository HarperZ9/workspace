# Workspace Index

## Purpose

The curated navigation layer for `C:\dev`. It tells a session where to start,
how to classify the top-level directories, and which areas are canonical,
private, generated, or historical. Use `WORKSPACE-REPO-MAP.json` for
machine-readable repository metadata, and repo-local instructions once inside a
repository.

This index is a map of the local filetree. `ECOSYSTEM.md` is the companion map
of the public tools and how they compose. Read that one for what the tools do;
read this one for where things live on disk.

## What this is

`C:\dev` is a local workspace for vendor portability, schema stability, and
operator-owned provenance across nested repos, CLIs, model routes, and research
lanes. Tools and models are replaceable materials, and external provider behavior
is a boundary fact carried by an adapter or a probe, never the design target. The
epistemic verification engine lives in `public/flywheel`.

Legacy trees under `state/` and `protected/` are capability sources. Useful code,
algorithms, tests, and parsers can be promoted into the current architecture over
time. Old headers, authority assertions, and provider-coupled prompts are
rewritten or dropped before promotion, not carried forward.

## Root entry points

| File | Role |
|---|---|
| `README.md` | Front door. Start here. |
| `AGENTS.md` / `CLAUDE.md` | The workspace canon, kept in sync by hand. |
| `ECOSYSTEM.md` | The public tools and how they compose. |
| `MISSION.md` | What Zentropy Labs is building and why. |
| `CREDO.md` | The belief the tools instantiate. |
| `WORKSPACE-ROADMAP.md` | Current workspace posture and near-term housekeeping. |
| `WORKSPACE-REPO-MAP.json` | Generated repo inventory. Regenerate before trusting it. |
| `public/flywheel/GETTING-STARTED.md` | First thirty minutes with the engine. |
| `public/flywheel/harness/lanes.py` | The live lane map, the ground truth for the tools. |

`project-docs/` holds historical specs, records, and inventories. Some predate
the Flywheel consolidation and organize around a superseded model. Treat them as
lineage, not as current architecture.

## Top-level areas

| Path | Class | Use |
|---|---|---|
| `public/` | public-surface | Public repos: the Flywheel engine, Index, the live site source, and the individual tool repos mapped in `ECOSYSTEM.md`. |
| `state/` | legacy-runtime | Archived state-runtime and engine material predating the Flywheel consolidation. A capability source, not the current architecture. |
| `protected/` | local-only | Do-not-redistribute mirrors, proprietary references, private corpus, warden-ops state, migration artifacts, session recovery. |
| `project-docs/` | root docs | Root specs, records, schemas, inventories, and local tools. May lag the code. |
| `frontier-models-research/` | research capture | Local research runs and source captures. |
| `data/` | local-private | Root runtime data lane. Private unless a repo-local rule promotes it. |
| `secrets/` | local-private | Secret-adjacent lane. Do not read, print, commit, or publish by default. |
| `worktrees/` | working | Named git worktrees for in-flight branch work across repos. |
| `scratch/` | generated | Root generated artifacts and caches. Check provenance before deleting. |
| `.warden/`, `.warden-safe-cache/`, `.claude/`, `.ruff_cache/` | local-runtime / cache | Local runtime state and generated caches. Do not commit into project repos. |

The root also holds many working checkouts, per-repo clones, feature worktrees,
and `_`/`tmp-`/`release-` scratch directories beyond these classes. They are a
working area, not canon. `WORKSPACE-REPO-MAP.json` and `git status` are ground
truth for what is present and dirty.

## Public and presentation surfaces

| Path | Use |
|---|---|
| `public/flywheel` | The flagship. The epistemic engine, the six lanes, the gateway, receipts, governance, the learning loop. |
| `public/index` | Index: the repository-inventory and code-intelligence tool. Owns the workspace repo map. |
| `public/portfolio-site` | Live checkout of the `HarperZ9.github.io` site. Site edits are PR-based against that repo; verify `git status` before touching this tree. |
| `public/telos-v2` | Source of the design and voice canon (`project-docs/DESIGN-VOICE-CANON.md`). Can lag the live site. |

## Knowledge, migration, and evidence areas

| Path | Use |
|---|---|
| `project-docs/records/` | Historical lineage, migration audit, and research records moved out of root. |
| `project-docs/inventory/` | Generated inventory and move manifests. |
| `protected/migration-ledger/` | Snapshots, bundles, private artifact preservation, status records. |
| `protected/research/` | Research scratch and supporting material. |
| `protected/local/` | Local data, secrets, and vault. Do not publish without an explicit scrub. |

## Repo selection rules

1. If the task names a repo, enter it and read its local instructions.
2. Engine or lane work starts at `public/flywheel`; read `harness/lanes.py` first.
3. Public-site or profile work is PR-based against the `HarperZ9.github.io`
   repo. Treat `public/portfolio-site` as a live checkout and check `git status`
   before editing it.
4. Old-repo migration starts at `protected/migration-ledger/`.
5. Secrets, credentials, browser profiles, or private ops: preserve locally and
   never publish raw material.
6. If an external model or provider changes, update the relevant adapter, probe,
   or map entry. Do not reorganize the workspace around the external change.
7. If useful legacy functionality is found under `state/` or `protected/`,
   promote the capability through the current architecture. Do not carry old
   posture, authority phrasing, or provider-coupled semantics forward unchanged.

## Repo inventory

`WORKSPACE-REPO-MAP.json` is a generated snapshot and goes stale. The generator
is now part of Index (`public/index`), which retired the standalone
`workspace-repo-map` tool into itself. Regenerate the inventory with Index:

```powershell
python -m index_graph map --root C:\dev
```

The count in any committed snapshot is not authoritative. Run `git status` in a
repo before relying on its branch, head, or dirty state.
