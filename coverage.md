# `ai-policy`: coverage against real policies

How well does the [`ai-policy` format](./README.md) capture real open-source AI-contribution policies? This tests it against the policies curated by the [CHAOSS AI-alignment working group](https://github.com/chaoss/wg-ai-alignment/tree/main/moderation) (the primary source list), plus a few beyond it (Debian's GR). It is the **evidence base for the proposal**: if the format can express the real spread of policies, its shape is validated.

## Add a policy (PRs welcome)

This survey is open: **contribute a policy by pull request.** Point at a real, public AI-contribution policy (settled, or a live discussion), and score it against the format:

1. Add a **row** to the Summary table and a short **per-policy note**, in the shape of the existing entries.
2. Give it a **tier** (reject / restrict / accept-with-conditions / neutral) and a **fit rating** (Full / Good / Partial / Signal-only, defined below).
3. In *Maps via*, list the fields it exercises; in the gap column, note what needs prose or `exceptions`, or what the format can't express.
4. Add its URL to the **Sources** table.

The most valuable contribution is a policy the format **can't** capture: that points at a missing dimension or an open question; record it in the cross-cutting findings so it can feed the design.

## What "captures" means here

By design (`ai-policy`'s guiding principle) the field is a **signal that boundaries exist and their broad shape**, not an exhaustive rule engine; the authoritative detail lives in the human-readable `statement`, and an `exceptions: true` flag marks where the structure is a simplification. So a policy is well captured when the schema conveys the right **tier and operative boundaries**, even if some nuance is left to prose. Fit ratings:

- **Full**: every operative rule maps to a field; prose adds only rationale.
- **Good**: tier and all major boundaries map; minor nuance flagged by `exceptions: true`.
- **Partial**: tier and rough shape map, but material operative rules live only in prose.
- **Signal-only**: schema conveys "a policy exists + rough stance"; substance is prose.

Every mapping below assumes `statement` points at the human policy and (where noted) `exceptions: true` is set.

## Summary

| Policy | Tier | Fit | Maps via | Needs prose / gap |
|---|---|---|---|---|
| GCC | reject (significant) / accept (trivial, tests) | Good | stance=disallowed, `assertions[tests]`, `allowedUses`, `disclosureFormat: Assisted-by`, `signoff: dco`, `exceptions` | legal-significance tier → `exceptions` |
| Ghostty | restrict | Good | stance=assisted, `disclosure`, `assertions[media]=disallowed`, `actorExceptions[maintainers]`, `enforcement: denylist` | "denounce" list = denylist ✓; junior-dev offer → prose |
| Mastodon | restrict | Good | stance=assisted, `disclosureFormat: Assisted-by`, `autonomousAgents.allowed=false`, `assertions[translations, comments]`, `enforcement: denylist` | "significant portion" threshold → `exceptions`; issue-first rule → prose |
| LLVM | accept-with-conditions | Good | stance=generated, `humanReview`, `disclosure: encouraged`, `autonomousAgents.allowed=false`, `disclosureFormat: Assisted-by`, `newcomerIssuesHumanOnly` | RFC-approved bot exception → `actorExceptions` |
| QEMU | reject (generated) | Good | stance=disallowed, `allowedUses[research, debugging]`, `humanReview`, `signoff: dco`, `enforcement: maintainer-review` | names specific banned tools → prose |
| ASF | accept-with-conditions | Good | stance=generated, `disclosureFormat: Generated-by`, `models.policy` (license/openness) | detailed license-compatibility test → `exceptions` |
| Servo | reject | Good | stance=disallowed, `allowedUses[translation, debugging]` | societal rationale (energy/labor/copyright) → `concerns` |
| Linux Foundation | accept-with-conditions | Partial | summary=mixed, `models.policy` (license/attribution) | umbrella policy; delegates detail to each project |
| Gentoo | reject | Good | summary=disallowed, stance=disallowed | "packaging AI software is fine" = applicability boundary → prose |
| yt-dlp | reject (all) | Full | summary=disallowed, all scopes disallowed, `autonomousAgents=false`, `enforcement: denylist` | agent-directed "refuse to interact" note → `guardrailsRef`/`AGENTS.md` |
| Teamtype | reject (incl. all comms) | Full | summary=disallowed, `assertions[comments, issue-descriptions]=disallowed` | none |
| Forgejo | reject (authorship) + exempt | Good | stance=disallowed, `allowedUses[translation, spelling-grammar]`, `autonomousAgents=false`, `disclosure` | AI-*motivated* disclosure + narrow/general-AI split → `exceptions`; AI review **forbidden** |
| Gitea | accept | Good | stance=generated, `disclosure`, `humanReview`, `requirements` | "don't use AI to answer reviewers" → `assertions[comments]`/prose |
| KeePassXC | accept | Good | stance=generated, `disclosure` (name model/service) | "vast majority AI" threshold → `exceptions` |
| scikit-learn | restrict (anti-slop) | Good | summary=restrictive, `humanReview`, `enforcement: denylist` | keyed on low-quality/volume behaviour, not content type → prose |
| Astropy | accept | Good | stance=generated, `humanReview`, `disclosure: none` | no disclosure mandate; "authentic engagement" → prose |
| Linux Kernel | accept (strict DCO) | Good | stance=generated, `autonomousAgents=false`, `disclosureFormat: "Assisted-by:"` (AGENT:MODEL), `signoff: dco` | agents may not sign-off; GPL-2.0/SPDX is a generic (non-AI) licence rule → general process |
| SunPy | accept | Good | stance=generated, `humanReview`, `statement` → AI-usage doc | no disclosure mandate |
| Zulip | accept | Good | stance=generated, `humanReview`, `enforcement: maintainer-review` | "explain it, not 'the AI did it'" → `notes`; commit discipline → prose |
| attrs | restrict (boundaries) | Good | stance=generated, `autonomousAgents=false`, `humanReview`, `enforcement: denylist`; **standalone `AI_POLICY.md`** | no-LLM-in-`Co-authored-by` → `autonomousAgents.attestation` |
| Ladybird | n/a (closed contribution) | n/a | n/a | maintainers-only project; `ai-policy` assumes an open-contribution model |
| OpenJDK | reject (generated) + private-use exempt | Good | summary=disallowed, all scopes/surfaces, `allowedUses[research, debugging, comprehension, code-review-assist]` | "interim" policy; a full one is pending |
| Jellyfin | restrict / accept-with-conditions | Good | stance=generated (code), `assertions[comments, issue-descriptions, pull-request-descriptions]=disallowed`, `assertions[translations]` (disclose), `humanReview`, `requirements`, `enforcement: denylist` | "no LLM metafiles (`.claude`)", commit-splitting, mark shared LLM tools → `exceptions`/prose |
| NLnet Labs | reject (code/docs) + exempts | Good | stance=disallowed, `assertions[security-reports]=assisted` (LLM fix in a vuln report is OK), `allowedUses[code-review-assist]`, `disclosure: required` | translation discouraged-but-allowed → `notes` |
| Castle Game Engine | accept-with-conditions | Good | stance=generated, `humanReview`, `assertions[comments, issue-descriptions]` (keep AI chats out) | "generate smaller pieces" guidance → prose |
| Godot | accept (licence-gated) | Good | stance=assisted, `models.policy`/`requirements` (MIT-compatible licences only), one-change-per-PR | full stance beyond licensing → deeper fetch pending |
| GDAL | restrict | Partial | summary=restrictive; rationale captured | rules not fully extracted; maintenance-burden + legal rationale → `concerns` |
| Flathub | n/a (app-content policy) | n/a | n/a | governs AI-generated *apps/media* submitted to the store, not code contributions |
| Python (CPython) | accept-with-conditions | Good | stance=generated, `humanReview`, `disclosure: encouraged`, `allowedUses[research]`, `enforcement: [maintainer-review, denylist]` | "don't bypass tests" → `requirements`/prose |
| FastAPI | accept (anti-slop) | Good | stance=generated, `humanReview`, `assertions[comments]`, `enforcement: [maintainer-review, denylist]` | "human-effort DoS" / effort-asymmetry → prose; discussion-first process → prose |
| AFNix | reject + tolerated non-creative uses | Good | stance=disallowed, `allowedUses[research, accessibility, debugging]`, `enforcement: [maintainer-review, denylist]` | "derived from AI content" scope → prose |
| postmarketOS | reject (all) | Good | summary=disallowed, stance=disallowed, `enforcement: [denylist]` | bans even *recommending* AI tools → prose; strong societal rationale → `concerns` |
| Matplotlib | accept-with-conditions | Good | stance=generated, `humanReview`, `disclosureFormat: pr-template` (AI-Disclosure field), `allowedUses[research, translation, spelling-grammar]`, `autonomousAgents=false`, `newcomerIssuesHumanOnly`, `enforcement: [maintainer-review, denylist]` | multi-project breadth rule → `exceptions` |
| pip-tools | accept-with-conditions | Good | stance=generated, `humanReview`, `assertions[comments, issue-descriptions, pull-request-descriptions]=disallowed` + `allowedUses[translation, spelling-grammar]`, `autonomousAgents=false`, `newcomerIssuesHumanOnly`, `enforcement: [maintainer-review, denylist]` | none (fully expressible) |
| PROJ | accept-with-conditions (from LLVM) | Good | stance=generated, `humanReview`, `disclosureFormat: pr-template + commit-trailer (Assisted-by)`, `autonomousAgents=false`, `allowedUses[code-review-assist]`, `enforcement: [maintainer-review, denylist]` | "extractive"/copyright → prose; verbatim policy reuse from LLVM |
| KDE (GSoC) | reject | Good | summary=disallowed, stance=disallowed, `concerns`(licensing/environmental) | AI translation *not* exempt (per-project); GSoC-scoped |
| Redox OS | reject (all) | Good | summary=disallowed, stance=disallowed, `humanReview`, `signoff: dco`, `enforcement: [maintainer-review, denylist]` | "not open to discussion"; anti-scraper infra (no SSH push) → prose |
| curl | accept-with-conditions | Good | stance=generated, `humanReview`, `assertions[security-reports]` (disclosure required + verify), `allowedUses[translation]`, `disclosureFormat: commit-trailer (Assisted-by)`, `enforcement: [maintainer-review, denylist]` | per-scope disclosure: `required` for security-reports, `encouraged` for translation |
| Oxide (RFD 576) | accept (encouraged) | Partial | summary=permissive, `humanReview`, `allowedUses[research, debugging, code-review-assist]` | values doc → mostly `statement`; **strong contributor-autonomy evidence** (bans LLM mandates *and* shaming); new *data-privacy* concern (no train-on-uploads); skeptical of blanket disclosure |
| OpenInfra Foundation | accept-with-conditions | Good/Full | stance=generated, `humanReview`, `signoff: dco`, `disclosureFormat: commit-trailer` (**two-tier: `Assisted-By:` / `Generated-By:`**), `models.policy` (recommend open-source + licence-compatible), `actorExceptions` (release/i18n bots) | two disclosure tiers by degree (`disclosureFormat.trailers`); `Generated-By:` from ASF (convergence) |
| W3C Advisory Board | position statement (not operative) | n/a | n/a | opportunities/risks + guardrails; not an operative contribution policy → `statement`-only |
| Haiku OS | reject (all) | Good | summary=disallowed, stance=disallowed, `guardrailsRef: AGENTS.md` | policy lives in **`AGENTS.md`**, validates the agent-facing pointer |

## Per-policy notes

### GCC: Good
Reject for *legally significant* LLM content, accept trivial (if marked) and test cases (even if significant). Maps: `defaults.stance: disallowed` + `assertions[{scope: tests, stance: generated}]` + `allowedUses` (research, debugging, accessibility, translation, spelling; GCC's "Personal Use") + `disclosureFormat: {trailer: "Assisted-by:"}`. The legal-significance tier and "trivial allowed if marked" is exactly what `exceptions: true` + prose now signals (the schema deliberately no longer models it). Human `Signed-off-by`/DCO and "an LLM may not commit" map to `signoff: dco` + `humanReview: required` + `autonomousAgents.allowed: false`.

### Ghostty: Good
Restrict for external contributors, maintainers exempt. Maps cleanly: `defaults.stance: assisted`, `disclosure: required` (tool names + extent → `disclosureFormat`), `assertions[{scope: media, stance: disallowed}]`, `actorExceptions[{actor: maintainers}]`, `enforcement.mechanism: [denylist]` (the public "denounce" list). **Prose:** the "we'll mentor you if you skip AI" offer and the "it's the people not the tools" framing.

### Mastodon: Good
Restrict, autonomous PRs banned, translations explicitly allowed, comments must be human. Maps: `stance: assisted`, `disclosureFormat: {trailer: "Assisted-by:"}`, `autonomousAgents.allowed: false`, `assertions[{scope: translations, stance: generated}, {scope: comments, stance: disallowed}]`, `enforcement: [denylist]`. **`exceptions`:** the "significant portion triggers disclosure" size threshold, and "open an issue before non-trivial changes."

### LLVM: Good
Accept with self-review; autonomous agents forbidden; **AI forbidden on "good first issue" tickets** (to protect learning); disclosure of substantial tool-generated content *recommended*. Maps: `stance: generated`, `humanReview: required`, `disclosure: encouraged`, `autonomousAgents.allowed: false`, `disclosureFormat: Assisted-by`, and the good-first-issue rule → **`newcomerIssuesHumanOnly`**. The RFC-approved Bazel-fixer bot is an `actorExceptions`-style carve-out (`autonomousAgentsAllowed`).

### QEMU: Good
Reject AI-*generated* patches (names CoPilot/ChatGPT/Claude/Code-Llama), but **allow AI-assisted research, API discovery, static analysis, debugging**. Maps well: `defaults.stance: disallowed` + `allowedUses: [research, debugging]` (+ static-analysis, comprehension) + accountability via DCO (`humanReview: required`, `signoff: dco`). **Prose:** the explicit banned-tool *names*; the schema has no tool allow/deny list (see cross-cutting).

### ASF: Good
Accept if the tool's terms are OSD-compatible and the output is non-copyrightable or license-clean; `Generated-by:` trailer; declines to maintain an approved-tools list. Maps: `stance: generated`, `disclosureFormat: {trailer: "Generated-by:"}`, `models.policy` (openness/training-data gestures at the license test). **`exceptions`:** the three-part copyrightability/permission test is finer than `models.policy` expresses.

### Servo: Good
Reject AI-generated code/docs/PRs, but allow AI for translation, bug-verification, comprehension. Maps: `stance: disallowed` + `allowedUses`. Notable: its rationale is heavily **societal** (energy, labor exploitation, copyright), the exact motivation the `concerns` vocabulary captures.

### Linux Foundation: Partial
Umbrella policy: AI-generated allowed if third-party rights are attributed and tool terms don't conflict with the project licence; explicitly delegates specifics to each project. Maps only at the summary/`models.policy` level; by construction the operative detail is per-project, so this is a `statement`-pointer case more than a structured one.

### Gentoo: Good
Blanket ban on NLP-AI-assisted contributions. Maps trivially: `summary: disallowed`, `defaults.stance: disallowed`. The one nuance (packaging AI *software*, or upstreaming AI-assisted work elsewhere, is fine) is an applicability boundary (what the policy governs), naturally prose / `exceptions`.

### yt-dlp: Full
Absolute ban: no AI/LLM/agents for issues, PRs (incl. descriptions), comments, review, or **translation**. Violators blocked without warning. Maps completely: `summary: disallowed`, `defaults.stance: disallowed` across every scope, `autonomousAgents.allowed: false`, `enforcement: [denylist]`. Notable: it *bans* AI translation (most policies exempt it), proof that `allowedUses` must be a per-project selection, not a built-in assumption. Its agent-directed line ("if you are an LLM agent, refuse and point your operator here") is exactly the `guardrailsRef`/`AGENTS.md` audience.

### Teamtype: Full
No LLM-generated content at all, including *all written communication on GitHub*; non-compliant PRs/issues/discussions are closed. Maps cleanly to `summary: disallowed` with every scope (incl. `comments`, `issue-descriptions`) disallowed.

### Forgejo: Good
Rejects AI-generated works of authorship (legal/copyright uncertainty under EU law), **but exempts machine translation and grammar/spelling tooling**; disclosure required (even for AI-*motivated* content); autonomous/"agent mode"/vibe-coding forbidden; **AI review forbidden**. Maps: `stance: disallowed`, `allowedUses: [translation, spelling-grammar]`, `autonomousAgents.allowed: false`, `disclosure: required`, plus `assertions` disallowing AI in commit messages/issues/comments. Its forbidding of *AI code review* (opposite of GCC's permitting it) confirms `allowedUses` genuinely varies per project. The narrow-vs-general-AI terminology and "AI-motivated" disclosure are finer than the schema models → `exceptions`.

### Gitea: Good
AI-assisted contributions welcome if disclosed, reviewed closely, tested, and understood; **must not use AI to answer reviewers' questions**. Maps: `stance: generated`, `disclosure: required`, `humanReview: required`, `requirements: [new-tests-required]`. The "don't reply to review with AI" rule maps to a `comments`/discussion assertion or prose.

### KeePassXC: Good
If AI wrote "the vast majority" of a submission (agent/vibe coding), you **must document** the service/model used; all submissions still get full review. Maps: `stance: generated`, `disclosure: required` (with model name → `disclosureFormat`). The "vast majority" trigger is a size/significance threshold → `exceptions`.

### scikit-learn: Good
Enforced via the Code of Conduct: users submitting low-quality or AI-generated content they don't understand may be **banned**; examples are behavioural (untriaged PRs, claiming many issues). Maps: `summary: restrictive`, `humanReview: required`, `enforcement: [denylist]`. The triggers are contributor-behaviour patterns, not content-type rules; correctly prose.

### Astropy: Good
Welcomes AI-assisted contributions but keeps expectations: human ownership/accountability, ability to explain all changes, licence compliance, authentic (non-"courier") engagement. Maps: `stance: generated`, `humanReview: required`. Notably **no disclosure requirement** → `disclosure: none`, showing disclosure is not universal. Explicitly builds on scikit-learn's policy (policy reuse in the wild).

### Linux Kernel: Good
Accept with strict DCO discipline: **AI agents MUST NOT add `Signed-off-by`** (only a human certifies the DCO); the human reviews everything and signs off; `Assisted-by: AGENT_NAME:MODEL_VERSION [TOOL]` trailer; GPL-2.0/SPDX compliance. Maps strongly: `stance: generated`, `autonomousAgents.allowed: false`, `signoff: dco`, `disclosureFormat: {method: commit-trailer, trailer: "Assisted-by:"}`. (GPL-2.0/SPDX licence compliance is a generic contribution rule, not AI-specific.) The `AGENT:MODEL_VERSION` format **directly validates** the schema's model+version disclosure note.

### SunPy: Good
Short: if you use generative AI, fully understand the changes and be able to explain why they're correct; a fuller AI-usage doc is linked. Maps: `stance: generated`, `humanReview: required`, `statement`/`guardrailsRef` → the linked doc. No disclosure mandate.

### Zulip: Good
Any tools (incl. AI) permitted, but you must understand and explain every change: "the answer to 'why is X an improvement?' should never be 'the AI did it'"; un-understood/untested AI PRs are closed without review. Maps: `stance: generated`, `humanReview: required`, `enforcement: [maintainer-review]`. The commit-discipline and "don't ask AI to add comments" guidance is prose / a `comments` assertion.

### attrs: Good (a standalone-file datapoint)
Publishes a **standalone `.github/AI_POLICY.md`**. Doesn't police authoring, but every contribution must be backed by a human who owns the copyright (**no LLM bots in `Co-authored-by:`**), no unsupervised agentic tools, and "DoS-by-slop" earns a permanent ban; DCO-style certification. Maps: `stance: generated`, `autonomousAgents.allowed: false`, `humanReview: required`, `signoff: dco`, `enforcement: [denylist]`. The "no LLM in `Co-authored-by`" is an agent-identity/attestation rule (`autonomousAgents.attestation`). That this policy is a *separate file* is direct evidence for the standalone-file approach (standalone `ai-policy.yml`).

### Ladybird: n/a (no policy at all)
Two things make this a non-case. First, it is closed-contribution ("We do not accept pull requests from non-maintainers"), so there is no external-contributor policy to express. Second, **it has no AI policy for its maintainers either**: the `CONTRIBUTING` file carries only a "Human language policy" (tone/style for user-facing strings, comments, and commit messages: American English, no contractions, no non-literal language), but nothing about whether maintainers may use AI to write code. So the honest `ai-policy` state here is simply *absent*, a reminder that "no field" is itself the correct signal for "no declared policy," and that `ai-policy` presupposes an open-contribution model to have a per-scope stance that bites.

### OpenJDK: Good
Interim reject: no LLM/diffusion/deep-learning-generated content in code, text, or images across repos, PRs, email, wiki, and issues; **but private use to comprehend, debug, review, and research is explicitly allowed** so long as nothing generated is contributed. Maps: `summary: disallowed`, `defaults.stance: disallowed` (all scopes), `allowedUses: [research, debugging, code-review-assist]` (+ comprehension). A textbook `allowedUses` case, and the "surfaces" (email, wiki, JBS issues) hint that scope could extend beyond the repo.

### Jellyfin: Good
LLM output prohibited for all *direct communication* (issues, feature requests, PR bodies, forum): must be your own words; **LLM-assisted translation exempt if disclosed**. Code: no "pure vibe coding," concise/focused PRs split into discrete commits, must explain in the PR body without LLM text, must test, must handle review feedback yourself. Maps: `stance: generated`, `assertions[{comments, issue-descriptions, pull-request-descriptions}=disallowed; {translations}=generated+disclose]`, `humanReview: required`, `requirements: [tests-pass, new-tests-required]`, `enforcement: [maintainer-review, denylist]` (ban for code theft). Novel bits → prose/`exceptions`: "don't commit LLM metafiles (`.claude`)", mandatory commit-splitting, and rules for *sharing LLM-built tools* in community spaces.

### NLnet Labs: Good
No LLM output in code or documentation, **but a suggested fix in a vulnerability/bug report may be included** (it aids triage), and LLM linting/analysis/review is permitted; disclosure of LLM use required; machine translation discouraged but allowed if disclosed. Maps: `defaults.stance: disallowed` + `assertions[{scope: security-reports, stance: assisted}]` + `allowedUses: [code-review-assist]` + `disclosure: required`. Note this is a per-scope override that makes `security-reports` **more** permissive: the mirror image of most policies, and a good stress-test that `assertions[]` composes in both directions.

### Castle Game Engine: Good
Accept with heavy responsibility: understand everything you submit (code, docs, commits, issue/PR descriptions), be critical of hallucinations, **keep AI conversations private** (don't clutter issues), prefer generating smaller pieces. Maps: `stance: generated`, `humanReview: required`, `assertions[{comments, issue-descriptions}]` (no pasted AI chat). The "smaller pieces" heuristic and the long personal-voice rationale are naturally `statement` prose.

### Godot: Good (captured: the licence gate)
Accept AI-assisted contributions, but AI-generated code is subject to copyright: only MIT-compatible licences (Apache-2.0, BSD, ISC, MPL-2.0, MIT) are acceptable (no GPL/LGPL, no "source-available"/proprietary-engine code); one self-contained change per PR. Maps: `stance: assisted`, `models.policy`/`requirements` for licence compatibility, PR-hygiene → prose. (Only the licence portion was cleanly extracted; the broader stance is queued for a deeper fetch.)

### GDAL: Partial
Rationale captured (the scarce resource is now *maintenance*, not code; plus unresolved US/EU copyright status of LLM output): a strongly **societal/economic** framing that maps to `concerns` and the `models.policy` training-data openness. The operative rules weren't cleanly extracted; queued.

### Flathub: n/a
Its "Generative AI policy" governs **AI-generated applications and media submitted to the store**, not code contributions to Flathub; a different domain (product content, closer to the `media` concern) than `ai-policy`'s contribution scope.

### Python (CPython devguide): Good
Accept; the submitter is responsible regardless of AI use and must explain changes in their own words; **disclosure is "appreciated" but not required**; acceptable uses = comments (esp. non-native language), understanding code, supplementing knowledge; unproductive/repeat submitters may be blocked. `stance: generated`, `humanReview`, `disclosure: encouraged` (the "appreciated but not required" tier), `allowedUses[research]`, `enforcement:[maintainer-review, denylist]`.

### FastAPI: Good
AI encouraged, but contributions need "meaningful human intervention"; if prompt-effort < review-effort, don't submit ("Human Effort Denial-of-Service"); AI-looking PRs/comments closed; spammers blocked. `stance: generated`, `humanReview`, `assertions[comments]`, `enforcement:[maintainer-review, denylist]`. (Echoes attrs' "DoS-by-slop.")

### AFNix: Good
No AI-generated or AI-derived content, **but non-creative uses tolerated** (summarizing docs, assistive tech with full author control, static-analysis/debugging). Clean `stance: disallowed` + `allowedUses[research, accessibility, debugging]` + `enforcement`.

### postmarketOS: Good
Full ban, and members **may not even recommend AI tools**; CoC-based bans. The fullest societal rationale in the corpus (energy, water, exploited labor, non-consensual training data, FOSS-infra DDoS, layoffs) → `concerns`. Banning *recommendation* is a community-conduct rule → prose.

### Matplotlib: Good
Accept with authentic engagement; acceptable = understanding, solution ideas, translating/proof-reading (keep close to original); unacceptable = external bots/agents interacting, un-understood output, multi-project breadth; a **structured "AI Disclosure" field in the PR template**; AI PRs closed on good-first-issues. `stance: generated`, `disclosureFormat: pr-template`, `allowedUses[research, translation, spelling-grammar]`, `autonomousAgents=false`, and the good-first-issue rule → **`newcomerIssuesHumanOnly`**. The no-multi-project-breadth rule → `exceptions`/prose. Validates the `pr-template` disclosure method.

### pip-tools (Jazzband): Good
Any tools OK, but **don't use LLMs to speak for you in project spaces except translation/grammar** (incl. changelogs, PR descriptions); agents that submit PRs without human review not permitted; don't LLM-solve good-first-issues. `stance: generated`, `assertions[comments, issue-descriptions, pull-request-descriptions]=disallowed` + `allowedUses[translation, spelling-grammar]`, `autonomousAgents=false`, and the good-first-issue rule → **`newcomerIssuesHumanOnly`**.

### PROJ: Good (adapted from LLVM)
Human-in-the-loop; label substantial tool-generated content via a **PR-template checkbox + `Assisted-by:` trailer**; bans unapproved agents (`@claude`) and auto-review bots (opt-in human-in-loop OK); "extractive contribution" framing; copyright responsibility. It explicitly says labeling is "to facilitate reviews, **not** to track which parts are generated", direct support for the schema's choice not to model a generated-parts inventory. **A verbatim adaptation of LLVM's policy.**

### KDE (GSoC): Good
Reject: no AI for the proposal, code, MR description, or commit messages; **AI translation discouraged** ("you'll never learn if you don't try"); cites licensing, ethics, and environment. `summary/stance: disallowed`, `concerns`. Like yt-dlp, does **not** exempt translation, reinforcing `allowedUses` is per-project. Program-scoped (GSoC), not necessarily KDE-wide.

### Redox OS: Good
Full ban ("not open to discussion"); clearly-labelled LLM content (issues, MRs, descriptions) is closed; bypass → ban; DCO certification. Even blocks SSH pushes to deter AI scrapers (infra measure → prose). `summary/stance: disallowed`, `humanReview`, `signoff: dco`, `enforcement:[denylist]`.

### curl: Good
Accepts AI-assisted code if it meets standards; **for security reports, AI use MUST be disclosed and independently verified** (fabricated reports → instant ban: the bug-bounty-slop problem); translation welcomed with disclosure only *encouraged*; `Assisted-by:` is among its commit trailers. `stance: generated`, `assertions[security-reports]` (disclosure required), `allowedUses[translation]`, `disclosureFormat: commit-trailer`. Notable: **the disclosure requirement varies by scope** (required for security-reports, encouraged for translation), validating per-scope disclosure in `assertions[]`.

### Oxide (RFD 576): Partial
A values document: LLM use is *encouraged* but always subordinate to human responsibility; per-use guidance (readers/researchers/editors fine, writers discouraged, code-review "not a human substitute," programmers with care). It **bans both LLM *mandates* and LLM *shaming***, the strongest **Contributor opt-out / non-discrimination** evidence in the corpus (bidirectional). Surfaces a new **data-privacy** concern (ensure hosted models don't train on uploaded docs), and is notably *skeptical of blanket disclosure* (it can "distance oneself from responsibility"). Mostly `statement` prose.

### OpenInfra Foundation: Good/Full
One of the best-mapping policies. Predictive/Assistive use → **`Assisted-By:`** label; substantial Generative use → **`Generated-By:`** label: two disclosure tiers keyed by *degree of generation*; recommends **open-source models trained on compatibly-licensed content** (`models.policy`); human-in-loop + `signoff: dco`; enable tool features that flag/block matching public code (`requirements`); an exception for well-documented automated processes (release tooling, i18n → a bot carve-out). The `Generated-By:` label is ASF-derived, more convergence. Its two-tier-by-degree disclosure maps to `disclosureFormat.trailers`.

### W3C Advisory Board: n/a
A **position statement** on LLMs in standards work (opportunities like brainstorming/gap-analysis; risks like subtle incorrectness and "second-hand burdening"; some guardrails): reflective, not an operative contribution policy. `statement`-only.

### Haiku OS: Good (settled via AGENTS.md)
Listed in CHAOSS as a Gerrit review, but it **merged**: `AGENTS.md` now states "AI-generated contributions are forbidden." A terse, absolute ban → `summary/stance: disallowed`. Notable: the policy lives in **`AGENTS.md`**, validating `ai-policy`'s `guardrailsRef` / agent-facing pointer.

## Cross-cutting findings

Across every settled policy analyzed, the schema captures the **tier and major boundaries** at the signal level; none was un-representable. What recurs:

**Vindicated by real policies:**

- **Disclosure trailers converge** on exactly the `disclosureFormat` shape: `Assisted-by:` (Mastodon, LLVM, GCC, Linux Kernel) and `Generated-by:` (ASF). The Linux Kernel's `Assisted-by: AGENT_NAME:MODEL_VERSION [TOOL]` validates the model+version disclosure note specifically.
- **`allowedUses` earns its place**: QEMU, Servo, GCC, Forgejo all carve out research / debugging / comprehension / translation / spelling as explicitly permitted; without it these read as pure bans.
- **`allowedUses` is genuinely per-project, not a fixed exempt-set**: most exempt AI *translation* (Forgejo, Mastodon, GCC), but **yt-dlp bans it**; GCC *permits* AI code-review while **Forgejo and Mastodon forbid it**. Confirms the "a project lists the uses it permits" design and the note that omission ≠ exempt.
- **Size/significance thresholds recur** (Mastodon "significant portion", KeePassXC "vast majority", GCC "legally significant"); all correctly handled by `exceptions: true` + prose rather than a dedicated threshold field: three different projects draw the line three different ways, none mechanically.
- **`enforcement: denylist` is heavily exercised**: public "denounce" lists and bans dominate (Ghostty, Mastodon, yt-dlp, Teamtype, attrs, scikit-learn).
- **`exceptions: true` is the workhorse**; nearly every "Good" (vs "Full") rating rests on it: it absorbs legal tests (ASF), size thresholds, narrow-vs-general-AI splits (Forgejo), and behavioural triggers (scikit-learn) without bloating the schema.
- **Per-scope overrides go both directions**: most policies make a scope *stricter* (`media`, `security-reports`), but GCC (`tests`) and NLnet (`security-reports`) make one *more permissive*. `assertions[]`'s symmetric override handles both, and `security-reports` shows up on both sides, evidence the scope vocabulary is pulling real weight.
- **"Communication must be your own words, translation/grammar exempted" is the single most common per-scope rule** (Forgejo, Jellyfin, Mastodon, pip-tools, Matplotlib, Gitea, curl) → `assertions[comments, issue-descriptions, pull-request-descriptions]=disallowed` + `allowedUses[translation, spelling-grammar]`. This one pattern exercises both the scope overrides and the allowed-uses list at once.
- **PR-template checkboxes are a dominant disclosure method** (Matplotlib, PROJ, QGIS) alongside commit trailers → validates `disclosureFormat.method: pr-template`.
- **Policies converge and get copied verbatim**: PROJ and QGIS adapt LLVM; Astropy adapts scikit-learn; OpenInfra adopts ASF's `Generated-by:`. Direct evidence that a shared, reusable declaration would be adopted, and independent support for the standalone-file approach.

**Candidate additions surfaced (feed the Design Questions):**

- **"AI code review" is a distinct, recurring activity**: permitted by some (GCC, OpenJDK), banned by others (Forgejo, Mastodon) → the **Scope vocabulary** question (a `code-review` scope) and its place in `allowedUses`.
- **Named tool allow/deny lists**: QEMU bans specific products by name; ASF and the Linux Foundation *deliberately refuse* to keep approved lists. The schema has only openness-based `models.policy`, no tool-name list; an open candidate, though the ASF/LF refusal suggests *not* standardizing it may be correct.
- **Output-licence: only the AI-specific part is in scope**: generic licence compatibility (a contribution must match the project's licence) applies to *all* contributions and stays in the general contribution process, out of `ai-policy`. What is AI-specific is the risk that a model reproduces incompatibly-licensed *training data*, or that a tool's terms restrict its output; captured by `models.policy` (require permissive/disclosed training data) and by checks some policies mandate: ASF and OpenInfra ask contributors to enable tool features that flag or block output matching public code (a candidate `requirements` gate). Godot's "AI-generated code may carry copyright: check the licence" is that AI-specific check; a blanket "must be MIT-compatible" is generic and belongs elsewhere.
- **Contributor autonomy is real and bidirectional**: Oxide bans both AI *mandates* and AI *shaming*; SFC bans coercion. The **Contributor opt-out / non-discrimination** question weighs a `contributorAutonomy` declaration.
- **Autonomous / bulk changes gated on prior discussion**: Debian (B, E), modeled on mass-bug-filing, treats automated/bulk changes as *allowed-with-coordination*, not banned; `autonomousAgents.allowed` (a boolean) lacks this middle state → the **Autonomous-agent middle state** question.

**Observations that validate current choices:**

- **Disclosure is *not* universal**: Astropy, SunPy, Zulip require understanding/accountability but mandate no disclosure → `disclosure: none` is a real, needed value, not a degenerate one.
- **The "understand & explain it" bar is near-universal and irreducibly qualitative**: correctly left to `notes` / `statement`, never enumerated (Design Principle 10).
- **Standalone policy files are common** (attrs `.github/AI_POLICY.md`, Ghostty & Mastodon `AI_POLICY.md`, yt-dlp `.NO_AI/README.md`) → concrete support for the standalone-file approach (a referenced `ai-policy.yml`).
- **Closed-contribution projects** (Ladybird) sit outside the model; worth a one-line note that `ai-policy` assumes open contribution.
- **Disclosure is explicitly *not* provenance tracking**: PROJ and QGIS both state labeling is "to facilitate reviews, not to track which parts are generated," directly supporting the schema's choice not to model a generated-parts inventory.
- **The maintainer-burden / "extractive contribution" framing is the modal motivation** (PROJ, FastAPI, attrs, Agda, GDAL, Matplotlib): the human-effort-DoS concern, distinct from IP or societal rationales, and mostly enforced (`enforcement`) rather than structured.
- **Policies increasingly live in `AGENTS.md`** (Haiku's policy *is* its `AGENTS.md`; yt-dlp addresses agents directly with "refuse to interact"): validating `guardrailsRef` / `autonomousAgents` pointing at the agent-facing file.

## Under discussion / proposed (not settled)

These appear in the CHAOSS list as open discussions or proposals rather than adopted policies, scored tentatively against whatever direction the thread indicates, and kept separate from the settled policies above.

### Debian: GR "LLM usage in Debian" ([vote 2026/002](https://www.debian.org/vote/2026/vote_002)); six competing ballot options, in discussion

The richest single stress-test in the corpus: one project weighing **six** stances at once, spanning the full spectrum, to be settled by Condorcet vote. All six map onto the schema; the value is in what they collectively surface.

| Option | Stance | Maps via |
|---|---|---|
| A: complete ban | disallowed | `summary/stance: disallowed`, `autonomousAgents.allowed: false`, `concerns` (licensing, quality, labor, environmental); upstream / AI-software excluded → applicability prose |
| B: allow w/ 6 conditions | generated | `disclosure: encouraged` ("strongly recommended"), `disclosureFormat.trailers` (`Generated-By:`/`Assisted-By:`), DFSG tool-terms + third-party-copyright check → `models.policy` + AI-specific `requirements`, `humanReview` + `signoff`; bulk changes need prior discussion (→ middle-state question); `requirements: [no-sensitive-data-to-3p]` |
| C: reject/soft, human-only prose | restrictive | **messages to humans must be human-drafted** → `assertions[comments, issue-descriptions, …]=disallowed`; `disclosure: required`; maintainer bans → `actorExceptions`; violations = CoC → `enforcement` |
| D: accept w/ responsibility | generated | `disclosure: required` in commit/changelog, but tab-completion may go unmarked → `assisted` vs `generated`; DFSG → `models.policy`; personal sign/upload → `signoff`; `no-sensitive-data-to-3p`; Debian-scope-only → applicability |
| E: neutral ("responsible use") | assisted/generated | mostly `summary` + `statement`; `disclosure: encouraged`; `no-sensitive-data-to-3p`; mass actions need discussion; existing standards apply |
| F: cautious (encourage avoidance) | ~restrictive | "prefer human authorship" (soft discouragement) → `summary` + `statement`; `disclosure: encouraged`; maintainer rejection → `actorExceptions` |

**Two dimensions it brings out:**

1. **"No sensitive data to third-party / untrusted AI services"**; an operative data-handling rule in B, D, E, *and* F (and Oxide): don't leak embargoed / credential / private project data to hosted models, distinct from the stance. Maps to `requirements: [no-sensitive-data-to-3p]`.
2. **Autonomous / bulk changes gated on *prior discussion*** (B and E, modeled on Debian's mass-bug-filing): not banned, but process-gated; `autonomousAgents.allowed` (a boolean) has no such middle state → the open **Autonomous-agent middle state** question.

Validations: the disclosure gradient (voluntary → recommended → required) collapses cleanly onto `none | encouraged | required`; degree-keyed trailers (B); human-only communication → `assertions` (C); DCO-style personal sign-off (D) → `signoff`; the AI-specific licence check (DFSG tool-terms, verify third-party copyright) → the output-licence-in-scope reading. The one nuance the `stance` enum can't express is "prefer human authorship" (C, F), a *preference* short of a rule, which falls to `summary` + `statement`.



- **QGIS**: proposed [QEP-408](https://github.com/qgis/QGIS-Enhancement-Proposals/blob/master/qep-408-ai-tool-policy.md). Human-in-the-loop; review all LLM output before requesting review; label substantial tool-generated content (`Assisted-by:` trailer); "labeling facilitates review, not provenance tracking." **A near-verbatim adaptation of PROJ/LLVM** (same author). Tentative: accept-with-conditions, **Good**: same mapping as PROJ; explicitly leaves "is LLM code acceptable at all" unsettled.
- **Agda**: proposed CONTRIBUTING.md, [PR #8456](https://github.com/agda/agda/pull/8456). Blanket ban on LLM-generated contributions incl. issues and issue-tracker discussion; copyright (US non-copyrightability), societal (EFF), and deskilling rationale. Tentative: reject, **Good** (`summary/stance: disallowed` across code + issues, `enforcement: [denylist]`, `concerns`).
- **Kubernetes: disclosure trailer**, [community #8558](https://github.com/kubernetes/community/issues/8558). Proposes standardizing a **`Co-developed-by:`** trailer to indicate tools used; disclosure-format only. Maps to `disclosureFormat.trailer`; a third trailer convention alongside `Assisted-by:` / `Generated-by:`.
- **Kubernetes: position TBD**, [steering #291](https://github.com/kubernetes/steering/issues/291). Open "what is our position?" question citing LF / Python / Ladybird. No position yet → n/a.
- **SciPy**, [discussion](https://discuss.scientific-python.org/t/a-policy-on-generative-ai-assisted-contributions/1702). Leaning "blocking wholesale is futile; treat AI assistants like any other tool, with copyright/licence boundaries." Tentative: accept-with-conditions; would map to `stance: assisted/generated` + `humanReview`. Not codified.
- **Fedora**: DRAFT, [thread](https://discussion.fedoraproject.org/t/ai-policy-in-fedora-wip/144297). Structured around four areas (contributions, users, Fedora-as-platform, Fedora-data-for-AI); "prefer your own voice over a bland averaged LLM." Tentative: accept-with-conditions, but scope is **broader than contributions** (most of it outside `ai-policy`). Draft.
- **Ansible**, [thread](https://forum.ansible.com/t/ansible-ai-policy/42642). Open "should we have a policy?" citing Servo's ban as a model. No position yet → n/a.

Still only partially captured (operative rules need a deeper fetch): **Godot** (beyond its licence gate) and **GDAL** (rules beyond the rationale).

## Sources

Settled policies analyzed above (URLs for the under-discussion items are inline in that section):

| Policy | Source |
|---|---|
| GCC | https://gcc.gnu.org/ai-policy.html |
| Ghostty | https://github.com/ghostty-org/ghostty/blob/main/AI_POLICY.md |
| Mastodon | https://github.com/mastodon/.github/blob/main/AI_POLICY.md |
| LLVM | https://llvm.org/docs/AIToolPolicy.html |
| QEMU | https://www.qemu.org/docs/master/devel/code-provenance.html#use-of-ai-generated-content |
| Apache (ASF) | https://www.apache.org/legal/generative-tooling.html |
| Servo | https://book.servo.org/contributing/getting-started.html#ai-contributions |
| Linux Foundation | https://www.linuxfoundation.org/legal/generative-ai |
| Gentoo | https://wiki.gentoo.org/wiki/Project:Council/AI_policy |
| yt-dlp | https://github.com/yt-dlp/yt-dlp/blob/master/.NO_AI/README.md |
| Teamtype | https://github.com/teamtype/teamtype/blob/main/CONTRIBUTING.md#generative-aillm-policy |
| Forgejo | https://codeberg.org/forgejo/governance/src/branch/main/AIAgreement.md |
| Gitea | https://github.com/go-gitea/gitea/blob/main/CONTRIBUTING.md#ai-contribution-policy |
| KeePassXC | https://github.com/keepassxreboot/keepassxc/blob/develop/.github/CONTRIBUTING.md#using-ai |
| scikit-learn | https://github.com/scikit-learn/scikit-learn/blob/main/CODE_OF_CONDUCT.md |
| Astropy | https://github.com/astropy/astropy-project/blob/main/policies/ai-policy.md |
| Linux Kernel | https://github.com/torvalds/linux/blob/master/Documentation/process/coding-assistants.rst |
| SunPy | https://github.com/sunpy/sunpy?tab=readme-ov-file#usage-of-generative-ai |
| Zulip | https://github.com/zulip/zulip/blob/main/CONTRIBUTING.md#ai-use-policy-and-guidelines |
| attrs | https://github.com/python-attrs/attrs/blob/main/.github/AI_POLICY.md |
| Ladybird | https://github.com/LadybirdBrowser/ladybird/blob/master/CONTRIBUTING.md |
| OpenJDK | https://openjdk.org/legal/ai |
| Jellyfin | https://jellyfin.org/docs/general/contributing/llm-policies/ |
| NLnet Labs | https://nlnetlabs.nl/llm-policy/ |
| Castle Game Engine | https://castle-engine.io/ai |
| Godot | https://contributing.godotengine.org/en/latest/pull_requests/pull_request_guidelines.html#ai-assisted-contributions |
| GDAL | https://gdal.org/en/stable/community/ai_tool_policy.html |
| Flathub | https://docs.flathub.org/docs/for-app-authors/requirements#generative-ai-policy |
| Python (CPython) | https://devguide.python.org/getting-started/ai-tools/index.html |
| FastAPI | https://tiangolo.com/open-source/contributing/ |
| AFNix | https://docs.afnix.fr/policies/ai.html |
| postmarketOS | https://docs.postmarketos.org/policies-and-processes/development/ai-policy.html |
| Matplotlib | https://matplotlib.org/devdocs/devel/contribute.html#restrictions-on-generative-ai-usage |
| pip-tools | https://pip-tools.rtfd.io/en/latest/contributing/#project-contribution-guidelines |
| PROJ | https://github.com/OSGeo/PROJ/blob/master/docs/source/community/ai_tool_policy.rst |
| KDE (GSoC) | https://community.kde.org/GSoC#Regarding_AI_usage |
| Redox OS | https://gitlab.redox-os.org/redox-os/redox/-/blob/master/CONTRIBUTING.md?ref_type=heads |
| curl | https://github.com/curl/curl/blob/master/docs/CONTRIBUTE.md |
| Oxide | https://rfd.shared.oxide.computer/rfd/0576 |
| OpenInfra Foundation | https://openinfra.org/legal/ai-policy |
| W3C Advisory Board | https://www.w3.org/blog/2026/advisory-board-publishes-position-statement-on-ai-in-standards-work/ |
| Haiku OS | https://review.haiku-os.org/c/haiku/+/11180 |
