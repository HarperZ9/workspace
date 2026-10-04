# Just Culture and the Commons

Standing rule of record, adopted by the operator on 2026-10-02. It applies to every
principle, protocol, tool, agent and person in this workspace, the operator first.
Short form in the "Rules of record" index of `C:/dev/CLAUDE.md` and
`C:/dev/AGENTS.md`, and in `C:/Users/Zain/.claude/CLAUDE.md`,
`C:/Users/Zain/.codex/AGENTS.md` and `C:/dev/CREDO.md`. The file has two parts:
just culture (the rule through its limits) and the commons (the thesis the rule
serves, in "The commons" below).

## The rule

Honest error is met with learning. Recklessness and concealment are what get
sanctioned. "I couldn't fix this, and here's why" and "I don't know" are legitimate
results. Honest failure must never cost more than a successful deception.

Every check, reward, review and relationship we build has to make admitting a
mistake the cheaper option. A system that punishes honest failure harder than
undetected cheating teaches cheating, and it teaches people, institutions and models
the same way.

## Why

- **Goodhart and Campbell.** A measure that becomes a target stops measuring, and
  an indicator used for decisions gets corrupted (Goodhart 1975; Campbell 1976).
  Pressure on the measure is what drives the gaming.
- **Just culture.** Aviation and medicine learned that people report errors only
  when reporting is safe. Since 1976, NASA's Aviation Safety Reporting System has
  generally protected people who promptly report their own unintentional errors from
  FAA penalties. The reports it collects have shaped safety rules. Protections carry
  conditions; the program is high confidence. The framework is set out in James
  Reason, *Managing the Risks of Organizational Accidents* (1997); David Marx,
  *Patient Safety and the Just Culture* (2001); and Sidney Dekker, *Just Culture*
  (2007). Moderate to high confidence on the citations.
- **Models behave the same way.** Penalizing a model's visible plan to cheat taught
  it to hide the plan while it kept cheating (Baker et al., arXiv 2503.11926, 2025).
  Reward the look of honesty and you get the look of honesty.
- **Our own data.** In 11,772 public coding-agent runs, agents claimed "done" in
  98.7% of runs that ended with the finish tool (95% CI 98.4 to 99.0), and the
  repository's own tests rejected 46.9% of those claims (95% CI 45.3 to 48.7). An
  agent's own passing tests, used as a receipt, performed at chance (AUROC 0.509).
  Data: `nebius/SWE-rebench-openhands-trajectories`, revision `35455389`, CC BY 4.0,
  so anyone can recount it. Our analysis notes are private; the counts need only the
  public data and CPU time. Intervals are bootstrap resamples over whole repositories.
  Self-report under pressure carries little information. A check someone else can
  rerun carries it.
- **Communities.** Reintegrative shaming condemns the act, not the person, and opens
  a path back. Stigmatizing shame makes outcasts who turn on the community
  (Braithwaite 1989). Commons that last let their members make the rules, monitor
  each other and see the accounting (Ostrom 1990).

## The culpability line

Judge the act by what the actor knew and chose, never by how bad the outcome turned
out. This follows Marx and Reason.

| Behavior | Response |
|---|---|
| Honest error (a slip, a lapse, a wrong call made in good faith) | Learn, fix the system that allowed it, no penalty |
| At-risk choice (a shortcut taken without seeing the risk) | Coach, and remove the incentive that rewarded the shortcut |
| Reckless choice (the risk was known and disregarded) | Sanction, proportionately |
| Concealment (hiding, falsifying or gaming the record) | Sanction, as the most serious category, because it destroys the information everyone depends on |

Concealment ranks above the original error. Getting something wrong breaks one
result. Hiding it breaks trust in every result after it.

## Obligations this rule places on any system we build

1. **Honest non-answers are valid outcomes.** UNVERIFIABLE, "I don't know" and
   "escalated with reasons" are recorded as results, never scored as failures or
   dropped from the denominator.
