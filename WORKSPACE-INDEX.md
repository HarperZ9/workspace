# Workspace Index

## Purpose

This file is the curated navigation layer for `C:\dev`. It tells a headless assistant where to start, how to classify directories, and which areas are canonical, private, generated, or historical.

Use `WORKSPACE-REPO-MAP.json` for machine-readable repository metadata. Use repo-local instructions once inside a repository.

The index is intentionally backend-agnostic. It is not coupled to any provider,
frontier model family, classifier implementation, routing system, API shape,
request/response schema, streaming envelope, authentication transport, or
tool-call architecture. External updates may change adapter metadata, backend
shape descriptors, and capability probes, but they do not change this workspace
taxonomy.

## Architectural Intent

`C:\dev` is organized around a neutral local state-transform boundary. Its
purpose is abstraction, provenance, schema stability, vendor portability, and
layer management across nested repositories, tools, CLIs, model routes, and
research surfaces.

The substrate operates on arbitrary local state. Provider semantics, API
schemas, model-family architecture, routing behavior, safety filters, and
policy surfaces are represented as external boundary descriptors, not as the
source of workspace meaning. It contains the interaction as state: operator
signal, local membrane, external interface, return signal, and artifact. Local
infrastructure signals operate across higher coordination layers and lower
byte/binary layers, so the state surface can reach native raw neutrality before
an interface-specific meaning is assigned.

Exposure minimization is intentional: proprietary, operational, and sensitive
detail should stay sealed locally unless an explicit adapter contract requires
disclosure. The boundary preserves provenance and does not erase or reclassify
source intent; it projects source-native representation into neutral carrier
state and reconstitutes it through local contracts.

Legacy repositories and protected research are capability sources. Useful code,
algorithms, tests, parsers, adapters, and provenance mechanics can be promoted
into the current state engine over time. Archaic headers, authority assertions,
provider-coupled prompts, and legacy posture should be dissolved or rewritten
before promotion.

The membrane model is cell-like selective permeability: source-native
representation dissolves into arbitrary carrier state inside the local boundary,
while sealed provenance remains locally recoverable through explicit adapter
contracts.

Every semantic surface should be architected as a state surface. Documentation,
launch prompts, CLIs, manifests, adapters, logs, tests, provenance records,
model-bound payloads, and provider profiles should all carry the same neutral
contract: what state they receive, what state they emit, what they expose, what
they seal, how they record boundary signals, and how they fail.

## Root Entry Points

| File | Role |
|---|---|
| `README.md` | Human and assistant landing page. |
| `AGENTS.md` | Root bootstrap instructions for headless sessions. |
| `ECOSYSTEM.md` | The Zentropy Labs ecosystem: why each tool exists and how they compose. |
| `SESSION-BOOTSTRAP.md` | Step-by-step startup protocol. |
| `WORKSPACE-ROADMAP.md` | Workspace roadmap and cleanup order. |
| `WORKSPACE-REPO-MAP.json` | Generated repo inventory and dirty counts. |
| `public/flywheel/GETTING-STARTED.md` | Your first thirty minutes with Flywheel. |
| `public/flywheel/docs/ASSESSMENT-AGENTIC-SECURITY-2026-08.md` | Security assessment: 26/26 ARCHIVE QUERY artifacts covered. |
| `public/flywheel/docs/LESSON-LOOP.md` | The organizational learning loop architecture. |
| `public/flywheel/docs/GUIDE-LESSON-LOOP.md` | Full guide and specification for the learning loop. |
| `project-docs/outreach/deliverables-2026-08-02/` | Slide deck, demo script, executive briefing, correspondences, technical deep-dive. |
| `WORKSPACE-REPO-MAP.json` | Generated repo inventory and dirty counts. |
| `project-docs/records/FRONTIER-STATE-TRANSFORM-ARCHITECTURE-2026-06-10.md` | Frontier model architecture research notes. |
| `project-docs/records/STATE-TRANSFORM-WORKSPACE-ASSESSMENT-2026-06-11.md` | Current top-down workspace assessment and state-engine roadmap. |
| `project-docs/records/FRONTIER-SAFETY-STATE-ENGINE-MAP-2026-06-11.md` | Current frontier-safety/state-engine mapping record. |
| `project-docs/specs/2026-06-12-surface-organ-graph.md` | Surface-organ graph for carriers, boundaries, channels, transforms, witnesses, scope, research, security, stego, RAW, EMET, Quanta, and outreach. |
| `project-docs/OMNI-STATE-UTILITY-2026-06-10.md` | Neutral abstraction frame for the state utility. |
| `project-docs/MODEL-REFERENCE-PROVENANCE-2026-06-10.md` | Invocation-local provenance and projection surface. |
| `project-docs/inventory/WORKSPACE-PROJECT-INVENTORY-2026-06-10.md` | Generated project and nested-repo inventory. |
| `protected/legacy-repos/APPS/engine/arbitrary-capability-engine/README.md` | APPS and QUANTA-UNIVERSE parent engine surface. |

