## One file, read before the pull request

- A small YAML file in your repository
- Says what your project [permits for AI contributions](https://codeberg.org/open-source-ecosystem/ai-policy/src/branch/main/README.md#the-gap)
- Read by [coding agents](https://codeberg.org/open-source-ecosystem/ai-policy/src/branch/main/README.md#why-this-is-an-agent-tooling-problem-the-consumer-story), CI checks, aggregators
- And by people, [before they invest effort](https://codeberg.org/open-source-ecosystem/ai-policy/src/branch/main/README.md#also-a-tool-for-the-humans)

**A signal that boundaries exist and their shape,<br />not an exhaustive rule engine.**

[↳ README: the gap](https://codeberg.org/open-source-ecosystem/ai-policy/src/branch/main/README.md#the-gap)

Note:

↓ The prose stays authoritative

**Acronyms:** CI = continuous integration; MCP = Model Context Protocol

- Today AI-contribution policies exist only in prose, and in no consistent place: `CONTRIBUTING.md`, `AI_POLICY.md`, `AGENTS.md`, a docs page, a wiki. An agent about to contribute has nothing machine-readable to consult; it guesses, or scrapes prose
- The pre-flight check: an agent reads the file before opening a pull request, the way a crawler reads `robots.txt`. May I contribute generated code here? Must I disclose it? May an autonomous agent open this pull request at all?
- For people it structures the policy debate one axis at a time and sets expectations: fewer wasted pull requests, fewer surprise rejections
- Underneath both: agency. The project owns its contribution norms, and the file makes that ownership machine-legible
- Status: early proposal, design not settled

**Q&A details:**

- `AGENTS.md` and `CLAUDE.md` are prose instructions to agents; `ai-policy.yaml` is the structured counterpart, co-located and cross-linked. A section of `AGENTS.md` is named as a plausible alternative home
- The reference consumer *could be* an MCP server that serves the file and validates a proposed change against it; none exists yet
- Closest model: `FUNDING.yml`, a tiny single-purpose file that spread because something consumed it

--

## The prose stays authoritative

<!-- .slide: data-timing="0" -->

- [`statement`](https://codeberg.org/open-source-ecosystem/ai-policy/src/branch/main/README.md#the-format-in-brief): where your human-readable policy is
- [`guardrailsRef`](https://codeberg.org/open-source-ecosystem/ai-policy/src/branch/main/README.md#the-format-in-brief): a contributor's practical checklist
- `exceptions: true`: the prose says more than the fields
- Nuance that fits no field: a `notes` string

**The file summarises the policy;<br />the prose it points at decides.**

[↳ README: how it's designed](https://codeberg.org/open-source-ecosystem/ai-policy/src/branch/main/README.md#how-it-s-designed-a-signal-not-a-rule-engine)

Note:

- `statement` is a repository-relative path or a URL, usually `AI_POLICY.md` or a section of `CONTRIBUTING.md`
- `guardrailsRef` is optional: only if the checklist lives apart from the policy
- `exceptions` is a boolean flag: the structured stance is a summary, with carve-outs in `statement`. A consumer that sees it reads the prose rather than treating the structure as complete
- `notes` is available on every object that carries a rule. Collecting `notes` across adopters is how the format decides which nuance earns a field next

**Q&A details:**

- Structure only what recurs, or what a consumer must act on before submitting; point at prose for the rest
- Judgements such as what counts as menial or significant stay in prose: structure that pretended otherwise would be false precision