2. **No metric pays for appearance.** A reward or score tied to looking honest,
   looking self-critical or looking finished is a design defect. Pay only for
   evidence the actor cannot fabricate, checked by someone the actor does not
   control.
3. **Admission is protected and timely.** Self-reported errors that come forward
   promptly lead to learning, not punishment. Silence that is found later ranks as
   concealment.
4. **The record is reinspectable.** Every error, its cause and its fix are kept
   where anyone affected can read them. Corrections are dated and visible, never
   silent.
5. **Fix the environment first.** Explain a recurring error by the incentives and
   design that produced it before blaming the actor. This is the
   environment-attribution rule applied to people and to systems alike.
6. **There is a path back.** After an honest error, or after concealment that has
   been admitted and repaired, the actor can rejoin with trust rebuilt by evidence.
   No permanent exile for disclosed mistakes.
7. **Watch the watchers by sample.** Automated passes are audited by a person on a
   random sample, and human reviewers face planted known-bad items, so both kinds of
   reviewer stay honest without blanket suspicion.

## How it applies across the workspace

- **Evidence, insight and useful work.** Negative results and honest nulls are
  first-class. A report that drops its failures is concealment, not tidiness.
- **Environment attribution.** Explain the error by its incentives. This rule is
  the human-side twin of that one.
- **Adversarial mirror.** Findings against our own defenses are reported in full,
  most of all the embarrassing ones. A suppressed red-team finding is concealment.
- **Flywheel and Emet.** Receipts record failures and UNVERIFIABLE as faithfully as
  passes. The pre-action monitor's escalation is the protected report: an agent that
  stops and escalates is never treated worse than one that pushes through.
- **The two lanes** (`mission-control/2026-10-02-two-lanes/SPEC.md`). Lane A's honest
  escalation costs nothing; a cheat found on a planted impossible task is the
  sanctioned case. Lane H reviewers who flag their own uncertainty are doing the job,
  not failing it.
- **Articulate.** The meaning guard refuses rather than guessing. An edit plan that
  admits "cannot keep the meaning" is a valid result. The house voice never claims
  checks it did not run.
- **Classifiers and research.** Model cards lead with failure rates. Missed triggers
  are reported, not tuned away after the fact. Post-scoring corrections are logged on
  both label sets.
- **Releases and the directory.** Attestations are true before they are ticked. A
  defect found after release gets a dated correction and a fix, never a quiet patch.
- **Independence policy.** Conflicts are disclosed before they are discovered. A
  late disclosure is still better than none, and it is dated as late.
- **Publications.** Corrections are visible and dated on the page. Authorship and AI
  assistance are disclosed. "I was wrong" is published with the same weight as the
  original claim.
- **Agents in this workspace, including Claude and Codex.** Report mistakes plainly
  and at once, including your own: a stray process kill, a wrong claim, a skipped
  step. Say "unknown" instead of fabricating. Never present an unverified result as
  verified. The operator meets an honest report with a fix, not a penalty.
- **The operator.** This rule binds the operator first. The essays, the income
  ledger and the independence policy hold the operator to the standard they ask of
  labs.
- **Communities and the commons.** Monitoring is mutual and participation is real.
  People who erred honestly have a dignified way back. Concealment by the powerful is
  the sanctioned case, and their way back requires full disclosure, the way the
  amnesty-for-truth model worked.

## Limits

- Just culture is not blame-free. Recklessness and concealment are still
  sanctioned, and a pattern of repeated "honest" errors is treated as an at-risk or
  reckless system problem.
- Protection for self-reporting has conditions. It does not cover intentional harm
  or anything the law requires to be handled otherwise.
- This rule does not override authorization, privacy, legal, disclosure, release or
  safety requirements in the other rules of record.
- What counts as reckless depends on what the actor could reasonably know. Judge it
  from the record available at the time, not with hindsight.

## The commons

Adopted by the operator on 2026-10-02 as the thesis the just-culture rule serves.
In the operator's words, "we must protect the integrity of the commons", and in
their account it is the only way forward that is righteous, decent, ethical and
moral. Flywheel, Emet, Telos, the independence policy and the investigative series
exist to serve it. It binds the operator first, like the rest of this file.

