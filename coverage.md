# `ai-policy`: coverage against real policies

How well does the [`ai-policy` format](./README.md) capture real open-source AI-contribution policies? This tests it against the policies curated by the [CHAOSS AI-alignment working group](https://github.com/chaoss/wg-ai-alignment/tree/main/moderation) (the primary source list), plus a few beyond it. It is the **evidence base for the proposal**: if the format can express the real spread of policies, its shape is validated. A second question — whether those policies cover the ground they should — is scored separately in [Specificity](#specificity-against-the-chaoss-domain-taxonomy) against the working group's own domain taxonomy.

## Add a policy (PRs welcome)

This survey is open: **contribute a policy by pull request.** Point at a real, public AI-contribution policy (settled, or a live discussion), and score it against the format:

1. Add a **row** to the Summary table and a short **per-policy note**, in the shape of the existing entries.
2. Give it a **tier** (reject / restrict / accept-with-conditions / neutral) and a **fit rating** (Full / Good / Partial / Signal-only, defined below).
3. In *Maps via*, list the fields it exercises; in the gap column, note what needs prose or `exceptions`, or what the format can't express.
4. Add its URL to the **Sources** table.

The most valuable contribution is a policy the format **can't** capture: that points at a missing dimension or an open question; record it in the cross-cutting findings so it can feed the design.

**Where to find candidates.** Two curated lists are far broader than what is scored here and are the pool to draw from. The [CHAOSS AI-alignment moderation list](https://github.com/chaoss/wg-ai-alignment/tree/main/moderation) is this survey's primary source and tracks live discussions alongside adopted policies. [`melissawm/open-source-ai-contribution-policies`](https://github.com/melissawm/open-source-ai-contribution-policies) is larger by an order of magnitude — several hundred projects — and classifies each along four axes (AI allowed, disclosure required, copyright statement present, human-in-the-loop required) that are a useful independent check on this format's field set: a policy that list can classify but this format cannot express is precisely the contribution worth making.

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
| Debian | neutral ("responsible use") | Good | summary=mixed, `disclosure: encouraged`, `humanReview`, `signoff: dco`, `requirements: [no-sensitive-data-to-3p]`; existing licence process applies unchanged | bulk/automated changes gated on *prior discussion* → the **Autonomous-agent middle state** question, still no field |
| Rust (`rust-lang/rust`) | accept-with-conditions (time-boxed experiment) | Partial | stance=generated, `humanReview`, `disclosure: required`, `assertions[docs, comments, issue-descriptions, pull-request-descriptions]=disallowed`, `allowedUses[research, debugging, code-review-assist, translation, spelling-grammar]`, `autonomousAgents.allowed=false`, `requirements[new-tests-required, no-generated-in-security-paths]`, `enforcement: [maintainer-review]` | **reviewer must agree *before* the PR is opened** — no field; **forge label** (`llm-assisted`) as the disclosure method — not a `disclosureFormat` value; **volume circuit-breaker** — not expressible; per-team applicability → prose |
| Codeberg | reject (platform hosting) | Partial | summary=disallowed, `concerns[ip-provenance, security, environmental, oss-sustainability]`, `enforcement: [maintainer-review]` | **platform-level, not contribution-level**: governs what may be *hosted* and binds the forge itself not to train on hosted code. Neither is a contributor rule `ai-policy` models — see [Specificity](#specificity-against-the-chaoss-domain-taxonomy) |

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

### Debian: Good (GR carried; the corpus's widest single deliberation)

The richest stress-test in the corpus: one project weighing the full spectrum at once on a Condorcet ballot, settled 30 Aug 2026. Every drafted option maps onto the schema; the value is in what they collectively surface, and the losing options are as informative as the winner because each is a real, drafted policy text the format has to be able to carry.

**[Choice 5, "Responsible Use of Generative AI", carried](https://www.debian.org/vote/2026/vote_002)** — it was alone in the Schwartz set. Debian neither endorses nor prohibits generative AI: the same quality and licensing standards apply regardless of tooling, contributors are fully responsible for and must understand what they submit, disclosure is encouraged but not required, confidential or sensitive project data must not go to third-party services, and large-scale automated changes need prior discussion. Maps to `summary: mixed`, `disclosure: encouraged`, `humanReview`, `signoff: dco`, `requirements: [no-sensitive-data-to-3p]`, with licence compliance staying in the general contribution process.

| Ballot choice | Stance | Maps via |
|---|---|---|
| 1: No LLM contributions, via the Social Contract | disallowed | `summary/stance: disallowed`, `autonomousAgents.allowed: false`, `concerns` (licensing, quality, labor, environmental); upstream / AI-software excluded → applicability prose |
| 2: Allow AI-assisted contributions with conditions | generated | `disclosure: encouraged` ("strongly recommended"), `disclosureFormat.trailers` (`Generated-By:`/`Assisted-By:`), DFSG tool-terms + third-party-copyright check → `models.policy` + AI-specific `requirements`, `humanReview` + `signoff`; bulk changes need prior discussion (→ middle-state question); `requirements: [no-sensitive-data-to-3p]` |
| 3: Reject LLMs as far as practical, update the CoC | restrictive | **messages to humans must be human-drafted** → `assertions[comments, issue-descriptions, …]=disallowed`; `disclosure: required`; maintainer bans → `actorExceptions`; violations = CoC → `enforcement` |
| 4: Accept AI contributions for Debian-specific work | generated | `disclosure: required` in commit/changelog, but tab-completion may go unmarked → `assisted` vs `generated`; DFSG → `models.policy`; personal sign/upload → `signoff`; `no-sensitive-data-to-3p`; Debian-scope-only → applicability |
| **5: Responsible use of generative AI — carried** | assisted/generated | `summary: mixed` + `statement`; `disclosure: encouraged`; `no-sensitive-data-to-3p`; mass actions need discussion; existing standards apply |
| 6: A cautious approach to generative AI | ~restrictive | "prefer human authorship" (soft discouragement) → `summary` + `statement`; `disclosure: encouraged`; maintainer rejection → `actorExceptions` |
| 7: Debian is created by humans | assisted | output may not be contributed *directly*, but assistive use (explore, research, analyze, critique) is fine → `stance: assisted` + `allowedUses`; broad surface (packaging, BTS, Salsa, lists, infrastructure, web, docs, official communications), upstream excluded → applicability prose; rationale is reviewer-burden transfer, the "extractive contribution" concern |
| 8: Avoid LLMs — climate destruction is a deal breaker | *no operative rule* | Explicitly non-binding: a stated position that contributors should avoid LLMs where practical, conceding detection and enforcement are impractical. `concerns: [environmental]` carries it and nothing else does — the purest instance in the corpus of a concern that shapes a decision without becoming a rule |

**Three dimensions it brings out:**

1. **"No sensitive data to third-party / untrusted AI services"**; an operative data-handling rule in Choices 2, 4, 5 and 6 (and Oxide): don't leak embargoed / credential / private project data to hosted models, distinct from the stance. Maps to `requirements: [no-sensitive-data-to-3p]`, and it is now *adopted* rather than proposed.
2. **Autonomous / bulk changes gated on *prior discussion*** (Choices 2 and 5, modeled on Debian's mass-bug-filing): not banned, but process-gated. `autonomousAgents.allowed` is a boolean with no such middle state → the open **Autonomous-agent middle state** question, which the carried option now makes a requirement rather than a hypothetical.
3. **Environmental concern reached the ballot as its own option and lost.** Choice 8 put climate impact forward as the deciding consideration and was itself drafted as a non-binding preference; the neutral option carried. That is the rationale-versus-rule gap at its sharpest, in the largest deliberation available — see [Specificity](#specificity-against-the-chaoss-domain-taxonomy).

Validations: the disclosure gradient (voluntary → recommended → required) collapses cleanly onto `none | encouraged | required`; degree-keyed trailers (Choice 2); human-only communication → `assertions` (Choice 3); DCO-style personal sign-off (Choice 4) → `signoff`; the AI-specific licence check (DFSG tool-terms, verify third-party copyright) → the output-licence-in-scope reading. The nuance the `stance` enum cannot express is "prefer human authorship" (Choices 3, 6, 8), a *preference* short of a rule, which falls to `summary` + `statement`.

### Rust: Partial (three dimensions the format cannot reach)

Adopted 6 Aug 2026 for [`rust-lang/rust`](https://forge.rust-lang.org/policies/llm-usage.html), and deliberately narrow: it binds only the teams that ratified it (compiler, libs, types, rustdoc, bootstrap and their subteams), not other repositories, submodules, or the wider project. The organising line is "fine to use LLMs to answer questions, analyze, distill, refine, check, suggest, review — but not to **create**", which is `stance: assisted` as a default with a carved-out, disclosed exception for generated code. Private use is unrestricted; generating a solution privately and then writing it from scratch is explicitly fine. LLM-created code is admitted as a *time-boxed experiment*: non-critical, high-quality, well-tested, well-reviewed changes, with disclosure. Public documentation, doc-comments, safety comments, compiler diagnostics and user-facing text are prohibited outright, as are LLM-written issue bodies and PR descriptions from a personal account; machine translation, trivial changes and bug discovery are conditionally allowed with disclosure. LLM review bots must run under separate, blockable accounts and their comments are advisory only — never sufficient to merge.

Most of that maps cleanly. Three things do not, and they are the most valuable findings in the corpus since Debian:

- **Reviewer pre-agreement.** A reviewer must agree to review the change *before the pull request is opened*; new contributors must discuss it with their assigned reviewer first. This is a consent gate on the *human* contribution path, adjacent to but distinct from the autonomous-agent middle state (which gates *agent* actions on prior discussion). One generalised `prior-arrangement` state would serve both.
- **A forge label as the disclosure method.** Merged LLM-created PRs carry an `llm-assisted` label. `disclosureFormat.method` knows commit trailers and PR templates; a label is a third, forge-native mechanism, and unlike the other two it is applied by the *reviewer at merge* rather than by the contributor at submission — so it doubles as the project's own measurement instrument.
- **A volume circuit-breaker.** If LLM-created changes exceed half of merged PRs over a six-week window, further LLM-created merges halt until the rate falls back. This is a *proportionality threshold relative to project throughput* — an operative rule keyed to volume rather than to content, which the format has no way to express and which the survey has not seen before.

Also notable: enforcement is explicitly **not** detection. Contributors are asked to be honest, deliberate misrepresentation is a Code of Conduct matter, and members are told *not* to investigate whether others used an LLM — the clearest statement in the corpus of the design assumption behind `attestation` (declared identity is the tractable lever, detection is not).

### Codeberg: Partial (a platform policy, not a contribution policy)

The one **forge** in the corpus, and it sits at a different layer from everything else here. Two motions carried by member vote on 22 Jul 2026. The first binds the platform: "The Codeberg forge and its associated services are not and will not use the code or data of projects and users to train 'Artificial Intelligence' tools such as Large Language Models." The second added [Terms of Use §2(1)7](https://codeberg.org/Codeberg/org/src/branch/main/TermsOfUse.md): "You must not share projects that mostly consist of code written by 'generative AI'-tools (including services such as *Claude*, *OpenAI Codex*)", reaching projects created by autonomous agents, projects maintained with heavy LLM use, and projects consuming resources disproportionate to their human users. Established communities with significant pre-LLM history, small low-resource experiments, and individual AI-assisted contributions inside a human-maintained codebase are all exempt. Enforcement is case-by-case moderation with no automated content analysis and no mass deletion.

`ai-policy` reaches the stance and the concerns, and nothing more — because **the operative rules are not addressed to contributors.** One governs what the platform may be used to *host*; the other is a commitment the platform makes about *itself*. `ai-policy` models a project's rules for people contributing to it, so a hosting restriction lands the way Flathub's app-content policy did (recorded, not scored), and a self-binding data commitment has nowhere to go at all.

That layer mismatch is the finding, not a defect in either document, and it generalises well beyond Codeberg — see [Specificity](#specificity-against-the-chaoss-domain-taxonomy). Codeberg's stated rationale is also the most concrete infrastructure argument on record: SSD prices rising from €700 to €3,700 amid hardware scarcity, with LLM-generated "ghost projects" consuming storage and database capacity out of all proportion to their human users, against donation funding.

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
- **Prior arrangement is a recurring gate, and it is not only about agents**: Debian's carried option treats bulk/automated changes as *allowed-with-coordination* rather than banned (modeled on mass-bug-filing), and Rust requires a reviewer to agree *before* an LLM-created pull request is opened. `autonomousAgents.allowed` is a boolean with no middle state, and nothing at all covers the human path → the **Autonomous-agent middle state** question, which both policies now make a live requirement rather than a hypothetical, and which should probably generalise to a `prior-arrangement` state covering both.
- **A forge label as a disclosure method**: Rust marks merged LLM-created pull requests with an `llm-assisted` label. `disclosureFormat.method` knows commit trailers and PR templates, both applied by the contributor at submission; a label is applied by the *reviewer at merge*, which makes it the project's own measurement instrument as much as a disclosure. A third method value, and the first one that is forge-native.
- **Volume thresholds as an operative rule**: Rust halts further LLM-created merges if they exceed half of merged pull requests over a six-week window. Every other threshold in the corpus is a significance judgement correctly left to prose; this one is countable and mechanical, and is the first evidence that the **scope/volume limits stay in prose** choice may need revisiting.
- **Advisory-only review, and bot identity**: Rust permits LLM review bots only under separate, user-blockable accounts with non-blocking comments, and forbids treating LLM review as sufficient to merge. `allowedUses: code-review-assist` is a permission and expresses none of this → the **Scope vocabulary** question needs a `review` domain with more than a yes/no.

**Observations that validate current choices:**

- **Disclosure is *not* universal**: Astropy, SunPy, Zulip require understanding/accountability but mandate no disclosure → `disclosure: none` is a real, needed value, not a degenerate one.
- **The "understand & explain it" bar is near-universal and irreducibly qualitative**: correctly left to `notes` / `statement`, never enumerated (Design Principle 10).
- **Standalone policy files are common** (attrs `.github/AI_POLICY.md`, Ghostty & Mastodon `AI_POLICY.md`, yt-dlp `.NO_AI/README.md`) → concrete support for the standalone-file approach (a referenced `ai-policy.yml`).
- **Closed-contribution projects** (Ladybird) sit outside the model; worth a one-line note that `ai-policy` assumes open contribution.
- **Disclosure is explicitly *not* provenance tracking**: PROJ and QGIS both state labeling is "to facilitate reviews, not to track which parts are generated," directly supporting the schema's choice not to model a generated-parts inventory.
- **The maintainer-burden / "extractive contribution" framing is the modal motivation** (PROJ, FastAPI, attrs, Agda, GDAL, Matplotlib): the human-effort-DoS concern, distinct from IP or societal rationales, and mostly enforced (`enforcement`) rather than structured.
- **Policies increasingly live in `AGENTS.md`** (Haiku's policy *is* its `AGENTS.md`; yt-dlp addresses agents directly with "refuse to interact"): validating `guardrailsRef` / `autonomousAgents` pointing at the agent-facing file.

## Specificity against the CHAOSS domain taxonomy

The survey above asks whether the **format** can express the policies that exist. A sibling question — whether the **policies** cover the ground they should — is being asked independently by the CHAOSS AI-alignment working group, whose [consent policy specificity](https://github.com/chaoss/wg-ai-alignment/blob/main/metrics/ai-alignment-community-governed-use/ai-use-consent-policy-specificity.md) metric scores how specifically a policy addresses each of nine domains where AI shows up, and by Emma Irwin's [first application of it](https://github.com/emmairwin/ai-oss-use-specificity/blob/main/reports/README.md) across 39 projects drawn from the same moderation list this survey uses. The metric is a candidate within the [Governed AI Use](https://github.com/chaoss/wg-ai-alignment/blob/main/metrics/ai-alignment-community-governed-use/metric-model-ai-alignment-community-governed-use.md) model, due to be finalised in September 2026, and its author expects the taxonomy to expand toward the openness of the models and data in use.

The two instruments are orthogonal and compose: hers scores policy specificity per domain (`X` addressed, `~` partial, `R` raised in rationale without governance, blank absent); this one scores format expressiveness per policy. Reading them together is what makes the findings below available, and neither produces them alone.

### What the format reaches

| CHAOSS domain | `ai-policy` reach |
|---|---|
| Code contributions (PRs, issues, comments) | `defaults` / `assertions` over `scope: code, tests, commit-messages, comments, issue-descriptions, pull-request-descriptions` — the format's core, and the one domain most policies govern |
| Content (documentation, blogs, design assets) | `scope: docs, media, translations` |
| Autonomous / agentic use | `autonomousAgents` plus `attestation` — reached, but the boolean still lacks the prior-arrangement middle state that Debian and Rust both now require |
| Review (who or what may review using AI) | Only `allowedUses: code-review-assist`, a permission. Cannot express *who* may review, nor that AI review is advisory-only and never sufficient to merge (Rust), nor that review bots must run under separate blockable accounts |
| Moderation actions | No `scope` value. The near-miss is universal: policies reach moderation by referring violations to a code of conduct, which governs the *response* to bad contributions rather than AI's use in moderating |
| Notetaker / meeting bots | No `scope` value, and no policy in either survey governs it |
| Environmental impact | `concerns: environmental` — motivation, deliberately not a rule surface |
| Infrastructure strain | Nothing, in `concerns` or elsewhere |
| Data use for training (platform user data) | `models.policy.trainingData` covers the training data of models a project *consumes*; nothing covers a platform binding itself over data it *holds* |

### The `concerns` field is the format's answer to the rationale-versus-rule gap

The headline finding of the specificity work is a gap between what motivates a policy and what it governs: environmental impact shaped the reasoning of several projects and became a rule in none, and infrastructure strain did the same. Establishing that took a second manual pass over preambles and blog posts after the policy texts themselves had been scored, and it earned a distinct code (`R`) in the results.

That distinction is already structural here. [`concerns`](./ai-policy.schema.yaml) is defined as a *motivation signal* — `environmental`, `labor-ethics`, `data-consent`, `oss-sustainability`, `skill-preservation` — carried separately from `defaults`, `assertions` and `requirements`, which carry rules. A project that publishes `ai-policy.yml` states in one machine-readable place both what it governs and what moved it, and the gap between them is then a query rather than a research project. Two entries in this survey make the point on their own: Debian put climate impact on the ballot as its own option, drafted from the outset as a non-binding preference, and the neutral option carried; Servo and postmarketOS both rest bans on societal rationale that only `concerns` carries.

This is the strongest external validation the format has received for a design choice made on other grounds, and it is the most useful thing this survey can offer the working group in return: the metric's stated implementation is manual audit plus text analysis of prose, and the `R`/rule distinction it has to reconstruct by hand is a field.

### Three domains are forge-level, not project-level

Notetaker bots, infrastructure strain and data use for training score zero across 39 projects, and environmental impact scores zero as a rule. The natural reading is that projects have not got to them yet. The Codeberg entry above suggests a different one: for three of them a project policy is the wrong instrument, because the thing to be governed is not the project's to govern.

Codeberg is the one forge in the corpus, and it is where those domains suddenly have rules. It bound itself never to train on hosted code or user data, and it restricted what may be hosted on explicitly infrastructure-and-environment grounds. In the specificity scoring all of that lands as `R` — raised in rationale, not governed — which is correct against an instrument that scores rules addressed to contributors, and which is exactly why the finding is interesting: the strongest instance of data-use-for-training governance in the corpus reads as rationale because it is a rule the platform binds *itself* to, and the taxonomy has no slot for that. Meeting bots belong to whoever runs the meeting infrastructure; server load belongs to whoever pays for the servers; training on hosted code belongs to whoever holds it.

Fedora's draft is independent support: it structures itself around contributions, users, *Fedora-as-platform*, and *Fedora-data-for-AI* — a project that hosts infrastructure recognising the layer split unprompted, and separating the two platform-facing areas from the contribution-facing ones.

So the finding to feed back is not that projects are silent on these domains but that the **domains have the wrong subject**: they need a declaring party axis (project / forge / foundation) before an absence can be read as a gap. This is also where a declaration format has something to offer that a survey cannot — a forge-level record, discoverable at `.well-known`, is a natural carrier for commitments of exactly this shape, and none exists today.

### Divergences kept on purpose

The metric scores four consent attributes per domain. Two map, two are deliberately unstructured here:

- **Supervision level** (banned → fully unsupervised) is one axis where the format keeps two: `stance` for what may be contributed, `autonomousAgents` for what may act unattended. The corpus supports the split — the Linux Kernel accepts generated code while barring agents from signing off — and collapsing them would lose that.
- **Accountability holder** maps partially: `humanReview` and `signoff` establish *that* a human is answerable, never *which* role. No policy surveyed names a role rather than "the contributor", so the gap is untested rather than known-harmful.
- **Scope and volume limits** stay in prose by design: three projects drew significance thresholds three different ways and none mechanically, so `exceptions: true` plus `statement` carries them. Rust's volume circuit-breaker is the first counter-example — an operative, countable threshold — and if a second appears the choice deserves revisiting.
- **Proportionality relative to community size** likewise stays in prose, and is the attribute the format is least likely to adopt: it is a judgement a maintainer makes, not a value a file declares.

### Corpus overlap

The two surveys overlap heavily and neither contains the other. Beyond what is scored here, the specificity corpus adds **Polars**, and scores **QGIS** (still under discussion below) and a second GDAL surface. **Codeberg** and **Rust** came from it and are now scored above — both earned their place, Codeberg for the layer mismatch and Rust for three dimensions nothing else in the corpus surfaced. Going the other way, this survey covers curl, FastAPI, OpenJDK, CPython, Redox OS, Haiku OS, Flathub, Ladybird and the W3C Advisory Board, which the specificity corpus does not.

## Under discussion / proposed (not settled)

These appear in the CHAOSS list as open discussions or proposals rather than adopted policies, scored tentatively against whatever direction the thread indicates, and kept separate from the settled policies above.

- **QGIS**: proposed [QEP-408](https://github.com/qgis/QGIS-Enhancement-Proposals/blob/master/qep-408-ai-tool-policy.md). Human-in-the-loop; review all LLM output before requesting review; label substantial tool-generated content (`Assisted-by:` trailer); "labeling facilitates review, not provenance tracking." **A near-verbatim adaptation of PROJ/LLVM** (same author). Tentative: accept-with-conditions, **Good**: same mapping as PROJ; explicitly leaves "is LLM code acceptable at all" unsettled.
- **Agda**: proposed CONTRIBUTING.md, [PR #8456](https://github.com/agda/agda/pull/8456). Blanket ban on LLM-generated contributions incl. issues and issue-tracker discussion; copyright (US non-copyrightability), societal (EFF), and deskilling rationale. Tentative: reject, **Good** (`summary/stance: disallowed` across code + issues, `enforcement: [denylist]`, `concerns`).
- **Kubernetes: disclosure trailer**, [community #8558](https://github.com/kubernetes/community/issues/8558). Proposes standardizing a **`Co-developed-by:`** trailer to indicate tools used; disclosure-format only. Maps to `disclosureFormat.trailer`; a third trailer convention alongside `Assisted-by:` / `Generated-by:`.
- **Kubernetes: position TBD**, [steering #291](https://github.com/kubernetes/steering/issues/291). Open "what is our position?" question citing LF / Python / Ladybird. No position yet → n/a.
- **SciPy**, [discussion](https://discuss.scientific-python.org/t/a-policy-on-generative-ai-assisted-contributions/1702). Leaning "blocking wholesale is futile; treat AI assistants like any other tool, with copyright/licence boundaries." Tentative: accept-with-conditions; would map to `stance: assisted/generated` + `humanReview`. Not codified.
- **Fedora**: DRAFT, [thread](https://discussion.fedoraproject.org/t/ai-policy-in-fedora-wip/144297). Structured around four areas (contributions, users, Fedora-as-platform, Fedora-data-for-AI); "prefer your own voice over a bland averaged LLM." Tentative: accept-with-conditions, but scope is **broader than contributions** (most of it outside `ai-policy`). Draft.
- **Ansible**, [thread](https://forum.ansible.com/t/ansible-ai-policy/42642). Open "should we have a policy?" citing Servo's ban as a model. No position yet → n/a.

Still only partially captured (operative rules need a deeper fetch): **Godot** (beyond its licence gate), **GDAL** (rules beyond the rationale), and **Polars** (not yet scored; carried over from the specificity corpus).

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
| Debian | https://www.debian.org/vote/2026/vote_002 |
| Rust | https://forge.rust-lang.org/policies/llm-usage.html |
| Codeberg | https://codeberg.org/Codeberg/org/src/branch/main/TermsOfUse.md |
