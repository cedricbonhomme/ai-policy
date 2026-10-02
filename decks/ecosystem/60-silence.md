## Open is not absent

| What the project publishes | What it means |
| --- | --- |
| **No file** | No declared policy |
| **`summary: neutral`** | Considered AI; no rule of its own needed |
| **`undecided`** | Discussed, not yet settled |

**A prose policy cannot say<br />which kind of silence it is.**

[↳ README: resolution](https://codeberg.org/open-source-ecosystem/ai-policy/src/branch/main/README.md#resolution)

Note:

↓ Publishing before everything is settled

- Absence is itself a signal: *no declared policy*, distinct from a declared permissive one
- `summary: neutral` is Kubernetes' position: the steering committee decided generative AI needs no dedicated rule, and the ordinary contribution rules govern every contribution
- `undecided` names what is still open, with or without the rule that applies meanwhile
- In the larger corpus of popular projects (Hora, Robbes and Zacchiroli, 2026; more later), 58% of policies say nothing about AI in communication and 69% nothing about issues and security: that silence is why *absent* and `undecided` are kept apart

**Q&A details:**

- Every field is optional, but a file must declare something: a stance, any other rule, an open question in `undecided`, or `summary: neutral`
- A neutral file carries no other AI-specific field, and a consumer applies no AI-specific gate

--

## Publishing before everything is settled

<!-- .slide: data-timing="0" -->

- A project should not invent an answer to publish
- Nor let silence pass for a decision
- An open field can still carry an **interim rule**
- With no interim rule, never read as permission

**Partial adoption is honest,<br />and the open questions stay on the agenda.**

[↳ Coverage: under discussion / proposed](https://codeberg.org/open-source-ecosystem/ai-policy/src/branch/main/coverage.md#under-discussion-proposed-not-settled)

Note:

- QGIS is the case that shaped `undecided`: QEP-408 is adopted and governs *how* AI contributions are handled, but states it is not settled whether LLM code is acceptable at all
- `undecided: [defaults.stance]` with `stance: generated` means accepted while we decide; with `stance: disallowed`, not until we have decided
- Where an open field without a value grants or withholds something (`stance`, `autonomousAgents`, `review`), a consumer applies the restrictive reading; elsewhere it refers to `statement`

**Q&A details:**

- QEP = QGIS Enhancement Proposal
