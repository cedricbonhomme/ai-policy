## What the corpus research found

- A [curated survey](https://codeberg.org/open-source-ecosystem/ai-policy/src/branch/main/coverage.md#cross-cutting-findings), read field by field
- Every settled one maps at the signal level
- A [larger corpus](https://codeberg.org/open-source-ecosystem/ai-policy/src/branch/main/coverage.md#a-larger-corpus-popular-projects): 281 policies, mapped by script
- 280 schema-valid records; 247 expressed completely

**The evidence for the shape<br />is that real policies fit it.**

[↳ Coverage: cross-cutting findings](https://codeberg.org/open-source-ecosystem/ai-policy/src/branch/main/coverage.md#cross-cutting-findings)

Note:

↓ What the counts settled

- The curated survey draws on the CHAOSS AI-alignment working group's moderation list, plus a few policies beyond it, last audited against live sources on 16 September 2026
- Coverage's claim: across every settled policy, the schema captures the **tier and major boundaries** at the signal level, with some nuance left to prose
- Tier is the coarse stance: reject, restrict, accept, accept-with-conditions or neutral
- Signal level is not full fit: Rust, Oxide, Codeberg and the Linux Foundation umbrella still rate only Partial, with material rules in prose
- Two policies carry an operative rule the format does not reach: Rust's volume circuit-breaker, and Fedora's bar on AI scoring governance decisions, which is out of scope by design
- The larger corpus is Hora, Robbes and Zacchiroli (2026): 281 policies, from the 2,000 most-starred active GitHub repositories plus 36 well-known projects added by hand. The one exception, github/awesome-copilot, carries no labels at all, so there is nothing to declare

**Acronyms:** CHAOSS = the open-source community-health metrics project whose AI-alignment working group keeps the moderation list

**Q&A details:**

- Paper: "We Permit the Use of AI, but […]", arXiv 2609.07542; the labelled corpus is published under CC BY 4.0
- The mapping script is `research/hora-2026/map.py`: it turns each labelled policy into the partial file its labels support and validates it
- Outside the format: *medium* human involvement meaning prompting only (6), labels the paper coded as unclear (6), a code-block disclosure (1), and some countermeasures

--

## What the counts settled

<!-- .slide: data-timing="0" -->

| What a disclosure describes | Policies |
| --- | --- |
| How AI was used | 56 |
| The tool | 40 |
| The extent | 16 |
| The model | 9 |

**Involvement and accountability are separate:<br />119 policies require both, 70 only involvement.**

[↳ Coverage: a larger corpus](https://codeberg.org/open-source-ecosystem/ai-policy/src/branch/main/coverage.md#a-larger-corpus-popular-projects)

Note:

↓ Rationale is not rule

- Counts are of the policies that say what a disclosure must contain; they became `disclosureFormat.content`
- The curated survey had shown trailers converging on *where* a disclosure goes (`Assisted-by:`, `Generated-by:`) but not on *what* it must name
- The 70 require the contributor to review, understand and test without saying they answer for the result, so `humanReview` means involvement only and `accountability: contributor` says the rest
- No policy in the corpus disclaims accountability, which is why the field has no negative value

--

## Rationale is not rule

<!-- .slide: data-timing="0" -->

- Environmental impact shaped several projects' reasoning
- It became a rule in none
- Finding that took a [manual second pass](https://codeberg.org/open-source-ecosystem/ai-policy/src/branch/main/coverage.md#specificity-against-the-chaoss-domain-taxonomy)
- Here, **`concerns`** carries motivation apart from rules

**The gap between what moved a project<br />and what it governs becomes a query.**

[↳ Coverage: specificity (CHAOSS taxonomy)](https://codeberg.org/open-source-ecosystem/ai-policy/src/branch/main/coverage.md#specificity-against-the-chaoss-domain-taxonomy)

Note:

- The CHAOSS specificity metric scores how specifically a policy addresses each of nine domains; Emma Irwin's first application covers 39 projects, and had to code "raised in rationale without governance" by hand
- `concerns` takes values from a shared list (`code-quality`, `security`, `ip-provenance`, `environmental`, `oss-sustainability` and others) plus `notes` in the project's own words
- Coverage calls this the strongest external validation the format has received for a design choice made on other grounds
- Servo and postmarketOS both rest bans on societal rationale that only `concerns` carries