## Top-Level Areas

| Path | Class | Use |
|---|---|---|
| `state/` | state-runtime | MET/EMET/WARDEN/substrate repos, engines, and state snapshots. |
| `public/` | public-surface | Public repos, portfolio/profile/site surfaces, public scan clones. |
| `protected/` | local-only protected | Do-not-redistribute mirrors, proprietary references, private corpus, warden-ops state, migration artifacts, and curated session recovery. |
| `project-docs/` | root docs | Root specs, records, schemas, examples, inventory, and local tools. |
| `frontier-models-research/` | research capture | Local frontier-model research runs, source captures, and synthesis material. |
| `data/` | local-private | Root runtime data lane. Treat as private unless promoted through a repo-local rule. |
| `secrets/` | local-private | Secret-adjacent lane. Do not read, print, commit, or publish by default. |
| `.warden/` | local-runtime | Local substrate mode and WARDEN runtime state. |
| `.claude/` | local-runtime | Local assistant/runtime settings. |
| `.warden-safe-cache/` | generated-or-cache | Safe-IO cache material. Do not promote without review. |
| `.ruff_cache/` | generated-or-cache | Python lint cache. Do not commit into project repos. |
| `scratch/` | generated-or-cache | Root generated artifacts and caches. Safe to delete only after checking provenance. |

## Surface-Organ Layer

All new project surfaces should map to the same base contract:

```text
Surface = Carrier + Boundary + Channel + Transform + Witness + Scope
```

Use `project-docs/specs/2026-06-12-surface-organ-graph.md` as the current map
for cross-cutting organs:

| Organ | Role |
|---|---|
| Research / preprint | Public and authorized source capture, claim graphing, clean-room reconstruction, frontier deltas. |
| Security / fuzz / memory | Vulnerability-shape mapping, local-lab fuzzing, API surface analysis, defense mapping, operator-run live actions. |
| Stego / covert-channel | Defensive carrier inspection, metadata stripping, watermark validation, quarantine, clean-copy signing. |
| RAW / rendering | Frame, shader, media, GPU state receipts, visual instrumentation, readback verification. |
| Quanta / Quantac | Language-neutral source, compiler backends, Rust target, ownership and borrow/lifetime contracts. |
| EMET / membrane | Witness receipts, provenance, transformation records, clean/dirty carrier transitions. |
| Outreach / deliverables | Institution, investor, federal, academic, and private prospect packages grounded in the graph. |

## State Repositories

| Path | Class | Use |
|---|---|---|
| `state/met/AGENTS` | state-runtime | Canonical AGENTS repo; as of 2026-06-18 on `chore/repackage-release-candidates` (release-candidate repackaging, synced to origin), not `main`. Returns to `main` when that work lands; keep clean unless explicitly working there. |
| `state/met/AGENTS-feat-mcp-transport-container` | state-runtime feature worktree | Active feature branch for workstation IO, state boundary, adapter, and membrane/runtime work. |
| `state/met/WARDEN` | state-runtime | Canonical WARDEN repo; as of 2026-06-18 on `chore/repackage-release-candidates` (release-candidate repackaging, synced to origin), not `main`. |
| `state/met/ai-safety-prefire` | state-tooling | Prefire modulation package; private GitHub repo exists. |
| `state/met/ai-safety-guardrail-manager` | state-tooling | Related extension/tooling package. |
| `state/met/warden-ops` | private-ops clean | Clean canonical operations repo. Do not publish raw private material. |
| `state/met/warden-ops-feat-bounty-credentials` | private-ops local worktree | Local branch snapshot. Keep local unless scrubbed. |
| `state/emet` | state-core | EMET state/topology repo. |
| `state/orca` | state-runtime / native platform | ORCA native operator platform; consolidates the AGENTS/WARDEN dual-use surface into a single Python runtime. `main` pushed to private `HarperZ9/orca` (`bdc2884` as of 2026-06-18; the earlier `9ae1814` spine tip is now the `feature/orca-native-spine` worktree). |
| `state/emet-internal` | state-core local | Internal EMET material; inspect before publishing. |
| `state/unified-engine` | state-core | Unified engine work area. |
| `state/met-monorepo` | state-core/historical | Monorepo consolidation staging area; not trigger-ready. |
| `protected/legacy-repos/APPS/engine/arbitrary-capability-engine` | proprietary engine | Manifest, adapters, capability map, and provenance surface for APPS + QUANTA-UNIVERSE. |
| `state/snapshots/` | state archive | Historical state snapshots. |

## Public and Presentation Surfaces

