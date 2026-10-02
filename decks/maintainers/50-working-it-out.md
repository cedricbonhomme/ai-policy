## Still working it out?

- [Settle the common ground](https://codeberg.org/open-source-ecosystem/ai-policy/src/branch/main/writing-a-policy.md#working-it-out) first
- Name your [`concerns`](https://codeberg.org/open-source-ecosystem/ai-policy/src/branch/main/writing-a-policy.md#working-it-out) before choosing rules
- Give each concern its narrowest lever
- Argue the stance last

**"Should we allow AI?" is the question<br />most projects start with, and the worst place to start.**

[↳ Writing a policy: working it out](https://codeberg.org/open-source-ecosystem/ai-policy/src/branch/main/writing-a-policy.md#working-it-out)

Note:

↓ Concerns meet levers

- Argued in the abstract, the stance question goes in circles: it bundles a dozen smaller questions people answer differently for different reasons. The order unbundles it
- Common ground, which published policies mostly answer alike: `humanReview: required`, `accountability: contributor`, `review.humanDecision: required`, whether `autonomousAgents.allowed`, whether communication must be in the contributor's own words, and any existing `signoff`
- Own-voice scopes: `assertions[]` with `stance: disallowed` on `comments`, `issue-descriptions` and `pull-request-descriptions`, usually with `allowedUses: [translation, spelling-grammar]`
- Concerns come from a shared list: `code-quality`, `security`, `ip-provenance`, `licensing-ethics`, `data-consent`, `labor-ethics`, `skill-preservation`, `environmental`, `oss-sustainability`; say them in your own words in `concerns.notes` too
- Then the mechanics: `disclosureFormat`, `attestation`, `enforcement`; and finally the pointers: `statement`, `exceptions`, `status`, `summary`

**Q&A details:**

- Two people arguing over the stance are often arguing about different things, one about review load and the other about licensing; named concerns can be answered one at a time
- `concerns` changes nothing a consumer does; it shows aggregators what moves projects
- A concern missing from the list goes in `notes`: that is how the list grows

--

## Concerns meet levers

<!-- .slide: data-timing="0" class="compact" -->

| Concern | [Narrowest lever](https://codeberg.org/open-source-ecosystem/ai-policy/src/branch/main/writing-a-policy.md#working-it-out) |
| --- | --- |
| `code-quality` | `requirements`, e.g. `tests-pass`, `ci-green` |
| `oss-sustainability` | `priorArrangement`, `newContributors` |
| `security` | a `security-reports` scope with `reproduced` |
| `skill-preservation` | `newContributors`, the own-voice scopes |
| `environmental` | none: only the stance answers it |

**Some concerns only the stance can answer.**

[↳ Writing a policy: give each concern its narrowest lever](https://codeberg.org/open-source-ecosystem/ai-policy/src/branch/main/writing-a-policy.md#working-it-out)

Note:

↓ Open is not absent

- `labor-ethics` and `environmental` are objections to the tools themselves, not to how they are used; no gate answers them, and that is exactly what the stance is for
- If every concern found a lever, `stance: generated` is usually where a project lands, and the levers carry the load
- `newContributors` applies to contributors with no merged contribution yet: a stricter stance (`disallowed` or `assisted`), and `issuesHumanOnly` to reserve "good first issue" tickets for human authorship
- `priorArrangement` gates kinds of contribution (`agent-submissions`, `bulk-changes`, `ai-generated-prs`) on agreement before submission, with a `basis`: `accepted-issue`, `reviewer-agreement`, `governance-body` or `discussion`

**Q&A details:**

- More levers from the guide: `ip-provenance` gets `requirements: [provenance-attested]`, `disclosure: required` and `models.policy.openness.trainingData`; `oss-sustainability` also `requirements: [reproduced]` and `enforcement.mechanism: [denylist]`; `security` also `no-generated-in-security-paths` and `no-sensitive-data-to-3p`
- `licensing-ethics` and `data-consent`: `models.policy.openness`, a floor on which models may be used at all

--

## Open is not absent

<!-- .slide: data-timing="0" -->

```yaml
version: 1
status: under-discussion
statement: CONTRIBUTING.md
undecided: [defaults.stance, autonomousAgents]
defaults:
  stance: generated     # interim: accepted while we decide
  humanReview: required
```

- Listed with a value: the rule in force meanwhile
- Listed without one: never read as permission

**No step has to block you.**

[↳ README: resolution](https://codeberg.org/open-source-ecosystem/ai-policy/src/branch/main/README.md#resolution)

Note:

- `undecided` names questions the project has considered and not settled, distinct from fields it has not addressed at all
- Here `defaults.stance` carries `generated`, so AI contributions are accepted while the project decides; with `disallowed` it would mean not until it has decided
- `autonomousAgents` is listed with no value: no interim rule, and because it grants or withholds something, a consumer applies the restrictive reading
- A field neither declared nor listed is simply not addressed; the consumer refers to `statement`
- No `summary` here: it is optional, and a file can omit it

**Q&A details:**

- Open question: `undecided` names whole-file fields and the `defaults` field-set only, so a project cannot yet say its stance on `code` is settled while `docs` is open
