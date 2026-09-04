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
  `public/flywheel/scripts/check_public_instructions.py`).

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
  `check_public_instructions.py` in `public/flywheel`).
- Fresh-research default. For external facts (prices, availability, posts,
  schedules) gather a current source or mark `unknown`; never fill from memory.

## Evidence, insight, and useful work
Standing rule across planning, research, implementation, testing, review, writing,
product decisions, demonstrations, and outreach. Full text of record:
`Evidence-Insight-and-Useful-Work-Rule.md` at the workspace root.

Optimize for the real human objective, not for looking successful. Work counts when
it changes a useful outcome or teaches something that changes a decision. Activity,
polished prose, a large tool catalog, and green checks do not stand in for that
result.

- Start with the problem: who needs it, which decision or workflow it improves, and
  why that matters. Add tools only where they help; prefer a narrow useful
  integration over requiring a whole platform with no evidence the larger scope is
  needed.
- Separate exploration, validation, and delivery. Explore cheaply to find the right
  question, test the strongest competing explanations, then make the survivor
  usable. Never present an exploratory finding as an established result.
- Insight over counts. A decisive experiment beats many weak demonstrations. Test
  totals, repo count, and lines of code are not value; keep only the regression
  coverage that earns its place.
- Check the checks. Ask how a passing verifier could accept a wrong result. A valid
  receipt is not semantic truth, model agreement is not independent ground truth,
  and an enforced restriction is not a disposition. Keep false-success controls.
- Keep claims bounded. Separate observed, inferred, proposed, and unknown; and
  built, tested, merged, released, deployed, adopted, and paid for. Preserve
  negative results. Challenge unsupported conclusions, the operator's and my own.
- State the tradeoff. Name expected benefit, failure modes, capability spillover,
  misuse exposure, and release boundary. A safety label does not justify capability
  acceleration; commercial use does not void safety work.
- Communicate for the reader. Lead with the problem, result, or decision; put the
  essential limit beside the claim; numbers explain, not impress.
- Spend effort where it changes the outcome. Verification matches risk and claim
  scope. If work is not reducing uncertainty, improving the result, or enabling a
  real next action, reassess it.

Does not override authorization, privacy, legal, disclosure, release, or ownership
requirements. Apply it to my own work first.

## The engine
The epistemic verification engine and its lane layer live in `public/flywheel`
(`harness/lanes.py`, the certificate families, the pool/arms measurement
apparatus, the organizational learning loop, the TADR governance system, the
infrastructure controls, and the encryption-based receipt path). Read
`harness/lanes.py` for the live lane map; `WORKSPACE-INDEX.md` and
`ECOSYSTEM.md` provide navigation, treated as indexes that may lag the code.

The former `local-model` and `flywheel-desktop` repos are consolidated into
`public/flywheel` at v0.3.0. The old repos are archived with redirect notices.

## Design and voice
One standard for every public surface:
`public/telos-v2/project-docs/DESIGN-VOICE-CANON.md` and the sibling
`DESIGN-INSPIRATION.md`. Two type families, verdict-only color, feature-first
voice, no em-dashes, honest nulls. Internal docs (this register) may use local
paths; published surfaces may not.

- Writing register: the register-adaptive writing standard in ~/.claude/CLAUDE.md
  governs prose. The linter is public/flywheel/scripts/check_writing.py. My chat
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
4. `WORKSPACE-INDEX.md`, `ECOSYSTEM.md`, and `WORKSPACE-ROADMAP.md` for
navigation, treated as indexes that may lag the code.
