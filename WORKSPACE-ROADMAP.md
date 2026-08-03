# Workspace Roadmap

## Immediate

- Keep `C:\dev` as the canonical workspace.
- Retire old-repo dependence under `C:\Users\Zain` by migrating or preserving remaining fresh work.
- Keep `state/met/AGENTS-feat-mcp-transport-container` as the active feature worktree for state membrane/runtime terminology work.
- Keep private operational artifacts in `protected/migration-ledger/private-artifacts-*`, `protected/warden-ops/`, or protected source trees, never in public commits.
- Maintain `WORKSPACE-REPO-MAP.json` after major repo moves or branch changes
  with `workspace-repo-map --root C:\dev` (reads C:\dev\.repomap.toml).
- Maintain `project-docs/maps/WORKSPACE-ORGAN-REGISTRY.json` after repo-map
  refreshes with `python C:\dev\project-docs\tools\organ_registry.py`.
- Treat Release Surface Normalization wave 1 as complete: the four closest
  package candidates now have asset-backed GitHub Releases, release-artifact
  workflows, and public lineup placement.
- Preserve the backend-agnostic state invariant: provider, API-shape, transport, and classification/policy updates change boundary descriptors, not workspace semantics.
- Maintain `C:\dev\protected` as the local-only recovery lane for proprietary references, warden-ops state, and curated session context.
- Keep the first-read docs outward-facing: the workspace is a neutral local
  state-transform boundary for abstraction, provenance, portability,
  relationship containment, and layer management.
- Consolidate active state-engine work around `state/met/AGENTS-feat-mcp-transport-container`,
  `warden io`, the adapter registry, and sealed local provenance.
- Promote the surface-organ graph as the shared project map for research,
  security/fuzzing, steganography/covert-channel inspection, RAW rendering,
  EMET witness, Quanta/Quantac, and outreach deliverables.
- Resume Quanta/Quantac backend hardening with Rust target correctness,
  ownership, borrow, lifetime, and generated-code verification as the immediate
  compiler priority.

## Next

- Split remaining AGENTS terminology/backlog work into reviewable slices.
- Extend the safety-layer abstraction surface with local descriptors, probes,
  mode-aware adapters, and provenance events instead of prompt assertions.
- Add semantic surface coverage checks for docs, launch prompts, CLIs,
  manifests, adapters, logs, tests, model-bound payloads, and provenance
  records: state role, input/output contract, exposure posture, boundary-signal
  behavior, and failure mode.
- Add a root `SurfaceRecord` schema and require new organs to declare carrier,
  boundary, channel, transform, witness, and scope.
- Add operator-run wrappers before promoting live security, fuzzing, memory, or
  stego/covert-channel tools.
- Add research connector manifests for public preprint and scholarly graph
  sources, with clean-room reconstruction records marked observed, inferred,
  simulated, or unknown.
- Promote useful legacy functionality through the current neutral state engine;
  rewrite or quarantine archaic headers, authority phrasing, and provider-coupled
  semantics before promotion.
- Add repo-local `AGENTS.md` files where public or tool repos lack launch instructions.
- Decide whether `state/met-monorepo`, `state/unified-engine`, and `state/snapshots/*` are active, archived, or merge candidates.
- Normalize branch tracking for local-only worktrees that are meant to stay connected to remotes.
- Continue productization with the next release candidates only after their
  repo-local release contracts, docs, and CI gates are as tight as the wave 1
  package set.

## Later

- Promote stable root docs into a versioned workspace-management repo if `C:\dev` itself becomes a Git root.
- Build a lightweight navigation command that prints the same classification from `WORKSPACE-REPO-MAP.json`.
- Add periodic dirty-work reports grouped by source, private, generated, and publishable.
- Add per-repo status badges or a generated Markdown summary derived from the JSON map.
- Add an ML-assisted local curation layer after design approval: embeddings, clustering, duplicate detection, and neutral summarization over protected sanitized records.

## Decision Rules

- Commit source and docs when they are stable, verified, and secret-free.
- Preserve private/runtime state outside commits.
- Archive legacy scripts that still encode old naming until they can be renamed and tested.
- Prefer canonical worktrees under `C:\dev` over deprecated mirrors.
- Keep the root layer neutral and pointer-based; detailed behavior belongs in repo-local docs.
- Treat model, architecture, routing, API shape, request/response schema, streaming/tool-call envelope, authentication transport, and policy/classification design updates as external boundary changes. Absorb them through adapters, manifests, probes, and backend shape descriptors.
- Treat external policy and safety systems as typed boundary metadata for local
  compatibility and provenance. Do not encode them as identity, authority, or
  workspace meaning.