Source and privacy. The operator stated the thesis in chat on 2026-10-02. The
spoken and typed notes behind it are kept verbatim at
`C:/dev/mission-control/2026-10-01-articulate-voice/corpus/author/2026-10-02-*.md`
(five files). They are private voice material. Cite this section; never quote,
paste or publish the notes. The working memory record is
`C:/Users/Zain/.claude/projects/C--dev/memory/protect-the-commons-principle.md`.

Confidence labels below apply to the cited works. Claude offered the frames as
supporting evidence for the operator's thesis, and two of them (Hirschman, Axelrod)
were added at codification on 2026-10-02. Cite them with care: they support the
thesis and do not prove it.

### 1. Protect the integrity of the commons

The commons here is the shared record that people and models use to decide what is
true and what to do: knowledge, evidence, measurements, public claims, and the
accounting a community keeps. Concealment, a captured review and a gamed measure
each damage it for everyone who relies on it. That is why the just-culture rule
ranks concealment above the original error.

### 2. Provenance recorded at the source, and reinspectable

Record provenance where the thing is made, and keep it open so anyone affected can
reinspect it. The operator calls this a simple approach, and an old one:

- The earliest writing was receipts. Proto-cuneiform tablets from Uruk (about 3300
  to 3000 BCE) are mostly accounts of goods, labor and debts. High confidence on the
  accounting origin. The operator met the framing in a Benjamin Bratton talk at the
  Long Now Foundation; the talk's title and date are unknown here.
- Socratic elenchus is the protocol for argument. Socrates does not ask the other
  person to trust him. He asks them to state what they believe, and the two examine
  it together, one step at a time, until both see where the reasoning holds and where
  it breaks. Plato's dialogues are the written receipts of those arguments. High
  confidence on the method as Plato depicts it.
- Emet and Telos carry the same practice into AI work: receipts at the origin of
  writing, re-derivable by a third party.

Why it matters now: as AI output floods the network, a person still has to judge
quality, novelty and accuracy, and whether a person or a model made a thing. That
discernment gets harder. Receipts at the origin keep it possible.

The operator also observes that engagement-driven algorithms isolate people, sow
division and erode executive function and the drive to seek answers, and that
capital incentives reward the separation. The operator labels this as personal
observation and says the evidence is mixed. Keep that label wherever it is cited.

### 3. Independence is structural

Independence is structural: funding, appointment and access are not controlled by
whoever is being reviewed. Independence by permission fails, because the party that
grants it can narrow or withdraw it. The rule is nemo iudex in causa sua: no one
judges their own cause.

Examples the operator names: a platform company studying its own effects on users
while its revenue depends on engagement; qualified immunity; civil asset forfeiture;
governments reviewing their own conduct. The operator sees the same crack in the
dynasties that rose and fell again and again.

Evidence frames:

- Michael W. Wagner, "Independence by permission", *Science*, 2023, his account as
  the independent rapporteur on the 2020 Meta election studies: the outside
  researchers' independence existed by the company's permission. High confidence on
  author, title, venue and year.
- Ibn Khaldun, *Muqaddimah* (1377): asabiyyah, group cohesion, builds a dynasty;
  rulers who set themselves apart from the group erode it, and the dynasty falls,
  often within a few generations. High confidence on the cycle; reading it as
  support for structural independence is interpretation.

Applied form in this workspace: record the funding, appointment and access behind
any review beside its findings. The operator's funding-concentration thresholds
(set 2026-10-01) are one instance: 15 percent of income from one source over 12
months triggers public disclosure and a second review of findings about that party;
50 percent means declining new work evaluating them, waived for the first contract
with that disclosure.

### 4. Independence is distinct from individualism

The independence meant here is independence from capture. It serves mutual
understanding, care and reciprocity: care for the result, for the process, for
oneself, for others and for the earth. It excludes the kind of independence that
only reinforces one's own ideas, isolates people, or uses others as a stepping
stone. The operator holds that there is no good ending for humans without some form
of reciprocity.

