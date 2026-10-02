## The gap

- Projects publish [AI-contribution policies](https://codeberg.org/open-source-ecosystem/ai-policy/src/branch/main/README.md#the-gap)
- Only in prose, and in no consistent place
- A coding agent about to contribute cannot read them
- It guesses, or scrapes prose

**The rules exist. Nothing a machine<br />can consult says what they are.**

[↳ README: the gap](https://codeberg.org/open-source-ecosystem/ai-policy/src/branch/main/README.md#the-gap)

Note:

↓ Where policies live today

- A coding agent here means software that writes a change and can open the pull request itself, not just suggest text to a person
- Same problem for a CI check that wants to enforce a policy, and for an aggregator that wants to compare projects
- The file is `ai-policy.yaml` (or `.yml`) at the repository root: the structured layer between `AGENTS.md` prose and the agent acting
- Early proposal, design not settled

**Q&A details:**

- `AGENTS.md` and `CLAUDE.md` are prose instruction files addressed to coding agents, kept in the repository
- Discovery order: `ai-policy.yml` at the root; a peer record that points at it (for example a `publiccode.yml` `externalMetadata` entry); `.well-known/ai-policy.yml`

--

## Where policies live today

<!-- .slide: data-timing="0" -->

- `CONTRIBUTING.md`, `AI_POLICY.md`
- Codes of conduct, devguides, docs pages, wikis
- READMEs, `AGENTS.md`, legal pages, an RFD
- The [coverage survey](https://codeberg.org/open-source-ecosystem/ai-policy/src/branch/main/coverage.md#summary) found all of these

**Each is a sensible home for prose.<br />None is where a tool would know to look.**

[↳ README: the gap](https://codeberg.org/open-source-ecosystem/ai-policy/src/branch/main/README.md#the-gap)

Note:

**Acronyms:** RFD = Request for Discussion (Oxide's design-document series)

- The list is the README's, from the coverage survey of real policies
- Haiku's policy *is* its `AGENTS.md`; Oxide's is RFD 576
- In the larger corpus of popular projects, 34 policies live in `AGENTS.md` or `CLAUDE.md`, which supports reading this format's pointer from there

**Q&A details:**

- Standalone policy files are common: attrs `.github/AI_POLICY.md`, Ghostty and Mastodon `AI_POLICY.md`, yt-dlp `.NO_AI/README.md`
- ai-policy.dev publishes ready-made `AI_POLICY.md` texts; it tags each preset with rules on the site, but that metadata is stripped when the policy is copied, so an adopting repository publishes nothing a consumer can read
