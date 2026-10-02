# Slide decks

Reveal.js decks for the `ai-policy.yaml` proposal. The engine — reveal.js setup, styles, deck assembly, speaker view, spotlight, clicker bindings, Mermaid and QR rendering — is the [deck-engine](https://codeberg.org/open-source-ecosystem/deck-engine) package, pinned by tag in `package.json`. Its README is the reference for deck structure, per-deck `<meta>` settings, freezing a talk, speaker notes and keyboard shortcuts; this file covers only what is specific to these decks.

## Layout

```
decks/
  vite.config.js                 engine configuration and the shared footer
  index.html                     landing page linking every deck
  assets/                        images shared by every deck
  maintainers/                   maintained deck: for open source maintainers
  ecosystem/                     maintained deck: the why and the design
  talks/<conference>-<date>/     a talk as it was actually presented, frozen (none yet)
```

To move to a new engine release, install its tag (`npm install -D git+https://codeberg.org/open-source-ecosystem/deck-engine.git#<tag>`, which updates both `package.json` and the lockfile) and check every diagram slide before committing.

## Run locally

Requires a current Node.js LTS release.

```sh
npm install
npm run start
```

Open the local address printed by Vite and navigate to `/maintainers/` or `/ecosystem/`. Press `S` for the speaker view. Build a static version with `npm run build`; the output is written to `dist/`.

## Hosting on Codeberg Pages

The repository root ships a `.woodpecker.yml` pipeline that builds every deck and publishes it to [Codeberg Pages](https://docs.codeberg.org/codeberg-pages/) under `https://open-source-ecosystem.codeberg.page/ai-policy/`, by force-pushing `decks/dist` to the `pages` branch.

It runs only when a push to `main` touches `decks/**` or the pipeline file itself, so commits to the documents spend no shared CI capacity; the decks link into those documents by URL, so a docs-only change never leaves them stale. Trigger a manual run in Woodpecker to force a rebuild.

One-time setup, not yet done: activate the repository in Codeberg's Woodpecker, add a Codeberg deploy key with write access, and store its private key as the repository secret `codeberg_ssh_key`.

## Slide conventions

- Horizontal slides (`---`) carry the talk; vertical slides (`--`) are optional depth reached with the down arrow, and each carries `<!-- .slide: data-timing="0" -->` so skipping it never skews the pacing indicator.
- Keep the slide body short: about four bullets of around fifty characters and a one- or two-line bold punchline. Detail belongs in the notes, not on the slide.
- `Note:` blocks open with the live speaking cues; a `**Q&A details:**` label separates reference material to reach for only when asked. A `↓ <title>` line at the top names the vertical below.
- Define a term on or before the first slide that relies on it. Field names, enum values and resolution rules are the [schema](../ai-policy.schema.yaml)'s and the [README](../README.md#resolution)'s, exactly as written there: field names are case-sensitive.
- YAML on a slide validates against the schema, or is labelled as an excerpt. Re-validate every example when the schema changes, since the top level uses `unevaluatedProperties: false`.
- Link into the documents generously: inline links on key terms in bullets and table cells cost no slide height, and a `↳ …` line under the punchline names the section to read next. Both point at `##` sections by full Codeberg URL, so they resolve from the published deck. Diagram nodes cannot carry links (see the deck-engine README); put them in the slide text or a vertical.
- The format is an early proposal, its design not settled. Keep hedges visible: anything the README lists under its open questions stays an open question on the slide or in its notes.
- Follow the repository's [AGENTS.md](../AGENTS.md): quotations verbatim, every URL fetched, and this repository's own policy values never restated in prose.

## Related decks

The same engine builds the decks of the sibling repositories:

- [publiccode-metadata](https://codeberg.org/open-source-ecosystem/publiccode-metadata/src/branch/main/decks) — the publiccode.yml evidence layer, for developers and for policy makers and buyers
- [oss-levy](https://codeberg.org/open-source-ecosystem/oss-levy/src/branch/main/decks) — extended producer responsibility for digital infrastructure, for policy makers and legal reviewers
- [deployment-inventory](https://codeberg.org/open-source-ecosystem/deployment-inventory/src/branch/main/decks) — knowing what runs: the deployment inventory pipeline, for engineers
- [opencode-forges](https://codeberg.org/open-source-ecosystem/opencode-forges/src/branch/main/decks) — the public-sector forge roadmap, for technical policy makers
- [ai-model-sovereignty](https://codeberg.org/open-source-ecosystem/ai-model-sovereignty/src/branch/main/decks) — what a public institution needs in order to keep depending on an AI model, for policy makers

## The decks

### `maintainers/` — `ai-policy.yaml` for maintainers

The audience is open source maintainers who want to publish a policy, and the deck is a short, hands-on overview of the format. The arc runs from what the file is and why the prose it points at stays authoritative, through where it lives and what its absence means, to the main fields and the stance field-set. The middle shows how to adopt one: start from a preset in `examples/`, or work a policy out in the order the guide recommends, with `undecided` for what is still open. It then covers how a consumer resolves the file per scope, how whole-file fields compose with the stance, validating against the schema and how `summary` is derived, what tools can do with the file today, and closes on what a maintainer can do now and the open questions that concern them.

The horizontal spine runs about 16 minutes at the configured 90 seconds per slide; the verticals carry the YAML examples, the preset tables, the resolution rules and the validation detail for questions.

### `ecosystem/` — the why and the design

Why `ai-policy.yaml` exists, for people deciding whether to support or adopt it: maintainers, foundations, forges and AI-tool builders. It covers the gap (AI-contribution policies exist only as prose in unpredictable places), why the file is both an agent-tooling problem and a tool for structuring a project's own debate, the aims, the design principles behind "a signal, not a rule engine", how a file tells "no policy", "no AI rule needed" and "not yet decided" apart, what the corpus research found, what the format deliberately does not govern, and the adoption-first ask. It needs no YAML knowledge; the field-by-field format is the `maintainers/` deck.
