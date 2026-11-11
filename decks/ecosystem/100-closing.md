## Continue the conversation

<!-- .slide: data-timing="45" -->

### Scan for the proposal and this deck

<img class="qr-code" data-qr="https://codeberg.org/open-source-ecosystem/ai-policy" alt="QR code for the ai-policy repository on Codeberg">

[codeberg.org/open-source-ecosystem/ai-policy](https://codeberg.org/open-source-ecosystem/ai-policy)

Note:

↓ Where to read more

- Start with the README: the gap, the aims, the design principles and the ask, in one page
- Close on the ask: is this the right shape, would tooling read it, and what is the smallest consumer that would prove it. Issues and pull requests are open
- The repository publishes its own `ai-policy.yaml` and `AI_POLICY.md`, as a worked case

**Q&A details:**

- Licensing: the prose is CC BY 4.0; the schema, examples and any tooling are MIT, so a validator or agent can embed them without an attribution clause riding along

--

## Where to read more

<!-- .slide: data-timing="0" class="compact" -->

| Document | Read it if |
| --- | --- |
| [README](https://codeberg.org/open-source-ecosystem/ai-policy/src/branch/main/README.md#design-principles) | you want the argument; start here |
| [Coverage](https://codeberg.org/open-source-ecosystem/ai-policy/src/branch/main/coverage.md#cross-cutting-findings) | you want the evidence from real policies |
| [Writing a policy](https://codeberg.org/open-source-ecosystem/ai-policy/src/branch/main/writing-a-policy.md#if-you-already-know-where-you-stand) | your project is about to adopt one |
| [Machine-readability](https://codeberg.org/open-source-ecosystem/ai-policy/src/branch/main/machine-readability.md) | you would build a consumer |
| [Corpus mapping](https://codeberg.org/open-source-ecosystem/ai-policy/src/branch/main/research/hora-2026/README.md) | you study policies as data |
| [Open questions](https://codeberg.org/open-source-ecosystem/ai-policy/src/branch/main/README.md#open-questions) | you want to shape what comes next |

**A signal, not a rule engine.**

[↳ README: the ask](https://codeberg.org/open-source-ecosystem/ai-policy/src/branch/main/README.md#questions-for-agent-tooling-builders)

Note:

- The format itself, field by field, is in `ai-policy.example.yaml` (fully commented) and the maintainers deck
- `ai-policy.schema.yaml` defines every value; the presets live in `examples/`
