## What tools can do with it

<!-- .slide: class="compact" -->

| [Property](https://codeberg.org/open-source-ecosystem/ai-policy/src/branch/main/machine-readability.md) | Rating |
| --- | --- |
| Parseable | full: YAML with a published JSON Schema |
| Discoverable | full-ish: conventional location; absence is a signal |
| Actionable | full: gate or annotate a pull request, warn, aggregate |
| Interpretable | partial: enums are local strings, not shared URIs |
| Verifiable | partial, by design: intent, not proof of authorship |

**Declare, don't adjudicate:<br />a signal, not a proof.**

[↳ Machine-readability evaluation](https://codeberg.org/open-source-ecosystem/ai-policy/src/branch/main/machine-readability.md)

Note:

**Acronyms:** IETF = Internet Engineering Task Force; JSON-LD = JSON for Linked Data; LLM = large language model; MCP = Model Context Protocol; URI = Uniform Resource Identifier

- The rubric is the [IETF machine-readability draft](https://datatracker.ietf.org/doc/draft-vaughan-machine-readability/), which defines no passing grade; it is a way of stating honestly what a format delivers
- Actionable: a consumer can act on the file, and resolution is deterministic, so two consumers reach the same decision from the same file. Per-scope for the stance field-set, whole-file for `autonomousAgents`, `priorArrangement` and `review`
- Interpretability is the open gap: binding each enum to a shared, dereferenceable vocabulary, a JSON-LD `@context`, would close it
- Verifiability is bounded on purpose: LLM authorship is undetectable in general. What can be checked is `requirements` gates, signed-commit `attestation` and the human `signoff`

**Q&A details:**

- What a consumer could be: a CLI, a CI action, or an MCP server that serves a repository's file to any MCP-speaking agent. Which one comes first is the open *Smallest consumer* question
- `notes` and `statement` are free prose by design, not machine-interpretable
