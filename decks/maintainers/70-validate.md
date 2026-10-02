## Validate against the schema

- [`ai-policy.schema.yaml`](https://codeberg.org/open-source-ecosystem/ai-policy/src/branch/main/ai-policy.schema.yaml): JSON Schema, draft 2020-12
- Authored in YAML; convert to JSON if a tool needs it
- Unknown or misspelt fields fail
- A file that declares nothing fails

**A `summary` that contradicts the stance<br />fails validation, not just review.**

[↳ Writing a policy: point at the prose and finish](https://codeberg.org/open-source-ecosystem/ai-policy/src/branch/main/writing-a-policy.md#working-it-out)

Note:

↓ One way to check it

**Acronyms:** CLI = command-line interface; CI = continuous integration; MCP = Model Context Protocol

- The guide ends on this step: validate the file against the schema, then point `AGENTS.md` and `CONTRIBUTING.md` at it
- The top level uses `unevaluatedProperties: false`, as does every nested object, so a typo or a field that does not exist is an error. Field names are case-sensitive. The one open map is `disclosureFormat.trailers`: its keys name degrees of involvement and are free, so any key is accepted there
- A file with only `version` and `status` fails: neither declares a rule or an open question
- `summary` is derived, not chosen, and the schema enforces that it agrees with the stance (vertical after next)

**Q&A details:**

- The schema's `$id` is a placeholder until a home is chosen
- The reference reader or validator (a CLI, a CI action or an MCP server) is itself an open question in the README, *Smallest consumer*

--

## One way to check it

<!-- .slide: data-timing="0" -->

```python
import yaml, jsonschema

schema = yaml.safe_load(open("ai-policy.schema.yaml"))
policy = yaml.safe_load(open("ai-policy.yml"))
jsonschema.Draft202012Validator(schema).validate(policy)
```

- Python with `pyyaml` and `jsonschema`
- Any full draft 2020-12 validator works

**Raises on an invalid file; silent when valid.**

[↳ The schema: `ai-policy.schema.yaml`](https://codeberg.org/open-source-ecosystem/ai-policy/src/branch/main/ai-policy.schema.yaml)

Note:

↓ How the summary is derived

- A sketch, not a published tool: run it from a checkout holding the schema next to your file
- The validator must implement draft 2020-12 in full, because the schema's strictness relies on `unevaluatedProperties`; one that ignores it accepts unknown fields silently. It must also read YAML, or take the schema converted to JSON
- To list every error rather than one, iterate `iter_errors(policy)` instead of calling `validate`

--

## How the summary is derived

<!-- .slide: data-timing="0" class="compact" -->

| `defaults.stance` | [`summary`](https://codeberg.org/open-source-ecosystem/ai-policy/src/branch/main/README.md#resolution) |
| --- | --- |
| `disallowed` | `disallowed` |
| `assisted` | `restrictive` |
| `generated` | `permissive` |
| `generated` + an AI-specific condition | `mixed` |
| no AI-specific rule at all | `neutral`, standing alone |

**Agent autonomy does not count:<br />it is a separate axis.**

[↳ README: resolution](https://codeberg.org/open-source-ecosystem/ai-policy/src/branch/main/README.md#resolution)

Note:

- `summary` is optional, a convenience for aggregators that do not resolve the file. A summary that is a matter of opinion would be the least clear field in the file
- An AI-specific condition: a scope held below `generated`, disclosure `required` or `prohibited`, a `requirements` gate, a non-empty `priorArrangement` (`appliesTo`), or a `newContributors` rule
- Without a default stance a file carries no `summary` (other than `neutral`)
- `summary: permissive` with `disclosure: required` fails validation
