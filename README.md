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

## Also a tool for the humans

The same structure earns its keep before any agent reads it:

- **It structures the discussion.** "Should we allow AI?" argued in the abstract goes in circles. The format's dimensions (stance, per-`scope`, disclosure, autonomy, models, concerns) turn the debate into an agenda a project can work through one axis at a time. Debian's six competing General-Resolution options differ almost entirely along these axes; the format is the shared frame that makes them comparable, and a project can adopt whichever combination it lands on.
- **It manages expectations.** Contributors see what is permitted *before* they invest effort: fewer wasted PRs, fewer surprise rejections, less reviewer burnout from "extractive" AI slop. Maintainers get one referenceable boundary instead of re-litigating it per pull request, and the `statement` pointer keeps the nuance where people actually read it.

## Placement

`ai-policy.yml`, in the project's version control, normally at the repository root. Its primary subject is **code**, but the `scope` vocabulary spans docs, translations, media, and discussion, so it applies to any contribution type.

Discovery, in order of preference: `ai-policy.yml` at the repository root; a peer record that points at it (for example a `publiccode.yml` `externalMetadata` entry); `.well-known/ai-policy.yml`. Absence of the file is itself a signal: *no declared policy* (distinct from a declared permissive one).

## How it's designed: a signal, not a rule engine

- **Structure only what recurs; point at prose for the rest.** `statement` holds the authoritative policy; `exceptions: true` says "this is a summary."
- **Declare, don't adjudicate.** Fields state intent; verification (tests, review, the human `signoff`) and the fact of LLM authorship (undetectable in general) stay outside the file. Declared identity (`attestation`) is the tractable lever, not detection.
- **Resolution is per-`scope`** (a contribution's content type); `actorExceptions` is a *signal*, not a resolution layer. Full rules below in [Resolution](#resolution).
- **Development-time, not runtime.** `models` is the AI used to *build* the project, not AI the product ships.
- **Stance is permission, not preference;** agent autonomy is a separate axis, never a stance value.
- **Named, not numbered:** enumerated items carry titles so references stay stable as items change.

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
| `defaults` + `assertions[]` | Per-content-type `stance` / `disclosure` / `humanReview` / `requirements`. |
| `allowedUses` | Explicitly permitted AI uses whose output isn't a contribution. |
| `newcomerIssuesHumanOnly` | Reserve "good first issue" tickets for human authorship. |
| `autonomousAgents` (+ `attestation`) | Agent-autonomy switch and how agents must identify themselves. |
| `actorExceptions` | Actors governed differently (a signal, not a resolution layer). |
| `disclosureFormat` | How disclosure is formatted (`trailers` keyed by degree). |
| `enforcement`, `signoff` | Declared enforcement mechanism and the human sign-off (DCO/CLA). |
| `models.policy` | The AI used *in development*: openness components plus provenance (not runtime deps). |

## Resolution

A consumer resolves the effective policy for a contribution by its **`scope`** (content type), each layer overriding only the fields it sets:

- **`defaults`** is the base for every field.
- A `scope` present in **`assertions[]`** overrides `defaults` for that scope only; the fields it omits inherit from `defaults`. A scope *absent* from `assertions[]` resolves from `defaults`, and an omitted `assertions[]` is valid (pure defaults).
- **`actorExceptions`** is *not* part of this per-field resolution: it declares that a named actor is governed differently, and a consumer surfaces it and reads its `notes`/`statement`. Only its concrete `autonomousAgentsAllowed` carve-out is machine-actionable.
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
- **[AI Attribution format](https://aiattribution.github.io)** and **[CUSTODY](https://custody-framework.org)** are adjacent but distinct: attribution records *who or what produced* a work; CUSTODY *contains* autonomous agents at runtime. Neither expresses a *contribution policy* (the rules a project sets), but this format's disclosure and `attestation` facets can align with or reference them.
- **[IETF machine-readability draft](https://datatracker.ietf.org/doc/draft-vaughan-machine-readability/)** is a rubric (parseable / interpretable / discoverable / actionable / verifiable) this format is evaluated against in **[`machine-readability.md`](./machine-readability.md)** (parseable, discoverable, actionable today; interpretability the open gap).

## Open questions (named)

Format & tooling:

- **Smallest consumer:** the reference reader/validator (a CLI, a CI action, or an MCP server) that would prove the format is worth adopting.
- **File extension:** `.yml` vs `.yaml` (name and location are settled: `ai-policy.yml` in version control).
- **Interpretability `@context`:** the JSON Schema ([`ai-policy.schema.yaml`](./ai-policy.schema.yaml)) makes the format parseable and the stance field-set a shared `$ref`; the open gap ([machine-readability.md](./machine-readability.md)) is binding each enum to a shared, dereferenceable vocabulary (a JSON-LD `@context`) for full *interpretability*.
- **Peer-record discovery:** the registered `type` string and pointer shape for records (e.g. a `publiccode.yml` `externalMetadata` entry) that reference this file.

Field-level:

- **Scope vocabulary:** is the `scope` set extensible enough (moderation, code review, meeting/transcription bots, finer splits)?
- **Stance ordinality:** is `disallowed < assisted < generated` genuinely ordinal for all projects?
- **Enforcement consequence:** should `enforcement.consequence` be structured, or stay in `statement`?
- **`models.policy` vs `requirements`:** should model-provenance requirements fold into `requirements`?
- **`requirements` altitude:** should it list only genuinely AI-specific gates and leave universal ones (tests, CI) to the general contribution process?
- **Structuring the guard-rail prose:** should the `guardrailsRef` checklist be structured, not just pointed at?
- **Attestation placement:** should `attestation` be expressible per-scope (stricter identity in security paths)?
- **Autonomous-agent middle state:** should `autonomousAgents.allowed` gain an `allowed-with-prior-discussion` state?
- **Contributor opt-out / non-discrimination:** should the format declare that contributors may not be *coerced* into using AI, and won't be shamed for opting in or out?
- **`allowedUses` conditions:** should each permitted use carry a condition (e.g. research/debugging only where output isn't contributed)?
- **`newcomerIssuesHumanOnly`:** worth a dedicated field, or too narrow (better left to `statement`)?

## License

Dual-licensed to fit how each part is used:

- **Prose** (`README.md`, `coverage.md`, `machine-readability.md`, `AI_POLICY.md`): [CC BY 4.0](./LICENSE-CC-BY-4.0).
- **Machine-readable artifacts** (`ai-policy.schema.yaml`, `ai-policy.example.yml`, `ai-policy.yml`) and any tooling: [MIT](./LICENSE-MIT), so a validator or agent can embed the schema and example without an attribution clause riding along.
