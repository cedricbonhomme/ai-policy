## What you can do now

- Adopt a [preset](https://codeberg.org/open-source-ecosystem/ai-policy/src/branch/main/writing-a-policy.md#if-you-already-know-where-you-stand), or [work one out](https://codeberg.org/open-source-ecosystem/ai-policy/src/branch/main/writing-a-policy.md#working-it-out)
- Validate it against the schema
- Point `AGENTS.md` at it, without restating it
- Put what fits no field in `notes`

**Adoption first: a tiny file wins<br />by having a consumer, not by being standardized.**

[↳ README: the ask](https://codeberg.org/open-source-ecosystem/ai-policy/src/branch/main/README.md#the-ask)

Note:

↓ Open questions for maintainers

**Acronyms:** MCP = Model Context Protocol

- The model is `FUNDING.yml`: it spread because something read it (a Sponsor button), not because it was ratified
- On restating: this repository's own [`AGENTS.md`](https://codeberg.org/open-source-ecosystem/ai-policy/src/branch/main/AGENTS.md) points at its `ai-policy.yaml` and deliberately does not repeat the values. A structured policy plus a prose paraphrase gives copies that drift apart with no way to notice
- `notes` collected across adopters are how the next field gets chosen: a nuance that recurs in similar words across many projects earns structure
- The ask of the proposal: is this the right shape for an agent to consume; would agent tooling read a conventional repository file like this, natively or through an MCP server; what is the smallest consumer that would prove it

**Q&A details:**

- Licensing: the schema, the example and `examples/` are MIT, so a validator or agent can embed them without an attribution clause; the prose is CC BY 4.0

--

## Open questions for maintainers

<!-- .slide: data-timing="0" -->

- **Smallest consumer**: CLI, CI action or MCP server
- **Scope vocabulary**: are the splits principled?
- **Template provenance**: a `basedOn` reference?

**The open questions are load-bearing.**

[↳ README: open questions (named)](https://codeberg.org/open-source-ecosystem/ai-policy/src/branch/main/README.md#open-questions-named)

Note:

**Acronyms:** CLI = command-line interface; CI = continuous integration; MCP = Model Context Protocol

- Scope vocabulary: is the `scope` set extensible enough, for moderation or meeting bots, and do its splits follow a principle or only happen to match today's policies?
- Template provenance: should a file say which published template its prose came from, and at which version, so drift from the source is detectable? It needs a template publisher that versions its presets, which none yet does
- Also open: `undecided` granularity (no per-scope entries), a pointer to a library of sanctioned agent workflows, and `priorArrangement` pairing a basis with each trigger
