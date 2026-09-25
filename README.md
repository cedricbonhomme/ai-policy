# `ai-policy`: machine-readable rules of engagement for AI contributions

**One line:** a small, conventional repo file (`ai-policy.yml`) that an autonomous coding agent (or a CI check, or an aggregator) can read *before opening a pull request*, to learn what a project actually permits. The structured layer between `AGENTS.md` prose and the agent acting.

**Two audiences, one file:** an *agent* consumes it to act correctly; the *humans* use it to structure the policy debate and to set expectations with contributors.

Underneath both is **agency**: a project owns its contribution norms, and this makes that ownership machine-legible, so tools and agents respect a project's boundaries on its own terms instead of overriding them with their own defaults.

It's a **signal** that boundaries exist and their broad shape, not an exhaustive rule engine. The detail stays in a human-readable policy the file points at (`statement`); an `exceptions: true` flag marks where the structure is a simplification.

→ **[`ai-policy.example.yml`](./ai-policy.example.yml)** is the concrete artifact: a fully-commented example.

> **Status:** early proposal, design not settled; a *convention to prove out through adoption*, not a standard to ratify. The [open questions](#open-questions-named) are load-bearing.

## The gap

Projects increasingly publish an AI-contribution policy, but only in prose, and in no consistent place: a `CONTRIBUTING.md` section, an `AI_POLICY.md`, a `CODE_OF_CONDUCT.md`, a devguide or docs page, a wiki, an `AGENTS.md`, a `README`, even a legal page or an RFD (the [coverage survey](./coverage.md) found all of these). So an agent about to contribute, a CI check, or an aggregator has nothing machine-readable to consult; it guesses, or scrapes prose. A survey of real policies (the [CHAOSS AI-alignment moderation list](https://github.com/chaoss/wg-ai-alignment/tree/main/moderation)), analysed field-by-field in **[`coverage.md`](./coverage.md)**, shows a consistent set of dimensions beneath the surface variety, and *every one maps onto this format*. That coverage is the evidence its shape is right.

## Why this is an agent-tooling problem (the consumer story)

`ai-policy.yml` only matters if something *reads* it, and the natural readers are coding agents:

- **A pre-flight check.** Before an agent opens a PR it reads the file the way a crawler reads `robots.txt`, except this declares *stance, disclosure, and agent-identity rules*, not crawl permissions. "May I contribute generated code here? Must I disclose it? May an autonomous agent open this PR at all?"
- **A ready integration.** The reference consumer could be an **MCP server** that serves a repo's `ai-policy.yml` and validates a proposed change against it, so any MCP-speaking agent gets the policy without bespoke parsing. That turns "needs adoption" into "here's the integration."
- **Where agents already look.** It sits beside `AGENTS.md` / `CLAUDE.md` (which point to it), the same place agent instructions already live.
- **A sanctioned-workflow library is the other half, and one now exists.** Fedora's AI/ML SIG publishes a [skills library](https://forge.fedoraproject.org/ai-ml/skills-library) (CC BY-SA 4.0) in the [Agent Skills](https://agentskills.io/specification) open format: one directory per skill, each with a `SKILL.md` carrying YAML frontmatter and instructions. Its current skills automate compose triage, FTBFS bug search, meeting-log summarisation and Packit onboarding. A project that publishes approved agent workflows has answered in executable form part of what this file declares in prose, and "these workflows are sanctioned here" is a more useful thing to hand an agent than a restatement of the rules. Which field should point at it is [an open question](#open-questions-named).

## Also a tool for the humans

The same structure earns its keep before any agent reads it:

- **It structures the discussion.** "Should we allow AI?" argued in the abstract goes in circles. The format's dimensions (stance, per-`scope`, disclosure, autonomy, models, concerns) turn the debate into an agenda a project can work through one axis at a time. The distinction that makes the debate tractable at all is *adoption* versus *alignment*: Fedora's [Justin Wheeler](https://jwheel.org/blog/2026/09/ai-alignment/) separates "AI adoption", which "communicates a pre-defined, non-negotiable stance" whose goal is simply to increase usage, from "AI alignment", which "communicates that LLM-gen-AI use exists on a spectrum" to be squared with a community's existing values, norms and culture. A declaration format is only coherent under the second reading — there is nothing to declare where the answer is fixed in advance — and the spectrum is precisely what `stance`, `defaults` and `assertions[]` exist to carry. Debian's six competing General-Resolution options differ almost entirely along these axes; the format is the shared frame that makes them comparable, and a project can adopt whichever combination it lands on.
- **It manages expectations.** Contributors see what is permitted *before* they invest effort: fewer wasted PRs, fewer surprise rejections, less reviewer burnout from "extractive" AI slop. Maintainers get one referenceable boundary instead of re-litigating it per pull request, and the `statement` pointer keeps the nuance where people actually read it.

## Placement

`ai-policy.yml`, in the project's version control, normally at the repository root. Its primary subject is **code**, but the `scope` vocabulary spans docs, translations, media, and discussion, so it applies to any contribution type.

Discovery, in order of preference: `ai-policy.yml` at the repository root; a peer record that points at it (for example a `publiccode.yml` `externalMetadata` entry); `.well-known/ai-policy.yml`. Absence of the file is itself a signal: *no declared policy* (distinct from a declared permissive one).

### What this format does not govern

`ai-policy.yml` declares **what a project asks of a contribution**: what may be offered, and how the project handles what is offered. `scope` is a content type because the subject is a contribution; the primary consumer is something about to open a pull request, and the `review` fields tell it what becomes of the change once it does. Three neighbouring kinds of rule turn up in real policies and are deliberately out of scope, because none of them concerns a contribution's lifecycle:

- **Platform self-commitments.** Codeberg binds itself never to train on hosted code or user data. That governs the declarer's own conduct toward its users and never touches the handling of a contribution.
- **Hosting and content restrictions.** Codeberg's rule on what may be hosted, and Flathub's original policy on AI-generated applications, govern artifacts already in existence rather than contributions being offered.
- **Governance-process rules.** Fedora forbids AI scoring of code-of-conduct matters, funding requests, conference talks and leadership positions. These are decisions about people and events; no contribution is involved at any point. A project holding such a rule records it in `notes` with `exceptions: true`.

The [specificity analysis](./coverage.md#specificity-against-the-chaoss-domain-taxonomy) reaches the same boundary from the metrics side: meeting bots, infrastructure strain and training on hosted data score as ungoverned across projects largely because the wrong party is being asked, and they belong to whoever runs the meeting infrastructure, pays for the servers, or holds the data. The natural carrier is a **forge-level record**, and none exists today. Until then, the file's location and this boundary answer that question.

## How it's designed: a signal, not a rule engine

- **Structure only what recurs; point at prose for the rest.** `statement` holds the authoritative policy; `exceptions: true` says "this is a summary."
- **Declare, don't adjudicate.** Fields state intent; verification (tests, review, the human `signoff`) and the fact of LLM authorship (undetectable in general) stay outside the file. Declared identity (`attestation`) is the tractable lever, not detection.
- **Resolution is per-`scope`** (a contribution's content type); `actorExceptions` is a *signal*, not a resolution layer. Full rules below in [Resolution](#resolution).
- **Development-time, not runtime.** `models` is the AI used to *build* the project, not AI the product ships.
- **Stance is permission, not preference;** agent autonomy is a separate axis, never a stance value.
- **Named, not numbered:** enumerated items carry titles so references stay stable as items change.
- **Nuance goes in `notes`, and `notes` is how the next field gets chosen.** Not every distinction earns an enum. Where a rule can be stated in a sentence, it belongs in the `notes` string of the object it qualifies, which the schema now provides on every object that carries a rule. That keeps the enums to what a consumer actually branches on, and it leaves a trail: collecting `notes` across adopted files shows which nuances recur, and a nuance that recurs in similar words across many projects is the evidence for promoting it to structure. Structure earned this way is structure the corpus asked for, rather than structure guessed at from a single policy.
- **"AI" here is shorthand.** These documents say *AI* for brevity, but what the surveyed policies actually govern is generative models, not machine learning at large. **LLM-gen-AI** — the term Fedora's alignment work takes from the Software Freedom Conservancy — is the more precise one, and worth adopting if it settles in the CHAOSS working group's vocabulary; several policies in the [coverage survey](./coverage.md) already scope themselves that narrowly in their own words.

## The format, in brief

Top-level fields; everything is optional except a minimal `summary` + a default stance. Each field's meaning is in the [example](./ai-policy.example.yml); the shape is validated by [`ai-policy.schema.yaml`](./ai-policy.schema.yaml).

| Field | Purpose |
|---|---|
| `version` | The `ai-policy` format version. |
| `summary` | Quick contribution-stance filter (`permissive \| mixed \| restrictive \| disallowed`). |
| `status` | Maturity of the policy itself (`adopted \| draft \| under-discussion`). |
| `statement` / `guardrailsRef` | Pointers to the human-readable policy and the actionable guard-rail checklist. |
| `exceptions` | Flags that the structured stance is a summary with carve-outs in `statement`. |
| `concerns` | The societal/ethical motivation (for aggregation). |
| `defaults` + `assertions[]` | Per-content-type `stance` / `disclosure` / `humanReview` (the contributor's own) / `requirements`. |
| `allowedUses` | Explicitly permitted AI uses whose output isn't a contribution. |
| `review` | AI in the project's *review* of contributions: whether it may assist, and whether a human must still decide. |
| `newcomerIssuesHumanOnly` | Reserve "good first issue" tickets for human authorship. |
| `autonomousAgents` (+ `attestation`) | Agent-autonomy switch and how agents must identify themselves. |
| `priorArrangement` | Contribution kinds needing agreement *before* submission, and what satisfies it. |
| `actorExceptions` | Actors governed differently (a signal, not a resolution layer). |
| `disclosureFormat` | How disclosure is formatted (`trailers` keyed by degree). |
| `enforcement`, `signoff` | Declared enforcement mechanism and the human sign-off (DCO/CLA). |
| `models.policy` | The AI used *in development*: minimum model openness by component (not runtime deps). |

## Resolution

A consumer resolves the effective policy for a contribution by its **`scope`** (content type), each layer overriding only the fields it sets:

- **`defaults`** is the base for every field.
- A `scope` present in **`assertions[]`** overrides `defaults` for that scope only; the fields it omits inherit from `defaults`. A scope *absent* from `assertions[]` resolves from `defaults`, and an omitted `assertions[]` is valid (pure defaults).
- **`actorExceptions`** is *not* part of this per-field resolution: it declares that a named actor is governed differently, and a consumer surfaces it and reads its `notes`/`statement`. Only its concrete `autonomousAgentsAllowed` carve-out is machine-actionable.
- **Whole-file fields do not cascade, and they do not override the stance — they compose with it.** `autonomousAgents`, `priorArrangement` and `review` apply to the file as a whole and answer different questions from `stance`, so a consumer must satisfy each independently rather than picking a winner. `stance` says whether this kind of contribution may be offered at all; `priorArrangement` says whether it may be offered *without agreement obtained first*; `autonomousAgents` says whether a non-human may do the offering; `review` says what the project will do with it afterwards. A change permitted by `stance` and caught by `priorArrangement` is permitted **and** gated, not contradictory.
- Everything beyond `summary` and `defaults` is optional; a minimal declaration is a `summary` plus a default stance.

`defaults` and each `assertions[]` entry share one field-set (`stance`, `disclosure`, `humanReview`, `requirements`), defined once in the [schema](./ai-policy.schema.yaml) as a reusable `$ref`, so "same fields" is a structural guarantee, not a prose claim. The layering above is defined by this spec and applied by the consumer (as a browser applies the CSS cascade); it is never encoded in an individual file.

## The ask

Not "please ratify a standard." **Adoption first**, the [`FUNDING.yml`](#prior-art--related-work) model: a tiny file wins by having a *consumer*, not by being standardized. The questions that matter:

1. Is this the right *shape* for an agent to consume?
2. Would agent tooling actually read a conventional repo file like this, natively or via an MCP server?
3. What is the smallest consumer that would prove it?

## Prior art & related work

- **`FUNDING.yml`** is the closest model: a tiny, single-purpose YAML file that reached wide adoption not by being standardized but by having a *consumer* (GitHub renders it as a Sponsor button). Judge `ai-policy.yml` the same way.
- **`AGENTS.md` / `CLAUDE.md`** are prose instructions *to* agents. `ai-policy.yml` is the structured, machine-actionable counterpart, co-located and cross-linked; a *section of* `AGENTS.md` is a plausible alternative home.
- **[ai-policy.dev](https://ai-policy.dev/)** is the prose layer this format points at: a small library of ready-made `AI_POLICY.md` texts (*AI Allowed*, *Human Voice*, *Human Responsible*, *AI Disallowed*) that a project copies into its repository, in the manner of choosealicense.com. Each preset is tagged on the site with rule IDs marked as permits, requires or forbids, but that metadata is [stripped when the policy is copied](https://github.com/43081j/ai-policy/blob/main/policies/_template.md), so an adopting repository publishes nothing a consumer can read. The two compose rather than compete: a preset is a natural `statement` target, and every preset is expressible in this format: [`examples/`](./examples/) holds each one as an `ai-policy.yml` to ship beside its Markdown, scored in [coverage](./coverage.md#template-policies).
- **[AI Attribution format](https://aiattribution.github.io)** and **[CUSTODY](https://custody-framework.org)** are adjacent but distinct: attribution records *who or what produced* a work; CUSTODY *contains* autonomous agents at runtime. Neither expresses a *contribution policy* (the rules a project sets), but this format's disclosure and `attestation` facets can align with or reference them.
- **[IETF machine-readability draft](https://datatracker.ietf.org/doc/draft-vaughan-machine-readability/)** is a rubric (parseable / interpretable / discoverable / actionable / verifiable) this format is evaluated against in **[`machine-readability.md`](./machine-readability.md)** (parseable, discoverable, actionable today; interpretability the open gap).

## Open questions (named)

Format & tooling:

- **Smallest consumer:** the reference reader/validator (a CLI, a CI action, or an MCP server) that would prove the format is worth adopting.
- **File extension:** `.yml` vs `.yaml` (name and location are settled: `ai-policy.yml` in version control).
- **Interpretability `@context`:** the JSON Schema ([`ai-policy.schema.yaml`](./ai-policy.schema.yaml)) makes the format parseable and the stance field-set a shared `$ref`; the open gap ([machine-readability.md](./machine-readability.md)) is binding each enum to a shared, dereferenceable vocabulary (a JSON-LD `@context`) for full *interpretability*.
- **Template provenance:** should a declaration say which published template its prose was adopted from, and at which version (for example an [ai-policy.dev](https://ai-policy.dev/) preset)? Copied policy text drifts from its source silently, as copied licence texts did before SPDX identifiers; a `basedOn` reference would let a consumer compare like with like and an aggregator count adoption per template. It needs a template publisher that versions its presets, which none yet does.
- **Peer-record discovery:** the registered `type` string and pointer shape for records (e.g. a `publiccode.yml` `externalMetadata` entry) that reference this file.

Field-level:

- **Scope vocabulary:** is the `scope` set extensible enough (moderation, meeting/transcription bots, finer splits)? Review has been taken out of this question and given its own field, because it is done *to* a contribution rather than being one and so was never a content type. What remains open is narrower and mostly about whether the existing splits are principled: Gitea permits AI to draft issues and pull requests while banning it in replies to reviewers, a line the vocabulary happens to reproduce (`issue-descriptions` and `pull-request-descriptions` on one side, `comments` on the other) without modelling the reason, which is composing versus conversing. It works today; it may not survive a project that splits differently.
- **`review` depth:** the field carries `aiAssist`, `humanDecision` and a `notes` string. Rust's requirement that review bots run under separate blockable accounts with non-blocking comments, and Flathub's ban on a contributor *requesting* an AI-agent review, are sentences in `notes` for now. If either recurs across several projects in comparable words, it is a candidate for promotion.
- **A forge-level record:** platform self-commitments, hosting restrictions and governance-process rules are [out of scope here](#what-this-format-does-not-govern) and have no carrier at all. Codeberg's undertaking never to train on hosted code is the clearest instance, and the CHAOSS domains that score as ungoverned across projects are mostly of this kind. Whether this project should specify that record, or only name the gap, is open. If one is built, this format gains a companion rather than a field, and both will then need to say which kind of document they are.
- **Deliberate non-policy:** should `status` distinguish "we considered this and decided no AI-specific rule is needed" from having no policy? Kubernetes steering reached exactly that position, and the Linux Kernel folds AI into tool-generated content generally rather than giving it a surface. Absence of the file currently means *no declared policy*, which cannot express either.
- **Disclosure content:** should `disclosureFormat` say what a disclosure must *name*? It currently describes only where one goes. Projects diverge sharply: KeePassXC wants the service or model, Polars wants the tools and the extent, GDAL wants authorship apportioned ("what was written by whom/what"), while the Linux Kernel's trailer names no model at all and Gitea removed its model-naming clause. A consumer cannot presently tell these regimes apart.
- **Sanctioned-workflow pointer:** should a declaration point at a library of approved agent workflows, such as [Fedora's skills library](https://forge.fedoraproject.org/ai-ml/skills-library)? `guardrailsRef` points at rules a contributor must observe; a skills library is the opposite direction, naming what the project has already blessed. Folding both into one pointer may be right, but the semantics differ.
- **Stance ordinality:** is `disallowed < assisted < generated` genuinely ordinal for all projects?
- **Enforcement consequence:** should `enforcement.consequence` be structured, or stay in `statement`?
- **`models.policy` vs `requirements`:** should model-provenance requirements fold into `requirements`?
- **`requirements` altitude:** should it list only genuinely AI-specific gates and leave universal ones (tests, CI) to the general contribution process? Godot shows why the boundary needs watching: its June 2026 rewrite was driven by AI pressure and the review backlog together, and the resulting document bars new contributors (three or fewer merged pull requests) from features and significant refactors without maintainer permission — a mentorship and trust rule that applies whatever tools are used, stated before the AI section. A policy revised *because of* AI can carry rules that are not AI rules, and those belong to the general contribution process.
- **Structuring the guard-rail prose:** should the `guardrailsRef` checklist be structured, not just pointed at?
- **Attestation placement:** should `attestation` be expressible per-scope (stricter identity in security paths)?
- **`priorArrangement` shape (settled in principle, open in detail):** the gate itself is now a field, added because four adopted policies require it — Debian (bulk changes, prior discussion), Rust (a reviewer agreeing before an LLM-created pull request is opened), Fedora (large-scale initiatives to the Council), Polars (an already-accepted issue). Because most of these gate the *human* path, it sits outside `autonomousAgents` and covers both. What remains open is its shape where a project gates two kinds of contribution differently: `appliesTo` is a list while `basis` is single, so Debian's *bulk changes to discussion* and Rust's *AI-generated pull requests to reviewer agreement* cannot both be stated in one file. Making `basis` a list would not fix that; the shape needed pairs a basis with each trigger. Two smaller gaps: `agent-submissions` and `ai-generated-prs` are not distinguished, though an agent's pull request is normally both, and `bulk-changes` may not belong at all, since mass-change conventions predate LLMs and outlive them.
- **Disclosure by forge label:** should `disclosureFormat.method` gain a `label` value? Rust marks merged LLM-created pull requests `llm-assisted`. Unlike a trailer or a PR template it is applied by the reviewer at merge, which makes it a measurement instrument as much as a disclosure.
- **Contributor opt-out / non-discrimination:** should the format declare that contributors may not be *coerced* into using AI, and won't be shamed for opting in or out? The reverse commitment turns up too: ai-policy.dev's *Human Responsible* preset promises that a contributor's own tooling "is not policed, will not be asked about, and does not need to be shared". That is a promise of non-inquiry, distinct from `disclosure: prohibited`, which only governs what the submission may carry.
- **`allowedUses` conditions:** should each permitted use carry a condition (e.g. research/debugging only where output isn't contributed)?
- **`newcomerIssuesHumanOnly`:** worth a dedicated field, or too narrow (better left to `statement`)?

Decided for now, kept here because new evidence would reopen them:

- **Numeric thresholds.** Significance thresholds stay in prose; no field. Two policies state one mechanically, but they differ in kind and only one is consumable: Godot presumes code under fifteen lines trivial, which an agent holding a diff can evaluate, while Rust's circuit-breaker (halt LLM-created merges above half of merged pull requests over six weeks) needs project-wide merge history no contributor or agent has, and answers whether the door is currently open rather than whether a change complies. The test that settled it generalises to any future candidate that looks countable: **a threshold earns a field only if a consumer can evaluate it before submitting.** On that test the evidence is a single project, against a deliberate design choice and seven policies drawing the line qualitatively. *Reopen if:* further projects publish per-contribution thresholds a submitter could check, and they converge on a comparable unit — several more line counts, or a shared measure that is not line counts. Divergent units would confirm the prose choice rather than undermine it.

## License

Dual-licensed to fit how each part is used:

- **Prose** (`README.md`, `coverage.md`, `machine-readability.md`, `AI_POLICY.md`): [CC BY 4.0](./LICENSE-CC-BY-4.0).
- **Machine-readable artifacts** (`ai-policy.schema.yaml`, `ai-policy.example.yml`, `ai-policy.yml`, `examples/`) and any tooling: [MIT](./LICENSE-MIT), so a validator or agent can embed the schema and example without an attribution clause riding along.