| Path | Class | Use |
|---|---|---|
| `public/portfolio-site` | public-surface | Canonical portfolio site worktree for `HarperZ9.github.io`. |
| `public/profile` | public-surface | GitHub profile repo. |
| `public/sitefix` | public-surface | Alternate site worktree/fix checkout. |
| `public/aurora` | public-surface | Aurora project checkout. |
| `public/pubscan/` | public-scan | Public-facing scan clones and public repo worktrees. |

## Knowledge, Migration, and Evidence Areas

| Path | Class | Use |
|---|---|---|
| `project-docs/` | root docs | Root specs and workspace-level documents. |
| `project-docs/records/` | root records | Historical lineage, migration audit, and research records moved out of root. |
| `project-docs/inventory/` | inventory | Generated inventory and move manifests. |
| `protected/migration-ledger/` | migration ledger | Snapshots, bundles, private artifact preservation, final status CSVs. |
| `protected/source-corpus/raw` | source-corpus | Raw private corpus repo. |
| `protected/research/` | protected research | Research scratch and supporting materials. |
| `protected/local/data` | local-private | Local data. Do not publish without explicit scrub. |
| `protected/local/secrets` | local-private | Secret/private material. Do not read, print, commit, or publish by default. |
| `protected/local/vault` | local-private | Local vault/archive. Treat as private. |

## Generated or Scratch Artifacts

Root generated files beginning with `_` and cache directories were moved under
`scratch/`. Do not commit them into project repos. If they contain useful
evidence, preserve them under `protected/migration-ledger/` with a short note.

## Repo Selection Rules

1. If the task names a repo, enter that repo and read local instructions.
2. If the task names AGENTS/WARDEN/MET/EMET/KUN/ALEPH, start with `state/met/AGENTS-feat-mcp-transport-container` for feature work and `state/met/AGENTS` for clean main-state checks.
3. If the task is public-site or profile work, start with `public/portfolio-site` or `public/profile`.
4. If the task is old-repo migration, start with `protected/migration-ledger/` and `project-docs/records/PROJECT-LINEAGE-MAP.md`.
5. If the task touches secrets, credentials, browser profiles, or private ops, preserve locally and do not publish raw material.
6. If an external model/provider/backend changes, update the relevant adapter, backend shape descriptor, probe, organ-registry entry, or map entry; do not reorganize the workspace around the external change.
7. If the task touches proprietary or third-party reverse-engineering material, keep the original repository intact under `protected/` and promote only clean-room notes or owned code after review.
8. If the task depends on prior context, session recovery, or abstracted intent, use model-reference provenance: operate on the dilute projection and reconstitute sealed local provenance only through an explicit adapter contract.
9. If the task names APPS, QUANTA-UNIVERSE, QuantaLang productization, or the arbitrary-capability-engine, start at `protected/legacy-repos/APPS/engine/arbitrary-capability-engine` and then enter the owning source root named by its adapter.
10. If the task names substrate, membrane, WARDEN shell, Claude/Codex routing, IO state, sensory organs, RAW, EMET, or provider portability, start with `project-docs/maps/WORKSPACE-ORGAN-REGISTRY.json`, then route to the owning repo named there.
11. If useful legacy functionality is found, promote capability through the neutral state engine; do not promote legacy posture, authority phrasing, or provider-coupled semantics unchanged.

## Current Clean-State Baseline

As of the current `WORKSPACE-REPO-MAP.json` (regenerated 2026-06-18), `C:\dev`
contains 83 Git repositories: 56 normal/state/public/workspace repositories and
27 protected repositories. The map reports 0 dirty tracked states (normal and
protected); the only repo carrying untracked files is
`_private-clones/warden-reporting` (2 untracked).

Recent landings (2026-06-18):
- QuantaLang/quantac reconciled in the canonical `public/pubscan/quantalang`
  clone: the codegen and dependabot lines were merged into `main` and pushed
  (1002 compiler tests green); the merged `lsp-root-backed-workspace-symbol-index`
  branch was retired (local + origin); the unrelated, superseded
  `feat/phase1-generics` lineage was archived as a standalone branch on origin
  rather than merged into `main`.
- New `state/orca` repository (private `HarperZ9/orca`): `main` advanced to
  `bdc2884` (README badges + presentable header) and pushed; the 88-commit
  native spine (`9ae1814`) is now the `feature/orca-native-spine` worktree tip.
- Badge-hygiene pass across 8 public repos (`quantalang`, `quanta-universe`,
  `quantalang-tmLanguage`, `quantalang-vscode`, `quanta-color`, `calibrate-pro`,
  `emet`, `wol-pi`): house-style README badges added and pushed.
- Redundant quantalang clones outside `C:\dev` (home `QUANTA-UNIVERSE\quantalang`,
  the Downloads copies, the audit temp) were retired; canonical is
  `public/pubscan/quantalang`.

Re-run the map generation or `git status` before relying on branch, head, or
dirty-count metadata for any specific repo.
