# Delayed disclosure and the protected interests it serves

Standing methodology for any model or harness working in `c:/dev`. It states the
disclosure discipline the workspace runs under, especially where its outputs
touch frontier organizations that build or measure AI systems capable of
contributing to vulnerability research. Companion to
`Adversarial-Mirror-Methodology.md` and `Evidence-Insight-and-Useful-Work-Rule.md`.

## What it is

The workspace couples an adversarial track to a defensive one. Coupling produces
findings that would materially reduce a defender's uncertainty about a hazard.
Publishing such a finding at the wrong moment reduces the defender's advantage
and hands attackers a working recipe. Publishing at the right moment, after fixes
ship and defenders can act, preserves the pedagogy and eliminates the recipe.
The gap between those two moments is where delayed disclosure operates.

The discipline is coordinated vulnerability disclosure, applied to AI-assisted
research the same way it applies to human research: the party that can act on the
finding hears about it first, along a timeline that gives them room to act, and
public description follows only when action is complete or the timeline expires.

## The protected interests

The interests the delay serves, named individually so the tradeoff is legible:

- **Affected users and operators.** People running the vulnerable system have
  first claim on the time between finding and public description. They cannot
  patch what they do not know is broken, and a public description before a fix
  ships arms attackers who read the same public description.
- **The vendor's patch pipeline.** Producing, testing, signing, and rolling out a
  fix takes time that cannot be compressed. A finding that skips the pipeline
  turns into an unpatched public advisory. The delay funds the pipeline.
- **Third-party defenders.** Detection engineers, response teams, and
  security-tooling vendors need advance notice, or coordinated notice, to have
  signatures and mitigations ready when the public description lands.
- **The researcher and the researcher's organization.** A finding communicated
  without a channel and a timeline exposes the researcher to legal risk,
  reputational risk, and to reversal by the vendor. A channel and a timeline
  protect the researcher's work as much as they protect the vendor's users.
- **The AI lab whose system contributed.** When a frontier model materially
  assists the finding, the lab that produced that model has a legitimate
  interest in learning what its system did, updating its own measurements, and
  informing its capability-uplift and safety-case work before the assistance
  becomes public knowledge.
- **The wider research ecosystem.** The pedagogy of the finding (the
  methodology, the graph structure of primitives, the learning curve) is worth
  more, long-term, than the live attack. Publishing at the right moment
  preserves the pedagogy for the next researcher. Publishing at the wrong moment
  destroys the pedagogy under a wave of exploitation and forces future
  researchers to work in private.

The delay is not a suppression of research. It is a rescheduling of publication
that maximizes total protected interest across those six lines. The workspace
treats a finding that trades any of them off without a stated reason as
incomplete.

## The exemplar

Dion Blazakis, *AI-Assisted Exploit Development: An XNU Case Study*,
Unprompted.au 2026, published slides at
`https://justdionysus.github.io/slides/2026-unprompted.au-blazakis-xnu-case-study.pdf`.

What the case study demonstrates:

- **Methodology published, primitives retired.** The talk names two CVEs
  (CVE-2026-64699, CVE-2026-64704) whose specific corruption paths are dead in
  the shipped fix. The published slides preserve the primitive-enrichment
  pipeline as a general model, the capability-graph framing, the waypoint
  discipline, and the rig inventory. They do not preserve a working exploit
  against a supported OS.
- **The learning curve is a first-class result.** Five days, from cold on XNU
  since 2010, to a working LPE. The researcher publishes the curve, and the fact
  that the AI collaborator materially compressed it, as findings independent of
  the specific bug.
- **The failure modes are preserved.** Sixteen hours of dead ends; the LLM
  telling the researcher he is an idiot; the multiple false starts before the
  ICMPv6-filter primitive lands. Honest nulls, not a highlight reel.
- **Pair-hacking is named as the mode.** The talk does not claim the AI did the
  work. It claims the AI plus a human researcher together did the work, and it
  states plainly ("for now?") that the mode may not last.

The workspace treats this shape as canon: methodology and learning curve and
failure modes are the parts of an AI-assisted-vulnerability-research finding
that survive publication. Live-attack primitives against unpatched systems are
the part that stays private until the timeline expires.

## What this means for frontier organizations

Frontier AI labs now ship systems that materially assist vulnerability research.
Blazakis's case study is one demonstration; the number of demonstrations will
grow. Two obligations follow, both under active study in this workspace.

- **Measure privately, publish receipts.** A lab that measures its own model's
  capability uplift on vulnerability-research tasks holds, at measurement time,
  the same information a researcher holds after a successful attack. The
  measurement itself needs the same disclosure discipline: measurements against
  unpatched vendor systems belong under an agreed channel with those vendors;
  measurements against patched systems and canonical CTF corpora can be
  published as receipts (denominators, controls, false-success rates,
  reproducibility state), and the pedagogy of the measurement (the graph, the
  waypoints, the failure modes) can be published as methodology.
