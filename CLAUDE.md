# CLAUDE.md — c:\dev workspace canon

> Model-facing. A Claude session rooted at `c:\dev` inherits this. `AGENTS.md`
> carries the same guidance for other harnesses; the two are kept in sync by
> hand. This is not inherited by a standalone project repo (each project is its
> own repo, cloned and operated on its own, and is self-contained); it is the
> workspace-session layer only.

**What this is.** The workspace layer a session rooted here inherits. Global
engineering standards live in `~/.claude/CLAUDE.md` and are inherited above this.
Each project is its own standalone repo with its own instructions. This is the
layer between the global standards and a project. Last verified: 2026-07-26.

## Inheritance
- `~/.claude/CLAUDE.md` — global standards (secrets, testing, voice). Inherited
  everywhere, not repeated here.
- `c:\dev\CLAUDE.md` / `AGENTS.md` — this canon, inherited by a session at the
  workspace root.
- `<repo>/CLAUDE.md` / `AGENTS.md` — SELF-CONTAINED. A project repo is cloned and
  operated on its own, so it cannot rely on inheriting this canon and does not
  point at it. Anything from here a project also needs is copied into that repo's
  own file, in that repo's own register (public repos stay public-clean; see
  `local-model/scripts/check_public_instructions.py`).

## The workspace, honestly
`c:\dev` is a local state-transform workspace: its job is vendor portability,
schema stability, and operator-owned provenance across nested repos, CLIs, model
routes, and research lanes. The container exists so tools and models are
replaceable materials. The boundary is portability, not provider-control evasion.
External model and provider behavior is a typed boundary fact — an adapter, a
probe, a receipt — never the design target.

## Model-neutral by default
Any model, local or endpoint, is a first-class but swappable material, and the
user chooses it. So:
- Do not assume a specific model, its context window, or its refusal profile.
- Keep task-irrelevant, high-salience tooling OUT of a directory's default
  context. Offensive-security rosters load where that work happens, not in
  general engineering or the epistemic-engine context. This is context hygiene,
  and it keeps a smaller model from tripping on content its task never needed.

## Verification discipline (the workspace method)
- Truth over approval. Verify a specific claim (grep, read, run) or label it:
  high / moderate / low / unknown. "Unknown" beats a plausible fabrication.
- No receipt, no accept. A measurement without its denominator, interval, and
  does-not-prove is instrument development, not a result. Honest nulls stay.
- No-drift gates over hand-transcription. Numbers and public copy are
  hash-tracked or gated, not trusted (`findings.py`, `check_claim_language.py`,
  `check_public_instructions.py` in `local-model`).
- Fresh-research default. For external facts (prices, availability, posts,
  schedules) gather a current source or mark `unknown`; never fill from memory.

## The engine
The epistemic verification engine and its lane layer live in `local-model`
(`harness/lanes.py`, the certificate families, the pool/arms measurement
apparatus). Read `harness/lanes.py` for the live lane map; `WORKSPACE-INDEX.md`
predates it and may lag.

## Design and voice
One standard for every public surface:
`public/telos-v2/project-docs/DESIGN-VOICE-CANON.md` and the sibling
`DESIGN-INSPIRATION.md`. Two type families, verdict-only color, feature-first
voice, no em-dashes, honest nulls. Internal docs (this register) may use local
paths; published surfaces may not.

- Writing register: the register-adaptive writing standard in ~/.claude/CLAUDE.md
  governs prose. The linter is local-model/scripts/check_writing.py. My chat
  prose to the operator uses the flavored `chat` profile: active voice, no
  em-dashes, no marketing words, calibrated uncertainty kept.

## Safety and hygiene
- Never commit `.env`, keys, tokens, browser profiles, local databases, or
  credential files. Verify before every commit.
- Do not publish `protected/`, `secrets/`, `state/*/warden-ops*`, or private
  runtime material.
- No production deploy without an explicit "yes, deploy". Preserve dirty work
  before cleanup; prefer ledger snapshots over deletion.
- Branch before committing to a default branch.

## Launch order (headless)
1. This canon. 2. The repo's own instructions. 3. `git status` before editing.
4. `WORKSPACE-INDEX.md` and `WORKSPACE-ROADMAP.md` for navigation, treated as
indexes that may lag the code.
