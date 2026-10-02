## How a consumer resolves it

- [`defaults`](https://codeberg.org/open-source-ecosystem/ai-policy/src/branch/main/README.md#resolution) is the base for every field
- An `assertions[]` entry overrides it for one `scope`
- Fields the entry omits inherit from `defaults`
- [`actorExceptions`](https://codeberg.org/open-source-ecosystem/ai-policy/src/branch/main/README.md#resolution): a signal, not a layer

**Per content type, field by field:<br />applied by the consumer, never encoded in the file.**

[↳ README: resolution](https://codeberg.org/open-source-ecosystem/ai-policy/src/branch/main/README.md#resolution)

Note:

↓ Resolution, worked

- A consumer resolves the effective policy for a contribution by its `scope`, its content type: `code`, `docs`, `tests`, `comments`, `issue-descriptions`, `pull-request-descriptions`, `commit-messages`, `translations`, `media`, `security-reports`
- A scope absent from `assertions[]` resolves from `defaults`; omitting `assertions[]` altogether is valid
- The README compares the layering to a browser applying the CSS cascade
- `actorExceptions` declares that a named actor, such as maintainers, is governed differently; a consumer surfaces it and reads its `notes` and `statement`. Only its `autonomousAgentsAllowed` carve-out is machine-actionable

**Q&A details:**

- `newContributors` tightens, never loosens: for a contributor with no merged contribution yet, the stricter of `newContributors.stance` and the scope's own stance applies
- Is `disallowed < assisted < generated` genuinely ordinal for every project? Open question

--

## Resolution, worked

<!-- .slide: data-timing="0" -->

```yaml
version: 1
defaults:
  stance: generated
  disclosure: encouraged
  humanReview: required
assertions:
  - scope: comments
    stance: disallowed
  - scope: security-reports
    disclosure: required
    requirements: [reproduced]
```

**`code` inherits everything;<br />each entry changes only what it sets.**

[↳ README: resolution](https://codeberg.org/open-source-ecosystem/ai-policy/src/branch/main/README.md#resolution)

Note:

↓ Whole-file fields compose

- Resolved: a `code` change is `generated`, disclosure `encouraged`; a comment is `disallowed`; a security report is `generated`, disclosure `required`, and must be `reproduced`
- `code` has no entry, so it resolves entirely from `defaults`
- The `comments` entry sets only `stance`; disclosure and `humanReview: required` still inherit
- The `security-reports` entry keeps the default stance and tightens disclosure and requirements
- `humanReview: required` applies to every scope here
- No `summary` here; if one were set it would have to be `mixed`, since a scope is held below `generated`

--

## Whole-file fields compose

<!-- .slide: data-timing="0" class="compact" -->

| Field | Question it answers |
| --- | --- |
| `stance` (per scope) | may this kind of contribution be offered at all? |
| [`priorArrangement`](https://codeberg.org/open-source-ecosystem/ai-policy/src/branch/main/README.md#resolution) | may it be offered without agreement first? |
| [`autonomousAgents`](https://codeberg.org/open-source-ecosystem/ai-policy/src/branch/main/README.md#resolution) | may a non-human do the offering? |
| [`review`](https://codeberg.org/open-source-ecosystem/ai-policy/src/branch/main/README.md#resolution) | what will the project do with it afterwards? |

**Permitted by `stance` and caught by `priorArrangement`<br />is permitted and gated, not contradictory.**

[↳ README: resolution](https://codeberg.org/open-source-ecosystem/ai-policy/src/branch/main/README.md#resolution)

Note:

- These fields apply to the file as a whole: they do not cascade, and they do not override the stance. A consumer satisfies each independently rather than picking a winner
- `review.aiAssist` (`disallowed`, `permitted`) says whether AI may assist a reviewer; `review.humanDecision: required` means an AI review is never sufficient on its own
- `autonomousAgents.attestation.identity` says how agents identify themselves: `bot-account`, `signed-commits`, `integration-manifest`

**Q&A details:**

- Still open: `priorArrangement` has a list of triggers but a single `basis`, so a project that gates two kinds of contribution on different bases cannot state both in one file
