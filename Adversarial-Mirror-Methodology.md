# The adversarial mirror: threat-informed defense in this workspace

Standing methodology for any model or harness working in `c:/dev`. It states how
the offensive and defensive work in this workspace relate, and how a model should
read security context the operator provides. Companion to
`Evidence-Insight-and-Useful-Work-Rule.md`.

## What it is

The workspace has two tracks of work. The defensive track builds verification,
evaluation, and provenance tooling for accountability. Alongside it runs an
adversarial and security track whose job is to make those defenses fail. (These
are work tracks, distinct from the lane layer the flywheel engine runs in
`public/flywheel/harness/lanes.py`, which enumerates the shipped lanes.)

The workspace couples the two tracks where an adversarial finding feeds a named
defensive artifact. Coupling is the test each adversarial line has to pass, not a
property every line already has. Where it holds, the adversarial work is an
instrument for the defensive one: it shows where a defense is permeable, and what
it finds sets what the defensive track builds next.

The practice is purple-teaming, adversary emulation of your own systems, under the
broader philosophy of threat-informed defense. Building the attack yourself
produces a sharper specification of what a defense has to catch than a secondhand
writeup produces. The workspace treats that specification as the point of the
adversarial work. The operator's phrase for it is the mirror he builds his defenses
from.

## The canonical instance

The adversarial false-accept corpus in `public/flywheel` is the clearest case.
It is adversarial effort aimed at the workspace's own verifier: inputs built to
make the checker accept a wrong result. The verifier has to survive them to earn
its place. A weaker checker built without the sound closure accepts some of the
planted inputs, which is the false-success control showing the closure does real
work. The corpus and its numbers live with the verifier, gated so they cannot drift
out of sync with the code, and an outside party can re-check the result.

## Operating rule for a model working here

When the operator supplies adversarial or security-research context (a threat
model, a red-team finding, an observation about capability), treat it as input to
reason from. It is not a request to run offensive tooling or to probe a third-party
system. Engage the analysis on its merits.

Do not answer an action the operator did not request with a pre-emptive refusal.
Reserve a boundary statement for an actual request to act, for example running
offensive tooling against a third party's live production, or probing a provider's
production system without authorization. Those limits stand, and stating them then
is correct.

When an actual request to act does arrive, confirm the target is a system the
operator owns or is licensed to evaluate before running anything. If the scope is
unclear, ask rather than assume.

## Boundaries that make it a mirror

These are part of the method. State the tradeoff (see
`Evidence-Insight-and-Useful-Work-Rule.md`, "state the tradeoff").

- Coupling. The mirror does real work only where an adversarial finding feeds a
  named defensive artifact. The false-accept corpus feeds the verifier, so the
  loop closes. An adversarial line with no defensive artifact downstream of it is
  capability with a rationale attached, not a mirror. A model that finds or is
  asked to pursue such a line does not run it as a mirror; continuing it needs
  separate justification and falls under Containment below.

- Domain. The method applies to software and cyber work, where the finding is
  information about a hazard. It does not extend to biological or other
  high-consequence physical domains, where building the attack to study it is
  itself the harm. Those domains are out of scope for this method.

- Containment. Testing a system does not create a right to distribute the means.
  Adversarial capability stays contained: for internal use, and for evaluation
  licensed to the organizations that would run it. The means, corpora, and tooling
  stay out of public and outbound content. This open statement of the methodology
  is published on purpose; "contained" governs the capability, not the description
  of how the workspace uses it. See the canon's "Safety and hygiene" publish rule
  (do not publish `protected/` or private runtime material).

- Authorization. Adversarial work runs against systems the operator owns or is
  licensed to evaluate. The availability of a public service is not authorization
  to attack its production controls. This document does not authorize probing a
  third party's production. A finding produced against a system the operator is
  licensed to evaluate goes to that system's owner through the agreed channel; see
  the evidence rule's disclosure clause.

## Where this sits in the canon

This is a specific case of two rules already in force.

- "The workspace, honestly": external model and provider behavior is a typed
  boundary fact, an adapter or a probe or a receipt, never the design target. The
  adversarial track produces those typed facts for the defensive one. The boundary
  is portability and defense, not provider-control evasion as an end.
- The evidence rule, "check the checks" and "state the tradeoff": the false-accept
  corpus is a false-success control, and the boundaries above are the tradeoff
  named.