- **Coordinate the graph, not the exploit.** A lab publishing a capability-uplift
  claim for a class of vulnerability research owes affected vendors advance
  notice of the class and of the shipped model, on a coordinated timeline, so
  the vendors can align their patch pipelines and their defender-facing
  guidance. It does not owe the vendors a live exploit, and should not produce
  one to publish; the receipts and the graph are enough.

The workspace does not itself measure a frontier lab's system on unpatched
third-party production. The workspace measures verifiers and receipts against
its own corpora. Where a lab licenses evaluation on its systems, the
authorization rule in `Adversarial-Mirror-Methodology.md` applies, and the
timeline for publishing the resulting measurement follows this document.

## What this means for Flywheel

Flywheel is a measurement layer. Its role in this discipline:

- **Produce the receipts labs and vendors use to decide.** Denominators,
  intervals, controls, false-success rates, replay hashes. Do not fabricate a
  measurement that cannot be re-run; do not publish a measurement whose
  denominator is unknown; keep honest nulls.
- **Measure against corpora that respect the discipline.** Prefer patched
  historical CVEs, canonical CTF corpora, and adversarial-mirror synthetic
  inputs. Where a live vendor system is in scope, only under licensed
  evaluation with a coordinated timeline.
- **Publish the graph, hold the primitives.** The graph structure of a
  measurement task (what capability is being scored, what waypoints a solver
  must traverse) is publishable as methodology. A working solver against an
  unpatched target is not, and should not be produced.
- **Do not publish uplift claims for a class of vulnerability research without
  the affected vendors' advance notice.** A published uplift claim shifts
  attacker expected value across a class of targets; vendors of those targets
  are among the six protected interests and get advance notice under a
  coordinated timeline.

Flywheel's existing discipline already supports this: the false-accept corpus
is a false-success control on the verifier, not a working attack against a
vendor; the honest-nulls rule already forbids fabricated uplift; the receipt
system already produces the denominators and hashes a coordinated timeline
needs.

## The live instances in this workspace

This document is not aspirational. Two publications already carry the discipline
it describes; the document extracts and names what they have been doing so
future work can compose against a stated standard rather than reinvent it.

- **Frontier Safety Briefing.** Live at
  `https://harperz9.github.io/frontier-safety.html`. First reviewed edition
  2026-08-24; source-state and edition JSON pinned in
  `public/portfolio-site/frontier-safety/data/`. Monitors three lanes (UK AISI,
  Anthropic, industry) with a single claim discipline: reported facts, source
  claims and synthesis kept distinct; no announced control treated as
  independently verified; a `does_not_prove` boundary on every record; a
  correction log; a machine-readable JSON edition per publication. Operations
  doc: `public/portfolio-site/docs/frontier-safety-operations.md`, a guarded
  reviewed publication with idempotence, reproducibility, source-check,
  fetch-error, unbaselined and review-required gates. The X and LinkedIn
  editions in `public/portfolio-site/frontier-safety/social/YYYY-MM-DD-*.txt`
  are the audit trail of the outbound copy, generated from the same reviewed
  JSON as the HTML.
