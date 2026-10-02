## The ask: adoption first

- **[Shape](https://codeberg.org/open-source-ecosystem/ai-policy/src/branch/main/README.md#the-ask)**: right for an agent to consume?
- **Reading**: would agent tooling read a repo file?
- **Smallest consumer**: what would prove it?
- The `FUNDING.yml` model: won by a consumer

**Not "please ratify a standard":<br />a tiny file wins by having something that reads it.**

[↳ README: the ask](https://codeberg.org/open-source-ecosystem/ai-policy/src/branch/main/README.md#the-ask)

Note:

↓ What each of you can do

- The questions are the README's own: shape and reading ask for judgement, the smallest consumer for a build
- Reading: natively, or via an MCP server
- `FUNDING.yml` is a tiny single-purpose YAML file that reached wide adoption not by being standardized but by having a consumer: GitHub renders it as a Sponsor button. Judge this file the same way
- Status: early proposal, a convention to prove out through adoption

**Q&A details:**

- Smallest consumer candidates named in the open questions: a CLI, a CI action, or an MCP server, as the reference reader and validator
- Early adopters of ai-policy.dev's prose presets exist, all verbatim copies; none publishes anything machine-readable, because the site strips its own metadata on copy

--

## What each of you can do

<!-- .slide: data-timing="0" class="compact" -->

| Who | Where to start (a reading) |
| --- | --- |
| **Maintainers** | a [preset](https://codeberg.org/open-source-ecosystem/ai-policy/src/branch/main/writing-a-policy.md#if-you-already-know-where-you-stand) beside your prose policy |
| **Everyone** | [add a policy](https://codeberg.org/open-source-ecosystem/ai-policy/src/branch/main/coverage.md#add-a-policy-prs-welcome) the format can't capture |
| **Tool builders** | the [smallest consumer](https://codeberg.org/open-source-ecosystem/ai-policy/src/branch/main/README.md#open-questions-named) |
| **Forges** | the open [forge-level record](https://codeberg.org/open-source-ecosystem/ai-policy/src/branch/main/README.md#open-questions-named) |
| **Foundations** | [shared vocabulary, template provenance](https://codeberg.org/open-source-ecosystem/ai-policy/src/branch/main/README.md#open-questions-named) |

**A policy the format cannot capture<br />is the most valuable contribution.**

Note:

- The table is this deck's reading of the open questions by audience; the README addresses none of them to a particular audience, and no one has committed to any of it
- Maintainers: copy the matching `examples/` file as `ai-policy.yaml`; the survey is open to pull requests
- Tool builders: agentscan, which flags agent-like accounts, is named in the coverage as a candidate consumer of `autonomousAgents.allowed`; its repository copies a prose preset and publishes nothing machine-readable
- Forges: platform commitments such as Codeberg's have no carrier today
- Foundations: binding the vocabulary to shared identifiers (the interpretability `@context`), and whether a declaration should name the template its prose was adopted from, are questions about shared vocabulary rather than one project's choice. The README itself looks to the CHAOSS working group's vocabulary for the term LLM-gen-AI

**Q&A details:**

- Template provenance needs a template publisher that versions its presets, which none yet does