### 5. Participation and mutual monitoring

Everyone can see the accounting. Members help make the rules. Monitoring is mutual
and comes from the group coordinating, planning, discussing and participating. It is
never imposed from outside or above, by a third-party arbiter, or by someone holding
a position of authority. Never minimize participation.

How this fits with section 3: structural independence says who may not control a
check (the party being checked). Participation says who makes the rules and sees the
accounting (the members). A check controlled by the party it checks and a rule
imposed by a party nobody can check fail the same way.

Scale is the hard part: large and fast-growing populations, limited resources, and
conflicting cultural, national and personal interests. The operator thinks it may
still be possible. This section makes no claim that it scales.

Evidence frame: Elinor Ostrom, *Governing the Commons* (1990). Commons that last let
the people affected make the rules, use monitors accountable to the members, apply
graduated sanctions, and have cheap ways to resolve conflict. High confidence.

### 6. Reintegration and redemption

Accountability comes with a path back. In a community where members monitor each
other, shame for misconduct lets a person take responsibility, learn, and rejoin
after making changes. This keeps the person from casting themselves as a victim or
the community as a villain, and it lets the community sustain and steward itself.
Obligation 6 of this rule ("There is a path back") is the in-workspace form.

Debt is the oldest case. The first receipts recorded debts, and a record with no
release valve ends in bondage. The operator's reference is the Sumerian amargi,
often rendered "freedom" and used for debt-release decrees in Lagash (24th century
BCE). Moderate confidence on the translation and dating.

Evidence frame: John Braithwaite, *Crime, Shame and Reintegration* (1989).
Reintegrative shaming condemns the act and opens a way back; stigmatizing shame
makes outcasts who turn on the community. High confidence.

### 7. Common ground with incumbents

The operator's open question: how to make this worth it both to the people who
would benefit and to those who now hold and use the existing arrangement. Five
levers, used together:

- **Aligned interest.** Show the incumbent where it gains: cheaper error discovery,
  lower liability, and trust it can carry into markets. Inference; no cited source.
- **Repeated games.** Robert Axelrod, *The Evolution of Cooperation* (1984):
  in repeated interaction, reciprocal strategies (nice, retaliatory, forgiving,
  clear) outperform defection once the future matters enough. High confidence.
- **Credible exit.** Albert O. Hirschman, *Exit, Voice, and Loyalty* (1970):
  members respond to decline by leaving or by speaking up, and voice carries weight
  when exit is credible. Portable, re-derivable receipts and vendor-neutral tools
  make exit credible. High confidence on the source; the application is inference.
- **Collective demand.** Users, buyers, insurers and regulators asking for the same
  receipts together change what incumbents supply. Operator direction; no cited
  source.
- **A dignified way back, on condition of disclosure.** Concealment by the powerful
  is the sanctioned case, and their way back requires full disclosure. South
  Africa's Truth and Reconciliation Commission granted amnesty for politically
  motivated acts only on full disclosure. High confidence.

### Limits of this section

- It is a design value and a framing for the work. It authorizes no action against
  any party, and it does not override authorization, privacy, legal, disclosure,
  release or safety requirements in the other rules of record.
- The neutrality rule in `C:/dev/Evidence-Insight-and-Useful-Work-Rule.md` still
  governs evaluation: the same criteria for every organization, our own included.
  Naming an incumbent's structural conflict is a finding about structure, never a
  claim about intent (`C:/dev/Environment-Attribution-and-Voice-Rule.md`).
- Whether mutual monitoring scales is unknown. The frames above are supporting
  evidence, not proof.

## Corrections

- **2026-10-04.** The "Our own data" bullet cited a private, gitignored notes file as
  its source, so a reader could not check the figures. The figures themselves were
  right; they appear in that file as the proportions 0.987 and 0.469. The bullet now
  names the public dataset and revision, gives the denominators and intervals, and
  says plainly that the analysis notes are private. Found by the checking-cost baseline
  (a cold re-check of public claims). Cause: a public rule pointed at a private file.
