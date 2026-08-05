# Machine-readability evaluation

Scoring `ai-policy.yml` against the five properties in the [IETF machine-readability draft](https://datatracker.ietf.org/doc/draft-vaughan-machine-readability/) (`draft-vaughan-machine-readability`), which decomposes "machine-readable" into *parseable, interpretable, discoverable, actionable, verifiable*. The draft defines no passing grade; it is a rubric for stating honestly what a format delivers.

| Property | Rating | Notes |
|---|---|---|
| **Parseable** | Full | YAML with a published JSON Schema ([`ai-policy.schema.yaml`](./ai-policy.schema.yaml)); any conforming parser recovers the structure, and the schema catches malformed instances. |
| **Interpretable** | Partial | The controlled vocabularies (`stance`, `scope`, `requirements`, `concerns`, openness components…) give shared meaning, but the terms are **local strings, not URIs bound to a shared, identified vocabulary**, which is the draft's bar for *interpretable*. A JSON-LD `@context` mapping each enum to a dereferenceable term would close this. `notes` and `statement` are deliberately free prose, not machine-interpretable, by design. |
| **Discoverable** | Full-ish | Conventional location (`ai-policy.yml` in version control), plus `.well-known/` and typed peer-record pointers; **absence is itself a signal** (no declared policy). |
| **Actionable** | Full | A consumer can act on it: gate or annotate a PR, warn a contributor, aggregate a badge. Resolution is deterministic (per-`scope`), so two consumers reach the same decision from the same file. |
| **Verifiable** | Partial, by design | The format **declares intent**; it does not, and cannot, prove that a contribution was AI-generated (undetectable in the general case). Verifiability applies to the *checkable* parts: `requirements` gates (tests pass, provenance attested), signed-commit `attestation`, the human `signoff`. The draft's rejection of LLM-based interpretation matches this format's "declare, don't adjudicate" principle. |

**Headline:** parseable, discoverable, and actionable today; **interpretability is the open gap** (a shared `@context` for the enums), and **verifiability is intentionally bounded** to what can honestly be checked. Both align with the format's core stance: a *signal, not a proof*.
