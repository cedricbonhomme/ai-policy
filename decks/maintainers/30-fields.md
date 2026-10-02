## The main fields

<!-- .slide: class="compact" -->

| [Field](https://codeberg.org/open-source-ecosystem/ai-policy/src/branch/main/README.md#the-format-in-brief) | Answers |
| --- | --- |
| `defaults`, `assertions[]` | may AI produce this, disclosed how? |
| `autonomousAgents` | may a non-human do the offering? |
| `priorArrangement` | is agreement needed before submitting? |
| `review` | what may AI do in the project's review? |
| `allowedUses` | which AI uses produce no contribution? |
| `undecided` | what is still open? |

**Every field is optional,<br />but a file must declare something.**

[↳ README: the format in brief](https://codeberg.org/open-source-ecosystem/ai-policy/src/branch/main/README.md#the-format-in-brief)

Note:

↓ The stance field-set

**Acronyms:** DCO = Developer Certificate of Origin; CLA = contributor licence agreement

- `defaults` is the base rule for every content type; `assertions[]` is a list of per-scope overrides, where a *scope* is a content type such as `code`, `docs` or `comments`
- Agent autonomy is a separate axis, never a stance value: a project can accept generated code from people and still bar agents from opening pull requests
- *Something* means: a stance, by default or for a single scope, any other rule, an open question in `undecided`, or `summary: neutral`
- The schema defines the core values, among them every stance, disclosure, scope, requirement and concern; the commented example explains each field

**Q&A details:**

- Further fields: `concerns` (why the project holds its stance; changes nothing a consumer does), `newContributors`, `actorExceptions`, `disclosureFormat`, `enforcement`, `signoff` (`none`, `dco`, `cla`), `models.policy`, plus `summary`, `status` and `version`
- `models` is the AI used to *build* the project, not AI the product ships at runtime
- `allowedUses` values: `research`, `comprehension`, `bug-triage`, `debugging`, `accessibility`, `spelling-grammar`, `translation`. Assistance whose output is contributed is `stance: assisted`, not an allowed use

--

## The stance field-set

<!-- .slide: data-timing="0" class="compact" -->

| Field, in `defaults` or `assertions[]` | Values |
| --- | --- |
| [`stance`](https://codeberg.org/open-source-ecosystem/ai-policy/src/branch/main/ai-policy.schema.yaml) | `disallowed`, `assisted`, `generated` |
| `disclosure` | `prohibited`, `none`, `encouraged`, `required` |
| `humanReview` | `none`, `required` |
| `accountability` | `contributor` |
| `requirements` | gates, e.g. `tests-pass`, `reproduced` |

**Stance is permission, not preference.**

[↳ README: how it's designed](https://codeberg.org/open-source-ecosystem/ai-policy/src/branch/main/README.md#how-it-s-designed-a-signal-not-a-rule-engine)

Note:

- `stance`: `disallowed` means nothing produced by AI; `assisted` means AI may help only menially (completion, find-and-replace, mechanical refactoring) and the substance is the contributor's; `generated` means AI may produce the substance, subject to the rest of the file
- `disclosure`: `prohibited` means leave notes about AI tools out, so an agent that adds a trailer by habit must not; `none` not asked for; `encouraged` welcome, nothing gated on it; `required` a contribution without it may be refused
- `humanReview` is the *contributor's* involvement: they have personally reviewed, understood and tested the change. The project's own review is `review.humanDecision`
- `accountability: contributor`: whoever submits answers for all of it, AI-produced parts included. Absent means the policy does not say
- `notes` is in the set as well

**Q&A details:**

- All `requirements` values: `tests-pass`, `new-tests-required`, `ci-green`, `type-check`, `no-generated-in-security-paths`, `provenance-attested`, `prompt-logs-retained`, `no-sensitive-data-to-3p`, `reproduced`. Each is a gate the contributor can check before submitting
- The set is defined once in the schema as a reusable `$ref`, so "same fields" in `defaults` and `assertions[]` is a structural guarantee
- Field names are case-sensitive: `Stance` fails validation
