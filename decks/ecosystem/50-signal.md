## A signal, not a rule engine

- **[Structure only what recurs](https://codeberg.org/open-source-ecosystem/ai-policy/src/branch/main/README.md#how-it-s-designed-a-signal-not-a-rule-engine)**; point at prose
- **Declare, don't adjudicate**: intent, not detection
- **Stance is permission**, not preference
- **Agent autonomy** is a separate axis

**The file says that boundaries exist and their shape.<br />The detail stays in the human policy it points at.**

[↳ README: how it's designed](https://codeberg.org/open-source-ecosystem/ai-policy/src/branch/main/README.md#how-it-s-designed-a-signal-not-a-rule-engine)

Note:

↓ How the next field gets chosen

- `statement` points at the authoritative prose; `exceptions: true` says "this is a summary": the carve-outs are in the prose
- Declare, don't adjudicate: whether code was written by an LLM is undetectable in general; verification (tests, review, the human sign-off) stays outside the file. Declared identity of agents is the tractable lever, not detection
- Stance: may this kind of contribution be offered at all. Autonomy: may a non-human do the offering. The Linux Kernel shows why they are split: it accepts generated code while barring agents from signing off
- Development-time, not runtime: `models` describes the AI used to *build* the project, not AI the product ships

**Q&A details:**

- Resolution is per `scope`, a contribution's content type (code, docs, translations and so on); whole-file rules compose with the stance rather than overriding it, so a change can be permitted and gated at once
- Named, not numbered: enumerated items carry titles so references stay stable

--

## How the next field gets chosen

<!-- .slide: data-timing="0" -->

- Nuance goes in a **`notes`** sentence, not an enum
- Collected across adopters, notes show what recurs
- Recurrence in similar words earns structure
- Or a consumer must act on it **before submitting**

**Structure the corpus asked for,<br />not structure guessed from one policy.**

[↳ README: how it's designed](https://codeberg.org/open-source-ecosystem/ai-policy/src/branch/main/README.md#how-it-s-designed-a-signal-not-a-rule-engine)

Note:

↓ The threshold test

- An enum is a fixed list of allowed values that a consumer can branch on
- The second route is narrow: a value earns an enum on first sight when a consumer holding only the file and the contribution must branch on it before submitting
- Example: `disclosure: prohibited` entered that way. An agent that adds a disclosure trailer by habit breaks such a policy with every commit
- This repository's own policy states two concerns no surveyed project cites, retired and exclusionary language and communities losing the shaping of their own language, in `concerns.notes` only, waiting for others to name them too

--

## The threshold test

<!-- .slide: data-timing="0" -->

- **Godot**: code under fifteen lines presumed trivial
- **Rust**: halt LLM-created merges above half
- Godot's is checkable by whoever holds the diff
- Rust's needs project-wide merge history

**A threshold earns a field only if a consumer<br />can evaluate it before submitting.**

[↳ README: open questions (numeric thresholds)](https://codeberg.org/open-source-ecosystem/ai-policy/src/branch/main/README.md#open-questions-named)

Note:

- Decided for now: significance thresholds stay in prose; no field
- Rust's circuit-breaker counts merged pull requests over six weeks, and answers whether the door is currently open rather than whether a change complies
- On that test the evidence is a single project, against seven policies drawing the line qualitatively
- Reopen if: further projects publish per-contribution thresholds a submitter could check, and they converge on a comparable unit. Divergent units would confirm the prose choice
