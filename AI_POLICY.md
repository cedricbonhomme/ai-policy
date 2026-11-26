# AI-contribution policy

This project welcomes contributions made with AI assistance and contributions made without it. The machine-readable summary is in [`ai-policy.yaml`](./ai-policy.yaml); this document is its authoritative human-readable statement and covers what the structured fields cannot (yet) express.

## No coercion, no discrimination

Using an AI tool is never required, and it is never prohibited by default. No contributor is pressured to adopt AI to be taken seriously, and no contributor is shamed for using it or for choosing not to. Contributions are judged on the change, not on how it was produced.

(This clause has no dedicated field in the `ai-policy` format yet; it is the open "Contributor opt-out / non-discrimination" question. Expressing it here in prose, with `exceptions: true` set in `ai-policy.yaml`, is the intended illustration of how a project covers a concern the structured fields do not reach.)

## Human review

Responsibility is two-sided. The contributor who submits a change vouches for it as their own: AI may have helped write it, but submitting it means you have understood and verified it, not forwarded unchecked model output. The maintainer who reviews it then takes responsibility for merging it. AI can help write a change; it cannot own the decision to propose one or the decision to accept it.

## Disclosure

Note AI involvement where it is material — in the pull request description, the commit message, or wherever authorship is normally indicated. It is encouraged, not required, and nothing is gated on it: a change is not rejected for lacking a note, and a disclosed change gets no lesser review. The point is to help a reviewer calibrate, not to track provenance, and certainly not to sort contributors into categories, which the clause above rules out.

When you note it in a commit, end the commit message with a `Co-Authored-By` trailer naming the model and its version, for example `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`. A tool can then read it, as [Say which AI](https://www.saywhichai.org) does. This format applies since 26 November 2026, when this repository was taken over; it is still encouraged, not required.

This is `disclosure: encouraged` and `disclosureFormat` in [`ai-policy.yaml`](./ai-policy.yaml).

## No sign-off ceremony

There is no DCO or CLA. The human review above is the accountability mechanism.
