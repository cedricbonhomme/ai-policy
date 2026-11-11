## What it deliberately does not do

- **Detect** whether AI wrote a change
- **Govern runtime AI** the product ships
- **Govern platforms**: hosting, training on hosted code
- **Govern AI in decisions** about people and events

**It declares what a project asks of a contribution.<br />Rules with another subject belong elsewhere.**

[↳ README: placement (what it does not govern)](https://codeberg.org/open-source-ecosystem/ai-policy/src/branch/main/README.md#placement)

Note:

↓ A missing forge-level record

- Detection: LLM authorship is undetectable in general; the format declares intent, and declared identity is the lever
- Runtime: `models` is the AI used to build the project
- Platform self-commitments and hosting restrictions: Codeberg binds itself never to train on hosted code or user data; Flathub's original policy on AI-generated applications governed artifacts already in existence
- Governance-process rules: Fedora forbids AI scoring of code-of-conduct matters, funding requests, conference talks and leadership positions. A project holding such a rule records it in `notes` with `exceptions: true`

**Q&A details:**

- None of these concerns a contribution's lifecycle, which is why they are out of scope rather than missing

--

## A missing forge-level record

<!-- .slide: data-timing="0" -->

- Meeting bots, server load, training on hosted data
- Score as ungoverned across projects
- Largely because the wrong party is asked
- A [forge-level record](https://codeberg.org/open-source-ecosystem/ai-policy/src/branch/main/coverage.md#specificity-against-the-chaoss-domain-taxonomy) would carry them; none exists

**Whether this project should specify it,<br />or only name the gap, is open.**

[↳ README: open questions (a forge-level record)](https://codeberg.org/open-source-ecosystem/ai-policy/src/branch/main/README.md#open-questions)

Note:

↓ How machine-readable is it?

- Meeting bots belong to whoever runs the meeting infrastructure; server load to whoever pays for the servers; training on hosted code to whoever holds it
- Codeberg is the one forge in the corpus, and it is where those domains suddenly have rules
- The coverage finding: these domains need a declaring-party axis (project, forge, foundation) before an absence can be read as a gap
- If one is built, this format gains a companion rather than a field
- A natural carrier would be discoverable at `.well-known`

--

## How machine-readable is it?

<!-- .slide: data-timing="0" -->

| Property | Rating |
| --- | --- |
| Parseable | Full |
| Interpretable | Partial |
| Discoverable | Full-ish |
| Actionable | Full |
| Verifiable | Partial, by design |

**Interpretability is the open gap;<br />verifiability is bounded on purpose.**

[↳ Machine-readability evaluation](https://codeberg.org/open-source-ecosystem/ai-policy/src/branch/main/machine-readability.md)

Note:

**Acronyms:** IETF = Internet Engineering Task Force; JSON-LD = JSON for Linked Data

- Scored against the five properties of the IETF machine-readability draft (draft-vaughan-machine-readability), a rubric with no passing grade
- Interpretable is partial because the vocabulary terms are local strings with schema definitions, not URIs bound to a shared vocabulary. A JSON-LD `@context` would close it
- Verifiable is partial by design: the format declares intent; only the checkable parts (requirements gates, signed-commit attestation, the human sign-off) can be verified
- Actionable: two consumers reach the same decision from the same file
