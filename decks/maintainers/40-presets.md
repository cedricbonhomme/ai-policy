## Start from a preset

- Copy a [preset from `examples/`](https://codeberg.org/open-source-ecosystem/ai-policy/src/branch/main/examples) as `ai-policy.yml`
- Put the matching [ai-policy.dev](https://ai-policy.dev/) `AI_POLICY.md` beside it
- Presets list the questions they leave open
- Decide them, mark them `undecided`, or delete them

**If you already know where you stand,<br />take a preset and skip the rest.**

[↳ Writing a policy: if you already know where you stand](https://codeberg.org/open-source-ecosystem/ai-policy/src/branch/main/writing-a-policy.md#if-you-already-know-where-you-stand)

Note:

↓ Presets that hold AI back

- A *preset* is a ready-made `ai-policy.yml` in `examples/`. Most express one of the ai-policy.dev prose policies, so the structured file and the prose it summarises ship together
- ai-policy.dev is a small library of `AI_POLICY.md` texts a project copies, in the manner of choosealicense.com. Its metadata is stripped when a policy is copied, so on its own an adopting repository publishes nothing a consumer can read
- Every preset but Neutral ends with a "Not addressed by this preset" section (a neutral file can carry no other AI-specific field): commented-out lines with their possible values. Uncomment one to decide it, list its name in `undecided` if you discussed it and could not agree, or delete the section; the preset is complete without it
- Research Only has no ai-policy.dev prose preset yet; Neutral points `statement` at your contribution guide

**Q&A details:**

- Commented lines mean nothing to a consumer
- `undecided` with a value keeps that value as the rule meanwhile (the working-it-out slide)

--

## Presets that hold AI back

<!-- .slide: data-timing="0" class="compact" -->

| Preset | Where you stand | `summary` |
| --- | --- | --- |
| [AI Disallowed](https://codeberg.org/open-source-ecosystem/ai-policy/src/branch/main/examples/ai-disallowed.yml) | no AI at all, not even translation | `disallowed` |
| [Research Only](https://codeberg.org/open-source-ecosystem/ai-policy/src/branch/main/examples/research-only.yml) | AI to understand and debug; nothing contributed | `disallowed` |
| [Human Responsible](https://codeberg.org/open-source-ecosystem/ai-policy/src/branch/main/examples/human-responsible.yml) | private tools; submission entirely yours, no AI notes | `restrictive` |

**Say what stays permitted,<br />or the policy reads as blanket hostility.**

[↳ Writing a policy: if you already know where you stand](https://codeberg.org/open-source-ecosystem/ai-policy/src/branch/main/writing-a-policy.md#if-you-already-know-where-you-stand)

Note:

↓ Presets that let AI in

- `summary` is derived from the stance, not chosen; the validation slide shows how
- AI Disallowed sets `allowedUses: []`: an empty list says explicitly that no use is exempt
- Research Only sets `allowedUses: [research, comprehension, debugging]`, uses whose output is never submitted. It is modelled on OpenJDK, with QEMU and Servo close variants
- Human Responsible sets `stance: assisted` and `disclosure: prohibited`, and holds comments, issue and pull request descriptions and commit messages at `disallowed`

--

## Presets that let AI in

<!-- .slide: data-timing="0" class="compact" -->

| Preset | Where you stand | `summary` |
| --- | --- | --- |
| [Human Copyright](https://codeberg.org/open-source-ecosystem/ai-policy/src/branch/main/examples/human-copyright.yml) | any tools; a human who can license it | `mixed` |
| [Human Voice](https://codeberg.org/open-source-ecosystem/ai-policy/src/branch/main/examples/human-voice.yml) | AI may write code; words are your own | `mixed` |
| [AI Disclosed](https://codeberg.org/open-source-ecosystem/ai-policy/src/branch/main/examples/ai-disclosed.yml) | AI welcome, as long as it is disclosed | `mixed` |
| [AI Allowed](https://codeberg.org/open-source-ecosystem/ai-policy/src/branch/main/examples/ai-allowed.yml) | any tools, agents included | `permissive` |
| [Neutral](https://codeberg.org/open-source-ecosystem/ai-policy/src/branch/main/examples/neutral.yml) | no AI-specific rule needed | `neutral` |

**`mixed`: AI may produce the substance,<br />with at least one AI-specific condition.**

[↳ Writing a policy: if you already know where you stand](https://codeberg.org/open-source-ecosystem/ai-policy/src/branch/main/writing-a-policy.md#if-you-already-know-where-you-stand)

Note:

↓ AI Disclosed, condensed

- The conditions behind `mixed` here: Human Copyright requires `provenance-attested`; Human Voice holds comments, issue and pull request descriptions at `disallowed`; AI Disclosed requires disclosure and holds `media` at `disallowed`
- AI Allowed is the only preset that sets `autonomousAgents.allowed: true`
- Agent autonomy never affects `summary`: it is a separate axis

--

## AI Disclosed, condensed

<!-- .slide: data-timing="0" -->

```yaml
version: 1
summary: mixed
statement: AI_POLICY.md
status: adopted
defaults:
  stance: generated
  disclosure: required
  humanReview: required
assertions:
  - scope: media
    stance: disallowed
autonomousAgents:
  allowed: false
```

Excerpt of [`examples/ai-disclosed.yml`](https://codeberg.org/open-source-ecosystem/ai-policy/src/branch/main/examples/ai-disclosed.yml); valid on its own

Note:

- Left out of the excerpt: `concerns`, `disclosureFormat` (`method: [free-text]`, `content: [tool, extent]`) and `enforcement` (`maintainer-review`, with a consequence sentence)
- With a `generated` default, `disclosure: required` and the `media` assertion are each enough to make the summary `mixed` rather than `permissive`; the schema checks it
- The `media` assertion overrides only `stance`; disclosure and human review inherit from `defaults`
- `autonomousAgents.allowed: false`: a person reviews and posts every submission
