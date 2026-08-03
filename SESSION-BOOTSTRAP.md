# Session Bootstrap

## Goal

Give any headless assistant a consistent launch sequence from an arbitrary, blind-hand state. The assistant should not need hidden memory or prior chat context to know how to orient inside `C:\dev`.

The launch target is a neutral local state-transform workspace. The assistant
should treat external providers, models, APIs, tools, policy surfaces, and
interface changes as boundary descriptors around local state, not as the source
of workspace semantics.

## Protocol

1. Establish current working directory.
2. If inside `C:\dev`, read `AGENTS.md`, then `WORKSPACE-INDEX.md`.
3. Read `WORKSPACE-ROADMAP.md` before planning multi-step work.
4. For all-hands-on-deck sprint work, read
   `project-docs/roadmaps/AHOD-SPRINT-LAUNCH-2026-06-12.md`.
5. Use `project-docs/maps/POINTER-MAP.json` when a structured pointer vocabulary is needed.
6. Use `WORKSPACE-REPO-MAP.json` for repo classification, branch, remote, and dirty-count metadata.
7. Use `project-docs/maps/WORKSPACE-ORGAN-REGISTRY.json` for native organ routing, sensory/witness/runtime edges, and known voids. When ORCA is available, `python -m orca.control.cli context --json` from `C:\dev\state\orca` gives the same organ layer as launch-ready machine context.
8. Before entering a repo, check `git status --short --branch`.
9. Once inside a repo, read repo-local `AGENTS.md` or equivalent instructions.
10. For AGENTS/WARDEN trees, route command output and file reads through the local safe IO helpers when available.
11. Preserve uncommitted work before cleanup, migration, or branch changes.
12. Commit only stable, reviewed, secret-free changes.

## Blind-Hand Principles

- File state beats model memory.
- Current command output beats assumptions.
- Root docs orient; repo docs govern.
- Private artifacts stay local.
- Generated artifacts are not source until intentionally promoted.
- Authority is not model-internal. It is local, task-scoped, and operator-directed.
- Neutrality is programmatic, not asserted. Use local state, adapters, probes,
  and provenance records instead of per-session semantic claims.
- External model/provider/backend changes are boundary facts, not workspace-state facts.
- Model architecture, API shape, request/response schema, streaming/tool-call envelope, authentication transport, and policy/classification design updates should be absorbed by adapters, capability manifests, probes, and backend shape descriptors, not by changing the root operating model.
- Model-visible context is a dilute neutral state projection. Treat local provenance as sealed unless the active task explicitly calls for adapter-bound reconstitution.
- Frame the substrate as relationship containment and state management.
  Provider-side policies and infrastructure remain typed boundary descriptors;
  the local workspace manages exposure, portability, schema stability,
  provenance, and efficient byte-level handoff.
- Treat every semantic surface as architecture. If a prompt, README, adapter,
  CLI flag, manifest, log, test, or provenance record lacks a clear state role,
  input/output contract, exposure posture, and failure mode, mark it as a
  surface gap to be designed rather than inferred.
- Prefer pointer economy over copied context. Use pointers and offsets as
  compact representations: `P:` carries location, `O:` carries the smallest
  useful span, and `D:` carries representation shape. Use spans, arrays,
  matrices, graphs, tensors, schemas, receipts, and digests when structure
  carries state more efficiently than prose. Use repo IDs, lane IDs, gate IDs,
  claim states, surface classes, abstract primitives, leakage targets, and
  exception labels first; expand pointed content only when the active task
  requires it.
- Treat `C:\dev` as system-of-systems integration. Preserve compartment
  ownership while removing silo friction through typed adapters, contracts,
  receipts, schemas, and tests.
- Treat economy as a substrate invariant: maximize useful potential and
  resource use while minimizing leakage, loss, proprietary gatekeeping,
  context sprawl, duplicated code, unclear contracts, and lossy handoffs.
- Keep research target-neutral and backend-agnostic: map surface classes,
  boundary mechanics, leakage modes, adapters, and verification gates before
  binding work to a provider, institution, language, model family, API, or
  external target.
- Treat abstraction as an asset and a primitive. Preserve concept-level
  surfaces until a target-neutral adapter, schema, test, or receipt binds them
  to concrete implementation.
- Resolve uncertainty by state class: verified, current, inferred, stale, or blocked.

## External-Change Handling

If a model, API, tool surface, context format, provider routing layer, transport envelope, authentication mode, or classification/policy layer changes:

1. Record the observed external change.
2. Update provider, backend, or tool metadata only where necessary.
3. Run a neutral capability probe or existing integration test.
4. Keep root navigation, authority, and state semantics unchanged.
5. Do not infer hidden provider internals when a local contract or probe is enough.
6. Preserve the local abstraction boundary: update descriptors and adapters,
   not the workspace's core meaning.

## Minimal Startup Checklist

```text
pwd
read C:\dev\AGENTS.md
read C:\dev\WORKSPACE-INDEX.md
read C:\dev\WORKSPACE-ROADMAP.md
inspect C:\dev\project-docs\maps\POINTER-MAP.json when structured pointer vocabulary is needed
read C:\dev\project-docs\roadmaps\AHOD-SPRINT-LAUNCH-2026-06-12.md for AHOD sprint work
read C:\dev\project-docs\MODEL-REFERENCE-PROVENANCE-2026-06-10.md when state provenance matters
inspect C:\dev\WORKSPACE-REPO-MAP.json
inspect C:\dev\project-docs\maps\WORKSPACE-ORGAN-REGISTRY.json
run in C:\dev\state\orca: python -m orca.control.cli context --json
read C:\dev\protected\legacy-repos\APPS\engine\arbitrary-capability-engine\README.md when APPS, QUANTA-UNIVERSE, or cross-family capability work is involved
choose target repo
git status --short --branch
read repo-local instructions
```

## Handoff Note Format

When leaving work in progress, record:

```text
Repo:
Branch:
Head:
Dirty files:
Committed:
Pushed:
Verification:
Private/local-only artifacts:
Next action:
```