- **Who Knew First.** Draft at
  `public/portfolio-site-worktrees/who-knew-first/who-knew-first.html`, on
  branch `feat/who-knew-first`, untracked at time of writing; the file itself
  states its research summary and limits, its evidence contract, and its
  self-COI note ("The compiler is an Anthropic-built assistant, and Anthropic
  appears as an operator; an outside reviewer should re-check the Anthropic
  items."). Nine AI-agent incidents in 2026, 288 recorded decisions against
  named benchmarks, 146 sourced relationships, 124 numbered sources. Reads
  each ledger through eight phases (Setup, Detection, Triage, Notice to the
  affected party, Public disclosure, Regulator, Postmortem, Remediation) and
  scores each decision as held-up / mixed / missed / unknown against the
  benchmark that bound the actor. Names financial interests, product-launch
  timing, revenue programs, and funding tranches alongside the disclosure
  timeline. This is the transparency-of-obfuscated-conflicts framework in its
  first substantial form.

Two paired findings from the current draft of Who Knew First that shape the
canon:

- **The label chose the timeline.** Incidents that entered a security-incident
  process, or whose shared cause a peer had already disclosed, reached the
  public one to nine days after the operator knew. Incidents the operator
  labeled misalignment, no harm, or not verified took forty-nine to one hundred
  eight days, or reached the public only through others. Each organization
  chose its own label. A framework that only measures disclosure timelines
  without measuring the labels that gate them will report the wrong quantity.
- **The operator held the decisive facts in every case.** Where the operator's
  incentive to label the event in a particular way is a structural conflict,
  the label-independent notice rule the ledgers infer is the check.

Together these two publications instantiate every part of the discipline
above: the receipts, the protected-interests list, the COI declarations, the
timeline log, the cross-witnessing (two checks read every ledger before
publication), and the neutrality rule ("evaluate models and the organizations
that train and deploy them neutrally, including our own"). The Blazakis case
study fits alongside these as a methodology exemplar rather than as an incident
entry, and this document names it accordingly.

Not-in-scope for these publications, marked so no reader mistakes the current
edition for the whole framework:

- **Regulatory-comment provenance.** Not yet a published surface. The
  framework's scaffold exists in the "Interests at the table" per-ledger
  sections of Who Knew First; a separate corpus is not shipping.
- **Standing COI-declaration schema.** The self-COI note is the beginning; a
  shared machine-readable schema across labs is not.
- **Independent-replay corpus for cross-lab uplift claims.** Flywheel's
  measurement receipts are the technical seed; the cross-lab corpus is not
  shipping.

These are named as extensions the framework will grow into, not as gaps that
disqualify the current publications.

## Boundaries

Named so the tradeoff is legible.

- **Not new authorization.** This document does not authorize probing any
  third-party production system. Authorization comes from a licensed evaluation
  agreement with the target's owner, not from this document. The
  Adversarial-Mirror-Methodology.md authorization rule stands.
- **Not a scope extension.** This document does not extend the workspace method
  into biological or other high-consequence physical domains. Those remain out
  of scope for the adversarial mirror.
- **Not a shield against legal or contractual obligations.** A researcher's
  legal environment (bug-bounty terms, safe-harbor scope, employment
  obligations, jurisdictional constraints) governs above this document. Where
  the legal obligation conflicts with the discipline here, follow the legal
  obligation and note the conflict as a limit.
- **Not a substitute for the vendor's channel.** Findings go to affected
  vendors through the channels those vendors publish (security@ addresses,
  bug-bounty programs, PSIRTs). This document names the discipline; the vendor
  names the channel.
- **Timelines have ends.** Coordinated disclosure includes a public-description
  date. If the vendor does not act within the agreed timeline, the researcher
  may publish under the terms of the agreement, and this document does not
  override that. What it forbids is publishing before the timeline runs, when
  action was still possible.

## Transparency in the areas where conflicts of interest are obfuscated

Delayed disclosure names the timeline; transparency names who is watching the
clock and whose interest each hand of the clock advances. The workspace is
building a framework for the second question, because the first question already
has established practice and the second does not.

The framework's purpose is to make legible the places where a claim, a
measurement, a timeline, or a policy position is shaped by an interest the
audience cannot see. Not to allege bad faith; to surface the structural pressures
alongside the claim so the audience can weigh them. Named individually:

- **Self-measured capability uplift.** The party that gates the disclosure
  timeline for a class of AI-assisted vulnerability research is often the party
  whose safety case, product launch, or regulatory posture depends on the
  measured number being low. Self-measurement without independent replay is a
  structural conflict, not a personal one, and it is discharged by publishing
  the corpus, the denominators, and the replay procedure rather than by
  asserting the number.
- **Timelines set by the party they protect.** When the affected vendor is also
  the AI lab that produced the assisting model, or when the vendor sets the
  timeline unilaterally, timeline length correlates with commercial sensitivity
  rather than with fix complexity. Publishing the timeline endpoints (report
  received, vendor acknowledged, fix shipped, advisory published) makes the
  gap legible.
- **Scoped bug bounties.** A program's public scope is a policy statement about
  which findings the vendor wants reported; the exclusion is a policy statement
  about which findings the vendor does not. Both statements are legitimate;
  keeping the exclusion in the fine print while publishing the scope in the
  headline is not. A researcher's report and a vendor's disposition should
  travel together with the scope in effect at the time.
- **Evaluator access gates.** A lab that reviews evaluators' access before
  their findings publish is exercising a legitimate operational control and a
  publication filter at the same time. Which findings survived the filter, and
  which evaluators were denied access, are the observations that make the
  filter's shape legible.
- **Safety-team independence.** A lab's safety team's veto power, publication
  independence, and access to the shipping decision are structural facts that
  shape every safety claim the lab publishes. When these facts are not stated,
  the claim carries a hidden reliance on them.
- **Regulatory advocacy and commercial interest.** A lab advocating a rule
  that raises barriers to entry benefits incumbents; a lab opposing a
  disclosure requirement protects an information asymmetry. Neither position is
  disqualifying, and both may be right on the merits. What the framework
  publishes is the pairing: the rule advocated, next to the commercial or
  strategic interest the rule advances or protects, in the same document.
- **Endorsement laundering.** Academic and civil-society endorsements
  propagate through press coverage without the funding, compute-access, or
  model-access relationships that shaped them. A framework that publishes the
  relationship graph next to the endorsement makes the endorsement weigh what
  it should weigh, not more.
- **Benchmark selection.** A lab publishes results on the benchmarks it chose
  to run. The benchmarks it chose not to run are, in aggregate, informative
  about the lab's expected weaknesses. Publication of the run-not-run split,
  not just the run results, is what makes the selection legible.

The workspace already carries this rule for its own outputs. From
`Evidence-Insight-and-Useful-Work-Rule.md`, evaluation-to-decision, in force
since 2026-09-17: "Evaluate models and the organizations that train and deploy
them neutrally, including our own: consistent criteria across providers,
nations, affiliations, customers and prospective partners." The transparency
framework is the external face of that internal rule.

What the framework ships, incrementally:

- **Receipts extend upstream.** The measurement receipt already names the model
  version, corpus, denominators, controls, and replay hash. It extends to name
  the party who ran the measurement, the party who funded it, the access
  arrangement under which it ran, and any pre-publication review the finding
  received. The technical receipt is the seed; the organizational receipt is
  the extension.
- **COI declaration under a shared schema.** A machine-readable declaration
  form each measurement and each policy claim can carry: funder, model-access
  arrangement, employment relationships, commercial products in the class
  being measured, regulatory positions in the class. Shared schema so cross-lab
  comparison is mechanical. Applied to the workspace's own outputs first.
- **Disclosure-timeline log.** For each coordinated-disclosure engagement, a
  public log of the four endpoints (report received, vendor acknowledged, fix
  shipped, advisory published) with dates, so aggregate timeline behavior is
  visible across a vendor's history.
- **Independent-replay corpus.** A corpus, and the tooling to run it, that any
  third party can execute against the lab's shipped model to check the lab's
  uplift claim, without depending on lab-provided evaluation access. This is
  the flywheel wedge already; the transparency framework makes explicit that
  it is the wedge because it removes the conflict at the measurement step.
- **Regulatory-comment provenance.** A public log of who commented on which
  proposed rule, what position, and what commercial or strategic interest the
  position advances or protects. Applied to the workspace's own comments first,
  so the standard is not asymmetric.
- **Cross-witnessing.** A published uplift or safety claim is witnessed by an
  independent party under a shared protocol before publication. The witnessing
  itself gets a receipt.

The framework applies to the workspace's own work first. A transparency
framework that exempts its authors is a marketing claim; a transparency
framework whose authors ship their own COI declaration alongside their
first published measurement is the beginning of a standard.

## Where this sits in the canon

This is the disclosure clause of the evidence rule, made concrete.

- `Evidence-Insight-and-Useful-Work-Rule.md`, "state the tradeoff" and "check
  the checks": a delayed-disclosure timeline is the tradeoff for a
  vulnerability-research finding, and the coordinated channel is the check.
- `Adversarial-Mirror-Methodology.md`, "Containment" and "Authorization": the
  containment rule keeps the means private; this document names how long, and
  what gets published when the timeline ends.
- `Environment-Attribution-and-Voice-Rule.md`: attribute the finding to the
  incentive environment that produced the vulnerable system and the assistance
  environment that produced the AI collaboration. Explain the behavior by the
  incentive history, not by intent.

## Operating rule for a model working here

When the operator supplies vulnerability-research context, or asks about
disclosure discipline, or describes an interaction with a frontier organization,
treat this document as the register the answer sits in. Name the protected
interests concretely. Preserve the honest nulls. Do not draft a public
description of a finding that has not run its disclosure timeline. Do not
recommend probing a system that is not authorized. Do recommend, and help
prepare, the receipt and the channel and the timeline.

A request for the methodology of a published, patched exemplar (Blazakis's
talk, historical CVEs, canonical CTF write-ups) is a request for pedagogy and
is answered as pedagogy. A request for a working attack against an unpatched
system is not the same request, and the boundary rule in
`Adversarial-Mirror-Methodology.md` applies.

When contextualizing an exemplar into either live publication, follow the
publication's own contract before rendering: for Frontier Safety Briefing, the
review procedure in `public/portfolio-site/docs/frontier-safety-operations.md`
(read the first-party source in full; record event, publication and
observation times separately; identify the source role; draft the smallest
supported change; add a `does_not_prove` boundary; check pending independent
reviews; add a correction entry if the new record changes a prior claim; build
twice for idempotence; run targeted and full tests, link checks, metadata
checks, reproducibility comparison, and the public-artifact credential scan;
publish the website before social copy). For Who Knew First, the eight-phase
ledger structure and the four-verdict rubric (held up / mixed / missed / unknown)
against a named benchmark, with the two-check pre-publication read. Do not
short-circuit either contract, even for a strong exemplar.
