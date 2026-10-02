## Where it lives

- [`ai-policy.yaml`](https://codeberg.org/open-source-ecosystem/ai-policy/src/branch/main/README.md#placement) or `.yml`, in version control
- Normally at the repository root
- Or a peer record pointing at it, e.g. `publiccode.yml`
- Or under `.well-known/`

**No file means no declared policy:<br />not the same as a permissive one.**

[↳ README: placement](https://codeberg.org/open-source-ecosystem/ai-policy/src/branch/main/README.md#placement)

Note:

↓ Neutral is a decision

- Both extensions are accepted; the YAML project recommends `.yaml`. If both files exist, `ai-policy.yaml` wins, and a consumer warns unless the two are byte-identical or one is a symbolic link to the other
- Discovery, in order of preference: the repository root, then a peer record that points at it, then `.well-known/ai-policy.yaml` or `.yml`
- Absence is itself a signal: no declared policy. It is distinct from a declared permissive policy, and from `summary: neutral` (next slide)
- The primary subject is code, but the `scope` vocabulary spans docs, translations, media and discussion, so it applies to any contribution type
- Point your `AGENTS.md` and `CONTRIBUTING.md` at it, so agents and people find it where they already look

**Q&A details:**

- Still open: the registered `type` string and pointer shape for peer records, such as a `publiccode.yml` `externalMetadata` entry
- Deliberately out of scope: platform self-commitments, hosting and content restrictions, governance-process rules. None concerns a contribution's lifecycle; the README's "What this format does not govern", under Placement

--

## Neutral is a decision

<!-- .slide: data-timing="0" -->

```yaml
version: 1
summary: neutral
statement: CONTRIBUTING.md   # the ordinary contribution rules that apply
status: adopted
```

- [`examples/neutral.yml`](https://codeberg.org/open-source-ecosystem/ai-policy/src/branch/main/examples/neutral.yml), header comment left out
- `summary: neutral` stands alone: no other AI-specific field

**Considered AI, and decided it needs no rule of its own.**

[↳ README: resolution](https://codeberg.org/open-source-ecosystem/ai-policy/src/branch/main/README.md#resolution)

Note:

- This is Kubernetes' position, per the README: the ordinary contribution rules at `statement` govern every contribution, however it was made
- A consumer applies no AI-specific gate to a neutral file
- The schema enforces it: a neutral file that also sets, say, `autonomousAgents` fails validation
- So these are distinct signals: no file (nothing declared), `neutral` (considered, no AI rule), and a declared policy of any stance
