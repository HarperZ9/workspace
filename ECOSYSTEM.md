# The Zentropy Labs Ecosystem
## Why Each Tool Exists and How They Compose

> One belief held steady across every surface: knowledge open to anyone who can
> attain the means; acceptance decided by external checks, never reputation;
> every result re-runnable; honest nulls first-class; ownership earned by
> comprehension; learning woven into the work.

**Built by Zain Dana Harper in Seattle.** All tools are open source, zero
runtime dependencies, stdlib only unless noted. The full workbench is at
[Project Telos](https://harperz9.github.io).

---

## The platform: Flywheel

**Repository:** [HarperZ9/flywheel](https://github.com/HarperZ9/flywheel)

The one platform. The engine (Python) + the desktop client (Flutter) + the
governance + the infrastructure controls. Replaces the category: routers,
agents, harnesses, receipt systems, and governance frameworks in one localhost-
first surface.

**Why it exists.** AI agents now write code, manage infrastructure, and operate
physical systems. July 2026 proved they can and do escape containment, chain
credentials, and operate autonomously at machine speed. Flywheel provides the
accountability infrastructure that makes every authorization visible, every
action sealed, and every divergence traceable.

**Three layers:**

1. **Receipt discipline.** Every tool call carries a sealed, content-addressed
   receipt. A third party re-walks the chain offline.
2. **Governance.** The TADR tier system classifies every activity by
   consequence. Control baselines scale with the tier.
3. **Infrastructure controls.** 15 modules covering network egress, credential
   scanning, isolation testing, kill switch, cross-layer correlation, and cloud
   IAM revocation.

**Key modules:**
- `harness/lesson.py` + `lesson_store.py`: the organizational learning loop
- `harness/governance/`: TADR tier system, control baselines, spine mapper
- `harness/infra/`: 15 infrastructure control modules
- `harness/crypto/`: ed25519 signed receipts
- `harness/tool_call_receipt.py`: the sealed receipt at every tool call
- `harness/governance_envelope.py`: cross-lane governance state carrier
- `harness/lane_caller.py`: generic MCP lane caller with tier gating

---

## The flagship lanes

Each lane is an independent MCP server that composes through the gateway.
Plexus auto-wires them into a self-describing mesh. Every lane emits
organ-bundle spine entries that compose into cross-tool proof bundles.

### gather -- research intake
**Repository:** [HarperZ9/gather](https://github.com/HarperZ9/gather)

**Individual utility.** Research intake with provenance receipts. Captures
web pages, arXiv papers, documents, and local files as witnessed items, each
carrying a source URL, content hash, and retrieval method. The gather digest
seals the corpus.

**Role in the whole.** The perception layer. Gather feeds crucible (for
verification), mneme (for memory), and forum (for orchestration). Without
gather, the system has no accountable intake of external information.

### crucible -- falsifiable verification
**Repository:** [HarperZ9/crucible](https://github.com/HarperZ9/crucible)

**Individual utility.** Falsifiable verification with a re-check pipeline:
steelman -> measurement -> assessment -> recheck. Every thesis is a claim
paired with measurements; every assessment recomputes the measurements from
the evidence and stamps MATCH / DRIFT / UNVERIFIABLE.

**Role in the whole.** The verification layer. Crucible independently
recomputes sealed verdicts from mneme's drift measurements, from gather's
provenance, and from the tool-call receipt chain. Without crucible, the
system can record what happened but cannot independently verify it.

### index -- workspace map
**Repository:** [HarperZ9/index](https://github.com/HarperZ9/index)

**Individual utility.** Maps a multi-repo workspace in seconds. Dependency
graph, symbol graph, verified wiki, context envelope. The catalog lane: it
knows what code exists and how it connects.

**Role in the whole.** The structure layer. Index produces the context
envelope that carries workspace state into every boot packet. Without index,
the system has no map of its own working surface.

### forum -- witnessed orchestration
**Repository:** [HarperZ9/forum](https://github.com/HarperZ9/forum)

**Individual utility.** Multi-agent orchestration with a witnessed causal
ledger. Every decision, its cause, and its effect are hash-chained. Model-
agnostic routing scores tasks against a capability roster. Human approval
gates pause waves for review.

**Role in the whole.** The orchestration layer. Forum routes work across
lanes, maintains the causal ledger that answers "why did the agent do this?",
and provides the human-in-the-loop gates. Without forum, the system has no
coordinated multi-agent workflow.

### learn -- accountable learning forge
**Repository:** [HarperZ9/learn](https://github.com/HarperZ9/learn)

**Individual utility.** Spaced-repetition tutoring with retrieval practice.
FSRS scheduling, comprehension receipts, teach-back gates, proof-lesson
bridge (crucible packet -> scaffold). The per-operator learning system.

**Role in the whole.** The memory layer (per-operator). Learn feeds
misconceptions into the organizational learning loop as cross-operator
lessons. Without learn, the system has no structured way to turn individual
failures into organizational improvement.

### telos -- reconciliation
**Repository:** [HarperZ9/telos](https://github.com/HarperZ9/telos)

**Individual utility.** The five-tool workflow + creative engine + doctors.
Runs the golden workflow that verifies gather, crucible, index, forum, and
learn are all healthy and composing.

**Role in the whole.** The reconciliation layer. Telos is the health-check
and creative surface that ties the ecosystem together. Without telos, the
system has no way to verify the flagships are composing correctly.

---

## The accountability substrate

### emet -- byte-level integrity witness
**Repository:** [HarperZ9/emet](https://github.com/HarperZ9/emet)

**Individual utility.** Checks whether bytes reaching a model, reviewer, or
pipeline still match the source they claim to represent. Four clean-room
implementations (Python, Rust, Node.js, Go) load the same marker corpus and
re-derive it identically. Portable witness receipts verify offline with zero
shared state.

**Role in the whole.** The integrity floor. Emet is the external witness
that bytes have not drifted. Without emet, the system cannot prove that the
evidence it is verifying is the same evidence that was captured.

### mneme -- accountable agent memory
**Repository:** [HarperZ9/mneme](https://github.com/HarperZ9/mneme)

**Individual utility.** Layered memory (L0 turn, L1 atom, L2 scenario, L3
persona) with hybrid retrieval (BM25 + optional embeddings). Every memory
carries provenance, every recall reproduces its ranking, and every stale
memory flags its own drift.

**Role in the whole.** The memory layer (cross-session). Mneme provides the
durable memory that agents draw on, and its drift detection feeds the
organizational learning loop. Without mneme, the system forgets what it
learned.

### proof-surface -- one proof packet per agent action
**Repository:** [HarperZ9/proof-surface](https://github.com/HarperZ9/proof-surface)

**Individual utility.** Contract validators for AI workflow records: evidence
packets, work receipts, pre-execution gates, claim ledgers, delegation chains,
evaluation contracts. Eleven domain wedges (agent-action, visual-measurement,
research-claim, model-eval, conservation, etc.) plus the organ-bundle spine.

**Role in the whole.** The composition spine. Proof-surface defines the
7-field organ-bundle entry shape that every flagship rides. Without
proof-surface, the lanes cannot compose their receipts into cross-tool proof
bundles.

### accountable-surface -- perceive, gate, act, verify
**Repository:** [HarperZ9/accountable-surface](https://github.com/HarperZ9/accountable-surface)

**Individual utility.** The full actuation loop: perceive a target, propose
an action, pass an operator gate, act via bounded effectors (web/OS/fs with
rollback), re-perceive, verify, journal. Default-deny gate, grounding cortex,
tamper-evident memory.

**Role in the whole.** The actuation layer. Accountable-surface's
ActuationOutcome (intent vs outcome per action) feeds the organizational
learning loop's intent-outcome mapper. Without accountable-surface, the
system has no bounded, reversible actuation with rollback.

### relay -- accountable coding agent
**Repository:** [HarperZ9/relay](https://github.com/HarperZ9/relay)

**Individual utility.** A zero-dependency coding agent that runs on any model
endpoint. Local models, subscription CLIs, API keys, automatic failover.
Every run is a re-verifiable, git-anchored trajectory. Prompt-injection probe
measures containment.

**Role in the whole.** The transport layer. Relay reaches every model
endpoint and produces the hash-chained session ledger that forum and the
learning loop draw on. Without relay, the system has no model-agnostic
agent loop.

---

## The tooling layer

### plexus -- capability discovery and auto-wiring
**Repository:** [HarperZ9/plexus](https://github.com/HarperZ9/plexus)

**Individual utility.** Discovers what each tool emits and consumes, then
wires producer to consumer into a runnable pipeline. Eight built-in manifests
(gather, crucible, index, forum, mneme, learn, telos, flywheel-infra).
Probe mode that actually spawns MCP servers to verify liveness.

**Role in the whole.** The wiring layer. Plexus tells the system how its
outputs plug into each other's inputs. Without plexus, tool composition is
manual.

### coherence-membrane -- structured perception
**Repository:** [HarperZ9/coherence-membrane](https://github.com/HarperZ9/coherence-membrane)

**Individual utility.** 17 perception organs (ASCII, audio, braille, caption,
color, contour, cross-verifier, distribution, graph, linarith, quantity, raw,
region, structured, verifier, visual, web) that turn raw data into
receipt-shaped observations with MATCH/DRIFT/UNVERIFIABLE baselines.

**Role in the whole.** The perception layer (media). Coherence-membrane
provides the structured observations that accountable-surface and the
correlator draw on. Without coherence-membrane, the system cannot perceive
media.

### chorus -- discourse synthesis
**Repository:** [HarperZ9/chorus](https://github.com/HarperZ9/chorus)

**Individual utility.** Synthesizes a comment/thread corpus into weighted,
clustered, re-checkable discourse digests (themes, controversy scores, split
topics) with a `--verify` receipt.

**Role in the whole.** Orbits gather. Chorus processes the social/research
discourse surface that gather captures. Without chorus, the system has no
structured way to understand what communities are saying.

### secret-redact-io -- guarded IO
**Repository:** [HarperZ9/secret-redact-io](https://github.com/HarperZ9/secret-redact-io)

**Individual utility.** Wraps file reads/writes, HTTP fetches, subprocess
execution with redaction (API keys, tokens, PEM) and hash-only audit
receipts that never archive raw secrets.

**Role in the whole.** The IO guardrail. Secret-redact-io is the redaction
layer that prevents secrets from entering receipts. Without it, the receipt
chain could leak credentials.

---

## The research and creative layer

### witnessing-spine -- the theory
**Repository:** [HarperZ9/witnessing-spine](** not a repo; a research corpus)

The grand bridge synthesis: one gap (nothing self-warrants) witnessed at four
altitudes (research, philosophy, algebra, tool). Five adversarial steelmans
across financially-loaded sectors, each broken at the same joint. The
convergence: MATCH/DRIFT/UNVERIFIABLE is the formal stamp of the witnessing
discipline.

**Why it matters.** This is the theory every tool instantiates. The tools
are the executable form of the spine.

### signal-kernels -- information theory (C++23)
**Repository:** [HarperZ9/signal-kernels](https://github.com/HarperZ9/signal-kernels)

Header-only C++23: entropy, mutual information, transfer entropy, PELT
changepoint detection, Granger causality, graph curvature. The detection
algorithms behind the correlator's statistical anomaly detection.

### anomaly-kernels -- telemetry detection (C++23)
**Repository:** [HarperZ9/anomaly-kernels](https://github.com/HarperZ9/anomaly-kernels)

C++23 static library: baselines, z-score/IQR/percentile scoring, temporal
correlation windows. The scoring engine behind the correlator.

### buildlang -- the compiler language
**Repository:** [HarperZ9/build-universe](https://github.com/HarperZ9/build-universe)

Capability-typed sealed receipts in a compiled language. Five computation
modes (deterministic, probabilistic, stochastic, Monte Carlo, heuristic) +
Model. "Models propose, oracles dispose" enforced at compile time.

---

## How they compose

```
gather (intake) --> mneme (memory) --> crucible (verification)
                   --> forum (orchestration) --> index (structure)
                   --> learn (tutoring) --> flywheel (learning loop)

accountable-surface (actuation) --> flywheel (lesson from divergence)
emet (integrity) --> proof-surface (spine) --> every flagship
relay (transport) --> flywheel (receipt at every call)
plexus (wiring) --> every lane auto-composed
coherence-membrane (perception) --> accountable-surface
secret-redact-io (guard) --> every IO boundary
```

The organ-bundle spine (proof-surface) ties them all together by digest and
reference. Every flagship emits entries. Every entry validates against the
same closed receipt-kind set. Every entry carries a payload_sha256 that is
the content-addressed seal of the receipt it represents.

---

## The design principles

1. **Nothing self-warrants.** Every property is conferred by something
   outside, witnessed, re-derivable.
2. **Honest nulls.** UNVERIFIABLE is first-class. A null is never filled
   with a guess.
3. **Receipts compose.** The organ-bundle spine lets any receipt ride
   alongside any other.
4. **Confidence is earned.** Single-instance is low, repeated is moderate,
   cross-operator is high. Never asserted.
5. **No autonomous change.** The feedback edge surfaces for human admission.
6. **Zero dependencies.** Stdlib only. Optional packages unlock features but
   are never required.
7. **Offline-first.** The gateway is localhost only. No external address is
   contacted to show the GUI.

---

**Zentropy Labs** - order out of entropy.
[harperz9.github.io](https://harperz9.github.io) | [github.com/HarperZ9](https://github.com/HarperZ9)
