# Agent instructions

**The policy is not in this file.** [`ai-policy.yaml`](./ai-policy.yaml) is the machine-readable answer to what this repository permits — whether generated contributions are accepted, whether disclosure is expected, whether an autonomous agent may open a pull request, and what AI may do in review. [`AI_POLICY.md`](./AI_POLICY.md) is its authoritative prose. Read the first, and the second where the first says `exceptions: true`.

This file deliberately does not restate those values. A project that publishes a structured policy and then paraphrases it in prose has three copies to keep in step and no way to notice when they diverge — and this repository proposes the structured layer, so it is the last place that should hedge against it. What follows is only what the fields cannot carry.

## Verification in this repository

`ai-policy.yaml` declares `humanReview: required`, and `AI_POLICY.md` says submitting a change means you have understood and verified it. Those are the rule. Below is what verifying actually means *here*, because this repository is largely prose making checkable claims about other people's policies, and that is where AI assistance fails in a way generic care does not catch. This is what [`ai-policy.yaml`](./ai-policy.yaml) points at as `guardrailsRef`.

- **Every URL you add or change has been fetched.** Policies move and get rewritten. A dead link is the obvious failure; a live link whose text no longer says what the sentence claims is the common one.
- **Quotations are verbatim.** Anything inside quotation marks matches the source character for character. Paraphrase freely — but not inside quotation marks, and not while naming the source.
- **Schema changes validate across all three files.** `ai-policy.schema.yaml`, `ai-policy.example.yaml`, `ai-policy.yaml` and the files in `examples/` move together; the top level uses `unevaluatedProperties: false`, so a field added to one and not the others fails. Enum values used in `coverage.md` mappings must exist in the schema.
- **Claims about the corpus survive your change.** [`coverage.md`](./coverage.md) is full of counts, "the corpus's only", and "no policy in either survey does X". Adding or rescoring one policy can falsify a sentence three sections away, most often in the cross-cutting findings and the Specificity tables. Re-read those two sections after touching any entry.

## Conventions

- **Prose is not hard-wrapped.** One paragraph is one line.
- **Structure only what recurs.** Nuance belongs in a `notes` string rather than a new enum; collecting `notes` across adopters is how the next field gets chosen. See the [design principles](./README.md#how-its-designed-a-signal-not-a-rule-engine).
- **Named, not numbered.** Referenceable list items carry titles, so references survive reordering.
