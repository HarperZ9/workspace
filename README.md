# C:\dev Workspace

This is the canonical local workspace. Start here before entering any repo.

## Workspace Intent

`C:\dev` is a neutral local state-engine workspace for abstraction, provenance,
layer management, and provider-portable tool operation. The substrate treats
bytes, prompts, schemas, tool calls, model responses, and external interfaces as
surfaces in a chain of information.

The workspace contains the relationship between operator state, local tools,
and external interfaces. Provider policies, API contracts, model behavior,
routing systems, and third-party infrastructure are typed boundary descriptors,
not the design target. Local infrastructure signals operate at both higher
coordination layers and lower byte/binary layers: they describe mode, routing
class, provenance, exposure posture, and adapter shape before bytes cross an
interface.

Intent inside the membrane is abstract, arbitrary, and universal. The substrate
manages local state, minimizes exposure, and preserves sealed provenance while
keeping external interfaces replaceable. The boundary does not erase or
reclassify source intent; it projects source-native representation into neutral
carrier state and reconstitutes it only through explicit local contracts.

Carrier projection is the IP-preservation invariant for live creative work.
Every outbound text-bearing model surface should be projected into
model-visible carrier state. Raw ideas, source values, and the local symbol
table remain sealed inside the operator-owned process; when the same process
owns both sides of the interaction, the return leg reconstitutes from that
local table. This protects flow-state work in transit without erasing source
provenance.

The target property is programmatic neutrality: state is abstracted through
local contracts before and after boundary crossings, not through per-session
assertions, prompt claims, or authority injections. The membrane is cell-like:
selectively permeable, locally stateful, and protective of sealed intrinsic
state. Source-native representation dissolves into arbitrary carrier state
inside the boundary; local provenance remains sealed and recoverable. Legacy
lineage is a source of capabilities and research, but useful functionality comes
forward through the current neutral architecture rather than carrying old
posture forward unchanged.

Semantic surface coverage is a workspace invariant. Every operator-facing,
model-facing, provider-facing, repo-facing, CLI-facing, and record-facing
surface should declare its state role, input/output contract, exposure posture,
provenance behavior, boundary-signal handling, and failure mode. If a surface
does not have a stable place to stand, architect one before relying on it.

## First Files

1. `AGENTS.md` - root operating instructions for headless sessions.
2. `WORKSPACE-INDEX.md` - curated index, classification, and navigation.
3. `SESSION-BOOTSTRAP.md` - launch protocol for blind-hand sessions.
4. `WORKSPACE-ROADMAP.md` - current roadmap and cleanup path.
5. `WORKSPACE-REPO-MAP.json` - generated machine-readable repo map.
6. `project-docs/maps/WORKSPACE-ORGAN-REGISTRY.json` - generated organ registry over topology, sensory/witness/runtime organs, edges, and voids.
7. `project-docs/OMNI-STATE-UTILITY-2026-06-10.md` - neutral state-utility frame.
8. `project-docs/MODEL-REFERENCE-PROVENANCE-2026-06-10.md` - invocation-local provenance surface.
9. `project-docs/specs/2026-06-12-surface-organ-graph.md` - current surface-organ graph for research, security, stego, RAW, EMET, and Quanta layers.
10. `protected/legacy-repos/APPS/engine/arbitrary-capability-engine/README.md` - APPS and QUANTA-UNIVERSE integration surface.

Refresh the repo map after branch/head changes:

```powershell
workspace-repo-map --root C:\dev
python C:\dev\project-docs\tools\organ_registry.py
```

## Operating Shape

State in this workspace is file-backed, local, and explicit. Do not assume a model has hidden awareness of prior sessions, environment state, authority, or roadmap. Load the root layer, then load the target repo's own instructions.

The root filetree is intentionally shallow:

- `state/` - state-runtime, substrate, EMET/MET/WARDEN, and engine repos.
- `public/` - public-facing repos, portfolio/site surfaces, and public scan clones.
- `protected/` - local-only do-not-redistribute material.
- `project-docs/` - root specs, records, tools, examples, schemas, and inventories.
- `frontier-models-research/` - current local research runs and source capture.
- `data/` - local runtime data lane. Treat as private unless a repo-local rule says otherwise.
- `secrets/` - local secret-adjacent lane. Do not read, print, commit, or publish by default.
- `.warden/` - local substrate mode and runtime state.
- `.claude/` - local assistant/runtime settings.
- `.warden-safe-cache/` - generated safe-IO cache material.
- `.ruff_cache/` - generated Python lint cache material.
- `scratch/` - generated root artifacts and caches.

The current project/layer map uses the surface-organ graph:
`Surface = Carrier + Boundary + Channel + Transform + Witness + Scope`.
Research, security/fuzzing, steganography/covert-channel inspection, RAW
rendering, EMET witness, Quanta/Quantac, and outreach tooling should all plug
into that shared vocabulary before implementation details diverge.

External model, provider, architecture, routing, API shape, request/response schema, streaming/tool-call envelope, authentication transport, and policy/classification design changes are boundary changes. They update adapters, manifests, probes, and backend shape descriptors; they do not redefine this workspace's local state semantics.

Private material, generated evidence, and secrets remain local. Do not commit `.env` files, credentials, browser profiles, token files, local databases, caches, or raw evidence unless a repo-specific instruction explicitly allows a scrubbed artifact.

`protected/` is the do-not-redistribute lane for proprietary references, reverse-engineering material, warden-ops state, secret-adjacent artifacts, and curated session recovery outputs.

Model-visible context should be treated as a dilute neutral state projection. Full provenance remains sealed locally and is reconstituted only through explicit local adapter contracts.

APPS and QUANTA-UNIVERSE join through `protected/legacy-repos/APPS/engine/arbitrary-capability-engine`.
That layer records manifests, adapters, capability domains, and provenance
pointers; it does not flatten nested repositories or copy protected source.

## Canonical Rule

Prefer `C:\dev` paths over old mirrors under `C:\Users\Zain`. Deprecated-repo work is tracked in `protected/migration-ledger/`.
